---
title: 'Sampling | Sentry for Next.js'
description: "Adding Sentry to your app gives you a great deal of very valuable information about errors and performance you wouldn't otherwise get. And lots of inf..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling

# Sampling | Sentry for Next.js

Adding Sentry to your app gives you a great deal of very valuable information about errors and performance you wouldn't otherwise get. And lots of information is good -- as long as it's the right information, at a reasonable volume.

## [Sampling Error Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#sampling-error-events)

To send a representative sample of your errors to Sentry, set the `sampleRate` option in your SDK configuration to a number between `0` (0% of errors sent) and `1` (100% of errors sent). This is a static rate, which will apply equally to all errors. For example, to sample 25% of your errors:

```javascript
Sentry.init({ sampleRate: 0.25 });
```

The error sample rate defaults to `1`, meaning all errors are sent to Sentry.

Changing the error sample rate requires re-deployment. In addition, setting an SDK sample rate limits visibility into the source of events. Setting a rate limit for your project (which only drops events when volume is high) may better suit your needs.

## [Sampling Transaction Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#sampling-transaction-events)

We recommend sampling your transactions for two reasons:

1. Capturing a single trace involves minimal overhead, but capturing traces for *every* page load or *every* API request may add an undesirable load to your system.
2. Enabling sampling allows you to better manage the number of events sent to Sentry, so you can tailor your volume to your organization's needs.

Choose a sampling rate with the goal of finding a balance between performance and volume concerns with data accuracy. You don't want to collect *too* much data, but you want to collect sufficient data from which to draw meaningful conclusions. If you’re not sure what rate to choose, start with a low value and gradually increase it as you learn more about your traffic patterns and volume.

## [Configuring the Transaction Sample Rate](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#configuring-the-transaction-sample-rate)

The Sentry SDKs have two configuration options to control the volume of transactions sent to Sentry, allowing you to take a representative sample:

