---
title: "테스트 프로젝트"
description: "이 기능은 라고도 알려져 있습니다. 는 3.2부터 deprecated 되었으며  구성으로 대체되었습니다. 기능적으로는 동일합니다."
---

출처 URL: https://vitest.dev/guide/projects

# 테스트 프로젝트

::: tip 샘플 프로젝트

[GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/projects) - [온라인에서 실행](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/projects?initialPath=__vitest__/)

:::

::: warning
이 기능은 `workspace`라고도 알려져 있습니다. `workspace`는 3.2부터 deprecated 되었으며 `projects` 구성으로 대체되었습니다. 기능적으로는 동일합니다.
:::

Vitest는 단일 Vitest 프로세스 내에서 여러 프로젝트 구성을 정의하는 방법을 제공합니다. 이 기능은 특히 모노레포 설정에서 유용하지만, `resolve.alias`, `plugins`, `test.browser` 등과 같이 서로 다른 구성으로 테스트를 실행하는 데에도 사용할 수 있습니다.

## 프로젝트 정의하기

루트 [config](https://vitest.dev/config/)에서 프로젝트를 정의할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: ["packages/*"],
  },
});
```

프로젝트 구성은 인라인 구성, 파일, 또는 프로젝트를 참조하는 glob 패턴일 수 있습니다. 예를 들어 프로젝트를 담고 있는 `packages`라는 폴더가 있다면, 루트 Vitest 구성에 배열을 정의할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: ["packages/*"],
  },
});
```

Vitest는 `packages` 안의 각 폴더를, 내부에 config 파일이 없더라도 별도의 프로젝트로 취급합니다. glob 패턴이 파일과 일치하는 경우, Vitest 구성 파일인지 확인하기 위해 이름이 `vitest.config`/`vite.config`로 시작하거나 `(vite|vitest).*.config.*` 패턴과 일치하는지 검증합니다. 예를 들어 다음 config 파일들은 유효합니다:

- `vitest.config.ts`
- `vite.config.js`
- `vitest.unit.config.ts`
- `vite.e2e.config.js`
- `vitest.config.unit.js`
- `vite.config.e2e.js`

폴더와 파일을 제외하려면 negation 패턴을 사용할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    // include all folders inside "packages" except "excluded"
    projects: ["packages/*", "!packages/excluded"],
  },
});
```

일부 폴더는 프로젝트여야 하지만 다른 폴더는 자체 하위 폴더를 가진 중첩 구조라면, 상위 폴더가 매칭되는 것을 피하기 위해 괄호를 사용해야 합니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

// For example, this will create projects:
// packages/a
// packages/b
// packages/business/c
// packages/business/d
// Notice that "packages/business" is not a project itself

export default defineConfig({
  test: {
    projects: [
      // matches every folder inside "packages" except "business"
      "packages/!(business)",
      // matches every folder inside "packages/business"
      "packages/business/*",
    ],
  },
});
```

::: warning
Vitest는 구성에서 명시적으로 지정하지 않는 한 루트 `vitest.config` 파일을 프로젝트로 취급하지 않습니다. 따라서 루트 구성은 `reporters`, `coverage` 같은 전역 옵션에만 영향을 줍니다. 참고로 Vitest는 루트 config 파일에 지정된 `apply`, `config`, `configResolved`, `configureServer` 같은 특정 플러그인 훅을 항상 실행합니다. 또한 Vitest는 전역 설정 실행과 사용자 정의 coverage provider 실행에 동일한 플러그인을 사용합니다.
:::

config 파일로 프로젝트를 참조할 수도 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: ["packages/*/vitest.config.{e2e,unit}.ts"],
  },
});
```

이 패턴은 확장자 앞에 `e2e` 또는 `unit`을 포함한 `vitest.config` 파일이 있는 프로젝트만 포함합니다.

인라인 구성을 사용해 프로젝트를 정의할 수도 있습니다. 이 구성은 두 문법을 동시에 지원합니다.

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      // matches every folder and file inside the `packages` folder
      "packages/*",
      {
        // add "extends: true" to inherit the options from the root config
        extends: true,
        test: {
          include: ["tests/**/*.{browser}.test.{ts,js}"],
          // it is recommended to define a name when using inline configs
          name: "happy-dom",
          environment: "happy-dom",
        },
      },
      {
        test: {
          include: ["tests/**/*.{node}.test.{ts,js}"],
          // color of the name label can be changed
          name: { label: "node", color: "green" },
          environment: "node",
        },
      },
    ],
  },
});
```

