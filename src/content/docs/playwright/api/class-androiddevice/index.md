---
title: "AndroidDevice"
description: "추가: v1.9 androidDevice.close"
---

Source URL: https://playwright.dev/docs/api/class-androiddevice

# AndroidDevice | Playwright

[AndroidDevice](https://playwright.dev/docs/api/class-androiddevice "AndroidDevice")는 실제 하드웨어 또는 에뮬레이션된 연결 디바이스를 나타냅니다. 디바이스는 [android.devices()](https://playwright.dev/docs/api/class-android#android-devices)를 사용해 가져올 수 있습니다.

---

## 메서드[​](https://playwright.dev/docs/api/class-androiddevice#methods "Direct link to Methods")

### close[​](https://playwright.dev/docs/api/class-androiddevice#android-device-close "Direct link to close")

추가: v1.9 androidDevice.close

디바이스 연결을 해제합니다.

**사용법**

```
    await androidDevice.close();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-close-return)

---

### drag[​](https://playwright.dev/docs/api/class-androiddevice#android-device-drag "Direct link to drag")

추가: v1.9 androidDevice.drag

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-drag-option-selector)로 정의된 위젯을 [dest](https://playwright.dev/docs/api/class-androiddevice#android-device-drag-option-dest) 지점으로 드래그합니다.

**사용법**

```
    await androidDevice.drag(selector, dest);
    await androidDevice.drag(selector, dest, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-drag-option-selector)

드래그할 선택자입니다.

- `dest` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-drag-option-dest)
  - `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

  - `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

드래그할 대상 지점입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `speed` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-drag-option-speed)

초당 픽셀 단위 드래그 속도(선택 사항)입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-drag-option-timeout)

최대 대기 시간(밀리초)이며 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-drag-return)

---

### fill[​](https://playwright.dev/docs/api/class-androiddevice#android-device-fill "Direct link to fill")

추가: v1.9 androidDevice.fill

특정 [selector](https://playwright.dev/docs/api/class-androiddevice#android-device-fill-option-selector) 입력 상자에 [text](https://playwright.dev/docs/api/class-androiddevice#android-device-fill-option-text)를 채웁니다.

**사용법**

```
    await androidDevice.fill(selector, text);
    await androidDevice.fill(selector, text, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-fill-option-selector)

채울 선택자입니다.

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-fill-option-text)

입력 상자에 채울 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-fill-option-timeout)

최대 대기 시간(밀리초)이며 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-fill-return)

---

### fling[​](https://playwright.dev/docs/api/class-androiddevice#android-device-fling "Direct link to fling")

추가: v1.9 androidDevice.fling

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-fling-option-selector)로 정의된 위젯을 지정한 [direction](https://playwright.dev/docs/api/class-androiddevice#android-device-fling-option-direction)으로 플링합니다.

**사용법**

```
    await androidDevice.fling(selector, direction);
    await androidDevice.fling(selector, direction, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-fling-option-selector)

플링할 선택자입니다.

- `direction` "down" | "up" | "left" | "right"[#](https://playwright.dev/docs/api/class-androiddevice#android-device-fling-option-direction)

플링 방향입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `speed` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-fling-option-speed)

초당 픽셀 단위 플링 속도(선택 사항)입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-fling-option-timeout)

최대 대기 시간(밀리초)이며 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-fling-return)

---

### info[​](https://playwright.dev/docs/api/class-androiddevice#android-device-info "Direct link to info")

추가: v1.9 androidDevice.info

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-info-option-selector)로 정의된 위젯의 정보를 반환합니다.

**사용법**

```
    await androidDevice.info(selector);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-info-option-selector)

정보를 반환할 선택자입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[AndroidElementInfo]>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-info-return)

---

### installApk[​](https://playwright.dev/docs/api/class-androiddevice#android-device-install-apk "Direct link to installApk")

추가: v1.9 androidDevice.installApk

디바이스에 apk를 설치합니다.

**사용법**

```
    await androidDevice.installApk(file);
    await androidDevice.installApk(file, options);

