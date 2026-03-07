---
title: "Vitest 설정하기"
description: "Vite를 사용하고  파일이 있다면, Vitest는 해당 파일을 읽어 Vite 앱의 플러그인 및 설정과 일치시키려고 합니다. 테스트용으로 다른 설정을 사용하고 싶거나, 메인 앱이 Vite에 특별히 의존하지 않는 경우에는 다음 중 하나를 사용할 수 있습니다."
---

출처 URL: https://vitest.dev/config

# Vitest 설정하기

Vite를 사용하고 `vite.config` 파일이 있다면, Vitest는 해당 파일을 읽어 Vite 앱의 플러그인 및 설정과 일치시키려고 합니다. 테스트용으로 다른 설정을 사용하고 싶거나, 메인 앱이 Vite에 특별히 의존하지 않는 경우에는 다음 중 하나를 사용할 수 있습니다.

- `vitest.config.ts`를 생성합니다. 이 파일은 더 높은 우선순위를 가지며 `vite.config.ts`의 설정을 **override**합니다(Vitest는 일반적인 JS/TS 확장자를 모두 지원하지만 `json`은 지원하지 않습니다). 즉, `vite.config`의 모든 옵션이 **ignored**됩니다.
- CLI에 `--config` 옵션을 전달합니다. 예: `vitest --config ./path/to/vitest.config.ts`
- `vite.config.ts`에서 `process.env.VITEST` 또는 `defineConfig`의 `mode` 속성(`--mode`로 재정의하지 않으면 `test`/`benchmark`로 설정됨)을 사용해 조건부로 다른 설정을 적용합니다. 다른 환경 변수와 마찬가지로 `VITEST`도 테스트에서 `import.meta.env`에 노출된다는 점에 유의하세요.

`vitest` 자체를 설정하려면 Vite 설정에 `test` 속성을 추가하세요. 또한 `defineConfig`를 `vite`에서 직접 가져오는 경우, 설정 파일 상단에 [triple slash command](https://www.typescriptlang.org/docs/handbook/triple-slash-directives.html#-reference-types-)를 사용해 Vitest 타입 참조를 추가해야 합니다.

`vite`를 사용하지 않는다면, 설정 파일에 `vitest/config`에서 가져온 `defineConfig`를 추가하세요.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    // ... Specify options here.
  },
});
```

이미 `vite` 설정이 있다면, `test` 타입을 포함하기 위해 `/// <reference types="vitest/config" />`를 추가할 수 있습니다.

```js [vite.config.js]
/// <reference types="vitest/config" />
import { defineConfig } from "vite";

export default defineConfig({
  test: {
    // ... Specify options here.
  },
});
```

필요하다면 확장할 수 있도록 Vitest의 기본 옵션을 가져올 수 있습니다.

```js [vitest.config.js]
import { configDefaults, defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    exclude: [...configDefaults.exclude, "packages/template/*"],
  },
});
```

별도의 `vitest.config.js`를 사용할 때도, 필요하면 다른 설정 파일의 Vite 옵션을 확장할 수 있습니다.

```js [vitest.config.js]
import { defineConfig, mergeConfig } from "vitest/config";
import viteConfig from "./vite.config";

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      exclude: ["packages/template/*"],
    },
  }),
);
```

Vite 설정이 함수로 정의되어 있다면, 다음과 같이 설정을 정의할 수 있습니다.

```js [vitest.config.js]
import { defineConfig, mergeConfig } from "vitest/config";
import viteConfig from "./vite.config";

export default defineConfig((configEnv) =>
  mergeConfig(
    viteConfig(configEnv),
    defineConfig({
      test: {
        exclude: ["packages/template/*"],
      },
    }),
  ),
);
```

Vitest는 Vite 설정을 사용하므로, [Vite](https://vitejs.dev/config/)의 모든 설정 옵션도 사용할 수 있습니다. 예를 들어 전역 변수를 정의하는 `define`, 별칭을 정의하는 `resolve.alias` 등이 있습니다. 이러한 옵션은 `test` 속성 내부가 아니라 최상위 레벨에 정의해야 합니다.

[project](https://vitest.dev/guide/projects) 설정 내부에서 지원되지 않는 설정 옵션에는 옆에 아이콘이 표시됩니다. 이는 해당 옵션들이 루트 Vitest 설정에서만 지정될 수 있음을 의미합니다.
