---
title: "Commands"
description: "Command는 서버에서 다른 함수를 호출하고 그 결과를 브라우저로 다시 전달하는 함수입니다. Vitest는 브라우저 테스트에서 사용할 수 있는 여러 내장 command를 제공합니다."
---

출처 URL: https://vitest.dev/api/browser/commands

# Commands

Command는 서버에서 다른 함수를 호출하고 그 결과를 브라우저로 다시 전달하는 함수입니다. Vitest는 브라우저 테스트에서 사용할 수 있는 여러 내장 command를 제공합니다.

## Built-in Commands

### Files Handling

브라우저 테스트에서 파일을 다루기 위해 `readFile`, `writeFile`, `removeFile` API를 사용할 수 있습니다. Vitest 3.2부터는 모든 경로가 [project](https://vitest.dev/guide/projects) 루트(수동으로 재정의하지 않는 한 `process.cwd()`)를 기준으로 해석됩니다. 이전에는 경로가 테스트 파일 기준으로 해석되었습니다.

기본적으로 Vitest는 `utf-8` 인코딩을 사용하지만, 옵션으로 이를 재정의할 수 있습니다.

::: tip
보안상의 이유로 이 API는 [`server.fs`](https://vitejs.dev/config/server-options.html#server-fs-allow) 제한을 따릅니다.
:::

```ts
import { server } from "vitest/browser";

const { readFile, writeFile, removeFile } = server.commands;

it("handles files", async () => {
  const file = "./test.txt";

  await writeFile(file, "hello world");
  const content = await readFile(file);

  expect(content).toBe("hello world");

  await removeFile(file);
});
```

## CDP Session

Vitest는 `vitest/browser`에서 내보내는 `cdp` 메서드를 통해 원시 Chrome DevTools Protocol에 접근할 수 있도록 제공합니다. 이는 주로 라이브러리 작성자가 그 위에 도구를 구축할 때 유용합니다.

```ts
import { cdp } from "vitest/browser";

const input = document.createElement("input");
document.body.appendChild(input);
input.focus();

await cdp().send("Input.dispatchKeyEvent", {
  type: "keyDown",
  text: "a",
});

expect(input).toHaveValue("a");
```

::: warning
CDP session은 `playwright` provider에서, 그리고 `chromium` 브라우저를 사용할 때만 동작합니다. 자세한 내용은 playwright의 [`CDPSession`](https://playwright.dev/docs/api/class-cdpsession) 문서를 참고하세요.
:::

## Custom Commands

[`browser.commands`](https://vitest.dev/config/browser/commands) config 옵션을 통해 사용자 정의 command를 추가할 수도 있습니다. 라이브러리를 개발하는 경우, plugin 내부의 `config` hook을 통해 이를 제공할 수 있습니다.

```ts
import type { Plugin } from "vitest/config";
import type { BrowserCommand } from "vitest/node";

const myCustomCommand: BrowserCommand<[arg1: string, arg2: string]> = (
  { testPath, provider },
  arg1,
  arg2,
) => {
  if (provider.name === "playwright") {
    console.log(testPath, arg1, arg2);
    return { someValue: true };
  }

  throw new Error(`provider ${provider.name} is not supported`);
};

export default function BrowserCommands(): Plugin {
  return {
    name: "vitest:custom-commands",
    config() {
      return {
        test: {
          browser: {
            commands: {
              myCustomCommand,
            },
          },
        },
      };
    },
  };
}
```

그다음 테스트에서 `vitest/browser`에서 가져와 호출할 수 있습니다.

```ts
import { commands } from "vitest/browser";
import { expect, test } from "vitest";

test("custom command works correctly", async () => {
  const result = await commands.myCustomCommand("test1", "test2");
  expect(result).toEqual({ someValue: true });
});

// if you are using TypeScript, you can augment the module
declare module "vitest/browser" {
  interface BrowserCommands {
    myCustomCommand: (
      arg1: string,
      arg2: string,
    ) => Promise<{
      someValue: true;
    }>;
  }
}
```

::: warning
사용자 정의 함수 이름이 내장 함수와 같으면 내장 함수를 덮어씁니다.
:::

### Custom `playwright` commands

Vitest는 command context에 `playwright` 전용 속성 여러 가지를 제공합니다.

- `page`는 테스트 iframe을 포함하는 전체 페이지를 참조합니다. 이는 orchestrator HTML이며, 문제를 일으키지 않으려면 대부분 직접 건드리지 않는 것이 좋습니다.
- `frame`은 tester [`Frame`](https://playwright.dev/docs/api/class-frame)으로 resolve되는 async 메서드입니다. `page`와 유사한 API를 가지지만 일부 메서드는 지원하지 않습니다. 요소를 조회해야 한다면 더 안정적이고 빠른 `context.iframe` 사용을 권장합니다.
- `iframe`은 페이지의 다른 요소를 조회할 때 사용해야 하는 [`FrameLocator`](https://playwright.dev/docs/api/class-framelocator)입니다.
- `context`는 고유한 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext)를 가리킵니다.

```ts
import { BrowserCommand } from "vitest/node";

export const myCommand: BrowserCommand<[string, number]> = async (
  ctx,
  arg1: string,
  arg2: number,
) => {
  if (ctx.provider.name === "playwright") {
    const element = await ctx.iframe.findByRole("alert");
    const screenshot = await element.screenshot();
    // do something with the screenshot
    return difference;
  }
};
```

### Custom `webdriverio` commands

Vitest는 context object에 `webdriverio` 전용 속성 일부를 제공합니다.

- `browser`는 `WebdriverIO.Browser` API입니다.

Vitest는 command가 호출되기 전에 `browser.switchFrame`을 호출해 `webdriver` context를 테스트 iframe으로 자동 전환하므로, `$` 및 `$$` 메서드는 orchestrator가 아니라 iframe 내부 요소를 가리킵니다. 다만 webdriver가 아닌 API는 여전히 부모 frame context를 참조합니다.
