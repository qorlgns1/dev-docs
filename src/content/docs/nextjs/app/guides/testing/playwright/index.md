---
title: '테스트: Playwright'
description: 'Playwright는 하나의 API로 Chromium, Firefox, WebKit을 자동화할 수 있는 테스트 프레임워크입니다. 이를 사용해 엔드 투 엔드(E2E) 테스트를 작성할 수 있습니다. 이 가이드는 Playwright를 Next.js와 함께 설정하고 첫 번째 ...'
---

# 테스트: Playwright | Next.js

출처 URL: https://nextjs.org/docs/app/guides/testing/playwright

# Playwright를 Next.js에 설정하는 방법

마지막 업데이트 2026년 2월 20일

Playwright는 하나의 API로 Chromium, Firefox, WebKit을 자동화할 수 있는 테스트 프레임워크입니다. 이를 사용해 **엔드 투 엔드(E2E)** 테스트를 작성할 수 있습니다. 이 가이드는 Playwright를 Next.js와 함께 설정하고 첫 번째 테스트를 작성하는 방법을 보여줍니다.

## 빠른 시작[](https://nextjs.org/docs/app/guides/testing/playwright#quickstart)

가장 빠른 시작 방법은 [with-playwright 예제](https://github.com/vercel/next.js/tree/canary/examples/with-playwright)가 포함된 `create-next-app`을 사용하는 것입니다. 이렇게 하면 Playwright가 구성된 Next.js 프로젝트가 생성됩니다.

pnpmnpmyarnbun

터미널
```
    pnpm create next-app --example with-playwright with-playwright-app
```

## 수동 설정[](https://nextjs.org/docs/app/guides/testing/playwright#manual-setup)

Playwright를 설치하려면 다음 명령을 실행하세요:

pnpmnpmyarnbun

터미널
```
    pnpm create playwright
```

이 명령은 `playwright.config.ts` 파일 추가를 포함해 Playwright를 프로젝트에 설정하고 구성하는 일련의 프롬프트를 안내합니다. 단계별 안내는 [Playwright 설치 가이드](https://playwright.dev/docs/intro#installation)를 참고하세요.

## 첫 번째 Playwright E2E 테스트 만들기[](https://nextjs.org/docs/app/guides/testing/playwright#creating-your-first-playwright-e2e-test)

새로운 Next.js 페이지 두 개를 만듭니다:

app/page.tsx
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

app/about/page.tsx
```
    import Link from 'next/link'

    export default function Page() {
      return (
        <div>
          <h1>About</h1>
          <Link href="/">Home</Link>
        </div>
      )
    }
```

그런 다음 내비게이션이 제대로 작동하는지 확인하는 테스트를 추가합니다:

tests/example.spec.ts
```
    import { test, expect } from '@playwright/test'

    test('should navigate to the about page', async ({ page }) => {
      // Start from the index page (the baseURL is set via the webServer in the playwright.config.ts)
      await page.goto('http://localhost:3000/')
      // Find an element with the text 'About' and click on it
      await page.click('text=About')
      // The new URL should be "/about" (baseURL is used there)
      await expect(page).toHaveURL('http://localhost:3000/about')
      // The new page should contain an h1 with "About"
      await expect(page.locator('h1')).toContainText('About')
    })
```

> **알아두면 좋아요**: [`"baseURL": "http://localhost:3000"`](https://playwright.dev/docs/api/class-testoptions#test-options-base-url)을 `playwright.config.ts` [구성 파일](https://playwright.dev/docs/test-configuration)에 추가하면 `page.goto("http://localhost:3000/")` 대신 `page.goto("/")`를 사용할 수 있습니다.

### Playwright 테스트 실행하기[](https://nextjs.org/docs/app/guides/testing/playwright#running-your-playwright-tests)

Playwright는 Chromium, Firefox, Webkit 세 브라우저에서 사용자가 애플리케이션을 탐색하는 과정을 시뮬레이션하므로 Next.js 서버가 실행 중이어야 합니다. 애플리케이션의 실제 동작과 더 가깝게 만들기 위해 프로덕션 코드에 대해 테스트를 실행하는 것을 권장합니다.

`npm run build`와 `npm run start`를 실행한 뒤, 다른 터미널 창에서 `npx playwright test`를 실행해 Playwright 테스트를 구동하세요.

> **알아두면 좋아요**: Playwright가 개발 서버를 시작하고 완전히 준비될 때까지 기다리도록 [`webServer`](https://playwright.dev/docs/test-webserver/) 기능을 사용할 수도 있습니다.

### 지속적 통합(CI)에서 Playwright 실행하기[](https://nextjs.org/docs/app/guides/testing/playwright#running-playwright-on-continuous-integration-ci)

Playwright는 기본적으로 [헤드리스 모드](https://playwright.dev/docs/ci#running-headed)에서 테스트를 실행합니다. 모든 Playwright 의존성을 설치하려면 `npx playwright install-deps`를 실행하세요.

Playwright와 지속적 통합에 대해 더 자세히 알아보려면 다음 자료를 참고하세요:

  * [Playwright가 포함된 Next.js 예제](https://github.com/vercel/next.js/tree/canary/examples/with-playwright)
  * [CI 공급자에서 Playwright 사용](https://playwright.dev/docs/ci)
  * [Playwright Discord](https://discord.com/invite/playwright-807756831384403968)