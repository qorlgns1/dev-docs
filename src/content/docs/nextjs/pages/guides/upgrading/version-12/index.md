---
title: '업그레이드: 버전 12'
description: '원본 URL: https://nextjs.org/docs/pages/guides/upgrading/version-12'
---

# 업그레이드: 버전 12 | Next.js

원본 URL: https://nextjs.org/docs/pages/guides/upgrading/version-12

[가이드](https://nextjs.org/docs/pages/guides)[업그레이드](https://nextjs.org/docs/pages/guides/upgrading)버전 12

페이지 복사

# 버전 12로 업그레이드하는 방법

마지막 업데이트 2026년 2월 20일

버전 12로 업그레이드하려면 다음 명령을 실행하세요:

터미널
[code]
    npm i next@12 react@17 react-dom@17 eslint-config-next@12
[/code]

터미널
[code]
    yarn add next@12 react@17 react-dom@17 eslint-config-next@12
[/code]

터미널
[code]
    pnpm up next@12 react@17 react-dom@17 eslint-config-next@12
[/code]

터미널
[code]
    bun add next@12 react@17 react-dom@17 eslint-config-next@12
[/code]

> **알아두면 좋아요:** TypeScript를 사용 중이라면 `@types/react`와 `@types/react-dom`도 해당 버전에 맞춰 업그레이드하세요.

### 12.2로 업그레이드[](https://nextjs.org/docs/pages/guides/upgrading/version-12#upgrading-to-122)

[Middleware](https://nextjs.org/docs/messages/middleware-upgrade-guide) \- `12.2` 이전에 Middleware를 사용했다면 자세한 내용은 [업그레이드 가이드](https://nextjs.org/docs/messages/middleware-upgrade-guide)를 참고하세요.

### 12.0으로 업그레이드[](https://nextjs.org/docs/pages/guides/upgrading/version-12#upgrading-to-120)

[최소 Node.js 버전](https://nodejs.org/en/) \- 최소 Node.js 버전이 `12.0.0`에서 `12.22.0`으로 상향되었습니다. 이 버전은 Node.js에서 ES Modules를 기본 지원하는 첫 버전입니다.

[최소 React 버전](https://react.dev/learn/add-react-to-an-existing-project) \- 필요한 최소 React 버전은 `17.0.2`입니다. 업그레이드하려면 터미널에서 다음 명령을 실행하세요:

터미널
[code]
    npm install react@latest react-dom@latest
     
    yarn add react@latest react-dom@latest
     
    pnpm update react@latest react-dom@latest
     
    bun add react@latest react-dom@latest
[/code]

#### Babel을 대체하는 SWC[](https://nextjs.org/docs/pages/guides/upgrading/version-12#swc-replacing-babel)

Next.js는 이제 Rust 기반 컴파일러 [SWC](https://swc.rs/)를 사용해 JavaScript/TypeScript를 컴파일합니다. 이 새로운 컴파일러는 개별 파일 컴파일 시 최대 17배, Fast Refresh 시 최대 5배 더 빠릅니다.

Next.js는 [커스텀 Babel 구성](https://nextjs.org/docs/pages/guides/babel)을 가진 애플리케이션과 완전한 하위 호환성을 제공합니다. Next.js가 기본으로 처리하는 styled-jsx, `getStaticProps` / `getStaticPaths` / `getServerSideProps` 트리 셰이킹 같은 변환은 모두 Rust로 포팅되었습니다.

애플리케이션에 커스텀 Babel 구성이 있으면, Next.js는 JavaScript/Typescript 컴파일 시 자동으로 SWC 사용을 중단하고 Next.js 11과 동일하게 Babel을 사용합니다.

현재 커스텀 Babel 변환이 필요한 많은 외부 라이브러리 통합이 가까운 시일 내에 Rust 기반 SWC 변환으로 포팅될 예정입니다. 여기에는 다음이 포함되지만 이에 국한되지는 않습니다:

  * Styled Components
  * Emotion
  * Relay

SWC 채택에 도움이 되는 변환의 우선순위를 정하기 위해 [이 피드백 스레드](https://github.com/vercel/next.js/discussions/30174)에 `.babelrc`를 공유해 주세요.

#### 축소 작업에서 Terser를 대체하는 SWC[](https://nextjs.org/docs/pages/guides/upgrading/version-12#swc-replacing-terser-for-minification)

`next.config.js`에서 플래그를 사용해 Terser 대신 SWC를 사용하도록 선택하면 JavaScript 축소 작업 속도를 최대 7배까지 높일 수 있습니다:

next.config.js
[code]
    module.exports = {
      swcMinify: true,
    }
[/code]

SWC를 이용한 축소는 Next.js 12.1에서 기본값이 되기 전에 더 많은 실제 Next.js 애플리케이션에서 테스트할 수 있도록 옵트인 플래그로 제공됩니다. 축소에 대한 의견이 있다면 [이 피드백 스레드](https://github.com/vercel/next.js/discussions/30237)에 남겨 주세요.

#### styled-jsx CSS 파싱 개선[](https://nextjs.org/docs/pages/guides/upgrading/version-12#improvements-to-styled-jsx-css-parsing)

Rust 기반 컴파일러 위에 styled-jsx Babel 변환에서 사용하는 것과 동일한 새 CSS 파서를 구현했습니다. 이 파서는 CSS 처리 방식이 개선되었으며, 이전에는 지나쳐 예상치 못한 동작을 일으키던 잘못된 CSS를 이제 오류로 보고합니다.

이 변경으로 인해 잘못된 CSS는 개발 중과 `next build`에서 오류를 발생시키며, styled-jsx 사용에만 영향을 줍니다.

#### `next/image` 래핑 요소 변경[](https://nextjs.org/docs/pages/guides/upgrading/version-12#nextimage-changed-wrapping-element)

`next/image`는 이제 `<div>` 대신 `<span>` 내부에 `<img>`를 렌더링합니다.

애플리케이션에서 `.container span`처럼 `span`을 타깃팅하는 CSS가 있다면, Next.js 12로 업그레이드할 때 `<Image>` 컴포넌트 내부의 래핑 요소가 잘못 매칭될 수 있습니다. 이를 피하려면 `.container span.item`처럼 특정 클래스로 선택자를 제한하고 `<span className="item" />`처럼 해당 클래스명을 컴포넌트에 추가하세요.

애플리케이션에서 `.container div`처럼 `next/image` `<div>` 태그를 특정 타깃으로 삼는 CSS가 있다면 더 이상 매칭되지 않을 수 있습니다. 선택자를 `.container span`으로 업데이트하거나, `<Image>` 컴포넌트를 감싸는 `<div className="wrapper">`를 추가하고 `.container .wrapper`를 타깃으로 하는 것이 좋습니다.

`className` prop은 변경되지 않았으며 여전히 내부 `<img>` 요소에 전달됩니다.

자세한 내용은 [문서](https://nextjs.org/docs/pages/api-reference/components/image#styling-images)를 확인하세요.

#### HMR 연결이 이제 WebSocket 사용[](https://nextjs.org/docs/pages/guides/upgrading/version-12#hmr-connection-now-uses-a-websocket)

이전에는 Next.js가 HMR 이벤트를 받기 위해 [server-sent events](https://developer.mozilla.org/docs/Web/API/Server-sent_events) 연결을 사용했습니다. 이제 Next.js 12는 WebSocket 연결을 사용합니다.

Next.js 개발 서버로 요청을 프록시하는 경우 업그레이드 요청이 올바로 처리되도록 해야 합니다. 예를 들어 `nginx`에서는 다음 구성을 추가해야 합니다:
[code] 
    location /_next/webpack-hmr {
        proxy_pass http://localhost:3000/_next/webpack-hmr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
[/code]

Apache(2.x)를 사용하는 경우 서버에서 웹소켓을 활성화하려면 다음 구성을 추가할 수 있습니다. 포트, 호스트 이름, 서버 이름을 확인하세요.
[code] 
    <VirtualHost *:443>
     # ServerName yourwebsite.local
     ServerName "${WEBSITE_SERVER_NAME}"
     ProxyPass / http://localhost:3000/
     ProxyPassReverse / http://localhost:3000/
     # Next.js 12 uses websocket
     <Location /_next/webpack-hmr>
        RewriteEngine On
        RewriteCond %{QUERY_STRING} transport=websocket [NC]
        RewriteCond %{HTTP:Upgrade} websocket [NC]
        RewriteCond %{HTTP:Connection} upgrade [NC]
        RewriteRule /(.*) ws://localhost:3000/_next/webpack-hmr/$1 [P,L]
        ProxyPass ws://localhost:3000/_next/webpack-hmr retry=0 timeout=30
        ProxyPassReverse ws://localhost:3000/_next/webpack-hmr
     </Location>
    </VirtualHost>
    
[/code]

`express` 같은 커스텀 서버의 경우, 요청이 올바르게 전달되도록 `app.all`을 사용해야 할 수 있습니다. 예시는 다음과 같습니다:
[code] 
    app.all('/_next/webpack-hmr', (req, res) => {
      nextjsRequestHandler(req, res)
    })
[/code]

#### Webpack 4 지원 제거[](https://nextjs.org/docs/pages/guides/upgrading/version-12#webpack-4-support-has-been-removed)

이미 webpack 5를 사용 중이라면 이 섹션은 건너뛰어도 됩니다.

Next.js는 Next.js 11에서 컴파일 기본값으로 webpack 5를 채택했습니다. [webpack 5 업그레이드 문서](https://nextjs.org/docs/messages/webpack5)에서 안내했듯 Next.js 12는 webpack 4 지원을 제거합니다.

애플리케이션이 아직 옵트아웃 플래그를 사용해 webpack 4를 사용 중이라면 이제 [webpack 5 업그레이드 문서](https://nextjs.org/docs/messages/webpack5)로 연결되는 오류가 표시됩니다.

#### `target` 옵션 사용 중단[](https://nextjs.org/docs/pages/guides/upgrading/version-12#target-option-deprecated)

`next.config.js`에 `target`이 없다면 이 섹션을 건너뛰어도 됩니다.

target 옵션은 페이지 실행에 필요한 의존성을 추적하는 기본 제공 기능으로 대체되어 사용 중단되었습니다.

`next build` 중 Next.js는 각 페이지와 그 의존성을 자동으로 추적해 애플리케이션 프로덕션 배포에 필요한 모든 파일을 파악합니다.

현재 `target` 옵션을 `serverless`로 설정하고 있다면 [새 출력 활용 방법에 대한 문서](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output)를 읽어 보세요.

도움이 되었나요?

지원됨.

보내기
