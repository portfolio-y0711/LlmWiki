import os
import requests
from requests.auth import HTTPBasicAuth

# 환경 설정
# 도메인 뒤에 /wiki를 포함하여 설정하면 경로 관리가 훨씬 쉽습니다.
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
    """정상 확인된 v1 엔드포인트를 사용하여 스페이스 키 조회"""
    url = f"{DOMAIN}/rest/api/space"
    params = {"limit": 50}
    
    try:
        response = requests.get(url, headers=headers, auth=auth, params=params)
        
        # 403 에러(권한) 또는 404(경로) 발생 시 상세 내용 출력
        if not response.ok:
            print(f"에러 발생: {response.status_code}")
            print(f"상세 내용: {response.text}")
            
        response.raise_for_status()
        
        # v1 API의 응답 구조는 'results' 키 내에 목록이 있습니다.
        results = response.json().get("results", [])
        for space in results:
            if space["name"] == space_name:
                return space["key"]
        
        raise ValueError(f"'{space_name}' 이름의 스페이스를 찾을 수 없습니다. (검색된 스페이스 수: {len(results)})")
        
    except Exception as e:
        print(f"스페이스 조회 중 오류 발생: {e}")
        raise

def create_page(space_key: str, title: str, body: str, parent_id: str | None = None) -> dict:
    """페이지 생성 (v1 엔드포인트)"""
    url = f"{DOMAIN}/rest/api/content"
    
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {
            "storage": {
                "value": body,
                "representation": "storage",
            }
        },
    }
    
    if parent_id:
        payload["ancestors"] = [{"id": parent_id}]
    
    response = requests.post(url, json=payload, headers=headers, auth=auth)
    
    if not response.ok:
        print(f"페이지 생성 실패: {response.status_code}")
        print(f"에러 내용: {response.text}")
        
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        # 1. 스페이스 키 조회 ("운영 기획" 이름 확인 필요)
        target_space_name = "운영 기획"
        print(f"'{target_space_name}' 스페이스 조회 중...")
        space_key = get_space_key(target_space_name)
        print(f"성공! 스페이스 키: {space_key}")

        # 2. 페이지 생성
        title = "테스트 문서 (Claude Code API)"
        body = "<h2>자동 생성 문서</h2><p>Python v1 API를 사용하여 생성되었습니다.</p>"
        
        result = create_page(space_key=space_key, title=title, body=body)
        
        page_id = result["id"]
        webui = result.get("_links", {}).get("webui", "")
        page_url = f"{DOMAIN}{webui}"

        print("\n" + "="*40)
        print(f"문서 생성 완료!")
        print(f"  ID   : {page_id}")
        print(f"  URL  : {page_url}")
        print("="*40)

    except Exception as e:
        print(f"\n[실행 실패] {e}")
