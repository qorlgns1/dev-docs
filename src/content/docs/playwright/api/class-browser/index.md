---
title: "Browser"
description: "Browser는 browserType.launch()를 통해 생성됩니다. Browser를 사용해 Page를 만드는 예시는 다음과 같습니다:"
---

Source URL: https://playwright.dev/docs/api/class-browser

# Browser | Playwright

Browser는 [browserType.launch()](https://playwright.dev/docs/api/class-browsertype#browser-type-launch)를 통해 생성됩니다. [Browser](https://playwright.dev/docs/api/class-browser "Browser")를 사용해 [Page](https://playwright.dev/docs/api/class-page "Page")를 만드는 예시는 다음과 같습니다:

```
    const { firefox } = require('playwright');  // Or 'chromium' or 'webkit'.

    (async () => {
      const browser = await firefox.launch();
      const page = await browser.newPage();
      await page.goto('https://example.com');
      await browser.close();
    })();

```

---

## 메서드[​](https://playwright.dev/docs/api/class-browser#methods "Direct link to Methods")

### browserType[​](https://playwright.dev/docs/api/class-browser#browser-browser-type "Direct link to browserType")

추가됨: v1.23 browser.browserType

이 브라우저가 속한 브라우저 타입(chromium, firefox 또는 webkit)을 가져옵니다.

**사용법**

```
    browser.browserType();

```

**반환값**

- [BrowserType](https://playwright.dev/docs/api/class-browsertype "BrowserType")[#](https://playwright.dev/docs/api/class-browser#browser-browser-type-return)

---

### close[​](https://playwright.dev/docs/api/class-browser#browser-close "Direct link to close")

v1.9 이전에 추가됨 browser.close

이 브라우저를 [browserType.launch()](https://playwright.dev/docs/api/class-browsertype#browser-type-launch)로 얻은 경우, 브라우저와 그 안의 모든 페이지(열려 있었다면)를 닫습니다.

이 브라우저에 연결된 경우, 이 브라우저에 속한 생성된 모든 컨텍스트를 정리하고 브라우저 서버와의 연결을 끊습니다.

참고

이는 브라우저를 강제 종료하는 것과 유사합니다. 페이지를 정상적으로 닫고 페이지 종료 이벤트를 확실히 받으려면, [browser.close()](https://playwright.dev/docs/api/class-browser#browser-close)를 호출하기 **전에** [browser.newContext()](https://playwright.dev/docs/api/class-browser#browser-new-context)로 명시적으로 생성한 모든 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext") 인스턴스에서 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 호출하세요.

[Browser](https://playwright.dev/docs/api/class-browser "Browser") 객체 자체는 dispose된 것으로 간주되며 더 이상 사용할 수 없습니다.

**사용법**

```
    await browser.close();
    await browser.close(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `reason` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_ 추가됨: v1.40[#](https://playwright.dev/docs/api/class-browser#browser-close-option-reason)

브라우저 종료로 인해 중단된 작업들에 보고될 이유입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browser#browser-close-return)

---

### contexts[​](https://playwright.dev/docs/api/class-browser#browser-contexts "Direct link to contexts")

v1.9 이전에 추가됨 browser.contexts

현재 열려 있는 모든 브라우저 컨텍스트의 배열을 반환합니다. 새로 생성된 브라우저에서는 브라우저 컨텍스트가 0개 반환됩니다.

**사용법**

```
    const browser = await pw.webkit.launch();
    console.log(browser.contexts().length); // prints `0`

    const context = await browser.newContext();
    console.log(browser.contexts().length); // prints `1`

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")>[#](https://playwright.dev/docs/api/class-browser#browser-contexts-return)

---

### isConnected[​](https://playwright.dev/docs/api/class-browser#browser-is-connected "Direct link to isConnected")

v1.9 이전에 추가됨 browser.isConnected

브라우저가 연결되어 있는지를 나타냅니다.

**사용법**

```
    browser.isConnected();

```

**반환값**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-browser#browser-is-connected-return)

---

### newBrowserCDPSession[​](https://playwright.dev/docs/api/class-browser#browser-new-browser-cdp-session "Direct link to newBrowserCDPSession")

추가됨: v1.11 browser.newBrowserCDPSession

참고

CDP 세션은 Chromium 기반 브라우저에서만 지원됩니다.

새로 생성된 브라우저 세션을 반환합니다.

**사용법**

```
    await browser.newBrowserCDPSession();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[CDPSession](https://playwright.dev/docs/api/class-cdpsession "CDPSession")>[#](https://playwright.dev/docs/api/class-browser#browser-new-browser-cdp-session-return)

---

### newContext[​](https://playwright.dev/docs/api/class-browser#browser-new-context "Direct link to newContext")

v1.9 이전에 추가됨 browser.newContext

새 브라우저 컨텍스트를 생성합니다. 다른 브라우저 컨텍스트와 쿠키/캐시를 공유하지 않습니다.

참고

이 메서드를 직접 사용해 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")를 생성하는 경우, 코드에서 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext") 사용이 끝났을 때 그리고 [browser.close()](https://playwright.dev/docs/api/class-browser#browser-close)를 호출하기 전에, 반환된 컨텍스트를 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)로 명시적으로 닫는 것이 모범 사례입니다. 이렇게 하면 `context`가 정상적으로 닫히고 HAR 및 비디오 같은 아티팩트가 완전히 flush되어 저장됩니다.

**사용법**

```
    (async () => {
      const browser = await playwright.firefox.launch();  // Or 'chromium' or 'webkit'.
      // Create a new incognito browser context.
      const context = await browser.newContext();
      // Create a new page in a pristine context.
      const page = await context.newPage();
      await page.goto('https://example.com');

      // Gracefully close up everything
      await context.close();
      await browser.close();
    })();

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `acceptDownloads` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-accept-downloads)

모든 첨부 파일을 자동으로 다운로드할지 여부입니다. 기본값은 `true`이며 모든 다운로드를 허용합니다.

    * `baseURL` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url)

[page.goto()](https://playwright.dev/docs/api/class-page#page-goto), [page.route()](https://playwright.dev/docs/api/class-page#page-route), [page.waitForURL()](https://playwright.dev/docs/api/class-page#page-wait-for-url), [page.waitForRequest()](https://playwright.dev/docs/api/class-page#page-wait-for-request), 또는 [page.waitForResponse()](https://playwright.dev/docs/api/class-page#page-wait-for-response)를 사용할 때, 대응 URL을 만들기 위해 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 사용하여 base URL을 고려합니다. 기본적으로 설정되지 않습니다. 예시:

      * baseURL: `http://localhost:3000`이고 `/bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다
      * baseURL: `http://localhost:3000/foo/`이고 `./bar.html`로 이동하면 `http://localhost:3000/foo/bar.html`이 됩니다
      * baseURL: `http://localhost:3000/foo`(끝에 슬래시 없음)이고 `./bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다
    * `bypassCSP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-bypass-csp)

페이지의 Content-Security-Policy 우회를 켜거나 끕니다. 기본값은 `false`입니다.

    * `clientCertificates` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(선택 사항)_ 추가됨: 1.46[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-client-certificates)

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

인증서가 유효한 정확한 origin입니다. Origin에는 `https` 프로토콜, 호스트명, 그리고 선택적 포트가 포함됩니다.

      * `certPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

PEM 형식 인증서 파일의 경로입니다.

      * `cert` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(선택 사항)_

PEM 형식 인증서의 직접 값입니다.

      * `keyPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

PEM 형식 개인 키 파일의 경로입니다.

      * `key` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(선택 사항)_

PEM 형식 개인 키의 직접 값입니다.

      * `pfxPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

PFX 또는 PKCS12로 인코딩된 개인 키 및 인증서 체인 파일의 경로입니다.

      * `pfx` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(선택 사항)_

PFX 또는 PKCS12로 인코딩된 개인 키 및 인증서 체인의 직접 값입니다.

      * `passphrase` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

개인 키(PEM 또는 PFX)의 암호입니다.

TLS 클라이언트 인증을 사용하면 서버가 클라이언트 인증서를 요청하고 검증할 수 있습니다.

**세부 정보**

사용할 클라이언트 인증서 배열입니다. 각 인증서 객체에는 `certPath`와 `keyPath`를 함께 제공하거나, `pfxPath` 하나만 제공하거나, 해당 직접 값(`cert`와 `key` 또는 `pfx`)을 제공해야 합니다. 인증서가 암호화된 경우 선택적으로 `passphrase` 속성을 제공해야 합니다. `origin` 속성에는 인증서가 유효한 요청 origin과 정확히 일치하는 값을 제공해야 합니다.

클라이언트 인증서 인증은 최소 하나의 클라이언트 인증서가 제공될 때만 활성화됩니다. 서버가 보내는 모든 클라이언트 인증서를 거부하려면, 방문하려는 어떤 도메인과도 일치하지 않는 `origin`을 가진 클라이언트 인증서를 제공해야 합니다.

참고

macOS에서 WebKit을 사용할 때 `localhost` 접근 시 클라이언트 인증서를 가져오지 못합니다. `localhost`를 `local.playwright`로 바꾸면 동작하게 할 수 있습니다.

    * `colorScheme` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "light" | "dark" | "no-preference" _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-color-scheme)

[prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) 미디어 기능을 에뮬레이션하며, 지원 값은 `'light'`와 `'dark'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'light'`입니다.

    * `contrast` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "no-preference" | "more" _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-contrast)

`'prefers-contrast'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'no-preference'`, `'more'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `deviceScaleFactor` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-device-scale-factor)

디바이스 스케일 팩터(dpr로 생각할 수 있음)를 지정합니다. 기본값은 `1`입니다. [device scale factor를 사용한 디바이스 에뮬레이션](https://playwright.dev/docs/emulation#devices)에 대해 자세히 알아보세요.

- `extraHTTPHeaders` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-extra-http-headers)

모든 요청과 함께 전송할 추가 HTTP 헤더를 포함하는 객체입니다. 기본값은 없습니다.

    * `forcedColors` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "active" | "none" _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-forced-colors)

`'forced-colors'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'active'`, `'none'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'none'`입니다.

    * `geolocation` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-geolocation)

      * `latitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-90에서 90 사이의 위도입니다.

      * `longitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-180에서 180 사이의 경도입니다.

      * `accuracy` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_

