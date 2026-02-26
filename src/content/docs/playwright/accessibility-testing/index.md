---
title: "접근성 테스트"
description: "Playwright를 사용하면 애플리케이션에서 다양한 유형의 접근성 문제를 테스트할 수 있습니다."
---

Source URL: https://playwright.dev/docs/accessibility-testing

# 접근성 테스트 | Playwright

## 소개[​](https://playwright.dev/docs/accessibility-testing#introduction "Direct link to Introduction")

Playwright를 사용하면 애플리케이션에서 다양한 유형의 접근성 문제를 테스트할 수 있습니다.

이로써 발견할 수 있는 문제의 예시는 다음과 같습니다.

- 배경과의 색상 대비가 낮아 시각 장애가 있는 사용자가 읽기 어려운 텍스트
- 스크린 리더가 식별할 수 있는 레이블이 없는 UI 컨트롤 및 폼 요소
- 보조 기술을 혼란스럽게 만들 수 있는, 중복된 ID를 가진 인터랙티브 요소

아래 예제는 [`@axe-core/playwright`](https://npmjs.org/@axe-core/playwright) 패키지에 의존하며, 이 패키지는 Playwright 테스트의 일부로 [axe accessibility testing engine](https://www.deque.com/axe/)을 실행할 수 있도록 지원합니다.

면책 고지

자동화된 접근성 테스트는 누락되었거나 유효하지 않은 속성 같은 일반적인 접근성 문제 일부를 탐지할 수 있습니다. 하지만 많은 접근성 문제는 수동 테스트를 통해서만 발견할 수 있습니다. 자동화 테스트, 수동 접근성 평가, 포괄적 사용자 테스트를 함께 사용하는 것을 권장합니다.

수동 평가에는 무료 오픈소스 개발 도구인 [Accessibility Insights for Web](https://accessibilityinsights.io/docs/web/overview/?referrer=playwright-accessibility-testing-js)을 권장합니다. 이 도구는 웹사이트의 [WCAG 2.1 AA](https://www.w3.org/WAI/WCAG21/quickref/?currentsidebar=%23col_customize&levels=aaa) 충족 범위를 단계별로 점검할 수 있게 도와줍니다.

## 접근성 테스트 예제[​](https://playwright.dev/docs/accessibility-testing#example-accessibility-tests "Direct link to Example accessibility tests")

접근성 테스트는 다른 Playwright 테스트와 동일하게 동작합니다. 별도의 테스트 케이스를 만들 수도 있고, 기존 테스트 케이스에 접근성 스캔과 assertion을 통합할 수도 있습니다.

다음 예제는 기본적인 접근성 테스트 시나리오 몇 가지를 보여줍니다.

### 전체 페이지 스캔[​](https://playwright.dev/docs/accessibility-testing#scanning-an-entire-page "Direct link to Scanning an entire page")

이 예제는 자동으로 탐지 가능한 접근성 위반 사항에 대해 페이지 전체를 테스트하는 방법을 보여줍니다. 이 테스트는 다음을 수행합니다.

1. `@axe-core/playwright` 패키지를 import합니다.
2. 일반적인 Playwright Test 문법으로 테스트 케이스를 정의합니다.
3. 일반적인 Playwright 문법으로 테스트 대상 페이지로 이동합니다.
4. 페이지에 대해 접근성 스캔을 실행하기 위해 `AxeBuilder.analyze()`를 await합니다.
5. 반환된 스캔 결과에 위반 사항이 없는지 확인하기 위해 일반적인 Playwright Test [assertions](https://playwright.dev/docs/test-assertions)을 사용합니다.

- TypeScript
- JavaScript

```
    import { test, expect } from '@playwright/test';
    import AxeBuilder from '@axe-core/playwright'; // 1

    test.describe('homepage', () => { // 2
      test('should not have any automatically detectable accessibility issues', async ({ page }) => {
        await page.goto('https://your-site.com/'); // 3

        const accessibilityScanResults = await new AxeBuilder({ page }).analyze(); // 4

        expect(accessibilityScanResults.violations).toEqual([]); // 5
      });
    });

```

```
    const { test, expect } = require('@playwright/test');
    const AxeBuilder = require('@axe-core/playwright').default; // 1

    test.describe('homepage', () => { // 2
      test('should not have any automatically detectable accessibility issues', async ({ page }) => {
        await page.goto('https://your-site.com/'); // 3

        const accessibilityScanResults = await new AxeBuilder({ page }).analyze(); // 4

        expect(accessibilityScanResults.violations).toEqual([]); // 5
      });
    });

```

### 페이지의 특정 부분만 스캔하도록 axe 구성하기[​](https://playwright.dev/docs/accessibility-testing#configuring-axe-to-scan-a-specific-part-of-a-page "Direct link to Configuring axe to scan a specific part of a page")

`@axe-core/playwright`는 axe를 위한 다양한 구성 옵션을 지원합니다. `AxeBuilder` 클래스로 Builder 패턴을 사용해 이러한 옵션을 지정할 수 있습니다.

예를 들어 [`AxeBuilder.include()`](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/playwright/README.md#axebuilderincludeselector-string--string)을 사용해 접근성 스캔 범위를 페이지의 특정 부분 하나로 제한할 수 있습니다.

`AxeBuilder.analyze()`는 호출 시점의 _현재 페이지 상태_ 를 스캔합니다. UI 상호작용에 따라 노출되는 페이지 영역을 스캔하려면 `analyze()`를 호출하기 전에 [Locators](https://playwright.dev/docs/locators)로 페이지와 상호작용하세요.

```
    test('navigation menu should not have automatically detectable accessibility violations', async ({
      page,
    }) => {
      await page.goto('https://your-site.com/');

      await page.getByRole('button', { name: 'Navigation Menu' }).click();

      // It is important to waitFor() the page to be in the desired
      // state *before* running analyze(). Otherwise, axe might not
      // find all the elements your test expects it to scan.
      await page.locator('#navigation-menu-flyout').waitFor();

      const accessibilityScanResults = await new AxeBuilder({ page })
          .include('#navigation-menu-flyout')
          .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    });

```

### WCAG 위반 스캔[​](https://playwright.dev/docs/accessibility-testing#scanning-for-wcag-violations "Direct link to Scanning for WCAG violations")

기본적으로 axe는 매우 다양한 접근성 규칙을 검사합니다. 이 중 일부는 [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/)의 특정 성공 기준에 대응하고, 일부는 특정 WCAG 기준에서 명시적으로 요구하지 않는 "best practice" 규칙입니다.

[`AxeBuilder.withTags()`](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/playwright/README.md#axebuilderwithtagstags-stringarray)를 사용하면 특정 WCAG 성공 기준에 대응하도록 "tagged"된 규칙만 실행하도록 접근성 스캔을 제한할 수 있습니다. 예를 들어 [Accessibility Insights for Web's Automated Checks](https://accessibilityinsights.io/docs/web/getstarted/fastpass/?referrer=playwright-accessibility-testing-js)는 WCAG A 및 AA 성공 기준 위반을 테스트하는 axe 규칙만 포함합니다. 이 동작과 일치시키려면 `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` 태그를 사용하면 됩니다.

자동화 테스트로는 모든 유형의 WCAG 위반을 탐지할 수 없다는 점에 유의하세요.

```
    test('should not have any automatically detectable WCAG A or AA violations', async ({ page }) => {
      await page.goto('https://your-site.com/');

      const accessibilityScanResults = await new AxeBuilder({ page })
          .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
          .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    });

```

axe-core가 지원하는 규칙 태그의 전체 목록은 [axe API 문서의 "Axe-core Tags" 섹션](https://www.deque.com/axe/core-documentation/api-documentation/#axecore-tags)에서 확인할 수 있습니다.

## 알려진 이슈 처리[​](https://playwright.dev/docs/accessibility-testing#handling-known-issues "Direct link to Handling known issues")

애플리케이션에 접근성 테스트를 추가할 때 자주 나오는 질문은 "알려진 위반 사항은 어떻게 억제하나요?"입니다. 아래 예제는 사용할 수 있는 몇 가지 기법을 보여줍니다.

### 스캔에서 개별 요소 제외하기[​](https://playwright.dev/docs/accessibility-testing#excluding-individual-elements-from-a-scan "Direct link to Excluding individual elements from a scan")

애플리케이션에 알려진 이슈가 있는 특정 요소가 몇 개 있다면, [`AxeBuilder.exclude()`](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/playwright/README.md#axebuilderexcludeselector-string--string)를 사용해 문제를 수정할 수 있을 때까지 해당 요소를 스캔 대상에서 제외할 수 있습니다.

보통 가장 단순한 옵션이지만, 중요한 단점이 있습니다.

- `exclude()`는 지정된 요소 _및 그 하위 모든 요소_ 를 제외합니다. 자식 요소가 많은 컴포넌트에는 사용을 피하세요.
- `exclude()`는 지정된 요소에 대해 알려진 이슈에 해당하는 규칙만이 아니라 _모든_ 규칙 실행을 막습니다.

아래는 특정 테스트 하나에서 요소 하나를 스캔 대상에서 제외하는 예제입니다.

```
    test('should not have any accessibility violations outside of elements with known issues', async ({
      page,
    }) => {
      await page.goto('https://your-site.com/page-with-known-issues');

      const accessibilityScanResults = await new AxeBuilder({ page })
          .exclude('#element-with-known-issue')
          .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    });

```

해당 요소가 많은 페이지에서 반복적으로 사용된다면, [test fixture 사용](https://playwright.dev/docs/accessibility-testing#using-a-test-fixture-for-common-axe-configuration)을 고려해 동일한 `AxeBuilder` 구성을 여러 테스트에서 재사용하세요.

### 개별 스캔 규칙 비활성화[​](https://playwright.dev/docs/accessibility-testing#disabling-individual-scan-rules "Direct link to Disabling individual scan rules")

애플리케이션에 특정 규칙에 대한 기존 위반이 많이 있다면, 문제를 수정할 수 있을 때까지 [`AxeBuilder.disableRules()`](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/playwright/README.md#axebuilderdisablerulesrules-stringarray)를 사용해 개별 규칙을 일시적으로 비활성화할 수 있습니다.

`disableRules()`에 전달할 규칙 ID는 억제하려는 위반 항목의 `id` 속성에서 찾을 수 있습니다. [axe 규칙 전체 목록](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)은 `axe-core` 문서에서 확인할 수 있습니다.

```
    test('should not have any accessibility violations outside of rules with known issues', async ({
      page,
    }) => {
      await page.goto('https://your-site.com/page-with-known-issues');

      const accessibilityScanResults = await new AxeBuilder({ page })
          .disableRules(['duplicate-id'])
          .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    });

```

### 스냅샷으로 특정 알려진 이슈 허용하기[​](https://playwright.dev/docs/accessibility-testing#using-snapshots-to-allow-specific-known-issues "Direct link to Using snapshots to allow specific known issues")

더 세밀한 단위로 알려진 이슈를 허용하고 싶다면, [Snapshots](https://playwright.dev/docs/test-snapshots)를 사용해 기존 위반 집합이 변경되지 않았는지 검증할 수 있습니다. 이 접근법은 복잡성과 취약성이 약간 늘어나는 대신 `AxeBuilder.exclude()` 사용의 단점을 피할 수 있습니다.

`accessibilityScanResults.violations` 배열 전체를 스냅샷으로 사용하지 마세요. 여기에는 렌더링된 HTML 스니펫처럼 해당 요소의 구현 세부사항이 포함됩니다. 이를 스냅샷에 포함하면, 관련 없는 이유로 해당 컴포넌트가 변경될 때마다 테스트가 쉽게 깨지게 됩니다.

```
    // Don't do this! This is fragile.
    expect(accessibilityScanResults.violations).toMatchSnapshot();

```

대신 해당 위반을 고유하게 식별하는 데 필요한 정보만 담은 _fingerprint_ 를 만들고, 그 fingerprint를 스냅샷으로 사용하세요.

```
    // This is less fragile than snapshotting the entire violations array.
    expect(violationFingerprints(accessibilityScanResults)).toMatchSnapshot();

    // my-test-utils.js
    function violationFingerprints(accessibilityScanResults) {
      const violationFingerprints = accessibilityScanResults.violations.map(violation => ({
        rule: violation.id,
        // These are CSS selectors which uniquely identify each element with
        // a violation of the rule in question.
        targets: violation.nodes.map(node => node.target),
      }));

      return JSON.stringify(violationFingerprints, null, 2);
    }

```

## 스캔 결과를 테스트 첨부 파일로 내보내기[​](https://playwright.dev/docs/accessibility-testing#exporting-scan-results-as-a-test-attachment "Direct link to Exporting scan results as a test attachment")

대부분의 접근성 테스트는 주로 axe 스캔 결과의 `violations` 속성에 집중합니다. 하지만 스캔 결과에는 `violations` 외의 정보도 포함됩니다. 예를 들어 통과한 규칙 정보와, 일부 규칙에 대해 axe가 결론을 내리지 못한 요소 정보도 포함됩니다. 이 정보는 테스트가 기대한 모든 위반을 잡아내지 못할 때 디버깅에 유용할 수 있습니다.

디버깅 목적으로 스캔 결과 _전체_ 를 테스트 결과에 포함하려면, [`testInfo.attach()`](https://playwright.dev/docs/api/class-testinfo#test-info-attach)로 스캔 결과를 테스트 첨부 파일로 추가하면 됩니다. 그러면 [Reporters](https://playwright.dev/docs/test-reporters)가 테스트 출력에 전체 결과를 포함하거나 링크할 수 있습니다.

다음 예제는 스캔 결과를 테스트에 첨부하는 방법을 보여줍니다.

```
    test('example with attachment', async ({ page }, testInfo) => {
      await page.goto('https://your-site.com/');

      const accessibilityScanResults = await new AxeBuilder({ page }).analyze();

      await testInfo.attach('accessibility-scan-results', {
        body: JSON.stringify(accessibilityScanResults, null, 2),
        contentType: 'application/json'
      });

      expect(accessibilityScanResults.violations).toEqual([]);
    });

```

## 공통 axe 구성을 위한 test fixture 사용[​](https://playwright.dev/docs/accessibility-testing#using-a-test-fixture-for-common-axe-configuration "Direct link to Using a test fixture for common axe configuration")

[Test fixtures](https://playwright.dev/docs/test-fixtures)는 여러 테스트에서 공통 `AxeBuilder` 구성을 공유하기에 좋은 방법입니다. 다음과 같은 시나리오에서 특히 유용합니다.

- 모든 테스트에서 공통 규칙 집합 사용
- 여러 페이지에 공통으로 나타나는 요소의 알려진 위반 억제
- 여러 스캔에서 독립적인 접근성 리포트를 일관되게 첨부

아래 예제는 위 시나리오를 모두 다루는 test fixture를 만들고 사용하는 방법을 보여줍니다.

### fixture 만들기[​](https://playwright.dev/docs/accessibility-testing#creating-a-fixture "Direct link to Creating a fixture")

이 fixture 예제는 공유 `withTags()` 및 `exclude()` 구성이 미리 적용된 `AxeBuilder` 객체를 생성합니다.

- TypeScript
- JavaScript

axe-test.ts

```
    import { test as base } from '@playwright/test';
    import AxeBuilder from '@axe-core/playwright';

    type AxeFixture = {
      makeAxeBuilder: () => AxeBuilder;
    };

    // Extend base test by providing "makeAxeBuilder"
    //
    // This new "test" can be used in multiple test files, and each of them will get
    // a consistently configured AxeBuilder instance.
    export const test = base.extend<AxeFixture>({
      makeAxeBuilder: async ({ page }, use) => {
        const makeAxeBuilder = () => new AxeBuilder({ page })
            .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
            .exclude('#commonly-reused-element-with-known-issue');

        await use(makeAxeBuilder);
      }
    });
    export { expect } from '@playwright/test';

```

axe-test.js

```
    const base = require('@playwright/test');
    const AxeBuilder = require('@axe-core/playwright').default;

    // Extend base test by providing "makeAxeBuilder"
    //
    // This new "test" can be used in multiple test files, and each of them will get
    // a consistently configured AxeBuilder instance.
    exports.test = base.test.extend({
      makeAxeBuilder: async ({ page }, use) => {
        const makeAxeBuilder = () => new AxeBuilder({ page })
            .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
            .exclude('#commonly-reused-element-with-known-issue');

        await use(makeAxeBuilder);
      }
    });
    exports.expect = base.expect;

```

### fixture 사용하기[​](https://playwright.dev/docs/accessibility-testing#using-a-fixture "Direct link to Using a fixture")

fixture를 사용하려면, 앞선 예제의 `new AxeBuilder({ page })`를 새로 정의한 `makeAxeBuilder` fixture로 교체하세요.

```
    const { test, expect } = require('./axe-test');

    test('example using custom fixture', async ({ page, makeAxeBuilder }) => {
      await page.goto('https://your-site.com/');

      const accessibilityScanResults = await makeAxeBuilder()
          // Automatically uses the shared AxeBuilder configuration,
          // but supports additional test-specific configuration too
          .include('#specific-element-under-test')
          .analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    });

```
