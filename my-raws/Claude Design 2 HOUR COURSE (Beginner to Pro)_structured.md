## 📝 1. 영상 전체 요약

> Claude Design(Opus 4.7 구동, 별도 주간 쿼터)을 완전히 처음부터 배우는 2시간짜리 마스터클래스로, 브랜드 아이디어 → 디자인 시스템 → 피치덱·랜딩페이지·모바일 앱 프로토타입·런치 비디오를 한 흐름으로 빌드하고, Hyperframes·Kling/SeeDance·ChatGPT Image 2.0·Claude Code→GitHub→Vercel 배포 파이프라인과 세션 토큰을 아끼는 실전 전략까지 모두 다룬다.

---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **[Claude Design 이해: 제품 개요와 사용 환경 설정]**

    - **세부 주제:** Claude Design의 정체: 별도 앱(Claude Chat·Claude Code와 구분), Anthropic Labs 제품. Figma 킬러로 불리며 웹사이트·슬라이드·프로토타입·애니메이션·비디오 제작 지원. Opus 4.7(최고 비전 모델) 구동, verify agent가 빌드 결과물을 시각적으로 검증.
    - **세부 주제:** 유료 플랜 필수 + 주간 별도 쿼터: Pro/Max/Team/Enterprise만 사용 가능. Claude 일반 사용량과 완전히 분리된 주간 리셋 Claude Design 쿼터 존재. 플랜이 높을수록 할당량 증가. 초과 시 추가 크레딧으로 구매 가능.
    - **세부 주제:** Claude Design의 기본 인터페이스: 왼쪽 채팅 패널(파일 첨부·피드백), 오른쪽 미리보기. 프로젝트 유형: Prototype(Wireframe/High-Fidelity), Slide Deck, From Template(Animation 등). Design Files 탭에서 에셋·프리뷰·문서 확인 및 ZIP·PDF·HTML 내보내기 가능.

*   **[디자인 시스템: 가장 먼저 해야 할 일]**

    - **세부 주제:** 디자인 시스템이 핵심인 이유: 앞으로 만드는 모든 것(영상, 랜딩페이지, 슬라이드 등)에 동일한 색상·폰트·로고·버튼 스타일이 자동 적용됨. 팀 플랜에서 팀 전체 공유 가능. 한 번만 만들고 반복 사용.
    - **세부 주제:** 기존 브랜드 vs 처음 시작: 기존 브랜드는 GitHub 레포·웹사이트 URL·로고를 입력하면 자동 스크래핑. 처음 시작하는 경우 색상·폰트·무드를 먼저 결정해야 함 → 본 영상에서는 Claude 일반 채팅에서 브랜드 아이디어 먼저 구체화 후 진행.
    - **세부 주제:** 디자인 시스템 구성 요소: 브랜드 마크·워드마크·태그라인, 색상 팔레트(Primary·Accent·Neutral), 타이포그래피(Primary/Secondary 폰트), 버튼·카드·배지·아이콘 컴포넌트, 스페이싱·레이아웃 규칙. 이 모든 것이 편집 가능한 마크다운으로 저장.

*   **[브랜드 아이디어 도출: Claude 일반 채팅과 ChatGPT Image 2.0 활용]**

    - **세부 주제:** 브레인스토밍은 반드시 일반 Claude에서: Claude Design은 쿼터가 별도이므로 아이디어 도출·시장 조사·피치덱 개요·앱 스펙 작성은 일반 Claude 채팅에서 수행. "아이디어가 완성되고 빌드할 준비가 됐을 때만 Claude Design 사용"이 핵심 원칙.
    - **세부 주제:** Tally 브랜드 완성 과정: Claude와 채팅으로 회사명·미션·포지셔닝·페르소나·색상 팔레트·폰트·로고 개념까지 완성. 좋아하는 콘셉트를 선택해 브랜드 개념 마크다운 파일로 저장 → Claude Design 입력값으로 활용.
    - **세부 주제:** ChatGPT Image 2.0 활용법: 브랜드 가이드라인 PDF 제작에 유용. 색상·로고·타이포그래피 정보를 텍스트와 이미지로 주면 1페이저 브랜드 가이드라인 생성. 폰트를 완벽히 재현하지 못하는 경우 Canva에서 최종 수정. 2분 이내 완성.

