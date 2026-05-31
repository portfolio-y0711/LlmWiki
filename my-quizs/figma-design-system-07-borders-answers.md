# ✅ 정답지: Figma Design System 07 — Borders

> 퀴즈 파일: `figma-design-system-07-borders-quiz.md`

---

## 1부. 객관식 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q1 | **C** | 강의에서 Microsoft 스타일(각진) vs Apple 스타일(둥근)을 비교하며 "sharp corners look corporate and rounded corners look consumer-friendly"라고 설명했습니다. 각진 디자인=기업적, 둥근 디자인=소비자 친화적이 정확한 매핑입니다. |
| Q2 | **B** | Pill 값이 999인 이유는 직사각형의 짧은 쪽 크기에 관계없이 항상 좌우를 완전히 둥글게 만들 수 있는 "충분히 큰 값"이기 때문입니다. 9999 같은 더 큰 값도 동작하지만 관례적으로 999를 사용합니다. |
| Q3 | **C** | Small(1.5px)은 **아이콘 전용 두께**입니다. 강의에서 "Small is for icons as it stays crisp on high resolution displays"라고 명시했습니다. |
| Q4 | **C** | 강의에서 변수 컬렉션 이름을 **`"border"`** (단수형)로 생성했습니다. `borders`(복수)나 `border-radius`가 아닌 단수 `border`가 정답입니다. |
| Q5 | **B** | 강의에서 Figma는 아직 Number 변수에 퍼센트(%) 입력을 지원하지 않아 **50**으로 입력하고, 엔지니어에게 "50px가 아닌 50%로 처리해달라"고 별도 안내해야 한다고 설명했습니다. |
| Q6 | **C** | 스트로크 필드에 변수 아이콘이 보이지 않을 때의 대안은 **우클릭 → Apply Variable** 입니다. Scoping이 아직 스트로크 필드를 완전히 지원하지 않아 발생하는 문제로, 우클릭 컨텍스트 메뉴로 해결합니다. |
| Q7 | **C** | 인풋 필드 focused 상태에는 **Medium — 2px** Border Width 변수를 적용했습니다. default 상태의 Extra Small(1px)에서 두께가 두 배로 증가합니다. |

---

## 2부. O / X 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q8 | **X** | Figma Variables 패널은 아직 Number 타입에서 퍼센트(%) 입력을 지원하지 않습니다. 강의에서 "Figma doesn't support percentage values in variables yet, so we enter 50 and tell engineers to treat it as 50%"라고 명시했습니다. |
| Q9 | **O** | 강의에서 Border Radius 그룹 6개를 먼저 생성한 뒤, 해당 그룹 전체를 **복제(Duplicate)**하고 변수 이름과 값을 수정하는 방식으로 Border Width 그룹을 만들었습니다. |
| Q10 | **O** | 강의에서 `border-width/XL(8)`을 Strokes per side 기능으로 한 측면에만 적용하여 "한쪽 면만 두꺼운 Border 효과"를 시연했습니다. 각 면에 서로 다른 변수를 독립적으로 적용할 수 있습니다. |

---

## 3부. 빈칸 채우기 정답

**Q11. Border Radius 변수 6가지**

| 이름 | 값 | 설명 |
|------|---|------|
| Circle | **50**% | 정사각형을 원으로 (Figma에서는 50으로 입력, 엔지니어에게 50%로 전달) |
| Pill | **999** | 직사각형 좌우를 완전히 둥글게 만드는 충분히 큰 값 |
| Large | **16** | 카드 외곽 등 큰 컴포넌트 |
| Medium | **12** | 카드 내부 요소, 인풋 필드 등 |
| Small | **8** | — |
| Extra Small | **4** | — |

---

**Q12. Border Width 변수 5가지**

| 이름 | 값(px) |
|------|-------|
| XL | **8** |
| Large | **4** |
| Medium | **2** |
| Small | **1.5** |
| Extra Small | **1** |

---

**Q13.**
> 인풋 필드 default 상태 Border Width: **1**px (Extra Small), focused 상태: **2**px (Medium)로 두꺼워진다. 두께뿐 아니라 **색상(color)** 도 함께 변경된다. Border Width 변수는 컬렉션 내에서 **"border-width"** 그룹으로 묶여 관리된다.

---

## 4부. 단답형 정답

**Q14.**
> **Shift+Enter**는 Variables 패널에서 현재 변수를 **즉시 복제(Duplicate)**하는 단축키입니다.
> 이 팁은 이전 에피소드(06 Layout and Breakpoints)에서 커뮤니티 멤버 **Abdul**이 소개한 것으로, 강의에서 "here's a trick I picked up from a community member called Abdul"이라고 언급했습니다. 에피소드 07에서도 동일하게 활용하여 Pill→Large→Medium→Small→Extra Small 순으로 빠르게 변수를 복제했습니다.

---

**Q15.**
> **Scoping 업데이트**가 구현되면 변수가 적합한 필드에만 표시됩니다. 예를 들어 Border Radius 변수는 Corner Radius 필드에서만, Border Width 변수는 Stroke/Width 필드에서만 선택할 수 있게 됩니다. 현재는 스트로크 필드에 변수 아이콘이 나타나지 않아 우클릭 → Apply Variable로 우회해야 하지만, Scoping이 적용되면 해당 필드에 자동으로 변수 아이콘이 표시되어 직접 연결할 수 있게 됩니다.

---

