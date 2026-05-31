# /// script
# dependencies = ["requests", "markdown"]
# ///

import argparse
import os
import markdown as md_lib
import requests
from requests.auth import HTTPBasicAuth

DOMAIN = "https://seguataneo.atlassian.net/wiki"
EMAIL = os.environ.get("CONFLUENCE_EMAIL")
TOKEN = os.environ.get("CONFLUENCE_TOKEN")

if not EMAIL or not TOKEN:
    raise EnvironmentError("환경 변수 CONFLUENCE_EMAIL 또는 CONFLUENCE_TOKEN이 설정되지 않았습니다.")

auth = HTTPBasicAuth(EMAIL, TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def get_space_key(space_name: str) -> str:
    url = f"{DOMAIN}/rest/api/space"
    response = requests.get(url, headers=headers, auth=auth, params={"limit": 50})
    response.raise_for_status()
    for space in response.json().get("results", []):
        if space["name"] == space_name:
            return space["key"]
    raise ValueError(f"스페이스를 찾을 수 없습니다: '{space_name}'")


def read_markdown_file(filepath: str) -> tuple[str, str]:
    """마크다운 파일에서 첫 번째 # 제목과 본문을 분리합니다."""
    with open(filepath, encoding="utf-8") as f:
        lines = f.read().splitlines()

    title = ""
    body_lines = []
    for line in lines:
        if not title and line.startswith("# "):
            title = line[2:].strip()
        else:
            body_lines.append(line)

    return title, "\n".join(body_lines).strip()


def normalize_youtube_url(url: str) -> str:
    """youtu.be 단축 URL을 youtube.com/watch?v= 형식으로 변환합니다."""
    import re
    # youtu.be/VIDEO_ID 패턴
    short = re.match(r'https?://youtu\.be/([A-Za-z0-9_-]+)', url)
    if short:
        return f"https://www.youtube.com/watch?v={short.group(1)}"
    # 이미 youtube.com 형식이면 그대로
    return url


def youtube_embed_macro(url: str) -> str:
    """YouTube 임베드를 위한 Confluence Widget Connector 매크로를 생성합니다."""
    watch_url = normalize_youtube_url(url)
    return (
        '<ac:structured-macro ac:name="widget" ac:schema-version="1">'
        f'<ac:parameter ac:name="url"><ri:url ri:value="{watch_url}"/></ac:parameter>'
        '<ac:parameter ac:name="width">640</ac:parameter>'
        '<ac:parameter ac:name="height">360</ac:parameter>'
        '</ac:structured-macro>'
        '<p></p>'
    )


def markdown_to_confluence_html(text: str) -> str:
    return md_lib.markdown(text, extensions=["extra"])


def create_page(space_key: str, title: str, body: str, parent_id: str | None = None, live: bool = True) -> dict:
    url = f"{DOMAIN}/rest/api/content"
    payload = {
        "type": "live-page" if live else "page",
        "title": title,
        "space": {"key": space_key},
        "body": {"storage": {"value": body, "representation": "storage"}},
    }
    if parent_id:
        payload["ancestors"] = [{"id": parent_id}]

    response = requests.post(url, json=payload, headers=headers, auth=auth)
    if not response.ok and live:
        print(f"live-page 생성 실패 ({response.status_code}), 일반 페이지로 재시도...")
        payload["type"] = "page"
        response = requests.post(url, json=payload, headers=headers, auth=auth)
    if not response.ok:
        print(f"페이지 생성 실패: {response.status_code}\n{response.text}")
    response.raise_for_status()
    return response.json()


def update_page(page_id: str, title: str, body: str) -> dict:
    """기존 페이지를 새 내용으로 업데이트합니다."""
    # 현재 페이지 버전 조회
    get_url = f"{DOMAIN}/rest/api/content/{page_id}?expand=version,ancestors"
    get_resp = requests.get(get_url, headers=headers, auth=auth)
    get_resp.raise_for_status()
    page_data = get_resp.json()

    current_version = page_data["version"]["number"]
    page_type = page_data["type"]

    put_url = f"{DOMAIN}/rest/api/content/{page_id}"
    payload = {
        "type": page_type,
        "title": title,
        "version": {"number": current_version + 1},
        "body": {"storage": {"value": body, "representation": "storage"}},
    }

    response = requests.put(put_url, json=payload, headers=headers, auth=auth)
    if not response.ok:
        print(f"페이지 업데이트 실패: {response.status_code}\n{response.text}")
    response.raise_for_status()
    return response.json()


def set_full_width(page_id: str) -> None:
    """페이지를 full-width 레이아웃으로 설정합니다."""
    prop_url = f"{DOMAIN}/rest/api/content/{page_id}/property"
    for key in ("content-appearance-published", "content-appearance-draft"):
        response = requests.post(
            prop_url,
            json={"key": key, "value": "full-width"},
            headers=headers,
            auth=auth,
        )
        if not response.ok:
            print(f"  [경고] full-width 설정 실패 ({key}): {response.status_code}")


def main():
    parser = argparse.ArgumentParser(description="마크다운 파일로 Confluence 페이지 생성/업데이트")
    parser.add_argument("--file", required=True, help="마크다운 파일 경로")
    parser.add_argument("--title", help="페이지 제목 (파일의 # 제목 대신 사용)")
    parser.add_argument("--youtube-url", help="페이지 상단에 임베드할 YouTube URL")
    parser.add_argument("--parent-id", help="상위 페이지 ID")
    parser.add_argument("--no-live", action="store_true", help="일반 페이지로 생성 (live 비활성화)")
    parser.add_argument("--update-id", help="업데이트할 기존 페이지 ID (지정 시 새 페이지 생성 대신 업데이트)")
    args = parser.parse_args()

    title, body_text = read_markdown_file(args.file)
    if args.title:
        title = args.title
    if not title:
        title = os.path.splitext(os.path.basename(args.file))[0]

    body_parts = []
    if args.youtube_url:
        body_parts.append(youtube_embed_macro(args.youtube_url))
    body_parts.append(markdown_to_confluence_html(body_text))
    body_html = "\n".join(body_parts)

    if args.update_id:
        print(f"페이지 업데이트 중... (ID: {args.update_id})")
        result = update_page(page_id=args.update_id, title=title, body=body_html)
        set_full_width(result["id"])
        page_url = f"{DOMAIN}{result['_links']['webui']}"
        print("\n" + "=" * 40)
        print("문서 업데이트 완료!")
        print(f"  제목 : {result['title']}")
        print(f"  ID   : {result['id']}")
        print(f"  URL  : {page_url}")
        print("=" * 40)
    else:
        print("스페이스 '운영 기획' 조회 중...")
        space_key = get_space_key("운영 기획")
        print(f"스페이스 키: {space_key}")

        result = create_page(
            space_key=space_key,
            title=title,
            body=body_html,
            parent_id=args.parent_id,
            live=not args.no_live,
        )
        set_full_width(result["id"])

        page_url = f"{DOMAIN}{result['_links']['webui']}"
        print("\n" + "=" * 40)
        print("문서 생성 완료!")
        print(f"  제목 : {result['title']}")
        print(f"  ID   : {result['id']}")
        print(f"  URL  : {page_url}")
        print("=" * 40)


if __name__ == "__main__":
    main()
