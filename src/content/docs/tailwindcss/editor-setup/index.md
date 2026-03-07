---
title: "에디터 설정 - 시작하기 - Tailwind CSS"
description: "Tailwind CSS는 @theme, @variant, @source 같은 커스텀 CSS 문법을 사용하며, 일부 에디터에서는 이러한 규칙을 인식하지 못해 경고나 오류가 발생할 수 있습니다."
---

출처 URL: https://tailwindcss.com/docs/editor-setup

# 에디터 설정 - 시작하기 - Tailwind CSS

## 문법 지원

Tailwind CSS는 `@theme`, `@variant`, `@source` 같은 커스텀 CSS 문법을 사용하며, 일부 에디터에서는 이러한 규칙을 인식하지 못해 경고나 오류가 발생할 수 있습니다.

VS Code를 사용 중이라면, 공식 [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) 플러그인에 Tailwind가 사용하는 모든 커스텀 at-rule과 함수들을 지원하는 전용 Tailwind CSS 언어 모드가 포함되어 있습니다.

경우에 따라 에디터가 CSS 파일에서 기대하는 문법에 매우 엄격하다면, 기본 CSS linting/validation을 비활성화해야 할 수도 있습니다.

## Cursor

[Cursor](https://cursor.com/?utm_source=tailwind)는 컨텍스트 인식 자동완성과 내장 코딩 에이전트 같은 기능을 갖춘 AI 네이티브 코드 에디터입니다. VS Code 확장을 지원하므로, 이미 익숙한 Tailwind CSS 도구들이 별도 설정 없이 바로 동작합니다. 여기에는 공식 [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) 확장과 클래스 정렬을 위한 [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)이 포함됩니다.

![Cursor용 Tailwind CSS IntelliSense 확장](https://tailwindcss.com/_next/static/media/cursor-intellisense.dbd6aaee.png)

[Cursor](https://cursor.com/?utm_source=tailwind)를 확인하고 다운로드해 보세요.

## Zed

[Zed](https://zed.dev/?utm_source=tailwind)는 빠르고 현대적인 코드 에디터로, AI를 활용한 에이전트 기반 편집을 포함한 최첨단 개발 워크플로를 위해 처음부터 설계되었습니다. 별도 확장을 설치하거나 설정할 필요 없이 Tailwind CSS 자동완성, linting, hover 미리보기를 기본 지원합니다. 또한 Prettier와 긴밀하게 통합되어 있어, 공식 [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)을 설치하면 Zed에서 매끄럽게 동작합니다.

![Tailwind CSS IntelliSense를 통한 Zed의 Tailwind CSS 기본 지원](https://tailwindcss.com/_next/static/media/zed-intellisense.5d0c529d.png)

[Zed](https://zed.dev/?utm_source=tailwind)를 확인하고, [Tailwind CSS와 함께 동작하는 방식](https://zed.dev/docs/languages/tailwindcss?utm_source=tailwind)에 대해 더 알아보세요.

## VS Code용 IntelliSense

Visual Studio Code용 공식 [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) 확장은 자동완성, 문법 하이라이팅, linting 같은 고급 기능을 제공하여 Tailwind 개발 경험을 향상시킵니다.

![Visual Studio Code용 Tailwind CSS IntelliSense 확장](https://tailwindcss.com/_next/static/media/intellisense.64b4d269.png)

- **자동완성** — 유틸리티 클래스뿐 아니라 [CSS functions and directives](https://tailwindcss.com/docs/functions-and-directives)에 대한 지능형 제안을 제공합니다.
- **Linting** — CSS와 마크업 모두에서 오류와 잠재적인 버그를 강조 표시합니다.
- **Hover 미리보기** — 유틸리티 클래스 위에 마우스를 올리면 해당 클래스의 전체 CSS를 보여줍니다.
- **문법 하이라이팅** — 커스텀 CSS 문법을 사용하는 Tailwind 기능이 올바르게 하이라이트되도록 합니다.

자세한 내용은 [GitHub](https://github.com/tailwindcss/intellisense) 프로젝트를 확인하거나, 지금 바로 시작하려면 [Visual Studio Code에 추가](vscode:extension/bradlc.vscode-tailwindcss)하세요.

## Prettier로 클래스 정렬

Tailwind CSS용 공식 [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)을 유지 관리하고 있으며, 이 플러그인은 [권장 클래스 순서](https://tailwindcss.com/blog/automatic-class-sorting-with-prettier#how-classes-are-sorted)에 따라 클래스를 자동으로 정렬합니다.

![](https://tailwindcss.com/_next/static/media/prettier-banner.1039345a.jpg)

커스텀 Tailwind 설정과도 매끄럽게 동작하며, 단순한 Prettier 플러그인이기 때문에 Prettier가 동작하는 곳이라면 어디서든 사용할 수 있습니다. 즉, 모든 주요 에디터와 IDE는 물론 명령줄에서도 동작합니다.

HTML

```
    <!-- Before --><button class="text-white px-4 sm:px-8 py-2 sm:py-3 bg-sky-700 hover:bg-sky-800">Submit</button><!-- After --><button class="bg-sky-700 px-4 py-2 text-white hover:bg-sky-800 sm:px-8 sm:py-3">Submit</button>
```

자세한 내용과 시작 방법은 [GitHub](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)에서 확인하세요.

## JetBrains IDE

WebStorm, PhpStorm 등 JetBrains IDE는 HTML에서 지능형 Tailwind CSS 자동완성을 지원합니다.

[JetBrains IDE의 Tailwind CSS 지원에 대해 자세히 알아보기 →](https://www.jetbrains.com/help/webstorm/tailwind-css.html)
