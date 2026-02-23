---
title: '시작하기: 배포'
description: 'Next.js는 Node.js 서버, Docker 컨테이너, 정적 내보내기, 또는 다양한 플랫폼에 맞춘 어댑터 형태로 배포할 수 있습니다.'
---

# 시작하기: 배포 | Next.js

출처 URL: https://nextjs.org/docs/app/getting-started/deploying

# 배포

마지막 업데이트 2026년 2월 20일

Next.js는 Node.js 서버, Docker 컨테이너, 정적 내보내기, 또는 다양한 플랫폼에 맞춘 어댑터 형태로 배포할 수 있습니다.

배포 옵션| 기능 지원
---|---
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| 전체
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| 전체
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| 제한적
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| 플랫폼별

## Node.js server[](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)

Next.js는 Node.js를 지원하는 모든 제공업체에 배포할 수 있습니다. `package.json`에 `"build"`와 `"start"` 스크립트가 포함되어 있는지 확인하세요:

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start"
      }
    }
[/code]

그런 다음 애플리케이션을 빌드하려면 `npm run build`, Node.js 서버를 시작하려면 `npm run start`를 실행하세요. 이 서버는 모든 Next.js 기능을 지원합니다. 필요하다면 [custom server](https://nextjs.org/docs/app/guides/custom-server)로 전환할 수도 있습니다.

Node.js 배포는 모든 Next.js 기능을 지원합니다. 인프라에 맞게 [구성하는 방법](https://nextjs.org/docs/app/guides/self-hosting)을 확인하세요.

### Templates[](https://nextjs.org/docs/app/getting-started/deploying#templates)

  * [Flightcontrol](https://github.com/nextjs/deploy-flightcontrol)
  * [Railway](https://github.com/nextjs/deploy-railway)
  * [Replit](https://github.com/nextjs/deploy-replit)

## Docker[](https://nextjs.org/docs/app/getting-started/deploying#docker)

Next.js는 [Docker](https://www.docker.com/) 컨테이너를 지원하는 모든 제공업체에 배포할 수 있습니다. 여기에는 Kubernetes 같은 컨테이너 오케스트레이터나 Docker를 실행하는 클라우드 제공업체가 포함됩니다.

Docker 배포는 모든 Next.js 기능을 지원합니다. 인프라에 맞게 [구성하는 방법](https://nextjs.org/docs/app/guides/self-hosting)을 확인하세요.

> **개발용 참고:** Docker는 프로덕션 배포에 매우 적합하지만, Mac과 Windows에서 개발 중에는 더 나은 성능을 위해 Docker 대신 로컬 개발(`npm run dev`)을 사용하는 것을 고려하세요. [로컬 개발 최적화 방법 알아보기](https://nextjs.org/docs/app/guides/local-development).

### Templates[](https://nextjs.org/docs/app/getting-started/deploying#templates-1)

  * [Docker](https://github.com/vercel/next.js/tree/canary/examples/with-docker)
  * [Docker Multi-Environment](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env)
  * [DigitalOcean](https://github.com/nextjs/deploy-digitalocean)
  * [Fly.io](https://github.com/nextjs/deploy-fly)
  * [Google Cloud Run](https://github.com/nextjs/deploy-google-cloud-run)
  * [Render](https://github.com/nextjs/deploy-render)
  * [SST](https://github.com/nextjs/deploy-sst)

## Static export[](https://nextjs.org/docs/app/getting-started/deploying#static-export)

Next.js는 정적 사이트 또는 [Single-Page Application (SPA)](https://nextjs.org/docs/app/guides/single-page-applications)로 시작한 뒤, 나중에 서버가 필요한 기능으로 업그레이드할 수 있습니다.

Next.js가 [static exports](https://nextjs.org/docs/app/guides/static-exports)를 지원하므로, HTML/CSS/JS 정적 에셋을 제공할 수 있는 모든 웹 서버(AWS S3, Nginx, Apache 등)에 배포하고 호스팅할 수 있습니다.

[static export](https://nextjs.org/docs/app/guides/static-exports) 모드로 실행할 때는 서버가 필요한 Next.js 기능을 **지원하지 않습니다**. [자세히 보기](https://nextjs.org/docs/app/guides/static-exports#unsupported-features).

### Templates[](https://nextjs.org/docs/app/getting-started/deploying#templates-2)

  * [GitHub Pages](https://github.com/nextjs/deploy-github-pages)

## Adapters[](https://nextjs.org/docs/app/getting-started/deploying#adapters)

Next.js는 다양한 플랫폼에서 해당 인프라 기능을 활용할 수 있도록 맞춤형 어댑터로 실행할 수 있습니다.

각 제공업체 문서를 참고하여 지원되는 Next.js 기능을 확인하세요:

  * [Appwrite Sites](https://appwrite.io/docs/products/sites/quick-start/nextjs)
  * [AWS Amplify Hosting](https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components)
  * [Cloudflare](https://developers.cloudflare.com/workers/frameworks/framework-guides/nextjs)
  * [Deno Deploy](https://docs.deno.com/examples/next_tutorial)
  * [Firebase App Hosting](https://firebase.google.com/docs/app-hosting/get-started)
  * [Netlify](https://docs.netlify.com/frameworks/next-js/overview/#next-js-support-on-netlify)
  * [Vercel](https://vercel.com/docs/frameworks/nextjs)

> **참고:** 현재 모든 플랫폼이 채택할 수 있는 [Deployment Adapters API](https://github.com/vercel/next.js/discussions/77740)를 개발 중입니다. 완성되면 자체 어댑터 작성 방법에 대한 문서를 추가할 예정입니다.
