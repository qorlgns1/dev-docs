---
title: '라우팅: 사용자 정의 오류'
description: '404 페이지는 자주 접근될 수 있습니다. 방문마다 오류 페이지를 서버 렌더링하면 Next.js 서버의 부하가 증가하여 비용 증가와 느린 경험으로 이어질 수 있습니다.'
---

# 라우팅: 사용자 정의 오류 | Next.js

소스 URL: https://nextjs.org/docs/pages/building-your-application/routing/custom-error

[애플리케이션 빌드](https://nextjs.org/docs/pages/building-your-application)[라우팅](https://nextjs.org/docs/pages/building-your-application/routing)사용자 정의 오류

# 사용자 정의 오류

마지막 업데이트 2026년 2월 20일

## 404 페이지[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)

404 페이지는 자주 접근될 수 있습니다. 방문마다 오류 페이지를 서버 렌더링하면 Next.js 서버의 부하가 증가하여 비용 증가와 느린 경험으로 이어질 수 있습니다.

위와 같은 문제를 피하기 위해 Next.js는 별도의 파일을 추가하지 않아도 기본적으로 정적 404 페이지를 제공합니다.

### 404 페이지 사용자 정의[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#customizing-the-404-page)

사용자 정의 404 페이지를 만들려면 `pages/404.js` 파일을 생성하면 됩니다. 이 파일은 빌드 시점에 정적으로 생성됩니다.

pages/404.js
```
    export default function Custom404() {
      return <h1>404 - Page Not Found</h1>
    }
```

> **알아두세요** : 빌드 타임에 데이터를 가져올 필요가 있다면 이 페이지 안에서 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)를 사용할 수 있습니다.

## 500 페이지[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#500-page)

방문마다 오류 페이지를 서버 렌더링하면 오류 응답 처리의 복잡도가 높아집니다. 사용자가 가능한 한 빠르게 오류 응답을 받도록 돕기 위해 Next.js는 별도의 파일을 추가하지 않아도 기본적으로 정적 500 페이지를 제공합니다.

### 500 페이지 사용자 정의[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#customizing-the-500-page)

500 페이지를 사용자 정의하려면 `pages/500.js` 파일을 생성하면 됩니다. 이 파일은 빌드 시점에 정적으로 생성됩니다.

pages/500.js
```
    export default function Custom500() {
      return <h1>500 - Server-side error occurred</h1>
    }
```

> **알아두세요** : 빌드 타임에 데이터를 가져올 필요가 있다면 이 페이지 안에서 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)를 사용할 수 있습니다.

### 더 고급 오류 페이지 사용자 정의[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#more-advanced-error-page-customizing)

500 오류는 `Error` 컴포넌트가 클라이언트와 서버 양쪽에서 처리합니다. 이를 재정의하려면 `pages/_error.js` 파일을 정의하고 다음 코드를 추가하세요:
```
    function Error({ statusCode }) {
      return (
        <p>
          {statusCode
            ? `An error ${statusCode} occurred on server`
            : 'An error occurred on client'}
        </p>
      )
    }

    Error.getInitialProps = ({ res, err }) => {
      const statusCode = res ? res.statusCode : err ? err.statusCode : 404
      return { statusCode }
    }

    export default Error
```

> `pages/_error.js`는 프로덕션에서만 사용됩니다. 개발 환경에서는 오류가 발생한 위치를 파악할 수 있도록 호출 스택과 함께 오류가 표시됩니다.

### 기본 제공 오류 페이지 재사용[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#reusing-the-built-in-error-page)

기본 제공 오류 페이지를 렌더링하려면 `Error` 컴포넌트를 가져와 사용할 수 있습니다:
```
    import Error from 'next/error'

    export async function getServerSideProps() {
      const res = await fetch('https://api.github.com/repos/vercel/next.js')
      const errorCode = res.ok ? false : res.status
      const json = await res.json()

      return {
        props: { errorCode, stars: json.stargazers_count },
      }
    }

    export default function Page({ errorCode, stars }) {
      if (errorCode) {
        return <Error statusCode={errorCode} />
      }

      return <div>Next stars: {stars}</div>
    }
```

`Error` 컴포넌트는 `statusCode`와 함께 텍스트 메시지를 전달하고 싶을 때 `title` 속성도 받을 수 있습니다.

사용자 정의 `Error` 컴포넌트가 있다면 반드시 해당 컴포넌트를 대신 임포트하세요. `next/error`는 Next.js에서 사용하는 기본 컴포넌트를 내보냅니다.

### 주의 사항[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#caveats)

  * `Error`는 현재 [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)나 [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) 같은 Next.js [데이터 패칭 메서드](https://nextjs.org/docs/pages/building-your-application/data-fetching)를 지원하지 않습니다.
  * `_error`는 `_app`과 마찬가지로 예약된 경로명입니다. `_error`는 오류 페이지의 사용자 정의 레이아웃과 동작을 정의하는 데 사용됩니다. [라우팅](https://nextjs.org/docs/pages/building-your-application/routing) 또는 [사용자 정의 서버](https://nextjs.org/docs/pages/guides/custom-server)에서 직접 `/_error`에 접근하면 404가 렌더링됩니다.

보내기