```

**인수**

- `file` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-install-apk-option-file)

apk 파일 경로 또는 apk 파일 콘텐츠입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `args` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-install-apk-option-args)

`shell:cmd package install` 호출에 전달할 선택적 인수입니다. 기본값은 `-r -t -S`입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-install-apk-return)

---

### launchBrowser[​](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser "Direct link to launchBrowser")

추가: v1.9 androidDevice.launchBrowser

디바이스에서 Chrome 브라우저를 실행하고 해당 persistent context를 반환합니다.

**사용법**

```
    await androidDevice.launchBrowser();
    await androidDevice.launchBrowser(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `acceptDownloads` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-accept-downloads)

모든 첨부 파일을 자동으로 다운로드할지 여부입니다. 기본값은 `true`이며 모든 다운로드를 허용합니다.

    * `args` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_ Added in: v1.29[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-args)

warning

일부 인수는 Playwright 기능을 손상시킬 수 있으므로 사용자 지정 브라우저 인수는 신중하게 사용하세요.

브라우저 인스턴스에 전달할 추가 인수입니다. Chromium 플래그 목록은 [here](https://peter.sh/experiments/chromium-command-line-switches/)에서 확인할 수 있습니다.

    * `baseURL` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-base-url)

[page.goto()](https://playwright.dev/docs/api/class-page#page-goto), [page.route()](https://playwright.dev/docs/api/class-page#page-route), [page.waitForURL()](https://playwright.dev/docs/api/class-page#page-wait-for-url), [page.waitForRequest()](https://playwright.dev/docs/api/class-page#page-wait-for-request), 또는 [page.waitForResponse()](https://playwright.dev/docs/api/class-page#page-wait-for-response)를 사용할 때, 대응되는 URL을 구성하기 위해 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 사용하여 base URL을 고려합니다. 기본적으로는 설정되지 않습니다. 예시:

      * baseURL: `http://localhost:3000` 이고 `/bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다.
      * baseURL: `http://localhost:3000/foo/` 이고 `./bar.html`로 이동하면 `http://localhost:3000/foo/bar.html`이 됩니다.
      * baseURL: `http://localhost:3000/foo` (trailing slash 없음) 이고 `./bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다.

- `bypassCSP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-bypass-csp)

페이지의 Content-Security-Policy 우회를 전환합니다. 기본값은 `false`입니다.

    * `colorScheme` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "light" | "dark" | "no-preference" _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-color-scheme)

[prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) 미디어 기능을 에뮬레이션하며, 지원 값은 `'light'`와 `'dark'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'light'`입니다.

    * `contrast` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "no-preference" | "more" _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-contrast)

`'prefers-contrast'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'no-preference'`, `'more'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `deviceScaleFactor` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-device-scale-factor)

디바이스 스케일 팩터(dpr로 생각할 수 있음)를 지정합니다. 기본값은 `1`입니다. [device scale factor로 디바이스 에뮬레이션](https://playwright.dev/docs/emulation#devices)에 대해 더 알아보세요.

    * `extraHTTPHeaders` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-extra-http-headers)

모든 요청과 함께 전송할 추가 HTTP 헤더를 담은 객체입니다. 기본값은 없음입니다.

    * `forcedColors` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "active" | "none" _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-forced-colors)

`'forced-colors'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'active'`, `'none'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'none'`입니다.

    * `geolocation` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-geolocation)

      * `latitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-90에서 90 사이의 위도입니다.

      * `longitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-180에서 180 사이의 경도입니다.

      * `accuracy` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

0 이상의 정확도 값입니다. 기본값은 `0`입니다.

    * `hasTouch` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-has-touch)

뷰포트가 터치 이벤트를 지원하는지 지정합니다. 기본값은 false입니다. [모바일 에뮬레이션](https://playwright.dev/docs/emulation#devices)에 대해 더 알아보세요.

    * `httpCredentials` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-http-credentials)

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

특정 origin(scheme://host:port)에 대해서만 http credentials 전송을 제한합니다.

      * `send` "unauthorized" | "always" _(optional)_

이 옵션은 해당 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")에서 전송되는 요청에만 적용되며 브라우저에서 전송되는 요청에는 영향을 주지 않습니다. `'always'` \- 기본 인증 자격 증명이 포함된 `Authorization` 헤더가 각 API 요청과 함께 전송됩니다. `'unauthorized` \- `WWW-Authenticate` 헤더를 포함한 401 (Unauthorized) 응답을 수신한 경우에만 자격 증명이 전송됩니다. 기본값은 `'unauthorized'`입니다.

[HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)을 위한 자격 증명입니다. origin을 지정하지 않으면 인증되지 않은 응답 시 사용자 이름과 비밀번호가 모든 서버로 전송됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `isMobile` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-is-mobile)

`meta viewport` 태그를 고려하고 터치 이벤트를 활성화할지 여부입니다. isMobile은 디바이스의 일부이므로 실제로 수동 설정할 필요가 없습니다. 기본값은 `false`이며 Firefox에서는 지원되지 않습니다. [모바일 에뮬레이션](https://playwright.dev/docs/emulation#ismobile)에 대해 더 알아보세요.

    * `javaScriptEnabled` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-java-script-enabled)

컨텍스트에서 JavaScript를 활성화할지 여부입니다. 기본값은 `true`입니다. [JavaScript 비활성화](https://playwright.dev/docs/emulation#javascript-enabled)에 대해 더 알아보세요.

    * `locale` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-locale)

예: `en-GB`, `de-DE`와 같이 사용자 로캘을 지정합니다. 로캘은 `navigator.language` 값, `Accept-Language` 요청 헤더 값, 숫자 및 날짜 형식 규칙에 영향을 줍니다. 기본값은 시스템 기본 로캘입니다. 에뮬레이션에 대한 자세한 내용은 [emulation guide](https://playwright.dev/docs/emulation#locale--timezone)를 참고하세요.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-logger)

지원 중단됨

logger가 수신하는 로그는 완전하지 않습니다. 대신 tracing을 사용하세요.

Playwright 로깅을 위한 Logger sink입니다.

    * `offline` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-offline)

네트워크 오프라인 상태를 에뮬레이션할지 여부입니다. 기본값은 `false`입니다. [network emulation](https://playwright.dev/docs/emulation#offline)에 대해 더 알아보세요.

    * `permissions` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-permissions)

이 컨텍스트의 모든 페이지에 부여할 권한 목록입니다. 자세한 내용은 [browserContext.grantPermissions()](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions)를 참고하세요. 기본값은 없음입니다.

    * `pkg` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-pkg)

기본 Chrome for Android 대신 실행할 선택적 패키지 이름입니다.

    * `proxy` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ Added in: v1.29[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-proxy)

      * `server` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

모든 요청에 사용할 프록시입니다. HTTP 및 SOCKS 프록시를 지원하며, 예: `http://myproxy.com:3128` 또는 `socks5://myproxy.com:3128`입니다. 축약형 `myproxy.com:3128`은 HTTP 프록시로 간주됩니다.

      * `bypass` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

프록시를 우회할 선택적 쉼표 구분 도메인 목록입니다. 예: `".com, chromium.org, .domain.com"`.

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 사용자 이름입니다.

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 비밀번호입니다.

네트워크 프록시 설정입니다.

    * `recordHar` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-record-har)

      * `omitContent` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_

HAR에서 요청 콘텐츠를 생략할지 제어하는 선택적 설정입니다. 기본값은 `false`입니다. 지원 중단되었으며, 대신 `content` 정책을 사용하세요.

      * `content` "omit" | "embed" | "attach" _(optional)_

리소스 콘텐츠 관리를 제어하는 선택적 설정입니다. `omit`을 지정하면 콘텐츠가 저장되지 않습니다. `attach`를 지정하면 리소스가 별도 파일 또는 ZIP 아카이브의 항목으로 저장됩니다. `embed`를 지정하면 HAR 사양에 따라 콘텐츠가 HAR 파일에 인라인으로 저장됩니다. 기본값은 `.zip` 출력 파일의 경우 `attach`, 그 외 모든 파일 확장자의 경우 `embed`입니다.

      * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

HAR 파일을 기록할 파일 시스템 경로입니다. 파일 이름이 `.zip`으로 끝나면 기본적으로 `content: 'attach'`가 사용됩니다.

      * `mode` "full" | "minimal" _(optional)_

`minimal`로 설정하면 HAR에서 라우팅에 필요한 정보만 기록합니다. 이 경우 HAR 재생 시 사용되지 않는 크기, 타이밍, 페이지, 쿠키, 보안 및 기타 HAR 정보 유형이 생략됩니다. 기본값은 `full`입니다.

