---
title: 'Redis Cluster'
description: 'Bull 내부 동작은 서로 다른 키에 걸친 원자적 연산을 필요로 합니다. 이 동작은 클러스터 구성에서의 Redis 규칙을 깨뜨립니다. 하지만 bull prefix 옵션을 클러스터 "hash tag"로 올바르게 사용하면 클러스터 환경을 여전히 사용할 수 있습니다. 해시 ...'
---

Source URL: https://docs.bullmq.io/patterns/redis-cluster

# Redis Cluster

Bull 내부 동작은 서로 다른 키에 걸친 원자적 연산을 필요로 합니다. 이 동작은 클러스터 구성에서의 Redis 규칙을 깨뜨립니다. 하지만 bull prefix 옵션을 클러스터 "hash tag"로 올바르게 사용하면 클러스터 환경을 여전히 사용할 수 있습니다. 해시 태그는 특정 키가 동일한 해시 슬롯에 배치되도록 보장하는 데 사용됩니다. 해시 태그에 대한 자세한 내용은 [redis cluster tutorial](https://redis.io/topics/cluster-tutorial)에서 확인하세요. 해시 태그는 대괄호로 정의됩니다. 즉, 키에 대괄호 안의 부분 문자열이 있으면 해당 부분 문자열을 기준으로 키가 배치될 해시 슬롯이 결정됩니다.

요약하면, bull을 Redis 클러스터와 호환되게 하려면 대괄호 안에 큐 prefix를 사용하세요. 예:

큐를 클러스터와 호환되게 만드는 방법은 두 가지가 있습니다. 큐 prefix를 정의하거나:

```typescript
const queue = new Queue('cluster', {
  prefix: '{myprefix}',
});
```

큐 이름 자체를 감싸는 방법입니다:

```typescript
const queue = new Queue('{cluster}');
```

같은 클러스터에서 여러 큐를 사용하는 경우, 큐들이 클러스터 노드에 고르게 배치되도록 서로 다른 prefix를 사용해야 합니다. 이는 성능과 메모리 사용 측면에서 잠재적으로 향상을 가져올 수 있습니다.

