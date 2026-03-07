---
title: "testTimeout"
description: "테스트의 기본 타임아웃(밀리초)입니다. 타임아웃을 완전히 비활성화하려면 을 사용하세요."
---

출처 URL: https://vitest.dev/config/testtimeout

# testTimeout

- **타입:** `number`
- **기본값:** Node.js에서는 `5_000`, `browser.enabled`가 `true`이면 `15_000`
- **CLI:** `--test-timeout=5000`, `--testTimeout=5000`

테스트의 기본 타임아웃(밀리초)입니다. 타임아웃을 완전히 비활성화하려면 `0`을 사용하세요.
