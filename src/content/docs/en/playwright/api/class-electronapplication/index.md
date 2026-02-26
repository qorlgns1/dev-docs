---
title: "ElectronApplication"
description: "Electron application representation. You can use electron.launch() to obtain the application instance. This instance you can control main electron pro..."
---

Source URL: https://playwright.dev/docs/api/class-electronapplication

# ElectronApplication | Playwright

Electron application representation. You can use [electron.launch()](https://playwright.dev/docs/api/class-electron#electron-launch) to obtain the application instance. This instance you can control main electron process as well as work with Electron windows:

```
    const { _electron: electron } = require('playwright');

    (async () => {
      // Launch Electron app.
      const electronApp = await electron.launch({ args: ['main.js'] });

      // Evaluation expression in the Electron context.
      const appPath = await electronApp.evaluate(async ({ app }) => {
        // This runs in the main Electron process, parameter here is always
        // the result of the require('electron') in the main app script.
        return app.getAppPath();
      });
      console.log(appPath);

      // Get the first window that the app opens, wait if necessary.
      const window = await electronApp.firstWindow();
      // Print the title.
      console.log(await window.title());
      // Capture a screenshot.
      await window.screenshot({ path: 'intro.png' });
      // Direct Electron console to Node terminal.
      window.on('console', console.log);
      // Click button.
      await window.click('text=Click me');
      // Exit app.
      await electronApp.close();
    })();

```

---

## Methods[​](https://playwright.dev/docs/api/class-electronapplication#methods "Direct link to Methods")

### browserWindow[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-browser-window "Direct link to browserWindow")

Added in: v1.11 electronApplication.browserWindow

Returns the BrowserWindow object that corresponds to the given Playwright page.

**Usage**

```
    await electronApplication.browserWindow(page);

```

**Arguments**

- `page` [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-browser-window-option-page)

Page to retrieve the window for.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-browser-window-return)

---

### close[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-close "Direct link to close")

Added in: v1.9 electronApplication.close

Closes Electron application.

**Usage**

```
    await electronApplication.close();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-close-return)

---

### context[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-context "Direct link to context")

Added in: v1.9 electronApplication.context

This method returns browser context that can be used for setting up context-wide routing, etc.

**Usage**

```
    electronApplication.context();

```

**Returns**

- [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-context-return)

---

### evaluate[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate "Direct link to evaluate")

Added in: v1.9 electronApplication.evaluate

Returns the return value of [pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-expression).

If the function passed to the [electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate) would wait for the promise to resolve and return its value.

If the function passed to the [electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate) returns a non-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") value, then [electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate) returns `undefined`. Playwright also supports transferring some additional values that are not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

```
    await electronApplication.evaluate(pageFunction);
    await electronApplication.evaluate(pageFunction, arg);

```

**Arguments**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Electron](https://playwright.dev/docs/api/class-electron "Electron")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-expression)

Function to be evaluated in the main Electron process.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-arg)

Optional argument to pass to [pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-expression).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-return)

---

### evaluateHandle[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle "Direct link to evaluateHandle")

Added in: v1.9 electronApplication.evaluateHandle

Returns the return value of [pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-expression) as a [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle").

The only difference between [electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate) and [electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle) is that [electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle) returns [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle").

If the function passed to the [electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle) would wait for the promise to resolve and return its value.

**Usage**

```
    await electronApplication.evaluateHandle(pageFunction);
    await electronApplication.evaluateHandle(pageFunction, arg);

```

**Arguments**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Electron](https://playwright.dev/docs/api/class-electron "Electron")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-expression)

Function to be evaluated in the main Electron process.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-arg)

Optional argument to pass to [pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-expression).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-return)

---

### firstWindow[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-first-window "Direct link to firstWindow")

Added in: v1.9 electronApplication.firstWindow

Convenience method that waits for the first application window to be opened.

**Usage**

```
    const electronApp = await electron.launch({
      args: ['main.js']
    });
    const window = await electronApp.firstWindow();
    // ...

```

**Arguments**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.33[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-first-window-option-timeout)

Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-first-window-return)

---

### process[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-process "Direct link to process")

Added in: v1.21 electronApplication.process

Returns the main process for this Electron Application.

**Usage**

```
    electronApplication.process();

```

**Returns**

- [ChildProcess](https://nodejs.org/api/child_process.html "ChildProcess")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-process-return)

---

### waitForEvent[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event "Direct link to waitForEvent")

Added in: v1.9 electronApplication.waitForEvent

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy value. Will throw an error if the application is closed before the event is fired. Returns the event data value.

**Usage**

```
    const windowPromise = electronApp.waitForEvent('window');
    await mainWindow.click('button');
    const window = await windowPromise;

```

**Arguments**

- `event` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event-option-event)

Event name, same one typically passed into `*.on(event)`.

- `optionsOrPredicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event-option-options-or-predicate)
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")

receives the event data and resolves to truthy value when the waiting should resolve.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout).

Either a predicate that receives an event or an options object. Optional.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event-return)

---

### windows[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-windows "Direct link to windows")

Added in: v1.9 electronApplication.windows

Convenience method that returns all the opened windows.

**Usage**

```
    electronApplication.windows();

```

**Returns**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-windows-return)

---

## Events[​](https://playwright.dev/docs/api/class-electronapplication#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-event-close "Direct link to on('close')")

Added in: v1.9 electronApplication.on('close')

This event is issued when the application process has been terminated.

**Usage**

```
    electronApplication.on('close', data => {});

```

---

### on('console')[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-event-console "Direct link to on('console')")

Added in: v1.42 electronApplication.on('console')

Emitted when JavaScript within the Electron main process calls one of console API methods, e.g. `console.log` or `console.dir`.

The arguments passed into `console.log` are available on the [ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage") event handler argument.

**Usage**

```
    electronApp.on('console', async msg => {
      const values = [];
      for (const arg of msg.args())
        values.push(await arg.jsonValue());
      console.log(...values);
    });
    await electronApp.evaluate(() => console.log('hello', 5, { foo: 'bar' }));

```

**Event data**

- [ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage")

---

### on('window')[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-event-window "Direct link to on('window')")

Added in: v1.9 electronApplication.on('window')

This event is issued for every window that is created **and loaded** in Electron. It contains a [Page](https://playwright.dev/docs/api/class-page "Page") that can be used for Playwright automation.

**Usage**

```
    electronApplication.on('window', data => {});

```

**Event data**

- [Page](https://playwright.dev/docs/api/class-page "Page")
