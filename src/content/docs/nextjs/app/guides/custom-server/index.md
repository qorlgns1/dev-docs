---
title: '가이드: Custom Server'
description: '마지막 업데이트 2026년 2월 20일'
---

# 가이드: Custom Server | Next.js

Source URL: https://nextjs.org/docs/app/guides/custom-server

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)Custom Server

페이지 복사

# Next.js에서 Custom Server를 설정하는 방법

마지막 업데이트 2026년 2월 20일

Next.js는 기본적으로 `next start`와 함께 자체 서버를 포함합니다. 기존 백엔드를 보유하고 있어도 Next.js와 함께 사용할 수 있으며, 이는 커스텀 서버가 아닙니다. 커스텀 Next.js 서버를 사용하면 맞춤 패턴을 위해 서버를 프로그래밍 방식으로 시작할 수 있습니다. 대부분의 경우 이 접근 방식은 필요하지 않지만, 언젠가 분리해야 할 때 사용할 수 있습니다.

> **알아두면 좋아요** :
> 
>   * 커스텀 서버를 사용하기로 결정하기 전에, 이는 Next.js 통합 라우터로 앱 요구 사항을 충족할 수 없을 때만 써야 한다는 점을 명심하세요. 커스텀 서버를 사용하면 **[Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)** 같은 중요한 성능 최적화가 사라집니다.
>   * standalone 출력 모드를 사용할 때는 커스텀 서버 파일을 추적하지 않습니다. 이 모드는 대신 별도의 최소 `server.js` 파일을 출력하며, 둘을 함께 사용할 수 없습니다.
> 

커스텀 서버의 [다음 예시](https://github.com/vercel/next.js/tree/canary/examples/custom-server)를 확인하세요:

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

> `server.js`는 Next.js Compiler나 번들링 과정을 거치지 않습니다. 이 파일이 요구하는 구문과 소스 코드가 현재 사용 중인 Node.js 버전과 호환되는지 확인하세요. [예시 보기](https://github.com/vercel/next.js/tree/canary/examples/custom-server).

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

또는 `nodemon`을 설정할 수도 있습니다([예시](https://github.com/vercel/next.js/tree/canary/examples/custom-server)). 커스텀 서버는 다음 import를 사용하여 서버와 Next.js 애플리케이션을 연결합니다:
[code] 
    import next from 'next'
     
    const app = next({})
[/code]

위의 `next` import는 다음 옵션이 포함된 객체를 인수로 받는 함수입니다:

옵션| 유형| 설명  
---|---|---  
`conf`| `Object`| `next.config.js`에서 사용하는 것과 동일한 객체입니다. 기본값은 `{}`  
`dev`| `Boolean`| (_옵션_) Next.js를 dev 모드로 실행할지 여부입니다. 기본값은 `false`  
`dir`| `String`| (_옵션_) Next.js 프로젝트 위치입니다. 기본값은 `'.'`  
`quiet`| `Boolean`| (_옵션_) 서버 정보를 포함한 오류 메시지를 숨깁니다. 기본값은 `false`  
`hostname`| `String`| (_옵션_) 서버가 실행 중인 호스트 이름  
`port`| `Number`| (_옵션_) 서버가 실행 중인 포트  
`httpServer`| `node:http#Server`| (_옵션_) Next.js가 뒤에서 실행 중인 HTTP 서버  
`turbopack`| `Boolean`| (_옵션_) Turbopack을 활성화합니다(기본적으로 활성화됨)  
`webpack`| `Boolean`| (_옵션_) webpack을 활성화합니다  
  
반환된 `app`은 필요한 대로 요청을 Next.js가 처리하도록 사용할 수 있습니다.

도움이 되었나요?

지원됨.

전송
