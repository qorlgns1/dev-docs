---
title: '작업 취소'
description: '원본 URL: https://docs.bullmq.io/guide/workers/cancelling-jobs'
---

원본 URL: https://docs.bullmq.io/guide/workers/cancelling-jobs

# 작업 취소

작업 취소 기능을 사용하면 워커가 현재 처리 중인 작업을 정상적으로 취소할 수 있습니다. 이는 표준 `AbortController` 및 `AbortSignal` API를 사용해 구현됩니다.

## 작동 방식

워커가 작업을 처리할 때, 프로세서 함수의 세 번째 파라미터로 선택적인 `AbortSignal`을 받을 수 있습니다. 이 시그널을 사용해 작업이 취소되었는지 감지하고 정리 작업을 수행할 수 있습니다.

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('myQueue', async (job, token, signal) => {
  // The signal parameter is optional and provides cancellation support
  // Your job processing logic here
});
```

## 작업 취소하기

`Worker` 클래스는 작업 취소를 위한 메서드를 제공합니다.

```typescript
// Cancel a specific job by ID
const cancelled = worker.cancelJob('job-id-123');
console.log('Job cancelled:', cancelled); // true if job was active, false otherwise

// Cancel with a reason (useful for debugging)
worker.cancelJob('job-id-456', 'User requested cancellation');

// Cancel all active jobs
worker.cancelAllJobs();

// Cancel all with a reason
worker.cancelAllJobs('System shutdown');

// Get list of active jobs from queue
const activeJobs = await queue.getActive();
console.log(
  'Active jobs:',
  activeJobs.map(j => j.id),
);
```

### 취소 사유

취소 사유를 제공하면 해당 값이 `AbortController.abort(reason)` 메서드로 전달되며, `signal.reason`을 통해 접근할 수 있습니다.

```typescript
const worker = new Worker('myQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    signal?.addEventListener('abort', () => {
      // Access the cancellation reason
      const reason = signal.reason || 'No reason provided';
      console.log(`Job ${job.id} cancelled: ${reason}`);

      reject(new Error(`Cancelled: ${reason}`));
    });

    // Your processing logic
  });
});

// Later, cancel with a descriptive reason
worker.cancelJob(job.id, 'Resource limit exceeded');
```

## 취소 처리 (권장 패턴)

**이벤트 기반 접근 방식**은 취소에 즉시 반응할 수 있으므로 권장되는 패턴입니다.

```typescript
import { Worker } from 'bullmq';

