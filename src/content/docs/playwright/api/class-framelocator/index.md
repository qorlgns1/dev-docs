---
title: "FrameLocator"
description: "FrameLocator는 페이지의 에 대한 뷰를 나타냅니다. 을 가져오고 해당 iframe 내에서 요소를 찾는 데 충분한 로직을 캡처합니다. FrameLocator는 locator.contentFrame(), page.frameLocator(), 또는 locator.f..."
---

Source URL: https://playwright.dev/docs/api/class-framelocator

# FrameLocator | Playwright

FrameLocator는 페이지의 `iframe`에 대한 뷰를 나타냅니다. `iframe`을 가져오고 해당 iframe 내에서 요소를 찾는 데 충분한 로직을 캡처합니다. FrameLocator는 [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame), [page.frameLocator()](https://playwright.dev/docs/api/class-page#page-frame-locator), 또는 [locator.frameLocator()](https://playwright.dev/docs/api/class-locator#locator-frame-locator) 메서드로 생성할 수 있습니다.

```
    const locator = page.locator('#my-frame').contentFrame().getByText('Submit');
    await locator.click();

```

**엄격성**

Frame locator는 엄격합니다. 즉, frame locator에 대한 모든 작업은 주어진 selector와 일치하는 요소가 둘 이상이면 예외를 발생시킵니다.

```
    // Throws if there are several frames in DOM:
    await page.locator('.result-frame').contentFrame().getByRole('button').click();

    // Works because we explicitly tell locator to pick the first frame:
    await page.locator('.result-frame').contentFrame().first().getByRole('button').click();

```

**Locator를 FrameLocator로 변환**

`iframe`을 가리키는 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 객체가 있다면, [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame)을 사용해 [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")로 변환할 수 있습니다.

**FrameLocator를 Locator로 변환**

[FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator") 객체가 있다면, [frameLocator.owner()](https://playwright.dev/docs/api/class-framelocator#frame-locator-owner)를 사용해 동일한 `iframe`을 가리키는 [Locator](https://playwright.dev/docs/api/class-locator "Locator")로 변환할 수 있습니다.

---

## 메서드[​](https://playwright.dev/docs/api/class-framelocator#methods "Direct link to Methods")

### frameLocator[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-frame-locator "Direct link to frameLocator")

추가된 버전: v1.17 frameLocator.frameLocator

iframe으로 작업할 때, iframe 내부로 진입하고 그 iframe 안의 요소를 선택할 수 있는 frame locator를 만들 수 있습니다.

**사용법**

```
    frameLocator.frameLocator(selector);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-frame-locator-option-selector)

DOM 요소를 해석할 때 사용할 selector입니다.

**반환값**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-frame-locator-return)

---

### getByAltText[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text "Direct link to getByAltText")

추가된 버전: v1.27 frameLocator.getByAltText

alt 텍스트로 요소를 찾을 수 있게 해줍니다.

**사용법**

예를 들어, 이 메서드는 alt 텍스트가 "Playwright logo"인 이미지를 찾습니다:

```
    <img alt='Playwright logo'>

```

```
    await page.getByAltText('Playwright logo').click();

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text-option-exact)

정확히 일치하는 항목(대소문자 구분 및 전체 문자열 일치)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾는 경우에는 무시됩니다. 정확 일치에서도 공백은 trim된다는 점에 유의하세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text-return)

---

### getByLabel[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label "Direct link to getByLabel")

추가된 버전: v1.27 frameLocator.getByLabel

연결된 `<label>` 또는 `aria-labelledby` 요소의 텍스트, 또는 `aria-label` 속성으로 input 요소를 찾을 수 있게 해줍니다.

**사용법**

예를 들어, 이 메서드는 다음 DOM에서 "Username"과 "Password" 레이블로 input을 찾습니다:

```
    <input aria-label="Username">
    <label for="password-input">Password:</label>
    <input id="password-input">

```

```
    await page.getByLabel('Username').fill('john');
    await page.getByLabel('Password').fill('secret');

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label-option-exact)

정확히 일치하는 항목(대소문자 구분 및 전체 문자열 일치)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾는 경우에는 무시됩니다. 정확 일치에서도 공백은 trim된다는 점에 유의하세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label-return)

---

### getByPlaceholder[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder "Direct link to getByPlaceholder")

추가된 버전: v1.27 frameLocator.getByPlaceholder

placeholder 텍스트로 input 요소를 찾을 수 있게 해줍니다.

**사용법**

예를 들어, 다음 DOM 구조를 보겠습니다.

```
    <input type="email" placeholder="name@example.com" />

```

placeholder 텍스트로 input을 찾은 뒤 값을 입력할 수 있습니다:

```
    await page
        .getByPlaceholder('name@example.com')
        .fill('playwright@microsoft.com');

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder-option-exact)

