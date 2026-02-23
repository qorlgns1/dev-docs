---
title: '파일 시스템 규칙: error.js'
description: 'app/dashboard/error.tsx'
---

# 파일 시스템 규칙: error.js | Next.js
Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/error

Copy page

# error.js

최종 업데이트 2026년 2월 20일

**error** 파일을 사용하면 예기치 못한 런타임 오류를 처리하고 대체 UI를 표시할 수 있습니다.

app/dashboard/error.tsx

JavaScriptTypeScript
[code]
    'use client' // Error boundaries must be Client Components

    import { useEffect } from 'react'

    export default function Error({
      error,
      reset,
    }: {
      error: Error & { digest?: string }
      reset: () => void
    }) {
      useEffect(() => {
        // Log the error to an error reporting service
        console.error(error)
      }, [error])

      return (
        <div>
          <h2>Something went wrong!</h2>
          <button
            onClick={
              // Attempt to recover by trying to re-render the segment
              () => reset()
            }
          >
            Try again
          </button>
        </div>
      )
    }
[/code]

`error.js`는 경로 세그먼트와 중첩된 하위 요소를 [React Error Boundary](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)로 감쌉니다. 경계 내부에서 오류가 발생하면 `error` 컴포넌트가 대체 UI로 표시됩니다.

> **알아두면 좋은 점** :
>
>   * [React DevTools](https://react.dev/learn/react-developer-tools)를 사용해 오류 경계를 토글하고 오류 상태를 테스트할 수 있습니다.
>   * 오류가 상위 오류 경계까지 전파되길 원한다면 `error` 컴포넌트를 렌더링할 때 `throw`를 호출하면 됩니다.
>

## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/error#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/error#props)

#### `error`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#error)

`error.js` 클라이언트 컴포넌트로 전달되는 [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error) 객체 인스턴스입니다.

> **알아두면 좋은 점:** 개발 중에는 클라이언트로 전달되는 `Error` 객체가 직렬화되어 원래 오류의 `message`를 포함하므로 디버깅이 더 쉽습니다. 하지만 **프로덕션에서는 이 동작이 달라지므로** 오류에 담긴 잠재적으로 민감한 세부 정보가 클라이언트로 유출되지 않습니다.

#### `error.message`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#errormessage)

  * 클라이언트 컴포넌트에서 전달된 오류는 원래 `Error` 메시지를 표시합니다.
  * 서버 컴포넌트에서 전달된 오류는 식별자가 포함된 일반적인 메시지를 표시합니다. 이는 민감한 세부 정보를 노출하지 않기 위한 조치입니다. `errors.digest` 아래의 식별자를 사용해 해당 서버 로그와 매칭할 수 있습니다.

#### `error.digest`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#errordigest)

발생한 오류의 자동 생성 해시입니다. 서버 측 로그에서 해당 오류를 매칭하는 데 사용할 수 있습니다.

#### `reset`[](https://nextjs.org/docs/app/api-reference/file-conventions/error#reset)

오류의 원인은 일시적일 수 있습니다. 이런 경우에는 다시 시도하면 문제가 해결될 수 있습니다.

오류 컴포넌트는 `reset()` 함수를 사용해 사용자가 오류에서 복구를 시도하도록 유도할 수 있습니다. 실행하면 함수가 오류 경계의 콘텐츠를 다시 렌더링하려고 시도합니다. 성공하면 대체 오류 컴포넌트는 재렌더링 결과로 교체됩니다.

app/dashboard/error.tsx

JavaScriptTypeScript
[code]
    'use client' // Error boundaries must be Client Components

    export default function Error({
      error,
      reset,
    }: {
      error: Error & { digest?: string }
      reset: () => void
    }) {
      return (
        <div>
          <h2>Something went wrong!</h2>
          <button onClick={() => reset()}>Try again</button>
        </div>
      )
    }
[/code]

## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/error#examples)

### Global Error[](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error)

비록 드물지만, 루트 앱 디렉터리에 있는 `global-error.jsx`를 사용해 루트 레이아웃 또는 템플릿에서 오류를 처리할 수 있으며 [국제화](https://nextjs.org/docs/app/guides/internationalization)를 활용하는 경우에도 가능합니다. 글로벌 오류 UI는 고유한 `<html>` 및 `<body>` 태그, 전역 스타일, 폰트 또는 오류 페이지에 필요한 기타 의존성을 정의해야 합니다. 이 파일은 활성화되면 루트 레이아웃 또는 템플릿을 대체합니다.

> **알아두면 좋은 점** : 오류 경계는 반드시 [클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components#using-client-components)여야 하므로, `global-error.jsx`에서는 [`metadata` 및 `generateMetadata`](https://nextjs.org/docs/app/getting-started/metadata-and-og-images) 내보내기를 지원하지 않습니다. 대안으로 React [`<title>`](https://react.dev/reference/react-dom/components/title) 컴포넌트를 사용할 수 있습니다.

app/global-error.tsx

JavaScriptTypeScript
[code]
    'use client' // Error boundaries must be Client Components

    export default function GlobalError({
      error,
      reset,
    }: {
      error: Error & { digest?: string }
      reset: () => void
    }) {
      return (
        // global-error must include html and body tags
        <html>
          <body>
            <h2>Something went wrong!</h2>
            <button onClick={() => reset()}>Try again</button>
          </body>
        </html>
      )
    }
[/code]

### 사용자 정의 오류 경계로 우아한 오류 복구[](https://nextjs.org/docs/app/api-reference/file-conventions/error#graceful-error-recovery-with-a-custom-error-boundary)

클라이언트 렌더링이 실패할 때 마지막으로 서버에서 렌더링된 UI를 보여주면 사용자 경험을 개선할 수 있습니다.

`GracefullyDegradingErrorBoundary`는 오류가 발생하기 전에 현재 HTML을 캡처하고 유지하는 사용자 정의 오류 경계 예시입니다. 렌더링 오류가 발생하면 캡처된 HTML을 다시 렌더링하고 지속적인 알림 표시줄을 띄워 사용자에게 알립니다.

app/dashboard/error.tsx

JavaScriptTypeScript
[code]
    'use client'

    import React, { Component, ErrorInfo, ReactNode } from 'react'

    interface ErrorBoundaryProps {
      children: ReactNode
      onError?: (error: Error, errorInfo: ErrorInfo) => void
    }

    interface ErrorBoundaryState {
      hasError: boolean
    }

    export class GracefullyDegradingErrorBoundary extends Component<
      ErrorBoundaryProps,
      ErrorBoundaryState
    > {
      private contentRef: React.RefObject<HTMLDivElement | null>

      constructor(props: ErrorBoundaryProps) {
        super(props)
        this.state = { hasError: false }
        this.contentRef = React.createRef()
      }

      static getDerivedStateFromError(_: Error): ErrorBoundaryState {
        return { hasError: true }
      }

      componentDidCatch(error: Error, errorInfo: ErrorInfo) {
        if (this.props.onError) {
          this.props.onError(error, errorInfo)
        }
      }

      render() {
        if (this.state.hasError) {
          // Render the current HTML content without hydration
          return (
            <>
              <div
                ref={this.contentRef}
                suppressHydrationWarning
                dangerouslySetInnerHTML={{
                  __html: this.contentRef.current?.innerHTML || '',
                }}
              />
              <div className="fixed bottom-0 left-0 right-0 bg-red-600 text-white py-4 px-6 text-center">
                <p className="font-semibold">
                  An error occurred during page rendering
                </p>
              </div>
            </>
          )
        }

        return <div ref={this.contentRef}>{this.props.children}</div>
      }
    }

    export default GracefullyDegradingErrorBoundary
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/error#version-history)

Version| Changes
---|---
`v15.2.0`| 개발 환경에서도 `global-error`를 표시합니다.
`v13.1.0`| `global-error`가 도입되었습니다.
`v13.0.0`| `error`가 도입되었습니다.

## 오류 처리 더 알아보기

- [Error Handling예상된 오류를 표시하고 처리되지 않은 예외를 다루는 방법을 알아보세요.](https://nextjs.org/docs/app/getting-started/error-handling)

보내기