::: warning
모든 프로젝트는 고유한 이름을 가져야 하며, 그렇지 않으면 Vitest가 오류를 발생시킵니다. 인라인 구성에서 이름을 제공하지 않으면 Vitest가 숫자를 할당합니다. glob 문법으로 정의된 프로젝트 구성의 경우, Vitest는 가장 가까운 `package.json` 파일의 "name" 속성을 기본값으로 사용하고, 없으면 폴더 이름을 사용합니다.
:::

프로젝트는 모든 구성 속성을 지원하지 않습니다. 더 나은 타입 안정성을 위해 프로젝트 구성 파일 내에서는 `defineConfig` 대신 `defineProject` 메서드를 사용하세요:

```ts twoslash [packages/a/vitest.config.ts]
// @errors: 2769
import { defineProject } from "vitest/config";

export default defineProject({
  test: {
    environment: "jsdom",
    // "reporters" is not supported in a project config,
    // so it will show an error
    reporters: ["json"],
  },
});
```

## 테스트 실행하기

테스트를 실행하려면 루트 `package.json`에 스크립트를 정의하세요:

```json [package.json]
{
  "scripts": {
    "test": "vitest"
  }
}
```

이제 패키지 매니저를 사용해 테스트를 실행할 수 있습니다:

::: code-group

```bash [npm]
npm run test
```

```bash [yarn]
yarn test
```

```bash [pnpm]
pnpm run test
```

```bash [bun]
bun run test
```

:::

단일 프로젝트 내에서만 테스트를 실행해야 한다면 `--project` CLI 옵션을 사용하세요:

::: code-group

```bash [npm]
npm run test --project e2e
```

```bash [yarn]
yarn test --project e2e
```

```bash [pnpm]
pnpm run test --project e2e
```

```bash [bun]
bun run test --project e2e
```

:::

::: tip
`--project` CLI 옵션은 여러 번 사용하여 여러 프로젝트를 필터링할 수 있습니다:

::: code-group

```bash [npm]
npm run test --project e2e --project unit
```

```bash [yarn]
yarn test --project e2e --project unit
```

```bash [pnpm]
pnpm run test --project e2e --project unit
```

```bash [bun]
bun run test --project e2e --project unit
```

:::

## 구성

어떤 구성 옵션도 루트 레벨 config 파일에서 상속되지 않습니다. 공유 config 파일을 만들고 이를 프로젝트 config와 직접 병합할 수 있습니다:

```ts [packages/a/vitest.config.ts]
import { defineProject, mergeConfig } from "vitest/config";
import configShared from "../vitest.shared.js";

export default mergeConfig(
  configShared,
  defineProject({
    test: {
      environment: "jsdom",
    },
  }),
);
```

또한 `extends` 옵션을 사용해 루트 레벨 구성에서 상속할 수 있습니다. 모든 옵션이 병합됩니다.

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    pool: "threads",
    projects: [
      {
        // will inherit options from this config like plugins and pool
        extends: true,
        test: {
          name: "unit",
          include: ["**/*.unit.test.ts"],
        },
      },
      {
        // won't inherit any options from this config
        // this is the default behaviour
        extends: false,
        test: {
          name: "integration",
          include: ["**/*.integration.test.ts"],
        },
      },
    ],
  },
});
```

::: danger 지원되지 않는 옵션
일부 구성 옵션은 프로젝트 config에서 허용되지 않습니다. 대표적으로 다음과 같습니다:

- `coverage`: coverage는 전체 프로세스 단위로 수행됩니다
- `reporters`: 루트 레벨 reporters만 지원될 수 있습니다
- `resolveSnapshotPath`: 루트 레벨 resolver만 반영됩니다
- 테스트 러너에 영향을 주지 않는 기타 모든 옵션

프로젝트 구성 내부에서 지원되지 않는 모든 구성 옵션에는 이름 옆에 아이콘이 표시됩니다. 이러한 옵션은 루트 config 파일에서 한 번만 정의할 수 있습니다.
:::