정확히 일치하는 항목(대소문자 구분 및 전체 문자열 일치)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾는 경우에는 무시됩니다. 정확 일치에서도 공백은 trim된다는 점에 유의하세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder-return)

---

### getByRole[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role "Direct link to getByRole")

추가된 버전: v1.27 frameLocator.getByRole

[ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles), [ARIA 속성](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes), 그리고 [접근 가능한 이름](https://w3c.github.io/accname/#dfn-accessible-name)으로 요소를 찾을 수 있게 해줍니다.

**사용법**

다음 DOM 구조를 보겠습니다.

```
    <h3>Sign up</h3>
    <label>
      <input type="checkbox" /> Subscribe
    </label>
    <button>Submit</button>

```

각 요소를 암시적 role로 찾을 수 있습니다:

```
    await expect(page.getByRole('heading', { name: 'Sign up' })).toBeVisible();

    await page.getByRole('checkbox', { name: 'Subscribe' }).check();

    await page.getByRole('button', { name: /submit/i }).click();

```

**인수**

- `role` "alert" | "alertdialog" | "application" | "article" | "banner" | "blockquote" | "button" | "caption" | "cell" | "checkbox" | "code" | "columnheader" | "combobox" | "complementary" | "contentinfo" | "definition" | "deletion" | "dialog" | "directory" | "document" | "emphasis" | "feed" | "figure" | "form" | "generic" | "grid" | "gridcell" | "group" | "heading" | "img" | "insertion" | "link" | "list" | "listbox" | "listitem" | "log" | "main" | "marquee" | "math" | "meter" | "menu" | "menubar" | "menuitem" | "menuitemcheckbox" | "menuitemradio" | "navigation" | "none" | "note" | "option" | "paragraph" | "presentation" | "progressbar" | "radio" | "radiogroup" | "region" | "row" | "rowgroup" | "rowheader" | "scrollbar" | "search" | "searchbox" | "separator" | "slider" | "spinbutton" | "status" | "strong" | "subscript" | "superscript" | "switch" | "tab" | "table" | "tablist" | "tabpanel" | "term" | "textbox" | "time" | "timer" | "toolbar" | "tooltip" | "tree" | "treegrid" | "treeitem"[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-role)

필수 aria role입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `checked` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-checked)

일반적으로 `aria-checked` 또는 네이티브 `<input type=checkbox>` 컨트롤로 설정되는 속성입니다.

[`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked)에 대해 자세히 알아보세요.

    * `disabled` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-disabled)

일반적으로 `aria-disabled` 또는 `disabled`로 설정되는 속성입니다.

note

대부분의 다른 속성과 달리 `disabled`는 DOM 계층을 통해 상속됩니다. [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled)에 대해 자세히 알아보세요.

    * `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ Added in: v1.28[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-exact)

[name](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-name)를 정확히 일치시킬지 여부입니다(대소문자 구분 및 전체 문자열 일치). 기본값은 false입니다. [name](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-name)이 정규식이면 무시됩니다. 정확 일치에서도 공백은 trim된다는 점에 유의하세요.

    * `expanded` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-expanded)

일반적으로 `aria-expanded`로 설정되는 속성입니다.

[`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded)에 대해 자세히 알아보세요.

    * `includeHidden` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-include-hidden)

숨겨진 요소를 매칭할지 제어하는 옵션입니다. 기본적으로 role selector는 [ARIA에서 정의된](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion) 숨겨지지 않은 요소만 매칭합니다.

[`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden)에 대해 자세히 알아보세요.

    * `level` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-level)

일반적으로 `heading`, `listitem`, `row`, `treeitem` role에 존재하는 숫자 속성이며, `<h1>-<h6>` 요소에는 기본값이 있습니다.

[`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level)에 대해 자세히 알아보세요.

    * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-name)

[접근 가능한 이름](https://w3c.github.io/accname/#dfn-accessible-name)을 매칭하기 위한 옵션입니다. 기본적으로 대소문자를 구분하지 않고 부분 문자열을 검색하며, 이 동작은 [exact](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-exact)로 제어할 수 있습니다.

[접근 가능한 이름](https://w3c.github.io/accname/#dfn-accessible-name)에 대해 자세히 알아보세요.

    * `pressed` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-pressed)

일반적으로 `aria-pressed`로 설정되는 속성입니다.

[`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed)에 대해 자세히 알아보세요.

    * `selected` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-selected)

