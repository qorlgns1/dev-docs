---
title: '작업 타임아웃'
description: 'BullMQ는 작업 타임아웃을 위한 특정 메커니즘을 제공하지 않지만, 많은 경우 워커의 process 함수에 커스텀 타임아웃 코드를 넣어 이를 구현할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/patterns/timeout-jobs

# 작업 타임아웃

BullMQ는 작업 타임아웃을 위한 특정 메커니즘을 제공하지 않지만, 많은 경우 워커의 process 함수에 커스텀 타임아웃 코드를 넣어 이를 구현할 수 있습니다.

기본 개념은 작업 처리를 중단시키는 타임아웃 콜백을 설정하고 `UnrecoverableError`를 던지는 것입니다(재시도를 피하기 위해서이며, 이것이 항상 원하는 동작은 아닐 수 있습니다. 그런 경우에는 일반 `Error`를 던지면 됩니다). 작업마다 서로 다른 타임아웃을 적용할 수 있도록 타임아웃을 작업 데이터의 속성으로 지정한 점에 주목하세요. 물론 원한다면 모든 작업에 대해 고정된 상수 타임아웃을 사용할 수도 있습니다.

```typescript
const worker = new Worker('foo', async job => {
  let controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), job.data.timeout);

  try {
    await doSomethingAbortable(controller.signal);
  } catch(err) {
     if (err.name == "AbortError") {
      throw new UnrecoverableError("Timeout");
    } else {
      throw err;
    }
  } finally {
    clearTimeout(timer);
  }
});
```

이 간단한 예제에서는 `doSomethingAbortable`이 abort signal을 처리하고 스스로 정상적으로 중단할 수 있는 비동기 함수라고 가정합니다.

이제 `fetch` 호출에 타임아웃을 적용하려는 또 다른 경우를 보겠습니다. 형태는 다음과 같습니다:

```typescript
const worker = new Worker("foo", async (job) => {
  let controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), job.data.timeout);
  try {
    let response = await fetch("/slowserver.com", {
      signal: controller.signal,
    });
    const result = await response.text();
  } catch (err) {
    if (err.name == "AbortError") {
      throw new UnrecoverableError("Timeout");
    } else {
      throw err;
    }
  } finally {
    clearTimeout(timer)
  }
});
```

이 예제에서는 `fetch` 호출을 중단하기 위해 [AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)를 사용합니다. 이는 `fetch`가 호출 중단을 위해 기본으로 제공하는 메커니즘입니다. abort가 발생하면 `response.text()`에 대한 비동기 호출도 `Abort` 예외를 던지게 됩니다.

요약하면, 작업에 타임아웃을 구현하는 것은 가능하지만 그 방법은 작업이 수행하는 비동기 연산의 종류에 따라 달라질 수 있습니다. 다만 많은 경우 `AbortController`와 `setTimeout`을 함께 사용하는 것만으로도 충분합니다.

