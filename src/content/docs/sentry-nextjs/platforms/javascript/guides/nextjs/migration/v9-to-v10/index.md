---
title: '9.x에서 10.x로 마이그레이션 | Next.js용 Sentry'
description: 'Sentry JavaScript SDK 버전 10은 주로 기반 OpenTelemetry 의존성을 v2로 업그레이드하는 데 초점을 맞추며, 브레이킹 체인지는 최소화되었습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10

# 9.x에서 10.x로 마이그레이션 | Next.js용 Sentry

Sentry JavaScript SDK 버전 10은 주로 기반 OpenTelemetry 의존성을 v2로 업그레이드하는 데 초점을 맞추며, 브레이킹 체인지는 최소화되었습니다.

SDK 버전 10은 Sentry self-hosted 버전 24.4.2 이상과 호환됩니다(v9와 동일). 더 낮은 버전도 계속 동작할 수는 있지만, 모든 기능을 지원하지 않을 수 있습니다.

## [버전 지원 변경 사항:](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#version-support-changes)

Sentry SDK 버전 10에서는 런타임과 프레임워크에 대한 새로운 호환 범위가 적용됩니다.

- [Node.js](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#nodejs)

모든 OpenTelemetry 의존성은 각각 `2.x.x` / `0.20x.x`로 상향되었고, 모든 OpenTelemetry instrumentation도 최신 버전으로 업그레이드되었습니다.

OpenTelemetry v2 버전으로 실행할 수 없다면, SDK 버전 9를 계속 사용하거나 OpenTelemetry peer dependency 범위가 더 넓게 설정된 [@sentry/node-core](https://www.npmjs.com/package/@sentry/node-core)를 대신 사용하는 것을 고려하세요.

- [AWS Lambda Layer 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#aws-lambda-layer-changes)

버전 10용 새로운 AWS Lambda Layer는 `SentryNodeServerlessSDKv10`으로 게시됩니다.

버전 9에 대한 업데이트와 수정은 `SentryNodeServerlessSDKv9`로 게시됩니다.

## [FID Web Vital 보고 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#removed-fid-web-vital-reporting)

**SDK는 더 이상 First Input Delay(FID) 웹 바이탈을 보고하지 않습니다**.

이는 FID가 Interaction to Next Paint(INP)로 대체되어 웹사이트 성능을 평가하고 추적하는 데 더 이상 적절하지 않기 때문입니다. 참고로 FID는 Google의 공식 `web-vitals` 라이브러리에서 오래전에 deprecated 되었고, 결국 버전 `5.0.0`에서 제거되었습니다. Sentry도 이에 맞춰 FID를 제거했습니다.

이 제거는 **브레이킹 API 변경을 수반하지 않습니다**. 다만 드문 경우, Sentry SDK 및 제품 설정 일부를 조정해야 할 수 있습니다.

* `beforeSend` 또는 기타 필터링/이벤트 처리 로직에서 FID에 의존하는 부분을 제거하거나 INP 로직으로 대체하세요.
* FID에 의존하는 Sentry Alerts를 설정해 두었다면, SDK 업그레이드 후 새 값이 없어 해당 알림이 트리거될 수 있다는 점에 유의하세요. 이를 대체하려면 알림(또는 대시보드)을 INP를 사용하도록 조정하세요.

## [Session Replays의 `_experiments.autoFlushOnFeedback` 제거](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#removed-_experimentsautoflushonfeedback-for-session-replays)

`_experiments.autoFlushOnFeedback` 옵션은 제거되었으며, 이제 해당 동작이 기본값입니다.

## [업데이트: `sendDefaultPii`로 제어되는 사용자 IP 주소 수집](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#update-user-ip-address-collection-gated-by-senddefaultpii)

버전 `10.4.0`에서는 원래 SDK `10.0.0`에 포함되었어야 할 변경이 도입되었습니다. 본래 [버전 `9.0.0`](https://docs.sentry.io/platforms/javascript/migration/v8-to-v9.md#behavior-changes)을 대상으로 했지만 v10 전까지 의도한 효과가 없었던 이 변경으로, SDK는 이제 최상위 `sendDefaultPii` init 옵션 값에 따라 사용자 IP 주소 추론을 제어합니다.

* `sendDefaultPii`가 `true`이면, 모든 브라우저 기반 SDK에서 Sentry가 이벤트(에러, 트레이스, 리플레이 등)에 사용자 디바이스의 IP 주소를 추론해 추가합니다.
* `sendDefaultPii`가 `false`이거나 설정되지 않으면, Sentry는 IP 주소 데이터를 추론하거나 수집하지 않습니다.

이는 v9부터 이미 [공지된 동작](https://docs.sentry.io/platforms/javascript/data-management/data-collected.md#users-ip-address-and-location)이었기 때문에, 저희는 이 변경을 [수정 사항](https://github.com/getsentry/sentry-javascript/pull/17364)으로 분류합니다. 다만 그 영향 가능성은 인지하고 있습니다.

사용자 IP 주소를 계속 수신하려면 `Sentry.init` 설정에 `sendDefaultPii: true`를 설정하세요.

```js
Sentry.init({
  // ...
  sendDefaultPii: true,
});
```

불편을 끼쳐드려 죄송합니다.

## [제거된 API](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#removed-apis)

이 섹션의 변경 사항은 deprecated 되었고 이제 제거된 API를 설명합니다.

* `BaseClient`는 제거되었으며, 직접 대체로 `Client`를 사용하세요.
* `hasTracingEnabled`는 제거되었으며, 직접 대체로 `hasSpansEnabled`를 사용하세요.
* `@sentry/core`의 내부 `logger` 및 타입 `Logger` export는 제거되었으며, 대신 `debug`와 타입 `SentryDebugLogger`를 사용하세요. 이는 [Sentry Logging](https://docs.sentry.io/product/explore/logs/getting-started.md)에 사용되는 `logger` export에는 영향을 주지 않습니다.
* `_experiments.enableLogs` 및 `_experiments.beforeSendLog` 옵션은 제거되었으며, 대신 최상위 `enableLogs`와 `beforeSendLog` 옵션을 사용하세요.

```js
// before
Sentry.init({
  _experiments: {
    enableLogs: true,
    beforeSendLog: (log) => {
      return log;
    },
  },
});

// after
Sentry.init({
  enableLogs: true,
  beforeSendLog: (log) => {
    return log;
  },
});
```

## [버전 지원 타임라인](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v9-to-v10.md#version-support-timeline)

버전 지원 타임라인은 SDK를 사용하는 모든 분께 부담이 될 수 있으므로, 별도의 타임라인을 정의하지 않겠습니다. 대신 수요가 있는 한 이전 버전에도 버그 수정과 기능을 적용하겠습니다.

또한 보안 이슈에 대해서는 책임 있게 대응하며, 취약점이 발견되면 거의 모든 경우에 백포트하겠습니다.

단, 백포트 여부는 사안별로 결정됩니다. 이전 SDK 버전에 수정이나 기능이 필요하면 [GitHub Issue](https://github.com/getsentry/sentry-javascript/issues)를 통해 문의해 주세요.

