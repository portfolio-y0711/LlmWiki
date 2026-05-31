# ✅ 정답지: Figma Design System 03 — Semantic Color Variables

> 퀴즈 파일: `figma-design-system-03-semantic-color-variables-quiz.md`

---

## 1부. 객관식 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q1 | **B** | Semantic 색상은 색상의 **외형(Hex 값)이 아닌 사용 목적**에 따라 이름을 붙입니다. `background/brand`처럼 "이 색상이 어디에 어떻게 쓰이는가"를 이름에 담는 것이 핵심입니다. |
| Q2 | **C** | `brand`는 그룹이 아닌 **역할(Role)** 에 해당합니다. 그룹은 `content`, `background`, `border`, `surface`, `overlay` 5가지입니다. |
| Q3 | **C** | Black/50와 White/50는 모달이 열릴 때 뒤 배경을 반투명하게 처리하는 **오버레이(Overlay) 효과**에 사용됩니다. 강의에서 "we're going to make some overlays"라고 명시했습니다. |
| Q4 | **B** | **Content → Background → Border → Surface → Overlay** 순서로 실행했습니다. |
| Q5 | **C** | 플러그인의 핵심 한계는 Primitive 변수 참조(예: `neutral/900`)를 유지하지 못하고 **실제 Hex 값으로 대체**한다는 점입니다. 이로 인해 각 변수마다 Primitive 변수를 수동으로 재할당해야 합니다. |
| Q6 | **C** | 기존 Semantic 컬렉션에서 **"New Variable Mode"를 추가**하고 이름을 "dark"로 변경합니다. 이렇게 하면 light 모드의 값이 복사된 상태로 시작합니다. |
| Q7 | **B** | **Figma가 아직 Effect(Shadow)에 대한 Variables를 지원하지 않기 때문**입니다. 강의에서 "we're going to keep the Shadows because Figma doesn't have variables for them yet"이라고 명시했습니다. |

---

## 2부. O / X 정답

| 문제 | 정답 | 해설 |
|------|------|------|
| Q8 | **O** | 강의에서 "spend one to two hours adding each one individually"라고 언급했습니다. 변수 수가 54개에 달하기 때문에 수동 생성은 매우 비효율적입니다. |
| Q9 | **X** | 플러그인은 Primitive 변수 참조를 **유지하지 못하고 Hex 값으로 변환**합니다. 강의에서 "there's nothing I've found that will convert those Styles into variables that retain the color variable"이라고 명시했습니다. |
| Q10 | **X** | **반대**입니다. dark 모드를 추가하면 **light 모드의 값이 그대로 복사**됩니다. 따라서 각 변수의 값을 다크 모드에 맞는 Primitive 변수로 직접 교체해야 합니다. |

---

## 3부. 빈칸 채우기 정답

**Q11.**
> ① **그룹(Group)** (content·background·border·surface·overlay 중 선택), ② **역할(Role)** (primary·brand·link·negative 등), ③ **수식어(Modifier)** (bold·subtle·inverse) 및 상태(hover·press·disabled 등).

---

**Q12.**
> 총 **54**개이며, 컬렉션 이름은 소문자 **"semantic"** 으로 설정했다.

---

**Q13.**
> **오버레이(Overlay)** 용도를 위해 각각 **50**% 불투명도 버전도 추가 생성했다. 이 4개 변수(Black, White, Black/50, White/50)는 모두 **"primary"** 그룹으로 묶어 Primitives 컬렉션 최상단에 배치한다.

---

## 4부. 단답형 정답

**Q14.**
> Semantic 변수는 Primitive 변수를 **참조**하는 구조이기 때문입니다. 브랜드 색이 Blue에서 Purple로 바뀔 때, `background/brand` 같은 Semantic 변수가 참조하는 Primitive 변수 값(예: `brand/500`)만 새로운 Purple 팔레트로 교체하면, 해당 Semantic 변수를 사용하는 **전체 시스템과 모든 제품에 자동으로 반영**됩니다.

---

**Q15.**
> Surface 그룹 실행 시 **Shadow Effect Style**(그림자 효과 스타일)도 함께 생성됩니다.  
> 활용 용도: 엘리베이션(Elevation) 레벨별 그림자 표현에 사용하며, `Surface L1 Shadow`처럼 "Surface Lx Shadow" 형태로 이름을 변경하여 각 Surface 레벨에 대응하는 그림자 스타일로 활용합니다.

