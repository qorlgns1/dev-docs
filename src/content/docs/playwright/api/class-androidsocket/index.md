---
title: "AndroidSocket"
description: "추가된 버전: v1.9 androidSocket.close"
---

Source URL: https://playwright.dev/docs/api/class-androidsocket

# AndroidSocket | Playwright

[AndroidSocket](https://playwright.dev/docs/api/class-androidsocket "AndroidSocket")는 [AndroidDevice](https://playwright.dev/docs/api/class-androiddevice "AndroidDevice")에서 시작된 프로세스와 통신하는 방법입니다. 소켓을 열려면 [androidDevice.open()](https://playwright.dev/docs/api/class-androiddevice#android-device-open)을 사용하세요.

---

## 메서드[​](https://playwright.dev/docs/api/class-androidsocket#methods "Direct link to Methods")

### close[​](https://playwright.dev/docs/api/class-androidsocket#android-socket-close "Direct link to close")

추가된 버전: v1.9 androidSocket.close

소켓을 닫습니다.

**사용법**

```
    await androidSocket.close();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androidsocket#android-socket-close-return)

---

### write[​](https://playwright.dev/docs/api/class-androidsocket#android-socket-write "Direct link to write")

추가된 버전: v1.9 androidSocket.write

소켓에 일부 [data](https://playwright.dev/docs/api/class-androidsocket#android-socket-write-option-data)를 씁니다.

**사용법**

```
    await androidSocket.write(data);

```

**인수**

- `data` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")[#](https://playwright.dev/docs/api/class-androidsocket#android-socket-write-option-data)

쓸 데이터입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-androidsocket#android-socket-write-return)

---

## 이벤트[​](https://playwright.dev/docs/api/class-androidsocket#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-androidsocket#android-socket-event-close "Direct link to on('close')")

추가된 버전: v1.9 androidSocket.on('close')

소켓이 닫힐 때 발생합니다.

**사용법**

```
    androidSocket.on('close', data => {});

```

---

### on('data')[​](https://playwright.dev/docs/api/class-androidsocket#android-socket-event-data "Direct link to on('data')")

추가된 버전: v1.9 androidSocket.on('data')

소켓에서 읽을 수 있는 데이터가 있을 때 발생합니다.

**사용법**

```
    androidSocket.on('data', data => {});

```

**이벤트 데이터**

- [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")
