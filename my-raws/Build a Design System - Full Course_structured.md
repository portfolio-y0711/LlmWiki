---

## 📝 1. 영상 전체 요약

> Figma 변수(Variables)를 활용한 3계층 디자인 토큰 아키텍처(브랜드 → 별칭 → 맵)를 기반으로, 버튼·입력 필드·체크박스·테이블 등 필수 UI 컴포넌트를 체계적으로 구축하고 라이브러리로 퍼블리시하는 전체 과정을 안내하는 풀 코스 영상. 단순 컴포넌트 제작을 넘어, 다크모드·멀티브랜드·반응형 타입 스케일까지 실무 수준의 설계 원칙을 다룬다.

---

## 📖 2. 영상 주요 주제 (추상화된 목차)

* **[디자인 토큰 기초 및 아키텍처 설계]**

    - **세부 주제:** 2계층(Primitive/Semantic) vs 3계층(Brand/Alias/Map) 방식 비교 및 3계층 채택 이유
    - **세부 주제:** 브랜드 컬렉션 — 색상 스케일(100단위 네이밍), 폰트 패밀리/웨이트 변수, 4px 기반 수치 스케일 구성
    - **세부 주제:** 별칭 컬렉션 — 역할 지정(Primary, Error, Success, Warning, Neutral 등), 보더 Width/Radius 변수화
    - **세부 주제:** 멀티브랜드 처리 — Branded House vs House of Brands 전략 및 Mode 전환 방식
    - **세부 주제:** 맵 컬렉션 — Text, Icon, Surface, Border 변수 정의 및 라이트/다크 모드 전환 세팅

* **[반응형 타입 시스템 구축]**

    - **세부 주제:** typescale.io를 활용한 데스크탑/모바일 폰트 스케일 산출 및 4px 그리드 근사치 적용
    - **세부 주제:** 반응형 컬렉션 — H1~H6, Paragraph(XS/S/M/L) 폰트 사이즈·라인높이·단락 간격 변수화
    - **세부 주제:** Figma 텍스트 스타일 생성 — 변수 바인딩 방식으로 H1~H6 및 Body(Regular/Semibold/Link) 스타일 등록

* **[핵심 UI 컴포넌트 구축]**

    - **세부 주제:** 버튼 컴포넌트 — Variant(Default/Hover/Focus/Disabled), Type(Filled/Outline/Transparent), Props(Icon Left/Right, Label)
    - **세부 주제:** 라벨·인풋·필드 컴포넌트 — 분리 설계 원칙, 중첩 인스턴스(Nested Instances), 힌트텍스트 레이어 속성
    - **세부 주제:** 체크박스·라디오버튼·스위치 — Selected/Unselected Type 변수, Focus 링 절대 위치 배치, Constraints 설정
    - **세부 주제:** 텍스트 에어리어 — 멀티라인 특성에 따른 아이콘 구성 제거 이유, 기존 Field 컴포넌트 재활용 전략

* **[복합 컴포넌트 및 심화 패턴]**

    - **세부 주제:** 메뉴·탭바·버튼그룹 — 선택 상태(Selected/Unselected) 처리, 스크롤바 서브컴포넌트 구성
    - **세부 주제:** 아바타·배지·태그·로더·진행바(Progress Bar/Circle) — 사이즈 변형 및 Scale 제약 조건 활용
    - **세부 주제:** 스낵바·캐러셀 — 아톰 컴포넌트 조합 방식(Atomic Design), 진행바 내장 및 방향(Left/Right) Variant
    - **세부 주제:** 테이블 컴포넌트 — 컬럼/로우 방식, Adjust Gap 트릭을 통한 컴포넌트 분리 없이 너비 조정

* **[라이브러리 퍼블리시 및 운영]**

    - **세부 주제:** 디자인 시스템 퍼블리시 절차 — Figma 팀 스페이스에서 라이브러리 공개 및 구독 방법
    - **세부 주제:** 업데이트 관리 — 변경된 컴포넌트만 선별 재퍼블리시하는 워크플로우 소개

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*

---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 디자인 토큰 아키텍처 개요**

    - UI Collective의 3계층 접근법(Brand → Alias → Map) 소개. 타 크리에이터들이 잘못 변형하는 사례를 언급하며 올바른 구조의 중요성 강조
    - 브랜드 컬렉션 = "나무의 뿌리" — 아직 역할 없이 순수 값(Hex 코드, 수치)만 저장하는 계층
    - 2계층(Primitive/Semantic) vs 3계층 비교. 멀티브랜드 사용 시 2계층의 한계 설명

