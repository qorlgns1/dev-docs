---
title: "BrowserType"
description: "BrowserType는 특정 브라우저 인스턴스를 실행하거나 기존 인스턴스에 연결하는 메서드를 제공합니다. 다음은 Playwright를 사용해 자동화를 구동하는 일반적인 예시입니다:"
---

Source URL: https://playwright.dev/docs/api/class-browsertype

# BrowserType | Playwright

BrowserType는 특정 브라우저 인스턴스를 실행하거나 기존 인스턴스에 연결하는 메서드를 제공합니다. 다음은 Playwright를 사용해 자동화를 구동하는 일반적인 예시입니다:

```
    const { chromium } = require('playwright');  // Or 'firefox' or 'webkit'.

    (async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      await page.goto('https://example.com');
      // other actions...
      await browser.close();
    })();

```

---

## Methods[​](https://playwright.dev/docs/api/class-browsertype#methods "Direct link to Methods")

### connect[​](https://playwright.dev/docs/api/class-browsertype#browser-type-connect "Direct link to connect")

v1.9 이전에 추가됨 `browserType.connect`

이 메서드는 Node.js에서 `BrowserType.launchServer`를 통해 생성된 기존 브라우저 인스턴스에 Playwright를 연결합니다.

note

연결하는 Playwright 인스턴스의 메이저/마이너 버전은 브라우저를 실행한 Playwright 버전과 일치해야 합니다 (1.2.3 → 1.2.x와 호환).

**Usage**

```
    await browserType.connect(wsEndpoint);
    await browserType.connect(wsEndpoint, options);

```

**Arguments**

- `wsEndpoint` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") v1.10에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-option-ws-endpoint)

연결할 Playwright 브라우저 websocket endpoint입니다. 이 endpoint는 `BrowserServer.wsEndpoint`를 통해 얻을 수 있습니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exposeNetwork` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ v1.37에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-option-expose-network)

이 옵션은 연결 클라이언트에서 사용 가능한 네트워크를 연결 대상 브라우저에 노출합니다. 쉼표로 구분된 규칙 목록으로 구성됩니다.

사용 가능한 규칙:

      1. 호스트네임 패턴, 예: `example.com`, `*.org:99`, `x.*.y.com`, `*foo.org`.
      2. IP 리터럴, 예: `127.0.0.1`, `0.0.0.0:99`, `[::1]`, `[0:0::1]:99`.
      3. 로컬 루프백 인터페이스와 일치하는 `<loopback>`: `localhost`, `*.localhost`, `127.0.0.1`, `[::1]`.

일반적인 예시:

      1. `"*"`: 모든 네트워크 노출.
      2. `"<loopback>"`: localhost 네트워크 노출.
      3. `"*.test.internal-domain,*.staging.internal-domain,<loopback>"`: 테스트/스테이징 배포 및 localhost 노출.
    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_ v1.11에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-option-headers)

웹 소켓 연결 요청과 함께 전송할 추가 HTTP 헤더입니다. 선택 사항입니다.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(optional)_ v1.14에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-option-logger)

Deprecated

logger로 수신되는 로그는 불완전합니다. 대신 tracing을 사용하세요.

Playwright 로깅을 위한 Logger sink입니다. 선택 사항입니다.

    * `slowMo` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ v1.10에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-option-slow-mo)

Playwright 작업을 지정한 밀리초만큼 느리게 실행합니다. 동작 과정을 확인할 때 유용합니다. 기본값은 0입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ v1.10에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-option-timeout)

연결이 설정될 때까지 대기하는 최대 시간(밀리초)입니다. 기본값은 `0`(타임아웃 없음)입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Browser](https://playwright.dev/docs/api/class-browser "Browser")>[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-return)

---

### connectOverCDP[​](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp "Direct link to connectOverCDP")

v1.9에 추가됨 `browserType.connectOverCDP`

이 메서드는 Chrome DevTools Protocol을 사용해 기존 브라우저 인스턴스에 Playwright를 연결합니다.

기본 브라우저 컨텍스트는 [browser.contexts()](https://playwright.dev/docs/api/class-browser#browser-contexts)로 접근할 수 있습니다.

note

Chrome DevTools Protocol을 통한 연결은 Chromium 기반 브라우저에서만 지원됩니다.

note

이 연결은 [browserType.connect()](https://playwright.dev/docs/api/class-browsertype#browser-type-connect)를 통한 Playwright 프로토콜 연결보다 충실도가 상당히 낮습니다. 문제가 발생하거나 고급 기능을 사용하려는 경우 [browserType.connect()](https://playwright.dev/docs/api/class-browsertype#browser-type-connect)를 사용하는 것이 좋습니다.

**Usage**

```
    const browser = await playwright.chromium.connectOverCDP('http://localhost:9222');
    const defaultContext = browser.contexts()[0];
    const page = defaultContext.pages()[0];

