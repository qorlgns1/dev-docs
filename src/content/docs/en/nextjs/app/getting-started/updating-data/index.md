---
title: 'Getting Started: Updating Data'
description: "You can update data in Next.js using React's Server Functions. This page will go through how you can create and invoke Server Functions."
---

# Getting Started: Updating Data | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/updating-data

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Updating Data

Copy page

# Updating Data

Last updated February 20, 2026

You can update data in Next.js using React's [Server Functions](https://react.dev/reference/rsc/server-functions). This page will go through how you can [create](https://nextjs.org/docs/app/getting-started/updating-data#creating-server-functions) and [invoke](https://nextjs.org/docs/app/getting-started/updating-data#invoking-server-functions) Server Functions.

## What are Server Functions?[](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions)

A **Server Function** is an asynchronous function that runs on the server. They can be called from the client through a network request, which is why they must be asynchronous.

In an `action` or mutation context, they are also called **Server Actions**.

> **Good to know:** A Server Action is a Server Function used in a specific way (for handling form submissions and mutations). Server Function is the broader term.

By convention, a Server Action is an async function used with [`startTransition`](https://react.dev/reference/react/startTransition). This happens automatically when the function is:

  * Passed to a `<form>` using the `action` prop.
  * Passed to a `<button>` using the `formAction` prop.



In Next.js, Server Actions integrate with the framework's [caching](https://nextjs.org/docs/app/guides/caching) architecture. When an action is invoked, Next.js can return both the updated UI and new data in a single server roundtrip.

Behind the scenes, actions use the `POST` method, and only this HTTP method can invoke them.

## Creating Server Functions[](https://nextjs.org/docs/app/getting-started/updating-data#creating-server-functions)

A Server Function can be defined by using the [`use server`](https://react.dev/reference/rsc/use-server) directive. You can place the directive at the top of an **asynchronous** function to mark the function as a Server Function, or at the top of a separate file to mark all exports of that file.

app/lib/actions.ts

JavaScriptTypeScript
[code]
    export async function createPost(formData: FormData) {
      'use server'
      const title = formData.get('title')
      const content = formData.get('content')
     
      // Update data
      // Revalidate cache
    }
     
    export async function deletePost(formData: FormData) {
      'use server'
      const id = formData.get('id')
     
      // Update data
      // Revalidate cache
    }
[/code]

### Server Components[](https://nextjs.org/docs/app/getting-started/updating-data#server-components)

Server Functions can be inlined in Server Components by adding the `"use server"` directive to the top of the function body:

app/page.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      // Server Action
      async function createPost(formData: FormData) {
        'use server'
        // ...
      }
     
      return <></>
    }
[/code]

> **Good to know:** Server Components support progressive enhancement by default, meaning forms that call Server Actions will be submitted even if JavaScript hasn't loaded yet or is disabled.

### Client Components[](https://nextjs.org/docs/app/getting-started/updating-data#client-components)

It's not possible to define Server Functions in Client Components. However, you can invoke them in Client Components by importing them from a file that has the `"use server"` directive at the top of it:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function createPost() {}
[/code]

app/ui/button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { createPost } from '@/app/actions'
     
    export function Button() {
      return <button formAction={createPost}>Create</button>
    }
[/code]

> **Good to know:** In Client Components, forms invoking Server Actions will queue submissions if JavaScript isn't loaded yet, and will be prioritized for hydration. After hydration, the browser does not refresh on form submission.

### Passing actions as props[](https://nextjs.org/docs/app/getting-started/updating-data#passing-actions-as-props)

You can also pass an action to a Client Component as a prop:
[code] 
    <ClientComponent updateItemAction={updateItem} />
[/code]

app/client-component.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    export default function ClientComponent({
      updateItemAction,
    }: {
      updateItemAction: (formData: FormData) => void
    }) {
      return <form action={updateItemAction}>{/* ... */}</form>
    }
[/code]

## Invoking Server Functions[](https://nextjs.org/docs/app/getting-started/updating-data#invoking-server-functions)

There are two main ways you can invoke a Server Function:

  1. [Forms](https://nextjs.org/docs/app/getting-started/updating-data#forms) in Server and Client Components
  2. [Event Handlers](https://nextjs.org/docs/app/getting-started/updating-data#event-handlers) and [useEffect](https://nextjs.org/docs/app/getting-started/updating-data#useeffect) in Client Components



> **Good to know:** Server Functions are designed for server-side mutations. The client currently dispatches and awaits them one at a time. This is an implementation detail and may change. If you need parallel data fetching, use [data fetching](https://nextjs.org/docs/app/getting-started/fetching-data#server-components) in Server Components, or perform parallel work inside a single Server Function or [Route Handler](https://nextjs.org/docs/app/guides/backend-for-frontend#manipulating-data).

### Forms[](https://nextjs.org/docs/app/getting-started/updating-data#forms)

React extends the HTML [`<form>`](https://react.dev/reference/react-dom/components/form) element to allow a Server Function to be invoked with the HTML `action` prop.

When invoked in a form, the function automatically receives the [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData/FormData) object. You can extract the data using the native [`FormData` methods](https://developer.mozilla.org/en-US/docs/Web/API/FormData#instance_methods):

app/ui/form.tsx

JavaScriptTypeScript
[code]
    import { createPost } from '@/app/actions'
     
    export function Form() {
      return (
        <form action={createPost}>
          <input type="text" name="title" />
          <input type="text" name="content" />
          <button type="submit">Create</button>
        </form>
      )
    }
[/code]

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    export async function createPost(formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')
     
      // Update data
      // Revalidate cache
    }
[/code]

### Event Handlers[](https://nextjs.org/docs/app/getting-started/updating-data#event-handlers)

You can invoke a Server Function in a Client Component by using event handlers such as `onClick`.

app/like-button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { incrementLike } from './actions'
    import { useState } from 'react'
     
    export default function LikeButton({ initialLikes }: { initialLikes: number }) {
      const [likes, setLikes] = useState(initialLikes)
     
      return (
        <>
          <p>Total Likes: {likes}</p>
          <button
            onClick={async () => {
              const updatedLikes = await incrementLike()
              setLikes(updatedLikes)
            }}
          >
            Like
          </button>
        </>
      )
    }
[/code]

## Examples[](https://nextjs.org/docs/app/getting-started/updating-data#examples)

### Showing a pending state[](https://nextjs.org/docs/app/getting-started/updating-data#showing-a-pending-state)

While executing a Server Function, you can show a loading indicator with React's [`useActionState`](https://react.dev/reference/react/useActionState) hook. This hook returns a `pending` boolean:

app/ui/button.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useActionState, startTransition } from 'react'
    import { createPost } from '@/app/actions'
    import { LoadingSpinner } from '@/app/ui/loading-spinner'
     
    export function Button() {
      const [state, action, pending] = useActionState(createPost, false)
     
      return (
        <button onClick={() => startTransition(action)}>
          {pending ? <LoadingSpinner /> : 'Create Post'}
        </button>
      )
    }
[/code]

### Refreshing[](https://nextjs.org/docs/app/getting-started/updating-data#refreshing)

After a mutation, you may want to refresh the current page to show the latest data. You can do this by calling [`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh) from `next/cache` in a Server Action:

app/lib/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { refresh } from 'next/cache'
     
    export async function updatePost(formData: FormData) {
      // Update data
      // ...
     
      refresh()
    }
[/code]

This refreshes the client router, ensuring the UI reflects the latest state. The `refresh()` function does not revalidate tagged data. To revalidate tagged data, use [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) instead.

### Revalidating[](https://nextjs.org/docs/app/getting-started/updating-data#revalidating)

After performing an update, you can revalidate the Next.js cache and show the updated data by calling [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) within the Server Function:

app/lib/actions.ts

JavaScriptTypeScript
[code]
    import { revalidatePath } from 'next/cache'
     
    export async function createPost(formData: FormData) {
      'use server'
      // Update data
      // ...
     
      revalidatePath('/posts')
    }
[/code]

### Redirecting[](https://nextjs.org/docs/app/getting-started/updating-data#redirecting)

You may want to redirect the user to a different page after performing an update. You can do this by calling [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect) within the Server Function.

app/lib/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { revalidatePath } from 'next/cache'
    import { redirect } from 'next/navigation'
     
    export async function createPost(formData: FormData) {
      // Update data
      // ...
     
      revalidatePath('/posts')
      redirect('/posts')
    }
[/code]

Calling `redirect` [throws](https://nextjs.org/docs/app/api-reference/functions/redirect#behavior) a framework handled control-flow exception. Any code after it won't execute. If you need fresh data, call [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) beforehand.

### Cookies[](https://nextjs.org/docs/app/getting-started/updating-data#cookies)

You can `get`, `set`, and `delete` cookies inside a Server Action using the [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API.

When you [set or delete](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-functions) a cookie in a Server Action, Next.js re-renders the current page and its layouts on the server so the **UI reflects the new cookie value**.

> **Good to know** : The server update applies to the current React tree, re-rendering, mounting, or unmounting components, as needed. Client state is preserved for re-rendered components, and effects re-run if their dependencies changed.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { cookies } from 'next/headers'
     
    export async function exampleAction() {
      const cookieStore = await cookies()
     
      // Get cookie
      cookieStore.get('name')?.value
     
      // Set cookie
      cookieStore.set('name', 'Delba')
     
      // Delete cookie
      cookieStore.delete('name')
    }
[/code]

### useEffect[](https://nextjs.org/docs/app/getting-started/updating-data#useeffect)

You can use the React [`useEffect`](https://react.dev/reference/react/useEffect) hook to invoke a Server Action when the component mounts or a dependency changes. This is useful for mutations that depend on global events or need to be triggered automatically. For example, `onKeyDown` for app shortcuts, an intersection observer hook for infinite scrolling, or when the component mounts to update a view count:

app/view-count.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { incrementViews } from './actions'
    import { useState, useEffect, useTransition } from 'react'
     
    export default function ViewCount({ initialViews }: { initialViews: number }) {
      const [views, setViews] = useState(initialViews)
      const [isPending, startTransition] = useTransition()
     
      useEffect(() => {
        startTransition(async () => {
          const updatedViews = await incrementViews()
          setViews(updatedViews)
        })
      }, [])
     
      // You can use `isPending` to give users feedback
      return <p>Total Views: {views}</p>
    }
[/code]

## API Reference

Learn more about the features mentioned in this page by reading the API Reference.

### [revalidatePathAPI Reference for the revalidatePath function.](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)### [revalidateTagAPI Reference for the revalidateTag function.](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)### [redirectAPI Reference for the redirect function.](https://nextjs.org/docs/app/api-reference/functions/redirect)

Was this helpful?

supported.

Send
