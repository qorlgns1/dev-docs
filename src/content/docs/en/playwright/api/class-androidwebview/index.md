---
title: "AndroidWebView"
description: "Added in: v1.9 androidWebView.page"
---

Source URL: https://playwright.dev/docs/api/class-androidwebview

# AndroidWebView | Playwright

[AndroidWebView](https://playwright.dev/docs/api/class-androidwebview "AndroidWebView") represents a WebView open on the [AndroidDevice](https://playwright.dev/docs/api/class-androiddevice "AndroidDevice"). WebView is usually obtained using [androidDevice.webView()](https://playwright.dev/docs/api/class-androiddevice#android-device-web-view).

---

## Methods[​](https://playwright.dev/docs/api/class-androidwebview#methods "Direct link to Methods")

### page[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-page "Direct link to page")

Added in: v1.9 androidWebView.page

Connects to the WebView and returns a regular Playwright [Page](https://playwright.dev/docs/api/class-page "Page") to interact with.

**Usage**

```
    await androidWebView.page();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Page](https://playwright.dev/docs/api/class-page "Page")>[#](https://playwright.dev/docs/api/class-androidwebview#android-web-view-page-return)

---

### pid[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pid "Direct link to pid")

Added in: v1.9 androidWebView.pid

WebView process PID.

**Usage**

```
    androidWebView.pid();

```

**Returns**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pid-return)

---

### pkg[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pkg "Direct link to pkg")

Added in: v1.9 androidWebView.pkg

WebView package identifier.

**Usage**

```
    androidWebView.pkg();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-androidwebview#android-web-view-pkg-return)

---

## Events[​](https://playwright.dev/docs/api/class-androidwebview#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-androidwebview#android-web-view-event-close "Direct link to on('close')")

Added in: v1.9 androidWebView.on('close')

Emitted when the WebView is closed.

**Usage**

```
    androidWebView.on('close', data => {});

```