```

**Arguments**

- `endpointURL` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") v1.11에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-option-endpoint-url)

연결할 CDP websocket endpoint 또는 http url입니다. 예: `http://localhost:9222/` 또는 `ws://127.0.0.1:9222/devtools/browser/387adf4c-243f-4051-a181-46798f4a46f4`.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `endpointURL` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ v1.14에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-option-endpoint-url)

Deprecated

대신 첫 번째 인수를 사용하세요.

    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_ v1.11에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-option-headers)

연결 요청과 함께 전송할 추가 HTTP 헤더입니다. 선택 사항입니다.

    * `isLocal` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ v1.58에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-option-is-local)

Playwright가 CDP 서버와 같은 호스트에서 실행 중임을 알립니다. Playwright와 Browser 간 파일 시스템이 동일하다는 전제에 의존하는 특정 최적화를 활성화합니다.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(optional)_ v1.14에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-option-logger)

Deprecated

logger로 수신되는 로그는 불완전합니다. 대신 tracing을 사용하세요.

Playwright 로깅을 위한 Logger sink입니다. 선택 사항입니다.

    * `slowMo` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ v1.11에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-option-slow-mo)

Playwright 작업을 지정한 밀리초만큼 느리게 실행합니다. 동작 과정을 확인할 때 유용합니다. 기본값은 0입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ v1.11에 추가됨[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-option-timeout)

연결이 설정될 때까지 대기하는 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Browser](https://playwright.dev/docs/api/class-browser "Browser")>[#](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp-return)

---

### executablePath[​](https://playwright.dev/docs/api/class-browsertype#browser-type-executable-path "Direct link to executablePath")

v1.9 이전에 추가됨 `browserType.executablePath`

Playwright가 번들된 브라우저 실행 파일을 찾을 것으로 기대하는 경로입니다.

**Usage**

```
    browserType.executablePath();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browsertype#browser-type-executable-path-return)

---

### launch[​](https://playwright.dev/docs/api/class-browsertype#browser-type-launch "Direct link to launch")

v1.9 이전에 추가됨 `browserType.launch`

브라우저 인스턴스를 반환합니다.

**Usage**

[ignoreDefaultArgs](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-ignore-default-args)를 사용해 기본 인수에서 `--mute-audio`를 제외할 수 있습니다:

```
    const browser = await chromium.launch({  // Or 'firefox' or 'webkit'.
      ignoreDefaultArgs: ['--mute-audio']
    });

```

> **Chromium-only** Playwright는 Google Chrome 또는 Microsoft Edge 브라우저를 제어하는 데도 사용할 수 있지만, 번들된 Chromium 버전에서 가장 잘 동작합니다. 다른 버전에서 동작함을 보장하지 않습니다. [executablePath](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-executable-path) 옵션은 매우 주의해서 사용하세요.
>
> Chromium이 아닌 Google Chrome을 선호한다면 [Chrome Canary](https://www.google.com/chrome/browser/canary.html) 또는 [Dev Channel](https://www.chromium.org/getting-involved/dev-channel) 빌드를 권장합니다.
>
> Google Chrome 및 Microsoft Edge 같은 스톡 브라우저는 비디오 재생을 위한 독점 미디어 코덱이 필요한 테스트에 적합합니다. Chromium과 Chrome의 다른 차이점은 [this article](https://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/)를 참고하세요. Linux 사용자 관점의 일부 차이점은 [This article](https://chromium.googlesource.com/chromium/src/+/lkgr/docs/chromium_browser_vs_google_chrome.md)에서 설명합니다.

**Arguments**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `args` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-args)

warning

일부 인수는 Playwright 기능을 손상시킬 수 있으므로, 커스텀 브라우저 인수는 본인 책임하에 사용하세요.

브라우저 인스턴스에 전달할 추가 인수입니다. Chromium 플래그 목록은 [here](https://peter.sh/experiments/chromium-command-line-switches/)에서 확인할 수 있습니다.

    * `channel` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-channel)

브라우저 배포 채널입니다.

새 headless 모드를 사용하려면 `"chromium"`을 사용하세요([opt in to new headless mode](https://playwright.dev/docs/browsers#chromium-new-headless-mode)).

브랜드된 [Google Chrome and Microsoft Edge](https://playwright.dev/docs/browsers#google-chrome--microsoft-edge)를 사용하려면 `"chrome"`, `"chrome-beta"`, `"chrome-dev"`, `"chrome-canary"`, `"msedge"`, `"msedge-beta"`, `"msedge-dev"`, `"msedge-canary"`를 사용하세요.

    * `chromiumSandbox` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-chromium-sandbox)

Chromium 샌드박싱을 활성화합니다. 기본값은 `false`입니다.

- `downloadsPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-downloads-path)

