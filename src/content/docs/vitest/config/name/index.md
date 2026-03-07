---
title: "name"
description: "interface UserConfig {"
---

출처 URL: https://vitest.dev/config/name

# name

- **타입:**

```ts
interface UserConfig {
  name?: string | { label: string; color?: LabelColor };
}
```

테스트 프로젝트 또는 Vitest 프로세스에 사용자 지정 이름을 할당합니다. 이 이름은 CLI와 UI에 표시되며, Node.js API에서는 [`project.name`](https://vitest.dev/api/advanced/test-project#name)으로 사용할 수 있습니다.

`color` 속성이 있는 객체를 제공하면 CLI와 UI에서 사용되는 색상을 변경할 수 있습니다.

## 색상

표시되는 색상은 터미널의 색상 구성표에 따라 달라집니다. UI에서는 색상이 해당 CSS 색상과 일치합니다.

- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white

## 예시

::: code-group

```js [string]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    name: "unit",
  },
});
```

```js [object]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    name: {
      label: "unit",
      color: "blue",
    },
  },
});
```

:::

이 속성은 특히 여러 프로젝트가 있을 때 유용하며, 터미널에서 프로젝트를 구분하는 데 도움이 됩니다:

```js{7,11} [vitest.config.js]
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    projects: [
      {
        name: 'unit',
        include: ['./test/*.unit.test.js'],
      },
      {
        name: 'e2e',
        include: ['./test/*.e2e.test.js'],
      },
    ],
  },
})
```

::: tip
이름이 제공되지 않으면 Vitest가 자동으로 이름을 할당합니다. 확인 순서는 다음과 같습니다.

- 프로젝트가 config 파일 또는 디렉터리로 지정된 경우, Vitest는 package.json의 `name` 필드를 사용합니다.
- `package.json`이 없으면 Vitest는 프로젝트 폴더의 basename으로 대체합니다.
- 프로젝트가 `projects` 배열 안에서 인라인(객체)으로 정의된 경우, Vitest는 해당 프로젝트의 배열 인덱스(0부터 시작)와 동일한 숫자 이름을 할당합니다.
  :::

::: warning
프로젝트는 같은 이름을 가질 수 없습니다. Vitest는 config 확인 과정에서 오류를 발생시킵니다.
:::

서로 다른 브라우저 [instances](https://vitest.dev/config/browser/instances)에 서로 다른 이름을 할당할 수도 있습니다.

```js{10,11} [vitest.config.js]
import { defineConfig } from 'vitest/config'
import { playwright } from '@vitest/browser-playwright'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [
        { browser: 'chromium', name: 'Chrome' },
        { browser: 'firefox', name: 'Firefox' },
      ],
    },
  },
})
```

::: tip
브라우저 인스턴스는 부모 프로젝트 이름을 상속하고, 괄호 안에 브라우저 이름이 덧붙습니다. 예를 들어 `browser`라는 프로젝트에 chromium 인스턴스가 있으면 `browser (chromium)`으로 표시됩니다.

부모 프로젝트에 이름이 없거나 인스턴스가 루트 레벨(이름 있는 프로젝트 내부가 아님)에 정의된 경우, 인스턴스 이름은 기본적으로 브라우저 값(예: `chromium`)이 됩니다. 이 동작을 재정의하려면 인스턴스에 명시적으로 `name`을 설정하세요.
:::
