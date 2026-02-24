---
title: 'Prometheus'
description: 'BullMQ는 Prometheus로 메트릭을 내보낼 수 있는 간단한 API를 제공합니다. 사용하려면 웹 서버에 를 호출하는 엔드포인트를 만들고, Prometheus가 이 엔드포인트에서 메트릭을 스크랩하도록 설정하세요.'
---

Source URL: https://docs.bullmq.io/guide/metrics/prometheus

# Prometheus

BullMQ는 Prometheus로 메트릭을 내보낼 수 있는 간단한 API를 제공합니다. 사용하려면 웹 서버에 `exportPrometheusMetrics()`를 호출하는 엔드포인트를 만들고, Prometheus가 이 엔드포인트에서 메트릭을 스크랩하도록 설정하세요.

#### 기본 사용법

아래는 순수 Node.js를 사용하는 예시입니다:

```typescript
import http from 'http';
import { Queue } from 'bullmq';

const queue = new Queue('my-queue');

const server = http.createServer(
  async (req: http.IncomingMessage, res: http.ServerResponse) => {
    try {
      if (req.url === '/metrics' && req.method === 'GET') {
        const metrics = await queue.exportPrometheusMetrics();

        res.writeHead(200, {
          'Content-Type': 'text/plain',
          'Content-Length': Buffer.byteLength(metrics),
        });
        res.end(metrics);
      } else {
        res.writeHead(404);
        res.end('Not Found');
      }
    } catch (err: unknown) {
      res.writeHead(500);
      res.end(`Error: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  },
);

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
  console.log(`Prometheus metrics server running on port ${PORT}`);
  console.log(`Metrics available at http://localhost:${PORT}/metrics`);
});
```

다음으로 엔드포인트를 테스트하세요:

```bash
curl http://localhost:3000/metrics
```

그러면 다음과 같은 출력이 반환됩니다:

```
HELP bullmq_job_count Number of jobs in the queue by state
TYPE bullmq_job_count gauge
bullmq_job_count{queue="my-queue", state="waiting"} 5
bullmq_job_count{queue="my-queue", state="active"} 3
bullmq_job_count{queue="my-queue", state="completed"} 12
bullmq_job_count{queue="my-queue", state="failed"} 2
```

Express.js로 더 간단하게 구성하려면:

```typescript
import express from 'express';
import { Queue } from './src/queue';

const app = express();
const queue = new Queue('my-queue');

app.get('/metrics', async (req, res) => {
  try {
    const metrics = await queue.exportPrometheusMetrics();
    res.set('Content-Type', 'text/plain');
    res.send(metrics);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Prometheus metrics server running on port ${PORT}`);
  console.log(`Metrics available at http://localhost:${PORT}/metrics`);
});
```

#### 고급 사용법: 전역 변수를 레이블로 추가하기

`exportPrometheusMetrics` 함수는 선택적 `globalVariables` 파라미터도 지원합니다. 이를 통해 메트릭에 추가 레이블(예: env, server)을 포함할 수 있으며, Grafana 같은 도구에서 여러 환경(예: production 또는 staging)의 메트릭을 집계할 때 특히 유용합니다. `globalVariables` 파라미터는 키-값 쌍의 레코드를 받으며, 각 메트릭에 레이블로 추가됩니다.

#### 전역 변수 사용 예시

다음은 순수 Node.js에서 이 기능을 사용하는 방법입니다:

```typescript
import http from 'http';
import { Queue } from 'bullmq';

const queue = new Queue('my-queue');

const server = http.createServer(
  async (req: http.IncomingMessage, res: http.ServerResponse) => {
    try {
      if (req.url === '/metrics' && req.method === 'GET') {
        const globalVariables = { env: 'Production', server: '1' };
        const metrics = await queue.exportPrometheusMetrics(globalVariables);

        res.writeHead(200, {
          'Content-Type': 'text/plain',
          'Content-Length': Buffer.byteLength(metrics),
        });
        res.end(metrics);
      } else {
        res.writeHead(404);
        res.end('Not Found');
      }
    } catch (err: unknown) {
      res.writeHead(500);
      res.end(`Error: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  },
);

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
  console.log(`Prometheus metrics server running on port ${PORT}`);
  console.log(`Metrics available at http://localhost:${PORT}/metrics`);
});
```

`globalVariables = { env: 'Production', server: '1' }`인 경우 출력은 다음과 같이 바뀝니다:

```plaintext
# HELP bullmq_job_count Number of jobs in the queue by state
# TYPE bullmq_job_count gauge
bullmq_job_count{queue="my-queue", state="waiting", env="Production", server="1"} 5
bullmq_job_count{queue="my-queue", state="active", env="Production", server="1"} 3
bullmq_job_count{queue="my-queue", state="completed", env="Production", server="1"} 12
bullmq_job_count{queue="my-queue", state="failed", env="Production", server="1"} 2
```

이러한 추가 레이블을 사용하면 Prometheus 또는 Grafana에서 메트릭을 필터링하고 그룹화할 수 있어, 서로 다른 환경이나 서버를 더 쉽게 구분할 수 있습니다.

## 더 읽어보기:

* 💡 [Export Prometheus Metrics API Reference](https://api.docs.bullmq.io/classes/v5.Queue.html#exportprometheusmetrics)

