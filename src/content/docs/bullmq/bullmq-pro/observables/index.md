---
title: 'Observables'
description: '일반적인 promise를 반환하는 대신, 워커는 을 반환할 수도 있으며, 이를 통해 좀 더 고급 사용 사례를 구현할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/bullmq-pro/observables

# Observables

일반적인 promise를 반환하는 대신, 워커는 `Observable`을 반환할 수도 있으며, 이를 통해 좀 더 고급 사용 사례를 구현할 수 있습니다.

* 실행 중인 job을 깔끔하게 취소할 수 있습니다.
* "Time to live"(TTL)를 정의하여, 너무 오래 걸리는 job이 자동으로 취소되게 할 수 있습니다.
* observable이 반환한 마지막 값이 유지되므로, 예를 들어 job이 state machine 같은 형태로 구현되어 있다면 job을 재시도하면서 중단한 지점부터 이어서 계속할 수 있습니다.

`Observables`이 처음이라면 이 [introduction](https://www.learnrxjs.io/learn-rxjs/concepts/rxjs-primer)을 읽어보는 것이 좋습니다. `Observables`이 `Promises`보다 가지는 가장 큰 두 가지 장점은 1개보다 많은 값을 emit할 수 있다는 점과 *취소 가능*하다는 점입니다.

`Observables`을 사용하는 워커의 간단한 예시를 살펴보겠습니다.

```typescript
import { WorkerPro } from "@taskforcesh/bullmq-pro"
import { Observable } from "rxjs"

const processor = async () => {
  return new Observable<number>(subscriber => {
    subscriber.next(1);
    subscriber.next(2);
    subscriber.next(3);
    const intervalId = setTimeout(() => {
      subscriber.next(4);
      subscriber.complete();
    }, 500);

    // Provide a way of canceling and disposing the interval resource
    return function unsubscribe() {
      clearInterval(intervalId);
    };
  });
};

const worker = new WorkerPro(queueName, processor, { connection });
```

위 예시에서 observable은 4개의 값을 emit합니다. 처음 3개는 즉시, 4번째 값은 500ms 후에 emit됩니다. 또한 `subscriber`가 `unsubscribe` 함수를 반환한다는 점도 주목하세요. 이 함수는 `Observable`이 취소될 때 호출되므로, 필요한 정리 작업은 여기에서 수행하면 됩니다.

워커에서 여러 값을 반환하는 것이 무슨 용도인지 궁금할 수 있습니다. 떠오르는 한 가지 경우는 더 큰 processor가 있을 때, 프로세스가 크래시 나더라도 최신 값부터 이어서 계속할 수 있게 하고 싶은 상황입니다. 반환값에 대한 `switch` 문으로 이를 구현할 수 있으며, 대략 다음과 같습니다.

```typescript
import { WorkerPro } from "@taskforcesh/bullmq-pro"
import { Observable } from "rxjs"

const processor = async (job) => {
  return new Observable<number>(subscriber => {
    switch(job.returnvalue){
      default:
        subscriber.next(1);
      case 1:
        subscriber.next(2);
      case 2:
        subscriber.next(3);
      case 3:
        subscriber.complete();
    }
  });
};

const worker = new WorkerPro(queueName, processor, { connection });
```

