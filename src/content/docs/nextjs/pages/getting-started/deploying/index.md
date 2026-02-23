---
title: '시작하기: 배포'
description: 'Next.js는 Node.js 서버, Docker 컨테이너, 정적 내보내기, 또는 다양한 플랫폼에 맞춘 어댑터 형태로 배포할 수 있습니다.'
---

# 시작하기: 배포 | Next.js

출처 URL: https://nextjs.org/docs/pages/getting-started/deploying

[Pages Router](https://nextjs.org/docs/pages)[Getting Started](https://nextjs.org/docs/pages/getting-started)Deploying

페이지 복사

# Next.js 애플리케이션 배포 방법

최종 업데이트 2026년 2월 20일

Next.js는 Node.js 서버, Docker 컨테이너, 정적 내보내기, 또는 다양한 플랫폼에 맞춘 어댑터 형태로 배포할 수 있습니다.

배포 옵션| 기능 지원  
---|---  
[Node.js server](https://nextjs.org/docs/pages/getting-started/deploying#nodejs-server)| 모든 기능  
[Docker container](https://nextjs.org/docs/pages/getting-started/deploying#docker)| 모든 기능  
[Static export](https://nextjs.org/docs/pages/getting-started/deploying#static-export)| 제한적  
[Adapters](https://nextjs.org/docs/pages/getting-started/deploying#adapters)| 플랫폼별  
  
## Node.js server[](https://nextjs.org/docs/pages/getting-started/deploying#nodejs-server)

Next.js는 Node.js를 지원하는 어떤 제공자에게도 배포할 수 있습니다. `package.json`에 `"build"`와 `"start"` 스크립트가 포함되어 있는지 확인하세요:

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

그런 다음 `npm run build`로 애플리케이션을 빌드하고 `npm run start`로 Node.js 서버를 시작합니다. 이 서버는 모든 Next.js 기능을 지원합니다. 필요하다면 [custom server](https://nextjs.org/docs/app/guides/custom-server)로 전환할 수도 있습니다.

Node.js 배포는 Next.js의 모든 기능을 지원합니다. 인프라에 맞게 [구성하는 방법](https://nextjs.org/docs/app/guides/self-hosting)을 확인하세요.

### 템플릿[](https://nextjs.org/docs/pages/getting-started/deploying#templates)

  * [Flightcontrol](https://github.com/nextjs/deploy-flightcontrol)
  * [Railway](https://github.com/nextjs/deploy-railway)
  * [Replit](https://github.com/nextjs/deploy-replit)



## Docker[](https://nextjs.org/docs/pages/getting-started/deploying#docker)

Next.js는 [Docker](https://www.docker.com/) 컨테이너를 지원하는 모든 제공자에게 배포할 수 있습니다. 여기에는 Kubernetes 같은 컨테이너 오케스트레이터나 Docker를 실행하는 클라우드 제공자가 포함됩니다.

Docker 배포는 Next.js의 모든 기능을 지원합니다. 인프라에 맞게 [구성하는 방법](https://nextjs.org/docs/app/guides/self-hosting)을 확인하세요.

> **개발 환경 참고:** Docker는 프로덕션 배포에는 훌륭하지만, Mac과 Windows에서 개발 중이라면 더 나은 성능을 위해 Docker 대신 로컬 개발(`npm run dev`)을 고려하세요. [로컬 개발 최적화 방법 알아보기](https://nextjs.org/docs/app/guides/local-development).

### 템플릿[](https://nextjs.org/docs/pages/getting-started/deploying#templates-1)

  * [Docker](https://github.com/vercel/next.js/tree/canary/examples/with-docker)
  * [Docker Multi-Environment](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env)
  * [DigitalOcean](https://github.com/nextjs/deploy-digitalocean)
  * [Fly.io](https://github.com/nextjs/deploy-fly)
  * [Google Cloud Run](https://github.com/nextjs/deploy-google-cloud-run)
  * [Render](https://github.com/nextjs/deploy-render)
  * [SST](https://github.com/nextjs/deploy-sst)



## Static export[](https://nextjs.org/docs/pages/getting-started/deploying#static-export)

Next.js는 정적 사이트나 [Single-Page Application (SPA)](https://nextjs.org/docs/app/guides/single-page-applications)로 시작한 뒤, 필요 시 서버가 요구되는 기능을 사용하도록 업그레이드할 수 있습니다.

Next.js는 [static exports](https://nextjs.org/docs/app/guides/static-exports)를 지원하므로 HTML/CSS/JS 정적 자산을 제공할 수 있는 모든 웹 서버에 배포하고 호스팅할 수 있습니다. AWS S3, Nginx, Apache 같은 도구가 여기에 해당합니다.

[static export](https://nextjs.org/docs/app/guides/static-exports)로 실행하면 서버가 필요한 Next.js 기능은 **지원되지 않습니다**. [자세히 알아보기](https://nextjs.org/docs/app/guides/static-exports#unsupported-features).

### 템플릿[](https://nextjs.org/docs/pages/getting-started/deploying#templates-2)

  * [GitHub Pages](https://github.com/nextjs/deploy-github-pages)



## Adapters[](https://nextjs.org/docs/pages/getting-started/deploying#adapters)

Next.js는 다양한 플랫폼에서 해당 인프라 기능을 활용할 수 있도록 조정할 수 있습니다.

각 제공자의 문서를 참고하여 지원되는 Next.js 기능을 확인하세요:

  * [Appwrite Sites](https://appwrite.io/docs/products/sites/quick-start/nextjs)
  * [AWS Amplify Hosting](https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components)
  * [Cloudflare](https://developers.cloudflare.com/workers/frameworks/framework-guides/nextjs)
  * [Deno Deploy](https://docs.deno.com/examples/next_tutorial)
  * [Firebase App Hosting](https://firebase.google.com/docs/app-hosting/get-started)
  * [Netlify](https://docs.netlify.com/frameworks/next-js/overview/#next-js-support-on-netlify)
  * [Vercel](https://vercel.com/docs/frameworks/nextjs)



> **참고:** 모든 플랫폼이 채택할 수 있는 [Deployment Adapters API](https://github.com/vercel/next.js/discussions/77740)를 개발 중입니다. 완료되면 자체 어댑터를 작성하는 방법에 대한 문서를 추가할 예정입니다.

도움이 되었나요?

지원됨.

전송
