---
title: "ConsoleMessage"
description: "// Listen for all console logs"
---

Source URL: https://playwright.dev/docs/api/class-consolemessage

# ConsoleMessage | Playwright

[ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage") objects are dispatched by page via the [page.on('console')](https://playwright.dev/docs/api/class-page#page-event-console) event. For each console message logged in the page there will be corresponding event in the Playwright context.

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

## Methods[​](https://playwright.dev/docs/api/class-consolemessage#methods "Direct link to Methods")

### args[​](https://playwright.dev/docs/api/class-consolemessage#console-message-args "Direct link to args")

Added before v1.9 consoleMessage.args

List of arguments passed to a `console` function call. See also [page.on('console')](https://playwright.dev/docs/api/class-page#page-event-console).

**Usage**

```
    consoleMessage.args();

```

**Returns**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-consolemessage#console-message-args-return)

---

### location[​](https://playwright.dev/docs/api/class-consolemessage#console-message-location "Direct link to location")

Added before v1.9 consoleMessage.location

**Usage**

```
    consoleMessage.location();

```

**Returns**

- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-location-return)
  - `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

URL of the resource.

    * `lineNumber` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

0-based line number in the resource.

    * `columnNumber` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

0-based column number in the resource.

---

### page[​](https://playwright.dev/docs/api/class-consolemessage#console-message-page "Direct link to page")

Added in: v1.34 consoleMessage.page

The page that produced this console message, if any.

**Usage**

```
    consoleMessage.page();

```

**Returns**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-page-return)

---

### text[​](https://playwright.dev/docs/api/class-consolemessage#console-message-text "Direct link to text")

Added before v1.9 consoleMessage.text

The text of the console message.

**Usage**

```
    consoleMessage.text();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-text-return)

---

### type[​](https://playwright.dev/docs/api/class-consolemessage#console-message-type "Direct link to type")

Added before v1.9 consoleMessage.type

**Usage**

```
    consoleMessage.type();

```

**Returns**

- "log" | "debug" | "info" | "error" | "warning" | "dir" | "dirxml" | "table" | "trace" | "clear" | "startGroup" | "startGroupCollapsed" | "endGroup" | "assert" | "profile" | "profileEnd" | "count" | "time" | "timeEnd"[#](https://playwright.dev/docs/api/class-consolemessage#console-message-type-return)

---

### worker[​](https://playwright.dev/docs/api/class-consolemessage#console-message-worker "Direct link to worker")

Added in: v1.57 consoleMessage.worker

The web worker or service worker that produced this console message, if any. Note that console messages from web workers also have non-null [consoleMessage.page()](https://playwright.dev/docs/api/class-consolemessage#console-message-page).

**Usage**

```
    consoleMessage.worker();

```

**Returns**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Worker](https://playwright.dev/docs/api/class-worker "Worker")[#](https://playwright.dev/docs/api/class-consolemessage#console-message-worker-return)
