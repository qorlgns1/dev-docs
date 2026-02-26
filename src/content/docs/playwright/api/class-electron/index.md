---
title: "Electron"
description: "Playwright는 Electron 자동화를 실험적으로 지원합니다.  네임스페이스는 다음을 통해 접근할 수 있습니다:"
---

Source URL: https://playwright.dev/docs/api/class-electron

# Electron | Playwright

Playwright는 Electron 자동화를 **실험적**으로 지원합니다. `electron` 네임스페이스는 다음을 통해 접근할 수 있습니다:

```
    const { _electron } = require('playwright');

```

Electron 자동화 스크립트 예시는 다음과 같습니다:

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

**지원되는 Electron 버전:**

- v12.2.0+
- v13.4.0+
- v14+

**알려진 이슈:**

Electron을 실행하지 못하고 실행 중 타임아웃이 발생하는 경우, 다음을 시도해 보세요:

- `nodeCliInspect` ([FuseV1Options.EnableNodeCliInspectArguments](https://www.electronjs.org/docs/latest/tutorial/fuses#nodecliinspect)) fuse가 `false`로 설정되어 있지 않은지 확인하세요.

---

## 메서드[​](https://playwright.dev/docs/api/class-electron#methods "Direct link to Methods")

### launch[​](https://playwright.dev/docs/api/class-electron#electron-launch "Direct link to launch")

추가된 버전: v1.9 electron.launch

[executablePath](https://playwright.dev/docs/api/class-electron#electron-launch-option-executable-path)로 지정된 electron 애플리케이션을 실행합니다.

**사용법**

```
    await electron.launch();
    await electron.launch(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `acceptDownloads` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-accept-downloads)

모든 첨부 파일을 자동으로 다운로드할지 여부입니다. 기본값은 `true`이며, 모든 다운로드를 허용합니다.

    * `args` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-args)

실행 시 애플리케이션에 전달할 추가 인수입니다. 일반적으로 여기에는 메인 스크립트 이름을 전달합니다.

    * `bypassCSP` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-bypass-csp)

페이지의 Content-Security-Policy 우회를 켜거나 끕니다. 기본값은 `false`입니다.

    * `colorScheme` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | "light" | "dark" | "no-preference" _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-color-scheme)

[prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) 미디어 기능을 에뮬레이션하며, 지원 값은 `'light'`와 `'dark'`입니다. 자세한 내용은 [page.emulateMedia()](https://playwright.dev/docs/api/class-page#page-emulate-media)를 참고하세요. `null`을 전달하면 에뮬레이션이 시스템 기본값으로 재설정됩니다. 기본값은 `'light'`입니다.

    * `cwd` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-cwd)

애플리케이션을 실행할 현재 작업 디렉터리입니다.

    * `env` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-env)

Electron에서 볼 수 있는 환경 변수를 지정합니다. 기본값은 `process.env`입니다.

    * `executablePath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-executable-path)

지정한 Electron 애플리케이션을 실행합니다. 지정하지 않으면 이 패키지에 설치된 기본 Electron 실행 파일(`node_modules/.bin/electron`)을 실행합니다.

    * `extraHTTPHeaders` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-extra-http-headers)

모든 요청과 함께 전송할 추가 HTTP 헤더를 포함하는 객체입니다. 기본값은 없음입니다.

    * `geolocation` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-geolocation)

      * `latitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-90에서 90 사이의 위도입니다.

      * `longitude` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

-180에서 180 사이의 경도입니다.

      * `accuracy` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

0 이상의 정확도 값입니다. 기본값은 `0`입니다.

    * `httpCredentials` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-http-credentials)

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

특정 origin (scheme://host:port)에만 http 자격 증명 전송을 제한합니다.

      * `send` "unauthorized" | "always" _(optional)_

이 옵션은 해당 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")에서 전송되는 요청에만 적용되며, 브라우저에서 전송되는 요청에는 영향을 주지 않습니다. `'always'` - 기본 인증 자격 증명이 포함된 `Authorization` 헤더가 각 API 요청마다 전송됩니다. `'unauthorized` - `WWW-Authenticate` 헤더가 포함된 401 (Unauthorized) 응답을 받은 경우에만 자격 증명이 전송됩니다. 기본값은 `'unauthorized'`입니다.

[HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)을 위한 자격 증명입니다. origin을 지정하지 않으면, 인증되지 않은 응답 시 사용자 이름과 비밀번호가 모든 서버로 전송됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `locale` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-locale)

