---
title: "BrowserContext"
description: "BrowserContext는 여러 개의 독립적인 브라우저 세션을 운영할 수 있는 방법을 제공합니다."
---

Source URL: https://playwright.dev/docs/api/class-browsercontext

# BrowserContext | Playwright

BrowserContext는 여러 개의 독립적인 브라우저 세션을 운영할 수 있는 방법을 제공합니다.

페이지가 `window.open` 호출 등으로 다른 페이지를 열면, 해당 팝업은 부모 페이지의 browser context에 속하게 됩니다.

Playwright는 [browser.newContext()](https://playwright.dev/docs/api/class-browser#browser-new-context) 메서드를 통해 격리된 비영구 browser context를 생성할 수 있습니다. 비영구 browser context는 어떤 브라우징 데이터도 디스크에 기록하지 않습니다.

```
    // Create a new incognito browser context
    const context = await browser.newContext();
    // Create a new page inside context.
    const page = await context.newPage();
    await page.goto('https://example.com');
    // Dispose context once it's no longer needed.
    await context.close();

```

---

## Methods[​](https://playwright.dev/docs/api/class-browsercontext#methods "Methods로 직접 연결")

### addCookies[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-cookies "addCookies로 직접 연결")

v1.9 이전에 추가됨 browserContext.addCookies

이 browser context에 쿠키를 추가합니다. 이 context 내의 모든 페이지에 해당 쿠키가 설치됩니다. 쿠키는 [browserContext.cookies()](https://playwright.dev/docs/api/class-browsercontext#browser-context-cookies)로 가져올 수 있습니다.

**Usage**

```
    await browserContext.addCookies([cookieObject1, cookieObject2]);

```

**Arguments**

- `cookies` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-cookies-option-cookies)
  - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

  - `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

  - `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

`url` 또는 `domain`과 `path` 둘 다가 필요합니다. 선택 사항입니다.

    * `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

쿠키를 모든 하위 도메인에도 적용하려면, 도메인 앞에 점을 붙이세요. 예: ".example.com". `url` 또는 `domain`과 `path` 둘 다가 필요합니다. 선택 사항입니다.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

`url` 또는 `domain`과 `path` 둘 다가 필요합니다. 선택 사항입니다.

    * `expires` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

초 단위 Unix 시간입니다. 선택 사항입니다.

    * `httpOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_

선택 사항입니다.

    * `secure` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_

선택 사항입니다.

    * `sameSite` "Strict" | "Lax" | "None" _(optional)_

선택 사항입니다.

    * `partitionKey` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

파티션된 서드파티 쿠키(즉, [CHIPS](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Partitioned_cookies))의 partition key입니다. 선택 사항입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-cookies-return)

---

### addInitScript[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script "addInitScript로 직접 연결")

v1.9 이전에 추가됨 browserContext.addInitScript

다음 상황 중 하나에서 평가될 스크립트를 추가합니다:

- browser context에서 페이지가 생성되거나 탐색될 때마다.
- browser context의 어떤 페이지에서든 자식 프레임이 attach되거나 탐색될 때마다. 이 경우 스크립트는 새로 attach된 프레임의 context에서 평가됩니다.

이 스크립트는 문서가 생성된 후, 문서 내 어떤 스크립트도 실행되기 전에 평가됩니다. 이는 JavaScript 환경을 보정할 때 유용합니다. 예를 들어 `Math.random` 시드 설정 등에 사용할 수 있습니다.

**Usage**

페이지 로드 전에 `Math.random`을 재정의하는 예시:

```
    // preload.js
    Math.random = () => 42;

```

```
    // In your playwright script, assuming the preload.js file is in same directory.
    await browserContext.addInitScript({
      path: 'preload.js'
    });

```

note

[browserContext.addInitScript()](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script)와 [page.addInitScript()](https://playwright.dev/docs/api/class-page#page-add-init-script)로 설치한 여러 스크립트의 평가 순서는 정의되어 있지 않습니다.

**Arguments**

- `script` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script-option-script)
  - `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

JavaScript 파일 경로입니다. `path`가 상대 경로이면 현재 작업 디렉터리를 기준으로 해석됩니다. 선택 사항입니다.

    * `content` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

원시 스크립트 내용입니다. 선택 사항입니다.

browser context의 모든 페이지에서 평가될 스크립트입니다.

- `arg` [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script-option-arg)

[script](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script-option-script)에 전달할 선택적 인수입니다(함수를 전달하는 경우에만 지원).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script-return)

---

### browser[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-browser "browser로 직접 연결")

v1.9 이전에 추가됨 browserContext.browser

이 context를 소유한 브라우저 인스턴스를 가져옵니다. context가 일반 브라우저 외부(예: Android 또는 Electron)에서 생성된 경우 `null`을 반환합니다.

**Usage**

```
    browserContext.browser();

```

**Returns**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Browser](https://playwright.dev/docs/api/class-browser "Browser")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-browser-return)

---

### clearCookies[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-clear-cookies "clearCookies로 직접 연결")

v1.9 이전에 추가됨 browserContext.clearCookies

context에서 쿠키를 제거합니다. 선택적 필터를 받을 수 있습니다.

**Usage**

```
    await context.clearCookies();
    await context.clearCookies({ name: 'session-id' });
    await context.clearCookies({ domain: 'my-origin.com' });
    await context.clearCookies({ domain: /.*my-origin\.com/ });
    await context.clearCookies({ path: '/api/v1' });
    await context.clearCookies({ name: 'session-id', domain: 'my-origin.com' });

