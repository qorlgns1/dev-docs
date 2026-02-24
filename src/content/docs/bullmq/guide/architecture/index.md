---
title: '아키텍처'
description: 'Bull 큐의 잠재력을 최대한 활용하려면 job의 라이프사이클을 이해하는 것이 중요합니다. 프로듀서가  인스턴스에서  메서드를 호출하는 순간부터, job은 완료되거나 실패할 때까지(기술적으로는 실패한 job도 재시도되어 새로운 라이프사이클을 가질 수 있음) 여러 상태를...'
---

Source URL: https://docs.bullmq.io/guide/architecture

# 아키텍처

Bull 큐의 잠재력을 최대한 활용하려면 job의 라이프사이클을 이해하는 것이 중요합니다. 프로듀서가 `Queue` 인스턴스에서 [`add`](https://api.docs.bullmq.io/classes/v5.Queue.html#add) 메서드를 호출하는 순간부터, job은 완료되거나 실패할 때까지(기술적으로는 실패한 job도 재시도되어 새로운 라이프사이클을 가질 수 있음) 여러 상태를 거치는 라이프사이클에 들어갑니다.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-8ccf86e0633ddb1016f5f56af5dbe0decc412aa3%2Fsimple-architecture.png?alt=media" alt="큐에서 job의 라이프사이클을 보여주는 다이어그램으로, wait, prioritized, delayed, active, completed, failed 상태를 포함합니다"><figcaption><p>job 라이프사이클 - Queue</p></figcaption></figure>

job이 큐에 추가되면 다음 세 가지 상태 중 하나가 될 수 있습니다:

* **“wait”**: 처리되기 전에 모든 job이 먼저 들어가야 하는 대기 목록입니다.
* **“prioritized”**: 더 높은 우선순위를 가진 job이 먼저 처리됨을 의미합니다.
* **“delayed”**: job이 특정 timeout을 기다리거나 처리 대상으로 승격되기를 기다리는 상태를 의미합니다. 이러한 job은 직접 처리되지 않고, 대신 대기 목록의 맨 앞이나 우선순위 집합에 배치되며, worker가 유휴 상태가 되는 즉시 처리됩니다.

{% hint style="warning" %}
우선순위는 `0`부터 `2^21`까지이며, `0`이 가장 높은 우선순위입니다. 이는 Unix에서 사용되는 유사한 표준(<https://en.wikipedia.org/wiki/Nice\\_(Unix)>, 숫자가 클수록 우선순위가 낮음)을 따릅니다.
{% endhint %}

job의 다음 상태는 **“active”** 상태입니다. active 상태는 집합으로 표현되며, 현재 처리 중인 job들(즉, 이전 장에서 설명한 `process` 함수에서 실행 중인 job들)을 의미합니다. job은 프로세스가 완료되거나 예외가 발생할 때까지 시간 제한 없이 active 상태에 머무를 수 있으며, 그 결과 최종적으로 **“completed”** 또는 **“failed”** 상태가 됩니다.

job을 추가하는 또 다른 방법은 flow producer 인스턴스에서 [`add`](https://api.docs.bullmq.io/classes/v5.FlowProducer.html#add) 메서드를 사용하는 것입니다.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-72f32539e4167247ee0da7bcae189dc085ea6ec2%2Fflow-architecture.png?alt=media" alt="flow producer에서 job의 라이프사이클을 보여주는 다이어그램으로, wait, prioritized, delayed, waiting-children, active, completed, failed 상태를 포함합니다"><figcaption><p>job 라이프사이클 - Flow Producer</p></figcaption></figure>

flow producer로 job이 추가되면 세 가지 상태 중 하나가 될 수 있습니다. 자식이 없으면 **“wait”**, **“prioritized“**, **“delayed“** 상태 중 하나가 될 수 있고, **“waiting-children”** 상태가 될 수도 있습니다. waiting-children 상태는 해당 job이 모든 자식 job의 완료를 기다리고 있음을 의미합니다. 다만 waiting-children job은 직접 처리되지 않으며, 마지막 자식이 completed로 표시되는 즉시 대기 목록, delayed 집합(`delay`가 제공된 경우), 또는 prioritized 집합(`delay`가 0이고 `priority`가 0보다 큰 경우)으로 이동됩니다.

