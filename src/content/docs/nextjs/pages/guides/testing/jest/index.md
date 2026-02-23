---
title: '테스트: Jest'
description: '마지막 업데이트: 2026년 2월 20일'
---

# 테스트: Jest | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/testing/jest

[가이드](https://nextjs.org/docs/pages/guides)[테스트](https://nextjs.org/docs/pages/guides/testing)Jest

페이지 복사

# Next.js에서 Jest 설정 방법

마지막 업데이트: 2026년 2월 20일

Jest와 React Testing Library는 **단위 테스트** 및 **스냅샷 테스트**에 자주 함께 사용됩니다. 이 가이드는 Next.js와 Jest를 설정하고 첫 번째 테스트를 작성하는 방법을 보여줍니다.

> **알아두면 좋아요:** `async` 서버 컴포넌트는 React 생태계에서 새로워서, 현재 Jest는 이를 지원하지 않습니다. 동기 서버 및 클라이언트 컴포넌트에 대해서는 **단위 테스트**를 계속 실행할 수 있지만, `async` 컴포넌트에는 **E2E 테스트**를 권장합니다.

## Quickstart[](https://nextjs.org/docs/pages/guides/testing/jest#quickstart)

`create-next-app`과 Next.js [with-jest](https://github.com/vercel/next.js/tree/canary/examples/with-jest) 예제를 사용하면 빠르게 시작할 수 있습니다:

pnpmnpmyarnbun

터미널
[code]
    pnpm create next-app --example with-jest with-jest-app
[/code]

## Manual setup[](https://nextjs.org/docs/pages/guides/testing/jest#manual-setup)

[Next.js 12](https://nextjs.org/blog/next-12) 릴리스 이후 Next.js는 Jest를 위한 기본 구성을 제공합니다.

Jest를 설정하려면 `jest`와 다음 패키지를 devDependencies로 설치하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm add -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
[/code]

다음 명령으로 기본 Jest 구성 파일을 생성하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm create jest@latest
[/code]

이 작업은 Jest 설정을 위한 일련의 프롬프트를 안내하며, `jest.config.ts|js` 파일도 자동으로 생성합니다.

구성 파일을 `next/jest`를 사용하도록 업데이트하세요. 이 트랜스포머에는 Jest가 Next.js와 함께 작동하는 데 필요한 모든 구성 옵션이 포함되어 있습니다:

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

내부적으로 `next/jest`는 다음을 포함해 Jest 구성을 자동으로 처리합니다:

  * [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)를 사용하는 `transform` 설정
  * 스타일시트(`.css`, `.module.css`, 및 scss 변형), 이미지 import, [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) 자동 모킹
  * `.env`(모든 변형 포함)을 `process.env`에 로드
  * 테스트 해석 및 트랜스폼에서 `node_modules` 무시
  * 테스트 해석에서 `.next` 무시
  * SWC 트랜스폼을 활성화하는 플래그를 위해 `next.config.js` 로딩



> **알아두면 좋아요**: 환경 변수를 직접 테스트하려면 별도의 설정 스크립트나 `jest.config.ts` 파일에서 수동으로 로드하세요. 자세한 내용은 [Test Environment Variables](https://nextjs.org/docs/app/guides/environment-variables#test-environment-variables)를 참고하세요.

## Setting up Jest (with Babel)[](https://nextjs.org/docs/pages/guides/testing/jest#setting-up-jest-with-babel)

[Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)를 사용하지 않고 Babel을 선택하면, 위 패키지 외에 `babel-jest`와 `identity-obj-proxy`를 설치하고 Jest를 수동으로 구성해야 합니다.

Next.js용 Jest 구성에 권장되는 옵션은 다음과 같습니다:

jest.config.js
[code]
    module.exports = {
      collectCoverage: true,
      // on node 14.x coverage provider v8 offers good speed and more or less good report
      coverageProvider: 'v8',
      collectCoverageFrom: [
        '**/*.{js,jsx,ts,tsx}',
        '!**/*.d.ts',
        '!**/node_modules/**',
        '!<rootDir>/out/**',
        '!<rootDir>/.next/**',
        '!<rootDir>/*.config.js',
        '!<rootDir>/coverage/**',
      ],
      moduleNameMapper: {
        // Handle CSS imports (with CSS modules)
        // https://jestjs.io/docs/webpack#mocking-css-modules
        '^.+\\.module\\.(css|sass|scss)$': 'identity-obj-proxy',
     
        // Handle CSS imports (without CSS modules)
        '^.+\\.(css|sass|scss)$': '<rootDir>/__mocks__/styleMock.js',
     
        // Handle image imports
        // https://jestjs.io/docs/webpack#handling-static-assets
        '^.+\\.(png|jpg|jpeg|gif|webp|avif|ico|bmp|svg)$': `<rootDir>/__mocks__/fileMock.js`,
     
        // Handle module aliases
        '^@/components/(.*)$': '<rootDir>/components/$1',
     
        // Handle @next/font
        '@next/font/(.*)': `<rootDir>/__mocks__/nextFontMock.js`,
        // Handle next/font
        'next/font/(.*)': `<rootDir>/__mocks__/nextFontMock.js`,
        // Disable server-only
        'server-only': `<rootDir>/__mocks__/empty.js`,
      },
      // Add more setup options before each test is run
      // setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
      testPathIgnorePatterns: ['<rootDir>/node_modules/', '<rootDir>/.next/'],
      testEnvironment: 'jsdom',
      transform: {
        // Use babel-jest to transpile tests with the next/babel preset
        // https://jestjs.io/docs/configuration#transform-objectstring-pathtotransformer--pathtotransformer-object
        '^.+\\.(js|jsx|ts|tsx)$': ['babel-jest', { presets: ['next/babel'] }],
      },
      transformIgnorePatterns: [
        '/node_modules/',
        '^.+\\.module\\.(css|sass|scss)$',
      ],
    }
[/code]

각 구성 옵션에 대한 자세한 내용은 [Jest 문서](https://jestjs.io/docs/configuration)를 참고하세요. 또한 Next.js가 Jest를 어떻게 구성하는지 확인하려면 [`next/jest` 구성](https://github.com/vercel/next.js/blob/e02fe314dcd0ae614c65b505c6daafbdeebb920e/packages/next/src/build/jest/jest.ts)을 검토하는 것이 좋습니다.

### 스타일시트 및 이미지 import 처리[](https://nextjs.org/docs/pages/guides/testing/jest#handling-stylesheets-and-image-imports)

스타일시트와 이미지는 테스트에서 사용되지 않지만 import하면 오류를 유발할 수 있으므로 모킹해야 합니다.

위 구성에서 참조한 `fileMock.js`와 `styleMock.js` 모크 파일을 `__mocks__` 디렉터리 안에 만드세요:

__mocks__/fileMock.js
[code]
    module.exports = 'test-file-stub'
[/code]

__mocks__/styleMock.js
[code]
    module.exports = {}
[/code]

정적 에셋 처리에 대한 자세한 내용은 [Jest 문서](https://jestjs.io/docs/webpack#handling-static-assets)를 참고하세요.

## 폰트 처리[](https://nextjs.org/docs/pages/guides/testing/jest#handling-fonts)

폰트를 처리하려면 `__mocks__` 디렉터리에 `nextFontMock.js` 파일을 만들고 다음 구성을 추가하세요:

__mocks__/nextFontMock.js
[code]
    module.exports = new Proxy(
      {},
      {
        get: function getter() {
          return () => ({
            className: 'className',
            variable: 'variable',
            style: { fontFamily: 'fontFamily' },
          })
        },
      }
    )
[/code]

## 선택 사항: 절대 import 및 모듈 경로 별칭 처리[](https://nextjs.org/docs/pages/guides/testing/jest#optional-handling-absolute-imports-and-module-path-aliases)

프로젝트에서 [모듈 경로 별칭](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases)을 사용한다면, `jsconfig.json`의 paths 옵션과 `jest.config.js`의 `moduleNameMapper` 옵션을 일치시켜 Jest가 import를 해석하도록 구성해야 합니다. 예:

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

## 선택 사항: Jest를 사용자 정의 matcher로 확장[](https://nextjs.org/docs/pages/guides/testing/jest#optional-extend-jest-with-custom-matchers)

`@testing-library/jest-dom`에는 `.toBeInTheDocument()`와 같은 편리한 [사용자 정의 matcher](https://github.com/testing-library/jest-dom#custom-matchers)가 포함되어 있어 테스트 작성이 쉬워집니다. 다음 옵션을 Jest 구성 파일에 추가하여 모든 테스트에서 사용자 정의 matcher를 가져올 수 있습니다:

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

> **알아두면 좋아요:** [`extend-expect`는 `v6.0`에서 제거되었습니다](https://github.com/testing-library/jest-dom/releases/tag/v6.0.0). 따라서 `@testing-library/jest-dom` 6 이전 버전을 사용하는 경우 `@testing-library/jest-dom/extend-expect`를 대신 import해야 합니다.

각 테스트 전에 추가 설정 옵션이 필요하면 위의 `jest.setup` 파일에 추가할 수 있습니다.

## `package.json`에 테스트 스크립트 추가[](https://nextjs.org/docs/pages/guides/testing/jest#add-a-test-script-to-packagejson)

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

`jest --watch`는 파일이 변경될 때 테스트를 다시 실행합니다. 더 많은 Jest CLI 옵션은 [Jest 문서](https://jestjs.io/docs/cli#reference)를 참고하세요.

### 첫 번째 테스트 만들기[](https://nextjs.org/docs/pages/guides/testing/jest#creating-your-first-test)

이제 프로젝트에서 테스트를 실행할 준비가 되었습니다. 프로젝트 루트 디렉터리에 `__tests__` 폴더를 만드세요.

예를 들어 `<Home />` 컴포넌트가 헤딩을 성공적으로 렌더링하는지 확인하는 테스트를 추가할 수 있습니다:
[code]
    export default function Home() {
      return <h1>Home</h1>
    }
[/code]

__tests__/index.test.js
[code]
    import '@testing-library/jest-dom'
    import { render, screen } from '@testing-library/react'
    import Home from '../pages/index'
     
    describe('Home', () => {
      it('renders a heading', () => {
        render(<Home />)
     
        const heading = screen.getByRole('heading', { level: 1 })
     
        expect(heading).toBeInTheDocument()
      })
    })
[/code]

선택적으로, 컴포넌트의 예기치 않은 변화를 추적하기 위해 [스냅샷 테스트](https://jestjs.io/docs/snapshot-testing)를 추가하세요:

__tests__/snapshot.js
[code]
    import { render } from '@testing-library/react'
    import Home from '../pages/index'
     
    it('renders homepage unchanged', () => {
      const { container } = render(<Home />)
      expect(container).toMatchSnapshot()
    })
[/code]

> **알아두면 좋아요**: 페이지 라우터 내부의 파일은 모두 라우트로 간주되므로, 테스트 파일을 페이지 라우터 안에 포함하지 마세요.

## 테스트 실행[](https://nextjs.org/docs/pages/guides/testing/jest#running-your-tests)

그런 다음 다음 명령을 실행해 테스트를 실행하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm test
[/code]

## 추가 자료[](https://nextjs.org/docs/pages/guides/testing/jest#additional-resources)

추가로 참고할 만한 자료는 다음과 같습니다:

  * [Next.js with Jest 예제](https://github.com/vercel/next.js/tree/canary/examples/with-jest)
  * [Jest 문서](https://jestjs.io/docs/getting-started)

* [React Testing Library 문서](https://testing-library.com/docs/react-testing-library/intro/)
  * [Testing Playground](https://testing-playground.com/) \- 요소를 찾을 때는 우수한 테스트 작성 관행을 따르세요.

도움이 되었나요?

지원됨.

보내기
