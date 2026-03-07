---
title: "반응형 디자인 - 핵심 개념 - Tailwind CSS"
description: "Tailwind의 모든 유틸리티 클래스는 다양한 브레이크포인트에서 조건부로 적용할 수 있어, HTML을 벗어나지 않고도 복잡한 반응형 인터페이스를 매우 쉽게 구축할 수 있..."
---

Source URL: https://tailwindcss.com/docs/responsive-design

# 반응형 디자인 - 핵심 개념 - Tailwind CSS

## 개요

Tailwind의 모든 유틸리티 클래스는 서로 다른 브레이크포인트에서 조건부로 적용할 수 있으므로, HTML을 벗어나지 않고도 복잡한 반응형 인터페이스를 아주 쉽게 만들 수 있습니다.

먼저 문서의 `<head>`에 [viewport meta tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)를 추가했는지 확인하세요:

index.html

```
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

그다음 특정 브레이크포인트에서만 적용되는 유틸리티를 추가하려면, 유틸리티 앞에 브레이크포인트 이름과 `:` 문자를 붙이면 됩니다:

HTML

```
    <!-- Width of 16 by default, 32 on medium screens, and 48 on large screens --><img class="w-16 md:w-32 lg:w-48" src="..." />
```

기본적으로는 일반적인 디바이스 해상도를 참고한 다섯 가지 브레이크포인트가 있습니다:

| Breakpoint prefix | Minimum width    | CSS                               |
| ----------------- | ---------------- | --------------------------------- |
| `sm`              | 40rem _(640px)_  | `@media (width >= 40rem) { ... }` |
| `md`              | 48rem _(768px)_  | `@media (width >= 48rem) { ... }` |
| `lg`              | 64rem _(1024px)_ | `@media (width >= 64rem) { ... }` |
| `xl`              | 80rem _(1280px)_ | `@media (width >= 80rem) { ... }` |
| `2xl`             | 96rem _(1536px)_ | `@media (width >= 96rem) { ... }` |

이 방식은 **프레임워크의 모든 유틸리티 클래스**에 동작하므로, 특정 브레이크포인트에서 문자 간격이나 커서 스타일 같은 것까지 사실상 무엇이든 변경할 수 있습니다.

다음은 작은 화면에서는 세로로 쌓이는 레이아웃을, 큰 화면에서는 좌우 배치 레이아웃을 사용하는 마케팅 페이지 컴포넌트의 간단한 예시입니다:

```
    <div class="mx-auto max-w-md overflow-hidden rounded-xl bg-white shadow-md md:max-w-2xl">  <div class="md:flex">    <div class="md:shrink-0">      <img        class="h-48 w-full object-cover md:h-full md:w-48"        src="/img/building.jpg"        alt="Modern building architecture"      />    </div>    <div class="p-8">      <div class="text-sm font-semibold tracking-wide text-indigo-500 uppercase">Company retreats</div>      <a href="#" class="mt-1 block text-lg leading-tight font-medium text-black hover:underline">        Incredible accommodation for your team      </a>      <p class="mt-2 text-gray-500">        Looking to take your team away on a retreat to enjoy awesome food and take in some sunshine? We have a list of        places to do just that.      </p>    </div>  </div></div>
```

위 예시는 다음과 같이 동작합니다:

- 기본적으로 바깥 `div`는 `display: block`이지만, `md:flex` 유틸리티를 추가하면 중간 화면 이상에서 `display: flex`가 됩니다.
- 부모가 flex 컨테이너일 때는 이미지가 절대 줄어들지 않도록 해야 하므로, 중간 화면 이상에서 축소를 막기 위해 `md:shrink-0`를 추가했습니다. 기술적으로는 작은 화면에서 영향이 없으므로 `shrink-0`만 써도 되지만, `md` 화면에서만 중요한 설정이기 때문에 클래스 이름에서 이를 명확히 하는 것이 좋습니다.
- 작은 화면에서는 이미지가 기본적으로 자동 전체 너비입니다. 중간 화면 이상에서는 `md:h-full md:w-48`을 사용해 너비를 고정 크기로 제한하고 이미지가 전체 높이를 채우게 했습니다.

이 예시에서는 브레이크포인트를 하나만 사용했지만, `sm`, `lg`, `xl`, `2xl` 반응형 접두사를 사용해 다른 크기에서도 이 컴포넌트를 쉽게 커스터마이즈할 수 있습니다.

## 모바일 우선 방식으로 작업하기

Tailwind는 Bootstrap 같은 다른 프레임워크에서 익숙할 수 있는 방식과 비슷한 모바일 우선 브레이크포인트 시스템을 사용합니다.

즉, 접두사가 없는 유틸리티(`uppercase` 같은)는 모든 화면 크기에서 적용되고, 접두사가 있는 유틸리티(`md:uppercase` 같은)는 지정한 브레이크포인트 _이상_ 에서만 적용됩니다.

- 모바일 화면 타겟팅

이 접근 방식에서 사람들이 가장 자주 헷갈리는 점은 모바일용 스타일을 지정할 때 `sm:` 접두사 버전이 아니라, 접두사 없는 유틸리티 버전을 사용해야 한다는 것입니다. `sm:`을 "작은 화면에서"라고 생각하지 말고, "small _breakpoint_ 에서"라고 생각하세요.

모바일 디바이스를 타겟팅하기 위해 `sm:`을 사용하지 마세요

HTML

```
    <!-- This will only center text on screens 640px and wider, not on small screens --><div class="sm:text-center"></div>
