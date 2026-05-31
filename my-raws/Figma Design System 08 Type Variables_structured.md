---

## 📝 1. 영상 전체 요약

> Figma Design System 시리즈의 8번째 에피소드로, Primitive·Semantic 두 계층의 **타입 변수(Type Variables)**를 구성하여 텍스트 스타일을 완전히 변수 기반으로 연결하는 방법을 소개한다. 이를 통해 Desktop/Mobile/iOS/Android 모드 전환 시 폰트 패밀리·사이즈가 자동으로 바뀌는 반응형 타이포그래피 시스템을 Figma와 코드 양쪽에서 동일한 구조로 구현할 수 있다.



---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **도입 — 타입 변수의 개념과 필요성**

    - **세부 주제:** 타입 변수(Type Variables)란 무엇인가 — 폰트 패밀리·웨이트·사이즈·라인 높이·레터 스페이싱을 모두 변수로 구동하는 개념 설명
    - **세부 주제:** 코드(CSS 변수·믹스인)와 Figma 변수 패널이 같은 계층 구조를 공유하는 방식 설명

*   **핵심 구조 — Primitive & Semantic 컬렉션 설계**

    - **세부 주제:** Global Unit 변수 세트 도입 — 사이즈·레터 스페이싱을 구동하는 공통 단위값
    - **세부 주제:** Primitive Type 컬렉션 — family(Inter/SF Pro/Roboto), weight, size, line-height, letter-spacing 각 세트 구성
    - **세부 주제:** Semantic Type 컬렉션 — Desktop·Mobile·iOS·Android 4가지 모드와 반응형 브레이크포인트(1440 / 393) 설정, 폰트 패밀리 모드 전환

*   **심화 활용 — 텍스트 스타일 연결 및 실습 데모**

    - **세부 주제:** 기존 텍스트 스타일(heading L, text L 등)에 Semantic Type 변수를 매핑하는 방법
    - **세부 주제:** 실제 프레임(iPhone 14 Pro)에 텍스트를 배치하고 모드를 전환해 폰트 패밀리·사이즈 변화를 시각적으로 확인하는 실습

*   **결론 — 정리 및 다음 에피소드 예고**

    - **세부 주제:** Primitive → Semantic → 스타일 연결이라는 믹스인(mixin) 패턴 재확인
    - **세부 주제:** 다음 에피소드 주제(아이코노그래피) 예고

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*



---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 시리즈 소개 및 에피소드 개요**

    - FDS(Figma Design System) 시리즈 8번째 에피소드임을 소개
    - 이번 에피소드는 튜토리얼이 아닌 '워크스루(walkthrough)' 형식으로 진행됨을 안내
    - 플러그인으로 원하는 구조를 만들 수 없어 수동으로 진행한다고 설명
    - 영상 설명 링크에서 예제 파일을 받도록 안내

*   **[00:01:00] ~ 타입 변수 개념 설명**

    - 타입 변수는 텍스트 스타일(폰트 패밀리·웨이트·사이즈·라인 높이·레터 스페이싱)의 모든 값을 구동함
    - 컬러 변수와 동일하게 Primitive → Semantic 계층 구조로 구성됨
    - 예시: `heading-L`의 family는 `family-inter`, weight는 `weight-semibold`, size는 `size-5XL` 등으로 연결
    - 코드 측 구현: root 변수 파일(primitive) → semantic 믹스인 파일 → 스타일시트에서 믹스인 포함

*   **[00:03:00] ~ Figma 변수 패널 탐색**

    - Figma UI3에서 변수 패널 위치 확인
    - **Global Unit 변수 세트** 소개: 2, 4, 4… 와 같이 120까지 내려가는 공통 크기 단위값, size 및 letter-spacing에 활용
    - **Primitive Type 컬렉션** 내 세트 확인
        - family: Inter, SF Pro Text, Roboto
        - weight: regular, semi-bold
        - size: XS·S·M·L ~ 10XL (global unit 연동)
        - line-height: XS·S·M·L ~ 10XL (size L = 16, line-height L = 24 예시)
        - letter-spacing: excess(-10.5), small, none(0)

*   **[00:05:30] ~ Semantic Type 컬렉션 구성**

    - Desktop(1440px)·Mobile·iOS·Android 4가지 모드로 구성
    - 폰트 패밀리 모드 전환: 반응형 웹→Inter, iOS→SF Pro, Android→Roboto
    - `heading-L` 예시: Desktop = size-5XL + line-height-5XL, Mobile = size-4XL + line-height-4XL (실제값: 32→28)
    - 모든 heading과 text(regular/semibold 두 가지 weight)의 size·weight·line-height·letter-spacing 변수 완비
    - text-xs까지 내려가며 size 10, line-height 14로 마무리

*   **[00:08:00] ~ 텍스트 스타일에 Semantic 변수 매핑 확인**

    - 기존에 생성된 Web/Desktop/Mobile/iOS/Android용 텍스트 스타일 목록 확인
    - `heading-L` 스타일 편집 화면: family → semantic type family heading-L semibold, weight → heading-L semibold weight, size/line-height/letter-spacing도 동일하게 변수로 연결됨
    - `text-L-regular`도 동일한 방식으로 모두 연결 완료

*   **[00:09:30] ~ 실습 데모 — 프레임 생성 및 모드 전환**

    - iPhone 14 Pro 사이즈 프레임 생성, 이름: `type variable test`
    - `heading-L` 텍스트와 `text-L` 텍스트 배치, 색상 적용(content-primary / content-secondary)
    - 레이아웃 설정에서 **Semantic Type Breakpoint** 모드 적용 → 프레임 너비 자동 조정
    - Appearance에서 **Semantic Type** 모드 전환 실습
        - Desktop: 기본 상태
        - Mobile: heading 사이즈 축소(5XL→4XL), text는 변화 없음
        - iOS: 두 텍스트 모두 SF Pro로 패밀리 변경
        - Android: Roboto로 패밀리 변경

*   **[00:11:30] ~ 정리 및 마무리**

    - Primitive Type(family·weight·size·global unit) → Semantic Type(모드·브레이크포인트·패밀리) → 텍스트 스타일 순서로 연결되는 구조 재정리
    - 코드의 믹스인 패턴과 동일한 방식임을 강조
    - 다음 에피소드 예고: **아이코노그래피(Iconography)**

---
