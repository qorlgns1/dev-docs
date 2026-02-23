---
title: 'next.config.js: serverExternalPackages'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js: serverExternalPackages | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)serverExternalPackages

페이지 복사

# serverExternalPackages

마지막 업데이트 2026년 2월 20일

[Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)와 [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) 내부에서 사용하는 의존성은 Next.js가 자동으로 번들링합니다.

특정 의존성이 Node.js 전용 기능을 사용한다면, 해당 의존성을 Server Components 번들링에서 선택적으로 제외하고 네이티브 Node.js `require`를 사용할 수 있습니다.

next.config.js
[code]
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      serverExternalPackages: ['@acme/ui'],
    }
     
    module.exports = nextConfig
[/code]

Next.js에는 현재 호환성 작업 중이며 자동으로 제외되는 [인기 패키지의 짧은 목록](https://github.com/vercel/next.js/blob/canary/packages/next/src/lib/server-external-packages.jsonc)이 포함되어 있습니다.

  * `@alinea/generated`
  * `@appsignal/nodejs`
  * `@aws-sdk/client-s3`
  * `@aws-sdk/s3-presigned-post`
  * `@blockfrost/blockfrost-js`
  * `@highlight-run/node`
  * `@huggingface/transformers`
  * `@jpg-store/lucid-cardano`
  * `@libsql/client`
  * `@mikro-orm/core`
  * `@mikro-orm/knex`
  * `@node-rs/argon2`
  * `@node-rs/bcrypt`
  * `@prisma/client`
  * `@react-pdf/renderer`
  * `@sentry/profiling-node`
  * `@sparticuz/chromium`
  * `@sparticuz/chromium-min`
  * `@statsig/statsig-node-core`
  * `@swc/core`
  * `@xenova/transformers`
  * `@zenstackhq/runtime`
  * `argon2`
  * `autoprefixer`
  * `aws-crt`
  * `bcrypt`
  * `better-sqlite3`
  * `canvas`
  * `chromadb-default-embed`
  * `config`
  * `cpu-features`
  * `cypress`
  * `dd-trace`
  * `eslint`
  * `express`
  * `firebase-admin`
  * `htmlrewriter`
  * `import-in-the-middle`
  * `isolated-vm`
  * `jest`
  * `jsdom`
  * `keyv`
  * `libsql`
  * `mdx-bundler`
  * `mongodb`
  * `mongoose`
  * `newrelic`
  * `next-mdx-remote`
  * `next-seo`
  * `node-cron`
  * `node-pty`
  * `node-web-audio-api`
  * `onnxruntime-node`
  * `oslo`
  * `pg`
  * `pino`
  * `pino-pretty`
  * `pino-roll`
  * `playwright`
  * `playwright-core`
  * `postcss`
  * `prettier`
  * `prisma`
  * `puppeteer-core`
  * `puppeteer`
  * `ravendb`
  * `require-in-the-middle`
  * `rimraf`
  * `sharp`
  * `shiki`
  * `sqlite3`
  * `thread-stream`
  * `ts-morph`
  * `ts-node`
  * `typescript`
  * `vscode-oniguruma`
  * `webpack`
  * `websocket`
  * `zeromq`



Version|Changes  
---|---  
`v15.0.0`| 실험 단계에서 안정화 단계로 이동했으며, `serverComponentsExternalPackages`에서 `serverExternalPackages`로 이름이 변경되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
