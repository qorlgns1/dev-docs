---
title: "시작하기"
description: "Vitest는 Vite를 기반으로 동작하는 차세대 테스트 프레임워크입니다."
---

출처 URL: https://vitest.dev/guide

# 시작하기

## 개요

Vitest(발음: _"veetest"_)는
Vite를 기반으로 동작하는
차세대 테스트 프레임워크입니다.

프로젝트의 배경과 의도는 [Why Vitest](https://vitest.dev/guide/why) 섹션에서 더 자세히 확인할 수 있습니다.

## 온라인에서 Vitest 사용해 보기

[StackBlitz](https://vitest.new)에서 Vitest를 온라인으로 사용해 볼 수 있습니다. 브라우저에서 Vitest를 직접 실행하며, 로컬 환경과 거의 동일하지만 로컬 머신에 아무것도 설치할 필요가 없습니다.

## 프로젝트에 Vitest 추가하기

영상으로 설치하는 방법도 확인할 수 있습니다.

::: code-group

```bash [npm]
npm install -D vitest
```

```bash [yarn]
yarn add -D vitest
```

```bash [pnpm]
pnpm add -D vitest
```

```bash [bun]
bun add -D vitest
```

:::

:::tip
Vitest는 Vite >=v6.0.0 및 Node >=v20.0.0을 필요로 합니다.
:::

위에 나열된 방법 중 하나를 사용해 `package.json`에 `vitest` 사본을 설치하는 것을 권장합니다. 다만 `vitest`를 직접 실행하고 싶다면 `npx vitest`를 사용할 수 있습니다(`npx` 도구는 npm 및 Node.js에 포함되어 있습니다).

`npx` 도구는 지정된 명령을 실행합니다. 기본적으로 `npx`는 먼저 로컬 프로젝트의 바이너리에 해당 명령이 있는지 확인합니다. 거기에서 찾지 못하면 시스템의 `$PATH`를 확인하고, 발견되면 실행합니다. 두 위치 모두에서 명령을 찾지 못하면 실행 전에 임시 위치에 설치합니다.

## 테스트 작성하기

예제로, 두 숫자를 더하는 함수의 출력이 올바른지 검증하는 간단한 테스트를 작성해 보겠습니다.

```js [sum.js]
export function sum(a, b) {
  return a + b;
}
```

```js [sum.test.js]
import { expect, test } from "vitest";
import { sum } from "./sum.js";

test("adds 1 + 2 to equal 3", () => {
  expect(sum(1, 2)).toBe(3);
});
```

::: tip
기본적으로 테스트 파일 이름에는 `.test.` 또는 `.spec.`이 포함되어야 합니다.
:::

다음으로, 테스트를 실행하기 위해 `package.json`에 아래 섹션을 추가하세요:

```json [package.json]
{
  "scripts": {
    "test": "vitest"
  }
}
```

마지막으로 사용하는 패키지 매니저에 따라 `npm run test`, `yarn test`, 또는 `pnpm test`를 실행하면 Vitest가 다음 메시지를 출력합니다:

```txt
✓ sum.test.js (1)
  ✓ adds 1 + 2 to equal 3

Test Files  1 passed (1)
     Tests  1 passed (1)
  Start at  02:15:44
  Duration  311ms
```

::: warning
패키지 매니저로 Bun을 사용 중이라면 `bun test` 대신 반드시 `bun run test` 명령을 사용하세요. 그렇지 않으면 Bun이 자체 테스트 러너를 실행합니다.
:::

Vitest 사용법에 대한 자세한 내용은 [API](https://vitest.dev/api/) 섹션을 참고하세요.

## Vitest 설정하기

Vitest의 주요 장점 중 하나는 Vite와 설정이 통합된다는 점입니다. `vitest`는 존재할 경우 루트 `vite.config.ts`를 읽어 Vite 앱의 플러그인 및 설정과 일치시킵니다. 예를 들어 Vite의 [resolve.alias](https://vitejs.dev/config/shared-options.html#resolve-alias) 및 [plugins](https://vitejs.dev/guide/using-plugins.html) 설정은 별도 작업 없이 그대로 동작합니다. 테스트 시 다른 설정을 사용하고 싶다면 다음을 선택할 수 있습니다.

- 우선순위가 더 높은 `vitest.config.ts`를 생성
- CLI에 `--config` 옵션 전달, 예: `vitest --config ./path/to/vitest.config.ts`
- `vite.config.ts`에서 `process.env.VITEST` 또는 `defineConfig`의 `mode` 속성(재정의하지 않으면 `test`로 설정됨)을 사용해 조건부로 다른 설정 적용. 다른 환경 변수와 마찬가지로 `VITEST`는 테스트에서 `import.meta.env`에도 노출됩니다.

Vitest는 Vite와 동일한 설정 파일 확장자를 지원합니다: `.js`, `.mjs`, `.cjs`, `.ts`, `.cts`, `.mts`. Vitest는 `.json` 확장자는 지원하지 않습니다.

빌드 도구로 Vite를 사용하지 않는 경우, 설정 파일의 `test` 속성을 사용해 Vitest를 설정할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    // ...
  },
});
```

::: tip
직접 Vite를 사용하지 않더라도 Vitest는 변환 파이프라인에서 Vite에 크게 의존합니다. 따라서 [Vite 문서](https://vitejs.dev/config/)에 설명된 모든 속성도 설정할 수 있습니다.
:::

이미 Vite를 사용 중이라면 Vite 설정에 `test` 속성을 추가하세요. 또한 설정 파일 상단에 [triple slash directive](https://www.typescriptlang.org/docs/handbook/triple-slash-directives.html#-reference-types-)를 사용해 Vitest 타입 참조를 추가해야 합니다.

```ts [vite.config.ts]
/// <reference types="vitest/config" />
import { defineConfig } from "vite";

export default defineConfig({
  test: {
    // ...
  },
});
```

설정 옵션 목록은 [Config Reference](https://vitest.dev/config/)에서 확인하세요.

::: warning
Vite와 Vitest를 위해 두 개의 별도 설정 파일을 사용하기로 했다면, Vitest 설정 파일에 동일한 Vite 옵션을 반드시 정의하세요. Vitest 설정은 Vite 파일을 확장하는 것이 아니라 덮어쓰기 때문입니다. `vite` 또는 `vitest/config` 엔트리의 `mergeConfig` 메서드를 사용해 Vite 설정과 Vitest 설정을 병합할 수도 있습니다:

:::code-group

```ts [vitest.config.mjs]
import { defineConfig, mergeConfig } from "vitest/config";
import viteConfig from "./vite.config.mjs";

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      // ...
    },
  }),
);
```

```ts [vite.config.mjs]
import { defineConfig } from "vite";
import Vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [Vue()],
});
```

하지만 별도 파일 두 개를 만드는 대신 Vite와 Vitest에 동일한 파일 하나를 사용하는 것을 권장합니다.
:::

## Projects 지원

같은 프로젝트 안에서 [Test Projects](https://vitest.dev/guide/projects)를 사용해 서로 다른 프로젝트 설정을 실행할 수 있습니다. `vitest.config` 파일에서 프로젝트를 정의하는 파일 및 폴더 목록을 지정할 수 있습니다.

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      // you can use a list of glob patterns to define your projects
      // Vitest expects a list of config files
      // or directories where there is a config file
      "packages/*",
      "tests/*/vitest.config.{e2e,unit}.ts",
      // you can even run the same tests,
      // but with different configs in the same "vitest" process
      {
        test: {
          name: "happy-dom",
          root: "./shared_tests",
          environment: "happy-dom",
          setupFiles: ["./setup.happy-dom.ts"],
        },
      },
      {
        test: {
          name: "node",
          root: "./shared_tests",
          environment: "node",
          setupFiles: ["./setup.node.ts"],
        },
      },
    ],
  },
});
```