0 이상의 정확도 값입니다. 기본값은 `0`입니다.

    * `hasTouch` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-has-touch)

뷰포트가 터치 이벤트를 지원하는지 지정합니다. 기본값은 false입니다. [모바일 에뮬레이션](https://playwright.dev/docs/emulation#devices)에 대해 더 알아보세요.

    * `httpCredentials` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-http-credentials)

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

특정 origin (scheme://host:port)에 대해서만 http 자격 증명을 전송하도록 제한합니다.

      * `send` "unauthorized" | "always" _(선택 사항)_

이 옵션은 해당 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")에서 전송되는 요청에만 적용되며 브라우저에서 전송되는 요청에는 영향을 주지 않습니다. `'always'` \- 기본 인증 자격 증명이 포함된 `Authorization` 헤더가 각 API 요청과 함께 전송됩니다. `'unauthorized` \- `WWW-Authenticate` 헤더를 포함한 401 (Unauthorized) 응답을 받은 경우에만 자격 증명이 전송됩니다. 기본값은 `'unauthorized'`입니다.

[HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)을 위한 자격 증명입니다. origin을 지정하지 않으면, 인증되지 않은 응답 시 사용자 이름과 비밀번호가 모든 서버로 전송됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-ignore-https-errors)

네트워크 요청을 보낼 때 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `isMobile` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-is-mobile)

