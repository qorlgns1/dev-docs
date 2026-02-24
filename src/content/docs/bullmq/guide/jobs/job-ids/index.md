---
title: 'Job Ids'
description: 'BullMQ의 모든 job은 고유한 job id를 가져야 합니다. 이 id는 Redis에 데이터를 저장하기 위한 키를 구성하는 데 사용되며, job이 수명 주기 동안 가질 수 있는 여러 상태 사이를 이동할 때 해당 job을 가리키는 포인터로도 사용됩니다.'
---

Source URL: https://docs.bullmq.io/guide/jobs/job-ids

# Job Ids

BullMQ의 모든 job은 고유한 job id를 가져야 합니다. 이 id는 Redis에 데이터를 저장하기 위한 키를 구성하는 데 사용되며, job이 수명 주기 동안 가질 수 있는 여러 상태 사이를 이동할 때 해당 job을 가리키는 포인터로도 사용됩니다.

기본적으로 job id는 증가하는 카운터로 자동 생성되지만, *custom id*를 지정할 수도 있습니다.

{% hint style="info" %}
고유성 요구사항은 queue 범위로 제한됩니다. 즉, 서로 다른 queue에서는 동일한 job id를 문제없이 사용할 수 있습니다. 자동 생성되는 id의 카운터도 queue 범위로 제한됩니다.
{% endhint %}

custom id를 지정할 수 있는 가장 큰 이유는 중복 job을 방지하려는 경우입니다. id는 고유해야 하므로, 기존 id로 job을 추가하면 해당 job은 무시되며 queue에 전혀 추가되지 않습니다.

{% hint style="danger" %}
queue에서 제거된 job(수동 제거 또는 `removeOnComplete`/`removeOnFailed` 같은 설정 사용 시)은 **중복으로 간주되지 않습니다**. 즉, 이전 job이 이미 queue에서 제거되었다면 동일한 job id를 여러 번 추가할 수 있습니다.
{% endhint %}

custom job id를 지정하려면 queue에 job을 추가할 때 `jobId` 옵션을 사용하세요.

```typescript
await myQueue.add(
  'wall',
  { color: 'pink' },
  {
    jobId: customJobId,
  },
);
```

{% hint style="danger" %}
custom job id에는 **:** 구분자를 포함하면 안 됩니다. Redis 네이밍 규칙도 따르기 때문에 두 개의 서로 다른 값으로 해석될 수 있습니다. 따라서 구분자가 필요하면 **-**, **\_** 같은 다른 값을 사용하세요.
{% endhint %}

## 더 읽어보기:

* 💡 [Duplicated Event Reference](https://api.docs.bullmq.io/interfaces/v5.QueueEventsListener.html#duplicated)

