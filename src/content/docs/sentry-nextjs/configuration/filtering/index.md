---
title: '필터링 | Next.js용 Sentry'
description: '앱에 Sentry를 추가하면 오류와 성능에 대한 많은 유용한 정보를 얻을 수 있습니다. 그리고 많은 정보는 적절한 정보가 합리적인 볼륨으로 들어올 때 좋은 것입니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering

# 필터링 | Next.js용 Sentry

앱에 Sentry를 추가하면 오류와 성능에 대한 많은 유용한 정보를 얻을 수 있습니다. 그리고 많은 정보는 적절한 정보가 합리적인 볼륨으로 들어올 때 좋은 것입니다.

Sentry는 sentry.io에서 다양한 이벤트를 걸러낼 수 있도록 프로젝트별로 활성화할 수 있는 [Inbound Filters](https://docs.sentry.io/concepts/data-management/filtering.md)를 제공합니다. 미리 정의된 인바운드 필터(예: 알려진 브라우저 확장 프로그램 필터링)를 사용할 수 있고, 메시지 기반 사용자 정의 필터도 추가할 수 있습니다.

다만 실제로 원하지 않는 이벤트를 전송하는 오버헤드를 없앨 수 있으므로 클라이언트 수준에서 필터링하는 것을 권장합니다. [Sentry SDKs](https://docs.sentry.io/platforms.md)에는 이벤트를 필터링하는 데 도움이 되는 여러 구성 옵션이 있으며, 이 문서에서 설명합니다. 필터링에 사용할 수 있는 이벤트 필드에 대해 자세히 알아보려면 [Event Payloads](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/)를 참조하세요.

## [오류 이벤트 필터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-error-events)

`beforeSend` 콜백 메서드를 사용하고 통합을 구성, 활성화 또는 비활성화하여 SDK가 오류 이벤트를 필터링하도록 설정하세요.

- [`ignoreErrors` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-ignore-errors)

`ignoreErrors` 옵션을 사용하면 특정 패턴과 일치하는 오류를 필터링할 수 있습니다. 이 옵션은 오류 메시지와 매칭할 문자열 및 정규식 목록을 받습니다. 문자열을 사용할 경우 부분 일치도 필터링됩니다. 정확히 일치하는 항목만 필터링해야 한다면 대신 정규식 패턴을 사용하세요.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  ignoreErrors: ["fb_xd_fragment", /^Exact Match Message$/],
});
```

자세한 내용은 [ignoreErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#ignoreErrors)를 참조하세요.

- [`beforeSend` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-before-send)

`beforeSend` 콜백 메서드를 설정해 오류 이벤트를 필터링할 수 있습니다. 이 메서드는 이벤트가 서버로 전송되기 직전에 호출되므로, 데이터를 전송하지 않거나 수정할 수 있는 마지막 기회입니다. `beforeSend`는 이벤트 객체를 매개변수로 받고, 이벤트에 포함된 데이터와 사용자 정의 로직에 따라 이벤트 데이터를 수정하거나 `null`을 반환해 완전히 버릴 수 있습니다. 이 훅은 오류 이벤트와 메시지 이벤트 모두에 대해 호출됩니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSend(event) {
    if (event.user) {
      // Don't send user's email address
      delete event.user.email;
    }
    return event;
  },
});
```

자세한 내용은 [beforeSend](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeSend)를, `hint` 객체에 대한 자세한 내용은 [Using Hints](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints)를 참조하세요.

- [`allowUrls` 및 `denyUrls` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-allowurls-and-denyurls)

특정 도메인의 스크립트에서 발생한 오류를 전송하지 않도록 SDK를 구성할 수 있습니다. 예를 들어 스크립트를 `cdn.example.com`에서 로드하고 사이트가 `example.com`이라면, 다른 도메인에서 발생한 오류를 수집하지 않도록 아래와 같이 `allowUrls`를 설정할 수 있습니다.

```javascript
Sentry.init({
  allowUrls: [/https?:\/\/((cdn|www)\.)?example\.com/],
});
```

이 설정은 오류가 발생한 페이지 URL이 아니라 스택 프레임을 기준으로 오류를 필터링한다는 점에 유의하세요.

특정 URL에서 생성된 오류를 Sentry로 보내지 않으려면 `denyUrls`도 사용할 수 있습니다.

