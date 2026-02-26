---
title: "Keyboard"
description: "Keyboard는 가상 키보드를 관리하기 위한 API를 제공합니다. 상위 수준 API는 keyboard.type()이며, 원시 문자를 받아 페이지에서 적절한 , /,  이벤트를 생성합니다."
---

Source URL: https://playwright.dev/docs/api/class-keyboard

# Keyboard | Playwright

Keyboard는 가상 키보드를 관리하기 위한 API를 제공합니다. 상위 수준 API는 [keyboard.type()](https://playwright.dev/docs/api/class-keyboard#keyboard-type)이며, 원시 문자를 받아 페이지에서 적절한 `keydown`, `keypress`/`input`, `keyup` 이벤트를 생성합니다.

더 세밀하게 제어하려면 [keyboard.down()](https://playwright.dev/docs/api/class-keyboard#keyboard-down), [keyboard.up()](https://playwright.dev/docs/api/class-keyboard#keyboard-up), [keyboard.insertText()](https://playwright.dev/docs/api/class-keyboard#keyboard-insert-text)를 사용해 실제 키보드에서 생성된 것처럼 이벤트를 수동으로 발생시킬 수 있습니다.

일부 텍스트를 선택하고 삭제하기 위해 `Shift`를 누른 상태로 유지하는 예시:

```
    await page.keyboard.type('Hello World!');
    await page.keyboard.press('ArrowLeft');

    await page.keyboard.down('Shift');
    for (let i = 0; i < ' World'.length; i++)
      await page.keyboard.press('ArrowLeft');
    await page.keyboard.up('Shift');

    await page.keyboard.press('Backspace');
    // Result text will end up saying 'Hello!'

```

대문자 `A`를 누르는 예시

```
    await page.keyboard.press('Shift+KeyA');
    // or
    await page.keyboard.press('Shift+A');

```

키보드로 전체 선택을 트리거하는 예시

```
    await page.keyboard.press('ControlOrMeta+A');

```

---

## Methods[​](https://playwright.dev/docs/api/class-keyboard#methods "Direct link to Methods")

### down[​](https://playwright.dev/docs/api/class-keyboard#keyboard-down "Direct link to down")

v1.9 이전에 추가됨 keyboard.down

`keydown` 이벤트를 디스패치합니다.

[key](https://playwright.dev/docs/api/class-keyboard#keyboard-down-option-key)는 의도한 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 값을 지정하거나, 텍스트 생성을 위한 단일 문자를 지정할 수 있습니다. [key](https://playwright.dev/docs/api/class-keyboard#keyboard-down-option-key) 값의 상위 집합은 [여기](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values)에서 확인할 수 있습니다. 키 예시는 다음과 같습니다.

`F1` \- `F12`, `Digit0`\- `Digit9`, `KeyA`\- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp` 등.

다음 수정자 단축키도 지원됩니다: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta`는 Windows와 Linux에서는 `Control`, macOS에서는 `Meta`로 해석됩니다.

`Shift`를 누른 상태로 유지하면 [key](https://playwright.dev/docs/api/class-keyboard#keyboard-down-option-key)에 해당하는 텍스트가 대문자로 입력됩니다.

[key](https://playwright.dev/docs/api/class-keyboard#keyboard-down-option-key)가 단일 문자라면 대소문자를 구분하므로 `a`와 `A`는 각각 서로 다른 텍스트를 생성합니다.

[key](https://playwright.dev/docs/api/class-keyboard#keyboard-down-option-key)가 `Shift`, `Meta`, `Control`, `Alt` 같은 수정자 키라면, 이후 키 입력은 해당 수정자가 활성화된 상태로 전송됩니다. 수정자 키를 해제하려면 [keyboard.up()](https://playwright.dev/docs/api/class-keyboard#keyboard-up)을 사용하세요.

키를 한 번 누른 뒤에는 이후 [keyboard.down()](https://playwright.dev/docs/api/class-keyboard#keyboard-down) 호출에서 [repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat)가 true로 설정됩니다. 키를 해제하려면 [keyboard.up()](https://playwright.dev/docs/api/class-keyboard#keyboard-up)을 사용하세요.

note

수정자 키는 `keyboard.down`에 영향을 줍니다. `Shift`를 누른 상태로 유지하면 텍스트가 대문자로 입력됩니다.

**Usage**

```
    await keyboard.down(key);

```

**Arguments**

- `key` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-keyboard#keyboard-down-option-key)

누를 키 이름 또는 생성할 문자(예: `ArrowLeft`, `a`).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-keyboard#keyboard-down-return)

---

### insertText[​](https://playwright.dev/docs/api/class-keyboard#keyboard-insert-text "Direct link to insertText")

v1.9 이전에 추가됨 keyboard.insertText

`input` 이벤트만 디스패치하며, `keydown`, `keyup`, `keypress` 이벤트는 발생시키지 않습니다.

**Usage**

```
    page.keyboard.insertText('嗨');

```

note

수정자 키는 `keyboard.insertText`에 영향을 주지 않습니다. `Shift`를 누른 상태로 유지해도 텍스트는 대문자로 입력되지 않습니다.

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-keyboard#keyboard-insert-text-option-text)

입력을 지정한 텍스트 값으로 설정합니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-keyboard#keyboard-insert-text-return)

---

### press[​](https://playwright.dev/docs/api/class-keyboard#keyboard-press "Direct link to press")

v1.9 이전에 추가됨 keyboard.press

tip

대부분의 경우 [locator.press()](https://playwright.dev/docs/api/class-locator#locator-press)를 대신 사용해야 합니다.

[key](https://playwright.dev/docs/api/class-keyboard#keyboard-press-option-key)는 의도한 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 값을 지정하거나, 텍스트 생성을 위한 단일 문자를 지정할 수 있습니다. [key](https://playwright.dev/docs/api/class-keyboard#keyboard-press-option-key) 값의 상위 집합은 [여기](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values)에서 확인할 수 있습니다. 키 예시는 다음과 같습니다.

`F1` \- `F12`, `Digit0`\- `Digit9`, `KeyA`\- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp` 등.

다음 수정자 단축키도 지원됩니다: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta`는 Windows와 Linux에서는 `Control`, macOS에서는 `Meta`로 해석됩니다.

`Shift`를 누른 상태로 유지하면 [key](https://playwright.dev/docs/api/class-keyboard#keyboard-press-option-key)에 해당하는 텍스트가 대문자로 입력됩니다.

[key](https://playwright.dev/docs/api/class-keyboard#keyboard-press-option-key)가 단일 문자라면 대소문자를 구분하므로 `a`와 `A`는 각각 서로 다른 텍스트를 생성합니다.

`key: "Control+o"`, `key: "Control++`, `key: "Control+Shift+T"` 같은 단축키도 지원됩니다. 수정자와 함께 지정하면 이후 키를 누르는 동안 수정자도 함께 눌린 상태로 유지됩니다.

**Usage**

```
    const page = await browser.newPage();
    await page.goto('https://keycode.info');
    await page.keyboard.press('A');
    await page.screenshot({ path: 'A.png' });
    await page.keyboard.press('ArrowLeft');
    await page.screenshot({ path: 'ArrowLeft.png' });
    await page.keyboard.press('Shift+O');
    await page.screenshot({ path: 'O.png' });
    await browser.close();

```

[keyboard.down()](https://playwright.dev/docs/api/class-keyboard#keyboard-down)과 [keyboard.up()](https://playwright.dev/docs/api/class-keyboard#keyboard-up)의 단축 형태입니다.

**Arguments**

- `key` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-keyboard#keyboard-press-option-key)

누를 키 이름 또는 생성할 문자(예: `ArrowLeft`, `a`).

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-keyboard#keyboard-press-option-delay)

`keydown`과 `keyup` 사이 대기 시간(밀리초)입니다. 기본값은 0입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-keyboard#keyboard-press-return)

---

### type[​](https://playwright.dev/docs/api/class-keyboard#keyboard-type "Direct link to type")

v1.9 이전에 추가됨 keyboard.type

caution

대부분의 경우 [locator.fill()](https://playwright.dev/docs/api/class-locator#locator-fill)을 대신 사용해야 합니다. 페이지에 특별한 키보드 처리가 있는 경우에만 키를 하나씩 눌러야 하며, 이 경우 [locator.pressSequentially()](https://playwright.dev/docs/api/class-locator#locator-press-sequentially)를 사용하세요.

텍스트의 각 문자마다 `keydown`, `keypress`/`input`, `keyup` 이벤트를 전송합니다.

`Control` 또는 `ArrowDown` 같은 특수 키를 누르려면 [keyboard.press()](https://playwright.dev/docs/api/class-keyboard#keyboard-press)를 사용하세요.

**Usage**

```
    await page.keyboard.type('Hello'); // Types instantly
    await page.keyboard.type('World', { delay: 100 }); // Types slower, like a user

```

note

수정자 키는 `keyboard.type`에 영향을 주지 않습니다. `Shift`를 누른 상태로 유지해도 텍스트는 대문자로 입력되지 않습니다.

note

미국 키보드에 없는 문자에 대해서는 `input` 이벤트만 전송됩니다.

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-keyboard#keyboard-type-option-text)

포커스된 요소에 입력할 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-keyboard#keyboard-type-option-delay)

키 입력 사이 대기 시간(밀리초)입니다. 기본값은 0입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-keyboard#keyboard-type-return)

---

### up[​](https://playwright.dev/docs/api/class-keyboard#keyboard-up "Direct link to up")

v1.9 이전에 추가됨 keyboard.up

`keyup` 이벤트를 디스패치합니다.

**Usage**

```
    await keyboard.up(key);

```

**Arguments**

- `key` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-keyboard#keyboard-up-option-key)

누를 키 이름 또는 생성할 문자(예: `ArrowLeft`, `a`).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-keyboard#keyboard-up-return)
