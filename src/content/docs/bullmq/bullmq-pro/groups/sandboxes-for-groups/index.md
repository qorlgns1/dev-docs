---
title: '그룹용 샌드박스'
description: '그룹을 처리할 때 샌드박스를 사용하는 것도 가능합니다. 기본적으로는 표준 BullMQ에서와 동일하게 동작하지만, 예를 들어 프로세서로 전달되는 job 객체에서  속성에 접근할 수 있습니다:'
---

출처 URL: https://docs.bullmq.io/bullmq-pro/groups/sandboxes-for-groups

# 그룹용 샌드박스

그룹을 처리할 때 [샌드박스](https://docs.bullmq.io/guide/workers/sandboxed-processors)를 사용하는 것도 가능합니다. 기본적으로는 표준 BullMQ에서와 동일하게 동작하지만, 예를 들어 프로세서로 전달되는 job 객체에서 `gid` 속성에 접근할 수 있습니다:

```typescript
import { SandboxedJobPro } from '@taskforcesh/bullmq-pro';

module.exports = function (job: SandboxedJobPro) {
  expect(job).to.have.property('gid');
  expect(job.opts).to.have.property('group');
  expect(job.opts.group).to.have.property('id');
  expect(job.opts.group.id).to.be.a('string');
  expect(job.opts.group.id).to.equal(job.gid);
};
```

{% hint style="danger" %}
현재 샌드박스 프로세서에서 지원되는 Pro 기능은 Groups뿐입니다.
{% endhint %}