- `urlFilter` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_

HAR에 저장되는 요청을 필터링하기 위한 glob 또는 regex 패턴입니다. 컨텍스트 옵션을 통해 [baseURL](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url)이 제공되었고 전달된 URL이 경로인 경우, [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 통해 병합됩니다. 기본값은 없음입니다.

모든 페이지에 대해 HAR 녹화를 활성화하여 `recordHar.path` 파일에 저장합니다. 지정하지 않으면 HAR은 기록되지 않습니다. HAR이 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `recordVideo` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-record-video)

      * `dir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

동영상을 저장할 디렉터리 경로입니다.

      * `size` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_

        * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

        * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

녹화된 비디오의 선택적 크기입니다. 지정하지 않으면 크기는 `viewport`와 같고 800x800 안에 맞도록 축소됩니다. `viewport`가 명시적으로 설정되지 않은 경우 비디오 크기 기본값은 800x450입니다. 필요하면 각 페이지의 실제 화면은 지정된 크기에 맞도록 축소됩니다.

모든 페이지에 대해 비디오 녹화를 활성화하여 `recordVideo.dir` 디렉터리에 저장합니다. 지정하지 않으면 비디오는 녹화되지 않습니다. 비디오가 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `reducedMotion` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "reduce" | "no-preference" _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-reduced-motion)

`'prefers-reduced-motion'` 미디어 기능을 에뮬레이션하며, 지원되는 값은 `'reduce'`, `'no-preference'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참조하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `screen` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-screen)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

웹 페이지 내부에서 `window.screen`으로 접근 가능한 일관된 창 화면 크기를 에뮬레이션합니다. [viewport](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-viewport)가 설정된 경우에만 사용됩니다.

    * `serviceWorkers` "allow" | "block" _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-service-workers)

사이트의 Service worker 등록 허용 여부입니다. 기본값은 `'allow'`입니다.

      * `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)를 등록할 수 있습니다.
      * `'block'`: Playwright가 모든 Service Worker 등록을 차단합니다.
    * `strictSelectors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-strict-selectors)

`true`로 설정하면 이 컨텍스트에서 strict selectors 모드가 활성화됩니다. strict selectors 모드에서는 단일 대상 DOM 요소를 전제로 하는 모든 selector 작업이, selector와 일치하는 요소가 둘 이상이면 예외를 발생시킵니다. 이 옵션은 Locator API에는 영향을 주지 않습니다(Locators는 항상 strict). 기본값은 `false`입니다. strict 모드에 대한 자세한 내용은 [Locator](https://playwright.dev/docs/api/class-locator "Locator")를 참조하세요.

    * `timezoneId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-timezone-id)

컨텍스트의 시간대를 변경합니다. 지원되는 timezone ID 목록은 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)를 참조하세요. 기본값은 시스템 시간대입니다.

    * `userAgent` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-user-agent)

이 컨텍스트에서 사용할 특정 user agent입니다.

    * `videoSize` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-video-size)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-record-video)를 사용하세요.

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

    * `videosPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-videos-path)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-record-video)를 사용하세요.

    * `viewport` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-option-viewport)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

각 페이지에 대해 일관된 viewport를 에뮬레이션합니다. 기본값은 1280x720 viewport입니다. 일관된 viewport 에뮬레이션을 비활성화하려면 `null`을 사용하세요. [viewport emulation](https://playwright.dev/docs/emulation#viewport)에 대해 더 알아보세요.

note

`null` 값은 기본 프리셋 사용을 해제하고, viewport가 운영체제에서 정의한 호스트 창 크기에 의존하도록 만듭니다. 이로 인해 테스트 실행이 비결정적이 됩니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-launch-browser-return)

---

### longTap[​](https://playwright.dev/docs/api/class-androiddevice#android-device-long-tap "Direct link to longTap")

추가 버전: v1.9 androidDevice.longTap

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-long-tap-option-selector)로 정의된 위젯에서 길게 탭을 수행합니다.

**Usage**

```
    await androidDevice.longTap(selector);
    await androidDevice.longTap(selector, options);

```

