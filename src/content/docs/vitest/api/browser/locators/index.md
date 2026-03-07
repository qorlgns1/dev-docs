---
title: "Locators"
description: "locator는 하나의 요소 또는 여러 요소를 나타내는 표현입니다. 모든 locator는 selector라고 하는 문자열로 정의됩니다. Vitest는 내부적으로 selector를 생성해 주는 편의 메서드를 제공하여 이를 추상화합니다."
---

출처 URL: https://vitest.dev/api/browser/locators

# Locators

locator는 하나의 요소 또는 여러 요소를 나타내는 표현입니다. 모든 locator는 selector라고 하는 문자열로 정의됩니다. Vitest는 내부적으로 selector를 생성해 주는 편의 메서드를 제공하여 이를 추상화합니다.

locator API는 [Ivya](https://npmjs.com/ivya)라고 불리는 [Playwright의 locator](https://playwright.dev/docs/api/class-locator) 포크를 사용합니다. 하지만 Vitest는 playwright에만 국한하지 않고 모든 [provider](https://vitest.dev/config/browser#browser-provider)에 이 API를 제공합니다.

::: tip
이 페이지는 API 사용법을 다룹니다. locator와 사용법을 더 잘 이해하려면 [Playwright의 "Locators" 문서](https://playwright.dev/docs/locators)를 읽어보세요.
:::

## getByRole

```ts
function getByRole(
  role: ARIARole | string,
  options?: LocatorByRoleOptions,
): Locator;
```

[ARIA role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles), [ARIA attributes](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes), 그리고 [accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)으로 요소를 찾는 방법을 생성합니다.

::: tip
`getByText('The name')`로 단일 요소만 조회하는 경우, `getByRole(expectedRole, { name: 'The name' })`를 사용하는 편이 더 나은 경우가 많습니다. accessible name 쿼리는 `*ByAltText`나 `*ByTitle` 같은 다른 쿼리를 대체하지 않습니다. accessible name이 해당 속성과 같을 수는 있지만, 그 속성들의 기능 자체를 대체하지는 않습니다.
:::

다음 DOM 구조를 생각해 봅시다.

```html
<h3>Sign up</h3>
<label>
  Login
  <input type="text" />
</label>
<label>
  Password
  <input type="password" />
</label>
<br />
<button>Submit</button>
```

각 요소를 암시적 role로 찾을 수 있습니다:

```ts
await expect
  .element(page.getByRole("heading", { name: "Sign up" }))
  .toBeVisible();

await page.getByRole("textbox", { name: "Login" }).fill("admin");
await page.getByRole("textbox", { name: "Password" }).fill("admin");

await page.getByRole("button", { name: /submit/i }).click();
```

::: warning
role은 ARIA role 계층 구조를 상속하지 않고 문자열 동등성으로 매칭됩니다. 따라서 `checkbox` 같은 상위 role을 조회해도 `switch` 같은 하위 role 요소는 포함되지 않습니다.

기본적으로 HTML의 많은 시맨틱 요소는 role을 가집니다. 예를 들어 `<input type="radio">`는 "radio" role을 가집니다. 반면 HTML의 비시맨틱 요소는 role이 없습니다. 의미가 추가되지 않은 `<div>`와 `<span>`은 `null`을 반환합니다. `role` 속성으로 시맨틱을 제공할 수 있습니다.

이미 암시적 role이 있는 내장 요소에 `role` 또는 `aria-*` 속성으로 role을 제공하는 것은 ARIA 가이드라인에서 **강하게 권장되지 않습니다**.
:::

##### Options

- `exact: boolean`

  `name`을 정확히 매칭할지 여부입니다: 대소문자를 구분하고 전체 문자열이 일치해야 합니다. 기본값은 비활성화입니다. `name`이 정규식이면 이 옵션은 무시됩니다. 정확 매칭이어도 공백은 trim된다는 점에 유의하세요.

  ```tsx
  <button>Hello World</button>;

  page.getByRole("button", { name: "hello world" }); // ✅
  page.getByRole("button", { name: "hello world", exact: true }); // ❌
  page.getByRole("button", { name: "Hello World", exact: true }); // ✅
  ```

- `checked: boolean`

  체크된 요소(`aria-checked` 또는 `<input type="checkbox"/>`로 설정)를 포함할지 여부입니다. 기본적으로 필터는 적용되지 않습니다.

  자세한 내용은 [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked)를 참고하세요.

  ```tsx
  <>
    <button role="checkbox" aria-checked="true" />
    <input type="checkbox" checked />
  </>;

  page.getByRole("checkbox", { checked: true }); // ✅
  page.getByRole("checkbox", { checked: false }); // ❌
  ```

- `disabled: boolean`

  비활성화된 요소를 포함할지 여부입니다. 기본적으로 필터는 적용되지 않습니다. 다른 속성과 달리 `disable` 상태는 상속된다는 점에 유의하세요.

  자세한 내용은 [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled)를 참고하세요.

  ```tsx
  <input type="text" disabled />;

  page.getByRole("textbox", { disabled: true }); // ✅
  page.getByRole("textbox", { disabled: false }); // ❌
  ```

- `expanded: boolean`

  확장된 요소를 포함할지 여부입니다. 기본적으로 필터는 적용되지 않습니다.

  자세한 내용은 [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded)를 참고하세요.

  ```tsx
  <a aria-expanded="true" href="example.com">
    Link
  </a>;

  page.getByRole("link", { expanded: true }); // ✅
  page.getByRole("link", { expanded: false }); // ❌
  ```

- `includeHidden: boolean`

  접근성 트리에서 [일반적으로 제외되는](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion) 요소도 조회할지 여부입니다. 기본적으로 role selector는 숨겨지지 않은 요소만 매칭합니다.

  `none` 및 `presentation` role은 항상 포함됩니다.

  ```tsx
  <button style="display: none" />;

  page.getByRole("button"); // ❌
  page.getByRole("button", { includeHidden: false }); // ❌
  page.getByRole("button", { includeHidden: true }); // ✅
  ```

- `level: number`

  `heading`, `listitem`, `row`, `treeitem` role에 주로 존재하는 숫자 속성으로, `<h1>-<h6>` 요소는 기본값을 가집니다. 기본적으로 필터는 적용되지 않습니다.

  자세한 내용은 [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level)를 참고하세요.

  ```tsx
  <>
    <h1>Heading Level One</h1>
    <div role="heading" aria-level="1">
      Second Heading Level One
    </div>
  </>;

  page.getByRole("heading", { level: 1 }); // ✅
  page.getByRole("heading", { level: 2 }); // ❌
  ```

- `name: string | RegExp`

  [accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)입니다. 기본적으로 대소문자를 구분하지 않고 부분 문자열을 검색합니다. 이 동작은 `exact` 옵션으로 제어할 수 있습니다.

  ```tsx
  <button>Click Me!</button>;

  page.getByRole("button", { name: "Click Me!" }); // ✅
  page.getByRole("button", { name: "click me!" }); // ✅
  page.getByRole("button", { name: "Click Me?" }); // ❌
  ```

- `pressed: boolean`

  눌린 요소를 포함할지 여부입니다. 기본적으로 필터는 적용되지 않습니다.

  자세한 내용은 [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed)를 참고하세요.

  ```tsx
  <button aria-pressed="true">👍</button>;

  page.getByRole("button", { pressed: true }); // ✅
  page.getByRole("button", { pressed: false }); // ❌
  ```

- `selected: boolean`

  선택된 요소를 포함할지 여부입니다. 기본적으로 필터는 적용되지 않습니다.

  자세한 내용은 [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected)를 참고하세요.

  ```tsx
  <button role="tab" aria-selected="true">
    Vue
  </button>;

  page.getByRole("button", { selected: true }); // ✅
  page.getByRole("button", { selected: false }); // ❌
  ```

##### See also

- MDN의 ARIA role 목록
- w3.org의 ARIA role 목록
- testing-library의 `ByRole`

## getByAltText

```ts
function getByAltText(text: string | RegExp, options?: LocatorOptions): Locator;
```

텍스트와 일치하는 `alt` 속성을 가진 요소를 찾을 수 있는 locator를 생성합니다. testing-library 구현과 달리, Vitest는 일치하는 `alt` 속성이 있는 모든 요소를 매칭합니다.

```tsx
<img alt="Incredibles 2 Poster" src="/incredibles-2.png" />;

page.getByAltText(/incredibles.*? poster/i); // ✅
page.getByAltText("non existing alt text"); // ❌
```

#### Options

- `exact: boolean`

  `text`를 정확히 매칭할지 여부입니다: 대소문자를 구분하고 전체 문자열이 일치해야 합니다. 기본값은 비활성화입니다. `text`가 정규식이면 이 옵션은 무시됩니다. 정확 매칭이어도 공백은 trim된다는 점에 유의하세요.

#### See also

- testing-library의 `ByAltText`

## getByLabelText

```ts
function getByLabelText(
  text: string | RegExp,
  options?: LocatorOptions,
): Locator;
```

연결된 label이 있는 요소를 찾을 수 있는 locator를 생성합니다.

아래 예시에서 `page.getByLabelText('Username')` locator는 모든 input을 찾습니다:

```html
// for/htmlFor relationship between label and form element id
<label for="username-input">Username</label>
<input id="username-input" />

// The aria-labelledby attribute with form elements
<label id="username-label">Username</label>
<input aria-labelledby="username-label" />

// Wrapper labels
<label>Username <input /></label>

// Wrapper labels where the label text is in another child element
<label>
  <span>Username</span>
  <input />
</label>

// aria-label attributes // Take care because this is not a label that users can
see on the page, // so the purpose of your input must be obvious to visual
users.
<input aria-label="Username" />
```

#### Options

- `exact: boolean`

  `text`를 정확히 매칭할지 여부입니다: 대소문자를 구분하고 전체 문자열이 일치해야 합니다. 기본값은 비활성화입니다. `text`가 정규식이면 이 옵션은 무시됩니다. 정확 매칭이어도 공백은 trim된다는 점에 유의하세요.

#### See also

- testing-library의 `ByLabelText`

## getByPlaceholder

```ts
function getByPlaceholder(
  text: string | RegExp,
  options?: LocatorOptions,
): Locator;
```

지정한 `placeholder` 속성을 가진 요소를 찾을 수 있는 locator를 생성합니다. Vitest는 `input`뿐 아니라 일치하는 `placeholder` 속성이 있는 모든 요소를 매칭합니다.

```tsx
<input placeholder="Username" />;

page.getByPlaceholder("Username"); // ✅
page.getByPlaceholder("not found"); // ❌
```

::: warning
일반적으로 placeholder보다 [`getByLabelText`](#getbylabeltext)로 label에 의존하는 것이 더 좋습니다.
:::

#### Options

- `exact: boolean`

  `text`를 정확히 매칭할지 여부입니다: 대소문자를 구분하고 전체 문자열이 일치해야 합니다. 기본값은 비활성화입니다. `text`가 정규식이면 이 옵션은 무시됩니다. 정확 매칭이어도 공백은 trim된다는 점에 유의하세요.

#### See also

- testing-library의 `ByPlaceholderText`

## getByText

```ts
function getByText(text: string | RegExp, options?: LocatorOptions): Locator;
```

지정한 텍스트를 포함하는 요소를 찾을 수 있는 locator를 생성합니다. 텍스트는 TextNode의 [`nodeValue`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeValue)와 매칭되며, type이 `button` 또는 `reset`인 input의 경우 value와 매칭됩니다. 텍스트 매칭은 정확 매칭이어도 항상 공백을 정규화합니다. 예를 들어 여러 공백은 하나로 바꾸고, 줄바꿈은 공백으로 바꾸며, 앞뒤 공백은 무시합니다.

```tsx
<a href="/about">About ℹ️</a>;

page.getByText(/about/i); // ✅
page.getByText("about", { exact: true }); // ❌
```

::: tip
이 locator는 비상호작용 요소를 찾을 때 유용합니다. 버튼이나 input 같은 상호작용 요소를 찾아야 한다면 [`getByRole`](#getbyrole)을 우선 사용하세요.
:::

#### Options

- `exact: boolean`

  `text`를 정확히 매칭할지 여부입니다: 대소문자를 구분하고 전체 문자열이 일치해야 합니다. 기본값은 비활성화입니다. `text`가 정규식이면 이 옵션은 무시됩니다. 정확 매칭이어도 공백은 trim된다는 점에 유의하세요.

#### See also

- testing-library의 `ByText`

## getByTitle

```ts
function getByTitle(text: string | RegExp, options?: LocatorOptions): Locator;
```

지정한 `title` 속성을 가진 요소를 찾을 수 있는 locator를 생성합니다. testing-library의 `getByTitle`과 달리, Vitest는 SVG 내부의 `title` 요소를 찾을 수 없습니다.

```tsx
<span title="Delete" id="2"></span>;

page.getByTitle("Delete"); // ✅
page.getByTitle("Create"); // ❌
```

#### Options

- `exact: boolean`

  `text`를 정확히 매칭할지 여부입니다: 대소문자를 구분하고 전체 문자열이 일치해야 합니다. 기본값은 비활성화입니다. `text`가 정규식이면 이 옵션은 무시됩니다. 정확 매칭이어도 공백은 trim된다는 점에 유의하세요.

#### See also

- testing-library의 `ByTitle`

## getByTestId

```ts
function getByTestId(text: string | RegExp): Locator;
```

지정한 test id 속성과 일치하는 요소를 찾을 수 있는 locator를 생성합니다. 속성 이름은 [`browser.locators.testIdAttribute`](https://vitest.dev/config/browser/locators#testidattribute)로 설정할 수 있습니다.

```tsx
<div data-testid="custom-element" />;

page.getByTestId("custom-element"); // ✅
page.getByTestId("non-existing-element"); // ❌
```

::: warning
다른 locator로 사용 사례를 해결할 수 없을 때만 이것을 사용하는 것을 권장합니다. `data-testid` 속성 사용은 소프트웨어의 실제 사용 방식과 유사하지 않으므로 가능하면 피해야 합니다.
:::

#### Options

- `exact: boolean`

  `text`를 정확히 매칭할지 여부입니다: 대소문자를 구분하고 전체 문자열이 일치해야 합니다. 기본값은 비활성화입니다. `text`가 정규식이면 이 옵션은 무시됩니다. 정확 매칭이어도 공백은 trim된다는 점에 유의하세요.

#### See also

- testing-library의 `ByTestId`

## nth

```ts
function nth(index: number): Locator;
```

이 메서드는 다중 요소 쿼리 결과에서 특정 인덱스만 매칭하는 새 locator를 반환합니다. 0부터 시작하며 `nth(0)`은 첫 번째 요소를 선택합니다. `elements()[n]`과 달리 `nth` locator는 요소가 나타날 때까지 재시도합니다.

```html
<div aria-label="one"><input /><input /><input /></div>
<div aria-label="two"><input /></div>
```

```tsx
page.getByRole("textbox").nth(0); // ✅
page.getByRole("textbox").nth(4); // ❌
```

::: tip
`nth`를 사용하기 전에 체이닝된 locator로 검색 범위를 좁히는 것이 유용할 수 있습니다.
때로는 요소 위치 외에 구분 방법이 없을 수 있습니다. flaky를 유발할 수는 있지만, 아무것도 없는 것보다는 낫습니다.
:::

```tsx
page.getByLabel("two").getByRole("input"); // ✅ better alternative to page.getByRole('textbox').nth(3)
page.getByLabel("one").getByRole("input"); // ❌ too ambiguous
page.getByLabel("one").getByRole("input").nth(1); // ✅ pragmatic compromise
```

## first

```ts
function first(): Locator;
```

이 메서드는 다중 요소 쿼리 결과에서 첫 번째 인덱스만 매칭하는 새 locator를 반환합니다.
`nth(0)`의 축약형입니다.

```html
<input /> <input /> <input />
```

```tsx
page.getByRole("textbox").first(); // ✅
```

## last

```ts
function last(): Locator;
```

이 메서드는 다중 요소 쿼리 결과에서 마지막 인덱스만 매칭하는 새 locator를 반환합니다.
`nth(-1)`의 축약형입니다.

```html
<input /> <input /> <input />
```

```tsx
page.getByRole("textbox").last(); // ✅
```

## and

```ts
function and(locator: Locator): Locator;
```

이 메서드는 부모 locator와 제공된 locator를 모두 만족하는 새 locator를 만듭니다. 다음 예시는 특정 title을 가진 버튼을 찾습니다:

```ts
page.getByRole("button").and(page.getByTitle("Subscribe"));
```

## or

```ts
function or(locator: Locator): Locator;
```

이 메서드는 두 locator 중 하나 또는 둘 다 매칭하는 새 locator를 만듭니다.

::: warning
locator가 단일 요소보다 많이 매칭되면, 단일 요소를 기대하는 다른 메서드를 호출할 때 오류가 발생할 수 있습니다:

```tsx
<>
  <button>Click me</button>
  <a href="https://vitest.dev">Error happened!</a>
</>;

page.getByRole("button").or(page.getByRole("link")).click(); // ❌ matches multiple elements
```

:::

## filter

```ts
function filter(options: LocatorOptions): Locator;
```

이 메서드는 텍스트 필터링 같은 옵션에 따라 locator 범위를 좁힙니다. 여러 필터를 적용하기 위해 체이닝할 수 있습니다.

### has

- **Type:** `Locator`

이 옵션은 제공된 locator와 매칭되는 다른 요소를 포함하는 요소만 매칭하도록 selector 범위를 좁힙니다. 예를 들어 다음 HTML에서:

```html{1,3}
<article>
  <div>Vitest</div>
</article>
<article>
  <div>Rolldown</div>
</article>
```

`Vitest` 텍스트를 내부에 가진 `article`만 찾도록 locator를 좁힐 수 있습니다:

```ts
page.getByRole("article").filter({ has: page.getByText("Vitest") }); // ✅
```

::: warning
제공된 locator(예시의 `page.getByText('Vitest')`)는 부모 locator(예시의 `page.getByRole('article')`)를 기준으로 한 상대 locator여야 합니다. 문서 루트가 아니라 부모 locator부터 조회됩니다.

즉, 부모 locator 밖의 요소를 조회하는 locator는 전달할 수 없습니다:

```ts
page.getByText("Vitest").filter({ has: page.getByRole("article") }); // ❌
```

이 예시는 `article` 요소가 `Vitest` 텍스트를 가진 요소의 바깥에 있기 때문에 실패합니다.
:::

::: tip
이 메서드는 요소 범위를 더 좁히기 위해 체이닝할 수 있습니다:

```ts
page
  .getByRole("article")
  .filter({ has: page.getByRole("button", { name: "delete row" }) })
  .filter({ has: page.getByText("Vitest") });
```

:::

### hasNot

- **Type:** `Locator`

이 옵션은 제공된 locator와 매칭되는 다른 요소를 포함하지 않는 요소만 매칭하도록 selector 범위를 좁힙니다. 예를 들어 다음 HTML에서:

```html{1,3}
<article>
  <div>Vitest</div>
</article>
<article>
  <div>Rolldown</div>
</article>
```

내부에 `Rolldown`이 없는 `article`만 찾도록 locator를 좁힐 수 있습니다.

```ts
page.getByRole("article").filter({ hasNot: page.getByText("Rolldown") }); // ✅
page.getByRole("article").filter({ hasNot: page.getByText("Vitest") }); // ❌
```

::: warning
제공된 locator는 [`has`](#has) 옵션과 마찬가지로 문서 루트가 아니라 부모를 기준으로 조회된다는 점에 유의하세요.
:::

### hasText

- **Type:** `string | RegExp`

이 옵션은 내부 어딘가에 제공된 텍스트를 포함하는 요소만 매칭하도록 selector 범위를 좁힙니다. `string`이 전달되면 대소문자를 구분하지 않고 부분 문자열을 검색합니다.

```html{1,3}
<article>
  <div>Vitest</div>
</article>
<article>
  <div>Rolldown</div>
</article>
```

두 locator는 검색이 대소문자를 구분하지 않기 때문에 동일한 요소를 찾습니다:

```ts
page.getByRole("article").filter({ hasText: "Vitest" }); // ✅
page.getByRole("article").filter({ hasText: "Vite" }); // ✅
```

### hasNotText

- **타입:** `string | RegExp`

이 옵션은 내부 어딘가에 제공된 텍스트를 포함하지 않는 요소만 매칭하도록 selector를 좁힙니다. `string`이 전달되면 매칭은 대소문자를 구분하지 않으며 부분 문자열을 검색합니다.

## 메서드

모든 메서드는 비동기이며 반드시 await 해야 합니다. Vitest 3부터는 메서드를 await 하지 않으면 테스트가 실패합니다.

### click

```ts
function click(options?: UserEventClickOptions): Promise<void>;
```

요소를 클릭합니다. 옵션을 사용해 커서 위치를 설정할 수 있습니다.

```ts
import { page } from "vitest/browser";

await page.getByRole("img", { name: "Rose" }).click();
```

- 자세한 내용은 `userEvent.click` 참고

### dblClick

```ts
function dblClick(options?: UserEventDoubleClickOptions): Promise<void>;
```

요소에서 더블 클릭 이벤트를 트리거합니다. 옵션을 사용해 커서 위치를 설정할 수 있습니다.

```ts
import { page } from "vitest/browser";

await page.getByRole("img", { name: "Rose" }).dblClick();
```

- 자세한 내용은 `userEvent.dblClick` 참고

### tripleClick

```ts
function tripleClick(options?: UserEventTripleClickOptions): Promise<void>;
```

요소에서 트리플 클릭 이벤트를 트리거합니다. 브라우저 API에는 `tripleclick`이 없으므로, 이 메서드는 click 이벤트를 연속으로 세 번 발생시킵니다.

```ts
import { page } from "vitest/browser";

await page.getByRole("img", { name: "Rose" }).tripleClick();
```

- 자세한 내용은 `userEvent.tripleClick` 참고

### clear

```ts
function clear(options?: UserEventClearOptions): Promise<void>;
```

input 요소의 내용을 비웁니다.

```ts
import { page } from "vitest/browser";

await page.getByRole("textbox", { name: "Full Name" }).clear();
```

- 자세한 내용은 `userEvent.clear` 참고

### hover

```ts
function hover(options?: UserEventHoverOptions): Promise<void>;
```

커서 위치를 선택된 요소로 이동합니다.

```ts
import { page } from "vitest/browser";

await page.getByRole("img", { name: "Rose" }).hover();
```

- 자세한 내용은 `userEvent.hover` 참고

### unhover

```ts
function unhover(options?: UserEventHoverOptions): Promise<void>;
```

이 메서드는 [`locator.hover`](#hover)와 동일하게 동작하지만, 대신 커서를 `document.body` 요소로 이동합니다.

```ts
import { page } from "vitest/browser";

await page.getByRole("img", { name: "Rose" }).unhover();
```

- 자세한 내용은 `userEvent.unhover` 참고

### fill

```ts
function fill(text: string, options?: UserEventFillOptions): Promise<void>;
```

현재 `input`, `textarea` 또는 `contenteditable` 요소의 값을 설정합니다.

```ts
import { page } from "vitest/browser";

await page.getByRole("input", { name: "Full Name" }).fill("Mr. Bean");
```

- 자세한 내용은 `userEvent.fill` 참고

### dropTo

```ts
function dropTo(
  target: Locator,
  options?: UserEventDragAndDropOptions,
): Promise<void>;
```

현재 요소를 대상 위치로 드래그합니다.

```ts
import { page } from "vitest/browser";

const paris = page.getByText("Paris");
const france = page.getByText("France");

await paris.dropTo(france);
```

- 자세한 내용은 `userEvent.dragAndDrop` 참고

### selectOptions

```ts
function selectOptions(
  values: HTMLElement | HTMLElement[] | Locator | Locator[] | string | string[],
  options?: UserEventSelectOptions,
): Promise<void>;
```

`<select>` 요소에서 하나 이상의 값을 선택합니다.

```ts
import { page } from "vitest/browser";

const languages = page.getByRole("select", { name: "Languages" });

await languages.selectOptions("EN");
await languages.selectOptions(["ES", "FR"]);
await languages.selectOptions([
  languages.getByRole("option", { name: "Spanish" }),
  languages.getByRole("option", { name: "French" }),
]);
```

- 자세한 내용은 `userEvent.selectOptions` 참고

### screenshot

```ts
function screenshot(
  options: LocatorScreenshotOptions & { save: false },
): Promise<string>;
function screenshot(
  options: LocatorScreenshotOptions & { base64: true },
): Promise<{
  path: string;
  base64: string;
}>;
function screenshot(
  options?: LocatorScreenshotOptions & { base64?: false },
): Promise<string>;
```

locator의 selector와 일치하는 요소의 스크린샷을 생성합니다.

`path` 옵션으로 스크린샷 저장 위치를 지정할 수 있으며, 현재 테스트 파일을 기준으로 한 상대 경로입니다. `path` 옵션을 설정하지 않으면 Vitest는 기본적으로 [`browser.screenshotDirectory`](https://vitest.dev/config/browser/screenshotdirectory) (기본값 `__screenshot__`)와 파일명 및 테스트명을 함께 사용해 스크린샷 파일 경로를 결정합니다.

스크린샷 콘텐츠도 함께 필요하다면 `base64: true`를 지정하여 스크린샷이 저장된 파일 경로와 함께 반환받을 수 있습니다.

```ts
import { page } from "vitest/browser";

const button = page.getByRole("button", { name: "Click Me!" });

const path = await button.screenshot();

const { path, base64 } = await button.screenshot({
  path: "./button-click-me.png",
  base64: true, // also return base64 string
});
// path - fullpath to the screenshot
// bas64 - base64 encoded string of the screenshot
```

::: warning WARNING 3.2.0
`screenshot`은 `save`가 `false`로 설정되면 항상 base64 문자열을 반환합니다.
이 경우 `path`도 무시됩니다.
:::

### query

```ts
function query(): Element | null;
```

이 메서드는 locator의 selector와 일치하는 단일 요소를 반환하며, 요소를 찾지 못하면 `null`을 반환합니다.

여러 요소가 selector와 일치하면 이 메서드는 오류를 발생시킵니다. 일치하는 모든 DOM Element가 필요하면 [`.elements()`](#elements)를 사용하고, selector와 일치하는 locator 배열이 필요하면 [`.all()`](#all)을 사용하세요.

다음 DOM 구조를 가정해 봅시다:

```html
<div>Hello <span>World</span></div>
<div>Hello</div>
```

다음 locator는 오류를 발생시키지 않습니다:

```ts
page.getByText("Hello World").query(); // ✅ HTMLDivElement
page.getByText("Hello Germany").query(); // ✅ null
page.getByText("World").query(); // ✅ HTMLSpanElement
page.getByText("Hello", { exact: true }).query(); // ✅ HTMLSpanElement
```

다음 locator는 오류를 발생시킵니다:

```ts
// returns multiple elements
page.getByText("Hello").query(); // ❌
page.getByText(/^Hello/).query(); // ❌
```

### element

```ts
function element(): Element;
```

이 메서드는 locator의 selector와 일치하는 단일 요소를 반환합니다.

selector와 일치하는 요소가 _하나도 없으면_ 오류가 발생합니다. 요소 존재 여부만 확인하려면 [`.query()`](#query)를 사용하는 것이 좋습니다.

selector와 일치하는 요소가 _여러 개면_ 오류가 발생합니다. 일치하는 모든 DOM Element가 필요하면 [`.elements()`](#elements)를 사용하고, selector와 일치하는 locator 배열이 필요하면 [`.all()`](#all)을 사용하세요.

::: tip
외부 라이브러리에 전달해야 할 때 이 메서드가 유용할 수 있습니다. assertion이 [재시도](https://vitest.dev/api/browser/assertions)될 때마다 locator가 `expect.element`와 함께 사용되면 자동으로 호출됩니다:

```ts
await expect.element(page.getByRole("button")).toBeDisabled();
```

:::

다음 DOM 구조를 가정해 봅시다:

```html
<div>Hello <span>World</span></div>
<div>Hello Germany</div>
<div>Hello</div>
```

다음 locator는 오류를 발생시키지 않습니다:

```ts
page.getByText("Hello World").element(); // ✅
page.getByText("Hello Germany").element(); // ✅
page.getByText("World").element(); // ✅
page.getByText("Hello", { exact: true }).element(); // ✅
```

다음 locator는 오류를 발생시킵니다:

```ts
// returns multiple elements
page.getByText("Hello").element(); // ❌
page.getByText(/^Hello/).element(); // ❌

// returns no elements
page.getByText("Hello USA").element(); // ❌
```

### elements

```ts
function elements(): Element[];
```

이 메서드는 locator의 selector와 일치하는 요소 배열을 반환합니다.

이 함수는 오류를 발생시키지 않습니다. selector와 일치하는 요소가 없으면 빈 배열을 반환합니다.

다음 DOM 구조를 가정해 봅시다:

```html
<div>Hello <span>World</span></div>
<div>Hello</div>
```

다음 locator는 항상 성공합니다:

```ts
page.getByText("Hello World").elements(); // ✅ [HTMLElement]
page.getByText("World").elements(); // ✅ [HTMLElement]
page.getByText("Hello", { exact: true }).elements(); // ✅ [HTMLElement]
page.getByText("Hello").elements(); // ✅ [HTMLElement, HTMLElement]
page.getByText("Hello USA").elements(); // ✅ []
```

### all

```ts
function all(): Locator[];
```

이 메서드는 selector와 일치하는 새 locator들의 배열을 반환합니다.

내부적으로 이 메서드는 `.elements`를 호출하고 각 요소를 [`page.elementLocator`](https://vitest.dev/api/browser/context#page)로 감쌉니다.

- [`locator.elements()`](#elements) 참고

## 속성

### selector

`selector`는 브라우저 provider가 요소를 찾는 데 사용하는 문자열입니다. Playwright는 `playwright` locator 문법을 사용하고, `preview`와 `webdriverio`는 CSS를 사용합니다.

::: danger
테스트 코드에서 이 문자열을 사용하면 안 됩니다. `selector` 문자열은 Commands API와 함께 작업할 때만 사용해야 합니다:

```ts [commands.ts]
import type { BrowserCommand } from "vitest/node";

const test: BrowserCommand<string> = function test(context, selector) {
  // playwright
  await context.iframe.locator(selector).click();
  // webdriverio
  await context.browser.$(selector).click();
};
```

```ts [example.test.ts]
import { test } from "vitest";
import { commands, page } from "vitest/browser";

test("works correctly", async () => {
  await commands.test(page.getByText("Hello").selector); // ✅
  // vitest will automatically unwrap it to a string
  await commands.test(page.getByText("Hello")); // ✅
});
```

:::

### length

이 getter는 이 locator가 매칭하는 요소 수를 반환합니다. `locator.elements().length`를 호출하는 것과 동일합니다.

다음 DOM 구조를 가정해 봅시다:

```html
<button>Click Me!</button> <button>Don't click me!</button>
```

이 속성은 항상 성공합니다:

```ts
page.getByRole("button").length; // ✅ 2
page.getByRole("button", { title: "Click Me!" }).length; // ✅ 1
page.getByRole("alert").length; // ✅ 0
```

## Custom Locators 3.2.0 advanced {#custom-locators}

locator factory 객체를 정의해 내장 locator API를 확장할 수 있습니다. 이 메서드들은 `page` 객체와 생성된 모든 locator의 메서드로 존재하게 됩니다.

내장 locator만으로 충분하지 않을 때 이러한 locator가 유용할 수 있습니다. 예를 들어 UI에 커스텀 프레임워크를 사용하는 경우입니다.

locator factory는 selector 문자열 또는 locator 자체를 반환해야 합니다.

::: tip
selector 문법은 Playwright locator와 동일합니다. 사용 방법을 더 잘 이해하려면 [가이드](https://playwright.dev/docs/other-locators)를 읽어보세요.
:::

```ts
import { locators } from "vitest/browser";

locators.extend({
  getByArticleTitle(title) {
    return `[data-title="${title}"]`;
  },
  getByArticleCommentsCount(count) {
    return `.comments :text("${count} comments")`;
  },
  async previewComments() {
    // you have access to the current locator via "this"
    // beware that if the method was called on `page`, `this` will be `page`,
    // not the locator!
    if (this !== page) {
      await this.click();
    }
    // ...
  },
});

// if you are using typescript, you can extend LocatorSelectors interface
// to have the autocompletion in locators.extend, page.* and locator.* methods
declare module "vitest/browser" {
  interface LocatorSelectors {
    // if the custom method returns a string, it will be converted into a locator
    // if it returns anything else, then it will be returned as usual
    getByArticleTitle(title: string): Locator;
    getByArticleCommentsCount(count: number): Locator;

    // Vitest will return a promise and won't try to convert it into a locator
    previewComments(this: Locator): Promise<void>;
  }
}
```

메서드가 전역 `page` 객체에서 호출되면 selector는 전체 페이지에 적용됩니다. 아래 예시에서 `getByArticleTitle`은 `data-title` 속성 값이 `title`인 모든 요소를 찾습니다. 하지만 메서드가 locator에서 호출되면 해당 locator 범위로 한정됩니다.

```html
<article data-title="Hello, World!">
  Hello, World!
  <button id="comments">2 comments</button>
</article>

<article data-title="Hello, Vitest!">
  Hello, Vitest!
  <button id="comments">0 comments</button>
</article>
```

```ts
const articles = page.getByRole("article");
const worldArticle = page.getByArticleTitle("Hello, World!"); // ✅
const commentsElement = worldArticle.getByArticleCommentsCount(2); // ✅
const wrongCommentsElement = worldArticle.getByArticleCommentsCount(0); // ❌
const wrongElement = page.getByArticleTitle("No Article!"); // ❌

await commentsElement.previewComments(); // ✅
await wrongCommentsElement.previewComments(); // ❌
```
