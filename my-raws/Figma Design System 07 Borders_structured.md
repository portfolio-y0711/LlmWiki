---

## 📝 1. 영상 전체 요약

> Figma Design System 시리즈 7번째 에피소드로, UI 요소의 모서리 곡률과 테두리 두께를 표준화하는 **Border Radius·Border Width 변수**를 생성하고 실제 컴포넌트에 적용하는 방법을 다룬다. T-shirt 사이즈 명명 체계로 변수 값을 체계화하고, Dev Mode에서 엔지니어가 즉시 확인할 수 있도록 연결하는 워크플로우를 보여준다.



---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **도입 — Border의 개념과 역할**

    - **세부 주제:** Border Radius 개념 — 모서리 곡률이 UI의 느낌(기업적 ↔ 친근함)에 미치는 시각적 영향 설명
    - **세부 주제:** Border Width 개념 — 테두리 두께가 상태 변화(default → focused)를 사용자에게 전달하는 역할

*   **핵심 구조 — 변수 명명 체계와 값 설계**

    - **세부 주제:** Border Radius 변수 세트 — Circle(50%), Pill(999), Large(16), Medium(12), Small(8), Extra Small(4)
    - **세부 주제:** Border Width 변수 세트 — XL(8px), Large(4px), Medium(2px), Small(1.5px), Extra Small(1px)
    - **세부 주제:** T-shirt 사이즈 기반 명명 규칙으로 두 세트를 일관성 있게 구성하는 방식

*   **심화 활용 — 변수 생성 및 컴포넌트 적용 실습**

    - **세부 주제:** Figma 변수 패널에서 `border` 컬렉션 생성, radius·width 그룹 구성 방법
    - **세부 주제:** 카드 및 인풋 필드에 Border Radius 변수 적용 (command+shift 다중 선택 기법)
    - **세부 주제:** 아웃라인 스트로크에 Border Width 변수를 우클릭으로 적용하는 방법

*   **결론 — Dev Mode 확인 및 예고**

    - **세부 주제:** Dev Mode에서 `radius-L: 16`, `border-width-M: 2px` 등 변수 연결 확인
    - **세부 주제:** 향후 Scoping 업데이트 예고 및 다음 에피소드(Typography Variables) 예고

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*



---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 에피소드 소개 및 Border 개념 설명**

    - FDS 시리즈 7번째 에피소드, Border Radius와 Border Width 변수 생성을 다룸
    - Border의 정의: 버튼·카드·이미지 등 UI 요소의 가장자리를 둘러싸는 요소(radius, width, style)
    - Border Radius 시각 효과 예시: 각진 디자인(Microsoft 스타일) vs 둥근 디자인(Apple 스타일) 비교
    - 로그인 폼 예시로 secondary 버튼·인풋 필드의 sharp vs rounded 차이 설명

*   **[00:02:00] ~ Border Radius 변수 명세 소개**

    - T-shirt 사이즈 명명 체계 설명
    - **Border Radius 값 표:** Circle=50%, Pill=999, Large=16, Medium=12, Small=8, Extra Small=4
    - Circle: 정사각형을 원으로 만드는 용도 / Pill: 직사각형의 좌우를 완전히 둥글게 만드는 용도

*   **[00:03:00] ~ Border Width 변수 명세 소개**

    - Border Width: 요소의 외곽선 두께, 상태 변화(interaction state)를 시각적으로 전달
    - 인풋 필드 예시: default=1px, focused=2px (두께 + 색상 동시 변경)
    - Small(1.5px)은 아이콘 전용, 고해상도 화면에서도 선명하게 표시
    - **Border Width 값 표:** XL=8, Large=4, Medium=2, Small=1.5, Extra Small=1

*   **[00:04:30] ~ 변수 패널에서 Border 컬렉션 생성**

    - 변수 패널 열기 → `border` 컬렉션 생성
    - Number 타입 변수로 `border-radius/circle` = 50 추가 (현재 Figma에서 % 미지원, 엔지니어에게 50px→50% 전환 안내 필요)
    - Shift+Enter로 빠른 변수 복제: pill(999), large(16), medium(12), small(8), extra-small(4) 순차 입력
    - 전체 선택 후 우클릭 → `New Group with Selection`으로 `border-radius` 그룹 생성
    - 그룹 복제 후 `border-width` 그룹으로 전환, 불필요한 변수 삭제 후 XL(8)·Large(4)·Medium(2)·Small(1.5)·Extra Small(1) 값 수정

*   **[00:07:30] ~ 카드 컴포넌트에 Border Radius 적용**

    - 카드 전체 선택 → 디자인 패널 Border Radius에서 `radius/large(16)` 적용
    - Command+Shift 클릭으로 내부 요소 다중 선택 → `radius/medium(12)` 적용
    - Dev Mode 확인: `border-radius: radius-L 16` 표시로 엔지니어 핸드오프 준비 완료

*   **[00:09:00] ~ 인풋 필드에 Border Width 변수 적용**

    - 인풋 필드 + Focus 상태 선택 → Border Radius `radius/medium(12)` 적용
    - Scoping 미적용 시 스트로크 변수 아이콘이 안 보임 → **우클릭 → Apply Variable** 방법으로 해결
    - `border-width/medium(2)` 적용 후 Strokes per side에서 개별 측면 독립 적용 가능 확인
    - XL(8)로 변경해 한쪽 면만 두꺼운 Border 효과 시연

*   **[00:10:30] ~ Dev Mode 최종 확인 및 마무리**

    - Dev Mode에서 `border-width-M: 2px`, `border-focus: semantic variable`, `radius-M: 12` 확인
    - 향후 Scoping 업데이트 예고: Corner Radius, Spacing 등 변수가 적합한 필드에만 표시되도록 개선 예정
    - 다음 에피소드 예고: **Typography Variables(타이포그래피 변수)** 업데이트

---
