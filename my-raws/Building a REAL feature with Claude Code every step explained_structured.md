---

## 📝 1. 영상 전체 요약

> "Grill Me → PRD → Issues → AFK Agent → QA" 5단계 워크플로우를 실제 프로젝트에 적용하며, 철학적 이론이 아닌 **실제 피처 개발 전 과정**을 날 것으로 보여주는 영상. 코드를 거의 보지 않고 LLM과의 대화·모듈 인터페이스·입출력 검토에 집중하는 것이 현대 AI 엔지니어링의 핵심임을 실증한다.



---

## 📖 2. 영상 주요 주제 (추상화된 목차)

*   **도입 — 프로젝트 맥락과 피처 아이디어 소개**

    - **세부 주제:** 1,200 커밋, 637 이슈의 실제 운영 프로젝트(Course Video Manager) — React Router + TypeScript + Node + Drizzle + Postgres + Vitest 스택
    - **세부 주제:** 기존 Ghost Lesson/Real Lesson 개념과 개선이 필요한 UX 페인 포인트 — "두 단계 생성(ghost 먼저 → 나중에 materialize)이 번거롭다"
    - **세부 주제:** Ghost Course(파일 시스템 없이 계획 단계 코스) 신규 피처 아이디어

*   **핵심 기법 1 — Grill Me 세션으로 요구사항 정제**

    - **세부 주제:** Grill Me 스킬의 원리 — LLM이 Explore 서브에이전트로 코드베이스를 먼저 조사한 뒤 스마트한 질문을 던져 요구사항의 구멍을 메우는 방식
    - **세부 주제:** 유비쿼터스 언어(Ubiquitous Language) 문서 — Domain-Driven Design 개념을 LLM과의 협업에 적용, ghost/real/materialize/materialization cascade 등 공유 용어 확립
    - **세부 주제:** "Why(이유)를 LLM에게 설명하는 것"의 중요성 — What만 알면 구현하지만 Why를 알아야 대안을 제안할 수 있음

*   **핵심 기법 2 — PRD 작성 및 GitHub Issues 분해**

    - **세부 주제:** Grill Me Q&A 결과를 PRD 스킬로 자동 요약 — 모듈 인터페이스 변경 사항(course write service 신규 메서드 등)을 표면화하여 검토
    - **세부 주제:** PRD를 4개 GitHub Issue로 분해 — 블로킹 관계 명시, 너무 잘게 쪼개지 않고 적절한 크기로 병합
    - **세부 주제:** 구현을 직접 리뷰하지 않고 신뢰하는 전략 — LLM의 요약 능력에 위임

*   **핵심 기법 3 — AFK Agent(Ralph Loop)로 자율 구현**

    - **세부 주제:** Sandcastle — Docker 컨테이너에서 Claude를 실행하고 커밋을 패치로 추출해 로컬 레포에 적용하는 AFK 인프라
    - **세부 주제:** "Day Shift / Night Shift" 패턴 — 인간이 Grill Me·PRD로 아이디어를 정제하는 동안(Day), AFK Agent가 병렬로 이전 이슈를 구현(Night)
    - **세부 주제:** 테스트와 타입 체크를 매 커밋마다 강제하는 것이 AFK Loop 성공의 핵심

*   **핵심 기법 4 — QA Loop와 피드백 이슈 생성**

    - **세부 주제:** QA Plan을 GitHub Issue로 생성 — AFK Agent가 생성한 커밋을 기반으로 단계별 테스트 가이드 자동 작성
    - **세부 주제:** 피드백 버튼으로 QA 중 발견된 버그를 즉시 이슈화 → Ralph Loop가 QA하는 동안 백그라운드에서 버그 수정
    - **세부 주제:** "Specs to Code" 접근법의 한계 — Ghost Course가 Git 레포가 아닐 경우 등 QA에서만 발견 가능한 엣지 케이스의 존재

*   **결론 — AI 시대 엔지니어링 철학**

    - **세부 주제:** 코드를 직접 보는 시간을 최소화하고 입출력·인터페이스·모듈에 집중하는 레버리지 높은 리뷰 방식
    - **세부 주제:** QA와 버그 픽스를 병렬화하는 것이 핵심 생산성 승수

*(참고: 이 항목은 영상의 논리적 구조를 추상화하여 그룹화한 것이며, 시간 정보는 포함되지 않습니다.)*



---

## ⏳ 3. 주요 시간대별 상세 요약

*   **[00:00:00] ~ 도입 — 실전 시연 선언**

    - 철학 위주의 이전 영상들과 달리 실제 프로젝트에서 피처를 처음부터 끝까지 개발하는 과정을 날 것으로 시연
    - "LLM을 팀에서 위임할 수 있는 사람처럼 대하라" — 아키텍처와 피드백 루프에 집중하는 것이 핵심
    - 사용 중인 프로젝트: Course Video Manager (1,200 커밋, 637 이슈 클로즈, React Router + TypeScript + Drizzle + Postgres)



*   **[00:02:00] ~ 피처 아이디어 정의 — Ghost vs Real 개념 설명**

    - Ghost Lesson: DB에만 존재하고 파일 시스템에는 없는 계획 단계 레슨
    - 현재 UX 페인 포인트: ① Real Lesson을 만들려면 Ghost를 먼저 만든 뒤 Materialize해야 함 (두 단계 번거로움), ② Real Lesson 삭제 시 Ghost로 변환 후에야 삭제 가능
    - 새 아이디어: Ghost Course — 파일 경로 없이 코스를 계획 단계로 생성하는 개념 (레포 초기화가 번거로울 때 유용)



