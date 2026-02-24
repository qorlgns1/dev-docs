---
title: '옵션 1: 릴리스 다운로드(권장)'
description: 'PHP 패키지는 PHP 애플리케이션에서 BullMQ 큐에 작업을 추가할 수 있는 Queue client를 제공합니다. 이렇게 추가된 작업은 Node.js, Python, 또는 Elixir로 작성된 워커가 처리할 수 있습니다.'
---

원문 URL: https://docs.bullmq.io/php/introduction

# 소개

PHP 패키지는 PHP 애플리케이션에서 BullMQ 큐에 작업을 추가할 수 있는 **Queue client**를 제공합니다. 이렇게 추가된 작업은 Node.js, Python, 또는 Elixir로 작성된 워커가 처리할 수 있습니다.

{% hint style="info" %}
PHP 패키지는 Queue 클래스(프로듀서 측)만 구현합니다. PHP의 실행 모델은 장시간 실행되는 워커 프로세스에 적합하지 않기 때문에 워커는 포함되지 않습니다. 작업 처리는 Node.js, Python, 또는 Elixir 워커를 사용하세요.
{% endhint %}

### 설치

#### 옵션 1: 릴리스 다운로드(권장)

[releases page](https://github.com/taskforcesh/bullmq/releases)에서 최신 릴리스를 다운로드하고(`bullmq-php-X.X.X.zip` 파일 확인), 프로젝트에 압축 해제한 뒤 Composer를 설정하세요:

```json
{
  "repositories": [
    {
      "type": "path",
      "url": "./bullmq-php-X.X.X"
    }
  ],
  "require": {
    "taskforcesh/bullmq-php": "*"
  }
}
```

그다음 실행하세요:

```bash
composer install
```

#### 옵션 2: GitHub에서 설치(개발용)

개발 목적이거나 최신 변경 사항을 사용하려면 저장소에서 직접 설치하세요:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/taskforcesh/bullmq"
    }
  ],
  "require": {
    "taskforcesh/bullmq-php": "dev-master"
  },
  "minimum-stability": "dev",
  "prefer-stable": true
}
```

{% hint style="warning" %}
VCS에서 설치하려면 Lua 스크립트를 빌드해야 합니다. `composer install` 후, 모노레포 루트에서 다음을 실행하세요:

```bash
yarn install && yarn build && yarn copy:lua:php
```

{% endhint %}

### 요구 사항

* PHP 8.1 이상
* Redis 5.0 이상(6.2+ 권장)
* Composer

### 시작하기

다음과 같이 큐에 작업을 추가할 수 있습니다:

```php
<?php

use BullMQ\Queue;

$queue = new Queue('myQueue');

// Add a job with data to the queue
$job = $queue->add('myJob', ['foo' => 'bar']);

echo "Added job with ID: " . $job->id . "\n";

// Close when done
$queue->close();
```

### 작업 옵션

작업을 추가할 때 다양한 옵션을 전달할 수 있습니다:

```php
<?php

use BullMQ\Queue;

$queue = new Queue('myQueue');

// Delayed job (delay in milliseconds)
$job = $queue->add('sendEmail', $emailData, [
    'delay' => 60000, // Process after 60 seconds
]);

// Priority job (lower number = higher priority)
$job = $queue->add('urgent', $data, [
    'priority' => 1,
]);

// Job with custom ID
$job = $queue->add('processOrder', $orderData, [
    'jobId' => 'order-' . $orderId,
]);

// Job with retry settings
$job = $queue->add('flakyOperation', $data, [
    'attempts' => 3,
    'backoff' => [
        'type' => 'exponential',
        'delay' => 1000,
    ],
]);

// LIFO (Last In, First Out) - process newest jobs first
$job = $queue->add('task', $data, [
    'lifo' => true,
]);
```

### 여러 작업 추가하기

```php
<?php

$jobs = $queue->addBulk([
    ['name' => 'email', 'data' => ['to' => 'user1@example.com']],
    ['name' => 'email', 'data' => ['to' => 'user2@example.com']],
    ['name' => 'email', 'data' => ['to' => 'user3@example.com']],
]);
```

### 큐 관리

```php
<?php

// Get job counts
$counts = $queue->getJobCounts();
echo "Waiting: " . $counts['waiting'] . "\n";
echo "Active: " . $counts['active'] . "\n";

// Get a specific job
$job = $queue->getJob('job-id');

// Pause/Resume the queue
$queue->pause();
$queue->resume();

// Clean old jobs
$cleaned = $queue->clean(3600000, 100, 'completed'); // 1 hour grace period
```

### 상호 운용성

PHP 클라이언트로 추가한 작업은 다음 환경의 BullMQ 워커와 완전히 호환됩니다:

* **Node.js** - 공식 [BullMQ](https://www.npmjs.com/package/bullmq) 패키지 사용
* **Python** - [BullMQ Python](https://pypi.org/project/bullmq/) 패키지 사용
* **Elixir** - [BullMQ Elixir](https://hex.pm/packages/bullmq) 패키지 사용

PHP에서 추가한 작업을 처리하는 Node.js 워커 예시:

```javascript
import { Worker } from 'bullmq';

const worker = new Worker('myQueue', async job => {
  console.log(`Processing job ${job.id} with data:`, job.data);
  // Process the job...
  return { success: true };
});
```

### 연결 옵션

```php
<?php

use BullMQ\Queue;

// Custom Redis connection
$queue = new Queue('myQueue', [
    'connection' => [
        'host' => 'redis.example.com',
        'port' => 6379,
        'password' => 'your-password',
    ],
]);

// Using a Redis URI
$queue = new Queue('myQueue', [
    'connection' => 'redis://user:password@localhost:6379/0',
]);

// Custom prefix
$queue = new Queue('myQueue', [
    'prefix' => 'myapp',
]);
```

### 작업 재시도 및 승격

```php
<?php

// Retry all failed jobs
$queue->retryJobs([
    'count' => 100,      // Max jobs to retry per iteration (default: 1000)
    'state' => 'failed', // State to retry from: 'failed' or 'completed'
]);

// Promote all delayed jobs to waiting
$queue->promoteJobs(['count' => 100]);

// Get counts by priority
$counts = $queue->getCountsPerPriority([0, 1, 2, 3]);
```

{% hint style="warning" %}
**Job Scheduler 관련 참고**: 반복/예약 작업(cron 패턴)은 Node.js 측에서 `JobScheduler`를 사용해 생성해야 합니다. PHP 클라이언트는 스케줄러 관리가 아니라 개별 작업 추가를 위해 설계되었습니다.
{% endhint %}

### 추가 정보

자세한 내용은 GitHub의 [PHP README](https://github.com/taskforcesh/bullmq/tree/master/php)를 참고하세요.

