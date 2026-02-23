---
title: 'No CSS Tags'
description: '> Prevent manual stylesheet tags.'
---

# No CSS Tags | Next.js

Source URL: https://nextjs.org/docs/messages/no-css-tags

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No CSS Tags

# No CSS Tags

> Prevent manual stylesheet tags.

## Why This Error Occurred[](https://nextjs.org/docs/messages/no-css-tags#why-this-error-occurred)

A `link` element was used to link to an external stylesheet. This can negatively affect CSS resource loading on your webpage.

## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-css-tags#possible-ways-to-fix-it)

There are multiple ways to include styles using Next.js' built-in CSS support, including the option to use `@import` within the root stylesheet that is imported in `pages/_app.js`:

styles.css
[code]
    /* Root stylesheet */
    @import 'extra.css';
     
    body {
      /* ... */
    }
[/code]

Another option is to use CSS Modules to import the CSS file scoped specifically to the component.

pages/index.js
[code]
    import styles from './extra.module.css'
     
    export class Home {
      render() {
        return (
          <div>
            <button type="button" className={styles.active}>
              Open
            </button>
          </div>
        )
      }
    }
[/code]

Refer to the [Built-In CSS Support](https://nextjs.org/docs/app/getting-started/css) documentation to learn about all the ways to include CSS to your application.

Was this helpful?

supported.

Send
