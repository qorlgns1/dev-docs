---
title: '샌드박스 프로세서의 타임아웃'
description: '샌드박스 프로세서를 사용할 때는 모든 작업이 별도의 프로세스에서 실행됩니다. 이로 인해 TTL(time-to-live) 메커니즘을 구현할 수 있으며, 작업이 합리적인 시간 안에 완료되지 못하면 해당 프로세스를 종료할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/patterns/timeout-for-sandboxed-processors

# 샌드박스 프로세서의 타임아웃

샌드박스 프로세서를 사용할 때는 모든 작업이 별도의 프로세스에서 실행됩니다. 이로 인해 TTL(time-to-live) 메커니즘을 구현할 수 있으며, 작업이 합리적인 시간 안에 완료되지 못하면 해당 프로세스를 종료할 수 있습니다.

프로세스를 강제 종료하면 의도치 않은 결과가 발생할 수 있다는 점을 이해하는 것이 중요합니다. 예를 들어 파일에 쓰기 트랜잭션을 수행하는 도중에 종료되면 파일이 손상될 가능성이 큽니다. 하지만 이벤트 루프 내 비동기 호출에 기반한 NodeJS 런타임에서는 이것이 사실상 최선에 가깝습니다. 현재로서는 이 기능을 더 견고하게 구현할 수 있는 알려진 방법이 없습니다.

이 패턴은 가능한 한 안전하게 동작하도록 설계되었지만, 위에서 언급한 트레이드오프를 반드시 염두에 두어야 합니다. 이 패턴은 두 개의 타임아웃을 사용하므로, 프로세스를 하드 킬하기 전에 정리(cleanup) 작업을 수행해 영향을 최소화할 수 있습니다. 물론 정리 작업 자체가 멈추거나 정리 로직이 올바르게 구현되지 않았다면, 여전히 데이터베이스 연결이나 쓰기 작업을 한가운데서 끊게 될 수 있으며, 그에 따른 부정적인 결과가 발생할 수 있습니다.

```typescript
// This processor will timeout in 30 seconds.
const MAX_TTL = 30_000;

// The processor will have a cleanup timeout of 5 seconds.
const CLEANUP_TTL = 5_000;

// We use a custom exit code to mark the TTL, but any would do in practice
// as long as it is < 256 (Due to Unix limitation to 8 bits per exit code)
const TTL_EXIT_CODE = 10;

module.exports = async function (job) {
  let hasCompleted = false;
  const harKillTimeout = setTimeout(() => {
    if (!hasCompleted) {
      process.exit(TTL_EXIT_CODE);
    }
  }, MAX_TTL);

  const softKillTimeout = setTimeout(async () => {
    if (!hasCompleted) {
      await doCleanup(job);
    }
  }, CLEANUP_TTL);

  try {
    // If doAsyncWork is CPU intensive and blocks NodeJS loop forever,
    // the timeout will never be triggered either.
    await doAsyncWork(job);
    hasCompleted = true;
  } finally {
    // Important to clear the timeouts before returning as this process will be reused.
    clearTimeout(harKillTimeout);
    clearTimeout(softKillTimeout);
  }
};

const doAsyncWork = async job => {
  // Simulate a long running operation.
  await new Promise(resolve => setTimeout(resolve, 10000));
};

const doCleanup = async job => {
  // Simulate a cleanup operation.
  await job.updateProgress(50);
};

```

이 패턴에서 고려해야 할 매우 중요한 사항들이 있습니다.

* 프로세서가 NodeJS 이벤트 루프가 실행되지 못하는 무한 루프 때문에 멈춘 경우, TTL 타임아웃 콜백은 절대 호출되지 않습니다.
* `hasCompleted` 플래그를 유지하여, 타임아웃이 트리거되는 정확한 시점에 비동기 작업이 막 완료되는 엣지 케이스를 처리합니다.
* 이 패턴을 사용할 때는 TTL 초과로 작업이 종료될 때 실제로 어디에서 멈추는지 확인할 수 있도록, 전략적인 지점에 디버그 로그를 남기는 것이 매우 유용합니다.

