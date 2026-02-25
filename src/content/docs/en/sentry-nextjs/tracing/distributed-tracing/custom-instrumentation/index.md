---
title: 'Custom Trace Propagation | Sentry for Next.js'
description: 'On this page you will learn how to manually propagate trace information into and out of your JavaScript application.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation

# Custom Trace Propagation | Sentry for Next.js

On this page you will learn how to manually propagate trace information into and out of your JavaScript application.

Trace propagation is set up automatically in this SDK. By default, outgoing HTTP requests will automatically be instrumented for you. For other cases where you may want to continue traces (for example, in a job queue or when working with websockets), you can manually extract and inject tracing information.

What is Distributed Tracing?

Distributed tracing connects and records the path of requests as they travel through the different tiers of your application architecture. If your architecture consists of multiple services that live on different sub-domains (e.g. `fe.example.com` and `api.example.com`), distributed tracing will help you follow the path of events as they move from one service to another.

This end-to-end visibility allows developers to identify bottlenecks, pinpoint the root cause of errors, and understand component interactions—turning what would be a complex debugging nightmare into a manageable process that improves system reliability and performance.

## [Manually Extracting and Injecting Distributed Tracing Information](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#manually-extracting-and-injecting-distributed-tracing-information)

You can also manually extract and inject tracing data into your application. For this, you must:

* Extract and store incoming tracing information from incoming request headers or similar.
* Inject tracing information to any outgoing requests.

To learn more about distributed tracing, see our [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/trace-propagation.md) docs.

- [Extracting Incoming Tracing Information](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#extracting-incoming-tracing-information)

You must extract and store incoming tracing information in memory for later use. Sentry provides the `continueTrace()` function to help you with this. Incoming tracing information can come from different places:

* In a web environment, it's sent with HTTP headers, for example, by another Sentry SDK used in your frontend project.
* In a job queue, it can be retrieved from meta or header variables.
* You also can pick up tracing information from environment variables.

Here's an example of how to extract and store incoming tracing information using `continueTrace()`:

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

In this example, we create a new transaction that is attached to the trace specified in the `sentry-trace` and `baggage` headers.

- [Injecting Tracing Information Into HTML](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#injecting-tracing-information-into-html)

If you're server-side rendering HTML and you use a Sentry SDK in your browser application, you can connect the backend and frontend traces by injecting your server's tracing information as `<meta>` tags into the HTML that's initially served to the browser. When the frontend SDK is initialized, it will automatically pick up the tracing information from the `<meta>` tags and continue the trace. Note, that your browser SDK needs to register `browserTracingIntegration` for this to work.

The easiest and recommended way to do this is to use the `Sentry.getTraceMetaTags()`:

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

Alternatively, if you need more control over how meta tags are generated, you can use `Sentry.getTraceData()` to get only the meta tag values and generate the meta tags yourself:

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

- [Inject Tracing Information into Outgoing Requests](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#inject-tracing-information-into-outgoing-requests)

For distributed tracing to work, the two headers that you extracted and stored in the active root span, `sentry-trace` and `baggage`, must be added to outgoing HTTP requests.

Here's an example of how to collect and inject this tracing information to outgoing requests:

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

In this example, tracing information is propagated to the project running at `https://example.com`. If this project uses a Sentry SDK, it will extract and save the tracing information for later use.

The two services are now connected with your custom distributed tracing implementation.

- [Starting a New Trace](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#starting-a-new-trace)

Available since: `v8.5.0`

In case the SDK's [default behavior](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#trace-duration) for the trace duration does not fit your needs, you can manually start a new trace that will no longer be connected to the current (distributed) trace. This means that spans or errors collected by the SDK during this new trace will not be connected to spans or errors collected before or after this new trace.

To start a new trace that remains valid throughout the duration of a callback, use `startNewTrace`:

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

Once the callback ends, the SDK will continue the previous trace (if available).

## [Verification](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#verification)

If you make outgoing requests from your project to other services, check if the headers `sentry-trace` and `baggage` are present in the request. If so, distributed tracing is working.

## [Example: Manual Instrumentation for gRPC](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#example-manual-instrumentation-for-grpc)

- [Server-Side Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#server-side-propagation)

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

- [Client-Side Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#client-side-propagation)

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