*   **[브랜드 컬렉션 구축] ~ 색상·폰트·스케일 변수 생성**

    - 색상 스케일 제작 방법 — 핵심 브랜드 컬러에 불투명도 조정 후 색상 매칭으로 Hex 값 추출. Purple/Red/Green/Gray/Orange/Blue 6개 스케일 생성
    - 100단위 네이밍 규칙 — 20% 간격이면 100, 10% 간격이면 50으로 스케일 번호 부여하는 원칙 설명
    - 폰트 패밀리(String 변수), 폰트 웨이트(Regular/Medium/Semibold/Bold) 변수 생성 및 Figma 연결 확인
    - 4px 배수 기반 수치 스케일(100=4, 200=8, …800=32, +25=1, +50=2) 구성, 실무 활용 사례(Border Radius, Border Width) 안내

*   **[별칭(Alias) 컬렉션 구축] ~ 역할 지정 및 멀티브랜드**

    - 별칭 컬렉션 = "나무의 줄기" — 브랜드 스케일에 Primary/Error/Success/Warning/Neutral/Information 역할 부여
    - Border Width(none/small/medium/large), Border Radius(none/small/medium/large) 변수 추가
    - Branded House(주요 색상만 다름)와 House of Brands(완전히 다른 브랜드) 개념 비교
    - Branded House 멀티브랜드: Alias 컬렉션에 Mode 추가 후 Primary 색상만 교체하는 방식 실습
    - Foundation White/Black 변수 처리 및 Neutral 그룹 내 white/black 보관 팁

*   **[맵(Map) 컬렉션 구축] ~ 컴포넌트 적용 변수 정의**

    - 맵 컬렉션 = "나무의 잎" — 실제 컴포넌트에 적용되는 최종 변수(Text/Icon/Surface/Border)
    - Text 변수: Headings(neutral-800), Body(neutral-700), Action/Action Hover/Disabled, 상태별(Info/Warning/Success/Error), On-Action
    - Icon 변수: Text와 동일 구조로 복사 (일관성 유지), Default(neutral-700) 추가
    - Surface 변수: Page(white), Default, Action/Action Hover, 상태별(Success/Warning/Error/Info, 각 50레벨), Disabled
    - Border 변수: Default, Action/Action Hover/Disabled/Focus, 상태별(Success/Warning/Error/Info, 각 200레벨)
    - 다크 모드 설정 — Map 컬렉션에 Dark Mode 추가, 색상 반전 원칙. Primary 등 고정 색상에 'default-fixed' 표기 규칙

*   **[반응형 컬렉션 구축] ~ 타입 스케일 및 텍스트 스타일**

    - typescale.io 도구로 Major Third 스케일(기준 16px) 선택, 데스크탑/모바일 두 가지 캡처
    - 4px 근사치 적용: H1=60, H2=48, H3=40, H4=32, H5=24, H6=20 (데스크탑); H1=48, H2=40, H3=32 ~ (모바일)
    - 라인 높이 = 폰트 사이즈 × 1.2 후 4px 근사치. Paragraph 스페이싱은 브랜드 취향에 따라 자유롭게 설정
    - 폰트 사이즈 Number 변수로 생성 후 Figma 텍스트 스타일(H1~H6, Body XS/S/M/L, 각 Regular/Semibold/Link)에 변수 바인딩
    - Variable Scope 설정(color scoping) — 컴포넌트에 변수 적용 시 관련 없는 변수 숨김 처리

*   **[버튼 컴포넌트] ~ 핵심 컴포넌트 구축 시작**

    - Shift+A로 Auto Layout 추가, Surface Action + Text On-Action + Icon On-Action 변수 적용
    - Properties 추가: Icon Left(Layer+Instance Swap), Icon Right(Layer+Instance Swap), Label(Text)
    - Variant 구성: Status(Default/Hover/Focus/Disabled) × Type(Filled/Outline/Transparent)
    - Focus 링 구현 — 절대 위치 배치, 외부 2px Border, Constraints Left-Right-Top-Bottom 고정
    - Disabled 처리 — Surface/Border/Text/Icon Disabled 변수 적용, 적절한 시인성 조정