*   **[주요 빌드 실습: 피치덱·랜딩페이지·모바일 앱·런치 비디오]**

    - **세부 주제:** 피치덱 빌드: 디자인 시스템 + 브랜드 콘셉트 마크다운 + Claude로 작성한 시장 조사 개요 → 슬라이드 자동 생성. Verify Agent가 각 슬라이드를 시각적으로 검증·수정. 완성 후 Tweaks 패널에서 커버·배경 텍스처(Warm Haze 추천)·액센트 색상·슬라이드 크롬 등 비코딩 조정 가능.
    - **세부 주제:** 랜딩페이지 빌드: Kling AI로 로고 드로잉 애니메이션(MP4) 제작 → Claude Design에 업로드. Sketch로 영웅 섹션 레이아웃(비디오 우측, 텍스트 좌측)을 미리 정렬 → 원샷 프롬프트로 배경색 매칭·내비게이션·섹션별 색상 변환 구현. 워터마크·눈금 숫자 등 Tweaks로 브랜드 감성 추가.
    - **세부 주제:** 모바일 앱 프로토타입: 일반 Claude에서 804줄짜리 앱 스펙 생성 → Claude Design에 붙여넣기. 전체 화면 캔버스에 iOS 프레임별 UI 자동 배치, 인터랙티브 버튼·다크/라이트 모드·온보딩 플로우 구현. Tweaks로 Accent 강도·카드 스타일(Lifted 추천)·배경 텍스처 조정.
    - **세부 주제:** 런치 비디오 (Hyperframes): Animation 템플릿 + Tally 디자인 시스템 + Hyperframes 마크다운 스킬 → 25초 애니메이션 비디오 자동 생성. 초안이 밋밋하면 "스토리텔링·더 많은 모션 그래픽" 요청으로 개선. Hyperframes 카탈로그에서 앱 쇼케이스 등 컴포넌트 URL을 직접 붙여넣어 새 씬 추가 가능. 완성 후 화면 녹화 또는 Claude Code에서 MP4 렌더링.

*   **[배포 파이프라인: Claude Design → Claude Code → GitHub → Vercel]**

    - **세부 주제:** 내보내기 방법: ① "Hand off to Claude Code" 명령(원클릭 연동, 간혹 404 버그) ② ZIP 파일 직접 다운로드 → 로컬 폴더에 압축 해제 → Claude Code로 열기.
    - **세부 주제:** GitHub 연동: Claude Code에서 "push to private GitHub repo" 요청 → 자동 레포 생성. index.html 루트 파일명 문제 등 404 오류 시 Claude Code가 원인 파악 및 수정 커밋 처리.
    - **세부 주제:** Vercel 배포: Vercel 계정 + GitHub 연동 → 레포 Import → Deploy 클릭 → 60초 이내 실제 도메인 생성. 이후 로컬에서 변경 → Claude Code가 GitHub push → Vercel 자동 재배포. 커스텀 도메인 연결도 Claude Code와 채팅으로 처리.
    - **세부 주제:** 모바일 반응형 주의: Claude Design은 데스크톱 기준으로 생성 → 배포 전 F12 개발자 콘솔에서 모바일 뷰 확인 필수. Claude Code에서 모바일 최적화 요청으로 보완.

*   **[토큰 관리 전략과 모범 사례]**

    - **세부 주제:** 가장 빠르게 쿼터를 태우는 행동: ① 모든 작업에 Opus 4.7 사용 ② 준비 없이 Claude Design에서 브레인스토밍 ③ URL/GitHub 레포 없이 복잡한 디자인 시스템 생성 ④ 긴 스레드에서 계속 대화.
    - **세부 주제:** 모델별 단계 활용(Model by Stage): 초기 기획·디자인 시스템 생성 → Opus 4.7. 이후 작은 반복·텍스트 수정 → Sonnet 4.6 또는 Haiku. 브랜드 스타일이 명확해지면 대부분 Sonnet으로 충분.
    - **세부 주제:** 4가지 복합 전략: ①Reference, don't describe (구체적 스크린샷·링크 첨부). ②Don't use defaults (AI 슬롭 방지 → 직접 디자인 시스템·카피 제공). ③Design system first (하나만, 잘 만들어서 팀 공유). ④Iterate in chunks (한 번에 여러 변경 요청 금지, 변경 하나씩 집중).
    - **세부 주제:** Tweaks 패널 적극 활용: 프롬프트 없이 색상·폰트·레이아웃·텍스처를 실시간으로 슬라이더/토글로 탐색 → 마음에 들지 않으면 되돌리기. Claude Code와 달리 되돌리기 비용 없음 → 쿼터 절약 핵심.
    - **세부 주제:** 기타 절약 팁: ① 긴 스레드는 ZIP 내보내기 후 새 세션에서 재시작. ② /clear 명령으로 컨텍스트 정리 시도. ③ 업로드 파일 크기 제한(약 30~40MB). ④ Claude Design이 한계에 도달하면 ZIP → Claude Code로 이동해 계속 작업.

