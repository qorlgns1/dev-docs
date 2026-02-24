---
title: 'QueueScheduler'
description: '{% hint style="danger" %}'
---

Source URL: https://docs.bullmq.io/guide/queuescheduler

# QueueScheduler

{% hint style="danger" %}
`QueueScheduler`는 BullMQ 2.0부터 더 이상 사용이 권장되지 않습니다(deprecated). 아래 정보는 이전 버전에만 해당됩니다.
{% endhint %}

`QueueScheduler`는 특정 Queue의 중단(stalled) 및 지연(delayed) 작업을 관리하는 데 사용되는 헬퍼 클래스입니다.

```typescript
import { QueueScheduler } from 'bullmq';

const queueScheduler = new QueueScheduler('test');

// Later, when shuting down gracefully
await queueScheduler.close();
```

이 클래스는 지연된 작업을 처리해야 할 적절한 시점이 되면 자동으로 대기 큐로 다시 이동시킵니다. 또한 중단된 작업도 자동으로 확인합니다(즉, 작업이 active 상태지만 워커가 크래시했거나 정상적으로 동작을 멈춘 경우를 감지). [중단된 작업](https://docs.bullmq.io/guide/jobs/stalled)은 클래스 인스턴스를 생성할 때 선택한 설정에 따라 다시 이동되거나 실패 처리됩니다.

{% hint style="info" %}
지연 작업, backoff를 적용한 재시도, rate limiting 같은 기능이 필요하다면, 해당 queue에 대해 어딘가에서 최소 하나 이상의 `QueueScheduler`가 실행 중이어야 합니다.
{% endhint %}

이 기능이(Bull 3.x처럼) 워커 내부가 아니라 별도 클래스로 분리된 이유는, 병렬 처리를 위해 많은 수의 워커를 두고 싶을 수 있는 반면 스케줄러는 지연 또는 중단 검사에 필요한 queue마다 보통 1~2개 인스턴스만 두는 편이 적절하기 때문입니다. 하나면 충분하지만, 이중화를 위해 더 둘 수도 있습니다.

{% hint style="warning" %}
원하는 만큼 `QueueScheduler` 인스턴스를 두어도 괜찮습니다. 다만 각 인스턴스가 일부 bookkeeping 작업을 수행하므로 Redis 인스턴스에서 눈에 띄는 CPU 및 IO 사용량이 발생할 수 있다는 점을 유의하세요.
{% endhint %}

## 더 읽어보기:

* 💡 [Queue Scheduler API 레퍼런스](https://api.docs.bullmq.io/classes/v1.QueueScheduler.html)

