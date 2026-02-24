---
title: 'AWS MemoryDB'
description: 'AWS는 사용이 쉽고 BullMQ와 완전히 호환되는 Redis™ 7 호환 관리형 데이터베이스를 제공합니다.'
---

Source URL: https://docs.bullmq.io/guide/redis-tm-hosting/aws-memorydb

# AWS MemoryDB

AWS는 사용이 쉽고 BullMQ와 완전히 호환되는 Redis™ 7 호환 관리형 데이터베이스를 제공합니다.

다만 MemoryDB를 사용할 때는 몇 가지 고려사항이 있습니다.

* MemoryDB는 Cluster 모드에서만 동작합니다. 따라서 큐가 특정 클러스터 노드에 연결되도록 "hash tags"를 사용해야 합니다([여기에서 자세히 보기](https://docs.bullmq.io/bull/patterns/redis-cluster)).
* MemoryDB는 AWS VPC 내부에서만 접근할 수 있으므로, AWS 외부에서는 Redis™ 클러스터에 접근할 수 없습니다.

BullMQ와 함께 MemoryDB를 사용하는 가장 쉬운 방법은 먼저 IORedis Cluster 인스턴스를 생성한 다음, 예를 들어 해당 연결을 워커 또는 큐 인스턴스의 옵션으로 사용하는 것입니다.

```typescript
import { Cluster } from 'ioredis';
import { Worker } from 'bullmq';

const connection = new Cluster(
  [
    {
      host: 'clustercfg.xxx.amazonaws.com',
      port: 6379,
    },
  ],
  {
    tls: {},
  },
);

const worker = new Worker(
  'myqueue',
  async (job: Job) => {
    // Do some usefull stuff
  },
  { connection },
);

// ...

// Do not forget to close the connection as well as the worker when shutting down
await worker.close();
await connection.quit();
```

