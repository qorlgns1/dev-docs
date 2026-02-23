---
title: 'next/dynamic has deprecated loading multiple modules at once'
description: "The ability to load multiple modules at once has been deprecated in  to be closer to React's implementation ( and )."
---

# `next/dynamic` has deprecated loading multiple modules at once | Next.js

Source URL: https://nextjs.org/docs/messages/next-dynamic-modules

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)`next/dynamic` has deprecated loading multiple modules at once

# `next/dynamic` has deprecated loading multiple modules at once

## Why This Error Occurred[](https://nextjs.org/docs/messages/next-dynamic-modules#why-this-error-occurred)

The ability to load multiple modules at once has been deprecated in `next/dynamic` to be closer to React's implementation (`React.lazy` and `Suspense`).

Updating code that relies on this behavior is relatively straightforward! We've provided an example of a before/after to help you migrate your application:

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/next-dynamic-modules#possible-ways-to-fix-it)

Migrate to using separate dynamic calls for each module.

**Before**

example.js
[code]
    import dynamic from 'next/dynamic'
     
    const HelloBundle = dynamic({
      modules: () => {
        const components = {
          Hello1: () => import('../components/hello1').then((m) => m.default),
          Hello2: () => import('../components/hello2').then((m) => m.default),
        }
     
        return components
      },
      render: (props, { Hello1, Hello2 }) => (
        <div>
          <h1>{props.title}</h1>
          <Hello1 />
          <Hello2 />
        </div>
      ),
    })
     
    function DynamicBundle() {
      return <HelloBundle title="Dynamic Bundle" />
    }
     
    export default DynamicBundle
[/code]

**After**

example.js
[code]
    import dynamic from 'next/dynamic'
     
    const Hello1 = dynamic(() => import('../components/hello1'))
    const Hello2 = dynamic(() => import('../components/hello2'))
     
    function HelloBundle({ title }) {
      return (
        <div>
          <h1>{title}</h1>
          <Hello1 />
          <Hello2 />
        </div>
      )
    }
     
    function DynamicBundle() {
      return <HelloBundle title="Dynamic Bundle" />
    }
     
    export default DynamicBundle
[/code]

Was this helpful?

supported.

Send
