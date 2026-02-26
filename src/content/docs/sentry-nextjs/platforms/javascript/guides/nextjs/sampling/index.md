---
title: '샘플링 | Next.js용 Sentry'
description: '앱에 Sentry를 추가하면, 그렇지 않으면 얻기 어려운 오류 및 성능에 대한 매우 가치 있는 정보를 많이 얻을 수 있습니다. 그리고 많은 정보는 적절한 양으로, 올바른 정보일 때 유용합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling

# 샘플링 | Next.js용 Sentry

앱에 Sentry를 추가하면, 그렇지 않으면 얻기 어려운 오류 및 성능에 대한 매우 가치 있는 정보를 많이 얻을 수 있습니다. 그리고 많은 정보는 적절한 양으로, 올바른 정보일 때 유용합니다.

## [오류 이벤트 샘플링](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#sampling-error-events)

오류의 대표 샘플을 Sentry로 전송하려면 SDK 구성에서 `sampleRate` 옵션을 `0`(오류 0% 전송)과 `1`(오류 100% 전송) 사이의 숫자로 설정하세요. 이는 정적 비율이며 모든 오류에 동일하게 적용됩니다. 예를 들어 오류의 25%를 샘플링하려면 다음과 같습니다.

```javascript
Sentry.init({ sampleRate: 0.25 });
```

오류 샘플 비율의 기본값은 `1`이며, 이는 모든 오류가 Sentry로 전송된다는 뜻입니다.

오류 샘플 비율을 변경하려면 재배포가 필요합니다. 또한 SDK 샘플 비율을 설정하면 이벤트 소스에 대한 가시성이 제한됩니다. 프로젝트에 비율 제한(볼륨이 높을 때만 이벤트 드롭)을 설정하는 것이 필요에 더 적합할 수 있습니다.

## [트랜잭션 이벤트 샘플링](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#sampling-transaction-events)

다음 두 가지 이유로 트랜잭션 샘플링을 권장합니다.

1. 단일 trace 수집의 오버헤드는 최소지만, 모든 페이지 로드나 모든 API 요청에 대해 trace를 수집하면 시스템에 원치 않는 부하를 줄 수 있습니다.
2. 샘플링을 활성화하면 Sentry로 전송되는 이벤트 수를 더 잘 관리할 수 있어, 조직의 필요에 맞게 볼륨을 조정할 수 있습니다.

샘플링 비율은 성능과 볼륨 문제, 그리고 데이터 정확성 사이의 균형을 목표로 선택하세요. 데이터를 *너무* 많이 수집하고 싶지는 않지만, 의미 있는 결론을 도출할 만큼 충분한 데이터는 필요합니다. 어떤 비율을 선택해야 할지 확신이 없다면 낮은 값에서 시작해 트래픽 패턴과 볼륨을 파악하면서 점진적으로 늘리세요.

## [트랜잭션 샘플 비율 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#configuring-the-transaction-sample-rate)

Sentry SDK에는 Sentry로 전송되는 트랜잭션 볼륨을 제어하여 대표 샘플을 취할 수 있게 해주는 두 가지 구성 옵션이 있습니다.

