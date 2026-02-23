---
title: '가이드: Custom Server'
description: 'Next.js는 기본적으로 와 함께 자체 서버를 포함합니다. 기존 백엔드가 있더라도 Next.js와 함께 사용할 수 있으며(이 경우 커스텀 서버가 아님) 커스텀 Next.js 서버를 통해 특정 패턴에 맞춰 프로그래밍 방식으로 서버를 시작할 수 있습니다. 대부분의 경우...'
---

# 가이드: Custom Server | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/custom-server

[페이지 라우터](https://nextjs.org/docs/pages)[가이드](https://nextjs.org/docs/pages/guides)Custom Server

페이지 복사

# Next.js에서 커스텀 서버를 설정하는 방법

마지막 업데이트: 2026년 2월 20일

Next.js는 기본적으로 `next start`와 함께 자체 서버를 포함합니다. 기존 백엔드가 있더라도 Next.js와 함께 사용할 수 있으며(이 경우 커스텀 서버가 아님) 커스텀 Next.js 서버를 통해 특정 패턴에 맞춰 프로그래밍 방식으로 서버를 시작할 수 있습니다. 대부분의 경우 이러한 접근 방식이 필요하지 않지만, 필요하다면 이탈할 수 있도록 제공됩니다.

> **알아두면 좋은 점** :
> 
>   * 커스텀 서버 사용을 결정하기 전에, Next.js의 통합 라우터가 앱 요구 사항을 충족하지 못할 때만 사용해야 한다는 점을 기억하세요. 커스텀 서버를 사용하면 **[Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)** 과 같은 중요한 성능 최적화가 제거됩니다.
>   * 단독 출력 모드를 사용할 때는 커스텀 서버 파일을 추적하지 않습니다. 대신 별도의 최소한의 `server.js` 파일을 출력하며, 이 모드와 커스텀 서버는 동시에 사용할 수 없습니다.
> 

커스텀 서버의 [다음 예제](https://github.com/vercel/next.js/tree/canary/examples/custom-server)를 살펴보세요:

server.ts

JavaScriptTypeScript
[code]
    import { createServer } from 'http'
    import next from 'next'
     
    const port = parseInt(process.env.PORT || '3000', 10)
    const dev = process.env.NODE_ENV !== 'production'
    const app = next({ dev })
    const handle = app.getRequestHandler()
     
    app.prepare().then(() => {
      createServer((req, res) => {
        handle(req, res)
      }).listen(port)
     
      console.log(
        `> Server listening at http://localhost:${port} as ${
          dev ? 'development' : process.env.NODE_ENV
        }`
      )
    })
[/code]

> `server.js`는 Next.js Compiler 또는 번들링 과정을 거치지 않습니다. 이 파일이 필요로 하는 문법과 소스 코드가 현재 사용 중인 Node.js 버전과 호환되는지 확인하세요. [예제 보기](https://github.com/vercel/next.js/tree/canary/examples/custom-server).

커스텀 서버를 실행하려면 `package.json`의 `scripts`를 다음과 같이 업데이트해야 합니다:

package.json
[code]
    {
      "scripts": {
        "dev": "node server.js",
        "build": "next build",
        "start": "NODE_ENV=production node server.js"
      }
    }
[/code]

또는 `nodemon`을 설정할 수 있습니다([예제](https://github.com/vercel/next.js/tree/canary/examples/custom-server)). 커스텀 서버는 다음 임포트를 사용하여 서버를 Next.js 애플리케이션과 연결합니다:
[code] 
    import next from 'next'
     
    const app = next({})
[/code]

위 `next` 임포트는 다음 옵션을 포함한 객체를 인수로 받는 함수입니다:

옵션| 유형| 설명  
---|---|---  
`conf`| `Object`| `next.config.js`에서 사용하는 것과 동일한 객체. 기본값은 `{}`  
`dev`| `Boolean`| (_옵션_) Next.js를 dev 모드로 실행할지 여부. 기본값은 `false`  
`dir`| `String`| (_옵션_) Next.js 프로젝트 위치. 기본값은 `'.'`  
`quiet`| `Boolean`| (_옵션_) 서버 정보를 포함한 오류 메시지를 숨길지 여부. 기본값은 `false`  
`hostname`| `String`| (_옵션_) 서버가 실행되는 호스트 이름  
`port`| `Number`| (_옵션_) 서버가 실행되는 포트  
`httpServer`| `node:http#Server`| (_옵션_) Next.js가 뒤에서 실행되는 HTTP Server  
`turbopack`| `Boolean`| (_옵션_) Turbopack 활성화(기본적으로 활성화됨)  
`webpack`| `Boolean`| (_옵션_) webpack 활성화  
  
반환된 `app`은 필요한 대로 Next.js가 요청을 처리하도록 사용할 수 있습니다.

## 파일 시스템 라우팅 비활성화[](https://nextjs.org/docs/pages/guides/custom-server#disabling-file-system-routing)

기본적으로 `Next`는 `pages` 폴더의 각 파일을 파일 이름과 일치하는 경로명으로 제공합니다. 커스텀 서버를 사용하는 프로젝트에서는 동일한 콘텐츠가 여러 경로에서 제공될 수 있어 SEO 및 UX에 문제가 발생할 수 있습니다.

이 동작을 비활성화하고 `pages`의 파일 기반 라우팅을 방지하려면 `next.config.js`를 열고 `useFileSystemPublicRoutes` 설정을 비활성화하세요:

next.config.js
[code]
    module.exports = {
      useFileSystemPublicRoutes: false,
    }
[/code]

> `useFileSystemPublicRoutes`는 SSR에서 파일 이름 경로를 비활성화하지만, 클라이언트 측 라우팅은 여전히 해당 경로에 접근할 수 있습니다. 이 옵션을 사용하는 경우 원하지 않는 경로로의 내비게이션을 프로그래밍 방식으로 차단해야 합니다.

> 또한 클라이언트 측 라우터가 파일 이름 경로로 리디렉션하지 못하도록 구성하고 싶을 수 있습니다. 이를 위해 [`router.beforePopState`](https://nextjs.org/docs/pages/api-reference/functions/use-router#routerbeforepopstate)를 참조하세요.

도움이 되었나요?

지원됨.

전송
