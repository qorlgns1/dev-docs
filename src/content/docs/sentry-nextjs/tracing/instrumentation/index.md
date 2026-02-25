---
title: '계측 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation

# 계측 | Next.js용 Sentry

조직의 요구에 맞게 커스터마이즈된 트랜잭션과 스팬을 수집하려면 먼저 [tracing을 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)해야 합니다.

애플리케이션에 커스텀 성능 데이터를 추가하려면 스팬 형태의 커스텀 계측을 추가해야 합니다. 스팬은 특정 작업이 발생하는 데 걸리는 시간을 측정하는 방법입니다. 예를 들어 함수 실행에 걸리는 시간을 측정하는 스팬을 만들 수 있습니다.

모든 tracing API 목록은 [Tracing API](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#tracing) 섹션에서 확인할 수 있습니다.

시작하려면 SDK를 import하세요.

```javascript
import * as Sentry from "@sentry/nextjs";
```

스팬 생성에 사용하는 핵심 함수는 세 가지입니다.

* [startSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-an-active-span-startspan): 활성 상태의 새 스팬을 생성하며 자동으로 종료됩니다. 일반적으로 이 함수를 사용하는 것이 좋습니다.
* [startSpanManual](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-an-active-span-with-manual-end-startspanmanual): 활성 상태의 새 스팬을 생성하며 수동으로 종료해야 합니다.
* [startInactiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-inactive-spans-startinactivespan): 비활성 상태의 새 스팬을 생성하며 수동으로 종료해야 합니다.

## [활성 스팬 vs. 비활성 스팬](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#active-vs-inactive-spans)

새 스팬이 시작되면, 현재 활성 스팬이 있는 경우 자동으로 그 활성 스팬의 자식으로 시작됩니다. 즉, 스팬이 **활성 스팬**으로 시작되면 해당 스팬이 활성인 콜백 내부에서 생성되는 모든 스팬은 그 스팬의 자식이 됩니다. 또한 활성 스팬이 있으면 에러도 현재 활성 스팬에 연결됩니다.

반대로 **비활성 스팬**은 자식이 자동으로 연결되지 않습니다. 자식 활동을 수집할 필요가 없을 때 유용합니다.

활성 스팬의 핵심 제약은 콜백 내부에서만 활성화할 수 있다는 점입니다. 이 제약이 있는 이유는 그렇지 않으면 비동기 코드에서 어떤 스팬이 올바른 부모 스팬인지 연결할 수 없게 되기 때문입니다.

코드를 콜백에서 실행할 수 없는 위치(예: 훅 또는 유사한 구조)에서는 비활성 스팬을 사용해야 하며, [withActiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#withactivespan)과 결합해 자식 스팬을 올바른 부모 스팬에 수동으로 연결할 수 있습니다.

## [브라우저에서의 스팬 계층 구조](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#span-hierarchy-in-the-browser)

브라우저 환경에서는 기본적으로 모든 스팬이 루트 스팬(전체 트레이스를 시작하는 최초 작업)의 직접 자식이 되는 평면 계층으로 수집됩니다. 더 세분화된 계층 구조를 선택할 수는 있지만 트레이드오프가 있습니다.

평면 계층을 유지하는 핵심 이유는 브라우저에서 비동기 경계를 넘어 활성 스팬을 신뢰성 있게 추적할 수 없기 때문입니다. 즉, 여러 비동기 작업이 병렬로 시작되면 어떤 스팬이 어떤 자식 스팬의 부모인지 판단할 수 없습니다. 다음 예시를 보세요.

```javascript
Sentry.startSpan({ name: "span 1" }, async () => {
  await fetch("https://example.com/1");
  await fetch("https://example.com/2");
  await fetch("https://example.com/3");
});

Sentry.startSpan({ name: "span 2" }, async () => {
  await fetch("https://example.com/4");
  await fetch("https://example.com/5");
  await fetch("https://example.com/6");
});
```

브라우저에서는 `span 1`이 자신의 콜백 내부에서만 활성이고, `span 2`는 다른 콜백에서 활성이라는 사실을 알 방법이 없습니다. 그래서 실제로는 *모든* fetch 스팬이 `span 2`의 자식이 됩니다. 이는 오해를 부르고 혼란스럽기 때문에, 브라우저 기본 동작에서는 **모든 스팬이 루트 스팬의 자식이 됩니다**(보통 pageload 또는 navigation 스팬). 즉, 항상 평면 스팬 계층 구조가 됩니다.

이는 수집되는 데이터의 정확성과 신뢰성을 보장하기 위해 선택한 트레이드오프입니다. 더 복잡한 스팬 계층 구조를 수집해야 한다면 `parentSpanIsAlwaysRootSpan: false`를 설정해 이 동작을 비활성화할 수 있습니다.

```javascript
Sentry.init({
  parentSpanIsAlwaysRootSpan: false,
});
```

이렇게 하면 스팬이 현재 활성 스팬의 자식이 되는 전체 계층 동작으로 되돌아갑니다. 다만 여러 비동기 작업이 병렬로 실행되는 경우 잘못된 데이터가 생길 수 있으므로, 이 설정에서는 스팬을 시작하는 병렬 비동기 작업이 없도록 직접 보장해야 합니다.

## [스팬 시작 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#span-starting-options)

다음 옵션은 모든 스팬 시작 함수에서 사용할 수 있습니다.

| 옵션             | 타입                        | 설명                                                                                                            |
| ------------------ | --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `name`             | `string`                    | 스팬 이름입니다.                                                                                                  |
| `op`               | `string`                    | 스팬의 작업(operation)입니다.                                                                                             |
| `startTime`        | `number`                    | 스팬 시작 시간입니다.                                                                                            |
| `attributes`       | `Record<string, Primitive>` | 스팬에 첨부할 속성입니다.                                                                                      |
| `parentSpan`       | `Span`                      | 설정하면 해당 스팬의 자식으로 만듭니다. 그렇지 않으면 현재 활성 스팬의 자식이 됩니다. |
| `onlyIfParent`     | `boolean`                   | true이면 활성 부모 스팬이 없을 때 이 스팬을 무시합니다.                                                            |
| `forceTransaction` | `boolean`                   | true이면 이 스팬이 Sentry UI에서 트랜잭션으로 표시되도록 보장합니다.                                                    |

필수 옵션은 `name`뿐이며, 나머지는 모두 선택 사항입니다.

## [활성 스팬 시작하기 (`startSpan`)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-an-active-span-startspan)

대부분의 시나리오에서는 `Sentry.startSpan()`으로 활성 스팬을 시작하는 것을 권장합니다. 제공한 콜백에서 활성인 새 스팬을 시작하고, 콜백이 끝나면 자동으로 종료됩니다. 콜백은 동기일 수도 비동기(프라미스)일 수도 있습니다. 비동기 콜백의 경우 프라미스가 resolve 또는 reject될 때 스팬이 종료됩니다. 제공한 콜백이 에러를 throw하거나 프라미스를 reject하면 해당 스팬은 실패로 표시됩니다.

동기 작업의 스팬 시작:

```javascript
const result = Sentry.startSpan({ name: "Important Function" }, () => {
  return expensiveFunction();
});
```

비동기 작업의 스팬 시작:

```javascript
const result = await Sentry.startSpan(
  { name: "Important Function" },
  async () => {
    const res = await doSomethingAsync();
    return updateRes(res);
  },
);
```

스팬을 중첩할 수도 있습니다.

```javascript
const result = await Sentry.startSpan(
  {
    name: "Important Function",
  },
  async () => {
    const res = await Sentry.startSpan({ name: "Child Span" }, () => {
      return expensiveAsyncFunction();
    });

    return updateRes(res);
  },
);
```

## [수동 종료를 사용하는 활성 스팬 시작 (`startSpanManual`)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-an-active-span-with-manual-end-startspanmanual)

경우에 따라 콜백이 끝날 때 스팬이 자동 종료되지 않기를 원할 수 있습니다. 이때는 `Sentry.startSpanManual()`을 사용할 수 있습니다. 제공한 콜백에서 활성인 새 스팬을 시작하지만, 콜백이 끝나도 자동으로 종료되지 않습니다. `span.end()`를 호출해 직접 종료해야 합니다.

```javascript
// Start a span that tracks the duration of middleware
function middleware(_req, res, next) {
  return Sentry.startSpanManual({ name: "middleware" }, (span) => {
    res.once("finish", () => {
      span.setHttpStatus(res.status);
      // manually tell the span when to end
      span.end();
    });
    return next();
  });
}
```

## [비활성 스팬 시작하기 (`startInactiveSpan`)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-inactive-spans-startinactivespan)

활성이 아닌 스팬을 추가하려면 독립적인 스팬을 생성할 수 있습니다. 이는 단일 부모 스팬 아래로 묶이지만 현재 활성 스팬과는 독립적인 작업이 있을 때 유용합니다. 다만 대부분의 경우 위의 [startSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-an-active-span-startspan) API를 생성해 사용하는 것이 좋습니다.

```javascript
const span1 = Sentry.startInactiveSpan({ name: "span1" });

someWork();

span1.end();
```

- [비활성 스팬을 활성으로 설정하기(브라우저 전용)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#setting-an-inactive-span-active-browser-only)

사용 가능 버전: `v10.15.0`

브라우저 환경에서는 콜백 기반 스팬 API만으로는 충분하지 않은 사용 사례가 있을 수 있습니다. 이런 경우(아래 예시 참고) `startInactiveSpan`으로 처음에는 비활성 스팬을 시작한 뒤, 스팬을 수동으로 종료할 때까지 활성으로 설정할 수 있습니다.

```javascript
let checkoutSpan;

on("startCheckout", () => {
  checkoutSpan = Sentry.startInactiveSpan({ name: "checkout-flow" });
  Sentry.setActiveSpanInBrowser(checkoutSpan);
});

doSomeWork();

on("endCheckout", () => {
  // Ending the span automatically removes it as the active span
  checkoutSpan.end();
});
```

`startInactiveSpan`과 `setActiveSpanInBrowser`를 함께 사용하면, 비활성 스팬을 생성한 뒤 수동 종료 시점까지 활성으로 만들 수 있습니다. 반면 [`startSpanManual`](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-an-active-span-with-manual-end-startspanmanual)은 원하는 시점에 수동 종료할 수 있지만, 활성 상태는 콜백 내부에서만 유지됩니다.

`setActiveSpanInBrowser`는 브라우저 환경에서만 사용할 수 있다는 점에 유의하세요. 서버에서 코드를 실행하는 경우(예: server-side rendering) 이 호출이 브라우저에서만 실행되도록 반드시 가드해야 합니다.

## [특정 스팬의 자식으로 스팬 시작하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#starting-spans-as-children-of-a-specific-span)

기본적으로 시작되는 모든 스팬은 현재 활성 스팬의 자식이 됩니다. 다른 동작을 원한다면 `parentSpan` 옵션으로 특정 스팬의 자식이 되도록 강제할 수 있습니다.

```javascript
const parentSpan = Sentry.startInactiveSpan({ name: "Parent Span" });
const childSpan = Sentry.startInactiveSpan({
  name: "Child Span",
  parentSpan,
});

childSpan.end();
parentSpan.end();
```

이 옵션은 `startSpan`과 `startSpanManual`에서도 사용할 수 있습니다.

## [스팬 작업을 위한 유틸리티](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#utilities-to-work-with-spans)

커스텀 계측에 도움이 되는 유용한 유틸리티도 제공합니다. 자세한 내용은 [Tracing Utility APIs](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#tracing-utilities)를 확인하세요.

## [분산 트레이싱](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#distributed-tracing)

분산 트레이싱을 수동으로 설정하는 방법은 [Custom Trace Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/trace-propagation/custom-instrumentation.md)을 참고하세요.

## [스팬 데이터 개선](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#improving-span-data)

- [스팬 속성 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#adding-span-attributes)

스팬과 함께 스팬 속성을 수집할 수 있습니다. 스팬 속성의 타입은 `string`, `number`, `boolean` 또는 이 타입들의 (혼합되지 않은) 배열일 수 있습니다. 스팬을 시작할 때 속성을 지정할 수 있습니다.

```javascript
Sentry.startSpan(
  {
    attributes: {
      attr1: "value1",
      attr2: 42,
      attr3: true,
    },
  },
  () => {
    // Do something
  },
);
```

또는 기존 스팬에 속성을 추가할 수도 있습니다.

```javascript
const span = Sentry.getActiveSpan();
if (span) {
  span.setAttribute("attr1", "value1");
  // Or set multiple attributes at once:
  span.setAttributes({
    attr2: 42,
    attr3: true,
  });
}
```

- [모든 스팬에 속성 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#adding-attributes-to-all-spans)

모든 스팬에 속성을 추가하려면 `beforeSendSpan` 콜백을 사용하세요.

```javascript
Sentry.init({
  // dsn, ...
  beforeSendSpan(span) {
    span.data = {
      ...span.data,
      "environment.region": "us-west-2",
    };

    return span;
  },
});
```

- [스팬 작업("op") 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#adding-span-operations-op)

스팬에는 작업(operation)을 연결할 수 있으며, 이를 통해 Sentry가 해당 스팬에 대한 추가 컨텍스트를 식별할 수 있습니다. 예를 들어 데이터베이스 관련 스팬에는 `db` 스팬 작업이 연결됩니다. Sentry 제품은 알려진 작업이 있는 스팬에 대해 추가 제어, 시각화, 필터를 제공합니다.

Sentry는 [잘 알려진 스팬 작업 목록](https://develop.sentry.dev/sdk/performance/span-operations/#list-of-operations)을 유지 관리하며, 스팬에 적용 가능하다면 그중 하나를 사용하는 것을 권장합니다.

```JavaScript
const result = Sentry.startSpan({ name: 'GET /users', op: 'http.client' }, () => {
  return fetchUsers();
})
```

- [Span 이름 업데이트](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#updating-the-span-name)

사용 가능 버전: `v8.47.0`

스팬 이름은 언제든지 업데이트할 수 있습니다:

```javascript
const span = Sentry.getActiveSpan();
if (span) {
  Sentry.updateSpanName(span, "New Name");
}
```

v8.39.0 이전에는 `span.updateName('New Name')`를 사용해야 했으며, 이는 `@sentry/node` 및 이를 기반으로 하는 SDK(예: `@sentry/nextjs`)에서 몇 가지 제한이 있었습니다:

* `http.method` 또는 `http.request.method` 속성이 있는 스팬은 이름이 자동으로 method + URL path로 설정되었습니다.
* `db.system` 속성이 있는 스팬은 이름이 자동으로 system + statement로 설정되었습니다.

`Sentry.updateSpanName()`을 사용하면 이러한 경우에도 이름이 올바르게 업데이트되고 더 이상 덮어쓰이지 않습니다.

브라우저 환경에서 `@sentry/browser`, `@sentry/react` 등을 사용하는 경우 `span.updateName()`과 `Sentry.updateSpanName()`은 동일하게 동작하므로 둘 중 어느 것을 사용해도 됩니다.

- [Span 상태 업데이트](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md#updating-the-span-status)

기본적으로 스팬의 상태는 `unknown`입니다. 스팬이 성공했는지 실패했는지를 나타내기 위해 상태를 수동으로 업데이트할 수 있습니다:

```javascript
// Status codes:
// 0: unknown
// 1: ok
// 2: error
span.setStatus({ code: 2 });
```

또는 더 구체적인 오류 상태를 설정하기 위해 [`Sentry.setHttpStatus()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setHttpStatus) 유틸리티 함수를 사용할 수도 있습니다.

## 이 섹션의 페이지

- [자동 인스트루멘테이션](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md)
- [큐 인스트루먼트](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/queues-module.md)
- [MCP 서버 인스트루먼트](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md)
- [캐시 인스트루먼트](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/caches-module.md)
- [HTTP 요청 인스트루먼트](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/requests-module.md)