지정하면 허용된 다운로드가 이 디렉터리에 저장됩니다. 그렇지 않으면 임시 디렉터리가 생성되며 브라우저가 닫힐 때 삭제됩니다. 두 경우 모두, 다운로드는 해당 다운로드가 생성된 브라우저 컨텍스트가 닫힐 때 삭제됩니다.

    * `env` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [undefined]> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-env)

    * `executablePath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-executable-path)

번들된 브라우저 대신 실행할 브라우저 실행 파일 경로입니다. [executablePath](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-executable-path)가 상대 경로인 경우 현재 작업 디렉터리를 기준으로 해석됩니다. Playwright는 번들된 Chromium, Firefox 또는 WebKit에서만 동작하므로 주의해서 사용하세요.

    * `firefoxUserPrefs` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-firefox-user-prefs)

Firefox 사용자 기본 설정입니다. Firefox 사용자 기본 설정에 대한 자세한 내용은 [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox)에서 확인하세요.

또한 `PLAYWRIGHT_FIREFOX_POLICIES_JSON` 환경 변수를 통해 사용자 지정 [`policies.json` file](https://mozilla.github.io/policy-templates/) 경로를 제공할 수 있습니다.

    * `handleSIGHUP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-handle-sighup)

SIGHUP 시 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `handleSIGINT` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-handle-sigint)

Ctrl-C 시 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `handleSIGTERM` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-handle-sigterm)

SIGTERM 시 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `headless` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-headless)

브라우저를 헤드리스 모드로 실행할지 여부입니다. 자세한 내용은 [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) 및 [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/)를 참고하세요. 기본값은 `true`입니다.

    * `ignoreDefaultArgs` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-ignore-default-args)

`true`이면 Playwright는 자체 구성 인수를 전달하지 않고 [args](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-args)의 값만 사용합니다. 배열이 주어지면 지정된 기본 인수를 필터링해 제외합니다. 위험한 옵션이므로 주의해서 사용하세요. 기본값은 `false`입니다.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-logger)

지원 중단됨

logger가 수신하는 로그는 불완전합니다. 대신 tracing을 사용하세요.

Playwright 로깅을 위한 logger sink입니다.

    * `proxy` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-proxy)

      * `server` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

모든 요청에 사용할 프록시입니다. HTTP 및 SOCKS 프록시를 지원하며, 예를 들어 `http://myproxy.com:3128` 또는 `socks5://myproxy.com:3128` 형태를 사용할 수 있습니다. 축약형 `myproxy.com:3128`은 HTTP 프록시로 간주됩니다.

      * `bypass` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

프록시를 우회할 도메인 목록(쉼표 구분)입니다. 예: `".com, chromium.org, .domain.com"`.

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에서 인증이 필요한 경우 사용할 선택적 사용자 이름입니다.

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에서 인증이 필요한 경우 사용할 선택적 비밀번호입니다.

네트워크 프록시 설정입니다.

    * `slowMo` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-slow-mo)

지정한 밀리초만큼 Playwright 동작을 느리게 합니다. 동작 과정을 확인할 때 유용합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-timeout)

브라우저 인스턴스 시작을 기다리는 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

    * `tracesDir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-traces-dir)

지정하면 트레이스가 이 디렉터리에 저장됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Browser](https://playwright.dev/docs/api/class-browser "Browser")>[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-return)

---

### launchPersistentContext[​](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context "Direct link to launchPersistentContext")

v1.9 이전에 추가됨 browserType.launchPersistentContext

영구 브라우저 컨텍스트 인스턴스를 반환합니다.

[userDataDir](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-user-data-dir)에 위치한 영구 저장소를 사용하는 브라우저를 실행하고 유일한 컨텍스트를 반환합니다. 이 컨텍스트를 닫으면 브라우저도 자동으로 닫힙니다.

**사용법**

```
    await browserType.launchPersistentContext(userDataDir);
    await browserType.launchPersistentContext(userDataDir, options);

```

**인수**

- `userDataDir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-user-data-dir)

쿠키 및 로컬 스토리지 같은 브라우저 세션 데이터를 저장하는 User Data Directory 경로입니다. 임시 디렉터리를 만들려면 빈 문자열을 전달하세요.

자세한 내용은 [Chromium](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md#introduction) 및 [Firefox](https://wiki.mozilla.org/Firefox/CommandLineOptions#User_profile)를 참고하세요. Chromium의 user data directory는 `chrome://version`에서 보이는 "Profile Path"의 **상위** 디렉터리입니다.

브라우저는 동일한 User Data Directory로 여러 인스턴스를 실행하는 것을 허용하지 않습니다.

warning

Chromium/Chrome: 최근 Chrome 정책 변경으로 인해 기본 Chrome 사용자 프로필 자동화는 지원되지 않습니다. `userDataDir`를 Chrome의 기본 "User Data" 디렉터리(일반 브라우징에 사용하는 프로필)로 지정하면 페이지가 로드되지 않거나 브라우저가 종료될 수 있습니다. 대신 자동화 프로필로 별도 디렉터리(예: 빈 폴더)를 만들어 사용하세요. 자세한 내용은 <https://developer.chrome.com/blog/remote-debugging-port>를 참고하세요.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `acceptDownloads` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-accept-downloads)

모든 첨부 파일을 자동으로 다운로드할지 여부입니다. 기본값은 `true`이며 모든 다운로드가 허용됩니다.

    * `args` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-args)

