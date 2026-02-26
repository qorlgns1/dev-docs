---
title: "BrowserServer"
description: "v1.9 이전에 추가됨: browserServer.close"
---

Source URL: https://playwright.dev/docs/api/class-browserserver

# BrowserServer | Playwright

---

## 메서드[​](https://playwright.dev/docs/api/class-browserserver#methods "메서드로 직접 연결")

### close[​](https://playwright.dev/docs/api/class-browserserver#browser-server-close "close로 직접 연결")

v1.9 이전에 추가됨: browserServer.close

브라우저를 정상적으로 종료하고 프로세스가 종료되었는지 확인합니다.

**사용법**

```
    await browserServer.close();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browserserver#browser-server-close-return)

---

### kill[​](https://playwright.dev/docs/api/class-browserserver#browser-server-kill "kill로 직접 연결")

v1.9 이전에 추가됨: browserServer.kill

브라우저 프로세스를 강제 종료하고, 프로세스가 완전히 종료될 때까지 기다립니다.

**사용법**

```
    await browserServer.kill();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-browserserver#browser-server-kill-return)

---

### process[​](https://playwright.dev/docs/api/class-browserserver#browser-server-process "process로 직접 연결")

v1.9 이전에 추가됨: browserServer.process

생성된 브라우저 애플리케이션 프로세스입니다.

**사용법**

```
    browserServer.process();

```

**반환값**

- [ChildProcess](https://nodejs.org/api/child_process.html "ChildProcess")[#](https://playwright.dev/docs/api/class-browserserver#browser-server-process-return)

---

### wsEndpoint[​](https://playwright.dev/docs/api/class-browserserver#browser-server-ws-endpoint "wsEndpoint로 직접 연결")

v1.9 이전에 추가됨: browserServer.wsEndpoint

브라우저 websocket url입니다.

브라우저와의 연결을 설정하기 위해 [browserType.connect()](https://playwright.dev/docs/api/class-browsertype#browser-type-connect)의 인자로 사용할 수 있는 브라우저 websocket endpoint입니다.

`launchServer` 옵션에서 listen `host` 옵션을 지정하지 않으면, 실제로는 미지정 주소에서 수신하더라도 localhost가 출력됩니다.

**사용법**

```
    browserServer.wsEndpoint();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-browserserver#browser-server-ws-endpoint-return)

---

## 이벤트[​](https://playwright.dev/docs/api/class-browserserver#events "이벤트로 직접 연결")

### on('close')[​](https://playwright.dev/docs/api/class-browserserver#browser-server-event-close "on('close')로 직접 연결")

v1.9 이전에 추가됨: browserServer.on('close')

브라우저 서버가 종료될 때 발생합니다.

**사용법**

```
    browserServer.on('close', data => {});

```
