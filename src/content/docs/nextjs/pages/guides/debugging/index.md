---
title: '가이드: 디버깅'
description: '이 문서는 VS Code 디버거, Chrome DevTools, Firefox DevTools를 이용해 소스 맵을 온전히 활용하면서 Next.js 프런트엔드와 백엔드 코드를 디버깅하는 방법을 설명합니다.'
---

# 가이드: 디버깅 | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/debugging

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)디버깅

페이지 복사

# Next.js에서 디버깅 도구를 사용하는 방법

마지막 업데이트 2026년 2월 20일

이 문서는 [VS Code 디버거](https://code.visualstudio.com/docs/editor/debugging), [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools), [Firefox DevTools](https://firefox-source-docs.mozilla.org/devtools-user/)를 이용해 소스 맵을 온전히 활용하면서 Next.js 프런트엔드와 백엔드 코드를 디버깅하는 방법을 설명합니다.

Node.js에 연결할 수 있는 디버거라면 Next.js 애플리케이션 디버깅에도 사용할 수 있습니다. 자세한 내용은 Node.js [디버깅 가이드](https://nodejs.org/en/docs/guides/debugging-getting-started/)를 참고하세요.

## VS Code로 디버깅하기[](https://nextjs.org/docs/pages/guides/debugging#debugging-with-vs-code)

프로젝트 루트에 `.vscode/launch.json` 파일을 만들고 다음 내용을 추가하세요:

launch.json
[code]
    {
      "version": "0.2.0",
      "configurations": [
        {
          "name": "Next.js: debug server-side",
          "type": "node-terminal",
          "request": "launch",
          "command": "npm run dev -- --inspect"
        },
        {
          "name": "Next.js: debug client-side",
          "type": "chrome",
          "request": "launch",
          "url": "http://localhost:3000"
        },
        {
          "name": "Next.js: debug client-side (Firefox)",
          "type": "firefox",
          "request": "launch",
          "url": "http://localhost:3000",
          "reAttach": true,
          "pathMappings": [
            {
              "url": "webpack://_N_E",
              "path": "${workspaceFolder}"
            }
          ]
        },
        {
          "name": "Next.js: debug full stack",
          "type": "node",
          "request": "launch",
          "program": "${workspaceFolder}/node_modules/next/dist/bin/next",
          "runtimeArgs": ["--inspect"],
          "skipFiles": ["<node_internals>/**"],
          "serverReadyAction": {
            "action": "debugWithEdge",
            "killOnServerStop": true,
            "pattern": "- Local:.+(https?://.+)",
            "uriFormat": "%s",
            "webRoot": "${workspaceFolder}"
          }
        }
      ]
    }
[/code]

> **참고**: VS Code에서 Firefox 디버깅을 사용하려면 [Firefox Debugger 확장](https://marketplace.visualstudio.com/items?itemName=firefox-devtools.vscode-firefox-debug)을 설치해야 합니다.

Yarn을 사용 중이면 `npm run dev` 대신 `yarn dev`, pnpm을 사용 중이면 `pnpm dev`로 바꿀 수 있습니다.

"Next.js: debug full stack" 구성에서 `serverReadyAction.action`은 서버가 준비되었을 때 열 브라우저를 지정합니다. `debugWithEdge`는 Edge 브라우저를 실행한다는 의미입니다. Chrome을 사용한다면 값을 `debugWithChrome`으로 바꾸세요.

애플리케이션이 시작되는 포트 번호를 [변경 중](https://nextjs.org/docs/pages/api-reference/cli/next#next-dev-options)이라면 `http://localhost:3000`의 `3000`을 사용 중인 포트로 교체하세요.

Next.js를 루트가 아닌 다른 디렉터리(예: Turborepo 사용 시)에서 실행한다면 서버 사이드와 풀스택 디버깅 작업에 `cwd`를 추가해야 합니다. 예: `"cwd": "${workspaceFolder}/apps/web"`.

이제 디버그 패널(Windows/Linux는 `Ctrl+Shift+D`, macOS는 `⇧+⌘+D`)로 이동해 실행 구성을 선택한 뒤 `F5`를 누르거나 커맨드 팔레트에서 **Debug: Start Debugging**을 선택해 디버깅 세션을 시작하세요.

## Jetbrains WebStorm의 디버거 사용하기[](https://nextjs.org/docs/pages/guides/debugging#using-the-debugger-in-jetbrains-webstorm)

런타임 구성을 표시하는 드롭다운 메뉴를 클릭하고 `Edit Configurations...`를 선택하세요. URL이 `http://localhost:3000`인 `JavaScript Debug` 구성을 만듭니다. 필요에 따라(예: 디버깅용 브라우저, 프로젝트 파일로 저장) 사용자 지정한 뒤 `OK`를 클릭합니다. 이 디버그 구성을 실행하면 선택한 브라우저가 자동으로 열립니다. 이 시점에는 NextJS Node 애플리케이션과 클라이언트/브라우저 애플리케이션 두 개가 디버그 모드에 진입해야 합니다.

## 브라우저 DevTools로 디버깅하기[](https://nextjs.org/docs/pages/guides/debugging#debugging-with-browser-devtools)

### 클라이언트 사이드 코드[](https://nextjs.org/docs/pages/guides/debugging#client-side-code)

`next dev`, `npm run dev`, `yarn dev` 중 하나를 실행해 평소처럼 개발 서버를 시작합니다. 서버가 시작되면 선호하는 브라우저에서 `http://localhost:3000`(또는 대체 URL)을 엽니다.

Chrome:

  * Chrome 개발자 도구를 엽니다(Windows/Linux는 `Ctrl+Shift+J`, macOS는 `⌥+⌘+I`)
  * **Sources** 탭으로 이동합니다



Firefox:

  * Firefox 개발자 도구를 엽니다(Windows/Linux는 `Ctrl+Shift+I`, macOS는 `⌥+⌘+I`)
  * **Debugger** 탭으로 이동합니다



두 브라우저 모두 클라이언트 사이드 코드가 [`debugger`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/debugger) 문에 도달하면 실행이 일시 중지되고 해당 파일이 디버그 영역에 표시됩니다. 파일을 검색해 직접 브레이크포인트를 설정할 수도 있습니다.

  * Chrome: Windows/Linux는 `Ctrl+P`, macOS는 `⌘+P`
  * Firefox: Windows/Linux는 `Ctrl+P`, macOS는 `⌘+P`, 또는 왼쪽 패널의 파일 트리를 사용



검색할 때 소스 파일 경로는 `webpack://_N_E/./`로 시작한다는 점을 참고하세요.

### React Developer Tools[](https://nextjs.org/docs/pages/guides/debugging#react-developer-tools)

React 전용 디버깅을 위해 [React Developer Tools](https://react.dev/learn/react-developer-tools) 브라우저 확장을 설치하세요. 이 필수 도구로 다음을 수행할 수 있습니다.

  * React 컴포넌트 검사
  * props와 state 편집
  * 성능 문제 식별



### 서버 사이드 코드[](https://nextjs.org/docs/pages/guides/debugging#server-side-code)

브라우저 DevTools로 서버 사이드 Next.js 코드를 디버깅하려면 `--inspect` 플래그를 전달해야 합니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm dev --inspect
[/code]

`--inspect` 값은 기본 Node.js 프로세스에 전달됩니다. 고급 사용 사례는 [`--inspect` 문서](https://nodejs.org/api/cli.html#--inspecthostport)를 참고하세요.

> **알아두면 좋아요**: Docker 컨테이너처럼 localhost 밖에서 원격 디버깅을 허용하려면 `--inspect=0.0.0.0`을 사용하세요.

`--inspect` 플래그로 Next.js dev 서버를 실행하면 다음과 비슷하게 표시됩니다.

Terminal
[code]
    Debugger listening on ws://127.0.0.1:9229/0cf90313-350d-4466-a748-cd60f4e47c95
    For help, see: https://nodejs.org/en/docs/inspector
    ready - started server on 0.0.0.0:3000, url: http://localhost:3000
[/code]

Chrome:

  1. 새 탭을 열고 `chrome://inspect`로 이동합니다
  2. **Remote Target** 섹션에서 Next.js 애플리케이션을 찾습니다
  3. 별도 DevTools 창을 열기 위해 **inspect**를 클릭합니다
  4. **Sources** 탭으로 이동합니다



Firefox:

  1. 새 탭을 열고 `about:debugging`으로 이동합니다
  2. 왼쪽 사이드바에서 **This Firefox**를 클릭합니다
  3. **Remote Targets** 아래에서 Next.js 애플리케이션을 찾습니다
  4. 디버거를 열려면 **Inspect**를 클릭합니다
  5. **Debugger** 탭으로 이동합니다



서버 사이드 디버깅은 클라이언트 사이드 디버깅과 거의 동일하게 동작합니다. 파일을 검색할 때(`Ctrl+P`/`⌘+P`) 소스 파일 경로는 `webpack://{application-name}/./`로 시작합니다(`{application-name}`은 `package.json`에 정의된 앱 이름으로 바뀝니다).

`--inspect-brk` 또는 `--inspect-wait`를 사용하려면 대신 `NODE_OPTIONS`를 지정해야 합니다. 예: `NODE_OPTIONS=--inspect-brk next dev`.

### 브라우저 DevTools로 서버 오류 검사하기[](https://nextjs.org/docs/pages/guides/debugging#inspect-server-errors-with-browser-devtools)

에러가 발생하면 소스 코드를 확인해 근본 원인을 추적할 수 있습니다.

Next.js는 오류 오버레이의 Next.js 버전 표시 아래에 Node.js 아이콘을 보여줍니다. 아이콘을 클릭하면 DevTools URL이 클립보드로 복사됩니다. 해당 URL로 새 브라우저 탭을 열어 Next.js 서버 프로세스를 검사할 수 있습니다.

### Windows에서 디버깅하기[](https://nextjs.org/docs/pages/guides/debugging#debugging-on-windows)

Windows Defender가 비활성화되어 있는지 확인하세요. 이 외부 서비스는 _읽는 모든 파일_ 을 검사하며, `next dev` 사용 시 Fast Refresh 시간이 크게 늘어나는 것으로 보고되었습니다. 이는 Next.js와 무관한 알려진 이슈지만 Next.js 개발에 영향을 줍니다.

## 추가 정보[](https://nextjs.org/docs/pages/guides/debugging#more-information)

JavaScript 디버거 사용법을 더 알아보려면 다음 문서를 참고하세요.

  * [VS Code의 Node.js 디버깅: Breakpoints](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_breakpoints)
  * [Chrome DevTools: Debug JavaScript](https://developers.google.com/web/tools/chrome-devtools/javascript)
  * [Firefox DevTools: Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/)



도움이 되었나요?

지원됨.

전송
