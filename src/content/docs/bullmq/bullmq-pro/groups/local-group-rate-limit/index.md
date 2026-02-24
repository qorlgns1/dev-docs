---
title: '로컬 그룹 rate limit'
description: '때로는 그룹마다 서로 다른 rate limit이 필요합니다. 예를 들어 그룹이 시스템의 특정 사용자를 나타내는 경우, 사용자의 quota나 기타 요인에 따라 해당 그룹에 다른 rate-limit을 적용하고 싶을 수 있습니다.'
---

Source URL: https://docs.bullmq.io/bullmq-pro/groups/local-group-rate-limit

# 로컬 그룹 rate limit

때로는 그룹마다 서로 다른 rate limit이 필요합니다. 예를 들어 그룹이 시스템의 특정 사용자를 나타내는 경우, 사용자의 quota나 기타 요인에 따라 해당 그룹에 다른 rate-limit을 적용하고 싶을 수 있습니다.

로컬 그룹 rate limit을 사용할 수 있으며, 이는 rate-limit이 설정된 특정 그룹에만 적용됩니다. 예를 들면 다음과 같습니다.

```typescript
import { QueuePro, WorkerPro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = 'my group';
const maxJobsPerDuration = 100;

const duration = 1000; // duration in ms.
await queue.setGroupRateLimit(groupId, maxJobsPerDuration, duration);

const worker = new WorkerPro(
  'myQueue',
  async () => {
    // do something
  },
  {
    group: {
      limit: {
        // default rate limit configuration
        max: 1000,
        duration: 1000,
      },
    },
    connection,
  },
);
```

이 코드는 그룹 "my group"에 초당 최대 100개의 job으로 특정 rate limit을 설정합니다. 나머지 그룹에 대해서는 ["default" rate-limit](https://docs.bullmq.io/bullmq-pro/groups/rate-limiting)을 계속 지정할 수 있으며, 따라서 `setGroupRateLimit` 호출을 통해 해당 rate-limit을 재정의할 수 있습니다.

{% hint style="warning" %}
각 Worker 인스턴스에서 group.limit 옵션을 전달해 기본 rate limit을 반드시 지정해야 합니다. 이렇게 해야 worker가 그룹이 rate limited 상태인지 아닌지 확인할 수 있습니다.
{% endhint %}

### 더 읽어보기:

* 💡 [로컬 Rate Limit Group API 레퍼런스](https://api.bullmq.pro/classes/v7.QueuePro.html#setgroupratelimit)