```

모바일은 접두사 없는 유틸리티로 타겟팅하고, 더 큰 브레이크포인트에서 이를 오버라이드하세요

HTML

```
    <!-- This will center text on mobile, and left align it on screens 640px and wider --><div class="text-center sm:text-left"></div>
```

이 때문에 보통은 먼저 디자인의 모바일 레이아웃을 구현하고, 이후 `sm` 화면에 필요한 변경을 얹고, 그다음 `md` 화면 변경을 추가하는 식으로 진행하는 것이 좋습니다.

- 브레이크포인트 범위 타겟팅

기본적으로 `md:flex` 같은 규칙으로 적용한 스타일은 해당 브레이크포인트에서 적용되어 더 큰 브레이크포인트에서도 계속 유지됩니다.

특정 브레이크포인트 범위에서만 유틸리티를 적용하려면, `md` 같은 반응형 variant를 `max-*` variant와 함께 쌓아 해당 스타일을 특정 범위로 제한하세요:

HTML

```
    <div class="md:max-xl:flex">  <!-- ... --></div>
```

Tailwind는 각 브레이크포인트에 대응하는 `max-*` variant를 생성하므로, 기본 제공 variant는 다음과 같습니다:

| Variant   | Media query                      |
| --------- | -------------------------------- |
| `max-sm`  | `@media (width < 40rem) { ... }` |
| `max-md`  | `@media (width < 48rem) { ... }` |
| `max-lg`  | `@media (width < 64rem) { ... }` |
| `max-xl`  | `@media (width < 80rem) { ... }` |
| `max-2xl` | `@media (width < 96rem) { ... }` |

- 단일 브레이크포인트 타겟팅

단일 브레이크포인트를 타겟팅하려면, `md` 같은 반응형 variant를 다음 브레이크포인트의 `max-*` variant와 함께 쌓아 해당 브레이크포인트 범위를 지정하세요:

HTML

```
    <div class="md:max-lg:flex">  <!-- ... --></div>
```

자세한 내용은 [브레이크포인트 범위 타겟팅](https://tailwindcss.com/docs/responsive-design#targeting-a-breakpoint-range)을 참고하세요.

## 커스텀 브레이크포인트 사용하기

- 테마 커스터마이징

브레이크포인트를 커스터마이징하려면 `--breakpoint-*` 테마 변수를 사용하세요:

app.css

```
    @import "tailwindcss";@theme {  --breakpoint-xs: 30rem;  --breakpoint-2xl: 100rem;  --breakpoint-3xl: 120rem;}
```

이렇게 하면 `2xl` 브레이크포인트가 기본값 `96rem` 대신 `100rem`을 사용하도록 업데이트되고, 마크업에서 사용할 수 있는 새 `xs` 및 `3xl` 브레이크포인트가 생성됩니다:

HTML

```
    <div class="grid xs:grid-cols-2 3xl:grid-cols-6">  <!-- ... --></div>
```

브레이크포인트를 정의할 때는 항상 같은 단위를 사용하는 것이 중요합니다. 그렇지 않으면 생성된 유틸리티 정렬 순서가 예상과 달라져, 브레이크포인트 클래스가 서로를 예상치 못하게 덮어쓸 수 있습니다.

Tailwind는 기본 브레이크포인트에 `rem`을 사용하므로, 기본값에 브레이크포인트를 추가할 때도 `rem`을 사용하세요.

테마 커스터마이징에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme)을 참고하세요.

- 기본 브레이크포인트 제거하기

기본 브레이크포인트를 제거하려면 값을 `initial` 키워드로 재설정하세요:

app.css

```
    @import "tailwindcss";@theme {  --breakpoint-2xl: initial;}
```

`--breakpoint-*: initial`을 사용해 기본 브레이크포인트를 모두 재설정한 다음, 모든 브레이크포인트를 처음부터 다시 정의할 수도 있습니다:

app.css

```
    @import "tailwindcss";@theme {  --breakpoint-*: initial;  --breakpoint-tablet: 40rem;  --breakpoint-laptop: 64rem;  --breakpoint-desktop: 80rem;}
```

기본 테마 값 제거에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme)을 참고하세요.

- 임의 값 사용하기

테마에 포함할 필요가 없는 일회성 브레이크포인트가 필요하다면, `min` 또는 `max` variant를 사용해 임의 값으로 즉석에서 커스텀 브레이크포인트를 생성하세요.

```
    <div class="max-[600px]:bg-sky-300 min-[320px]:text-center">  <!-- ... --></div>
