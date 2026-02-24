---
title: '그룹 내 우선순위 지정'
description: 'BullMQ Pro는 그룹별 우선순위를 지원합니다. 그룹과 우선순위 옵션이 *함께* 제공되면 작업은 해당 그룹 내에서 우선순위가 적용됩니다.'
---

Source URL: https://docs.bullmq.io/bullmq-pro/groups/prioritized

# 그룹 내 우선순위 지정

BullMQ Pro는 그룹별 우선순위를 지원합니다. 그룹과 우선순위 옵션이 *함께* 제공되면 작업은 해당 그룹 내에서 우선순위가 적용됩니다.

```typescript
await myQueue.add(
  'paint',
  { foo: 'bar' },
  {
    group: {
      id: 'groupId',
      priority: 10,
    },
  },
);
```

{% hint style="info" %}
우선순위 범위는 0부터 2097151까지이며, 숫자가 클수록 우선순위는 낮습니다(Unix [processes](https://en.wikipedia.org/wiki/Nice_\(Unix\))와 동일). 따라서 명시적인 우선순위를 지정하지 않은 작업이 가장 높은 우선순위를 가집니다.
{% endhint %}

## 그룹의 우선순위별 개수 가져오기

특정 그룹에서 `prioritized` 상태(우선순위가 0보다 큼) 또는 `waiting` 상태(우선순위 0)에 있는 작업의 `count`를 가져오려면 **`getCountsPerPriorityForGroup`** 메서드를 사용하세요. 예를 들어 `priority` `1`과 `0`의 개수를 가져오려면 다음과 같습니다:

```typescript
const counts = await queue.getCountsPerPriorityForGroup('groupId', [1, 0]);
/*
{
  '1': 11,
  '0': 10
}
*/
```

## 더 읽어보기:

* 💡 [Add Job API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#add)
* 💡 [Get Counts per Priority for Group API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#getcountsperpriorityforgroup)

