## 📝 1. 영상 전체 요약

> FDS 시리즈 2화로, Primitive 색상(브랜드 포함 13가지 Hue)을 9단계 Tint/Shade 스케일로 확장하고 플러그인(Color Tint & Shade Generator → Styler → Styles to Variables)을 활용해 Figma 변수 컬렉션 "Primitives"를 효율적으로 생성한 뒤, 디자이너에게는 숨기고 Semantic 변수에서만 참조하도록 설정하는 전체 워크플로우를 다룬다.

---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **[Primitive 색상의 개념 및 팔레트 설계]**

    - **세부 주제:** Primitive 색상이란: 디자인 시스템의 기본 색상 팔레트를 이루는 베이스 Hue. FDS는 Brand·Blue·Purple·Violet·Red·Pink·Orange·Yellow·Green·Teal·Cyan·Black·White 총 13종 사용.
    - **세부 주제:** 브랜드 색상 선정과 팔레트 조화: 브랜드 컬러(주 Accent 색)를 기준으로, 나머지 색상은 Hue·Saturation·Lightness 값을 조정해 색조적으로 통일감 있는 세트 구성.

*   **[9단계 Tint/Shade 스케일 생성]**

    - **세부 주제:** Tint vs. Shade 개념: Tint는 기본 색의 Lightness를 높여 밝게, Shade는 낮춰 어둡게 만드는 방식. 각 색상에 100~900 9단계 스케일 적용.
    - **세부 주제:** 수동 방식 vs. 플러그인: 수동으로 흰색·검정을 20/40/60/80% 오버레이 후 플래트닝·컬러 피킹하는 방법이 있으나 비효율적. "Color Tint & Shade Generator" 플러그인을 사용하면 Hex 값 입력만으로 동일 결과 자동 생성.
    - **세부 주제:** Neutral 스케일 처리: Black 기반 19단계 Neutral은 스타터 파일의 사전 플래트닝된 값(00~F2 범위)을 그대로 사용. 생성된 스케일들과 함께 그룹화.

*   **[네이밍 컨벤션과 레이어 정리]**

    - **세부 주제:** 네이밍 규칙: "color/shade값" 형식 사용 (예: blue/500, pink/100). Figma의 Rename Selected Layers 기능으로 색상명(brand, blue 등)과 단계값(100~900)을 일괄 적용.
    - **세부 주제:** 레이어 순서 정리: "Reverse Layer Order" 플러그인으로 각 색상 세트의 레이어 순서를 100→900 방향으로 역정렬. Brand가 최상단, Neutral이 최하단에 오도록 배치.

*   **[Figma 변수 컬렉션 "Primitives" 생성]**

    - **세부 주제:** 스타일→변수 변환 2단계 플러그인 워크플로우: ① "Styler" 플러그인으로 모든 색상 프레임을 Color Style로 일괄 생성 → ② "Styles to Variables" 플러그인으로 118개 Color Style을 "Primitives" 컬렉션 변수로 일괄 변환. 이후 기존 Color Style은 삭제.
    - **세부 주제:** Primitive 변수 숨기기: 디자이너에게 Primitive 변수를 직접 노출하지 않기 위해 Variables 패널에서 전체 선택 → Edit Variables → "Hide from Publishing" 설정. Semantic 변수에서만 참조하게 하여 색상 적용의 확장성과 라이트/다크 모드 전환을 지원.

*   **[문서화: Variable Color Style Guide 플러그인 활용]**

    - **세부 주제:** 색상 스와치 자동 생성: "Variable Color Style Guide" 플러그인으로 Primitives 컬렉션의 스와치 페이지 자동 생성. 변수명·Hex값·RGBA·HSL 정보 표시.
    - **세부 주제:** 스와치 컴포넌트 커스터마이즈: 색상 칩 크기(32×32), Border Radius(4), 카드 너비(704), Auto Layout 방향(Horizontal), 패딩(상하 8) 등을 조정해 라이브러리 내 문서 스타일과 일치시킴.

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*

---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 도입: Primitive 색상의 정의와 FDS 팔레트**

    - Primitive 색상 = 디자인 시스템의 기반이 되는 베이스 Hue. FDS는 Brand·Blue·Purple·Violet·Red·Pink·Orange·Yellow·Green·Teal·Cyan·Black·White 13종.
    - 브랜드 컬러(Brand Blue)를 기준으로 HSL 값을 조정해 나머지 색상들과 색조 통일감 유지.

*   **[00:00:40] ~ 9단계 Tint/Shade 스케일 생성**

    - Tint(Lightness 증가)와 Shade(Lightness 감소)로 9단계 스케일 구성. 수동 방법(흰·검 오버레이 → 플래트닝 → 컬러 피킹)은 번거로움.
    - "Color Tint & Shade Generator" 플러그인 사용: 색상 선택 → Hex 값 입력 → Generate로 자동 생성. Brand, Blue 등 각 색상별로 반복 실행.
    - Neutral(Black 기반 19단계): 스타터 파일의 사전 처리된 값 활용. 생성된 스케일 전체를 선택해 간격(32) 조정으로 정렬.

*   **[00:02:00] ~ 네이밍과 레이어 순서 정리**

    - 네이밍 컨벤션: "color/shade" 형식 (blue/500, pink/100 등). Rename Selected Layers 기능으로 색상명 + 단계값(100~900) 일괄 적용.
    - "Reverse Layer Order" 플러그인으로 각 스케일의 레이어를 100→900 순으로 재정렬. Brand 최상단, Neutral 최하단 배치.

*   **[00:03:30] ~ Figma 변수 생성: Styler + Styles to Variables 플러그인**

    - 모든 색상 프레임 선택 → Styler 플러그인 "Generate Styles" 실행 → 모든 색상이 Color Style로 생성(Blue, Purple, Violet, Red, Pink, Orange, Yellow, Green, Teal, Cyan, Neutral 순 재정렬).
    - "Styles to Variables" 플러그인 실행: 118개 Color Style을 컬렉션명 "Primitives"로 변환. Variables 패널에서 생성 확인 후 기존 Color Style 전체 삭제.
    - 전체 변수 선택 → Edit Variables → "Hide from Publishing": Primitive는 내부 참조용으로만 사용, 디자이너에게 직접 노출 차단. 이로써 Semantic 변수 기반 색상 적용 및 라이트/다크 모드 네이티브 전환 지원.

*   **[00:05:00] ~ 문서화: Variable Color Style Guide 플러그인**

    - "Variable Color Style Guide" 플러그인 → Primitives 컬렉션 선택 → Create Swatches로 스와치 페이지 자동 생성. 변수명·Hex·RGBA·HSL 표시 확인.
    - 스와치 컴포넌트 커스터마이즈: 색상 칩 32×32, Border Radius 4, 카드 너비 704, Auto Layout Horizontal, 상하 패딩 8, 테두리 제거, 텍스트 레이어 Auto Width 설정.
    - 인덱스 너비 조정, Auto Layout Fill Container 적용으로 전체 정렬 통일. 문서 표기를 "Brand Primitives → B Primitives"로 수정해 마무리.

*   **[00:07:00] ~ 마무리 및 다음 예고**

    - Primitive 색상 변수 생성 완료. 다음 에피소드에서는 Semantic 색상 변수 생성 예정.

*(이후 영상 끝까지 중요한 흐름이 바뀔 때마다 시간대별 요약 추가)*

---