```

**Arguments**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_ Added in: v1.43[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-clear-cookies-option-domain)

주어진 도메인의 쿠키만 제거합니다.

    * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_ Added in: v1.43[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-clear-cookies-option-name)

주어진 이름의 쿠키만 제거합니다.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_ Added in: v1.43[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-clear-cookies-option-path)

주어진 경로의 쿠키만 제거합니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-clear-cookies-return)

---

### clearPermissions[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-clear-permissions "clearPermissions로 직접 연결")

v1.9 이전에 추가됨 browserContext.clearPermissions

browser context의 모든 권한 재정의를 초기화합니다.

**Usage**

```
    const context = await browser.newContext();
    await context.grantPermissions(['clipboard-read']);
    // do stuff ..
    context.clearPermissions();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-clear-permissions-return)

---

### close[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-close "close로 직접 연결")

v1.9 이전에 추가됨 browserContext.close

browser context를 닫습니다. browser context에 속한 모든 페이지도 함께 닫힙니다.

note

기본 browser context는 닫을 수 없습니다.

**Usage**

```
    await browserContext.close();
    await browserContext.close(options);

```

**Arguments**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `reason` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ Added in: v1.40[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-close-option-reason)

context 종료로 인해 중단된 작업들에 보고할 사유입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-close-return)

---

### cookies[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-cookies "cookies로 직접 연결")

v1.9 이전에 추가됨 browserContext.cookies

URL을 지정하지 않으면 이 메서드는 모든 쿠키를 반환합니다. URL을 지정하면 해당 URL에 영향을 주는 쿠키만 반환합니다.

**Usage**

```
    await browserContext.cookies();
    await browserContext.cookies(urls);

```

**Arguments**

- `urls` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-cookies-option-urls)

선택적 URL 목록입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-cookies-return)

- `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")
  - `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

  - `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

  - `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

  - `expires` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

Unix time(초 단위)입니다.

    * `httpOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

    * `secure` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

    * `sameSite` "Strict" | "Lax" | "None"

    * `partitionKey` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

---

### exposeBinding[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding "Direct link to exposeBinding")

v1.9 이전에 추가됨 browserContext.exposeBinding

이 메서드는 컨텍스트 내 모든 페이지의 모든 프레임에 있는 `window` 객체에 [name](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-name)이라는 함수를 추가합니다. 이 함수가 호출되면 [callback](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-callback)을 실행하고, [callback](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-callback)의 반환값으로 resolve되는 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환합니다. [callback](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-callback)이 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면 await 됩니다.

[callback](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-callback) 함수의 첫 번째 인수에는 호출자 정보가 포함됩니다: `{ browserContext: BrowserContext, page: Page, frame: Frame }`.

페이지 전용 버전은 [page.exposeBinding()](https://playwright.dev/docs/api/class-page#page-expose-binding)을 참고하세요.

**Usage**

컨텍스트 내 모든 페이지의 모든 프레임에 페이지 URL을 노출하는 예시:

```
    const { webkit } = require('playwright');  // Or 'chromium' or 'firefox'.

    (async () => {
      const browser = await webkit.launch({ headless: false });
      const context = await browser.newContext();
      await context.exposeBinding('pageURL', ({ page }) => page.url());
      const page = await context.newPage();
      await page.setContent(`
        <script>
          async function onClick() {
            document.querySelector('div').textContent = await window.pageURL();
          }
        </script>
        <button onclick="onClick()">Click me</button>
        <div></div>
      `);
      await page.getByRole('button').click();
    })();

```

**Arguments**

- `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-name)

window 객체에 추가될 함수 이름입니다.

- `callback` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-callback)

Playwright 컨텍스트에서 호출될 콜백 함수입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `handle` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-option-handle)

더 이상 권장되지 않음

이 옵션은 향후 제거될 예정입니다.

인수를 값으로 전달하는 대신 핸들로 전달할지 여부입니다. 핸들로 전달할 때는 인수 하나만 지원합니다. 값으로 전달할 때는 여러 인수를 지원합니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding-return)

---

### exposeFunction[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function "Direct link to exposeFunction")

v1.9 이전에 추가됨 browserContext.exposeFunction

이 메서드는 컨텍스트 내 모든 페이지의 모든 프레임에 있는 `window` 객체에 [name](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function-option-name)이라는 함수를 추가합니다. 이 함수가 호출되면 [callback](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function-option-callback)을 실행하고, [callback](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function-option-callback)의 반환값으로 resolve되는 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환합니다.

[callback](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function-option-callback)이 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면 await 됩니다.