*   **[영감 자원 및 Claude Design 한계]**

    - **세부 주제:** 영감 사이트: motionsites.ai(배경 애니메이션·사이트 프롬프트 복사), godly.website(무한 스크롤 갤러리), 21st.dev(개별 컴포넌트+프롬프트), Hyperframes 카탈로그(전환 효과·앱 쇼케이스·알림 UI). Claude Design이 웹 검색·GitHub 레포 fetch 가능 → URL만 붙여넣어도 컴포넌트 적용.
    - **세부 주제:** 주요 한계: 로고 이미지 재해석 문제(아이콘 기반 로고 변형됨 → 텍스트 기반 로고는 안전). 그리기(Draw) 기능 버그. 복잡한 그라디언트 전환 부정확. 모바일 자동 최적화 미지원. 런치 비디오 MP4 네이티브 내보내기 미지원(화면 녹화 또는 Claude Code 렌더링 필요). 연구 프리뷰 단계로 버그 잦음.

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*

---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 소개: 영상 구성 및 학습 목표**

    - Claude Design을 완전 초보자(한 번도 사용 안 한 사람)부터 전문가 수준까지 가르치는 마스터클래스. 다루는 범위: 브랜드 아이디어 → 디자인 시스템 → 피치덱 → 랜딩페이지 → 모바일 앱 → 런치 비디오. 세션 한도를 효율적으로 쓰는 방법 포함.
    - 영상 세 파트 구성: ①Foundations(Claude Design 개요·셋업), ②Builds(실제 브랜드 구축 라이브), ③Best Practices(최대 효율 방법론 + What Comes Next).

*   **[00:03:00] ~ Claude Design 개요: 제품 설명 및 Opus 4.7**

    - Claude Design = Anthropic 생태계 내 별도 앱. Figma 킬러로 불림. 웹사이트·슬라이드·프로토타입·애니메이션 생성 지원. Opus 4.7(최고 비전 모델) 탑재 → 빌드 결과를 시각적으로 검증(Verify Agent).
    - Krieger(전 Figma 이사)가 Anthropic CPO로 이동한 직후 Claude Design 출시라는 흥미로운 맥락. 별도 주간 쿼터이므로 낭비 없이 사용하는 전략 필요.

*   **[00:07:00] ~ 셋업: 유료 플랜 필수 및 사용량 확인**

    - Pro·Max·Team·Enterprise 사용자만 이용 가능. 무료 플랜 불가. 플랜이 높을수록 주간 Claude Design 할당량 증가(월 $200 Max 20X 플랜 기준으로 데모 진행).
    - 인터페이스 구성: 신규 프로젝트(Prototype/Slide Deck/Template), 기존 디자인 시스템 목록, 예제 갤러리(Organic Loaders·Globe·Text Streaming 등 영감용 프롬프트 제공).

*   **[00:10:00] ~ 디자인 시스템 생성: 가장 중요한 첫 번째 단계**

    - 디자인 시스템이 왜 먼저인가: 이 파일 하나로 이후 모든 빌드가 브랜드 색상·폰트·로고·컴포넌트를 자동 참조 → 반복 지시 불필요. 팀 전체 공유 가능.
    - 기존 브랜드 경우: 웹사이트 URL + GitHub 레포 + 로고 입력으로 자동 스크래핑 → 디자인 시스템 생성. 주의: URL 없이 레포만 주면 더 많은 토큰 소모.
    - 비용: AI Automation Society 디자인 시스템 구축에 약 6%의 쿼터 소모(완성 후 10% 사용 상태). 입력 자료가 많을수록 토큰 더 소모.