**Arguments**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-long-tap-option-selector)

탭할 selector입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-long-tap-option-timeout)

최대 시간(밀리초)이며 기본값은 30초입니다. timeout을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-long-tap-return)

---

### model[​](https://playwright.dev/docs/api/class-androiddevice#android-device-model "Direct link to model")

추가 버전: v1.9 androidDevice.model

디바이스 모델.

**Usage**

```
    androidDevice.model();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-model-return)

---

### open[​](https://playwright.dev/docs/api/class-androiddevice#android-device-open "Direct link to open")

추가 버전: v1.9 androidDevice.open

디바이스에서 shell 프로세스를 시작하고, 시작된 프로세스와 통신할 수 있는 소켓을 반환합니다.

**Usage**

```
    await androidDevice.open(command);

```

**Arguments**

- `command` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-open-option-command)

실행할 shell 명령입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[AndroidSocket](https://playwright.dev/docs/api/class-androidsocket "AndroidSocket")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-open-return)

---

### pinchClose[​](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-close "Direct link to pinchClose")

추가 버전: v1.9 androidDevice.pinchClose

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-close-option-selector)로 정의된 위젯을 닫는 방향으로 핀치합니다.

**Usage**

```
    await androidDevice.pinchClose(selector, percent);
    await androidDevice.pinchClose(selector, percent, options);

```

**Arguments**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-close-option-selector)

핀치 클로즈할 selector입니다.

- `percent` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-close-option-percent)

위젯 크기 대비 핀치 크기의 백분율입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `speed` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-close-option-speed)

초당 픽셀 단위의 선택적 핀치 속도입니다.

- `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-close-option-timeout)

밀리초 단위의 최대 시간이며, 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-close-return)

---

### pinchOpen[​](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-open "Direct link to pinchOpen")

추가된 버전: v1.9 androidDevice.pinchOpen

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-open-option-selector)로 정의된 위젯을 벌리는 방향으로 핀치합니다.

**사용법**

```
    await androidDevice.pinchOpen(selector, percent);
    await androidDevice.pinchOpen(selector, percent, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-open-option-selector)

벌리기 핀치를 수행할 selector입니다.

- `percent` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-open-option-percent)

위젯 크기 대비 백분율로 나타낸 핀치 크기입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `speed` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-open-option-speed)

픽셀/초 단위의 선택적 핀치 속도입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-open-option-timeout)

밀리초 단위의 최대 시간이며, 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-pinch-open-return)

---

### press[​](https://playwright.dev/docs/api/class-androiddevice#android-device-press "Direct link to press")

추가된 버전: v1.9 androidDevice.press

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-press-option-selector)로 정의된 위젯에서 지정한 [key](https://playwright.dev/docs/api/class-androiddevice#android-device-press-option-key)를 누릅니다.

**사용법**

```
    await androidDevice.press(selector, key);
    await androidDevice.press(selector, key, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-press-option-selector)

키 입력을 수행할 selector입니다.

- `key` [AndroidKey][#](https://playwright.dev/docs/api/class-androiddevice#android-device-press-option-key)

누를 키입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-press-option-timeout)

밀리초 단위의 최대 시간이며, 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-press-return)

---

### push[​](https://playwright.dev/docs/api/class-androiddevice#android-device-push "Direct link to push")

추가된 버전: v1.9 androidDevice.push

파일을 디바이스로 복사합니다.

**사용법**

```
    await androidDevice.push(file, path);
    await androidDevice.push(file, path, options);

```

**인수**

- `file` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-push-option-file)

파일 경로 또는 파일 내용입니다.

- `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-push-option-path)

디바이스 내 파일 경로입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `mode` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-push-option-mode)

선택적 파일 모드이며, 기본값은 `644` (`rw-r--r--`)입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-push-return)

---

### screenshot[​](https://playwright.dev/docs/api/class-androiddevice#android-device-screenshot "Direct link to screenshot")

추가된 버전: v1.9 androidDevice.screenshot

디바이스에서 캡처한 스크린샷이 담긴 버퍼를 반환합니다.

**사용법**

```
    await androidDevice.screenshot();
    await androidDevice.screenshot(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-screenshot-option-path)