warning

일부 인수는 Playwright 기능을 손상시킬 수 있으므로, 사용자 지정 브라우저 인수는 본인 책임하에 사용하세요.

브라우저 인스턴스에 전달할 추가 인수입니다. Chromium 플래그 목록은 [여기](https://peter.sh/experiments/chromium-command-line-switches/)에서 확인할 수 있습니다.

    * `baseURL` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-base-url)

[page.goto()](https://playwright.dev/docs/api/class-page#page-goto), [page.route()](https://playwright.dev/docs/api/class-page#page-route), [page.waitForURL()](https://playwright.dev/docs/api/class-page#page-wait-for-url), [page.waitForRequest()](https://playwright.dev/docs/api/class-page#page-wait-for-request), 또는 [page.waitForResponse()](https://playwright.dev/docs/api/class-page#page-wait-for-response)를 사용할 때, 해당 URL을 구성하기 위해 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 사용하며 base URL을 고려합니다. 기본적으로는 설정되지 않습니다. 예시:

      * baseURL: `http://localhost:3000`이고 `/bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다.
      * baseURL: `http://localhost:3000/foo/`이고 `./bar.html`로 이동하면 `http://localhost:3000/foo/bar.html`이 됩니다.
      * baseURL: `http://localhost:3000/foo`(끝 슬래시 없음)이고 `./bar.html`로 이동하면 `http://localhost:3000/bar.html`이 됩니다.
    * `bypassCSP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-bypass-csp)

페이지의 Content-Security-Policy 우회 여부를 전환합니다. 기본값은 `false`입니다.

- `channel` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-channel)

브라우저 배포 채널입니다.

새 헤드리스 모드를 [사용하려면](https://playwright.dev/docs/browsers#chromium-new-headless-mode) `"chromium"`을 사용하세요.

브랜드된 [Google Chrome and Microsoft Edge](https://playwright.dev/docs/browsers#google-chrome--microsoft-edge)를 사용하려면 `"chrome"`, `"chrome-beta"`, `"chrome-dev"`, `"chrome-canary"`, `"msedge"`, `"msedge-beta"`, `"msedge-dev"`, 또는 `"msedge-canary"`를 사용하세요.

    * `chromiumSandbox` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-chromium-sandbox)

Chromium 샌드박싱을 활성화합니다. 기본값은 `false`입니다.

    * `clientCertificates` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_ Added in: 1.46[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-client-certificates)

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

인증서가 유효한 정확한 origin입니다. Origin에는 `https` 프로토콜, 호스트 이름, 그리고 선택적으로 포트가 포함됩니다.

      * `certPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PEM 형식 인증서가 있는 파일 경로입니다.

      * `cert` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PEM 형식 인증서의 직접 값입니다.

      * `keyPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PEM 형식 개인 키가 있는 파일 경로입니다.

      * `key` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PEM 형식 개인 키의 직접 값입니다.

      * `pfxPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PFX 또는 PKCS12로 인코딩된 개인 키 및 인증서 체인이 있는 파일 경로입니다.

      * `pfx` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PFX 또는 PKCS12로 인코딩된 개인 키 및 인증서 체인의 직접 값입니다.

      * `passphrase` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

개인 키(PEM 또는 PFX)의 패스프레이즈입니다.

TLS 클라이언트 인증을 사용하면 서버가 클라이언트 인증서를 요청하고 검증할 수 있습니다.

**Details**

사용할 클라이언트 인증서 배열입니다. 각 인증서 객체에는 `certPath`와 `keyPath`를 함께 지정하거나, 단일 `pfxPath`를 지정하거나, 이에 해당하는 직접 값(`cert`와 `key`, 또는 `pfx`)을 지정해야 합니다. 인증서가 암호화된 경우 선택적으로 `passphrase` 속성을 제공해야 합니다. `origin` 속성은 인증서가 유효한 요청 origin과 정확히 일치하도록 제공해야 합니다.

클라이언트 인증서 인증은 하나 이상의 클라이언트 인증서가 제공될 때만 활성화됩니다. 서버가 보내는 모든 클라이언트 인증서를 거부하려면, 방문할 도메인과 일치하지 않는 `origin`을 가진 클라이언트 인증서를 제공해야 합니다.

note

macOS에서 WebKit을 사용할 때 `localhost`에 접근하면 클라이언트 인증서가 적용되지 않습니다. `localhost`를 `local.playwright`로 바꾸면 동작하게 만들 수 있습니다.

    * `colorScheme` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "light" | "dark" | "no-preference" _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-color-scheme)

[prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) 미디어 기능을 에뮬레이션하며, 지원 값은 `'light'`와 `'dark'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'light'`입니다.

    * `contrast` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "no-preference" | "more" _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-contrast)

`'prefers-contrast'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'no-preference'`, `'more'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `deviceScaleFactor` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-device-scale-factor)

디바이스 스케일 팩터(dpr로 생각할 수 있음)를 지정합니다. 기본값은 `1`입니다. [emulating devices with device scale factor](https://playwright.dev/docs/emulation#devices)에서 더 알아보세요.

    * `downloadsPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-downloads-path)

지정하면 수락된 다운로드가 이 디렉터리에 저장됩니다. 그렇지 않으면 임시 디렉터리가 생성되며 브라우저가 닫힐 때 삭제됩니다. 어떤 경우든 다운로드는 해당 다운로드가 생성된 브라우저 컨텍스트가 닫힐 때 삭제됩니다.

    * `env` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [undefined]> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-env)

    * `executablePath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-executable-path)

번들된 실행 파일 대신 실행할 브라우저 실행 파일 경로입니다. [executablePath](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-executable-path)가 상대 경로이면 현재 작업 디렉터리를 기준으로 해석됩니다. Playwright는 번들된 Chromium, Firefox 또는 WebKit에서만 동작하므로, 사용 시 주의하세요.

    * `extraHTTPHeaders` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-extra-http-headers)

모든 요청과 함께 전송할 추가 HTTP 헤더를 담은 객체입니다. 기본값은 없음입니다.

    * `firefoxUserPrefs` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> _(optional)_ Added in: v1.40[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-firefox-user-prefs)

Firefox 사용자 설정입니다. Firefox 사용자 설정에 대한 자세한 내용은 [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox)에서 확인하세요.

`PLAYWRIGHT_FIREFOX_POLICIES_JSON` 환경 변수를 통해 사용자 지정 [`policies.json` file](https://mozilla.github.io/policy-templates/) 경로를 제공할 수도 있습니다.

    * `forcedColors` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "active" | "none" _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-forced-colors)

`'forced-colors'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'active'`, `'none'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'none'`입니다.

    * `geolocation` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-geolocation)

      * `latitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-90에서 90 사이의 위도입니다.

      * `longitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-180에서 180 사이의 경도입니다.

      * `accuracy` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

음수가 아닌 정확도 값입니다. 기본값은 `0`입니다.

    * `handleSIGHUP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-handle-sighup)

SIGHUP에서 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `handleSIGINT` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-handle-sigint)

Ctrl-C에서 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `handleSIGTERM` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-handle-sigterm)

SIGTERM에서 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `hasTouch` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-has-touch)

뷰포트가 터치 이벤트를 지원하는지 지정합니다. 기본값은 false입니다. [mobile emulation](https://playwright.dev/docs/emulation#devices)에서 더 알아보세요.

    * `headless` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-headless)

브라우저를 헤드리스 모드로 실행할지 여부입니다. [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) 및 [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/)의 자세한 내용을 확인하세요. 기본값은 `true`입니다.

    * `httpCredentials` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-http-credentials)

- `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

특정 origin(`scheme://host:port`)에 대해서만 HTTP 자격 증명을 전송하도록 제한합니다.

      * `send` "unauthorized" | "always" _(optional)_

이 옵션은 해당 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")에서 전송되는 요청에만 적용되며, 브라우저에서 전송되는 요청에는 영향을 주지 않습니다. `'always'` \- 기본 인증 자격 증명이 포함된 `Authorization` 헤더가 각 API 요청과 함께 전송됩니다. `'unauthorized` \- `WWW-Authenticate` 헤더가 포함된 401(Unauthorized) 응답을 받은 경우에만 자격 증명이 전송됩니다. 기본값은 `'unauthorized'`입니다.

[HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)의 자격 증명입니다. origin을 지정하지 않으면, unauthorized 응답 시 username과 password가 모든 서버로 전송됩니다.

    * `ignoreDefaultArgs` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-ignore-default-args)

`true`이면 Playwright는 자체 구성 인자를 전달하지 않고 [args](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-args)의 값만 사용합니다. 배열이 제공되면 지정된 기본 인자들을 필터링하여 제외합니다. 위험할 수 있는 옵션이므로 주의해서 사용하세요. 기본값은 `false`입니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `isMobile` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-is-mobile)

`meta viewport` 태그를 고려하고 터치 이벤트를 활성화할지 여부입니다. isMobile은 device의 일부이므로 일반적으로 수동으로 설정할 필요가 없습니다. 기본값은 `false`이며 Firefox에서는 지원되지 않습니다. 자세한 내용은 [mobile emulation](https://playwright.dev/docs/emulation#ismobile)을 참고하세요.

    * `javaScriptEnabled` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-java-script-enabled)

