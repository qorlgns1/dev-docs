---
title: "모듈 모킹"
description: '"모듈"을 모킹하기 전에, 먼저 모듈이 무엇인지 정의해야 합니다. Vitest 맥락에서 "모듈"은 무언가를 export하는 파일입니다. plugins를 사용하면 어떤 파일이든 JavaScript 모듈로 변환할 수 있습니다. "모듈 객체(module object)"는 e...'
---

출처 URL: https://vitest.dev/guide/mocking/modules

# 모듈 모킹

## 모듈 정의하기

"모듈"을 모킹하기 전에, 먼저 모듈이 무엇인지 정의해야 합니다. Vitest 맥락에서 "모듈"은 무언가를 export하는 파일입니다. [plugins](https://vite.dev/guide/api-plugin.html)를 사용하면 어떤 파일이든 JavaScript 모듈로 변환할 수 있습니다. "모듈 객체(module object)"는 export된 식별자에 대한 동적 참조를 보관하는 네임스페이스 객체입니다. 간단히 말해, export된 메서드와 프로퍼티를 가진 객체입니다. 이 예시에서 `example.js`는 `answer`와 `variable`을 export하는 모듈입니다:

```js [example.js]
export function answer() {
  // ...
  return 42;
}

export const variable = "example";
```

여기서 `exampleObject`는 모듈 객체입니다:

```js [example.test.js]
import * as exampleObject from "./example.js";
```

example를 named import로 가져왔더라도 `exampleObject`는 항상 존재합니다:

```js [example.test.js]
import { answer, variable } from "./example.js";
```

`exampleObject`는 example 모듈 자체 바깥에서만 참조할 수 있습니다. 예를 들어 테스트에서 참조할 수 있습니다.

## 모듈 모킹

이 가이드의 목적을 위해 몇 가지 용어를 정의하겠습니다.

- **Mocked module**은 다른 모듈로 완전히 대체된 모듈입니다.
- **Spied module**은 mocked module의 한 종류이지만, export된 메서드가 원래 구현을 유지합니다. 또한 추적할 수 있습니다.
- **Mocked export**는 호출을 추적할 수 있는 모듈 export입니다.
- **Spied export**는 mocked export입니다.

모듈을 완전히 모킹하려면 [`vi.mock` API](https://vitest.dev/api/vi#vi-mock)를 사용할 수 있습니다. 두 번째 인자로 새 모듈을 반환하는 factory를 제공해 새 모듈을 동적으로 정의할 수 있습니다:

```ts
import { vi } from "vitest";

// The ./example.js module will be replaced with
// the result of a factory function, and the
// original ./example.js module will never be called
vi.mock(import("./example.js"), () => {
  return {
    answer() {
      // ...
      return 42;
    },
    variable: "mock",
  };
});
```

::: tip
`vi.mock`을 [setup file](https://vitest.dev/config/setupfiles)에서 호출하면 모든 테스트 파일에 모듈 모킹을 자동으로 적용할 수 있다는 점을 기억하세요.
:::

::: tip
동적 import 사용에 주목하세요: `import('./example.ts')`. Vitest는 코드 실행 전에 이를 제거하지만, 이 방식은 TypeScript가 문자열을 올바르게 검증하고 IDE 또는 CLI에서 `importOriginal` 메서드 타입을 제대로 추론할 수 있게 해줍니다.
:::

코드가 이 factory에서 반환되지 않은 메서드에 접근하려 하면, Vitest는 도움이 되는 메시지와 함께 에러를 발생시킵니다. `answer`는 모킹되지 않았으므로 추적할 수 없다는 점에 유의하세요. 추적 가능하게 만들려면 대신 `vi.fn()`을 사용하세요:

```ts
import { vi } from "vitest";

vi.mock(import("./example.js"), () => {
  return {
    answer: vi.fn(),
    variable: "mock",
  };
});
```

factory 메서드는 `importOriginal` 함수를 인자로 받으며, 이 함수는 원본 모듈을 실행하고 해당 모듈 객체를 반환합니다:

```ts
import { expect, vi } from "vitest";
import { answer } from "./example.js";

vi.mock(import("./example.js"), async (importOriginal) => {
  const originalModule = await importOriginal();
  return {
    answer: vi.fn(originalModule.answer),
    variable: "mock",
  };
});

expect(answer()).toBe(42);

expect(answer).toHaveBeenCalled();
expect(answer).toHaveReturned(42);
```

::: warning
`importOriginal`은 비동기이므로 `await`가 필요하다는 점에 유의하세요.
:::

위 예시에서는 `vi.fn()` 호출에 원본 `answer`를 전달해, 추적하면서도 원본 호출을 유지하도록 했습니다.

`importOriginal` 사용이 필요하다면, 다른 API인 `vi.spyOn`으로 export를 직접 스파이하는 방식을 고려하세요. 전체 모듈을 교체하는 대신, 하나의 export된 메서드만 스파이할 수 있습니다. 이를 위해 모듈을 네임스페이스 객체로 import해야 합니다:

```ts
import { expect, vi } from "vitest";
import * as exampleObject from "./example.js";

const spy = vi.spyOn(exampleObject, "answer").mockReturnValue(0);

expect(exampleObject.answer()).toBe(0);
expect(exampleObject.answer).toHaveBeenCalled();
```

::: danger Browser Mode Support
이 방법은 [Browser Mode](https://vitest.dev/guide/browser/)에서는 동작하지 않습니다. 브라우저의 네이티브 ESM 지원으로 모듈을 제공하기 때문입니다. 모듈 네임스페이스 객체는 sealed되어 재구성할 수 없습니다. 이 제한을 우회하기 위해 Vitest는 `vi.mock('./example.js')`에서 `{ spy: true }` 옵션을 지원합니다. 이 옵션은 모듈의 모든 export를 가짜로 교체하지 않고 자동으로 스파이합니다.

```ts
import { vi } from "vitest";
import * as exampleObject from "./example.js";

vi.mock("./example.js", { spy: true });

vi.mocked(exampleObject.answer).mockReturnValue(0);
```

:::

::: warning
`vi.spyOn` 유틸리티를 사용하는 파일에서만 모듈을 네임스페이스 객체로 import하면 됩니다. `answer`가 다른 파일에서 호출되고 그곳에서 named export로 import되더라도, `vi.spyOn` 이후에 그 함수를 호출하기만 하면 Vitest는 이를 올바르게 추적할 수 있습니다:

```ts [source.js]
import { answer } from "./example.js";

export function question() {
  if (answer() === 42) {
    return "Ultimate Question of Life, the Universe, and Everything";
  }

  return "Unknown Question";
}
```

:::

`vi.spyOn`은 스파이 설정 이후에 발생한 호출만 추적한다는 점에 유의하세요. 따라서 함수가 import 시점의 top-level에서 실행되었거나 스파이 설정 전에 호출되었다면, `vi.spyOn`은 이를 보고할 수 없습니다.

모듈이 import되기 전에 자동으로 모킹하려면, 경로와 함께 `vi.mock`을 호출할 수 있습니다:

```ts
import { vi } from "vitest";

vi.mock(import("./example.js"));
```

`./__mocks__/example.js` 파일이 존재하면 Vitest는 그 파일을 대신 로드합니다. 그렇지 않으면 원본 모듈을 로드하고 모든 항목을 재귀적으로 교체합니다:

{#automocking-algorithm}

- 모든 배열은 빈 배열이 됩니다
- 모든 원시값은 그대로 유지됩니다
- 모든 getter는 `undefined`를 반환합니다
- 모든 메서드는 `undefined`를 반환합니다
- 모든 객체는 깊은 복사됩니다
- 클래스의 모든 인스턴스와 그 프로토타입이 복제됩니다

이 동작을 비활성화하려면 두 번째 인자로 `spy: true`를 전달할 수 있습니다:

```ts
import { vi } from "vitest";

vi.mock(import("./example.js"), { spy: true });
```

`undefined`를 반환하는 대신, 모든 메서드는 원본 구현을 호출하지만 호출 추적은 계속할 수 있습니다:

```ts
import { expect, vi } from "vitest";
import { answer } from "./example.js";

vi.mock(import("./example.js"), { spy: true });

// calls the original implementation
expect(answer()).toBe(42);
// vitest can still track the invocations
expect(answer).toHaveBeenCalled();
```

모킹된 모듈이 지원하는 좋은 점 중 하나는 인스턴스와 프로토타입 간 상태를 공유할 수 있다는 것입니다. 다음 모듈을 보세요:

```ts [answer.js]
export class Answer {
  constructor(value) {
    this._value = value;
  }

  value() {
    return this._value;
  }
}
```

이 모듈을 모킹하면, 인스턴스 자체에 접근할 수 없어도 `.value()`의 모든 호출을 추적할 수 있습니다:

```ts [answer.test.js]
import { expect, test, vi } from "vitest";
import { Answer } from "./answer.js";

vi.mock(import("./answer.js"), { spy: true });

test("instance inherits the state", () => {
  // these invocations could be private inside another function
  // that you don't have access to in your test
  const answer1 = new Answer(42);
  const answer2 = new Answer(0);

  expect(answer1.value()).toBe(42);
  expect(answer1.value).toHaveBeenCalled();
  // note that different instances have their own states
  expect(answer2.value).not.toHaveBeenCalled();

  expect(answer2.value()).toBe(0);

  // but the prototype state accumulates all calls
  expect(Answer.prototype.value).toHaveBeenCalledTimes(2);
  expect(Answer.prototype.value).toHaveReturned(42);
  expect(Answer.prototype.value).toHaveReturned(0);
});
```

이는 외부로 노출되지 않는 인스턴스 호출을 추적할 때 매우 유용합니다.

## 존재하지 않는 모듈 모킹

Vitest는 가상 모듈(virtual module) 모킹을 지원합니다. 이런 모듈은 파일 시스템에는 없지만 코드에서 import합니다. 예를 들어 개발 환경과 운영 환경이 다를 때 이런 일이 발생할 수 있습니다. 대표적인 예로 단위 테스트에서 `vscode` API를 모킹하는 경우가 있습니다.

기본적으로 Vitest는 import 소스를 찾을 수 없으면 파일 변환에 실패합니다. 이를 우회하려면 config에 명시해야 합니다. import를 항상 특정 파일로 리디렉션하거나, Vite에 이를 무시하라고 알리고 `vi.mock` factory로 export를 정의할 수 있습니다.

import를 리디렉션하려면 [`test.alias`](https://vitest.dev/config/#alias) config 옵션을 사용하세요:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { resolve } from "node:path";

export default defineConfig({
  test: {
    alias: {
      vscode: resolve(import.meta.dirname, "./mock/vscode.js"),
    },
  },
});
```

모듈이 항상 resolve된 것으로 표시하려면, 플러그인의 `resolveId` hook에서 동일한 문자열을 반환하세요:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { resolve } from "node:path";

export default defineConfig({
  plugins: [
    {
      name: "virtual-vscode",
      resolveId(id) {
        if (id === "vscode") {
          return "vscode";
        }
      },
    },
  ],
});
```

이제 테스트에서 평소처럼 `vi.mock`을 사용할 수 있습니다:

```ts
import { vi } from "vitest";

vi.mock(import("vscode"), () => {
  return {
    window: {
      createOutputChannel: vi.fn(),
    },
  };
});
```

## 동작 방식

Vitest는 환경에 따라 서로 다른 모듈 모킹 메커니즘을 구현합니다. 이들이 공통으로 가지는 기능은 플러그인 transformer뿐입니다. Vitest가 파일 안에서 `vi.mock`을 발견하면, 모든 정적 import를 동적 import로 변환하고 `vi.mock` 호출을 파일 최상단으로 이동합니다. 이를 통해 hoist된 import라는 ESM 규칙을 깨지 않으면서 import가 일어나기 전에 mock을 등록할 수 있습니다.

::: code-group

```ts [example.js]
import { answer } from "./answer.js";

vi.mock(import("./answer.js"));

console.log(answer);
```

```ts [example.transformed.js]
vi.mock("./answer.js");

const __vitest_module_0__ = await __handle_mock__(() => import("./answer.js"));
// to keep the live binding, we have to access
// the export on the module namespace
console.log(__vitest_module_0__.answer());
```

:::

`__handle_mock__` 래퍼는 import가 시작되기 전에 mock이 resolve되도록 보장할 뿐이며, 모듈 자체를 어떤 방식으로도 수정하지 않습니다.

모듈 모킹 플러그인은 [`@vitest/mocker` package](https://github.com/vitest-dev/vitest/tree/main/packages/mocker)에서 사용할 수 있습니다.

### JSDOM, happy-dom, Node

에뮬레이션 환경에서 테스트를 실행하면, Vitest는 Vite 코드를 소비할 수 있는 [module runner](https://vite.dev/guide/api-environment-runtimes.html#modulerunner)를 생성합니다. module runner는 Vitest가 모듈 평가 과정에 개입해, mock이 등록되어 있다면 mock으로 대체할 수 있도록 설계되어 있습니다. 즉, Vitest는 ESM과 유사한 환경에서 코드를 실행하지만 네이티브 ESM 메커니즘을 직접 사용하지는 않습니다. 이 덕분에 테스트 러너는 ES Modules의 불변성 규칙을 우회할 수 있고, 사용자는 겉보기엔 ES Module인 대상에도 `vi.spyOn`을 호출할 수 있습니다.

### Browser Mode

Vitest는 Browser Mode에서 네이티브 ESM을 사용합니다. 즉, 모듈을 쉽게 교체할 수 없습니다. 대신 Vitest는 fetch 요청(playwright의 `page.route` 또는 `preview`/`webdriverio` 사용 시 Vite 플러그인 API를 통해)을 가로채고, 모듈이 모킹된 경우 변환된 코드를 제공합니다.

예를 들어 모듈이 automock된 경우, Vitest는 정적 export를 파싱해 플레이스홀더 모듈을 생성할 수 있습니다:

::: code-group

```ts [answer.js]
export function answer() {
  return 42;
}
```

```ts [answer.transformed.js]
function answer() {
  return 42;
}

const __private_module__ = {
  [Symbol.toStringTag]: "Module",
  answer: vi.fn(answer),
};

export const answer = __private_module__.answer;
```

:::

예시는 간결성을 위해 단순화했지만, 개념은 동일합니다. 모듈에 `__private_module__` 변수를 주입해 모킹된 값을 보관할 수 있습니다. 사용자가 `spy: true`와 함께 `vi.mock`을 호출했다면 원본 값을 전달하고, 그렇지 않으면 단순한 `vi.fn()` mock을 생성합니다.

사용자가 커스텀 factory를 정의한 경우 코드 주입은 더 어려워지지만 불가능하지는 않습니다. 모킹된 파일이 제공될 때, 먼저 브라우저에서 factory를 resolve한 다음 키를 서버로 다시 전달하고, 이를 사용해 플레이스홀더 모듈을 생성합니다:

```ts
const resolvedFactoryKeys = await resolveBrowserFactory(url);
const mockedModule = `
const __private_module__ = getFactoryReturnValue(${url})
${resolvedFactoryKeys.map((key) => `export const ${key} = __private_module__["${key}"]`).join("\n")}
`;
```

이 모듈은 이제 브라우저로 다시 제공될 수 있습니다. 테스트 실행 시 devtools에서 해당 코드를 확인할 수 있습니다.

## 모듈 모킹의 함정

같은 파일의 다른 메서드 내부에서 호출되는 메서드 호출은 모킹할 수 없다는 점에 주의하세요. 예를 들어 다음 코드에서:

```ts [foobar.js]
export function foo() {
  return "foo";
}

export function foobar() {
  return `${foo()}bar`;
}
```

`foo` 메서드는 직접 참조되므로 외부에서 모킹할 수 없습니다. 따라서 아래 코드는 `foobar` 내부의 `foo` 호출에는 영향을 주지 않습니다(다만 다른 모듈의 `foo` 호출에는 영향을 줍니다):

```ts [foobar.test.ts]
import { vi } from "vitest";
import * as mod from "./foobar.js";

// this will only affect "foo" outside of the original module
vi.spyOn(mod, "foo");
vi.mock(import("./foobar.js"), async (importOriginal) => {
  return {
    ...(await importOriginal()),
    // this will only affect "foo" outside of the original module
    foo: () => "mocked",
  };
});
```

이 동작은 `foobar` 메서드에 구현을 직접 제공해 확인할 수 있습니다:

```ts [foobar.test.js]
import * as mod from "./foobar.js";

vi.spyOn(mod, "foo");

// exported foo references mocked method
mod.foobar(mod.foo);
```

```ts [foobar.js]
export function foo() {
  return "foo";
}

export function foobar(injectedFoo) {
  return injectedFoo === foo; // false
}
```

이것은 의도된 동작이며, 우회 방법을 구현할 계획은 없습니다. 코드를 여러 파일로 리팩터링하거나 [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) 같은 기법 사용을 고려하세요. 애플리케이션을 테스트 가능하게 만드는 책임은 테스트 러너가 아니라 애플리케이션 아키텍처에 있다고 우리는 봅니다.
