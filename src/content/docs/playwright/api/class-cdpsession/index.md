---
title: "CDPSession"
description: "인스턴스는 원시 Chrome Devtools Protocol과 통신하는 데 사용됩니다:"
---

Source URL: https://playwright.dev/docs/api/class-cdpsession

# CDPSession | Playwright

`CDPSession` 인스턴스는 원시 Chrome Devtools Protocol과 통신하는 데 사용됩니다:

- 프로토콜 메서드는 `session.send` 메서드로 호출할 수 있습니다.
- 프로토콜 이벤트는 `session.on` 메서드로 구독할 수 있습니다.

유용한 링크:

- DevTools Protocol 문서는 여기에서 확인할 수 있습니다: [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/).
- DevTools Protocol 시작하기: <https://github.com/aslushnikov/getting-started-with-cdp/blob/master/README.md>

```
    const client = await page.context().newCDPSession(page);
    await client.send('Animation.enable');
    client.on('Animation.animationCreated', () => console.log('Animation created!'));
    const response = await client.send('Animation.getPlaybackRate');
    console.log('playback rate is ' + response.playbackRate);
    await client.send('Animation.setPlaybackRate', {
      playbackRate: response.playbackRate / 2
    });

```

---

## Methods[​](https://playwright.dev/docs/api/class-cdpsession#methods "Direct link to Methods")

### detach[​](https://playwright.dev/docs/api/class-cdpsession#cdp-session-detach "Direct link to detach")

v1.9 이전에 추가됨 cdpSession.detach

대상에서 CDPSession을 분리합니다. 분리된 후에는 CDPSession 객체가 더 이상 어떤 이벤트도 발생시키지 않으며, 메시지 전송에도 사용할 수 없습니다.

**사용법**

```
    await cdpSession.detach();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-cdpsession#cdp-session-detach-return)

---

### send[​](https://playwright.dev/docs/api/class-cdpsession#cdp-session-send "Direct link to send")

v1.9 이전에 추가됨 cdpSession.send

**사용법**

```
    await cdpSession.send(method);
    await cdpSession.send(method, params);

```

**인수**

- `method` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-cdpsession#cdp-session-send-option-method)

프로토콜 메서드 이름입니다.

- `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-cdpsession#cdp-session-send-option-params)

선택적 메서드 매개변수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-cdpsession#cdp-session-send-return)
