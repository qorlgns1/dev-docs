---
title: "testNamePattern {#testnamepattern}"
description: "전체 이름이 패턴과 일치하는 테스트를 실행합니다."
---

출처 URL: https://vitest.dev/config/testnamepattern

# testNamePattern {#testnamepattern}

- **타입** `string | RegExp`
- **CLI:** `-t <pattern>`, `--testNamePattern=<pattern>`, `--test-name-pattern=<pattern>`

전체 이름이 패턴과 일치하는 테스트를 실행합니다.
이 속성에 `OnlyRunThis`를 추가하면, 테스트 이름에 `OnlyRunThis`라는 단어가 포함되지 않은 테스트는 건너뜁니다.

```js
import { expect, test } from "vitest";

// run
test("OnlyRunThis", () => {
  expect(true).toBe(true);
});

// skipped
test("doNotRun", () => {
  expect(true).toBe(true);
});
```
