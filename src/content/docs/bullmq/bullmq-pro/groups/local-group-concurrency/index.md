---
title: '로컬 그룹 동시성'
description: '특정 그룹에 대해 개별 동시성 값을 설정할 수도 있습니다. 이는 서로 다른 그룹을 서로 다른 동시성 계수로 실행해야 할 때 유용합니다.'
---

Source URL: https://docs.bullmq.io/bullmq-pro/groups/local-group-concurrency

# 로컬 그룹 동시성

특정 그룹에 대해 개별 동시성 값을 설정할 수도 있습니다. 이는 서로 다른 그룹을 서로 다른 동시성 계수로 실행해야 할 때 유용합니다.

그룹의 동시성 계수를 지정하면 이 값이 Redis에 저장된다는 점을 유의하세요. 따라서 더 이상 사용하지 않을 경우 직접 제거해야 합니다.

`setGroupConcurrency` 메서드는 다음과 같이 사용할 수 있습니다:

```typescript
import { QueuePro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = 'my group';
await queue.setGroupConcurrency(groupId, 4);
```

{% hint style="warning" %}
원하는 로컬 동시성과 함께 워커 인스턴스 수준에서도 [Group Concurrency](https://docs.bullmq.io/bullmq-pro/groups/concurrency)를 반드시 설정하세요. 이 기능이 올바르게 동작하려면 필요하며, 로컬 동시성이 정의되지 않은 그룹에는 기본 동시성 값으로도 사용됩니다.
{% endhint %}

그리고 `getGroupConcurrency` 메서드는 다음과 같이 사용할 수 있습니다:

```typescript
const concurrency = await queue.getGroupConcurrency(groupId);
```

## 더 읽어보기:

* 💡 [Set Group Concurrency API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#setgroupconcurrency)
* 💡 [Get Group Concurrency API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupconcurrency)

