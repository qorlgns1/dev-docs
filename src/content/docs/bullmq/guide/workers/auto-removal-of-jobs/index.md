---
title: '작업 자동 제거'
description: '기본적으로 큐 작업이 완료(또는 실패)되면  세트와  세트라는 두 개의 특수 세트에 저장됩니다. 이는 특히 개발 초기 단계에서 작업 결과를 확인할 수 있어 유용합니다. 하지만 솔루션이 프로덕션 수준에 도달하면, 크게 유용하지 않은 데이터로 Redis가 가득 차지 않도록...'
---

Source URL: https://docs.bullmq.io/guide/workers/auto-removal-of-jobs

# 작업 자동 제거

기본적으로 큐 작업이 완료(또는 실패)되면 `"completed"` 세트와 `"failed"` 세트라는 두 개의 특수 세트에 저장됩니다. 이는 특히 개발 초기 단계에서 작업 결과를 확인할 수 있어 유용합니다. 하지만 솔루션이 프로덕션 수준에 도달하면, 크게 유용하지 않은 데이터로 Redis가 가득 차지 않도록 보관할 완료 작업 수를 제한해야 하는 경우가 일반적입니다.

BullMQ는 최종 처리된 작업을 자동으로 제거하기 위한 여러 전략을 지원합니다. 이러한 전략은 Worker 옵션 [`removeOnComplete`](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#removeoncomplete) 및 [`removeOnFail`](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#removeonfail)에서 설정합니다.

### 최종 처리된 모든 작업 제거

가장 간단한 방법은 `removeOnComplete`/`removeOnFail`을 `{count: 0}`으로 설정하는 것입니다. 이 경우 모든 작업은 최종 처리되는 즉시 자동으로 제거됩니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const myWorker = new Worker(
  'myQueueName',
  async job => {
    // do some work
  },
  {
    connection,
    removeOnFail: { count: 0 },
  },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

def process_job(job):
    # do some work
    pass

worker = Worker(
    'myQueueName',
    process_job,
    {
        "connection": connection,
        "removeOnFail": {"count": 0},
    },
)
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
defmodule MyWorker do
  use BullMQ.Worker

  def process_job(_job) do
    # do some work
    :ok
  end
end

{:ok, worker} = BullMQ.Worker.start_link(
  queue: "myQueueName",
  processor: &MyWorker.process_job/1,
  connection: connection,
  remove_on_fail: %{count: 0}
)
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
작업 이름과 관계없이 삭제됩니다.
{% endhint %}

### 일정 개수의 작업 유지

유지할 작업의 최대 개수를 지정할 수도 있습니다. 일반적으로 완료된 작업은 소수만 유지하고, 실패한 작업은 훨씬 더 큰 수로 유지하는 것이 좋은 방법입니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const myWorker = new Worker(
  'myQueueName',
  async job => {
    // do some work
  },
  {
    connection,
    removeOnComplete: { count: 1000 },
    removeOnFail: { count: 5000 },
  },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

def process_job(job):
    # do some work
    pass

worker = Worker(
    'myQueueName',
    process_job,
    {
        "connection": connection,
        "removeOnComplete": {"count": 1000},
        "removeOnFail": {"count": 5000},
    },
)
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
defmodule MyWorker do
  use BullMQ.Worker

  def process_job(_job) do
    # do some work
    :ok
  end
end

{:ok, worker} = BullMQ.Worker.start_link(
  queue: "myQueueName",
  processor: &MyWorker.process_job/1,
  connection: connection,
  remove_on_complete: %{count: 1000},
  remove_on_fail: %{count: 5000}
)
```

{% endtab %}
{% endtabs %}

### 작업의 경과 시간 기준으로 유지

또 다른 방법은 특정 기간 이내의 작업만 유지하는 것입니다. `removeOn` 옵션은 `age`, `count`, `limit` 필드를 포함한 [`KeepJobs`](https://api.docs.bullmq.io/interfaces/v5.KeepJobs.html) 객체를 받습니다. `age`는 유지할 작업의 경과 시간(초)을 지정하는 데 사용되고, `count`는 전체 유지 개수를 제한하는 데 사용할 수 있으며, `limit`는 정리(cleanup) 반복 한 번에 제거할 작업 수를 제어합니다. `count` 옵션은 매우 짧은 시간에 예상치 못한 많은 작업이 발생했을 때 유용하며, 이 경우 메모리 부족을 방지하기 위해 일정 개수로 제한하고자 할 수 있습니다. `limit` 옵션은 한 번에 처리하는 작업 수를 제한해 정리 작업의 성능 영향을 제어하는 데 도움이 됩니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
const myWorker = new Worker(
  'myQueueName',
  async job => {
    // do some work
  },
  {
    connection,
    removeOnComplete: {
      age: 3600, // keep up to 1 hour
      count: 1000, // keep up to 1000 jobs
      limit: 100, // remove up to 100 jobs per cleanup iteration
    },
    removeOnFail: {
      age: 24 * 3600, // keep up to 24 hours
      limit: 50, // remove up to 50 jobs per cleanup iteration
    },
  },
);
```

{% endtab %}

{% tab title="Python" %}

```python
from bullmq import Worker

def process_job(job):
    # do some work
    pass

worker = Worker(
    'myQueueName',
    process_job,
    {
        "connection": connection,
        "removeOnComplete": {
            "age": 3600,  # keep up to 1 hour
            "count": 1000,  # keep up to 1000 jobs
            "limit": 100,  # remove up to 100 jobs per cleanup iteration
        },
        "removeOnFail": {
            "age": 24 * 3600,  # keep up to 24 hours
            "limit": 50,  # remove up to 50 jobs per cleanup iteration
        },
    },
)
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
defmodule MyWorker do
  use BullMQ.Worker

  def process_job(_job) do
    # do some work
    :ok
  end
end

{:ok, worker} = BullMQ.Worker.start_link(
  queue: "myQueueName",
  processor: &MyWorker.process_job/1,
  connection: connection,
  remove_on_complete: %{
    age: 3600,    # keep up to 1 hour
    count: 1000,  # keep up to 1000 jobs
    limit: 100    # remove up to 100 jobs per cleanup iteration
  },
  remove_on_fail: %{
    age: 24 * 3600,  # keep up to 24 hours
    limit: 50        # remove up to 50 jobs per cleanup iteration
  }
)
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
작업 자동 제거는 지연(lazy) 방식으로 동작합니다. 즉, 새 작업이 완료되거나 실패할 때만 작업이 제거되며, 자동 제거는 그 시점에 수행됩니다.
{% endhint %}

