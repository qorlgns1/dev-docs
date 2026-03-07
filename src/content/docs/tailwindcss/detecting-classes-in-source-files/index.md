---
title: "소스 파일에서 클래스 감지하기 - 핵심 개념 - Tailwind CSS"
description: "Tailwind는 프로젝트를 스캔해 유틸리티 클래스를 찾은 다음, 실제로 사용한 클래스에 기반해 필요한 모든 CSS를 생성하는 방식으로 동작합니다."
---

# 소스 파일에서 클래스 감지하기 - 핵심 개념 - Tailwind CSS

## 개요

Tailwind는 프로젝트를 스캔해 유틸리티 클래스를 찾은 다음, 실제로 사용한 클래스에 기반해 필요한 모든 CSS를 생성하는 방식으로 동작합니다.

이 방식은 CSS를 가능한 한 작게 유지해 주며, [arbitrary values](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values) 같은 기능을 가능하게 하는 이유이기도 합니다.

- 클래스가 감지되는 방식

Tailwind는 모든 소스 파일을 일반 텍스트로 취급하며, 어떤 방식으로도 파일을 코드로 실제 파싱하려고 하지 않습니다.

대신 Tailwind가 클래스 이름에서 기대하는 문자 기준으로, 파일 안에서 클래스일 가능성이 있는 모든 토큰을 찾습니다:

JSX

```
    export function Button({ color, children }) {  const colors = {    black: "bg-black text-white",    blue: "bg-blue-500 text-white",    white: "bg-white text-black",  };  return (    <button className={`${colors[color]} rounded-full px-2 py-1.5 font-sans text-sm/6 font-medium shadow`}>      {children}    </button>  );}
```

그다음 이 모든 토큰에 대해 CSS 생성을 시도하고, 프레임워크가 알고 있는 유틸리티 클래스에 매핑되지 않는 토큰은 버립니다.

- 동적 클래스 이름

Tailwind는 소스 파일을 일반 텍스트로 스캔하므로, 사용하는 프로그래밍 언어의 문자열 연결이나 보간을 이해할 방법이 없습니다.

클래스 이름을 동적으로 만들지 마세요

HTML

```
    <div class="text-{{ error ? 'red' : 'green' }}-600"></div>
```

위 예시에서는 `text-red-600`과 `text-green-600` 문자열이 존재하지 않기 때문에 Tailwind가 해당 클래스를 생성하지 않습니다.

대신, 사용하는 클래스 이름이 항상 완전한 형태로 존재하도록 하세요:

항상 완전한 클래스 이름을 사용하세요

HTML

```
    <div class="{{ error ? 'text-red-600' : 'text-green-600' }}"></div>
```

React나 Vue 같은 컴포넌트 라이브러리를 사용한다면, props로 클래스를 동적으로 만들지 않아야 한다는 뜻입니다:

props로 클래스 이름을 동적으로 만들지 마세요

JSX

```
    function Button({ color, children }) {  return <button className={`bg-${color}-600 hover:bg-${color}-500 ...`}>{children}</button>;}
```

대신, props를 빌드 시점에 정적으로 감지 가능한 완전한 클래스 이름에 매핑하세요:

항상 props를 정적 클래스 이름에 매핑하세요

JSX

```
    function Button({ color, children }) {  const colorVariants = {    blue: "bg-blue-600 hover:bg-blue-500",    red: "bg-red-600 hover:bg-red-500",  };  return <button className={`${colorVariants[color]} ...`}>{children}</button>;}
```

이 방식은 예를 들어 서로 다른 prop 값에 서로 다른 색조를 매핑할 수 있다는 추가 이점도 있습니다:

JSX

```
    function Button({ color, children }) {  const colorVariants = {    blue: "bg-blue-600 hover:bg-blue-500 text-white",    red: "bg-red-500 hover:bg-red-400 text-white",    yellow: "bg-yellow-300 hover:bg-yellow-400 text-black",  };  return <button className={`${colorVariants[color]} ...`}>{children}</button>;}
```

코드에서 항상 완전한 클래스 이름을 사용하기만 하면, Tailwind는 매번 모든 CSS를 정확하게 생성합니다.

- 어떤 파일이 스캔되는가

Tailwind는 다음 경우를 제외하고 프로젝트의 모든 파일을 클래스 이름 대상으로 스캔합니다:

- `.gitignore` 파일에 포함된 파일
- `node_modules` 디렉터리의 파일
- 이미지, 비디오, zip 파일 같은 바이너리 파일
- CSS 파일
- 일반적인 패키지 매니저 lock 파일

