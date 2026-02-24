---
title: '빠른 가이드'
description: '원본 URL: https://docs.bullmq.io/bull/quick-guide'
---

원본 URL: https://docs.bullmq.io/bull/quick-guide

# 빠른 가이드

### **기본 사용법**

```javascript
const Queue = require("bull");

const videoQueue = new Queue("video transcoding", "redis://127.0.0.1:6379");
const audioQueue = new Queue("audio transcoding", {
  redis: { port: 6379, host: "127.0.0.1", password: "foobared" },
}); // Specify Redis connection using object
const imageQueue = new Queue("image transcoding");
const pdfQueue = new Queue("pdf transcoding");

videoQueue.process(function (job, done) {
  // job.data contains the custom data passed when the job was created
  // job.id contains id of this job.

  // transcode video asynchronously and report progress
  job.progress(42);

  // call done when finished
  done();

  // or give a error if error
  done(new Error("error transcoding"));

  // or pass it a result
  done(null, { framerate: 29.5 /* etc... */ });

  // If the job throws an unhandled exception it is also handled correctly
  throw new Error("some unexpected error");
});

audioQueue.process(function (job, done) {
  // transcode audio asynchronously and report progress
  job.progress(42);

  // call done when finished
  done();

  // or give a error if error
  done(new Error("error transcoding"));

  // or pass it a result
  done(null, { samplerate: 48000 /* etc... */ });

  // If the job throws an unhandled exception it is also handled correctly
  throw new Error("some unexpected error");
});

imageQueue.process(function (job, done) {
  // transcode image asynchronously and report progress
  job.progress(42);

  // call done when finished
  done();

  // or give a error if error
  done(new Error("error transcoding"));

  // or pass it a result
  done(null, { width: 1280, height: 720 /* etc... */ });

  // If the job throws an unhandled exception it is also handled correctly
  throw new Error("some unexpected error");
});

pdfQueue.process(function (job) {
  // Processors can also return promises instead of using the done callback
  return pdfAsyncProcessor();
});

videoQueue.add({ video: "http://example.com/video1.mov" });
audioQueue.add({ audio: "http://example.com/audio1.mp3" });
imageQueue.add({ image: "http://example.com/image1.tiff" });

```

### **Promise 사용하기**

또는 `done` 콜백 대신 Promise 반환을 사용할 수 있습니다:

```javascript
videoQueue.process(function (job) {
  // don't forget to remove the done callback!
  // Simply return a promise
  return fetchVideo(job.data.url).then(transcodeVideo);

  // Handles promise rejection
  return Promise.reject(new Error("error transcoding"));

  // Passes the value the promise is resolved with to the "completed" event
  return Promise.resolve({ framerate: 29.5 /* etc... */ });

  // If the job throws an unhandled exception it is also handled correctly
  throw new Error("some unexpected error");
  // same as
  return Promise.reject(new Error("some unexpected error"));
});

```

### **샌드박스 프로세스**

process 함수는 별도 프로세스에서 실행할 수도 있습니다. 이렇게 하면 다음과 같은 장점이 있습니다:

* 프로세스가 샌드박스로 격리되므로 크래시가 발생해도 worker에 영향을 주지 않습니다.
* 큐에 영향을 주지 않고 블로킹 코드를 실행할 수 있습니다(작업이 멈추지 않음).
* 멀티코어 CPU를 더 효율적으로 활용할 수 있습니다.
* redis 연결 수가 줄어듭니다.

이 기능을 사용하려면 processor를 별도 파일로 만들기만 하면 됩니다:

```javascript
// processor.js
module.exports = function (job) {
  // Do some heavy work

  return Promise.resolve(result);
}
```

그리고 processor를 다음과 같이 정의합니다:

```javascript
// Single process:
queue.process('/path/to/my/processor.js');

// You can use concurrency as well:
queue.process(5, '/path/to/my/processor.js');

// and named processors:
queue.process('my processor', 5, '/path/to/my/processor.js');
```

### **반복 작업**

작업은 큐에 추가한 뒤 cron 명세에 따라 반복 처리되도록 설정할 수 있습니다:

```javascript
paymentsQueue.process(function (job) {
  // Check payments
});

// Repeat payment job once every day at 3:15 (am)
paymentsQueue.add(paymentsData, { repeat: { cron: "15 3 * * *" } });

```

팁: 식이 올바른지 여기에서 확인해 보세요: [cron expression generator](https://crontab.cronhub.io)

### **일시 중지 / 재개**

큐는 전역으로 일시 중지 및 재개할 수 있습니다(이 worker에 대해서만 처리를 중지하려면 `true`를 전달):

```javascript
queue.pause().then(function () {
  // queue is paused now
});

queue.resume().then(function () {
  // queue is resumed now
});
```

### **이벤트**

큐는 유용한 이벤트를 몇 가지 발생시킵니다. 예를 들면...

```javascript
myqueue.on('completed', function (job, result) {
  // Job completed with output result!
})
```

발생하는 이벤트의 전체 목록을 포함한 자세한 내용은 Events reference를 확인하세요.

### **큐 성능**

큐는 비교적 저렴하므로 많이 필요하다면 서로 다른 이름으로 새 큐를 만들면 됩니다. 하지만 큐가 너무 많아지면 관리가 어려워질 수 있습니다. 보통 12개 정도까지는 괜찮습니다.

```javascript
const userJohn = new Queue('john');
const userLisa = new Queue('lisa');
.
.
.
```

또한 각 큐 인스턴스마다 새로운 redis 연결이 필요하다는 점을 기억하세요. [reuse connections](https://github.com/OptimalBits/bull/blob/master/PATTERNS.md#reusing-redis-connections) 방법을 확인하거나, 비슷한 결과를 위해 [named processors](https://github.com/OptimalBits/bull/blob/master/REFERENCE.md#queueprocess)를 사용할 수도 있습니다.

### **클러스터 지원**

{% hint style="info" %}
버전 3.2.0 이상에서는 threaded processors 사용을 권장합니다.
{% endhint %}

큐는 견고하며, 여러 스레드 또는 프로세스에서 병렬로 실행해도 충돌 위험이나 큐 손상 위험이 없습니다. cluster를 사용해 프로세스 간 작업을 병렬화하는 아래의 간단한 예제를 확인하세요:

```javascript
const Queue = require("bull");
const cluster = require("cluster");

const numWorkers = 8;
const queue = new Queue("test concurrent queue");

if (cluster.isMaster) {
  for (let i = 0; i < numWorkers; i++) {
    cluster.fork();
  }

  cluster.on("online", function (worker) {
    // Let's create a few jobs for the queue workers
    for (let i = 0; i < 500; i++) {
      queue.add({ foo: "bar" });
    }
  });

  cluster.on("exit", function (worker, code, signal) {
    console.log("worker " + worker.process.pid + " died");
  });
} else {
  queue.process(function (job, jobDone) {
    console.log("Job done by worker", cluster.worker.id, job.id);
    jobDone();
  });
}

```

***