컨텍스트에서 JavaScript를 활성화할지 여부입니다. 기본값은 `true`입니다. 자세한 내용은 [disabling JavaScript](https://playwright.dev/docs/emulation#javascript-enabled)를 참고하세요.

    * `locale` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-locale)

예: `en-GB`, `de-DE`처럼 사용자 로캘을 지정합니다. 로캘은 `navigator.language` 값, `Accept-Language` 요청 헤더 값, 숫자/날짜 형식 규칙에 영향을 줍니다. 기본값은 시스템 기본 로캘입니다. 에뮬레이션 관련 자세한 내용은 [emulation guide](https://playwright.dev/docs/emulation#locale--timezone)를 참고하세요.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-logger)

지원 중단됨

logger로 수신되는 로그는 불완전합니다. 대신 tracing을 사용하세요.

Playwright 로깅용 logger sink입니다.

    * `offline` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-offline)

네트워크 오프라인 상태를 에뮬레이션할지 여부입니다. 기본값은 `false`입니다. 자세한 내용은 [network emulation](https://playwright.dev/docs/emulation#offline)을 참고하세요.

    * `permissions` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-permissions)

이 컨텍스트의 모든 페이지에 부여할 권한 목록입니다. 자세한 내용은 [browserContext.grantPermissions()](https://playwright.dev/docs/api/class-browsercontext#browser-context-grant-permissions)를 참고하세요. 기본값은 없음입니다.

    * `proxy` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-proxy)

      * `server` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

모든 요청에 사용할 프록시입니다. HTTP 및 SOCKS 프록시를 지원하며, 예: `http://myproxy.com:3128` 또는 `socks5://myproxy.com:3128`. 축약형 `myproxy.com:3128`은 HTTP 프록시로 간주됩니다.

      * `bypass` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

프록시를 우회할 도메인을 쉼표로 구분해 지정합니다. 예: `".com, chromium.org, .domain.com"`.

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 사용자 이름입니다.

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 비밀번호입니다.

네트워크 프록시 설정입니다.

    * `recordHar` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-record-har)

      * `omitContent` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_

HAR에서 요청 콘텐츠를 생략할지 제어하는 선택적 설정입니다. 기본값은 `false`입니다. 지원 중단되었으며, 대신 `content` 정책을 사용하세요.

      * `content` "omit" | "embed" | "attach" _(optional)_

리소스 콘텐츠 관리를 제어하는 선택적 설정입니다. `omit`을 지정하면 콘텐츠가 저장되지 않습니다. `attach`를 지정하면 리소스가 별도 파일 또는 ZIP 아카이브 항목으로 저장됩니다. `embed`를 지정하면 HAR 사양에 따라 콘텐츠가 HAR 파일 내에 인라인으로 저장됩니다. 기본값은 `.zip` 출력 파일의 경우 `attach`, 그 외 모든 파일 확장자의 경우 `embed`입니다.

      * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

HAR 파일을 기록할 파일시스템 경로입니다. 파일명이 `.zip`으로 끝나면 기본적으로 `content: 'attach'`가 사용됩니다.

      * `mode` "full" | "minimal" _(optional)_

`minimal`로 설정하면 HAR에서 라우팅에 필요한 정보만 기록합니다. 이 경우 HAR 재생에 사용되지 않는 크기, 타이밍, 페이지, 쿠키, 보안 및 기타 HAR 정보가 생략됩니다. 기본값은 `full`입니다.

      * `urlFilter` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_

HAR에 저장할 요청을 필터링하는 glob 또는 regex 패턴입니다. 컨텍스트 옵션을 통해 [baseURL](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url)이 제공되고 전달된 URL이 경로인 경우, [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 통해 병합됩니다. 기본값은 없음입니다.

모든 페이지에 대해 `recordHar.path` 파일로 [HAR](http://www.softwareishard.com/blog/har-12-spec) 기록을 활성화합니다. 지정하지 않으면 HAR은 기록되지 않습니다. HAR이 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `recordVideo` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-record-video)

      * `dir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

비디오를 저장할 디렉터리 경로입니다.

      * `size` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_

        * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

        * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

기록된 비디오의 선택적 크기입니다. 지정하지 않으면 `viewport`를 800x800 안에 맞추도록 축소한 크기가 사용됩니다. `viewport`를 명시적으로 설정하지 않으면 비디오 크기 기본값은 800x450입니다. 각 페이지의 실제 화면은 필요 시 지정된 크기에 맞도록 축소됩니다.

모든 페이지에 대해 `recordVideo.dir` 디렉터리로 비디오 기록을 활성화합니다. 지정하지 않으면 비디오는 기록되지 않습니다. 비디오가 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `reducedMotion` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "reduce" | "no-preference" _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-reduced-motion)

`'prefers-reduced-motion'` 미디어 기능을 에뮬레이션하며, 지원 값은 `'reduce'`, `'no-preference'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'no-preference'`입니다.

    * `screen` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-screen)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

웹 페이지 내부에서 `window.screen`으로 접근 가능한 일관된 창 화면 크기를 에뮬레이션합니다. [viewport](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-viewport)가 설정된 경우에만 사용됩니다.

    * `serviceWorkers` "allow" | "block" _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-service-workers)

사이트의 Service worker 등록 허용 여부입니다. 기본값은 `'allow'`입니다.

      * `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)를 등록할 수 있습니다.

- `'block'`: Playwright가 Service Worker의 모든 등록을 차단합니다.
  - `slowMo` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-slow-mo)

