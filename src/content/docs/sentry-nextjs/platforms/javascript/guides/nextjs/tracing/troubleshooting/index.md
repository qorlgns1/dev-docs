---
title: '문제 해결 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/troubleshooting'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/troubleshooting

# 문제 해결 | Next.js용 Sentry

트랜잭션 관리에 도움이 필요하면 여기에서 더 자세히 확인할 수 있습니다. 추가 도움이 필요하면 GitHub에서 질문할 수 있습니다. 유료 플랜 고객은 지원팀에 문의할 수도 있습니다.

## [트랜잭션 그룹화](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/troubleshooting.md#group-transactions)

Sentry가 트랜잭션을 수집하면 트랜잭션 이름이 할당됩니다. 이 이름은 일반적으로 사용 중인 프레임워크 통합을 바탕으로 Sentry SDK가 자동 생성합니다. 자동 트랜잭션 생성 기능을 활용할 수 없거나(또는 트랜잭션 이름 생성 방식을 사용자 지정하고 싶은 경우), 설정으로 SDK를 초기화할 때 등록되는 전역 이벤트 프로세서를 사용할 수 있습니다.

예를 들어:

```javascript
// All JavaScript-based SDKs include this function, so it's safe to replace `@sentry/browser`
// with your particular SDK
import { addEventProcessor } from "@sentry/browser";

addEventProcessor((event) => {
  if (event.type === "transaction") {
    event.transaction = sanitizeTransactionName(event.transaction);
  }
  return event;
});
```

`browserTracingIntegration` 통합을 사용하는 브라우저 JavaScript 애플리케이션에서는 `beforeStartSpan` 옵션을 사용해 URL 기준으로 `navigation`/`pageload` 트랜잭션을 더 잘 그룹화할 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  // ...
  integrations: [
    Sentry.browserTracingIntegration({
      beforeStartSpan: (context) => {
        return {
          ...context,
          // You could use your UI's routing library to find the matching
          // route template here. We don't have one right now, so do some basic
          // parameter replacements.
          name: location.pathname
            .replace(/\/[a-f0-9]{32}/g, "/<hash>")
            .replace(/\/\d+/g, "/<digits>"),
        };
      },
    }),
  ],
});
```

## [데이터 잘림 제어](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/troubleshooting.md#control-data-truncation)

현재 모든 태그에는 최대 200자의 문자 제한이 있습니다. 200자 제한을 초과한 태그는 잘려서(truncated) 잠재적으로 중요한 정보를 잃게 됩니다. 이 데이터를 유지하려면 데이터를 여러 태그로 나누어 저장할 수 있습니다.

예를 들어, 다음과 같은 200자 이상의 태그는:

`https://empowerplant.io/api/0/projects/ep/setup_form/?user_id=314159265358979323846264338327&tracking_id=EasyAsABC123OrSimpleAsDoReMi&product_name=PlantToHumanTranslator&product_id=161803398874989484820458683436563811772030917980576`

...다음처럼 잘립니다:

`https://empowerplant.io/api/0/projects/ep/setup_form/?user_id=314159265358979323846264338327&tracking_id=EasyAsABC123OrSimpleAsDoReMi&product_name=PlantToHumanTranslator&product_id=1618033988749894848`

태그를 사용하는 대신, 데이터를 속성으로 스팬에 추가하는 것을 권장합니다. `span.setAttribute()`를 사용하면 길이에 제한 없이 데이터를 스팬에 추가할 수 있습니다. 원하는 만큼 스팬에 속성을 추가할 수 있습니다.

```javascript
const baseUrl = "https://empowerplant.io";
const endpoint = "/api/0/projects/ep/setup_form";
const parameters = {
  user_id: 314159265358979323846264338327,
  tracking_id: "EasyAsABC123OrSimpleAsDoReMi",
  product_name: PlantToHumanTranslator,
  product_id: 161803398874989484820458683436563811772030917980576,
};

startSpan(
  {
    op: "http.client",
    name: "setup form",
    // you can add attributes when starting the span
    attributes: {
      baseUrl,
      endpoint,
    },
  },
  (span) => {
    // or you can add attributes to an existing span
    for (const key of parameters) {
      span.setAttribute(`parameters.${key}`, parameters[key]);
    }

    // do something to be measured
  },
);
```

