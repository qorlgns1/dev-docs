---
title: 'Components: Head'
description: 'Last updated February 20, 2026'
---

# Components: Head | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/components/head

[API Reference](https://nextjs.org/docs/pages/api-reference)[Components](https://nextjs.org/docs/pages/api-reference/components)Head

Copy page

# Head

Last updated February 20, 2026

We expose a built-in component for appending elements to the `head` of the page:
[code] 
    import Head from 'next/head'
     
    function IndexPage() {
      return (
        <div>
          <Head>
            <title>My page title</title>
          </Head>
          <p>Hello world!</p>
        </div>
      )
    }
     
    export default IndexPage
[/code]

## Avoid duplicated tags[](https://nextjs.org/docs/pages/api-reference/components/head#avoid-duplicated-tags)

To avoid duplicate tags in your `head` you can use the `key` property, which will make sure the tag is only rendered once, as in the following example:
[code] 
    import Head from 'next/head'
     
    function IndexPage() {
      return (
        <div>
          <Head>
            <title>My page title</title>
            <meta property="og:title" content="My page title" key="title" />
          </Head>
          <Head>
            <meta property="og:title" content="My new title" key="title" />
          </Head>
          <p>Hello world!</p>
        </div>
      )
    }
     
    export default IndexPage
[/code]

In this case only the second `<meta property="og:title" />` is rendered. `meta` tags with duplicate `key` attributes are automatically handled.

> **Good to know** : `<title>` and `<base>` tags are automatically checked for duplicates by Next.js, so using key is not necessary for these tags.

> The contents of `head` get cleared upon unmounting the component, so make sure each page completely defines what it needs in `head`, without making assumptions about what other pages added.

## Use minimal nesting[](https://nextjs.org/docs/pages/api-reference/components/head#use-minimal-nesting)

`title`, `meta` or any other elements (e.g. `script`) need to be contained as **direct** children of the `Head` element, or wrapped into maximum one level of `<React.Fragment>` or arrays—otherwise the tags won't be correctly picked up on client-side navigations.

## Use `next/script` for scripts[](https://nextjs.org/docs/pages/api-reference/components/head#use-nextscript-for-scripts)

We recommend using [`next/script`](https://nextjs.org/docs/pages/guides/scripts) in your component instead of manually creating a `<script>` in `next/head`.

## No `html` or `body` tags[](https://nextjs.org/docs/pages/api-reference/components/head#no-html-or-body-tags)

You **cannot** use `<Head>` to set attributes on `<html>` or `<body>` tags. This will result in an `next-head-count is missing` error. `next/head` can only handle tags inside the HTML `<head>` tag.

Was this helpful?

supported.

Send
