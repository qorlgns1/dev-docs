---
title: '메시지 큐'
description: 'Bull은 영속적인 메시지 큐로도 사용할 수 있습니다. 이는 일부 사용 사례에서 매우 유용한 기능입니다. 예를 들어, 서로 통신해야 하는 두 개의 서버가 있을 수 있습니다. 큐를 사용하면 서버들이 동시에 온라인 상태일 필요가 없으므로, 매우 견고한 통신 채널을 만들 수...'
---

Source URL: https://docs.bullmq.io/bull/patterns/message-queue

# 메시지 큐

Bull은 영속적인 메시지 큐로도 사용할 수 있습니다. 이는 일부 사용 사례에서 매우 유용한 기능입니다. 예를 들어, 서로 통신해야 하는 두 개의 서버가 있을 수 있습니다. 큐를 사용하면 서버들이 동시에 온라인 상태일 필요가 없으므로, 매우 견고한 통신 채널을 만들 수 있습니다. `add`를 *전송*으로, `process`를 *수신*으로 간주할 수 있습니다:

서버 A:

```typescript
const Queue = require('bull');

const sendQueue = new Queue('Server B');
const receiveQueue = new Queue('Server A');

receiveQueue.process(function (job, done) {
  console.log('Received message', job.data.msg);
  done();
});

sendQueue.add({ msg: 'Hello' });
```

서버 B:

```typescript
const Queue = require('bull');

const sendQueue = new Queue('Server A');
const receiveQueue = new Queue('Server B');

receiveQueue.process(function (job, done) {
  console.log('Received message', job.data.msg);
  done();
});

sendQueue.add({ msg: 'World' });
```

