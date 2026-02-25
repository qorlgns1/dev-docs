---
title: '커스텀 통합 | Next.js용 Sentry'
description: 'SDK에 기본 포함된 통합 외에도, 커스텀 통합을 직접 작성할 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom

# 커스텀 통합 | Next.js용 Sentry

SDK에 기본 포함된 통합 외에도, 커스텀 통합을 직접 작성할 수 있습니다.

커스텀 통합은 [Integration interface](https://github.com/getsentry/sentry-javascript/blob/master/packages/core/src/types-hoist/integration.ts)를 따라야 합니다.

커스텀 통합은 다음과 같이 생성해 SDK에 추가할 수 있습니다:

```javascript
function myAwesomeIntegration() {
  return {
    name: "MyAwesomeIntegration",
    setup(client) {
      // Do something when the SDK is initialized
      // The client that is being setup is passed to the hook
    },
  };
}

Sentry.init({
  // ...
  integrations: [myAwesomeIntegration()],
});
```

통합의 모든 hook은 선택 사항입니다. 필수 필드는 `name` 하나뿐입니다. 커스텀 통합에서는 다음 hook 중 하나 또는 여러 개를 사용할 수 있습니다:

- [`setup`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md#setup)

`setup` hook은 SDK가 초기화될 때 호출됩니다. 인자로 client 인스턴스를 받습니다. 초기화 시점에 코드를 실행하려면 이 hook을 사용해야 합니다.

```javascript
const integration = {
  name: "MyAwesomeIntegration",
  setup(client) {
    setupCustomSentryListener(client);
  },
};
```

- [`processEvent`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md#processevent)

이 hook은 이벤트가 Sentry로 전송되기 전에 이벤트를 수정하는 데 사용할 수 있습니다. 인자로 event를 받고, 수정된 event를 반환해야 합니다. 또한 이 hook은 추가 이벤트 메타데이터를 담을 수 있는 hint 객체와, 이벤트를 전송하는 client도 함께 받습니다. 이벤트 전송을 중단하려면 `null`을 반환할 수도 있습니다.

```javascript
const integration = {
  name: "MyAwesomeIntegration",
  processEvent(event, hint, client) {
    event.extra = {
      ...event.extra,
      myCustomTag: "value",
    };
    // Return the modified event,
    // or return `null` to drop the event
    return event;
  },
};
```

event 또는 `null`로 resolve되는 promise를 반환할 수도 있습니다. 하지만 이벤트 전송을 지연시킬 수 있으므로 권장되지 않으며, 가능한 한 피해야 합니다.

- [`preprocessEvent`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md#preprocessevent)

이 hook은 `processEvent`와 유사하지만, 이벤트가 다른 `processEvent` hook으로 전달되기 전에 먼저 호출됩니다. 처리 순서가 중요한 경우에 사용할 수 있습니다.

대부분의 경우 `processEvent`만 사용하면 됩니다. 다른 `processEvent` hook보다 먼저 호출되어야 함을 보장해야 할 때만 `preprocessEvent`를 사용하세요.

`processEvent`와 마찬가지로, 이 hook도 event, hint, client를 인자로 받습니다. 다만 이 hook에서는 수정된 event를 반환하거나 이벤트를 중단하기 위한 `null` 반환이 허용되지 않습니다. 대신 전달된 event를 이 hook 내부에서 직접 변경만 할 수 있습니다:

```javascript
const integration = {
  name: "MyAwesomeIntegration",
  preprocessEvent(event, hint, client) {
    event.extra = {
      ...event.extra,
      myCustomTag: "value",
    };
    // Nothing to return, just mutate the event
  },
};
```

- [`setupOnce`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md#setuponce)

이 hook은 `setup`과 비슷하지만, SDK를 다시 초기화하더라도 한 번만 실행됩니다. 인자는 받지 않습니다. 일반적으로는 이것 대신 `setup`을 사용하는 것이 좋습니다. `setupOnce`를 써야 하는 유일한 이유는, 예를 들어 `Sentry.init()`를 여러 번 호출할 수 있는 상황에서 특정 코드가 정확히 한 번만 실행되도록 보장하려는 경우입니다.

```javascript
const integration = {
  name: "MyAwesomeIntegration",
  setupOnce() {
    wrapLibrary();
  },
};
```

- [`afterAllSetup`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md#afterallsetup)

이 hook은 모든 통합에 대해 `setupOnce()`와 `setup()`이 호출된 뒤에 트리거됩니다. 다른 모든 통합이 먼저 실행된 뒤여야 중요한 경우에 사용할 수 있습니다.

대부분의 경우 이 hook은 필요하지 않으며, 대신 `setup`을 사용하면 됩니다.

이 hook은 첫 번째 인자로 설정 중인 `client`를 받습니다.

```javascript
const integration = {
  name: "MyAwesomeIntegration",
  afterAllSetup(client) {
    // We can be sure that all other integrations
    // have run their `setup` and `setupOnce` hooks now
    startSomeThing(client);
  },
};
```

