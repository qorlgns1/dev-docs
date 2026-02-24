---
title: '작업 제거하기'
description: '때로는 작업을 제거해야 할 필요가 있습니다. 예를 들어, 잘못된 데이터를 가진 작업이 있을 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/jobs/removing-job

# 작업 제거하기

때로는 작업을 제거해야 할 필요가 있습니다. 예를 들어, 잘못된 데이터를 가진 작업이 있을 수 있습니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

const job = await queue.add('wall', { color: 1 });

await job.remove();
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue

queue = Queue('paint')

job = await queue.add('wall', {'color': 1})

await job.remove()
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
잠긴 작업(활성 상태)은 제거할 수 없습니다. 오류가 발생합니다.
{% endhint %}

## 부모 작업이 있는 경우

가능한 경우는 2가지입니다.

1. 대기 중인 의존성이 없는 경우: 부모는 wait 상태로 이동하며, 이 작업을 처리하려고 시도할 수 있습니다.
2. 대기 중인 의존성이 있는 경우: 부모는 waiting-children 상태로 유지됩니다.

{% hint style="info" %}
이 자식 작업이 제거되는 시점에 **completed** 상태라면, 처리된 값은 부모의 processed `hset`에 그대로 유지된다는 점을 고려하세요.
{% endhint %}

## 대기 중인 의존성이 있는 경우

먼저 해당 작업의 모든 대기 중인 하위 작업을 제거하려고 시도할 수 있습니다.

{% hint style="warning" %}
자식 작업 중 하나라도 잠겨 있으면 삭제 프로세스가 중단됩니다.
{% endhint %}

### 더 읽어보기:

* 💡 [Remove API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#remove)

