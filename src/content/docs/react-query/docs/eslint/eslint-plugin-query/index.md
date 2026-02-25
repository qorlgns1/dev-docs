---
title: 'ESLint Plugin Query'
description: 'TanStack Query에는 전용 ESLint 플러그인이 포함되어 있습니다. 이 플러그인은 모범 사례를 강제하고, 흔히 발생하는 실수를 피할 수 있도록 도와줍니다.'
---

Source URL: https://tanstack.com/query/latest/docs/eslint/eslint-plugin-query

# ESLint Plugin Query

TanStack Query에는 전용 ESLint 플러그인이 포함되어 있습니다. 이 플러그인은 모범 사례를 강제하고, 흔히 발생하는 실수를 피할 수 있도록 도와줍니다.

## 설치

이 플러그인은 별도 패키지이므로 직접 설치해야 합니다:

```bash
npm i -D @tanstack/eslint-plugin-query
```

또는

```bash
pnpm add -D @tanstack/eslint-plugin-query
```

또는

```bash
yarn add -D @tanstack/eslint-plugin-query
```

또는

```bash
bun add -D @tanstack/eslint-plugin-query
```

## Flat Config (`eslint.config.js`)

### 권장 설정

플러그인의 모든 권장 규칙을 활성화하려면 다음 설정을 추가하세요:

```js
import pluginQuery from '@tanstack/eslint-plugin-query'

export default [
  ...pluginQuery.configs['flat/recommended'],
  // Any other config...
]
```

### 사용자 지정 설정

또는 플러그인을 로드한 뒤, 사용하려는 규칙만 선택해서 설정할 수 있습니다:

```js
import pluginQuery from '@tanstack/eslint-plugin-query'

export default [
  {
    plugins: {
      '@tanstack/query': pluginQuery,
    },
    rules: {
      '@tanstack/query/exhaustive-deps': 'error',
    },
  },
  // Any other config...
]
```

## Legacy Config (`.eslintrc`)

### 권장 설정

플러그인의 모든 권장 규칙을 활성화하려면 `extends`에 `plugin:@tanstack/query/recommended`를 추가하세요:

```json
{
  "extends": ["plugin:@tanstack/query/recommended"]
}
```

### 사용자 지정 설정

또는 `plugins` 섹션에 `@tanstack/query`를 추가하고, 사용하려는 규칙을 설정하세요:

```json
{
  "plugins": ["@tanstack/query"],
  "rules": {
    "@tanstack/query/exhaustive-deps": "error"
  }
}
```

## 규칙

- [@tanstack/query/exhaustive-deps](https://tanstack.com/query/latest/docs/eslint/exhaustive-deps.md)
- [@tanstack/query/no-rest-destructuring](https://tanstack.com/query/latest/docs/eslint/no-rest-destructuring.md)
- [@tanstack/query/stable-query-client](https://tanstack.com/query/latest/docs/eslint/stable-query-client.md)
- [@tanstack/query/no-unstable-deps](https://tanstack.com/query/latest/docs/eslint/no-unstable-deps.md)
- [@tanstack/query/infinite-query-property-order](https://tanstack.com/query/latest/docs/eslint/infinite-query-property-order.md)
- [@tanstack/query/no-void-query-fn](https://tanstack.com/query/latest/docs/eslint/no-void-query-fn.md)
- [@tanstack/query/mutation-property-order](https://tanstack.com/query/latest/docs/eslint/mutation-property-order.md)

