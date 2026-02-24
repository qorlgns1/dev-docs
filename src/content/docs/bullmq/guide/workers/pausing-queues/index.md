---
title: '큐 일시 중지'
description: 'BullMQ는 큐를 *전역적으로* 또는 *로컬로* 일시 중지하는 기능을 지원합니다. 큐가 *전역적으로* 일시 중지되면 어떤 워커도 해당 큐에서 작업을 가져오지 않습니다. 큐를 일시 중지하면, 현재 작업을 처리 중인 워커는 해당 작업이 완료(또는 실패)될 때까지 계속 처...'
---

원문 URL: https://docs.bullmq.io/guide/workers/pausing-queues

# 큐 일시 중지

BullMQ는 큐를 *전역적으로* 또는 *로컬로* 일시 중지하는 기능을 지원합니다. 큐가 *전역적으로* 일시 중지되면 어떤 워커도 해당 큐에서 작업을 가져오지 않습니다. 큐를 일시 중지하면, 현재 작업을 처리 중인 워커는 해당 작업이 완료(또는 실패)될 때까지 계속 처리하고, 이후 큐의 일시 중지가 해제될 때까지 대기 상태를 유지합니다.

큐 일시 중지는 [queue](https://api.docs.bullmq.io/classes/v5.Queue.html) 인스턴스에서 ***`pause`*** 메서드를 호출해 수행합니다:

```typescript
await myQueue.pause();
```

특정 워커 인스턴스를 *로컬로* 일시 중지하는 것도 가능합니다. 이 일시 중지는 전역 일시 중지와 유사하게 동작하며, 워커는 이미 시작한 작업 처리는 끝까지 수행하지만 새로운 작업은 처리하지 않습니다:

```typescript
await myWorker.pause();
```

위 호출은 이 워커가 현재 처리 중인 모든 작업이 완료(또는 실패)될 때까지 기다립니다. 호출이 완료되기 전에 현재 작업의 완료를 기다리고 싶지 않다면, 워커를 일시 중지할 때 `true`를 전달해 **실행 중인 작업을 무시한 채** 일시 중지할 수 있습니다:

```typescript
await myWorker.pause(true);
```

## 더 읽어보기:

* 💡 [Queue 일시 중지 API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Queue.html#pause)
* 💡 [Worker 일시 중지 API 레퍼런스](https://api.docs.bullmq.io/classes/v5.Worker.html#pause)

