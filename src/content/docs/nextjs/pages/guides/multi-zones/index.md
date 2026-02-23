---
title: '가이드: Multi-Zones'
description: 'Multi-Zones는 하나의 도메인에서 큰 애플리케이션을 여러 개의 Next.js 애플리케이션으로 분리하여 각 애플리케이션이 특정 경로 집합을 서비스하도록 하는 마이크로 프런트엔드 접근 방식입니다. 이는 애플리케이션 내의 다른 페이지와 관련 없는 페이지 모음을 다룰 ...'
---

# 가이드: Multi-Zones | Next.js

소스 URL: https://nextjs.org/docs/pages/guides/multi-zones

# Multi-Zones와 Next.js로 마이크로 프런트엔드를 구축하는 방법

최종 업데이트 2026년 2월 20일

예제

  * [With Zones](https://github.com/vercel/next.js/tree/canary/examples/with-zones)

Multi-Zones는 하나의 도메인에서 큰 애플리케이션을 여러 개의 Next.js 애플리케이션으로 분리하여 각 애플리케이션이 특정 경로 집합을 서비스하도록 하는 마이크로 프런트엔드 접근 방식입니다. 이는 애플리케이션 내의 다른 페이지와 관련 없는 페이지 모음을 다룰 때 유용합니다. 해당 페이지를 별도의 존(즉, 별도의 애플리케이션)으로 이동하면 각 애플리케이션의 크기를 줄여 빌드 시간을 개선하고 특정 존에만 필요한 코드를 제거할 수 있습니다. 애플리케이션이 분리되어 있으므로, Multi-Zones를 사용하면 동일한 도메인의 다른 애플리케이션이 원하는 프레임워크를 선택할 수도 있습니다.

예를 들어, 다음과 같은 페이지 집합을 분리하고 싶다고 가정해 보겠습니다:

  * `/blog/*` — 모든 블로그 게시물
  * `/dashboard/*` — 대시보드에 로그인한 사용자를 위한 모든 페이지
  * `/*` — 다른 존에서 다루지 않는 웹사이트의 나머지 부분

Multi-Zones를 지원하면 동일한 도메인에서 사용자에게 동일하게 보이도록 세 개의 애플리케이션을 제공하면서, 각 애플리케이션을 독립적으로 개발 및 배포할 수 있습니다.

동일한 존 내에서 페이지를 이동할 때는 페이지를 다시 로드하지 않는 소프트 내비게이션이 수행됩니다. 예를 들어, 아래 다이어그램에서 `/`에서 `/products`로 이동하면 소프트 내비게이션입니다.

한 존의 페이지에서 다른 존의 페이지로 이동할 때(예: `/`에서 `/dashboard`로 이동)에는 하드 내비게이션이 수행되어 현재 페이지의 리소스를 언로드하고 새 페이지의 리소스를 로드합니다. 자주 함께 방문하는 페이지는 하드 내비게이션을 피하기 위해 동일한 존에 배치해야 합니다.

## 존을 정의하는 방법[](https://nextjs.org/docs/pages/guides/multi-zones#how-to-define-a-zone)

존은 일반적인 Next.js 애플리케이션이며, 다른 존의 페이지나 정적 파일과 충돌하지 않도록 [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)를 추가로 구성합니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      assetPrefix: '/blog-static',
    }
```

JavaScript와 CSS 같은 Next.js 에셋은 `assetPrefix`가 접두사로 붙어 다른 존의 에셋과 충돌하지 않도록 합니다. 이러한 에셋은 각 존에서 `/assetPrefix/_next/...` 경로 아래에서 제공됩니다.

다른 보다 구체적인 존으로 라우팅되지 않는 모든 경로를 처리하는 기본 애플리케이션에는 `assetPrefix`가 필요하지 않습니다.

Next.js 15 이전 버전에서는 정적 에셋을 처리하기 위한 추가 rewrite가 필요할 수 있습니다. Next.js 15에서는 더 이상 필요하지 않습니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      assetPrefix: '/blog-static',
      async rewrites() {
        return {
          beforeFiles: [
            {
              source: '/blog-static/_next/:path+',
              destination: '/_next/:path+',
            },
          ],
        }
      },
    }
```

