---
title: '테스트: Vitest'
description: 'Vitest와 React Testing Library는 단위 테스트에 자주 함께 사용됩니다. 이 가이드는 Next.js에서 Vitest를 설정하고 첫 번째 테스트를 작성하는 방법을 보여줍니다.'
---

# 테스트: Vitest | Next.js

Source URL: https://nextjs.org/docs/pages/guides/testing/vitest

Copy page

# Next.js에서 Vitest 설정 방법

Last updated February 20, 2026

Vitest와 React Testing Library는 **단위 테스트**에 자주 함께 사용됩니다. 이 가이드는 Next.js에서 Vitest를 설정하고 첫 번째 테스트를 작성하는 방법을 보여줍니다.

> **알아두면 좋아요:** `async` Server Components는 React 생태계에서 새로워 Vitest가 아직 지원하지 않습니다. 동기 Server 및 Client Components에 대해서는 여전히 **단위 테스트**를 실행할 수 있지만, `async` 컴포넌트에는 **E2E 테스트**를 권장합니다.

## Quickstart[](https://nextjs.org/docs/pages/guides/testing/vitest#quickstart)

Next.js [with-vitest](https://github.com/vercel/next.js/tree/canary/examples/with-vitest) 예제를 사용한 `create-next-app`으로 빠르게 시작할 수 있습니다:

pnpmnpmyarnbun

Terminal
```
    pnpm create next-app --example with-vitest with-vitest-app
```

## Manual Setup[](https://nextjs.org/docs/pages/guides/testing/vitest#manual-setup)

수동으로 Vitest를 설정하려면 `vitest`와 다음 패키지를 devDependencies로 설치하세요:

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

그다음 `package.json`에 `test` 스크립트를 추가합니다:

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

`npm run test`를 실행하면 Vitest는 기본적으로 프로젝트 변경 사항을 **감시**합니다.

## Creating your first Vitest Unit Test[](https://nextjs.org/docs/pages/guides/testing/vitest#creating-your-first-vitest-unit-test)

`<Page />` 컴포넌트가 제목을 정상 렌더링하는지 확인하는 테스트를 만들어 모든 것이 잘 동작하는지 점검하세요:

pages/index.tsx

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

__tests__/index.test.tsx

JavaScriptTypeScript
```
    import { expect, test } from 'vitest'
    import { render, screen } from '@testing-library/react'
    import Page from '../pages/index'

    test('Page', () => {
      render(<Page />)
      expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
    })
```

## Running your tests[](https://nextjs.org/docs/pages/guides/testing/vitest#running-your-tests)

테스트를 실행하려면 다음 명령을 실행하세요:

pnpmnpmyarnbun

Terminal
```
    pnpm test
```

## Additional Resources[](https://nextjs.org/docs/pages/guides/testing/vitest#additional-resources)

다음 자료가 도움이 될 수 있습니다:

  * [Next.js with Vitest example](https://github.com/vercel/next.js/tree/canary/examples/with-vitest)
  * [Vitest Docs](https://vitest.dev/guide/)
  * [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)

Was this helpful?

supported.

Send