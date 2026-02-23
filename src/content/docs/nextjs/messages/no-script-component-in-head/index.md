---
title: '헤드에서 Script 컴포넌트 사용 금지'
description: '>  컴포넌트 안에서는 를 사용하지 마세요.'
---

# 헤드에서 Script 컴포넌트 사용 금지 | Next.js

Source URL: https://nextjs.org/docs/messages/no-script-component-in-head

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)헤드에서 Script 컴포넌트 사용 금지

# 헤드에서 Script 컴포넌트 사용 금지

> `next/head` 컴포넌트 안에서는 `next/script`를 사용하지 마세요.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-script-component-in-head#why-this-error-occurred)

`next/script` 컴포넌트는 `next/head` 컴포넌트 안에서 사용하면 안 됩니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/no-script-component-in-head#possible-ways-to-fix-it)

`<Script />` 컴포넌트를 `<Head>` 바깥으로 옮기면 됩니다.

**변경 전**

pages/index.js
```
    import Script from 'next/script'
    import Head from 'next/head'

    export default function Index() {
      return (
        <Head>
          <title>Next.js</title>
          <Script src="/my-script.js" />
        </Head>
      )
    }
```

**변경 후**

pages/index.js
```
    import Script from 'next/script'
    import Head from 'next/head'

    export default function Index() {
      return (
        <>
          <Head>
            <title>Next.js</title>
          </Head>
          <Script src="/my-script.js" />
        </>
      )
    }
```

## 유용한 링크[](https://nextjs.org/docs/messages/no-script-component-in-head#useful-links)

  * [next/head](https://nextjs.org/docs/pages/api-reference/components/head)
  * [next/script](https://nextjs.org/docs/pages/guides/scripts)

supported.

Send