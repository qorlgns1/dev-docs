---
title: '테스트: Cypress'
description: '>   * Cypress 13.6.3 미만 버전은  설정에서 TypeScript 5를 지원하지 않습니다. 이 문제는 Cypress 13.6.3 이후 버전에서 해결되었습니다. cypress v13.6.3'
---

# 테스트: Cypress | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/testing/cypress

[Guides](https://nextjs.org/docs/pages/guides)[Testing](https://nextjs.org/docs/pages/guides/testing)Cypress

Copy page

# Next.js와 함께 Cypress 설정하기

마지막 업데이트 2026년 2월 20일

[Cypress](https://www.cypress.io/)는 **엔드투엔드(E2E)** 및 **컴포넌트 테스트**에 사용되는 테스트 러너입니다. 이 문서는 Next.js와 함께 Cypress를 설정하고 첫 번째 테스트를 작성하는 방법을 안내합니다.

> **경고:**
> 
>   * Cypress 13.6.3 미만 버전은 `moduleResolution:"bundler"` 설정에서 [TypeScript 5](https://github.com/cypress-io/cypress/issues/27731)를 지원하지 않습니다. 이 문제는 Cypress 13.6.3 이후 버전에서 해결되었습니다. [cypress v13.6.3](https://docs.cypress.io/guides/references/changelog#13-6-3)
> 


## 수동 설정[](https://nextjs.org/docs/pages/guides/testing/cypress#manual-setup)

수동으로 Cypress를 설정하려면 `cypress`를 dev 의존성으로 설치하세요:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add -D cypress
[/code]

`package.json`의 scripts 필드에 Cypress `open` 명령을 추가합니다:

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "eslint",
        "cypress:open": "cypress open"
      }
    }
[/code]

처음으로 Cypress를 실행하여 Cypress 테스트 스위트를 엽니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm cypress:open
[/code]

**E2E Testing**과/또는 **Component Testing**을 구성할 수 있습니다. 이 옵션 중 하나를 선택하면 프로젝트에 `cypress.config.js` 파일과 `cypress` 폴더가 자동으로 생성됩니다.

## 첫 번째 Cypress E2E 테스트 만들기[](https://nextjs.org/docs/pages/guides/testing/cypress#creating-your-first-cypress-e2e-test)

`cypress.config` 파일에 다음 구성이 포함되어 있는지 확인하세요:

cypress.config.ts

JavaScriptTypeScript
[code]
    import { defineConfig } from 'cypress'
     
    export default defineConfig({
      e2e: {
        setupNodeEvents(on, config) {},
      },
    })
[/code]

그런 다음 Next.js 파일 두 개를 새로 만드세요:

pages/index.js
[code]
    import Link from 'next/link'
     
    export default function Home() {
      return (
        <div>
          <h1>Home</h1>
          <Link href="/about">About</Link>
        </div>
      )
    }
[/code]

pages/about.js
[code]
    import Link from 'next/link'
     
    export default function About() {
      return (
        <div>
          <h1>About</h1>
          <Link href="/">Home</Link>
        </div>
      )
    }
[/code]

내비게이션이 올바르게 작동하는지 확인하는 테스트를 추가하세요:

cypress/e2e/app.cy.js
[code]
    describe('Navigation', () => {
      it('should navigate to the about page', () => {
        // Start from the index page
        cy.visit('http://localhost:3000/')
     
        // Find a link with an href attribute containing "about" and click it
        cy.get('a[href*="about"]').click()
     
        // The new url should include "/about"
        cy.url().should('include', '/about')
     
        // The new page should contain an h1 with "About"
        cy.get('h1').contains('About')
      })
    })
[/code]

### E2E 테스트 실행[](https://nextjs.org/docs/pages/guides/testing/cypress#running-e2e-tests)

Cypress는 사용자가 애플리케이션을 탐색하는 과정을 시뮬레이션하므로 Next.js 서버가 실행 중이어야 합니다. 애플리케이션이 실제로 동작하는 방식에 더 가깝게 테스트하려면 프로덕션 코드를 대상으로 테스트를 실행하는 것이 좋습니다.

Next.js 애플리케이션을 빌드하려면 `npm run build && npm run start`를 실행한 뒤, 다른 터미널 창에서 `npm run cypress:open`을 실행하여 Cypress를 시작하고 E2E 테스트 스위트를 구동하세요.

> **알아두면 좋은 점:**
> 
>   * `cypress.config.js` 구성 파일에 `baseUrl: 'http://localhost:3000'`을 추가하면 `cy.visit("http://localhost:3000/")` 대신 `cy.visit("/")`를 사용할 수 있습니다.
>   * 혹은 [`start-server-and-test`](https://www.npmjs.com/package/start-server-and-test) 패키지를 설치해 Cypress와 함께 Next.js 프로덕션 서버를 실행할 수 있습니다. 설치 후 `package.json`의 scripts 필드에 `"test": "start-server-and-test start http://localhost:3000 cypress"`를 추가하세요. 새 변경 사항이 있을 때마다 애플리케이션을 다시 빌드하는 것도 잊지 마세요.
> 


## 첫 번째 Cypress 컴포넌트 테스트 만들기[](https://nextjs.org/docs/pages/guides/testing/cypress#creating-your-first-cypress-component-test)

컴포넌트 테스트는 전체 애플리케이션을 번들하거나 서버를 시작하지 않고 특정 컴포넌트를 빌드하고 마운트합니다.

Cypress 앱에서 **Component Testing**을 선택한 다음 프런트엔드 프레임워크로 **Next.js**를 선택하세요. 그러면 프로젝트에 `cypress/component` 폴더가 생성되고, 컴포넌트 테스트를 활성화하도록 `cypress.config.js` 파일이 업데이트됩니다.

`cypress.config` 파일에 다음 구성이 포함되어 있는지 확인하세요:

cypress.config.ts

JavaScriptTypeScript
[code]
    import { defineConfig } from 'cypress'
     
    export default defineConfig({
      component: {
        devServer: {
          framework: 'next',
          bundler: 'webpack',
        },
      },
    })
[/code]

앞선 섹션에서 사용한 컴포넌트를 그대로 사용한다고 가정하고, 컴포넌트가 기대한 출력을 렌더링하는지 확인하는 테스트를 추가하세요:

cypress/component/about.cy.js
[code]
    import AboutPage from '../../pages/about'
     
    describe('<AboutPage />', () => {
      it('should render and display expected content', () => {
        // Mount the React component for the About page
        cy.mount(<AboutPage />)
     
        // The new page should contain an h1 with "About page"
        cy.get('h1').contains('About')
     
        // Validate that a link with the expected URL is present
        // *Following* the link is better suited to an E2E test
        cy.get('a[href="/"]').should('be.visible')
      })
    })
[/code]

> **알아두면 좋은 점** :
> 
>   * Cypress는 현재 `async` 서버 컴포넌트에 대한 컴포넌트 테스트를 지원하지 않습니다. E2E 테스트 사용을 권장합니다.
>   * 컴포넌트 테스트는 Next.js 서버를 필요로 하지 않기 때문에 `<Image />`처럼 서버에 의존하는 기능은 기본 설정으로 동작하지 않을 수 있습니다.
> 


### 컴포넌트 테스트 실행[](https://nextjs.org/docs/pages/guides/testing/cypress#running-component-tests)

터미널에서 `npm run cypress:open`을 실행해 Cypress를 시작하고 컴포넌트 테스트 스위트를 구동하세요.

## 지속적 통합(CI)[](https://nextjs.org/docs/pages/guides/testing/cypress#continuous-integration-ci)

대화형 테스트 외에도 `cypress run` 명령을 사용해 Cypress를 헤드리스 모드로 실행할 수 있으며, 이는 CI 환경에 더 적합합니다:

package.json
[code]
    {
      "scripts": {
        //...
        "e2e": "start-server-and-test dev http://localhost:3000 \"cypress open --e2e\"",
        "e2e:headless": "start-server-and-test dev http://localhost:3000 \"cypress run --e2e\"",
        "component": "cypress open --component",
        "component:headless": "cypress run --component"
      }
    }
[/code]

Cypress와 지속적 통합에 대해 더 알아보려면 다음 자료를 참고하세요:

  * [Next.js with Cypress example](https://github.com/vercel/next.js/tree/canary/examples/with-cypress)
  * [Cypress Continuous Integration Docs](https://docs.cypress.io/guides/continuous-integration/introduction)
  * [Cypress GitHub Actions Guide](https://on.cypress.io/github-actions)
  * [Official Cypress GitHub Action](https://github.com/cypress-io/github-action)
  * [Cypress Discord](https://discord.com/invite/cypress)



도움이 되었나요?

지원됨.

Send
