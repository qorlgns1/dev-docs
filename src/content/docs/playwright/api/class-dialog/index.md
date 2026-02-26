---
title: "Dialog"
description: "const { chromium } = require('playwright');  // Or 'firefox' or 'webkit'."
---

Source URL: https://playwright.dev/docs/api/class-dialog

# Dialog | Playwright

[Dialog](https://playwright.dev/docs/api/class-dialog "Dialog") 객체는 [page.on('dialog')](https://playwright.dev/docs/api/class-page#page-event-dialog) 이벤트를 통해 page에서 전달됩니다.

`Dialog` 클래스 사용 예시:

```
    const { chromium } = require('playwright');  // Or 'firefox' or 'webkit'.

    (async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      page.on('dialog', async dialog => {
        console.log(dialog.message());
        await dialog.dismiss();
      });
      await page.evaluate(() => alert('1'));
      await browser.close();
    })();

```

note

[page.on('dialog')](https://playwright.dev/docs/api/class-page#page-event-dialog) 리스너가 없는 경우, Dialog는 자동으로 닫힙니다. 리스너가 있는 경우에는 반드시 [dialog.accept()](https://playwright.dev/docs/api/class-dialog#dialog-accept) 또는 [dialog.dismiss()](https://playwright.dev/docs/api/class-dialog#dialog-dismiss)로 다이얼로그를 처리해야 합니다. 그렇지 않으면 페이지가 다이얼로그를 기다리며 [freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop#never_blocking) 상태가 되고, click 같은 동작이 끝나지 않습니다.

---

## Methods[​](https://playwright.dev/docs/api/class-dialog#methods "Direct link to Methods")

### accept[​](https://playwright.dev/docs/api/class-dialog#dialog-accept "Direct link to accept")

v1.9 이전에 추가됨 dialog.accept

다이얼로그가 수락되면 반환됩니다.

**Usage**

```
    await dialog.accept();
    await dialog.accept(promptText);

```

**Arguments**

- `promptText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-dialog#dialog-accept-option-prompt-text)

prompt에 입력할 텍스트입니다. 다이얼로그의 `type`이 prompt가 아니면 아무 효과가 없습니다. 선택 사항입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-dialog#dialog-accept-return)

---

### defaultValue[​](https://playwright.dev/docs/api/class-dialog#dialog-default-value "Direct link to defaultValue")

v1.9 이전에 추가됨 dialog.defaultValue

다이얼로그가 prompt이면 기본 prompt 값을 반환합니다. 그렇지 않으면 빈 문자열을 반환합니다.

**Usage**

```
    dialog.defaultValue();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-dialog#dialog-default-value-return)

---

### dismiss[​](https://playwright.dev/docs/api/class-dialog#dialog-dismiss "Direct link to dismiss")

v1.9 이전에 추가됨 dialog.dismiss

다이얼로그가 닫히면 반환됩니다.

**Usage**

```
    await dialog.dismiss();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-dialog#dialog-dismiss-return)

---

### message[​](https://playwright.dev/docs/api/class-dialog#dialog-message "Direct link to message")

v1.9 이전에 추가됨 dialog.message

다이얼로그에 표시되는 메시지입니다.

**Usage**

```
    dialog.message();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-dialog#dialog-message-return)

---

### page[​](https://playwright.dev/docs/api/class-dialog#dialog-page "Direct link to page")

추가됨: v1.34 dialog.page

사용 가능하다면, 이 다이얼로그를 시작한 page입니다.

**Usage**

```
    dialog.page();

```

**Returns**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-dialog#dialog-page-return)

---

### type[​](https://playwright.dev/docs/api/class-dialog#dialog-type "Direct link to type")

v1.9 이전에 추가됨 dialog.type

다이얼로그의 타입을 반환하며, `alert`, `beforeunload`, `confirm`, `prompt` 중 하나입니다.

**Usage**

```
    dialog.type();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-dialog#dialog-type-return)