*   **[00:15:00] ~ 브랜드 아이디어 도출: 일반 Claude 채팅 활용**

    - "Claude Design에서는 절대 브레인스토밍 금지" 원칙. 일반 Claude 채팅에서 회사 콘셉트·미션·타겟·색상·폰트·로고 시안까지 완성 후 마크다운으로 저장.
    - Tally 브랜드 구축 과정: Claude와 채팅으로 핀테크 앱 "Tally" 콘셉트(월간 재정 소화 다이제스트, $8/월 단일 요금) 완성. 색상 팔레트(Bone·Navy·Green Signal·Amber), 폰트(Berkeley Mono·Inter) 선정.
    - ChatGPT Image 2.0으로 로고 시안 생성(아이콘형 vs 텍스트형) → 마음에 드는 하이브리드 선택. 이후 상세 타이포그래피 레이아웃 요청으로 "미니 브랜드 가이드라인" 형태 시각화.

*   **[00:25:00] ~ Tally 디자인 시스템 구축 및 피드백**

    - Claude Design "Create New Design System"에서 회사명·미션 블러브·로고 PNG·브랜드 콘셉트 마크다운 파일 업로드. 로고 변형 문제(Claude Design이 아이콘 로고를 재해석하는 버그) 발견 → "원본 PNG 그대로 유지" 피드백 반복.
    - 완성된 디자인 시스템: 브랜드 마크·타이포그래피·색상 팔레트·버튼·카드·배지·입력 필드·아이콘 컴포넌트. Verify Agent가 레이아웃 검증 완료. 랜딩페이지 목업 미리보기도 포함.

*   **[00:38:00] ~ ChatGPT Image 2.0: 브랜드 가이드라인 1페이저 제작**

    - Claude Design에서 브랜드 가이드라인 텍스트 추출(로고 규칙·색상 코드·타이포그래피·스페이싱·UI 아이콘) → ChatGPT "Create Image"에 텍스트 + 로고 2종 붙여넣기 → 세로형 브랜드 가이드라인 생성.
    - 결과: "Don't recolor, Don't remove the period" 규칙·색상 매핑·Berkeley Mono 타이포그래피 등 포함. 폰트가 약간 어긋나면 Canva에서 최종 보정. 내부 참조 또는 외부 디자이너 공유용으로 유용.

*   **[00:45:00] ~ 피치덱 빌드**

    - 일반 Claude에서 시장 조사 + 피치덱 구조 마크다운(372줄) 생성 → Claude Design Slide Deck에 Tally 디자인 시스템 + 브랜드 콘셉트 마크다운 + 시장 조사 개요 입력.
    - 결과: Navy 배경, Tally 로고, 투자자 설득 흐름(문제→솔루션→시장 갭→GTM 전략→팀→재무 목표). 자동 Verify Agent가 슬라이드 6·10 수정. 사용량 32% 도달.
    - Tweaks 탐색: Cover Bold Mark, 배경 Warm Haze(그린·오렌지 그라디언트), Accent Vivid Green 선택. Slide Chrome Default 유지. 트윅으로 구현한 변경은 "이걸 촉구했을까?" 생각이 안 나는 결과까지 도출.

*   **[01:00:00] ~ 와이어프레임 실험 및 평가**

    - 랜딩페이지용 와이어프레임 3종(Mid-Fi, 라이트 2종+다크 1종) 생성 → 사용량 7% 추가 소모. 결론: "단순 랜딩페이지에는 와이어프레임이 낭비". 유용한 경우: 멀티페이지 퍼널 시각화, 모바일 앱 레이아웃 계획, 로고·패키징 아이디어.
    - 와이어프레임 결과물: 3가지 스타일(Honest Mirror·Receipt Ledger·Quiet Night) 제안. 페르소나별 적합 웹사이트 자동 분류. 완성 후 HTML 내보내기 가능.

*   **[01:08:00] ~ 랜딩페이지 빌드: 배경 비디오 애니메이션 포함**

    - Kling AI로 Tally 로고 드로잉 애니메이션 MP4 제작(시작 프레임: 빈 Bone 배경 → 종료 프레임: 로고) → Claude Design에 업로드.
    - Sketch로 영웅 섹션 레이아웃 사전 정렬(왼쪽: 텍스트, 오른쪽: 비디오, 상단: 내비게이션). 원샷 프롬프트: 배경색 Bone 매칭·영웅 텍스트/서브텍스트 배치·디자인 시스템 기반 하단 섹션 자동 생성.
    - Tweaks: 배경 텍스처(Dot Grid 강도 조정), 워터마크(배경에 Tally 마크 반복, 보너스 Depth 효과), 눈금 숫자 표시 유지. 프레젠트 시 영상과 배경이 자연스럽게 통합.

