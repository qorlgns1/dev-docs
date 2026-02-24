---
title: '조회 메서드'
description: '모든 그룹에 작업이 몇 개 있는지 알아야 하는 경우가 자주 있습니다:'
---

Source URL: https://docs.bullmq.io/bullmq-pro/groups/getters

# 조회 메서드

#### 작업 수

모든 그룹에 작업이 몇 개 있는지 알아야 하는 경우가 자주 있습니다:

```typescript
import { QueuePro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = 'my group';
const count = await queue.getGroupsJobsCount(1000); // 1000 groups in each iteration
```

{% hint style="info" %}
이 카운트 값에는 그룹에 포함된 우선순위 작업과 비우선순위 작업이 모두 포함됩니다.
{% endhint %}

또는 특정 그룹의 활성 작업 수를 가져오려는 경우:

```typescript
const activeCount = await queue.getGroupActiveCount(groupId);
```

#### 작업 가져오기

특정 그룹에서 페이지네이션 방식으로 작업을 조회하는 것도 가능합니다. 예를 들어:

```typescript
const jobs = await queue.getGroupJobs(groupId, 0, 100);
```

## 더 읽어보기:

* 💡 [그룹 작업 수 가져오기 API 레퍼런스](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupsjobscount)
* 💡 [그룹 활성 작업 수 가져오기 API 레퍼런스](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupactivecount)
* 💡 [그룹 작업 가져오기 API 레퍼런스](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupjobs)