```

임의 값 지원에 대한 자세한 내용은 [arbitrary values](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values) 문서를 참고하세요.

## 컨테이너 쿼리

- 컨테이너 쿼리란?

[Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries)는 전체 viewport 크기가 아니라 부모 요소의 크기를 기준으로 스타일을 적용할 수 있게 해주는 최신 CSS 기능입니다. 컴포넌트에 실제로 주어진 공간에 따라 변화할 수 있으므로, 더 이식 가능하고 재사용 가능한 컴포넌트를 만들 수 있습니다.

- 기본 예시

요소를 컨테이너로 지정하려면 `@container` 클래스를 사용하고, 컨테이너 크기에 따라 자식 요소를 스타일링하려면 `@sm`, `@md` 같은 variant를 사용하세요:

HTML

```
    <div class="@container">  <div class="flex flex-col @md:flex-row">    <!-- ... -->  </div></div>
```

브레이크포인트 variant와 마찬가지로, Tailwind CSS의 컨테이너 쿼리는 모바일 우선이며 대상 컨테이너 크기 이상에서 적용됩니다.

- 최대 너비 컨테이너 쿼리

특정 컨테이너 크기 미만에서 스타일을 적용하려면 `@max-sm`, `@max-md` 같은 variant를 사용하세요:

HTML

```
    <div class="@container">  <div class="flex flex-row @max-md:flex-col">    <!-- ... -->  </div></div>
```

- 컨테이너 쿼리 범위

특정 범위를 타겟팅하려면 일반 컨테이너 쿼리 variant와 최대 너비 컨테이너 쿼리 variant를 함께 쌓으세요:

HTML

```
    <div class="@container">  <div class="flex flex-row @sm:@max-md:flex-col">    <!-- ... -->  </div></div>
```

- 이름 있는 컨테이너

여러 중첩 컨테이너를 사용하는 복잡한 디자인에서는 `@container/{name}`으로 컨테이너에 이름을 붙이고, `@sm/{name}`, `@md/{name}` 같은 variant로 특정 컨테이너를 타겟팅할 수 있습니다:

HTML

```
    <div class="@container/main">  <!-- ... -->  <div class="flex flex-row @sm/main:flex-col">    <!-- ... -->  </div></div>
```

이렇게 하면 가장 가까운 컨테이너뿐 아니라, 더 멀리 있는 컨테이너의 크기를 기준으로도 스타일을 적용할 수 있습니다.

- 커스텀 컨테이너 크기 사용하기

컨테이너 크기를 커스터마이징하려면 `--container-*` 테마 변수를 사용하세요:

app.css

```
    @import "tailwindcss";@theme {  --container-8xl: 96rem;}
```

이렇게 하면 마크업에서 사용할 수 있는 새 `8xl` 컨테이너 쿼리 variant가 추가됩니다:

HTML

```
    <div class="@container">  <div class="flex flex-col @8xl:flex-row">    <!-- ... -->  </div></div>
```

테마 커스터마이징에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme)을 참고하세요.

- 임의 값 사용하기

테마에 추가하고 싶지 않은 일회성 컨테이너 쿼리 크기에는 `@min-[475px]`, `@max-[960px]` 같은 variant를 사용하세요:

HTML

```
    <div class="@container">  <div class="flex flex-col @min-[475px]:flex-row">    <!-- ... -->  </div></div>
```

- 컨테이너 쿼리 단위 사용하기

컨테이너 크기를 참조하려면 `cqw` 같은 [container query length units](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries#container_query_length_units)를 다른 유틸리티 클래스에서 임의 값으로 사용하세요:

HTML

```
    <div class="@container">  <div class="w-[50cqw]">    <!-- ... -->  </div></div>
```

- 컨테이너 크기 참조

기본적으로 Tailwind에는 16rem _(256px)_ 부터 80rem _(1280px)_ 까지의 컨테이너 크기가 포함되어 있습니다:

| Variant | Minimum width    | CSS                                 |
| ------- | ---------------- | ----------------------------------- |
| `@3xs`  | 16rem _(256px)_  | `@container (width >= 16rem) { … }` |
| `@2xs`  | 18rem _(288px)_  | `@container (width >= 18rem) { … }` |
| `@xs`   | 20rem _(320px)_  | `@container (width >= 20rem) { … }` |
| `@sm`   | 24rem _(384px)_  | `@container (width >= 24rem) { … }` |
| `@md`   | 28rem _(448px)_  | `@container (width >= 28rem) { … }` |
| `@lg`   | 32rem _(512px)_  | `@container (width >= 32rem) { … }` |
| `@xl`   | 36rem _(576px)_  | `@container (width >= 36rem) { … }` |
| `@2xl`  | 42rem _(672px)_  | `@container (width >= 42rem) { … }` |
| `@3xl`  | 48rem _(768px)_  | `@container (width >= 48rem) { … }` |
| `@4xl`  | 56rem _(896px)_  | `@container (width >= 56rem) { … }` |
| `@5xl`  | 64rem _(1024px)_ | `@container (width >= 64rem) { … }` |
| `@6xl`  | 72rem _(1152px)_ | `@container (width >= 72rem) { … }` |
| `@7xl`  | 80rem _(1280px)_ | `@container (width >= 80rem) { … }` |
