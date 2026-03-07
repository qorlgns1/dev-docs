---
title: "Trace View"
description: "Vitest Browser Mode는 Playwright의 trace files 생성을 지원합니다. 트레이싱을 활성화하려면  설정에서  옵션을 설정해야 합니다."
---

출처 URL: https://vitest.dev/guide/browser/trace-view

# Trace View

Vitest Browser Mode는 Playwright의 [trace files](https://playwright.dev/docs/trace-viewer#viewing-remote-traces) 생성을 지원합니다. 트레이싱을 활성화하려면 `test.browser` 설정에서 [`trace`](https://vitest.dev/config/browser/trace) 옵션을 설정해야 합니다.

::: warning
트레이스 파일 생성은 [Playwright provider](https://vitest.dev/config/browser/playwright)를 사용할 때만 가능합니다.
:::

::: code-group

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      trace: "on",
    },
  },
});
```

```bash [CLI]
vitest --browser.trace=on
```

:::

기본적으로 Vitest는 각 테스트마다 트레이스 파일을 생성합니다. `trace`를 `'on-first-retry'`, `'on-all-retries'`, `'retain-on-failure'`로 설정하면 테스트 실패 시에만 트레이스를 생성하도록 구성할 수도 있습니다. 파일은 테스트 파일 옆의 `__traces__` 폴더에 저장됩니다. 트레이스 파일 이름에는 프로젝트 이름, 테스트 이름, 그리고 [`repeats` count와 `retry` count](https://vitest.dev/api/#test-api-reference)가 포함됩니다.

```
chromium-my-test-0-0.trace.zip
^^^^^^^^ project name
         ^^^^^^ test name
                ^ repeat count
                  ^ retry count
```

출력 디렉터리를 변경하려면 `test.browser.trace` 설정에서 `tracesDir` 옵션을 지정하면 됩니다. 이렇게 하면 모든 트레이스가 테스트 파일별로 그룹화되어 동일한 디렉터리에 저장됩니다.

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      trace: {
        mode: "on",
        // the path is relative to the root of the project
        tracesDir: "./playwright-traces",
      },
    },
  },
});
```

트레이스는 리포터에서 [annotations](https://vitest.dev/guide/test-annotations)로 사용할 수 있습니다. 예를 들어 HTML 리포터에서는 테스트 상세 정보에서 트레이스 파일 링크를 확인할 수 있습니다.

## Preview

트레이스 파일을 열려면 Playwright Trace Viewer를 사용할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
npx playwright show-trace "path-to-trace-file"
```

그러면 Trace Viewer가 시작되고 지정한 트레이스 파일을 불러옵니다.

또는 브라우저에서 https://trace.playwright.dev 를 열고 해당 위치에 트레이스 파일을 업로드할 수도 있습니다.

## Limitations

현재 Vitest는 Trace Viewer의 "Sources" 탭을 채울 수 없습니다. 즉, 테스트 중 캡처된 동작과 스크린샷은 확인할 수 있지만, Trace Viewer 내에서 테스트 소스 코드를 직접 볼 수는 없습니다. 테스트 구현은 코드 편집기에서 다시 확인해야 합니다.
