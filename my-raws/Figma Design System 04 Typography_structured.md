## 📝 1. 영상 전체 요약

> FDS 시리즈 4화로, 타이포그래피의 개념(글꼴 배열의 예술)과 FDS에서 사용하는 폰트 패밀리(Inter·SF Pro·Roboto), 웨이트(Regular·Semi Bold), 그룹(Heading·Text), T셔츠 사이징 네이밍 방식을 설명하고, Styler 플러그인으로 텍스트 스타일을 일괄 생성한 뒤 플러그인 실패 시 누락 스타일을 수동으로 보완하는 전체 워크플로우를 다룬다.

---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **[타이포그래피의 정의와 디자인 시스템에서의 역할]**

    - **세부 주제:** 타이포그래피 = 폰트 선택을 넘어 글자를 배열하는 예술. 가독성·판독성·시각적 매력을 결정하며, 디자인 시스템에서 콘텐츠의 시각적 아이덴티티와 계층 구조 확립에 핵심적인 역할을 담당.

*   **[FDS 폰트 패밀리·웨이트·그룹 구성]**

    - **세부 주제:** 폰트 패밀리 선택: 웹은 Inter(기본), iOS는 SF Pro Display·SF Pro Text, Android는 Roboto. 폰트 패밀리 = 시스템 전체에서 사용하는 서체 그룹.
    - **세부 주제:** 웨이트: Regular와 Semi Bold 두 가지만 사용. 두께(캐릭터의 굵기)를 의미하며 최소한으로 유지해 일관성 확보.
    - **세부 주제:** 그룹: Heading과 Text 두 그룹. 대부분의 사용 사례를 커버하며, 필요 시 Label·Link 등을 추가 가능.

*   **[타입 스케일 설계: 4포인트 글로벌 스케일 + T셔츠 사이징]**

    - **세부 주제:** 스케일(크기): 글로벌 4포인트 스케일과 T셔츠 사이징을 결합. 크기는 48·40·32·24(4포인트씩 감소) → 20·16(추가 감소), 라인 높이는 56·48·40·32·28·24.
    - **세부 주제:** T셔츠 사이징의 장점: H1·H2 같은 역할 기반 명명 대신 2xs~5xl 규모 기반 명명 사용. 제품마다 "Heading XL"을 H1로 쓸 수도, "Heading L"로 쓸 수도 있어 여러 제품에 동일 Typography Set 재사용 가능.

*   **[네이밍 컨벤션]**

    - **세부 주제:** 명명 구조: `그룹 / 크기 / 웨이트` 형식. 예: `heading/L/semibold`, `text/L/regular`, `text/L/semibold`. Heading은 Semi Bold부터 시작 후 필요에 따라 웨이트 추가.

*   **[Styler 플러그인을 이용한 스타일 생성 워크플로우]**

    - **세부 주제:** 사전 준비: 레이어명을 스타일명(예: `web/heading/5XL/semibold`)으로 지정하고 각 레이어에 웨이트·크기·라인 높이·자간 값을 미리 적용.
    - **세부 주제:** 실행 방법: 웹·iOS·Android별로 Heading·Text 레이어를 Command+Shift로 다중 선택 → Styler 플러그인 → Generate Styles 실행. 웹 16개, iOS·Android 각 20개 스타일 생성.
    - **세부 주제:** 플러그인 실패 처리: 간헐적으로 스타일이 생성되지 않는 경우 발생(텍스트 Regular 웨이트 누락). Local Styles에서 + 버튼으로 수동 생성(web/text/L/regular: 16pt/24lh, M/regular: 14pt/20lh, S/regular: 12pt/16lh, XS/regular: 10pt/14lh).

*   **[스타일 정렬·할당 및 최종 확인]**

    - **세부 주제:** 스타일 순서 정렬: 생성 후 순서가 뒤섞이므로 Heading은 5XL→4XL→…→2XS, Text는 크기 내림차순 + Regular가 Semi Bold 위에 오도록 수동 재정렬.
    - **세부 주제:** 텍스트 스타일 할당: Styler가 스타일을 생성하면서 레이어에 자동 할당하지 못한 경우, 텍스트 선택 → 우측 패널 Styles → 스타일명(예: text/L/regular) 검색 후 수동 할당.

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*

---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 타이포그래피란 무엇인가**

    - 타이포그래피 = 글자를 배열하여 가독성(legible)·판독성(readable)·시각적 매력을 만드는 예술. 디자인 시스템에서 시각적 아이덴티티와 콘텐츠 계층 확립의 핵심.
    - FDS 폰트 패밀리: 웹 Inter, iOS SF Pro Display·SF Pro Text, Android Roboto. 웨이트: Regular·Semi Bold.

*   **[00:00:40] ~ 그룹·스케일·T셔츠 사이징 설명**

    - 그룹: Heading·Text (필요 시 Label·Link 추가 가능).
    - 스케일: 48→40→32→24→20→16pt (라인 높이: 56→48→40→32→28→24). 글로벌 4포인트 스케일 적용.
    - T셔츠 사이징(2xs~5xl): H1·H2 같은 역할명 대신 규모명 사용 → 여러 제품에서 "heading XL"을 각자의 H1로 활용 가능. 제품별 별도 Typography Set 불필요.

*   **[00:01:30] ~ 네이밍 컨벤션**

    - 명명 구조: `그룹/크기/웨이트` (예: `heading/L/semibold`, `text/L/regular`, `text/L/semibold`).
    - Heading은 Semi Bold만 먼저 시작, 이후 추가 웨이트 도입. 추후 Figma Typography 변수 업데이트 시 Family·Size·Line Height·Weight·Letter Spacing 변수 생성 예정.

*   **[00:02:00] ~ Styler 플러그인으로 스타일 생성**

    - 파일에 미리 테이블 형태로 레이어 준비(레이어명 = 스타일명, 값 적용 완료). 에피소드 2·3과 동일한 Styler 플러그인 방식 사용.
    - 웹 Heading·Text 레이어를 Command+Shift로 선택 → Styler → Generate Styles → 16개 생성. iOS 동일하게 실행 → 20개 생성. Android도 동일하게 20개 생성.
    - 생성 후 스타일 순서가 뒤섞임 → 각 플랫폼·그룹별로 크기 내림차순(5XL→…→2XS) 및 웨이트 순서(Regular→Semi Bold) 재정렬.

*   **[00:03:30] ~ 플러그인 실패 및 수동 스타일 생성**

    - 웹 Text 그룹의 Regular 웨이트 일부가 Styler 플러그인 오류로 생성되지 않음(플러그인은 항상 완벽하지 않음).
    - Local Styles → + 버튼으로 누락된 스타일 수동 생성:
      - `web/text/L/regular`: 16pt / 라인 높이 24
      - `web/text/M/regular`: 14pt / 라인 높이 20
      - `web/text/S/regular`: 12pt / 라인 높이 16
      - `web/text/XS/regular`: 10pt / 라인 높이 14
    - iOS·Android는 Styler가 정상 동작하여 추가 수동 작업 불필요.

*   **[00:05:00] ~ 스타일 할당 및 마무리**

    - Styler가 생성 시 자동 할당하지 못한 텍스트 레이어에는 우측 패널 Styles 검색으로 수동 할당(text/L/regular, text/M/regular, text/S/regular, text/XS/regular 순으로 적용).
    - 웹·iOS·Android 모두 Heading·Text 스타일 완성 확인.
    - 다음 에피소드 예고: Spacing.

*(이후 영상 끝까지 중요한 흐름이 바뀔 때마다 시간대별 요약 추가)*

---
