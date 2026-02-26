---
title: 'BrowserApiErrors | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors

# BrowserApiErrors | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 작동합니다.

*가져오기 이름: `Sentry.browserApiErrorsIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

이 통합은 비동기 예외를 처리하기 위해 네이티브 시간 및 이벤트 API(`setTimeout`, `setInterval`, `requestAnimationFrame`, `addEventListener/removeEventListener`)를 `try/catch` 블록으로 감쌉니다.

```JavaScript
Sentry.init({
  integrations: [
    Sentry.browserApiErrorsIntegration({
      setTimeout: true,
      setInterval: true,
      requestAnimationFrame: true,
      XMLHttpRequest: true,
      eventTarget: true,
      unregisterOriginalCallbacks: true,
    }),
  ],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#options)

- [`setTimeout`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#settimeout)

*Type: `boolean`*

`setTimeout` 브라우저 내장 메서드를 계측합니다.

- [`setInterval`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#setinterval)

*Type: `boolean`*

`setInterval` 브라우저 내장 메서드를 계측합니다.

- [`requestAnimationFrame`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#requestanimationframe)

*Type: `boolean`*

`requestAnimationFrame` 브라우저 내장 메서드를 계측합니다.

- [`XMLHttpRequest`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#xmlhttprequest)

*Type: `boolean`*

`XMLHttpRequest` 브라우저 내장 메서드를 계측합니다.

- [`eventTarget`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#eventtarget)

*Type: `boolean | string[]`*

기본 이벤트 타깃으로 정해진 항목들에 대해 `addEventListener` 브라우저 내장 메서드를 계측합니다. 기본 이벤트 타깃을 재정의하려면 이벤트 타깃 이름이 담긴 문자열 배열을 제공하세요.

기본 이벤트 타깃 목록:

* `EventTarget`
* `Window`
* `Node`
* `ApplicationCache`
* `AudioTrackList`
* `BroadcastChannel`
* `ChannelMergerNode`
* `CryptoOperation`
* `EventSource`
* `FileReader`
* `HTMLUnknownElement`
* `IDBDatabase`
* `IDBRequest`
* `IDBTransaction`
* `KeyOperation`
* `MediaController`
* `MessagePort`
* `ModalWindow`
* `Notification`
* `SVGElementInstance`
* `Screen`
* `SharedWorker`
* `TextTrack`
* `TextTrackCue`
* `TextTrackList`
* `WebSocket`
* `WebSocketWorker`
* `Worker`
* `XMLHttpRequest`
* `XMLHttpRequestEventTarget`
* `XMLHttpRequestUpload`

- [`unregisterOriginalCallbacks`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md#unregisteroriginalcallbacks)

*Type: `boolean`*

원래의 `EventTarget.addEventListener` 콜백 등록을 해제합니다. 이 통합(또는 SDK) 때문에 `addEventListener` 콜백이 중복 호출되는 문제가 발생한다면, 이 옵션을 `true`로 설정하세요. 이는 보통 페이지 라이프사이클에서 SDK가 너무 늦게 초기화되었다는 신호입니다. 이런 경우 이 문제를 피하려면 SDK를 가능한 한 이르게 초기화하는 것을 고려하는 것이 좋습니다.

