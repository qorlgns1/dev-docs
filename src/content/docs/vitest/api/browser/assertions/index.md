---
title: "Assertion API"
description: "Vitest는  라이브러리에서 포크한 다양한 DOM assertion을 기본으로 제공하며, locator 지원과 내장 재시도 기능이 추가되어 있습니다."
---

출처 URL: https://vitest.dev/api/browser/assertions

# Assertion API

Vitest는 [`@testing-library/jest-dom`](https://github.com/testing-library/jest-dom) 라이브러리에서 포크한 다양한 DOM assertion을 기본으로 제공하며, locator 지원과 내장 재시도 기능이 추가되어 있습니다.

::: tip TypeScript 지원
[TypeScript](https://vitest.dev/guide/browser/#typescript)를 사용 중이거나 `expect`에서 올바른 타입 힌트를 원한다면, 어딘가에서 `vitest/browser`를 참조하고 있는지 확인하세요. 해당 경로에서 한 번도 import하지 않았다면, `tsconfig.json`에 포함되는 아무 파일에나 `reference` 주석을 추가할 수 있습니다:

```ts
/// <reference types="vitest/browser" />
```

:::

브라우저에서 실행되는 테스트는 비동기적 특성 때문에 일관성 없이 실패할 수 있습니다. 따라서 조건 충족이 지연되더라도(예: 타임아웃, 네트워크 요청, 애니메이션) assertion이 성공하도록 보장할 방법이 중요합니다. 이를 위해 Vitest는 [`expect.poll`](https://vitest.dev/api/expect#poll) 및 `expect.element` API를 통해 재시도 가능한 assertion을 기본 제공합니다:

```ts
import { expect, test } from "vitest";
import { page } from "vitest/browser";

test("error banner is rendered", async () => {
  triggerError();

  // This creates a locator that will try to find the element
  // when any of its methods are called.
  // This call by itself doesn't check the existence of the element.
  const banner = page.getByRole("alert", {
    name: /error/i,
  });

  // Vitest provides `expect.element` with built-in retry-ability
  // It will repeatedly check that the element exists in the DOM and that
  // the content of `element.textContent` is equal to "Error!"
  // until all the conditions are met
  await expect.element(banner).toHaveTextContent("Error!");
});
```

`page.getBy*` locator와 함께 작업할 때는 테스트 flaky 현상을 줄이기 위해 항상 `expect.element`를 사용하는 것을 권장합니다. `expect.element`는 두 번째 옵션도 받는다는 점에 유의하세요:

```ts
interface ExpectPollOptions {
  // The interval to retry the assertion for in milliseconds
  // Defaults to "expect.poll.interval" config option
  interval?: number;
  // Time to retry the assertion for in milliseconds
  // Defaults to "expect.poll.timeout" config option
  timeout?: number;
  // The message printed when the assertion fails
  message?: string;
}
```

::: tip
`expect.element`는 `expect.poll(() => element)`의 축약형이며, 완전히 동일하게 동작합니다.

`toHaveTextContent` 및 다른 모든 assertion은 내장 재시도 메커니즘이 없는 일반 `expect`에서도 계속 사용할 수 있습니다:

```ts
// will fail immediately if .textContent is not `'Error!'`
expect(banner).toHaveTextContent("Error!");
```

:::

## toBeDisabled

```ts
function toBeDisabled(): Promise<void>;
```

사용자 관점에서 요소가 비활성화되었는지 확인할 수 있습니다.

요소가 form control이고 이 요소에 `disabled` 속성이 지정되어 있거나,
`disabled` 속성이 있는 form 요소의 자손 요소인 경우 매칭됩니다.

HTML `button`, `input`, `select`, `textarea`, `option`, `optgroup` 같은 네이티브 control 요소만
`disabled` 속성으로 비활성화할 수 있다는 점에 유의하세요. 다른 요소의 `disabled` 속성은 custom element가 아닌 한 무시됩니다.

```html
<button data-testid="button" type="submit" disabled>submit</button>
```

```ts
await expect.element(getByTestId("button")).toBeDisabled(); // ✅
await expect.element(getByTestId("button")).not.toBeDisabled(); // ❌
```

## toBeEnabled

```ts
function toBeEnabled(): Promise<void>;
```

사용자 관점에서 요소가 비활성화되지 않았는지 확인할 수 있습니다.

[`not.toBeDisabled()`](#tobedisabled)와 동일하게 동작합니다. 테스트에서 이중 부정을 피하려면 이 matcher를 사용하세요.

```html
<button data-testid="button" type="submit" disabled>submit</button>
```

```ts
await expect.element(getByTestId("button")).toBeEnabled(); // ✅
await expect.element(getByTestId("button")).not.toBeEnabled(); // ❌
```

## toBeEmptyDOMElement

```ts
function toBeEmptyDOMElement(): Promise<void>;
```

요소에 사용자에게 보이는 콘텐츠가 없는지 assertion할 수 있습니다. 주석은 무시하지만, 요소에 공백 문자가 포함되어 있으면 실패합니다.

```html
<span data-testid="not-empty"><span data-testid="empty"></span></span>
<span data-testid="with-whitespace"> </span>
<span data-testid="with-comment"><!-- comment --></span>
```

```ts
await expect.element(getByTestId("empty")).toBeEmptyDOMElement();
await expect.element(getByTestId("not-empty")).not.toBeEmptyDOMElement();
await expect.element(getByTestId("with-whitespace")).not.toBeEmptyDOMElement();
```

## toBeInTheDocument

```ts
function toBeInTheDocument(): Promise<void>;
```

요소가 문서에 존재하는지 여부를 assertion합니다.

```html
<svg data-testid="svg-element"></svg>
```

```ts
await expect.element(getByTestId("svg-element")).toBeInTheDocument();
await expect.element(getByTestId("does-not-exist")).not.toBeInTheDocument();
```

::: warning
이 matcher는 분리(detached)된 요소를 찾지 않습니다. `toBeInTheDocument`로 찾으려면 요소가 문서에 추가되어 있어야 합니다. 분리된 요소에서 검색하려면 [`toContainElement`](#tocontainelement)를 사용하세요.
:::

## toBeInvalid

```ts
function toBeInvalid(): Promise<void>;
```

요소가 현재 유효하지 않은지 확인할 수 있습니다.

요소는 [`aria-invalid` attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-invalid)가 값 없이 존재하거나 값이 `"true"`이거나, [`checkValidity()`](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation) 결과가 `false`인 경우 유효하지 않습니다.

```html
<input data-testid="no-aria-invalid" />
<input data-testid="aria-invalid" aria-invalid />
<input data-testid="aria-invalid-value" aria-invalid="true" />
<input data-testid="aria-invalid-false" aria-invalid="false" />

<form data-testid="valid-form">
  <input />
</form>

<form data-testid="invalid-form">
  <input required />
</form>
```

```ts
await expect.element(getByTestId("no-aria-invalid")).not.toBeInvalid();
await expect.element(getByTestId("aria-invalid")).toBeInvalid();
await expect.element(getByTestId("aria-invalid-value")).toBeInvalid();
await expect.element(getByTestId("aria-invalid-false")).not.toBeInvalid();

await expect.element(getByTestId("valid-form")).not.toBeInvalid();
await expect.element(getByTestId("invalid-form")).toBeInvalid();
```

## toBeRequired

```ts
function toBeRequired(): Promise<void>;
```

form 요소가 현재 필수인지 확인할 수 있습니다.

요소에 `required` 또는 `aria-required="true"` 속성이 있으면 필수 요소입니다.

```html
<input data-testid="required-input" required />
<input data-testid="aria-required-input" aria-required="true" />
<input data-testid="conflicted-input" required aria-required="false" />
<input data-testid="aria-not-required-input" aria-required="false" />
<input data-testid="optional-input" />
<input data-testid="unsupported-type" type="image" required />
<select data-testid="select" required></select>
<textarea data-testid="textarea" required></textarea>
<div data-testid="supported-role" role="tree" required></div>
<div data-testid="supported-role-aria" role="tree" aria-required="true"></div>
```

```ts
await expect.element(getByTestId("required-input")).toBeRequired();
await expect.element(getByTestId("aria-required-input")).toBeRequired();
await expect.element(getByTestId("conflicted-input")).toBeRequired();
await expect.element(getByTestId("aria-not-required-input")).not.toBeRequired();
await expect.element(getByTestId("optional-input")).not.toBeRequired();
await expect.element(getByTestId("unsupported-type")).not.toBeRequired();
await expect.element(getByTestId("select")).toBeRequired();
await expect.element(getByTestId("textarea")).toBeRequired();
await expect.element(getByTestId("supported-role")).not.toBeRequired();
await expect.element(getByTestId("supported-role-aria")).toBeRequired();
```

## toBeValid

```ts
function toBeValid(): Promise<void>;
```

요소의 값이 현재 유효한지 확인할 수 있습니다.

요소에 [`aria-invalid` attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-invalid)가 없거나 속성 값이 `"false"`이면 유효합니다. form 요소인 경우 [`checkValidity()`](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation) 결과도 `true`여야 합니다.

```html
<input data-testid="no-aria-invalid" />
<input data-testid="aria-invalid" aria-invalid />
<input data-testid="aria-invalid-value" aria-invalid="true" />
<input data-testid="aria-invalid-false" aria-invalid="false" />

<form data-testid="valid-form">
  <input />
</form>

<form data-testid="invalid-form">
  <input required />
</form>
```

```ts
await expect.element(getByTestId("no-aria-invalid")).toBeValid();
await expect.element(getByTestId("aria-invalid")).not.toBeValid();
await expect.element(getByTestId("aria-invalid-value")).not.toBeValid();
await expect.element(getByTestId("aria-invalid-false")).toBeValid();

await expect.element(getByTestId("valid-form")).toBeValid();
await expect.element(getByTestId("invalid-form")).not.toBeValid();
```

## toBeVisible

```ts
function toBeVisible(): Promise<void>;
```

요소가 현재 사용자에게 보이는지 확인할 수 있습니다.

요소는 bounding box가 비어 있지 않고, 계산된 스타일에 `visibility:hidden`이 없을 때 보이는 것으로 간주됩니다.

이 정의에 따르면:

- 크기가 0인 요소는 **보이는 것으로 간주되지 않습니다**.
- `display:none`인 요소는 **보이는 것으로 간주되지 않습니다**.
- `opacity:0`인 요소는 **보이는 것으로 간주됩니다**.

목록에서 최소 하나의 요소가 보이는지 확인하려면 `locator.first()`를 사용하세요.

```ts
// A specific element is visible.
await expect.element(page.getByText("Welcome")).toBeVisible();

// At least one item in the list is visible.
await expect.element(page.getByTestId("todo-item").first()).toBeVisible();

// At least one of the two elements is visible, possibly both.
await expect
  .element(
    page
      .getByRole("button", { name: "Sign in" })
      .or(page.getByRole("button", { name: "Sign up" }))
      .first(),
  )
  .toBeVisible();
```

## toBeInViewport 4.0.0 {#tobeinviewport}

```ts
function toBeInViewport(options: { ratio?: number }): Promise<void>;
```

[IntersectionObserver API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)를 사용해 요소가 현재 viewport 안에 있는지 확인할 수 있습니다.

옵션으로 `ratio` 인자를 전달할 수 있으며, 이는 요소가 viewport 안에 있어야 하는 최소 비율을 의미합니다. `ratio`는 0~1 범위여야 합니다.

```ts
// A specific element is in viewport.
await expect.element(page.getByText("Welcome")).toBeInViewport();

// 50% of a specific element should be in viewport
await expect.element(page.getByText("To")).toBeInViewport({ ratio: 0.5 });

// Full of a specific element should be in viewport
await expect.element(page.getByText("Vitest")).toBeInViewport({ ratio: 1 });
```

## toContainElement

```ts
function toContainElement(
  element: HTMLElement | SVGElement | Locator | null,
): Promise<void>;
```

요소가 다른 요소를 자손으로 포함하는지 여부를 assertion할 수 있습니다.

```html
<span data-testid="ancestor"><span data-testid="descendant"></span></span>
```

```ts
const ancestor = getByTestId("ancestor");
const descendant = getByTestId("descendant");
const nonExistantElement = getByTestId("does-not-exist");

await expect.element(ancestor).toContainElement(descendant);
await expect.element(descendant).not.toContainElement(ancestor);
await expect.element(ancestor).not.toContainElement(nonExistantElement);
```

## toContainHTML

```ts
function toContainHTML(htmlText: string): Promise<void>;
```

HTML 요소를 나타내는 문자열이 다른 요소 안에 포함되어 있는지 assertion합니다. 문자열은 유효한 html이어야 하며, 불완전한 html이면 안 됩니다.

```html
<span data-testid="parent"><span data-testid="child"></span></span>
```

```ts
// These are valid usages
await expect
  .element(getByTestId("parent"))
  .toContainHTML('<span data-testid="child"></span>');
await expect
  .element(getByTestId("parent"))
  .toContainHTML('<span data-testid="child" />');
await expect.element(getByTestId("parent")).not.toContainHTML("<br />");

// These won't work
await expect
  .element(getByTestId("parent"))
  .toContainHTML('data-testid="child"');
await expect.element(getByTestId("parent")).toContainHTML("data-testid");
await expect.element(getByTestId("parent")).toContainHTML("</span>");
```

::: warning
대부분의 경우 이 matcher를 사용할 필요가 없을 가능성이 높습니다. 브라우저에서 사용자가 앱을 인식하는 관점에서 테스트하는 것을 권장합니다. 그래서 특정 DOM 구조를 기준으로 테스트하는 것은 권장되지 않습니다.

테스트 대상 코드가 외부 소스에서 얻은 html을 렌더링하고, 해당 html 코드가 의도대로 사용되었는지 검증하려는 상황에서는 유용할 수 있습니다.

직접 제어하는 DOM 구조를 확인하는 용도로는 사용하면 안 됩니다. 대신 [`toContainElement`](#tocontainelement)를 사용하세요.
:::

## toHaveAccessibleDescription

```ts
function toHaveAccessibleDescription(
  description?: string | RegExp,
): Promise<void>;
```

요소가 기대한 [accessible description](https://w3c.github.io/accname/)을 가지는지 assertion할 수 있습니다.

기대한 accessible description의 정확한 문자열을 전달할 수도 있고,
정규식을 전달해 부분 일치를 수행하거나
[`expect.stringContaining`](https://vitest.dev/api/expect#expect-stringcontaining) 또는 [`expect.stringMatching`](https://vitest.dev/api/expect#expect-stringmatching)을 사용할 수도 있습니다.

```html
<a
  data-testid="link"
  href="/"
  aria-label="Home page"
  title="A link to start over"
  >Start</a
>
<a data-testid="extra-link" href="/about" aria-label="About page">About</a>
<img src="avatar.jpg" data-testid="avatar" alt="User profile pic" />
<img
  src="logo.jpg"
  data-testid="logo"
  alt="Company logo"
  aria-describedby="t1"
/>
<span id="t1" role="presentation">The logo of Our Company</span>
<img
  src="logo.jpg"
  data-testid="logo2"
  alt="Company logo"
  aria-description="The logo of Our Company"
/>
```

```ts
await expect.element(getByTestId("link")).toHaveAccessibleDescription();
await expect
  .element(getByTestId("link"))
  .toHaveAccessibleDescription("A link to start over");
await expect
  .element(getByTestId("link"))
  .not.toHaveAccessibleDescription("Home page");
await expect
  .element(getByTestId("extra-link"))
  .not.toHaveAccessibleDescription();
await expect.element(getByTestId("avatar")).not.toHaveAccessibleDescription();
await expect
  .element(getByTestId("logo"))
  .not.toHaveAccessibleDescription("Company logo");
await expect
  .element(getByTestId("logo"))
  .toHaveAccessibleDescription("The logo of Our Company");
await expect
  .element(getByTestId("logo2"))
  .toHaveAccessibleDescription("The logo of Our Company");
```

## toHaveAccessibleErrorMessage

```ts
function toHaveAccessibleErrorMessage(message?: string | RegExp): Promise<void>;
```

요소가 기대한 [accessible error message](https://w3c.github.io/aria/#aria-errormessage)를 가지는지 assertion할 수 있습니다.

기대한 accessible error message의 정확한 문자열을 전달할 수 있습니다.
또는 정규식을 전달하거나
[`expect.stringContaining`](https://vitest.dev/api/expect#expect-stringcontaining) 또는 [`expect.stringMatching`](https://vitest.dev/api/expect#expect-stringmatching)을 사용해 부분 일치를 수행할 수 있습니다.

```html
<input
  aria-label="Has Error"
  aria-invalid="true"
  aria-errormessage="error-message"
/>
<div id="error-message" role="alert">This field is invalid</div>

<input aria-label="No Error Attributes" />
<input
  aria-label="Not Invalid"
  aria-invalid="false"
  aria-errormessage="error-message"
/>
```

```ts
// Inputs with Valid Error Messages
await expect
  .element(getByRole("textbox", { name: "Has Error" }))
  .toHaveAccessibleErrorMessage();
await expect
  .element(getByRole("textbox", { name: "Has Error" }))
  .toHaveAccessibleErrorMessage("This field is invalid");
await expect
  .element(getByRole("textbox", { name: "Has Error" }))
  .toHaveAccessibleErrorMessage(/invalid/i);
await expect
  .element(getByRole("textbox", { name: "Has Error" }))
  .not.toHaveAccessibleErrorMessage("This field is absolutely correct!");

// Inputs without Valid Error Messages
await expect
  .element(getByRole("textbox", { name: "No Error Attributes" }))
  .not.toHaveAccessibleErrorMessage();

await expect
  .element(getByRole("textbox", { name: "Not Invalid" }))
  .not.toHaveAccessibleErrorMessage();
```

## toHaveAccessibleName

```ts
function toHaveAccessibleName(name?: string | RegExp): Promise<void>;
```

요소가 기대한 [accessible name](https://w3c.github.io/accname/)을 가지는지 assertion할 수 있습니다. 예를 들어 form 요소와 버튼에 올바른 라벨이 지정되었는지 확인할 때 유용합니다.

기대한 accessible name의 정확한 문자열을 전달할 수도 있고,
정규식을 전달해 부분 일치를 수행하거나
[`expect.stringContaining`](https://vitest.dev/api/expect#expect-stringcontaining) 또는 [`expect.stringMatching`](https://vitest.dev/api/expect#expect-stringmatching)을 사용할 수도 있습니다.

```html
<img data-testid="img-alt" src="" alt="Test alt" />
<img data-testid="img-empty-alt" src="" alt="" />
<svg data-testid="svg-title"><title>Test title</title></svg>
<button data-testid="button-img-alt"><img src="" alt="Test" /></button>
<p><img data-testid="img-paragraph" src="" alt="" /> Test content</p>
<button data-testid="svg-button"><svg><title>Test</title></svg></p>
<div><svg data-testid="svg-without-title"></svg></div>
<input data-testid="input-title" title="test" />
```

```javascript
await expect.element(getByTestId("img-alt")).toHaveAccessibleName("Test alt");
await expect.element(getByTestId("img-empty-alt")).not.toHaveAccessibleName();
await expect
  .element(getByTestId("svg-title"))
  .toHaveAccessibleName("Test title");
await expect.element(getByTestId("button-img-alt")).toHaveAccessibleName();
await expect.element(getByTestId("img-paragraph")).not.toHaveAccessibleName();
await expect.element(getByTestId("svg-button")).toHaveAccessibleName();
await expect
  .element(getByTestId("svg-without-title"))
  .not.toHaveAccessibleName();
await expect.element(getByTestId("input-title")).toHaveAccessibleName();
```

## toHaveAttribute

```ts
function toHaveAttribute(attribute: string, value?: unknown): Promise<void>;
```

주어진 요소에 특정 속성이 있는지 확인할 수 있습니다. 또한 선택적으로 해당 속성이 기대하는 특정 값을 갖는지, 또는 [`expect.stringContaining`](https://vitest.dev/api/expect#expect-stringcontaining)이나 [`expect.stringMatching`](https://vitest.dev/api/expect#expect-stringmatching)을 사용한 부분 일치인지도 확인할 수 있습니다.

```html
<button data-testid="ok-button" type="submit" disabled>ok</button>
```

```ts
const button = getByTestId("ok-button");

await expect.element(button).toHaveAttribute("disabled");
await expect.element(button).toHaveAttribute("type", "submit");
await expect.element(button).not.toHaveAttribute("type", "button");

await expect
  .element(button)
  .toHaveAttribute("type", expect.stringContaining("sub"));
await expect
  .element(button)
  .toHaveAttribute("type", expect.not.stringContaining("but"));
```

## toHaveClass

```ts
function toHaveClass(
  ...classNames: string[],
  options?: { exact: boolean },
): Promise<void>;
function toHaveClass(...classNames: (string | RegExp)[]): Promise<void>;
```

주어진 요소가 `class` 속성 안에 특정 클래스들을 가지고 있는지 확인할 수 있습니다. 요소에 클래스가 전혀 없음을 assertion하는 경우를 제외하면, 최소 하나의 클래스를 제공해야 합니다.

클래스 이름 목록에는 문자열과 정규식을 포함할 수 있습니다. 정규식은 대상 요소의 각 개별 클래스에 대해 매칭되며, 전체 `class` 속성 값을 하나로 묶어 매칭하는 것이 아닙니다.

::: warning
정규식만 제공된 경우에는 `exact: true` 옵션을 사용할 수 없습니다.
:::

```html
<button data-testid="delete-button" class="btn extra btn-danger">
  Delete item
</button>
<button data-testid="no-classes">No Classes</button>
```

```ts
const deleteButton = getByTestId("delete-button");
const noClasses = getByTestId("no-classes");

await expect.element(deleteButton).toHaveClass("extra");
await expect.element(deleteButton).toHaveClass("btn-danger btn");
await expect.element(deleteButton).toHaveClass(/danger/, "btn");
await expect.element(deleteButton).toHaveClass("btn-danger", "btn");
await expect.element(deleteButton).not.toHaveClass("btn-link");
await expect.element(deleteButton).not.toHaveClass(/link/);

// ⚠️ regexp matches against individual classes, not the whole classList
await expect.element(deleteButton).not.toHaveClass(/btn extra/);

// the element has EXACTLY a set of classes (in any order)
await expect.element(deleteButton).toHaveClass("btn-danger extra btn", {
  exact: true,
});
// if it has more than expected it is going to fail
await expect.element(deleteButton).not.toHaveClass("btn-danger extra", {
  exact: true,
});

await expect.element(noClasses).not.toHaveClass();
```

## toHaveFocus

```ts
function toHaveFocus(): Promise<void>;
```

요소가 포커스를 가지고 있는지 여부를 assertion할 수 있습니다.

```html
<div><input type="text" data-testid="element-to-focus" /></div>
```

```ts
const input = page.getByTestId("element-to-focus");
input.element().focus();
await expect.element(input).toHaveFocus();
input.element().blur();
await expect.element(input).not.toHaveFocus();
```

## toHaveFormValues

```ts
function toHaveFormValues(
  expectedValues: Record<string, unknown>,
): Promise<void>;
```

form 또는 fieldset에 주어진 각 name에 대한 form control이 존재하고, 지정한 값을 가지는지 확인할 수 있습니다.

::: tip
이 matcher는 [form](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement) 또는 [fieldset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFieldSetElement) 요소에서만 호출할 수 있다는 점을 강조하는 것이 중요합니다.

이 덕분에 `form`과 `fieldset`의 [`.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements) 속성을 활용해, 내부의 모든 form control을 신뢰성 있게 가져올 수 있습니다.

또한 사용자가 둘 이상의 `form`을 포함한 컨테이너를 전달해 서로 관련 없는 form control이 섞이거나, 심지어 서로 충돌하는 상황도 방지할 수 있습니다.
:::

이 matcher는 form control 유형에 따라 값이 얻어지는 방식의 차이를 추상화합니다.
예를 들어 `<input>` 요소에는 `value` 속성이 있지만 `<select>` 요소에는 없습니다.
다음은 지원되는 모든 경우의 목록입니다:

- `<input type="number">` 요소는 문자열 대신 값을 **number**로 반환합니다.
- `<input type="checkbox">` 요소:
  - 주어진 `name` 속성을 가진 항목이 하나뿐이면 **boolean**으로 처리되어,
    체크되어 있으면 `true`, 아니면 `false`를 반환합니다.
  - 같은 `name` 속성을 가진 체크박스가 여러 개면,
    이들은 하나의 form control로 집합 처리되며,
    해당 컬렉션에서 선택된 체크박스들의 값을 모두 담은 **array**를 반환합니다.
- `<input type="radio">` 요소는 `name` 속성으로 모두 그룹화되며,
  이 그룹은 하나의 form control로 처리됩니다. 이 form control은
  그룹 내에서 선택된 라디오 버튼의 `value` 속성에 해당하는 **string** 값을 반환합니다.
- `<input type="text">` 요소는 값을 **string**으로 반환합니다. 이는 위의 다른 규칙에서 명시적으로 다루지 않은 다른 `type` 속성을 가진 `<input>` 요소(예: `search`, `email`, `date`, `password`, `hidden` 등)에도 적용됩니다.
- `multiple` 속성이 없는 `<select>` 요소는 선택된 `option`의 `value` 속성에 해당하는 **string** 값을 반환하며, 선택된 option이 없으면 `undefined`를 반환합니다.
- `<select multiple>` 요소는 [selected options](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/selectedOptions)의 모든 값을 담은 **array**를 반환합니다.
- `<textarea>` 요소는 값을 **string**으로 반환합니다. 이 값은 해당 노드의 콘텐츠에 대응합니다.

위 규칙 덕분에 예를 들어 단일 select control을 라디오 버튼 그룹으로 바꾸거나,
멀티 select control을 체크박스 그룹으로 바꾸는 작업이 쉬워집니다.
이 matcher가 비교에 사용하는 최종 form 값 집합은 동일하게 유지됩니다.

```html
<form data-testid="login-form">
  <input type="text" name="username" value="jane.doe" />
  <input type="password" name="password" value="12345678" />
  <input type="checkbox" name="rememberMe" checked />
  <button type="submit">Sign in</button>
</form>
```

```ts
await expect.element(getByTestId("login-form")).toHaveFormValues({
  username: "jane.doe",
  rememberMe: true,
});
```

## toHaveStyle

```ts
function toHaveStyle(css: string | Partial<CSSStyleDeclaration>): Promise<void>;
```

특정 요소에 특정 값이 적용된 css 속성이 있는지 확인할 수 있습니다.
요소에 기대한 속성 중 일부가 아니라, _모든_ 기대 속성이 적용되어 있어야만 일치합니다.

```html
<button
  data-testid="delete-button"
  style="display: none; background-color: red"
>
  Delete item
</button>
```

```ts
const button = getByTestId("delete-button");

await expect.element(button).toHaveStyle("display: none");
await expect.element(button).toHaveStyle({ display: "none" });
await expect.element(button).toHaveStyle(`
  background-color: red;
  display: none;
`);
await expect.element(button).toHaveStyle({
  backgroundColor: "red",
  display: "none",
});
await expect.element(button).not.toHaveStyle(`
  background-color: blue;
  display: none;
`);
await expect.element(button).not.toHaveStyle({
  backgroundColor: "blue",
  display: "none",
});
```

현재 문서에서 활성화된 스타일시트에 정의된 클래스 이름을 통해 요소에 적용된 규칙에도 동일하게 동작합니다.
일반적인 css 우선순위 규칙이 적용됩니다.

## toHaveTextContent

```ts
function toHaveTextContent(
  text: string | RegExp,
  options?: { normalizeWhitespace: boolean },
): Promise<void>;
```

주어진 노드에 텍스트 콘텐츠가 있는지 확인할 수 있습니다.
요소뿐 아니라 텍스트 노드와 프래그먼트도 지원합니다.

`string` 인수를 전달하면 노드 콘텐츠에 대해 대소문자를 구분하는 부분 일치를 수행합니다.

대소문자를 구분하지 않는 일치를 수행하려면 `/i` 수정자가 있는 `RegExp`를 사용할 수 있습니다.

전체 콘텐츠를 일치시키고 싶다면 `RegExp`를 사용하면 됩니다.

```html
<span data-testid="text-content">Text Content</span>
```

```ts
const element = getByTestId("text-content");

await expect.element(element).toHaveTextContent("Content");
// to match the whole content
await expect.element(element).toHaveTextContent(/^Text Content$/);
// to use case-insensitive match
await expect.element(element).toHaveTextContent(/content$/i);
await expect.element(element).not.toHaveTextContent("content");
```

## toHaveValue

```ts
function toHaveValue(value: string | string[] | number | null): Promise<void>;
```

주어진 폼 요소가 지정한 값을 가지는지 확인할 수 있습니다.
`<input>`, `<select>`, `<textarea>` 요소를 허용하지만, `<input type="checkbox">`와 `<input type="radio">`는 예외이며, 이러한 요소는 [`toBeChecked`](#tobechecked) 또는 [`toHaveFormValues`](#tohaveformvalues)로만 의미 있게 매칭할 수 있습니다.

또한 역할이 `meter`, `progressbar`, `slider`, `spinbutton`인 요소도 허용하며, 해당 요소의 `aria-valuenow` 속성(숫자)을 확인합니다.

그 외 모든 폼 요소의 경우, 값은 [`toHaveFormValues`](#tohaveformvalues)와 동일한 알고리즘으로 매칭됩니다.

```html
<input type="text" value="text" data-testid="input-text" />
<input type="number" value="5" data-testid="input-number" />
<input type="text" data-testid="input-empty" />
<select multiple data-testid="select-number">
  <option value="first">First Value</option>
  <option value="second" selected>Second Value</option>
  <option value="third" selected>Third Value</option>
</select>
```

```ts
const textInput = getByTestId("input-text");
const numberInput = getByTestId("input-number");
const emptyInput = getByTestId("input-empty");
const selectInput = getByTestId("select-number");

await expect.element(textInput).toHaveValue("text");
await expect.element(numberInput).toHaveValue(5);
await expect.element(emptyInput).not.toHaveValue();
await expect.element(selectInput).toHaveValue(["second", "third"]);
```

## toHaveDisplayValue

```typescript
function toHaveDisplayValue(
  value: string | RegExp | (string | RegExp)[],
): Promise<void>;
```

주어진 폼 요소가 지정한 표시 값(최종 사용자가 보게 되는 값)을 가지는지 확인할 수 있습니다.
`<input>`, `<select>`, `<textarea>` 요소를 허용하지만, `<input type="checkbox">`와 `<input type="radio">`는 예외이며, 이러한 요소는 [`toBeChecked`](#tobechecked) 또는 [`toHaveFormValues`](#tohaveformvalues)로만 의미 있게 매칭할 수 있습니다.

```html
<label for="input-example">First name</label>
<input type="text" id="input-example" value="Luca" />

<label for="textarea-example">Description</label>
<textarea id="textarea-example">An example description here.</textarea>

<label for="single-select-example">Fruit</label>
<select id="single-select-example">
  <option value="">Select a fruit...</option>
  <option value="banana">Banana</option>
  <option value="ananas">Ananas</option>
  <option value="avocado">Avocado</option>
</select>

<label for="multiple-select-example">Fruits</label>
<select id="multiple-select-example" multiple>
  <option value="">Select a fruit...</option>
  <option value="banana" selected>Banana</option>
  <option value="ananas">Ananas</option>
  <option value="avocado" selected>Avocado</option>
</select>
```

```ts
const input = page.getByLabelText("First name");
const textarea = page.getByLabelText("Description");
const selectSingle = page.getByLabelText("Fruit");
const selectMultiple = page.getByLabelText("Fruits");

await expect.element(input).toHaveDisplayValue("Luca");
await expect.element(input).toHaveDisplayValue(/Luc/);
await expect
  .element(textarea)
  .toHaveDisplayValue("An example description here.");
await expect.element(textarea).toHaveDisplayValue(/example/);
await expect.element(selectSingle).toHaveDisplayValue("Select a fruit...");
await expect.element(selectSingle).toHaveDisplayValue(/Select/);
await expect.element(selectMultiple).toHaveDisplayValue([/Avocado/, "Banana"]);
```

## toBeChecked

```ts
function toBeChecked(): Promise<void>;
```

주어진 요소가 체크되어 있는지 확인할 수 있습니다.
`checkbox` 또는 `radio` 타입의 `input`, 그리고 유효한 `aria-checked` 속성 값 `"true"` 또는 `"false"`를 가진 `checkbox`, `radio`, `switch` 역할의 요소를 허용합니다.

```html
<input type="checkbox" checked data-testid="input-checkbox-checked" />
<input type="checkbox" data-testid="input-checkbox-unchecked" />
<div role="checkbox" aria-checked="true" data-testid="aria-checkbox-checked" />
<div
  role="checkbox"
  aria-checked="false"
  data-testid="aria-checkbox-unchecked"
/>

<input type="radio" checked value="foo" data-testid="input-radio-checked" />
<input type="radio" value="foo" data-testid="input-radio-unchecked" />
<div role="radio" aria-checked="true" data-testid="aria-radio-checked" />
<div role="radio" aria-checked="false" data-testid="aria-radio-unchecked" />
<div role="switch" aria-checked="true" data-testid="aria-switch-checked" />
<div role="switch" aria-checked="false" data-testid="aria-switch-unchecked" />
```

```ts
const inputCheckboxChecked = getByTestId("input-checkbox-checked");
const inputCheckboxUnchecked = getByTestId("input-checkbox-unchecked");
const ariaCheckboxChecked = getByTestId("aria-checkbox-checked");
const ariaCheckboxUnchecked = getByTestId("aria-checkbox-unchecked");
await expect.element(inputCheckboxChecked).toBeChecked();
await expect.element(inputCheckboxUnchecked).not.toBeChecked();
await expect.element(ariaCheckboxChecked).toBeChecked();
await expect.element(ariaCheckboxUnchecked).not.toBeChecked();

const inputRadioChecked = getByTestId("input-radio-checked");
const inputRadioUnchecked = getByTestId("input-radio-unchecked");
const ariaRadioChecked = getByTestId("aria-radio-checked");
const ariaRadioUnchecked = getByTestId("aria-radio-unchecked");
await expect.element(inputRadioChecked).toBeChecked();
await expect.element(inputRadioUnchecked).not.toBeChecked();
await expect.element(ariaRadioChecked).toBeChecked();
await expect.element(ariaRadioUnchecked).not.toBeChecked();

const ariaSwitchChecked = getByTestId("aria-switch-checked");
const ariaSwitchUnchecked = getByTestId("aria-switch-unchecked");
await expect.element(ariaSwitchChecked).toBeChecked();
await expect.element(ariaSwitchUnchecked).not.toBeChecked();
```

## toBePartiallyChecked

```typescript
function toBePartiallyChecked(): Promise<void>;
```

주어진 요소가 부분 체크 상태인지 확인할 수 있습니다.
`checkbox` 타입의 `input`, `aria-checked="mixed"`를 가진 `checkbox` 역할의 요소, 또는 `indeterminate`가 `true`로 설정된 `checkbox` 타입의 `input`을 허용합니다.

```html
<input type="checkbox" aria-checked="mixed" data-testid="aria-checkbox-mixed" />
<input type="checkbox" checked data-testid="input-checkbox-checked" />
<input type="checkbox" data-testid="input-checkbox-unchecked" />
<div role="checkbox" aria-checked="true" data-testid="aria-checkbox-checked" />
<div
  role="checkbox"
  aria-checked="false"
  data-testid="aria-checkbox-unchecked"
/>
<input type="checkbox" data-testid="input-checkbox-indeterminate" />
```

```ts
const ariaCheckboxMixed = getByTestId("aria-checkbox-mixed");
const inputCheckboxChecked = getByTestId("input-checkbox-checked");
const inputCheckboxUnchecked = getByTestId("input-checkbox-unchecked");
const ariaCheckboxChecked = getByTestId("aria-checkbox-checked");
const ariaCheckboxUnchecked = getByTestId("aria-checkbox-unchecked");
const inputCheckboxIndeterminate = getByTestId("input-checkbox-indeterminate");

await expect.element(ariaCheckboxMixed).toBePartiallyChecked();
await expect.element(inputCheckboxChecked).not.toBePartiallyChecked();
await expect.element(inputCheckboxUnchecked).not.toBePartiallyChecked();
await expect.element(ariaCheckboxChecked).not.toBePartiallyChecked();
await expect.element(ariaCheckboxUnchecked).not.toBePartiallyChecked();

inputCheckboxIndeterminate.element().indeterminate = true;
await expect.element(inputCheckboxIndeterminate).toBePartiallyChecked();
```

## toHaveRole

```ts
function toHaveRole(role: ARIARole): Promise<void>;
```

요소가 기대한 [role](https://www.w3.org/TR/html-aria/#docconformance)을 가지는지 단언할 수 있습니다.

역할 자체가 아닌 다른 쿼리로 이미 요소에 접근한 상태에서, 접근성 관련 추가 단언을 하고 싶을 때 유용합니다.

role은 명시적 role(`role` 속성)과 [암시적 ARIA 시맨틱](https://www.w3.org/TR/html-aria/#docconformance)을 통한 암시적 role 모두 일치할 수 있습니다.

```html
<button data-testid="button">Continue</button>
<div role="button" data-testid="button-explicit">Continue</button>
<button role="switch button" data-testid="button-explicit-multiple">Continue</button>
<a href="/about" data-testid="link">About</a>
<a data-testid="link-invalid">Invalid link<a/>
```

```ts
await expect.element(getByTestId("button")).toHaveRole("button");
await expect.element(getByTestId("button-explicit")).toHaveRole("button");
await expect
  .element(getByTestId("button-explicit-multiple"))
  .toHaveRole("button");
await expect
  .element(getByTestId("button-explicit-multiple"))
  .toHaveRole("switch");
await expect.element(getByTestId("link")).toHaveRole("link");
await expect.element(getByTestId("link-invalid")).not.toHaveRole("link");
await expect.element(getByTestId("link-invalid")).toHaveRole("generic");
```

::: warning
role은 ARIA role 계층 구조 상속 없이 문자열 동등성으로 그대로 매칭됩니다. 따라서 `checkbox` 같은 상위 role을 쿼리해도 `switch` 같은 하위 role 요소는 포함되지 않습니다.

또한 `testing-library`와 달리, Vitest는 Playwright의 동작을 따라 첫 번째 유효한 role을 제외한 모든 사용자 정의 role을 무시합니다:

```jsx
<div data-testid="switch" role="switch alert"></div>;

await expect.element(getByTestId("switch")).toHaveRole("switch"); // ✅
await expect.element(getByTestId("switch")).toHaveRole("alert"); // ❌
```

:::

## toHaveSelection

```ts
function toHaveSelection(selection?: string): Promise<void>;
```

요소가 [text selection](https://developer.mozilla.org/en-US/docs/Web/API/Selection)을 가지는지 단언할 수 있습니다.

요소 내부에서 텍스트 전체 또는 일부가 선택되었는지 확인할 때 유용합니다.
요소는 텍스트 타입 input, textarea, 또는 paragraph/span/div처럼 텍스트를 포함하는 다른 어떤 요소여도 됩니다.

::: warning
기대 selection은 문자열이며, selection 범위 인덱스는 확인할 수 없습니다.
:::

```html
<div>
  <input type="text" value="text selected text" data-testid="text" />
  <textarea data-testid="textarea">text selected text</textarea>
  <p data-testid="prev">prev</p>
  <p data-testid="parent">
    text <span data-testid="child">selected</span> text
  </p>
  <p data-testid="next">next</p>
</div>
```

```ts
getByTestId("text").element().setSelectionRange(5, 13);
await expect.element(getByTestId("text")).toHaveSelection("selected");

getByTestId("textarea").element().setSelectionRange(0, 5);
await expect.element("textarea").toHaveSelection("text ");

const selection = document.getSelection();
const range = document.createRange();
selection.removeAllRanges();
selection.empty();
selection.addRange(range);

// selection of child applies to the parent as well
range.selectNodeContents(getByTestId("child").element());
await expect.element(getByTestId("child")).toHaveSelection("selected");
await expect.element(getByTestId("parent")).toHaveSelection("selected");

// selection that applies from prev all, parent text before child, and part child.
range.setStart(getByTestId("prev").element(), 0);
range.setEnd(getByTestId("child").element().childNodes[0], 3);
await expect.element(queryByTestId("prev")).toHaveSelection("prev");
await expect.element(queryByTestId("child")).toHaveSelection("sel");
await expect.element(queryByTestId("parent")).toHaveSelection("text sel");
await expect.element(queryByTestId("next")).not.toHaveSelection();

// selection that applies from part child, parent text after child and part next.
range.setStart(getByTestId("child").element().childNodes[0], 3);
range.setEnd(getByTestId("next").element().childNodes[0], 2);
await expect.element(queryByTestId("child")).toHaveSelection("ected");
await expect.element(queryByTestId("parent")).toHaveSelection("ected text");
await expect.element(queryByTestId("prev")).not.toHaveSelection();
await expect.element(queryByTestId("next")).toHaveSelection("ne");
```

## toMatchScreenshot experimental {#tomatchscreenshot}

```ts
function toMatchScreenshot(options?: ScreenshotMatcherOptions): Promise<void>;
function toMatchScreenshot(
  name?: string,
  options?: ScreenshotMatcherOptions,
): Promise<void>;
```

::: tip
`toMatchScreenshot` 단언은 [Vitest config](https://vitest.dev/config/browser/expect#tomatchscreenshot)에서 전역 설정할 수 있습니다.
:::

이 단언을 사용하면 요소 또는 페이지의 스크린샷을 저장된 참조 이미지와 비교하여 시각적 회귀 테스트를 수행할 수 있습니다.

설정된 임계값을 초과하는 차이가 감지되면 테스트가 실패합니다.
변경 사항을 파악할 수 있도록 이 단언은 다음을 생성합니다:

- 테스트 중 캡처된 실제 스크린샷
- 기대하는 참조 스크린샷
- 차이점을 강조한 diff 이미지(가능한 경우)

::: warning Screenshots Stability
이 단언은 연속으로 두 번 같은 결과가 나올 때까지 스크린샷 촬영을 자동으로 재시도합니다.
이렇게 하면 애니메이션, 로딩 상태, 기타 동적 콘텐츠로 인한 플래키 현상을 줄일 수 있습니다.
이 동작은 `timeout` 옵션으로 제어할 수 있습니다.

하지만 브라우저 렌더링은 다음 환경에 따라 달라질 수 있습니다:

- 브라우저 및 브라우저 버전 차이
- 운영체제(Windows, macOS, Linux)
- 화면 해상도 및 픽셀 밀도
- GPU 드라이버 및 하드웨어 가속
- 폰트 렌더링 및 시스템 폰트

이 테스트 전략을 효율적으로 구현하려면 [Visual Regression Testing guide](https://vitest.dev/guide/browser/visual-regression-testing)를 읽는 것을 권장합니다.
:::

::: tip
의도된 변경으로 인해 스크린샷 비교가 실패한 경우, watch 모드에서 `u` 키를 누르거나 `-u` 또는 `--update` 플래그로 테스트를 실행해 참조 스크린샷을 업데이트할 수 있습니다.
:::

```html
<button data-testid="button">Fancy Button</button>
```

```ts
// basic usage, auto-generates screenshot name
await expect.element(getByTestId("button")).toMatchScreenshot();

// with custom name
await expect.element(getByTestId("button")).toMatchScreenshot("fancy-button");

// with options
await expect.element(getByTestId("button")).toMatchScreenshot({
  comparatorName: "pixelmatch",
  comparatorOptions: {
    allowedMismatchedPixelRatio: 0.01,
  },
});

// with both name and options
await expect.element(getByTestId("button")).toMatchScreenshot("fancy-button", {
  comparatorName: "pixelmatch",
  comparatorOptions: {
    allowedMismatchedPixelRatio: 0.01,
  },
});
```

### Options

- `comparatorName: "pixelmatch" = "pixelmatch"`

  이미지 비교에 사용하는 알고리즘/라이브러리 이름입니다.

  현재는 [`"pixelmatch"`](https://github.com/mapbox/pixelmatch)만 지원됩니다.

- `comparatorOptions: object`

  이 옵션으로 comparator의 동작을 변경할 수 있습니다.
  설정 가능한 속성은 선택한 comparator 알고리즘에 따라 달라집니다.

  Vitest는 기본값을 제공하지만, 재정의할 수 있습니다.
  - [`"pixelmatch"` options](#pixelmatch-comparator-options)

  ::: warning
  `comparatorOptions`에 대해 올바른 타입 추론을 얻으려면 **반드시 `comparatorName`을 명시적으로 설정하세요**.

  그렇지 않으면 TypeScript는 어떤 옵션이 유효한지 알 수 없습니다:

  ```ts
  // ❌ TypeScript can't infer the correct options
  await expect.element(button).toMatchScreenshot({
    comparatorOptions: {
      // might error when new comparators are added
      allowedMismatchedPixelRatio: 0.01,
    },
  });

  // ✅ TypeScript knows these are pixelmatch options
  await expect.element(button).toMatchScreenshot({
    comparatorName: "pixelmatch",
    comparatorOptions: {
      allowedMismatchedPixelRatio: 0.01,
    },
  });
  ```

  :::

- `screenshotOptions: object`

  [`locator.screenshot()`](https://vitest.dev/api/browser/locators.html#screenshot)에서 허용하는 옵션과 동일하지만, 다음은 제외됩니다:
  - `'base64'`
  - `'path'`
  - `'save'`
  - `'type'`

- `timeout: number = 5_000`

  안정적인 스크린샷을 찾을 때까지 기다리는 시간입니다.

  이 값을 `0`으로 설정하면 타임아웃이 비활성화되지만, 안정적인 스크린샷을 결정할 수 없는 경우 프로세스가 종료되지 않습니다.

#### `"pixelmatch"` comparator options

`"pixelmatch"` comparator를 사용할 때 다음 옵션을 사용할 수 있습니다:

- `allowedMismatchedPixelRatio: number | undefined = undefined`

  캡처된 스크린샷과 참조 이미지 간에 서로 다른 픽셀 비율의 최대 허용치입니다.

  `0`에서 `1` 사이 값이어야 합니다.

  예를 들어 `allowedMismatchedPixelRatio: 0.02`는 최대 2% 픽셀 차이까지는 테스트가 통과하고, 2%를 초과하면 실패함을 의미합니다.

- `allowedMismatchedPixels: number | undefined = undefined`

  캡처된 스크린샷과 저장된 참조 이미지 간에 서로 다를 수 있는 픽셀 수의 최대 허용치입니다.

  `undefined`로 설정하면 0이 아닌 모든 차이에서 테스트가 실패합니다.

  예를 들어 `allowedMismatchedPixels: 10`은 10픽셀 이하 차이는 통과하고, 11픽셀 이상 차이 나면 실패함을 의미합니다.

- `threshold: number = 0.1`

  두 이미지의 동일한 픽셀 간 허용되는 지각 색상 차이입니다.

  값 범위는 `0`(엄격)에서 `1`(매우 관대)입니다.
  값이 낮을수록 작은 차이도 감지됩니다.

  비교에는 [YIQ color space](https://en.wikipedia.org/wiki/YIQ)를 사용합니다.

- `includeAA: boolean = false`

  `true`이면 안티앨리어싱 픽셀의 감지 및 무시를 비활성화합니다.

- `alpha: number = 0.1`

  diff 이미지에서 변경되지 않은 픽셀의 블렌딩 수준입니다.

  `0`(흰색)에서 `1`(원래 밝기) 범위입니다.

- `aaColor: [r: number, g: number, b: number] = [255, 255, 0]`

  diff 이미지에서 안티앨리어싱 픽셀에 사용하는 색상입니다.

- `diffColor: [r: number, g: number, b: number] = [255, 0, 0]`

  diff 이미지에서 서로 다른 픽셀에 사용하는 색상입니다.

- `diffColorAlt: [r: number, g: number, b: number] | undefined = undefined`

  밝은 배경 위 어두운 차이에 대해, 추가된 부분과 제거된 부분을 더 잘 구분하기 위한 선택적 대체 색상입니다.

  설정하지 않으면 모든 차이에 `diffColor`가 사용됩니다.

- `diffMask: boolean = false`

  `true`이면 원본 이미지 위에 오버레이하지 않고, 투명 배경 위에 diff만 마스크로 표시합니다.

  안티앨리어싱 픽셀은(감지된 경우) 표시되지 않습니다.

::: warning
`allowedMismatchedPixels`와 `allowedMismatchedPixelRatio`를 모두 설정하면, 더 엄격한 값이 사용됩니다.

예를 들어 100픽셀 또는 2% 비율을 허용하고 이미지가 10,000픽셀이라면, 유효 한도는 200픽셀이 아니라 100픽셀이 됩니다.
:::
