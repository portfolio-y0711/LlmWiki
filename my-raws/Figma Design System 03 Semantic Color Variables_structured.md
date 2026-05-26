## 📝 1. 영상 전체 요약

> FDS 시리즈 3화로, Semantic 색상 변수의 개념(의미 기반 명명)과 그룹·역할·수식어로 구성된 네이밍 스키마를 설명하고, Styler 플러그인으로 Color Style을 생성한 뒤 Styles to Variables 플러그인으로 "Semantic" 컬렉션을 만들어 Primitive 변수를 수동 재할당하는 방식으로 라이트/다크 모드를 완성하는 전체 워크플로우를 다룬다.

---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **[누락된 Primitive 보완: Black/White 추가]**

    - **세부 주제:** 전 에피소드 누락 항목 처리: Black(#000000)·White(#FFFFFF) 변수 생성. 오버레이 용도를 위해 50% 불투명도 버전(Black/50, White/50)도 추가. 모두 "primary" 그룹으로 묶어 Primitives 컬렉션 최상단 배치.

*   **[Semantic 색상 변수의 개념과 네이밍 스키마]**

    - **세부 주제:** Primitive vs. Semantic의 차이: Primitive는 Hex 값 기반의 실제 색상(Brand 500 등). Semantic은 "어떻게 사용되는가"에 따른 의미 기반 이름(background/brand 등). Primitive가 변경되면 Semantic을 통해 전체 시스템에 자동 반영.
    - **세부 주제:** 네이밍 스키마 구성 3요소: ①그룹(content·background·border·surface·overlay), ②역할(primary·secondary·tertiary·brand·mono·link·info·notice·negative·positive), ③수식어(bold·subtle·inverse) 및 상태(hover·focus·pressed·selected·disabled), 값(L0~L6·overlay 50). 조합 예시: content/link/hover, background/primary/press, surface/L3, overlay/inverse/50.

*   **[Semantic 변수 생성 워크플로우]**

    - **세부 주제:** 변수 테이블 사전 준비: Variable Color Style 플러그인으로 라이트/다크 모드용 Semantic 색상을 표 형태로 미리 배치(수동 생성 시 1~2시간 소요 방지). 그룹·역할·수식어 조합이 직관적인 멘탈 모델 형성.
    - **세부 주제:** Styler 플러그인으로 Color Style 생성: Content·Background·Border·Surface·Overlay 색상 레이어를 그룹별로 선택해 "Generate Styles" 실행. Surface 그룹 실행 시 Shadow Effect Style도 함께 생성됨 → Shadow로 이름 변경(Surface L1 Shadow 등).
    - **세부 주제:** Styles to Variables 플러그인으로 변수 변환: 생성된 Style들을 "semantic" 컬렉션으로 일괄 변환(54개 변수 생성). 단, 플러그인이 할당된 Primitive 변수 참조를 유지하지 못하고 Hex 값으로 변환하는 한계 → 각 변수에 Primitive 변수를 수동 재할당 필요.

*   **[라이트·다크 모드 설정 및 마무리]**

    - **세부 주제:** 라이트 모드 완성: Semantic 변수 패널에서 Mode를 "light"로 설정 후 각 변수마다 Libraries에서 해당 Primitive 변수(neutral/900 등)를 찾아 재할당.
    - **세부 주제:** 다크 모드 추가: 변수 패널에서 "New Variable Mode" → "dark"로 이름 변경. 라이트 모드와 동일한 값이 복사되므로 각 변수의 다크 모드 값을 적절한 Primitive 변수로 교체(예: content/primary → neutral/900 → white).
    - **세부 주제:** 정리: 변환에 사용된 Color Style(content·background·border·surface·overlay) 삭제. Shadow Effect Style은 Figma가 아직 변수를 지원하지 않으므로 유지. 문서 테이블의 색상 칩을 Semantic 변수로 재할당해 문서화 완성. 시작·완료 파일 두 버전 모두 설명 링크 제공.

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*

---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 누락된 Primitive 보완: Black/White 변수 추가**

    - 전 에피소드에서 누락된 Black(#000000)·White(#FFFFFF) 변수를 Variables 패널에서 직접 생성. 오버레이용 50% 불투명도 버전(Black/50, White/50)도 추가.
    - 4개 변수를 "primary" 그룹으로 묶어 Primitives 컬렉션 최상단 배치.

*   **[00:00:40] ~ Semantic 색상이란 무엇인가**

    - Semantic 색상 = 색상의 외형이 아닌 사용 목적에 따른 의미 기반 명명. 예: background/brand는 버튼 배경에 사용되며, 브랜드 색이 파랑→보라로 바뀌어도 Semantic 변수는 그대로이므로 전체 시스템에 자동 반영.
    - 네이밍 스키마: 그룹(content/background/border/surface/overlay) + 역할(primary/brand/link/negative/positive 등) + 수식어(bold/subtle/inverse) + 상태(hover/press/disabled 등) + 값(L0~L6, overlay 50).
    - 예시 읽기: content/primary(최상위 텍스트·아이콘), content/link(링크), background/brand/press(버튼 누른 상태 배경), border/notice(경고 보더), surface/L3(레벨3 엘리베이션), overlay/50(모달 뒷 배경).

*   **[00:02:00] ~ Styler 플러그인으로 Color Style 생성**

    - Variable Color Style 플러그인으로 미리 배치한 테이블에서 그룹별 색상 레이어 선택 → Styler "Generate Styles" 실행. Content → Background → Border → Surface → Overlay 순으로 반복.
    - Surface 실행 시 Shadow Effect Style도 함께 생성 → "L1 Shadow" 등으로 이름 변경(surface L1 elevation 그림자용).
    - 생성 후 순서가 뒤섞이므로 정렬 수정 후 진행.

*   **[00:03:30] ~ Styles to Variables 변환 및 Primitive 재할당**

    - "Styles to Variables" 플러그인으로 54개 Semantic Color Style을 "semantic" 컬렉션 변수로 일괄 변환. 단, Primitive 변수 참조가 Hex 값으로 대체되는 한계 발생.
    - Variables 패널 → Mode를 "light"로 설정 → 각 변수마다 Libraries에서 올바른 Primitive 변수(neutral/900 등)를 찾아 수동 재할당.

*   **[00:05:00] ~ 다크 모드 추가 및 최종 정리**

    - Semantic 컬렉션에서 "New Variable Mode" 추가 → "dark"로 이름 변경. 라이트 모드 값이 복사되어 있으므로 다크 모드에 맞는 Primitive 변수로 교체(예: content/primary → white).
    - 모드 완성 후 Color Style(content·background·border·surface·overlay) 전부 삭제. Shadow Effect Style은 Figma 미지원으로 유지.
    - 문서 테이블의 색상 칩을 Semantic 변수로 재할당해 문서화 완료. 시작·완료 파일 두 버전 링크 제공.
    - 다음 에피소드 예고: Typography.

*(이후 영상 끝까지 중요한 흐름이 바뀔 때마다 시간대별 요약 추가)*

---
