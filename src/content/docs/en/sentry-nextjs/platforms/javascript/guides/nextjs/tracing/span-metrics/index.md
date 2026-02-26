---
title: 'Sending Span Metrics | Sentry for Next.js'
description: 'To use span metrics, you must first configure tracing in your application.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics

# Sending Span Metrics | Sentry for Next.js

To use span metrics, you must first [configure tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) in your application.

Span metrics allow you to extend the default metrics that are collected by tracing and track custom performance data and debugging information within your application's traces. There are two main approaches to instrumenting metrics:

1. [Adding metrics to existing spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#adding-metrics-to-existing-spans)
2. [Creating dedicated spans with custom metrics](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#creating-dedicated-metric-spans)

## [Adding Metrics to Existing Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#adding-metrics-to-existing-spans)

You can enhance existing spans with custom metrics by adding attributes. This is useful when you want to augment automatic instrumentation or add contextual data to spans you've already created.

```javascript
const span = Sentry.getActiveSpan();
if (span) {
  // Add individual metrics
  span.setAttribute("database.rows_affected", 42);
  span.setAttribute("cache.hit_rate", 0.85);

  // Add multiple metrics at once
  span.setAttributes({
    "memory.heap_used": 1024000,
    "queue.length": 15,
    "processing.duration_ms": 127,
  });
}
```

- [Best Practices for Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#best-practices-for-span-attributes)

When adding metrics as span attributes:

* Use consistent naming conventions (for example, `category.metric_name`)
* Keep attribute names concise but descriptive
* Use appropriate data types (string, number, boolean, or an array containing only one of these types)

## [Creating Dedicated Metric Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#creating-dedicated-metric-spans)

For more detailed operations, tasks, or process tracking, you can create custom dedicated spans that focus on specific metrics or attributes that you want to track. This approach provides better discoverability and more precise span configurations, however it can also create more noise in your trace waterfall.

```javascript
Sentry.startSpan(
  {
    name: "Database Query Metrics",
    op: "db.metrics",
    attributes: {
      "db.query_type": "SELECT",
      "db.table": "users",
      "db.execution_time_ms": 45,
      "db.rows_returned": 100,
      "db.connection_pool_size": 5,
    },
  },
  () => {
    // Your database operation here
  },
);
```

For detailed examples of how to implement span metrics in common scenarios, see our [Span Metrics Examples](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md) guide.

## [Adding Metrics to All Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#adding-metrics-to-all-spans)

To consistently add metrics across all spans in your application, you can use the `beforeSendSpan` callback:

```javascript
Sentry.init({
  beforeSendSpan(span) {
    span.data = {
      ...span.data,
      "app.version": "1.2.3",
      "environment.region": "us-west-2",
    };

    return span;
  },
});
```

For detailed examples of how to implement span metrics in common scenarios, see our [Span Metrics Examples](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md) guide.

## [Span Metrics vs. Measurements](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#span-metrics-vs-measurements)

Previously, Sentry supported adding metrics to transactions using the `Sentry.setMeasurement()` API. This approach is deprecated, you should use span attributes instead.

## Pages in this section

- [Example Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md)

