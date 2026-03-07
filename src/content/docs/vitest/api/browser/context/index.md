---
title: "Context API"
description: "Vitest는  엔트리 포인트를 통해 context 모듈을 제공합니다. 2.0부터 테스트에서 유용할 수 있는 소규모 유틸리티 집합을 제공합니다."
---

출처 URL: https://vitest.dev/api/browser/context

# Context API

Vitest는 `vitest/browser` 엔트리 포인트를 통해 context 모듈을 제공합니다. 2.0부터 테스트에서 유용할 수 있는 소규모 유틸리티 집합을 제공합니다.

## `userEvent`

::: tip
`userEvent` API는 [Interactivity API](https://vitest.dev/api/browser/interactivity)에서 자세히 설명합니다.
:::

```ts
/**
 * Handler for user interactions. The support is implemented by the browser provider (`playwright` or `webdriverio`).
 * If used with `preview` provider, fallbacks to simulated events via `@testing-library/user-event`.
 * @experimental
 */
export const userEvent: {
  setup: () => UserEvent;
  cleanup: () => Promise<void>;
  click: (element: Element, options?: UserEventClickOptions) => Promise<void>;
  dblClick: (
    element: Element,
    options?: UserEventDoubleClickOptions,
  ) => Promise<void>;
  tripleClick: (
    element: Element,
    options?: UserEventTripleClickOptions,
  ) => Promise<void>;
  selectOptions: (
    element: Element,
    values: HTMLElement | HTMLElement[] | string | string[],
    options?: UserEventSelectOptions,
  ) => Promise<void>;
  keyboard: (text: string) => Promise<void>;
  type: (
    element: Element,
    text: string,
    options?: UserEventTypeOptions,
  ) => Promise<void>;
  clear: (element: Element) => Promise<void>;
  tab: (options?: UserEventTabOptions) => Promise<void>;
  hover: (element: Element, options?: UserEventHoverOptions) => Promise<void>;
  unhover: (element: Element, options?: UserEventHoverOptions) => Promise<void>;
  fill: (
    element: Element,
    text: string,
    options?: UserEventFillOptions,
  ) => Promise<void>;
  dragAndDrop: (
    source: Element,
    target: Element,
    options?: UserEventDragAndDropOptions,
  ) => Promise<void>;
};
```

## `commands`

::: tip
이 API는 [Commands API](https://vitest.dev/api/browser/commands)에서 자세히 설명합니다.
:::

```ts
/**
 * Available commands for the browser.
 * A shortcut to `server.commands`.
 */
export const commands: BrowserCommands;
```

## `page`

`page` export는 현재 `page`와 상호작용할 수 있는 유틸리티를 제공합니다.

::: warning
Playwright의 `page`에서 일부 유틸리티를 노출하긴 하지만, 동일한 객체는 아닙니다. 브라우저 컨텍스트는 브라우저에서 평가되므로, 테스트는 서버에서 실행되는 Playwright의 `page`에 접근할 수 없습니다.

Playwright의 `page` 객체에 접근해야 한다면 [Commands API](https://vitest.dev/api/browser/commands)를 사용하세요.
:::

```ts
export const page: {
  /**
   * Change the size of iframe's viewport.
   */
  viewport(width: number, height: number): Promise<void>;
  /**
   * Make a screenshot of the test iframe or a specific element.
   * @returns Path to the screenshot file or path and base64.
   */
  screenshot(
    options: Omit<ScreenshotOptions, "base64"> & { base64: true },
  ): Promise<{
    path: string;
    base64: string;
  }>;
  screenshot(options?: ScreenshotOptions): Promise<string>;
  /**
   * Extend default `page` object with custom methods.
   */
  extend(methods: Partial<BrowserPage>): BrowserPage;
  /**
   * Wrap an HTML element in a `Locator`. When querying for elements, the search will always return this element.
   */
  elementLocator(element: Element): Locator;
  /**
   * The iframe locator. This is a document locator that enters the iframe body
   * and works similarly to the `page` object.
   * **Warning:** At the moment, this is supported only by the `playwright` provider.
   */
  frameLocator(iframeElement: Locator): FrameLocator;

  /**
   * Locator APIs. See its documentation for more details.
   */
  getByRole(role: ARIARole | string, options?: LocatorByRoleOptions): Locator;
  getByLabelText(text: string | RegExp, options?: LocatorOptions): Locator;
  getByTestId(text: string | RegExp): Locator;
  getByAltText(text: string | RegExp, options?: LocatorOptions): Locator;
  getByPlaceholder(text: string | RegExp, options?: LocatorOptions): Locator;
  getByText(text: string | RegExp, options?: LocatorOptions): Locator;
  getByTitle(text: string | RegExp, options?: LocatorOptions): Locator;
};
```

::: tip
`getBy*` API는 [Locators API](https://vitest.dev/api/browser/locators)에서 설명합니다.
:::

::: warning WARNING 3.2.0
`screenshot`은 `save`가 `false`로 설정된 경우 항상 base64 문자열을 반환합니다.
이 경우 `path`도 무시됩니다.
:::

### frameLocator

```ts
function frameLocator(iframeElement: Locator): FrameLocator;
```

`frameLocator` 메서드는 iframe 내부 요소를 찾는 데 사용할 수 있는 `FrameLocator` 인스턴스를 반환합니다.

frame locator는 `page`와 유사합니다. Iframe HTML 요소 자체를 참조하는 것이 아니라 iframe의 document를 참조합니다.

```ts
const frame = page.frameLocator(page.getByTestId("iframe"));

await frame.getByText("Hello World").click(); // ✅
await frame.click(); // ❌ Not available
```

::: danger IMPORTANT
현재 `frameLocator` 메서드는 `playwright` provider에서만 지원됩니다.

`click`이나 `fill` 같은 상호작용 메서드는 iframe 내부 요소에서 항상 사용할 수 있지만, `expect.element`를 사용한 assertion은 iframe이 [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)를 충족해야 합니다.
:::

## `cdp`

```ts
function cdp(): CDPSession;
```

`cdp` export는 현재 Chrome DevTools Protocol 세션을 반환합니다. 주로 이를 기반으로 도구를 구축하는 라이브러리 작성자에게 유용합니다.

::: warning
CDP 세션은 `playwright` provider에서만 동작하며, `chromium` 브라우저를 사용할 때만 지원됩니다. 자세한 내용은 playwright의 [`CDPSession`](https://playwright.dev/docs/api/class-cdpsession) 문서를 참고하세요.
:::

```ts
export const cdp: () => CDPSession;
```

## `server`

`server` export는 Vitest 서버가 실행 중인 Node.js 환경을 나타냅니다. 주로 디버깅하거나 환경에 따라 테스트를 제한할 때 유용합니다.

```ts
export const server: {
  /**
   * Platform the Vitest server is running on.
   * The same as calling `process.platform` on the server.
   */
  platform: Platform;
  /**
   * Runtime version of the Vitest server.
   * The same as calling `process.version` on the server.
   */
  version: string;
  /**
   * Name of the browser provider.
   */
  provider: string;
  /**
   * Name of the current browser.
   */
  browser: string;
  /**
   * Available commands for the browser.
   */
  commands: BrowserCommands;
  /**
   * Serialized test config.
   */
  config: SerializedConfig;
};
```

## `utils`

커스텀 렌더 라이브러리에 유용한 유틸리티 함수입니다.

```ts
export const utils: {
  /**
   * This is simillar to calling `page.elementLocator`, but it returns only
   * locator selectors.
   */
  getElementLocatorSelectors(element: Element): LocatorSelectors;
  /**
   * Prints prettified HTML of an element.
   */
  debug(
    el?: Element | Locator | null | (Element | Locator)[],
    maxLength?: number,
    options?: PrettyDOMOptions,
  ): void;
  /**
   * Returns prettified HTML of an element.
   */
  prettyDOM(
    dom?: Element | Locator | undefined | null,
    maxLength?: number,
    prettyFormatOptions?: PrettyDOMOptions,
  ): string;
  /**
   * Configures default options of `prettyDOM` and `debug` functions.
   * This will also affect `vitest-browser-{framework}` package.
   * @experimental
   */
  configurePrettyDOM(options: StringifyOptions): void;
  /**
   * Creates "Cannot find element" error. Useful for custom locators.
   */
  getElementError(selector: string, container?: Element): Error;
};
```
