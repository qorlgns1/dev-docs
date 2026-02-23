---
title: 'next.config.js: env'
description: "This is a legacy API and no longer recommended. It's still supported for backward compatibility."
---

# next.config.js: env | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/env

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)env

Copy page

# env

This is a legacy API and no longer recommended. It's still supported for backward compatibility.

Last updated February 20, 2026

> Since the release of [Next.js 9.4](https://nextjs.org/blog/next-9-4) we now have a more intuitive and ergonomic experience for [adding environment variables](https://nextjs.org/docs/app/guides/environment-variables). Give it a try!

> **Good to know** : environment variables specified in this way will **always** be included in the JavaScript bundle, prefixing the environment variable name with `NEXT_PUBLIC_` only has an effect when specifying them [through the environment or .env files](https://nextjs.org/docs/app/guides/environment-variables).

To add environment variables to the JavaScript bundle, open `next.config.js` and add the `env` config:

next.config.js
[code]
    module.exports = {
      env: {
        customKey: 'my-value',
      },
    }
[/code]

Now you can access `process.env.customKey` in your code. For example:
[code] 
    function Page() {
      return <h1>The value of customKey is: {process.env.customKey}</h1>
    }
     
    export default Page
[/code]

Next.js will replace `process.env.customKey` with `'my-value'` at build time. Trying to destructure `process.env` variables won't work due to the nature of webpack [DefinePlugin](https://webpack.js.org/plugins/define-plugin/).

For example, the following line:
[code] 
    return <h1>The value of customKey is: {process.env.customKey}</h1>
[/code]

Will end up being:
[code] 
    return <h1>The value of customKey is: {'my-value'}</h1>
[/code]

Was this helpful?

supported.

Send