지정한 밀리초만큼 Playwright 작업 속도를 늦춥니다. 내부에서 어떤 일이 일어나는지 확인할 때 유용합니다.

    * `strictSelectors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-strict-selectors)

`true`로 설정하면 이 컨텍스트에서 strict selectors 모드를 활성화합니다. strict selectors 모드에서는 단일 대상 DOM 요소를 전제로 하는 selector 작업에서, selector와 일치하는 요소가 둘 이상이면 예외가 발생합니다. 이 옵션은 Locator API에는 영향을 주지 않습니다(Locator는 항상 strict). 기본값은 `false`입니다. strict 모드에 대한 자세한 내용은 [Locator](https://playwright.dev/docs/api/class-locator "Locator")를 참고하세요.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-timeout)

브라우저 인스턴스 시작을 기다리는 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. timeout을 비활성화하려면 `0`을 전달하세요.

    * `timezoneId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-timezone-id)

컨텍스트의 시간대를 변경합니다. 지원되는 timezone ID 목록은 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)를 참고하세요. 기본값은 시스템 시간대입니다.

    * `tracesDir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-traces-dir)

지정하면 trace가 이 디렉터리에 저장됩니다.

    * `userAgent` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-user-agent)

이 컨텍스트에서 사용할 특정 user agent입니다.

    * `videoSize` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-video-size)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-record-video)를 사용하세요.

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

    * `videosPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-videos-path)

사용 중단됨

대신 [recordVideo](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-record-video)를 사용하세요.

    * `viewport` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-option-viewport)

      * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 너비입니다.

      * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

픽셀 단위 페이지 높이입니다.

각 페이지에 대해 일관된 viewport를 에뮬레이션합니다. 기본값은 1280x720 viewport입니다. 일관된 viewport 에뮬레이션을 비활성화하려면 `null`을 사용하세요. 자세한 내용은 [viewport emulation](https://playwright.dev/docs/emulation#viewport)을 참고하세요.

참고

`null` 값을 사용하면 기본 프리셋을 사용하지 않고, viewport가 운영 체제가 정의한 호스트 창 크기에 따라 달라집니다. 이로 인해 테스트 실행이 비결정적이 됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")>[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context-return)

---

### launchServer[​](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server "Direct link to launchServer")

v1.9 이전에 추가됨 browserType.launchServer

브라우저 앱 인스턴스를 반환합니다. [browserType.connect()](https://playwright.dev/docs/api/class-browsertype#browser-type-connect)로 연결할 수 있으며, 이때 클라이언트/서버의 major/minor 버전이 일치해야 합니다(1.2.3 → 1.2.x와 호환).

**사용법**

클라이언트가 연결할 수 있는 브라우저 서버를 시작합니다. 아래는 브라우저 실행 파일을 시작한 뒤 나중에 연결하는 예시입니다:

```
    const { chromium } = require('playwright');  // Or 'webkit' or 'firefox'.

    (async () => {
      const browserServer = await chromium.launchServer();
      const wsEndpoint = browserServer.wsEndpoint();
      // Use web socket endpoint later to establish a connection.
      const browser = await chromium.connect(wsEndpoint);
      // Close browser instance.
      await browserServer.close();
    })();

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `args` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-args)

경고

일부 인수는 Playwright 기능을 깨뜨릴 수 있으므로 사용자 지정 브라우저 인수는 신중하게 사용하세요.

브라우저 인스턴스에 전달할 추가 인수입니다. Chromium 플래그 목록은 [여기](https://peter.sh/experiments/chromium-command-line-switches/)에서 확인할 수 있습니다.

    * `channel` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-channel)

브라우저 배포 채널입니다.

새 headless 모드를 사용하려면 `"chromium"`을 사용하세요([opt in to new headless mode](https://playwright.dev/docs/browsers#chromium-new-headless-mode)).

브랜드 버전 [Google Chrome and Microsoft Edge](https://playwright.dev/docs/browsers#google-chrome--microsoft-edge)를 사용하려면 `"chrome"`, `"chrome-beta"`, `"chrome-dev"`, `"chrome-canary"`, `"msedge"`, `"msedge-beta"`, `"msedge-dev"`, 또는 `"msedge-canary"`를 사용하세요.

    * `chromiumSandbox` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-chromium-sandbox)

Chromium sandboxing을 활성화합니다. 기본값은 `false`입니다.

    * `downloadsPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-downloads-path)

지정하면 수락된 다운로드가 이 디렉터리에 저장됩니다. 그렇지 않으면 임시 디렉터리가 생성되며 브라우저가 닫힐 때 삭제됩니다. 어느 경우든 다운로드는 생성된 브라우저 컨텍스트가 닫힐 때 삭제됩니다.

    * `env` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [undefined]> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-env)

    * `executablePath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-executable-path)

번들된 실행 파일 대신 실행할 브라우저 실행 파일 경로입니다. [executablePath](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-executable-path)가 상대 경로이면 현재 작업 디렉터리 기준으로 해석됩니다. Playwright는 번들된 Chromium, Firefox, WebKit에서만 정상 동작하므로 사용 시 주의하세요.

    * `firefoxUserPrefs` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-firefox-user-prefs)

Firefox 사용자 기본 설정입니다. Firefox 사용자 기본 설정에 대한 자세한 내용은 [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox)에서 확인하세요.

`PLAYWRIGHT_FIREFOX_POLICIES_JSON` 환경 변수를 통해 사용자 지정 [`policies.json` file](https://mozilla.github.io/policy-templates/) 경로를 제공할 수도 있습니다.

    * `handleSIGHUP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-handle-sighup)

