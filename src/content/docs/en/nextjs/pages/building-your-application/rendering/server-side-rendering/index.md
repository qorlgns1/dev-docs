---
title: 'Rendering: Server-side Rendering (SSR)'
description: 'Last updated February 20, 2026'
---

# Rendering: Server-side Rendering (SSR) | Next.js

Source URL: https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering

[Building Your Application](https://nextjs.org/docs/pages/building-your-application)[Rendering](https://nextjs.org/docs/pages/building-your-application/rendering)Server-side Rendering (SSR)

Copy page

# Server-side Rendering (SSR)

Last updated February 20, 2026

> Also referred to as "SSR" or "Dynamic Rendering".

If a page uses **Server-side Rendering** , the page HTML is generated on **each request**.

To use Server-side Rendering for a page, you need to `export` an `async` function called `getServerSideProps`. This function will be called by the server on every request.

For example, suppose that your page needs to pre-render frequently updated data (fetched from an external API). You can write `getServerSideProps` which fetches this data and passes it to `Page` like below:
[code] 
    export default function Page({ data }) {
      // Render data...
    }
     
    // This gets called on every request
    export async function getServerSideProps() {
      // Fetch data from external API
      const res = await fetch(`https://.../data`)
      const data = await res.json()
     
      // Pass data to the page via props
      return { props: { data } }
    }
[/code]

As you can see, `getServerSideProps` is similar to `getStaticProps`, but the difference is that `getServerSideProps` is run on every request instead of on build time.

To learn more about how `getServerSideProps` works, check out our [Data Fetching documentation](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props).

Was this helpful?

supported.

Send
