---
title: 'Guides: Sass'
description: 'Next.js has built-in support for integrating with Sass after the package is installed using both the  and  extensions. You can use component-level Sas...'
---

# Guides: Sass | Next.js

Source URL: https://nextjs.org/docs/pages/guides/sass

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)Sass

Copy page

# How to use Sass in Next.js

Last updated February 20, 2026

Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss`or `.module.sass` extension.

First, install [`sass`](https://github.com/sass/sass):

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D sass
[/code]

> **Good to know** :
> 
> Sass supports [two different syntaxes](https://sass-lang.com/documentation/syntax), each with their own extension. The `.scss` extension requires you use the [SCSS syntax](https://sass-lang.com/documentation/syntax#scss), while the `.sass` extension requires you use the [Indented Syntax ("Sass")](https://sass-lang.com/documentation/syntax#the-indented-syntax).
> 
> If you're not sure which to choose, start with the `.scss` extension which is a superset of CSS, and doesn't require you learn the Indented Syntax ("Sass").

### Customizing Sass Options[](https://nextjs.org/docs/pages/guides/sass#customizing-sass-options)

If you want to configure your Sass options, use `sassOptions` in `next.config`.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      sassOptions: {
        additionalData: `$var: red;`,
      },
    }
     
    export default nextConfig
[/code]

#### Implementation[](https://nextjs.org/docs/pages/guides/sass#implementation)

You can use the `implementation` property to specify the Sass implementation to use. By default, Next.js uses the [`sass`](https://www.npmjs.com/package/sass) package.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      sassOptions: {
        implementation: 'sass-embedded',
      },
    }
     
    export default nextConfig
[/code]

### Sass Variables[](https://nextjs.org/docs/pages/guides/sass#sass-variables)

Next.js supports Sass variables exported from CSS Module files.

For example, using the exported `primaryColor` Sass variable:

app/variables.module.scss
[code]
    $primary-color: #64ff00;
     
    :export {
      primaryColor: $primary-color;
    }
[/code]

pages/_app.js
[code]
    import variables from '../styles/variables.module.scss'
     
    export default function MyApp({ Component, pageProps }) {
      return (
        <Layout color={variables.primaryColor}>
          <Component {...pageProps} />
        </Layout>
      )
    }
[/code]

Was this helpful?

supported.

Send
