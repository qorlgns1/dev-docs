---
title: 'Dragonfly'
description: 'Dragonfly의 기능을 최대한 활용하려면 몇 가지 특정 단계가 필요합니다. 가장 중요한 것은 큐 이름을 중괄호를 사용해 지정하는 것입니다. 이 네이밍 규칙을 사용하면 Dragonfly가 각 큐에 스레드를 할당할 수 있습니다. 예를 들어 큐 이름이 라면 로 변경하세요...'
---

Source URL: https://docs.bullmq.io/guide/redis-tm-compatibility/dragonfly

# Dragonfly

[Dragonfly](https://www.dragonflydb.io/)는 Redis™를 대체할 수 있는 drop-in 솔루션을 제공하며, BullMQ에서 사용하는 여러 데이터 구조를 훨씬 더 빠르고 메모리 효율적으로 구현합니다. 또한 CPU의 모든 가용 코어를 활용할 수 있게 해줍니다. 일부 성능 결과는 [이 글](https://bullmq.io/news/101023/dragonfly-compatibility/)에서 확인할 수 있습니다.

Dragonfly의 기능을 최대한 활용하려면 몇 가지 특정 단계가 필요합니다. 가장 중요한 것은 큐 이름을 중괄호를 사용해 지정하는 것입니다. 이 네이밍 규칙을 사용하면 Dragonfly가 각 큐에 스레드를 할당할 수 있습니다. 예를 들어 큐 이름이 `myqueue,`라면 `{myqueue}`로 변경하세요.

여러 큐를 운영하는 경우, 이 방식으로 각 큐에 서로 다른 CPU 코어를 할당해 성능을 크게 향상할 수 있습니다. 큐가 하나뿐이어도 경우에 따라 멀티코어의 이점을 활용할 수 있습니다. 큐를 `{myqueue-1}`, `{myqueue-2}`처럼 여러 개로 분리하고, 작업을 무작위로 또는 라운드 로빈 방식으로 분배하는 것을 고려해 보세요.

{% hint style="info" %}
우선순위(priorities)나 rate-limiting 같은 일부 기능은 여러 큐에 걸쳐서는 동작하지 않을 수 있습니다. 단일 큐를 이런 방식으로 나눌 수 있는지는 여러분의 구체적인 요구사항에 따라 달라집니다.
{% endhint %}

BullMQ에 맞게 Dragonfly 인스턴스를 최적화하기 위한 자세한 지침과 필요한 플래그는 [공식 통합 가이드](https://www.dragonflydb.io/docs/integrations/bullmq)를 참고하세요.

