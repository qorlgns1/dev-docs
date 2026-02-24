---
title: 'Redis 클러스터'
description: '원본 URL: https://docs.bullmq.io/bull/patterns/redis-cluster'
---

원본 URL: https://docs.bullmq.io/bull/patterns/redis-cluster

# Redis 클러스터

Bull 내부 동작은 서로 다른 키에 걸친 원자적 연산을 필요로 합니다. 이 동작은 클러스터 구성에서의 Redis 규칙을 깨뜨립니다. 하지만 클러스터 "hash tag"로 적절한 bull prefix 옵션을 사용하면 여전히 클러스터 환경을 사용할 수 있습니다. Hash tag는 특정 키가 동일한 hash slot에 배치되도록 보장하는 데 사용되며, 자세한 내용은 [Redis 클러스터 튜토리얼](https://redis.io/topics/cluster-tutorial)에서 확인할 수 있습니다. Hash tag는 대괄호로 정의됩니다. 즉, 키에 대괄호 안의 부분 문자열이 있으면 해당 부분 문자열을 사용해 키가 어느 hash slot에 배치될지 결정합니다.

요약하면, bull을 Redis 클러스터와 호환되게 하려면 대괄호 안에 큐 prefix를 사용하세요. 예를 들면 다음과 같습니다.

큐를 클러스터와 호환되게 만드는 방법은 두 가지가 있습니다. 큐 prefix를 정의하거나:

```typescript
const queue = new Queue('cluster', {
  prefix: '{myprefix}'
});
```

큐 이름 자체를 감쌀 수 있습니다:

```typescript
const queue = new Queue('{cluster}');
```

동일한 클러스터에서 여러 큐를 사용하는 경우, 큐들이 클러스터 노드에 고르게 배치되도록 서로 다른 prefix를 사용해야 합니다. 이렇게 하면 성능과 메모리 사용 측면에서 잠재적으로 이점이 있을 수 있습니다.

