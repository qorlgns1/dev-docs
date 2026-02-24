---
title: '부모 작업 계속 진행'
description: '{% hint style="info" %}'
---

Source URL: https://docs.bullmq.io/guide/flows/continue-parent

# 부모 작업 계속 진행

{% hint style="info" %}
v5.58.0부터 사용 가능
{% endhint %}

`continueParentOnFailure` 옵션은 자식 작업이 실패하는 즉시 부모 작업이 처리를 시작할 수 있게 해주며, `removeUnprocessedChildren` 메서드는 아직 처리되지 않은 자식 작업을 동적으로 정리할 수 있게 해줍니다. 또한 `getFailedChildrenValues`() 메서드를 사용하면 부모가 자식 실패로 인해 처리 중인지, 아니면 모든 자식이 성공적으로 완료되어 처리 중인지 판단할 수 있어 서로 다른 로직 경로를 정의할 수 있습니다.

### continueParentOnFailure

자식 작업에서 이 값을 `true`로 설정하면, 해당 자식이 실패할 때 부모 작업이 즉시 처리를 시작합니다. 이는 부모가 모든 자식의 종료를 기다리는 기본 동작과 대비됩니다.

* **핵심 동작**: 이 옵션이 설정된 자식이 실패하면, 다른 자식이 아직 실행 중이거나 미처리 상태여도 부모는 즉시 active 상태로 이동합니다.
* **사용 사례**: 자식 실패 시 워크플로를 중단하거나 정리 작업을 수행하는 등, 부모의 즉각적인 개입이 필요한 시나리오에 적합합니다.

### removeUnprocessedChildren

작업 인스턴스에서 사용할 수 있는 이 메서드는, 큐에서 아직 처리되지 않은 모든 자식 작업(대기 또는 지연 상태)을 제거합니다. 실패 후 남은 자식을 정리하기 위해 `continueParentOnFailure`와 함께 사용할 때 특히 유용합니다.

* **핵심 동작**: 아직 처리가 시작되지 않은 자식에게만 영향을 주며, **active, completed 또는 failed** 상태의 자식은 그대로 유지됩니다.
* **사용 방법**: 부모의 processor 내부에서 호출해 동적으로 정리합니다.

### getFailedChildrenValues

`getFailedChildrenValues()` 메서드는 실패한 자식 작업의 ID를 실패 오류 메시지에 매핑한 객체를 반환합니다. 이를 통해 부모 작업은 자신이 왜 처리 중인지 판단할 수 있습니다. 즉, 자식 실패(`continueParentOnFailure`로 트리거됨) 때문인지, 모든 자식이 성공적으로 완료되었기 때문인지 구분할 수 있습니다.

* **반환값**: 키는 작업 ID, 값은 오류 메시지인 객체를 반환합니다(예: { "job-id-1": "Upload failed" }). 실패한 자식이 없으면 객체는 비어 있습니다.
* **사용 방법**: 부모의 processor에서 이를 사용해 실패한 자식의 존재 여부에 따라 로직을 분기합니다.

### 예시

다음 예시는 이 기능들을 함께 사용하는 방법을 보여주며, 자식이 실패했는지 또는 모든 자식이 성공했는지에 따라 부모 작업이 다르게 반응합니다:

```typescript
const { FlowProducer } = require('bullmq');
const flow = new FlowProducer({ connection });

// Define the flow
const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name: 'child-job-1',
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      opts: { continueParentOnFailure: true }, // Parent processes if this child fails
    },
    {
      name: 'child-job-2',
      data: { idx: 1, foo: 'baz' },
      queueName: 'childrenQueueName',
    },
    {
      name: 'child-job-3',
      data: { idx: 2, foo: 'qux' },
      queueName: 'childrenQueueName',
    },
  ],
});

// Processor for the parent job
const processor = async (job) => {
  // Check if any children failed
  const failedChildren = await job.getFailedChildrenValues();
  const hasFailedChildren = Object.keys(failedChildren).length > 0;

  if (hasFailedChildren) {
    // Path 1: A child failed, triggering continueParentOnFailure
    console.log(`Parent job ${job.name} triggered by child failure(s):`, failedChildren);

    // Remove unprocessed children
    await job.removeUnprocessedChildren();
    console.log('Unprocessed child jobs have been removed.');

    // Additional cleanup or error handling can go here
  } else {
    // Path 2: All children completed successfully
    console.log(`Parent job ${job.name} processing after all children completed successfully.`);

    // Proceed with normal parent logic (e.g., aggregating results)
  }
};

```

### 실전 사용 사례

서로 다른 서버에 파일을 업로드하는 자식 작업들로 구성된 워크플로를 생각해보세요. 하나의 업로드가 실패하면(예: `child-job-1`), 부모는 continueParentOnFailure를 사용해 즉시 반응하고, `getFailedChildrenValues()`로 실패를 확인한 뒤, `removeUnprocessedChildren()`를 호출해 남은 업로드를 취소할 수 있습니다. 모든 업로드가 성공한 경우에는, 부모가 대신 결과를 집계할 수 있습니다.

