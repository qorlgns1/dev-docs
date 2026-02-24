---
title: '시작하기'
description: '원본 URL: https://docs.bullmq.io/python/introduction'
---

원본 URL: https://docs.bullmq.io/python/introduction

# 소개

### 설치

BullMQ는 pip 패키지로 제공되므로 pip를 사용해 설치할 수 있습니다:

```
$ pip install bullmq
```

### 시작하기

BullMQ는 동시성을 구현하고 작업을 효율적으로 처리하기 위해 [asyncio](https://docs.python.org/3/library/asyncio.html)를 사용합니다.

로컬에서 Redis 호스트가 실행 중이라고 가정하면, 다음과 같이 큐에 작업을 추가할 수 있습니다:

```python
from bullmq import Queue

queue = Queue("myQueue")

# Add a job with data { "foo": "bar" } to the queue
await queue.add("myJob", { "foo": "bar" })

...

# Close when done adding jobs
await queue.close()

```

큐에서 작업을 소비하려면 `Worker` 클래스를 사용해야 하며, 작업을 처리할 "processor" 함수를 제공해야 합니다. 워커가 인스턴스화되는 즉시 작업 소비를 시작합니다:

```python
from bullmq import Worker
import asyncio
import signal

async def process(job, job_token):
    # job.data will include the data added to the queue
    return doSomethingAsync(job)

async def main():

    # Create an event that will be triggered for shutdown
    shutdown_event = asyncio.Event()

    def signal_handler(signal, frame):
        print("Signal received, shutting down.")
        shutdown_event.set()

    # Assign signal handlers to SIGTERM and SIGINT
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # Feel free to remove the connection parameter, if your redis runs on localhost
    worker = Worker("myQueue", process, {"connection": "rediss://<user>:<password>@<host>:<port>"})

    # Wait until the shutdown event is set
    await shutdown_event.wait()

    # close the worker
    print("Cleaning up worker...")
    await worker.close()
    print("Worker shut down successfully.")

if __name__ == "__main__":
    asyncio.run(main())
```

{% hint style="warning" %}
Redis 응답이 바이너리 형식인 경우, (decode\_responses)\[<https://redis-py.readthedocs.io/en/latest/examples/connection\\_examples.html#By-default-Redis-return-binary-responses,-to-decode-them-use-decode\\_responses=True>] 옵션을 *True*로 전달해야 합니다.
{% endhint %}

