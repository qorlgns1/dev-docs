---
title: "VS Code"
description: "테스트를 디버깅할 때는 다음 옵션을 사용하는 것이 좋습니다:"
---

출처 URL: https://vitest.dev/guide/debugging

# 디버깅

:::tip
테스트를 디버깅할 때는 다음 옵션을 사용하는 것이 좋습니다:

- 브레이크포인트에서 멈췄을 때 테스트가 타임아웃되지 않도록 [`--test-timeout=0`](https://vitest.dev/guide/cli#testtimeout)
- 테스트 파일이 병렬로 실행되지 않도록 [`--no-file-parallelism`](https://vitest.dev/guide/cli#fileparallelism)

:::

## VS Code

VS Code에서 테스트를 디버깅하는 가장 빠른 방법은 `JavaScript Debug Terminal`을 사용하는 것입니다. 새 `JavaScript Debug Terminal`을 열고 `npm run test` 또는 `vitest`를 직접 실행하세요. _이 방식은 Node에서 실행되는 모든 코드에 적용되므로, 대부분의 JS 테스트 프레임워크에서 동작합니다._

![image](https://user-images.githubusercontent.com/5594348/212169143-72bf39ce-f763-48f5-822a-0c8b2e6a8484.png)

VS Code에서 테스트 파일을 디버깅하기 위한 전용 launch configuration을 추가할 수도 있습니다:

```json
{
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Current Test File",
      "autoAttachChildProcesses": true,
      "skipFiles": ["<node_internals>/**", "**/node_modules/**"],
      "program": "${workspaceRoot}/node_modules/vitest/vitest.mjs",
      "args": ["run", "${relativeFile}"],
      "smartStep": true,
      "console": "integratedTerminal"
    }
  ]
}
```

그다음 디버그 탭에서 'Debug Current Test File'이 선택되어 있는지 확인하세요. 이후 디버깅하려는 테스트 파일을 열고 F5를 눌러 디버깅을 시작할 수 있습니다.

### Browser mode

[Vitest Browser Mode](https://vitest.dev/guide/browser/index.md)를 디버깅하려면 CLI에서 `--inspect` 또는 `--inspect-brk`를 전달하거나 Vitest 설정에 정의하세요:

::: code-group

```bash [CLI]
vitest --inspect-brk --browser --no-file-parallelism
```

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    inspectBrk: true,
    fileParallelism: false,
    browser: {
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

:::

기본적으로 Vitest는 디버깅 포트로 `9229`를 사용합니다. `--inspect-brk`에 값을 전달해 이를 덮어쓸 수 있습니다:

```bash
vitest --inspect-brk=127.0.0.1:3000 --browser --no-file-parallelism
```

브라우저에서 Vitest를 실행하고 디버거를 연결하려면 다음 [VSCode Compound configuration](https://code.visualstudio.com/docs/editor/debugging#_compound-launch-configurations)을 사용하세요:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Run Vitest Browser",
      "program": "${workspaceRoot}/node_modules/vitest/vitest.mjs",
      "console": "integratedTerminal",
      "args": ["--inspect-brk", "--browser", "--no-file-parallelism"]
    },
    {
      "type": "chrome",
      "request": "attach",
      "name": "Attach to Vitest Browser",
      "port": 9229
    }
  ],
  "compounds": [
    {
      "name": "Debug Vitest Browser",
      "configurations": ["Attach to Vitest Browser", "Run Vitest Browser"],
      "stopAll": true
    }
  ]
}
```

## IntelliJ IDEA

[vitest](https://www.jetbrains.com/help/idea/vitest.html#createRunConfigVitest) 실행 구성을 만드세요. 모든 테스트를 디버그 모드로 실행하려면 다음 설정을 사용하세요:

| Setting       | Value                        |
| ------------- | ---------------------------- |
| 작업 디렉터리 | `/path/to/your-project-root` |

그런 다음 이 구성을 디버그 모드로 실행하세요. IDE는 에디터에 설정된 JS/TS 브레이크포인트에서 실행을 멈춥니다.

## Node Inspector, 예: Chrome DevTools

Vitest는 IDE 없이 테스트를 디버깅하는 것도 지원합니다. 다만 이 경우 테스트가 병렬 실행되지 않아야 합니다. 다음 명령 중 하나를 사용해 Vitest를 실행하세요.

```sh
# To run in a single worker
vitest --inspect-brk --no-file-parallelism

# To run in browser mode
vitest --inspect-brk --browser --no-file-parallelism
```

Vitest가 시작되면 실행을 멈추고 [Node.js inspector](https://nodejs.org/en/docs/guides/debugging-getting-started/)에 연결할 수 있는 개발자 도구를 열 때까지 대기합니다. 이를 위해 브라우저에서 `chrome://inspect`를 열어 Chrome DevTools를 사용할 수 있습니다.

watch mode에서는 `--isolate false` 옵션을 사용해 테스트 재실행 중에도 디버거를 계속 열어둘 수 있습니다.
