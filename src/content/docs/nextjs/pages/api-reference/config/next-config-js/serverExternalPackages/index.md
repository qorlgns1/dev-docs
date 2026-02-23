---
title: 'next.config.js 옵션: serverExternalPackages'
description: '이러한 페이지는 이후 네이티브 Node.js 를 사용해 의존성을 해석합니다.'
---

# next.config.js 옵션: serverExternalPackages | Next.js

소스 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages

# serverExternalPackages

마지막 업데이트 2026년 2월 20일

[`bundlePagesRouterDependencies`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies) 옵션의 자동 번들링에 포함되지 않도록 특정 의존성을 선택적으로 제외합니다.

이러한 페이지는 이후 네이티브 Node.js `require`를 사용해 의존성을 해석합니다.

next.config.js
```
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      serverExternalPackages: ['@acme/ui'],
    }

    module.exports = nextConfig
```

Next.js에는 현재 호환성 작업이 진행 중이며 자동으로 제외되는 [인기 패키지의 짧은 목록](https://github.com/vercel/next.js/blob/canary/packages/next/src/lib/server-external-packages.jsonc)이 포함되어 있습니다.

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

보내기