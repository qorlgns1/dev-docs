---
title: "watch {#watch}"
description: "대화형(interactive) 환경에서는 이 명시적으로 지정되지 않는 한 이것이 기본값입니다."
---

출처 URL: https://vitest.dev/config/watch

# watch {#watch}

- **Type:** `boolean`
- **Default:** `!process.env.CI && process.stdin.isTTY`
- **CLI:** `-w`, `--watch`, `--watch=false`

watch 모드를 활성화합니다.

대화형(interactive) 환경에서는 `--run`이 명시적으로 지정되지 않는 한 이것이 기본값입니다.

CI 환경이거나 비대화형 셸에서 실행할 때는 "watch" 모드가 기본값이 아니지만, 이 플래그로 명시적으로 활성화할 수 있습니다.
