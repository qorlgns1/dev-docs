---
title: 'File-system conventions: Parallel Routes'
description: 'Parallel Routes allows you to simultaneously or conditionally render one or more pages within the same layout. They are useful for highly dynamic sect...'
---

# File-system conventions: Parallel Routes | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)Parallel Routes

Copy page

# Parallel Routes

Last updated February 20, 2026

Parallel Routes allows you to simultaneously or conditionally render one or more pages within the same layout. They are useful for highly dynamic sections of an app, such as dashboards and feeds on social sites.

For example, considering a dashboard, you can use parallel routes to simultaneously render the `team` and `analytics` pages:

## Convention[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#convention)

### Slots[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#slots)

Parallel routes are created using named **slots**. Slots are defined with the `@folder` convention. For example, the following file structure defines two slots: `@analytics` and `@team`:

Slots are passed as props to the shared parent layout. For the example above, the component in `app/layout.js` now accepts the `@analytics` and `@team` slots props, and can render them in parallel alongside the `children` prop:

app/layout.tsx

JavaScriptTypeScript
[code]
    export default function Layout({
      children,
      team,
      analytics,
    }: {
      children: React.ReactNode
      analytics: React.ReactNode
      team: React.ReactNode
    }) {
      return (
        <>
          {children}
          {team}
          {analytics}
        </>
      )
    }
[/code]

However, slots are **not** route segments and do not affect the URL structure. For example, for `/@analytics/views`, the URL will be `/views` since `@analytics` is a slot. Slots are combined with the regular [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page) component to form the final page associated with the route segment. Because of this, you cannot have separate [static](https://nextjs.org/docs/app/guides/caching#static-rendering) and [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) slots at the same route segment level. If one slot is dynamic, all slots at that level must be dynamic.

> **Good to know** :
> 
>   * The `children` prop is an implicit slot that does not need to be mapped to a folder. This means `app/page.js` is equivalent to `app/@children/page.js`.
> 


### `default.js`[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#defaultjs)

You can define a `default.js` file to render as a fallback for unmatched slots during the initial load or full-page reload.

Consider the following folder structure. The `@team` slot has a `/settings` page, but `@analytics` does not.

When navigating to `/settings`, the `@team` slot will render the `/settings` page while maintaining the currently active page for the `@analytics` slot.

On refresh, Next.js will render a `default.js` for `@analytics`. If `default.js` doesn't exist, a `404` is rendered instead.

Additionally, since `children` is an implicit slot, you also need to create a `default.js` file to render a fallback for `children` when Next.js cannot recover the active state of the parent page.

## Behavior[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#behavior)

By default, Next.js keeps track of the active _state_ (or subpage) for each slot. However, the content rendered within a slot will depend on the type of navigation:

  * [**Soft Navigation**](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions): During client-side navigation, Next.js will perform a [partial render](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions), changing the subpage within the slot, while maintaining the other slot's active subpages, even if they don't match the current URL.
  * **Hard Navigation** : After a full-page load (browser refresh), Next.js cannot determine the active state for the slots that don't match the current URL. Instead, it will render a [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#defaultjs) file for the unmatched slots, or `404` if `default.js` doesn't exist.



> **Good to know** :
> 
>   * The `404` for unmatched routes helps ensure that you don't accidentally render a parallel route on a page that it was not intended for.
> 


## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#examples)

### With `useSelectedLayoutSegment(s)`[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#with-useselectedlayoutsegments)

Both [`useSelectedLayoutSegment`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment) and [`useSelectedLayoutSegments`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments) accept a `parallelRoutesKey` parameter, which allows you to read the active route segment within a slot.

app/layout.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useSelectedLayoutSegment } from 'next/navigation'
     
    export default function Layout({ auth }: { auth: React.ReactNode }) {
      const loginSegment = useSelectedLayoutSegment('auth')
      // ...
    }
[/code]

When a user navigates to `app/@auth/login` (or `/login` in the URL bar), `loginSegment` will be equal to the string `"login"`.

### Conditional Routes[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#conditional-routes)

You can use Parallel Routes to conditionally render routes based on certain conditions, such as user role. For example, to render a different dashboard page for the `/admin` or `/user` roles:

app/dashboard/layout.tsx

JavaScriptTypeScript
[code]
    import { checkUserRole } from '@/lib/auth'
     
    export default function Layout({
      user,
      admin,
    }: {
      user: React.ReactNode
      admin: React.ReactNode
    }) {
      const role = checkUserRole()
      return role === 'admin' ? admin : user
    }
[/code]

### Tab Groups[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#tab-groups)

You can add a `layout` inside a slot to allow users to navigate the slot independently. This is useful for creating tabs.

For example, the `@analytics` slot has two subpages: `/page-views` and `/visitors`.

