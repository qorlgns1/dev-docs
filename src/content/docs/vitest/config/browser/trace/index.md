---
title: "browser.trace"
description: "브라우저 테스트 실행의 트레이스를 캡처합니다. Playwright Trace Viewer로 트레이스를 미리 볼 수 있습니다."
---

출처 URL: https://vitest.dev/config/browser/trace

# browser.trace

- **유형:** `'on' | 'off' | 'on-first-retry' | 'on-all-retries' | 'retain-on-failure' | object`
- **CLI:** `--browser.trace=on`, `--browser.trace=retain-on-failure`
- **기본값:** `'off'`

브라우저 테스트 실행의 트레이스를 캡처합니다. [Playwright Trace Viewer](https://trace.playwright.dev/)로 트레이스를 미리 볼 수 있습니다.

이 옵션은 다음 값을 지원합니다:

- `'on'` - 모든 테스트에 대해 트레이스를 캡처합니다. (성능 부담이 커서 권장되지 않음)
- `'off'` - 트레이스를 캡처하지 않습니다.
- `'on-first-retry'` - 테스트를 처음 재시도할 때만 트레이스를 캡처합니다.
- `'on-all-retries'` - 테스트의 모든 재시도에서 트레이스를 캡처합니다.
- `'retain-on-failure'` - 실패한 테스트에 대해서만 트레이스를 캡처합니다. 통과한 테스트의 트레이스는 자동으로 삭제됩니다.
- `object` - 다음 형태의 객체입니다:

```ts
interface TraceOptions {
  mode:
    | "on"
    | "off"
    | "on-first-retry"
    | "on-all-retries"
    | "retain-on-failure";
  /**
   * The directory where all traces will be stored. By default, Vitest
   * stores all traces in `__traces__` folder close to the test file.
   */
  tracesDir?: string;
  /**
   * Whether to capture screenshots during tracing. Screenshots are used to build a timeline preview.
   * @default true
   */
  screenshots?: boolean;
  /**
   * If this option is true tracing will
   * - capture DOM snapshot on every action
   * - record network activity
   * @default true
   */
  snapshots?: boolean;
}
```

::: danger WARNING
이 옵션은 [**playwright**](https://vitest.dev/config/browser/playwright) provider에서만 지원됩니다.
:::
