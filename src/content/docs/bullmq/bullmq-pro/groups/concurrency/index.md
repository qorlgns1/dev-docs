---
title: 'index'
description: '기본적으로 각 그룹마다 워커가 병렬로 실행할 수 있는 작업 수에는 제한이 없습니다. rate limit를 사용하더라도 처리 속도만 제한할 뿐, 각 그룹에서 동시에 처리되는 작업 수는 여전히 무제한일 수 있습니다.'
---

Source URL: https://docs.bullmq.io/bullmq-pro/groups/concurrency

# 동시성

기본적으로 각 그룹마다 워커가 병렬로 실행할 수 있는 작업 수에는 제한이 없습니다. rate limit를 사용하더라도 처리 속도만 제한할 뿐, 각 그룹에서 동시에 처리되는 작업 수는 여전히 무제한일 수 있습니다.

그룹별로 동시에 처리되도록 허용되는 작업 수를 제한할 수 있습니다. 예를 들어 최대 동시성 계수를 3으로 설정하면, 워커는 어떤 특정 그룹에 대해서도 동시에 3개를 초과하는 작업을 처리하지 않습니다. 이 제한은 그룹에만 적용되므로, 같은 그룹의 작업만 아니라면 동시 작업 수는 얼마든지 많을 수 있습니다.

동시성 계수는 다음과 같이 설정합니다:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro('myQueue', processFn, {
  group: {
    concurrency: 3, // Limit to max 3 parallel jobs per group
  },
  concurrency: 100,
  connection,
});
```

동시성 계수는 전역으로 적용됩니다. 따라서 위 예시에서는 워커별 동시성 계수나 애플리케이션에서 생성한 워커 수와 관계없이, 어떤 시점에도 그룹당 3개를 초과하는 작업을 처리하지 않습니다.