페이지 전용 버전은 [page.exposeFunction()](https://playwright.dev/docs/api/class-page#page-expose-function)을 참고하세요.

**Usage**

컨텍스트 내 모든 페이지에 `sha256` 함수를 추가하는 예시:

```
    const { webkit } = require('playwright');  // Or 'chromium' or 'firefox'.
    const crypto = require('crypto');

    (async () => {
      const browser = await webkit.launch({ headless: false });
      const context = await browser.newContext();
      await context.exposeFunction('sha256', text =>
        crypto.createHash('sha256').update(text).digest('hex'),
      );
      const page = await context.newPage();
      await page.setContent(`
        <script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        </script>
        <button onclick="onClick()">Click me</button>
        <div></div>
      `);
      await page.getByRole('button').click();
    })();

```

**Arguments**

- `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function-option-name)

window 객체에 추가될 함수 이름입니다.

- `callback` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function-option-callback)

Playwright 컨텍스트에서 호출될 콜백 함수입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function-return)

---

### grantPermissions[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions "Direct link to grantPermissions")

v1.9 이전에 추가됨 browserContext.grantPermissions

브라우저 컨텍스트에 지정된 권한을 부여합니다. `origin`이 지정된 경우 해당 origin에 대응하는 권한만 부여합니다.

**Usage**

```
    await browserContext.grantPermissions(permissions);
    await browserContext.grantPermissions(permissions, options);

```

**Arguments**

- `permissions` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions-option-permissions)

부여할 권한 목록입니다.

danger

지원되는 권한은 브라우저마다 다르며, 같은 브라우저라도 버전에 따라 다를 수 있습니다. 어떤 권한이든 업데이트 후 동작하지 않을 수 있습니다.

다음은 일부 브라우저에서 지원될 수 있는 권한입니다:

    * `'accelerometer'`
    * `'ambient-light-sensor'`
    * `'background-sync'`
    * `'camera'`
    * `'clipboard-read'`
    * `'clipboard-write'`
    * `'geolocation'`
    * `'gyroscope'`
    * `'local-fonts'`
    * `'local-network-access'`
    * `'magnetometer'`
    * `'microphone'`
    * `'midi-sysex'` (system-exclusive midi)
    * `'midi'`
    * `'notifications'`
    * `'payment-handler'`
    * `'storage-access'`

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions-option-origin)

권한을 부여할 [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "Origin")입니다. 예: "<https://example.com>".

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions-return)

---

### newCDPSession[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session "Direct link to newCDPSession")

추가됨: v1.11 browserContext.newCDPSession

note

CDP 세션은 Chromium 기반 브라우저에서만 지원됩니다.

새로 생성된 세션을 반환합니다.

**Usage**

```
    await browserContext.newCDPSession(page);

```

**Arguments**

- `page` [Page](https://playwright.dev/docs/api/class-page "Page") | [Frame](https://playwright.dev/docs/api/class-frame "Frame")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session-option-page)

새 세션을 만들 대상입니다. 하위 호환성을 위해 이 매개변수 이름은 `page`이지만, 타입은 `Page` 또는 `Frame`일 수 있습니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[CDPSession](https://playwright.dev/docs/api/class-cdpsession "CDPSession")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-cdp-session-return)

---

### newPage[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-page "Direct link to newPage")

v1.9 이전에 추가됨 browserContext.newPage

브라우저 컨텍스트에 새 페이지를 생성합니다.

**Usage**

```
    await browserContext.newPage();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-page-return)

---

### pages[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-pages "Direct link to pages")

v1.9 이전에 추가됨 browserContext.pages

컨텍스트에서 열려 있는 모든 페이지를 반환합니다.

**Usage**

```
    browserContext.pages();

```

**Returns**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-pages-return)

---

### removeAllListeners[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-remove-all-listeners "Direct link to removeAllListeners")

추가됨: v1.47 browserContext.removeAllListeners

지정한 타입의 리스너(타입이 없으면 등록된 모든 리스너)를 모두 제거합니다. 비동기 리스너가 완료될 때까지 기다리거나, 이후 해당 리스너에서 발생하는 오류를 무시하도록 할 수 있습니다.

**Usage**

```
    await browserContext.removeAllListeners();
    await browserContext.removeAllListeners(type, options);

```

**Arguments**

- `type` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-remove-all-listeners-option-type)
- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `behavior` "wait" | "ignoreErrors" | "default" _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-remove-all-listeners-option-behavior)

이미 실행 중인 리스너를 기다릴지, 그리고 리스너가 오류를 던질 경우 어떻게 처리할지 지정합니다:

      * `'default'` \- 현재 리스너 호출(있는 경우)이 끝날 때까지 기다리지 않으며, 리스너가 오류를 던지면 처리되지 않은 오류가 발생할 수 있습니다
      * `'wait'` \- 현재 리스너 호출(있는 경우)이 끝날 때까지 기다립니다

- `'ignoreErrors'` \- 현재 리스너 호출(있는 경우)이 끝날 때까지 기다리지 않으며, 제거 이후 리스너가 던지는 모든 오류는 조용히 포착됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-remove-all-listeners-return)

---

### route[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-route "Direct link to route")

v1.9 이전에 추가됨 browserContext.route

라우팅은 브라우저 컨텍스트의 모든 페이지가 수행하는 네트워크 요청을 수정할 수 있는 기능을 제공합니다. route가 활성화되면 URL 패턴과 일치하는 모든 요청은 continue, fulfill 또는 abort 되기 전까지 중단됩니다.

참고

[browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route)는 Service Worker가 가로챈 요청은 가로채지 않습니다. [이](https://github.com/microsoft/playwright/issues/1090) 이슈를 참고하세요. 요청 인터셉션 사용 시 [serviceWorkers](https://playwright.dev/docs/api/class-browser#browser-new-context-option-service-workers)를 `'block'`으로 설정해 Service Worker를 비활성화할 것을 권장합니다.

**사용법**

모든 이미지 요청을 중단하는 단순한 핸들러 예시:

```
    const context = await browser.newContext();
    await context.route('**/*.{png,jpg,jpeg}', route => route.abort());
    const page = await context.newPage();
    await page.goto('https://example.com');
    await browser.close();

```

또는 동일한 스니펫을 정규식 패턴으로 사용하는 예시:

```
    const context = await browser.newContext();
    await context.route(/(\.png$)|(\.jpg$)/, route => route.abort());
    const page = await context.newPage();
    await page.goto('https://example.com');
    await browser.close();

```

요청을 검사해 라우트 동작을 결정할 수도 있습니다. 예를 들어 일부 post data를 포함한 모든 요청을 모킹하고, 나머지 요청은 그대로 두는 방식입니다:

```
    await context.route('/api/**', async route => {
      if (route.request().postData().includes('my-string'))
        await route.fulfill({ body: 'mocked-data' });
      else
        await route.continue();
    });

```

요청이 두 핸들러와 모두 일치할 때 페이지 라우트([page.route()](https://playwright.dev/docs/api/class-page#page-route)로 설정)가 브라우저 컨텍스트 라우트보다 우선합니다.

핸들러와 함께 라우트를 제거하려면 [browserContext.unroute()](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute)를 사용할 수 있습니다.

참고

라우팅을 활성화하면 http cache가 비활성화됩니다.

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([URL](https://nodejs.org/api/url.html "URL")):[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-option-url)

라우팅 중 매칭에 사용할 [URL](https://nodejs.org/api/url.html "URL")을 받는 glob 패턴, 정규식 패턴 또는 predicate입니다. 컨텍스트 옵션에서 [baseURL](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url)이 설정되어 있고 제공된 URL이 `*`로 시작하지 않는 문자열이면 [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 사용해 해석됩니다.

- `handler` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([Route](https://playwright.dev/docs/api/class-route "Route"), [Request](https://playwright.dev/docs/api/class-request "Request")):[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-option-handler)

요청을 라우팅하는 handler 함수입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `times` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ v1.15에 추가됨[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-option-times)

라우트를 사용할 횟수입니다. 기본값은 매번 사용입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-return)

---

### routeFromHAR[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har "Direct link to routeFromHAR")

v1.23에 추가됨 browserContext.routeFromHAR

지정하면 컨텍스트에서 발생하는 네트워크 요청이 HAR 파일에서 제공됩니다. 자세한 내용은 [Replaying from HAR](https://playwright.dev/docs/mock#replaying-from-har)를 참고하세요.

Playwright는 Service Worker가 가로챈 요청을 HAR 파일에서 제공하지 않습니다. [이](https://github.com/microsoft/playwright/issues/1090) 이슈를 참고하세요. 요청 인터셉션 사용 시 [serviceWorkers](https://playwright.dev/docs/api/class-browser#browser-new-context-option-service-workers)를 `'block'`으로 설정해 Service Worker를 비활성화할 것을 권장합니다.

**사용법**

```
    await browserContext.routeFromHAR(har);
    await browserContext.routeFromHAR(har, options);

```

**인수**

- `har` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har-option-har)

사전 기록된 네트워크 데이터가 담긴 [HAR](http://www.softwareishard.com/blog/har-12-spec) 파일 경로입니다. `path`가 상대 경로이면 현재 작업 디렉터리를 기준으로 해석됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `notFound` "abort" | "fallback" _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har-option-not-found)
    - 'abort'로 설정하면 HAR 파일에서 찾지 못한 모든 요청이 중단됩니다.
    - 'fallback'으로 설정하면 핸들러 체인의 다음 route handler로 넘어갑니다.

기본값은 abort입니다.

    * `update` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har-option-update)

지정하면 파일에서 제공하는 대신 실제 네트워크 정보로 지정된 HAR를 업데이트합니다. 파일은 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)가 호출될 때 디스크에 기록됩니다.

    * `updateContent` "embed" | "attach" _(optional)_ v1.32에 추가됨[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har-option-update-content)

리소스 콘텐츠 관리 제어를 위한 선택 설정입니다. `attach`를 지정하면 리소스가 별도 파일 또는 ZIP 아카이브 항목으로 저장됩니다. `embed`를 지정하면 콘텐츠가 HAR 파일 내부에 인라인으로 저장됩니다.

    * `updateMode` "full" | "minimal" _(optional)_ v1.32에 추가됨[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har-option-update-mode)

`minimal`로 설정하면 HAR 라우팅에 필요한 정보만 기록합니다. 이 경우 HAR 재생 시 사용되지 않는 크기, 타이밍, 페이지, 쿠키, 보안 및 기타 HAR 정보는 생략됩니다. 기본값은 `minimal`입니다.

    * `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har-option-url)

요청 URL을 매칭할 glob 패턴, 정규식 또는 predicate입니다. 패턴과 URL이 일치하는 요청만 HAR 파일에서 제공됩니다. 지정하지 않으면 모든 요청이 HAR 파일에서 제공됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har-return)

---

### routeWebSocket[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-web-socket "Direct link to routeWebSocket")

v1.48에 추가됨 browserContext.routeWebSocket

이 메서드는 브라우저 컨텍스트의 모든 페이지에서 생성되는 websocket 연결을 수정할 수 있게 해줍니다.

이 메서드 호출 이후에 생성된 `WebSocket`만 라우팅됩니다. 어떤 페이지든 생성하기 전에 이 메서드를 호출하는 것을 권장합니다.

**사용법**

아래는 일부 websocket 메시지를 차단하는 단순한 핸들러 예시입니다. 자세한 내용과 예시는 [WebSocketRoute](https://playwright.dev/docs/api/class-websocketroute "WebSocketRoute")를 참고하세요.

```
    await context.routeWebSocket('/ws', async ws => {
      ws.routeSend(message => {
        if (message === 'to-be-blocked')
          return;
        ws.send(message);
      });
      await ws.connect();
    });

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([URL](https://nodejs.org/api/url.html "URL")):[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-web-socket-option-url)

이 패턴과 URL이 일치하는 WebSocket만 라우팅됩니다. 문자열 패턴은 [baseURL](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url) 컨텍스트 옵션을 기준으로 하는 상대 경로일 수 있습니다.

- `handler` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([WebSocketRoute](https://playwright.dev/docs/api/class-websocketroute "WebSocketRoute")):[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-web-socket-option-handler)

WebSocket을 라우팅하는 handler 함수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-web-socket-return)

---

### serviceWorkers[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-service-workers "Direct link to serviceWorkers")

v1.11에 추가됨 browserContext.serviceWorkers

참고

Service worker는 Chromium 기반 브라우저에서만 지원됩니다.

컨텍스트의 모든 기존 service worker입니다.

**사용법**

```
    browserContext.serviceWorkers();

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Worker](https://playwright.dev/docs/api/class-worker "Worker")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-service-workers-return)

---

### setDefaultNavigationTimeout[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout "Direct link to setDefaultNavigationTimeout")

v1.9 이전에 추가됨 browserContext.setDefaultNavigationTimeout

이 설정은 다음 메서드 및 관련 단축 동작의 기본 최대 탐색 시간을 변경합니다.

- [page.goBack()](https://playwright.dev/docs/api/class-page#page-go-back)

- [page.goForward()](https://playwright.dev/docs/api/class-page#page-go-forward)
  - [page.goto()](https://playwright.dev/docs/api/class-page#page-goto)
  - [page.reload()](https://playwright.dev/docs/api/class-page#page-reload)
  - [page.setContent()](https://playwright.dev/docs/api/class-page#page-set-content)
  - [page.waitForNavigation()](https://playwright.dev/docs/api/class-page#page-wait-for-navigation)

note

[page.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) 및 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout)이 [browserContext.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout)보다 우선 적용됩니다.

**사용법**

```
    browserContext.setDefaultNavigationTimeout(timeout);

```

**인수**

- `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout-option-timeout)

밀리초 단위의 최대 탐색 시간

---

### setDefaultTimeout[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout "Direct link to setDefaultTimeout")

v1.9 이전에 추가됨 browserContext.setDefaultTimeout

이 설정은 [timeout](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout-option-timeout) 옵션을 받는 모든 메서드의 기본 최대 시간을 변경합니다.

note

[page.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout), [browserContext.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout)이 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout)보다 우선 적용됩니다.

**사용법**

```
    browserContext.setDefaultTimeout(timeout);

```

**인수**

- `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout-option-timeout)

밀리초 단위 최대 시간입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

---

### setExtraHTTPHeaders[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-extra-http-headers "Direct link to setExtraHTTPHeaders")

v1.9 이전에 추가됨 browserContext.setExtraHTTPHeaders

추가 HTTP 헤더는 해당 컨텍스트의 모든 페이지가 시작한 모든 요청과 함께 전송됩니다. 이 헤더들은 [page.setExtraHTTPHeaders()](https://playwright.dev/docs/api/class-page#page-set-extra-http-headers)로 설정한 페이지별 추가 HTTP 헤더와 병합됩니다. 페이지가 특정 헤더를 재정의하면 브라우저 컨텍스트 헤더 값 대신 페이지별 헤더 값이 사용됩니다.

note

[browserContext.setExtraHTTPHeaders()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-extra-http-headers)는 나가는 요청의 헤더 순서를 보장하지 않습니다.

**사용법**

```
    await browserContext.setExtraHTTPHeaders(headers);

```

**인수**

- `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-extra-http-headers-option-headers)

모든 요청과 함께 전송할 추가 HTTP 헤더를 포함하는 객체입니다. 모든 헤더 값은 문자열이어야 합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-extra-http-headers-return)

---

### setGeolocation[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-geolocation "Direct link to setGeolocation")

v1.9 이전에 추가됨 browserContext.setGeolocation

컨텍스트의 지리적 위치를 설정합니다. `null` 또는 `undefined`를 전달하면 위치를 사용할 수 없는 상태를 에뮬레이션합니다.

**사용법**

```
    await browserContext.setGeolocation({ latitude: 59.95, longitude: 30.31667 });

```

note

브라우저 컨텍스트 페이지가 지리적 위치를 읽을 수 있도록 권한을 부여하려면 [browserContext.grantPermissions()](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions) 사용을 고려하세요.

**인수**

- `geolocation` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-geolocation-option-geolocation)
  - `latitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-90에서 90 사이의 위도입니다.

    * `longitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-180에서 180 사이의 경도입니다.

    * `accuracy` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

0 이상의 정확도 값입니다. 기본값은 `0`입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-geolocation-return)

---

### setOffline[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-offline "Direct link to setOffline")

v1.9 이전에 추가됨 browserContext.setOffline

**사용법**

```
    await browserContext.setOffline(offline);

```

**인수**

- `offline` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-offline-option-offline)

브라우저 컨텍스트에 대해 네트워크 오프라인 상태를 에뮬레이션할지 여부입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-offline-return)

---

### storageState[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state "Direct link to storageState")

v1.9 이전에 추가됨 browserContext.storageState

이 브라우저 컨텍스트의 저장소 상태를 반환하며, 현재 쿠키, 로컬 스토리지 스냅샷, IndexedDB 스냅샷을 포함합니다.

**사용법**

```
    await browserContext.storageState();
    await browserContext.storageState(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `indexedDB` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.51[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state-option-indexed-db)

저장소 상태 스냅샷에 [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)를 포함하려면 `true`로 설정하세요. 애플리케이션이 Firebase Authentication처럼 인증 토큰 저장에 IndexedDB를 사용한다면 이를 활성화하세요.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state-option-path)

저장소 상태를 저장할 파일 경로입니다. [path](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state-option-path)가 상대 경로이면 현재 작업 디렉터리를 기준으로 해석됩니다. 경로를 제공하지 않아도 저장소 상태는 반환되지만 디스크에 저장되지는 않습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state-return)
  - `cookies` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>
    - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `expires` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

초 단위 Unix 시간입니다.

      * `httpOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

      * `secure` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

      * `sameSite` "Strict" | "Lax" | "None"

    * `origins` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `localStorage` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

---

### unroute[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute "Direct link to unroute")

v1.9 이전에 추가됨 browserContext.unroute

[browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route)로 생성한 라우트를 제거합니다. [handler](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-option-handler)를 지정하지 않으면 [url](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-option-url)에 대한 모든 라우트를 제거합니다.

**사용법**

```
    await browserContext.unroute(url);
    await browserContext.unroute(url, handler);

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([URL](https://nodejs.org/api/url.html "URL")):[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-option-url)

[browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route)로 라우팅을 등록할 때 사용한 [URL](https://nodejs.org/api/url.html "URL")을 받는 glob 패턴, 정규식 패턴 또는 predicate입니다.

- `handler` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([Route](https://playwright.dev/docs/api/class-route "Route"), [Request](https://playwright.dev/docs/api/class-request "Request")):[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-option-handler)

[browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route)로 라우팅을 등록할 때 사용하는 선택적 핸들러 함수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-return)

---

### unrouteAll[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-all "Direct link to unrouteAll")

추가된 버전: v1.41 browserContext.unrouteAll

[browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route) 및 [browserContext.routeFromHAR()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route-from-har)로 생성된 모든 라우트를 제거합니다.

**사용법**

```
    await browserContext.unrouteAll();
    await browserContext.unrouteAll(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `behavior` "wait" | "ignoreErrors" | "default" _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-all-option-behavior)

이미 실행 중인 핸들러를 기다릴지 여부와, 핸들러에서 오류가 발생했을 때의 동작을 지정합니다.

      * `'default'` \- 현재 핸들러 호출(있는 경우)이 끝날 때까지 기다리지 않으며, unroute된 핸들러에서 예외가 발생하면 처리되지 않은 오류가 될 수 있습니다.
      * `'wait'` \- 현재 핸들러 호출(있는 경우)이 끝날 때까지 기다립니다.
      * `'ignoreErrors'` \- 현재 핸들러 호출(있는 경우)이 끝날 때까지 기다리지 않으며, unroute 이후 핸들러에서 발생하는 모든 오류를 조용히 잡아냅니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-unroute-all-return)

---

### waitForEvent[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-wait-for-event "Direct link to waitForEvent")

v1.9 이전에 추가됨 browserContext.waitForEvent

이벤트가 발생할 때까지 기다린 뒤 그 값을 predicate 함수에 전달합니다. predicate가 truthy 값을 반환하면 종료됩니다. 이벤트가 발생하기 전에 컨텍스트가 닫히면 오류를 던집니다. 이벤트 데이터 값을 반환합니다.

**사용법**

```
    const pagePromise = context.waitForEvent('page');
    await page.getByRole('button').click();
    const page = await pagePromise;

```

**인수**

- `event` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-wait-for-event-option-event)

