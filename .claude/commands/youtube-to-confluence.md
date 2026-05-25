유튜브 영상의 자막을 다운로드하고 Confluence '운영 기획' 스페이스에 문서를 생성합니다.

**입력값:** $ARGUMENTS
(형식: `<YouTube URL> <문서 제목>`)

다음 순서로 정확히 실행하세요:

## 1단계 — 자막 다운로드

입력값에서 YouTube URL(첫 번째 토큰)과 제목(나머지 전체)을 파싱하여 아래 명령을 실행하세요:

```
uv run my-scripts/download-youtube-subtitle.py --url <URL> --title <제목>
```

- 성공 시 `my-raws/<제목>.md` 파일이 생성됩니다.
- 오류가 발생하면 내용을 확인하고 사용자에게 알린 뒤 중단하세요.

## 2단계 — Confluence 페이지 생성

1단계가 성공한 경우에만 아래 명령을 실행하세요:

```
uv run my-scripts/write-confluence-live-page.py --file my-raws/<제목>.md
```

## 3단계 — 결과 보고

생성된 Confluence 페이지 URL을 사용자에게 알려주세요.