이미지를 저장할 파일 경로입니다. [path](https://playwright.dev/docs/api/class-androiddevice#android-device-screenshot-option-path)가 상대 경로이면 현재 작업 디렉터리를 기준으로 해석됩니다. path를 제공하지 않으면 이미지는 디스크에 저장되지 않습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-screenshot-return)

---

### scroll[​](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll "Direct link to scroll")

추가된 버전: v1.9 androidDevice.scroll

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-option-selector)로 정의된 위젯을 지정한 [direction](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-option-direction)으로 스크롤합니다.

**사용법**

```
    await androidDevice.scroll(selector, direction, percent);
    await androidDevice.scroll(selector, direction, percent, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-option-selector)

스크롤할 selector입니다.

- `direction` "down" | "up" | "left" | "right"[#](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-option-direction)

스크롤 방향입니다.

- `percent` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-option-percent)

위젯 크기 대비 백분율로 나타낸 스크롤 거리입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `speed` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-option-speed)

픽셀/초 단위의 선택적 스크롤 속도입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-option-timeout)

밀리초 단위의 최대 시간이며, 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-scroll-return)

---

### serial[​](https://playwright.dev/docs/api/class-androiddevice#android-device-serial "Direct link to serial")

추가된 버전: v1.9 androidDevice.serial

디바이스 시리얼 번호입니다.

**사용법**

```
    androidDevice.serial();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-serial-return)

---

### setDefaultTimeout[​](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout "Direct link to setDefaultTimeout")

추가된 버전: v1.9 androidDevice.setDefaultTimeout

이 설정은 [timeout](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout-option-timeout) 옵션을 받는 모든 메서드의 기본 최대 시간을 변경합니다.

**사용법**

```
    androidDevice.setDefaultTimeout(timeout);

```

**인수**

- `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout-option-timeout)

밀리초 단위의 최대 시간

---

### shell[​](https://playwright.dev/docs/api/class-androiddevice#android-device-shell "Direct link to shell")

추가된 버전: v1.9 androidDevice.shell

디바이스에서 shell 명령을 실행하고 그 출력을 반환합니다.

**사용법**

```
    await androidDevice.shell(command);

```

**인수**

- `command` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-shell-option-command)

실행할 shell 명령입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-shell-return)

---

### swipe[​](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe "Direct link to swipe")

추가된 버전: v1.9 androidDevice.swipe

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-option-selector)로 정의된 위젯을 지정한 [direction](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-option-direction)으로 스와이프합니다.

**사용법**

```
    await androidDevice.swipe(selector, direction, percent);
    await androidDevice.swipe(selector, direction, percent, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-option-selector)

스와이프할 셀렉터입니다.

- `direction` "down" | "up" | "left" | "right"[#](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-option-direction)

스와이프 방향입니다.

- `percent` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-option-percent)

위젯 크기 대비 백분율로 지정하는 스와이프 거리입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `speed` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-option-speed)

초당 픽셀 단위의 스와이프 속도(선택 사항)입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-option-timeout)

밀리초 단위 최대 시간이며 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-swipe-return)

---

### tap[​](https://playwright.dev/docs/api/class-androiddevice#android-device-tap "Direct link to tap")

추가된 버전: v1.9 androidDevice.tap

[selector](https://playwright.dev/docs/api/class-androiddevice#android-device-tap-option-selector)로 정의된 위젯을 탭합니다.

**사용법**

```
    await androidDevice.tap(selector);
    await androidDevice.tap(selector, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-tap-option-selector)

탭할 셀렉터입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `duration` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-tap-option-duration)

탭 지속 시간(밀리초, 선택 사항)입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-tap-option-timeout)

밀리초 단위 최대 시간이며 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-tap-return)

---

### wait[​](https://playwright.dev/docs/api/class-androiddevice#android-device-wait "Direct link to wait")

추가된 버전: v1.9 androidDevice.wait

[state](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-option-state)에 따라, 특정 [selector](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-option-selector)가 나타나거나 사라질 때까지 대기합니다.

**사용법**

```
    await androidDevice.wait(selector);
    await androidDevice.wait(selector, options);

```

**인수**

- `selector` [AndroidSelector][#](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-option-selector)

대기할 셀렉터입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `state` "gone" _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-option-state)

선택적 상태입니다. 다음 중 하나일 수 있습니다:

      * default - 요소가 존재할 때까지 대기합니다.
      * `'gone'` \- 요소가 존재하지 않을 때까지 대기합니다.
    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-option-timeout)

밀리초 단위 최대 시간이며 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-return)

---

### waitForEvent[​](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-for-event "Direct link to waitForEvent")

추가된 버전: v1.9 androidDevice.waitForEvent

이벤트가 발생할 때까지 기다리고 그 값을 predicate 함수에 전달합니다. predicate가 truthy 값을 반환하면 완료됩니다.

**사용법**

```
    await androidDevice.waitForEvent(event);
    await androidDevice.waitForEvent(event, optionsOrPredicate);

```

**인수**

- `event` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-for-event-option-event)

이벤트 이름으로, 일반적으로 `*.on(event)`에 전달하는 것과 동일합니다.

- `optionsOrPredicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-for-event-option-options-or-predicate)
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")