이벤트 이름으로, `browserContext.on(event)`에 전달하는 것과 동일합니다.

- `optionsOrPredicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-wait-for-event-option-options-or-predicate)
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")

이벤트 데이터를 받아, 대기가 해제되어야 할 때 truthy 값으로 resolve됩니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

대기할 최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 메서드로 변경할 수 있습니다.

이벤트를 받는 predicate 또는 options 객체를 전달할 수 있습니다. 선택 사항입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") _(optional)_[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-wait-for-event-option-predicate)

이벤트 데이터를 받아, 대기가 해제되어야 할 때 truthy 값으로 resolve됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-wait-for-event-return)

---

## Properties[​](https://playwright.dev/docs/api/class-browsercontext#properties "Direct link to Properties")

### clock[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-clock "Direct link to clock")

추가된 버전: v1.45 browserContext.clock

Playwright는 시계와 시간의 흐름을 모킹할 수 있습니다.

**사용법**

```
    browserContext.clock

```

**타입**

- [Clock](https://playwright.dev/docs/api/class-clock "Clock")

---

### request[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-request "Direct link to request")

추가된 버전: v1.16 browserContext.request

이 컨텍스트와 연결된 API 테스트 헬퍼입니다. 이 API로 수행한 요청은 컨텍스트 쿠키를 사용합니다.

**사용법**

```
    browserContext.request

