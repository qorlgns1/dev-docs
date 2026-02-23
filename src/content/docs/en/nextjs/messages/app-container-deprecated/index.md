---
title: 'Addressing "App Container Deprecated" Error in Next.js'
description: 'This document guides developers on how to resolve the "App Container Deprecated" error in Next.js by updating their custom App component.'
---

# Addressing "App Container Deprecated" Error in Next.js | Next.js

Source URL: https://nextjs.org/docs/messages/app-container-deprecated

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Addressing "App Container Deprecated" Error in Next.js

# Addressing "App Container Deprecated" Error in Next.js

This document guides developers on how to resolve the "App Container Deprecated" error in Next.js by updating their custom App component.

## Why This Error Occurred[](https://nextjs.org/docs/messages/app-container-deprecated#why-this-error-occurred)

The "App Container Deprecated" error usually occurs when you are using the `<Container>` component in your custom `<App>` (`pages/_app.js`). Prior to version `9.0.4` of Next.js, the `<Container>` component was used to handle scrolling to hashes.

From version `9.0.4` onwards, this functionality was moved up the component tree, rendering the `<Container>` component unnecessary in your custom `<App>`.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/app-container-deprecated#possible-ways-to-fix-it)

To resolve this issue, you need to remove the `<Container>` component from your custom `<App>` (`pages/_app.js`).

**Before**

pages/_app.js
[code]
    import React from 'react'
    import App, { Container } from 'next/app'
     
    class MyApp extends App {
      render() {
        const { Component, pageProps } = this.props
        return (
          <Container>
            <Component {...pageProps} />
          </Container>
        )
      }
    }
     
    export default MyApp
[/code]

**After**

pages/_app.js
[code]
    import React from 'react'
    import App from 'next/app'
     
    class MyApp extends App {
      render() {
        const { Component, pageProps } = this.props
        return <Component {...pageProps} />
      }
    }
     
    export default MyApp
[/code]

After making this change, your custom `<App>` should work as expected without the `<Container>` component.

## Useful Links[](https://nextjs.org/docs/messages/app-container-deprecated#useful-links)

  * [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)



Was this helpful?

supported.

Send