## 적절한 존으로 요청을 라우팅하는 방법[](https://nextjs.org/docs/pages/guides/multi-zones#how-to-route-requests-to-the-right-zone)

Multi-Zones 구성을 사용하면 서로 다른 애플리케이션이 요청을 처리하므로 경로를 올바른 존으로 라우팅해야 합니다. 이를 위해 어떤 HTTP 프록시도 사용할 수 있지만, Next.js 애플리케이션 중 하나를 사용해 전체 도메인의 요청을 라우팅할 수도 있습니다.

Next.js 애플리케이션을 사용해 올바른 존으로 라우팅하려면 [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)를 사용할 수 있습니다. 다른 존이 제공하는 각 경로에 대해 해당 경로를 다른 존의 도메인으로 전달하는 rewrite 규칙을 추가하고, 정적 에셋 요청도 다시 작성해야 합니다. 예시는 다음과 같습니다:

next.config.js
```
    async rewrites() {
        return [
            {
                source: '/blog',
                destination: `${process.env.BLOG_DOMAIN}/blog`,
            },
            {
                source: '/blog/:path+',
                destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
            },
            {
                source: '/blog-static/:path+',
                destination: `${process.env.BLOG_DOMAIN}/blog-static/:path+`,
            }
        ];
    }
```

`destination`은 존이 제공하는 URL(스킴과 도메인 포함)이어야 합니다. 이는 존의 프로덕션 도메인을 가리켜야 하지만, 로컬 개발 시 `localhost`로 요청을 라우팅하는 데도 사용할 수 있습니다.

> **알아두면 좋아요** : URL 경로는 존마다 고유해야 합니다. 예를 들어, 두 존이 `/blog`를 제공하려고 하면 라우팅 충돌이 발생합니다.

### 프록시를 사용해 요청 라우팅하기[](https://nextjs.org/docs/pages/guides/multi-zones#routing-requests-using-proxy)

[`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)를 통한 요청 라우팅은 요청 지연을 최소화하기 위해 권장되지만, 라우팅 시 동적인 결정이 필요할 때는 프록시도 사용할 수 있습니다. 예를 들어, 마이그레이션 중에 특정 경로를 어디로 보낼지 기능 플래그를 사용해 결정하는 경우 프록시를 활용할 수 있습니다.

proxy.js
```
    export async function proxy(request) {
      const { pathname, search } = request.nextUrl
      if (pathname === '/your-path' && myFeatureFlag.isEnabled()) {
        return NextResponse.rewrite(`${rewriteDomain}${pathname}${search}`)
      }
    }
```

## 존 간 링크 연결[](https://nextjs.org/docs/pages/guides/multi-zones#linking-between-zones)

다른 존의 경로로 이동하는 링크는 Next.js [`<Link>`](https://nextjs.org/docs/pages/api-reference/components/link) 컴포넌트 대신 `a` 태그를 사용해야 합니다. Next.js는 `<Link>` 컴포넌트에서 모든 상대 경로를 프리페치하고 소프트 내비게이션하려고 시도하기 때문에 존 간에는 작동하지 않습니다.

## 코드 공유[](https://nextjs.org/docs/pages/guides/multi-zones#sharing-code)

서로 다른 존을 구성하는 Next.js 애플리케이션은 어떤 리포지토리에도 위치할 수 있습니다. 그러나 코드 공유를 더 쉽게 하기 위해 이러한 존을 [모노레포](https://en.wikipedia.org/wiki/Monorepo)에 배치하는 것이 종종 편리합니다. 서로 다른 리포지토리에 있는 존의 경우, 공개 또는 비공개 NPM 패키지를 통해서도 코드를 공유할 수 있습니다.

각 존의 페이지는 서로 다른 시점에 릴리스될 수 있으므로, 기능 플래그를 사용하면 여러 존에서 기능을 동시에 활성화하거나 비활성화하는 데 도움이 됩니다.

보내기