`meta viewport` 태그를 고려하고 터치 이벤트를 활성화할지 여부입니다. isMobile은 device의 일부이므로 실제로 수동 설정할 필요가 없습니다. 기본값은 `false`이며 Firefox에서는 지원되지 않습니다. [모바일 에뮬레이션](https://playwright.dev/docs/emulation#ismobile)에 대해 더 알아보세요.

    * `javaScriptEnabled` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-java-script-enabled)

컨텍스트에서 JavaScript를 활성화할지 여부입니다. 기본값은 `true`입니다. [JavaScript 비활성화](https://playwright.dev/docs/emulation#javascript-enabled)에 대해 더 알아보세요.

    * `locale` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-locale)

사용자 로캘(예: `en-GB`, `de-DE` 등)을 지정합니다. 로캘은 `navigator.language` 값, `Accept-Language` 요청 헤더 값, 숫자 및 날짜 서식 규칙에 영향을 줍니다. 기본값은 시스템 기본 로캘입니다. 에뮬레이션에 대한 자세한 내용은 [emulation guide](https://playwright.dev/docs/emulation#locale--timezone)를 참고하세요.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-logger)

사용 중단됨

logger가 수신하는 로그는 불완전합니다. 대신 tracing을 사용하세요.

Playwright 로깅을 위한 Logger sink입니다.

    * `offline` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-offline)

네트워크 오프라인 상태를 에뮬레이션할지 여부입니다. 기본값은 `false`입니다. [네트워크 에뮬레이션](https://playwright.dev/docs/emulation#offline)에 대해 더 알아보세요.

    * `permissions` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-permissions)

이 컨텍스트의 모든 페이지에 부여할 권한 목록입니다. 자세한 내용은 [browserContext.grantPermissions()](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions)를 참고하세요. 기본값은 없습니다.

    * `proxy` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-proxy)

      * `server` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

모든 요청에 사용할 프록시입니다. HTTP 및 SOCKS 프록시를 지원하며, 예를 들어 `http://myproxy.com:3128` 또는 `socks5://myproxy.com:3128` 형식을 사용할 수 있습니다. 축약형 `myproxy.com:3128`은 HTTP 프록시로 간주됩니다.

      * `bypass` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

프록시를 우회할 도메인을 쉼표로 구분해 지정하는 선택 항목입니다. 예: `".com, chromium.org, .domain.com"`.

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 사용자 이름입니다.

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 비밀번호입니다.

이 컨텍스트에서 사용할 네트워크 프록시 설정입니다. 기본값은 없습니다.

    * `recordHar` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-record-har)

      * `omitContent` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_

HAR에서 요청 콘텐츠를 생략할지 제어하는 선택적 설정입니다. 기본값은 `false`입니다. 사용 중단되었으며 대신 `content` 정책을 사용하세요.

      * `content` "omit" | "embed" | "attach" _(선택 사항)_

리소스 콘텐츠 관리를 제어하는 선택적 설정입니다. `omit`을 지정하면 콘텐츠가 저장되지 않습니다. `attach`를 지정하면 리소스가 별도 파일 또는 ZIP 아카이브 항목으로 저장됩니다. `embed`를 지정하면 HAR 사양에 따라 콘텐츠가 HAR 파일 안에 인라인으로 저장됩니다. 기본값은 `.zip` 출력 파일의 경우 `attach`, 그 외 모든 파일 확장자의 경우 `embed`입니다.

      * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

