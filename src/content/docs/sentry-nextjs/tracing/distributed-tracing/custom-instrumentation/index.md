---
title: '사용자 지정 Trace 전파 | Next.js용 Sentry'
description: '이 페이지에서는 JavaScript 애플리케이션 안팎으로 trace 정보를 수동으로 전파하는 방법을 배웁니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation

# 사용자 지정 Trace 전파 | Next.js용 Sentry

이 페이지에서는 JavaScript 애플리케이션 안팎으로 trace 정보를 수동으로 전파하는 방법을 배웁니다.

이 SDK에서는 trace 전파가 자동으로 설정됩니다. 기본적으로 나가는 HTTP 요청은 자동으로 계측됩니다. trace를 계속 이어가고 싶은 다른 경우(예: 작업 큐 또는 websockets 사용 시)에는 tracing 정보를 수동으로 추출하고 주입할 수 있습니다.

분산 추적이란 무엇인가요?

분산 추적은 요청이 애플리케이션 아키텍처의 서로 다른 계층을 통과할 때 그 경로를 연결하고 기록합니다. 아키텍처가 서로 다른 서브도메인(예: `fe.example.com` 및 `api.example.com`)에 있는 여러 서비스로 구성되어 있다면, 분산 추적을 통해 이벤트가 한 서비스에서 다른 서비스로 이동하는 경로를 따라갈 수 있습니다.

이러한 엔드 투 엔드 가시성을 통해 개발자는 병목 지점을 식별하고, 오류의 근본 원인을 정확히 찾아내며, 컴포넌트 간 상호작용을 이해할 수 있습니다. 즉, 복잡한 디버깅 악몽을 시스템 신뢰성과 성능을 개선하는 관리 가능한 프로세스로 바꿔줍니다.

## [분산 추적 정보 수동 추출 및 주입](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#manually-extracting-and-injecting-distributed-tracing-information)

애플리케이션에 tracing 데이터를 수동으로 추출하고 주입할 수도 있습니다. 이를 위해서는 다음이 필요합니다.

* 들어오는 요청 헤더 등에서 들어오는 tracing 정보를 추출해 저장합니다.
* 나가는 모든 요청에 tracing 정보를 주입합니다.

분산 추적에 대해 더 알아보려면 [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/trace-propagation.md) 문서를 참고하세요.

