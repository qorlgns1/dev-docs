---
title: 'Guides: Forms'
description: 'Last updated February 20, 2026'
---

# Guides: Forms | Next.js

Source URL: https://nextjs.org/docs/pages/guides/forms

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Forms

Copy page

# How to create forms with API Routes

Last updated February 20, 2026

Forms enable you to create and update data in web applications. Next.js provides a powerful way to handle data mutations using **API Routes**. This guide will walk you through how to handle form submission on the server.

## Server Forms[](https://nextjs.org/docs/pages/guides/forms#server-forms)

To handle form submissions on the server, create an API endpoint that securely mutates data.

pages/api/submit.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
     
    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      const data = req.body
      const id = await createItem(data)
      res.status(200).json({ id })
    }
[/code]

Then, call the API Route from the client with an event handler:

pages/index.tsx

JavaScriptTypeScript
[code]
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
[/code]

> **Good to know:**
> 
>   * API Routes [do not specify CORS headers](https://developer.mozilla.org/docs/Web/HTTP/CORS), meaning they are same-origin only by default.
>   * Since API Routes run on the server, we're able to use sensitive values (like API keys) through [Environment Variables](https://nextjs.org/docs/pages/guides/environment-variables) without exposing them to the client. This is critical for the security of your application.
> 


## Form validation[](https://nextjs.org/docs/pages/guides/forms#form-validation)

We recommend using HTML validation like `required` and `type="email"` for basic client-side form validation.

For more advanced server-side validation, you can use a schema validation library like [zod](https://zod.dev/) to validate the form fields before mutating the data:

pages/api/submit.ts

JavaScriptTypeScript
[code]
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
[/code]

### Error handling[](https://nextjs.org/docs/pages/guides/forms#error-handling)

You can use React state to show an error message when a form submission fails:

pages/index.tsx

JavaScriptTypeScript
[code]
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
[/code]

## Displaying loading state[](https://nextjs.org/docs/pages/guides/forms#displaying-loading-state)

You can use React state to show a loading state when a form is submitting on the server:

pages/index.tsx

JavaScriptTypeScript
[code]
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
[/code]

### Redirecting[](https://nextjs.org/docs/pages/guides/forms#redirecting)

If you would like to redirect the user to a different route after a mutation, you can [`redirect`](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#response-helpers) to any absolute or relative URL:

pages/api/submit.ts

JavaScriptTypeScript
[code]
    import type { NextApiRequest, NextApiResponse } from 'next'
     
    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      const id = await addPost()
      res.redirect(307, `/post/${id}`)
    }
[/code]

Was this helpful?

supported.

Send
