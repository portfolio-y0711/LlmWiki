# 📝 퀴즈: Figma Design System 03 — Semantic Color Variables

> 아래 문제를 풀어보세요. 답은 `figma-design-system-03-semantic-color-variables-answers.md` 파일에 있습니다.

---

## 1부. 객관식 (4지선다)

**Q1.** Semantic 색상 변수의 핵심 특징으로 가장 올바른 것은?

- A) 색상의 실제 Hex 값을 기반으로 이름을 붙인다 (예: `#1A73E8`)
- B) 색상의 **사용 목적과 의미**에 따라 이름을 붙인다 (예: `background/brand`)
- C) 플랫폼별(Web/iOS/Android)로 각각 다른 색상 값을 가진다
- D) Primitive 색상과 동일한 Hex 값을 가지므로 서로 혼용할 수 있다

---

**Q2.** Semantic 네이밍 스키마의 **그룹(Group)** 에 해당하지 않는 것은?

- A) `content`
- B) `surface`
- C) `brand`
- D) `overlay`

---

**Q3.** 이번 에피소드에서 Black과 White의 **50% 불투명도 버전**을 추가로 생성한 이유는?

- A) 비활성화(Disabled) 상태의 컴포넌트 색상에 사용하기 위해
- B) 다크 모드에서 텍스트 가독성을 높이기 위해
- C) 모달이 열릴 때 배경을 어둡게 처리하는 **오버레이(Overlay)** 용도로 사용하기 위해
- D) Primitive 팔레트의 색상 단계를 보완하기 위해

---

**Q4.** Styler 플러그인으로 Color Style을 생성할 때, 강의에서 진행한 **그룹 실행 순서**는?

- A) Background → Content → Surface → Border → Overlay
- B) Content → Background → Border → Surface → Overlay
- C) Overlay → Surface → Border → Background → Content
- D) Content → Border → Background → Overlay → Surface

---

**Q5.** "Styles to Variables" 플러그인의 **한계점**으로 올바른 것은?

- A) 한 번에 50개 이상의 Style을 변환할 수 없다
- B) 변환된 Variables의 이름에 슬래시(`/`) 구분자를 지원하지 않는다
- C) 할당된 Primitive 변수 참조를 유지하지 못하고 **Hex 값으로 변환**한다
- D) 라이트 모드와 다크 모드를 동시에 생성하지 못한다

---

**Q6.** Semantic 컬렉션에 다크 모드를 추가하는 방법은?

- A) 새로운 "dark"라는 이름의 Variables 컬렉션을 별도로 생성한다
- B) 기존 "light" 모드의 각 변수를 복제한 뒤 값을 변경한다
- C) Variables 패널에서 **"New Variable Mode"** 를 추가하고 "dark"로 이름을 변경한다
- D) Styler 플러그인을 다크 모드 색상 레이어에 한 번 더 실행한다

---

**Q7.** 변수 생성 완료 후 Color Style을 삭제할 때, **Shadow Effect Style만 유지하는 이유**는?

- A) Shadow는 Semantic 변수와 연결되어 있어 삭제하면 컴포넌트가 깨지기 때문에
- B) Figma가 아직 Shadow(Effect)에 대한 **Variables를 지원하지 않기** 때문에
- C) Shadow는 Primitive 변수와 직접 연결되어 있어 별도 관리가 필요하기 때문에
- D) Shadow Style은 문서화 페이지에서 자동으로 참조되기 때문에

---

## 2부. O / X 문제

**Q8.** Semantic 변수를 Variables 패널에서 하나씩 수동으로 생성할 경우, 1~2시간이 소요될 수 있다.

> O / X

---

**Q9.** "Styles to Variables" 플러그인은 Color Style을 Variables로 변환할 때 각 Style에 할당된 Primitive 변수 참조를 그대로 유지한다.

> O / X

---

**Q10.** Semantic 컬렉션에서 "New Variable Mode"로 dark 모드를 추가하면, 처음에는 light 모드와 완전히 다른 빈 값이 채워진다.

> O / X

---

## 3부. 빈칸 채우기

**Q11.** Semantic 네이밍 스키마는 세 가지 핵심 요소로 구성된다. ① ____ (content·background·border·surface·overlay 중 선택), ② ____ (primary·brand·link·negative 등), ③ ____ (bold·subtle·inverse) 및 상태(hover·press·disabled 등).

---

**Q12.** 이번 에피소드에서 Styler와 Styles to Variables 플러그인을 통해 최종적으로 생성된 Semantic 컬렉션 변수의 총 개수는 ____개이며, 컬렉션 이름은 소문자 "____"로 설정했다.

---

**Q13.** 전 에피소드에서 누락된 Black과 White 변수 외에, ____ 용도를 위해 각각 ____% 불투명도 버전도 추가 생성했다. 이 4개 변수는 모두 "____" 그룹으로 묶어 Primitives 컬렉션 최상단에 배치한다.

---

## 4부. 단답형

**Q14.** 브랜드 색상이 Blue에서 Purple로 전면 변경될 때, Semantic 변수 구조가 이 변경을 효율적으로 처리할 수 있는 이유를 한두 문장으로 설명하세요.

---

**Q15.** Surface 그룹의 색상 레이어로 Styler를 실행했을 때, Color Style 외에 추가로 생성되는 스타일의 종류와 그 활용 용도를 설명하세요.

---

**Q16.** Semantic 네이밍 스키마에서 **역할(Role)** 에 해당하는 항목을 강의 기준으로 5가지 이상 나열하세요.

---

## 5부. 서술형

**Q17.** Primitive 색상 변수와 Semantic 색상 변수의 차이점을 설명하고, 이 두 레이어 구조가 디자인 시스템의 **유지보수성과 확장성**에 어떤 이점을 주는지 구체적인 예시를 들어 서술하세요.

---

**Q18.** 이 강의에서 Semantic 변수 생성 시 플러그인을 사용했음에도 불구하고 **수동 작업이 여전히 필요했던 이유**를 설명하고, 수동 작업 단계에서 라이트 모드와 다크 모드 각각 어떤 작업을 수행했는지 서술하세요.

---

*총 18문제 | 예상 소요 시간: 10~15분*
