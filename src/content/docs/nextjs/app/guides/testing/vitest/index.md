---
title: '테스트: Vitest'
description: 'Vitest와 React Testing Library는 단위 테스트에 자주 함께 사용됩니다. 이 가이드에서는 Next.js에서 Vitest를 설정하고 첫 번째 테스트를 작성하는 방법을 설명합니다.'
---

# 테스트: Vitest | Next.js

Source URL: https://nextjs.org/docs/app/guides/testing/vitest

Copy page

# Next.js와 Vitest 설정 방법

최종 업데이트 2026년 2월 20일

Vitest와 React Testing Library는 **단위 테스트**에 자주 함께 사용됩니다. 이 가이드에서는 Next.js에서 Vitest를 설정하고 첫 번째 테스트를 작성하는 방법을 설명합니다.

> **알아두면 좋아요:** `async` Server Component는 React 생태계에서 아직 새롭기 때문에 Vitest가 현재 지원하지 않습니다. 동기 Server 및 Client Component에 대해서는 계속 **단위 테스트**를 실행할 수 있지만, `async` 컴포넌트에는 **E2E 테스트** 사용을 권장합니다.

## 빠른 시작[](https://nextjs.org/docs/app/guides/testing/vitest#quickstart)

`create-next-app`과 Next.js [with-vitest](https://github.com/vercel/next.js/tree/canary/examples/with-vitest) 예제를 사용해 빠르게 시작할 수 있습니다:

pnpmnpmyarnbun

Terminal
```
    pnpm create next-app --example with-vitest with-vitest-app
```

## 수동 설정[](https://nextjs.org/docs/app/guides/testing/vitest#manual-setup)

Vitest를 수동으로 설정하려면 `vitest`와 다음 패키지를 dev dependency로 설치하세요:

pnpmnpmyarnbun

Terminal
```
    # Using TypeScript
    pnpm add -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom vite-tsconfig-paths
    # Using JavaScript
    pnpm add -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom
```

프로젝트 루트에 `vitest.config.mts|js` 파일을 만들고 다음 옵션을 추가합니다:

vitest.config.mts

JavaScriptTypeScript
```
    import { defineConfig } from 'vitest/config'
    import react from '@vitejs/plugin-react'
    import tsconfigPaths from 'vite-tsconfig-paths'

    export default defineConfig({
      plugins: [tsconfigPaths(), react()],
      test: {
        environment: 'jsdom',
      },
    })
```

Vitest 구성에 대한 자세한 내용은 [Vitest Configuration](https://vitest.dev/config/#configuration) 문서를 참고하세요.

이후 `package.json`에 `test` 스크립트를 추가합니다:

package.json
```
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "test": "vitest"
      }
    }
```

`npm run test`를 실행하면 Vitest가 기본적으로 프로젝트 변경 사항을 **감시(watch)** 합니다.

## 첫 번째 Vitest 단위 테스트 만들기[](https://nextjs.org/docs/app/guides/testing/vitest#creating-your-first-vitest-unit-test)

`<Page />` 컴포넌트가 헤딩을 제대로 렌더링하는지 확인하는 테스트를 만들어 모든 것이 정상 작동하는지 확인하세요:

app/page.tsx

JavaScriptTypeScript
```
    import Link from 'next/link'

    export default function Page() {
      return (
        <div>
          <h1>Home</h1>
          <Link href="/about">About</Link>
        </div>
      )
    }
```

__tests__/page.test.tsx

JavaScriptTypeScript
```
    import { expect, test } from 'vitest'
    import { render, screen } from '@testing-library/react'
    import Page from '../app/page'

    test('Page', () => {
      render(<Page />)
      expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
    })
```

> **알아두면 좋아요**: 위 예시는 일반적인 `__tests__` 규칙을 사용하지만, 테스트 파일은 `app` 라우터 내부에 함께 배치할 수도 있습니다.

## 테스트 실행하기[](https://nextjs.org/docs/app/guides/testing/vitest#running-your-tests)

다음 명령을 실행해 테스트를 돌립니다:

pnpmnpmyarnbun

Terminal
```
    pnpm test
```

## 추가 자료[](https://nextjs.org/docs/app/guides/testing/vitest#additional-resources)

아래 자료가 도움이 될 수 있습니다:

  * [Next.js with Vitest example](https://github.com/vercel/next.js/tree/canary/examples/with-vitest)
  * [Vitest Docs](https://vitest.dev/guide/)
  * [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)

Was this helpful?

supported.

Send