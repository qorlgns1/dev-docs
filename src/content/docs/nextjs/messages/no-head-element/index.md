---
title: 'head 요소 없음'
description: '페이지 수준 메타데이터를 포함하기 위해  요소를 사용했지만, 이는 Next.js 애플리케이션에서 예상치 못한 동작을 일으킬 수 있습니다. 대신 Next.js에 내장된  컴포넌트를 사용하세요.'
---

# head 요소 없음 | Next.js

Source URL: https://nextjs.org/docs/messages/no-head-element

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)No Head Element

# head 요소 없음

> `<head>` 요소 사용을 방지하세요.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-head-element#why-this-error-occurred)

페이지 수준 메타데이터를 포함하기 위해 `<head>` 요소를 사용했지만, 이는 Next.js 애플리케이션에서 예상치 못한 동작을 일으킬 수 있습니다. 대신 Next.js에 내장된 `next/head` 컴포넌트를 사용하세요.

## 해결 방법[](https://nextjs.org/docs/messages/no-head-element#possible-ways-to-fix-it)

`<Head />` 컴포넌트를 가져와 사용하세요:

pages/index.js
[code]
    import Head from 'next/head'
     
    function Index() {
      return (
        <>
          <Head>
            <title>My page title</title>
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
          </Head>
        </>
      )
    }
     
    export default Index
[/code]

## 유용한 링크[](https://nextjs.org/docs/messages/no-head-element#useful-links)

  * [next/head](https://nextjs.org/docs/pages/api-reference/components/head)



도움이 되었나요?

지원됨.

보내기
