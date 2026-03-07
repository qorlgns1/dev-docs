---
title: "browser.instances"
description: "여러 브라우저 설정을 정의합니다. 각 설정에는 최소한  필드가 있어야 합니다."
---

출처 URL: https://vitest.dev/config/browser/instances

# browser.instances

- **유형:** `BrowserConfig`
- **기본값:** `[]`

여러 브라우저 설정을 정의합니다. 각 설정에는 최소한 `browser` 필드가 있어야 합니다.

[project options](https://vitest.dev/config/)의 대부분(아이콘으로 표시되지 않은 항목)과 `browser.testerHtmlPath` 같은 일부 `browser` 옵션을 지정할 수 있습니다.

::: warning
모든 브라우저 설정은 루트 설정의 옵션을 상속합니다:

```ts{3,9} [vitest.config.ts]
export default defineConfig({
  test: {
    setupFile: ['./root-setup-file.js'],
    browser: {
      enabled: true,
      testerHtmlPath: './custom-path.html',
      instances: [
        {
          // will have both setup files: "root" and "browser"
          setupFile: ['./browser-setup-file.js'],
          // implicitly has "testerHtmlPath" from the root config // [!code warning]
          // testerHtmlPath: './custom-path.html', // [!code warning]
        },
      ],
    },
  },
})
```

더 많은 예시는 ["Multiple Setups" guide](https://vitest.dev/guide/browser/multiple-setups)를 참고하세요.
:::

사용 가능한 `browser` 옵션 목록:

- `browser` (브라우저 이름)
- `headless`
- `locators`
- `viewport`
- `testerHtmlPath`
- `screenshotDirectory`
- `screenshotFailures`
- `provider`

내부적으로 Vitest는 이러한 인스턴스를 별도의 [test projects](https://vitest.dev/api/advanced/test-project)로 변환하며, 캐싱 성능 향상을 위해 단일 Vite 서버를 공유합니다.