일반적으로 `aria-selected`로 설정되는 속성입니다.

[`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected)에 대해 자세히 알아보세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-return)

**세부 정보**

Role selector는 접근성 감사 및 적합성 테스트를 **대체하지 않으며**, ARIA 가이드라인에 대한 조기 피드백을 제공합니다.

많은 html 요소는 role selector가 인식하는 암시적으로 [정의된 role](https://w3c.github.io/html-aam/#html-element-role-mappings)을 가집니다. [지원되는 모든 role은 여기](https://www.w3.org/TR/wai-aria-1.2/#role_definitions)에서 확인할 수 있습니다. ARIA 가이드라인은 `role` 및/또는 `aria-*` 속성을 기본값으로 설정해 암시적 role과 속성을 중복하는 것을 **권장하지 않습니다**.

---

### getByTestId[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-test-id "Direct link to getByTestId")

추가된 버전: v1.27 frameLocator.getByTestId

test id로 요소를 찾습니다.

**사용법**

다음 DOM 구조를 보겠습니다.

```
    <button data-testid="directions">Itinéraire</button>

```

test id로 요소를 찾을 수 있습니다:

```
    await page.getByTestId('directions').click();

```

**인수**

- `testId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-test-id-option-test-id)

요소를 찾을 때 사용할 ID입니다.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-test-id-return)

**세부 정보**

기본적으로 `data-testid` 속성이 test id로 사용됩니다. 필요하면 [selectors.setTestIdAttribute()](https://playwright.dev/docs/api/class-selectors#selectors-set-test-id-attribute)를 사용해 다른 test id 속성으로 설정하세요.

```
    // Set custom test id attribute from @playwright/test config:
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        testIdAttribute: 'data-pw'
      },
    });

```

---

### getByText[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text "Direct link to getByText")

추가된 버전: v1.27 frameLocator.getByText

주어진 텍스트를 포함하는 요소를 찾을 수 있게 해줍니다.

접근 가능한 role 같은 다른 기준으로 먼저 매칭한 다음 텍스트 내용으로 필터링할 수 있는 [locator.filter()](https://playwright.dev/docs/api/class-locator#locator-filter)도 참고하세요.

**사용법**

다음 DOM 구조를 보겠습니다:

```
    <div>Hello <span>world</span></div>
    <div>Hello</div>

```

텍스트 부분 문자열, 정확한 문자열, 또는 정규식으로 찾을 수 있습니다:

```
    // Matches <span>
    page.getByText('world');

    // Matches first <div>
    page.getByText('Hello world');

    // Matches second <div>
    page.getByText('Hello', { exact: true });

    // Matches both <div>s
    page.getByText(/Hello/);

    // Matches second <div>
    page.getByText(/^hello$/i);

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text-option-exact)

정확히 일치하는 항목(대소문자 구분 및 전체 문자열 일치)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾는 경우에는 무시됩니다. 정확 일치에서도 공백은 trim된다는 점에 유의하세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text-return)

**세부 정보**

텍스트 매칭은 정확 일치인 경우에도 항상 공백을 정규화합니다. 예를 들어, 여러 공백을 하나로 바꾸고 줄바꿈을 공백으로 바꾸며 앞뒤 공백을 무시합니다.

`button` 및 `submit` 타입의 input 요소는 텍스트 내용 대신 `value`로 매칭됩니다. 예를 들어, 텍스트 `"Log in"`으로 찾으면 `<input type=button value="Log in">`과 매칭됩니다.

---

### getByTitle[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title "Direct link to getByTitle")

추가된 버전: v1.27 frameLocator.getByTitle

title 속성으로 요소를 찾을 수 있게 해줍니다.

**사용법**

다음 DOM 구조를 보겠습니다.

```
    <span title='Issues count'>25 issues</span>

```

title 텍스트로 찾은 뒤 이슈 개수를 확인할 수 있습니다:

```
    await expect(page.getByTitle('Issues count')).toHaveText('25 issues');

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title-option-exact)

정확히 일치하는 항목(대소문자 구분 및 전체 문자열 일치)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾는 경우에는 무시됩니다. 정확 일치에서도 공백은 trim된다는 점에 유의하세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title-return)

---

### locator[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator "Direct link to locator")

추가된 버전: v1.17 frameLocator.locator

