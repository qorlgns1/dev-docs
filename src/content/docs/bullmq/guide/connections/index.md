---
title: 'maxRetriesPerRequest'
description: '원본 URL: https://docs.bullmq.io/guide/connections'
---

원본 URL: https://docs.bullmq.io/guide/connections

# 연결

Queue로 작업을 시작하려면 Redis 인스턴스에 대한 연결이 필요합니다. BullMQ는 node 모듈 [ioredis](https://github.com/luin/ioredis)를 사용하며, BullMQ에 전달하는 옵션은 그대로 ioredis의 생성자에 전달됩니다. 아무 옵션도 제공하지 않으면 기본값으로 포트 6379와 localhost가 사용됩니다.

모든 클래스는 최소 하나의 Redis 연결을 사용하지만, 일부 상황에서는 연결을 재사용할 수도 있습니다. 예를 들어 *Queue*와 *Worker* 클래스는 기존 ioredis 인스턴스를 받아 해당 연결을 재사용할 수 있습니다. 하지만 *QueueScheduler*와 *QueueEvents*는 Redis에 대한 블로킹 연결이 필요하므로 재사용할 수 없습니다.

예시:

```typescript
import { Queue, Worker } from 'bullmq';

// Create a new connection in every instance
const myQueue = new Queue('myqueue', {
  connection: {
    host: 'myredis.taskforce.run',
    port: 32856,
  },
});

const myWorker = new Worker('myqueue', async job => {}, {
  connection: {
    host: 'myredis.taskforce.run',
    port: 32856,
  },
});
```

```typescript
import { Queue } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis();

// Reuse the ioredis instance in 2 different producers
const myFirstQueue = new Queue('myFirstQueue', { connection });
const mySecondQueue = new Queue('mySecondQueue', { connection });
```

```typescript
import { Worker } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis({ maxRetriesPerRequest: null });

// Reuse the ioredis instance in 2 different consumers
const myFirstWorker = new Worker('myFirstWorker', async job => {}, {
  connection,
});
const mySecondWorker = new Worker('mySecondWorker', async job => {}, {
  connection,
});
```

세 번째 예시에서는 ioredis 인스턴스를 재사용하더라도, worker는 블로킹 연결을 처리하기 위해 내부적으로 필요한 중복 연결을 하나 더 생성한다는 점에 유의하세요. `IORedis` 인스턴스를 올바르게 생성하는 방법은 [ioredis](https://github.com/luin/ioredis/blob/master/API.md) 문서를 참고하세요.

#### `maxRetriesPerRequest`

이 설정은 ioredis 클라이언트에서 명령이 실패했을 때 오류를 던지기 전에 몇 번 재시도할지를 지정합니다. 따라서 Redis에 연결할 수 없거나 오프라인 상태여도, 상황이 바뀌거나 최대 시도 횟수에 도달할 때까지 명령을 재시도합니다.

이렇게 하면 정상 동작하는 연결이 있는 한 worker가 계속 처리하도록 보장할 수 있습니다. Redis 클라이언트를 수동으로 생성하는 경우, worker 인스턴스에 전달될 때 이 설정이 null로 되어 있지 않으면 BullMQ는 예외를 발생시킵니다.

### Queue

또한 작업 추가, 일시 중지, getter 사용 등 큐 관리를 위해 사용하는 단순 Queue 인스턴스는 보통 worker와 요구사항이 다르다는 점도 유의하세요.

예를 들어 HTTP 엔드포인트 호출 결과로 큐에 작업을 추가하는 producer 서비스를 생각해 봅시다. 이 엔드포인트의 호출자는 호출 시점에 Redis 연결이 다운되어 있더라도 무한정 기다릴 수 없습니다. 따라서 `maxRetriesPerRequest` 설정은 기본값(현재 20)으로 두거나, 사용자에게 빠르게 오류를 반환해 나중에 재시도할 수 있도록 1 같은 다른 값으로 설정하는 것이 좋습니다.

반면 Worker processor 내부에서 작업을 추가하는 경우, 이 프로세스는 백그라운드에서 동작하는 consumer 서비스로 예상됩니다. 이 경우에는 동일한 연결을 공유할 수 있습니다.

자세한 내용은 [persistent connections](https://docs.bullmq.io/bull/patterns/persistent-connections) 페이지를 참고하세요.

{% hint style="danger" %}
ioredis 연결을 사용할 때는 [ioredis](https://redis.github.io/ioredis/interfaces/CommonRedisOptions.html#keyPrefix)의 "keyPrefix" 옵션을 사용하지 않도록 주의하세요. 이 옵션은 BullMQ와 호환되지 않으며, BullMQ는 [prefix](https://api.docs.bullmq.io/interfaces/v5.QueueOptions.html#prefix) 옵션을 통해 자체 키 프리픽싱 메커니즘을 제공합니다.
{% endhint %}

연결을 많이 사용할 수 있다면 그대로 사용하는 것이 좋습니다. Redis 연결의 오버헤드는 매우 낮기 때문에, 서비스 제공자가 강한 제한을 두지 않는 한 연결 재사용을 크게 신경 쓸 필요는 없습니다.

{% hint style="danger" %}
BullMQ에서 예상치 못한 오류를 유발할 수 있는 키 자동 삭제를 피하려면 Redis 인스턴스에 아래 설정이 있는지 확인하세요.

`maxmemory-policy=noeviction`
{% endhint %}