HAR 파일을 기록할 파일 시스템 경로입니다. 파일 이름이 `.zip`으로 끝나면 기본적으로 `content: 'attach'`가 사용됩니다.

      * `mode` "full" | "minimal" _(선택 사항)_

`minimal`로 설정하면 HAR에서 라우팅에 필요한 정보만 기록합니다. 이 경우 HAR에서 재생할 때 사용되지 않는 크기, 타이밍, 페이지, 쿠키, 보안 및 기타 HAR 정보 유형은 생략됩니다. 기본값은 `full`입니다.

      * `urlFilter` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(선택 사항)_

HAR에 저장할 요청을 필터링하는 glob 또는 regex 패턴입니다. 컨텍스트 옵션을 통해 [baseURL](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url)이 제공되었고 전달된 URL이 경로인 경우, [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 통해 병합됩니다. 기본값은 없습니다.

모든 페이지에 대해 `recordHar.path` 파일로 [HAR](http://www.softwareishard.com/blog/har-12-spec) 기록을 활성화합니다. 지정하지 않으면 HAR는 기록되지 않습니다. HAR가 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `recordVideo` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-record-video)

      * `dir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

비디오를 저장할 디렉터리 경로입니다.

      * `size` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_

        * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

        * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

기록되는 비디오의 선택적 크기입니다. 지정하지 않으면 크기는 `viewport`를 800x800에 맞게 축소한 값과 동일합니다. `viewport`를 명시적으로 설정하지 않으면 비디오 크기의 기본값은 800x450입니다. 각 페이지의 실제 화면은 필요 시 지정한 크기에 맞도록 축소됩니다.

모든 페이지에 대해 `recordVideo.dir` 디렉터리로 비디오 기록을 활성화합니다. 지정하지 않으면 비디오는 기록되지 않습니다. 비디오가 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `reducedMotion` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "reduce" | "no-preference" _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-reduced-motion)

`'prefers-reduced-motion'` 미디어 기능을 에뮬레이션하며, 지원되는 값은 `'reduce'`, `'no-preference'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `screen` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-screen)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

웹 페이지 내부에서 `window.screen`을 통해 접근 가능한 일관된 window screen 크기를 에뮬레이션합니다. [viewport](https://playwright.dev/docs/api/class-browser#browser-new-context-option-viewport)가 설정된 경우에만 사용됩니다.

    * `serviceWorkers` "allow" | "block" _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-service-workers)

사이트가 Service workers를 등록할 수 있도록 허용할지 여부입니다. 기본값은 `'allow'`입니다.

      * `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)를 등록할 수 있습니다.
      * `'block'`: Playwright가 Service Workers의 모든 등록을 차단합니다.
    * `storageState` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-storage-state)

      * `cookies` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

Domain과 path는 필수입니다. 쿠키를 모든 하위 도메인에도 적용하려면 domain 앞에 점을 붙이세요. 예: ".example.com"

        * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

Domain과 path는 필수입니다.

        * `expires` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

초 단위 Unix 시간입니다.

        * `httpOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

        * `secure` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

        * `sameSite` "Strict" | "Lax" | "None"

sameSite 플래그

context에 설정할 쿠키

      * `origins` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `localStorage` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

          * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

          * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

context에 설정할 localStorage

[storage state와 auth](https://playwright.dev/docs/auth)에 대해 더 알아보세요.

주어진 storage state로 context를 채웁니다. 이 옵션은 [browserContext.storageState()](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state)로 얻은 로그인 정보를 사용해 context를 초기화하는 데 사용할 수 있습니다.

    * `strictSelectors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-strict-selectors)

`true`로 설정하면 이 context에서 strict selectors 모드를 활성화합니다. strict selectors 모드에서는 단일 대상 DOM 요소를 전제로 하는 모든 selector 작업이 selector와 일치하는 요소가 둘 이상일 때 예외를 발생시킵니다. 이 옵션은 Locator API에는 영향을 주지 않습니다(Locator는 항상 strict입니다). 기본값은 `false`입니다. strict 모드에 대한 자세한 내용은 [Locator](https://playwright.dev/docs/api/class-locator "Locator")를 참고하세요.

    * `timezoneId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-timezone-id)

context의 시간대를 변경합니다. 지원되는 timezone ID 목록은 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)를 참고하세요. 기본값은 시스템 시간대입니다.

    * `userAgent` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-user-agent)