*   **[00:04:00] ~ Grill Me 세션 시작 — 요구사항 딕테이션**

    - VS Code에서 Grill Me 스킬 실행, 음성 딕테이션으로 rough한 아이디어를 LLM에 입력
    - "Why를 설명하지 않으면 LLM이 대안을 제안할 수 없다" — Ghost Course를 원하는 이유(파일 시스템 커밋 없이 자유롭게 계획하기 위해)를 명시적으로 추가
    - Grill Me 스킬의 Explore 단계: 서브에이전트가 코드베이스를 대량 탐색하고 요약만 부모에게 전달 → 토큰 효율적



*   **[00:06:00] ~ Grill Me Q&A — 유비쿼터스 언어와 스마트 질문들**

    - LLM의 첫 번째 발견: DB의 `deletelesson` 서비스는 이미 Ghost/Real 모두 처리 가능 → 실제 문제는 UI 갭
    - Domain-Driven Design의 **유비쿼터스 언어** 개념 도입 설명: LLM과 개발자 사이의 공유 용어(ghost, materialize, materialization cascade)가 정밀한 소통을 가능하게 함
    - LLM의 핵심 질문들: "Ghost Course에 Real Lesson을 추가하면 어떤 상태가 되는가?", "Ghost Course가 Real Course로 전환되면 되돌릴 수 있는가?", "Ghost Course 안에서 Create Real Lesson 버튼을 보여줄 것인가?"
    - 스키마 변경: `courses` 테이블의 `file_path` 컬럼을 nullable로 변경 — 유일한 DB 스키마 변경



*   **[00:14:00] ~ Grill Me 완료 — 8개 요구사항으로 수렴**

    - 22분 대화로 도출된 8가지 명확한 요구사항:
      1. Courses.file_path nullable 허용
      2. Ghost Course 생성 (이름만 입력, 파일 경로 없음)
      3. Ghost Course UI에서 Publish/Export 액션 숨김
      4. Real/Ghost Course 모두에서 Create Real Lesson 버튼 제공
      5. Ghost Course에서 Real Lesson 생성 시 Materialization Cascade 트리거 (모달로 파일 경로 할당)
      6. Create Ghost Lesson은 기존과 동일하게 유지
      7. Real Lesson 삭제 액션 추가 (DB + 파일 시스템 동시 삭제)
      8. Convert to Ghost는 Real Lesson에서 유지
    - 유비쿼터스 언어 문서 업데이트 후 커밋: ghost course, materialization cascade 개념 추가



*   **[00:16:00] ~ PRD 작성 및 GitHub Issue 분해**

    - "Write a PRD" 스킬 실행 → Grill Me 대화를 기반으로 모듈별 변경 사항 정리
    - 모듈 인터페이스 검토: course write service에 신규 `materializeCourseAndLesson` 메서드 추가 여부 논의 — "구현보다 인터페이스에 집중"
    - PRD를 6개 이슈로 초안화 → 너무 작은 이슈들 병합하여 최종 4개로 조정
    - 각 이슈에 blocking 관계, 수용 기준, 부모 PRD 링크, 테스팅 결정 포함
    - 컨텍스트 창 40k 토큰 — 긴 세션임에도 효율적으로 유지됨



*   **[00:20:00] ~ AFK Agent 실행 — Sandcastle + Ralph Loop**

    - Sandcastle: Docker 컨테이너에서 Claude 실행 → 커밋을 패치로 추출해 로컬 레포에 적용하는 AFK 인프라
    - `pnpm ralph` 실행 — 최대 100회 반복 설정, GitHub Issues를 순서대로 클로즈하며 진행
    - "이제 내 일은 끝났다" — AFK Agent가 구현하는 동안 다음 Grill Me 세션 진행 가능
    - Day Shift(인간: 아이디어 정제) / Night Shift(LLM: 구현) 패턴



*   **[00:22:00] ~ 약 1.5시간 후 복귀 — AFK 결과 확인 및 QA**

    - 5 iterations, 14 커밋 생성 — 상세한 커밋 메시지로 변경 사항 추적 가능
    - QA Plan 생성: "최근 5개 커밋을 기반으로 단계별 QA 가이드를 GitHub Issue로 저장해줘"
    - QA 중 발견된 주요 피드백: ① Add Course 모달에서 Ghost 탭이 불필요하게 보임, ② Ghost Course 생성 후 해당 페이지로 자동 이동 안 됨 + React 에러, ③ 레슨 추가 UI에서 Ghost/Real 두 버튼보다 "Create on file system" 체크박스 방식이 더 자연스러움
    - 피드백 버튼으로 즉시 이슈화 → Ralph Loop이 QA와 병렬로 버그 수정



*   **[00:35:00] ~ 최종 결과 확인 및 마무리**

    - Ralph 8회 반복으로 QA 피드백 이슈까지 처리 완료
    - 최종 UI: Create Lesson 모달에 "Create on file system" 체크박스 적용 확인
    - 핵심 인사이트: "Specs to Code는 결코 완벽하지 않다 — QA 중에만 발견 가능한 엣지 케이스(예: Git 레포가 아닐 때 롤백 누락)는 항상 존재한다"
    - 엔지니어의 역할: 코드를 직접 보기보다 입출력·모듈 인터페이스를 검토하고, QA와 버그 픽스를 병렬화하는 것

---
