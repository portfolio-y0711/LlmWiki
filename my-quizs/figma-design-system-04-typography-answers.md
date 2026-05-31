# ✅ 정답지: Figma Design System 04 — Typography

> 퀴즈 파일: `figma-design-system-04-typography-quiz.md`

---

## 1부. 객관식 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q1 | **B** | 강의 정의: "typography is more than just picking fonts, it's the art of arranging type to make written language legible, readable and visually appealing." 디자인 시스템에서는 시각적 아이덴티티와 콘텐츠 계층(hierarchy) 확립이 핵심 역할입니다. |
| Q2 | **B** | **웹: Inter**, **iOS: SF Pro Display + SF Pro Text**, **Android: Roboto**. 강의에서 "FDS uses Inter as its default typeface with SF Pro Display and Text for iOS and Roboto for Android"라고 명시했습니다. |
| Q3 | **C** | FDS는 **Regular**와 **Semi Bold** 두 가지 웨이트만 사용합니다. 최소한으로 유지해 일관성을 확보하는 전략입니다. |
| Q4 | **B** | 핵심 장점: H1·H2 같은 역할 고정 이름 대신 규모 이름을 사용하면 "제품 A에서 Heading XL이 H1이고, 제품 B에서는 Heading L이 H1"이 될 수 있어 **하나의 Typography Set으로 여러 제품을 지원**할 수 있습니다. |
| Q5 | **B** | **48 → 40 → 32 → 24 → 20 → 16pt**. 강의에서 "the scale is going down from 48 to 40 to 32 to 24 then makes a four-point drop to 20 then 16"이라고 설명했습니다. |
| Q6 | **B** | 웹 플랫폼에서 Styler 실행 후 **16개** 생성됩니다. iOS와 Android는 각각 **20개**가 생성됩니다(플랫폼별 차이 주의). |
| Q7 | **B** | Text 그룹 정렬: **크기 내림차순(5XL→XS)**, 각 크기 내에서 **Regular가 Semi Bold 위**에 위치. 강의에서 "regular has to go above semi bold"라고 명시했습니다. |

---

## 2부. O / X 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q8 | **X** | FDS의 **기본 그룹은 Heading과 Text 2가지**입니다. Label·Link는 "추가 가능"하다고 언급됐지만 FDS의 시작점에는 포함되지 않습니다. 강의: "for fds we'll start with heading and text." |
| Q9 | **O** | 강의에서 "we're going to start with just semi bold for the headings then introduce extra weights later"라고 명확히 언급했습니다. Heading은 Semi Bold → 이후 필요에 따라 추가 웨이트 도입. |
| Q10 | **X** | **iOS와 Android는 Styler가 정상 동작**했습니다. 실패한 것은 **웹(Web) Text 그룹의 Regular 웨이트 일부**였습니다. 강의: "iOS·Android ran Styler and got 20 each, so let's move on." |

---

## 3부. 빈칸 채우기 정답

**Q11.**
> `**그룹** / **크기** / **웨이트**` 형식. 플랫폼 포함 시: `web/**heading**/**L**/**semibold**` 형식.
>
> *참고: 레이어명에는 플랫폼 접두사(web/iOS/Android)를 붙이지만 최종 스타일 네이밍 컨벤션의 핵심 3요소는 그룹·크기·웨이트입니다.*

---

**Q12.**

| 스타일명 | 크기(pt) | 라인 높이 |
|---------|---------|---------|
| web/text/L/regular | **16** | 24 |
| web/text/M/regular | **14** | 20 |
| web/text/S/regular | **12** | 16 |
| web/text/XS/regular | **10** | 14 |

---

**Q13.**
> **4**포인트 스케일 기반. 48pt의 라인 높이: **56**, 24pt의 라인 높이: **32**. T셔츠 사이징 범위: **2XS**부터 **5XL**까지.
>
> *참고: 라인 높이 전체 시퀀스: 56→48→40→32→28→24*

---

## 4부. 단답형 정답

**Q14.**
> Styler 플러그인 사용 전 레이어에 미리 준비할 것들:
> 1. **레이어명을 스타일명으로 지정** (예: `web/heading/5XL/semibold`)
> 2. **해당 레이어에 실제 폰트 속성 적용**: 웨이트(Regular/Semi Bold), 폰트 크기(pt), 라인 높이, 자간(letter spacing)
>
> 강의: "you can see that here we've got web/heading/5XL/semibold on the right hand side we've got all of its details so the weight size line height letter spacing."

---

**Q15.**
> 강의에서 추가 가능하다고 언급한 그룹: **Label**과 **Link**.
> 강의: "you can add others like label and link but for fds we'll start with heading and text."

---

**Q16.**
> Figma Typography 변수 업데이트 시 생성 예정인 5가지 속성:
> 1. **Family** (폰트 패밀리)
> 2. **Size** (폰트 크기)
> 3. **Line Height** (라인 높이)
> 4. **Weight** (웨이트)
> 5. **Letter Spacing** (자간)

