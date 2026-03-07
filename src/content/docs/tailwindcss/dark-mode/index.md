---
title: "다크 모드 - 핵심 개념 - Tailwind CSS"
description: "다크 모드는 이제 많은 운영 체제에서 기본 기능이 되었기 때문에, 기본 디자인과 함께 웹사이트의 다크 버전을 설계하는 일이 점점 더 일반적이 되고 있습니다."
---

출처 URL: https://tailwindcss.com/docs/dark-mode

# 다크 모드 - 핵심 개념 - Tailwind CSS

## 개요

다크 모드는 이제 많은 운영 체제에서 기본 기능이 되었기 때문에, 기본 디자인과 함께 웹사이트의 다크 버전을 설계하는 일이 점점 더 일반적이 되고 있습니다.

이를 최대한 쉽게 만들기 위해 Tailwind는 다크 모드가 활성화되었을 때 사이트를 다르게 스타일링할 수 있는 `dark` variant를 제공합니다.

라이트 모드

거꾸로도 씁니다

Zero Gravity Pen은 거꾸로를 포함해 어떤 방향에서도 글을 쓸 수 있습니다. 심지어 우주 공간에서도 작동합니다.

다크 모드

거꾸로도 씁니다

Zero Gravity Pen은 거꾸로를 포함해 어떤 방향에서도 글을 쓸 수 있습니다. 심지어 우주 공간에서도 작동합니다.

```
    <div class="bg-white dark:bg-gray-800 rounded-lg px-6 py-8 ring shadow-xl ring-gray-900/5">  <div>    <span class="inline-flex items-center justify-center rounded-md bg-indigo-500 p-2 shadow-lg">      <svg class="h-6 w-6 stroke-white" ...>        <!-- ... -->      </svg>    </span>  </div>  <h3 class="text-gray-900 dark:text-white mt-5 text-base font-medium tracking-tight ">Writes upside-down</h3>  <p class="text-gray-500 dark:text-gray-400 mt-2 text-sm ">    The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer space.  </p></div>
```

기본적으로 이는 `prefers-color-scheme` CSS media feature를 사용하지만, dark variant를 재정의하면 [다크 모드를 수동으로 전환](https://tailwindcss.com/docs/dark-mode#toggling-dark-mode-manually)할 수 있는 사이트를 만들 수도 있습니다.

## 다크 모드 수동 전환

다크 테마를 `prefers-color-scheme` media query 대신 CSS selector로 제어하고 싶다면, `dark` variant를 재정의해 커스텀 selector를 사용하세요:

app.css

```
    @import "tailwindcss";@custom-variant dark (&:where(.dark, .dark *));
```

이제 `dark:*` 유틸리티는 `prefers-color-scheme` 기준으로 적용되는 대신, HTML 트리의 상위 어딘가에 `dark` class가 존재할 때마다 적용됩니다:

HTML

```
    <html class="dark">  <body>    <div class="bg-white dark:bg-black">      <!-- ... -->    </div>  </body></html>
```

`html` element에 `dark` class를 어떻게 추가할지는 자유지만, 일반적으로는 `class` attribute를 업데이트하고 그 선호도를 `localStorage` 같은 곳에 동기화하는 약간의 JavaScript를 사용하는 방식이 많이 쓰입니다.

- data attribute 사용

class 대신 data attribute로 다크 모드를 활성화하려면, attribute selector로 `dark` variant를 재정의하면 됩니다:

app.css

```
    @import "tailwindcss";@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

이제 트리 상위 어딘가에서 `data-theme` attribute가 `dark`로 설정될 때마다 다크 모드 유틸리티가 적용됩니다:

HTML

```
    <html data-theme="dark">  <body>    <div class="bg-white dark:bg-black">      <!-- ... -->    </div>  </body></html>
```

- 시스템 테마 지원

라이트 모드, 다크 모드, 시스템 테마를 모두 지원하는 3단계 테마 토글을 만들려면, 커스텀 다크 모드 selector와 [`window.matchMedia()` API](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)를 사용해 시스템 테마를 감지하고 필요할 때 `html` element를 업데이트하세요.

다음은 라이트 모드와 다크 모드를 지원하면서 운영 체제 설정도 존중하는 간단한 예시입니다:

spaghetti.js

```
    // On page load or when changing themes, best to add inline in `head` to avoid FOUCdocument.documentElement.classList.toggle(  "dark",  localStorage.theme === "dark" ||    (!("theme" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches),);// Whenever the user explicitly chooses light modelocalStorage.theme = "light";// Whenever the user explicitly chooses dark modelocalStorage.theme = "dark";// Whenever the user explicitly chooses to respect the OS preferencelocalStorage.removeItem("theme");
```

다시 말해 이 부분은 원하는 방식으로 자유롭게 관리할 수 있습니다. 선호도를 데이터베이스에 서버 측으로 저장하고 서버에서 class를 렌더링해도 됩니다. 전적으로 여러분의 선택입니다.
