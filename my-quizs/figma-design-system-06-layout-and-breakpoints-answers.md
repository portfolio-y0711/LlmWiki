# ✅ 정답지: Figma Design System 06 — Layout and Breakpoints

> 퀴즈 파일: `figma-design-system-06-layout-and-breakpoints-quiz.md`

---

## 1부. 객관식 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q1 | **B** | 강의 정의: "layout is a set of vertical columns that allow designers and engineers to define the layout of their screens in a structured way." 수직 컬럼 세트로 화면 구조를 정의하는 것이 핵심입니다. |
| Q2 | **C** | 모바일 브레이크포인트는 **S(Small), 393px**입니다. 강의에서 "the mobile breakpoint can also be used for app design as it's the same size as an iPhone 14 or 15 Pro"라고 명시했습니다. |
| Q3 | **B** | 각 컬럼의 **좌우 8px 패딩** + 사이드의 **8px 마진**이 합쳐져 컬럼 사이에 일관된 **16px 거터**를 형성합니다. 강의: "each column contains 8 pixel padding on either side and the 8 pixel side margins provide a consistent 16 pixel gutter size." |
| Q4 | **C** | **Shift+Enter**가 변수 빠른 복제 단축키입니다. 강의에서 "here's a trick I picked up from a community member called Abdul — you go Shift+Enter to duplicate the variable"이라고 소개했습니다. |
| Q5 | **B** | 레이아웃 그리드(컬럼 수)는 **자동 전환되지 않으며 수동으로 변경**해야 합니다. 강의: "the only thing left for you to do is change the layout grid." Figma가 아직 이를 지원하지 않습니다. |
| Q6 | **B** | 데스크톱 그리드: **12컬럼, Type: Stretch, Margin 16, Gutter 16**, 색상 Blue 10% 불투명도. 강의에서 직접 설정하는 과정을 보여줬습니다. |
| Q7 | **C** | **컬렉션명: "layout"**, **그룹명: "breakpoint"**. 컬렉션과 그룹 이름이 반대로 혼동되기 쉬우니 주의가 필요합니다. |

---

## 2부. O / X 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q8 | **O** | 강의에서 "the mobile breakpoint can also be used for app design as it's the same size as an iPhone 14 or 15 Pro"라고 명시했습니다. 393px 모바일 브레이크포인트 = 앱 디자인 기준. |
| Q9 | **X** | Typography 변수 모드 전환 시 **타이포그래피 크기만 자동 전환**됩니다. 레이아웃 그리드 컬럼 수는 자동 전환되지 않으며 수동 변경이 필요합니다. 강의: "the only thing left for you to do is change the layout grid / let's hope Figma updates variables so we can tell the layout grid to change automatically." |
| Q10 | **X** | 브레이크포인트 변수의 타입은 **Number**입니다. 픽셀 수치 값(1440, 1024, 768, 393)을 저장하는 숫자형 변수입니다. Color 타입은 색상 변수에 사용합니다. |

---

## 3부. 빈칸 채우기 정답

**Q11.**
> 데스크톱·태블릿: **12**컬럼, 모바일·앱: **4**컬럼. 컬럼당 좌우 **8**px 패딩, 사이드 마진 **8**px → **16**px 거터 형성.

---

**Q12.**

| T셔츠 이름 | 픽셀값(px) | 해당 기기 |
|-----------|-----------|---------|
| XL | **1440** | 데스크톱 |
| L | **1024** | 태블릿 가로 (Landscape) |
| M | **768** | 태블릿 세로 (Portrait) |
| S | **393** | 모바일 (iPhone 14/15 Pro) |

---

**Q13.**
> 변수 이름: **"breakpoint"**. layout 컬렉션의 **XL(1440)** 변수를 참조. Desktop 모드: **layout/XL**, Mobile 모드: **layout/S** 할당.

---

## 4부. 단답형 정답

**Q14.**
> **Shift+Enter**는 Variables 패널에서 현재 변수를 **즉시 복제(Duplicate)**하는 단축키입니다.
> 이 팁은 커뮤니티 멤버 **Abdul**이 소개한 것으로, 강의에서 "here's a trick I picked up from a community member called Abdul — thanks a lot man!"이라고 감사를 표했습니다.

