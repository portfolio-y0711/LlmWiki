---

## 📝 1. 영상 전체 요약

> Figma Design System 시리즈 11번째 에피소드로, FDS의 **첫 번째 컴포넌트인 Spinner**를 웹 컴포넌트 라이브러리에 생성하고 앱 라이브러리에 복사하는 전 과정을 다룬다. 크기(L/M/S) × 타입(primary/inverse/negative) 조합의 Variant를 구성하고, 시맨틱 컬러 변수를 활용해 다크 모드까지 지원하는 컴포넌트를 완성한다.



---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **도입 — 라이브러리 구조 설명 및 사전 준비**

    - **세부 주제:** FDS 컴포넌트 라이브러리 구조 — Web Library와 App Library 분리 운영 방식
    - **세부 주제:** 라이브러리 연결 확인 — Design Tokens Library와 Iconography Library를 Web Library에 연결하는 방법

*   **핵심 구조 — Spinner 컴포넌트 기본 형태 제작**

    - **세부 주제:** 48×48 프레임 생성 및 컴포넌트 명명 규칙 설정
    - **세부 주제:** Oval(타원)로 스피너 아크 그리기 — Fill 제거, `border-brand` 스트로크 변수(L=4px) 적용, 호(arc) 형태로 편집
    - **세부 주제:** 시맨틱 색상 변수를 활용한 primary / inverse / negative 타입 표현

*   **심화 활용 — Variant 세트 구성 (크기 × 타입)**

    - **세부 주제:** Size L(48px) · M(24px) · S(16px) 세 가지 크기 Variant 생성 방법
    - **세부 주제:** 각 크기에 맞는 스트로크 두께 조정 (L=4px, M=2px, S=1px) 및 내부 path 크기 일치시키기
    - **세부 주제:** Variant 복제(Option+Drag) 후 크기·속성 일괄 변경 워크플로우

*   **다중 라이브러리 배포 및 다크 모드 검증**

    - **세부 주제:** 완성된 컴포넌트를 App Library로 복사하는 방법 (보조 사각형 활용 정렬 기법)
    - **세부 주제:** 인스턴스 삽입 후 Figma 자동 흰색 Fill 제거 작업
    - **세부 주제:** Auto Layout 프레임에 시맨틱 다크 모드 적용해 primary / inverse / negative 동작 확인

*   **결론 — 정리 및 다음 에피소드 예고**

    - **세부 주제:** 다음 에피소드 예고: **Button Component** 제작

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*



---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 에피소드 소개 및 라이브러리 구조 설명**

    - FDS 시리즈 11번째 에피소드, 첫 번째 컴포넌트인 Spinner를 제작
    - FDS Components Web Library에서 제작 후 App Library로 복사하는 방식 설명
    - 일부 컴포넌트는 Web 전용, 일부는 App 전용으로 운영될 수 있음 (Button은 양쪽 모두)

*   **[00:01:00] ~ 라이브러리 연결 확인**

    - Assets 탭 → 라이브러리 아이콘에서 연결된 라이브러리 확인
    - **Design Tokens Library**와 **Iconography Library** 모두 Web Library에 연결 완료
    - 이를 통해 변수(토큰)와 아이콘을 Web Library 내에서 직접 사용 가능

