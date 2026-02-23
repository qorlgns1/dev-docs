---
title: 'next.config.js: reactCompiler'
description: 'Next.js는 컴포넌트 렌더링을 자동으로 최적화해 성능을 높이도록 설계된 React Compiler를 지원합니다. 이를 통해 와 으로 수동 메모이제이션을 해야 하는 필요성이 줄어듭니다.'
---

# next.config.js: reactCompiler | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)reactCompiler

Copy page

# reactCompiler

마지막 업데이트 2026년 2월 20일

Next.js는 컴포넌트 렌더링을 자동으로 최적화해 성능을 높이도록 설계된 [React Compiler](https://react.dev/learn/react-compiler/introduction)를 지원합니다. 이를 통해 `useMemo`와 `useCallback`으로 수동 메모이제이션을 해야 하는 필요성이 줄어듭니다.

Next.js에는 React Compiler를 더 효율적으로 만드는 SWC 기반의 맞춤형 성능 최적화가 포함되어 있습니다. 모든 파일에 컴파일러를 실행하는 대신, Next.js가 프로젝트를 분석해 관련 파일에만 React Compiler를 적용하므로 불필요한 작업을 피하고 Babel 플러그인 단독 사용보다 빌드 속도가 빨라집니다.

## 작동 방식[](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler#how-it-works)

React Compiler는 Babel 플러그인을 통해 실행됩니다. 빌드 속도를 유지하기 위해 Next.js는 JSX나 React Hooks가 있는 파일 등 관련 파일에만 React Compiler를 적용하는 SWC 최적화를 사용합니다.

이 방식은 전체를 컴파일하지 않아도 되어 성능 비용을 최소화합니다. 기본 Rust 기반 컴파일러와 비교하면 빌드가 약간 느릴 수 있지만 영향은 작고 국소적입니다.

사용하려면 `babel-plugin-react-compiler`를 설치하세요.

pnpm npm yarn bun

터미널
```bash
pnpm add -D babel-plugin-react-compiler
```

그런 다음 `next.config.js`에 `reactCompiler` 옵션을 추가합니다.

next.config.ts

JavaScript TypeScript
```ts
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  reactCompiler: true,
}
 
export default nextConfig
```

## 주석[](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler#annotations)

컴파일러를 다음과 같이 옵트인 모드로 설정할 수 있습니다.

next.config.ts

JavaScript TypeScript
```ts
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  reactCompiler: {
    compilationMode: 'annotation',
  },
}
 
export default nextConfig
```

그다음 React의 `"use memo"` 지시문으로 특정 컴포넌트나 훅에 주석을 추가해 옵트인할 수 있습니다.

app/page.tsx

JavaScript TypeScript
```tsx
export default function Page() {
  'use memo'
  // ...
}
```

> **참고:** 반대로 옵트아웃하려면 React의 `"use no memo"` 지시문을 사용할 수 있습니다.

Was this helpful?

supported.

Send
