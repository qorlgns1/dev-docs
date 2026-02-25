---
title: 'GraphQL | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql

# GraphQL | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 동작합니다.

*가져오기 이름: `Sentry.graphqlIntegration`*

이 통합은 성능 모니터링이 활성화되어 있을 때 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`graphqlIntegration`은 [`@opentelemetry/instrumentation-graphql`](https://www.npmjs.com/package/@opentelemetry/instrumentation-graphql)을 사용해 span을 수집하도록 `graphql` 라이브러리에 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.graphqlIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#supported-versions)

* `graphql`: `>=14.0.0 <17`

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#options)

- [`ignoreResolveSpans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#ignoreresolvespans)

*Type: `boolean`*

resolver 함수에 대한 span을 생성하지 않도록 할지 여부입니다. 기본값은 `true`입니다.

- [`ignoreTrivialResolveSpans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#ignoretrivialresolvespans)

*Type: `boolean`*

객체 속성에서 기본 resolver를 실행할 때의 span을 생성하지 않도록 할지 여부입니다. 기본값은 `true`입니다.

필드에 대해 스키마에 resolver 함수가 정의되어 있지 않으면, GraphQL은 객체에서 해당 이름의 속성을 찾는 기본 resolver를 사용합니다. 속성이 함수가 아니라면 추적 가치가 크지 않습니다. 이 옵션은 노이즈와 생성되는 span 수를 줄일 수 있습니다.

- [`useOperationNameForRootSpan`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md#useoperationnameforrootspan)

*Type: `boolean`*

기본적으로 이 옵션은 `true`입니다.

이 설정을 활성화하면 GraphQL 계측이 operation 이름을 덧붙여 `http.server` 루트 span 이름을 동적으로 업데이트합니다. `POST /graphql` 같은 일반적인 span 이름 대신 `POST /graphql (query MyQuery)`처럼 더 설명적인 이름이 사용됩니다. 여러 operation이 포함된 요청의 경우 span 이름은 operation 이름을 집계하여, 예를 들어 `POST /graphql (query Query1, query Query2)`와 같이 표시됩니다.

추가 컨텍스트 없이 기본 `http.server` span 이름을 유지하려면 이 옵션을 `false`로 설정하세요.

