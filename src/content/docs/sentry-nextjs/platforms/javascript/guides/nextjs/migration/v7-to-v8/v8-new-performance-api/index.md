---
title: '새로운 Tracing API | Sentry for Next.js'
description: 'SDK  릴리스에는 성능 모니터링을 위한 새로운 API가 도입되었습니다. 이 API들은 성능 데이터가 Sentry로 수집되고 보고되는 방식을 더 세밀하게 제어할 수 있도록 설계되었습니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api

# 새로운 Tracing API | Sentry for Next.js

SDK `8.x` 릴리스에는 성능 모니터링을 위한 새로운 API가 도입되었습니다. 이 API들은 성능 데이터가 Sentry로 수집되고 보고되는 방식을 더 세밀하게 제어할 수 있도록 설계되었습니다.

이 API들은 `7.x`에서도 사용할 수 있으므로, `8.x`로 업그레이드하기 전에 새 API로 점진적으로 전환할 수 있습니다.

기존에는 애플리케이션에 수동 성능 계측을 추가하기 위한 핵심 API가 두 가지였습니다:

* `startTransaction()`
* `span.startChild()`

이 API들은 Sentry의 원래 데이터 모델을 기반으로 했습니다. 이 모델은 중첩된 Span 트리를 포함할 수 있는 루트 Transaction을 기준으로 했습니다.

새 모델에서는 개념적으로 트랜잭션이 사라졌습니다. 이제 트리 내 위치와 관계없이 항상 span을 기준으로 작업이 수행됩니다. span은 여전히 Sentry UI에서 트랜잭션으로 그룹화될 수 있다는 점에 유의하세요. 다만 이는 백그라운드에서 처리되며, SDK 관점에서 신경 써야 할 대상은 span뿐입니다.

새 모델에서는 수동으로 시작하거나 종료할 때 트랜잭션과 span을 구분하지 않습니다. 대신, 새 span을 시작할 때 항상 동일한 API를 사용합니다. 그러면 현재 활성 span이 무엇인지에 따라 새 Root Span(부모가 없는 일반 span으로, 개념적으로 트랜잭션과 유사) 또는 Child Span이 자동으로 생성됩니다.

span 시작에 사용할 수 있는 핵심 API는 세 가지입니다:

* `startSpan()`
* `startSpanManual()`
* `startInactiveSpan()`

세 span API 모두 첫 번째 인자로 `StartSpanOptions`를 받으며, 형태는 다음과 같습니다:

```TypeScript
interface StartSpanOptions {
  // The only required field - the name of the span
  name: string;
  attributes?: SpanAttributes;
  op?: string;
  scope?: Scope;
  forceTransaction?: boolean;
}
```

