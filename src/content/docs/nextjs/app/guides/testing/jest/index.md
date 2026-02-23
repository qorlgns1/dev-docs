---
title: '테스트: Jest'
description: 'Jest와 React Testing Library는 단위 테스트와 스냅샷 테스트에서 자주 함께 사용됩니다. 이 가이드는 Next.js에서 Jest를 설정하고 첫 번째 테스트를 작성하는 방법을 안내합니다.'
---

# 테스트: Jest | Next.js

Source URL: https://nextjs.org/docs/app/guides/testing/jest

[Guides](https://nextjs.org/docs/app/guides)[Testing](https://nextjs.org/docs/app/guides/testing)Jest

Copy page

# Next.js에서 Jest 설정 방법

Last updated February 20, 2026

Jest와 React Testing Library는 **단위 테스트**와 **스냅샷 테스트**에서 자주 함께 사용됩니다. 이 가이드는 Next.js에서 Jest를 설정하고 첫 번째 테스트를 작성하는 방법을 안내합니다.

> **알아두면 좋아요:** `async` Server Components는 React 생태계에서 새로 도입된 기능이라 Jest가 아직 지원하지 않습니다. 동기 Server/Client 컴포넌트에 대해서는 **단위 테스트**를 실행할 수 있지만, `async` 컴포넌트에는 **E2E 테스트**를 사용하는 것이 좋습니다.

## 빠른 시작[](https://nextjs.org/docs/app/guides/testing/jest#quickstart)

Next.js [with-jest](https://github.com/vercel/next.js/tree/canary/examples/with-jest) 예제를 포함한 `create-next-app`을 사용하면 빠르게 시작할 수 있습니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm create next-app --example with-jest with-jest-app
[/code]

## 수동 설정[](https://nextjs.org/docs/app/guides/testing/jest#manual-setup)

[Next.js 12](https://nextjs.org/blog/next-12) 릴리스 이후 Next.js에는 Jest를 위한 기본 구성 요소가 포함되어 있습니다.

Jest를 설정하려면 `jest`와 다음 패키지를 devDependencies로 설치하세요:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
[/code]

다음 명령으로 기본 Jest 구성 파일을 생성합니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm create jest@latest
[/code]

이 명령은 프로젝트에 맞는 Jest 설정 질문을 안내하며 자동으로 `jest.config.ts|js` 파일을 생성합니다.

구성 파일을 `next/jest`를 사용하도록 업데이트하세요. 이 트랜스포머는 Next.js와 함께 Jest가 동작하는 데 필요한 옵션을 모두 포함합니다:

jest.config.ts

JavaScriptTypeScript
[code]
    import type { Config } from 'jest'
    import nextJest from 'next/jest.js'
     
    const createJestConfig = nextJest({
      // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
      dir: './',
    })
     
    // Add any custom config to be passed to Jest
    const config: Config = {
      coverageProvider: 'v8',
      testEnvironment: 'jsdom',
      // Add more setup options before each test is run
      // setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
    }
     
    // createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
    export default createJestConfig(config)
[/code]

`next/jest`는 내부적으로 다음과 같이 Jest 구성을 자동 처리합니다:

  * [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)를 사용해 `transform`을 설정합니다.
  * 스타일시트(`.css`, `.module.css`, scss 변형), 이미지 import, [`next/font`](https://nextjs.org/docs/app/api-reference/components/font)을 자동으로 모킹합니다.
  * `.env`(및 모든 변형)를 `process.env`에 로드합니다.
  * 테스트 해석 및 변환에서 `node_modules`를 무시합니다.
  * 테스트 해석에서 `.next`를 무시합니다.
  * SWC 변환을 활성화하는 플래그를 위해 `next.config.js`를 로드합니다.

> **알아두면 좋아요:** 환경 변수를 직접 테스트하려면 별도 설정 스크립트나 `jest.config.ts` 파일에서 수동으로 로드하세요. 자세한 내용은 [Test Environment Variables](https://nextjs.org/docs/app/guides/environment-variables#test-environment-variables)를 참고하세요.

## 선택 사항: 절대 경로 import와 모듈 경로 별칭 처리[](https://nextjs.org/docs/app/guides/testing/jest#optional-handling-absolute-imports-and-module-path-aliases)

프로젝트에서 [Module Path Aliases](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases)를 사용한다면, `jsconfig.json`의 paths 옵션과 `jest.config.js`의 `moduleNameMapper` 옵션이 일치하도록 설정하여 Jest가 import를 해석하도록 해야 합니다. 예시는 다음과 같습니다:

tsconfig.json 또는 jsconfig.json
[code]
    {
      "compilerOptions": {
        "module": "esnext",
        "moduleResolution": "bundler",
        "baseUrl": "./",
        "paths": {
          "@/components/*": ["components/*"]
        }
      }
    }
[/code]

jest.config.js
[code]
    moduleNameMapper: {
      // ...
      '^@/components/(.*)$': '<rootDir>/components/$1',
    }
[/code]

## 선택 사항: 커스텀 matcher로 Jest 확장하기[](https://nextjs.org/docs/app/guides/testing/jest#optional-extend-jest-with-custom-matchers)

`@testing-library/jest-dom`에는 `.toBeInTheDocument()`와 같이 테스트 작성이 쉬워지는 유용한 [커스텀 matcher](https://github.com/testing-library/jest-dom#custom-matchers)가 포함되어 있습니다. 아래 옵션을 Jest 구성 파일에 추가하면 모든 테스트에서 커스텀 matcher를 import할 수 있습니다:

jest.config.ts

JavaScriptTypeScript
[code]
    setupFilesAfterEnv: ['<rootDir>/jest.setup.ts']
[/code]

그런 다음 `jest.setup` 내부에 다음 import를 추가하세요:

jest.setup.ts

JavaScriptTypeScript
[code]
    import '@testing-library/jest-dom'
[/code]

> **알아두면 좋아요:** [`extend-expect`는 `v6.0`에서 제거](https://github.com/testing-library/jest-dom/releases/tag/v6.0.0)되었으므로, 6 이전 버전의 `@testing-library/jest-dom`을 사용한다면 대신 `@testing-library/jest-dom/extend-expect`를 import해야 합니다.

각 테스트 전에 더 많은 설정 옵션이 필요하다면 위의 `jest.setup` 파일에 추가할 수 있습니다.

## `package.json`에 테스트 스크립트 추가[](https://nextjs.org/docs/app/guides/testing/jest#add-a-test-script-to-packagejson)

마지막으로 `package.json` 파일에 Jest `test` 스크립트를 추가하세요:

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "test": "jest",
        "test:watch": "jest --watch"
      }
    }
[/code]

`jest --watch`는 파일이 변경될 때마다 테스트를 다시 실행합니다. 더 많은 Jest CLI 옵션은 [Jest Docs](https://jestjs.io/docs/cli#reference)를 참고하세요.

### 첫 번째 테스트 만들기[](https://nextjs.org/docs/app/guides/testing/jest#creating-your-first-test)

이제 프로젝트에서 테스트를 실행할 준비가 되었습니다. 프로젝트 루트 디렉터리에 `__tests__` 폴더를 만드세요.

예를 들어 `<Page />` 컴포넌트가 제목을 제대로 렌더링하는지 확인하는 테스트를 추가할 수 있습니다:

app/page.js
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return (
        <div>
          <h1>Home</h1>
          <Link href="/about">About</Link>
        </div>
      )
    }
[/code]

__tests__/page.test.jsx
[code]
    import '@testing-library/jest-dom'
    import { render, screen } from '@testing-library/react'
    import Page from '../app/page'
     
    describe('Page', () => {
      it('renders a heading', () => {
        render(<Page />)
     
        const heading = screen.getByRole('heading', { level: 1 })
     
        expect(heading).toBeInTheDocument()
      })
    })
[/code]

선택적으로 [스냅샷 테스트](https://jestjs.io/docs/snapshot-testing)를 추가하여 컴포넌트에 예기치 않은 변경이 생기는지를 추적할 수 있습니다:

__tests__/snapshot.js
[code]
    import { render } from '@testing-library/react'
    import Page from '../app/page'
     
    it('renders homepage unchanged', () => {
      const { container } = render(<Page />)
      expect(container).toMatchSnapshot()
    })
[/code]

## 테스트 실행[](https://nextjs.org/docs/app/guides/testing/jest#running-your-tests)

테스트를 실행하려면 다음 명령을 실행하세요:

pnpmnpmyarnbun

Terminal
[code]
    pnpm test
[/code]

## 추가 리소스[](https://nextjs.org/docs/app/guides/testing/jest#additional-resources)

더 자세한 내용을 알고 싶다면 아래 자료가 도움이 됩니다:

  * [Next.js with Jest 예제](https://github.com/vercel/next.js/tree/canary/examples/with-jest)
  * [Jest Docs](https://jestjs.io/docs/getting-started)
  * [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)
  * [Testing Playground](https://testing-playground.com/) \- 올바른 테스트 관행으로 요소를 찾는 데 활용하세요.



Was this helpful?

supported.

Send
