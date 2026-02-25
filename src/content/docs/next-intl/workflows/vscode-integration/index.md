---
title: 'VSCode 통합'
description: '코드 에디터에서 바로 메시지를 관리하는 워크플로를 개선하려면, 을 지원하는 VSCode 확장을 사용할 수 있습니다.'
---

소스 URL: https://next-intl.dev/docs/workflows/vscode-integration

[문서](https://next-intl.dev/docs/getting-started "Docs")[워크플로 및 통합](https://next-intl.dev/docs/workflows "Workflows & integrations")VSCode 통합

# VSCode 통합

동영상으로 보는 것을 선호하시나요?

[에디터 도구](https://learn.next-intl.dev/chapters/03-translations/05-tooling)

코드 에디터에서 바로 메시지를 관리하는 워크플로를 개선하려면, `next-intl`을 지원하는 VSCode 확장을 사용할 수 있습니다.

다음 확장들이 `next-intl`을 지원하는 것으로 알려져 있습니다:

  1. [i18n Ally](https://next-intl.dev/docs/workflows/vscode-integration#i18n-ally)
  2. [Loccy](https://next-intl.dev/docs/workflows/vscode-integration#loccy)
  3. [Sherlock](https://next-intl.dev/docs/workflows/vscode-integration#sherlock)

## i18n Ally[](https://next-intl.dev/docs/workflows/vscode-integration#i18n-ally)

**주요 기능:**

  * 메시지 추출
  * 인라인 주석
  * 인라인 메시지 편집
  * 기계 번역

**설정:**

  1. [i18n Ally](https://marketplace.visualstudio.com/items?itemName=lokalise.i18n-ally)를 설치합니다
  2. [워크스페이스 설정](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings)을 통해 프로젝트에서 확장을 구성합니다

.vscode/settings.json
```
    "i18n-ally.localesPaths": ["./path/to/your/messages"], // E.g. "./messages"
    "i18n-ally.keystyle": "nested"
```

자세한 내용은 [i18n Ally 문서](https://github.com/lokalise/i18n-ally/wiki)에서 확인하세요.

## Loccy[](https://next-intl.dev/docs/workflows/vscode-integration#loccy)

**주요 기능:**

  * 메시지 추출
  * 인라인 주석
  * 인라인 메시지 편집
  * 메시지 생성, 기계 번역 등을 위한 AI 강화 기능(유료)

**설정:**

  1. [Loccy](https://loccy.dev)를 설치하면 i18n 설정을 자동으로 감지합니다
  2. 고급 구성을 위해 명령 팔레트에서 `Loccy: Create Config File`을 실행합니다

자세한 내용은 [Loccy 웹사이트](https://loccy.dev)에서 확인하세요.

## Sherlock[](https://next-intl.dev/docs/workflows/vscode-integration#sherlock)

**주요 기능:**

  * 메시지 추출
  * 인라인 주석
  * 인라인 메시지 편집

**설정:**

  1. [Sherlock VS Code 확장](https://marketplace.visualstudio.com/items?itemName=inlang.vs-code-extension)을 설치합니다
  2. `project.inlang/settings.json`을 통해 프로젝트에서 확장을 구성합니다:

project.inlang/settings.json
```
    {
      "$schema": "https://inlang.com/schema/project-settings",
      "sourceLanguageTag": "en",
      "languageTags": ["en", "de"],
      "modules": [
        "https://cdn.jsdelivr.net/npm/@inlang/plugin-next-intl@latest/dist/index.js"
      ],
      "plugin.inlang.nextIntl": {
        "pathPattern": "./messages/{languageTag}.json"
      }
    }
```

자세한 내용은 [inlang 문서](https://inlang.com/m/193hsyds/plugin-inlang-nextIntl)에서 확인하세요.