---

**Q15.**
> 강의 당시 Figma가 **Type Variables(Typography 변수)를 막 출시**한 시점이었고, 변수를 Desktop/Mobile 모드로 나누어 레이아웃 그리드가 자동 전환되는 기능은 아직 지원되지 않았기 때문입니다. 브레이크포인트는 향후 모드 전환 기능이 확장될 때를 대비해 Number 변수로만 우선 생성하고, 실제 모드 전환은 별도의 "typography" 컬렉션에서 실험적으로 시연한 것입니다.

---

**Q16.**
> 모바일 레이아웃 그리드 Style 생성 단계:
> 1. 데스크톱 프레임을 **복제(Duplicate)**한다
> 2. 복제된 프레임의 이름을 **"mobile"**로 변경한다
> 3. Figma 우측 패널 **Styles**에서 **"mobile"** Style을 새로 추가한다
> 4. Style 편집에서 컬럼 수를 **4**로 변경한다

---

## 5부. 서술형 모범 답안

**Q17. FDS 레이아웃 그리드 구조와 반응형 그리드의 중요성**

> **그리드 구조 설명:**
> FDS는 데스크톱·태블릿에서 **12컬럼**, 모바일·앱에서 **4컬럼** 반응형 그리드를 사용합니다. 각 컬럼은 좌우에 **8px 패딩**을 가지며, 화면 가장자리에도 **8px 사이드 마진**이 적용됩니다. 이때 인접한 두 컬럼의 패딩(8px + 8px)이 합쳐져 컬럼 사이에 **16px 거터**가 일관되게 형성됩니다. 컬럼 자체의 너비는 화면 크기에 따라 유동적으로 변하는 반응형 구조입니다.
>
> **반응형 그리드가 중요한 이유:**
> 디자인 시스템에서 반응형 그리드는 다양한 화면 크기에서 콘텐츠가 일관되게 배치되도록 보장합니다. 디자이너와 엔지니어가 동일한 그리드 기준을 공유하면 "이 버튼은 몇 컬럼 너비인가"처럼 명확한 언어로 소통할 수 있습니다. 또한 12컬럼 시스템은 1/2, 1/3, 1/4, 1/6 등 다양한 비율로 콘텐츠를 분할하기 쉬워 레이아웃 설계의 유연성이 높습니다.

---

**Q18. Typography 변수 모드 전환 팁과 Figma의 현재 한계**

> **작동 원리 (단계별):**
> 1. "typography" 컬렉션을 생성하고 Number 변수 "breakpoint"를 만든다
> 2. 이 변수에 layout 컬렉션의 XL 변수를 참조(reference)로 연결한다
> 3. **Desktop** 모드와 **Mobile** 모드 두 가지를 추가한다
> 4. Desktop 모드 값: `layout/XL(1440)`, Mobile 모드 값: `layout/S(393)`
> 5. 프레임에 `typography/breakpoint` 변수를 할당한다
> 6. 이후 모드를 Desktop↔Mobile로 전환하면 해당 프레임의 **Typography 크기 전체가 자동으로 전환**된다
>
> **실무적 이점:**
> 하나의 프레임 안에서 데스크톱과 모바일 타이포그래피 크기를 빠르게 비교하고 검토할 수 있습니다. 반응형 디자인 리뷰 시 두 개의 별도 파일이나 프레임을 오가지 않아도 모드 전환 한 번으로 전체 텍스트 크기 변화를 즉시 확인할 수 있어 효율적입니다.
>
> **현재 Figma의 한계:**
> 모드 전환이 Typography에는 적용되지만, **레이아웃 그리드(컬럼 수: 12↔4)는 자동으로 전환되지 않습니다**. 그리드는 여전히 수동으로 변경해야 합니다. 강의에서 "let's hope Figma updates variables so we can tell the layout grid to change automatically when you switch between desktop and mobile"이라고 언급하며 아쉬움을 표했습니다.

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
