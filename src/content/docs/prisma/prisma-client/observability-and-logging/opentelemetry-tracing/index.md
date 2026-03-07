---
title: "OpenTelemetry 추적"
description: "각 쿼리의 상세 추적으로 애플리케이션 성능 진단하기"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing

# OpenTelemetry 추적

각 쿼리의 상세 추적으로 애플리케이션 성능 진단하기

추적은 Prisma Client가 수행하는 작업을 작업 단위 수준에서 상세히 기록하며, 각 쿼리를 실행하는 데 걸린 시간도 포함합니다. 이를 통해 애플리케이션 성능을 분석하고 병목 지점을 식별할 수 있습니다. 추적은 [OpenTelemetry](https://opentelemetry.io/)를 완전히 준수하므로, 엔드투엔드 애플리케이션 추적 시스템의 일부로 사용할 수 있습니다.

추적은 Prisma ORM 프로젝트에 대해 작업 단위 수준의 매우 상세한 인사이트를 제공합니다.

데이터베이스 쿼리를 추적과 상호 연관시키기

[`@prisma/sqlcommenter-trace-context`](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/sql-comments#trace-context) 플러그인을 사용하면 SQL 쿼리에 `traceparent` 헤더를 주석 형태로 추가할 수 있습니다. 이를 통해 모니터링 도구에서 분산 추적과 데이터베이스 쿼리 간의 상관관계를 설정할 수 있습니다.

## 추적 정보

추적을 활성화하면 Prisma Client는 다음을 출력합니다:

- Prisma Client가 수행하는 각 작업(예: findMany)마다 하나의 trace.
- 각 trace에는 하나 이상의 [span](https://opentelemetry.io/docs/specs/otel/trace/api/#span)이 포함됩니다. 각 span은 직렬화 또는 데이터베이스 쿼리처럼 작업의 한 단계에 걸리는 시간을 나타냅니다. span은 트리 구조로 표현되며, 하위 span은 더 큰 상위 span 내부에서 실행이 일어나고 있음을 의미합니다.

trace에 포함되는 span의 수와 유형은 trace가 다루는 작업 유형에 따라 다르지만, 예시는 다음과 같습니다:

![데이터베이스 작업(직렬화, query engine, 데이터베이스 쿼리)에 대한 부모/자식 span을 보여주는 Prisma Client trace 구조 예시.](https://docs.prisma.io/docs/img/orm/prisma-client/observability-and-logging/trace-diagram.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

[추적 출력을 콘솔로 보낼](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#send-tracing-output-to-the-console) 수도 있고, [Jaeger](https://www.jaegertracing.io/), [Honeycomb](https://www.honeycomb.io/distributed-tracing), [Datadog](https://www.datadoghq.com/) 같은 OpenTelemetry 호환 추적 시스템에서 분석할 수도 있습니다. 이 페이지에서는 추적 출력을 Jaeger로 보내는 예시를 제공하며, Jaeger는 [로컬에서 실행](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#visualize-traces-with-jaeger)할 수 있습니다.

## 추적 출력

각 trace에 대해 Prisma Client는 일련의 span을 출력합니다. 이 span의 수와 유형은 Prisma Client 작업에 따라 달라집니다. 일반적인 Prisma trace에는 다음 span이 포함됩니다:

- `prisma:client:operation`: Prisma Client에서 데이터베이스로 갔다가 다시 돌아오는 전체 Prisma Client 작업을 나타냅니다. Prisma Client가 호출한 모델과 메서드 같은 세부 정보가 포함됩니다. Prisma 작업에 따라 다음 span 중 하나 이상을 포함합니다:
  - `prisma:client:connect`: Prisma Client가 데이터베이스에 연결하는 데 걸리는 시간을 나타냅니다.
  - `prisma:client:serialize`: Prisma Client 작업을 검증하고 query engine용 쿼리로 변환하는 데 걸리는 시간을 나타냅니다.
  - `prisma:engine:query`: query engine에서 쿼리가 수행되는 데 걸리는 시간을 나타냅니다.
    - `prisma:engine:connection`: Prisma Client가 데이터베이스 연결을 얻는 데 걸리는 시간을 나타냅니다.
    - `prisma:engine:db_query`: 데이터베이스에 대해 실행된 데이터베이스 쿼리를 나타냅니다. 태그에 쿼리가 포함되며, 쿼리 실행 시간도 포함됩니다.
    - `prisma:engine:serialize`: 데이터베이스의 원시 응답을 타입이 지정된 결과로 변환하는 데 걸리는 시간을 나타냅니다.
    - `prisma:engine:response_json_serialization`: 데이터베이스 쿼리 결과를 Prisma Client에 대한 JSON 응답으로 직렬화하는 데 걸리는 시간을 나타냅니다.

예를 들어, 다음 Prisma Client 코드가 주어졌을 때:

```
    prisma.user.findMany({
      where: {
        email: email,
      },
      include: {
        posts: true,
      },
    });
```

trace 구조는 다음과 같습니다:

- `prisma:client:operation`
  - `prisma:client:serialize`
  - `prisma:engine:query`
    - `prisma:engine:connection`
    - `prisma:engine:db_query`: 첫 번째 SQL 쿼리 또는 명령의 세부 정보...
    - `prisma:engine:db_query`: ...다음 SQL 쿼리 또는 명령의 세부 정보...
    - `prisma:engine:serialize`
    - `prisma:engine:response_json_serialization`

## 고려사항 및 사전 요구사항

애플리케이션이 [collector](https://opentelemetry.io/docs/collector/)로 많은 수의 span을 전송하면 성능에 상당한 영향을 줄 수 있습니다. 이 영향을 최소화하는 방법은 [성능 영향 줄이기](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#reduce-performance-impact)를 참고하세요.

추적을 사용하려면 다음을 수행해야 합니다:

1. [적절한 의존성 설치](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#step-1-install-up-to-date-prisma-orm-dependencies).
2. [OpenTelemetry 패키지 설치](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#step-2-install-opentelemetry-packages).
3. [애플리케이션에서 추적 등록](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#step-3-register-tracing-in-your-application).

## Prisma ORM에서 추적 시작하기

이 섹션에서는 애플리케이션에 추적을 설치하고 등록하는 방법을 설명합니다.

- 1단계. Prisma ORM 의존성 설치

`prisma`, `@prisma/client`, `@prisma/instrumentation` npm 패키지를 설치하세요. peer dependency이므로 `@opentelemetry/api` 패키지도 설치해야 합니다.

npm

pnpm

yarn

bun

```
    npm install prisma@latest --save-dev
    npm install @prisma/client@latest --save
    npm install @prisma/instrumentation@latest --save
    npm install @opentelemetry/api@latest --save
```

이전 Prisma ORM 버전에서의 추적

추적 기능은 Prisma ORM `4.2.0` 버전에서 Preview 기능으로 추가되었습니다. `4.2.0`부터 `6.1.0` 사이 버전의 Prisma ORM에서는 Prisma 스키마 파일에서 `tracing` Preview 기능을 활성화해야 합니다.

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
      previewFeatures = ["tracing"]
    }
```

- 2단계: OpenTelemetry 패키지 설치

이제 다음과 같이 적절한 OpenTelemetry 패키지를 설치합니다:

npm

pnpm

yarn

bun

```
    npm install @opentelemetry/semantic-conventions \
      @opentelemetry/exporter-trace-otlp-http \
      @opentelemetry/sdk-trace-base \
      @opentelemetry/sdk-trace-node \
      @opentelemetry/resources
```

- 3단계: 애플리케이션에서 추적 등록

다음 코드는 Prisma에서 OpenTelemetry 추적을 구성하는 두 가지 예시를 제공합니다:

1. `@opentelemetry/sdk-trace-node` 사용(기존 예시): 추적 설정을 세밀하게 제어할 수 있습니다.
2. `@opentelemetry/sdk-node` 사용: 더 단순한 구성을 제공하며 OpenTelemetry의 JavaScript 시작 가이드와도 일치합니다.

---

#

- `@opentelemetry/sdk-trace-node` 사용 옵션 1

이 설정은 instrumentation과 추적을 세밀하게 제어할 수 있게 해줍니다. 이 구성은 애플리케이션에 맞게 사용자 지정해야 합니다. 이 접근 방식은 간결하며, Honeycomb, Jaeger, Datadog 같은 OTLP 호환 백엔드로 trace를 빠르게 전송하려는 사용자에게 더 쉽습니다.

```
    // Imports
    import { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } from "@opentelemetry/semantic-conventions";
    import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";
    import { SimpleSpanProcessor } from "@opentelemetry/sdk-trace-base";
    import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";
    import { PrismaInstrumentation, registerInstrumentations } from "@prisma/instrumentation";
    import { resourceFromAttributes } from "@opentelemetry/resources";

    // Configure the trace provider
    const provider = new NodeTracerProvider({
      resource: resourceFromAttributes({
        [ATTR_SERVICE_NAME]: "example application", // Replace with your service name
        [ATTR_SERVICE_VERSION]: "0.0.1", // Replace with your service version
      }),
      spanProcessors: [
        // Configure how spans are processed and exported. In this case, we're sending spans
        // as we receive them to an OTLP-compatible collector (e.g., Jaeger).
        new SimpleSpanProcessor(new OTLPTraceExporter()),
      ],
    });

    // Register your auto-instrumentors
    registerInstrumentations({
      tracerProvider: provider,
      instrumentations: [new PrismaInstrumentation()],
    });

    // Register the provider globally
    provider.register();
```

이 접근 방식은 최대한의 유연성을 제공하지만 추가 구성 단계가 필요할 수 있습니다.

#

- `@opentelemetry/sdk-node` 사용 옵션 2

많은 사용자, 특히 초보자의 경우 `NodeSDK` 클래스는 일반적인 기본값을 하나의 통합 구성으로 묶어 OpenTelemetry 설정을 단순화합니다.

```
    // Imports
    import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-proto";
    import { NodeSDK } from "@opentelemetry/sdk-node";
    import { PrismaInstrumentation } from "@prisma/instrumentation";

    // Configure the OTLP trace exporter
    const traceExporter = new OTLPTraceExporter({
      url: "https://api.honeycomb.io/v1/traces", // Replace with your collector's endpoint
      headers: {
        "x-honeycomb-team": "HONEYCOMB_API_KEY", // Replace with your Honeycomb API key or collector auth header
      },
    });

    // Initialize the NodeSDK
    const sdk = new NodeSDK({
      serviceName: "my-service-name", // Replace with your service name
      traceExporter,
      instrumentations: [new PrismaInstrumentation()],
    });

    // Start the SDK
    sdk.start();

    // Handle graceful shutdown
    process.on("SIGTERM", async () => {
      try {
        await sdk.shutdown();
        console.log("Tracing shut down successfully");
      } catch (err) {
        console.error("Error shutting down tracing", err);
      } finally {
        process.exit(0);
      }
    });
```

다음 경우 `NodeSDK` 접근 방식을 선택하세요:

- OpenTelemetry를 시작하는 단계이며 간소화된 설정을 원할 때.
- 최소한의 보일러플레이트로 추적을 빠르게 통합해야 할 때.
- Honeycomb, Jaeger, Datadog 같은 OTLP 호환 추적 백엔드를 사용할 때.

다음 경우 `NodeTracerProvider` 접근 방식을 선택하세요:

- span이 생성, 처리, 내보내지는 방식을 세부적으로 제어해야 할 때.
- 사용자 지정 span processor 또는 exporter를 사용할 때.
- 애플리케이션에 특정 instrumentation 또는 샘플링 전략이 필요할 때.

OpenTelemetry는 매우 높은 구성 가능성을 제공합니다. resource 속성, 어떤 구성 요소를 instrumentation할지, span을 어떻게 처리할지, span을 어디로 보낼지를 사용자 지정할 수 있습니다.

메트릭까지 포함된 전체 예시는 [이 샘플 애플리케이션](https://github.com/garrensmith/prisma-metrics-sample)에서 확인할 수 있습니다.

## 추적 활용 방법

- Jaeger로 trace 시각화

[Jaeger](https://www.jaegertracing.io/)는 trace를 시각화하는 데 사용할 수 있는 무료 오픈 소스 OpenTelemetry collector 및 대시보드입니다.

다음 스크린샷은 trace 시각화 예시를 보여줍니다:

![Jaeger UI](https://docs.prisma.io/docs/img/orm/prisma-client/observability-and-logging/jaeger.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

Jaeger를 로컬에서 실행하려면 다음 [Docker](https://www.docker.com/) 명령을 사용하세요:

```
    docker run --rm --name jaeger -d -e COLLECTOR_OTLP_ENABLED=true -p 16686:16686 -p 4318:4318 jaegertracing/all-in-one:latest
```

이제 `http://localhost:16686/`에서 추적 대시보드를 확인할 수 있습니다. 추적을 활성화한 상태로 애플리케이션을 사용하면 이 대시보드에서 trace가 보이기 시작합니다.

- 추적 출력을 콘솔로 보내기

다음 예시는 `@opentelemetry/sdk-trace-base`의 `ConsoleSpanExporter`를 사용해 추적 출력을 콘솔로 보냅니다.

```
    // Imports
    import { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } from "@opentelemetry/semantic-conventions";
    import { ConsoleSpanExporter, SimpleSpanProcessor } from "@opentelemetry/sdk-trace-base";
    import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";
    import { AsyncHooksContextManager } from "@opentelemetry/context-async-hooks";
    import * as api from "@opentelemetry/api";
    import { PrismaInstrumentation, registerInstrumentations } from "@prisma/instrumentation";
    import { resourceFromAttributes } from "@opentelemetry/resources";

    // Export the tracing
    export function otelSetup() {
      const contextManager = new AsyncHooksContextManager().enable();

      api.context.setGlobalContextManager(contextManager);

      //Configure the console exporter
      const consoleExporter = new ConsoleSpanExporter();

      // Configure the trace provider
      const provider = new NodeTracerProvider({
        resource: resourceFromAttributes({
          [ATTR_SERVICE_NAME]: "example application", // Replace with your service name
          [ATTR_SERVICE_VERSION]: "0.0.1", // Replace with your service version
        }),
        spanProcessors: [
          // Configure how spans are processed and exported. In this case, we're sending spans
          // as we receive them to the console
          new SimpleSpanProcessor(consoleExporter),
        ],
      });

      // Register your auto-instrumentors
      registerInstrumentations({
        tracerProvider: provider,
        instrumentations: [new PrismaInstrumentation()],
      });

      // Register the provider
      provider.register();
    }
```

- 대화형 트랜잭션 추적

대화형 트랜잭션을 수행하면 [표준 span](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#trace-output) 외에 다음 span이 추가로 표시됩니다:

- `prisma:client:transaction`: `prisma` span을 감싸는 [root span](https://opentelemetry.io/docs/concepts/observability-primer/#distributed-traces)입니다.

예시로, 다음 Prisma 스키마를 보겠습니다:

schema.prisma

```
    generator client {
      provider        = "prisma-client"
      output          = "./generated"
    }

    datasource db {
      provider = "postgresql"
    }

    model User {
      id    Int    @id @default(autoincrement())
      email String @unique
    }

    model Audit {
      id     Int    @id
      table  String
      action String
    }
```

다음 대화형 트랜잭션이 주어졌을 때:

```
    await prisma.$transaction(async (tx) => {
      const user = await tx.user.create({
        data: {
          email: email,
        },
      });

      await tx.audit.create({
        data: {
          table: "user",
          action: "create",
          id: user.id,
        },
      });

      return user;
    });
```

trace 구조는 다음과 같습니다:

- `prisma:client:transaction`
- `prisma:client:connect`
- `prisma:engine:itx_runner`
  - `prisma:engine:connection`
  - `prisma:engine:db_query`
  - `prisma:engine:itx_query_builder`
    - `prisma:engine:db_query`
    - `prisma:engine:db_query`
    - `prisma:engine:serialize`
  - `prisma:engine:itx_query_builder`
    - `prisma:engine:db_query`
    - `prisma:engine:db_query`
    - `prisma:engine:serialize`
- `prisma:client:operation`
  - `prisma:client:serialize`
- `prisma:client:operation`
  - `prisma:client:serialize`

* 계측 추가하기

OpenTelemetry의 큰 장점 중 하나는 애플리케이션 코드에 최소한의 변경만으로 더 많은 계측을 추가할 수 있다는 점입니다.

예를 들어 HTTP 및 [ExpressJS](https://expressjs.com/) 트레이싱을 추가하려면, OpenTelemetry 설정에 다음 계측을 추가하세요. 이러한 계측은 전체 요청-응답 수명 주기에 대한 스팬을 추가합니다. 이 스팬을 통해 HTTP 요청에 걸리는 시간을 확인할 수 있습니다.

```
    // Imports
    import { ExpressInstrumentation } from "@opentelemetry/instrumentation-express";
    import { HttpInstrumentation } from "@opentelemetry/instrumentation-http";

    // Register your auto-instrumentors
    registerInstrumentations({
      tracerProvider: provider,
      instrumentations: [
        new HttpInstrumentation(),
        new ExpressInstrumentation(),
        new PrismaInstrumentation(),
      ],
    });
```

사용 가능한 계측의 전체 목록은 [OpenTelemetry Registry](https://opentelemetry.io/ecosystem/registry/?language=js&component=instrumentation)를 참고하세요.

- 리소스 속성 사용자 지정

리소스 속성을 애플리케이션에 더 구체적으로 맞게 변경하면 애플리케이션의 트레이스가 그룹화되는 방식을 조정할 수 있습니다:

```
    const provider = new NodeTracerProvider({
      resource: new Resource({
        [ATTR_SERVICE_NAME]: "weblog",
        [ATTR_SERVICE_VERSION]: "1.0.0",
      }),
    });
```

공통 리소스 속성을 표준화하기 위한 작업이 진행 중입니다. 가능하면 [표준 속성 이름](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/general/trace.md)을 따르는 것이 좋습니다.

- 성능 영향 줄이기

애플리케이션이 많은 수의 스팬을 수집기로 전송하면 성능에 상당한 영향을 줄 수 있습니다. 다음 접근 방식으로 이 영향을 줄일 수 있습니다:

- `BatchSpanProcessor` 사용하기
- 수집기로 전송하는 스팬 수 줄이기

#

- `BatchSpanProcessor`를 사용해 배치로 트레이스 전송하기

프로덕션 환경에서는 OpenTelemetry의 `BatchSpanProcessor`를 사용해 스팬을 하나씩이 아니라 배치로 수집기에 전송할 수 있습니다. 하지만 개발 및 테스트 중에는 스팬을 배치로 전송하고 싶지 않을 수 있습니다. 이런 경우에는 `SimpleSpanProcessor`를 사용하는 편이 더 적합할 수 있습니다.

다음과 같이 환경에 따라 적절한 스팬 프로세서를 사용하도록 트레이싱 설정을 구성할 수 있습니다:

```
    import { SimpleSpanProcessor, BatchSpanProcessor } from "@opentelemetry/sdk-trace-base";
    import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";

    const spanProcessors = [];
    if (process.env.NODE_ENV === "production") {
      spanProcessors.push(new BatchSpanProcessor(otlpTraceExporter));
    } else {
      spanProcessors.push(new SimpleSpanProcessor(otlpTraceExporter));
    }

    const provider = new NodeTracerProvider({
      spanProcessors,
      // ...other configurations
    });
```

#

- 샘플링으로 수집기에 전송하는 스팬 수 줄이기

성능 영향을 줄이는 또 다른 방법은 [확률 샘플링 사용하기](https://opentelemetry.io/docs/specs/otel/trace/tracestate-probability-sampling/)를 통해 수집기에 전송하는 스팬 수를 줄이는 것입니다. 이렇게 하면 트레이싱 수집 비용은 줄이면서도 애플리케이션에서 어떤 일이 일어나고 있는지에 대한 좋은 대표성을 유지할 수 있습니다.

구현 예시는 다음과 같습니다:

```
    import { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } from "@opentelemetry/semantic-conventions";
    import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";
    import { TraceIdRatioBasedSampler } from "@opentelemetry/core";
    import { resourceFromAttributes } from "@opentelemetry/resources";

    const provider = new NodeTracerProvider({
      sampler: new TraceIdRatioBasedSampler(0.1),
      resource: resourceFromAttributes({
        // we can define some metadata about the trace resource
        [ATTR_SERVICE_NAME]: "test-tracing-service",
        [ATTR_SERVICE_VERSION]: "1.0.0",
      }),
    });
```

## 트레이싱 문제 해결

- 트레이스가 표시되지 않아요

트레이싱 설정 순서는 중요합니다. 애플리케이션에서는 계측된 의존성을 import하기 전에 트레이싱과 계측을 먼저 등록해야 합니다. 예를 들어:

```
    import { registerTracing } from "./tracing";

    registerTracing({
      name: "tracing-example",
      version: "0.0.1",
    });

    // You must import any dependencies after you register tracing.
    import { PrismaClient } from "../prisma/generated/client";
    import async from "express-async-handler";
    import express from "express";
```
