---
title: 'next.config.js 옵션: output'
description: '빌드 중 Next.js는 각 페이지와 그 의존성을 자동으로 추적하여 애플리케이션을 프로덕션 버전으로 배포하는 데 필요한 모든 파일을 파악합니다.'
---

# next.config.js 옵션: output | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/output

# output

마지막 업데이트 2026년 2월 20일

빌드 중 Next.js는 각 페이지와 그 의존성을 자동으로 추적하여 애플리케이션을 프로덕션 버전으로 배포하는 데 필요한 모든 파일을 파악합니다.

이 기능은 배포 크기를 크게 줄이는 데 도움이 됩니다. 과거에는 Docker로 배포할 때 `next start`를 실행하려면 패키지의 `dependencies` 전체를 설치해야 했습니다. Next.js 12부터는 `.next/` 디렉터리의 Output File Tracing을 활용해 필요한 파일만 포함할 수 있습니다.

또한 더 이상 권장되지 않는 `serverless` 타깃이 야기하던 여러 문제와 중복을 제거합니다.

## 작동 방식[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output#how-it-works)

`next build` 중 Next.js는 [`@vercel/nft`](https://github.com/vercel/nft)를 사용해 `import`, `require`, `fs` 사용을 정적 분석하여 각 페이지가 로드할 수 있는 모든 파일을 결정합니다.

Next.js 프로덕션 서버 역시 필요한 파일이 추적되어 `.next/next-server.js.nft.json`에 출력되며, 프로덕션에서 이를 활용할 수 있습니다.

`.next` 출력 디렉터리에 생성되는 `.nft.json` 파일을 활용하려면 각 추적 파일 안에 `.nft.json` 파일을 기준으로 상대 경로로 나열된 파일 목록을 읽고 배포 위치로 복사하면 됩니다.

## 추적된 파일 자동 복사[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output#automatically-copying-traced-files)

Next.js는 프로덕션 배포에 필요한 파일만(일부 `node_modules` 포함)을 복사하는 `standalone` 폴더를 자동으로 만들 수 있습니다.

이 자동 복사를 활용하려면 `next.config.js`에서 다음과 같이 활성화합니다:

next.config.js
```
    module.exports = {
      output: 'standalone',
    }
```

그러면 `.next/standalone` 폴더가 생성되며, `node_modules`를 설치하지 않고도 독립적으로 배포할 수 있습니다.

또한 최소한의 `server.js` 파일도 출력되어 `next start` 대신 사용할 수 있습니다. 이 최소 서버는 기본적으로 `public` 또는 `.next/static` 폴더를 복사하지 않는데, 이상적으로는 CDN이 이를 처리해야 하기 때문입니다. 다만 이러한 폴더를 수동으로 `standalone/public`, `standalone/.next/static`으로 복사하면 `server.js`가 자동으로 제공할 수 있습니다.

수동 복사를 위해 `next build` 이후 `cp` CLI를 사용할 수 있습니다:

Terminal
```
    cp -r public .next/standalone/ && cp -r .next/static .next/standalone/.next/
```

로컬에서 최소 `server.js` 파일을 시작하려면 다음 명령을 실행합니다:

Terminal
```
    node .next/standalone/server.js
```

> **알면 좋아요** :
>
>   * `next.config.js`는 `next build` 중 읽혀 `server.js` 출력 파일에 직렬화됩니다.
>   * 프로젝트가 특정 포트나 호스트 이름에 바인딩되어야 한다면 `server.js` 실행 전에 `PORT` 또는 `HOSTNAME` 환경 변수를 정의할 수 있습니다. 예를 들어 `PORT=8080 HOSTNAME=0.0.0.0 node server.js`를 실행하면 `http://0.0.0.0:8080`에서 서버가 시작됩니다.
>

## 주의 사항[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output#caveats)

  * 모노레포 설정에서 추적 시 기본적으로 프로젝트 디렉터리가 사용됩니다. 예를 들어 `next build packages/web-app`을 실행하면 `packages/web-app`이 추적 루트가 되며, 해당 폴더 밖의 파일은 포함되지 않습니다. 이 폴더 밖의 파일을 포함하려면 `next.config.js`에서 `outputFileTracingRoot`를 설정하세요.

packages/web-app/next.config.js
```
    const path = require('path')

    module.exports = {
      // this includes files from the monorepo base two directories up
      outputFileTracingRoot: path.join(__dirname, '../../'),
    }
```

  * Next.js가 필요한 파일을 포함하지 못하거나 사용되지 않는 파일을 잘못 포함하는 경우가 있습니다. 이런 경우 `next.config.js`에서 각각 `outputFileTracingExcludes`와 `outputFileTracingIncludes`를 활용할 수 있습니다. 각 옵션은 **경로 글롭**(예: `/api/hello`)을 키로, 프로젝트 루트 기준으로 해석되는 **글롭 패턴**을 값으로 받으며, 추적에 포함하거나 제외할 파일을 지정합니다.

> **알면 좋아요** : 모노레포에서 `project root`는 모노레포 루트가 아니라 Next.js 프로젝트 루트(예: packages/web-app처럼 next.config.js가 있는 폴더)를 의미합니다.

next.config.js
```
    module.exports = {
      outputFileTracingExcludes: {
        '/api/hello': ['./un-necessary-folder/**/*'],
      },
      outputFileTracingIncludes: {
        '/api/another': ['./necessary-folder/**/*'],
        '/api/login/\\[\\[\\.\\.\\.slug\\]\\]': [
          './node_modules/aws-crt/dist/bin/**/*',
        ],
      },
    }
```

`src/` 디렉터리를 사용하더라도 이 옵션을 작성하는 방식은 변하지 않습니다:

  * **키**는 여전히 라우트 경로(`'/api/hello'`, `'/products/[id]'` 등)와 일치합니다.
  * **값**은 프로젝트 루트 기준으로 해석되므로 `src/` 아래 경로를 참조할 수 있습니다.

next.config.js
```
    module.exports = {
      outputFileTracingIncludes: {
        '/products/*': ['src/lib/payments/**/*'],
        '/*': ['src/config/runtime/**/*.json'],
      },
      outputFileTracingExcludes: {
        '/api/*': ['src/temp/**/*', 'public/large-logs/**/*'],
      },
    }
```

`'/*'` 같은 전역 키를 사용해 모든 라우트를 대상으로 지정할 수도 있습니다:

next.config.js
```
    module.exports = {
      outputFileTracingIncludes: {
        '/*': ['src/i18n/locales/**/*.json'],
      },
    }
```

이 옵션은 서버 트레이스에 적용되며, 서버 트레이스 파일이 생성되지 않는 라우트에는 영향을 주지 않습니다:

  * Edge Runtime 라우트는 영향을 받지 않습니다.
  * 완전히 정적인 페이지는 영향을 받지 않습니다.

모노레포이거나 앱 폴더 밖의 파일을 포함해야 하는 경우 `outputFileTracingRoot`와 includes를 함께 사용합니다:

next.config.js
```
    const path = require('path')

    module.exports = {
      // Trace from the monorepo root
      outputFileTracingRoot: path.join(__dirname, '../../'),
      outputFileTracingIncludes: {
        '/route1': ['../shared/assets/**/*'],
      },
    }
```

> **알면 좋아요** :
>
>   * 교차 플랫폼 호환성을 위해 패턴에 슬래시(`/`)를 사용하는 것이 좋습니다.
>   * 패턴을 가능한 한 좁게 유지해 과도한 트레이스를 피하세요(레포 루트에서 `**/*`는 지양).
>

네이티브/런타임 에셋에 대한 일반적인 include 패턴:

next.config.js
```
    module.exports = {
      outputFileTracingIncludes: {
        '/*': ['node_modules/sharp/**/*', 'node_modules/aws-crt/dist/bin/**/*'],
      },
    }
```