---

## 5부. 서술형 모범 답안

**Q17. 4포인트 스케일 + T셔츠 사이징 조합과 역할 기반 명명 대비 이점**

> **스케일 구성 설명:**
> FDS 타입 스케일은 **글로벌 4포인트 스케일**을 기반으로 크기를 48→40→32→24pt로 4pt씩 감소하다가, 하단에서 20→16pt로 추가 감소하는 6단계 크기 체계를 사용합니다. 각 크기에 대응하는 라인 높이는 56→48→40→32→28→24입니다. 이 수치 스케일에 **T셔츠 사이징(2XS~5XL)**이라는 의미 있는 이름을 붙여 `heading/XL/semibold`, `text/S/regular`처럼 직관적으로 읽히는 스타일명을 만듭니다.
>
> **T셔츠 사이징 vs. 역할 기반 명명(H1·H2):**
> 역할 기반 명명(H1·H2·H3·Body)을 사용하면 모든 제품이 동일한 역할 구조를 따라야 합니다. 제품 A가 H1으로 48pt를 쓰고 제품 B가 H1으로 32pt를 쓴다면, 별도의 Typography Set을 만들어야 합니다.
> 반면 T셔츠 사이징을 사용하면 "제품 A는 heading/5XL을 H1으로, 제품 B는 heading/XL을 H1으로" 각자 정의할 수 있어 **하나의 Typography Set으로 서로 다른 규모의 여러 제품을 지원**할 수 있습니다. 이는 디자인 시스템의 확장성을 크게 높이는 핵심 설계 결정입니다.

---

**Q18. Styler 워크플로우 전체 + 실패 보완 + 후처리**

> **전체 워크플로우:**
> 1. **사전 준비**: 레이어명을 스타일명(`web/heading/5XL/semibold` 등)으로 설정하고, 각 레이어에 실제 폰트 속성(크기·웨이트·라인 높이·자간)을 미리 적용합니다.
> 2. **플러그인 실행**: 웹·iOS·Android별로 Heading·Text 레이어를 Command+Shift로 다중 선택 → Styler 플러그인 → Generate Styles 실행. 웹 16개, iOS·Android 각 20개 생성.
>
> **실패 시 수동 보완:**
> 강의에서 웹 Text Regular 웨이트(L·M·S·XS) 4개가 플러그인 오류로 생성되지 않았습니다. 이 경우 Local Styles 패널 → + 버튼으로 직접 스타일을 수동 생성하고 이름(`web/text/L/regular`)과 값(16pt/라인 높이 24 등)을 입력합니다. **"플러그인이 항상 완벽하지 않다"는 것을 인지하고 빠르게 수동 보완하는 것**이 중요합니다.
>
> **후처리가 필요한 이유:**
> - **정렬**: Styler는 스타일을 생성 순서로 나열하여 순서가 뒤섞입니다. 5XL→4XL→…→2XS 내림차순으로, Text 그룹은 Regular가 Semi Bold 위에 오도록 수동 재정렬해야 스타일 패널에서 직관적으로 사용할 수 있습니다.
> - **할당**: Styler가 스타일 생성 시 레이어에 자동 할당하지 못한 경우, 텍스트 레이어를 선택한 뒤 우측 패널 Styles 검색창에서 스타일명(text/L/regular 등)을 검색하여 수동으로 할당합니다.

---

## 채점 기준

| 파트 | 문항 | 배점 | 만점 |
|------|------|------|------|
| 1부 객관식 | Q1~Q7 | 각 5점 | 35점 |
| 2부 O/X | Q8~Q10 | 각 5점 | 15점 |
| 3부 빈칸 | Q11~Q13 | 각 5점 | 15점 |
| 4부 단답 | Q14~Q16 | 각 5점 | 15점 |
| 5부 서술 | Q17~Q18 | 각 10점 | 20점 |
| **합계** | | | **100점** |

### 서술형 부분 채점 기준 (각 10점)
- **10점**: 핵심 개념 2가지 이상 + 구체적 수치·예시 + 이유/맥락 포함
- **7점**: 핵심 개념은 맞으나 수치·예시가 부족하거나 한 관점 누락
- **4점**: 부분적으로 정확하나 핵심 내용의 절반 이상 누락
- **0점**: 내용이 틀리거나 학습 자료에 없는 내용 기술

### 점수대별 평가 기준
- **90점 이상** 🏆 — 강좌 내용을 완벽하게 이해했습니다!
- **70~89점** 👍 — 핵심 개념은 잡혔습니다. 놓친 부분을 다시 확인해보세요.
- **50~69점** 📖 — 강좌를 한 번 더 보고 구조를 다시 정리해보세요.
- **50점 미만** 🔄 — 강좌를 처음부터 다시 시청하는 것을 추천합니다.
