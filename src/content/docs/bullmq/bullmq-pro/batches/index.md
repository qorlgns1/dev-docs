---
title: '새로운 배치 옵션: minSize 및 timeout'
description: '워커를 설정하여 한 번에 하나의 작업만 처리하는 대신, 한 번에 여러 작업(소위 *batch*)을 최대 지정 개수까지 처리할 수 있습니다. 배치를 사용하는 워커는 일반 워커와 의미 체계와 동작 방식이 약간 다르므로, 함정을 피하려면 아래 예제를 주의 깊게 읽어야 합니다...'
---

Source URL: https://docs.bullmq.io/bullmq-pro/batches

# 배치

워커를 설정하여 한 번에 하나의 작업만 처리하는 대신, 한 번에 여러 작업(소위 *batch*)을 최대 지정 개수까지 처리할 수 있습니다. 배치를 사용하는 워커는 일반 워커와 의미 체계와 동작 방식이 약간 다르므로, 함정을 피하려면 아래 예제를 주의 깊게 읽어야 합니다.

배치를 활성화하려면, 배치당 최대 작업 수를 나타내는 `size` 속성을 포함한 `batch` 옵션을 전달하세요.

```typescript
const worker = new WorkerPro(
  'My Queue',
  async (job: JobPro) => {
    const batch = job.getBatch();

    for (let i = 0; i < batch.length; i++) {
      const batchedJob = batch[i];
      await doSomethingWithBatchedJob(batchedJob);
    }
  },
  { connection, batch: { size: 10 } },
);
```

{% hint style="info" %}
배치 크기에 대한 엄격한 최대 제한은 없습니다. 다만 배치가 커질수록 크기에 비례한 오버헤드가 생기며, 이는 성능 문제로 이어질 수 있다는 점을 유의하세요. 일반적인 배치 크기는 10~50개 작업 범위입니다.
{% endhint %}

### 새로운 배치 옵션: `minSize` 및 `timeout`

`size` 옵션 외에도, `minSize`와 `timeout`이라는 두 가지 새 옵션을 통해 배치 처리 제어를 더 세밀하게 할 수 있습니다.

* `minSize`: 워커가 배치를 처리하기 전에 필요한 최소 작업 수를 지정합니다. 워커는 최소 `minSize`개의 작업이 준비될 때까지 기다린 뒤, `size` 한도까지 가져와 처리합니다. 사용 가능한 작업이 `minSize`보다 적으면, `timeout`도 설정되어 있지 않은 한 무기한 대기합니다.
* `timeout`: `minSize` 작업이 쌓이기를 워커가 기다리는 최대 시간(밀리초)을 정의합니다. `minSize`에 도달하기 전에 시간이 만료되면, 워커는 `size` 한도 내에서 현재 가능한 작업을 처리합니다. `minSize`가 설정되지 않으면 `timeout` 옵션은 사실상 무시되며, 워커는 단순히 현재 가능한 작업만 배치로 묶습니다.

{% hint style="info" %}
중요: `minSize`와 `timeout`은 그룹과 호환되지 않습니다. 그룹을 사용할 때 워커는 `minSize`를 무시하고, 대기 없이 가능한 작업을 배치로 묶으려고 시도합니다.
{% endhint %}

다음은 `minSize`와 `timeout`을 모두 사용하는 설정 예시입니다.

```typescript
const worker = new WorkerPro(
  'My Queue',
  async (job: JobPro) => {
    const batch = job.getBatch();
    for (let i = 0; i < batch.length; i++) {
      const batchedJob = batch[i];
      await doSomethingWithBatchedJob(batchedJob);
    }
  },
  {
    connection,
    batch: {
      size: 10,      // Maximum jobs per batch
      minSize: 5,    // Wait for at least 5 jobs
      timeout: 30_000 // Wait up to 30 seconds
    },
  },
);
```

이 예시에서:

* 워커는 배치당 최대 10개 작업까지, 최소 5개 작업이 준비될 때까지 기다립니다.
* 30초 안에 5개 이상의 작업이 준비되면, 해당 배치(최대 10개 작업)를 처리합니다.
* 30초 후에도 작업이 5개 미만이면, `minSize`보다 적더라도 현재 존재하는 작업을 처리합니다.

### 작업 실패 처리

배치를 사용할 때 기본 동작은, 프로세서가 예외를 던지면 **배치 내 모든 작업이 실패**하는 것입니다.

특정 작업만 실패시키려면, 배치 내 개별 작업에서 `setAsFailed` 메서드를 사용하세요.

```typescript
const worker = new WorkerPro(
  'My Queue',
  async (job: JobPro) => {
    const batch = job.getBatch();

    for (let i = 0; i < batch.length; i++) {
      const batchedJob = batch[i];
      try {
        await doSomethingWithBatchedJob(batchedJob);
      } catch (err) {
        batchedJob.setAsFailed(err);
      }
    }
  },
  { connection, batch: { size: 10 } },
);
```

`setAsFailed`로 명시적으로 표시한 작업만 실패하며, 나머지 작업은 프로세서가 종료되면 성공적으로 완료됩니다.

### 이벤트 처리

배치는 배치 내 모든 작업을 내부 배열에 담고 있는 더미 작업으로 감싸 관리합니다. 이는 배치 처리를 단순화하지만 이벤트 처리에는 영향을 줍니다. 예를 들어 워커 수준 이벤트 리스너(`worker.on('completed', ...)`)는 개별 작업이 아니라 더미 배치 작업에 대한 이벤트를 보고합니다.

이벤트 핸들러에서 배치 내 작업을 가져오려면 `getBatch` 메서드를 사용하세요.

```typescript
worker.on('completed', job => {
  const batch = job.getBatch();
  // ...
});
```

전역 이벤트 리스너를 사용하면, 작업이 배치로 처리되더라도 개별 작업 이벤트를 수신할 수 있습니다.

```typescript
import { QueueEventsPro } from '@taskforcesh/bullmq-pro';

const queueEvents = new QueueEventsPro(queueName, { connection });
queueEvents.on('completed', (jobId, err) => {
  // ...
});
```

### 제한 사항

현재 배치에서는 모든 워커 옵션을 사용할 수 있습니다. 다만, 아직 지원되지 않지만 향후 구현될 수 있는 기능이 일부 있습니다.

* [동적 rate limit](https://docs.bullmq.io/guide/rate-limiting#manual-rate-limit)
* [수동 작업 처리](https://docs.bullmq.io/patterns/manually-fetching-jobs)
* [동적으로 작업 지연](https://docs.bullmq.io/patterns/process-step-jobs#delaying).

