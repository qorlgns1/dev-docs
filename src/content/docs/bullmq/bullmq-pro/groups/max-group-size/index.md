---
title: '최대 그룹 크기'
description: '최대 그룹 크기를 설정할 수 있습니다. 이는 작업 수를 일정 한도 내로 유지하고, 새 작업을 버려도 되는 경우에 유용합니다.'
---

Source URL: https://docs.bullmq.io/bullmq-pro/groups/max-group-size

# 최대 그룹 크기

최대 그룹 크기를 설정할 수 있습니다. 이는 작업 수를 일정 한도 내로 유지하고, 새 작업을 버려도 되는 경우에 유용합니다.

그룹이 정의된 최대 크기에 도달하면, 해당 그룹에 새 작업을 추가할 때 예외가 발생합니다. 이 예외는 필요하지 않다면 잡아서 무시할 수 있습니다.

다음과 같이 그룹에 작업을 추가할 때 `maxSize` 옵션을 사용할 수 있습니다:

```typescript
import { QueuePro, GroupMaxSizeExceededError } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = 'my group';
try {
  await queue.add('paint', { foo: 'bar' }, {
      group: {
        id: groupId,
        maxSize: 7,
      },
    });
} catch (err) {
  if (err instanceof GroupMaxSizeExceededError){
    console.log(`Job discarded for group ${groupId}`)
  } else {
    throw err;
  }
}
```

{% hint style="info" %}
`maxSize` 옵션은 아직 `addBulk`에서는 사용할 수 없습니다.
{% endhint %}

