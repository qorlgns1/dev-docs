---
title: '작업 재시도'
description: 'BullMQ는 이미 완료되었거나 실패한 작업을 프로그래밍 방식으로 재시도할 수 있는  메서드를 제공합니다. 이는 자동 재시도 메커니즘( 옵션으로 구성)과는 다릅니다.  메서드를 사용하면 언제든지 수동으로 작업을 대기 큐로 다시 이동할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/jobs/retrying-job

# 작업 재시도

BullMQ는 이미 완료되었거나 실패한 작업을 프로그래밍 방식으로 재시도할 수 있는 `retry` 메서드를 제공합니다. 이는 자동 재시도 메커니즘(`attempts` 옵션으로 구성)과는 다릅니다. `retry` 메서드를 사용하면 언제든지 수동으로 작업을 대기 큐로 다시 이동할 수 있습니다.

## Job.retry()를 사용해야 하는 경우

`retry` 메서드는 다음과 같은 시나리오에서 유용합니다:

* **수동 개입**: 일시적인 외부 이슈로 작업이 실패했지만 해당 이슈가 해결된 경우
* **완료된 작업 재처리**: 동일한 데이터로 완료된 작업을 다시 실행해야 하는 경우
* **워크플로 복구**: 작업이 잘못 실패하게 만든 시스템 장애나 버그에서 복구하는 경우

{% hint style="info" %}
`completed` 또는 `failed` 상태의 작업만 재시도할 수 있습니다. Active, waiting, delayed 작업은 재시도할 수 없습니다.
{% endhint %}

## 기본 사용법

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue, Job } from 'bullmq';

const queue = new Queue('my-queue');

// Get a failed job by ID
const job = await Job.fromId(queue, 'job-id');

// Retry a failed job (default state is 'failed')
await job.retry();

// Retry a completed job
await job.retry('completed');
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Queue, Job

queue = Queue('my-queue')

# Get a failed job by ID
job = await Job.fromId(queue, 'job-id')

# Retry a failed job (default state is 'failed')
await job.retry()

# Retry a completed job
await job.retry('completed')

await queue.close()
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
# Get a job reference (must have connection set)
job = %Job{id: "job-id", queue_name: "my-queue", prefix: "bull", connection: conn}

# Retry a failed job (default state is :failed)
{:ok, updated_job} = Job.retry(job)

# Retry a completed job
{:ok, updated_job} = Job.retry(job, :completed)
```

{% endtab %}
{% endtabs %}

## 재시도 옵션

`retry` 메서드는 시도 카운터를 초기화하는 옵션을 받습니다. 이는 재시도된 작업이 처음 처리되는 것처럼 동작하게 하려는 경우에 유용합니다.

### attemptsMade 초기화

`attemptsMade` 카운터는 작업이 몇 번 처리되었는지 추적합니다. 이를 초기화하면 작업이 다시 전체 재시도 허용 횟수를 사용할 수 있습니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
// Retry and reset the attempts counter
await job.retry('failed', { resetAttemptsMade: true });
```

{% endtab %}

{% tab title="Python" %}

```python
# Retry and reset the attempts counter
await job.retry('failed', {"resetAttemptsMade": True})
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
# Retry and reset the attempts counter
{:ok, updated_job} = Job.retry(job, :failed, reset_attempts_made: true)
```

{% endtab %}
{% endtabs %}

### attemptsStarted 초기화

`attemptsStarted` 카운터는 작업이 active 상태로 몇 번 이동했는지 추적합니다. 이는 추적 목적에 유용할 수 있습니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
// Retry and reset both counters
await job.retry('failed', {
  resetAttemptsMade: true,
  resetAttemptsStarted: true
});
```

{% endtab %}

{% tab title="Python" %}

```python
# Retry and reset both counters
await job.retry('failed', {
    "resetAttemptsMade": True,
    "resetAttemptsStarted": True
})
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
# Retry and reset both counters
{:ok, updated_job} = Job.retry(job, :failed,
  reset_attempts_made: true,
  reset_attempts_started: true
)
```

{% endtab %}
{% endtabs %}

## 재시도 시 발생하는 일

작업을 재시도하면 다음이 발생합니다:

1. **작업이 대기 큐로 이동**: 작업이 completed/failed 세트에서 제거되고 대기 큐에 다시 추가됩니다.
2. **속성 초기화**: 다음 작업 속성이 초기화됩니다:
   * `failedReason` / `failed_reason` → `null` / `nil`
   * `finishedOn` / `finished_on` → `null` / `nil`
   * `processedOn` / `processed_on` → `null` / `nil`
   * `returnvalue` / `return_value` → `null` / `nil`
3. **이벤트 발생**: 작업이 성공적으로 이동하면 `waiting` 이벤트가 발생합니다.
4. **부모 의존성 복원**: 작업이 플로우의 자식인 경우, 부모와의 의존 관계가 복원됩니다.

{% hint style="warning" %}
`attemptsMade`를 초기화하지 않고 작업을 재시도했을 때, 해당 작업이 이미 재시도 횟수를 모두 소진한 상태라면 다시 처리될 때 즉시 실패합니다.
{% endhint %}

## 오류 처리

`retry` 메서드는 다음 경우에 실패할 수 있습니다:

| Error Code | 설명                                    |
| ---------- | --------------------------------------- |
| `-1`       | 작업이 존재하지 않음                    |
| `-3`       | 예상된 상태에서 작업을 찾지 못함        |

{% tabs %}
{% tab title="TypeScript" %}

```typescript
try {
  await job.retry('failed');
} catch (error) {
  console.error('Failed to retry job:', error.message);
}
```

{% endtab %}

{% tab title="Python" %}

```python
try:
    await job.retry('failed')
except Exception as error:
    print(f'Failed to retry job: {error}')
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
case Job.retry(job, :failed) do
  {:ok, updated_job} ->
    IO.puts("Job retried successfully")

  {:error, {:reprocess_failed, -1}} ->
    IO.puts("Job does not exist")

  {:error, {:reprocess_failed, -3}} ->
    IO.puts("Job was not in the expected state")

  {:error, reason} ->
    IO.puts("Failed to retry: #{inspect(reason)}")
end
```

{% endtab %}
{% endtabs %}

## 더 읽어보기

* 💡 [Retry API Reference](https://api.docs.bullmq.io/classes/v5.Job.html#retry)
* 💡 [Retrying Failing Jobs](https://docs.bullmq.io/guide/retrying-failing-jobs) - backoff 전략을 포함한 자동 재시도 구성
* 💡 [Stop Retrying Jobs](https://github.com/taskforcesh/bullmq/blob/master/docs/gitbook/guide/patterns/stop-retrying-jobs.md) - 추가 재시도를 방지하는 방법

