---
title: 'Event Processors | Next.js용 Sentry'
description: '스코프 레벨 또는 전역에서 자체 이벤트 프로세서를 추가해, 이벤트에 추가 데이터를 보강할 수 있습니다. 이벤트 프로세서는  및 과 비슷하지만, 핵심적인 차이점이 두 가지 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/event-processors

# Event Processors | Next.js용 Sentry

스코프 레벨 또는 전역에서 자체 이벤트 프로세서를 추가해, 이벤트에 추가 데이터를 보강할 수 있습니다. 이벤트 프로세서는 `beforeSend` 및 `beforeSendTransaction`과 비슷하지만, 핵심적인 차이점이 두 가지 있습니다.

* `beforeSend` 및 `beforeSendTransaction`은 다른 모든 이벤트 프로세서 이후에 마지막으로 실행되도록 보장됩니다(즉, 전송 직전에 이벤트의 최종 버전을 받으므로 이름도 그에 맞습니다). 아래 두 방법으로 추가한 이벤트 프로세서는 실행 순서가 결정되어 있지 않으므로, 이벤트 프로세서가 실행된 뒤에도 이벤트가 계속 변경될 수 있습니다.
* `beforeSend`, `beforeSendTransaction`, 그리고 `Sentry.addEventProcessor`로 추가한 프로세서는 스코프와 무관하게 전역으로 실행되지만, `scope.addEventProcessor`로 추가한 프로세서는 해당 스코프가 활성화된 동안 캡처된 이벤트에서만 실행됩니다.

`beforeSend` 및 `beforeSendTransaction`과 마찬가지로, 이벤트 프로세서에는 이벤트 자체와 추가 메타데이터를 담은 [ `hint` 객체](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints)라는 두 인자가 전달됩니다.

현재 스코프에 추가된 이벤트 프로세서는 추가된 이후 전송되는 모든 이벤트에서 실행됩니다.

```javascript
Sentry.addEventProcessor(function (event, hint) {
  // Add anything to the event here
  // returning `null` will drop the event
  return event;
});
```

`withScope`를 사용해 로컬 스코프에 추가된 이벤트 프로세서는 해당 스코프 내부에서 캡처된 이벤트에만 적용됩니다.

```javascript
Sentry.withScope(function (scope) {
  scope.addEventProcessor(function (event, hint) {
    // Add anything to the event here
    // returning `null` will drop the event
    return event;
  });
  // The event processor will apply to this event
  Sentry.captureMessage("Test");
});

// The event processor will NOT apply to this event
Sentry.captureMessage("Test2");
```

