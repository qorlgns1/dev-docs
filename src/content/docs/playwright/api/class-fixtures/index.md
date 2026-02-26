---
title: "Fixtures"
description: "Playwright Test는 test fixtures 개념을 기반으로 합니다. 테스트 픽스처는 각 테스트를 위한 환경을 설정하는 데 사용되며, 테스트에 필요한 것만 정확히 제공합니다."
---

Source URL: https://playwright.dev/docs/api/class-fixtures

# Fixtures | Playwright

Playwright Test는 [test fixtures](https://playwright.dev/docs/test-fixtures) 개념을 기반으로 합니다. 테스트 픽스처는 각 테스트를 위한 환경을 설정하는 데 사용되며, 테스트에 필요한 것만 정확히 제공합니다.

Playwright Test는 각 테스트 선언을 확인하고, 해당 테스트에 필요한 픽스처 집합을 분석한 뒤 그 테스트에 맞게 픽스처를 준비합니다. 픽스처가 준비한 값은 하나의 객체로 병합되며, 이 객체는 `test`, 훅, 어노테이션 및 기타 픽스처에서 첫 번째 매개변수로 사용할 수 있습니다.

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ page }) => {
      // ...
    });

```

위 테스트를 기준으로 보면, Playwright Test는 테스트 실행 전에 `page` 픽스처를 설정하고 테스트가 끝난 뒤 해제합니다. `page` 픽스처는 테스트에서 사용할 수 있는 [Page](https://playwright.dev/docs/api/class-page "Page") 객체를 제공합니다.

Playwright Test에는 아래에 나열된 내장 픽스처가 포함되어 있으며, 사용자 정의 픽스처를 추가할 수도 있습니다. 또한 Playwright Test는 [fixtures.browser](https://playwright.dev/docs/api/class-fixtures#fixtures-browser), [fixtures.context](https://playwright.dev/docs/api/class-fixtures#fixtures-context), [fixtures.page](https://playwright.dev/docs/api/class-fixtures#fixtures-page)를 구성할 수 있는 [옵션](https://playwright.dev/docs/api/class-testoptions "TestOptions")도 [제공합니다](https://playwright.dev/docs/api/class-testoptions "TestOptions").

---

## 속성[​](https://playwright.dev/docs/api/class-fixtures#properties "Direct link to Properties")

### browser[​](https://playwright.dev/docs/api/class-fixtures#fixtures-browser "Direct link to browser")

추가된 버전: v1.10 fixtures.browser

[Browser](https://playwright.dev/docs/api/class-browser "Browser") 인스턴스는 [동일한 worker](https://playwright.dev/docs/test-parallel)의 모든 테스트 간에 공유되므로 테스트를 효율적으로 수행할 수 있습니다. 하지만 각 테스트는 격리된 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")에서 실행되며 새 환경을 제공받습니다.

[브라우저 구성 방법](https://playwright.dev/docs/test-configuration)과 [사용 가능한 옵션](https://playwright.dev/docs/api/class-testoptions "TestOptions")을 확인하세요.

**사용법**

```
    test.beforeAll(async ({ browser }) => {
      const page = await browser.newPage();
      // ...
    });

```

**타입**

- [Browser](https://playwright.dev/docs/api/class-browser "Browser")

---

### browserName[​](https://playwright.dev/docs/api/class-fixtures#fixtures-browser-name "Direct link to browserName")

추가된 버전: v1.10 fixtures.browserName

테스트를 실행하는 브라우저의 이름입니다. 기본값은 `'chromium'`입니다. 브라우저에 따라 테스트를 [어노테이트](https://playwright.dev/docs/test-annotations)할 때 유용합니다.

**사용법**

```
    test('skip this test in Firefox', async ({ page, browserName }) => {
      test.skip(browserName === 'firefox', 'Still working on it');
      // ...
    });

```

**타입**

- "chromium" | "firefox" | "webkit"

---

### context[​](https://playwright.dev/docs/api/class-fixtures#fixtures-context "Direct link to context")

추가된 버전: v1.10 fixtures.context

각 테스트마다 생성되는 격리된 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext") 인스턴스입니다. 컨텍스트는 서로 격리되어 있으므로, 최대 효율을 위해 여러 테스트가 하나의 [Browser](https://playwright.dev/docs/api/class-browser "Browser")에서 실행되더라도 모든 테스트는 새 환경을 받습니다.

[컨텍스트 구성 방법](https://playwright.dev/docs/test-configuration)과 [사용 가능한 옵션](https://playwright.dev/docs/api/class-testoptions "TestOptions")을 확인하세요.

기본 [fixtures.page](https://playwright.dev/docs/api/class-fixtures#fixtures-page)는 이 컨텍스트에 속합니다.

**사용법**

```
    test('example test', async ({ page, context }) => {
      await context.route('*external.com/*', route => route.abort());
      // ...
    });

```

**타입**

- [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")

---

### page[​](https://playwright.dev/docs/api/class-fixtures#fixtures-page "Direct link to page")

추가된 버전: v1.10 fixtures.page

각 테스트마다 생성되는 격리된 [Page](https://playwright.dev/docs/api/class-page "Page") 인스턴스입니다. 페이지는 [fixtures.context](https://playwright.dev/docs/api/class-fixtures#fixtures-context) 격리 덕분에 테스트 간에 분리됩니다.

테스트에서 가장 일반적으로 사용되는 픽스처입니다.

**사용법**

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ page }) => {
      await page.goto('/signin');
      await page.getByLabel('User Name').fill('user');
      await page.getByLabel('Password').fill('password');
      await page.getByText('Sign in').click();
      // ...
    });

```

**타입**

- [Page](https://playwright.dev/docs/api/class-page "Page")

---

### request[​](https://playwright.dev/docs/api/class-fixtures#fixtures-request "Direct link to request")

추가된 버전: v1.10 fixtures.request

각 테스트를 위한 격리된 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext") 인스턴스입니다.

**사용법**

```
    import { test, expect } from '@playwright/test';

    test('basic test', async ({ request }) => {
      await request.post('/signin', {
        data: {
          username: 'user',
          password: 'password'
        }
      });
      // ...
    });

```

**타입**

- [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")
