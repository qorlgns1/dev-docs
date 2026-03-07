---
title: "고급 시작하기 {#getting-started}"
description: "이 가이드는 Node.js 스크립트를 통해 테스트를 실행하기 위한 고급 API를 나열합니다. 단순히 테스트 실행만 하려는 경우에는 아마 이것이 필요하지 않습니다. 이 기능은 주로 라이브러리 작성자가 사용합니다."
---

출처 URL: https://vitest.dev/guide/advanced

# 고급 시작하기 {#getting-started}

::: warning
이 가이드는 Node.js 스크립트를 통해 테스트를 실행하기 위한 고급 API를 나열합니다. 단순히 [테스트 실행](https://vitest.dev/guide/)만 하려는 경우에는 아마 이것이 필요하지 않습니다. 이 기능은 주로 라이브러리 작성자가 사용합니다.
:::

`vitest/node` 엔트리 포인트에서 어떤 메서드든 import할 수 있습니다.

## startVitest

```ts
function startVitest(
  mode: VitestRunMode,
  cliFilters: string[] = [],
  options: CliOptions = {},
  viteOverrides?: ViteUserConfig,
  vitestOptions?: VitestOptions,
): Promise<Vitest>;
```

Node API를 사용해 Vitest 테스트 실행을 시작할 수 있습니다:

```js
import { startVitest } from "vitest/node";

const vitest = await startVitest("test");

await vitest.close();
```

테스트를 시작할 수 있으면 `startVitest` 함수는 [`Vitest`](https://vitest.dev/api/advanced/vitest) 인스턴스를 반환합니다.

watch 모드가 활성화되어 있지 않으면, Vitest가 `close` 메서드를 자동으로 호출합니다.

watch 모드가 활성화되어 있고 터미널이 TTY를 지원하면, Vitest가 콘솔 단축키를 등록합니다.

두 번째 인수로 필터 목록을 전달할 수 있습니다. Vitest는 파일 경로에 전달된 문자열 중 하나 이상이 포함된 테스트만 실행합니다.

또한 세 번째 인수로 CLI 인수를 전달할 수 있으며, 이는 모든 테스트 설정 옵션을 덮어씁니다. 또는 네 번째 인수로 전체 Vite 설정을 전달할 수 있으며, 이 경우 다른 사용자 정의 옵션보다 우선 적용됩니다.

테스트를 실행한 뒤에는 [`state.getTestModules`](https://vitest.dev/api/advanced/test-module) API에서 결과를 가져올 수 있습니다:

```ts
import type { TestModule } from "vitest/node";

const vitest = await startVitest("test");

console.log(vitest.state.getTestModules()); // [TestModule]
```

::: tip
["Running Tests"](https://vitest.dev/guide/advanced/tests#startvitest) 가이드에 사용 예제가 있습니다.
:::

## createVitest

```ts
function createVitest(
  mode: VitestRunMode,
  options: CliOptions,
  viteOverrides: ViteUserConfig = {},
  vitestOptions: VitestOptions = {},
): Promise<Vitest>;
```

`createVitest` 함수를 사용해 Vitest 인스턴스를 생성할 수 있습니다. 이 함수는 `startVitest`와 동일한 [`Vitest`](https://vitest.dev/api/advanced/vitest) 인스턴스를 반환하지만, 테스트를 시작하지 않고 설치된 패키지도 검증하지 않습니다.

```js
import { createVitest } from "vitest/node";

const vitest = await createVitest("test", {
  watch: false,
});
```

::: tip
["Running Tests"](https://vitest.dev/guide/advanced/tests#createvitest) 가이드에 사용 예제가 있습니다.
:::

## resolveConfig

```ts
function resolveConfig(
  options: UserConfig = {},
  viteOverrides: ViteUserConfig = {},
): Promise<{
  vitestConfig: ResolvedConfig;
  viteConfig: ResolvedViteConfig;
}>;
```

이 메서드는 사용자 지정 파라미터로 설정을 해석합니다. 파라미터를 주지 않으면 `root`는 `process.cwd()`가 됩니다.

```ts
import { resolveConfig } from "vitest/node";

// vitestConfig only has resolved "test" properties
const { vitestConfig, viteConfig } = await resolveConfig({
  mode: "custom",
  configFile: false,
  resolve: {
    conditions: ["custom"],
  },
  test: {
    setupFiles: ["/my-setup-file.js"],
    pool: "threads",
  },
});
```

::: info
Vite의 `createServer` 동작 방식 때문에, Vitest는 플러그인의 `configResolve` 훅에서 설정을 해석해야 합니다. 따라서 이 메서드는 내부적으로 실제 사용되지 않으며, 오직 공개 API로만 노출됩니다.

`startVitest` 또는 `createVitest` API에 설정을 전달하더라도, Vitest는 설정을 다시 해석합니다.
:::

::: warning
`resolveConfig`는 `projects`를 해석하지 않습니다. 프로젝트 설정을 해석하려면 Vitest에 설정된 Vite 서버가 필요합니다.

또한 `viteConfig.test`는 완전히 해석되지 않는다는 점에 유의하세요. Vitest 설정이 필요하다면 대신 `vitestConfig`를 사용하세요.
:::

## parseCLI

```ts
function parseCLI(
  argv: string | string[],
  config: CliParseOptions = {},
): {
  filter: string[];
  options: CliOptions;
};
```

이 메서드를 사용해 CLI 인수를 파싱할 수 있습니다. 문자열(인수를 단일 공백으로 분리) 또는 Vitest CLI가 사용하는 동일한 형식의 CLI 인수 문자열 배열을 받습니다. 이후 `createVitest` 또는 `startVitest` 메서드에 전달할 수 있는 filter와 `options`를 반환합니다.

```ts
import { parseCLI } from "vitest/node";

const result = parseCLI("vitest ./files.ts --coverage --browser=chrome");

result.options;
// {
//   coverage: { enabled: true },
//   browser: { name: 'chrome', enabled: true }
// }

result.filter;
// ['./files.ts']
```
