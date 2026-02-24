---
title: 'Redis가 다운되었을 때 빠르게 실패하기'
description: '설계상 BullMQ는 Redis에 자동으로 재연결합니다. 큐 인스턴스가 Redis와 연결이 끊긴 상태에서 큐에 작업이 추가되면  명령은 실패하지 않습니다. 대신, 호출은 재연결이 발생해 완료할 수 있을 때까지 계속 대기합니다.'
---

출처 URL: https://docs.bullmq.io/patterns/failing-fast-when-redis-is-down

# Redis가 다운되었을 때 빠르게 실패하기

설계상 BullMQ는 Redis에 자동으로 재연결합니다. 큐 인스턴스가 Redis와 연결이 끊긴 상태에서 큐에 작업이 추가되면 `add` 명령은 실패하지 않습니다. 대신, 호출은 재연결이 발생해 완료할 수 있을 때까지 계속 대기합니다.

이 동작이 항상 바람직한 것은 아닙니다. 예를 들어 `add` 호출로 이어지는 REST API를 구현한 경우, `add`가 큐의 Redis 재연결을 기다리는 동안 HTTP 호출이 계속 점유되기를 원하지 않을 수 있습니다. 이 경우 `enableOfflineQueue: false` 옵션을 전달하면 `ioredis`가 명령을 큐잉하지 않고 예외를 발생시킵니다.

```typescript
const myQueue = new Queue("transcoding", {
  connection: {
    enableOfflineQueue: false,
  },
});

app.post("/jobs", async (req, res) => {
  try {
    const job = await myQueue.add("myjob", { req.body });
    res.status(201).json(job.id);
  }catch(err){
    res.status(503).send(err);
  }
})
```

이 접근 방식을 사용하면 호출자는 예외를 포착해 요구사항에 따라 처리할 수 있습니다(예: 호출 재시도 또는 포기).

{% hint style="danger" %}
현재는 큐를 인스턴스화하는 시점에 Redis 인스턴스가 최소한 온라인 상태여야 한다는 제한이 있습니다.
{% endhint %}

