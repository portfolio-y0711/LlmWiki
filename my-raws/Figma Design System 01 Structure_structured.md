## 📝 1. 영상 전체 요약

> 2024년 시작을 맞아 "FDS(Figma Design System / Free Design System)" 시리즈의 첫 에피소드로, Figma 팀 프로젝트 내에 Foundation 2개(Design Tokens·Iconography)와 Component 2개(Web·App) 총 4개 라이브러리로 디자인 시스템을 구조화하는 방법을 개략적으로 소개한다.

---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **[디자인 시스템 프로젝트 구조 설계]**

    - **세부 주제:** 팀 프로젝트 "FDS" 개요: 제품 팀이 소비하는 시스템을 생성하고 게시하는 공간. 라이브러리 4개(Foundation 2개 + Component 2개)로 구성.
    - **세부 주제:** Foundation 라이브러리 #1 — Design Tokens: Border Radius·Border Weight 변수, Primitive/Semantic 색상 변수, Layout Grid, Spacing 변수, 웹/iOS/Android용 Typography 포함. 라이브러리 커버에 유형·내용·버전·기여자 명시.
    - **세부 주제:** Foundation 라이브러리 #2 — Iconography: Design Tokens 라이브러리를 깔끔하게 유지하기 위해 아이콘을 별도 분리. 아이콘(16~48px), 픽토그램(64~96px), 2D/3D 일러스트레이션 포함.

*   **[플랫폼별 컴포넌트 라이브러리 구성]**

    - **세부 주제:** Component 라이브러리 — Web: 버튼·입력 필드·Alert 등 기본 웹 컴포넌트와 헤더·모달 등 복합 컴포넌트 포함.
    - **세부 주제:** Component 라이브러리 — App: 웹 컴포넌트의 앱 버전 외에도 Navbar·Tabbar·Bottom Sheet 등 앱 고유 컴포넌트 포함.
    - **세부 주제:** 확장 전략: 라이브러리가 커지면 페이지 템플릿과 제품별 컴포넌트를 위한 신규 라이브러리를 별도로 생성하는 것을 권장. 문서화 위치는 향후 에피소드에서 다룸 예정.

*   **[스타터 파일 및 참고 자료]**

    - **세부 주제:** 스타터 파일 배포 방식: Figma 커뮤니티 대신 Google Drive 공유(시리즈 진행에 따라 지속 업데이트 예정). 시청자가 동일한 출발점에서 따라올 수 있도록 제공.
    - **세부 주제:** "Scale" 디자인 시스템 소개: 즉시 사용 가능한 완성된 Figma 디자인 시스템. 변수·네이티브 다크 모드·웹 및 앱 컴포넌트 포함. 4개 스타터 라이브러리 제공.

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*

---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 도입: FDS 시리즈 소개**

    - 2024년 시작과 함께 Figma에서 디자인 시스템을 만드는 신규 시리즈 "FDS" 발표. FDS는 Figma Design System 또는 Free Design System의 약자.
    - 이번 에피소드 목표: 시스템 구조와 필요한 라이브러리 개요 파악.

*   **[00:00:15] ~ 팀 프로젝트와 4개 라이브러리 구조**

    - 팀 프로젝트 "FDS" 내에 4개 라이브러리 구성: Foundation 2개(Design Tokens, Iconography) + Component 2개(Web, App).
    - Design Tokens 라이브러리 구성 요소: Border Radius·Border Weight 변수, Primitive/Semantic 색상 변수, Layout Grid, Spacing 변수, 웹/iOS/Android Typography. 커버 페이지에 라이브러리 유형·내용·버전·기여자 명시, 디자인 패널에서 콘텐츠 업데이트 가능한 속성 설정.

*   **[00:00:40] ~ Iconography 라이브러리**

    - 아이콘을 별도 라이브러리로 분리하는 이유: Design Tokens 라이브러리를 깔끔하게 유지 + 팀이 한 곳에서 아이콘 에셋 집중 관리.
    - 포함 에셋: 아이콘(16~48px), 픽토그램(64~96px), 2D/3D 일러스트레이션.

*   **[00:01:00] ~ Web & App 컴포넌트 라이브러리**

    - Web 컴포넌트 라이브러리: 버튼·입력 필드·Alert 등 기본 컴포넌트 + 헤더·모달 등 복합 컴포넌트.
    - App 컴포넌트 라이브러리: 웹 컴포넌트의 앱 버전 + Navbar·Tabbar·Bottom Sheet 등 앱 전용 컴포넌트.
    - 향후 확장: 라이브러리 규모 증가 시 페이지 템플릿·제품 특화 컴포넌트용 신규 라이브러리 생성 권장. 문서화 위치는 다음 에피소드에서 다룸.

*   **[00:01:20] ~ 스타터 파일 및 마무리**

    - 스타터 라이브러리 4개를 Figma 커뮤니티 대신 Google Drive로 배포(지속 업데이트 반영 목적). 시청자는 동일한 시작점에서 시리즈 따라하기 가능.
    - "Scale" 시스템 소개: 변수·네이티브 다크 모드·웹·앱 컴포넌트를 갖춘 즉시 사용 가능한 완성 시스템.
    - 다음 에피소드 예고: Primitive 색상 변수 생성.

*(이후 영상 끝까지 중요한 흐름이 바뀔 때마다 시간대별 요약 추가)*

---