*   **[라벨·필드·인풋 컴포넌트] ~ 중첩 컴포넌트 설계 원칙**

    - 라벨 컴포넌트 분리 이유 — 다른 컴포넌트(Input, TextArea 등)에서 재사용 가능, Required 변수(*표시 절대 위치 배치)
    - 필드 컴포넌트 — Placeholder 항상 Fill 처리로 아이콘 우측 고정, Border Width 변수 적용
    - 인풋 컴포넌트 — 라벨+필드 조합, Nested Instances로 하위 속성 노출, Hint Text(Explainer Text) 레이어 속성 추가
    - 상태(filled/not-filled) 구분 — text-placeholder 변수로 미입력 시 시각적 차별화

*   **[메뉴·체크박스·라디오버튼·스위치] ~ 선택 상태 컴포넌트**

    - 메뉴 컴포넌트 — dot 접두사로 퍼블리시 방지, 스크롤바 서브컴포넌트 구성, Nested Instances 활성화
    - 체크박스 — Status(Default/Hover/Focus/Disabled) × Type(Selected/Unselected), Focus 링 절대위치, Error 상태 선택 추가
    - 라디오버튼 — 타원 중첩 구조, Constraints 설정, 체크박스와 동일 Variant 패턴
    - 스위치 — Knob 위치(좌=unselected, 우=selected) 변환, Selected/Unselected Type 추가, 레이블 노출 여부 Layer Property

*   **[텍스트 에어리어·탭바·버튼그룹·링크·브레드크럼] ~ 복합 입력 및 내비게이션 컴포넌트**

    - 텍스트 에어리어 — 기존 필드 재활용, 아이콘 Left 제거(멀티라인에서 공백 이슈), Character Count/Hint Copy 옵션
    - 탭바 — Tab Item(Unselected/Selected) 하단 2px Border로 선택 표시, 전체 탭바 하단 border-default 추가
    - 버튼그룹 — 우측 Border만 적용(clip content 활용), Default/Hover/Selected/Disabled Variant
    - 링크 컴포넌트 — Basic/Inline Type 제공, Breadcrumb에 재사용(Chevron Right 아이콘, 마지막 항목 Inline 처리)

*   **[아바타·배지·태그·로더·진행바] ~ 피드백 및 상태 표시 컴포넌트**

    - 아바타 — Size(Large 64/Medium 48/Small 32) × Type(Icon/Image/Initials), Clip Content 활용, Avatar Group(-4px gap), Avatar Label
    - 배지 — 고정 24×24 크기, Default/Error/Success/Warning/Info 상태, Dot 타입(12×12)
    - 태그 — Interactive Tag, Selected/Unselected Type, Focus/Disabled Variant
    - 로더 — 4개 원 회전 애니메이션(200ms 딜레이 Variant), Small/Medium/Large 사이즈(Scale 제약 활용)
    - 진행바 — Adjust Gap 트릭(0×0 ellipse 두 개의 gap 조절로 컴포넌트 유지하면서 진행률 변경)
    - Progress Circle — 타원 중첩 구조, Scale+Scale 제약으로 사이즈 변형 지원

*   **[스낵바·캐러셀·버튼아이콘·테이블] ~ 고급 컴포넌트**

    - 스낵바 — 아이콘+타이틀+본문+링크+닫기 버튼+진행바 조합, Default/Success/Error/Warning/Info Variant
    - 캐러셀 — Left/Right 방향 Variant, Carousel Bar(배경)+Carousel Progress(진행 표시) 중첩 구성, Scale 제약 적용
    - 버튼아이콘 — 기존 버튼 컴포넌트 재활용, 라벨·아이콘Right 제거 후 정사각형(36×36) 고정
    - 테이블 — Cell Item(Copy/Link/Action Type) → Column/Row 컴포넌트 → 최종 Table; Adjust Gap으로 컬럼 너비 조정; Column/Row Type 전환 지원

*   **[디자인 시스템 퍼블리시] ~ 라이브러리 배포 및 관리**

    - Figma 팀 스페이스 필요 조건 안내, 드롭다운 → Publish Library 절차
    - 변경된 컴포넌트만 선별 재퍼블리시 가능한 업데이트 관리 워크플로우
    - 다른 파일에서 Teams/UI Kits 탭을 통해 구독(Subscribe) 방법 설명
    - dot 접두사 컴포넌트 퍼블리시 제외 확인 및 불필요 컴포넌트 unpublish 방법

---
