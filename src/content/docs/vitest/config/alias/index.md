---
title: "alias"
description: "테스트 실행 시 사용할 사용자 정의 alias를 정의합니다. 이 값들은 의 alias와 병합됩니다."
---

# alias

- **유형:** `Record<string, string> | Array<{ find: string | RegExp, replacement: string, customResolver?: ResolverFunction | ResolverObject }>`

테스트 실행 시 사용할 사용자 정의 alias를 정의합니다. 이 값들은 `resolve.alias`의 alias와 병합됩니다.

::: warning
Vitest는 테스트를 실행할 때 Vite SSR 프리미티브를 사용하며, 여기에는 [특정한 함정](https://vitejs.dev/guide/ssr.html#ssr-externals)이 있습니다.

1. alias는 [inlined](#server-deps-inline) 모듈(기본적으로 모든 소스 코드는 inlined됨)이 `import` 키워드로 직접 가져오는 모듈에만 영향을 줍니다.
1. Vitest는 `require` 호출에 대한 alias를 지원하지 않습니다.
1. 외부 의존성(예: `react` -> `preact`)에 alias를 적용하는 경우, 외부화된 의존성에서도 동작하게 하려면 실제 `node_modules` 패키지에 alias를 적용하는 것이 좋을 수 있습니다. [Yarn](https://classic.yarnpkg.com/en/docs/cli/add/#toc-yarn-add-alias)과 [pnpm](https://pnpm.io/aliases/) 모두 `npm:` 접두사를 통한 alias를 지원합니다.
   :::
