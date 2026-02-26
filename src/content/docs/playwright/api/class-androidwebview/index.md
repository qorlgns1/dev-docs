---
title: "AndroidWebView"
description: "추가된 버전: v1.9 androidWebView.page"
---

Source URL: https://playwright.dev/docs/api/class-androidwebview

# AndroidWebView | Playwright

[AndroidWebView](https://playwright.dev/docs/api/class-androidwebview "AndroidWebView")는 [AndroidDevice](https://playwright.dev/docs/api/class-androiddevice "AndroidDevice")에서 열려 있는 WebView를 나타냅니다. WebView는 일반적으로 [androidDevice.webView()](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view)를 사용해 가져옵니다.

---

## Methods[​](https://playwright.dev/docs/api/class-androidwebview#methods "Direct link to Methods")

### page[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-page "Direct link to page")

추가된 버전: v1.9 androidWebView.page

WebView에 연결하고 상호작용할 수 있는 일반 Playwright [Page](https://playwright.dev/docs/api/class-page "Page")를 반환합니다.

**사용법**

```
    await androidWebView.page();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-androidwebview#android-web-view-page-return)

---

### pid[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pid "Direct link to pid")

추가된 버전: v1.9 androidWebView.pid

WebView 프로세스 PID입니다.

**사용법**

```
    androidWebView.pid();

```

**반환값**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pid-return)

---

### pkg[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pkg "Direct link to pkg")

추가된 버전: v1.9 androidWebView.pkg

WebView 패키지 식별자입니다.

**사용법**

```
    androidWebView.pkg();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pkg-return)

---

## Events[​](https://playwright.dev/docs/api/class-androidwebview#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-event-close "Direct link to on('close')")

추가된 버전: v1.9 androidWebView.on('close')

WebView가 닫힐 때 발생합니다.

**사용법**

```
    androidWebView.on('close', data => {});

```
