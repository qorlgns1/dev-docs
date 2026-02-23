---
title: '구성 요소: Head'
description: '다음과 같이 페이지의 에 요소를 추가하는 내장 컴포넌트를 제공합니다:'
---

# 구성 요소: Head | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/components/head

Copy page

# Head

마지막 업데이트 2026년 2월 20일

다음과 같이 페이지의 `head`에 요소를 추가하는 내장 컴포넌트를 제공합니다:
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

## 중복 태그 피하기[](https://nextjs.org/docs/pages/api-reference/components/head#avoid-duplicated-tags)

`head`에서 태그가 중복되지 않도록 `key` 속성을 사용하면 태그가 한 번만 렌더링되도록 보장합니다. 다음 예제를 참고하세요:
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

이 경우 두 번째 `<meta property="og:title" />`만 렌더링됩니다. 중복된 `key` 속성을 가진 `meta` 태그는 자동으로 처리됩니다.

> **알아두면 좋아요**: `<title>`과 `<base>` 태그는 Next.js가 자동으로 중복 여부를 확인하므로, 이 태그들에는 key를 사용할 필요가 없습니다.

> 컴포넌트가 언마운트되면 `head`의 내용이 모두 제거되므로, 각 페이지는 다른 페이지가 추가한 내용을 가정하지 말고 필요한 `head` 내용을 완전히 정의해야 합니다.

## 최소한의 중첩 사용[](https://nextjs.org/docs/pages/api-reference/components/head#use-minimal-nesting)

`title`, `meta` 또는 다른 요소들(예: `script`)은 반드시 `Head` 요소의 **직접** 자식이거나 `<React.Fragment>` 혹은 배열로 한 번만 감싸져야 합니다. 그렇지 않으면 클라이언트 측 내비게이션에서 태그가 제대로 감지되지 않습니다.

## 스크립트에는 `next/script` 사용[](https://nextjs.org/docs/pages/api-reference/components/head#use-nextscript-for-scripts)

컴포넌트에서 `next/head`로 직접 `<script>`를 만드는 대신 [`next/script`](https://nextjs.org/docs/pages/guides/scripts)를 사용하는 것을 권장합니다.

## `html` 또는 `body` 태그 금지[](https://nextjs.org/docs/pages/api-reference/components/head#no-html-or-body-tags)

`<Head>`를 사용해 `<html>` 또는 `<body>` 태그에 속성을 설정할 수 **없습니다**. 이렇게 하면 `next-head-count is missing` 오류가 발생합니다. `next/head`는 HTML `<head>` 태그 내부의 태그만 처리할 수 있습니다.

Was this helpful?

supported.

Send