SIGHUP 시 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `handleSIGINT` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-handle-sigint)

Ctrl-C 시 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `handleSIGTERM` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-handle-sigterm)

SIGTERM 시 브라우저 프로세스를 종료합니다. 기본값은 `true`입니다.

    * `headless` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-headless)

브라우저를 headless 모드로 실행할지 여부입니다. [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) 및 [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/)에 대한 자세한 내용을 참고하세요. 기본값은 `true`입니다.

    * `host` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ 추가됨: v1.45[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-host)

웹 소켓에 사용할 호스트입니다. 선택 사항이며 생략하면 IPv6를 사용할 수 있을 때 서버는 지정되지 않은 IPv6 주소(::)에서 연결을 수락하고, 그렇지 않으면 지정되지 않은 IPv4 주소(0.0.0.0)에서 연결을 수락합니다. 특정 인터페이스를 선택해 보안을 강화하는 것을 고려하세요.

- `ignoreDefaultArgs` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-ignore-default-args)

`true`이면 Playwright는 자체 구성 인수를 전달하지 않고 [args](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-args)의 값만 사용합니다. 배열이 주어지면 지정된 기본 인수들을 필터링해 제외합니다. 위험한 옵션이므로 주의해서 사용하세요. 기본값은 `false`입니다.

    * `logger` [Logger](https://playwright.dev/docs/api/class-logger "Logger") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-logger)

사용 중단됨

logger로 수신되는 로그는 완전하지 않습니다. 대신 tracing을 사용하세요.

Playwright 로깅을 위한 Logger sink입니다.

    * `port` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-port)

웹 소켓에 사용할 포트입니다. 기본값은 0이며, 사용 가능한 아무 포트나 선택합니다.

    * `proxy` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-proxy)

      * `server` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

모든 요청에 사용할 프록시입니다. HTTP 및 SOCKS 프록시를 지원하며, 예: `http://myproxy.com:3128` 또는 `socks5://myproxy.com:3128`. 축약형 `myproxy.com:3128`은 HTTP 프록시로 간주됩니다.

      * `bypass` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

프록시를 우회할 도메인 목록(쉼표 구분)입니다. 예: `".com, chromium.org, .domain.com"`.

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 사용자 이름입니다.

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요한 경우 사용할 선택적 비밀번호입니다.

네트워크 프록시 설정입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-timeout)

브라우저 인스턴스 시작을 기다릴 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

    * `tracesDir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-traces-dir)

지정하면 trace가 이 디렉터리에 저장됩니다.

    * `wsPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ 추가됨: v1.15[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-option-ws-path)

Browser Server를 제공할 경로입니다. 보안을 위해 기본값은 추측하기 어려운 문자열입니다.

경고

`wsPath`를 알고 있는 모든 프로세스 또는 웹 페이지(Playwright에서 실행 중인 것 포함)는 OS 사용자를 제어할 수 있습니다. 따라서 이 옵션을 사용할 때는 추측하기 어려운 토큰을 사용해야 합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[BrowserServer](https://playwright.dev/docs/api/class-browserserver "BrowserServer")>[#](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-server-return)

---

### name[​](https://playwright.dev/docs/api/class-browsertype#browser-type-name "Direct link to name")

v1.9 이전에 추가됨 browserType.name

브라우저 이름을 반환합니다. 예: `'chromium'`, `'webkit'`, `'firefox'`.

**사용법**

```
    browserType.name();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browsertype#browser-type-name-return)
