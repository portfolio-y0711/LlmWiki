import argparse
import os
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
    if not response.ok:
        print(f"에러 발생: {response.status_code}\n{response.text}")
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


def markdown_to_confluence_html(text: str) -> str:
    """기본 마크다운을 Confluence 스토리지(HTML) 형식으로 변환합니다."""
    html_parts = []
    for para in text.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if para.startswith("## "):
            html_parts.append(f"<h2>{para[3:].strip()}</h2>")
        elif para.startswith("### "):
            html_parts.append(f"<h3>{para[4:].strip()}</h3>")
        else:
            html_parts.append(f"<p>{para.replace(chr(10), '<br/>')}</p>")
    return "\n".join(html_parts)


def create_page(space_key: str, title: str, body: str, parent_id: str | None = None) -> dict:
    url = f"{DOMAIN}/rest/api/content"
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {"storage": {"value": body, "representation": "storage"}},
    }
    if parent_id:
        payload["ancestors"] = [{"id": parent_id}]

    response = requests.post(url, json=payload, headers=headers, auth=auth)
    if not response.ok:
        print(f"페이지 생성 실패: {response.status_code}\n{response.text}")
    response.raise_for_status()
    return response.json()


def main():
    parser = argparse.ArgumentParser(description="마크다운 파일로 Confluence 페이지 생성")
    parser.add_argument("--file", required=True, help="마크다운 파일 경로 (my-raws/제목.md)")
    parser.add_argument("--title", help="페이지 제목 (파일의 # 제목 대신 사용)")
    parser.add_argument("--parent-id", help="상위 페이지 ID")
    args = parser.parse_args()

    title, body_text = read_markdown_file(args.file)
    if args.title:
        title = args.title
    if not title:
        title = os.path.splitext(os.path.basename(args.file))[0]

    body_html = markdown_to_confluence_html(body_text)

    print(f"스페이스 '운영 기획' 조회 중...")
    space_key = get_space_key("운영 기획")
    print(f"스페이스 키: {space_key}")

    result = create_page(
        space_key=space_key,
        title=title,
        body=body_html,
        parent_id=args.parent_id,
    )

    page_url = f"{DOMAIN}{result['_links']['webui']}"
    print("\n" + "=" * 40)
    print(f"문서 생성 완료!")
    print(f"  제목 : {result['title']}")
    print(f"  ID   : {result['id']}")
    print(f"  URL  : {page_url}")
    print("=" * 40)


if __name__ == "__main__":
    main()
