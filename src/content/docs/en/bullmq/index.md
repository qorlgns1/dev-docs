---
title: 'What is BullMQ'
description: 'BullMQ is a Node.js library that implements a fast and robust queue system built on top of Redis that helps in resolving many modern age micro-service...'
---

Source URL: https://docs.bullmq.io/

# What is BullMQ | BullMQ

BullMQ is a [Node.js](https://nodejs.org) library that implements a fast and robust queue system built on top of [Redis](https://redis.io) that helps in resolving many modern age micro-services architectures.

The library is designed so that it will fulfill the following goals:

  * Exactly once queue semantics, i.e., attempts to deliver every message exactly one time, but it will deliver at least once in the worst case scenario*.

  * Easy to scale horizontally. Add more workers for processing jobs in parallel.

  * Consistent.

  * High performant. Try to get the highest possible throughput from Redis by combining efficient .lua scripts and pipelining.

View the repository, see open issues, and contribute back [on GitHub](https://github.com/taskforcesh/bullmq)!

##

[](https://docs.bullmq.io/#features)

**Features**

If you are new to Message Queues, you may wonder why they are needed after all. Queues can solve many different problems in an elegant way, from smoothing out processing peaks to creating robust communication channels between micro-services or offloading heavy work from one server to many smaller workers, and many other use cases. Check the [Patterns](https://docs.bullmq.io/patterns/adding-bulks) section for getting some inspiration and information about best practices.

  * **Minimal CPU usage due to a polling-free design**

  * **Distributed job execution based on Redis**

  * **LIFO and FIFO jobs**

  * **Priorities**

  * **Delayed jobs**

  * **Scheduled and repeatable jobs according to cron specifications**

  * **Retries of failed jobs**

  * **Concurrency setting per worker**

  * **Threaded (sandboxed) processing functions**

  * **Automatic recovery from process crashes**

  * **Parent-Child dependencies**

###

[](https://docs.bullmq.io/#used-by)

Used by

BullMQ is used by many organizations big and small, here are some notable examples:

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-7eabf625a2932b111c2a5b7a651e2eaae6ad1b7a%252Fclipart1565701.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=88d0c630&sv=2)

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-7ffcd73605e901be045c7cf43cb61eb9a7a00ee4%252Fwordmark-logo.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b64bd75a&sv=2)

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-33c0c65bd9d6936b8ac33f4be7cbba2814b83ead%252Fdatawrapper-logo.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8ff2143f&sv=2)

![](https://docs.bullmq.io/~gitbook/image?url=https%3A%2F%2F1340146492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LUuDmt_xXMfG66Rn1GA%252Fuploads%252Fgit-blob-2038c9549e2aa39e1e8ce1a1017074c98953a7f4%252Fcurri-small.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4934647b&sv=2)

[NextQuick Start](https://docs.bullmq.io/readme-1)

Last updated 1 year ago

