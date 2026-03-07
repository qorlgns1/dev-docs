---
title: "파일 시스템 모킹"
description: "파일 시스템을 모킹하면 테스트가 실제 파일 시스템에 의존하지 않게 되어, 테스트를 더 신뢰성 있고 예측 가능하게 만들 수 있습니다. 이러한 격리는 이전 테스트에서 발생한 부작용을 피하는 데 도움이 됩니다. 또한 권한 문제, 디스크 용량 부족 상황, 읽기/쓰기 오류처럼 ..."
---

출처 URL: https://vitest.dev/guide/mocking/file-system

# 파일 시스템 모킹

파일 시스템을 모킹하면 테스트가 실제 파일 시스템에 의존하지 않게 되어, 테스트를 더 신뢰성 있고 예측 가능하게 만들 수 있습니다. 이러한 격리는 이전 테스트에서 발생한 부작용을 피하는 데 도움이 됩니다. 또한 권한 문제, 디스크 용량 부족 상황, 읽기/쓰기 오류처럼 실제 파일 시스템으로는 재현하기 어렵거나 불가능할 수 있는 오류 조건과 엣지 케이스를 테스트할 수 있게 해줍니다.

Vitest는 기본적으로 파일 시스템 모킹 API를 제공하지 않습니다. `vi.mock`을 사용해 `fs` 모듈을 수동으로 모킹할 수는 있지만, 유지보수가 어렵습니다. 대신 이를 위해 [`memfs`](https://www.npmjs.com/package/memfs)를 사용하는 것을 권장합니다. `memfs`는 메모리 내 파일 시스템을 생성하여 실제 디스크를 건드리지 않고 파일 시스템 작업을 시뮬레이션합니다. 이 방식은 빠르고 안전하며, 실제 파일 시스템에 대한 잠재적인 부작용을 피할 수 있습니다.

## 예제

모든 `fs` 호출을 자동으로 `memfs`로 리디렉션하려면, 프로젝트 루트에 `__mocks__/fs.cjs` 및 `__mocks__/fs/promises.cjs` 파일을 만들 수 있습니다:

::: code-group

```ts [__mocks__/fs.cjs]
// we can also use `import`, but then
// every export should be explicitly defined

const { fs } = require("memfs");
module.exports = fs;
```

```ts [__mocks__/fs/promises.cjs]
// we can also use `import`, but then
// every export should be explicitly defined

const { fs } = require("memfs");
module.exports = fs.promises;
```

:::

```ts [read-hello-world.js]
import { readFileSync } from "node:fs";

export function readHelloWorld(path) {
  return readFileSync(path, "utf-8");
}
```

```ts [hello-world.test.js]
import { beforeEach, expect, it, vi } from "vitest";
import { fs, vol } from "memfs";
import { readHelloWorld } from "./read-hello-world.js";

// tell vitest to use fs mock from __mocks__ folder
// this can be done in a setup file if fs should always be mocked
vi.mock("node:fs");
vi.mock("node:fs/promises");

beforeEach(() => {
  // reset the state of in-memory fs
  vol.reset();
});

it("should return correct text", () => {
  const path = "/hello-world.txt";
  fs.writeFileSync(path, "hello world");

  const text = readHelloWorld(path);
  expect(text).toBe("hello world");
});

it("can return a value multiple times", () => {
  // you can use vol.fromJSON to define several files
  vol.fromJSON(
    {
      "./dir1/hw.txt": "hello dir1",
      "./dir2/hw.txt": "hello dir2",
    },
    // default cwd
    "/tmp",
  );

  expect(readHelloWorld("/tmp/dir1/hw.txt")).toBe("hello dir1");
  expect(readHelloWorld("/tmp/dir2/hw.txt")).toBe("hello dir2");
});
```
