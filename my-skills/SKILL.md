# 프로젝트 커스텀 스킬 목록

## /generate-quiz

**설명:** 학습 자료 파일(강좌 자막, 구조화 요약 등)을 분석하여 퀴즈 파일과 정답지를 자동으로 생성합니다. 총 18문제(객관식·O/X·빈칸·단답·서술형) 100점 만점으로 구성됩니다.

**사용법:**
```
/generate-quiz <파일경로1> [파일경로2] ...
```

**예시:**
```
/generate-quiz my-raws/Figma Design System 01 Structure.md my-raws/Figma Design System 01 Structure_structured.md
```

**실행 흐름:**
1. 입력 파일 경로 파싱 및 파일 내용 읽기
2. `my-agents/quiz-generator-agent.md` 프롬프트 로드
3. 퀴즈 파일 생성 → `quiz/<기본이름>-quiz.md`
4. 정답 파일 생성 → `quiz/<기본이름>-answers.md`

**출력 파일 구성:**
- **퀴즈:** 1부 객관식(Q1~7), 2부 O/X(Q8~10), 3부 빈칸(Q11~13), 4부 단답(Q14~16), 5부 서술(Q17~18)
- **정답지:** 파트별 정답·해설, 서술형 모범답안, 채점기준표(100점 만점)

**관련 파일:**
- `.claude/commands/generate-quiz.md` — 스킬 실행 지침
- `my-agents/quiz-generator-agent.md` — 퀴즈 생성 에이전트 프롬프트

---

## /youtube-to-confluence

**설명:** 유튜브 영상의 자막을 다운로드하고, AI로 구조화 요약한 뒤 Confluence '운영 기획' 스페이스에 문서를 자동 생성합니다. 문서 제목은 YouTube 영상 제목을 자동으로 사용합니다.

**사용법:**
```
/youtube-to-confluence <YouTube URL>
```

**예시:**
```
/youtube-to-confluence https://www.youtube.com/watch?v=xxxxx
```

**실행 흐름:**
1. `my-scripts/download-youtube-subtitle.py` — YouTube oEmbed API로 영상 제목 자동 조회 후 자막을 `my-raws/<영상 제목>.md`로 저장
2. Claude Code — `my-agents/professional-video-content-structuring-agent.md` 프롬프트를 적용해 자막을 구조화 요약하고 `my-raws/<영상 제목>_structured.md`로 저장
3. `my-scripts/write-confluence-live-page.py` — 페이지 상단에 YouTube 영상 임베드 + 구조화된 내용으로 Confluence 페이지 생성

**사전 조건:**
- 환경 변수 `CONFLUENCE_EMAIL`, `CONFLUENCE_TOKEN` 설정 필요
- 영상에 한국어(`ko`) 또는 영어(`en`) 자막이 존재해야 함

**관련 파일:**
- `.claude/commands/youtube-to-confluence.md` — 스킬 실행 지침
- `my-scripts/download-youtube-subtitle.py` — 자막 다운로드 및 YouTube 제목 조회 스크립트
- `my-scripts/write-confluence-live-page.py` — Confluence 페이지 생성 스크립트 (YouTube 임베드 포함)
- `my-agents/professional-video-content-structuring-agent.md` — 영상 구조화 요약 에이전트 프롬프트