Within `@analytics`, create a [`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) file to share the tabs between the two pages:

app/@analytics/layout.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <>
          <nav>
            <Link href="/page-views">Page Views</Link>
            <Link href="/visitors">Visitors</Link>
          </nav>
          <div>{children}</div>
        </>
      )
    }
[/code]

### Modals[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#modals)

Parallel Routes can be used together with [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes) to create modals that support deep linking. This allows you to solve common challenges when building modals, such as:

  * Making the modal content **shareable through a URL**.
  * **Preserving context** when the page is refreshed, instead of closing the modal.
  * **Closing the modal on backwards navigation** rather than going to the previous route.
  * **Reopening the modal on forwards navigation**.



Consider the following UI pattern, where a user can open a login modal from a layout using client-side navigation, or access a separate `/login` page:

To implement this pattern, start by creating a `/login` route that renders your **main** login page.

app/login/page.tsx

JavaScriptTypeScript
[code]
    import { Login } from '@/app/ui/login'
     
    export default function Page() {
      return <Login />
    }
[/code]

Then, inside the `@auth` slot, add [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default) file that returns `null`. This ensures that the modal is not rendered when it's not active.

app/@auth/default.tsx

JavaScriptTypeScript
[code]
    export default function Default() {
      return null
    }
[/code]

Inside your `@auth` slot, intercept the `/login` route by importing the `<Modal>` component and its children into the `@auth/(.)login/page.tsx` file, and updating the folder name to `/@auth/(.)login/page.tsx`.

app/@auth/(.)login/page.tsx

JavaScriptTypeScript
[code]
    import { Modal } from '@/app/ui/modal'
    import { Login } from '@/app/ui/login'
     
    export default function Page() {
      return (
        <Modal>
          <Login />
        </Modal>
      )
    }
[/code]

> **Good to know:**
> 
>   * The convention `(.)` is used for intercepting routes. See [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) docs for more information.
>   * By separating the `<Modal>` functionality from the modal content (`<Login>`), you can ensure any content inside the modal, e.g. [forms](https://nextjs.org/docs/app/guides/forms), are Server Components. See [Interleaving Client and Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples#supported-pattern-passing-server-components-to-client-components-as-props) for more information.
> 


#### Opening the modal[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#opening-the-modal)

Now, you can leverage the Next.js router to open and close the modal. This ensures the URL is correctly updated when the modal is open, and when navigating backwards and forwards.

To open the modal, pass the `@auth` slot as a prop to the parent layout and render it alongside the `children` prop.

app/layout.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export default function Layout({
      auth,
      children,
    }: {
      auth: React.ReactNode
      children: React.ReactNode
    }) {
      return (
        <>
          <nav>
            <Link href="/login">Open modal</Link>
          </nav>
          <div>{auth}</div>
          <div>{children}</div>
        </>
      )
    }
[/code]

When the user clicks the `<Link>`, the modal will open instead of navigating to the `/login` page. However, on refresh or initial load, navigating to `/login` will take the user to the main login page.

#### Closing the modal[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#closing-the-modal)

You can close the modal by calling `router.back()` or by using the `Link` component.

app/ui/modal.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useRouter } from 'next/navigation'
     
    export function Modal({ children }: { children: React.ReactNode }) {
      const router = useRouter()
     
      return (
        <>
          <button
            onClick={() => {
              router.back()
            }}
          >
            Close modal
          </button>
          <div>{children}</div>
        </>
      )
    }
[/code]

When using the `Link` component to navigate away from a page that shouldn't render the `@auth` slot anymore, we need to make sure the parallel route matches to a component that returns `null`. For example, when navigating back to the root page, we create a `@auth/page.tsx` component:

app/ui/modal.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
     
    export function Modal({ children }: { children: React.ReactNode }) {
      return (
        <>
          <Link href="/">Close modal</Link>
          <div>{children}</div>
        </>
      )
    }
[/code]

app/@auth/page.tsx

JavaScriptTypeScript
[code]
    export default function Page() {
      return null
    }
[/code]

Or if navigating to any other page (such as `/foo`, `/foo/bar`, etc), you can use a catch-all slot:

app/@auth/[...catchAll]/page.tsx

JavaScriptTypeScript
[code]
    export default function CatchAll() {
      return null
    }
[/code]

> **Good to know:**
> 
>   * We use a catch-all route in our `@auth` slot to close the modal because of how parallel routes behave. Since client-side navigations to a route that no longer match the slot will remain visible, we need to match the slot to a route that returns `null` to close the modal.
>   * Other examples could include opening a photo modal in a gallery while also having a dedicated `/photo/[id]` page, or opening a shopping cart in a side modal.
>   * [View an example](https://github.com/vercel-labs/nextgram) of modals with Intercepted and Parallel Routes.
> 


### Loading and Error UI[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#loading-and-error-ui)

Parallel Routes can be streamed independently, allowing you to define independent error and loading states for each route:

See the [Loading UI](https://nextjs.org/docs/app/api-reference/file-conventions/loading) and [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling) documentation for more information.

## 

### [default.jsAPI Reference for the default.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/default)

Was this helpful?

supported.

Send
