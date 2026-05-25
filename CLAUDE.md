# Claude Python Environment Guidelines

이 프로젝트는 Python 의존성 관리를 위해 가상환경을 사용합니다.
시스템 Python 환경 충돌(externally-managed-environment)을 방지하기 위해 다음 규칙을 엄격히 따르세요.

## 실행 및 패키지 설치 규칙

1. **패키지 설치:** 기본 `pip` 대신 반드시 `uv pip install <패키지명>`을 사용하세요. (속도가 훨씬 빠르고 가상환경을 자동 인식합니다)
2. **스크립트 실행:** 코드를 실행할 때는 `python script.py` 대신 `uv run script.py`를 사용하세요.
3. **의존성 기록:** 새로운 패키지를 설치한 후에는 항상 `uv pip freeze > requirements.txt`를 실행하여 의존성을 업데이트하세요.

## Confluence 문서 생성 규칙

Confluence에 문서를 생성할 때는 항상 다음 설정을 사용하세요.

- **도메인:** `https://seguataneo.atlassian.net`
- **스페이스:** `운영 기획`
