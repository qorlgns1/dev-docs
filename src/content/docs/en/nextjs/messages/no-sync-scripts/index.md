---
title: 'No Sync Scripts'
description: '> Prevent synchronous scripts.'
---

# No Sync Scripts | Next.js

Source URL: https://nextjs.org/docs/messages/no-sync-scripts

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No Sync Scripts

# No Sync Scripts

> Prevent synchronous scripts.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-sync-scripts#why-this-error-occurred)

A synchronous script was used which can impact your webpage performance.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-sync-scripts#possible-ways-to-fix-it)

### Script component (recommended)[](https://nextjs.org/docs/messages/no-sync-scripts#script-component-recommended)

pages/index.js
[code]
    import Script from 'next/script'
     
    function Home() {
      return (
        <div class="container">
          <Script src="https://third-party-script.js"></Script>
          <div>Home Page</div>
        </div>
      )
    }
     
    export default Home
[/code]

### Use `async` or `defer`[](https://nextjs.org/docs/messages/no-sync-scripts#use-async-or-defer)
[code] 
    <script src="https://third-party-script.js" async />
    <script src="https://third-party-script.js" defer />
[/code]

## Useful Links[](https://nextjs.org/docs/messages/no-sync-scripts#useful-links)

  * [Efficiently load third-party JavaScript](https://web.dev/efficiently-load-third-party-javascript/)



Was this helpful?

supported.

Send