이 context에서 사용할 특정 user agent입니다.

    * `videoSize` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-video-size)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-browser#browser-new-context-option-record-video)를 사용하세요.

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

    * `videosPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-videos-path)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-browser#browser-new-context-option-record-video)를 사용하세요.

    * `viewport` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-context-option-viewport)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

각 페이지에 대해 일관된 viewport를 에뮬레이션합니다. 기본값은 1280x720 viewport입니다. 일관된 viewport 에뮬레이션을 비활성화하려면 `null`을 사용하세요. [viewport emulation](https://playwright.dev/docs/emulation#viewport)에 대해 더 알아보세요.

참고

`null` 값은 기본 프리셋 사용을 해제하고, viewport가 운영 체제에서 정의한 호스트 창 크기에 의존하도록 만듭니다. 이로 인해 테스트 실행이 비결정적이 됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")>[#](https://playwright.dev/docs/api/class-browser#browser-new-context-return)

---

### newPage[​](https://playwright.dev/docs/api/class-browser#browser-new-page "Direct link to newPage")

v1.9 이전에 추가됨 browser.newPage

새 browser context에서 새 페이지를 생성합니다. 이 페이지를 닫으면 context도 함께 닫힙니다.

이것은 편의 API로, 단일 페이지 시나리오와 짧은 스니펫에서만 사용해야 합니다. 프로덕션 코드와 테스트 프레임워크는 정확한 수명을 제어하기 위해 [browser.newContext()](https://playwright.dev/docs/api/class-browser#browser-new-context)를 명시적으로 생성한 다음 [browserContext.newPage()](https://playwright.dev/docs/api/class-browsercontext#browser-context-new-page)를 호출해야 합니다.

**사용법**

```
    await browser.newPage();
    await browser.newPage(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `acceptDownloads` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-accept-downloads)

모든 첨부 파일을 자동으로 다운로드할지 여부입니다. 기본값은 `true`이며, 모든 다운로드를 허용합니다.

    * `baseURL` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-base-url)

[page.goto()](https://playwright.dev/docs/api/class-page#page-goto), [page.route()](https://playwright.dev/docs/api/class-page#page-route), [page.waitForURL()](https://playwright.dev/docs/api/class-page#page-wait-for-url), [page.waitForRequest()](https://playwright.dev/docs/api/class-page#page-wait-for-request), 또는 [page.waitForResponse()](https://playwright.dev/docs/api/class-page#page-wait-for-response)를 사용할 때, 해당 URL을 구성하기 위해 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 사용하여 base URL을 고려합니다. 기본적으로 설정되어 있지 않습니다. 예시:

      * baseURL: `http://localhost:3000`이고 `/bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다.
      * baseURL: `http://localhost:3000/foo/`이고 `./bar.html`로 이동하면 `http://localhost:3000/foo/bar.html`이 됩니다.
      * baseURL: `http://localhost:3000/foo`(후행 슬래시 없음)이고 `./bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다.
    * `bypassCSP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-bypass-csp)

페이지의 Content-Security-Policy 우회를 전환합니다. 기본값은 `false`입니다.

    * `clientCertificates` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_ 추가된 버전: 1.46[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-client-certificates)

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

인증서가 유효한 정확한 origin입니다. origin에는 `https` 프로토콜, 호스트 이름, 그리고 선택적으로 포트가 포함됩니다.

      * `certPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PEM 형식 인증서 파일의 경로입니다.

      * `cert` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PEM 형식 인증서의 직접 값입니다.

      * `keyPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PEM 형식 개인 키 파일의 경로입니다.

- `key` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PEM 형식 개인 키의 직접 값입니다.

      * `pfxPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PFX 또는 PKCS12로 인코딩된 개인 키와 인증서 체인의 경로입니다.

      * `pfx` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PFX 또는 PKCS12로 인코딩된 개인 키와 인증서 체인의 직접 값입니다.

      * `passphrase` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

개인 키(PEM 또는 PFX)에 대한 패스프레이즈입니다.

TLS 클라이언트 인증을 사용하면 서버가 클라이언트 인증서를 요청하고 검증할 수 있습니다.

**세부 정보**

사용할 클라이언트 인증서 배열입니다. 각 인증서 객체에는 `certPath`와 `keyPath`를 모두 지정하거나, 단일 `pfxPath`를 지정하거나, 해당 직접 값(`cert`와 `key` 또는 `pfx`)을 지정해야 합니다. 인증서가 암호화되어 있다면 선택적으로 `passphrase` 속성을 제공해야 합니다. `origin` 속성은 인증서가 유효한 요청 origin과 정확히 일치하도록 제공해야 합니다.

클라이언트 인증서가 하나 이상 제공될 때만 클라이언트 인증서 인증이 활성화됩니다. 서버가 보내는 모든 클라이언트 인증서를 거부하려면, 방문하려는 어떤 도메인과도 일치하지 않는 `origin`을 가진 클라이언트 인증서를 제공해야 합니다.

참고

macOS에서 WebKit을 사용할 때 `localhost`에 접근하면 클라이언트 인증서를 가져오지 못합니다. `localhost`를 `local.playwright`로 바꾸면 동작하게 할 수 있습니다.

    * `colorScheme` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "light" | "dark" | "no-preference" _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-color-scheme)

[prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) 미디어 기능을 에뮬레이션하며, 지원 값은 `'light'`와 `'dark'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'light'`입니다.

    * `contrast` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "no-preference" | "more" _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-contrast)

`'prefers-contrast'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'no-preference'`, `'more'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `deviceScaleFactor` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-device-scale-factor)

장치 스케일 팩터(`dpr`로 생각할 수 있음)를 지정합니다. 기본값은 `1`입니다. [emulating devices with device scale factor](https://playwright.dev/docs/emulation#devices)에서 자세히 알아보세요.

    * `extraHTTPHeaders` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-extra-http-headers)

