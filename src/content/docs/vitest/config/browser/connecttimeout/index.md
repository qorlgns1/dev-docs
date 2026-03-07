---
title: "browser.connectTimeout"
description: "밀리초 단위의 타임아웃입니다. 브라우저 연결에 이보다 더 오래 걸리면 테스트 스위트가 실패합니다."
---

출처 URL: https://vitest.dev/config/browser/connecttimeout

# browser.connectTimeout

- **타입:** `number`
- **기본값:** `60_000`

밀리초 단위의 타임아웃입니다. 브라우저 연결에 이보다 더 오래 걸리면 테스트 스위트가 실패합니다.

::: info
브라우저가 Vitest 서버와 WebSocket 연결을 설정하는 데 걸려야 하는 시간입니다. 일반적인 상황에서는 이 타임아웃에 도달하면 안 됩니다.
:::
