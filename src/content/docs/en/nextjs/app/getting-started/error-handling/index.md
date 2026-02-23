---
title: 'Getting Started: Error Handling'
description: 'Errors can be divided into two categories: expected errors and uncaught exceptions. This page will walk you through how you can handle these errors in...'
---

# Getting Started: Error Handling | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/error-handling

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Error Handling

Copy page

# Error Handling

Last updated February 20, 2026

Errors can be divided into two categories: [expected errors](https://nextjs.org/docs/app/getting-started/error-handling#handling-expected-errors) and [uncaught exceptions](https://nextjs.org/docs/app/getting-started/error-handling#handling-uncaught-exceptions). This page will walk you through how you can handle these errors in your Next.js application.

## Handling expected errors[](https://nextjs.org/docs/app/getting-started/error-handling#handling-expected-errors)

Expected errors are those that can occur during the normal operation of the application, such as those from [server-side form validation](https://nextjs.org/docs/app/guides/forms) or failed requests. These errors should be handled explicitly and returned to the client.

### Server Functions[](https://nextjs.org/docs/app/getting-started/error-handling#server-functions)

You can use the [`useActionState`](https://react.dev/reference/react/useActionState) hook to handle expected errors in [Server Functions](https://react.dev/reference/rsc/server-functions).

For these errors, avoid using `try`/`catch` blocks and throw errors. Instead, model expected errors as return values.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function createPost(prevState: any, formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')
     
      const res = await fetch('https://api.vercel.app/posts', {
        method: 'POST',
        body: { title, content },
      })
      const json = await res.json()
     
      if (!res.ok) {
        return { message: 'Failed to create post' }
      }
    }
[/code]

You can pass your action to the `useActionState` hook and use the returned `state` to display an error message.

app/ui/form.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useActionState } from 'react'
    import { createPost } from '@/app/actions'
     
    const initialState = {
      message: '',
    }
     
    export function Form() {
      const [state, formAction, pending] = useActionState(createPost, initialState)
     
      return (
        <form action={formAction}>
          <label htmlFor="title">Title</label>
          <input type="text" id="title" name="title" required />
          <label htmlFor="content">Content</label>
          <textarea id="content" name="content" required />
          {state?.message && <p aria-live="polite">{state.message}</p>}
          <button disabled={pending}>Create Post</button>
        </form>
      )
    }
[/code]

### Server Components[](https://nextjs.org/docs/app/getting-started/error-handling#server-components)

When fetching data inside of a Server Component, you can use the response to conditionally render an error message or [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect).

app/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const res = await fetch(`https://...`)
      const data = await res.json()
     
      if (!res.ok) {
        return 'There was an error.'
      }
     
      return '...'
    }
[/code]

### Not found[](https://nextjs.org/docs/app/getting-started/error-handling#not-found)

You can call the [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) function within a route segment and use the [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) file to show a 404 UI.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
[code]
    import { getPostBySlug } from '@/lib/posts'
     
    export default async function Page({ params }: { params: { slug: string } }) {
      const { slug } = await params
      const post = getPostBySlug(slug)
     
      if (!post) {
        notFound()
      }
     
      return <div>{post.title}</div>
    }
[/code]

app/blog/[slug]/not-found.tsx

JavaScriptTypeScript
[code]
    export default function NotFound() {
      return <div>404 - Page Not Found</div>
    }
[/code]

## Handling uncaught exceptions[](https://nextjs.org/docs/app/getting-started/error-handling#handling-uncaught-exceptions)

Uncaught exceptions are unexpected errors that indicate bugs or issues that should not occur during the normal flow of your application. These should be handled by throwing errors, which will then be caught by error boundaries.

### Nested error boundaries[](https://nextjs.org/docs/app/getting-started/error-handling#nested-error-boundaries)

Next.js uses error boundaries to handle uncaught exceptions. Error boundaries catch errors in their child components and display a fallback UI instead of the component tree that crashed.

Create an error boundary by adding an [`error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error) file inside a route segment and exporting a React component:

app/dashboard/error.tsx

JavaScriptTypeScript
[code]
    'use client' // Error boundaries must be Client Components
     
    import { useEffect } from 'react'
     
    export default function ErrorPage({
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

Errors will bubble up to the nearest parent error boundary. This allows for granular error handling by placing `error.tsx` files at different levels in the [route hierarchy](https://nextjs.org/docs/app/getting-started/project-structure#component-hierarchy).

Error boundaries don’t catch errors inside event handlers. They’re designed to catch errors [during rendering](https://react.dev/reference/react/Component#static-getderivedstatefromerror) to show a **fallback UI** instead of crashing the whole app.

In general, errors in event handlers or async code aren’t handled by error boundaries because they run after rendering.

To handle these cases, catch the error manually and store it using `useState` or `useReducer`, then update the UI to inform the user.
[code] 
    'use client'
     
    import { useState } from 'react'
     
    export function Button() {
      const [error, setError] = useState(null)
     
      const handleClick = () => {
        try {
          // do some work that might fail
          throw new Error('Exception')
        } catch (reason) {
          setError(reason)
        }
      }
     
      if (error) {
        /* render fallback UI */
      }
     
      return (
        <button type="button" onClick={handleClick}>
          Click me
        </button>
      )
    }
[/code]

Note that unhandled errors inside `startTransition` from `useTransition`, will bubble up to the nearest error boundary.
[code] 
    'use client'
     
    import { useTransition } from 'react'
     
    export function Button() {
      const [pending, startTransition] = useTransition()
     
      const handleClick = () =>
        startTransition(() => {
          throw new Error('Exception')
        })
     
      return (
        <button type="button" onClick={handleClick}>
          Click me
        </button>
      )
    }
[/code]

### Global errors[](https://nextjs.org/docs/app/getting-started/error-handling#global-errors)

While less common, you can handle errors in the root layout using the [`global-error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error) file, located in the root app directory, even when leveraging [internationalization](https://nextjs.org/docs/app/guides/internationalization). Global error UI must define its own `<html>` and `<body>` tags, since it is replacing the root layout or template when active.

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

## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

### [redirectAPI Reference for the redirect function.](https://nextjs.org/docs/app/api-reference/functions/redirect)### [error.jsAPI reference for the error.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/error)### [notFoundAPI Reference for the notFound function.](https://nextjs.org/docs/app/api-reference/functions/not-found)### [not-found.jsAPI reference for the not-found.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)

Was this helpful?

supported.

Send
