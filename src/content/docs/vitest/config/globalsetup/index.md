---
title: "globalSetup"
description: "프로젝트 root를 기준으로 한 전역 설정 파일 경로입니다."
---

출처 URL: https://vitest.dev/config/globalsetup

# globalSetup

- **타입:** `string | string[]`

프로젝트 [root](https://vitest.dev/config/root)를 기준으로 한 전역 설정 파일 경로입니다.

전역 설정 파일은 이름 있는 함수 `setup`, `teardown`을 내보내거나, teardown 함수를 반환하는 `default` 함수를 내보낼 수 있습니다:

::: code-group

```js [exports]
export function setup(project) {
  console.log("setup");
}

export function teardown() {
  console.log("teardown");
}
```

```js [default]
export default function setup(project) {
  console.log("setup");

  return function teardown() {
    console.log("teardown");
  };
}
```

:::

`setup` 메서드와 `default` 함수는 첫 번째 인수로 [test project](https://vitest.dev/api/advanced/test-project)를 받습니다. 전역 설정은 테스트 워커가 생성되기 전에 호출되며, 대기 중인 테스트가 하나 이상 있을 때만 실행됩니다. 그리고 teardown은 모든 테스트 파일 실행이 끝난 뒤 호출됩니다. [watch mode](https://vitest.dev/config/watch)에서는 대신 프로세스가 종료되기 전에 teardown이 호출됩니다. 테스트 재실행 전에 설정을 다시 구성해야 한다면, 대신 [`onTestsRerun`](#handling-test-reruns) 훅을 사용할 수 있습니다.

여러 전역 설정 파일을 사용할 수 있습니다. `setup`과 `teardown`은 순차적으로 실행되며, teardown은 역순으로 실행됩니다.

::: danger
전역 설정은 테스트 워커가 생성되기 전, 별도의 전역 스코프에서 실행되므로 여기서 정의한 전역 변수에는 테스트가 접근할 수 없다는 점에 유의하세요. 대신 [`provide`](https://vitest.dev/config/provide) 메서드로 직렬화 가능한 데이터를 테스트에 전달하고, 테스트에서는 `vitest`에서 가져온 `inject`로 이를 읽을 수 있습니다:

:::code-group

```ts [example.test.ts]
import { inject } from "vitest";

inject("wsPort") === 3000;
```

```ts [globalSetup.ts]
import type { TestProject } from "vitest/node";

export default function setup(project: TestProject) {
  project.provide("wsPort", 3000);
}

declare module "vitest" {
  export interface ProvidedContext {
    wsPort: number;
  }
}
```

테스트와 동일한 프로세스에서 코드를 실행해야 한다면 대신 [`setupFiles`](https://vitest.dev/config/setupfiles)를 사용하세요. 다만 이 방식은 모든 테스트 파일마다 실행된다는 점에 주의하세요.
:::

### 테스트 재실행 처리

Vitest가 테스트를 재실행할 때 호출될 사용자 정의 콜백 함수를 정의할 수 있습니다. 테스트 러너는 이 함수가 완료될 때까지 기다린 후 테스트를 실행합니다. 이 기능은 컨텍스트에 의존하므로 `project`를 `{ onTestsRerun }`처럼 구조 분해할 수는 없습니다.

```ts [globalSetup.ts]
import type { TestProject } from "vitest/node";

export default function setup(project: TestProject) {
  project.onTestsRerun(async () => {
    await restartDb();
  });
}
```
