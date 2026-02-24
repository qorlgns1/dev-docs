---
title: 'AWS Elasticache'
description: '원본 URL: https://docs.bullmq.io/guide/redis-tm-hosting/aws-elasticache'
---

원본 URL: https://docs.bullmq.io/guide/redis-tm-hosting/aws-elasticache

# AWS Elasticache

Elasticache는 Amazon Web Services(AWS)에서 제공하는 관리형 캐싱 서비스이며, AWS 인프라 내에서 BullMQ를 사용할 때 좋은 선택지가 될 수 있습니다.

AWS에서 BullMQ와 함께 Elasticache를 사용할 때 고려할 몇 가지 사항은 다음과 같습니다:

1. 표준 cache-nodes 설정을 사용하세요(즉, serverless 버전은 사용하지 마세요. 현재 serverless는 호환되지 않는 maxmemory-policy를 사용합니다).
2. Elasticache 인스턴스에 접근하려면 BullMQ 인스턴스를 실행하는 서비스에서 접근할 수 있도록 허용하는 보안 그룹을 생성해야 합니다.
3.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-b5e688395c2061a69a970890d35e77fa217a460a%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

4\. VPC와 Inbound rule을 지정해야 합니다. 대부분의 경우 포트 범위 6379의 custom TCP와 적절한 source(테스트 및 일부 단순한 경우에는 anywhere도 잘 동작)를 사용하면 됩니다. 어떤 경우에도 클러스터는 AWS 외부에서 접근할 수 없다는 점을 기억하세요. 5. 보안 그룹을 Elasticache 클러스터와, 해당 클러스터에 접근해야 하는 서비스에 연결하세요. 6. Redis 파라미터에서 maxmemory-policy: noeviction을 사용하고 있는지 확인하세요. 기본 parameter group은 수정할 수 없으므로 새로 생성해야 합니다.

```
1. Go to Elasticache > Parameter Groups and click on Create.
2. Fill name, description, and Family, at the time of writing redis7 is the newest and the recommended one.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
```

7\. "Create"를 클릭하세요. 그런 다음 목록에서 parameter group을 찾습니다. Edit parameter values를 클릭한 뒤 maxmemory-policy를 검색하세요:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-6305ad6bc21de4aa7e6e56ea7d8ee9772d895226%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

8. 값을 "noeviction"으로 변경하세요:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-556e6c2decabcb31969d8e0913077e2ba118142b%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

9. 변경 사항을 저장하세요. 이제 elasticache 클러스터로 이동해 parameter group을 사용자 지정 그룹으로 변경할 수 있습니다. 인스턴스를 찾아 modify를 클릭하고 cluster settings로 이동하면 parameter group을 변경할 수 있습니다:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-837ae979da2ee9a9ed1405a576068d3dfbab2ea9%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

10. Preview changes를 클릭하고 Modify를 클릭하세요. 이후 클러스터는 BullMQ와 함께 사용할 준비가 완료됩니다.

