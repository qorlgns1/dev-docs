---
title: "hookTimeout"
description: "hook의 기본 타임아웃(밀리초)입니다. 타임아웃을 완전히 비활성화하려면 을 사용하세요."
---

출처 URL: https://vitest.dev/config/hooktimeout

# hookTimeout

- **유형:** `number`
- **기본값:** Node.js에서 `10_000`, `browser.enabled`가 `true`이면 `30_000`
- **CLI:** `--hook-timeout=10000`, `--hookTimeout=10000`

hook의 기본 타임아웃(밀리초)입니다. 타임아웃을 완전히 비활성화하려면 `0`을 사용하세요.
