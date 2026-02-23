---
title: 'File-system conventions: template.js'
description: 'A template file is similar to a layout in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are...'
---

# File-system conventions: template.js | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/template

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)template.js

Copy page

# template.js

Last updated February 20, 2026

A **template** file is similar to a [layout](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-layout) in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are given a unique key, meaning children Client Components reset their state on navigation.

They are useful when you need to:

  * Resynchronize `useEffect` on navigation.
  * Reset the state of a child Client Components on navigation. For example, an input field.
  * To change default framework behavior. For example, Suspense boundaries inside layouts only show a fallback on first load, while templates show it on every navigation.



## Convention[](https://nextjs.org/docs/app/api-reference/file-conventions/template#convention)

A template can be defined by exporting a default React component from a `template.js` file. The component should accept a `children` prop.

app/template.tsx

JavaScriptTypeScript
[code]
    export default function Template({ children }: { children: React.ReactNode }) {
      return <div>{children}</div>
    }
[/code]

In terms of nesting, `template.js` is rendered between a layout and its children. Here's a simplified output:

Output
[code]
    <Layout>
      {/* Note that the template is given a unique key. */}
      <Template key={routeParam}>{children}</Template>
    </Layout>
[/code]

## Props[](https://nextjs.org/docs/app/api-reference/file-conventions/template#props)

### `children` (required)[](https://nextjs.org/docs/app/api-reference/file-conventions/template#children-required)

Template accepts a `children` prop.

Output
[code]
    <Layout>
      {/* Note that the template is automatically given a unique key. */}
      <Template key={routeParam}>{children}</Template>
    </Layout>
[/code]

## Behavior[](https://nextjs.org/docs/app/api-reference/file-conventions/template#behavior)

  * **Server Components** : By default, templates are Server Components.
  * **With navigation** : Templates receive a unique key for their own segment level. They remount when that segment (including its dynamic params) changes. Navigations within deeper segments do not remount higher-level templates. Search params do not trigger remounts.
  * **State reset** : Any Client Component inside the template will reset its state on navigation.
  * **Effect re-run** : Effects like `useEffect` will re-synchronize as the component remounts.
  * **DOM reset** : DOM elements inside the template are fully recreated.



### Templates during navigation and remounting[](https://nextjs.org/docs/app/api-reference/file-conventions/template#templates-during-navigation-and-remounting)

This section illustrates how templates behave during navigation. It shows, step by step, which templates remount on each route change and why.

Using this project tree:
[code] 
    app
    ├── about
    │   ├── page.tsx
    ├── blog
    │   ├── [slug]
    │   │   └── page.tsx
    │   ├── page.tsx
    │   └── template.tsx
    ├── layout.tsx
    ├── page.tsx
    └── template.tsx
    
[/code]

Starting at `/`, the React tree looks roughly like this.

> Note: The `key` values shown in the examples are illustrative, the values in your application may differ.

Output
[code]
    <RootLayout>
      {/* app/template.tsx */}
      <Template key="/">
        <Page />
      </Template>
    </RootLayout>
[/code]

Navigating to `/about` (first segment changes), the root template key changes, it remounts:

Output
[code]
    <RootLayout>
      {/* app/template.tsx */}
      <Template key="/about">
        <AboutPage />
      </Template>
    </RootLayout>
[/code]

Navigating to `/blog` (first segment changes), the root template key changes, it remounts and the blog-level template mounts:

Output
[code]
    <RootLayout>
      {/* app/template.tsx (root) */}
      <Template key="/blog">
        {/* app/blog/template.tsx */}
        <Template key="/blog">
          <BlogIndexPage />
        </Template>
      </Template>
    </RootLayout>
[/code]

Navigating within the same first segment to `/blog/first-post` (child segment changes), the root template key doesn't change, but the blog-level template key changes, it remounts:

Output
[code]
    <RootLayout>
      {/* app/template.tsx (root) */}
      <Template key="/blog">
        {/* app/blog/template.tsx */}
        {/* remounts because the child segment at this level changed */}
        <Template key="/blog/first-post">
          <BlogPostPage slug="first-post" />
        </Template>
      </Template>
    </RootLayout>
[/code]

Navigating to `/blog/second-post` (same first segment, different child segment), the root template key doesn't change, but the blog-level template key changes, it remounts again:

Output
[code]
    <RootLayout>
      {/* app/template.tsx (root) */}
      <Template key="/blog">
        {/* app/blog/template.tsx */}
        {/* remounts again due to changed child segment */}
        <Template key="/blog/second-post">
          <BlogPostPage slug="second-post" />
        </Template>
      </Template>
    </RootLayout>
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/file-conventions/template#version-history)

Version| Changes  
---|---  
`v13.0.0`| `template` introduced.  
  
Was this helpful?

supported.

Send
