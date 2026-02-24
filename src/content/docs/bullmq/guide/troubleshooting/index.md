---
title: '문제 해결'
description: '이 섹션에서는 BullMQ를 사용할 때 마주칠 수 있는 몇 가지 일반적인 오류에 대한 힌트와 해결 방법을 확인할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/guide/troubleshooting

# 문제 해결

이 섹션에서는 BullMQ를 사용할 때 마주칠 수 있는 몇 가지 일반적인 오류에 대한 힌트와 해결 방법을 확인할 수 있습니다.

### Lock 누락

워커에서 다음과 같은 형태의 오류가 발생할 수 있습니다: “Missing lock for job 1234. moveToFinished.” 이 오류는 워커가 처리 중인 작업이 예상치 못하게 해당 “lock”을 잃었을 때 발생합니다.

워커가 작업을 처리할 때는, 해당 작업이 현재 그 워커에 의해 “소유”되고 있음을 보장하는 특별한 lock 키가 필요합니다. 이를 통해 다른 워커가 같은 작업을 가져가지 못하게 합니다. 하지만 이 lock은 삭제될 수 있으며, 워커가 작업을 completed 또는 failed 상태로 이동하려고 시도할 때까지는 이러한 삭제가 감지되지 않을 수 있습니다.

lock이 삭제되는 이유는 여러 가지가 있으며, 가장 흔한 원인은 다음과 같습니다:

* 워커가 CPU를 과도하게 사용해 lock을 30초마다(기본 lock 만료 시간) 갱신할 시간을 확보하지 못하는 경우
* 워커가 Redis와의 통신을 잃어 제때 lock을 갱신하지 못하는 경우
* BullMQ의 작업 제거 API 중 하나를 사용해 작업을 강제로 삭제한 경우(또는 전체 큐를 삭제한 경우)
* Redis 인스턴스의 [maxmemory](https://docs.bullmq.io/guide/going-to-production#max-memory-policy) 정책이 잘못 설정된 경우. Redis가 만료 시간이 설정된 키를 미리 삭제하지 않도록 no-eviction이어야 합니다.

### 유효하지 않거나 정의되지 않은 환경 변수

환경 변수(예: 큐 이름이나 작업 데이터)를 사용하는 경우, 흔한 함정은 해당 환경 변수를 BullMQ 메서드에 직접 전달하는 것입니다. 이때 환경 변수가 다음 상태일 수 있습니다:

* Undefined (전혀 설정되지 않음)
* Empty strings (즉, "")
* Non-string values (예: 의도치 않게 객체나 배열을 전달)

이 경우 BullMQ 내부 Lua 스크립트에서 ERR Error running script ... Lua redis() command arguments must be strings or integers 오류가 발생할 수 있습니다. 일반적으로 Redis 명령에 전달된 파라미터가 유효한 문자열이나 숫자가 아닌 값이 되었을 때 발생합니다.

**이 오류를 피하기 위한 모범 사례**

1. 환경 변수를 초기에 검증하기

   애플리케이션 초기화 코드에서 필수 환경 변수를 모두 확인하세요:

```typescript
const queueName = process.env.QUEUE_NAME;
if (!queueName) {
  throw new Error("QUEUE_NAME is not defined or is empty.");
}

const queue = new Queue(queueName, { ... });
```

이렇게 하면 숨겨진 Lua 스크립트 오류를 유발하기 전에, 변수가 설정되지 않은 경우 즉시 실패하도록 할 수 있습니다.

2. TypeScript 엄격 모드 사용하기

TypeScript를 사용 중이라면 strictNullChecks를 활성화하고, 환경 변수를 `string | undefined`로 명시적으로 타입 지정하세요. 그러면 적절한 검증 없이 이를 사용하려는 코드는 컴파일 시점에 오류가 발생합니다.

3. 적절한 경우 기본값 제공하기

일부 경우에는 환경 변수가 없을 때 대체 값을 사용하고 싶을 수 있습니다:

```typescript
const queueName = process.env.QUEUE_NAME ?? 'defaultQueue';
```

단, 이 대체 값이 실제 운영 워크플로에서 유효한지 반드시 확인하세요.

이 가이드를 따르면, Redis 명령에 undefined 또는 유효하지 않은 인자를 전달해서 발생하는 BullMQ의 난해한 Lua 스크립트 오류를 예방하는 데 도움이 됩니다.

