---
title: '구성: ESLint'
description: 'Next.js는 애플리케이션에서 일반적인 문제를 쉽게 찾아낼 수 있도록 라는 ESLint 구성 패키지를 제공합니다. 이 패키지는  플러그인과 , 의 권장 규칙 세트를 함께 포함합니다.'
---

# 구성: ESLint | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/eslint

Copy page

# ESLint

최종 업데이트 2026년 2월 20일

Next.js는 애플리케이션에서 일반적인 문제를 쉽게 찾아낼 수 있도록 [`eslint-config-next`](https://www.npmjs.com/package/eslint-config-next)라는 ESLint 구성 패키지를 제공합니다. 이 패키지는 [`@next/eslint-plugin-next`](https://www.npmjs.com/package/@next/eslint-plugin-next) 플러그인과 [`eslint-plugin-react`](https://www.npmjs.com/package/eslint-plugin-react), [`eslint-plugin-react-hooks`](https://www.npmjs.com/package/eslint-plugin-react-hooks)의 권장 규칙 세트를 함께 포함합니다.

이 패키지는 두 가지 기본 구성을 제공합니다.

  * **`eslint-config-next`** : Next.js, React, React Hooks 규칙이 포함된 기본 구성입니다. JavaScript와 TypeScript 파일을 모두 지원합니다.
  * **`eslint-config-next/core-web-vitals`** : 기본 구성의 모든 내용을 포함하며, [Core Web Vitals](https://web.dev/vitals/)에 영향을 주는 규칙을 경고에서 오류로 상향합니다. 대부분의 프로젝트에 권장됩니다.

또한 TypeScript 프로젝트의 경우:

  * **`eslint-config-next/typescript`** : [`typescript-eslint`](https://typescript-eslint.io/)의 TypeScript 전용 린팅 규칙을 추가합니다. 기본 구성 또는 core-web-vitals 구성과 함께 사용하세요.

## Setup ESLint[](https://nextjs.org/docs/pages/api-reference/config/eslint#setup-eslint)

ESLint CLI(플랫 구성)를 사용해 빠르게 린팅을 설정하세요.

  1. ESLint와 Next.js 구성을 설치합니다.

pnpmnpmyarnbun

Terminal
[code]pnpm add -D eslint eslint-config-next
[/code]

  2. Next.js 구성이 포함된 `eslint.config.mjs`를 생성합니다.

eslint.config.mjs
[code]import { defineConfig, globalIgnores } from 'eslint/config'
         import nextVitals from 'eslint-config-next/core-web-vitals'

         const eslintConfig = defineConfig([
           ...nextVitals,
           // Override default ignores of eslint-config-next.
           globalIgnores([
             // Default ignores of eslint-config-next:
             '.next/**',
             'out/**',
             'build/**',
             'next-env.d.ts',
           ]),
         ])

         export default eslintConfig
[/code]

  3. ESLint를 실행합니다.

pnpmnpmyarnbun

Terminal
[code]pnpm exec eslint .
[/code]

## Reference[](https://nextjs.org/docs/pages/api-reference/config/eslint#reference)

`eslint-config-next` 패키지는 다음 ESLint 플러그인의 `recommended` 규칙 세트를 포함합니다.

  * [`eslint-plugin-react`](https://www.npmjs.com/package/eslint-plugin-react)
  * [`eslint-plugin-react-hooks`](https://www.npmjs.com/package/eslint-plugin-react-hooks)
  * [`@next/eslint-plugin-next`](https://www.npmjs.com/package/@next/eslint-plugin-next)

### Rules[](https://nextjs.org/docs/pages/api-reference/config/eslint#rules)

포함된 `@next/eslint-plugin-next` 규칙은 다음과 같습니다.

Enabled in recommended config| Rule| Description
---|---|---
| [@next/next/google-font-display](https://nextjs.org/docs/messages/google-font-display)| Google Fonts에서 font-display 동작을 강제합니다.
| [@next/next/google-font-preconnect](https://nextjs.org/docs/messages/google-font-preconnect)| Google Fonts와 함께 `preconnect` 사용을 보장합니다.
| [@next/next/inline-script-id](https://nextjs.org/docs/messages/inline-script-id)| 인라인 콘텐츠가 있는 `next/script` 컴포넌트에 `id` 속성을 강제합니다.
| [@next/next/next-script-for-ga](https://nextjs.org/docs/messages/next-script-for-ga)| Google Analytics 인라인 스크립트를 사용할 때 `next/script` 컴포넌트를 권장합니다.
| [@next/next/no-assign-module-variable](https://nextjs.org/docs/messages/no-assign-module-variable)| `module` 변수에 대한 할당을 방지합니다.
| [@next/next/no-async-client-component](https://nextjs.org/docs/messages/no-async-client-component)| 클라이언트 컴포넌트가 async 함수가 되지 않도록 합니다.
| [@next/next/no-before-interactive-script-outside-document](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document)| `pages/_document.js` 외부에서 `next/script`의 `beforeInteractive` 전략 사용을 방지합니다.
| [@next/next/no-css-tags](https://nextjs.org/docs/messages/no-css-tags)| 수동 스타일시트 태그를 방지합니다.
| [@next/next/no-document-import-in-page](https://nextjs.org/docs/messages/no-document-import-in-page)| `pages/_document.js` 외부에서 `next/document`를 가져오는 것을 방지합니다.
| [@next/next/no-duplicate-head](https://nextjs.org/docs/messages/no-duplicate-head)| `pages/_document.js`에서 `<Head>`가 중복 사용되지 않도록 합니다.
| [@next/next/no-head-element](https://nextjs.org/docs/messages/no-head-element)| `<head>` 요소 사용을 방지합니다.
| [@next/next/no-head-import-in-document](https://nextjs.org/docs/messages/no-head-import-in-document)| `pages/_document.js`에서 `next/head` 사용을 방지합니다.
| [@next/next/no-html-link-for-pages](https://nextjs.org/docs/messages/no-html-link-for-pages)| 내부 Next.js 페이지 탐색에 `<a>` 요소 사용을 방지합니다.
| [@next/next/no-img-element](https://nextjs.org/docs/messages/no-img-element)| 느린 LCP와 높은 대역폭 때문에 `<img>` 요소 사용을 방지합니다.
| [@next/next/no-page-custom-font](https://nextjs.org/docs/messages/no-page-custom-font)| 페이지 전용 커스텀 폰트를 방지합니다.
| [@next/next/no-script-component-in-head](https://nextjs.org/docs/messages/no-script-component-in-head)| `next/head` 컴포넌트 내에서 `next/script` 사용을 방지합니다.
| [@next/next/no-styled-jsx-in-document](https://nextjs.org/docs/messages/no-styled-jsx-in-document)| `pages/_document.js`에서 `styled-jsx` 사용을 방지합니다.
| [@next/next/no-sync-scripts](https://nextjs.org/docs/messages/no-sync-scripts)| 동기 스크립트를 방지합니다.
| [@next/next/no-title-in-document-head](https://nextjs.org/docs/messages/no-title-in-document-head)| `next/document`의 `Head` 컴포넌트에서 `<title>` 사용을 방지합니다.
| @next/next/no-typos| [Next.js 데이터 패칭 함수](https://nextjs.org/docs/pages/building-your-application/data-fetching)에서 흔한 오타를 방지합니다.
| [@next/next/no-unwanted-polyfillio](https://nextjs.org/docs/messages/no-unwanted-polyfillio)| Polyfill.io의 중복 폴리필을 방지합니다.

개발 중에는 [integration](https://eslint.org/docs/user-guide/integrations#editors)을 적절히 사용해 코드 에디터에서 경고와 오류를 바로 확인하는 것이 좋습니다.

`next lint` 제거

Next.js 16부터 `next lint`가 제거됩니다.

이에 따라 Next 구성 파일의 `eslint` 옵션은 더 이상 필요하지 않으므로 안전하게 제거할 수 있습니다.

## Examples[](https://nextjs.org/docs/pages/api-reference/config/eslint#examples)

### 모노레포 내에서 루트 디렉터리 지정[](https://nextjs.org/docs/pages/api-reference/config/eslint#specifying-a-root-directory-within-a-monorepo)

Next.js가 루트 디렉터리에 설치되지 않은 프로젝트(예: 모노레포)에서 `@next/eslint-plugin-next`를 사용하는 경우 `eslint.config.mjs`의 `settings` 속성을 통해 Next.js 애플리케이션 위치를 지정할 수 있습니다.

eslint.config.mjs
[code]
    import { defineConfig } from 'eslint/config'
    import eslintNextPlugin from '@next/eslint-plugin-next'

    const eslintConfig = defineConfig([
      {
        files: ['**/*.{js,jsx,ts,tsx}'],
        plugins: {
          next: eslintNextPlugin,
        },
        settings: {
          next: {
            rootDir: 'packages/my-app/',
          },
        },
      },
    ])

    export default eslintConfig
[/code]

`rootDir`는 경로(상대 또는 절대), glob(예: `"packages/*/"`), 혹은 경로 및/또는 glob 배열이 될 수 있습니다.

### 규칙 비활성화[](https://nextjs.org/docs/pages/api-reference/config/eslint#disabling-rules)

지원되는 플러그인(`react`, `react-hooks`, `next`)에서 제공하는 규칙을 수정하거나 비활성화하려면 `eslint.config.mjs`의 `rules` 속성에서 바로 변경할 수 있습니다.

eslint.config.mjs
[code]
    import { defineConfig, globalIgnores } from 'eslint/config'
    import nextVitals from 'eslint-config-next/core-web-vitals'

    const eslintConfig = defineConfig([
      ...nextVitals,
      {
        rules: {
          'react/no-unescaped-entities': 'off',
          '@next/next/no-page-custom-font': 'off',
        },
      },
      // Override default ignores of eslint-config-next.
      globalIgnores([
        // Default ignores of eslint-config-next:
        '.next/**',
        'out/**',
        'build/**',
        'next-env.d.ts',
      ]),
    ])

    export default eslintConfig
[/code]

### Core Web Vitals와 함께 사용[](https://nextjs.org/docs/pages/api-reference/config/eslint#with-core-web-vitals)

ESLint 구성에서 `eslint-config-next/core-web-vitals` 구성을 활성화하세요.

eslint.config.mjs
[code]
    import { defineConfig, globalIgnores } from 'eslint/config'
    import nextVitals from 'eslint-config-next/core-web-vitals'

    const eslintConfig = defineConfig([
      ...nextVitals,
      // Override default ignores of eslint-config-next.
      globalIgnores([
        // Default ignores of eslint-config-next:
        '.next/**',
        'out/**',
        'build/**',
        'next-env.d.ts',
      ]),
    ])

    export default eslintConfig
[/code]

`eslint-config-next/core-web-vitals`는 `@next/eslint-plugin-next`의 일부 린트 규칙을 경고에서 오류로 상향해 [Core Web Vitals](https://web.dev/vitals/) 지표 향상에 도움이 됩니다.

> [Create Next App](https://nextjs.org/docs/app/api-reference/cli/create-next-app)으로 새 애플리케이션을 만들면 `eslint-config-next/core-web-vitals` 구성이 자동으로 포함됩니다.

### TypeScript와 함께 사용[](https://nextjs.org/docs/pages/api-reference/config/eslint#with-typescript)

Next.js ESLint 규칙에 추가로, `create-next-app --typescript`는 `eslint-config-next/typescript`를 통해 TypeScript 전용 린트 규칙도 구성에 추가합니다.

eslint.config.mjs
[code]
    import { defineConfig, globalIgnores } from 'eslint/config'
    import nextVitals from 'eslint-config-next/core-web-vitals'
    import nextTs from 'eslint-config-next/typescript'

    const eslintConfig = defineConfig([
      ...nextVitals,
      ...nextTs,
      // Override default ignores of eslint-config-next.
      globalIgnores([
        // Default ignores of eslint-config-next:
        '.next/**',
        'out/**',
        'build/**',
        'next-env.d.ts',
      ]),
    ])

    export default eslintConfig
[/code]

이러한 규칙은 [`plugin:@typescript-eslint/recommended`](https://typescript-eslint.io/linting/configs#recommended)를 기반으로 합니다. 자세한 내용은 [typescript-eslint > Configs](https://typescript-eslint.io/linting/configs)를 참고하세요.

### Prettier와 함께 사용[](https://nextjs.org/docs/pages/api-reference/config/eslint#with-prettier)

ESLint는 코드 포매팅 규칙도 포함하고 있어 기존 [Prettier](https://prettier.io/) 설정과 충돌할 수 있습니다. ESLint와 Prettier가 함께 동작하도록 [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)를 ESLint 구성에 포함하는 것을 권장합니다.

먼저, 의존성을 설치합니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D eslint-config-prettier
[/code]

그다음 기존 ESLint 구성에 `prettier`를 추가합니다.

eslint.config.mjs
[code]
    import { defineConfig, globalIgnores } from 'eslint/config'
    import nextVitals from 'eslint-config-next/core-web-vitals'
    import prettier from 'eslint-config-prettier/flat'

    const eslintConfig = defineConfig([
      ...nextVitals,
      prettier,
      // Override default ignores of eslint-config-next.
      globalIgnores([
        // Default ignores of eslint-config-next:
        '.next/**',
        'out/**',
        'build/**',
        'next-env.d.ts',
      ]),
    ])

    export default eslintConfig
[/code]

### 스테이징된 파일에서 린트 실행[](https://nextjs.org/docs/pages/api-reference/config/eslint#running-lint-on-staged-files)

[lint-staged](https://github.com/okonet/lint-staged)를 사용해 스테이징된 git 파일에 ESLint를 실행하려면, 프로젝트 루트의 `.lintstagedrc.js` 파일에 아래 내용을 추가하세요:

.lintstagedrc.js
```
    const path = require('path')

    const buildEslintCommand = (filenames) =>
      `eslint --fix ${filenames
        .map((f) => `"${path.relative(process.cwd(), f)}"`)
        .join(' ')}`

    module.exports = {
      '*.{js,jsx,ts,tsx}': [buildEslintCommand],
    }
```

## 기존 구성 마이그레이션[](https://nextjs.org/docs/pages/api-reference/config/eslint#migrating-existing-config)

애플리케이션에 이미 ESLint를 설정해 두었다면, 환경에 따라 Next.js 린팅 규칙을 통합하는 두 가지 방법이 있습니다.

#### 플러그인을 직접 사용하기[](https://nextjs.org/docs/pages/api-reference/config/eslint#using-the-plugin-directly)

다음 중 하나라도 이미 구성되어 있다면 `@next/eslint-plugin-next`를 직접 사용하세요.

  * 별도 설치했거나 다른 구성(`airbnb`, `react-app` 등)을 통해 가져온 충돌 가능한 플러그인:
    * `react`
    * `react-hooks`
    * `jsx-a11y`
    * `import`
  * Next.js 기본값과 다른 사용자 정의 `parserOptions` ( [Babel 구성을 커스터마이즈](https://nextjs.org/docs/pages/guides/babel)한 경우에만 해당)
  * 사용자 정의 Node.js 및/또는 TypeScript [resolver](https://github.com/benmosher/eslint-plugin-import#resolvers)를 사용한 `eslint-plugin-import`

이러한 경우에는 동일한 플러그인이나 파서를 여러 구성에서 불러오면서 발생할 수 있는 충돌을 피하기 위해 `@next/eslint-plugin-next`를 직접 사용합니다.

먼저 플러그인을 설치하세요:

pnpmnpmyarnbun

Terminal
```
    pnpm add -D @next/eslint-plugin-next
```

그다음 ESLint 구성에 추가합니다:

eslint.config.mjs
```
    import { defineConfig } from 'eslint/config'
    import nextPlugin from '@next/eslint-plugin-next'

    const eslintConfig = defineConfig([
      // Your other configurations...
      {
        files: ['**/*.{js,jsx,ts,tsx}'],
        plugins: {
          '@next/next': nextPlugin,
        },
        rules: {
          ...nextPlugin.configs.recommended.rules,
        },
      },
    ])

    export default eslintConfig
```

이 방식은 동일한 플러그인이나 파서를 여러 구성에서 가져올 때 발생할 수 있는 충돌이나 오류 위험을 제거합니다.

#### 기존 구성에 추가하기[](https://nextjs.org/docs/pages/api-reference/config/eslint#adding-to-existing-config)

기존 ESLint 설정에 Next.js를 추가하는 경우, 배열에 Next.js 구성을 전개하세요:

eslint.config.mjs
```
    import nextConfig from 'eslint-config-next/core-web-vitals'
    // Your other config imports...

    const eslintConfig = [
      // Your other configurations...
      ...nextConfig,
    ]

    export default eslintConfig
```

`...nextConfig`를 전개하면 파일 패턴, 플러그인, 규칙, ignore, 파서 설정을 포함한 여러 구성 객체가 추가됩니다. ESLint는 구성을 순서대로 적용하므로, 뒤에 오는 규칙이 일치하는 파일에 대해 앞선 규칙을 덮어쓸 수 있습니다.

> **알아두면 좋아요:** 이 방식은 단순한 설정에서 잘 작동합니다. 복잡한 파일 패턴이나 플러그인 구성이 있어 충돌 가능성이 있다면, 보다 세밀한 제어를 위해 플러그인을 직접 사용하는 방법(위 참고)을 고려하세요.

Version|Changes
---|---
`v16.0.0`| `next lint`와 `eslint` next.config.js 옵션이 제거되고 ESLint CLI가 권장됩니다. 마이그레이션을 도와주는 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-from-next-lint-to-eslint-cli)가 제공됩니다.

지원됩니다.

보내기
