---
title: "Android"
description: "Playwright는 Android 자동화를 실험적으로 지원합니다. 여기에는 Android용 Chrome과 Android WebView가 포함됩니다."
---

Source URL: https://playwright.dev/docs/api/class-android

# Android | Playwright

Playwright는 Android 자동화를 **실험적으로** 지원합니다. 여기에는 Android용 Chrome과 Android WebView가 포함됩니다.

_요구 사항_

- Android 기기 또는 AVD 에뮬레이터.
- 기기와 인증된 상태로 실행 중인 [ADB daemon](https://developer.android.com/studio/command-line/adb). 일반적으로 `adb devices`를 실행하는 것만으로 충분합니다.
- 기기에 설치된 [`Chrome 87`](https://play.google.com/store/apps/details?id=com.android.chrome) 이상
- `chrome://flags`에서 "Enable command line on non-rooted devices" 활성화.

_알려진 제한 사항_

- Raw USB 작업은 아직 지원되지 않으므로 ADB가 필요합니다.
- 스크린샷을 생성하려면 기기가 깨어 있어야 합니다. 개발자 모드의 "Stay awake"를 활성화하면 도움이 됩니다.
- 기기를 대상으로 모든 테스트를 실행하지는 않았으므로, 모든 기능이 동작하는 것은 아닙니다.

_실행 방법_

Android 자동화 스크립트 예시는 다음과 같습니다:

```
    const { _android: android } = require('playwright');

    (async () => {
      // Connect to the device.
      const [device] = await android.devices();
      console.log(`Model: ${device.model()}`);
      console.log(`Serial: ${device.serial()}`);
      // Take screenshot of the whole device.
      await device.screenshot({ path: 'device.png' });

      {
        // --------------------- WebView -----------------------

        // Launch an application with WebView.
        await device.shell('am force-stop org.chromium.webview_shell');
        await device.shell('am start org.chromium.webview_shell/.WebViewBrowserActivity');
        // Get the WebView.
        const webview = await device.webView({ pkg: 'org.chromium.webview_shell' });

        // Fill the input box.
        await device.fill({
          res: 'org.chromium.webview_shell:id/url_field',
        }, 'github.com/microsoft/playwright');
        await device.press({
          res: 'org.chromium.webview_shell:id/url_field',
        }, 'Enter');

        // Work with WebView's page as usual.
        const page = await webview.page();
        await page.waitForNavigation({ url: /.*microsoft\/playwright.*/ });
        console.log(await page.title());
      }

      {
        // --------------------- Browser -----------------------

        // Launch Chrome browser.
        await device.shell('am force-stop com.android.chrome');
        const context = await device.launchBrowser();

        // Use BrowserContext as usual.
        const page = await context.newPage();
        await page.goto('https://webkit.org/');
        console.log(await page.evaluate(() => window.location.href));
        await page.screenshot({ path: 'page.png' });

        await context.close();
      }

      // Close the device.
      await device.close();
    })();

```

---

## 메서드[​](https://playwright.dev/docs/api/class-android#methods "Direct link to Methods")

### connect[​](https://playwright.dev/docs/api/class-android#android-connect "Direct link to connect")

추가된 버전: v1.28 android.connect

이 메서드는 기존 Android 기기에 Playwright를 연결합니다. 새 Android 서버 인스턴스를 시작하려면 [android.launchServer()](https://playwright.dev/docs/api/class-android#android-launch-server)를 사용하세요.

**사용법**

```
    await android.connect(wsEndpoint);
    await android.connect(wsEndpoint, options);

```

**인수**

- `wsEndpoint` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-android#android-connect-option-ws-endpoint)

연결할 브라우저 websocket 엔드포인트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-connect-option-headers)

web socket 연결 요청과 함께 전송할 추가 HTTP 헤더입니다. 선택 사항입니다.

    * `slowMo` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-connect-option-slow-mo)

Playwright 작업을 지정한 밀리초만큼 느리게 만듭니다. 진행 상황을 확인할 때 유용합니다. 기본값은 `0`입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-connect-option-timeout)

