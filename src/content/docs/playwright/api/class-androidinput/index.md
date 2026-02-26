---
title: "AndroidInput"
description: "추가된 버전: v1.9 androidInput.drag"
---

Source URL: https://playwright.dev/docs/api/class-androidinput

# AndroidInput | Playwright

---

## 메서드[​](https://playwright.dev/docs/api/class-androidinput#methods "Direct link to Methods")

### drag[​](https://playwright.dev/docs/api/class-androidinput#android-input-drag "Direct link to drag")

추가된 버전: v1.9 androidInput.drag

[from](https://playwright.dev/docs/api/class-androidinput#android-input-drag-option-from) 지점과 [to](https://playwright.dev/docs/api/class-androidinput#android-input-drag-option-to) 지점 사이에서 드래그를 수행합니다.

**사용법**

```
    await androidInput.drag(from, to, steps);

```

**인수**

- `from` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-androidinput#android-input-drag-option-from)
  - `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

  - `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

드래그의 시작 지점입니다.

- `to` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-androidinput#android-input-drag-option-to)
  - `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

  - `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

드래그의 끝 지점입니다.

- `steps` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androidinput#android-input-drag-option-steps)

드래그의 단계 수입니다. 각 단계는 완료에 5밀리초가 걸립니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androidinput#android-input-drag-return)

---

### press[​](https://playwright.dev/docs/api/class-androidinput#android-input-press "Direct link to press")

추가된 버전: v1.9 androidInput.press

[key](https://playwright.dev/docs/api/class-androidinput#android-input-press-option-key)를 누릅니다.

**사용법**

```
    await androidInput.press(key);

```

**인수**

- `key` [AndroidKey][#](https://playwright.dev/docs/api/class-androidinput#android-input-press-option-key)

누를 키입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androidinput#android-input-press-return)

---

### swipe[​](https://playwright.dev/docs/api/class-androidinput#android-input-swipe "Direct link to swipe")

추가된 버전: v1.9 androidInput.swipe

[segments](https://playwright.dev/docs/api/class-androidinput#android-input-swipe-option-segments)로 정의된 경로를 따라 스와이프합니다.

**사용법**

```
    await androidInput.swipe(from, segments, steps);

```

**인수**

- `from` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-androidinput#android-input-swipe-option-from)
  - `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

  - `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

스와이프를 시작할 지점입니다.

- `segments` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-androidinput#android-input-swipe-option-segments)
  - `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

  - `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

스와이프 제스처에서 [from](https://playwright.dev/docs/api/class-androidinput#android-input-swipe-option-from) 지점 뒤를 잇는 지점들입니다.

- `steps` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androidinput#android-input-swipe-option-steps)

각 세그먼트의 단계 수입니다. 각 단계는 완료에 5밀리초가 걸리므로, 100단계는 세그먼트당 0.5초를 의미합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androidinput#android-input-swipe-return)

---

### tap[​](https://playwright.dev/docs/api/class-androidinput#android-input-tap "Direct link to tap")

추가된 버전: v1.9 androidInput.tap

지정된 [point](https://playwright.dev/docs/api/class-androidinput#android-input-tap-option-point)를 탭합니다.

**사용법**

```
    await androidInput.tap(point);

```

**인수**

- `point` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-androidinput#android-input-tap-option-point)
  - `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

  - `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

탭할 지점입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androidinput#android-input-tap-return)

---

### type[​](https://playwright.dev/docs/api/class-androidinput#android-input-type "Direct link to type")

추가된 버전: v1.9 androidInput.type

현재 포커스된 위젯에 [text](https://playwright.dev/docs/api/class-androidinput#android-input-type-option-text)를 입력합니다.

**사용법**

```
    await androidInput.type(text);

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androidinput#android-input-type-option-text)

입력할 텍스트입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androidinput#android-input-type-return)