**Q16.**
> Dev Mode에서 Border 변수가 적용된 컴포넌트를 확인하면 다음 정보가 표시됩니다:
> 1. **`radius-L: 16`** — Border Radius Large 변수가 연결된 값 (컬렉션명/변수명/실제 수치)
> 2. **`border-width-M: 2px`** — Border Width Medium 변수가 연결된 값 (컬렉션명/변수명/실제 수치)
>
> 엔지니어는 이 정보를 통해 하드코딩된 수치가 아닌 변수명을 코드에 매핑할 수 있어 핸드오프가 명확해집니다.

---

## 5부. 서술형 모범 답안

**Q17. Border Radius와 Border Width의 UI/UX 역할과 디자인 시스템 표준화의 중요성**

> **Border Radius의 역할 — 브랜드 아이덴티티와 감성 전달:**
> Border Radius는 UI의 시각적 성격을 결정하는 핵심 요소입니다. 강의에서 Microsoft 스타일(각진, 기업적)과 Apple 스타일(둥근, 소비자 친화적)을 비교하며 설명했습니다. 로그인 폼에서 버튼과 인풋 필드를 동일한 반경으로 처리하면 시각적 일관성이 형성되고, 브랜드의 감성(딱딱함/부드러움)이 명확히 전달됩니다. Circle(50%)은 아바타나 뱃지를 원형으로, Pill(999)은 태그나 버튼을 완전히 둥글게 처리하는 등 각 값이 구체적인 사용 목적을 가집니다.
>
> **Border Width의 역할 — 인터랙션 상태 전달:**
> Border Width는 상태 변화를 시각적으로 전달하는 역할을 합니다. 인풋 필드의 default 상태(Extra Small, 1px)에서 focused 상태(Medium, 2px)로 전환될 때, 두께가 두 배로 증가하면서 색상도 함께 변경됩니다. 이 두 가지 시각적 신호가 결합되어 사용자는 "지금 이 필드가 활성화되었다"는 것을 직관적으로 인식합니다. Small(1.5px)은 아이콘 전용으로 설계되어 고해상도 화면에서도 선명하게 표시됩니다.
>
> **디자인 시스템 표준화의 중요성:**
> 두 변수를 시스템에서 표준화하면 세 가지 이점이 생깁니다. 첫째, **일관성**: 모든 컴포넌트가 동일한 변수 세트를 참조하므로 전체 제품에서 시각적 일관성이 유지됩니다. 둘째, **확장성**: 브랜드 감성을 변경할 때 변수 값 하나만 수정하면 연결된 모든 컴포넌트가 자동으로 업데이트됩니다. 셋째, **협업**: Dev Mode에서 `radius-L: 16`, `border-width-M: 2px` 형태로 표시되어 디자이너-엔지니어 간 핸드오프가 명확해지고 구현 오류가 줄어듭니다.

---

**Q18. Border 변수 컬렉션 생성부터 컴포넌트 적용까지의 전체 워크플로우**

> **단계별 워크플로우:**
>
> **1단계 — 컬렉션 및 Border Radius 변수 생성**
> - 변수 패널에서 `border` 컬렉션 생성
> - Number 타입으로 첫 번째 변수 `border-radius/circle` = 50 추가 (% 미지원으로 숫자 50 입력)
> - **Shift+Enter**로 빠른 복제: pill(999) → large(16) → medium(12) → small(8) → extra-small(4) 순차 입력
> - 전체 선택 → 우클릭 → `New Group with Selection`으로 `border-radius` 그룹 생성
>
> **2단계 — Border Width 변수 생성 (그룹 복제 방식)**
> - `border-radius` 그룹 복제 후 `border-width`로 이름 변경
> - 불필요한 변수 삭제 후 XL(8)·Large(4)·Medium(2)·Small(1.5)·Extra Small(1)로 값 수정
> - 이 방법은 처음부터 새로 만드는 것보다 빠르고 그룹 구조를 재활용할 수 있음
>
> **3단계 — 카드 컴포넌트에 Border Radius 적용**
> - 카드 외곽 선택 → 디자인 패널 Corner Radius → `border-radius/large(16)` 적용
> - Command+Shift로 내부 이미지 등 다중 선택 → `border-radius/medium(12)` 적용
>
> **4단계 — 인풋 필드에 Border Width 적용 (우클릭 방법)**
> - 인풋 필드의 Outline 스트로크 선택 → 변수 아이콘이 보이지 않는 경우
> - **우클릭 → Apply Variable** → `border-width/extra-small(1)` 선택 (default 상태)
> - Focus 상태는 `border-width/medium(2)` 적용
>
> **5단계 — Dev Mode로 핸드오프 확인**
> - Dev Mode 전환 → 적용된 변수명과 값(`radius-L: 16`, `border-width-M: 2px`) 확인
>
> **Figma의 현재 한계 (퍼센트 미지원) 실무 처리:**
> Circle 변수는 50%가 아닌 **50(숫자)**으로 입력해야 합니다. Figma의 Number 변수 타입은 아직 퍼센트를 지원하지 않기 때문입니다. 실무에서는 ① Figma 변수에 50을 입력하고, ② 디자이너가 엔지니어에게 "이 값은 50px이 아닌 50%로 처리해야 한다"고 명시적으로 전달하거나, ③ Dev Mode 주석이나 Storybook 문서에 별도로 기재하는 방식으로 보완합니다.

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
