---
title: 'index'
description: 'BullMQ는 함께 사용해 다양한 문제를 해결할 수 있는 4개의 클래스를 기반으로 합니다. 이 클래스들은 *Queue*, *Worker*, *QueueEvents*, *FlowProducer*입니다.'
---

Source URL: https://docs.bullmq.io/guide/introduction

# 소개

BullMQ는 함께 사용해 다양한 문제를 해결할 수 있는 4개의 클래스를 기반으로 합니다. 이 클래스들은 [***Queue***](https://api.docs.bullmq.io/classes/v5.Queue.html), [***Worker***](https://api.docs.bullmq.io/classes/v5.Worker.html), [***QueueEvents***](https://api.docs.bullmq.io/classes/v5.QueueEvents.html), [***FlowProducer***](https://api.docs.bullmq.io/classes/v5.FlowProducer.html)입니다.

가장 먼저 알아야 할 클래스는 *Queue* 클래스입니다. 이 클래스는 큐를 나타내며, 큐에 ***job***을 추가하는 데 사용할 수 있고, 일시 중지, 정리, 큐에서 데이터 가져오기 같은 기본적인 조작도 수행할 수 있습니다.

BullMQ의 job은 기본적으로 큐에 저장할 수 있는 사용자가 만든 데이터 구조입니다. job은 ***worker***에 의해 처리됩니다. 두 번째로 알아두어야 할 클래스는 *Worker*입니다. Worker는 job을 처리할 수 있는 인스턴스입니다. Worker는 같은 Node.js 프로세스에서 여러 개 실행할 수도 있고, 별도의 프로세스나 서로 다른 머신에서 실행할 수도 있습니다. 이들은 모두 큐에서 job을 가져와 처리하고, 해당 job을 완료 또는 실패로 표시합니다.