*   **[01:30:00] ~ 모바일 앱 프로토타입 빌드**

    - 일반 Claude에서 Tally 앱 스펙(804줄) 생성 → Claude Design Mobile Prototype에 Tally 디자인 시스템 + 스펙 붙여넣기. 질문에 응답: "전체 화면", "인터랙티브", "다크/라이트 모드 토글", "3개 인사이트", 하드코딩 모의 데이터 선택.
    - 결과: 전체 앱 화면 캔버스(홈·플로우·위클리·온보딩·설정), 인터랙티브 버튼·토글·다크모드. 초안이 단조로워 "텍스처·Depth 추가 + Tweaks 제공" 요청.
    - Tweaks: Accent Green Medium, 카드 스타일 Lifted, 구독 표시 Bar 스타일. Draw 기능으로 iPhone 시간/배터리 UI 겹침 문제 지적 및 수정. 사용량 85% 도달.

*   **[02:00:00] ~ 런치 비디오: Hyperframes 활용**

    - AIS 프로모션 예시 시연(미리 만든 30초 애니메이션 비디오, 스크롤 배너·터미널 애니메이션·모션 그래픽 포함) → Tally용 런치 비디오 제작 시작.
    - Animation 템플릿 + Tally 디자인 시스템 + Hyperframes 마크다운 스킬 파일 → 25초 비디오 초안. 초안이 밋밋함 → "스토리텔링·빠른 페이스·더 많은 모션" 요청 → 2차 버전에서 페이드인·카운터 애니메이션·다이나믹 씬 구현.
    - Hyperframes 카탈로그에서 "App Showcase" URL → Claude Design이 GitHub 레포 직접 fetch → 모바일 폰 3대 바운스 애니메이션 씬 추가. 완성 후 화면 녹화 또는 Claude Code에서 MP4 렌더링.

*   **[02:15:00] ~ 두 번째 라이브 빌드: Lull 웹사이트 + Vercel 배포**

    - "Lull"(밤 음료 브랜드) 콘셉트를 Claude 채팅에서 완성 → 영웅 섹션용 배경 비디오 프롬프트 생성. Kling에서 이미지 생성, SeeDance 2.0으로 스팀 애니메이션 변환(8초 루프 MP4).
    - Claude Design에서 Sketch로 레이아웃 설계 → 비디오+브랜드 스펙 붙여넣기 → 원샷 빌드. motionsites.ai에서 유사한 스크롤 저니 사이트 영감 복사 → "내 배경 비디오로 교체+브랜드 반영" 요청으로 AIS 웹사이트 재현.
    - 배포 파이프라인: Claude Design에서 ZIP 내보내기 → Claude Code로 열기 → "GitHub private repo에 push" 요청 → 자동 레포 생성. Vercel에서 Import → Deploy → 실제 도메인(lull-website.vercel.app) 생성. 404 오류(index.html 경로 문제) → Claude Code가 자동 진단·수정·재배포.

*   **[02:45:00] ~ 토큰 관리 전략 심화 및 한계 정리**

    - 쿼터 소모 주요 원인: 모든 작업 Opus 4.7 사용, 준비 없는 브레인스토밍, 복잡한 디자인 시스템 생성(10~15분 소요), 긴 스레드 지속.
    - Model by Stage 전략: 초기 기획 → Opus 4.7, 작은 반복 → Sonnet 4.6 / Haiku. 브랜드 스타일 확립 후 대부분 Sonnet 가능. 일반 Claude에서 세밀한 계획 수립 후 Claude Design에서 실행.
    - 4 Compound Moves: ①Reference(스크린샷·링크·구체 요소 지목), ②No Defaults(AI 슬롭 방지), ③Design System First(하나만 잘 만들기), ④Iterate in Chunks(한 번에 하나씩).
    - 주요 한계: 아이콘 로고 변형, Draw 버그, MP4 내보내기 미지원, 모바일 자동 최적화 없음, 파일 업로드 약 30~40MB 제한. 연구 프리뷰 단계로 개선 예정.

*(이후 영상 끝까지 중요한 흐름이 바뀔 때마다 시간대별 요약 추가)*

---
