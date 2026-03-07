---
title: "browser.orchestratorScripts"
description: "테스트 iframe이 초기화되기 전에 오케스트레이터 HTML에 주입되어야 하는 커스텀 스크립트입니다. 이 HTML 문서는 iframe 설정만 수행하며, 실제로 여러분의 코드를 import하지는 않습니다."
---

출처 URL: https://vitest.dev/config/browser/orchestratorscripts

# browser.orchestratorScripts

- **유형:** `BrowserScript[]`
- **기본값:** `[]`

테스트 iframe이 초기화되기 전에 오케스트레이터 HTML에 주입되어야 하는 커스텀 스크립트입니다. 이 HTML 문서는 iframe 설정만 수행하며, 실제로 여러분의 코드를 import하지는 않습니다.

스크립트의 `src`와 `content`는 Vite 플러그인에 의해 처리됩니다. 스크립트는 다음 형태로 제공되어야 합니다.

```ts
export interface BrowserScript {
  /**
   * If "content" is provided and type is "module", this will be its identifier.
   *
   * If you are using TypeScript, you can add `.ts` extension here for example.
   * @default `injected-${index}.js`
   */
  id?: string;
  /**
   * JavaScript content to be injected. This string is processed by Vite plugins if type is "module".
   *
   * You can use `id` to give Vite a hint about the file extension.
   */
  content?: string;
  /**
   * Path to the script. This value is resolved by Vite so it can be a node module or a file path.
   */
  src?: string;
  /**
   * If the script should be loaded asynchronously.
   */
  async?: boolean;
  /**
   * Script type.
   * @default 'module'
   */
  type?: string;
}
```
