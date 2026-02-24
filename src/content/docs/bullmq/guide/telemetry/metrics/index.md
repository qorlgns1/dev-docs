---
title: '메트릭 활성화'
description: 'BullMQ는 트레이스뿐만 아니라 OpenTelemetry를 통한 메트릭 수집도 지원합니다. 메트릭은 완료/실패한 작업 수, 처리 시간과 같이 작업 처리에 대한 정량적 데이터를 제공합니다.'
---

Source URL: https://docs.bullmq.io/guide/telemetry/metrics

# 메트릭

BullMQ는 트레이스뿐만 아니라 OpenTelemetry를 통한 메트릭 수집도 지원합니다. 메트릭은 완료/실패한 작업 수, 처리 시간과 같이 작업 처리에 대한 정량적 데이터를 제공합니다.

## 메트릭 활성화

메트릭 수집을 활성화하려면 `BullMQOtel` 인스턴스를 생성할 때 `enableMetrics` 옵션을 전달하세요:

```typescript
import { Queue } from 'bullmq';
import { BullMQOtel } from 'bullmq-otel';

const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  meterName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});

const queue = new Queue('myQueue', {
  connection: {
    host: '127.0.0.1',
    port: 6379,
  },
  telemetry,
});
```

```typescript
import { Worker } from 'bullmq';
import { BullMQOtel } from 'bullmq-otel';

const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  meterName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});

const worker = new Worker(
  'myQueue',
  async job => {
    return 'some value';
  },
  {
    connection: {
      host: '127.0.0.1',
      port: 6379,
    },
    telemetry,
  },
);
```

## 사용 가능한 메트릭

BullMQ는 다음 메트릭을 자동으로 기록합니다:

### 카운터

| Metric Name                    | Description                                                    |
| ------------------------------ | -------------------------------------------------------------- |
| `bullmq.jobs.completed`        | 성공적으로 완료된 작업 수                                     |
| `bullmq.jobs.failed`           | 실패한 작업 수(모든 재시도 소진 후)                           |
| `bullmq.jobs.delayed`          | 지연 상태로 이동한 작업 수(재시도 지연 포함)                  |
| `bullmq.jobs.retried`          | 즉시 재시도된 작업 수                                          |
| `bullmq.jobs.waiting`          | 대기 상태로 다시 이동한 작업 수                                |
| `bullmq.jobs.waiting_children` | waiting-children 상태로 이동한 작업 수                         |

### 히스토그램

| Metric Name           | Description             | Unit         |
| --------------------- | ----------------------- | ------------ |
| `bullmq.job.duration` | 작업 처리 시간          | milliseconds |

## 메트릭 속성

모든 메트릭에는 필터링 및 그룹화를 위한 다음 속성이 포함됩니다:

| Attribute           | Description                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| `bullmq.queue.name` | 큐 이름                                                                            |
| `bullmq.job.name`   | 작업 이름                                                                          |
| `bullmq.job.status` | 작업 상태(completed, failed, delayed, retried, waiting, waiting-children)         |

## 구성 옵션

`BullMQOtel` 생성자는 다음 옵션을 받습니다:

```typescript
interface BullMQOtelOptions {
  /**
   * Name for the tracer (default: 'bullmq')
   */
  tracerName?: string;

  /**
   * Name for the meter (default: 'bullmq')
   */
  meterName?: string;

  /**
   * Version string for both tracer and meter
   */
  version?: string;

  /**
   * Enable metrics collection. When true, a meter will be created
   * to record job metrics like completed/failed counts and durations.
   * @default false
   */
  enableMetrics?: boolean;
}
```

## 사용자 정의 메트릭 옵션

`BullMQOtel`을 사용하면 Worker 또는 Queue에 telemetry 인스턴스를 전달하기 전에 사용자 정의 옵션으로 카운터와 히스토그램을 미리 구성할 수 있습니다. 메트릭이 사용자 정의 옵션으로 생성되면 BullMQ는 이를 재사용하며, 내부적으로 정의된 기본 옵션은 무시됩니다.

이 기능은 메트릭 설명, 단위 또는 기타 OpenTelemetry 메트릭 옵션을 사용자 정의하려는 경우 유용합니다:

```typescript
import { BullMQOtel } from 'bullmq-otel';
import { Worker } from 'bullmq';

const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  meterName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});

// Pre-configure a counter with custom options
// This will be reused by BullMQ, ignoring its default options
telemetry.meter.createCounter('bullmq.jobs.completed', {
  description: 'Custom description for completed jobs',
  unit: '1',
});

// Pre-configure the duration histogram with custom options
telemetry.meter.createHistogram('bullmq.job.duration', {
  description: 'Custom job processing duration',
  unit: 's', // Using seconds instead of default milliseconds
});

const worker = new Worker(
  'myQueue',
  async job => {
    return 'some value';
  },
  {
    connection: {
      host: '127.0.0.1',
      port: 6379,
    },
    telemetry,
  },
);
```

{% hint style="info" %}
`BullMQOTelMeter`는 생성된 모든 카운터와 히스토그램을 이름별로 캐시합니다. BullMQ 내부에서 동일한 이름으로 `createCounter` 또는 `createHistogram`을 호출하면 캐시된 인스턴스가 반환되며, 결과적으로 BullMQ가 전달한 기본 옵션은 무시됩니다.
{% endhint %}

## 하위 호환성

기존 생성자 시그니처는 하위 호환성을 위해 여전히 지원됩니다:

```typescript
// Old style (traces only)
const telemetry = new BullMQOtel('my-app', '1.0.0');

// New style with options object (traces + optional metrics)
const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  version: '1.0.0',
  enableMetrics: true,
});
```

## 메트릭 내보내기

관측성 백엔드로 메트릭을 내보내려면 OpenTelemetry 메트릭 exporter를 구성해야 합니다. 다음은 OTLP exporter를 사용하는 예시입니다:

```typescript
import {
  MeterProvider,
  PeriodicExportingMetricReader,
} from '@opentelemetry/sdk-metrics';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';
import { metrics } from '@opentelemetry/api';

// Configure the metrics exporter
const metricExporter = new OTLPMetricExporter({
  url: 'http://localhost:4318/v1/metrics',
});

const meterProvider = new MeterProvider({
  readers: [
    new PeriodicExportingMetricReader({
      exporter: metricExporter,
      exportIntervalMillis: 10000, // Export every 10 seconds
    }),
  ],
});

// Set the global meter provider
metrics.setGlobalMeterProvider(meterProvider);

// Now create your BullMQ instances with metrics enabled
const telemetry = new BullMQOtel({
  tracerName: 'my-app',
  enableMetrics: true,
});
```

{% hint style="info" %}
telemetry를 활성화한 BullMQ 인스턴스를 생성하기 전에 meter provider를 먼저 설정해야 합니다.
{% endhint %}

