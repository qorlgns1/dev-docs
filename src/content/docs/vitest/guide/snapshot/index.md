---
title: "스냅샷 사용하기"
description: "Vue School의 영상으로 Snapshot을 학습해 보세요."
---

출처 URL: https://vitest.dev/guide/snapshot

# 스냅샷

Vue School의 영상으로 Snapshot을 학습해 보세요.

스냅샷 테스트는 함수의 출력이 예기치 않게 변경되지 않았는지 확인하고 싶을 때 매우 유용한 도구입니다.

스냅샷을 사용하면 Vitest는 주어진 값의 스냅샷을 생성한 뒤, 테스트와 함께 저장된 기준 스냅샷 파일과 비교합니다. 두 스냅샷이 일치하지 않으면 테스트는 실패합니다. 즉, 변경이 예상치 못한 것이거나, 기준 스냅샷을 새로운 결과 버전에 맞게 업데이트해야 한다는 뜻입니다.

## 스냅샷 사용하기

값을 스냅샷으로 검증하려면 `expect()` API의 [`toMatchSnapshot()`](https://vitest.dev/api/expect#tomatchsnapshot)을 사용할 수 있습니다:

```ts
import { expect, it } from "vitest";

it("toUpperCase", () => {
  const result = toUpperCase("foobar");
  expect(result).toMatchSnapshot();
});
```

이 테스트를 처음 실행하면 Vitest는 다음과 같은 스냅샷 파일을 생성합니다:

```js
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports["toUpperCase 1"] = '"FOOBAR"';
```

스냅샷 산출물은 코드 변경과 함께 커밋하고, 코드 리뷰 과정의 일부로 검토해야 합니다. 이후 테스트 실행에서는 Vitest가 렌더링된 출력과 이전 스냅샷을 비교합니다. 일치하면 테스트는 통과합니다. 일치하지 않으면 테스트 러너가 수정이 필요한 코드 버그를 발견했거나, 구현이 변경되어 스냅샷을 업데이트해야 합니다.

::: warning
비동기 동시성 테스트에서 Snapshots를 사용할 때는 올바른 테스트가 감지되도록 로컬 [Test Context](https://vitest.dev/guide/test-context)의 `expect`를 사용해야 합니다.
:::

## 인라인 스냅샷

마찬가지로 [`toMatchInlineSnapshot()`](https://vitest.dev/api/expect#tomatchinlinesnapshot)을 사용해 테스트 파일 내부에 스냅샷을 인라인으로 저장할 수 있습니다.

```ts
import { expect, it } from "vitest";

it("toUpperCase", () => {
  const result = toUpperCase("foobar");
  expect(result).toMatchInlineSnapshot();
});
```

스냅샷 파일을 생성하는 대신, Vitest가 테스트 파일을 직접 수정하여 스냅샷을 문자열로 업데이트합니다:

```ts
import { expect, it } from "vitest";

it("toUpperCase", () => {
  const result = toUpperCase("foobar");
  expect(result).toMatchInlineSnapshot('"FOOBAR"');
});
```

이렇게 하면 파일을 오가며 확인할 필요 없이 기대 출력 결과를 바로 볼 수 있습니다.

::: warning
비동기 동시성 테스트에서 Snapshots를 사용할 때는 올바른 테스트가 감지되도록 로컬 [Test Context](https://vitest.dev/guide/test-context)의 `expect`를 사용해야 합니다.
:::

## 스냅샷 업데이트

수신된 값이 스냅샷과 일치하지 않으면 테스트가 실패하고 둘의 차이를 보여줍니다. 스냅샷 변경이 예상된 경우에는 현재 상태를 기준으로 스냅샷을 업데이트할 수 있습니다.

watch 모드에서는 터미널에서 `u` 키를 눌러 실패한 스냅샷을 바로 업데이트할 수 있습니다.

또는 CLI에서 `--update` 또는 `-u` 플래그를 사용해 Vitest가 스냅샷을 업데이트하도록 할 수 있습니다.

```bash
vitest -u
```

## 파일 스냅샷

`toMatchSnapshot()`을 호출하면 모든 스냅샷이 포맷된 snap 파일에 저장됩니다. 즉, 스냅샷 문자열에서 일부 문자(특히 큰따옴표 `"`와 백틱 `` ` ``)를 이스케이프해야 합니다. 또한 스냅샷 내용이 특정 언어라면 문법 하이라이팅이 사라질 수 있습니다.

이를 고려해, 파일과 명시적으로 매칭할 수 있는 [`toMatchFileSnapshot()`](https://vitest.dev/api/expect#tomatchfilesnapshot)을 도입했습니다. 이렇게 하면 스냅샷 파일에 원하는 확장자를 지정할 수 있고, 가독성도 높아집니다.

```ts
import { expect, it } from "vitest";

it("render basic", async () => {
  const result = renderHTML(h("div", { class: "foo" }));
  await expect(result).toMatchFileSnapshot("./test/basic.output.html");
});
```

이 경우 `./test/basic.output.html`의 내용과 비교합니다. 그리고 `--update` 플래그로 다시 쓸 수 있습니다.

## 비주얼 스냅샷

UI 컴포넌트와 페이지의 시각적 회귀 테스트를 위해, Vitest는 [`toMatchScreenshot()`](https://vitest.dev/api/browser/assertions#tomatchscreenshot-experimental) 단언과 함께 [browser mode](https://vitest.dev/guide/browser/)를 통한 내장 지원을 제공합니다:

```ts
import { expect, test } from "vitest";
import { page } from "vitest/browser";

test("button looks correct", async () => {
  const button = page.getByRole("button");
  await expect(button).toMatchScreenshot("primary-button");
});
```

이 기능은 스크린샷을 캡처하고 기준 이미지와 비교해 의도하지 않은 시각적 변경을 감지합니다. 자세한 내용은 [Visual Regression Testing guide](https://vitest.dev/guide/browser/visual-regression-testing)를 참고하세요.

## 커스텀 Serializer

스냅샷이 직렬화되는 방식을 변경하기 위해 자체 로직을 추가할 수 있습니다. Jest와 마찬가지로 Vitest는 기본적으로 내장 JavaScript 타입, HTML 요소, ImmutableJS, React 요소에 대한 serializer를 제공합니다.

[`expect.addSnapshotSerializer`](https://vitest.dev/api/expect#expect-addsnapshotserializer) API를 사용해 커스텀 serializer를 명시적으로 추가할 수 있습니다.

```ts
expect.addSnapshotSerializer({
  serialize(val, config, indentation, depth, refs, printer) {
    // `printer` is a function that serializes a value using existing plugins.
    return `Pretty foo: ${printer(val.foo, config, indentation, depth, refs)}`;
  },
  test(val) {
    return val && Object.prototype.hasOwnProperty.call(val, "foo");
  },
});
```

또한 커스텀 serializer를 암시적으로 추가할 수 있도록 [snapshotSerializers](https://vitest.dev/config/#snapshotserializers) 옵션도 지원합니다.

```ts [path/to/custom-serializer.ts]
import { SnapshotSerializer } from "vitest";

export default {
  serialize(val, config, indentation, depth, refs, printer) {
    // `printer` is a function that serializes a value using existing plugins.
    return `Pretty foo: ${printer(val.foo, config, indentation, depth, refs)}`;
  },
  test(val) {
    return val && Object.prototype.hasOwnProperty.call(val, "foo");
  },
} satisfies SnapshotSerializer;
```

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    snapshotSerializers: ["path/to/custom-serializer.ts"],
  },
});
```

다음과 같은 테스트를 추가하면:

```ts
test("foo snapshot test", () => {
  const bar = {
    foo: {
      x: 1,
      y: 2,
    },
  };

  expect(bar).toMatchSnapshot();
});
```

아래와 같은 스냅샷을 얻게 됩니다:

```
Pretty foo: Object {
  "x": 1,
  "y": 2,
}
```

스냅샷 직렬화에는 Jest의 `pretty-format`을 사용합니다. 자세한 내용은 여기에서 확인할 수 있습니다: [pretty-format](https://github.com/facebook/jest/blob/main/packages/pretty-format/README.md#serialize).

## Jest와의 차이점

Vitest는 [Jest의](https://jestjs.io/docs/snapshot-testing) Snapshot 기능과 거의 호환되지만, 몇 가지 예외가 있습니다:

#### 1. 스냅샷 파일의 주석 헤더가 다릅니다

```diff
- // Jest Snapshot v1, https://goo.gl/fbAQLP
+ // Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html
```

기능에 실제로 영향을 주지는 않지만, Jest에서 마이그레이션할 때 커밋 diff에는 영향을 줄 수 있습니다.

#### 2. `printBasicPrototype`의 기본값이 `false`입니다

Jest와 Vitest의 스냅샷은 모두 [`pretty-format`](https://github.com/facebook/jest/blob/main/packages/pretty-format)를 기반으로 동작합니다. Vitest에서는 더 깔끔한 스냅샷 출력을 위해 `printBasicPrototype`의 기본값을 `false`로 설정했고, Jest \<29.0.0에서는 기본값이 `true`입니다.

```ts
import { expect, test } from "vitest";

test("snapshot", () => {
  const bar = [
    {
      foo: "bar",
    },
  ];

  // in Jest
  expect(bar).toMatchInlineSnapshot(`
    Array [
      Object {
        "foo": "bar",
      },
    ]
  `);

  // in Vitest
  expect(bar).toMatchInlineSnapshot(`
    [
      {
        "foo": "bar",
      },
    ]
  `);
});
```

가독성과 전반적인 DX 측면에서 이것이 더 합리적인 기본값이라고 봅니다. 그래도 Jest의 동작을 선호한다면 설정을 변경할 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    snapshotFormat: {
      printBasicPrototype: true,
    },
  },
});
```

#### 3. 커스텀 메시지에서는 콜론 `:` 대신 구분자로 Chevron `>`를 사용합니다

Vitest는 스냅샷 파일 생성 시 커스텀 메시지가 전달되면 가독성을 위해 콜론 `:` 대신 chevron `>`를 구분자로 사용합니다.

다음 테스트 코드 예시에서:

```js
test("toThrowErrorMatchingSnapshot", () => {
  expect(() => {
    throw new Error("error");
  }).toThrowErrorMatchingSnapshot("hint");
});
```

Jest의 스냅샷은 다음과 같습니다:

```console
exports[`toThrowErrorMatchingSnapshot: hint 1`] = `"error"`;
```

Vitest에서 동일한 스냅샷은 다음과 같습니다:

```console
exports[`toThrowErrorMatchingSnapshot > hint 1`] = `[Error: error]`;
```

#### 4. `toThrowErrorMatchingSnapshot` 및 `toThrowErrorMatchingInlineSnapshot`의 기본 `Error` 스냅샷이 다릅니다

```js
import { expect, test } from 'vitest'

test('snapshot', () => {
  // in Jest and Vitest
  expect(new Error('error')).toMatchInlineSnapshot(`[Error: error]`)

  // Jest snapshots `Error.message` for `Error` instance
  // Vitest prints the same value as toMatchInlineSnapshot
  expect(() => {
    throw new Error('error')
  }).toThrowErrorMatchingInlineSnapshot(`"error"`) // [!code --]
  }).toThrowErrorMatchingInlineSnapshot(`[Error: error]`) // [!code ++]
})
```
