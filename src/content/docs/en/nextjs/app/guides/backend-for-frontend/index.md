---
title: 'Guides: Backend for Frontend'
description: 'Last updated February 20, 2026'
---

# Guides: Backend for Frontend | Next.js

Source URL: https://nextjs.org/docs/app/guides/backend-for-frontend

[App Router](https://nextjs.org/docs/app)[Guides](https://nextjs.org/docs/app/guides)Backend for Frontend

Copy page

# How to use Next.js as a backend for your frontend

Last updated February 20, 2026

Next.js supports the "Backend for Frontend" pattern. This lets you create public endpoints to handle HTTP requests and return any content type—not just HTML. You can also access data sources and perform side effects like updating remote data.

If you are starting a new project, using `create-next-app` with the `--api` flag automatically includes an example `route.ts` in your new project's `app/` folder, demonstrating how to create an API endpoint.

pnpmnpmyarnbun

Terminal
[code]
    pnpm create next-app --api
[/code]

> **Good to know** : Next.js backend capabilities are not a full backend replacement. They serve as an API layer that:
> 
>   * is publicly reachable
>   * handles any HTTP request
>   * can return any content type
> 


To implement this pattern, use:

  * [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)
  * [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  * In Pages Router, [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)



## Public Endpoints[](https://nextjs.org/docs/app/guides/backend-for-frontend#public-endpoints)

Route Handlers are public HTTP endpoints. Any client can access them.

Create a Route Handler using the `route.ts` or `route.js` file convention:

/app/api/route.ts

JavaScriptTypeScript
[code]
    export function GET(request: Request) {}
[/code]

This handles `GET` requests sent to `/api`.

Use `try/catch` blocks for operations that may throw an exception:

/app/api/route.ts

JavaScriptTypeScript
[code]
    import { submit } from '@/lib/submit'
     
    export async function POST(request: Request) {
      try {
        await submit(request)
        return new Response(null, { status: 204 })
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected error'
     
        return new Response(message, { status: 500 })
      }
    }
[/code]

Avoid exposing sensitive information in error messages sent to the client.

To restrict access, implement authentication and authorization. See [Authentication](https://nextjs.org/docs/app/guides/authentication).

## Content types[](https://nextjs.org/docs/app/guides/backend-for-frontend#content-types)

Route Handlers let you serve non-UI responses, including JSON, XML, images, files, and plain text.

Next.js uses file conventions for common endpoints:

  * [`sitemap.xml`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  * [`opengraph-image.jpg`, `twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  * [favicon, app icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
  * [`manifest.json`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
  * [`robots.txt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)



You can also define custom ones, such as:

  * `llms.txt`
  * `rss.xml`
  * `.well-known`



For example, `app/rss.xml/route.ts` creates a Route Handler for `rss.xml`.

/app/rss.xml/route.ts

JavaScriptTypeScript
[code]
    export async function GET(request: Request) {
      const rssResponse = await fetch(/* rss endpoint */)
      const rssData = await rssResponse.json()
     
      const rssFeed = `<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
    <channel>
     <title>${rssData.title}</title>
     <description>${rssData.description}</description>
     <link>${rssData.link}</link>
     <copyright>${rssData.copyright}</copyright>
     ${rssData.items.map((item) => {
       return `<item>
        <title>${item.title}</title>
        <description>${item.description}</description>
        <link>${item.link}</link>
        <pubDate>${item.publishDate}</pubDate>
        <guid isPermaLink="false">${item.guid}</guid>
     </item>`
     })}
    </channel>
    </rss>`
     
      const headers = new Headers({ 'content-type': 'application/xml' })
     
      return new Response(rssFeed, { headers })
    }
[/code]

Sanitize any input used to generate markup.

### Consuming request payloads[](https://nextjs.org/docs/app/guides/backend-for-frontend#consuming-request-payloads)

Use Request [instance methods](https://developer.mozilla.org/en-US/docs/Web/API/Request#instance_methods) like `.json()`, `.formData()`, or `.text()` to access the request body.

`GET` and `HEAD` requests don’t carry a body.

/app/api/echo-body/route.ts

JavaScriptTypeScript
[code]
    export async function POST(request: Request) {
      const res = await request.json()
      return Response.json({ res })
    }
[/code]

> **Good to know** : Validate data before passing it to other systems

/app/api/send-email/route.ts

JavaScriptTypeScript
[code]
    import { sendMail, validateInputs } from '@/lib/email-transporter'
     
    export async function POST(request: Request) {
      const formData = await request.formData()
      const email = formData.get('email')
      const contents = formData.get('contents')
     
      try {
        await validateInputs({ email, contents })
        const info = await sendMail({ email, contents })
     
        return Response.json({ messageId: info.messageId })
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected exception'
     
        return new Response(message, { status: 500 })
      }
    }
[/code]

You can only read the request body once. Clone the request if you need to read it again:

/app/api/clone/route.ts

JavaScriptTypeScript
[code]
    export async function POST(request: Request) {
      try {
        const clonedRequest = request.clone()
     
        await request.body()
        await clonedRequest.body()
        await request.body() // Throws error
     
        return new Response(null, { status: 204 })
      } catch {
        return new Response(null, { status: 500 })
      }
    }
[/code]

## Manipulating data[](https://nextjs.org/docs/app/guides/backend-for-frontend#manipulating-data)

Route Handlers can transform, filter, and aggregate data from one or more sources. This keeps logic out of the frontend and avoids exposing internal systems.

You can also offload heavy computations to the server and reduce client battery and data usage.
[code] 
    import { parseWeatherData } from '@/lib/weather'
     
    export async function POST(request: Request) {
      const body = await request.json()
      const searchParams = new URLSearchParams({ lat: body.lat, lng: body.lng })
     
      try {
        const weatherResponse = await fetch(`${weatherEndpoint}?${searchParams}`)
     
        if (!weatherResponse.ok) {
          /* handle error */
        }
     
        const weatherData = await weatherResponse.text()
        const payload = parseWeatherData.asJSON(weatherData)
     
        return new Response(payload, { status: 200 })
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected exception'
     
        return new Response(message, { status: 500 })
      }
    }
[/code]

> **Good to know** : This example uses `POST` to avoid putting geo-location data in the URL. `GET` requests may be cached or logged, which could expose sensitive info.

## Proxying to a backend[](https://nextjs.org/docs/app/guides/backend-for-frontend#proxying-to-a-backend)

You can use a Route Handler as a `proxy` to another backend. Add validation logic before forwarding the request.

/app/api/[...slug]/route.ts

JavaScriptTypeScript
[code]
    import { isValidRequest } from '@/lib/utils'
     
    export async function POST(request: Request, { params }) {
      const clonedRequest = request.clone()
      const isValid = await isValidRequest(clonedRequest)
     
      if (!isValid) {
        return new Response(null, { status: 400, statusText: 'Bad Request' })
      }
     
      const { slug } = await params
      const pathname = slug.join('/')
      const proxyURL = new URL(pathname, 'https://nextjs.org')
      const proxyRequest = new Request(proxyURL, request)
     
      try {
        return fetch(proxyRequest)
      } catch (reason) {
        const message =
          reason instanceof Error ? reason.message : 'Unexpected exception'
     
        return new Response(message, { status: 500 })
      }
    }
[/code]

Or use:

  * `proxy` [rewrites](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy)
  * [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) in `next.config.js`.



## NextRequest and NextResponse[](https://nextjs.org/docs/app/guides/backend-for-frontend#nextrequest-and-nextresponse)

Next.js extends the [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) Web APIs with methods that simplify common operations. These extensions are available in both Route Handlers and Proxy.

Both provide methods for reading and manipulating cookies.

`NextRequest` includes the [`nextUrl`](https://nextjs.org/docs/app/api-reference/functions/next-request#nexturl) property, which exposes parsed values from the incoming request, for example, it makes it easier to access request pathname and search params.

`NextResponse` provides helpers like `next()`, `json()`, `redirect()`, and `rewrite()`.

You can pass `NextRequest` to any function expecting `Request`. Likewise, you can return `NextResponse` where a `Response` is expected.

/app/echo-pathname/route.ts

JavaScriptTypeScript
[code]
    import { type NextRequest, NextResponse } from 'next/server'
     
    export async function GET(request: NextRequest) {
      const nextUrl = request.nextUrl
     
      if (nextUrl.searchParams.get('redirect')) {
        return NextResponse.redirect(new URL('/', request.url))
      }
     
      if (nextUrl.searchParams.get('rewrite')) {
        return NextResponse.rewrite(new URL('/', request.url))
      }
     
      return NextResponse.json({ pathname: nextUrl.pathname })
    }
[/code]

Learn more about [`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request) and [`NextResponse`](https://nextjs.org/docs/app/api-reference/functions/next-response).

## Webhooks and callback URLs[](https://nextjs.org/docs/app/guides/backend-for-frontend#webhooks-and-callback-urls)

Use Route Handlers to receive event notifications from third-party applications.

For example, revalidate a route when content changes in a CMS. Configure the CMS to call a specific endpoint on changes.

/app/webhook/route.ts

JavaScriptTypeScript
[code]
    import { type NextRequest, NextResponse } from 'next/server'
     
    export async function GET(request: NextRequest) {
      const token = request.nextUrl.searchParams.get('token')
     
      if (token !== process.env.REVALIDATE_SECRET_TOKEN) {
        return NextResponse.json({ success: false }, { status: 401 })
      }
     
      const tag = request.nextUrl.searchParams.get('tag')
     
      if (!tag) {
        return NextResponse.json({ success: false }, { status: 400 })
      }
     
      revalidateTag(tag)
     
      return NextResponse.json({ success: true })
    }
[/code]

Callback URLs are another use case. When a user completes a third-party flow, the third party sends them to a callback URL. Use a Route Handler to verify the response and decide where to redirect the user.

/app/auth/callback/route.ts

JavaScriptTypeScript
[code]
    import { type NextRequest, NextResponse } from 'next/server'
     
    export async function GET(request: NextRequest) {
      const token = request.nextUrl.searchParams.get('session_token')
      const redirectUrl = request.nextUrl.searchParams.get('redirect_url')
     
      const response = NextResponse.redirect(new URL(redirectUrl, request.url))
     
      response.cookies.set({
        value: token,
        name: '_token',
        path: '/',
        secure: true,
        httpOnly: true,
        expires: undefined, // session cookie
      })
     
      return response
    }
[/code]

## Redirects[](https://nextjs.org/docs/app/guides/backend-for-frontend#redirects)

app/api/route.ts

JavaScriptTypeScript
[code]
    import { redirect } from 'next/navigation'
     
    export async function GET(request: Request) {
      redirect('https://nextjs.org/')
    }
[/code]

Learn more about redirects in [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect) and [`permanentRedirect`](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)

## Proxy[](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy)

Only one `proxy` file is allowed per project. Use `config.matcher` to target specific paths. Learn more about [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy).

Use `proxy` to generate a response before the request reaches a route path.

proxy.ts

JavaScriptTypeScript
[code]
    import { isAuthenticated } from '@lib/auth'
     
    export const config = {
      matcher: '/api/:function*',
    }
     
    export function proxy(request: Request) {
      if (!isAuthenticated(request)) {
        return Response.json(
          { success: false, message: 'authentication failed' },
          { status: 401 }
        )
      }
    }
[/code]

You can also proxy requests using `proxy`:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
     
    export function proxy(request: Request) {
      if (request.nextUrl.pathname === '/proxy-this-path') {
        const rewriteUrl = new URL('https://nextjs.org')
        return NextResponse.rewrite(rewriteUrl)
      }
    }
[/code]

Another type of response `proxy` can produce are redirects:

proxy.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
     
    export function proxy(request: Request) {
      if (request.nextUrl.pathname === '/v1/docs') {
        request.nextUrl.pathname = '/v2/docs'
        return NextResponse.redirect(request.nextUrl)
      }
    }
[/code]

## Security[](https://nextjs.org/docs/app/guides/backend-for-frontend#security)

### Working with headers[](https://nextjs.org/docs/app/guides/backend-for-frontend#working-with-headers)

Be deliberate about where headers go, and avoid directly passing incoming request headers to the outgoing response.

  * **Upstream request headers** : In Proxy, `NextResponse.next({ request: { headers } })` modifies the headers your server receives and does not expose them to the client.
  * **Response headers** : `new Response(..., { headers })`, `NextResponse.json(..., { headers })`, `NextResponse.next({ headers })`, or `response.headers.set(...)` send headers back to the client. If sensitive values were appended to these headers, they will be visible to clients.



Learn more in [NextResponse headers in Proxy](https://nextjs.org/docs/app/api-reference/functions/next-response#next).

### Rate limiting[](https://nextjs.org/docs/app/guides/backend-for-frontend#rate-limiting)

You can implement rate limiting in your Next.js backend. In addition to code-based checks, enable any rate limiting features provided by your host.

/app/resource/route.ts

JavaScriptTypeScript
[code]
    import { NextResponse } from 'next/server'
    import { checkRateLimit } from '@/lib/rate-limit'
     
    export async function POST(request: Request) {
      const { rateLimited } = await checkRateLimit(request)
     
      if (rateLimited) {
        return NextResponse.json({ error: 'Rate limit exceeded' }, { status: 429 })
      }
     
      return new Response(null, { status: 204 })
    }
[/code]

### Verify payloads[](https://nextjs.org/docs/app/guides/backend-for-frontend#verify-payloads)

Never trust incoming request data. Validate content type and size, and sanitize against XSS before use.

Use timeouts to prevent abuse and protect server resources.

Store user-generated static assets in dedicated services. When possible, upload them from the browser and store the returned URI in your database to reduce request size.

### Access to protected resources[](https://nextjs.org/docs/app/guides/backend-for-frontend#access-to-protected-resources)

Always verify credentials before granting access. Do not rely on proxy alone for authentication and authorization.

Remove sensitive or unnecessary data from responses and backend logs.

Rotate credentials and API keys regularly.

## Preflight Requests[](https://nextjs.org/docs/app/guides/backend-for-frontend#preflight-requests)

Preflight requests use the `OPTIONS` method to ask the server if a request is allowed based on origin, method, and headers.

If `OPTIONS` is not defined, Next.js adds it automatically and sets the `Allow` header based on the other defined methods.

  * [CORS](https://nextjs.org/docs/app/api-reference/file-conventions/route#cors)



## Library patterns[](https://nextjs.org/docs/app/guides/backend-for-frontend#library-patterns)

Community libraries often use the factory pattern for Route Handlers.

/app/api/[...path]/route.ts
[code]
    import { createHandler } from 'third-party-library'
     
    const handler = createHandler({
      /* library-specific options */
    })
     
    export const GET = handler
    // or
    export { handler as POST }
[/code]

This creates a shared handler for `GET` and `POST` requests. The library customizes behavior based on the `method` and `pathname` in the request.

Libraries can also provide a `proxy` factory.

proxy.ts
[code]
    import { createMiddleware } from 'third-party-library'
     
    export default createMiddleware()
[/code]

> **Good to know** : Third-party libraries may still refer to `proxy` as `middleware`.

## More examples[](https://nextjs.org/docs/app/guides/backend-for-frontend#more-examples)

See more examples on using [Router Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route#examples) and the [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#examples) API references.

These examples include, working with [Cookies](https://nextjs.org/docs/app/api-reference/file-conventions/route#cookies), [Headers](https://nextjs.org/docs/app/api-reference/file-conventions/route#headers), [Streaming](https://nextjs.org/docs/app/api-reference/file-conventions/route#streaming), Proxy [negative matching](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#negative-matching), and other useful code snippets.

## Caveats[](https://nextjs.org/docs/app/guides/backend-for-frontend#caveats)

### Server Components[](https://nextjs.org/docs/app/guides/backend-for-frontend#server-components)

Fetch data in Server Components directly from its source, not via Route Handlers.

For Server Components pre-rendered at build time, using Route Handlers will fail the build step. This is because, while building there is no server listening for these requests.

For Server Components rendered on demand, fetching from Route Handlers is slower due to the extra HTTP round trip between the handler and the render process.

> A server side `fetch` request uses absolute URLs. This implies an HTTP round trip, to an external server. During development, your own development server acts as the external server. At build time there is no server, and at runtime, the server is available through your public facing domain.

Server Components cover most data-fetching needs. However, fetching data client side might be necessary for:

  * Data that depends on client-only Web APIs:
    * Geo-location API
    * Storage API
    * Audio API
    * File API
  * Frequently polled data



For these, use community libraries like [`swr`](https://swr.vercel.app/) or [`react-query`](https://tanstack.com/query/latest/docs/framework/react/overview).

### Server Actions[](https://nextjs.org/docs/app/guides/backend-for-frontend#server-actions)

Server Actions let you run server-side code from the client. Their primary purpose is to mutate data from your frontend client.

Server Actions are queued. Using them for data fetching introduces sequential execution.

### `export` mode[](https://nextjs.org/docs/app/guides/backend-for-frontend#export-mode)

`export` mode outputs a static site without a runtime server. Features that require the Next.js runtime are [not supported](https://nextjs.org/docs/app/guides/static-exports#unsupported-features), because this mode produces a static site, and no runtime server.

In `export mode`, only `GET` Route Handlers are supported, in combination with the [`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) route segment config, set to `'force-static'`.

This can be used to generate static HTML, JSON, TXT, or other files.

app/hello-world/route.ts
[code]
    export const dynamic = 'force-static'
     
    export function GET() {
      return new Response('Hello World', { status: 200 })
    }
[/code]

### Deployment environment[](https://nextjs.org/docs/app/guides/backend-for-frontend#deployment-environment)

Some hosts deploy Route Handlers as lambda functions. This means:

  * Route Handlers cannot share data between requests.
  * The environment may not support writing to File System.
  * Long-running handlers may be terminated due to timeouts.
  * WebSockets won’t work because the connection closes on timeout, or after the response is generated.



## API Reference

Learn more about Route Handlers and Proxy

### [route.jsAPI reference for the route.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/route)### [proxy.jsAPI reference for the proxy.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)

Was this helpful?

supported.

Send