1. 균일 샘플 비율 (`tracesSampleRate`):

   * 앱 내 위치나 발생 상황과 관계없이 트랜잭션의 고른 단면을 제공합니다.
   * 기본 [상속](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#inheritance) 및 [우선순위](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#precedence) 동작을 사용합니다.

2. 샘플링 함수 (`tracesSampler`), 다음을 수행합니다:

   * 서로 다른 트랜잭션을 서로 다른 비율로 샘플링
   * 일부 트랜잭션을 완전히 [필터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md)
   * 기본 [우선순위](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#precedence) 및 [상속](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#inheritance) 동작 수정

기본적으로는 이 옵션들이 설정되어 있지 않으므로 어떤 트랜잭션도 Sentry로 전송되지 않습니다. 트랜잭션 전송을 시작하려면 둘 중 하나를 반드시 설정해야 합니다.

- [균일 샘플 비율 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#setting-a-uniform-sample-rate)

이렇게 하려면 `Sentry.init()`에서 `tracesSampleRate` 옵션을 0과 1 사이의 숫자로 설정하세요. 이 옵션을 설정하면 생성되는 모든 트랜잭션은 해당 비율의 확률로 Sentry에 전송됩니다. (예: `tracesSampleRate`를 `0.5`로 설정하면 트랜잭션의 약 50%가 기록되어 전송됩니다.) 예시는 다음과 같습니다.

```javascript
Sentry.init({
  // ...

  tracesSampleRate: 0.5,
});
```

- [샘플링 함수 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#setting-a-sampling-function)

샘플링 함수를 사용하려면 `Sentry.init()`에서 `tracesSampler` 옵션을 함수로 설정하세요. 이 함수는 `samplingContext` 객체를 받아 0과 1 사이의 샘플 비율을 반환해야 합니다. 예를 들면 다음과 같습니다.

```typescript
// The shape of samplingContext that is passed to the tracesSampler function
interface SamplingContext {
  // Name of the span
  name: string;
  // Initial attributes of the span
  attributes: SpanAttributes | undefined;
  // If the parent span was sampled - undefined if there is no incoming trace
  parentSampled: boolean | undefined;
  // Sample rate that is coming from the incoming trace - undefined if there is no incoming trace
  parentSampleRate: number | undefined;
}

Sentry.init({
  // ...

  tracesSampler: ({ name, attributes, inheritOrSampleWith }) => {
    // Do not sample health checks ever
    if (name.includes("healthcheck")) {
      return 0;
    }

    // These are important - take a big sample
    if (name.includes("auth")) {
      return 1;
    }

    // These are less important or happen much more frequently - only take 1%
    if (name.includes("comment")) {
      return 0.01;
    }

    // Otherwise, inherit the sample sampling decision of the incoming trace, or use a fallback sampling rate.
    return inheritOrSampleWith(0.5);
  },
});
```

##### parentSampleRate

`inheritOrSampleWith` 샘플링 컨텍스트 유틸리티는 SDK 버전 9에서 도입되었습니다. 이전 SDK 버전에서 샘플링 결정을 상속하려면 `parentSampled` 샘플링 컨텍스트를 사용하세요.

앞으로는 `parentSampled`보다 `inheritOrSampleWith()` 사용을 강력히 권장합니다. 하위 trace에 대한 결정론적 샘플링과 메트릭 외삽이 가능해지기 때문입니다.

편의를 위해 함수는 불리언을 반환할 수도 있습니다. `true`를 반환하면 `1`을 반환하는 것과 동일하며, 트랜잭션이 Sentry로 전송됨이 보장됩니다. `false`를 반환하면 `0`을 반환하는 것과 동일하며, 트랜잭션이 Sentry로 전송되지 **않음**이 보장됩니다. 분산 추적을 설정한 경우 하위 서비스의 샘플링 결정은 상속된다는 점에 유의하세요.

## [샘플링 컨텍스트 데이터](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#sampling-context-data)

span이 시작되면 `tracesSampler` 함수는 샘플링 결정에 사용할 span `name`과 초기 span `attributes`를 자동으로 받습니다. 추가로 부모 span이 샘플링되었는지를 나타내는 `parentSampled` 불리언도 받습니다. 이 데이터는 span을 샘플링할지 여부를 더 정교하게 판단하는 데 사용할 수 있습니다.

```javascript
Sentry.startSpan({
  name: "Search from navbar",
  op: "search",
  attributes: {
    testGroup: "A3",
    treatmentName: "eager load",
  },
});

// Will result in `tracesSampler` receiving:
function tracesSampler(samplingContext) {
  /*
  samplingContext = {
    name: "Search from navbar",
    attributes: {
      testGroup: 'A3',
      treatmentName: 'eager load',
    },
  }
  */

  // Do not sample this specific span
  return name !== "Search from navbar";
}
```

`tracesSampler`에 전달되는 `name`은 최종적으로 Sentry에 전송되는 이름과 정확히 같지 않을 수 있습니다. 이름은 span 수명 동안 업데이트될 수 있지만, `tracesSampler`에 전달되는 `name`은 항상 초기 이름입니다. 예를 들어 `http.server` span의 `name`은 보통 `tracesSampler`에 전달될 때 아직 파라미터화되지 않으므로, `GET /users/:id` 대신 `GET /users/123` 같은 이름이 보일 수 있습니다.

## [상속](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#inheritance)

트랜잭션의 샘플링 결정이 무엇이든, 그 결정은 자식 span으로 전달되고, 거기에서 다시 다른 서비스에서 이후에 발생하는 모든 트랜잭션으로 전달됩니다.

(이 전파가 어떻게 이뤄지는지는 [분산 추적](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/trace-propagation.md)을 참고하세요.)

현재 생성 중인 트랜잭션이 그러한 이후 트랜잭션 중 하나라면(즉, 부모 트랜잭션이 있다면), 상류(부모) 샘플링 결정이 샘플링 컨텍스트 데이터에 포함됩니다. `tracesSampler`는 이 정보를 사용해 해당 결정을 상속할지 선택할 수 있습니다. 대부분의 경우 분산 trace가 끊어지는 것을 방지하기 위해 상속이 올바른 선택입니다. trace가 끊어지면 모든 서비스가 포함되지 않습니다.

```javascript
tracesSampler: samplingContext => {
  // always inherit
  if (samplingContext.parentSampled !== undefined) {
    return samplingContext.parentSampled
  }

  ...
  // rest of sampling logic here
}
```

`tracesSampler` 대신 `tracesSampleRate`를 사용하는 경우 결정은 항상 상속됩니다.

## [우선순위](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#precedence)

트랜잭션이 샘플링 결정을 갖게 되는 경로는 여러 가지입니다.

* `tracesSampleRate`에 설정된 정적 샘플 비율에 따른 무작위 샘플링
* `tracesSampler`가 반환한 샘플 함수 비율에 따른 무작위 샘플링
* `tracesSampler`가 반환한 절대 결정(100% 또는 0%)
* 트랜잭션에 부모가 있는 경우, 부모의 샘플링 결정 상속
* `startTransaction`에 전달된 절대 결정

이 중 둘 이상이 동시에 적용될 수 있을 때는 다음 우선순위 규칙이 적용됩니다.

1. `tracesSampler`가 정의되어 있으면 그 결정이 사용됩니다. 부모 샘플링 결정을 유지하거나 무시할 수 있고, 샘플링 컨텍스트 데이터를 사용해 자체 결정을 내리거나, 트랜잭션의 샘플 비율을 선택할 수도 있습니다. 부모 샘플링 결정을 재정의하면 분산 trace가 끊어지므로 권장하지 않습니다)
2. `tracesSampler`가 정의되어 있지 않지만 부모 샘플링 결정이 있으면, 부모 샘플링 결정이 사용됩니다.
3. `tracesSampler`가 정의되어 있지 않고 부모 샘플링 결정도 없으면 `tracesSampleRate`가 사용됩니다.

