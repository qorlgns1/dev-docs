---
title: '작업 데이터 반환'
description: '워커가 처리를 완료했을 때, 경우에 따라 일부 데이터를 반환하는 것이 편리합니다. 이렇게 반환된 데이터는 예를 들어  이벤트를 수신해 접근할 수 있습니다. 이 반환 데이터는 작업의  속성에서 확인할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/returning-job-data

# 작업 데이터 반환

워커가 처리를 완료했을 때, 경우에 따라 일부 데이터를 반환하는 것이 편리합니다. 이렇게 반환된 데이터는 예를 들어 `completed` 이벤트를 수신해 접근할 수 있습니다. 이 반환 데이터는 작업의 `returnvalue` 속성에서 확인할 수 있습니다.

간단한 비동기 처리를 수행하는 워커를 상상해 봅시다:

```typescript
import { Queue, Worker } from 'bullmq';

const myWorker = new Worker('AsyncProc', async job => {
  const result = await doSomeAsyncProcessing();
  return result;
});
```

{% hint style="info" %}
참고로, 위 예제에서는 `doSomeAsyncProcessing`의 결과를 바로 반환해도 됩니다. 여기서는 예제를 더 명확하게 보여주기 위해 임시 변수를 사용했습니다.
{% endhint %}

이제 결과 값을 얻기 위해 completed 이벤트를 수신할 수 있습니다:

```typescript
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('AsyncProc');

queueEvents.on('completed', ({ returnvalue }) => {
  console.log(returnvalue);
});
```

처리 함수의 결과를 저장하려면, 완료 이벤트에서 처리하는 것보다 프로세스 함수 자체에서 저장하는 방식이 훨씬 더 견고합니다. 이렇게 하면 작업이 완료되었을 때 반환 값도 함께 저장된다는 것이 보장됩니다. 반면 completed 이벤트에서 데이터를 저장하는 방식은 실패할 수 있고, 그 경우에도 오류를 감지하지 못한 채 작업은 완료될 수 있습니다.

## "results" 큐 사용

작업 결과를 안정적으로 전달하기 위한 또 다른 일반적인 방법은 결과를 보내는 전용 "results" 큐를 두는 것입니다. 이 "results" 큐의 워커는 데이터를 데이터베이스에 저장하는 등의 작업을 신뢰성 있게 수행할 수 있습니다. 이 접근 방식은 큐를 통해 서비스 간 데이터를 주고받는 견고한 마이크로서비스 아키텍처를 설계할 때 유용합니다. 결과 큐가 데이터를 받는 시점에 결과를 처리하는 서비스가 내려가 있더라도, 서비스가 다시 온라인 상태가 되면 결과는 여전히 처리됩니다.

