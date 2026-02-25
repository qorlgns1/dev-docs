---
title: '마이크로 프런트엔드 | Sentry for Next.js'
description: '마이크로 프런트엔드에서 Sentry JavaScript SDK가 동작하도록 하려면,  패키지를 import하는 모든 마이크로 프런트엔드가 동일한 버전의 Sentry SDK를 사용하고 있는지 확인하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends

# 마이크로 프런트엔드 | Sentry for Next.js

마이크로 프런트엔드에서 Sentry JavaScript SDK가 동작하도록 하려면, `@sentry/*` 패키지를 import하는 모든 마이크로 프런트엔드가 [동일한 버전의 Sentry SDK를 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#sdk-version-alignment)하고 있는지 확인하세요.

앱에서 마이크로 프런트엔드를 사용한다면, 어떤 마이크로 프런트엔드에서 에러가 발생했는지 추적할 수 있어야 매우 유용합니다. 이를 Sentry로 구현하려면 자동 또는 수동 설정을 통해 각 마이크로 프런트엔드를 나타내는 별도의 Sentry 프로젝트로 이벤트를 전송할 수 있습니다. 이렇게 하면 무엇이 어디서 잘못되었는지 더 쉽게 파악할 수 있어, 특히 복잡한 프런트엔드 아키텍처에서 이슈 추적과 해결 속도를 높일 수 있습니다.

아래에서 에러를 서로 다른 Sentry 프로젝트로 라우팅하는 자동 방식과 수동 방식의 설정 방법을 확인할 수 있습니다.

## [Vercel 멀티존 마이크로 프런트엔드](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#vercel-multi-zone-micro-frontends)

Vercel의 멀티존 애플리케이션을 사용하면 큰 앱을 더 작고 독립적으로 관리되는 프로젝트로 분할할 수 있습니다. 각 프로젝트는 자체 UI와 기술 스택을 갖춘 독립 애플리케이션으로 동작합니다. 예를 들어 한 프로젝트에는 Next.js, 다른 프로젝트에는 SvelteKit, 세 번째에는 React를 사용할 수 있습니다.

멀티존 설정에서 Sentry를 구성하려면 각 프로젝트 내부에서 Sentry를 개별적으로 설정하세요. 각 프로젝트가 사용하는 프레임워크의 설치 단계를 따르면 됩니다. 예시는 다음과 같습니다:

* **[Next.js](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)**
* **[React](https://docs.sentry.io/platforms/javascript/guides/react.md)**
* **[SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)**

각 프로젝트마다 서로 다른 DSN을 사용하는 것을 권장합니다. 이렇게 하면 어떤 프로젝트에서 에러가 발생했는지 더 쉽게 식별할 수 있어, 복잡한 프런트엔드 아키텍처에서 이슈 추적과 해결이 빨라집니다.

Vercel 멀티존 마이크로 프런트엔드를 제외하면, 애플리케이션에서 `Sentry.init()`는 한 번만 호출해야 합니다. Sentry를 여러 번 초기화하면 예상치 못한 동작이 발생할 수 있습니다.

## [에러를 자동으로 서로 다른 프로젝트로 라우팅](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#automatically-route-errors-to-different-projects)

`ModuleMetadata`와 `makeMultiplexedTransport`를 함께 사용하면 마이크로 프런트엔드 서비스를 나타내는 특정 Sentry 프로젝트로 이벤트를 자동 라우팅할 수 있습니다. 에러가 발생한 서비스가 식별되면 이벤트가 라우팅되어, 에러가 올바른 프로젝트에 추적되도록 보장합니다.

* `@sentry/webpack-plugin`, `@sentry/rollup-plugin`, `@sentry/vite-plugin`, `@sentry/esbuild-plugin` 중 하나의 버전이 `2.18.0` 이상이어야 합니다.

* SDK 버전 `7.59.0` 이상이 필요합니다.

에러의 출처를 식별하려면 먼저 어떤 번들이 에러에 관련되었는지 식별할 수 있도록 메타데이터를 주입해야 합니다. 이는 `moduleMetadata` 옵션을 활성화하여 Sentry 번들러 플러그인으로 수행할 수 있습니다. 아래 예시는 Webpack 기준이지만, Vite, Rollup, esbuild에서도 지원됩니다.

**아래 코드 스니펫을 마이크로 프런트엔드에 설치하세요:**

```javascript
// webpack.config.js
const { sentryWebpackPlugin } = require("@sentry/webpack-plugin");

module.exports = {
  devtool: "hidden-source-map", // Source map generation must be turned on ("hidden-source-map", "source-map", etc.)
  plugins: [
    sentryWebpackPlugin({
      moduleMetadata: ({ release }) => ({
        dsn: "__MODULE_DSN__",
        release,
      }),
    }),
  ],
};
```

**`__MODULE_DSN__`을 실제 Sentry 프로젝트 DSN으로 바꾸세요.** DSN은 Sentry 프로젝트 설정의 Client Keys (DSN)에서 찾을 수 있습니다.

모듈에 메타데이터가 주입되면 `moduleMetadataIntegration`을 사용해 해당 메타데이터를 조회하고, 파일명이 일치하는 스택 프레임에 연결할 수 있습니다. 이 메타데이터는 이후 `beforeSend` 콜백에서 각 `StackFrame`의 `module_metadata` 속성으로 사용할 수 있습니다. 이를 통해 어떤 번들이 에러 원인일 수 있는지 식별할 수 있습니다. 대상이 결정되면, 라우팅 시 multiplexed transport가 참조할 수 있도록 이를 DSN-release 쌍 목록으로 `event.extra[MULTIPLEXED_TRANSPORT_EXTRA_KEY]`에 저장할 수 있습니다.

**아래 코드 스니펫을 호스트에 설치하세요:**

```javascript
import {
  init,
  makeFetchTransport,
  moduleMetadataIntegration,
  makeMultiplexedTransport,
  MULTIPLEXED_TRANSPORT_EXTRA_KEY,
} from "@sentry/browser";

init({
  dsn: "__DEFAULT_DSN__",
  integrations: [moduleMetadataIntegration()],
  transport: makeMultiplexedTransport(makeFetchTransport),
  beforeSend: (event) => {
    if (event?.exception?.values?.[0].stacktrace.frames) {
      const frames = event.exception.values[0].stacktrace.frames;
      // Find the last frame with module metadata containing a DSN
      const routeTo = frames
        .filter(
          (frame) => frame.module_metadata && frame.module_metadata.dsn,
        )
        .map((v) => v.module_metadata)
        .slice(-1); // using top frame only - you may want to customize this according to your needs

      if (routeTo.length) {
        event.extra = {
          ...event.extra,
          [MULTIPLEXED_TRANSPORT_EXTRA_KEY]: routeTo,
        };
      }
    }

    return event;
  },
});
```

**`__DEFAULT_DSN__`을 실제 Sentry 프로젝트 DSN으로 바꾸세요.** 이것은 기본/fallback Sentry 프로젝트의 DSN이어야 합니다. DSN은 Sentry 프로젝트 설정의 Client Keys (DSN)에서 찾을 수 있습니다.

이 설정이 완료되면 처리된 에러와 처리되지 않은 에러 모두 올바른 프로젝트로 자동 라우팅됩니다.

기본적으로 `args.getEvent`는 에러 이벤트만 반환합니다. 다음과 같이 다른 이벤트 타입도 매칭할 수 있습니다: `args.getEvent(['event', 'transaction', 'replay_event'])`. 이 `getEvent` 스니펫은 에러, 트랜잭션, 리플레이에 대한 매칭을 반환합니다.

## [에러를 수동으로 서로 다른 프로젝트로 라우팅](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#manually-route-errors-to-different-projects)

각 `captureException`의 목적지를 명시적으로 지정할 수 있도록 더 많은 제어가 필요하다면, multiplexed transport API를 사용해 이벤트를 특정 프로젝트로 라우팅할 수 있습니다.

SDK 버전 `7.59.0` 이상이 필요합니다.

- [기본 Matcher 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#using-the-default-matcher)

이벤트를 수동 라우팅하는 가장 간단한 방법은 `MULTIPLEXED_TRANSPORT_EXTRA_KEY`와 함께 기본 matcher를 사용하는 것입니다:

```js
import {
  captureException,
  init,
  makeFetchTransport,
  makeMultiplexedTransport,
  MULTIPLEXED_TRANSPORT_EXTRA_KEY,
} from "@sentry/browser";

init({
  dsn: "__FALLBACK_DSN__",
  transport: makeMultiplexedTransport(makeFetchTransport),
});

// Route a specific error to different projects
captureException(new Error("oh no!"), {
  extra: {
    [MULTIPLEXED_TRANSPORT_EXTRA_KEY]: [
      { dsn: "__CART_DSN__", release: "cart@1.0.0" },
      { dsn: "__GALLERY_DSN__", release: "gallery@1.2.0" },
    ],
  },
});
```

- [커스텀 Matcher 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#using-a-custom-matcher)

더 고급 라우팅 로직이 필요하면 커스텀 matcher 함수를 제공할 수 있습니다. 아래 예시는 `feature` 태그를 사용해 이벤트를 어떤 Sentry 프로젝트로 보낼지 결정합니다. 이벤트에 `feature` 태그가 없으면 `Sentry.init`에 정의된 fallback DSN으로 전송합니다.

```js
import {
  captureException,
  init,
  makeFetchTransport,
  makeMultiplexedTransport,
} from "@sentry/browser";

init({
  dsn: "__FALLBACK_DSN__",
  transport: makeMultiplexedTransport(makeFetchTransport, ({ getEvent }) => {
    const event = getEvent();

    // Send to different DSNs, based on the event payload
    if (event?.tags?.feature === "cart") {
      return [{ dsn: "__CART_DSN__", release: "cart@1.0.0" }];
    } else if (event?.tags?.feature === "gallery") {
      return [{ dsn: "__GALLERY_DSN__", release: "gallery@1.2.0" }];
    } else {
      return [];
    }
  }),
});
```

**플레이스홀더 DSN 값을 실제 Sentry 프로젝트 DSN으로 바꾸세요:**

* `__FALLBACK_DSN__`을 fallback/default Sentry 프로젝트의 DSN으로 교체
* `__CART_DSN__`을 cart 마이크로 프런트엔드의 Sentry 프로젝트 DSN으로 교체
* `__GALLERY_DSN__`을 gallery 마이크로 프런트엔드의 Sentry 프로젝트 DSN으로 교체

각 DSN은 각 Sentry 프로젝트 설정의 Client Keys (DSN)에서 찾을 수 있습니다.

그다음 개별 마이크로 프런트엔드에서 이벤트에 태그/컨텍스트를 설정해 이벤트를 어떤 Sentry 프로젝트로 보낼지 다음과 같이 결정할 수 있습니다:

태그를 설정할 때는 항상 로컬 스코프를 사용하는 것이 중요합니다(아래 예시처럼 하거나<!-- -->

[withScope 문서<!-- -->](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#local-scopes)

사용). 예를 들어 `Sentry.setTag()`를 통해 전역 스코프를 사용하면, 이후의 모든 이벤트가 발생 위치와 관계없이 동일한 DSN으로 라우팅됩니다.

```typescript
captureException(new Error("oh no!"), (scope) => {
  scope.setTag("feature", "cart");
  return scope;
});
```

## [SDK 버전 정렬](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/micro-frontends.md#sdk-version-alignment)

버전 [8.7.0](https://github.com/getsentry/sentry-javascript/releases/tag/8.7.0)부터는 같은 페이지에 여러 Sentry JavaScript SDK가 있더라도, [동일한 버전을 사용하는 경우에만](https://github.com/getsentry/sentry-javascript/pull/12206) 서로 상호작용합니다. 이는 새로 추가되었거나 더 이상 존재하지 않는 SDK API를 호출하거나 접근해서 발생하는 원치 않는 SDK 간 상호작용을 방지합니다. 대표적인 예로, 호스트 앱도 Sentry를 사용하는 상황에서 브라우저 확장 프로그램이나 서드파티 스크립트가 Sentry를 사용하는 경우를 들 수 있습니다.

하지만 마이크로 프런트엔드처럼 여러 마이크로 프런트엔드 또는 하위 애플리케이션 간 SDK 상호작용을 *원하는* 사용 사례에서는, 모든 SDK가 동일한 버전을 사용하도록 보장해야 합니다. 예를 들어 호스트 또는 스켈레톤 애플리케이션에서 SDK를 초기화하고, 마이크로 프런트엔드 하위 애플리케이션에서 `Sentry.captureException` 또는 `Sentry.setTag` 같은 Sentry SDK 호출을 수행한다면, 호스트와 하위 애플리케이션의 SDK 패키지 버전을 동일하게 맞춰야 합니다.

모든 마이크로 프런트엔드의 SDK 버전을 동일하게 맞출 수 없다면, [이 우회 방법](https://github.com/getsentry/sentry-javascript/discussions/10576#discussioncomment-11446422)을 따를 수 있습니다. 다만 상호운용성은 보장되지 않으며 예상치 못한 동작이 발생할 수 있습니다.

