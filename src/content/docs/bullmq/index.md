---
title: 'BullMQ란 무엇인가'
description: '원본 URL: https://docs.bullmq.io/'
---

원본 URL: https://docs.bullmq.io/

# BullMQ란 무엇인가 | BullMQ

BullMQ는 [Redis](https://redis.io) 위에 구축된 빠르고 견고한 큐 시스템을 구현한 [Node.js](https://nodejs.org) 라이브러리로, 현대적인 마이크로서비스 아키텍처의 다양한 문제를 해결하는 데 도움을 줍니다.

이 라이브러리는 다음 목표를 충족하도록 설계되었습니다:

  * 정확히 한 번(exactly once) 큐 시맨틱. 즉, 모든 메시지를 정확히 한 번 전달하려고 시도하지만, 최악의 경우에는 최소 한 번 이상 전달됩니다*.

  * 수평 확장이 쉬움. 작업을 병렬로 처리하기 위해 워커를 더 추가할 수 있습니다.

  * 일관성.

  * 고성능. 효율적인 .lua 스크립트와 파이프라이닝을 결합해 Redis에서 가능한 한 높은 처리량을 얻도록 설계되었습니다.

저장소를 확인하고, 열린 이슈를 보고, [GitHub](https://github.com/taskforcesh/bullmq)에서 기여해 주세요!

##

[](https://docs.bullmq.io/#features)

**기능**

메시지 큐를 처음 접한다면, 왜 큐가 필요한지 궁금할 수 있습니다. 큐는 처리량 급증을 완화하는 것부터 마이크로서비스 간 견고한 통신 채널을 만드는 것, 또는 한 서버의 무거운 작업을 여러 작은 워커로 오프로드하는 것까지 다양한 문제를 우아하게 해결할 수 있으며, 그 외에도 많은 활용 사례가 있습니다. 영감과 모범 사례 정보를 얻으려면 [Patterns](https://docs.bullmq.io/patterns/adding-bulks) 섹션을 확인하세요.

  * **폴링 없는 설계로 인한 최소 CPU 사용량**

  * **Redis 기반 분산 작업 실행**

  * **LIFO 및 FIFO 작업**

  * **우선순위**

  * **지연 작업**

  * **cron 명세에 따른 스케줄 및 반복 작업**

  * **실패한 작업 재시도**

  * **워커별 동시성 설정**

  * **스레드 기반(샌드박스) 처리 함수**

  * **프로세스 크래시로부터 자동 복구**

  * **부모-자식 의존성**

###

[](https://docs.bullmq.io/#used-by)

사용 중인 곳

BullMQ는 크고 작은 많은 조직에서 사용되고 있으며, 다음은 대표적인 예시입니다:

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-7eabf625a2932b111c2a5b7a651e2eaae6ad1b7a%252Fclipart1565701.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=88d0c630&sv=2)

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-7ffcd73605e901be045c7cf43cb61eb9a7a00ee4%252Fwordmark-logo.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b64bd75a&sv=2)

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-33c0c65bd9d6936b8ac33f4be7cbba2814b83ead%252Fdatawrapper-logo.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8ff2143f&sv=2)

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-2038c9549e2aa39e1e8ce1a1017074c98953a7f4%252Fcurri-small.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4934647b&sv=2)

[다음빠른 시작](https://docs.bullmq.io/readme-1)

마지막 업데이트: 1년 전

