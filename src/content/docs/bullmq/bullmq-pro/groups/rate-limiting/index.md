---
title: '속도 제한'
description: '원본 URL: https://docs.bullmq.io/bullmq-pro/groups/rate-limiting'
---

원본 URL: https://docs.bullmq.io/bullmq-pro/groups/rate-limiting

# 속도 제한

그룹을 사용할 때 유용한 기능 중 하나는 각 그룹을 서로 독립적으로 속도 제한할 수 있다는 점입니다. 이렇게 하면 여러 그룹에 속한 작업을 고르게 처리하면서도, 시간 단위당 그룹별로 처리 가능한 작업 수를 제한할 수 있습니다.

속도 제한은 다음과 같이 동작합니다. 특정 그룹의 작업 수가 시간 단위당 최대 허용량을 초과하면, 해당 그룹에 속도 제한이 적용됩니다. 이 그룹에 속한 작업은 속도 제한이 만료될 때까지 처리되지 않습니다.

예를 들어, 아래 차트에서는 `"group 2"`에 속도 제한이 적용됩니다:

![속도 제한된 그룹](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-f99cb4797afb865d39a87c94a92595743d1ba93a%2Fimage.png?alt=media)

하나 이상의 그룹이 속도 제한 상태인 동안에도, 속도 제한이 걸리지 않은 다른 그룹의 작업은 정상적으로 소비되며, 해당 그룹들 또한 속도 제한에 걸리기 전까지 계속 처리됩니다.

속도 제한은 워커 인스턴스에서 설정합니다:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro('myQueue', processFn, {
    group: {
      limit: {
        max: 100,  // Limit to 100 jobs per second per group
        duration: 1000,
      }
    },
    connection
});
```

### 수동 레이트 리밋

정적인 옵션 대신 그룹에 수동으로 속도 제한을 적용하는 것이 유용할 때가 있습니다. 예를 들어 API가 `429 Too Many Requests`를 반환할 때, 그 응답을 기준으로 그룹에 속도 제한을 적용하고 싶을 수 있습니다.

이 목적을 위해 `rateLimitGroup` 워커 메서드를 다음과 같이 사용할 수 있습니다:

```typescript
import { WorkerPro } from '@taskforcesh/bullmq-pro';

const worker = new WorkerPro(
  'myQueue',
  async job => {
    const groupId = job.opts.group.id;
    const [isRateLimited, duration] = await doExternalCall(groupId);
    if (isRateLimited) {
      await worker.rateLimitGroup(job, duration);
      // Do not forget to throw this special exception,
      // since the job is no longer active after being rate limited.
      throw Worker.RateLimitError();
    }
  },
  {
    connection,
  },
);
```

### 그룹 레이트 리밋 TTL 가져오기

우리 그룹이 속도 제한 상태인지 확인해야 할 때가 있습니다.

이 목적을 위해 **`getGroupRateLimitTtl`** 메서드를 다음과 같이 사용할 수 있습니다:

```typescript
import { QueuePro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue', { connection });
const groupId = '0';
const maxJobs = 100;

const ttl = await queue.getGroupRateLimitTtl(groupId, maxJobs);

if (ttl > 0) {
  console.log('Group is rate limited');
}
```

## 더 읽어보기:

* 💡 [Rate Limit Group API 레퍼런스](https://api.bullmq.pro/classes/v7.QueuePro.html#ratelimitgroup)
* 💡 [Get Group Rate Limit Ttl API 레퍼런스](https://api.bullmq.pro/classes/v7.QueuePro.html#getgroupratelimitttl)