* 자세한 내용은 [allowUrls](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#allowUrls) 참조
* 자세한 내용은 [denyUrls](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#denyUrls) 참조

- [`thirdPartyErrorFilterIntegration` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-thirdpartyerrorfilterintegration)

*버전 8.10.0부터 브라우저 기반 SDK에서 사용 가능*

`thirdPartyErrorFilterIntegration`을 사용하면 브라우저 확장 프로그램, 코드 삽입 브라우저, 또는 Sentry를 함께 사용하는 서드파티 서비스의 위젯처럼 서드파티에서 발생한 오류를 필터링할 수 있습니다. 이 통합은 자체 애플리케이션 코드와 무관한 노이즈를 줄이는 데 매우 유용합니다.

**사전 요구사항**: `thirdPartyErrorFilterIntegration`을 사용하려면 번들러와 [Sentry의 bundler plugins](https://github.com/getsentry/sentry-javascript-bundler-plugins) 중 하나를 사용해야 합니다.

이 통합은 빌드 과정에서 JavaScript 파일에 "application key"를 "표시(mark)"하는 방식으로 동작합니다. 런타임에 오류가 발생하면, 이 통합은 스택 트레이스의 각 스택 프레임에 대해 application key를 확인합니다. 이를 통해 "표시되지 않은" 스택 프레임(즉, 서드파티 코드임을 의미)을 가진 오류를 필터링할 수 있습니다.

이 통합을 설정하고 JavaScript 파일에 application key를 표시하려면, 먼저 Sentry 번들러 플러그인에 `applicationKey` 옵션을 전달하세요. 애플리케이션 코드를 식별하는 임의의 문자열을 사용할 수 있습니다.

`next.config.js`

```javascript
module.exports = withSentryConfig(nextConfig, {
  unstable_sentryWebpackPluginOptions: {

    applicationKey: "your-custom-application-key",

  },
});
```

다음으로 Sentry 초기화에 `thirdPartyErrorFilterIntegration`을 추가하세요.

```javascript
Sentry.init({
  integrations: [

    Sentry.thirdPartyErrorFilterIntegration({
      // Specify the application keys that you specified in the Sentry bundler plugin
      filterKeys: ["your-custom-application-key"],

      // Defines how to handle errors that contain third party stack frames.
      // Possible values are:
      // - 'drop-error-if-contains-third-party-frames'
      // - 'drop-error-if-exclusively-contains-third-party-frames'
      // - 'apply-tag-if-contains-third-party-frames'
      // - 'apply-tag-if-exclusively-contains-third-party-frames'
      behaviour: "drop-error-if-contains-third-party-frames",
    }),

  ],
});
```

`filterKeys` 옵션은 문자열 배열을 받으며, 번들러 플러그인 옵션에서 설정한 `applicationKey` 값과 동일해야 합니다. 웹사이트가 둘 이상의 빌드 프로세스에서 생성된 파일을 호스팅하지 않는다면, 이 배열에는 일반적으로 항목 하나만 포함하면 됩니다.

`behaviour` 옵션은 서드파티 코드의 스택 프레임을 포함한 오류를 어떻게 처리할지 정의합니다. 다음 네 가지 모드 중에서 선택할 수 있습니다.

* `"drop-error-if-contains-third-party-frames"`: 서드파티 스택 프레임이 하나 이상 포함된 오류 이벤트를 드롭합니다.
* `"drop-error-if-exclusively-contains-third-party-frames"`: 서드파티 스택 프레임만 포함된 오류 이벤트를 드롭합니다.
* `"apply-tag-if-contains-third-party-frames"`: 모든 오류 이벤트를 유지하되, 서드파티 스택 프레임이 하나 이상 포함된 경우 `third_party_code: true` 태그를 적용합니다.
* `"apply-tag-if-exclusively-contains-third-party-frames"`: 모든 오류 이벤트를 유지하되, 서드파티 스택 프레임만 포함된 경우 `third_party_code: true` 태그를 적용합니다.

태그만 적용하는 모드를 선택하면, Sentry의 이슈 검색창에서 `third_party_code` 태그를 사용해 이슈 스트림을 필터링할 수 있습니다.

`thirdPartyErrorFilterIntegration`은 [Sentry Loader Script or CDN Bundles](https://docs.sentry.io/platforms/javascript/install/loader.md)에서는 동작하지 않습니다. Sentry Loader Script와 CDN Bundles는 이 통합에서 "third party"로 감지되기 때문입니다. Sentry SDK가 많은 브라우저 네이티브 API를 래핑하므로, 결과적으로 거의 모든 이벤트에 선택한 동작이 적용됩니다.

## [트랜잭션 이벤트 필터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-transaction-events)

특정 트랜잭션이 Sentry로 보고되지 않게 하려면 `tracesSampler` 또는 `beforeSendTransaction` 구성 옵션을 사용하세요. 현재 트랜잭션을 평가하는 함수를 제공할 수 있으며, 원하지 않는 트랜잭션이면 드롭할 수 있습니다.

- [`ignoreTransactions` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-ignore-transactions)

`ignoreTransactions` 옵션을 사용하면 특정 패턴과 일치하는 트랜잭션을 필터링할 수 있습니다. 이 옵션은 트랜잭션 이름과 매칭할 문자열 및 정규식 목록을 받습니다. 문자열을 사용할 경우 부분 일치도 필터링됩니다. 정확히 일치하는 항목만 필터링해야 한다면 대신 정규식 패턴을 사용하세요.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  ignoreTransactions: ["partial/match", /^Exact Transaction Name$/],
});
```

자세한 내용은 [ignoreTransactions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#ignoreTransactions)를 참조하세요.

- [`tracesSampler` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-traces-sampler)

[tracesSampler](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#tracesSampler) 옵션을 사용해 특정 트랜잭션이 Sentry로 보고되지 않도록 할 수도 있습니다.

사용 방법은 [Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/sampling.md#setting-a-sampling-function)을 참조하세요.

- [`beforeSendTransaction` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-beforesendtransaction)

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSendTransaction(event) {
    if (event.transaction === "/unimportant/route") {
      // Don't send the event to Sentry
      return null;
    }
    return event;
  },
});
```

자세한 내용은 [beforeSendTransaction](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeSendTransaction)을, `hint` 객체에 대한 자세한 내용은 [Using Hints](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints)를 참조하세요.

## [스팬 필터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-spans)

스팬을 수정하는 함수를 제공할 수 있는 `beforeSendSpan` 구성 옵션을 사용하세요. 이 함수는 루트 스팬과 모든 자식 스팬에 대해 호출됩니다. 자식 스팬을 포함한 루트 스팬 자체를 드롭하려면 대신 [`beforeSendTransaction`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-beforesendtransaction)을 사용하세요. `beforeSendSpan`으로는 스팬을 드롭할 수 없고, 스팬을 수정하고 그 안의 데이터를 필터링만 할 수 있다는 점에 유의하세요.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSendSpan(span) {
    if (span.description === "should be renamed") {
      span.description = "renamed span";
      span.data = {
        ...span.data,
        myExtraAttribute: true,
      };
    }

    return span;
  },
});
```

자세한 내용은 [beforeSendSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeSendSpan)을 참조하세요.

## [브레드크럼 필터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-breadcrumbs)

`beforeBreadcrumb` 구성 옵션을 사용해 브레드크럼을 필터링할 수 있습니다.

```javascript
Sentry.init({
  // ...
  beforeBreadcrumb(breadcrumb, hint) {
    return breadcrumb.category === "ui.click" ? null : breadcrumb;
  },
});
```

자세한 내용은 [beforeBreadcrumb](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeBreadcrumb)을 참조하세요.

## [Hints 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints)

Hints는 다음 두 위치에서 사용할 수 있습니다.

1. `beforeSend` / `beforeBreadcrumb`
2. `Sentry.addEventProcessor()`를 통해 추가된 이벤트 프로세서

이벤트 및 브레드크럼의 `hints`는 이벤트나 브레드크럼을 구성할 때 사용하는 다양한 정보를 담은 객체입니다. 일반적으로 `hints`에는 원본 예외가 포함되어 추가 데이터를 추출하거나 그룹화 방식에 영향을 줄 수 있습니다.

이벤트의 경우 hints에는 `event_id`, `originalException`, `syntheticException`(더 깔끔한 스택 트레이스를 생성하기 위해 내부적으로 사용), 그리고 사용자가 첨부한 기타 임의의 `data` 같은 속성이 포함됩니다.

브레드크럼의 경우 `hints` 사용 방식은 구현에 따라 달라집니다. XHR 요청에서는 hint에 xhr 객체 자체가 포함되고, 사용자 상호작용에서는 DOM 요소와 이벤트 이름 등이 포함됩니다.

```javascript
Sentry.init({
  // ...
  beforeSend(event, hint) {
    const error = hint.originalException;
    if (
      error &&
      error.message &&
      error.message.match(/database unavailable/i)
    ) {
      event.fingerprint = ["database-unavailable"];
    }
    return event;
  },
});
```

- [이벤트용 Hints](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#hints-for-events)

`originalException`

Sentry SDK가 이벤트를 생성하게 만든 원본 예외입니다. Sentry SDK의 이벤트 그룹화 방식을 변경하거나 추가 정보를 추출할 때 유용합니다.

`syntheticException`

문자열 또는 non-error 객체가 throw되면, Sentry는 기본 스택 트레이스를 얻을 수 있도록 synthetic exception을 생성합니다. 이 예외는 추가 데이터 추출을 위해 여기에 저장됩니다.

- [브레드크럼용 Hints](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#hints-for-breadcrumbs)

`event`

브라우저 이벤트에서 생성된 브레드크럼의 경우, Sentry SDK는 종종 해당 이벤트를 hint로 브레드크럼에 제공합니다. 예를 들어 타깃 DOM 요소에서 데이터를 추출해 브레드크럼에 넣는 데 사용할 수 있습니다.

`level` / `input`

콘솔 로그 가로채기로 생성된 브레드크럼에 사용됩니다. 원본 콘솔 로그 레벨과 로그 함수에 전달된 원본 입력 데이터를 담고 있습니다.

`response` / `input`

HTTP 요청으로 생성된 breadcrumb를 위한 항목입니다. `fetch` 함수의 입력 파라미터와 응답 객체(fetch API에서 가져옴)를 담습니다.

`request` / `response` / `event`

HTTP 요청으로 생성된 breadcrumb를 위한 항목입니다. 요청 및 응답 객체(node HTTP API에서 가져옴)와 node 이벤트(`response` 또는 `error`)를 담습니다.

`xhr`

레거시 `XMLHttpRequest` API를 사용해 수행된 HTTP 요청으로 생성된 breadcrumb를 위한 항목입니다. 원본 `xhr` 객체를 담습니다.

