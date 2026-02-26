---
title: 'LinkedErrors | Sentry for Next.js'
description: "This integration is enabled by default. If you'd like to modify your default integrations, read this."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors

# LinkedErrors | Sentry for Next.js

*Import name: `Sentry.linkedErrorsIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration allows you to configure linked errors. They'll be recursively read up to a specified limit, then lookup will be performed by a specific key. By default, the Sentry SDK sets the limit to five and the key used is `"cause"`.

```JavaScript
Sentry.init({
  integrations: [Sentry.linkedErrorsIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#options)

- [`key`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#key)

*Type: `string`*

- [`limit`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#limit)

*Type: `number`*

## [Example](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#example)

Here's a code example of how this could be implemented:

```javascript
document
  .querySelector("#get-reviews-btn")
  .addEventListener("click", async (event) => {
    const movie = event.target.dataset.title;
    try {
      const reviews = await fetchMovieReviews(movie);
      renderMovieReviews(reviews);
    } catch (e) {
      const fetchError = new Error(
        `Failed to fetch reviews for: ${movie}`,
      );
      fetchError.cause = e;
      Sentry.captureException(fetchError);
      renderMovieReviewsError(fetchError);
    }
  });
```