Tailwind가 기본적으로 무시하는 파일도 스캔해야 한다면, 해당 소스를 [명시적으로 등록](https://tailwindcss.com/docs/detecting-classes-in-source-files#explicitly-registering-sources)할 수 있습니다.

## 소스를 명시적으로 등록하기

스타일시트를 기준으로 한 상대 경로를 명시적으로 등록하려면 `@source`를 사용하세요:

CSS

```
    @import "tailwindcss";@source "../node_modules/@acmecorp/ui-lib";
```

이는 Tailwind로 빌드된 외부 라이브러리를 스캔해야 할 때 특히 유용합니다. 의존성은 보통 `.gitignore` 파일에 포함되어 있고, Tailwind가 기본적으로 무시하기 때문입니다.

- 기준 경로 설정하기

Tailwind는 기본적으로 클래스 이름 스캔 시작 지점으로 현재 작업 디렉터리를 사용합니다.

소스 감지의 기준 경로를 명시적으로 설정하려면 CSS에서 Tailwind를 가져올 때 `source()` 함수를 사용하세요:

CSS

```
    @import "tailwindcss" source("../src");
```

이는 빌드 명령이 각 프로젝트 루트가 아니라 모노레포 루트에서 실행되는 모노레포 환경에서 유용할 수 있습니다.

- 특정 경로 무시하기

클래스 이름을 스캔할 때 스타일시트 기준의 특정 경로를 무시하려면 `@source not`를 사용하세요:

CSS

```
    @import "tailwindcss";@source not "../src/components/legacy";
```

프로젝트에 레거시 컴포넌트나 서드파티 라이브러리처럼 Tailwind 클래스를 사용하지 않는 대규모 디렉터리가 있을 때 유용합니다.

- 자동 감지 비활성화하기

모든 소스를 명시적으로 등록하고 싶다면 `source(none)`으로 자동 소스 감지를 완전히 비활성화하세요:

CSS

```
    @import "tailwindcss" source(none);@source "../admin";@source "../shared";
```

이는 여러 Tailwind 스타일시트를 사용하는 프로젝트에서 각 스타일시트에 필요한 클래스만 포함되도록 보장하고 싶을 때 유용합니다.

## 특정 유틸리티 safelist에 추가하기

콘텐츠 파일에 존재하지 않더라도 Tailwind가 특정 클래스 이름을 생성하도록 보장해야 한다면, `@source inline()`을 사용해 강제로 생성하세요:

CSS

```
    @import "tailwindcss";@source inline("underline");
```

생성된 CSS

```
    .underline {  text-decoration-line: underline;}
```

- variant를 safelist에 추가하기

`@source inline()`을 사용해 variant가 포함된 클래스도 생성할 수 있습니다. 예를 들어 `underline` 클래스에 hover와 focus variant를 생성하려면, 소스 입력에 `{hover:,focus:,}`를 추가하세요:

CSS

```
    @import "tailwindcss";@source inline("{hover:,focus:,}underline");
```

생성된 CSS

```
    .underline {  text-decoration-line: underline;}@media (hover: hover) {  .hover\:underline:hover {    text-decoration-line: underline;  }}@media (focus: focus) {  .focus\:underline:focus {    text-decoration-line: underline;  }}
```

- 범위로 safelist 추가하기

소스 입력은 [brace expanded](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html)되므로 여러 클래스를 한 번에 생성할 수 있습니다. 예를 들어 hover variant가 포함된 모든 빨간 배경색을 생성하려면, 범위를 사용하세요:

CSS

```
    @import "tailwindcss";@source inline("{hover:,}bg-red-{50,{100..900..100},950}");
```

생성된 CSS

```
    .bg-red-50 {  background-color: var(--color-red-50);}.bg-red-100 {  background-color: var(--color-red-100);}.bg-red-200 {  background-color: var(--color-red-200);}/* ... */.bg-red-800 {  background-color: var(--color-red-800);}.bg-red-900 {  background-color: var(--color-red-900);}.bg-red-950 {  background-color: var(--color-red-950);}@media (hover: hover) {  .hover\:bg-red-50:hover {    background-color: var(--color-red-50);  }  /* ... */  .hover\:bg-red-950:hover {    background-color: var(--color-red-950);  }}
```

이렇게 하면 100부터 900까지 100 단위 증가의 빨간 배경색과, 처음과 마지막 색조인 50과 950이 함께 생성됩니다. 또한 각 클래스에 `hover:` variant도 추가됩니다.

- 클래스를 명시적으로 제외하기

소스 파일에서 감지되더라도 특정 클래스가 생성되지 않도록 하려면 `@source not inline()`을 사용하세요:

CSS

```
    @import "tailwindcss";@source not inline("{hover:,focus:,}bg-red-{50,{100..900..100},950}");
```

이렇게 하면 빨간 배경 유틸리티와 해당 hover, focus variant가 생성 대상에서 명시적으로 제외됩니다.
