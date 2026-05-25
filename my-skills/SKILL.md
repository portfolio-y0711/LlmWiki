# 프로젝트 커스텀 스킬 목록

## /youtube-to-confluence

**설명:** 유튜브 영상의 자막을 다운로드하고, 해당 내용으로 Confluence '운영 기획' 스페이스에 문서를 자동 생성합니다.

**사용법:**
```
/youtube-to-confluence <YouTube URL> <문서 제목>
```

**예시:**
```
/youtube-to-confluence https://www.youtube.com/watch?v=xxxxx Claude Code 활용법 정리
```

**실행 흐름:**
1. `my-scripts/download-youtube-subtitle.py` — 자막을 `my-raws/<제목>.md`로 저장
2. `my-scripts/write-confluence-live-page.py` — 저장된 파일로 Confluence 페이지 생성

**사전 조건:**
- 환경 변수 `CONFLUENCE_EMAIL`, `CONFLUENCE_TOKEN` 설정 필요
- 영상에 한국어(`ko`) 또는 영어(`en`) 자막이 존재해야 함

**관련 파일:**
- `.claude/commands/youtube-to-confluence.md` — 스킬 실행 지침
- `my-scripts/download-youtube-subtitle.py` — 자막 다운로드 스크립트
- `my-scripts/write-confluence-live-page.py` — Confluence 페이지 생성 스크립트
