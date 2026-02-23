---
title: '페이지용 HTML 링크 없음'
description: '원본 URL: https://nextjs.org/docs/messages/no-html-link-for-pages'
---

# 페이지용 HTML 링크 없음 | Next.js

원본 URL: https://nextjs.org/docs/messages/no-html-link-for-pages

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)No HTML link for pages

# 페이지용 HTML 링크 없음

> 내부 Next.js 페이지로 이동할 때 `<a>` 요소 사용을 방지하세요.

## 왜 이 오류가 발생했나요[](https://nextjs.org/docs/messages/no-html-link-for-pages#why-this-error-occurred)

`next/link` 컴포넌트를 사용하지 않고 페이지 경로로 이동하려고 `<a>` 요소를 사용하면 불필요한 전체 페이지 새로 고침이 발생합니다.

`Link` 컴포넌트는 페이지 간 클라이언트 전환을 활성화하고 단일 페이지 앱 경험을 제공하기 위해 필수입니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-html-link-for-pages#possible-ways-to-fix-it)

`Link` 컴포넌트를 반드시 import하고, 다른 페이지 경로로 이동하는 앵커 요소를 감싸세요.

**변경 전:**

pages/index.js
```
    function Home() {
      return (
        <div>
          <a href="/about">About Us</a>
        </div>
      )
    }
```

**변경 후:**

pages/index.js
```
    import Link from 'next/link'

    function Home() {
      return (
        <div>
          <Link href="/about">About Us</Link>
        </div>
      )
    }

    export default Home
```

### 옵션[](https://nextjs.org/docs/messages/no-html-link-for-pages#options)

#### `pagesDir`[](https://nextjs.org/docs/messages/no-html-link-for-pages#pagesdir)

이 규칙은 일반적으로 `pages` 디렉터리를 자동으로 찾을 수 있습니다.

모노레포에서 작업 중이라면 `pages` 디렉터리를 찾기 위해 `pagesDir`이 사용하는 [`rootDir`](https://nextjs.org/docs/pages/api-reference/config/eslint#specifying-a-root-directory-within-a-monorepo) 설정을 `eslint-plugin-next`에 구성하는 것이 좋습니다.

일부 경우에는 `pages` 디렉터리를 직접 지정하여 이 규칙을 구성해야 할 수도 있습니다. 단일 경로나 경로 배열을 제공할 수 있습니다.

eslint.config.json
```
    {
      "rules": {
        "@next/next/no-html-link-for-pages": ["error", "packages/my-app/pages/"]
      }
    }
```

## 유용한 링크[](https://nextjs.org/docs/messages/no-html-link-for-pages#useful-links)

  * [next/link API Reference](https://nextjs.org/docs/pages/api-reference/components/link)

보내기