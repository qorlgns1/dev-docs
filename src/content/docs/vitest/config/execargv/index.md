---
title: "execArgv"
description: "러너 워커에서 에 추가 인수를 전달합니다. 자세한 내용은 Command-line API | Node.js를 참고하세요."
---

출처 URL: https://vitest.dev/config/execargv

# execArgv

- **유형:** `string[]`
- **기본값:** `[]`

러너 워커에서 `node`에 추가 인수를 전달합니다. 자세한 내용은 [Command-line API | Node.js](https://nodejs.org/docs/latest/api/cli.html)를 참고하세요.

:::warning
사용 시 주의하세요. 일부 옵션은 워커를 크래시시킬 수 있습니다. 예: `--prof`, `--title`. https://github.com/nodejs/node/issues/41103 를 참고하세요.
:::
