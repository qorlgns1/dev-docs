---
title: "browser.api"
description: "브라우저에서 코드를 제공하는 Vite 서버 옵션을 구성합니다.  옵션에는 영향을 주지 않습니다. 기본적으로 Vitest는 개발 서버와의 충돌을 피하기 위해 포트 를 할당하므로, 두 서버를 병렬로 실행할 수 있습니다."
---

출처 URL: https://vitest.dev/config/browser/api

# browser.api

- **유형:** `number | { port?, strictPort?, host? }`
- **기본값:** `63315`
- **CLI:** `--browser.api=63315`, `--browser.api.port=1234, --browser.api.host=example.com`

브라우저에서 코드를 제공하는 Vite 서버 옵션을 구성합니다. [`test.api`](#api) 옵션에는 영향을 주지 않습니다. 기본적으로 Vitest는 개발 서버와의 충돌을 피하기 위해 포트 `63315`를 할당하므로, 두 서버를 병렬로 실행할 수 있습니다.
