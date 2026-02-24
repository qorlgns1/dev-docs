---
title: 'index'
description: '앞서 언급했듯이, 는 깔끔한 취소를 가능하게 합니다. 현재는 작업이 최종적으로 취소되기 전 최대 처리 시간을 정의하는 TTL 값을 지원합니다:'
---

Source URL: https://docs.bullmq.io/bullmq-pro/observables/cancelation

# 취소

앞서 언급했듯이, `Observables`는 깔끔한 취소를 가능하게 합니다. 현재는 작업이 최종적으로 취소되기 전 최대 처리 시간을 정의하는 TTL 값을 지원합니다:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro(queueName, processor, {
  ttl: 100,
  connection,
});
```

이 매개변수는 작업 이름별로 `ttl` 값을 제공할 수도 있습니다:

```typescript
const worker = new WorkerPro(queueName, processor, {
  ttl: { test1: 100, test2: 200 },
  connection,
});
```

