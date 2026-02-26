---
title: "ElectronApplication"
description: "Electron 애플리케이션 표현입니다. electron.launch()을 사용해 애플리케이션 인스턴스를 얻을 수 있습니다. 이 인스턴스를 통해 Electron의 메인 프로세스를 제어하고 Electron 창도 다룰 수 있습니다:"
---

Source URL: https://playwright.dev/docs/api/class-electronapplication

# ElectronApplication | Playwright

Electron 애플리케이션 표현입니다. [electron.launch()](https://playwright.dev/docs/api/class-electron#electron-launch)을 사용해 애플리케이션 인스턴스를 얻을 수 있습니다. 이 인스턴스를 통해 Electron의 메인 프로세스를 제어하고 Electron 창도 다룰 수 있습니다:

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

## 메서드[​](https://playwright.dev/docs/api/class-electronapplication#methods "Direct link to Methods")

### browserWindow[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-browser-window "Direct link to browserWindow")

추가된 버전: v1.11 electronApplication.browserWindow

주어진 Playwright 페이지에 대응하는 BrowserWindow 객체를 반환합니다.

**사용법**

```
    await electronApplication.browserWindow(page);

```

**인수**

- `page` [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-browser-window-option-page)

창을 조회할 페이지입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-browser-window-return)

---

### close[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-close "Direct link to close")

추가된 버전: v1.9 electronApplication.close

Electron 애플리케이션을 닫습니다.

**사용법**

```
    await electronApplication.close();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-close-return)

---

### context[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-context "Direct link to context")

추가된 버전: v1.9 electronApplication.context

이 메서드는 컨텍스트 전역 라우팅 설정 등에 사용할 수 있는 브라우저 컨텍스트를 반환합니다.

**사용법**

```
    electronApplication.context();

```

**반환값**

- [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-context-return)

---

### evaluate[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate "Direct link to evaluate")

추가된 버전: v1.9 electronApplication.evaluate

[pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-expression)의 반환값을 반환합니다.

[electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate)에 전달된 함수가 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate)는 해당 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

[electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate)에 전달된 함수가 [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")이 아닌 값을 반환하면, [electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate)는 `undefined`를 반환합니다. Playwright는 또한 `JSON`으로 직렬화할 수 없는 일부 추가 값도 전송할 수 있습니다: `-0`, `NaN`, `Infinity`, `-Infinity`.

**사용법**

```
    await electronApplication.evaluate(pageFunction);
    await electronApplication.evaluate(pageFunction, arg);

```

**인수**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Electron](https://playwright.dev/docs/api/class-electron "Electron")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-expression)

Electron 메인 프로세스에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(선택 사항)_[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-return)

---

### evaluateHandle[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle "Direct link to evaluateHandle")

추가된 버전: v1.9 electronApplication.evaluateHandle

[pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-expression)의 반환값을 [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")로 반환합니다.

[electronApplication.evaluate()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate)와 [electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle)의 유일한 차이는 [electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle)이 [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")을 반환한다는 점입니다.

[electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle)에 전달된 함수가 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [electronApplication.evaluateHandle()](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle)은 해당 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

**사용법**

```
    await electronApplication.evaluateHandle(pageFunction);
    await electronApplication.evaluateHandle(pageFunction, arg);

```

**인수**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Electron](https://playwright.dev/docs/api/class-electron "Electron")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-expression)

Electron 메인 프로세스에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(선택 사항)_[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-evaluate-handle-return)

---

### firstWindow[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-first-window "Direct link to firstWindow")

추가된 버전: v1.9 electronApplication.firstWindow

첫 번째 애플리케이션 창이 열릴 때까지 기다리는 편의 메서드입니다.

**사용법**

```
    const electronApp = await electron.launch({
      args: ['main.js']
    });
    const window = await electronApp.firstWindow();
    // ...

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_ 추가된 버전: v1.33[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-first-window-option-timeout)

기다릴 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout)을 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-first-window-return)

---

### process[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-process "Direct link to process")

추가된 버전: v1.21 electronApplication.process

이 Electron Application의 메인 프로세스를 반환합니다.

**사용법**

```
    electronApplication.process();

```

**반환값**

- [ChildProcess](https://nodejs.org/api/child_process.html "ChildProcess")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-process-return)

---

### waitForEvent[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event "Direct link to waitForEvent")

추가된 버전: v1.9 electronApplication.waitForEvent

이벤트가 발생할 때까지 기다리고 그 값을 predicate 함수에 전달합니다. predicate가 truthy 값을 반환하면 완료됩니다. 이벤트가 발생하기 전에 애플리케이션이 닫히면 오류를 throw합니다. 이벤트 데이터 값을 반환합니다.

**사용법**

```
    const windowPromise = electronApp.waitForEvent('window');
    await mainWindow.click('button');
    const window = await windowPromise;

```

**인수**

- `event` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event-option-event)

이벤트 이름으로, 일반적으로 `*.on(event)`에 전달하는 것과 동일합니다.

- `optionsOrPredicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event-option-options-or-predicate)
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")

이벤트 데이터를 받아, 대기가 완료되어야 할 때 truthy 값으로 resolve됩니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_

기다릴 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout)을 사용해 변경할 수 있습니다.

이벤트를 받는 predicate 또는 옵션 객체 중 하나입니다. 선택 사항입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-wait-for-event-return)

---

### windows[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-windows "Direct link to windows")

추가된 버전: v1.9 electronApplication.windows

열려 있는 모든 창을 반환하는 편의 메서드입니다.

**사용법**

```
    electronApplication.windows();

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-electronapplication#electron-application-windows-return)

---

## Events[​](https://playwright.dev/docs/api/class-electronapplication#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-event-close "Direct link to on('close')")

추가된 버전: v1.9 electronApplication.on('close')

이 이벤트는 애플리케이션 프로세스가 종료되었을 때 발생합니다.

**사용법**

```
    electronApplication.on('close', data => {});

```

---

### on('console')[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-event-console "Direct link to on('console')")

추가된 버전: v1.42 electronApplication.on('console')

Electron 메인 프로세스 내 JavaScript가 `console.log` 또는 `console.dir` 같은 console API 메서드 중 하나를 호출하면 발생합니다.

`console.log`에 전달된 인수는 [ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage") 이벤트 핸들러 인수에서 사용할 수 있습니다.

**사용법**

```
    electronApp.on('console', async msg => {
      const values = [];
      for (const arg of msg.args())
        values.push(await arg.jsonValue());
      console.log(...values);
    });
    await electronApp.evaluate(() => console.log('hello', 5, { foo: 'bar' }));

```

**이벤트 데이터**

- [ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage")

---

### on('window')[​](https://playwright.dev/docs/api/class-electronapplication#electron-application-event-window "Direct link to on('window')")

추가된 버전: v1.9 electronApplication.on('window')

이 이벤트는 Electron에서 생성되고 **로드된** 모든 창마다 발생합니다. 여기에는 Playwright 자동화에 사용할 수 있는 [Page](https://playwright.dev/docs/api/class-page "Page")가 포함됩니다.

**사용법**

```
    electronApplication.on('window', data => {});

```

**이벤트 데이터**

- [Page](https://playwright.dev/docs/api/class-page "Page")
