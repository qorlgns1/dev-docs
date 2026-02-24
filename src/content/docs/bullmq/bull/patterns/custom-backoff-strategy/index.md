---
title: '커스텀 백오프 전략'
description: '재시도 시 내장 백오프 전략만으로 충분하지 않다면 커스텀 전략을 정의할 수 있습니다. 커스텀 백오프 전략은 큐의 함수로 정의됩니다. 작업을 처리하기 위해 지금까지 시도한 횟수가 이 함수의 첫 번째 파라미터로 전달되고, 작업이 실패할 때 발생한 오류가 두 번째 파라미터로...'
---

Source URL: https://docs.bullmq.io/bull/patterns/custom-backoff-strategy

# 커스텀 백오프 전략

재시도 시 내장 백오프 전략만으로 충분하지 않다면 커스텀 전략을 정의할 수 있습니다. 커스텀 백오프 전략은 큐의 함수로 정의됩니다. 작업을 처리하기 위해 지금까지 시도한 횟수가 이 함수의 첫 번째 파라미터로 전달되고, 작업이 실패할 때 발생한 오류가 두 번째 파라미터로 전달됩니다. 이 함수는 재시도를 지연할 시간, 즉시 재시도하려면 0, 작업을 즉시 실패 처리하려면 -1을 반환합니다.

```typescript
const Queue = require('bull');

const myQueue = new Queue('Server B', {
  settings: {
    backoffStrategies: {
      jitter: function (attemptsMade, err) {
        return 5000 + Math.random() * 500;
      }
    }
  }
});
```

그런 다음 위에서 정의한 이름을 사용해 작업에서 새 백오프 전략을 지정할 수 있습니다:

```typescript
myQueue.add({foo: 'bar'}, {
  attempts: 3,
  backoff: {
    type: 'jitter'
  }
});
```

전략에 대한 옵션을 지정할 수도 있습니다:

```typescript
const Queue = require("bull");

const myQueue = new Queue("Server B", {
  settings: {
    backoffStrategies: {
      // truncated binary exponential backoff
      binaryExponential: function (attemptsMade, err, options) {
        // Options can be undefined, you need to handle it by yourself
        if (!options) {
          options = {};
        }
        const delay = options.delay || 1000;
        const truncate = options.truncate || 1000;
        console.error({ attemptsMade, err, options });
        return Math.round(
          Math.random() *
            (Math.pow(2, Math.min(attemptsMade, truncate)) - 1) *
            delay
        );
      },
    },
  },
});

myQueue.add(
  { foo: "bar" },
  {
    attempts: 10,
    backoff: {
      type: "binaryExponential",
      options: {
        delay: 500,
        truncate: 5,
      },
    },
  }
);

```

작업이 발생시키는 오류를 기준으로 백오프 전략을 구성할 수도 있습니다:

```typescript
const Queue = require('bull');

function MySpecificError() {};

const myQueue = new Queue('Server C', {
  settings: {
    backoffStrategies: {
      foo: function (attemptsMade, err) {
        if (err instanceof MySpecificError) {
          return 10000;
        }
        return 1000;
      }
    }
  }
});

myQueue.process(function (job, done) {
  if (job.data.msg === 'Specific Error') {
    throw new MySpecificError();
  } else {
    throw new Error();
  }
});

myQueue.add({ msg: 'Hello' }, {
  attempts: 3,
  backoff: {
    type: 'foo'
  }
});

myQueue.add({ msg: 'Specific Error' }, {
  attempts: 3,
  backoff: {
    type: 'foo'
  }
});
```

