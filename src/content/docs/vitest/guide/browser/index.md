---
title: "Browser Mode {#browser-mode}"
description: "이 페이지는 Vitest API의 브라우저 모드 기능에 대한 정보를 제공합니다. 이 기능을 사용하면 테스트를 브라우저에서 네이티브로 실행할 수 있으며, 와  같은 브라우저 전역 객체에 접근할 수 있습니다."
---

출처 URL: https://vitest.dev/guide/browser

# Browser Mode {#browser-mode}

이 페이지는 Vitest API의 브라우저 모드 기능에 대한 정보를 제공합니다. 이 기능을 사용하면 테스트를 브라우저에서 네이티브로 실행할 수 있으며, `window`와 `document` 같은 브라우저 전역 객체에 접근할 수 있습니다.

::: tip
`expect`, `vi`, 또는 테스트 프로젝트나 타입 테스트 같은 일반 API 문서를 찾고 있다면 ["Getting Started" guide](https://vitest.dev/guide/)를 참고하세요.
:::

## Installation

더 쉽게 설정하려면 `vitest init browser` 명령을 사용해 필요한 의존성을 설치하고 브라우저 설정을 만들 수 있습니다.

::: code-group

```bash [npm]
npx vitest init browser
```

```bash [yarn]
yarn exec vitest init browser
```

```bash [pnpm]
pnpx vitest init browser
```

```bash [bun]
bunx vitest init browser
```

:::

### Manual Installation

패키지를 수동으로 설치할 수도 있습니다. Vitest는 항상 provider가 정의되어 있어야 합니다. [`preview`](https://vitest.dev/config/browser/preview), [`playwright`](https://vitest.dev/config/browser/playwright), [`webdriverio`](https://vitest.dev/config/browser/webdriverio) 중 하나를 선택할 수 있습니다.

테스트가 어떻게 보이는지만 미리 확인하려면 `preview` provider를 사용할 수 있습니다:

::: code-group

```bash [npm]
npm install -D vitest @vitest/browser-preview
```

```bash [yarn]
yarn add -D vitest @vitest/browser-preview
```

```bash [pnpm]
pnpm add -D vitest @vitest/browser-preview
```

```bash [bun]
bun add -D vitest @vitest/browser-preview
```

:::

::: warning
하지만 CI에서 테스트를 실행하려면 [`playwright`](https://npmjs.com/package/playwright) 또는 [`webdriverio`](https://www.npmjs.com/package/webdriverio) 중 하나를 설치해야 합니다. 기본 `preview` provider는 Chrome DevTools Protocol을 사용하는 대신 이벤트 시뮬레이션에 의존하므로, 로컬 테스트에서도 이를 계속 사용하기보다는 두 provider 중 하나로 전환하는 것을 권장합니다.

아직 이 도구들 중 하나도 사용하지 않는다면, 병렬 실행을 지원해 테스트를 더 빠르게 실행할 수 있는 Playwright로 시작하는 것을 권장합니다.

::: tabs key:provider
== Playwright
[Playwright](https://npmjs.com/package/playwright)는 웹 테스트 및 자동화를 위한 프레임워크입니다.

::: code-group

```bash [npm]
npm install -D vitest @vitest/browser-playwright
```

```bash [yarn]
yarn add -D vitest @vitest/browser-playwright
```

```bash [pnpm]
pnpm add -D vitest @vitest/browser-playwright
```

```bash [bun]
bun add -D vitest @vitest/browser-playwright
```

== WebdriverIO

[WebdriverIO](https://www.npmjs.com/package/webdriverio)는 WebDriver 프로토콜을 사용해 로컬에서 테스트를 실행할 수 있게 해줍니다.

::: code-group

```bash [npm]
npm install -D vitest @vitest/browser-webdriverio
```

```bash [yarn]
yarn add -D vitest @vitest/browser-webdriverio
```

```bash [pnpm]
pnpm add -D vitest @vitest/browser-webdriverio
```

```bash [bun]
bun add -D vitest @vitest/browser-webdriverio
```

:::

## Configuration

Vitest 설정에서 브라우저 모드를 활성화하려면, Vitest 설정 파일에서 `browser.enabled` 필드를 `true`로 설정하세요. 아래는 browser 필드를 사용한 설정 예시입니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      enabled: true,
      // at least one instance is required
      instances: [{ browser: "chromium" }],
    },
  },
});
```

::: info
Vitest는 개발 서버와의 충돌을 피하기 위해 `63315` 포트를 할당하므로, 둘을 병렬로 실행할 수 있습니다. 이 값은 [`browser.api`](https://vitest.dev/config/#browser-api) 옵션으로 변경할 수 있습니다.

CLI는 Vite 서버 URL을 자동으로 출력하지 않습니다. watch 모드에서 실행 중일 때 "b"를 누르면 URL을 출력할 수 있습니다.
:::

아직 Vite를 사용해 본 적이 없다면, 프레임워크 플러그인이 설치되어 있고 설정에 지정되어 있는지 확인하세요. 일부 프레임워크는 동작을 위해 추가 설정이 필요할 수 있으므로 관련 Vite 문서를 확인하는 것이 좋습니다.

::: code-group

```ts [react]
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  plugins: [react()],
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

```ts [vue]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

```ts [svelte]
import { defineConfig } from "vitest/config";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  plugins: [svelte()],
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

```ts [solid]
import { defineConfig } from "vitest/config";
import solidPlugin from "vite-plugin-solid";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  plugins: [solidPlugin()],
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

```ts [marko]
import { defineConfig } from "vitest/config";
import marko from "@marko/vite";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  plugins: [marko()],
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

```ts [qwik]
import { defineConfig } from "vitest/config";
import { qwikVite } from "@builder.io/qwik/optimizer";
import { playwright } from "@vitest/browser-playwright";

// optional, run the tests in SSR mode
import { testSSR } from "vitest-browser-qwik/ssr-plugin";

export default defineConfig({
  plugins: [testSSR(), qwikVite()],
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

:::

일부 테스트를 Node 기반 runner로 실행해야 한다면, 테스트 전략별로 설정을 분리한 [`projects`](https://vitest.dev/guide/projects) 옵션을 정의할 수 있습니다:

{#projects-config}

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    projects: [
      {
        test: {
          // an example of file based convention,
          // you don't have to follow it
          include: [
            "tests/unit/**/*.{test,spec}.ts",
            "tests/**/*.unit.{test,spec}.ts",
          ],
          name: "unit",
          environment: "node",
        },
      },
      {
        test: {
          // an example of file based convention,
          // you don't have to follow it
          include: [
            "tests/browser/**/*.{test,spec}.ts",
            "tests/**/*.browser.{test,spec}.ts",
          ],
          name: "browser",
          browser: {
            enabled: true,
            provider: playwright(),
            instances: [{ browser: "chromium" }],
          },
        },
      },
    ],
  },
});
```

## Browser Option Types

Vitest의 browser 옵션은 provider에 따라 달라집니다. `--browser`를 전달했지만 설정 파일에 해당 이름을 지정하지 않으면 Vitest는 실패합니다. 사용 가능한 옵션은 다음과 같습니다:

- `webdriverio`는 다음 브라우저를 지원합니다:
  - `firefox`
  - `chrome`
  - `edge`
  - `safari`
- `playwright`는 다음 브라우저를 지원합니다:
  - `firefox`
  - `webkit`
  - `chromium`

## Browser Compatibility

Vitest는 테스트 실행에 [Vite dev server](https://vitejs.dev/guide/#browser-support)를 사용하므로, [`esbuild.target`](https://vitejs.dev/config/shared-options.html#esbuild) 옵션(기본값 `esnext`)에 지정된 기능만 지원합니다.

기본적으로 Vite는 네이티브 [ES Modules](https://caniuse.com/es6-module), 네이티브 [ESM dynamic import](https://caniuse.com/es6-module-dynamic-import), 그리고 [`import.meta`](https://caniuse.com/mdn-javascript_operators_import_meta)를 지원하는 브라우저를 대상으로 합니다. 여기에 더해 iframe 간 통신을 위해 [`BroadcastChannel`](https://caniuse.com/?search=BroadcastChannel)도 사용합니다:

- Chrome >=87
- Firefox >=78
- Safari >=15.4
- Edge >=88

## Running Tests

browser 옵션에서 브라우저 이름을 지정하면, Vitest는 기본적으로 `preview`를 사용해 해당 브라우저를 실행한 뒤 그 환경에서 테스트를 수행합니다. `preview`를 사용하고 싶지 않다면 `browser.provider` 옵션으로 사용자 지정 browser provider를 설정할 수 있습니다.

CLI에서 브라우저를 지정하려면 `--browser` 플래그 뒤에 브라우저 이름을 붙여 사용하세요:

```sh
npx vitest --browser=chromium
```

또는 점 표기법을 사용해 브라우저 옵션을 CLI에 전달할 수도 있습니다:

```sh
npx vitest --browser.headless
```

::: warning
Vitest 3.2부터는, 설정에 `browser` 옵션이 없는데 `--browser` 플래그를 지정하면 Vitest가 실패합니다. 해당 설정이 브라우저용인지 Node.js 테스트용인지 가정할 수 없기 때문입니다.
:::

기본적으로 Vitest는 개발 시 브라우저 UI를 자동으로 엽니다. 테스트는 중앙의 iframe 내부에서 실행됩니다. 선호하는 크기를 선택하거나, 테스트 내부에서 `page.viewport`를 호출하거나, [설정](https://vitest.dev/config/#browser-viewport)에서 기본값을 지정해 viewport를 구성할 수 있습니다.

## Headless

헤드리스 모드는 브라우저 모드에서 사용할 수 있는 또 다른 옵션입니다. 헤드리스 모드에서는 브라우저가 UI 없이 백그라운드에서 실행되므로 자동화 테스트 실행에 유용합니다. Vitest의 headless 옵션은 boolean 값으로 설정해 활성화/비활성화할 수 있습니다.

헤드리스 모드를 사용하면 Vitest는 UI를 자동으로 열지 않습니다. UI를 계속 사용하면서 테스트만 헤드리스로 실행하려면 [`@vitest/ui`](https://vitest.dev/guide/ui) 패키지를 설치하고 Vitest 실행 시 `--ui` 플래그를 전달하면 됩니다.

다음은 헤드리스 모드를 활성화한 설정 예시입니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      enabled: true,
      headless: true,
    },
  },
});
```

CLI에서 `--browser.headless` 플래그로 헤드리스 모드를 설정할 수도 있습니다:

```sh
npx vitest --browser.headless
```

이 경우 Vitest는 Chrome 브라우저를 사용해 헤드리스 모드로 실행됩니다.

::: warning
헤드리스 모드는 기본으로 제공되지 않습니다. 이 기능을 활성화하려면 [`playwright`](https://npmjs.com/package/playwright) 또는 [`webdriverio`](https://www.npmjs.com/package/webdriverio) provider를 사용해야 합니다.
:::

## Examples

기본적으로 Browser Mode를 사용하는 데 외부 패키지는 필요하지 않습니다:

```js [example.test.js]
import { expect, test } from "vitest";
import { page } from "vitest/browser";
import { render } from "./my-render-function.js";

test("properly handles form inputs", async () => {
  render(); // mount DOM elements

  // Asserts initial state.
  await expect
    .element(page.getByText("Hi, my name is Alice"))
    .toBeInTheDocument();

  // Get the input DOM node by querying the associated label.
  const usernameInput = page.getByLabelText(/username/i);

  // Type the name into the input. This already validates that the input
  // is filled correctly, no need to check the value manually.
  await usernameInput.fill("Bob");

  await expect
    .element(page.getByText("Hi, my name is Bob"))
    .toBeInTheDocument();
});
```

하지만 Vitest는 여러 인기 프레임워크의 컴포넌트를 바로 렌더링할 수 있는 패키지도 제공합니다:

- [`vitest-browser-vue`](https://github.com/vitest-dev/vitest-browser-vue): [vue](https://vuejs.org) 컴포넌트 렌더링
- [`vitest-browser-svelte`](https://github.com/vitest-dev/vitest-browser-svelte): [svelte](https://svelte.dev) 컴포넌트 렌더링
- [`vitest-browser-react`](https://github.com/vitest-dev/vitest-browser-react): [react](https://react.dev) 컴포넌트 렌더링
- [`vitest-browser-angular`](https://github.com/vitest-community/vitest-browser-angular): [Angular](https://angular.dev) 컴포넌트 렌더링

다른 프레임워크를 위한 커뮤니티 패키지도 제공됩니다:

- [`vitest-browser-lit`](https://github.com/EskiMojo14/vitest-browser-lit): [lit](https://lit.dev) 컴포넌트 렌더링
- [`vitest-browser-preact`](https://github.com/JoviDeCroock/vitest-browser-preact): [preact](https://preactjs.com) 컴포넌트 렌더링
- [`vitest-browser-qwik`](https://github.com/kunai-consulting/vitest-browser-qwik): [qwik](https://qwik.dev) 컴포넌트 렌더링

원하는 프레임워크가 없다면 직접 패키지를 만들어도 됩니다. 프레임워크 renderer와 `page.elementLocator` API를 감싼 단순한 wrapper입니다. 이 페이지에 링크를 추가해 드리겠습니다. 이름은 `vitest-browser-`로 시작해야 합니다.

컴포넌트 렌더링과 요소 탐색 외에도 assertion이 필요합니다. Vitest는 [`@testing-library/jest-dom`](https://github.com/testing-library/jest-dom) 라이브러리를 포크해, 다양한 DOM assertion을 기본 제공하도록 합니다. 자세한 내용은 [Assertions API](https://vitest.dev/api/browser/assertions)를 참고하세요.

```ts
import { expect } from "vitest";
import { page } from "vitest/browser";
// element is rendered correctly
await expect.element(page.getByText("Hello World")).toBeInTheDocument();
```

Vitest는 테스트에서 유용할 수 있는 소규모 유틸리티 집합을 가진 [Context API](https://vitest.dev/api/browser/context)를 제공합니다. 예를 들어 요소 클릭이나 입력값 타이핑 같은 상호작용이 필요하면 `vitest/browser`의 `userEvent`를 사용할 수 있습니다. 자세한 내용은 [Interactivity API](https://vitest.dev/api/browser/interactivity)를 참고하세요.

```ts
import { page, userEvent } from "vitest/browser";
await userEvent.fill(page.getByLabelText(/username/i), "Alice");
// or just locator.fill
await page.getByLabelText(/username/i).fill("Alice");
```

::: code-group

```ts [vue]
import { render } from "vitest-browser-vue";
import Component from "./Component.vue";

test("properly handles v-model", async () => {
  const screen = render(Component);

  // Asserts initial state.
  await expect
    .element(screen.getByText("Hi, my name is Alice"))
    .toBeInTheDocument();

  // Get the input DOM node by querying the associated label.
  const usernameInput = screen.getByLabelText(/username/i);

  // Type the name into the input. This already validates that the input
  // is filled correctly, no need to check the value manually.
  await usernameInput.fill("Bob");

  await expect
    .element(screen.getByText("Hi, my name is Bob"))
    .toBeInTheDocument();
});
```

```ts [svelte]
import { render } from "vitest-browser-svelte";
import { expect, test } from "vitest";

import Greeter from "./greeter.svelte";

test("greeting appears on click", async () => {
  const screen = render(Greeter, { name: "World" });

  const button = screen.getByRole("button");
  await button.click();
  const greeting = screen.getByText(/hello world/iu);

  await expect.element(greeting).toBeInTheDocument();
});
```

```tsx [react]
import { render } from "vitest-browser-react";
import Fetch from "./fetch";

test("loads and displays greeting", async () => {
  // Render a React element into the DOM
  const screen = render(<Fetch url="/greeting" />);

  await screen.getByText("Load Greeting").click();
  // wait before throwing an error if it cannot find an element
  const heading = screen.getByRole("heading");

  // assert that the alert message is correct
  await expect.element(heading).toHaveTextContent("hello there");
  await expect.element(screen.getByRole("button")).toBeDisabled();
});
```

```ts [lit]
import { render } from "vitest-browser-lit";
import { html } from "lit";
import "./greeter-button";

test("greeting appears on click", async () => {
  const screen = render(html`<greeter-button name="World"></greeter-button>`);

  const button = screen.getByRole("button");
  await button.click();
  const greeting = screen.getByText(/hello world/iu);

  await expect.element(greeting).toBeInTheDocument();
});
```

```tsx [preact]
import { render } from "vitest-browser-preact";
import { createElement } from "preact";
import Greeting from ".Greeting";

test("greeting appears on click", async () => {
  const screen = render(<Greeting />);

  const button = screen.getByRole("button");
  await button.click();
  const greeting = screen.getByText(/hello world/iu);

  await expect.element(greeting).toBeInTheDocument();
});
```

```tsx [qwik]
import { render } from "vitest-browser-qwik";
import Greeting from "./greeting";

test("greeting appears on click", async () => {
  // renderSSR and renderHook are also available
  const screen = render(<Greeting />);

  const button = screen.getByRole("button");
  await button.click();
  const greeting = screen.getByText(/hello world/iu);

  await expect.element(greeting).toBeInTheDocument();
});
```

:::

Vitest는 모든 프레임워크를 기본 지원하지는 않지만, 외부 도구를 사용해 해당 프레임워크로 테스트를 실행할 수 있습니다. 커뮤니티에서 자체 `vitest-browser` wrapper를 만드는 것도 권장합니다. 이미 가지고 있다면 위 예시에 자유롭게 추가하세요.

지원되지 않는 프레임워크의 경우 `testing-library` 패키지 사용을 권장합니다:

- [`@solidjs/testing-library`](https://testing-library.com/docs/solid-testing-library/intro): [solid](https://www.solidjs.com) 컴포넌트 렌더링
- [`@marko/testing-library`](https://testing-library.com/docs/marko-testing-library/intro): [marko](https://markojs.com) 컴포넌트 렌더링

[`browser-examples`](https://github.com/vitest-tests/browser-examples) 저장소에서 더 많은 예시도 확인할 수 있습니다.

::: warning
`testing-library`는 `@testing-library/user-event` 패키지를 제공합니다. 하지만 실제 트리거 대신 이벤트를 시뮬레이션하므로 직접 사용은 권장하지 않습니다. 대신 내부적으로 Chrome DevTools Protocol 또는 Webdriver(provider에 따라 다름)를 사용하는 `vitest/browser`의 [`userEvent`](https://vitest.dev/api/browser/interactivity)를 사용하세요.
:::

::: code-group

```tsx [solid]
// based on @testing-library/solid API
// https://testing-library.com/docs/solid-testing-library/api

import { render } from "@testing-library/solid";

it("uses params", async () => {
  const App = () => (
    <>
      <Route
        path="/ids/:id"
        component={() => (
          <p>
            Id:
            {useParams()?.id}
          </p>
        )}
      />
      <Route path="/" component={() => <p>Start</p>} />
    </>
  );
  const { baseElement } = render(() => <App />, { location: "ids/1234" });
  const screen = page.elementLocator(baseElement);

  await expect.screen(screen.getByText("Id: 1234")).toBeInTheDocument();
});
```

```ts [marko]
// based on @testing-library/marko API
// https://testing-library.com/docs/marko-testing-library/api

import { render, screen } from "@marko/testing-library";
import Greeting from "./greeting.marko";

test("renders a message", async () => {
  const { baseElement } = await render(Greeting, { name: "Marko" });
  const screen = page.elementLocator(baseElement);
  await expect.element(screen.getByText(/Marko/)).toBeInTheDocument();
  expect(container.firstChild).toMatchInlineSnapshot(`
    <h1>Hello, Marko!</h1>
  `);
});
```

:::

## Limitations

### Thread Blocking Dialogs

Vitest Browser를 사용할 때는 `alert`나 `confirm` 같은 thread blocking dialog를 네이티브로 사용할 수 없다는 점에 유의해야 합니다. 이러한 API는 웹 페이지를 블로킹하므로, Vitest가 페이지와 계속 통신할 수 없어 실행이 멈추게 됩니다.

이런 상황에서 Vitest는 해당 API들에 대해 기본 반환값을 갖는 기본 mock을 제공합니다. 덕분에 사용자가 실수로 동기 popup 웹 API를 사용해도 실행이 멈추지 않습니다. 다만 더 나은 사용 경험을 위해서는 사용자가 이 웹 API들을 직접 mock하는 것을 권장합니다. 자세한 내용은 [Mocking](https://vitest.dev/guide/mocking)에서 확인하세요.

### Spying on Module Exports

Browser Mode는 브라우저의 네이티브 ESM 지원을 사용해 모듈을 제공합니다. 모듈 namespace object는 seal되어 있어 재구성할 수 없으며, Vitest가 Module Runner를 패치할 수 있는 Node.js 테스트와 다릅니다. 즉, import한 객체에 대해 `vi.spyOn`을 호출할 수 없습니다:

```ts
import { vi } from "vitest";
import * as module from "./module.js";

vi.spyOn(module, "method"); // ❌ throws an error
```

이 제한을 우회하기 위해, Vitest는 `vi.mock('./module.js')`에서 `{ spy: true }` 옵션을 지원합니다. 이 옵션은 모듈의 모든 export를 가짜로 대체하지 않고 자동으로 spy 처리합니다.

```ts
import { vi } from "vitest";
import * as module from "./module.js";

vi.mock("./module.js", { spy: true });

vi.mocked(module.method).mockImplementation(() => {
  // ...
});
```

하지만 export된 *variables*를 mock하는 유일한 방법은 내부 값을 변경하는 메서드를 export하는 것입니다:

::: code-group

```js [module.js]
export let MODE = "test";
export function changeMode(newMode) {
  MODE = newMode;
}
```

```js [module.test.ts]
import { expect } from "vitest";
import { changeMode, MODE } from "./module.js";

changeMode("production");
expect(MODE).toBe("production");
```

:::