모든 요청과 함께 전송할 추가 HTTP 헤더를 담은 객체입니다. 기본값은 없음입니다.

    * `forcedColors` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "active" | "none" _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-forced-colors)

`'forced-colors'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'active'`, `'none'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'none'`입니다.

    * `geolocation` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-geolocation)

      * `latitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-90에서 90 사이의 위도입니다.

      * `longitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-180에서 180 사이의 경도입니다.

      * `accuracy` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

음수가 아닌 정확도 값입니다. 기본값은 `0`입니다.

    * `hasTouch` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-has-touch)

뷰포트가 터치 이벤트를 지원하는지 지정합니다. 기본값은 false입니다. [mobile emulation](https://playwright.dev/docs/emulation#devices)에서 자세히 알아보세요.

    * `httpCredentials` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-http-credentials)

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

특정 origin(scheme://host:port)으로 HTTP 자격 증명 전송을 제한합니다.

      * `send` "unauthorized" | "always" _(optional)_

이 옵션은 해당 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")에서 전송하는 요청에만 적용되며 브라우저에서 전송하는 요청에는 영향을 주지 않습니다. `'always'` \- 기본 인증 자격 증명이 포함된 `Authorization` 헤더가 각 API 요청과 함께 전송됩니다. `'unauthorized` \- `WWW-Authenticate` 헤더가 포함된 401(Unauthorized) 응답을 받았을 때만 자격 증명이 전송됩니다. 기본값은 `'unauthorized'`입니다.

[HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)을 위한 자격 증명입니다. origin을 지정하지 않으면 unauthorized 응답 시 사용자 이름과 비밀번호가 모든 서버로 전송됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `isMobile` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-is-mobile)

`meta viewport` 태그를 고려하고 터치 이벤트를 활성화할지 여부입니다. isMobile은 device의 일부이므로 실제로 수동 설정할 필요가 없습니다. 기본값은 `false`이며 Firefox에서는 지원되지 않습니다. [mobile emulation](https://playwright.dev/docs/emulation#ismobile)에서 자세히 알아보세요.

    * `javaScriptEnabled` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-java-script-enabled)

context에서 JavaScript를 활성화할지 여부입니다. 기본값은 `true`입니다. [disabling JavaScript](https://playwright.dev/docs/emulation#javascript-enabled)에서 자세히 알아보세요.

    * `locale` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-locale)

예: `en-GB`, `de-DE`처럼 사용자 로캘을 지정합니다. Locale은 `navigator.language` 값, `Accept-Language` 요청 헤더 값, 숫자 및 날짜 서식 규칙에 영향을 줍니다. 기본값은 시스템 기본 로캘입니다. 에뮬레이션에 대한 자세한 내용은 [emulation guide](https://playwright.dev/docs/emulation#locale--timezone)를 참고하세요.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-logger)

사용 중단됨

logger가 수신하는 로그는 불완전합니다. 대신 tracing을 사용하세요.

Playwright 로깅을 위한 Logger sink입니다.

    * `offline` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-offline)

네트워크 오프라인 상태를 에뮬레이션할지 여부입니다. 기본값은 `false`입니다. [network emulation](https://playwright.dev/docs/emulation#offline)에서 자세히 알아보세요.

    * `permissions` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-permissions)

이 context의 모든 페이지에 부여할 권한 목록입니다. 자세한 내용은 [browserContext.grantPermissions()](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions)를 참고하세요. 기본값은 없음입니다.

    * `proxy` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-proxy)

      * `server` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

모든 요청에 사용할 프록시입니다. HTTP 및 SOCKS 프록시를 지원하며, 예: `http://myproxy.com:3128` 또는 `socks5://myproxy.com:3128`입니다. 짧은 형식 `myproxy.com:3128`은 HTTP 프록시로 간주됩니다.

      * `bypass` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

프록시를 우회할 선택적 콤마 구분 도메인입니다. 예: `".com, chromium.org, .domain.com"`.

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 사용자 이름입니다.

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 비밀번호입니다.

이 context에서 사용할 네트워크 프록시 설정입니다. 기본값은 없음입니다.

    * `recordHar` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-record-har)

      * `omitContent` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_

HAR에서 요청 콘텐츠를 생략할지 제어하는 선택적 설정입니다. 기본값은 `false`입니다. 사용 중단되었으며, 대신 `content` 정책을 사용하세요.

      * `content` "omit" | "embed" | "attach" _(optional)_

리소스 콘텐츠 관리를 제어하기 위한 선택적 설정입니다. `omit`을 지정하면 콘텐츠가 영속 저장되지 않습니다. `attach`를 지정하면 리소스가 별도 파일 또는 ZIP 아카이브 항목으로 영속 저장됩니다. `embed`를 지정하면 HAR 사양에 따라 콘텐츠가 HAR 파일에 인라인으로 저장됩니다. 기본값은 `.zip` 출력 파일의 경우 `attach`, 그 외 모든 파일 확장자의 경우 `embed`입니다.

      * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

