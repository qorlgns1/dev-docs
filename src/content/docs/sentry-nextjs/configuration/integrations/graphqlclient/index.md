---
title: 'GraphQLClient | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient

# GraphQLClient | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 작동합니다.

*가져오기 이름: `Sentry.graphqlClientIntegration`*

이 통합은 애플리케이션의 GraphQL 요청에서 수집되는 데이터를 강화합니다. 구성한 엔드포인트와 일치하는 HTTP 요청에서 GraphQL 전용 정보를 추출하고, span과 breadcrumb 모두에 GraphQL 작업 세부 정보를 추가합니다.

활성화하면 이 통합은 다음을 수행합니다.

* span 이름을 GraphQL 작업 유형과 이름으로 업데이트
* span에 GraphQL 쿼리 문서 추가
* breadcrumb에 GraphQL 작업 정보 추가

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md#options)

- [`endpoints`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md#endpoints)

*유형: `(string|RegExp)[]`*

GraphQL 엔드포인트로 처리해야 하는 URL 또는 URL 패턴 배열입니다. 이 통합은 이러한 엔드포인트로 가는 요청만 처리합니다. 이 배열에는 문자열, 정규식 또는 둘의 조합이 포함될 수 있습니다.

예시:

```javascript
Sentry.init({
  integrations: [
    Sentry.graphqlClientIntegration({
      endpoints: ["https://graphql-api.example.com", /\/graphql$/],
    }),
  ],
});
```

`graphqlClientIntegration`으로 모든 엔드포인트를 **match all** 하려면, 구성에서 endpoints 옵션을 `[/.*/]`로 설정하면 됩니다. 이 정규식 패턴은 모든 URL과 일치합니다.

