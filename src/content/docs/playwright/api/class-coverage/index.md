---
title: "Coverage"
description: "Coverage는 페이지에서 사용된 JavaScript 및 CSS 부분에 대한 정보를 수집합니다."
---

Source URL: https://playwright.dev/docs/api/class-coverage

# Coverage | Playwright

Coverage는 페이지에서 사용된 JavaScript 및 CSS 부분에 대한 정보를 수집합니다.

페이지 로드에 대해 JavaScript coverage를 사용해 Istanbul 리포트를 생성하는 예시:

note

Coverage API는 Chromium 기반 브라우저에서만 지원됩니다.

```
    const { chromium } = require('playwright');
    const v8toIstanbul = require('v8-to-istanbul');

    (async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      await page.coverage.startJSCoverage();
      await page.goto('https://chromium.org');
      const coverage = await page.coverage.stopJSCoverage();
      for (const entry of coverage) {
        const converter = v8toIstanbul('', 0, { source: entry.source });
        await converter.load();
        converter.applyCoverage(entry.functions);
        console.log(JSON.stringify(converter.toIstanbul()));
      }
      await browser.close();
    })();

```

---

## 메서드[​](https://playwright.dev/docs/api/class-coverage#methods "Direct link to Methods")

### startCSSCoverage[​](https://playwright.dev/docs/api/class-coverage#coverage-start-css-coverage "Direct link to startCSSCoverage")

추가된 버전: v1.11 coverage.startCSSCoverage

커버리지 수집 시작을 반환합니다.

**사용법**

```
    await coverage.startCSSCoverage();
    await coverage.startCSSCoverage(options);

```

**인자**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `resetOnNavigation` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-coverage#coverage-start-css-coverage-option-reset-on-navigation)

탐색이 발생할 때마다 coverage를 초기화할지 여부입니다. 기본값은 `true`입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-coverage#coverage-start-css-coverage-return)

---

### startJSCoverage[​](https://playwright.dev/docs/api/class-coverage#coverage-start-js-coverage "Direct link to startJSCoverage")

추가된 버전: v1.11 coverage.startJSCoverage

커버리지 수집 시작을 반환합니다.

note

익명 스크립트는 연결된 url이 없는 스크립트입니다. 이런 스크립트는 페이지에서 `eval` 또는 `new Function`을 사용해 동적으로 생성됩니다. [reportAnonymousScripts](https://playwright.dev/docs/api/class-coverage#coverage-start-js-coverage-option-report-anonymous-scripts)가 `true`로 설정되면, 익명 스크립트의 URL은 `__playwright_evaluation_script__`가 됩니다.

**사용법**

```
    await coverage.startJSCoverage();
    await coverage.startJSCoverage(options);

```

**인자**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `reportAnonymousScripts` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-coverage#coverage-start-js-coverage-option-report-anonymous-scripts)

페이지에서 생성된 익명 스크립트를 리포트할지 여부입니다. 기본값은 `false`입니다.

    * `resetOnNavigation` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-coverage#coverage-start-js-coverage-option-reset-on-navigation)

탐색이 발생할 때마다 coverage를 초기화할지 여부입니다. 기본값은 `true`입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-coverage#coverage-start-js-coverage-return)

---

### stopCSSCoverage[​](https://playwright.dev/docs/api/class-coverage#coverage-stop-css-coverage "Direct link to stopCSSCoverage")

추가된 버전: v1.11 coverage.stopCSSCoverage

모든 스타일시트에 대한 coverage 리포트 배열을 반환합니다.

note

CSS Coverage에는 sourceURL이 없는 동적으로 주입된 style 태그가 포함되지 않습니다.

**사용법**

```
    await coverage.stopCSSCoverage();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>>[#](https://playwright.dev/docs/api/class-coverage#coverage-stop-css-coverage-return)
  - `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

StyleSheet URL

    * `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

사용 가능한 경우 StyleSheet 내용입니다.

    * `ranges` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

      * `start` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

텍스트 내 시작 오프셋(포함)

      * `end` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

텍스트 내 끝 오프셋(미포함)

사용된 StyleSheet 범위입니다. 범위는 정렬되어 있고 서로 겹치지 않습니다.

---

### stopJSCoverage[​](https://playwright.dev/docs/api/class-coverage#coverage-stop-js-coverage "Direct link to stopJSCoverage")

추가된 버전: v1.11 coverage.stopJSCoverage

모든 스크립트에 대한 coverage 리포트 배열을 반환합니다.

note

JavaScript Coverage에는 기본적으로 익명 스크립트가 포함되지 않습니다. 하지만 sourceURL이 있는 스크립트는 리포트됩니다.

**사용법**

```
    await coverage.stopJSCoverage();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>>[#](https://playwright.dev/docs/api/class-coverage#coverage-stop-js-coverage-return)
  - `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

스크립트 URL

    * `scriptId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

스크립트 ID

    * `source` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(선택 사항)_

해당하는 경우 스크립트 내용입니다.

    * `functions` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

      * `functionName` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `isBlockCoverage` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

      * `ranges` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `count` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

        * `startOffset` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

        * `endOffset` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

V8 전용 coverage 형식입니다.
