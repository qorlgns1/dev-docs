---
title: '정상 종료(Graceful shutdown)'
description: 'BullMQ는 워커의 정상 종료를 지원합니다. 이는 어떤 이유로든 워커를 종료해야 할 때 중단(stalled) 작업을 최소화하는 데 중요합니다. 다만 "비정상 종료(ungraceful shutdown)"가 발생하더라도, BullMQ의 stalled 메커니즘을 통해 새로...'
---

Source URL: https://docs.bullmq.io/guide/workers/graceful-shutdown

# 정상 종료(Graceful shutdown)

BullMQ는 워커의 정상 종료를 지원합니다. 이는 어떤 이유로든 워커를 종료해야 할 때 중단(stalled) 작업을 최소화하는 데 중요합니다. 다만 "비정상 종료(ungraceful shutdown)"가 발생하더라도, BullMQ의 stalled 메커니즘을 통해 새로운 워커가 stalled 작업을 가져와 계속 처리할 수 있습니다.

{% hint style="danger" %}
BullMQ 2.0 이전에는 stalled 작업을 다른 워커가 가져가 처리하려면 시스템에서 [`QueueScheduler`](https://docs.bullmq.io/guide/queuescheduler) 클래스를 실행하고 있어야 합니다.

BullMQ 2.0부터는 `QueueScheduler`가 더 이상 필요하지 않으므로, 위 정보는 구버전에만 해당합니다.
{% endhint %}

종료를 수행하려면 ***`close`*** 메서드를 호출하면 됩니다:

```typescript
await worker.close();
```

위 호출은 워커를 *closing* 상태로 표시하여 새 작업을 가져오지 않게 하고, 동시에 현재 처리 중인 모든 작업이 처리 완료(또는 실패)될 때까지 기다립니다. 이 호출 자체에는 타임아웃이 없으므로, 작업이 적절한 시간 내에 종료되도록 해야 합니다. 어떤 이유로 이 호출이 실패하거나 완료되지 못하면, 대기 중인 작업은 stalled로 표시되고 다른 워커가 처리하게 됩니다( [`QueueScheduler`](https://api.docs.bullmq.io/interfaces/v1.QueueSchedulerOptions.html) 에 올바른 stalled 옵션이 설정된 경우).