- [`startSpan()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#startspan)

가장 일반적인 API로, 대부분의 상황에서 이 API를 사용해야 합니다. 새 span을 시작하고, 주어진 콜백이 실행되는 동안 이를 활성 span으로 만들며, 콜백이 끝나면 자동으로 종료합니다. 다음처럼 사용할 수 있습니다:

```js
Sentry.startSpan(
  {
    name: "my-span",
    attributes: {
      attr1: "my-attribute",
      attr2: 123,
    },
  },
  (span) => {
    // do something that you want to measure
    // once this is done, the span is automatically ended
  }
);
```

`async` 함수도 전달할 수 있습니다:

```js
Sentry.startSpan(
  {
    name: "my-span",
    attributes: {},
  },
  async (span) => {
    // do something that you want to measure
    await waitOnSomething();
    // once this is done, the span is automatically ended
  }
);
```

`startSpan()`은 생성된 span을 활성 span으로 만들기 때문에, 콜백 내부에서 span을 생성하는 자동/수동 계측은 모두 방금 시작한 span의 자식 span으로 연결됩니다.

콜백 내부에서 오류가 발생하면 span 상태는 자동으로 오류 상태로 설정됩니다.

- [`startSpanManual()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#startspanmanual)

`startSpan()`의 변형으로, 유일한 차이점은 콜백이 끝날 때 span을 자동 종료하지 않는다는 것입니다. 이를 사용할 때는 `span.end()`를 직접 호출해야 합니다:

```js
Sentry.startSpanManual(
  {
    name: "my-span",
  },
  (span) => {
    // do something that you want to measure

    // Now manually end the span ourselves
    span.end();
  }
);
```

대부분의 경우 수동 계측에는 `startSpan()`만으로 충분합니다. 하지만 어떤 이유로든 span 자동 종료가 맞지 않는 경우 `startSpanManual()`을 대신 사용할 수 있습니다.

이 함수는 콜백 실행 동안 생성된 span을 *역시* 활성 span으로 설정하며, 콜백 내부에서 오류가 발생하면 span 상태를 *역시* 오류 상태로 업데이트합니다.

- [`startInactiveSpan()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#startinactivespan)

다른 두 메서드와 달리 이 메서드는 콜백을 받지 않으며, 생성된 span을 활성 span으로 만들지 않습니다. 자식이 필요 없는 독립 span을 만들고 싶을 때 사용할 수 있습니다:

```js
Sentry.startSpan({ name: "outer" }, () => {
  const inner1 = Sentry.startInactiveSpan({ name: "inner1" });
  const inner2 = Sentry.startInactiveSpan({ name: "inner2" });

  // do something

  // manually end the spans
  inner1.end();
  inner2.end();
});
```

비활성 span의 자식 span은 절대 생성되지 않습니다.

- [특정 span의 자식 span 만들기](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#creating-a-child-span-of-a-specific-span)

`withActiveSpan` 헬퍼를 사용하면 특정 span의 자식으로 span을 생성할 수 있습니다:

```js
Sentry.withActiveSpan(parentSpan, () => {
  Sentry.startSpan({ name: "my-span" }, (span) => {
    // span will be a direct child of parentSpan
  });
});
```

- [트랜잭션 만들기](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#creating-a-transaction)

대부분의 경우 span과 트랜잭션 중 무엇을 생성하는지 신경 쓸 필요는 없습니다(`startSpan()`만 호출하면 내부적으로 적절히 처리됩니다). 하지만 여전히 트랜잭션 생성이 *반드시* 필요한 경우가 있을 수 있습니다(예: Sentry UI에서 트랜잭션으로 보여야 하는 경우). 이런 경우 시작 span API에 `forceTransaction: true`를 전달할 수 있습니다. 예:

```js
const transaction = Sentry.startInactiveSpan({
  name: "transaction",
  forceTransaction: true,
});
```

## [Span 스키마](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#the-span-schema)

이전에는 span과 transaction에 사용할 수 있는 속성과 메서드가 많았습니다. 이들 대부분은 더 간결하고 직관적인 API를 위해 제거되었고, OpenTelemetry Span과도 정렬되었습니다. 아래 표에서 기존 항목과 앞으로의 매핑 방식을 확인할 수 있습니다:

`spanToJSON`, `getRootSpan`, `setHttpStatus`, `spanToTraceHeader`, `spanToTraceContext`는 모두 SDK에서 export되어 사용할 수 있습니다.

| Old name                   | Replace with                                                |
| -------------------------- | ----------------------------------------------------------- |
| `span.traceId`             | `span.spanContext().traceId`                                |
| `span.spanId`              | `span.spanContext().spanId`                                 |
| `span.parentSpanId`        | `spanToJSON(span).parent_span_id`                           |
| `span.status`              | `spanToJSON(span).status`                                   |
| `span.sampled`             | `spanIsSampled(span)`                                       |
| `span.startTimestamp`      | `span.startTime` - 참고: 형식이 다릅니다!                   |
| `span.tags`                | attributes를 사용하거나 scope에 태그를 설정                |
| `span.data`                | `spanToJSON(span).data`                                     |
| `span.transaction`         | `getRootSpan(span)`                                         |
| `span.instrumenter`        | 제거됨                                                      |
| `span.finish()`            | `span.end()`                                                |
| `span.end()`               | 동일                                                        |
| `span.setTag()`            | `span.setAttribute()` 또는 scope에 태그 설정                |
| `span.setData()`           | `span.setAttribute()`                                       |
| `span.setStatus()`         | `span.setStatus` - 참고: 시그니처가 다릅니다                |
| `span.setHttpStatus()`     | `setHttpStatus(span, status)`                               |
| `span.setName()`           | `span.updateName()`                                         |
| `span.startChild()`        | `Sentry.startSpan()`을 독립적으로 호출                      |
| `span.isSuccess()`         | `spanToJSON(span).status === 'ok'`                          |
| `span.toTraceparent()`     | `spanToTraceHeader(span)`                                   |
| `span.toContext()`         | 제거됨                                                      |
| `span.updateWithContext()` | 제거됨                                                      |
| `span.getTraceContext()`   | `spanToTraceContext(span)`                                  |

추가로 transaction에는 다음 API가 있습니다:

| Old name                    | Replace with                                     |
| --------------------------- | ------------------------------------------------ |
| `name`                      | `spanToJSON(span).description`                   |
| `trimEnd`                   | 제거됨                                           |
| `parentSampled`             | `spanIsSampled(span)` & `spanContext().isRemote` |
| `metadata`                  | 대신 attributes를 사용하거나 scope에 설정        |
| `setContext()`              | 대신 scope에 context 설정                        |
| `setMeasurement()`          | `Sentry.setMeasurement()`                        |
| `setMetadata()`             | 대신 attributes를 사용하거나 scope에 설정        |
| `getDynamicSamplingContext` | `getDynamicSamplingContextFromSpan(span)`        |

- [Attributes vs. Data vs. Tags vs. Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#attributes-vs-data-vs-tags-vs-context)

이전 모델에는 **Data**, **Tags**, **Context**라는 개념이 있었고, 각기 다른 용도로 사용할 수 있었습니다. 하지만 여기에는 두 가지 주요 단점이 있었습니다. 첫째, 어떤 상황에서 어떤 개념을 써야 하는지 항상 명확하지 않았습니다. 둘째, 이러한 개념이 transaction과 span에서 동일한 방식으로 표시되지 않았습니다.

이 문제를 해결하기 위해 새 모델에서는 span에 설정할 수 있는 **Attributes**만 제공합니다. 대체로 이는 과거의 Data 개념에 대응됩니다.

그래도 태그나 컨텍스트를 *반드시* 설정해야 한다면, span 시작 전에 scope에 설정할 수 있습니다:

```JavaScript
Sentry.withScope((scope) => {
  scope.setTag("my-tag", "tag-value");
  Sentry.startSpan({ name: "my-span" }, (span) => {
    // do something here
    // span will have the tags from the containing scope
  });
});
```

## [기타 주요 변경 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#other-notable-changes)

성능 API의 전반적인 변경 외에도, 이에 따라 적용되는 몇 가지 작은 변경 사항이 있습니다.

- [`tracesSampler()`의 `SamplingContext` 변경](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#changed-samplingcontext-for-tracessampler)

현재 `tracesSampler()`는 인자로 전달된 임의의 `SamplingContext`를 받을 수 있습니다. 이 컨텍스트의 상세 정의는 명확히 문서화되어 있지는 않지만, v8에서 형태가 변경됩니다. 앞으로는 주로 span의 attributes와 span 관련 기타 데이터가 전달됩니다. 기존에 (때때로) 전달되던 일부 속성, 예를 들어 node 기반 SDK의 `req`나 browser tracing의 `location`은 더 이상 전달되지 않습니다.

- [더 이상 `undefined` span 없음](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#no-more-undefined-spans)

v7에서는 tracing이 비활성화되어 있거나 span이 샘플링되지 않은 경우 성능 API `startSpan()` / `startInactiveSpan()` / `startSpanManual()`이 `undefined` span을 받을 수 있었습니다.

v8에서는 OpenTelemetry와 정렬되면서 이 API들이 *항상* span을 반환합니다. 단, 해당 span은 전송되지 않는 Noop-Span일 수 있습니다. 즉, 이제 코드 전반에서 span 존재 여부를 매번 가드할 필요가 없습니다:

```TypeScript
Sentry.startSpan((span: Span | undefined) => {
  // previously, in order to be type safe, you had to use optional chaining or similar
  span?.setAttribute("attr", 1);
});

// In v8, the signature changes to:
Sentry.startSpan((span: Span) => {
  // no need to guard anymore!
  span.setAttribute("attr", 1);
});
```

- [샘플링 결정 강제하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md#forcing-a-sampling-decision)

v7에서는 `startTransaction` 호출 시 `sampled` 옵션을 설정해 샘플링을 강제로 긍정/부정 결정할 수 있었습니다. 이는 해당 트랜잭션에 대해 [sampling configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/sampling.md)을 사실상 덮어썼습니다. v8에서는 OpenTelemetry와 정렬하기 위해 `sampled` 옵션이 제거되었습니다. 대신 `Sentry.init`에서 `tracesSampler` 콜백을 정의하고 특정 span에 대해 `1` 또는 `0`을 반환하여 여전히 결정을 강제할 수 있습니다:

```JavaScript
// v7
Sentry.startTransition({op: 'function.myFunction', sampled: true});

// v8
// 1. define a tracesSampler
Sentry.init({
  tracesSampler: (samplingContext) => {
    // force a positive sampling decision for a specific span
    if (samplingContext.op === 'function.myFunction') {
      return 1;
    }
    // force a negative sampling decision for a specific span
    if (samplingContext.op === 'function.healthCheck') {
      return 0;
    }
    // return 0.1 as a default sample rate for all other spans
    return 0.1;
  }
});

// 2. start the span
Sentry.startSpan({op: 'function.myFunction'}, {/*...*/});
```

