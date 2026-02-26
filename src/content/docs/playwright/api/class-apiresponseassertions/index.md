---
title: "APIResponseAssertions"
description: "import { test, expect } from '@playwright/test';"
---

소스 URL: https://playwright.dev/docs/api/class-apiresponseassertions

# APIResponseAssertions | Playwright

[APIResponseAssertions](https://playwright.dev/docs/api/class-apiresponseassertions "APIResponseAssertions") 클래스는 테스트에서 [APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")에 대한 단언을 수행할 때 사용할 수 있는 단언 메서드를 제공합니다.

```
    import { test, expect } from '@playwright/test';

    test('navigates to login', async ({ page }) => {
      // ...
      const response = await page.request.get('https://playwright.dev');
      await expect(response).toBeOK();
    });

```

---

## 메서드[​](https://playwright.dev/docs/api/class-apiresponseassertions#methods "Direct link to Methods")

### toBeOK[​](https://playwright.dev/docs/api/class-apiresponseassertions#api-response-assertions-to-be-ok "Direct link to toBeOK")

추가됨: v1.18 apiResponseAssertions.toBeOK

응답 상태 코드가 `200..299` 범위 내에 있는지 확인합니다.

**사용법**

```
    await expect(response).toBeOK();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-apiresponseassertions#api-response-assertions-to-be-ok-return)

---

## 속성[​](https://playwright.dev/docs/api/class-apiresponseassertions#properties "Direct link to Properties")

### not[​](https://playwright.dev/docs/api/class-apiresponseassertions#api-response-assertions-not "Direct link to not")

추가됨: v1.20 apiResponseAssertions.not

단언이 반대 조건을 검사하도록 합니다. 예를 들어, 아래 코드는 응답 상태가 성공이 아님을 테스트합니다:

```
    await expect(response).not.toBeOK();

```

**사용법**

```
    expect(response).not

```

**타입**

- [APIResponseAssertions](https://playwright.dev/docs/api/class-apiresponseassertions "APIResponseAssertions")
