---
title: 'Guides: Analytics'
description: 'Last updated February 20, 2026'
---

# Guides: Analytics | Next.js

Source URL: https://nextjs.org/docs/pages/guides/analytics

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Analytics

Copy page

# How to set up analytics

Last updated February 20, 2026

Next.js has built-in support for measuring and reporting performance metrics. You can either use the [`useReportWebVitals`](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals) hook to manage reporting yourself, or alternatively, Vercel provides a [managed service](https://vercel.com/analytics?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) to automatically collect and visualize metrics for you.

## Client Instrumentation[](https://nextjs.org/docs/pages/guides/analytics#client-instrumentation)

For more advanced analytics and monitoring needs, Next.js provides a `instrumentation-client.js|ts` file that runs before your application's frontend code starts executing. This is ideal for setting up global analytics, error tracking, or performance monitoring tools.

To use it, create an `instrumentation-client.js` or `instrumentation-client.ts` file in your application's root directory:

instrumentation-client.js
[code]
    // Initialize analytics before the app starts
    console.log('Analytics initialized')
     
    // Set up global error tracking
    window.addEventListener('error', (event) => {
      // Send to your error tracking service
      reportError(event.error)
    })
[/code]

## Build Your Own[](https://nextjs.org/docs/pages/guides/analytics#build-your-own)

pages/_app.js
[code]
    import { useReportWebVitals } from 'next/web-vitals'
     
    function MyApp({ Component, pageProps }) {
      useReportWebVitals((metric) => {
        console.log(metric)
      })
     
      return <Component {...pageProps} />
    }
[/code]

View the [API Reference](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals) for more information.

## Web Vitals[](https://nextjs.org/docs/pages/guides/analytics#web-vitals)

[Web Vitals](https://web.dev/vitals/) are a set of useful metrics that aim to capture the user experience of a web page. The following web vitals are all included:

  * [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
  * [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
  * [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
  * [First Input Delay](https://web.dev/fid/) (FID)
  * [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
  * [Interaction to Next Paint](https://web.dev/inp/) (INP)



You can handle all the results of these metrics using the `name` property.

pages/_app.js
[code]
    import { useReportWebVitals } from 'next/web-vitals'
     
    function MyApp({ Component, pageProps }) {
      useReportWebVitals((metric) => {
        switch (metric.name) {
          case 'FCP': {
            // handle FCP results
          }
          case 'LCP': {
            // handle LCP results
          }
          // ...
        }
      })
     
      return <Component {...pageProps} />
    }
[/code]

## Custom Metrics[](https://nextjs.org/docs/pages/guides/analytics#custom-metrics)

In addition to the core metrics listed above, there are some additional custom metrics that measure the time it takes for the page to hydrate and render:

  * `Next.js-hydration`: Length of time it takes for the page to start and finish hydrating (in ms)
  * `Next.js-route-change-to-render`: Length of time it takes for a page to start rendering after a route change (in ms)
  * `Next.js-render`: Length of time it takes for a page to finish render after a route change (in ms)



You can handle all the results of these metrics separately:
[code]
    export function reportWebVitals(metric) {
      switch (metric.name) {
        case 'Next.js-hydration':
          // handle hydration results
          break
        case 'Next.js-route-change-to-render':
          // handle route-change to render results
          break
        case 'Next.js-render':
          // handle render results
          break
        default:
          break
      }
    }
[/code]

These metrics work in all browsers that support the [User Timing API](https://caniuse.com/#feat=user-timing).

## Sending results to external systems[](https://nextjs.org/docs/pages/guides/analytics#sending-results-to-external-systems)

You can send results to any endpoint to measure and track real user performance on your site. For example:
[code] 
    useReportWebVitals((metric) => {
      const body = JSON.stringify(metric)
      const url = 'https://example.com/analytics'
     
      // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
      if (navigator.sendBeacon) {
        navigator.sendBeacon(url, body)
      } else {
        fetch(url, { body, method: 'POST', keepalive: true })
      }
    })
[/code]

> **Good to know** : If you use [Google Analytics](https://analytics.google.com/analytics/web/), using the `id` value can allow you to construct metric distributions manually (to calculate percentiles, etc.)

> 
[code]
>     useReportWebVitals((metric) => {
>       // Use `window.gtag` if you initialized Google Analytics as this example:
>       // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>       window.gtag('event', metric.name, {
>         value: Math.round(
>           metric.name === 'CLS' ? metric.value * 1000 : metric.value
>         ), // values must be integers
>         event_label: metric.id, // id unique to current page load
>         non_interaction: true, // avoids affecting bounce rate.
>       })
>     })
[/code]
> 
> Read more about [sending results to Google Analytics](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics).

Was this helpful?

supported.

Send