*   **[00:02:00] ~ 컴포넌트 페이지 및 문서 영역 설정**

    - 컴포넌트 이름을 `spinner`로 변경
    - Assets → Design Tokens → tools 폴더에서 FDS Heading 드래그 삽입
    - 제목 텍스트를 "spinner"로 변경
    - [Component Gallery](https://component.gallery) 웹사이트에서 Spinner 설명 복사 → Shift+Option+Command+V로 스타일 없이 붙여넣기
    - 캔버스 너비를 1024로 확장

*   **[00:03:30] ~ 기본 프레임 및 컴포넌트 생성**

    - F 키로 48×48 프레임 생성, 이름을 `spinner`로 변경
    - 우클릭 → Create Component로 컴포넌트 전환
    - 캔버스에서 왼쪽·위쪽 여백 48px로 위치 정렬

*   **[00:04:30] ~ Spinner 아크(호) 시각 요소 제작**

    - O 키로 Oval(타원) 그리기 → **44×44**으로 설정 (Large 버전), 컴포넌트 중앙 정렬
    - Fill 제거, Stroke 추가:
        - 색상: `border-brand` 시맨틱 변수
        - 두께: Border Width 변수 `L = 4px`
        - 정렬: Inside → **Center**로 변경
    - Edit Object 모드 진입 → 호의 일부 구간(섹션) 탭하여 제거 → 원호(arc) 형태 완성
    - 시작·끝 포인트를 **Round**로 설정
    - 레이어 이름을 `spinner`로 변경

*   **[00:06:00] ~ Variant 생성 — 타입(primary / inverse / negative)**

    - 컴포넌트 전체 선택 → Add Variant로 복제
    - 첫 번째: `size=L`, 두 번째: `size=L`로 임시 설정
    - 속성명 추가: `type=primary` (기본), `type=inverse`(스트로크를 `border-inverse`로 변경), `type=negative`(추가)
    - 결과: Size L에 primary / inverse / negative 3가지 타입 Variant 완성

*   **[00:08:00] ~ Size Medium(M) Variant 생성**

    - Size L 3개 Variant를 Option+Drag로 복제 → 하단에 배치
    - 복제본의 size 속성을 `M`으로 변경
    - Layout → Constrain Properties에서 크기를 **24**로 변경 (프레임 리사이즈)
    - Command+Shift로 내부 path들 다중 선택 → 크기를 **22**로, 스트로크 두께를 **2**로 변경
    - 각 Variant가 프레임 내에서 1px 여백으로 배치되어 있는지 확인
    - Medium 사이즈 용도: Large 버튼의 로딩 상태에 사용될 예정

*   **[00:10:00] ~ Size Small(S) Variant 생성**

    - M Variant 3개를 다시 Option+Drag로 복제 → size를 `S`로 변경
    - 프레임 크기를 **16**으로 변경
    - 내부 path 크기를 **14**, 스트로크 두께를 **1**로 변경
    - 소형 버튼 로딩 상태에 사용될 예정
    - 컴포넌트 전체 선택 → Layout → **Resize to Fit**으로 컴포넌트 경계 조정
    - 캔버스 내 위치(텍스트 요소로부터 32px 간격) 최종 확인

*   **[00:12:00] ~ App Library로 컴포넌트 복사**

    - 레이어 패널에서 컴포넌트 + 헤딩 선택 → Copy
    - App Library 파일로 이동 → Paste
    - 정렬 기법: 임시 사각형(0, 0 위치)을 생성 후 컴포넌트를 드래그하여 정렬, 키보드 1로 화면 중앙 이동
    - 페이지 이름을 `spinner`로 변경

*   **[00:13:30] ~ 인스턴스 삽입 및 흰색 Fill 제거**

    - Web Library Assets에서 Spinner 컴포넌트 확인 → 인스턴스 삽입
    - Figma 자동 추가 흰색 Fill을 모든 Variant에서 제거 (Web + App 양쪽 모두)

*   **[00:14:30] ~ 다크 모드 동작 검증**

    - 인스턴스를 Group으로 감싼 뒤 Frame + Auto Layout + Padding(32) + Border Radius(8) 추가
    - 배경 Fill: `L1` 변수 적용
    - 프레임 이름을 `dark`로 지정, Appearance에서 시맨틱 컬러 모드를 **dark**로 변경
    - 결과 확인:
        - primary: 브랜드 색상 스피너
        - inverse: 흰색(다크 배경에서 보이지 않음 → 의도된 동작)
        - negative: 반전 색상

*   **[00:15:30] ~ 마무리 및 다음 에피소드 예고**

    - 테스트 인스턴스 삭제, 키보드 1로 중앙 정렬 후 완성
    - 다음 에피소드 예고: **Button Component** 제작

---
