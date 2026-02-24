---
title: '더 알아보기:'
description: '원본 URL: https://docs.bullmq.io/guide/queues/meta'
---

원본 URL: https://docs.bullmq.io/guide/queues/meta

# 메타

모든 큐의 메타데이터는 다음과 같은 방식으로 조회할 수 있습니다:

```typescript
import { Queue } from 'bullmq';

const { concurrency, max, duration, maxLenEvents, paused, version } =
  await queue.getMeta();
```

## 더 알아보기:

* 💡 [Get Meta API 참조](https://api.docs.bullmq.io/classes/v5.Queue.html#getmeta)
* 💡 [전역 동시성](https://docs.bullmq.io/guide/queues/global-concurrency)
* 💡 [전역 속도 제한](https://docs.bullmq.io/guide/queues/global-rate-limit)