이 메서드는 locator 하위 트리에서 지정한 selector와 일치하는 요소를 찾습니다. 또한 [locator.filter()](https://playwright.dev/docs/api/class-locator#locator-filter) 메서드와 유사한 필터 옵션도 지원합니다.

[locator에 대해 더 알아보기](https://playwright.dev/docs/locators).

**사용법**

```
    frameLocator.locator(selectorOrLocator);
    frameLocator.locator(selectorOrLocator, options);

```

**인수**

- `selectorOrLocator` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-selector-or-locator)

DOM 요소를 해석할 때 사용할 selector 또는 locator입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `has` [Locator](https://playwright.dev/docs/api/class-locator "Locator") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has)

이 상대 locator와 일치하는 요소를 포함하는 결과로 메서드 결과를 좁힙니다. 예를 들어 `text=Playwright`를 가진 `article`은 `<article><div>Playwright</div></article>`과 매칭됩니다.

내부 locator는 **반드시 상대 경로여야 하며**, 문서 루트가 아니라 외부 locator 매치에서 시작해 조회됩니다. 예를 들어 `<article><content><div>Playwright</div></content></article>`에서 `div`를 가진 `content`를 찾을 수 있습니다. 하지만 `article div`를 가진 `content`를 찾는 것은 실패합니다. 내부 locator는 상대적이어야 하며 `content` 바깥 요소를 사용하면 안 되기 때문입니다.

외부 locator와 내부 locator는 같은 frame에 속해야 합니다. 내부 locator에는 [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")가 포함되면 안 됩니다.

    * `hasNot` [Locator](https://playwright.dev/docs/api/class-locator "Locator") _(선택 사항)_ Added in: v1.33[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has-not)

내부 locator와 일치하는 요소를 포함하지 않는 요소와 매칭됩니다. 내부 locator는 외부 locator를 기준으로 조회됩니다. 예를 들어 `div`가 없는 `article`은 `<article><span>Playwright</span></article>`과 매칭됩니다.

외부 locator와 내부 locator는 같은 frame에 속해야 합니다. 내부 locator에는 [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")가 포함되면 안 됩니다.

    * `hasNotText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(선택 사항)_ Added in: v1.33[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has-not-text)

내부 어딘가(자식 또는 하위 요소 포함)에 지정된 텍스트를 포함하지 않는 요소와 매칭됩니다. [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")이 전달되면 대소문자를 구분하지 않고 부분 문자열을 검색합니다.

    * `hasText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(선택 사항)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has-text)

내부 어딘가(자식 또는 하위 요소 포함)에 지정된 텍스트를 포함하는 요소와 매칭됩니다. [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")이 전달되면 대소문자를 구분하지 않고 부분 문자열을 검색합니다. 예를 들어 `"Playwright"`는 `<article><div>Playwright</div></article>`과 매칭됩니다.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-return)

---

### owner[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-owner "Direct link to owner")

추가된 버전: v1.43 frameLocator.owner

이 frame locator와 동일한 `iframe`을 가리키는 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 객체를 반환합니다.

어딘가에서 얻은 [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator") 객체가 있고, 이후 `iframe` 요소와 상호작용하고 싶을 때 유용합니다.

역방향 작업에는 [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame)을 사용하세요.

**사용법**

```
    const frameLocator = page.locator('iframe[name="embedded"]').contentFrame();
    // ...
    const locator = frameLocator.owner();
    await expect(locator).toBeVisible();

```

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-owner-return)

---

## 사용 중단됨[​](https://playwright.dev/docs/api/class-framelocator#deprecated "Direct link to Deprecated")

### first[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-first "Direct link to first")

추가된 버전: v1.17 frameLocator.first

사용 중단됨

대신 [locator.first()](https://playwright.dev/docs/api/class-locator#locator-first) 다음에 [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame)을 사용하세요.

첫 번째로 매칭되는 frame을 가리키는 locator를 반환합니다.

**사용법**

```
    frameLocator.first();

```

**반환값**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-first-return)

---

### last[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-last "Direct link to last")

추가된 버전: v1.17 frameLocator.last

사용 중단됨

대신 [locator.last()](https://playwright.dev/docs/api/class-locator#locator-last) 다음에 [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame)을 사용하세요.

마지막으로 매칭되는 frame을 가리키는 locator를 반환합니다.

**사용법**

```
    frameLocator.last();

```

**반환값**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-last-return)

---

### nth[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-nth "Direct link to nth")

추가된 버전: v1.17 frameLocator.nth

사용 중단됨

대신 [locator.nth()](https://playwright.dev/docs/api/class-locator#locator-nth) 다음에 [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame)을 사용하세요.

n번째로 매칭되는 frame을 가리키는 locator를 반환합니다. 0 기반이므로 `nth(0)`은 첫 번째 frame을 선택합니다.

**사용법**

```
    frameLocator.nth(index);

```

**인수**

- `index` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-nth-option-index)

**반환값**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-nth-return)
