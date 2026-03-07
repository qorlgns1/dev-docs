---
title: "유틸리티 클래스로 스타일링하기 - 핵심 개념 - Tailwind CSS"
description: "Tailwind에서는 마크업에 여러 단일 목적의 표현 클래스 _(utility classes)_ 를 직접 조합해 스타일을 적용합니다:"
---

출처 URL: https://tailwindcss.com/docs/styling-with-utility-classes

# 유틸리티 클래스로 스타일링하기 - 핵심 개념 - Tailwind CSS

## 개요

Tailwind에서는 마크업에 여러 단일 목적의 표현 클래스 _(utility classes)_ 를 직접 조합해 스타일을 적용합니다:

ChitChat

새 메시지가 도착했습니다!

```
    <div class="mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg outline outline-black/5 dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">  <img class="size-12 shrink-0" src="/img/logo.svg" alt="ChitChat Logo" />  <div>    <div class="text-xl font-medium text-black dark:text-white">ChitChat</div>    <p class="text-gray-500 dark:text-gray-400">You have a new message!</p>  </div></div>
```

예를 들어 위 UI에서는 다음을 사용했습니다:

- 전체 레이아웃을 제어하기 위해 [display](https://tailwindcss.com/docs/display#flex) 및 [padding](https://tailwindcss.com/docs/padding) 유틸리티(`flex`, `shrink-0`, `p-6`)를 사용
- 카드 너비를 제한하고 수평 중앙 정렬하기 위해 [max-width](https://tailwindcss.com/docs/max-width) 및 [margin](https://tailwindcss.com/docs/margin) 유틸리티(`max-w-sm`, `mx-auto`)를 사용
- 카드의 시각적 모양을 꾸미기 위해 [background-color](https://tailwindcss.com/docs/background-color), [border-radius](https://tailwindcss.com/docs/border-radius), [box-shadow](https://tailwindcss.com/docs/box-shadow) 유틸리티(`bg-white`, `rounded-xl`, `shadow-lg`)를 사용
- 로고 이미지의 너비와 높이를 설정하기 위해 [width](https://tailwindcss.com/docs/width) 및 [height](https://tailwindcss.com/docs/height) 유틸리티(`size-12`)를 사용
- 로고와 텍스트 사이 간격을 처리하기 위해 [gap](https://tailwindcss.com/docs/gap) 유틸리티(`gap-x-4`)를 사용
- 카드 텍스트를 스타일링하기 위해 [font-size](https://tailwindcss.com/docs/font-size), [color](https://tailwindcss.com/docs/text-color), [font-weight](https://tailwindcss.com/docs/font-weight) 유틸리티(`text-xl`, `text-black`, `font-medium` 등)를 사용

이런 방식의 스타일링은 기존의 많은 모범 사례와 상충되지만, 한번 써보면 금방 중요한 장점을 체감하게 됩니다:

- **작업 속도가 빨라집니다** — 클래스 이름을 짓거나 셀렉터를 고민하거나 HTML/CSS 파일을 오가느라 시간을 쓰지 않으므로, 디자인을 매우 빠르게 완성할 수 있습니다.
- **변경이 더 안전하게 느껴집니다** — 요소에 유틸리티 클래스를 추가하거나 제거해도 그 요소에만 영향이 있으므로, 같은 CSS를 쓰는 다른 페이지를 실수로 망가뜨릴 걱정을 하지 않아도 됩니다.
- **오래된 프로젝트 유지보수가 쉬워집니다** — 무언가를 바꿀 때 6개월 동안 건드리지 않은 커스텀 CSS 동작을 다시 떠올릴 필요 없이, 해당 요소를 찾아 클래스만 바꾸면 됩니다.
- **코드 이식성이 높아집니다** — 구조와 스타일이 한곳에 함께 있으므로, UI 덩어리를 프로젝트 내외로 쉽게 복사해 재사용할 수 있습니다.
- **CSS가 계속 커지지 않습니다** — 유틸리티 클래스는 재사용성이 높아 프로젝트에 기능을 추가해도 CSS가 선형적으로 계속 증가하지 않습니다.

이 장점들은 작은 프로젝트에서도 큰 차이를 만들지만, 대규모로 장기간 운영되는 팀 프로젝트에서는 훨씬 더 가치가 큽니다.

- 인라인 스타일만 쓰면 안 되나요?

이 접근에 대한 흔한 반응은 “이거 그냥 인라인 스타일 아닌가요?”라는 질문이며, 어떤 면에서는 맞습니다. 클래스 이름을 부여하고 그 클래스를 스타일링하는 대신, 스타일을 요소에 직접 적용하니까요.

하지만 유틸리티 클래스는 인라인 스타일 대비 중요한 장점이 많습니다. 예를 들면:

- **제약 기반 디자인** — 인라인 스타일에서는 모든 값이 매직 넘버가 됩니다. 유틸리티를 쓰면 [미리 정의된 디자인 시스템](https://tailwindcss.com/docs/theme) 안에서 스타일을 선택하게 되어, 시각적으로 일관된 UI를 훨씬 쉽게 만들 수 있습니다.
- **hover, focus, 기타 상태** — 인라인 스타일은 hover나 focus 같은 상태를 타깃할 수 없지만, Tailwind의 [state variants](https://tailwindcss.com/docs/hover-focus-and-other-states)를 쓰면 유틸리티 클래스로 이런 상태를 쉽게 스타일링할 수 있습니다.
- **미디어 쿼리** — 인라인 스타일에서는 미디어 쿼리를 사용할 수 없지만, Tailwind의 [responsive variants](https://tailwindcss.com/docs/responsive-design)를 사용하면 완전한 반응형 인터페이스를 쉽게 구축할 수 있습니다.

아래 컴포넌트는 완전 반응형이며 hover/active 스타일이 있는 버튼을 포함하고, 전부 유틸리티 클래스로만 작성되었습니다:

![여성의 얼굴](https://tailwindcss.com/_next/static/media/erin-lindford.fbd7bb53.jpg)

Erin Lindford

제품 엔지니어

메시지

```
    <div class="flex flex-col gap-2 p-8 sm:flex-row sm:items-center sm:gap-6 sm:py-4 ...">  <img class="mx-auto block h-24 rounded-full sm:mx-0 sm:shrink-0" src="/img/erin-lindford.jpg" alt="" />  <div class="space-y-2 text-center sm:text-left">    <div class="space-y-0.5">      <p class="text-lg font-semibold text-black">Erin Lindford</p>      <p class="font-medium text-gray-500">Product Engineer</p>    </div>    <button class="border-purple-200 text-purple-600 hover:border-transparent hover:bg-purple-600 hover:text-white active:bg-purple-700 ...">      Message    </button>  </div></div>
```

## 유틸리티 클래스로 사고하기

- hover와 focus 상태 스타일링

hover나 focus 같은 상태에서 요소를 스타일링하려면, 해당 상태 접두사를 유틸리티 앞에 붙이면 됩니다. 예: `hover:bg-sky-700`:

배경색이 바뀌는 것을 보려면 이 버튼 위에 마우스를 올려보세요

변경 사항 저장

```
    <button class="bg-sky-500 hover:bg-sky-700 ...">Save changes</button>
```

이 접두사들은 Tailwind에서 [variants](https://tailwindcss.com/docs/hover-focus-and-other-states)라고 부르며, 해당 variant 조건이 일치할 때만 유틸리티 클래스의 스타일을 적용합니다.

`hover:bg-sky-700` 클래스에 대해 생성된 CSS는 다음과 같습니다:

생성된 CSS

```
    .hover\:bg-sky-700 {  &:hover {    background-color: var(--color-sky-700);  }}
```

이 클래스는 요소에 hover되지 _않는 한_ 아무 일도 하지 않는다는 점에 주목하세요. 이 클래스의 _유일한_ 역할은 hover 스타일을 제공하는 것입니다.

이는 전통적인 CSS 작성 방식과 다릅니다. 전통적인 방식에서는 보통 하나의 클래스가 여러 상태의 스타일을 함께 제공합니다:

HTML

```
    <button class="btn">Save changes</button><style>  .btn {    background-color: var(--color-sky-500);    &:hover {      background-color: var(--color-sky-700);    }  }</style>
```

Tailwind에서는 variant를 겹쳐서, 예를 들어 `hover:`와 `disabled:`를 결합해 여러 조건이 동시에 맞을 때 유틸리티를 적용할 수도 있습니다.

```
    <button class="bg-sky-500 disabled:hover:bg-sky-500 ...">Save changes</button>
```

자세한 내용은 [hover, focus, and other states](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.

- 미디어 쿼리와 브레이크포인트

hover/focus 상태와 마찬가지로, 원하는 브레이크포인트 접두사를 유틸리티 앞에 붙여 각 브레이크포인트에서 요소를 스타일링할 수 있습니다:

레이아웃이 바뀌는 것을 보려면 이 예제 크기를 조절해 보세요

01

02

03

04

05

06

```
    <div class="grid grid-cols-2 sm:grid-cols-3">  <!-- ... --></div>
```

위 예제에서 `sm:` 접두사는 `grid-cols-3`가 기본 설정 기준 40rem인 `sm` 브레이크포인트 이상에서만 동작하도록 합니다:

생성된 CSS

```
    .sm\:grid-cols-3 {  @media (width >= 40rem) {    grid-template-columns: repeat(3, minmax(0, 1fr));  }}
```

자세한 내용은 [responsive design](https://tailwindcss.com/docs/responsive-design) 문서를 참고하세요.

- 다크 모드 타깃팅

다크 모드에서 요소를 스타일링하는 방법은 간단합니다. 다크 모드 활성 시 적용할 유틸리티 앞에 `dark:` 접두사를 추가하면 됩니다:

라이트 모드

거꾸로 써도 됩니다

Zero Gravity Pen은 거꾸로를 포함해 어떤 방향에서도 필기가 가능합니다. 우주 공간에서도 작동합니다.

다크 모드

거꾸로 써도 됩니다

Zero Gravity Pen은 거꾸로를 포함해 어떤 방향에서도 필기가 가능합니다. 우주 공간에서도 작동합니다.

```
    <div class="bg-white dark:bg-gray-800 rounded-lg px-6 py-8 ring shadow-xl ring-gray-900/5">  <div>    <span class="inline-flex items-center justify-center rounded-md bg-indigo-500 p-2 shadow-lg">      <svg        class="h-6 w-6 text-white"        fill="none"        viewBox="0 0 24 24"        stroke="currentColor"        aria-hidden="true"      >        <!-- ... -->      </svg>    </span>  </div>  <h3 class="text-gray-900 dark:text-white mt-5 text-base font-medium tracking-tight ">Writes upside-down</h3>  <p class="text-gray-500 dark:text-gray-400 mt-2 text-sm ">    The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer space.  </p></div>
```

hover 상태나 미디어 쿼리와 마찬가지로, 중요한 점은 하나의 유틸리티 클래스에 라이트/다크 스타일이 _동시에_ 들어가지 않는다는 것입니다. 다크 모드 스타일링은 라이트 모드용 클래스와 다크 모드용 클래스를 각각 함께 사용해 구성합니다.

생성된 CSS

```
    .dark\:bg-gray-800 {  @media (prefers-color-scheme: dark) {    background-color: var(--color-gray-800);  }}
```

자세한 내용은 [dark mode](https://tailwindcss.com/docs/dark-mode) 문서를 참고하세요.

- 클래스 조합 사용하기

Tailwind에서는 종종 하나의 CSS 속성 값을 만들기 위해 여러 클래스를 조합하기도 합니다. 예를 들어 요소에 여러 필터를 동시에 추가할 수 있습니다:

HTML

```
    <div class="blur-sm grayscale">  <!-- ... --></div>
```

이 두 효과는 모두 CSS의 `filter` 속성에 의존하므로, Tailwind는 CSS 변수를 사용해 이 효과들을 함께 조합할 수 있게 합니다:

생성된 CSS

```
    .blur-sm {  --tw-blur: blur(var(--blur-sm));  filter: var(--tw-blur,) var(--tw-brightness,) var(--tw-grayscale,);}.grayscale {  --tw-grayscale: grayscale(100%);  filter: var(--tw-blur,) var(--tw-brightness,) var(--tw-grayscale,);}
```

위 생성 CSS는 약간 단순화된 버전이지만, 핵심은 각 유틸리티가 자신이 적용할 효과에 해당하는 CSS 변수만 설정한다는 점입니다. 그리고 `filter` 속성은 이 변수들을 모두 확인하고, 설정되지 않은 변수는 빈 값으로 대체합니다.

Tailwind는 [gradients](https://tailwindcss.com/docs/background-image#adding-a-linear-gradient), [shadow colors](https://tailwindcss.com/docs/box-shadow#setting-the-shadow-color), [transforms](https://tailwindcss.com/docs/translate) 등에도 같은 접근을 사용합니다.

- 임의 값 사용하기

Tailwind의 많은 유틸리티는 `bg-blue-500`, `text-xl`, `shadow-md`처럼 [theme variables](https://tailwindcss.com/docs/theme)에 기반해 동작하며, 내부 색상 팔레트/타이포 스케일/그림자 설정에 매핑됩니다.

테마 밖의 일회성 값을 사용해야 할 때는, 대괄호 특수 문법으로 임의 값을 지정할 수 있습니다:

HTML

```
    <button class="bg-[#316ff6] ...">  Sign in with Facebook</button>
```

이 방식은 색상 팔레트 밖의 일회성 색상 _(위 Facebook 파란색처럼)_ 에 유용할 뿐 아니라, 매우 구체적인 그리드 같은 복잡한 커스텀 값이 필요할 때도 유용합니다:

HTML

```
    <div class="grid grid-cols-[24rem_2.5rem_minmax(0,1fr)]">  <!-- ... --></div>
```

테마 값을 사용하더라도 `calc()` 같은 CSS 기능이 필요할 때 역시 유용합니다:

HTML

```
    <div class="max-h-[calc(100dvh-(--spacing(6)))]">  <!-- ... --></div>
```

임의 속성 이름까지 포함해 완전히 임의의 CSS를 생성하는 문법도 있으며, CSS 변수를 설정할 때 유용합니다:

HTML

```
    <div class="[--gutter-width:1rem] lg:[--gutter-width:2rem]">  <!-- ... --></div>
```

자세한 내용은 [using arbitrary values](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values) 문서를 참고하세요.

#

- 이건 도대체 어떻게 동작하나요?

Tailwind CSS는 다른 CSS 프레임워크처럼 하나의 거대한 정적 스타일시트가 아닙니다. CSS를 컴파일할 때 실제로 사용한 클래스에 기반해 필요한 CSS를 생성합니다.

이를 위해 프로젝트의 모든 파일을 스캔하면서 클래스 이름처럼 보이는 모든 심볼을 찾습니다:

Button.jsx

```
    export default function Button({ size, children }) {  let sizeClasses = {    md: "px-4 py-2 rounded-md text-base",    lg: "px-5 py-3 rounded-lg text-lg",  }[size];  return (    <button type="button" className={`font-bold ${sizeClasses}`}>      {children}    </button>  );}
```

잠재 클래스들을 모두 찾고 나면, Tailwind가 각 클래스에 대한 CSS를 생성해 실제로 필요한 스타일만 하나의 스타일시트로 컴파일합니다.

CSS는 클래스 이름을 기반으로 생성되기 때문에, Tailwind는 `bg-[#316ff6]` 같은 임의 값 클래스도 인식하고, 값이 테마에 없더라도 필요한 CSS를 생성할 수 있습니다.

동작 방식에 대한 자세한 내용은 [detecting classes in source files](https://tailwindcss.com/docs/detecting-classes-in-source-files)에서 확인하세요.

- 복합 셀렉터

때로는 예를 들어 다크 모드이면서, 특정 브레이크포인트에서, hover 상태이고, 요소에 특정 data attribute가 있는 경우처럼 여러 조건 조합에서 요소를 스타일링해야 합니다.

Tailwind에서의 예시는 다음과 같습니다:

HTML

```
    <button class="dark:lg:data-current:hover:bg-indigo-600 ...">  <!-- ... --></button>
```

단순화된 CSS

```
    @media (prefers-color-scheme: dark) and (width >= 64rem) {  button[data-current]:hover {    background-color: var(--color-indigo-600);  }}
```

Tailwind는 `group-hover` 같은 기능도 지원해, 특정 부모 요소가 hover되었을 때 자식 요소를 스타일링할 수 있습니다:

HTML

```
    <a href="#" class="group rounded-lg p-8">  <!-- ... -->  <span class="group-hover:underline">Read more…</span></a>
```

단순화된 CSS

```
    @media (hover: hover) {  a:hover span {    text-decoration-line: underline;  }}
```

이 `group-*` 문법은 `group-focus`, `group-active`, 그리고 [그 외 다양한 variant](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-parent-state)에도 동일하게 적용됩니다.

아주 복잡한 시나리오 _(특히 제어할 수 없는 HTML을 스타일링할 때)_ 에서는 Tailwind의 [arbitrary variants](https://tailwindcss.com/docs/adding-custom-styles#arbitrary-variants)를 사용해 클래스 이름 안에서 원하는 셀렉터를 직접 작성할 수도 있습니다:

HTML

```
    <div class="[&>[data-active]+span]:text-blue-600 ...">  <span data-active><!-- ... --></span>  <span>This text will be blue</span></div>
```

단순화된 CSS

```
    div > [data-active] + span {  color: var(--color-blue-600);}
```

- 인라인 스타일을 사용해야 할 때

인라인 스타일은 Tailwind CSS 프로젝트에서도 여전히 매우 유용합니다. 특히 값이 데이터베이스나 API처럼 동적 소스에서 올 때 그렇습니다:

branded-button.jsx

```
    export function BrandedButton({ buttonColor, textColor, children }) {  return (    <button      style={{        backgroundColor: buttonColor,        color: textColor,      }}      className="rounded-md px-3 py-1.5 font-medium"    >      {children}    </button>  );}
```

클래스 이름으로 표현하면 읽기 어려운, 매우 복잡한 임의 값을 사용할 때도 인라인 스타일이 유용합니다:

HTML

```
    <div class="grid-[2fr_max(0,var(--gutter-width))_calc(var(--gutter-width)+10px)]"><div style="grid-template-columns: 2fr max(0, var(--gutter-width)) calc(var(--gutter-width) + 10px)">  <!-- ... --></div>
```

또 하나 유용한 패턴은 인라인 스타일로 동적 소스 기반 CSS 변수를 설정하고, 유틸리티 클래스에서 그 변수를 참조하는 방식입니다:

branded-button.jsx

```
    export function BrandedButton({ buttonColor, buttonColorHover, textColor, children }) {  return (    <button      style={{        "--bg-color": buttonColor,        "--bg-color-hover": buttonColorHover,        "--text-color": textColor,      }}      className="bg-(--bg-color) text-(--text-color) hover:bg-(--bg-color-hover) ..."    >      {children}    </button>  );}
```

## 중복 관리

유틸리티 클래스만으로 전체 프로젝트를 만들다 보면, 같은 디자인을 여러 곳에 재현하기 위해 특정 패턴을 반복하게 되는 경우가 생깁니다.

예를 들어 여기서는 각 아바타 이미지의 유틸리티 클래스가 다섯 번 별도로 반복됩니다:

#### 기여자

204

![](https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

\[

- 198명 더

\](https://tailwindcss.com/docs/styling-with-utility-classes)

```
    <div>  <div class="flex items-center space-x-2 text-base">    <h4 class="font-semibold text-slate-900">Contributors</h4>    <span class="bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700 ...">204</span>  </div>  <div class="mt-3 flex -space-x-2 overflow-hidden">    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt="" />    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />  </div>  <div class="mt-3 text-sm font-medium">    <a href="#" class="text-blue-500">+ 198 others</a>  </div></div>
```

걱정하지 마세요! 실제로는 생각보다 큰 문제가 아니며, 이를 처리하는 전략도 여러분이 이미 매일 하고 있는 것들입니다.

- 루프 사용하기

렌더링된 페이지에서 여러 번 나타나는 디자인 요소는 실제 마크업이 루프에서 렌더링되기 때문에, 실제로는 한 번만 작성되는 경우가 많습니다.

예를 들어, 이 가이드 시작 부분의 중복 아바타는 실제 프로젝트라면 거의 확실히 루프로 렌더링될 것입니다:

#### 기여자

204

![](https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)![](https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

\[

- 198명 더

\](https://tailwindcss.com/docs/styling-with-utility-classes)

```
    <div>  <div class="flex items-center space-x-2 text-base">    <h4 class="font-semibold text-slate-900">Contributors</h4>    <span class="bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700 ...">204</span>  </div>  <div class="mt-3 flex -space-x-2 overflow-hidden">    {#each contributors as user}      <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src={user.avatarUrl} alt={user.handle} />    {/each}  </div>  <div class="mt-3 text-sm font-medium">    <a href="#" class="text-blue-500">+ 198 others</a>  </div></div>
```

요소가 이렇게 루프로 렌더링되면 실제 클래스 목록은 한 번만 작성되므로, 해결해야 할 중복 문제 자체가 없습니다.

- 멀티 커서 편집 사용하기

중복이 단일 파일 내의 요소 그룹에 국한되어 있다면, 가장 쉬운 방법은 [multi-cursor editing](https://code.visualstudio.com/docs/editor/codebasics#_multiple-selections-multicursor)을 사용해 각 요소의 클래스 목록을 한 번에 빠르게 선택하고 수정하는 것입니다:

```
    <nav class="flex justify-center space-x-4">  <a href="/dashboard" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">    Home  </a>  <a href="/team" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">    Team  </a>  <a href="/projects" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">    Projects  </a>  <a href="/reports" class="font-medium rounded-lg px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900">    Reports  </a></nav>
```

이 방법이 최선의 해결책이 되는 경우가 생각보다 많습니다. 중복된 클래스 목록을 모두 동시에 빠르게 수정할 수 있다면, 추가 추상화를 도입할 이점이 없습니다.

- 컴포넌트 사용하기

여러 파일에서 일부 스타일을 재사용해야 한다면, React, Svelte, Vue 같은 프런트엔드 프레임워크를 사용 중일 때는 _component_ 를 만들고, Blade, ERB, Twig, Nunjucks 같은 템플릿 언어를 사용 중일 때는 _template partial_ 을 만드는 것이 가장 좋은 전략입니다.

![해변](https://images.unsplash.com/photo-1452784444945-3f422708fe5e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=512&q=80)

프라이빗 빌라

[칸쿤의 편안한 올인클루시브 리조트](https://tailwindcss.com/docs/styling-with-utility-classes)

1박당 $299 USD

```
    export function VacationCard({ img, imgAlt, eyebrow, title, pricing, url }) {  return (    <div>      <img className="rounded-lg" src={img} alt={imgAlt} />      <div className="mt-4">        <div className="text-xs font-bold text-sky-500">{eyebrow}</div>        <div className="mt-1 font-bold text-gray-700">          <a href={url} className="hover:underline">            {title}          </a>        </div>        <div className="mt-2 text-sm text-gray-600">{pricing}</div>      </div>    </div>  );}
```

이제 이 컴포넌트를 원하는 만큼 여러 곳에서 사용할 수 있으며, 스타일의 단일 진실 공급원(single source of truth)을 유지할 수 있어 한 곳에서 함께 쉽게 업데이트할 수 있습니다.

- 사용자 정의 CSS 사용하기

React나 Vue 같은 것을 쓰는 대신 ERB나 Twig 같은 템플릿 언어를 사용한다면, 버튼처럼 작은 요소를 위해 템플릿 partial을 만드는 일은 `btn` 같은 단순 CSS 클래스에 비해 과하다고 느껴질 수 있습니다.

더 복잡한 컴포넌트에는 적절한 템플릿 partial을 만드는 것을 강력히 권장하지만, 템플릿 partial이 지나치게 무겁게 느껴질 때는 일부 사용자 정의 CSS를 작성해도 전혀 괜찮습니다.

디자인 일관성을 유지하기 위해 [theme variables](https://tailwindcss.com/docs/theme#with-custom-css)를 사용하는 `btn-primary` 클래스는 다음과 같은 형태가 될 수 있습니다:

변경 사항 저장

HTML

```
    <button class="btn-primary">Save changes</button>
```

CSS

```
    @import "tailwindcss";@layer components {  .btn-primary {    border-radius: calc(infinity * 1px);    background-color: var(--color-violet-500);    padding-inline: --spacing(5);    padding-block: --spacing(2);    font-weight: var(--font-weight-semibold);    color: var(--color-white);    box-shadow: var(--shadow-md);    &:hover {      @media (hover: hover) {        background-color: var(--color-violet-700);      }    }  }}
```

다시 강조하지만, 단일 HTML 요소보다 복잡한 경우에는 스타일과 구조를 한곳에 캡슐화할 수 있도록 템플릿 partial 사용을 강력히 권장합니다.

## 스타일 충돌 관리

- 충돌하는 유틸리티 클래스

같은 CSS 속성을 대상으로 하는 클래스를 두 개 추가하면, 스타일시트에서 더 나중에 나타나는 클래스가 적용됩니다. 따라서 아래 예시에서는 실제 `class` 속성에서는 `flex`가 더 뒤에 오더라도 요소에는 `display: grid`가 적용됩니다:

HTML

```
    <div class="grid flex">  <!-- ... --></div>
```

CSS

```
    .flex {  display: flex;}.grid {  display: grid;}
```

일반적으로 같은 요소에 충돌하는 클래스 두 개를 절대 추가하지 말고, 실제로 적용되길 원하는 클래스 하나만 추가해야 합니다:

example.jsx

```
    export function Example({ gridLayout }) {  return <div className={gridLayout ? "grid" : "flex"}>{/* ... */}</div>;}
```

React나 Vue 같은 컴포넌트 기반 라이브러리를 사용할 때는, 컴포넌트 외부에서 사용자가 추가 클래스를 넣게 하기보다 스타일 커스터마이징을 위한 특정 props를 노출하는 경우가 많습니다. 외부 클래스는 자주 충돌하기 때문입니다.

- important modifier 사용하기

특정 유틸리티 클래스를 반드시 적용해야 하고 특이성을 관리할 다른 방법이 없다면, 클래스 이름 끝에 `!`를 붙여 모든 선언을 `!important`로 만들 수 있습니다:

HTML

```
    <div class="bg-teal-500 bg-red-500!">  <!-- ... --></div>
```

생성된 CSS

```
    .bg-red-500\! {  background-color: var(--color-red-500) !important;}.bg-teal-500 {  background-color: var(--color-teal-500);}
```

- important flag 사용하기

이미 높은 특이성 규칙을 가진 복잡한 기존 CSS가 있는 프로젝트에 Tailwind를 추가한다면, Tailwind를 가져올 때 `important` flag를 사용해 _all_ utilities를 `!important`로 표시할 수 있습니다:

app.css

```
    @import "tailwindcss" important;
```

컴파일된 CSS

```
    @layer utilities {  .flex {    display: flex !important;  }  .gap-4 {    gap: 1rem !important;  }  .underline {    text-decoration-line: underline !important;  }}
```

- prefix 옵션 사용하기

프로젝트에 Tailwind CSS 유틸리티와 충돌하는 클래스 이름이 있다면, `prefix` 옵션을 사용해 Tailwind가 생성한 모든 클래스와 CSS 변수를 접두사 처리할 수 있습니다:

app.css

```
    @import "tailwindcss" prefix(tw);
```

컴파일된 CSS

```
    @layer theme {  :root {    --tw-color-red-500: oklch(0.637 0.237 25.331);  }}@layer utilities {  .tw\:text-red-500 {    color: var(--tw-color-red-500);  }}
```
