---
title: "테스트 어노테이션"
description: "Vitest는  API를 통해 사용자 지정 메시지와 파일로 테스트에 어노테이션을 추가할 수 있습니다. 이러한 어노테이션은 테스트 케이스에 첨부되어  훅에서 리포터로 전달됩니다."
---

출처 URL: https://vitest.dev/guide/test-annotations

# 테스트 어노테이션

Vitest는 [`context.annotate`](https://vitest.dev/guide/test-context#annotate) API를 통해 사용자 지정 메시지와 파일로 테스트에 어노테이션을 추가할 수 있습니다. 이러한 어노테이션은 테스트 케이스에 첨부되어 [`onTestAnnotate`](https://vitest.dev/api/advanced/reporters#ontestannotate) 훅에서 리포터로 전달됩니다.

```ts
test("hello world", async ({ annotate }) => {
  await annotate("this is my test");

  if (condition) {
    await annotate("this should've errored", "error");
  }

  const file = createTestSpecificFile();
  await annotate("creates a file", { body: file });
});
```

::: warning
`annotate` 함수는 Promise를 반환하므로, 이를 어떤 방식으로든 의존한다면 `await`해야 합니다. 다만 Vitest는 테스트가 끝나기 전에 `await`되지 않은 어노테이션도 자동으로 `await`합니다.
:::

사용하는 리포터에 따라 이러한 어노테이션이 표시되는 방식은 다릅니다.

## 내장 리포터

### default

`default` 리포터는 테스트가 실패한 경우에만 어노테이션을 출력합니다.

```
  ⎯⎯⎯⎯⎯⎯⎯ Failed Tests 1 ⎯⎯⎯⎯⎯⎯⎯

  FAIL  example.test.js > an example of a test with annotation
Error: thrown error
  ❯ example.test.js:11:21
      9 |    await annotate('annotation 1')
      10|    await annotate('annotation 2', 'warning')
      11|    throw new Error('thrown error')
        |          ^
      12|  })

  ❯ example.test.js:9:15 notice
    ↳ annotation 1
  ❯ example.test.js:10:15 warning
    ↳ annotation 2

  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/1]⎯
```

### verbose

`verbose` 리포터는 테스트가 실패하지 않아도 어노테이션을 보고하는 유일한 터미널 리포터입니다.

```
✓ example.test.js > an example of a test with annotation

  ❯ example.test.js:9:15 notice
    ↳ annotation 1
  ❯ example.test.js:10:15 warning
    ↳ annotation 2

```

### html

HTML 리포터는 UI와 동일한 방식으로 어노테이션을 표시합니다. 어노테이션이 호출된 줄에서 이를 확인할 수 있습니다. 현재는 어노테이션이 테스트 파일에서 호출되지 않은 경우 UI에서 볼 수 없습니다. 별도의 테스트 요약 뷰를 지원하여 이 정보를 볼 수 있도록 할 계획입니다.

### junit

`junit` 리포터는 테스트 케이스의 `properties` 태그 안에 어노테이션을 나열합니다. JUnit 리포터는 모든 첨부 파일을 무시하고 type과 message만 출력합니다.

```xml
<testcase classname="basic/example.test.js" name="an example of a test with annotation" time="0.14315">
    <properties>
        <property name="notice" value="the message of the annotation">
        </property>
    </properties>
</testcase>
```

### github-actions

`github-actions` 리포터는 기본적으로 어노테이션을 [notice message](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#setting-a-notice-message)로 출력합니다. 두 번째 인수로 `notice`, `warning`, `error`를 전달해 `type`을 설정할 수 있습니다. type이 이들 중 하나가 아니면 Vitest는 메시지를 notice로 표시합니다.

### tap

`tap` 및 `tap-flat` 리포터는 `#` 기호로 시작하는 새 줄에 어노테이션을 진단 메시지로 출력합니다. 이들은 모든 첨부 파일을 무시하고 type과 message만 출력합니다.

```
ok 1 - an example of a test with annotation # time=143.15ms
    # notice: the message of the annotation
```
