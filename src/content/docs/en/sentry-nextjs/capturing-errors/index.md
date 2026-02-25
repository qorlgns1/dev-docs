---
title: 'Capturing Errors | Sentry for Next.js'
description: "Sentry's Next.js SDK automatically captures most unhandled errors. However, Next.js has built-in error handling patterns that intercept errors before ..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors

# Capturing Errors | Sentry for Next.js

Sentry's Next.js SDK automatically captures most unhandled errors. However, Next.js has built-in error handling patterns that intercept errors before they reach Sentry. This guide covers when and why you need manual capture.

## [Automatic vs Manual Capture](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#automatic-vs-manual-capture)

- [What's Captured Automatically](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#whats-captured-automatically)

The SDK captures these without any code:

* **Unhandled exceptions** in client-side code
* **Unhandled promise rejections**
* **Server errors** that crash (API routes, Server Components)

- [What Needs Manual Capture](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#what-needs-manual-capture)

Next.js intercepts errors in these patterns, hiding them from Sentry:

* **Error boundaries** (`error.tsx`) — catch rendering errors for UI recovery
* **Caught errors** — any `try/catch` where you handle the error gracefully

If you catch an error and don't re-throw it, Sentry never sees it.

```tsx
// Automatic: unhandled errors bubble up to Sentry
throw new Error("This is captured automatically");

// Manual needed: you caught it, Sentry doesn't see it
try {
  await riskyOperation();
} catch (error) {
  // Error is swallowed - add captureException
  Sentry.captureException(error);
  return { error: "Something went wrong" };
}
```

## [Error Boundaries](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#error-boundaries)

Next.js `error.tsx` files catch rendering errors to show a fallback UI. This is good for UX but means errors never reach Sentry's global handler.

**Add `captureException` in every error boundary** to maintain visibility.

`app/error.tsx`

```tsx
"use client";

import { useEffect } from "react";
import * as Sentry from "@sentry/nextjs";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    Sentry.captureException(error);
  }, [error]);

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```

- [Global Error Boundary](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#global-error-boundary)

`global-error.tsx` is a last-resort safety net that only triggers when your root layout itself fails. This is rare—most errors are caught by route-level `error.tsx` files first.

Include `<html>` and `<body>` tags since it replaces the entire document.

`app/global-error.tsx`

```tsx
"use client";

import { useEffect } from "react";
import * as Sentry from "@sentry/nextjs";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    Sentry.captureException(error);
  }, [error]);

  return (
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  );
}
```

## [Caught Errors](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#caught-errors)

When you catch errors to return graceful responses (in Server Actions, API routes, or middleware), add `captureException` before returning.

**The pattern is the same everywhere:** if you `catch` and don't `throw`, call `captureException`.

`app/actions.ts`

```tsx
"use server";

import * as Sentry from "@sentry/nextjs";

export async function createPost(formData: FormData) {
  try {
    const post = await db.posts.create({
      data: { title: formData.get("title") as string },
    });
    return { success: true, id: post.id };
  } catch (error) {
    Sentry.captureException(error);
    return { success: false, error: "Failed to create post" };
  }
}
```

- [Adding Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#adding-context)

Add metadata to help debug errors:

* **Tags**: Searchable in Sentry's UI for filtering and grouping (e.g., by feature area or user tier)
* **Extra**: Displayed in event details for debugging values like IDs (not searchable)

```tsx
Sentry.captureException(error, {
  tags: { section: "checkout" },
  extra: { orderId, userId: user.id },
});
```

See [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md) for more options like breadcrumbs, user context, and attachments.

For automatic tracing in Server Actions, see [`withServerActionInstrumentation`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withServerActionInstrumentation).

## [Quick Reference](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#quick-reference)

| Scenario                         | Captured Automatically? | Action Needed          |
| -------------------------------- | ----------------------- | ---------------------- |
| Unhandled client error           | Yes                     | None                   |
| Unhandled server crash           | Yes                     | None                   |
| `error.tsx` boundary             | No                      | Add `captureException` |
| `try/catch` with graceful return | No                      | Add `captureException` |
| `try/catch` that re-throws       | Yes                     | None                   |

**Error boundary placement:**

```bash
app/
├── global-error.tsx      # Root layout errors (rare)
├── error.tsx             # App-wide fallback
└── dashboard/
    └── error.tsx         # Dashboard-specific handling
```

## [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#troubleshooting)

- [Errors Not Appearing](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#errors-not-appearing)

1. **Error boundary intercepting** — Check that `captureException` is called in your `error.tsx` files
2. **SDK not initialized** — Verify config files exist with correct DSN
3. **`beforeSend` filtering** — Check if a hook is dropping errors

`app/error.tsx`

```tsx
"use client";

import { useEffect } from "react";
import * as Sentry from "@sentry/nextjs";

export default function Error({ error }: { error: Error }) {
  useEffect(() => {
    // This line is required!
    Sentry.captureException(error);
  }, [error]);

  return <div>Something went wrong</div>;
}
```

- [Duplicate Errors](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#duplicate-errors)

If you see the same error twice, you're likely capturing in multiple places. Check that only one handler captures each error.

```tsx
// Don't capture in both error.tsx AND a parent component
// Pick one location per error
```

- [Missing Stack Traces](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#missing-stack-traces)

Server errors may show minified traces in production. Enable source maps for readable traces.

The `digest` property on server errors is a hash you can search for in logs.

```tsx
// Server errors include a digest for debugging
error: Error & { digest?: string }

// Log it for cross-referencing
console.error("Error digest:", error.digest);
```

See [Source Maps](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md) for setup instructions.

