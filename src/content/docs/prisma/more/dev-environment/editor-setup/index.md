---
title: "에디터 설정"
description: "Prisma ORM으로 애플리케이션을 개발할 때 최적의 개발자 경험을 위해 에디터와 IDE를 구성하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/more/dev-environment/editor-setup

# 에디터 설정

Prisma ORM으로 애플리케이션을 개발할 때 최적의 개발자 경험을 위해 에디터와 IDE를 구성하는 방법을 알아보세요.

이 페이지에서는 Prisma ORM을 사용할 때 최적의 개발자 경험을 위해 에디터를 구성하는 방법을 설명합니다.

여기에서 사용 중인 에디터를 찾을 수 없다면, [기능 요청을 등록](https://github.com/prisma/prisma/issues/new?assignees=&labels=&template=feature_request.md&title=%22)하여 해당 에디터(예: 구문 강조 및 자동 포맷팅)에 대한 전용 지원을 요청해 주세요.

## VS Code 확장 프로그램

공식 [Prisma VS Code 확장 프로그램](https://marketplace.visualstudio.com/items?itemName=Prisma.prisma)을 설치할 수 있습니다. 이 확장 프로그램은 Prisma ORM으로 애플리케이션을 개발할 때 VS Code에 추가 기능을 제공합니다.

- `schema.prisma` 구문 강조
- Linting
  - 진단 도구를 사용해 스키마 파일을 입력하는 동안 오류와 경고를 표시합니다.
- 코드 완성
  - 입력하는 동안 심볼에 대한 완성 결과가 표시됩니다.
  - `Ctrl+Space` 단축키로 수동 실행할 수 있습니다.
- 문서 도움말
  - 완성 결과가 제공될 때 해당 결과의 문서가 팝업으로 표시됩니다.
- 호버 시 빠른 정보
  - 모델 및 enum의 문서 주석(`///`)이 해당 사용 위치에 마우스를 올리면 표시됩니다.
- 정의로 이동
  - 모델 또는 enum 선언으로 점프하거나 미리볼 수 있습니다.
- 포맷팅
  - 수동으로 또는 저장 시(구성된 경우) 코드를 포맷할 수 있습니다.
    - 저장 시 자동 포맷을 사용하려면 `settings.json` 파일에 다음을 추가하세요.

```
"editor.formatOnSave": true
```

      * `prettier`와 함께 포맷팅을 활성화하려면 `settings.json` 파일에 다음을 추가하세요.

[Prisma용 Prettier 플러그인](https://github.com/umidbekk/prettier-plugin-prisma)을 사용하세요.

```
"[prisma]": {
              "editor.defaultFormatter": "Prisma.prisma"
            },
```

- 이름 바꾸기
  - 모델, enum, 필드 및 enum 값을 이름 변경할 수 있습니다.
    - 모델 또는 enum 내부를 클릭하고 `F2`를 누른 뒤 원하는 새 이름을 입력하고 `Enter`를 누르세요.
    - 모든 사용처 이름이 함께 변경됩니다.
    - 스키마에 `@map` 또는 `@@map`이 자동으로 적용됩니다.
- 빠른 수정
  - 모델 및 enum 이름의 오타를 빠르게 수정합니다.
  - 한 번의 클릭으로 새 모델과 enum을 생성합니다.

VS Code를 사용 중이라면 [VS Code agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)를 사용해 “create Postgres database” 또는 “apply schema migration” 같은 프롬프트를 채팅에 직접 입력할 수 있습니다. VS Code agent는 내부적으로 필요한 Prisma CLI 호출과 API 호출을 모두 자동으로 처리합니다. 자세한 내용은 [VS Code Agent 문서](https://docs.prisma.io/docs/guides/postgres/vscode#agent-mode)를 참고하세요.

## 커뮤니티 프로젝트

> **참고** : 커뮤니티 프로젝트는 Prisma에서 유지보수하거나 공식 지원하지 않으며, 일부 기능은 동기화되지 않았을 수 있습니다. 사용 시 주의하세요.

- Emacs
  - [emacs-prisma-mode](https://github.com/pimeys/emacs-prisma-mode)는 Prisma Schema Language 구문 강조를 제공하며 Prisma Language Server를 사용합니다.

- Vim
  - [vim-prisma](https://github.com/prisma/vim-prisma)는 Prisma Schema Language의 파일 감지 및 구문 강조를 제공합니다.

- neovim
  - [coc-prisma](https://github.com/pantharshit00/coc-prisma)는 Prisma Language Server를 구현합니다.

- JetBrains IDE
  - [Prisma ORM](https://plugins.jetbrains.com/plugin/20686-prisma-orm) JetBrains에서 제공합니다. 이 플러그인은 PSL 문법, 구문 강조, LSP 등을 제공합니다.

- Sublime Text
  - [Prisma](https://packagecontrol.io/packages/Prisma) \- Sublime Text 3 및 4용 - Prisma Schema Language 구문 강조를 제공합니다. ([소스 코드](https://github.com/Sublime-Instincts/PrismaHighlight/))
  - [LSP-prisma](https://packagecontrol.io/packages/LSP-prisma) \- Sublime Text 4용 - Prisma 스키마 파일을 위한 Language Server 헬퍼 패키지로, Prisma의 Language Server를 사용해 linting, 오류 검사, 포맷팅, 자동완성, 이름 변경 등을 제공합니다. 참고: Prisma 패키지가 설치되어 있어야 합니다. ([소스 코드](https://github.com/Sublime-Instincts/LSP-prisma))

- nova
  - [nova](https://extensions.panic.com/extensions/robb-j/robb-j.Prisma/)는 Prisma Schema Language 구문 강조를 제공하며 Prisma Language Server를 사용합니다.

- Helix
  - [Helix](https://helix-editor.com/)는 (버전 22.08부터) Prisma Schema Language 구문 강조를 제공하며 Prisma Language Server를 사용합니다.

- CLI 자동완성

#

- inshellisense

[`inshellisense`](https://github.com/microsoft/inshellisense/tree/main)를 사용하면 Prisma CLI에 대해 IDE 스타일 자동완성을 사용할 수 있습니다. 지원 대상: bash, zsh, fish, pwsh, powershell (Windows Powershell).

설치하려면 다음을 실행하세요.

npm

pnpm

yarn

bun

```
    npm install -g @microsoft/inshellisense
```