1. Uniform sample rate (`tracesSampleRate`):

   * Provides an even cross-section of transactions, no matter where in your app or under what circumstances they occur.
   * Uses default [inheritance](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#inheritance) and [precedence](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#precedence) behavior

2. Sampling function (`tracesSampler`) which:

   * Samples different transactions at different rates
   * [Filters](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md) out some transactions entirely
   * Modifies default [precedence](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#precedence) and [inheritance](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#inheritance) behavior

By default, none of these options are set, meaning no transactions will be sent to Sentry. You must set either one of the options to start sending transactions.

- [Setting a Uniform Sample Rate](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#setting-a-uniform-sample-rate)

To do this, set the `tracesSampleRate` option in your `Sentry.init()` to a number between 0 and 1. With this option set, every transaction created will have that percentage chance of being sent to Sentry. (So, for example, if you set `tracesSampleRate` to `0.5`, approximately 50% of your transactions will get recorded and sent.) That looks like this:

```javascript
Sentry.init({
  // ...

  tracesSampleRate: 0.5,
});
```

- [Setting a Sampling Function](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#setting-a-sampling-function)

To use the sampling function, set the `tracesSampler` option in your `Sentry.init()` to a function that will accept a `samplingContext` object and return a sample rate between 0 and 1. For example:

```typescript
// The shape of samplingContext that is passed to the tracesSampler function
interface SamplingContext {
  // Name of the span
  name: string;
  // Initial attributes of the span
  attributes: SpanAttributes | undefined;
  // If the parent span was sampled - undefined if there is no incoming trace
  parentSampled: boolean | undefined;
  // Sample rate that is coming from the incoming trace - undefined if there is no incoming trace
  parentSampleRate: number | undefined;
}

Sentry.init({
  // ...

  tracesSampler: ({ name, attributes, inheritOrSampleWith }) => {
    // Do not sample health checks ever
    if (name.includes("healthcheck")) {
      return 0;
    }

    // These are important - take a big sample
    if (name.includes("auth")) {
      return 1;
    }

    // These are less important or happen much more frequently - only take 1%
    if (name.includes("comment")) {
      return 0.01;
    }

    // Otherwise, inherit the sample sampling decision of the incoming trace, or use a fallback sampling rate.
    return inheritOrSampleWith(0.5);
  },
});
```

##### parentSampleRate

The `inheritOrSampleWith` sampling context utility was introduced in version 9 of the SDK. To inherit sampling decisions in earlier versions of the SDK, use the `parentSampled` sampling context.

Going forward, using `inheritOrSampleWith()` is strongly encouraged over using `parentSampled`, because it allows for deterministic sampling and metric extrapolation for downstream traces.

For convenience, the function can also return a boolean. Returning `true` is equivalent to returning `1`, and will guarantee the transaction will be sent to Sentry. Returning `false` is equivalent to returning `0` and will guarantee the transaction will **not** be sent to Sentry. Note that sampling decisions will be inherited for downstream services if you have set up distributed tracing.

## [Sampling Context Data](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#sampling-context-data)

When a span is started, the `tracesSampler` function will automatically receive the span `name` and the initial span `attributes` to use in its sampling decision. Additionally, it will also receive a `parentSampled` boolean indicating whether the parent span was sampled. This data can be used to make a more informed decision about whether to sample the span.

```javascript
Sentry.startSpan({
  name: "Search from navbar",
  op: "search",
  attributes: {
    testGroup: "A3",
    treatmentName: "eager load",
  },
});

// Will result in `tracesSampler` receiving:
function tracesSampler(samplingContext) {
  /*
  samplingContext = {
    name: "Search from navbar",
    attributes: {
      testGroup: 'A3',
      treatmentName: 'eager load',
    },
  }
  */

  // Do not sample this specific span
  return name !== "Search from navbar";
}
```

Please note that the `name` passed to `tracesSampler` may not be the exact same name that is eventually sent to Sentry. The name may be updated during the lifetime of the span, but the `name` passed to `tracesSampler` will always be the initial name. For example, the `name` for `http.server` spans will usually not be parametrized yet when passed to `tracesSampler`, so instead of `GET /users/:id` you may see a name of `GET /users/123`.

## [Inheritance](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#inheritance)

Whatever a transaction's sampling decision, that decision will be passed to its child spans and from there to any transactions they subsequently cause in other services.

(See [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/trace-propagation.md) for more about how that propagation is done.)

If the transaction currently being created is one of those subsequent transactions (in other words, if it has a parent transaction), the upstream (parent) sampling decision will be included in the sampling context data. Your `tracesSampler` can use this information to choose whether to inherit that decision. In most cases, inheritance is the right choice, to avoid breaking distributed traces. A broken trace will not include all your services.

```javascript
tracesSampler: samplingContext => {
  // always inherit
  if (samplingContext.parentSampled !== undefined) {
    return samplingContext.parentSampled
  }

  ...
  // rest of sampling logic here
}
```

If you're using a `tracesSampleRate` rather than a `tracesSampler`, the decision will always be inherited.

## [Precedence](https://docs.sentry.io/platforms/javascript/guides/nextjs/sampling.md#precedence)

There are multiple ways for a transaction to end up with a sampling decision.

* Random sampling according to a static sample rate set in `tracesSampleRate`
* Random sampling according to a sample function rate returned by `tracesSampler`
* Absolute decision (100% chance or 0% chance) returned by `tracesSampler`
* If the transaction has a parent, inheriting its parent's sampling decision
* Absolute decision passed to `startTransaction`

When there's the potential for more than one of these to come into play, the following precedence rules apply:

1. If `tracesSampler` is defined, its decision will be used. It can choose to keep or ignore any parent sampling decision, use the sampling context data to make its own decision, or choose a sample rate for the transaction. We advise against overriding the parent sampling decision because it will break distributed traces)
2. If `tracesSampler` is not defined, but there's a parent sampling decision, the parent sampling decision will be used.
3. If `tracesSampler` is not defined and there's no parent sampling decision, `tracesSampleRate` will be used.

