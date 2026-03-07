---
title: "테스트 필터링"
description: "스위트와 테스트의 필터링, 타임아웃, 동시 실행"
---

출처 URL: https://vitest.dev/guide/filtering

# 테스트 필터링

스위트와 테스트의 필터링, 타임아웃, 동시 실행

## CLI

CLI를 사용해 이름으로 테스트 파일을 필터링할 수 있습니다:

```bash
$ vitest basic
```

그러면 `basic`을 포함하는 테스트 파일만 실행됩니다. 예:

```
basic.test.ts
basic-foo.test.ts
basic/foo.test.ts
```

`-t, --testNamePattern <pattern>` 옵션을 사용해 전체 이름으로 테스트를 필터링할 수도 있습니다. 파일명 자체가 아니라 파일 내부에 정의된 이름으로 필터링하고 싶을 때 유용합니다.

Vitest 3부터는 파일명과 줄 번호로 테스트를 지정할 수도 있습니다:

```bash
$ vitest basic/foo.test.ts:10
```

::: warning
이 기능이 동작하려면 Vitest에 전체 파일명이 필요하다는 점에 유의하세요. 현재 작업 디렉터리를 기준으로 한 상대 경로나 절대 파일 경로를 사용할 수 있습니다.

```bash
$ vitest basic/foo.js:10 # ✅
$ vitest ./basic/foo.js:10 # ✅
$ vitest /users/project/basic/foo.js:10 # ✅
$ vitest foo:10 # ❌
$ vitest ./basic/foo:10 # ❌
```

현재 Vitest는 범위 지정도 지원하지 않습니다:

```bash
$ vitest basic/foo.test.ts:10, basic/foo.test.ts:25 # ✅
$ vitest basic/foo.test.ts:10-25 # ❌
```

:::

## 타임아웃 지정하기

선택적으로 테스트의 세 번째 인자로 밀리초 단위 타임아웃을 전달할 수 있습니다. 기본값은 [5 seconds](https://vitest.dev/config/#testtimeout)입니다.

```ts
import { test } from "vitest";

test("name", async () => {
  /* ... */
}, 1000);
```

훅도 동일하게 기본 5초 타임아웃을 받을 수 있습니다.

```ts
import { beforeAll } from "vitest";

beforeAll(async () => {
  /* ... */
}, 1000);
```

## 스위트와 테스트 건너뛰기

특정 스위트나 테스트를 실행하지 않으려면 `.skip`을 사용하세요.

```ts
import { assert, describe, it } from "vitest";

describe.skip("skipped suite", () => {
  it("test", () => {
    // Suite skipped, no error
    assert.equal(Math.sqrt(4), 3);
  });
});

describe("suite", () => {
  it.skip("skipped test", () => {
    // Test skipped, no error
    assert.equal(Math.sqrt(4), 3);
  });
});
```

## 실행할 스위트와 테스트 선택하기

특정 스위트나 테스트만 실행하려면 `.only`를 사용하세요.

```ts
import { assert, describe, it } from "vitest";

// Only this suite (and others marked with only) are run
describe.only("suite", () => {
  it("test", () => {
    assert.equal(Math.sqrt(4), 3);
  });
});

describe("another suite", () => {
  it("skipped test", () => {
    // Test skipped, as tests are running in Only mode
    assert.equal(Math.sqrt(4), 3);
  });

  it.only("test", () => {
    // Only this test (and others marked with only) are run
    assert.equal(Math.sqrt(4), 2);
  });
});
```

파일 필터와 줄 번호를 함께 지정해 Vitest를 실행하세요:

```shell
vitest ./test/example.test.ts:5
```

```ts:line-numbers
import { assert, describe, it } from 'vitest'

describe('suite', () => {
  // Run only this test
  it('test', () => {
    assert.equal(Math.sqrt(4), 3)
  })
})
```

## 미구현 스위트와 테스트

구현 예정인 스위트와 테스트의 스텁을 만들려면 `.todo`를 사용하세요.

```ts
import { describe, it } from "vitest";

// An entry will be shown in the report for this suite
describe.todo("unimplemented suite");

// An entry will be shown in the report for this test
describe("suite", () => {
  it.todo("unimplemented test");
});
```
