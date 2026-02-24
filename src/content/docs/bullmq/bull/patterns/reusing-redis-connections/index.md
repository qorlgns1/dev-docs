---
title: 'Redis 연결 재사용'
description: '표준 큐는 Redis 서버에 3개의 연결이 필요합니다. 일부 상황에서는 연결을 재사용하고 싶을 수 있습니다. 예를 들어 Heroku처럼 연결 수가 제한된 환경이 그렇습니다. 이는  생성자의  옵션으로 처리할 수 있습니다.'
---

Source URL: https://docs.bullmq.io/bull/patterns/reusing-redis-connections

# Redis 연결 재사용

표준 큐는 Redis 서버에 **3개의 연결**이 필요합니다. 일부 상황에서는 연결을 재사용하고 싶을 수 있습니다. 예를 들어 Heroku처럼 연결 수가 제한된 환경이 그렇습니다. 이는 `Queue` 생성자의 `createClient` 옵션으로 처리할 수 있습니다.

#### 참고 사항:

* bclient 연결은 [재사용할 수 없으므로](https://github.com/OptimalBits/bull/issues/880), 이 호출이 일어날 때마다 새 연결을 반환해야 합니다.
* client 및 subscriber 연결은 공유할 수 있으며, 큐를 닫아도 닫히지 않습니다. 프로세스를 종료할 때는 먼저 큐를 닫고, 그다음 공유 연결(공유 중인 경우)을 닫으세요.
* 연결을 공유하지 않더라도 사용자 지정 연결 로직을 위해 `createClient`를 사용한다면, 나중에 큐가 종료될 때 수동으로 닫을 수 있도록 생성한 모든 연결 목록을 유지해야 할 수 있습니다. 프로세스의 graceful shutdown이 필요하다면 특히 그렇습니다.
* 생성하는 연결에 `keyPrefix`를 설정하지 마세요. 키 프리픽스가 필요하다면 bull의 내장 프리픽스 기능을 사용하세요.

```typescript
const { REDIS_URL } = process.env;

const Redis = require("ioredis");
const client = new Redis(REDIS_URL);
const subscriber = new Redis(REDIS_URL);

const opts = {
  // redisOpts here will contain at least a property of
  // connectionName which will identify the queue based on its name
  createClient: function (type, redisOpts) {
    switch (type) {
      case "client":
        return client;
      case "subscriber":
        return subscriber;
      case "bclient":
        return new Redis(REDIS_URL, redisOpts);
      default:
        throw new Error("Unexpected connection type: ", type);
    }
  },
};

const queueFoo = new Queue("foobar", opts);
const queueQux = new Queue("quxbaz", opts);
```

