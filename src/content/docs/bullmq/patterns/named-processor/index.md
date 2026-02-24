---
title: '네임드 프로세서'
description: 'Worker를 인스턴스화할 때 가장 일반적인 사용 방식은 process 함수를 지정하는 것입니다.'
---

원문 URL: https://docs.bullmq.io/patterns/named-processor

# 네임드 프로세서

Worker를 인스턴스화할 때 가장 일반적인 사용 방식은 process 함수를 지정하는 것입니다.

하지만 때로는 특정 조건에서 작업을 처리할 함수를 둘 이상 지정할 수 있으면 유용합니다:

```typescript
const worker = new Worker(
  'queueName',
  async job => {
    switch (job.name) {
      case 'taskType1': {
        await doSomeLogic1();
        break;
      }
      case 'taskType2': {
        await doSomeLogic2();
        break;
      }
    }
  },
  { connection },
);
```

간단한 switch case를 사용해 로직을 구분할 수 있습니다. 이 예제에서는 작업 이름을 사용합니다.

{% hint style="warning" %}
이 기능은 Bull 패키지에 있었지만, 많은 혼란을 일으켰습니다. 따라서 대안을 제공하기 위해 이 패턴을 사용할 수 있습니다. 참고: [#297](https://github.com/taskforcesh/bullmq/issues/297), [#69](https://github.com/taskforcesh/bullmq/issues/69)
{% endhint %}

