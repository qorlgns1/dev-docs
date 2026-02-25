---
title: '트리 셰이킹 | Next.js용 Sentry'
description: 'Sentry Next.js SDK는 몇 가지 추가 구성과 함께 webpack 빌드에 대한 트리 셰이킹을 지원합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking

# 트리 셰이킹 | Next.js용 Sentry

Sentry Next.js SDK는 몇 가지 추가 구성과 함께 webpack 빌드에 대한 [트리 셰이킹](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking)을 지원합니다.

Sentry SDK의 번들 크기를 최소화하려면, 이 페이지를 읽고 표시된 트리 셰이킹 구성을 적용하는 것을 권장합니다.

이 가이드는 Next.js 애플리케이션을 webpack으로 빌드하는 경우에만 관련이 있습니다. 현재 Turbopack 빌드에서는 트리 셰이킹 옵션이 지원되지 않습니다.

## [트리 셰이킹 가능한 선택적 코드](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#tree-shaking-optional-code)

Sentry Next.js SDK에는 디버그 로깅 및 트레이싱 기능처럼 기본 오류 수집에 반드시 필요하지는 않은 코드가 포함되어 있습니다. 디버그 코드는 개발 중에는 유용하지만, 프로덕션 번들에는 불필요한 크기 증가를 유발합니다. Next.js SDK는 `withSentryConfig` 함수를 통해 트리 셰이킹 옵션을 제공하므로 webpack 빌드 과정에서 이러한 선택적 코드를 제거할 수 있습니다.

가져오거나 사용하지 않는 모든 것은 webpack에 의해 트리 셰이킹될 수 있습니다. 즉, Session Replay, Browser Tracing, Browser Profiling 같은 선택적 통합과 사용하지 않는 유틸리티 메서드는 가져와서 사용하지 않는 한 번들에 포함되지 않습니다. 이 페이지의 나머지 부분에서는 내부 SDK 코드를 트리 셰이킹하는 방법을 다루며, 이는 특정 Sentry 기능을 사용할 때만 필요합니다.

## [트리 셰이킹 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#tree-shaking-options)

Next.js 프로젝트에서 Sentry 디버그 코드를 트리 셰이킹하려면, 다음 예시처럼 빌드 구성에서 `webpack.treeshake` 옵션을 사용하세요.

`next.config.(js|mjs)`

```javascript
const nextConfig = {
  // your next.js config
};

withSentryConfig(nextConfig, {
  webpack: {
    treeshake: {
      // Tree shaking options...
      removeDebugLogging: false,
      removeTracing: false,
      excludeReplayIframe: false,
      excludeReplayShadowDOM: false,
      excludeReplayCompressionWorker: false,
    },
  },
});
```

Next.js의 사용자 지정 webpack 구성에 대한 자세한 내용은 Next.js 문서의 [Custom Webpack Config](https://nextjs.org/docs/api-reference/next.config.js/custom-webpack-config)를 참고하세요.

다음 섹션에서는 사용 가능한 각 트리 셰이킹 옵션과 구성 방법을 설명합니다.

- [webpack.treeshake.removeDebugLogging](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.removeDebugLogging)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

이 옵션을 true로 설정하면 Sentry SDK의 모든 디버그 로깅 코드(SDK 구성에서 `debug: true`를 설정했을 때 나타나는 console 로그)가 제거됩니다. 이는 Sentry의 Logs 제품(`enableLogs` 옵션으로 제어됨)이나 앱의 로깅에는 영향을 주지 않습니다.

- [webpack.treeshake.removeTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.removeTracing)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

이 옵션을 `true`로 설정하면 트레이싱 및 성능 모니터링과 관련된 모든 코드가 제거됩니다.

이 옵션이 활성화된 경우 트레이싱 관련 SDK 기능(예: `Sentry.startSpan()`)을 사용하면 안 됩니다. 또한 `browserTracingIntegration`을 추가하지 않았다면 이 옵션은 아무런 효과가 없습니다.

- [webpack.treeshake.excludeReplayIframe](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.excludeReplayIframe)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

이 옵션을 `true`로 설정하면 [Session Replays](https://docs.sentry.io/platforms/javascript/session-replay.md) 중 iframe 콘텐츠 캡처와 관련된 모든 SDK 코드가 제거됩니다. 이는 `replayIntegration`을 활성화한 경우에만 적용됩니다.

- [webpack.treeshake.excludeReplayShadowDOM](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.excludeReplayShadowDOM)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

이 옵션을 `true`로 설정하면 [Session Replays](https://docs.sentry.io/platforms/javascript/session-replay.md) 중 shadow DOM 요소 캡처와 관련된 모든 SDK 코드가 제거됩니다. 이는 `replayIntegration`을 활성화한 경우에만 적용됩니다.

- [webpack.treeshake.excludeReplayCompressionWorker](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#webpack.treeshake.excludeReplayCompressionWorker)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

이 옵션을 `true`로 설정하면 [Session Replay](https://docs.sentry.io/platforms/javascript/session-replay.md)를 위해 포함된 압축 웹 워커와 관련된 모든 SDK 코드가 제거됩니다. 압축 워커를 직접 호스팅하려는 경우 이 옵션을 활성화하세요. 자세한 내용은 [Using a Custom Compression Worker](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md#using-a-custom-compression-worker)를 참고하세요. 이는 `replayIntegration`을 활성화한 경우에만 적용됩니다.

**커스텀 워커 URL을 제공하지 않는 한 이 옵션을 활성화하는 것은 권장하지 않습니다**.

사용 가능한 트리 셰이킹 옵션과, 다양한 번들러에서 이를 수동으로 설정하는 방법을 더 알아보려면 JavaScript SDK의 [트리 셰이킹 문서](https://docs.sentry.io/platforms/javascript/guides/react/configuration/tree-shaking.md#tree-shaking-with-webpack)를 참고하세요.