## 명령줄 인터페이스

Vitest가 설치된 프로젝트에서는 npm 스크립트에서 `vitest` 바이너리를 사용하거나 `npx vitest`로 직접 실행할 수 있습니다. 아래는 Vitest 스캐폴드 프로젝트의 기본 npm 스크립트입니다:

```json [package.json]
{
  "scripts": {
    "test": "vitest",
    "coverage": "vitest run --coverage"
  }
}
```

파일 변경 감시 없이 테스트를 한 번만 실행하려면 `vitest run`을 사용하세요.
`--port`, `--https` 같은 추가 CLI 옵션도 지정할 수 있습니다. 전체 CLI 옵션 목록은 프로젝트에서 `npx vitest --help`를 실행해 확인하세요.

자세한 내용은 [Command Line Interface](https://vitest.dev/guide/cli)를 참고하세요.

## 자동 의존성 설치

일부 의존성이 설치되어 있지 않으면 Vitest가 설치를 안내합니다. 이 동작은 `VITEST_SKIP_INSTALL_CHECKS=1` 환경 변수를 설정해 비활성화할 수 있습니다.

## IDE 통합

Vitest 테스트 경험 향상을 위해 Visual Studio Code용 공식 확장도 제공합니다.

[Install from VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=vitest.explorer)

자세한 내용은 [IDE Integrations](https://vitest.dev/guide/ide)를 참고하세요.

## 예제

| 예제             | 소스                                                                                 | 플레이그라운드                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `basic`          | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/basic)              | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/basic?initialPath=__vitest__/)              |
| `fastify`        | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/fastify)            | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/fastify?initialPath=__vitest__/)            |
| `in-source-test` | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/in-source-test)     | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/in-source-test?initialPath=__vitest__/)     |
| `lit`            | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/lit)                | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/lit?initialPath=__vitest__/)                |
| `vue`            | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/vue)    | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/vue?initialPath=__vitest__/)    |
| `marko`          | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/marko)  | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/marko?initialPath=__vitest__/)  |
| `preact`         | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/preact) | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/preact?initialPath=__vitest__/) |
| `qwik`           | [Github](https://github.com/vitest-tests/browser-examples/tree/main/examples/qwik)   | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/qwik?initialPath=__vitest__/)   |
| `react`          | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/react)  | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/react?initialPath=__vitest__/)  |
| `solid`          | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/solid)  | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/solid?initialPath=__vitest__/)  |
| `svelte`         | [GitHub](https://github.com/vitest-tests/browser-examples/tree/main/examples/svelte) | [Play Online](https://stackblitz.com/fork/github/vitest-tests/browser-examples/tree/main/examples/svelte?initialPath=__vitest__/) |
| `profiling`      | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/profiling)          | 사용 불가                                                                                                                         |
| `typecheck`      | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/typecheck)          | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/typecheck?initialPath=__vitest__/)          |
| `projects`       | [GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/projects)           | [Play Online](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/projects?initialPath=__vitest__/)           |

