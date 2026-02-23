---
title: '문서 헤드에 제목 없음'
description: '> 의  컴포넌트에서  사용을 방지하십시오.'
---

# 문서 헤드에 제목 없음 | Next.js

Source URL: https://nextjs.org/docs/messages/no-title-in-document-head

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)문서 헤드에 제목 없음

# 문서 헤드에 제목 없음

> `next/document`의 `Head` 컴포넌트에서 `<title>` 사용을 방지하십시오.

## 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-title-in-document-head#why-this-error-occurred)

`next/document`에서 가져온 `Head` 컴포넌트 내부에 `<title>` 요소를 정의했는데, 이 컴포넌트는 모든 페이지에 공통인 `<head>` 코드에만 사용해야 합니다. 대신 페이지 수준에서는 `next/head`를 사용해 제목 태그를 정의해야 합니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-title-in-document-head#possible-ways-to-fix-it)

페이지나 컴포넌트 내에서 `next/head`를 임포트하여 페이지 제목을 정의하십시오:

pages/index.js
[code]
    import Head from 'next/head'
     
    export function Home() {
      return (
        <div>
          <Head>
            <title>My page title</title>
          </Head>
        </div>
      )
    }
[/code]

## 유용한 링크[](https://nextjs.org/docs/messages/no-title-in-document-head#useful-links)

  * [next/head](https://nextjs.org/docs/pages/api-reference/components/head)
  * [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)



도움이 되었나요?

지원됨.

보내기