HAR 파일을 기록할 파일시스템 경로입니다. 파일 이름이 `.zip`으로 끝나면 기본적으로 `content: 'attach'`가 사용됩니다.

      * `mode` "full" | "minimal" _(optional)_

`minimal`로 설정하면 HAR에서 라우팅하는 데 필요한 정보만 기록합니다. 이 경우 HAR에서 재생할 때 사용되지 않는 크기, 타이밍, 페이지, 쿠키, 보안 및 기타 HAR 정보는 생략됩니다. 기본값은 `full`입니다.

      * `urlFilter` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_

HAR에 저장할 요청을 필터링하는 glob 또는 regex 패턴입니다. 컨텍스트 옵션을 통해 [baseURL](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url)이 제공되었고 전달된 URL이 경로인 경우, [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 통해 병합됩니다. 기본값은 없음입니다.

모든 페이지에 대해 `recordHar.path` 파일로 [HAR](http://www.softwareishard.com/blog/har-12-spec) 기록을 활성화합니다. 지정하지 않으면 HAR은 기록되지 않습니다. HAR이 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `recordVideo` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-record-video)

      * `dir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

비디오를 저장할 디렉터리 경로입니다.

      * `size` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_

        * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

        * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

녹화된 비디오의 선택적 크기입니다. 지정하지 않으면 크기는 `viewport`를 800x800에 맞도록 축소한 값과 같아집니다. `viewport`가 명시적으로 설정되지 않으면 비디오 크기 기본값은 800x450입니다. 각 페이지의 실제 화면은 필요 시 지정된 크기에 맞도록 축소됩니다.

모든 페이지에 대해 `recordVideo.dir` 디렉터리로 비디오 기록을 활성화합니다. 지정하지 않으면 비디오는 기록되지 않습니다. 비디오가 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `reducedMotion` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "reduce" | "no-preference" _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-reduced-motion)

`'prefers-reduced-motion'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'reduce'`, `'no-preference'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `screen` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-screen)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

웹 페이지 내부에서 `window.screen`을 통해 접근 가능한 일관된 창 화면 크기를 에뮬레이션합니다. [viewport](https://playwright.dev/docs/api/class-browser#browser-new-page-option-viewport)가 설정된 경우에만 사용됩니다.

    * `serviceWorkers` "allow" | "block" _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-service-workers)

사이트의 Service workers 등록 허용 여부입니다. 기본값은 `'allow'`입니다.

      * `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)를 등록할 수 있습니다.
      * `'block'`: Playwright가 Service Workers의 모든 등록을 차단합니다.
    * `storageState` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-storage-state)

      * `cookies` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

Domain과 path는 필수입니다. 쿠키를 모든 하위 도메인에도 적용하려면 다음과 같이 domain 앞에 점을 붙이세요: ".example.com"

        * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

Domain과 path는 필수입니다.

        * `expires` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

초 단위 Unix 시간입니다.

        * `httpOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

        * `secure` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

        * `sameSite` "Strict" | "Lax" | "None"

sameSite 플래그

컨텍스트에 설정할 쿠키입니다.

      * `origins` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `localStorage` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

          * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

          * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

컨텍스트에 설정할 localStorage입니다.

[storage state and auth](https://playwright.dev/docs/auth)에 대해 자세히 알아보세요.

주어진 storage state로 컨텍스트를 채웁니다. 이 옵션은 [browserContext.storageState()](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state)를 통해 얻은 로그인 정보를 사용해 컨텍스트를 초기화할 때 사용할 수 있습니다.

    * `strictSelectors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-strict-selectors)

`true`로 설정하면 이 컨텍스트에 strict selectors 모드가 활성화됩니다. strict selectors 모드에서는 단일 대상 DOM 요소를 전제로 하는 모든 selector 연산이, selector와 일치하는 요소가 둘 이상이면 예외를 발생시킵니다. 이 옵션은 Locator API에는 영향을 주지 않습니다(Locators는 항상 strict입니다). 기본값은 `false`입니다. strict 모드에 대한 자세한 내용은 [Locator](https://playwright.dev/docs/api/class-locator "Locator")를 참고하세요.

    * `timezoneId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-timezone-id)

컨텍스트의 시간대를 변경합니다. 지원되는 timezone ID 목록은 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)를 참고하세요. 기본값은 시스템 시간대입니다.

    * `userAgent` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-user-agent)

