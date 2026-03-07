---
title: "고급 작업 메타데이터"
description: "커스텀 reporter를 개발하거나 Vitest Node.js API를 사용하는 경우, 다양한 컨텍스트에서 실행되는 테스트의 데이터를 reporter 또는 커스텀 Vitest 핸들러로 전달하는 것이 유용할 수 있습니다."
---

출처 URL: https://vitest.dev/api/advanced/metadata

# 고급 작업 메타데이터

커스텀 reporter를 개발하거나 Vitest Node.js API를 사용하는 경우, 다양한 컨텍스트에서 실행되는 테스트의 데이터를 reporter 또는 커스텀 Vitest 핸들러로 전달하는 것이 유용할 수 있습니다.

이를 위해 [test context](https://vitest.dev/guide/test-context)에 의존하는 방법은 직렬화할 수 없기 때문에 적합하지 않습니다. 하지만 Vitest에서는 모든 작업(suite 또는 test)에 있는 `meta` 속성을 활용해 테스트와 Node.js 프로세스 간에 데이터를 공유할 수 있습니다. 중요한 점은 이 통신이 단방향이라는 것입니다. `meta` 속성은 test context 내부에서만 수정할 수 있기 때문입니다. Node.js context에서 변경한 내용은 테스트에서 보이지 않습니다.

suite 작업의 경우 test context 또는 `beforeAll`/`afterAll` 훅 내부에서 `meta` 속성을 채울 수 있습니다.

```ts
afterAll((suite) => {
  suite.meta.done = true;
});

test("custom", ({ task }) => {
  task.meta.custom = "some-custom-handler";
});
```

테스트가 완료되면 Vitest는 결과와 `meta`를 포함한 작업을 RPC를 사용해 Node.js 프로세스로 전송하고, 이후 `onTestCaseResult` 및 작업에 접근할 수 있는 다른 훅에서 이를 보고합니다. 이 테스트 케이스를 처리하려면 reporter 구현에서 제공되는 `onTestCaseResult` 메서드를 사용할 수 있습니다.

```ts [custom-reporter.js]
import type { Reporter, TestCase, TestModule } from "vitest/node";

export default {
  onTestCaseResult(testCase: TestCase) {
    // custom === 'some-custom-handler' ✅
    const { custom } = testCase.meta();
  },
  onTestRunEnd(testModule: TestModule) {
    testModule.meta().done === true;
    testModule.children.at(0).meta().custom === "some-custom-handler";
  },
} satisfies Reporter;
```

::: danger 주의
Vitest는 Node.js 프로세스와 통신할 때 서로 다른 방법을 사용합니다.

- Vitest가 worker threads 내부에서 테스트를 실행하면 [message port](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort)를 통해 데이터를 전송합니다.
- Vitest가 child process를 사용하면 데이터는 [`process.send`](https://nodejs.org/api/process.html#processsendmessage-sendhandle-options-callback) API를 통해 직렬화된 Buffer로 전송됩니다.
- Vitest가 브라우저에서 테스트를 실행하면 데이터는 [flatted](https://www.npmjs.com/package/flatted) 패키지를 사용해 문자열화됩니다.

이 속성은 `json` reporter의 모든 테스트에도 존재하므로, 데이터가 JSON으로 직렬화 가능하도록 해야 합니다.

또한 값을 설정하기 전에 [Error properties](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#error_types)를 직렬화해야 합니다.
:::

테스트 실행이 끝난 뒤에는 Vitest state에서도 이 정보를 가져올 수 있습니다.

```ts
const vitest = await createVitest("test");
const { testModules } = await vitest.start();

const testModule = testModules[0];
testModule.meta().done === true;
testModule.children.at(0).meta().custom === "some-custom-handler";
```

TypeScript를 사용할 때는 타입 정의를 확장하는 것도 가능합니다.

```ts
declare module "vitest" {
  interface TaskMeta {
    done?: boolean;
    custom?: string;
  }
}
```