```

**타입**

- [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")

---

### tracing[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-tracing "Direct link to tracing")

추가된 버전: v1.12 browserContext.tracing

**사용법**

```
    browserContext.tracing

```

**타입**

- [Tracing](https://playwright.dev/docs/api/class-tracing "Tracing")

---

## Events[​](https://playwright.dev/docs/api/class-browsercontext#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-close "Direct link to on('close')")

v1.9 이전에 추가됨 browserContext.on('close')

Browser context가 닫힐 때 발생합니다. 다음 중 하나로 인해 발생할 수 있습니다.

- Browser context가 닫힌 경우
- Browser 애플리케이션이 닫히거나 크래시된 경우
- [browser.close()](https://playwright.dev/docs/api/class-browser#browser-close) 메서드가 호출된 경우

**사용법**

```
    browserContext.on('close', data => {});

```

**이벤트 데이터**

- [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")

---

### on('console')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-console "Direct link to on('console')")

추가된 버전: v1.34 browserContext.on('console')

페이지 내 JavaScript가 `console.log` 또는 `console.dir` 같은 console API 메서드 중 하나를 호출할 때 발생합니다.

`console.log`에 전달된 인수와 페이지 정보는 [ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage") 이벤트 핸들러 인수에서 확인할 수 있습니다.

**사용법**

```
    context.on('console', async msg => {
      const values = [];
      for (const arg of msg.args())
        values.push(await arg.jsonValue());
      console.log(...values);
    });
    await page.evaluate(() => console.log('hello', 5, { foo: 'bar' }));

