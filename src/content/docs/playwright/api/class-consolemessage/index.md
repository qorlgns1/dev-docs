---
title: "ConsoleMessage"
description: "// Listen for all console logs"
---

Source URL: https://playwright.dev/docs/api/class-consolemessage

# ConsoleMessage | Playwright

[ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage") 객체는 [page.on('console')](https://playwright.dev/docs/api/class-page#page-event-console) 이벤트를 통해 페이지에서 전달됩니다. 페이지에서 기록되는 각 콘솔 메시지에 대해 Playwright 컨텍스트에서 해당 이벤트가 발생합니다.

```
    // Listen for all console logs
    page.on('console', msg => console.log(msg.text()));

    // Listen for all console events and handle errors
    page.on('console', msg => {
      if (msg.type() === 'error')
        console.log(`Error text: "${msg.text()}"`);
    });

    // Get the next console log
    const msgPromise = page.waitForEvent('console');
    await page.evaluate(() => {
      console.log('hello', 42, { foo: 'bar' });  // Issue console.log inside the page
    });
    const msg = await msgPromise;

    // Deconstruct console log arguments
    await msg.args()[0].jsonValue(); // hello
    await msg.args()[1].jsonValue(); // 42

```

---

## 메서드[​](https://playwright.dev/docs/api/class-consolemessage#methods "Direct link to Methods")

### args[​](https://playwright.dev/docs/api/class-consolemessage#console-message-args "Direct link to args")

v1.9 이전에 추가됨 consoleMessage.args

`console` 함수 호출에 전달된 인수 목록입니다. [page.on('console')](https://playwright.dev/docs/api/class-page#page-event-console)도 참고하세요.

**사용법**

```
    consoleMessage.args();

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-consolemessage#console-message-args-return)

---

### location[​](https://playwright.dev/docs/api/class-consolemessage#console-message-location "Direct link to location")

v1.9 이전에 추가됨 consoleMessage.location

**사용법**

```
    consoleMessage.location();

```

**반환값**

- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-location-return)
  - `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

리소스의 URL입니다.

    * `lineNumber` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

리소스에서 0부터 시작하는 줄 번호입니다.

    * `columnNumber` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

리소스에서 0부터 시작하는 열 번호입니다.

---

### page[​](https://playwright.dev/docs/api/class-consolemessage#console-message-page "Direct link to page")

추가된 버전: v1.34 consoleMessage.page

해당 콘솔 메시지를 생성한 페이지(있는 경우)입니다.

**사용법**

```
    consoleMessage.page();

```

**반환값**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-page-return)

---

### text[​](https://playwright.dev/docs/api/class-consolemessage#console-message-text "Direct link to text")

v1.9 이전에 추가됨 consoleMessage.text

콘솔 메시지의 텍스트입니다.

**사용법**

```
    consoleMessage.text();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-text-return)

---

### type[​](https://playwright.dev/docs/api/class-consolemessage#console-message-type "Direct link to type")

v1.9 이전에 추가됨 consoleMessage.type

**사용법**

```
    consoleMessage.type();

```

**반환값**

- "log" | "debug" | "info" | "error" | "warning" | "dir" | "dirxml" | "table" | "trace" | "clear" | "startGroup" | "startGroupCollapsed" | "endGroup" | "assert" | "profile" | "profileEnd" | "count" | "time" | "timeEnd"[#](https://playwright.dev/docs/api/class-consolemessage#console-message-type-return)

---

### worker[​](https://playwright.dev/docs/api/class-consolemessage#console-message-worker "Direct link to worker")

추가된 버전: v1.57 consoleMessage.worker

해당 콘솔 메시지를 생성한 웹 워커 또는 서비스 워커(있는 경우)입니다. 웹 워커의 콘솔 메시지에도 [consoleMessage.page()](https://playwright.dev/docs/api/class-consolemessage#console-message-page)가 `null`이 아님에 유의하세요.

**사용법**

```
    consoleMessage.worker();

```

**반환값**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Worker](https://playwright.dev/docs/api/class-worker "Worker")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-worker-return)