const worker = new Worker('myQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    // Listen for abort event
    signal?.addEventListener('abort', () => {
      console.log(`Job ${job.id} cancellation requested`);

      // Clean up resources
      clearInterval(interval);

      // Reject with error
      reject(new Error('Job was cancelled'));
    });

    // Your processing logic
    const interval = setInterval(() => {
      // Do work
      processNextItem();
    }, 100);
  });
});
```

### 이벤트 기반이 좋은 이유

* ✅ **즉시 반응** - 폴링 지연이 없음
* ✅ **더 효율적** - 루프에서 확인하느라 CPU를 낭비하지 않음
* ✅ **더 깔끔한 코드** - 관심사 분리
* ✅ **표준 패턴** - `fetch()` 같은 Web API와 일치

## 네이티브 API와 함께 사용하기 (권장)

많은 Web API가 `AbortSignal`을 네이티브로 지원합니다. 이 시그널은 **조합 가능**하므로 API에 전달하면서 동시에 직접 리스닝할 수도 있습니다.

```typescript
const worker = new Worker('fetchQueue', async (job, token, signal) => {
  return new Promise(async (resolve, reject) => {
    // Set up abort listener - handles cancellation for the job
    signal?.addEventListener('abort', () => {
      reject(new Error('Job was cancelled'));
    });

    // Pass the SAME signal to fetch - it will abort the network request
    const response = await fetch(job.data.url, {
      signal, // ✅ Cancels the HTTP request at network level
      method: 'GET',
      headers: job.data.headers,
    });

    const data = await response.json();
    resolve(data);
  });
});
```

**이 패턴이 더 나은 이유:**

* ✅ **더 단순함** - 하나의 abort 리스너가 모든 것을 처리
* ✅ **조합 가능** - 시그널을 `fetch()`에 전달하고 작업 내에서도 리스닝
* ✅ HTTP 요청이 네트워크 레벨에서 **실제로 취소됨**
* ✅ 취소 시 작업이 **정상적으로 실패 상태로 표시됨**
* ✅ 복잡한 오류 체크가 필요 없음

### `AbortSignal`을 지원하는 API

많은 최신 API는 `signal`을 직접 받습니다.

* `fetch(url, { signal })` - HTTP 요청
* `addEventListener(event, handler, { signal })` - abort 시 리스너 자동 제거
* 다수의 데이터베이스 클라이언트(Postgres, MongoDB 드라이버)
* 최신 Node.js API의 파일 시스템 작업

## 사용자 정의 작업 취소

`AbortSignal`을 네이티브로 지원하지 않는 작업의 경우, 적절한 정리 로직을 구현하세요.

```typescript
const worker = new Worker('customQueue', async (job, token, signal) => {
  // Start your operation
  const operation = startLongRunningOperation(job.data);

  // Set up cancellation handler that actually stops the operation
  signal?.addEventListener('abort', () => {
    operation.cancel(); // ✅ Actually stops the work
  });

  try {
    const result = await operation.promise;
    return result;
  } catch (error) {
    if (signal?.aborted) {
      throw new Error('Operation cancelled');
    }
    throw error;
  }
});
```

## 취소 시 비동기 정리

프로미스를 reject하기 전에 정리 작업을 수행하세요.

```typescript
const worker = new Worker('dbQueue', async (job, token, signal) => {
  // Acquire resources
  const db = await connectToDatabase();
  const cache = await connectToCache();

  return new Promise(async (resolve, reject) => {
    // Set up cleanup handler
    signal?.addEventListener('abort', async () => {
      try {
        console.log('Cleaning up resources...');

        // Close connections gracefully
        await db.close();
        await cache.disconnect();

        console.log('Cleanup complete');
        reject(new Error('Cancelled after cleanup'));
      } catch (cleanupError) {
        console.error('Cleanup failed:', cleanupError);
        reject(new Error('Cleanup failed during cancellation'));
      }
    });

    try {
      // Do your work
      const result = await processWithDatabase(db, job.data);
      await cache.set(`job:${job.id}`, result);
      resolve(result);
    } catch (error) {
      // Cleanup on error too
      await db.close();
      await cache.disconnect();
      throw error;
    }
  });
});
```

## 대안: 폴링 패턴

`signal.aborted`를 주기적으로 확인하는 방법도 가능합니다(효율은 낮지만 일부 사용 사례에서는 더 단순함).

```typescript
const worker = new Worker('batchQueue', async (job, token, signal) => {
  const items = job.data.items;
  const results = [];

  for (let i = 0; i < items.length; i++) {
    // Check if job has been cancelled
    if (signal?.aborted) {
      throw new Error(`Cancelled after processing ${i} items`);
    }

    const result = await processItem(items[i]);
    results.push(result);

    // Update progress
    await job.updateProgress(((i + 1) / items.length) * 100);
  }

  return { results, total: results.length };
});
```

## 취소 후 작업 상태

### 일반 `Error` 사용 시 (재시도됨)

취소 시 일반 `Error`를 throw하면:

* **작업 상태**: `failed`로 이동
* **재시도**: `attempts`가 남아 있으면 작업은 재시도됨
* **사용 사례**: 나중에 작업을 재시도하길 원할 때

```typescript
const worker = new Worker('retryQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    signal?.addEventListener('abort', () => {
      // Regular Error - job will retry if attempts remain
      reject(new Error('Cancelled, will retry'));
    });

    // Your work...
  });
});

// Set attempts when adding jobs
await queue.add('task', data, { attempts: 3 });
```

### `UnrecoverableError` 사용 시 (재시도 없음)

`UnrecoverableError`를 throw하면:

* **작업 상태**: `failed`로 이동
* **재시도**: 작업은 재시도되지 않음
* **사용 사례**: 취소가 영구적이어야 할 때

```typescript
import { Worker, UnrecoverableError } from 'bullmq';