사용자 로캘(예: `en-GB`, `de-DE` 등)을 지정합니다. 로캘은 `navigator.language` 값, `Accept-Language` 요청 헤더 값, 숫자 및 날짜 형식 규칙에 영향을 줍니다. 기본값은 시스템 기본 로캘입니다. 에뮬레이션에 대한 자세한 내용은 [emulation guide](https://playwright.dev/docs/emulation#locale--timezone)를 참고하세요.

    * `offline` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-offline)

네트워크 오프라인 상태를 에뮬레이션할지 여부입니다. 기본값은 `false`입니다. 자세한 내용은 [network emulation](https://playwright.dev/docs/emulation#offline)을 참고하세요.

    * `recordHar` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-record-har)

      * `omitContent` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_

HAR에서 요청 콘텐츠를 생략할지 제어하는 선택적 설정입니다. 기본값은 `false`입니다. 더 이상 권장되지 않으며, 대신 `content` 정책을 사용하세요.

      * `content` "omit" | "embed" | "attach" _(optional)_

리소스 콘텐츠 관리를 제어하는 선택적 설정입니다. `omit`을 지정하면 콘텐츠가 저장되지 않습니다. `attach`를 지정하면 리소스가 별도 파일 또는 ZIP 아카이브 항목으로 저장됩니다. `embed`를 지정하면 HAR 사양에 따라 콘텐츠가 HAR 파일 내에 인라인으로 저장됩니다. 기본값은 `.zip` 출력 파일의 경우 `attach`, 그 외 확장자는 모두 `embed`입니다.

      * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

HAR 파일을 기록할 파일 시스템 경로입니다. 파일 이름이 `.zip`으로 끝나면 기본적으로 `content: 'attach'`가 사용됩니다.

      * `mode` "full" | "minimal" _(optional)_

`minimal`로 설정하면 HAR 기반 라우팅에 필요한 정보만 기록합니다. 이 경우 HAR에서 재생할 때 사용되지 않는 크기, 타이밍, 페이지, 쿠키, 보안 및 기타 유형의 HAR 정보가 생략됩니다. 기본값은 `full`입니다.

      * `urlFilter` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_

HAR에 저장할 요청을 필터링하는 glob 또는 regex 패턴입니다. 컨텍스트 옵션으로 [baseURL](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url)이 제공되었고 전달된 URL이 경로인 경우, [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 통해 병합됩니다. 기본값은 없음입니다.

모든 페이지에 대해 `recordHar.path` 파일로 [HAR](http://www.softwareishard.com/blog/har-12-spec) 기록을 활성화합니다. 지정하지 않으면 HAR은 기록되지 않습니다. HAR이 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

    * `recordVideo` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-record-video)

      * `dir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

비디오를 저장할 디렉터리 경로입니다.

      * `size` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_

        * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 너비입니다.

        * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

비디오 프레임 높이입니다.

기록되는 비디오의 선택적 크기입니다. 지정하지 않으면 크기는 `viewport`를 800x800에 맞도록 축소한 값이 됩니다. `viewport`가 명시적으로 설정되지 않은 경우 비디오 크기의 기본값은 800x450입니다. 필요할 경우 각 페이지의 실제 화면은 지정된 크기에 맞도록 축소됩니다.

모든 페이지에 대해 `recordVideo.dir` 디렉터리에 비디오 기록을 활성화합니다. 지정하지 않으면 비디오는 기록되지 않습니다. 비디오가 저장되도록 [browserContext.close()](https://playwright.dev/docs/api/class-browsercontext#browser-context-close)를 반드시 await 하세요.

- `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_ 추가된 버전: v1.15[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-timeout)

애플리케이션 시작을 기다리는 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 제한 시간을 비활성화하려면 `0`을 전달하세요.

    * `timezoneId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_ 추가된 버전: v1.12[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-timezone-id)

컨텍스트의 시간대를 변경합니다. 지원되는 시간대 ID 목록은 [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)를 참조하세요. 기본값은 시스템 시간대입니다.

    * `tracesDir` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_ 추가된 버전: v1.36[#](https://playwright.dev/docs/api/class-electron#electron-launch-option-traces-dir)

지정하면 trace가 이 디렉터리에 저장됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[ElectronApplication](https://playwright.dev/docs/api/class-electronapplication "ElectronApplication")>[#](https://playwright.dev/docs/api/class-electron#electron-launch-return)
