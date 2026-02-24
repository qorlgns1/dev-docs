---
title: 'Bull에서 BullMQ로'
description: 'Bull과 BullMQ는 이제 너무 많이 분기되어, 실제로 하위 호환성을 보장하기 어렵습니다.'
---

Source URL: https://docs.bullmq.io/guide/migration-to-newer-versions/bull-to-bullmq

# Bull에서 BullMQ로

Bull과 BullMQ는 이제 너무 많이 분기되어, 실제로 하위 호환성을 보장하기 어렵습니다.

따라서 가장 안전한 방법은 BullMQ용 새 큐를 사용하고 기존 큐는 폐기(deprecate)하는 것입니다.

여기서 새 큐란 다른 큐 이름을 사용하거나 커스텀 prefix 옵션을 전달하는 것을 의미합니다. 기존 큐의 모든 작업이 완료될 때까지 bull과 bullmq 워커를 병렬로 실행하는 기간을 둘 수 있습니다. 이 기간에는 producer가 bullmq 큐에 작업을 추가해야 한다는 점을 고려하세요. bull의 모든 큐가 비워지면 이를 폐기할 수 있습니다.

이 과정을 모니터링하려면 <https://taskforce.sh> 같은 대시보드 도구를 사용할 수 있으며, 기존 큐를 제거하기 전에 완전히 비어 있는지 확인할 수 있습니다.

## 더 읽어보기:

* 💡 [Worker Prefix 옵션 참조](https://api.docs.bullmq.io/interfaces/v5.WorkerOptions.html#prefix)
* 💡 [Queue Prefix 옵션 참조](https://api.docs.bullmq.io/interfaces/v5.QueueOptions.html#prefix)

