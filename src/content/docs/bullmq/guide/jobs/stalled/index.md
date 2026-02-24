---
title: 'Stalled'
description: '{% hint style="danger" %}'
---

Source URL: https://docs.bullmq.io/guide/jobs/stalled

# Stalled

{% hint style="danger" %}
BullMQ 2.0부터는 `QueueScheduler`가 더 이상 필요하지 않습니다. 작업을 수동으로 가져오는 경우 이 [pattern](https://docs.bullmq.io/patterns/manually-fetching-jobs#checking-for-stalled-jobs)을 확인하세요.
{% endhint %}

작업이 active 상태(즉, 워커가 처리 중인 상태)에 있을 때는 워커가 해당 작업을 계속 처리 중임을 알리기 위해 큐를 지속적으로 업데이트해야 합니다. 이 메커니즘은 워커가 크래시되거나 무한 루프에 빠졌을 때 작업이 영구적으로 active 상태에 머무는 것을 방지합니다.

워커가 특정 작업을 아직 처리 중이라는 사실을 큐에 알리지 못하면, 해당 작업은 waiting 목록 또는 failed 세트로 다시 이동됩니다. 이때 작업이 stalled 되었다고 하며, 큐는 'stalled' 이벤트를 발생시킵니다.

{% hint style="info" %}
'stalled' 상태는 없고, 작업이 자동으로 *active* 상태에서 *waiting* 상태로 이동될 때 발생하는 'stalled' 이벤트만 있습니다.
{% endhint %}

작업이 사전 정의된 제한 횟수보다 더 많이 stalled 되면([`maxStalledCount` option](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#maxstalledcount) 참고), 해당 작업은 "*job stalled more than allowable limit*" 오류와 함께 영구적으로 failed 처리됩니다. 기본값은 1이며, stalled 작업은 드물게 발생해야 하지만 필요하면 이 값을 늘릴 수 있습니다.

stalled 작업을 피하려면 워커가 Node.js 이벤트 루프를 과도하게 점유하지 않도록 하세요. 기본 최대 stalled 검사 시간은 30초이므로, 이 값을 초과하는 CPU 작업만 수행하지 않으면 stalled 작업이 발생하지 않아야 합니다.

stalled 작업 가능성을 줄이는 또 다른 방법은 이른바 "sandboxed" 프로세서를 사용하는 것입니다. 이 경우 워커는 메인 프로세스와 분리되어 별도로 실행되는 새로운 Node.js 프로세스를 생성합니다.

{% code title="main.ts" %}

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('Paint', painter);
```

{% endcode %}

{% code title="painter.ts" %}

```typescript
export default = (job) => {
    // Paint something
}
```

{% endcode %}

## 더 읽어보기:

* 💡 [Queue Scheduler API 레퍼런스](https://api.docs.bullmq.io/classes/v1.QueueScheduler.html)

