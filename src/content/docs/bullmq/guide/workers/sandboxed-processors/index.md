---
title: '샌드박스 프로세서'
description: '워커를 별도 프로세스에서 실행하도록 정의하는 것도 가능합니다. 이를 *샌드박스* 프로세서라고 부르며, 나머지 코드와 격리되어 실행됩니다.'
---

Source URL: https://docs.bullmq.io/guide/workers/sandboxed-processors

# 샌드박스 프로세서

워커를 별도 프로세스에서 실행하도록 정의하는 것도 가능합니다. 이를 *샌드박스* 프로세서라고 부르며, 나머지 코드와 격리되어 실행됩니다.

워커가 CPU 집약적인 작업을 수행하면 NodeJS 이벤트 루프를 계속 점유하게 되고, 그 결과 BullMQ가 작업 락 연장 같은 잡 관리 작업을 수행하지 못해 결국 "stalled" 잡이 발생할 수 있습니다.

*샌드박스* 워커는 잡 관리 코드와 다른 프로세스에서 프로세서를 실행하므로, 일반 워커보다 stalled 잡이 발생할 가능성이 낮습니다. 이런 문제가 생기지 않도록 동시성 수치를 합리적인 범위로 유지하세요.

샌드박스 프로세서를 사용하려면, 별도 파일에 프로세서를 정의합니다:

```typescript
import { SandboxedJob } from 'bullmq';

module.exports = async (job: SandboxedJob) => {
    // Do something with job
};
```

그리고 해당 경로를 워커 생성자에 전달합니다:

```typescript
import { Worker } from 'bullmq'

const processorFile = path.join(__dirname, 'my_procesor.js');
worker = new Worker(queueName, processorFile);
```

Typescript에서 샌드박스 프로세서를 사용하는 방법에 대한 코드 예제 튜토리얼은 [여기](https://blog.taskforce.sh/using-typescript-with-bullmq/)에서 확인할 수 있습니다.

### URL 지원

프로세서는 URL 인스턴스를 사용해 정의할 수 있습니다:

```typescript
import { pathToFileURL } from 'url';

const processorUrl = pathToFileURL(__dirname + '/my_procesor.js');

worker = new Worker(queueName, processorUrl);
```

{% hint style="warning" %}
Windows OS에 권장됩니다.
{% endhint %}

### Worker Threads

샌드박스 워커를 실행하는 기본 메커니즘은 Node의 spawn process 라이브러리를 사용하는 것입니다. BullMQ v3.13.0부터는 Node의 새로운 Worker Threads 라이브러리를 사용해 워커를 실행할 수도 있습니다. 이 스레드는 이전 방식보다 리소스를 덜 사용하는 것으로 알려져 있지만, 각 스레드마다 Node 런타임을 복제해야 하므로 기대만큼 가볍지는 않습니다.

Worker Threads 지원을 활성화하려면 외부 프로세서 파일을 정의할 때 `useWorkerThreads` 옵션을 사용하세요:

```typescript
import { Worker } from 'bullmq'

const processorFile = path.join(__dirname, 'my_procesor.js');
worker = new Worker(queueName, processorFile, { useWorkerThreads: true });
```

## 더 읽어보기:

* 💡 [Worker API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html)