이 컨텍스트에서 사용할 특정 user agent입니다.

    * `videoSize` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-video-size)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-browser#browser-new-page-option-record-video)를 사용하세요.

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

    * `videosPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-videos-path)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-browser#browser-new-page-option-record-video)를 사용하세요.

    * `viewport` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browser#browser-new-page-option-viewport)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

각 페이지에 대해 일관된 viewport를 에뮬레이션합니다. 기본값은 1280x720 viewport입니다. 일관된 viewport 에뮬레이션을 비활성화하려면 `null`을 사용하세요. 자세한 내용은 [viewport emulation](https://playwright.dev/docs/emulation#viewport)을 참고하세요.

참고

`null` 값은 기본 프리셋을 사용하지 않도록 하며, viewport가 운영 체제에서 정의한 호스트 창 크기에 따라 달라지게 만듭니다. 이로 인해 테스트 실행이 비결정적이 됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-browser#browser-new-page-return)

---

### removeAllListeners[​](https://playwright.dev/docs/api/class-browser#browser-remove-all-listeners "Direct link to removeAllListeners")

추가됨: v1.47 browser.removeAllListeners

주어진 타입의 모든 리스너를 제거합니다(타입을 지정하지 않으면 등록된 모든 리스너 제거). 비동기 리스너의 완료를 기다리거나, 해당 리스너들에서 이후 발생하는 오류를 무시할 수 있습니다.

**사용법**

```
    await browser.removeAllListeners();
    await browser.removeAllListeners(type, options);

```

**인수**

- `type` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-remove-all-listeners-option-type)
  - `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
    - `behavior` "wait" | "ignoreErrors" | "default" _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-remove-all-listeners-option-behavior)

이미 실행 중인 리스너를 기다릴지 여부와, 리스너가 오류를 던질 때 어떻게 처리할지를 지정합니다:

      * `'default'` \- 현재 리스너 호출(있는 경우)이 끝날 때까지 기다리지 않으며, 리스너가 오류를 던지면 처리되지 않은 오류가 발생할 수 있습니다
      * `'wait'` \- 현재 리스너 호출(있는 경우)이 끝날 때까지 기다립니다
      * `'ignoreErrors'` \- 현재 리스너 호출(있는 경우)이 끝날 때까지 기다리지 않으며, 제거 이후 리스너가 던지는 모든 오류를 조용히 잡아냅니다

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browser#browser-remove-all-listeners-return)

---

### startTracing[​](https://playwright.dev/docs/api/class-browser#browser-start-tracing "Direct link to startTracing")

추가된 버전: v1.11 browser.startTracing

참고

이 API는 저수준의 Chromium 전용 디버깅 도구인 [Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool)을 제어합니다. [Playwright Tracing](https://playwright.dev/docs/trace-viewer)을 제어하는 API는 [여기](https://playwright.dev/docs/api/class-tracing)에서 확인할 수 있습니다.

[browser.startTracing()](https://playwright.dev/docs/api/class-browser#browser-start-tracing) 및 [browser.stopTracing()](https://playwright.dev/docs/api/class-browser#browser-stop-tracing)을 사용해 Chrome DevTools의 성능 패널에서 열 수 있는 트레이스 파일을 만들 수 있습니다.

**사용법**

```
    await browser.startTracing(page, { path: 'trace.json' });
    await page.goto('https://www.google.com');
    await browser.stopTracing();

```

**인수**

- `page` [Page](https://playwright.dev/docs/api/class-page "Page") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-start-tracing-option-page)

선택 사항이며, 지정하면 트레이싱에 해당 페이지의 스크린샷이 포함됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `categories` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-start-tracing-option-categories)

기본값 대신 사용할 사용자 지정 카테고리를 지정합니다.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-start-tracing-option-path)

트레이스 파일을 기록할 경로입니다.

    * `screenshots` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-browser#browser-start-tracing-option-screenshots)

트레이스에 스크린샷을 캡처합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browser#browser-start-tracing-return)

---

### stopTracing[​](https://playwright.dev/docs/api/class-browser#browser-stop-tracing "Direct link to stopTracing")

추가된 버전: v1.11 browser.stopTracing

참고

이 API는 저수준의 Chromium 전용 디버깅 도구인 [Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool)을 제어합니다. [Playwright Tracing](https://playwright.dev/docs/trace-viewer)을 제어하는 API는 [여기](https://playwright.dev/docs/api/class-tracing)에서 확인할 수 있습니다.

트레이스 데이터가 담긴 버퍼를 반환합니다.

**사용법**

```
    await browser.stopTracing();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")>[#](https://playwright.dev/docs/api/class-browser#browser-stop-tracing-return)

---

### version[​](https://playwright.dev/docs/api/class-browser#browser-version "Direct link to version")

v1.9 이전에 추가됨 browser.version

브라우저 버전을 반환합니다.

**사용법**

```
    browser.version();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browser#browser-version-return)

---

## 이벤트[​](https://playwright.dev/docs/api/class-browser#events "Direct link to Events")

### on('disconnected')[​](https://playwright.dev/docs/api/class-browser#browser-event-disconnected "Direct link to on('disconnected')")

v1.9 이전에 추가됨 browser.on('disconnected')

Browser가 브라우저 애플리케이션과의 연결이 끊어졌을 때 발생합니다. 이는 다음 중 하나의 이유로 발생할 수 있습니다:

- 브라우저 애플리케이션이 닫혔거나 충돌했습니다.
- [browser.close()](https://playwright.dev/docs/api/class-browser#browser-close) 메서드가 호출되었습니다.

**사용법**

```
    browser.on('disconnected', data => {});

```

**이벤트 데이터**

- [Browser](https://playwright.dev/docs/api/class-browser "Browser")
