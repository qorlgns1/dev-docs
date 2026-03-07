---
title: "파일 병렬성"
description: "기본적으로 Vitest는 *test files*를 병렬로 실행합니다. 지정한 에 따라 Vitest는 test files를 병렬화하기 위해 서로 다른 메커니즘을 사용합니다."
---

출처 URL: https://vitest.dev/guide/parallelism

# 병렬성

## 파일 병렬성

기본적으로 Vitest는 *test files*를 병렬로 실행합니다. 지정한 `pool`에 따라 Vitest는 test files를 병렬화하기 위해 서로 다른 메커니즘을 사용합니다.

- `forks`(기본값)와 `vmForks`는 서로 다른 [child processes](https://nodejs.org/api/child_process.html)에서 테스트를 실행합니다.
- `threads`와 `vmThreads`는 서로 다른 [worker threads](https://nodejs.org/api/worker_threads.html)에서 테스트를 실행합니다.

"child processes"와 "worker threads"는 모두 "workers"라고 부릅니다. [`maxWorkers`](https://vitest.dev/config/#maxworkers) 옵션으로 실행 중인 worker 수를 구성할 수 있습니다.

테스트가 많다면 일반적으로 병렬 실행이 더 빠르지만, 프로젝트, 환경, 그리고 [isolation](https://vitest.dev/config/#isolate) 상태에 따라 달라질 수 있습니다. 파일 병렬화를 비활성화하려면 [`fileParallelism`](https://vitest.dev/config/#fileparallelism)을 `false`로 설정하면 됩니다. 가능한 성능 개선 방법을 더 알아보려면 [Performance Guide](https://vitest.dev/guide/improving-performance)를 읽어보세요.

## 테스트 병렬성

*test files*와 달리, Vitest는 *tests*를 순차적으로 실행합니다. 즉, 하나의 test file 내부 테스트는 정의된 순서대로 실행됩니다.

Vitest는 테스트를 함께 실행하기 위한 [`concurrent`](https://vitest.dev/api/#test-concurrent) 옵션을 지원합니다. 이 옵션이 설정되면 Vitest는 같은 _file_ 안의 concurrent 테스트를 그룹화하고(동시에 실행되는 테스트 수는 [`maxConcurrency`](https://vitest.dev/config/#maxconcurrency) 옵션에 따라 달라짐), [`Promise.all`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)로 실행합니다.

Vitest는 어떤 스마트 분석도 수행하지 않으며, 이러한 테스트를 실행하기 위해 추가 worker를 만들지도 않습니다. 즉, 비동기 작업에 크게 의존하는 경우에만 테스트 성능이 향상됩니다. 예를 들어, 아래 테스트는 `concurrent` 옵션이 지정되어 있어도 여전히 하나씩 순서대로 실행됩니다. 동기식이기 때문입니다.

```ts
test.concurrent("the first test", () => {
  expect(1).toBe(1);
});

test.concurrent("the second test", () => {
  expect(2).toBe(2);
});
```

모든 테스트를 동시에 실행하고 싶다면 [`sequence.concurrent`](https://vitest.dev/config/#sequence-concurrent) 옵션을 `true`로 설정할 수 있습니다.
