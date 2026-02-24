---
title: '작업 제거'
description: '현재 queue 클래스에는 사용 가능한 메서드가 3가지 있습니다:'
---

Source URL: https://docs.bullmq.io/guide/queues/removing-jobs

# 작업 제거

현재 queue 클래스에는 사용 가능한 메서드가 3가지 있습니다:

## Drain

waiting 또는 delayed 상태의 작업은 모두 제거하지만, active, waiting-children, completed, failed 상태의 작업은 제거하지 않습니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

await queue.drain();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    await queue.drain()
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

:ok = Queue.drain("paint", connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

$queue->drain();

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

또한 delayed 파라미터를 설정하면 delayed 작업도 함께 제거할 수 있습니다:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

// Also drain delayed jobs
await queue.drain(true);
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    # Also drain delayed jobs
    await queue.drain(delayed=True)
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

# Also drain delayed jobs
:ok = Queue.drain("paint", delayed: true, connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

// Also drain delayed jobs
$queue->drain(true);

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
drain 대상 큐에 속한 부모 작업은 대기 중인 자식 작업이 있으면 **waiting-children** 상태로 유지되지만, 대기 중인 자식 작업이 없으면 제거됩니다.
{% endhint %}

{% hint style="warning" %}
drain 대상이 아닌 다른 큐의 부모 작업은, 다른 큐에 대기 중인 자식 작업이 있으면 **waiting-children** 상태로 유지되고, 그렇지 않으면 wait로 이동합니다.
{% endhint %}

## Clean

특정 상태의 작업을 제거하되, 지정한 유예 기간 내의 작업은 유지합니다.

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

const deletedJobIds = await queue.clean(
  60000, // 1 minute
  1000, // max number of jobs to clean
  'paused',
);
```

## Obliterate

큐와 그 안의 모든 내용을 완전히 삭제합니다.

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

await queue.obliterate();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    await queue.obliterate()
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

:ok = Queue.obliterate("paint", connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

$queue->obliterate();

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

active 작업이 있어도 강제로 obliterate해야 하는 고급 시나리오에서는 다음과 같이 할 수 있습니다:

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import { Queue } from 'bullmq';

const queue = new Queue('paint');

// Force obliteration even with active jobs
await queue.obliterate({ force: true });
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from bullmq import Queue

async def main():
    queue = Queue('paint')

    # Force obliteration even with active jobs
    await queue.obliterate(force=True)
    await queue.close()

asyncio.run(main())
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
alias BullMQ.Queue

# Force obliteration even with active jobs
:ok = Queue.obliterate("paint", force: true, connection: :redis)
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php
use BullMQ\Queue;

$queue = new Queue('paint');

// Force obliteration even with active jobs
$queue->obliterate(['force' => true]);

$queue->close();
?>
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
obliterate 대상이 아닌 다른 큐의 부모 작업은, 다른 큐에 대기 중인 자식 작업이 있으면 **waiting-children** 상태로 유지되고, 그렇지 않으면 wait로 이동합니다.
{% endhint %}

### 더 읽어보기:

* 💡 [Drain API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#drain)
* 💡 [Clean API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#clean)
* 💡 [Obliterate API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#obliterate)

