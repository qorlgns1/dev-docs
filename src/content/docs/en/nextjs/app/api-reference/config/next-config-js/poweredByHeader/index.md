---
title: 'poweredByHeader'
description: 'By default Next.js will add the  header. To opt-out of it, open  and disable the  config:'
---

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader

# poweredByHeader

By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

```js filename="next.config.js"
module.exports = {
  poweredByHeader: false,
}
```
---
