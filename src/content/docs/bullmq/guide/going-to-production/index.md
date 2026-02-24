---
title: '프로덕션으로 배포하기'
description: '이 장에서는 BullMQ 기반 애플리케이션을 프로덕션에 배포할 때 견고한 솔루션을 구축할 수 있도록 중요한 고려 사항과 팁을 제공합니다.'
---

Source URL: https://docs.bullmq.io/guide/going-to-production

# 프로덕션으로 배포하기

이 장에서는 BullMQ 기반 애플리케이션을 프로덕션에 배포할 때 견고한 솔루션을 구축할 수 있도록 중요한 고려 사항과 팁을 제공합니다.

### 영속성

BullMQ는 Redis 기반이므로 영속성을 수동으로 구성해야 합니다. 많은 호스팅 솔루션은 기본적으로 영속성을 제공하지 않으며, 대신 인스턴스별로 설정해야 합니다. 견고하고 빠른 솔루션을 제공하는 [AOF (*Append Only File*)](https://redis.io/docs/management/persistence/#aof-advantages)를 활성화하는 것을 권장합니다. 일반적으로 대부분의 애플리케이션에서는 쓰기당 1초면 충분합니다.

영속성은 매우 빠르지만 성능에 어느 정도 영향이 있으므로, 허용 가능한 범위를 벗어나지 않는지 확인하기 위해 적절한 벤치마크를 수행해야 합니다.

### 최대 메모리 정책

Redis는 캐시로 매우 자주 사용되며, 이는 메모리 사용량이 특정 수준에 도달하면 정의된 정책에 따라 키를 제거한다는 의미입니다. 반면 BullMQ는 Redis가 임의로 키를 제거하면 제대로 동작할 수 없습니다. **따라서 `maxmemory-policy` 설정을 `noeviction`으로 구성하는 것이 매우 중요합니다.** 큐의 올바른 동작을 보장하는 설정은 이것이 **유일**합니다.

### 자동 재연결

프로덕션 환경에서 시스템 견고성을 위해 중요한 요소 중 하나는 연결 문제 이후 자동으로 복구할 수 있어야 한다는 점입니다. BullMQ와 Redis 사이의 연결이 항상 온라인 상태를 유지한다고 보장하는 것은 불가능합니다. 그러나 중요한 것은 사람의 개입 없이 연결이 다시 가능해졌을 때 최대한 빠르게 복구되는 것입니다.

연결 끊김을 올바르게 처리하려면 [IORedis](https://www.npmjs.com/package/ioredis#Auto-reconnect)가 제공하는 몇 가지 옵션을 이해하는 것이 중요합니다. 여기서 중요한 옵션은 다음과 같습니다.

* `retryStrategy`
* `maxRetriesPerRequest`
* `enableOfflineQueue`

또한 `Queue`와 `Worker` 클래스에서 흔히 원하는 동작 차이를 이해하는 것도 중요합니다. 일반적으로 `Queue` 클래스를 사용하는 작업은 일시적인 연결 끊김이 있을 때 [빠르게 실패](https://docs.bullmq.io/patterns/failing-fast-when-redis-is-down)해야 하며, 반대로 `Worker`는 예외를 발생시키지 않고 무기한 대기하도록 하는 것이 바람직합니다.

#### `retryStrategy`

이 옵션은 재시도 수행에 사용할 함수를 결정하는 데 사용됩니다. 재연결이 완료될 때까지 재시도는 계속됩니다. BullMQ 내부에서 생성되는 IORedis 연결에는 다음 전략을 사용합니다.

```ts
 retryStrategy: function (times: number) {
    return Math.max(Math.min(Math.exp(times), 20000), 1000);
 }
```

즉, 최소 1초, 최대 20초의 재시도 시간으로 지수 백오프를 사용해 재시도합니다. 이 `retryStrategy`는 사용자 정의 IORedis 옵션을 정의한 커스텀 전략을 전달하여 쉽게 재정의할 수 있습니다.

#### `maxRetriesPerRequest`

이 옵션은 실패한 요청에 대해 재시도를 수행할 최대 횟수를 설정합니다. `Worker`의 경우 이 옵션을 **`null`**로 설정하는 것이 중요합니다. 그렇지 않으면 특정 명령 호출 시 Redis가 발생시키는 예외로 인해 워커 기능이 깨질 수 있습니다. `Worker`를 인스턴스화할 때 이 옵션은 기본적으로 항상 `null`로 설정되지만, 기존 IORedis 인스턴스를 전달하거나 `Worker` 인스턴스화 시 이 옵션에 다른 값을 전달하면 재정의될 수 있습니다. 두 경우 모두 BullMQ는 경고를 출력하므로, 의도치 않은 여러 결과를 초래할 수 있으니 반드시 이 경고를 해결해야 합니다.

#### `enableOfflineQueue`

IORedis는 연결이 오프라인일 때 명령을 큐잉하는 작은 오프라인 큐를 제공합니다. `Queue` 인스턴스에서는 이 큐를 비활성화하고, `Worker` 인스턴스에서는 그대로 두는 것이 좋습니다. 이렇게 하면 `Queue` 호출은 [빠르게 실패](https://docs.bullmq.io/patterns/failing-fast-when-redis-is-down)하고, `Worker`는 연결이 재수립될 때까지 필요에 따라 대기하게 됩니다.

### 오류 로깅

연결 문제가 있을 때 트리거되는 error 이벤트용 핸들러를 연결해 두면 매우 유용합니다. 이는 큐를 디버깅할 때 도움이 되고 "unhandled errors"를 방지합니다.

```typescript
worker.on("error", (err) => {
  // Log your error.
})
```

```typescript
queue.on("error", (err) => {
  // Log your error.
})
```

### 워커 정상 종료

워커는 서버에서 실행되므로, 서버를 주기적으로 재시작해야 하는 상황은 피할 수 없습니다. 서버 재시작 직전에 워커가 작업을 처리 중일 수 있으므로, stalled job 위험을 최소화하려면 워커를 올바르게 종료하는 것이 중요합니다. 진행 중인 작업이 완료되기를 기다리지 않고 워커를 종료하면 해당 작업은 stalled로 표시되며, 새 워커가 온라인 상태가 되면 자동으로 처리됩니다(기본 대기 시간은 약 30초). 하지만 stalled job은 피하는 것이 더 좋고, 앞서 언급했듯 서버 재시작 전에 워커를 종료하면 이를 달성할 수 있습니다.

Node.js 서버에서는 정상 종료를 위해 `SIGINT`와 `SIGTERM` 신호를 모두 수신하는 것이 좋은 관행으로 여겨집니다. 이유는 다음과 같습니다.

* `SIGINT`는 일반적으로 터미널에서 사용자가 Ctrl+C를 입력해 프로세스를 중단할 때 전송됩니다. 개발 중이거나 포그라운드에서 실행 중인 서버는 이 신호를 수신해, 해당 키 조합이 눌렸을 때 올바르게 종료할 수 있어야 합니다.
* `SIGTERM`은 일반적으로 프로세스 종료를 요청하기 위해 전송되는 신호입니다. `SIGKILL`과 달리 이 신호는 프로세스가 포착할 수 있으므로(리소스를 정리하고 정상 종료 가능), 시스템 데몬, Kubernetes 같은 오케스트레이션 도구, PM2 같은 프로세스 매니저가 서비스를 중지할 때 주로 사용합니다.

다음은 이를 구현하는 예시입니다.

```typescript

const gracefulShutdown = async (signal) => {
  console.log(`Received ${signal}, closing server...`);
  await worker.close();
  // Other asynchronous closings
  process.exit(0);
}

process.on('SIGINT', () => gracefulShutdown('SIGINT'));

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));

```

위 코드는 작업이 절대 stalled 상태가 되지 않음을 보장하지는 않습니다. 작업 시간이 서버 재시작을 위한 grace period보다 더 길 수 있기 때문입니다.

### 자동 작업 제거

기본적으로 BullMQ가 처리한 모든 작업은 *completed* 또는 *failed* 상태가 되며 영구적으로 보관됩니다. 이 동작은 일반적으로 가장 바람직하지 않으므로, 보관할 최대 작업 수를 구성하는 것이 좋습니다. 가장 일반적인 구성은 최근 완료 내역 가시성을 위해 완료된 작업은 소수만 유지하고, 실패한 작업은 수동 재시도나 실패 원인에 대한 심층 디버깅을 위해 전부 또는 매우 큰 수로 유지하는 것입니다.

자동 제거 구성 방법은 [여기](https://docs.bullmq.io/guide/queues/auto-removal-of-jobs)에서 더 자세히 확인할 수 있습니다.

### 데이터 보호

프로덕션 배포 시 고려해야 할 또 다른 중요한 점은 작업의 data 필드가 평문으로 저장된다는 사실입니다. **가장 좋은 방법은 작업에 민감한 데이터를 아예 저장하지 않는 것입니다.** 하지만 이것이 불가능하다면, 민감한 데이터 부분을 큐에 추가하기 전에 암호화하는 것을 강력히 권장합니다.

**보안을 가볍게 여기지 마십시오. 오늘날 보안은 핵심 관심사여야 하며, 데이터 유실과 비즈니스의 경제적 피해 위험은 현실적이고 매우 심각합니다.**

### 처리되지 않은 예외와 거부

특히 프로덕션 환경에서 흔한 또 다른 문제는 NodeJS가 기본적으로 처리되지 않은 예외가 있으면 중단된다는 점입니다. 이는 BullMQ 기반 애플리케이션만의 문제가 아니라 모든 NodeJS 애플리케이션에 해당하는 일반 원칙입니다. 서비스 어딘가에서 처리되지 않은 예외를 정상적으로 처리하도록 보장해 두면, 이런 문제가 발생했을 때 애플리케이션이 중단될 위험 없이 수정할 수 있습니다.

```typescript
process.on("uncaughtException", function (err) {
  // Handle the error safely
  logger.error(err, "Uncaught exception");
});

process.on("unhandledRejection", (reason, promise) => {
  // Handle the error safely
  logger.error({ promise, reason }, "Unhandled Rejection at: Promise");
});
```

