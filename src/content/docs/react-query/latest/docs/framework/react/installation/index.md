---
title: '요구 사항'
description: 'React Query는 NPM을 통해 설치하거나, ESM.sh에서 제공하는 전통적인 를 사용할 수 있습니다.'
---

# 설치

React Query는 [NPM](https://npmjs.com/)을 통해 설치하거나, [ESM.sh](https://esm.sh/)에서 제공하는 전통적인 `<script>`를 사용할 수 있습니다.

### NPM

```bash
npm i @tanstack/react-query
```

또는

```bash
pnpm add @tanstack/react-query
```

또는

```bash
yarn add @tanstack/react-query
```

또는

```bash
bun add @tanstack/react-query
```

[//]: # 'Compatibility'

React Query는 React v18+와 호환되며 ReactDOM 및 React Native와 함께 동작합니다.

> 다운로드 전에 직접 사용해 보고 싶나요? [simple](https://tanstack.com/query/latest/docs/framework/react/examples/simple) 또는 [basic](https://tanstack.com/query/latest/docs/framework/react/examples/basic) 예제를 살펴보세요!

[//]: # 'Compatibility'

### CDN

모듈 번들러나 패키지 관리자를 사용하지 않는 경우에도 [ESM.sh](https://esm.sh/)와 같은 ESM 호환 CDN을 통해 이 라이브러리를 사용할 수 있습니다. HTML 파일 하단에 `<script type="module">` 태그를 추가하기만 하면 됩니다.

[//]: # 'CDNExample'

```html
<script type="module">
  import React from 'https://esm.sh/react@18.2.0'
  import ReactDOM from 'https://esm.sh/react-dom@18.2.0'
  import { QueryClient } from 'https://esm.sh/@tanstack/react-query'
</script>
```

> JSX 없이 React를 사용하는 방법은 [여기](https://react.dev/reference/react/createElement#creating-an-element-without-jsx)에서 확인할 수 있습니다.

[//]: # 'CDNExample'

### 요구 사항

React Query는 최신 브라우저에 최적화되어 있습니다. 다음 브라우저 구성과 호환됩니다.

```
Chrome >= 91
Firefox >= 90
Edge >= 91
Safari >= 15
iOS >= 15
Opera >= 77
```

> 환경에 따라 폴리필을 추가해야 할 수도 있습니다. 구형 브라우저를 지원하려면 `node_modules`에서 라이브러리를 직접 트랜스파일해야 합니다.

### 권장 사항

코드를 작성하면서 버그와 불일치를 잡아내기 위해 [ESLint Plugin Query](https://tanstack.com/query/latest/docs/eslint/eslint-plugin-query.md) 사용을 권장합니다. 설치 방법은 다음과 같습니다.

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

