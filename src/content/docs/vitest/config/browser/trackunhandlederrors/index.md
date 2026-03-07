---
title: "browser.trackUnhandledErrors"
description: "Vitest에서 포착되지 않은 오류와 예외를 추적해 보고할 수 있도록 활성화합니다."
---

출처 URL: https://vitest.dev/config/browser/trackunhandlederrors

# browser.trackUnhandledErrors

- **Type:** `boolean`
- **Default:** `true`

Vitest에서 포착되지 않은 오류와 예외를 추적해 보고할 수 있도록 활성화합니다.

특정 오류를 숨겨야 한다면, 대신 [`onUnhandledError`](https://vitest.dev/config/#onunhandlederror) 옵션을 사용하는 것을 권장합니다.

이 설정을 비활성화하면 모든 Vitest 오류 핸들러가 완전히 제거되며, "Pause on exceptions" 체크박스를 켠 상태에서 디버깅할 때 도움이 될 수 있습니다.
