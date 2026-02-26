---
title: '오류 캡처 | Next.js용 Sentry'
description: 'Sentry의 Next.js SDK는 대부분의 처리되지 않은 오류를 자동으로 캡처합니다. 하지만 Next.js에는 오류가 Sentry에 도달하기 전에 가로채는 내장 오류 처리 패턴이 있습니다. 이 가이드는 수동 캡처가 언제, 왜 필요한지 설명합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors

# 오류 캡처 | Next.js용 Sentry

Sentry의 Next.js SDK는 대부분의 처리되지 않은 오류를 자동으로 캡처합니다. 하지만 Next.js에는 오류가 Sentry에 도달하기 전에 가로채는 내장 오류 처리 패턴이 있습니다. 이 가이드는 수동 캡처가 언제, 왜 필요한지 설명합니다.

## [자동 캡처 vs 수동 캡처](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#automatic-vs-manual-capture)

- [자동으로 캡처되는 항목](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#whats-captured-automatically)

SDK는 코드 추가 없이 다음을 캡처합니다:

* 클라이언트 측 코드의 **처리되지 않은 예외**
* **처리되지 않은 Promise rejection**
* 크래시를 일으키는 **서버 오류** (API routes, Server Components)

- [수동 캡처가 필요한 항목](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#what-needs-manual-capture)

Next.js는 다음 패턴에서 오류를 가로채므로 Sentry에서 보이지 않게 됩니다:

* **Error boundaries** (`error.tsx`) — UI 복구를 위해 렌더링 오류를 포착
* **Caught errors** — 오류를 우아하게 처리하는 모든 `try/catch`

오류를 잡고 다시 던지지 않으면 Sentry는 해당 오류를 절대 보지 못합니다.

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

Next.js `error.tsx` 파일은 fallback UI를 보여주기 위해 렌더링 오류를 포착합니다. UX 측면에서는 좋지만, 오류가 Sentry의 전역 핸들러에 도달하지 못하게 됩니다.

가시성을 유지하려면 **모든 error boundary에 `captureException`을 추가**하세요.

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

- [전역 Error Boundary](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#global-error-boundary)

`global-error.tsx`는 루트 레이아웃 자체가 실패할 때만 동작하는 최후의 안전장치입니다. 이런 경우는 드물며, 대부분의 오류는 먼저 라우트 수준 `error.tsx` 파일에서 포착됩니다.

문서 전체를 대체하므로 `<html>` 및 `<body>` 태그를 포함하세요.

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

오류를 포착해 우아한 응답을 반환할 때(서버 액션, API routes, middleware)에는 반환 전에 `captureException`을 추가하세요.

**패턴은 어디서나 동일합니다:** `catch`하고 `throw`하지 않는다면 `captureException`을 호출하세요.

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

- [컨텍스트 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#adding-context)

오류 디버깅에 도움이 되도록 메타데이터를 추가하세요:

* **Tags**: Sentry UI에서 필터링 및 그룹화(예: 기능 영역, 사용자 티어)에 사용할 수 있도록 검색 가능
* **Extra**: 이벤트 상세에서 ID 같은 디버깅 값을 표시(검색 불가)

```tsx
Sentry.captureException(error, {
  tags: { section: "checkout" },
  extra: { orderId, userId: user.id },
});
```

breadcrumbs, user context, attachments 같은 추가 옵션은 [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md)를 참고하세요.

서버 액션에서 자동 트레이싱을 사용하려면 [`withServerActionInstrumentation`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withServerActionInstrumentation)을 참고하세요.

## [빠른 참조](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#quick-reference)

| 시나리오                          | 자동 캡처 여부 | 필요한 조치           |
| --------------------------------- | -------------- | --------------------- |
| 처리되지 않은 클라이언트 오류     | 예             | 없음                  |
| 처리되지 않은 서버 크래시         | 예             | 없음                  |
| `error.tsx` 경계                  | 아니요         | `captureException` 추가 |
| 우아한 반환이 있는 `try/catch`    | 아니요         | `captureException` 추가 |
| 다시 던지는 `try/catch`           | 예             | 없음                  |

**Error boundary 배치:**

```bash
app/
├── global-error.tsx      # Root layout errors (rare)
├── error.tsx             # App-wide fallback
└── dashboard/
    └── error.tsx         # Dashboard-specific handling
```

## [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#troubleshooting)

- [오류가 표시되지 않는 경우](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#errors-not-appearing)

1. **Error boundary가 가로채는 경우** — `error.tsx` 파일에서 `captureException`이 호출되는지 확인
2. **SDK가 초기화되지 않음** — 올바른 DSN으로 설정 파일이 존재하는지 확인
3. **`beforeSend` 필터링** — 훅이 오류를 드롭하고 있는지 확인

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

- [중복 오류](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#duplicate-errors)

같은 오류가 두 번 보인다면 여러 위치에서 캡처하고 있을 가능성이 큽니다. 각 오류를 하나의 핸들러만 캡처하도록 확인하세요.

```tsx
// Don't capture in both error.tsx AND a parent component
// Pick one location per error
```

- [누락된 스택 트레이스](https://docs.sentry.io/platforms/javascript/guides/nextjs/capturing-errors.md#missing-stack-traces)

프로덕션 환경에서는 서버 오류의 트레이스가 난독화되어 보일 수 있습니다. 읽기 쉬운 트레이스를 위해 source maps를 활성화하세요.

서버 오류의 `digest` 속성은 로그에서 검색할 수 있는 해시입니다.

```tsx
// Server errors include a digest for debugging
error: Error & { digest?: string }

// Log it for cross-referencing
console.error("Error digest:", error.digest);
```

설정 방법은 [Source Maps](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md)를 참고하세요.

