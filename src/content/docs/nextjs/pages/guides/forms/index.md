---
title: '가이드: Forms'
description: '최종 업데이트: 2026년 2월 20일'
---

# 가이드: Forms | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/forms

# API Routes로 폼을 만드는 방법

최종 업데이트: 2026년 2월 20일

폼은 웹 애플리케이션에서 데이터를 생성하고 업데이트할 수 있게 합니다. Next.js는 **API Routes**를 사용해 데이터 변이를 처리하는 강력한 방식을 제공합니다. 이 가이드는 서버에서 폼 제출을 처리하는 방법을 안내합니다.

## Server Forms[](https://nextjs.org/docs/pages/guides/forms#server-forms)

서버에서 폼 제출을 처리하려면 데이터를 안전하게 변이하는 API 엔드포인트를 만드세요.

pages/api/submit.ts

JavaScriptTypeScript
```
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      const data = req.body
      const id = await createItem(data)
      res.status(200).json({ id })
    }
```

그다음 클라이언트에서 이벤트 핸들러로 API Route를 호출합니다:

pages/index.tsx

JavaScriptTypeScript
```
    import { FormEvent } from 'react'

    export default function Page() {
      async function onSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()

        const formData = new FormData(event.currentTarget)
        const response = await fetch('/api/submit', {
          method: 'POST',
          body: formData,
        })

        // Handle response if necessary
        const data = await response.json()
        // ...
      }

      return (
        <form onSubmit={onSubmit}>
          <input type="text" name="name" />
          <button type="submit">Submit</button>
        </form>
      )
    }
```

> **참고하세요:**
>
>   * API Routes는 [CORS 헤더를 지정하지 않습니다](https://developer.mozilla.org/docs/Web/HTTP/CORS). 따라서 기본적으로 동일 출처에서만 사용할 수 있습니다.
>   * API Routes는 서버에서 실행되므로 [Environment Variables](https://nextjs.org/docs/pages/guides/environment-variables)를 통해 API 키 같은 민감한 값을 클라이언트에 노출하지 않고 사용할 수 있습니다. 이는 애플리케이션 보안에 매우 중요합니다.
>

## Form validation[](https://nextjs.org/docs/pages/guides/forms#form-validation)

기본적인 클라이언트 측 폼 검증에는 `required`나 `type="email"` 같은 HTML 검증을 사용하는 것이 좋습니다.

보다 고급 서버 측 검증이 필요하다면, [zod](https://zod.dev/) 같은 스키마 검증 라이브러리를 사용해 데이터를 변이하기 전에 폼 필드를 검증할 수 있습니다:

pages/api/submit.ts

JavaScriptTypeScript
```
    import type { NextApiRequest, NextApiResponse } from 'next'
    import { z } from 'zod'

    const schema = z.object({
      // ...
    })

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      const parsed = schema.parse(req.body)
      // ...
    }
```

### Error handling[](https://nextjs.org/docs/pages/guides/forms#error-handling)

폼 제출이 실패했을 때 오류 메시지를 표시하려면 React state를 사용할 수 있습니다:

pages/index.tsx

JavaScriptTypeScript
```
    import React, { useState, FormEvent } from 'react'

    export default function Page() {
      const [isLoading, setIsLoading] = useState<boolean>(false)
      const [error, setError] = useState<string | null>(null)

      async function onSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
        setIsLoading(true)
        setError(null) // Clear previous errors when a new request starts

        try {
          const formData = new FormData(event.currentTarget)
          const response = await fetch('/api/submit', {
            method: 'POST',
            body: formData,
          })

          if (!response.ok) {
            throw new Error('Failed to submit the data. Please try again.')
          }

          // Handle response if necessary
          const data = await response.json()
          // ...
        } catch (error) {
          // Capture the error message to display to the user
          setError(error.message)
          console.error(error)
        } finally {
          setIsLoading(false)
        }
      }

      return (
        <div>
          {error && <div style={{ color: 'red' }}>{error}</div>}
          <form onSubmit={onSubmit}>
            <input type="text" name="name" />
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Loading...' : 'Submit'}
            </button>
          </form>
        </div>
      )
    }
```

## Displaying loading state[](https://nextjs.org/docs/pages/guides/forms#displaying-loading-state)

서버에서 폼을 제출하는 동안 로딩 상태를 표시하려면 React state를 사용할 수 있습니다:

pages/index.tsx

JavaScriptTypeScript
```
    import React, { useState, FormEvent } from 'react'

    export default function Page() {
      const [isLoading, setIsLoading] = useState<boolean>(false)

      async function onSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
        setIsLoading(true) // Set loading to true when the request starts

        try {
          const formData = new FormData(event.currentTarget)
          const response = await fetch('/api/submit', {
            method: 'POST',
            body: formData,
          })

          // Handle response if necessary
          const data = await response.json()
          // ...
        } catch (error) {
          // Handle error if necessary
          console.error(error)
        } finally {
          setIsLoading(false) // Set loading to false when the request completes
        }
      }

      return (
        <form onSubmit={onSubmit}>
          <input type="text" name="name" />
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Loading...' : 'Submit'}
          </button>
        </form>
      )
    }
```

### Redirecting[](https://nextjs.org/docs/pages/guides/forms#redirecting)

변이 후 사용자에게 다른 경로로 이동하도록 하려면 절대 또는 상대 URL로 [`redirect`](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#response-helpers)할 수 있습니다:

pages/api/submit.ts

JavaScriptTypeScript
```
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      const id = await addPost()
      res.redirect(307, `/post/${id}`)
    }
```

이 문서가 도움이 되었나요?

Send