## Vitest를 사용하는 프로젝트

- unocss
- unplugin-auto-import
- unplugin-vue-components
- vue
- vite
- vitesse
- vitesse-lite
- fluent-vue
- vueuse
- milkdown
- gridjs-svelte
- spring-easing
- bytemd
- faker
- million
- Vitamin
- neodrag
- svelte-multiselect
- iconify
- tdesign-vue-next
- cz-git

## 릴리스되지 않은 커밋 사용하기

main 브랜치의 각 커밋과 `cr-tracked` 라벨이 붙은 PR은 [pkg.pr.new](https://github.com/stackblitz-labs/pkg.pr.new)에 게시됩니다. `npm i https://pkg.pr.new/vitest@{commit}`로 설치할 수 있습니다.

로컬에서 직접 수정한 내용을 테스트하려면 직접 빌드하고 링크할 수 있습니다([pnpm](https://pnpm.io/) 필요):

```bash
git clone https://github.com/vitest-dev/vitest.git
cd vitest
pnpm install
cd packages/vitest
pnpm run build
pnpm link --global # you can use your preferred package manager for this step
```

그다음 Vitest를 사용하는 프로젝트로 이동해 `pnpm link --global vitest`를 실행하세요(또는 `vitest`를 전역 링크할 때 사용한 패키지 매니저를 사용하세요).

## 커뮤니티

질문이 있거나 도움이 필요하면 [Discord](https://chat.vitest.dev)와 [GitHub Discussions](https://github.com/vitest-dev/vitest/discussions) 커뮤니티에 문의하세요.