- [들어오는 tracing 정보 추출](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#extracting-incoming-tracing-information)

나중에 사용할 수 있도록 들어오는 tracing 정보를 메모리에 추출해 저장해야 합니다. Sentry는 이를 돕기 위해 `continueTrace()` 함수를 제공합니다. 들어오는 tracing 정보는 다양한 위치에서 올 수 있습니다.

* 웹 환경에서는 HTTP headers와 함께 전송되며, 예를 들어 프런트엔드 프로젝트에서 사용하는 다른 Sentry SDK가 보낼 수 있습니다.
* 작업 큐에서는 meta 또는 header 변수에서 가져올 수 있습니다.
* 환경 변수에서도 tracing 정보를 가져올 수 있습니다.

다음은 `continueTrace()`를 사용해 들어오는 tracing 정보를 추출하고 저장하는 예시입니다.

```javascript
const http = require("http");

http.createServer((request, response) => {
  const sentryTrace = request.headers["sentry-trace"];
  const baggage = request.headers["baggage"];

  Sentry.continueTrace({ sentryTrace, baggage }, () => {
    Sentry.startSpan(
      {,
        name: "my request",
        op: "http.server",
      },
      () => {
        // Your API code...
      }
    );
  });
});
```

이 예시에서는 `sentry-trace` 및 `baggage` headers에 지정된 trace에 연결된 새 transaction을 생성합니다.

- [HTML에 tracing 정보 주입](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#injecting-tracing-information-into-html)

서버 사이드에서 HTML을 렌더링하고 브라우저 애플리케이션에서 Sentry SDK를 사용하는 경우, 브라우저에 처음 전달되는 HTML에 서버의 tracing 정보를 `<meta>` tags로 주입해 백엔드와 프런트엔드 trace를 연결할 수 있습니다. 프런트엔드 SDK가 초기화되면 `<meta>` tags에서 tracing 정보를 자동으로 가져와 trace를 이어갑니다. 이 기능이 동작하려면 브라우저 SDK에서 `browserTracingIntegration`을 등록해야 합니다.

가장 쉽고 권장되는 방법은 `Sentry.getTraceMetaTags()`를 사용하는 것입니다.

`index.js`

```javascript
function renderHtml() {
  return `
    <html>
      <head>

        ${Sentry.getTraceMetaTags()}

      </head>
      <body>
        <!-- Your HTML content -->
      </body>
    </html>
  `;
}
```

또는 meta tags 생성 방식을 더 세밀하게 제어해야 한다면, `Sentry.getTraceData()`를 사용해 meta tag 값만 가져오고 meta tags는 직접 생성할 수 있습니다.

`index.js`

```javascript
function renderHtml() {

  const metaTagValues = Sentry.getTraceData();

  return `
    <html>
      <head>

        <meta name="sentry-trace" content="${metaTagValues["sentry-trace"]}">
        <meta name="baggage" content="${metaTagValues.baggage}">

      </head>
      <body>
        <!-- Your HTML content -->
      </body>
    </html>
  `;
}
```

- [나가는 요청에 tracing 정보 주입](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#inject-tracing-information-into-outgoing-requests)

분산 추적이 동작하려면 활성 루트 span에 추출 및 저장해 둔 두 header인 `sentry-trace`와 `baggage`를 나가는 HTTP 요청에 추가해야 합니다.

다음은 이 tracing 정보를 수집해 나가는 요청에 주입하는 예시입니다.

```javascript
const traceData = Sentry.getTraceData();
const sentryTraceHeader = traceData["sentry-trace"];
const sentryBaggageHeader = traceData["baggage"];

// Make outgoing request
fetch("https://example.com", {
  method: "GET",
  headers: {
    baggage: sentryBaggageHeader,
    "sentry-trace": sentryTraceHeader,
  },
}).then((response) => {
  // ...
});
```

이 예시에서는 tracing 정보가 `https://example.com`에서 실행 중인 프로젝트로 전파됩니다. 이 프로젝트가 Sentry SDK를 사용한다면 tracing 정보를 추출해 나중에 사용할 수 있도록 저장합니다.

이제 두 서비스가 사용자 지정 분산 추적 구현으로 연결되었습니다.

- [새 trace 시작](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#starting-a-new-trace)

사용 가능 버전: `v8.5.0`

trace 지속 시간에 대한 SDK의 [기본 동작](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#trace-duration)이 요구 사항에 맞지 않는 경우, 현재 (분산) trace와 더 이상 연결되지 않는 새 trace를 수동으로 시작할 수 있습니다. 즉, 이 새 trace 동안 SDK가 수집한 spans 또는 errors는 이 trace의 이전이나 이후에 수집된 spans 또는 errors와 연결되지 않습니다.

콜백 실행 시간 동안 유효한 새 trace를 시작하려면 `startNewTrace`를 사용하세요.

```javascript
myButton.addEventListener("click", async () => {

  Sentry.startNewTrace(() => {
    Sentry.startSpan(
      { op: "ui.interaction.click", name: "fetch click" },
      async () => {
        await fetch("http://example.com");
      },
    );
  });

});
```

콜백이 끝나면 SDK는 이전 trace(가능한 경우)를 계속 이어갑니다.

## [검증](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#verification)

프로젝트에서 다른 서비스로 나가는 요청을 보낸다면 요청에 `sentry-trace`와 `baggage` headers가 있는지 확인하세요. 있다면 분산 추적이 정상 동작하는 것입니다.

## [예시: gRPC 수동 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#example-manual-instrumentation-for-grpc)

- [서버 사이드 전파](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#server-side-propagation)

```javascript
// gRPC server interceptor with Sentry instrumentation
function sentryInterceptor(methodDescriptor, nextCall) {
  // Extract Sentry trace headers from the incoming metadata
  const metadata = nextCall.metadata.getMap();
  const sentryTrace = metadata["sentry-trace"];
  const baggage = metadata["baggage"];

  return new grpc.ServerInterceptingCall(nextCall, {
    start: (next) => {
      // Continue the trace using the extracted context
      Sentry.continueTrace({ sentryTrace, baggage }, () => {
        // Create a manual span that won't auto-close until we end it
        Sentry.startSpanManual(
          {
            name: methodDescriptor.path,
            op: "grpc.server",
            forceTransaction: true, // Make this a transaction in the Sentry UI
            attributes: {
              "grpc.method": methodDescriptor.path,
              "grpc.service": methodDescriptor.service.serviceName,
              "grpc.status_code": grpc.status.OK,
            },
          },
          (span) => {
            // Store the span for later use
            nextCall.sentrySpan = span;
            next();
          },
        );
      });
    },
    sendStatus: (status, next) => {
      const span = nextCall.sentrySpan;
      if (span) {
        // Update status based on the gRPC result
        if (status.code !== grpc.status.OK) {
          span.setStatus({ code: 2, message: "error" });
          span.setAttribute("grpc.status_code", status.code);
          span.setAttribute("grpc.status_description", status.details);
        }
        // End the span when the call completes
        span.end();
      }
      next(status);
    },
  });
}

// Add the interceptor to your gRPC server
const server = new grpc.Server({
  interceptors: [sentryInterceptor],
});

// In your service implementation, use the active span
const serviceImplementation = {
  myMethod: async (call, callback) => {
    try {
      const span = call.call?.nextCall?.sentrySpan;

      // Use withActiveSpan to make the span active during service execution
      await Sentry.withActiveSpan(span, async () => {
        // Create child spans for operations within the service
        await Sentry.startSpan(
          { name: "database.query", op: "db" },
          async (childSpan) => {
            // Database operations here
            const result = await database.query("SELECT * FROM table");
            childSpan.setAttribute("db.rows_affected", result.rowCount);
          },
        );

        callback(null, { result: "success" });
      });
    } catch (error) {
      // Capture the error with the current span as context
      Sentry.captureException(error);
      callback(error);
    }
  },
};
```

- [클라이언트 사이드 전파](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#client-side-propagation)

```javascript
function createGrpcClient() {
  // Create client with interceptor
  return new MyServiceClient(address, grpc.credentials.createInsecure(), {
    interceptors: [
      (options, nextCall) => {
        return new grpc.InterceptingCall(nextCall(options), {
          start: (callMetadata, listener, next) => {
            // `callMetadata` is the metadata object for the outgoing gRPC call.
            // We will add our Sentry tracing headers to this object.

            // Get current trace information from Sentry
            const traceData = Sentry.getTraceData();

            // Add Sentry trace and baggage headers to the call's metadata
            if (traceData) {
              callMetadata.set("sentry-trace", traceData["sentry-trace"]);
              callMetadata.set("baggage", traceData["baggage"]);
            }

            // Proceed with the call, now including the Sentry headers in its metadata
            next(callMetadata, listener);
          },
        });
      },
    ],
  });
}
```

