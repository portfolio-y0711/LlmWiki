## 📝 1. 영상 전체 요약

> FDS 시리즈 6화로, 레이아웃(12컬럼 반응형 그리드)과 브레이크포인트(데스크톱·태블릿·모바일 4단계)의 개념을 설명하고, Figma Variables 패널에서 "layout" 컬렉션으로 브레이크포인트 변수(XL/L/M/S: 1440·1024·768·393px)를 생성한 뒤, 레이아웃 그리드(데스크톱 12컬럼·모바일 4컬럼)를 Style로 설정하고 Typography 변수 모드 전환 팁을 함께 소개한다.

---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **[레이아웃과 브레이크포인트의 개념]**

    - **세부 주제:** 레이아웃 = 수직 컬럼 세트. 디자이너와 엔지니어가 화면 구조를 정의하는 기반. FDS는 데스크톱·태블릿 12컬럼, 모바일·앱 4컬럼 반응형 그리드 사용.
    - **세부 주제:** 그리드 구성: 컬럼당 좌우 8px 패딩, 좌우 8px 사이드 마진 → 전체 거터 16px. 반응형으로 컬럼 너비는 유동적.
    - **세부 주제:** 브레이크포인트 = 화면 크기·기기 방향에 따라 레이아웃이 전환되는 기준점. FDS 4단계: 데스크톱(XL·1440px), 태블릿 가로(L·1024px), 태블릿 세로(M·768px), 모바일(S·393px — iPhone 14/15 Pro 동일 크기, 앱 디자인에도 활용).

*   **[Figma Variables: Layout 컬렉션 생성]**

    - **세부 주제:** "layout" 컬렉션 생성 → Number 타입 변수 4개: XL(1440), L(1024), M(768), S(393). Shift+Enter 단축키로 빠른 복제(커뮤니티 팁).
    - **세부 주제:** 전체 선택 → New Group → "breakpoint" 그룹으로 묶기.

*   **[Typography 변수 모드 전환 팁 (미래 확장)]**

    - **세부 주제:** Figma의 신규 Type Variables 기능 활용: "typography" 컬렉션 생성 → Number 변수 "breakpoint"에 layout 변수 참조 → Desktop/Mobile 두 모드 설정.
    - **세부 주제:** 활용법: 프레임에 typography/breakpoint 변수 할당 후 모드를 Desktop↔Mobile로 전환하면 Typography 크기 전체가 자동 전환. 레이아웃 그리드 자동 전환은 Figma 미지원(수동 변경 필요).

*   **[레이아웃 그리드 Style 생성]**

    - **세부 주제:** 데스크톱 프레임에 Layout Grid 추가: Grid → Columns, 12컬럼, 색상(Blue 10% 불투명도), Type: Stretch, Margin 16, Gutter 16.
    - **세부 주제:** 모바일 그리드 Style 생성: 데스크톱 프레임 복제 → 이름 변경 → Styles 패널에서 "mobile" Style 추가 → 컬럼 수 4로 변경. 다음 에피소드 예고: Border Radius & Width Variables.

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*

---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 레이아웃과 브레이크포인트 개념 설명**

    - 레이아웃 = 수직 컬럼 세트. FDS: 데스크톱·태블릿 12컬럼, 모바일·앱 4컬럼. 컬럼당 좌우 8px 패딩, 사이드 마진 8px → 거터 16px.
    - 브레이크포인트 = 화면 크기에 따라 레이아웃이 전환되는 기준점. 4단계: 데스크톱(XL·1440), 태블릿 가로(L·1024), 태블릿 세로(M·768), 모바일(S·393). 모바일 = iPhone 14/15 Pro 크기 = 앱 디자인 기준.

*   **[00:01:30] ~ Figma Variables에서 Layout 컬렉션 생성**

    - Variables 패널 → "layout" 컬렉션 생성 → Number 타입 첫 변수: XL, 값 1440.
    - Shift+Enter로 빠른 복제(커뮤니티 멤버 Abdul 팁). L(1024), M(768), S(393) 순서로 생성.
    - 전체 선택 → New Group → "breakpoint" 그룹으로 묶기.

*   **[00:02:30] ~ Typography 변수 모드 전환 팁**

    - Figma 신규 Type Variables 기능을 활용한 확장 방법: "typography" 컬렉션 생성 → Number 변수 "breakpoint"에 layout 변수(XL) 참조 → Desktop/Mobile 두 모드 추가(Desktop: layout/XL, Mobile: layout/S).
    - 프레임에 typography/breakpoint 변수 할당 → 모드 전환 시 Typography 크기 전체 자동 전환. 레이아웃 그리드 자동 전환은 Figma 미지원(수동 변경 필요).

*   **[00:03:30] ~ 레이아웃 그리드 Style 생성 및 마무리**

    - 데스크톱 프레임 선택 → Layout Grid 추가(+) → Grid → Columns → 12컬럼, 색상 Blue 10%, Type: Stretch, Margin 16, Gutter 16.
    - 모바일 그리드: 데스크톱 프레임 복제 → "mobile"로 이름 변경 → Styles에서 "mobile" Style 추가 → 컬럼 수 4로 변경. 완료.
    - 다음 에피소드 예고: Border Radius & Width Variables.

*(이후 영상 끝까지 중요한 흐름이 바뀔 때마다 시간대별 요약 추가)*

---