---

**Q16.**
> 강의 기준 역할(Role) 항목 (5가지 이상):
> 1. `primary`
> 2. `secondary`
> 3. `tertiary`
> 4. `brand`
> 5. `mono`
> 6. `link`
> 7. `info`
> 8. `notice`
> 9. `negative`
> 10. `positive`

---

## 5부. 서술형 모범 답안

**Q17. Primitive vs. Semantic 구조의 유지보수성과 확장성**

> **Primitive 색상**은 `brand/500`, `neutral/900` 처럼 실제 Hex 값을 담은 기반 색상이고, **Semantic 색상**은 `background/brand`, `content/primary` 처럼 "이 색상이 어디에 어떻게 쓰이는가"라는 사용 목적으로 이름 붙인 색상입니다.
>
> 이 두 레이어 구조가 가져오는 핵심 이점은 다음과 같습니다:
>
> **유지보수성:** 브랜드 색상이 Blue에서 Purple로 전면 변경될 때, Primitive 팔레트의 `brand/xxx` 색상 값만 교체하면 Semantic 변수가 참조하는 모든 색상이 자동으로 변경됩니다. 만약 UI의 모든 컴포넌트에 Primitive 색상을 직접 적용했다면, 수백 개의 컴포넌트를 일일이 찾아 수정해야 합니다.
>
> **확장성(라이트/다크 모드):** Semantic 변수는 모드(Mode)별로 서로 다른 Primitive를 참조할 수 있습니다. 예를 들어 `content/primary`는 라이트 모드에서 `neutral/900`(거의 검정)을, 다크 모드에서 `white`를 참조하도록 설정합니다. 이렇게 하면 Figma 내에서 모드 전환 한 번으로 전체 UI의 라이트/다크 모드가 네이티브로 전환됩니다.

---

**Q18. 플러그인 한계와 수동 작업의 내용**

> **수동 작업이 필요했던 이유:**
> "Styles to Variables" 플러그인이 Color Style을 Variables로 변환할 때, 각 Style에 할당되어 있던 Primitive 변수 참조(예: `neutral/900`)를 유지하지 못하고 해당 Hex 값으로 대체하기 때문입니다. 즉, 변환 후에는 Variables가 Primitive 변수를 참조하는 것이 아니라 단순 Hex 코드를 값으로 가지게 됩니다. 이 상태로는 Semantic의 핵심 이점(Primitive 변경 시 자동 반영, 모드 전환)을 활용할 수 없습니다.
>
> **라이트 모드 수동 작업:**
> Variables 패널의 Mode를 "light"로 설정한 뒤, 54개 변수 각각에 대해 Libraries에서 올바른 Primitive 변수를 검색하여 재할당합니다. (예: `content/primary`의 Hex 값 → `neutral/900` 변수로 교체)
>
> **다크 모드 수동 작업:**
> Variables 패널에서 "New Variable Mode"를 추가하고 "dark"로 이름을 변경합니다. 다크 모드를 추가하면 라이트 모드 값이 그대로 복사되므로, 각 변수마다 다크 모드에 맞는 Primitive 변수로 교체합니다. (예: `content/primary`의 라이트 모드 값 `neutral/900` → 다크 모드 값 `white`)

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
- **10점**: 핵심 개념 2가지 이상 정확히 서술 + 이유/맥락 + 구체적 예시 포함
- **7점**: 핵심 개념은 맞으나 예시가 없거나 한 가지 개념이 누락
- **4점**: 부분적으로 정확하나 핵심 내용의 절반 이상 누락
- **0점**: 내용이 틀리거나 학습 자료에 없는 내용 기술

### 점수대별 평가 기준
- **90점 이상** 🏆 — 강좌 내용을 완벽하게 이해했습니다!
- **70~89점** 👍 — 핵심 개념은 잡혔습니다. 놓친 부분을 다시 확인해보세요.
- **50~69점** 📖 — 강좌를 한 번 더 보고 구조를 다시 정리해보세요.
- **50점 미만** 🔄 — 강좌를 처음부터 다시 시청하는 것을 추천합니다.
