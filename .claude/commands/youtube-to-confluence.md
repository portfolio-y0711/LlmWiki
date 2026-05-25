유튜브 영상의 자막을 다운로드하고 Confluence '운영 기획' 스페이스에 문서를 생성합니다.

**입력값:** $ARGUMENTS
(형식: `<YouTube URL>`)

다음 순서로 정확히 실행하세요:

## 1단계 — 자막 다운로드 및 YouTube 제목 조회

입력값에서 YouTube URL(첫 번째 토큰)을 파싱하여 아래 명령을 실행하세요:

```
uv run my-scripts/download-youtube-subtitle.py --url <URL>
```

- 출력에서 `YOUTUBE_TITLE=` 줄과 `OUTPUT_FILE=` 줄을 파싱하여 실제 제목과 파일 경로를 추출하세요.
- 오류가 발생하면 내용을 확인하고 사용자에게 알린 뒤 중단하세요.

## 2단계 — 자막 구조화 요약

다음 두 파일을 읽으세요:
1. `my-agents/professional-video-content-structuring-agent.md` — 구조화 에이전트 프롬프트
2. 1단계의 OUTPUT_FILE — 다운로드된 자막 내용

에이전트 프롬프트의 지침에 따라 자막 내용을 분석하고 구조화된 요약을 생성하세요.
생성한 결과를 `<OUTPUT_FILE 경로에서 .md 제거>_structured.md` 파일에 저장하세요.
이 파일 경로를 STRUCTURED_FILE로 기억하세요.

## 3단계 — Confluence 페이지 생성

2단계까지 성공한 경우에만 실행하세요.
`<YOUTUBE_TITLE>`은 1단계에서 파싱한 실제 YouTube 영상 제목을 사용하세요.

```
uv run my-scripts/write-confluence-live-page.py \
  --file <STRUCTURED_FILE> \
  --youtube-url <URL> \
  --title "<YOUTUBE_TITLE>"
```

## 4단계 — 결과 보고

생성된 Confluence 페이지 URL을 사용자에게 알려주세요.
