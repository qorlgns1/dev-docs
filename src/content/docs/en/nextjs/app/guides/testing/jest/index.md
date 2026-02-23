---
title: 'Testing: Jest'
description: 'Jest and React Testing Library are frequently used together for Unit Testing and Snapshot Testing. This guide will show you how to set up Jest with Ne...'
---

# Testing: Jest | Next.js

Source URL: https://nextjs.org/docs/app/guides/testing/jest

[Guides](https://nextjs.org/docs/app/guides)[Testing](https://nextjs.org/docs/app/guides/testing)Jest

Copy page

# How to set up Jest with Next.js

Last updated February 20, 2026

Jest and React Testing Library are frequently used together for **Unit Testing** and **Snapshot Testing**. This guide will show you how to set up Jest with Next.js and write your first tests.

> **Good to know:** Since `async` Server Components are new to the React ecosystem, Jest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using an **E2E tests** for `async` components.

## Quickstart[](https://nextjs.org/docs/app/guides/testing/jest#quickstart)

You can use `create-next-app` with the Next.js [with-jest](https://github.com/vercel/next.js/tree/canary/examples/with-jest) example to quickly get started:

pnpmnpmyarnbun

Terminal
[code]
    pnpm create next-app --example with-jest with-jest-app
[/code]

## Manual setup[](https://nextjs.org/docs/app/guides/testing/jest#manual-setup)

Since the release of [Next.js 12](https://nextjs.org/blog/next-12), Next.js now has built-in configuration for Jest.

To set up Jest, install `jest` and the following packages as dev dependencies:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
[/code]

Generate a basic Jest configuration file by running the following command:

pnpmnpmyarnbun

Terminal
[code]
    pnpm create jest@latest
[/code]

This will take you through a series of prompts to setup Jest for your project, including automatically creating a `jest.config.ts|js` file.

Update your config file to use `next/jest`. This transformer has all the necessary configuration options for Jest to work with Next.js:

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

Under the hood, `next/jest` is automatically configuring Jest for you, including:

  * Setting up `transform` using the [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler).
  * Auto mocking stylesheets (`.css`, `.module.css`, and their scss variants), image imports and [`next/font`](https://nextjs.org/docs/app/api-reference/components/font).
  * Loading `.env` (and all variants) into `process.env`.
  * Ignoring `node_modules` from test resolving and transforms.
  * Ignoring `.next` from test resolving.
  * Loading `next.config.js` for flags that enable SWC transforms.



> **Good to know** : To test environment variables directly, load them manually in a separate setup script or in your `jest.config.ts` file. For more information, please see [Test Environment Variables](https://nextjs.org/docs/app/guides/environment-variables#test-environment-variables).

## Optional: Handling Absolute Imports and Module Path Aliases[](https://nextjs.org/docs/app/guides/testing/jest#optional-handling-absolute-imports-and-module-path-aliases)

If your project is using [Module Path Aliases](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases), you will need to configure Jest to resolve the imports by matching the paths option in the `jsconfig.json` file with the `moduleNameMapper` option in the `jest.config.js` file. For example:

tsconfig.json or jsconfig.json
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

## Optional: Extend Jest with custom matchers[](https://nextjs.org/docs/app/guides/testing/jest#optional-extend-jest-with-custom-matchers)

`@testing-library/jest-dom` includes a set of convenient [custom matchers](https://github.com/testing-library/jest-dom#custom-matchers) such as `.toBeInTheDocument()` making it easier to write tests. You can import the custom matchers for every test by adding the following option to the Jest configuration file:

jest.config.ts

JavaScriptTypeScript
[code]
    setupFilesAfterEnv: ['<rootDir>/jest.setup.ts']
[/code]

Then, inside `jest.setup`, add the following import:

jest.setup.ts

JavaScriptTypeScript
[code]
    import '@testing-library/jest-dom'
[/code]

> **Good to know:** [`extend-expect` was removed in `v6.0`](https://github.com/testing-library/jest-dom/releases/tag/v6.0.0), so if you are using `@testing-library/jest-dom` before version 6, you will need to import `@testing-library/jest-dom/extend-expect` instead.

If you need to add more setup options before each test, you can add them to the `jest.setup` file above.

## Add a test script to `package.json`[](https://nextjs.org/docs/app/guides/testing/jest#add-a-test-script-to-packagejson)

Finally, add a Jest `test` script to your `package.json` file:

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

`jest --watch` will re-run tests when a file is changed. For more Jest CLI options, please refer to the [Jest Docs](https://jestjs.io/docs/cli#reference).

### Creating your first test[](https://nextjs.org/docs/app/guides/testing/jest#creating-your-first-test)

Your project is now ready to run tests. Create a folder called `__tests__` in your project's root directory.

For example, we can add a test to check if the `<Page />` component successfully renders a heading:

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

Optionally, add a [snapshot test](https://jestjs.io/docs/snapshot-testing) to keep track of any unexpected changes in your component:

__tests__/snapshot.js
[code]
    import { render } from '@testing-library/react'
    import Page from '../app/page'
     
    it('renders homepage unchanged', () => {
      const { container } = render(<Page />)
      expect(container).toMatchSnapshot()
    })
[/code]

## Running your tests[](https://nextjs.org/docs/app/guides/testing/jest#running-your-tests)

Then, run the following command to run your tests:

pnpmnpmyarnbun

Terminal
[code]
    pnpm test
[/code]

## Additional Resources[](https://nextjs.org/docs/app/guides/testing/jest#additional-resources)

For further reading, you may find these resources helpful:

  * [Next.js with Jest example](https://github.com/vercel/next.js/tree/canary/examples/with-jest)
  * [Jest Docs](https://jestjs.io/docs/getting-started)
  * [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)
  * [Testing Playground](https://testing-playground.com/) \- use good testing practices to match elements.



Was this helpful?

supported.

Send
