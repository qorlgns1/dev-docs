---
title: 'LIFO'
description: '일부 경우에는 작업을 LIFO (*Last-in, First-Out*) 방식으로 처리하는 것이 유용합니다. 이는 큐에 가장 최근에 추가된 작업이 더 오래된 작업보다 먼저 처리된다는 의미입니다.'
---

Source URL: https://docs.bullmq.io/guide/jobs/lifo

# LIFO

일부 경우에는 작업을 LIFO (*Last-in, First-Out*) 방식으로 처리하는 것이 유용합니다. 이는 큐에 가장 최근에 추가된 작업이 더 오래된 작업보다 **먼저** 처리된다는 의미입니다.

```typescript
import { Queue } from 'bullmq';

const myQueue = new Queue('Paint');

// Add a job that will be processed before all others
await myQueue.add('wall', { color: 'pink' }, { lifo: true });
```

