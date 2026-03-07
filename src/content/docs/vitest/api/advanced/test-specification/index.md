---
title: "TestSpecification"
description: "클래스는 어떤 모듈을 테스트로 실행할지와 그 매개변수를 설명합니다."
---

출처 URL: https://vitest.dev/api/advanced/test-specification

# TestSpecification

`TestSpecification` 클래스는 어떤 모듈을 테스트로 실행할지와 그 매개변수를 설명합니다.

테스트 프로젝트에서 [`createSpecification`](https://vitest.dev/api/advanced/test-project#createspecification) 메서드를 호출해서만 specification을 생성할 수 있습니다:

```ts
const specification = project.createSpecification(
  resolve("./example.test.ts"),
  [20, 40], // optional test lines
);
```

`createSpecification`은 해석 완료된 모듈 ID를 기대합니다. 파일을 자동으로 해석하거나 파일 시스템에 실제로 존재하는지 확인하지 않습니다.

## taskId

[Test module의](https://vitest.dev/api/advanced/test-suite#id) 식별자입니다.

## project

이 값은 테스트 모듈이 속한 [`TestProject`](https://vitest.dev/api/advanced/test-project)를 참조합니다.

## moduleId

Vite의 모듈 그래프에서 모듈의 ID입니다. 일반적으로 posix 구분자를 사용하는 절대 파일 경로입니다:

```ts
"C:/Users/Documents/project/example.test.ts"; // ✅
"/Users/mac/project/example.test.ts"; // ✅
"C:\\Users\\Documents\\project\\example.test.ts"; // ❌
```

## testModule

specification과 연결된 [`TestModule`](https://vitest.dev/api/advanced/test-module) 인스턴스입니다. 테스트가 아직 큐에 들어가지 않았다면 `undefined`입니다.

## pool experimental {#pool}

테스트 모듈이 실행될 [`pool`](https://vitest.dev/config/#pool)입니다.

::: danger
[`poolMatchGlob`](https://vitest.dev/config/#poolmatchglob) 및 [`typecheck.enabled`](https://vitest.dev/config/#typecheck-enabled)를 사용하면 하나의 테스트 프로젝트에 여러 pool이 있을 수 있습니다. 즉, 같은 `moduleId`를 가지지만 `pool`이 다른 여러 specification이 존재할 수 있습니다. Vitest 4에서는 프로젝트가 단일 pool만 지원하며, 이 속성은 제거될 예정입니다.
:::

## testLines

테스트 파일이 정의된 소스 코드의 줄 번호 배열입니다. 이 필드는 `createSpecification` 메서드가 배열을 전달받은 경우에만 정의됩니다.

지정한 줄 중 하나라도 테스트가 없으면 전체 suite가 실패한다는 점에 유의하세요. 올바른 `testLines` 구성 예시는 다음과 같습니다:

::: code-group

```ts [script.js]
const specification = project.createSpecification(
  resolve("./example.test.ts"),
  [3, 8, 9],
);
```

```ts:line-numbers{3,8,9} [example.test.js]
import { test, describe } from 'vitest'

test('verification works')

describe('a group of tests', () => { // [!code error]
  // ...

  test('nested test')
  test.skip('skipped test')
})
```

:::

## toJSON

```ts
function toJSON(): SerializedTestSpecification;
```

`toJSON`은 [Browser Mode](https://vitest.dev/guide/browser/) 또는 [Vitest UI](https://vitest.dev/guide/ui)에서 사용할 수 있는 JSON 친화적인 객체를 생성합니다.