```

**이벤트 데이터**

- [ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage")

---

### on('dialog')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-dialog "Direct link to on('dialog')")

추가된 버전: v1.34 browserContext.on('dialog')

`alert`, `prompt`, `confirm`, `beforeunload` 같은 JavaScript 다이얼로그가 나타날 때 발생합니다. 리스너는 반드시 [dialog.accept()](https://playwright.dev/docs/api/class-dialog#dialog-accept) 또는 [dialog.dismiss()](https://playwright.dev/docs/api/class-dialog#dialog-dismiss)를 호출해야 합니다. 그렇지 않으면 페이지가 다이얼로그를 기다리며 [freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop#never_blocking)되고, 클릭 같은 동작이 끝나지 않습니다.

**사용법**

```
    context.on('dialog', dialog => {
      dialog.accept();
    });

```

note

[page.on('dialog')](https://playwright.dev/docs/api/class-page#page-event-dialog) 또는 [browserContext.on('dialog')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-dialog) 리스너가 없으면, 모든 다이얼로그는 자동으로 dismiss됩니다.

**이벤트 데이터**

- [Dialog](https://playwright.dev/docs/api/class-dialog "Dialog")

---

### on('page')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-page "Direct link to on('page')")

v1.9 이전에 추가됨 browserContext.on('page')

BrowserContext에서 새 Page가 생성될 때 이벤트가 발생합니다. 페이지는 아직 로딩 중일 수 있습니다. 이 이벤트는 팝업 페이지에도 발생합니다. 특정 페이지와 관련된 팝업 이벤트를 받으려면 [page.on('popup')](https://playwright.dev/docs/api/class-page#page-event-popup)도 참고하세요.

페이지를 사용할 수 있는 가장 이른 시점은 초기 url로 이동한 시점입니다. 예를 들어 `window.open('http://example.com')`으로 팝업을 열면, "<http://example.com>"에 대한 네트워크 요청이 완료되고 응답이 팝업에서 로딩되기 시작할 때 이 이벤트가 발생합니다. 이 네트워크 요청을 라우팅/리스닝하려면 [Page](https://playwright.dev/docs/api/class-page "Page")의 유사 메서드 대신 각각 [browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route)와 [browserContext.on('request')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request)를 사용하세요.

```
    const newPagePromise = context.waitForEvent('page');
    await page.getByText('open new page').click();
    const newPage = await newPagePromise;
    console.log(await newPage.evaluate('location.href'));

```

note

페이지가 특정 상태에 도달할 때까지 기다리려면 [page.waitForLoadState()](https://playwright.dev/docs/api/class-page#page-wait-for-load-state)를 사용하세요(대부분의 경우 필요하지 않습니다).

**사용법**

```
    browserContext.on('page', data => {});

```

**이벤트 데이터**

- [Page](https://playwright.dev/docs/api/class-page "Page")

---

### on('request')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request "Direct link to on('request')")

추가된 버전: v1.12 browserContext.on('request')

이 컨텍스트를 통해 생성된 모든 페이지에서 요청이 발생할 때 이벤트가 발생합니다. [request](https://playwright.dev/docs/api/class-request "Request") 객체는 읽기 전용입니다. 특정 페이지의 요청만 들으려면 [page.on('request')](https://playwright.dev/docs/api/class-page#page-event-request)를 사용하세요.

요청을 가로채서 변경하려면 [browserContext.route()](https://playwright.dev/docs/api/class-browsercontext#browser-context-route) 또는 [page.route()](https://playwright.dev/docs/api/class-page#page-route)를 참고하세요.

**사용법**

```
    browserContext.on('request', data => {});

