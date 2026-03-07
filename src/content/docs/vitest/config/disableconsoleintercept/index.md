---
title: "disableConsoleIntercept"
description: "기본적으로 Vitest는 테스트 파일, 테스트 제목 등의 추가 포맷팅을 위해 테스트 중 console 로깅을 자동으로 가로챕니다."
---

출처 URL: https://vitest.dev/config/disableconsoleintercept

# disableConsoleIntercept

- **Type:** `boolean`
- **CLI:** `--disableConsoleIntercept`
- **Default:** `false`

기본적으로 Vitest는 테스트 파일, 테스트 제목 등의 추가 포맷팅을 위해 테스트 중 console 로깅을 자동으로 가로챕니다.

이는 Vitest UI에서 console 로그 미리보기를 위해서도 필요합니다.

하지만 이러한 가로채기를 비활성화하면 일반적인 동기식 터미널 console 로깅으로 코드를 디버깅할 때 도움이 될 수 있습니다.

::: warning
Vitest는 브라우저 devtools에서 원래 로깅을 유지하므로, 이 옵션은 [browser tests](https://vitest.dev/guide/browser/)에는 영향을 주지 않습니다.
:::