const worker = new Worker('noRetryQueue', async (job, token, signal) => {
  return new Promise((resolve, reject) => {
    signal?.addEventListener('abort', () => {
      // UnrecoverableError - no retries
      reject(new UnrecoverableError('Cancelled permanently'));
    });

    // Your work...
  });
});
```

## 락 갱신 실패 처리

워커가 작업 락을 잃는 경우(네트워크 이슈, Redis 문제, 또는 장시간 실행 작업 등), `lockRenewalFailed` 이벤트를 사용해 이 상황을 정상적으로 처리할 수 있습니다.

```typescript
const worker = new Worker(
  'myQueue',
  async (job, token, signal) => {
    return new Promise(async (resolve, reject) => {
      signal?.addEventListener('abort', async () => {
        console.log('Job cancelled - cleaning up resources');
        await cleanupResources();
        reject(new Error('Job cancelled'));
      });

      // Your work...
    });
  },
  { connection },
);

// Cancel jobs when lock renewal fails
worker.on('lockRenewalFailed', (jobIds: string[]) => {
  console.log('Lock renewal failed for jobs:', jobIds);
  jobIds.forEach(jobId => worker.cancelJob(jobId));
});
```

{% hint style="warning" %}
**중요:** 워커가 작업의 락을 잃으면(더 이상 락을 소유하지 않으므로) 해당 작업을 `failed` 상태로 이동시킬 수 없습니다. 대신:

1. `cancelJob()`이 시그널을 abort하여 프로세서가 리소스를 정리할 수 있게 함
2. 작업은 일시적으로 `active` 상태로 남음
3. BullMQ의 **stalled job checker**가 작업을 감지해 `waiting`으로 다시 이동시킴
4. 다른 워커(또는 동일한 워커)가 작업을 가져가 재시도함

이것은 올바르고 의도된 동작입니다. 락 손실 처리는 BullMQ의 stalled job 메커니즘을 신뢰하세요.
{% endhint %}

### 이 패턴이 동작하는 이유

* ✅ **즉시 정리**: 프로세서가 `signal.aborted`를 감지하고 리소스를 해제할 수 있음
* ✅ **불필요한 작업 없음**: 락을 잃으면 프로세서가 처리를 중단함
* ✅ **자동 복구**: stalled job checker가 작업을 다시 waiting으로 이동시킴
* ✅ **데이터 손실 없음**: 작업은 `attempts` 설정에 따라 재시도됨
* ✅ **기존 인프라와 호환**: BullMQ 내장 stalled job 처리 사용

## 취소를 고려한 다단계 작업

다단계 작업에서는 전략적인 지점마다 취소 여부를 확인하세요.

```typescript
const worker = new Worker('multiPhaseQueue', async (job, token, signal) => {
  return new Promise(async (resolve, reject) => {
    signal?.addEventListener('abort', () => {
      reject(new Error('Cancelled'));
    });

    try {
      // Phase 1: Download
      if (signal?.aborted) throw new Error('Cancelled before download');
      const data = await downloadData(job.data.url);
      await job.updateProgress(33);

      // Phase 2: Process
      if (signal?.aborted) throw new Error('Cancelled before processing');
      const processed = await processData(data);
      await job.updateProgress(66);

      // Phase 3: Upload
      if (signal?.aborted) throw new Error('Cancelled before upload');
      const result = await uploadResults(processed);
      await job.updateProgress(100);

      resolve(result);
    } catch (error) {
      reject(error);
    }
  });
});
```

## 하위 호환성

`signal` 파라미터는 선택 사항입니다. 이를 사용하지 않는 기존 프로세서는 계속 정상 동작합니다.

```typescript
// Old processor - still works
const worker = new Worker('myQueue', async job => {
  return await processJob(job);
});

// New processor - with cancellation support
const worker = new Worker('myQueue', async (job, token, signal) => {
  // Can now handle cancellation
});
```

{% hint style="info" %}
취소 기능은 완전한 하위 호환성을 제공합니다. 취소 지원이 필요할 때만 시그널 처리를 추가하면 됩니다.
{% endhint %}

## 모범 사례

1. 즉시 반응을 위해 **이벤트 기반 취소**를 사용하세요.
2. abort 핸들러에서 **리소스를 정리**하세요.
3. 취소가 영구적이어야 하면 **UnrecoverableError**를 사용하세요.
4. 더 나은 제어를 위해 **타임아웃과 함께 조합**하세요.
5. 장시간 작업에서는 전략적인 지점마다 **`signal.aborted`를 확인**하세요.
6. 리소스가 열린 채 남지 않도록 **정리 오류를 정상적으로 처리**하세요.

## 더 읽어보기:

* 💡 [Worker API Reference](https://api.docs.bullmq.io/classes/v5.Worker.html)
* 💡 [AbortController MDN](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
* 💡 [AbortSignal MDN](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)

