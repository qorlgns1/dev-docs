---
title: '그룹 일시 중지'
description: 'BullMQ Pro는 그룹을 전역적으로 일시 중지하는 기능을 지원합니다. 그룹이 일시 중지되면 워커는 해당 일시 중지된 그룹에 속한 어떤 작업도 가져가지 않습니다. 그룹을 일시 중지하면 현재 그 그룹의 작업을 처리 중인 워커는 해당 작업이 완료(또는 실패)될 때까지 계...'
---

Source URL: https://docs.bullmq.io/bullmq-pro/groups/pausing-groups

# 그룹 일시 중지

BullMQ Pro는 그룹을 전역적으로 일시 중지하는 기능을 지원합니다. 그룹이 일시 중지되면 워커는 해당 일시 중지된 그룹에 속한 어떤 작업도 가져가지 않습니다. 그룹을 일시 중지하면 현재 그 그룹의 작업을 처리 중인 워커는 해당 작업이 완료(또는 실패)될 때까지 계속 처리하고, 이후 그룹이 재개될 때까지 유휴 상태로 대기합니다.

그룹 일시 중지는 [`Queue`](https://api.bullmq.pro/classes/v7.QueuePro.html#pausegroup) 인스턴스에서 `pauseGroup` 메서드를 호출해 수행합니다:

```typescript
await myQueue.pauseGroup('groupId');
```

{% hint style="info" %}
해당 시점에 `groupId`가 존재하지 않더라도, 그룹은 일시적으로 생성될 수 있으므로 `groupId`는 일시 중지 목록에 추가됩니다.
{% endhint %}

{% hint style="warning" %}
그룹이 이미 일시 중지된 경우 `pauseGroup`은 `false`를 반환합니다.
{% endhint %}

그룹 재개는 [`Queue`](https://api.bullmq.pro/classes/v7.QueuePro.html#resumegroup) 인스턴스에서 `resumeGroup` 메서드를 호출해 수행합니다:

```typescript
await myQueue.resumeGroup('groupId');
```

{% hint style="warning" %}
그룹이 존재하지 않거나 이미 재개된 상태인 경우 `resumeGroup`은 `false`를 반환합니다.
{% endhint %}

## 더 읽어보기:

* 💡 [Pause Group API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#pausegroup)
* 💡 [Resume Group API Reference](https://api.bullmq.pro/classes/v7.QueuePro.html#resumegroup)

