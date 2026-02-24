---
title: 'index'
description: '{% hint style="warning" %}'
---

Source URL: https://docs.bullmq.io/patterns/flows

# 플로우

{% hint style="warning" %}
다음 패턴은 여전히 유용하지만, 새로운 [Flows](https://docs.bullmq.io/guide/flows) 기능으로 대부분 대체되었습니다.
{% endhint %}

일부 상황에서는 여러 작업으로 이루어진 플로우를 실행해야 할 수 있으며, 이 중 어떤 작업이든 실패할 수 있습니다. 예를 들어 데이터베이스를 업데이트하거나, 외부 서비스를 호출하거나, 그 밖의 비동기 호출을 수행해야 할 수 있습니다.

때로는 어떤 이유로든 작업 중 하나가 실패했을 때, 이 모든 작업을 다시 실행할 수 있는 [idempotent job](https://docs.bullmq.io/patterns/idempotent-jobs)을 만드는 것이 불가능할 수 있습니다. 대신 실패한 작업만 다시 실행하고, 아직 실행되지 않은 나머지 작업의 실행을 계속할 수 있기를 원할 수 있습니다.

이 문제를 해결하는 패턴은 작업 플로우를 각 작업마다 하나의 큐로 나누는 것입니다. 첫 번째 작업이 완료되면, 다음 작업을 해당 큐에 job으로 추가합니다.