연결이 설정될 때까지 기다리는 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[AndroidDevice](https://playwright.dev/docs/api/class-androiddevice "AndroidDevice")>[#](https://playwright.dev/docs/api/class-android#android-connect-return)

---

### devices[​](https://playwright.dev/docs/api/class-android#android-devices "Direct link to devices")

추가된 버전: v1.9 android.devices

감지된 Android 기기 목록을 반환합니다.

**사용법**

```
    await android.devices();
    await android.devices(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `host` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_ 추가된 버전: v1.22[#](https://playwright.dev/docs/api/class-android#android-devices-option-host)

ADB 서버 연결을 설정할 선택적 호스트입니다. 기본값은 `127.0.0.1`입니다.

    * `omitDriverInstall` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ 추가된 버전: v1.21[#](https://playwright.dev/docs/api/class-android#android-devices-option-omit-driver-install)

연결 시 playwright 드라이버를 자동 설치하지 않도록 합니다. 드라이버가 이미 설치되어 있다고 가정합니다.

    * `port` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_ 추가된 버전: v1.20[#](https://playwright.dev/docs/api/class-android#android-devices-option-port)

ADB 서버 연결을 설정할 선택적 포트입니다. 기본값은 `5037`입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[AndroidDevice](https://playwright.dev/docs/api/class-androiddevice "AndroidDevice")>>[#](https://playwright.dev/docs/api/class-android#android-devices-return)

---

### launchServer[​](https://playwright.dev/docs/api/class-android#android-launch-server "Direct link to launchServer")

추가된 버전: v1.28 android.launchServer

클라이언트가 연결할 수 있는 Playwright Android 서버를 시작합니다. 다음 예제를 참고하세요.

**사용법**

서버 측:

```
    const { _android } = require('playwright');

    (async () => {
      const browserServer = await _android.launchServer({
        // If you have multiple devices connected and want to use a specific one.
        // deviceSerialNumber: '<deviceSerialNumber>',
      });
      const wsEndpoint = browserServer.wsEndpoint();
      console.log(wsEndpoint);
    })();

```

클라이언트 측:

```
    const { _android } = require('playwright');

    (async () => {
      const device = await _android.connect('<wsEndpoint>');

      console.log(device.model());
      console.log(device.serial());
      await device.shell('am force-stop com.android.chrome');
      const context = await device.launchBrowser();

      const page = await context.newPage();
      await page.goto('https://webkit.org/');
      console.log(await page.evaluate(() => window.location.href));
      await page.screenshot({ path: 'page-chrome-1.png' });

      await context.close();
    })();

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `adbHost` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-launch-server-option-adb-host)

ADB 서버 연결을 설정할 선택적 호스트입니다. 기본값은 `127.0.0.1`입니다.

    * `adbPort` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-launch-server-option-adb-port)

ADB 서버 연결을 설정할 선택적 포트입니다. 기본값은 `5037`입니다.

    * `deviceSerialNumber` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-launch-server-option-device-serial-number)

브라우저를 시작할 선택적 기기 시리얼 번호입니다. 지정하지 않았는데 여러 기기가 연결되어 있으면 예외가 발생합니다.

    * `host` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_ 추가된 버전: v1.45[#](https://playwright.dev/docs/api/class-android#android-launch-server-option-host)

web socket에 사용할 호스트입니다. 선택 사항이며 생략하면 IPv6를 사용할 수 있을 때 서버는 지정되지 않은 IPv6 주소(::)에서 연결을 수락하고, 그렇지 않으면 지정되지 않은 IPv4 주소 (0.0.0.0)에서 연결을 수락합니다. 특정 인터페이스를 선택해 보안을 강화하는 것을 고려하세요.

    * `omitDriverInstall` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-launch-server-option-omit-driver-install)

연결 시 playwright 드라이버를 자동 설치하지 않도록 합니다. 드라이버가 이미 설치되어 있다고 가정합니다.

    * `port` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-launch-server-option-port)

web socket에 사용할 포트입니다. 기본값은 `0`이며 사용 가능한 임의의 포트를 선택합니다.

    * `wsPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_[#](https://playwright.dev/docs/api/class-android#android-launch-server-option-ws-path)

Android Server를 제공할 경로입니다. 보안을 위해 기본값은 추측할 수 없는 문자열입니다.

warning

`wsPath`를 알고 있는 모든 프로세스 또는 웹 페이지(Playwright에서 실행 중인 것 포함)는 OS 사용자를 제어할 수 있습니다. 따라서 이 옵션을 사용할 때는 추측할 수 없는 토큰을 사용해야 합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[BrowserServer](https://playwright.dev/docs/api/class-browserserver "BrowserServer")>[#](https://playwright.dev/docs/api/class-android#android-launch-server-return)

---

### setDefaultTimeout[​](https://playwright.dev/docs/api/class-android#android-set-default-timeout "Direct link to setDefaultTimeout")

추가된 버전: v1.9 android.setDefaultTimeout

이 설정은 [timeout](https://playwright.dev/docs/api/class-android#android-set-default-timeout-option-timeout) 옵션을 받는 모든 메서드의 기본 최대 시간을 변경합니다.

**사용법**

```
    android.setDefaultTimeout(timeout);

```

**인수**

- `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-android#android-set-default-timeout-option-timeout)

최대 시간(밀리초)