```

**이벤트 데이터**

- [Request](https://playwright.dev/docs/api/class-request "Request")

---

### on('requestfailed')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request-failed "Direct link to on('requestfailed')")

추가된 버전: v1.12 browserContext.on('requestfailed')

예를 들어 타임아웃으로 인해 요청이 실패하면 이벤트가 발생합니다. 특정 페이지의 실패한 요청만 들으려면 [page.on('requestfailed')](https://playwright.dev/docs/api/class-page#page-event-request-failed)를 사용하세요.

note

404 또는 503과 같은 HTTP 오류 응답도 HTTP 관점에서는 여전히 성공적인 응답이므로, 요청은 [browserContext.on('requestfinished')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request-finished) 이벤트로 완료되며 [browserContext.on('requestfailed')](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request-failed)로 완료되지 않습니다.

**사용법**

```
    browserContext.on('requestfailed', data => {});

```

**이벤트 데이터**

- [Request](https://playwright.dev/docs/api/class-request "Request")

---

### on('requestfinished')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-request-finished "Direct link to on('requestfinished')")

추가된 버전: v1.12 browserContext.on('requestfinished')

응답 본문 다운로드가 끝난 뒤 요청이 성공적으로 완료되면 발생합니다. 성공적인 응답의 이벤트 순서는 `request`, `response`, `requestfinished`입니다. 특정 페이지의 성공한 요청을 수신하려면 [page.on('requestfinished')](https://playwright.dev/docs/api/class-page#page-event-request-finished)를 사용하세요.

**사용법**

```
    browserContext.on('requestfinished', data => {});

```

**이벤트 데이터**

- [Request](https://playwright.dev/docs/api/class-request "Request")

---

### on('response')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-response "Direct link to on('response')")

추가된 버전: v1.12 browserContext.on('response')

요청에 대한 [response](https://playwright.dev/docs/api/class-response "Response") 상태와 헤더를 수신하면 발생합니다. 성공적인 응답의 이벤트 순서는 `request`, `response`, `requestfinished`입니다. 특정 페이지의 응답 이벤트를 수신하려면 [page.on('response')](https://playwright.dev/docs/api/class-page#page-event-response)를 사용하세요.

**사용법**

```
    browserContext.on('response', data => {});

```

**이벤트 데이터**

- [Response](https://playwright.dev/docs/api/class-response "Response")

---

### on('serviceworker')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-service-worker "Direct link to on('serviceworker')")

추가된 버전: v1.11 browserContext.on('serviceworker')

note

서비스 워커는 Chromium 기반 브라우저에서만 지원됩니다.

컨텍스트에서 새 서비스 워커가 생성되면 발생합니다.

**사용법**

```
    browserContext.on('serviceworker', data => {});

```

**이벤트 데이터**

- [Worker](https://playwright.dev/docs/api/class-worker "Worker")

---

### on('weberror')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-web-error "Direct link to on('weberror')")

추가된 버전: v1.38 browserContext.on('weberror')

이 컨텍스트의 모든 페이지에서 예외가 처리되지 않은 상태로 남으면 발생합니다. 특정 페이지의 오류를 수신하려면 대신 [page.on('pageerror')](https://playwright.dev/docs/api/class-page#page-event-page-error)를 사용하세요.

**사용법**

```
    browserContext.on('weberror', data => {});

```

**이벤트 데이터**

- [WebError](https://playwright.dev/docs/api/class-weberror "WebError")

---

## Deprecated[​](https://playwright.dev/docs/api/class-browsercontext#deprecated "Direct link to Deprecated")

### on('backgroundpage')[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-event-background-page "Direct link to on('backgroundpage')")

추가된 버전: v1.11 browserContext.on('backgroundpage')

사용 중단됨

백그라운드 페이지는 Manifest V2 확장 프로그램과 함께 Chromium에서 제거되었습니다.

이 이벤트는 발생하지 않습니다.

**사용법**

```
    browserContext.on('backgroundpage', data => {});

```

**이벤트 데이터**

- [Page](https://playwright.dev/docs/api/class-page "Page")

---

### backgroundPages[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-background-pages "Direct link to backgroundPages")

추가된 버전: v1.11 browserContext.backgroundPages

사용 중단됨

백그라운드 페이지는 Manifest V2 확장 프로그램과 함께 Chromium에서 제거되었습니다.

빈 목록을 반환합니다.

**사용법**

```
    browserContext.backgroundPages();

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-background-pages-return)

---

### setHTTPCredentials[​](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-http-credentials "Direct link to setHTTPCredentials")

v1.9 이전에 추가됨 browserContext.setHTTPCredentials

사용 중단됨

브라우저는 인증이 성공한 후 자격 증명을 캐시할 수 있습니다. 대신 새 브라우저 컨텍스트를 생성하세요.

**사용법**

```
    await browserContext.setHTTPCredentials(httpCredentials);

```

**인수**

- `httpCredentials` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-http-credentials-option-http-credentials)
  - `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

  - `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-http-credentials-return)
