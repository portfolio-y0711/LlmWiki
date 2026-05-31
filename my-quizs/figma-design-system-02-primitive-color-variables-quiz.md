# 📝 퀴즈: Figma Design System 02 — Primitive Color Variables

> 아래 문제를 풀어보세요. 답은 `figma-design-system-02-primitive-color-variables-answers.md` 파일에 있습니다.

---

## 1부. 객관식 (4지선다)

**Q1.** Primitive 색상(Primitive Colors)에 대한 설명으로 가장 올바른 것은?

- A) 디자이너가 UI에 직접 적용하는 완성된 색상 세트
- B) 디자인 시스템의 기반이 되는 베이스 Hue로, 기본 색상 팔레트를 구성하는 색상
- C) 다크 모드 전용으로 설계된 색상 변수
- D) Semantic 색상에서 파생되어 만들어지는 2차 색상

---

**Q2.** FDS(Figma Design System)에서 사용하는 Primitive 색상의 총 개수는?

- A) 9가지
- B) 11가지
- C) 13가지
- D) 19가지

---

**Q3.** Tint와 Shade에 대한 설명으로 올바른 것은?

- A) Tint는 채도(Saturation)를 높이고, Shade는 채도를 낮춘다
- B) Tint는 명도(Lightness)를 높여 밝게, Shade는 명도를 낮춰 어둡게 만든다
- C) Tint는 기본 색상에 검정을 섞고, Shade는 흰색을 섞는다
- D) Tint와 Shade는 색상(Hue)값만 다르며 명도와 채도는 동일하다

---

**Q4.** Neutral 스케일에 대한 설명으로 올바른 것은?

- A) Blue 기반으로 생성하며, 다른 색상과 동일하게 9단계로 구성된다
- B) "Color Tint & Shade Generator" 플러그인으로 실시간 생성한다
- C) Black 기반의 19단계 스케일이며, 스타터 파일에서 이미 플래트닝된 값을 사용한다
- D) White 기반으로 생성하며, 범위는 00부터 FF까지다

---

**Q5.** FDS에서 사용하는 Primitive 색상 네이밍 컨벤션으로 올바른 것은?

- A) `shade-color` 형식 (예: `500-blue`)
- B) `color_shade` 형식 (예: `blue_500`)
- C) `color/shade` 형식 (예: `blue/500`)
- D) `color.shade` 형식 (예: `blue.500`)

---

**Q6.** "Styler" 플러그인의 역할은 무엇인가?

- A) 색상 변수를 직접 Variables 패널에 생성한다
- B) 색상 프레임들을 Color Styles로 일괄 변환한다
- C) Color Styles를 Figma Variables로 변환한다
- D) 레이어 순서를 역정렬한다

---

**Q7.** Primitive 변수에 "Hide from Publishing"을 설정하는 주된 이유는?

- A) 파일 용량을 줄이기 위해
- B) 디자이너가 실수로 시스템 색상을 삭제하는 것을 방지하기 위해
- C) 디자이너에게 직접 노출하지 않고 Semantic 변수를 통해서만 사용하게 하여, 색상 적용의 확장성과 라이트/다크 모드 전환을 지원하기 위해
- D) Variables 패널의 목록이 너무 길어지는 것을 방지하기 위해

---

## 2부. O / X 문제

**Q8.** 색상 Tint/Shade를 수동으로 만들 때, 기본 색상 위에 흰색과 검정을 각각 20%, 40%, 60%, 80% 불투명도로 오버레이한 뒤 플래트닝하여 색상값을 추출한다.

> O / X

---

**Q9.** "Styles to Variables" 플러그인으로 Variables를 생성한 후에도 기존 Color Styles는 계속 유지하며 함께 사용한다.

> O / X

---

**Q10.** 레이어 패널에서 Brand 색상 세트는 최하단에, Neutral 색상 세트는 최상단에 배치한다.

> O / X

---

## 3부. 빈칸 채우기

**Q11.** FDS의 Primitive 색상은 총 ____가지이며, Brand를 포함해 Blue, Purple, Violet, Red, Pink, Orange, Yellow, Green, Teal, Cyan, ____, ____으로 구성된다.

---

**Q12.** Primitive 색상 스케일을 Variables로 변환하는 워크플로우는 두 단계다. 먼저 ____ 플러그인으로 Color Styles를 생성하고, 그 다음 ____ 플러그인으로 해당 Color Styles를 "Primitives" 컬렉션의 Variables로 변환한다.

---

**Q13.** 색상 스케일 사이의 간격은 ____px로 설정하며, Variables 패널에서 모든 Primitive 변수를 선택한 뒤 Edit Variables → "____" 옵션을 설정하여 디자이너에게 직접 노출되지 않도록 한다.

---

## 4부. 단답형

**Q14.** "Color Tint & Shade Generator" 플러그인을 사용해 색상 스케일을 생성할 때, 플러그인에 입력해야 하는 값은 무엇인가요?

---

**Q15.** 브랜드 색상(Brand Color)이란 무엇이며, FDS에서 나머지 색상들의 색조 통일감(tonal cohesion)을 만들기 위해 어떤 방법을 사용했나요?

---

**Q16.** "Variable Color Style Guide" 플러그인으로 생성한 스와치 페이지에서 각 색상 칩에 표시되는 정보 세 가지를 쓰세요. (강의에서 언급된 것 기준)

---

## 5부. 서술형

**Q17.** Primitive 변수를 생성한 후, 완성된 Variables를 다시 캔버스에서 모두 삭제해도 되는 이유를 설명하고, 디자이너에게 Primitive 변수를 직접 노출하지 않고 Semantic 변수만 사용하게 하는 것이 실무에서 왜 중요한지 서술하세요.

---

**Q18.** Tint/Shade 스케일을 수동으로 생성하는 방법과 플러그인을 사용하는 방법을 비교하고, Neutral 스케일이 일반 색상 스케일과 다른 점(단계 수, 출처, 생성 방법)을 함께 설명하세요.

---

*총 18문제 | 예상 소요 시간: 10~15분*
