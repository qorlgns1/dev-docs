---
title: "상호작용 API"
description: "Vitest는 이벤트를 가짜로 발생시키는 대신 Chrome DevTools Protocol 또는 webdriver를 사용해  API의 일부를 구현합니다. 이 방식은 브라우저 동작을 더 신뢰성 있게 만들고, 사용자가 페이지와 상호작용하는 방식과 더 일관되게 동작합니다."
---

출처 URL: https://vitest.dev/api/browser/interactivity

# 상호작용 API

Vitest는 이벤트를 가짜로 발생시키는 대신 [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) 또는 [webdriver](https://www.w3.org/TR/webdriver/)를 사용해 [`@testing-library/user-event`](https://testing-library.com/docs/user-event/intro) API의 일부를 구현합니다. 이 방식은 브라우저 동작을 더 신뢰성 있게 만들고, 사용자가 페이지와 상호작용하는 방식과 더 일관되게 동작합니다.

```ts
import { userEvent } from "vitest/browser";

await userEvent.click(document.querySelector(".button"));
```

거의 모든 `userEvent` 메서드는 provider 옵션을 상속합니다.

## userEvent.setup

```ts
function setup(): UserEvent;
```

새 user event 인스턴스를 생성합니다. 키보드 상태를 유지해 버튼 누름/해제를 정확히 처리해야 할 때 유용합니다.

::: warning
`@testing-library/user-event`와 달리, `vitest/browser`의 기본 `userEvent` 인스턴스는 메서드가 호출될 때마다 생성되지 않고 한 번만 생성됩니다. 동작 차이는 아래 스니펫에서 확인할 수 있습니다.

```ts
import { userEvent as vitestUserEvent } from "vitest/browser";
import { userEvent as originalUserEvent } from "@testing-library/user-event";

await vitestUserEvent.keyboard("{Shift}"); // press shift without releasing
await vitestUserEvent.keyboard("{/Shift}"); // releases shift

await originalUserEvent.keyboard("{Shift}"); // press shift without releasing
await originalUserEvent.keyboard("{/Shift}"); // DID NOT release shift because the state is different
```

이 동작은 키보드를 에뮬레이션하지 않고 실제로 Shift를 누르는 방식이기 때문에 더 유용합니다. 기존 동작을 유지하면 필드 입력 시 예상치 못한 문제가 생길 수 있습니다.
:::

## userEvent.click

```ts
function click(
  element: Element | Locator,
  options?: UserEventClickOptions,
): Promise<void>;
```

요소를 클릭합니다. provider 옵션을 상속합니다. 이 메서드의 동작 방식에 대한 자세한 설명은 사용하는 provider 문서를 참고하세요.

```ts
import { page, userEvent } from "vitest/browser";

test("clicks on an element", async () => {
  const logo = page.getByRole("img", { name: /logo/ });

  await userEvent.click(logo);
  // or you can access it directly on the locator
  await logo.click();

  // With WebdriverIO, this uses either ElementClick (with no arguments) or
  // actions (with arguments). Use an empty object to force the use of actions.
  await logo.click({});
});
```

### 보조 키와 함께 클릭하기

WebdriverIO 또는 Playwright 사용 시:

```ts
await userEvent.keyboard("{Shift>}");
// By using an empty object as the option, this opts in to using a chain of actions
// instead of an ElementClick in webdriver.
// Firefox has a bug that makes this necessary.
// Follow https://bugzilla.mozilla.org/show_bug.cgi?id=1456642 to know when this
// will be fixed.
await userEvent.click(element, {});
await userEvent.keyboard("{/Shift}");
```

Playwright 사용 시:

```ts
await userEvent.click(element, { modifiers: ["Shift"] });
```

참고 자료:

- Playwright `locator.click` API
- WebdriverIO `element.click` API
- testing-library `click` API

## userEvent.dblClick

```ts
function dblClick(
  element: Element | Locator,
  options?: UserEventDoubleClickOptions,
): Promise<void>;
```

요소에서 더블 클릭 이벤트를 발생시킵니다.

이 메서드의 동작 방식에 대한 자세한 설명은 사용하는 provider 문서를 참고하세요.

```ts
import { page, userEvent } from "vitest/browser";

test("triggers a double click on an element", async () => {
  const logo = page.getByRole("img", { name: /logo/ });

  await userEvent.dblClick(logo);
  // or you can access it directly on the locator
  await logo.dblClick();
});
```

참고 자료:

- Playwright `locator.dblclick` API
- WebdriverIO `element.doubleClick` API
- testing-library `dblClick` API

## userEvent.tripleClick

```ts
function tripleClick(
  element: Element | Locator,
  options?: UserEventTripleClickOptions,
): Promise<void>;
```

요소에서 트리플 클릭 이벤트를 발생시킵니다. 브라우저 API에는 `tripleclick`이 없으므로, 이 메서드는 click 이벤트를 연속으로 세 번 발생시킵니다. 따라서 이벤트를 필터링하려면 [click event detail](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event#usage_notes)을 확인해야 합니다: `evt.detail === 3`.

이 메서드의 동작 방식에 대한 자세한 설명은 사용하는 provider 문서를 참고하세요.

```ts
import { page, userEvent } from "vitest/browser";

test("triggers a triple click on an element", async () => {
  const logo = page.getByRole("img", { name: /logo/ });
  let tripleClickFired = false;
  logo.addEventListener("click", (evt) => {
    if (evt.detail === 3) {
      tripleClickFired = true;
    }
  });

  await userEvent.tripleClick(logo);
  // or you can access it directly on the locator
  await logo.tripleClick();

  expect(tripleClickFired).toBe(true);
});
```

참고 자료:

- [Playwright `locator.click` API](https://playwright.dev/docs/api/class-locator#locator-click): `clickCount: 3` 옵션을 사용한 `click`으로 구현됩니다.
- [WebdriverIO `browser.action` API](https://webdriver.io/docs/api/browser/action/): `move`와 연속된 세 번의 `down + up + pause` 이벤트를 조합한 actions API로 구현됩니다.
- testing-library `tripleClick` API

## userEvent.fill

```ts
function fill(element: Element | Locator, text: string): Promise<void>;
```

`input`/`textarea`/`contenteditable` 필드에 값을 설정합니다. 새 값을 설정하기 전에 기존 입력 텍스트를 제거합니다.

```ts
import { page, userEvent } from "vitest/browser";

test("update input", async () => {
  const input = page.getByRole("input");

  await userEvent.fill(input, "foo"); // input.value == foo
  await userEvent.fill(input, "{{a[["); // input.value == {{a[[
  await userEvent.fill(input, "{Shift}"); // input.value == {Shift}

  // or you can access it directly on the locator
  await input.fill("foo"); // input.value == foo
});
```

이 메서드는 요소에 포커스를 주고 값을 채운 뒤, 채우기 완료 후 `input` 이벤트를 발생시킵니다. 빈 문자열을 사용해 필드를 비울 수 있습니다.

::: tip
이 API는 [`userEvent.type`](#userevent-type) 또는 [`userEvent.keyboard`](#userevent-keyboard)보다 빠르지만, [user-event `keyboard` syntax](https://testing-library.com/docs/user-event/keyboard) (예: `{Shift}{selectall}`)는 **지원하지 않습니다**.

특수 문자 입력이 필요 없거나 keypress 이벤트를 세밀하게 제어할 필요가 없는 경우에는 [`userEvent.type`](#userevent-type)보다 이 API 사용을 권장합니다.
:::

참고 자료:

- Playwright `locator.fill` API
- WebdriverIO `element.setValue` API
- testing-library `type` API

## userEvent.keyboard

```ts
function keyboard(text: string): Promise<void>;
```

`userEvent.keyboard`는 키보드 입력을 발생시킬 수 있게 해줍니다. 포커스된 입력 요소가 있으면 해당 입력에 문자를 입력합니다. 그렇지 않으면 현재 포커스된 요소(포커스된 요소가 없으면 `document.body`)에서 키보드 이벤트를 발생시킵니다.

이 API는 [user-event `keyboard` syntax](https://testing-library.com/docs/user-event/keyboard)를 지원합니다.

```ts
import { userEvent } from "vitest/browser";

test("trigger keystrokes", async () => {
  await userEvent.keyboard("foo"); // translates to: f, o, o
  await userEvent.keyboard("{{a[["); // translates to: {, a, [
  await userEvent.keyboard("{Shift}{f}{o}{o}"); // translates to: Shift, f, o, o
  await userEvent.keyboard("{a>5}"); // press a without releasing it and trigger 5 keydown
  await userEvent.keyboard("{a>5/}"); // press a for 5 keydown and then release it
});
```

참고 자료:

- Playwright `Keyboard` API
- WebdriverIO `action('key')` API
- testing-library `type` API

## userEvent.tab

```ts
function tab(options?: UserEventTabOptions): Promise<void>;
```

`Tab` 키 이벤트를 전송합니다. `userEvent.keyboard('{tab}')`의 축약형입니다.

```ts
import { page, userEvent } from "vitest/browser";

test("tab works", async () => {
  const [input1, input2] = page.getByRole("input").elements();

  expect(input1).toHaveFocus();

  await userEvent.tab();

  expect(input2).toHaveFocus();

  await userEvent.tab({ shift: true });

  expect(input1).toHaveFocus();
});
```

참고 자료:

- Playwright `Keyboard` API
- WebdriverIO `action('key')` API
- testing-library `tab` API

## userEvent.type

```ts
function type(
  element: Element | Locator,
  text: string,
  options?: UserEventTypeOptions,
): Promise<void>;
```

::: warning
[special characters](https://testing-library.com/docs/user-event/keyboard) (예: `{shift}` 또는 `{selectall}`)에 의존하지 않는다면, 성능 향상을 위해 대신 [`userEvent.fill`](#userevent-fill) 사용을 권장합니다.
:::

`type` 메서드는 [`keyboard`](https://testing-library.com/docs/user-event/keyboard) API를 기반으로 구축된 `@testing-library/user-event`의 [`type`](https://testing-library.com/docs/user-event/utility/#type) 유틸리티를 구현합니다.

이 함수는 `input`/`textarea`/`contenteditable` 요소에 문자를 입력할 수 있게 해줍니다. [user-event `keyboard` syntax](https://testing-library.com/docs/user-event/keyboard)를 지원합니다.

입력 요소 없이 단순히 문자 키만 누르려면 [`userEvent.keyboard`](#userevent-keyboard) API를 사용하세요.

```ts
import { page, userEvent } from "vitest/browser";

test("update input", async () => {
  const input = page.getByRole("input");

  await userEvent.type(input, "foo"); // input.value == foo
  await userEvent.type(input, "{{a[["); // input.value == foo{a[
  await userEvent.type(input, "{Shift}"); // input.value == foo{a[
});
```

::: info
Vitest는 `userEvent` 라이브러리와의 호환성을 위해서만 존재하는 기능이므로 locator의 `.type` 메서드(`input.type` 같은 형태)를 노출하지 않습니다. 더 빠른 `.fill` 사용을 고려하세요.
:::

참고 자료:

- Playwright `locator.press` API
- WebdriverIO `action('key')` API
- testing-library `type` API

## userEvent.clear

```ts
function clear(
  element: Element | Locator,
  options?: UserEventClearOptions,
): Promise<void>;
```

이 메서드는 input 요소의 내용을 비웁니다.

```ts
import { page, userEvent } from "vitest/browser";

test("clears input", async () => {
  const input = page.getByRole("input");

  await userEvent.fill(input, "foo");
  expect(input).toHaveValue("foo");

  await userEvent.clear(input);
  // or you can access it directly on the locator
  await input.clear();

  expect(input).toHaveValue("");
});
```

참고 자료:

- Playwright `locator.clear` API
- WebdriverIO `element.clearValue` API
- testing-library `clear` API

## userEvent.selectOptions

```ts
function selectOptions(
  element: Element | Locator,
  values: HTMLElement | HTMLElement[] | Locator | Locator[] | string | string[],
  options?: UserEventSelectOptions,
): Promise<void>;
```

`userEvent.selectOptions`를 사용하면 `<select>` 요소에서 값을 선택할 수 있습니다.

::: warning
select 요소에 [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select#attr-multiple) 속성이 없으면, Vitest는 배열에서 첫 번째 요소만 선택합니다.

`@testing-library`와 달리, Vitest는 현재 [listbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/listbox_role)를 지원하지 않지만 향후 지원을 추가할 계획입니다.
:::

```ts
import { page, userEvent } from "vitest/browser";

test("clears input", async () => {
  const select = page.getByRole("select");

  await userEvent.selectOptions(select, "Option 1");
  // or you can access it directly on the locator
  await select.selectOptions("Option 1");

  expect(select).toHaveValue("option-1");

  await userEvent.selectOptions(select, "option-1");
  expect(select).toHaveValue("option-1");

  await userEvent.selectOptions(select, [
    page.getByRole("option", { name: "Option 1" }),
    page.getByRole("option", { name: "Option 2" }),
  ]);
  expect(select).toHaveValue(["option-1", "option-2"]);
});
```

::: warning
`webdriverio` provider는 다중 선택을 위한 API를 제공하지 않기 때문에 여러 요소 선택을 지원하지 않습니다.
:::

참고 자료:

- Playwright `locator.selectOption` API
- WebdriverIO `element.selectByIndex` API
- testing-library `selectOptions` API

## userEvent.hover

```ts
function hover(
  element: Element | Locator,
  options?: UserEventHoverOptions,
): Promise<void>;
```

이 메서드는 커서 위치를 선택된 요소로 이동합니다. 이 메서드의 동작 방식에 대한 자세한 설명은 사용하는 provider 문서를 참고하세요.

::: warning
`webdriverio` provider를 사용하는 경우, 기본적으로 커서는 요소의 중심으로 이동합니다.

`playwright` provider를 사용하는 경우, 커서는 요소의 보이는 지점 중 "어딘가"로 이동합니다.
:::

```ts
import { page, userEvent } from "vitest/browser";

test("hovers logo element", async () => {
  const logo = page.getByRole("img", { name: /logo/ });

  await userEvent.hover(logo);
  // or you can access it directly on the locator
  await logo.hover();
});
```

참고 자료:

- Playwright `locator.hover` API
- WebdriverIO `element.moveTo` API
- testing-library `hover` API

## userEvent.unhover

```ts
function unhover(
  element: Element | Locator,
  options?: UserEventHoverOptions,
): Promise<void>;
```

이 메서드는 [`userEvent.hover`](#userevent-hover)와 동일하게 동작하지만, 커서를 `document.body` 요소로 이동시킵니다.

::: warning
기본적으로 커서 위치는 body 요소의 "보이는 어딘가"(`playwright` provider) 또는 중심(`webdriverio` provider)입니다. 따라서 현재 hover된 요소가 이미 같은 위치에 있으면 이 메서드는 효과가 없습니다.
:::

```ts
import { page, userEvent } from "vitest/browser";

test("unhover logo element", async () => {
  const logo = page.getByRole("img", { name: /logo/ });

  await userEvent.unhover(logo);
  // or you can access it directly on the locator
  await logo.unhover();
});
```

참고 자료:

- Playwright `locator.hover` API
- WebdriverIO `element.moveTo` API
- testing-library `hover` API

## userEvent.upload

```ts
function upload(
  element: Element | Locator,
  files: string[] | string | File[] | File,
  options?: UserEventUploadOptions,
): Promise<void>;
```

파일 input 요소를 변경해 지정한 파일들을 갖도록 합니다.

```ts
import { page, userEvent } from "vitest/browser";

test("can upload a file", async () => {
  const input = page.getByRole("button", { name: /Upload files/ });

  const file = new File(["file"], "file.png", { type: "image/png" });

  await userEvent.upload(input, file);
  // or you can access it directly on the locator
  await input.upload(file);

  // you can also use file paths relative to the root of the project
  await userEvent.upload(input, "./fixtures/file.png");
});
```

::: warning
`webdriverio` provider는 `chrome` 및 `edge` 브라우저에서만 이 명령을 지원합니다. 또한 현재는 문자열 타입만 지원합니다.
:::

참고 자료:

- Playwright `locator.setInputFiles` API
- WebdriverIO `browser.uploadFile` API
- testing-library `upload` API

## userEvent.dragAndDrop

```ts
function dragAndDrop(
  source: Element | Locator,
  target: Element | Locator,
  options?: UserEventDragAndDropOptions,
): Promise<void>;
```

source 요소를 target 요소 위로 드래그합니다. `source` 요소에는 `draggable` 속성이 `true`로 설정되어 있어야 합니다.

```ts
import { page, userEvent } from "vitest/browser";

test("drag and drop works", async () => {
  const source = page.getByRole("img", { name: /logo/ });
  const target = page.getByTestId("logo-target");

  await userEvent.dragAndDrop(source, target);
  // or you can access it directly on the locator
  await source.dropTo(target);

  await expect.element(target).toHaveTextContent("Logo is processed");
});
```

::: warning
이 API는 기본 `preview` provider에서 지원되지 않습니다.
:::

참고 자료:

- Playwright `frame.dragAndDrop` API
- WebdriverIO `element.dragAndDrop` API

## userEvent.copy

```ts
function copy(): Promise<void>;
```

선택한 텍스트를 클립보드에 복사합니다.

```js
import { page, userEvent } from "vitest/browser";

test("copy and paste", async () => {
  // write to 'source'
  await userEvent.click(page.getByPlaceholder("source"));
  await userEvent.keyboard("hello");

  // select and copy 'source'
  await userEvent.dblClick(page.getByPlaceholder("source"));
  await userEvent.copy();

  // paste to 'target'
  await userEvent.click(page.getByPlaceholder("target"));
  await userEvent.paste();

  await expect
    .element(page.getByPlaceholder("source"))
    .toHaveTextContent("hello");
  await expect
    .element(page.getByPlaceholder("target"))
    .toHaveTextContent("hello");
});
```

참고 자료:

- testing-library `copy` API

## userEvent.cut

```ts
function cut(): Promise<void>;
```

선택한 텍스트를 클립보드로 잘라냅니다.

```js
import { page, userEvent } from "vitest/browser";

test("copy and paste", async () => {
  // write to 'source'
  await userEvent.click(page.getByPlaceholder("source"));
  await userEvent.keyboard("hello");

  // select and cut 'source'
  await userEvent.dblClick(page.getByPlaceholder("source"));
  await userEvent.cut();

  // paste to 'target'
  await userEvent.click(page.getByPlaceholder("target"));
  await userEvent.paste();

  await expect.element(page.getByPlaceholder("source")).toHaveTextContent("");
  await expect
    .element(page.getByPlaceholder("target"))
    .toHaveTextContent("hello");
});
```

참고 자료:

- testing-library `cut` API

## userEvent.paste

```ts
function paste(): Promise<void>;
```

클립보드의 텍스트를 붙여넣습니다. 사용 예시는 [`userEvent.copy`](#userevent-copy) 및 [`userEvent.cut`](#userevent-cut)을 참고하세요.

참고 자료:

- testing-library `paste` API