이벤트 데이터를 받아, 대기를 완료해야 할 때 truthy 값으로 resolve됩니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

밀리초 단위 최대 대기 시간입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout)으로 변경할 수 있습니다.

이벤트를 받는 predicate 또는 options 객체 중 하나입니다. 선택 사항입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-wait-for-event-return)

---

### webView[​](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view "Direct link to webView")

추가된 버전: v1.9 androidDevice.webView

이 메서드는 [selector](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view-option-selector)와 일치하는 [AndroidWebView](https://playwright.dev/docs/api/class-androidwebview "AndroidWebView")가 열릴 때까지 기다린 뒤 반환합니다. 이미 [selector](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view-option-selector)와 일치하는 열린 [AndroidWebView](https://playwright.dev/docs/api/class-androidwebview "AndroidWebView")가 있으면 즉시 반환합니다.

**사용법**

```
    await androidDevice.webView(selector);
    await androidDevice.webView(selector, options);

```

**인수**

- `selector` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view-option-selector)
  - `pkg` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

선택적 패키지 식별자입니다.

    * `socketName` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

선택적 webview 소켓 이름입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view-option-timeout)

밀리초 단위 최대 시간이며 기본값은 30초입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요. 기본값은 [androidDevice.setDefaultTimeout()](https://playwright.dev/docs/api/class-androiddevice#android-device-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[AndroidWebView](https://playwright.dev/docs/api/class-androidwebview "AndroidWebView")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view-return)

---

### webViews[​](https://playwright.dev/docs/api/class-androiddevice#android-device-web-views "Direct link to webViews")

추가된 버전: v1.9 androidDevice.webViews

현재 열려 있는 WebViews입니다.

**사용법**

```
    androidDevice.webViews();

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[AndroidWebView](https://playwright.dev/docs/api/class-androidwebview "AndroidWebView")>[#](https://playwright.dev/docs/api/class-androiddevice#android-device-web-views-return)

---

## 속성[​](https://playwright.dev/docs/api/class-androiddevice#properties "Direct link to Properties")

### input[​](https://playwright.dev/docs/api/class-androiddevice#android-device-input "Direct link to input")

추가된 버전: v1.9 androidDevice.input

**사용법**

```
    androidDevice.input

```

**타입**

- [AndroidInput](https://playwright.dev/docs/api/class-androidinput "AndroidInput")

---

## 이벤트[​](https://playwright.dev/docs/api/class-androiddevice#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-androiddevice#android-device-event-close "Direct link to on('close')")

추가된 버전: v1.28 androidDevice.on('close')

디바이스 연결이 종료되면 발생합니다.

**사용법**

```
    androidDevice.on('close', data => {});

```

**이벤트 데이터**

- [AndroidDevice](https://playwright.dev/docs/api/class-androiddevice "AndroidDevice")

---

### on('webview')[​](https://playwright.dev/docs/api/class-androiddevice#android-device-event-web-view "Direct link to on('webview')")

추가된 버전: v1.9 androidDevice.on('webview')

새로운 WebView 인스턴스가 감지되면 발생합니다.

**사용법**

```
    androidDevice.on('webview', data => {});

```

**이벤트 데이터**

- [AndroidWebView](https://playwright.dev/docs/api/class-androidwebview "AndroidWebView")
