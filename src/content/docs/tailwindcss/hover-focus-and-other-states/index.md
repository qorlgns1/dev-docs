---
title: "호버, 포커스 및 기타 상태 - 핵심 개념 - Tailwind CSS"
description: "Tailwind의 모든 유틸리티 클래스는 대상으로 삼고 싶은 조건을 설명하는 variant를 클래스 이름 앞에 붙여 _조건부로_ 적용할 수 있습니다."
---

출처 URL: https://tailwindcss.com/docs/hover-focus-and-other-states

# 호버, 포커스 및 기타 상태 - 핵심 개념 - Tailwind CSS

Tailwind의 모든 유틸리티 클래스는 대상으로 삼고 싶은 조건을 설명하는 variant를 클래스 이름 앞에 붙여 _조건부로_ 적용할 수 있습니다.

예를 들어, 호버 시 `bg-sky-700` 클래스를 적용하려면 `hover:bg-sky-700` 클래스를 사용합니다:

이 버튼 위에 마우스를 올려 배경색이 바뀌는 것을 확인해 보세요

변경 사항 저장

```
    <button class="bg-sky-500 hover:bg-sky-700 ...">Save changes</button>
```

기존 CSS와 비교하면 어떤가요?

기존 방식으로 CSS를 작성할 때는, 하나의 클래스 이름이 현재 상태에 따라 서로 다른 동작을 합니다:

기존 방식에서는 같은 클래스 이름이 호버 시 다른 스타일을 적용합니다

```
    .btn-primary {  background-color: #0ea5e9;}.btn-primary:hover {  background-color: #0369a1;}
```

Tailwind에서는 기존 클래스에 호버 상태 스타일을 추가하는 대신, 호버에서만 동작하는 클래스를 요소에 하나 더 추가합니다:

Tailwind에서는 기본 상태와 호버 상태에 서로 다른 클래스를 사용합니다

```
    .bg-sky-500 {  background-color: #0ea5e9;}.hover\:bg-sky-700:hover {  background-color: #0369a1;}
```

`hover:bg-sky-700`이 `:hover` 상태에 대한 스타일만 정의한다는 점에 주목하세요. 기본적으로는 아무 동작도 하지 않지만, 해당 클래스가 있는 요소에 마우스를 올리는 즉시 배경색이 `sky-700`으로 바뀝니다.

이것이 유틸리티 클래스를 _조건부로_ 적용할 수 있다고 말하는 의미입니다. variant를 사용하면 HTML을 벗어나지 않고도 다양한 상태에서 디자인이 어떻게 동작할지 정확히 제어할 수 있습니다.

Tailwind에는 다음을 포함해 거의 모든 상황에 필요한 variant가 포함되어 있습니다:

- `:hover`, `:focus`, `:first-child`, `:required` 같은 [의사 클래스](https://tailwindcss.com/docs/hover-focus-and-other-states#pseudo-classes)
- `::before`, `::after`, `::placeholder`, `::selection` 같은 [의사 요소](https://tailwindcss.com/docs/hover-focus-and-other-states#pseudo-elements)
- 반응형 브레이크포인트, 다크 모드, `prefers-reduced-motion` 같은 [미디어 및 기능 쿼리](https://tailwindcss.com/docs/hover-focus-and-other-states#media-and-feature-queries)
- `[dir="rtl"]`, `[open]` 같은 [속성 선택자](https://tailwindcss.com/docs/hover-focus-and-other-states#attribute-selectors)
- `& > *`, `& *` 같은 [자식 선택자](https://tailwindcss.com/docs/hover-focus-and-other-states#child-selectors)

이러한 variant는 더 구체적인 상황을 대상으로 겹쳐서 사용할 수도 있습니다. 예를 들어 다크 모드에서, 중간 브레이크포인트에서, 호버 시 배경색을 변경할 수 있습니다:

```
    <button class="dark:md:hover:bg-fuchsia-600 ...">Save changes</button>
```

이 가이드에서는 프레임워크에서 사용 가능한 모든 variant, 사용자 정의 클래스와 함께 사용하는 방법, 그리고 직접 variant를 만드는 방법까지 배우게 됩니다.

## 의사 클래스

- :hover, :focus, 및 :active

`hover`, `focus`, `active` variant를 사용해 호버, 포커스, 활성 상태에서 요소를 스타일링하세요:

이 버튼과 상호작용해서 hover, focus, active 상태를 확인해 보세요

변경 사항 저장

```
    <button class="bg-violet-500 hover:bg-violet-600 focus:outline-2 focus:outline-offset-2 focus:outline-violet-500 active:bg-violet-700 ...">  Save changes</button>
```

Tailwind에는 `:visited`, `:focus-within`, `:focus-visible` 등 다른 상호작용 상태를 위한 variant도 포함되어 있습니다.

사용 가능한 의사 클래스 variant 전체 목록은 [의사 클래스 레퍼런스](https://tailwindcss.com/docs/hover-focus-and-other-states#pseudo-class-reference)를 확인하세요.

- :first, :last, :odd, 및 :even

`first`, `last` variant를 사용하면 요소가 첫 번째 자식 또는 마지막 자식일 때 스타일을 적용할 수 있습니다:

- ![](https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Kristen Ramos

kristen.ramos@example.com

- ![](https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Floyd Miles

floyd.miles@example.com

- ![](https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Courtney Henry

courtney.henry@example.com

- ![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Ted Fox

ted.fox@example.com

```
    <ul role="list">  {#each people as person}    <!-- Remove top/bottom padding when first/last child -->    <li class="flex py-4 first:pt-0 last:pb-0">      <img class="h-10 w-10 rounded-full" src={person.imageUrl} alt="" />      <div class="ml-3 overflow-hidden">        <p class="text-sm font-medium text-gray-900 dark:text-white">{person.name}</p>        <p class="truncate text-sm text-gray-500 dark:text-gray-400">{person.email}</p>      </div>    </li>  {/each}</ul>
```

`odd`, `even` variant를 사용하면 요소가 홀수 또는 짝수 자식일 때도 스타일링할 수 있습니다:

| 이름            | 직함                       | 이메일                      |
| --------------- | -------------------------- | --------------------------- |
| Jane Cooper     | 지역 패러다임 기술자       | jane.cooper@example.com     |
| Cody Fisher     | 제품 지침 책임자           | cody.fisher@example.com     |
| Leonard Krasner | 수석 디자이너              | leonard.krasner@example.com |
| Emily Selman    | 하드웨어 엔지니어링 부사장 | emily.selman@example.com    |
| Anna Roberts    | 최고 전략 책임자           | anna.roberts@example.com    |

```
    <table>  <!-- ... -->  <tbody>    {#each people as person}      <!-- Use different background colors for odd and even rows -->      <tr class="odd:bg-white even:bg-gray-50 dark:odd:bg-gray-900/50 dark:even:bg-gray-950">        <td>{person.name}</td>        <td>{person.title}</td>        <td>{person.email}</td>      </tr>    {/each}  </tbody></table>
```

`nth-*` 및 `nth-last-*` variant를 사용해 목록에서의 위치에 따라 자식을 스타일링하세요:

```
    <div class="nth-3:underline">  <!-- ... --></div><div class="nth-last-5:underline">  <!-- ... --></div><div class="nth-of-type-4:underline">  <!-- ... --></div><div class="nth-last-of-type-6:underline">  <!-- ... --></div>
```

기본적으로 원하는 어떤 숫자든 전달할 수 있으며, `nth-[2n+1_of_li]` 같은 더 복잡한 식에는 임의 값을 사용할 수 있습니다.

Tailwind에는 `:only-child`, `:first-of-type`, `:empty` 같은 다른 구조적 의사 클래스용 variant도 포함되어 있습니다.

사용 가능한 의사 클래스 variant 전체 목록은 [의사 클래스 레퍼런스](https://tailwindcss.com/docs/hover-focus-and-other-states#pseudo-class-reference)를 확인하세요.

- :required 및 :disabled

`required`, `invalid`, `disabled` 같은 variant를 사용해 다양한 상태의 폼 요소를 스타일링하세요:

이메일 주소를 유효하게 만들어 스타일이 바뀌는지 확인해 보세요

사용자 이름

이메일

비밀번호

변경 사항 저장

```
    <input  type="text"  value="tbone"  disabled  class="invalid:border-pink-500 invalid:text-pink-600 focus:border-sky-500 focus:outline focus:outline-sky-500 focus:invalid:border-pink-500 focus:invalid:outline-pink-500 disabled:border-gray-200 disabled:bg-gray-50 disabled:text-gray-500 disabled:shadow-none dark:disabled:border-gray-700 dark:disabled:bg-gray-800/20 ..."/>
```

이런 용도로 variant를 사용하면 템플릿의 조건부 로직 양을 줄일 수 있습니다. 입력 상태와 관계없이 같은 클래스 집합을 사용할 수 있고, 브라우저가 적절한 스타일을 대신 적용해 줍니다.

Tailwind에는 `:read-only`, `:indeterminate`, `:checked` 같은 다른 폼 상태용 variant도 포함되어 있습니다.

사용 가능한 의사 클래스 variant 전체 목록은 [의사 클래스 레퍼런스](https://tailwindcss.com/docs/hover-focus-and-other-states#pseudo-class-reference)를 확인하세요.

- :has()

`has-*` variant를 사용하면 자손의 상태나 콘텐츠를 기준으로 요소를 스타일링할 수 있습니다:

결제 방법

Google PayApple PayCredit Card

```
    <label  class="has-checked:bg-indigo-50 has-checked:text-indigo-900 has-checked:ring-indigo-200 dark:has-checked:bg-indigo-950 dark:has-checked:text-indigo-200 dark:has-checked:ring-indigo-900 ...">  <svg fill="currentColor">    <!-- ... -->  </svg>  Google Pay  <input type="radio" class="checked:border-indigo-500 ..." /></label>
```

`has-*`를 `has-[:focus]`처럼 의사 클래스와 함께 사용하면 자손의 상태를 기준으로 요소를 스타일링할 수 있습니다. `has-[img]`, `has-[a]`처럼 요소 선택자도 사용할 수 있어 자손 콘텐츠를 기준으로 스타일링할 수 있습니다.

#

- 그룹의 자손을 기준으로 스타일링

부모 요소의 자손을 기준으로 요소를 스타일링해야 한다면, 부모에 `group` 클래스를 표시하고 `group-has-*` variant로 대상 요소를 스타일링할 수 있습니다:

![](https://spotlight.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Favatar.51a13c67.jpg&w=128&q=80)

Spencer Sharp

[planeteria.tech](https://tailwindcss.com/docs/hover-focus-and-other-states)의 제품 디자이너

![](https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?q=80&w=256&h=256&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

Casey Jordan

그저 여기 있어서 행복합니다.

![](https://images.unsplash.com/photo-1590895340509-793cb98788c9?q=80&w=256&h=256&&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

Alex Reed

예술과 기술의 교차점에서 일하는 다학제 디자이너입니다.

[alex-reed.com](https://tailwindcss.com/docs/hover-focus-and-other-states)

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=256&h=256&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

Taylor Bailey

픽셀을 다루고 div를 쌓습니다.

```
    <div class="group ...">  <img src="..." />  <h4>Spencer Sharp</h4>  <svg class="hidden group-has-[a]:block ..."><!-- ... --></svg>  <p>Product Designer at <a href="...">planeteria.tech</a></p></div>
```

#

- peer의 자손을 기준으로 스타일링

형제 요소의 자손을 기준으로 요소를 스타일링해야 한다면, 형제에 `peer` 클래스를 표시하고 `peer-has-*` variant로 대상 요소를 스타일링할 수 있습니다:

오늘

할 일 목록 만들기

첫 번째 항목 체크하기

경쟁 상태 조사하기

```
    <div>  <label class="peer ...">    <input type="checkbox" name="todo[1]" checked />    Create a to do list  </label>  <svg class="peer-has-checked:hidden ..."><!-- ... --></svg></div>
```

- :not()

`not-` variant를 사용하면 조건이 참이 아닐 때 요소를 스타일링할 수 있습니다.

특히 다른 의사 클래스 variant와 함께 사용할 때 강력합니다. 예를 들어 `not-focus:`와 `hover:`를 결합하면 요소가 포커스되지 않았을 때만 호버 스타일을 적용할 수 있습니다:

버튼에 포커스를 준 다음 마우스를 올려 보세요

변경 사항 저장

```
    <button class="bg-indigo-600 hover:not-focus:bg-indigo-700">  <!-- ... --></button>
```

`not-` variant를 `forced-colors`나 `supports` 같은 미디어 쿼리 variant와 결합해, 사용자 환경의 어떤 조건이 참이 아닐 때만 요소를 스타일링할 수도 있습니다:

```
    <div class="not-supports-[display:grid]:flex">  <!-- ... --></div>
```

- 부모 상태를 기준으로 스타일링

일부 _부모_ 요소의 상태를 기준으로 요소를 스타일링해야 할 때는, 부모에 `group` 클래스를 표시하고 `group-hover` 같은 `group-*` variant를 사용해 대상 요소를 스타일링하세요:

카드 위에 마우스를 올려 두 텍스트 요소의 색이 함께 바뀌는 것을 확인해 보세요

[새 프로젝트다양한 시작 템플릿에서 새 프로젝트를 만듭니다.](https://tailwindcss.com/docs/hover-focus-and-other-states)

```
    <a href="#" class="group ...">  <div>    <svg class="stroke-sky-500 group-hover:stroke-white ..." fill="none" viewBox="0 0 24 24">      <!-- ... -->    </svg>    <h3 class="text-gray-900 group-hover:text-white ...">New project</h3>  </div>  <p class="text-gray-500 group-hover:text-white ...">Create a new project from a variety of starting templates.</p></a>
```

이 패턴은 모든 의사 클래스 variant에서 동작합니다. 예를 들어 `group-focus`, `group-active`, `group-odd`까지 사용할 수 있습니다.

#

- 중첩된 그룹 구분하기

그룹을 중첩할 때는 `group/{name}` 클래스를 사용해 부모 그룹에 고유한 그룹 이름을 지정하고, `group-hover/{name}` 같은 클래스의 variant에 그 이름을 포함해 _특정_ 부모 그룹의 상태를 기준으로 스타일링할 수 있습니다:

- ![](https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

[Leslie Abbott](https://tailwindcss.com/docs/hover-focus-and-other-states)

공동 창립자 / CEO

[전화](https://tailwindcss.com/docs/hover-focus-and-other-states)

- ![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

[Hector Adams](https://tailwindcss.com/docs/hover-focus-and-other-states)

마케팅 부사장

[전화](https://tailwindcss.com/docs/hover-focus-and-other-states)

- ![](https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

[Blake Alexander](https://tailwindcss.com/docs/hover-focus-and-other-states)

어카운트 코디네이터

[전화](https://tailwindcss.com/docs/hover-focus-and-other-states)

```
    <ul role="list">  {#each people as person}    <li class="group/item ...">      <!-- ... -->      <a class="group/edit invisible group-hover/item:visible ..." href="tel:{person.phone}">        <span class="group-hover/edit:text-gray-700 ...">Call</span>        <svg class="group-hover/edit:translate-x-0.5 group-hover/edit:text-gray-500 ..."><!-- ... --></svg>      </a>    </li>  {/each}</ul>
```

그룹 이름은 원하는 대로 지정할 수 있고 별도 설정도 필요 없습니다. 마크업에서 그룹 이름을 직접 지정하면 Tailwind가 필요한 CSS를 자동으로 생성합니다.

#

- 임의 그룹

대괄호 안에 [임의 값](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values)으로 직접 선택자를 제공하면 즉석에서 일회성 `group-*` variant를 만들 수 있습니다:

HTML

생성된 CSS

```
    <div class="group is-published">  <div class="hidden group-[.is-published]:block">    Published  </div></div>
```

더 세밀하게 제어하려면 `&` 문자를 사용해 전달한 선택자 기준으로 최종 선택자에서 `.group`이 들어갈 위치를 표시할 수 있습니다:

HTML

생성된 CSS

```
    <div class="group">  <div class="group-[:nth-of-type(3)_&]:block">    <!-- ... -->  </div></div>
```

#

- 암시적 그룹

`in-*` variant는 `group`과 비슷하게 동작하지만 부모 요소에 `group`을 추가할 필요가 없습니다:

```
    <div tabindex="0" class="group">  <div class="opacity-50 group-focus:opacity-100"><div tabindex="0">  <div class="opacity-50 in-focus:opacity-100">    <!-- ... -->  </div></div>
```

`in-*` variant는 모든 부모의 상태 변화에 반응하므로, 더 세밀한 제어가 필요하면 대신 `group`을 사용해야 합니다.

- 형제 상태를 기준으로 스타일링

형제 요소의 상태를 기준으로 요소를 스타일링해야 할 때는, 형제에 `peer` 클래스를 표시하고 `peer-invalid` 같은 `peer-*` variant를 사용해 대상 요소를 스타일링하세요:

이메일 주소를 유효하게 만들어 경고가 사라지는지 확인해 보세요

이메일

유효한 이메일 주소를 입력해 주세요.

```
    <form>  <label class="block">    <span class="...">Email</span>    <input type="email" class="peer ..." />    <p class="invisible peer-invalid:visible ...">Please provide a valid email address.</p>  </label></form>
```

이렇게 하면 JS 없이도 예를 들어 [플로팅 레이블](https://www.youtube.com/watch?v=nJzKi6oIvBA) 같은 다양한 멋진 트릭을 구현할 수 있습니다.

이 패턴은 모든 의사 클래스 variant에서 동작합니다. 예를 들어 `peer-focus`, `peer-required`, `peer-disabled`를 사용할 수 있습니다.

`peer` 마커는 CSS에서 [subsequent-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Subsequent-sibling_combinator)가 동작하는 방식 때문에 _이전_ 형제 요소에만 사용할 수 있다는 점에 유의해야 합니다:

작동하지 않음, 오직 이전 형제 요소만 peer로 표시할 수 있습니다

```
    <label>  <span class="peer-invalid:text-red-500 ...">Email</span>  <input type="email" class="peer ..." /></label>
```

#

- peer 구분하기

여러 peer를 사용할 때는 `peer/{name}` 클래스를 사용해 특정 peer에 고유한 이름을 부여하고, `peer-checked/{name}` 같은 클래스로 variant에 그 이름을 포함해 _특정_ peer의 상태에 따라 스타일을 적용할 수 있습니다:

게시 상태

초안게시됨

초안은 관리자에게만 표시됩니다.

게시물이 사이트에 공개적으로 표시됩니다.

```
    <fieldset>  <legend>Published status</legend>  <input id="draft" class="peer/draft" type="radio" name="status" checked />  <label for="draft" class="peer-checked/draft:text-sky-500">Draft</label>  <input id="published" class="peer/published" type="radio" name="status" />  <label for="published" class="peer-checked/published:text-sky-500">Published</label>  <div class="hidden peer-checked/draft:block">Drafts are only visible to administrators.</div>  <div class="hidden peer-checked/published:block">Your post will be publicly visible on your site.</div></fieldset>
```

peer의 이름은 원하는 대로 지정할 수 있으며 별도 설정도 필요하지 않습니다. 마크업에서 peer에 직접 이름만 붙이면 Tailwind가 필요한 CSS를 자동으로 생성합니다.

#

- 임의 peer

대괄호 사이에 [arbitrary value](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values)로 직접 선택자를 넣으면, 즉석에서 일회성 `peer-*` variant를 만들 수 있습니다:

HTML

생성된 CSS

```
    <form>  <label for="email">Email:</label>  <input id="email" name="email" type="email" class="is-dirty peer" required />  <div class="peer-[.is-dirty]:peer-required:block hidden">This field is required.</div>  <!-- ... --></form>
```

더 세밀하게 제어하려면 `&` 문자를 사용해 전달한 선택자 기준으로 최종 선택자에서 `.peer`가 들어갈 위치를 표시할 수 있습니다:

HTML

생성된 CSS

```
    <div>  <input type="text" class="peer" />  <div class="hidden peer-[:nth-of-type(3)_&]:block">    <!-- ... -->  </div></div>
```

## 의사 요소

- ::before and ::after

`before` 및 `after` variant를 사용해 `::before`와 `::after` 의사 요소에 스타일을 적용하세요:

이메일

```
    <label>  <span class="text-gray-700 after:ml-0.5 after:text-red-500 after:content-['*'] ...">Email</span>  <input type="email" name="email" class="..." placeholder="you@example.com" /></label>
```

이 variant들을 사용할 때 Tailwind는 기본적으로 `content: ''`를 자동 추가하므로, 다른 값을 원하지 않는 한 직접 지정할 필요가 없습니다:

> 항상 짜증난 표정을 하고 있으면 사람들은 네가 바쁘다고 생각한다.

```
    <blockquote class="text-center text-2xl font-semibold text-gray-900 italic dark:text-white">  When you look  <span class="relative inline-block before:absolute before:-inset-1 before:block before:-skew-y-3 before:bg-pink-500">    <span class="relative text-white dark:text-gray-950">annoyed</span>  </span>  all the time, people think that you're busy.</blockquote>
```

Tailwind 프로젝트에서는 대부분의 경우 `::before`, `::after` 의사 요소가 꼭 필요하지 않다는 점도 알아둘 만합니다. 보통 실제 HTML 요소를 사용하는 편이 더 단순합니다.

예를 들어 아래는 위와 동일한 디자인을 `::before` 의사 요소 대신 `<span>`으로 구현한 것으로, 읽기도 조금 더 쉽고 코드도 실제로 더 적습니다:

```
    <blockquote class="text-center text-2xl font-semibold text-gray-900 italic">  When you look  <span class="relative">    <span class="absolute -inset-1 block -skew-y-3 bg-pink-500" aria-hidden="true"></span>    <span class="relative text-white">annoyed</span>  </span>  all the time, people think that you're busy.</blockquote>
```

의사 요소의 콘텐츠가 실제 DOM에 존재하면 안 되고 사용자가 선택할 수 없어야 하는 상황에서만 `before`, `after`를 사용하세요.

- ::placeholder

`placeholder` variant를 사용해 모든 input 또는 textarea의 플레이스홀더 텍스트에 스타일을 적용하세요:

검색

```
    <input  class="placeholder:text-gray-500 placeholder:italic ..."  placeholder="Search for anything..."  type="text"  name="search"/>
```

- ::file

`file` variant를 사용해 파일 입력의 버튼에 스타일을 적용하세요:

![현재 프로필 사진](https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1361&q=80)

프로필 사진 선택

```
    <input  type="file"  class="file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-violet-700 hover:file:bg-violet-100 dark:file:bg-violet-600 dark:file:text-violet-100 dark:hover:file:bg-violet-500 ..."/>
```

- ::marker

`marker` variant를 사용해 목록의 카운터나 불릿에 스타일을 적용하세요:

## 재료

- 다진 포르치니 버섯 5컵
- 올리브 오일 1/2컵
- 셀러리 3lb

```
    <ul role="list" class="list-disc marker:text-sky-400 ...">  <li>5 cups chopped Porcini mushrooms</li>  <li>1/2 cup of olive oil</li>  <li>3lb of celery</li></ul>
```

`marker` variant는 상속 가능하도록 설계되어 있어, `<li>` 요소에 직접 사용할 수도 있지만 반복을 줄이기 위해 부모 요소에 적용할 수도 있습니다.

- ::selection

`selection` variant를 사용해 활성 텍스트 선택 영역에 스타일을 적용하세요:

마우스로 이 텍스트 일부를 선택해 보세요

그래서 나는 물속으로 걸어 들어가기 시작했다. 솔직히 말하면, 얘들아, 정말 무서웠다. 하지만 계속 나아갔고, 파도를 지나가자 이상한 평온함이 나를 덮쳤다. 그게 신의 개입이었는지 모든 생명체의 유대감이었는지는 모르겠지만, 제리, 그 순간 나는 _정말_ 해양생물학자였다.

```
    <div class="selection:bg-fuchsia-300 selection:text-fuchsia-900">  <p>    So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my    way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all    living things but I tell you Jerry at that moment, I <em>was</em> a marine biologist.  </p></div>
```

`selection` variant는 상속 가능하도록 설계되어 있어 트리 어디에든 추가하면 모든 하위 요소에 적용됩니다.

덕분에 사이트 전체에서 브랜드에 맞는 선택 색상을 손쉽게 설정할 수 있습니다:

```
    <html>  <head>    <!-- ... -->  </head>  <body class="selection:bg-pink-300">    <!-- ... -->  </body></html>
```

- ::first-line and ::first-letter

`first-line` variant로 콘텐츠 블록의 첫 줄에, `first-letter` variant로 첫 글자에 스타일을 적용하세요:

좋아, 내가 한마디 해줄게, 웃긴 친구. "New York Public Library"라고 적힌 그 작은 도장 알지? 그게 너한텐 별거 아닐지 몰라도, 나한텐 엄청난 의미야. 정말 엄청나게 말이야.

그래, 원하면 웃어도 돼. 너 같은 타입 많이 봤어. 화려하고, 이목을 끌고, 관습을 과시하듯 무시하는 타입. 그래, 네가 무슨 생각하는지 알아. 이 사람은 낡은 도서관 책 가지고 왜 이렇게 난리를 치는 거지? 힌트를 하나 줄게, 친구.

```
    <div class="text-gray-700">  <p    class="first-letter:float-left first-letter:mr-3 first-letter:text-7xl first-letter:font-bold first-letter:text-gray-900 first-line:tracking-widest first-line:uppercase"  >    Well, let me tell you something, funny boy. Y'know that little stamp, the one that says "New York Public Library"?  </p>  <p class="mt-6">Well that may not mean anything to you, but that means a lot to me. One whole hell of a lot.</p></div>
```

- ::backdrop

`backdrop` variant를 사용해 [native `<dialog>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)의 배경(backdrop)에 스타일을 적용하세요:

```
    <dialog class="backdrop:bg-gray-50">  <form method="dialog">    <!-- ... -->  </form></dialog>
```

프로젝트에서 native `<dialog>` 요소를 사용 중이라면, `open` variant를 사용한 [styling open/closed states](https://tailwindcss.com/docs/hover-focus-and-other-states#openclosed-state)도 함께 읽어보는 것이 좋습니다.

## 미디어 및 기능 쿼리

- 반응형 브레이크포인트

특정 브레이크포인트에서 요소에 스타일을 적용하려면 `md`, `lg` 같은 반응형 variant를 사용하세요.

예를 들어 다음은 모바일에서는 3열 그리드, 중간 너비 화면에서는 4열, 큰 화면에서는 6열 그리드를 렌더링합니다:

```
    <div class="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6">  <!-- ... --></div>
```

뷰포트 대신 부모 요소의 너비를 기준으로 스타일을 적용하려면 `@md`, `@lg` 같은 variant를 사용하세요:

```
    <div class="@container">  <div class="flex flex-col @md:flex-row">    <!-- ... -->  </div></div>
```

이 기능이 동작하는 방식을 자세히 보려면 [Responsive design](https://tailwindcss.com/docs/responsive-design) 문서를 확인하세요.

- prefers-color-scheme

`prefers-color-scheme` 미디어 쿼리는 사용자가 라이트 테마와 다크 테마 중 무엇을 선호하는지 알려주며, 보통 운영체제 수준에서 설정됩니다.

라이트 모드는 variant 없이 유틸리티를 사용하고, 다크 모드 오버라이드는 `dark` variant를 사용하세요:

라이트 모드

거꾸로도 작성 가능

Zero Gravity Pen은 거꾸로를 포함해 어떤 방향에서도 쓸 수 있습니다. 심지어 우주 공간에서도 작동합니다.

다크 모드

거꾸로도 작성 가능

Zero Gravity Pen은 거꾸로를 포함해 어떤 방향에서도 쓸 수 있습니다. 심지어 우주 공간에서도 작동합니다.

```
    <div class="bg-white dark:bg-gray-900 ...">  <!-- ... -->  <h3 class="text-gray-900 dark:text-white ...">Writes upside-down</h3>  <p class="text-gray-500 dark:text-gray-400 ...">    The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer space.  </p></div>
```

이 기능이 동작하는 방식을 자세히 보려면 [Dark Mode](https://tailwindcss.com/docs/dark-mode) 문서를 확인하세요.

- prefers-reduced-motion

`prefers-reduced-motion` 미디어 쿼리는 사용자가 불필요한 모션을 최소화해 달라고 요청했는지 알려줍니다.

사용자가 모션 감소를 요청한 경우에만 조건부로 스타일을 추가하려면 `motion-reduce` variant를 사용하세요:

개발자 도구에서 `prefers-reduced-motion: reduce`를 에뮬레이션해 스피너가 숨겨지는지 확인해 보세요

처리 중...

```
    <button type="button" class="bg-indigo-500 ..." disabled>  <svg class="animate-spin motion-reduce:hidden ..." viewBox="0 0 24 24"><!-- ... --></svg>  Processing...</button>
```

Tailwind에는 사용자가 모션 감소를 _요청하지 않았을 때만_ 스타일을 추가하는 `motion-safe` variant도 있습니다. `motion-reduce` 헬퍼를 쓰면 많은 스타일을 다시 "되돌려야" 하는 경우에 유용합니다:

```
    <!-- Using `motion-reduce` can mean lots of "undoing" styles --><button class="transition hover:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0 ...">  Save changes</button><!-- Using `motion-safe` is less code in these situations --><button class="motion-safe:transition motion-safe:hover:-translate-x-0.5 ...">Save changes</button>
```

- prefers-contrast

`prefers-contrast` 미디어 쿼리는 사용자가 대비를 더 높이거나 낮추길 요청했는지 알려줍니다.

사용자가 더 높은 대비를 요청했을 때만 조건부로 스타일을 추가하려면 `contrast-more` variant를 사용하세요:

개발자 도구에서 `prefers-contrast: more`를 에뮬레이션해 변경 사항을 확인해 보세요

사회보장번호

신원 도용을 위해 필요합니다.

```
    <label class="block">  <span class="block text-sm font-medium text-gray-700">Social Security Number</span>  <input    class="border-gray-200 placeholder-gray-400 contrast-more:border-gray-400 contrast-more:placeholder-gray-500 ..."  />  <p class="text-gray-600 opacity-10 contrast-more:opacity-100 ...">We need this to steal your identity.</p></label>
```

Tailwind에는 사용자가 더 낮은 대비를 요청했을 때 조건부로 스타일을 추가할 수 있는 `contrast-less` variant도 포함되어 있습니다.

- forced-colors

`forced-colors` 미디어 쿼리는 사용자가 강제 색상 모드를 쓰는지 나타냅니다. 이 모드는 텍스트, 배경, 링크, 버튼 색상을 사용자 정의 팔레트로 사이트 색상 위에 덮어씁니다.

사용자가 강제 색상 모드를 활성화했을 때만 조건부로 스타일을 추가하려면 `forced-colors` variant를 사용하세요:

개발자 도구에서 `forced-colors: active`를 에뮬레이션해 변경 사항을 확인해 보세요

테마 선택:

시안

블루

인디고

퍼플

```
    <label>  <input type="radio" class="appearance-none forced-colors:appearance-auto" />  <p class="hidden forced-colors:block">Cyan</p>  <div class="bg-cyan-200 forced-colors:hidden ..."></div>  <div class="bg-cyan-500 forced-colors:hidden ..."></div></label>
```

사용자가 강제 색상 모드를 _사용하지 않을 때_ 조건부로 스타일을 적용하려면 `not-forced-colors` variant를 사용하세요:

```
    <div class="not-forced-colors:appearance-none ...">  <!-- ... --></div>
```

Tailwind에는 강제 색상 사용 여부를 선택할 수 있는 [forced color adjust](https://tailwindcss.com/docs/forced-color-adjust) 유틸리티도 포함되어 있습니다.

- inverted-colors

사용자가 반전 색상 스킴을 활성화했을 때 조건부로 스타일을 추가하려면 `inverted-colors` variant를 사용하세요:

```
    <div class="shadow-xl inverted-colors:shadow-none ...">  <!-- ... --></div>
```

- pointer and any-pointer

`pointer` 미디어 쿼리는 사용자가 마우스 같은 기본 포인팅 장치를 가지고 있는지, 그리고 그 장치의 정확도가 어느 정도인지 알려줍니다.

`pointer-fine` variant는 마우스나 트랙패드처럼 정확한 포인팅 장치를 대상으로 하고, `pointer-coarse` variant는 터치스크린처럼 덜 정확한 포인팅 장치를 대상으로 합니다. 이는 터치 기기에서 더 큰 클릭 영역을 제공할 때 유용합니다:

개발자 도구에서 터치 기기를 에뮬레이션해 변경 사항을 확인해 보세요

RAM

[성능 사양 보기](https://tailwindcss.com/docs/hover-focus-and-other-states)

4 GB8 GB16 GB32 GB64 GB128 GB

```
    <fieldset aria-label="Choose a memory option">  <div class="flex items-center justify-between">    <div>RAM</div>    <a href="#"> See performance specs </a>  </div>  <div class="mt-4 grid grid-cols-6 gap-2 pointer-coarse:mt-6 pointer-coarse:grid-cols-3 pointer-coarse:gap-4">    <label class="p-2 pointer-coarse:p-4 ...">      <input type="radio" name="memory-option" value="4 GB" className="sr-only" />      <span>4 GB</span>    </label>    <!-- ... -->  </div></fieldset>
```

`pointer`는 기본 포인팅 장치만 대상으로 하지만, `any-pointer`는 사용 가능한 모든 포인팅 장치를 대상으로 합니다. 연결된 포인팅 장치 중 하나 이상이 조건을 충족할 때 다른 스타일을 제공하려면 `any-pointer-fine`, `any-pointer-coarse` variant를 사용하세요.

포인팅 장치가 없는 경우를 대상으로 하려면 `pointer-none`, `any-pointer-none`을 사용할 수 있습니다.

- orientation

뷰포트가 특정 방향일 때만 조건부로 스타일을 추가하려면 `portrait`, `landscape` variant를 사용하세요:

```
    <div>  <div class="portrait:hidden">    <!-- ... -->  </div>  <div class="landscape:hidden">    <p>This experience is designed to be viewed in landscape. Please rotate your device to view the site.</p>  </div></div>
```

- scripting

사용자에게 JavaScript 같은 스크립팅이 활성화되어 있는지에 따라 조건부로 스타일을 추가하려면 `noscript` variant를 사용하세요:

```
    <div class="hidden noscript:block">  <p>This experience requires JavaScript to function. Please enable JavaScript in your browser settings.</p></div>
```

- print

문서가 인쇄될 때만 적용되는 조건부 스타일을 추가하려면 `print` variant를 사용하세요:

```
    <div>  <article class="print:hidden">    <h1>My Secret Pizza Recipe</h1>    <p>This recipe is a secret, and must not be shared with anyone</p>    <!-- ... -->  </article>  <div class="hidden print:block">Are you seriously trying to print this? It's secret!</div></div>
```

- @supports

사용자 브라우저에서 특정 기능이 지원되는지에 따라 스타일을 적용하려면 `supports-[...]` variant를 사용하세요:

```
    <div class="flex supports-[display:grid]:grid ...">  <!-- ... --></div>
```

내부적으로 `supports-[...]` variant는 [`@supports rules`](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)를 생성하며, 대괄호 안에는 속성/값 쌍은 물론 `and`, `or`를 사용하는 표현식까지 `@supports (...)`에 넣을 수 있는 모든 내용을 사용할 수 있습니다.

간결함을 위해 특정 값이 아니라 속성 지원 여부만 확인하면 된다면 속성 이름만 지정해도 됩니다:

```
    <div class="bg-black/75 supports-backdrop-filter:bg-black/25 supports-backdrop-filter:backdrop-blur ...">  <!-- ... --></div>
```

사용자 브라우저에서 특정 기능이 지원되지 않는지에 따라 스타일을 적용하려면 `not-supports-[...]` variant를 사용하세요:

```
    <div class="not-supports-[display:grid]:flex">  <!-- ... --></div>
```

프로젝트에서 자주 사용하는 `@supports` 규칙의 단축키를 `supports-*` 네임스페이스에 새 variant를 만들어 구성할 수 있습니다:

```
    @custom-variant supports-grid {  @supports (display: grid) {    @slot;  }}
```

그다음 프로젝트에서 이 사용자 정의 `supports-*` variant를 사용할 수 있습니다:

```
    <div class="supports-grid:grid">  <!-- ... --></div>
```

- @starting-style

요소가 DOM에 처음 렌더링될 때 또는 `display: none`에서 보이는 상태로 전환될 때의 모양을 설정하려면 `starting` variant를 사용하세요:

```
    <div>  <button popovertarget="my-popover">Check for updates</button>  <div popover id="my-popover" class="opacity-0 starting:open:opacity-0 ...">    <!-- ... -->  </div></div>
```

## 속성 선택자

- ARIA states

[ARIA attributes](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes)를 기준으로 조건부 스타일을 적용하려면 `aria-*` variant를 사용하세요.

예를 들어 `aria-checked` 속성이 `true`일 때 `bg-sky-700` 클래스를 적용하려면 `aria-checked:bg-sky-700` 클래스를 사용하세요:

```
    <div aria-checked="true" class="bg-gray-600 aria-checked:bg-sky-700">  <!-- ... --></div>
```

기본적으로 가장 일반적인 불리언 ARIA 속성에 대한 variant가 포함되어 있습니다:

| 변형            | CSS                       |
| --------------- | ------------------------- |
| `aria-busy`     | `&[aria-busy="true"]`     |
| `aria-checked`  | `&[aria-checked="true"]`  |
| `aria-disabled` | `&[aria-disabled="true"]` |
| `aria-expanded` | `&[aria-expanded="true"]` |
| `aria-hidden`   | `&[aria-hidden="true"]`   |
| `aria-pressed`  | `&[aria-pressed="true"]`  |
| `aria-readonly` | `&[aria-readonly="true"]` |
| `aria-required` | `&[aria-required="true"]` |
| `aria-selected` | `&[aria-selected="true"]` |

새 variant를 만들어 사용 가능한 `aria-*` variant를 사용자 지정할 수 있습니다:

```
    @custom-variant aria-asc (&[aria-sort="ascending"]);@custom-variant aria-desc (&[aria-sort="descending"]);
```

프로젝트에 포함하기에는 적절하지 않은 일회성 `aria` variant를 사용해야 하거나, 특정 값을 받는 더 복잡한 ARIA 속성을 다뤄야 한다면, 대괄호를 사용해 임의 값으로 속성을 즉석에서 생성할 수 있습니다:

| 송장 번호 | 고객                        | 금액       |
| --------- | --------------------------- | ---------- |
| #100      | Pendant Publishing          | $2,000.00  |
| #101      | Kruger Industrial Smoothing | $545.00    |
| #102      | J. Peterman                 | $10,000.25 |

HTML

생성된 CSS

```
    <table>  <thead>    <tr>      <th        aria-sort="ascending"        class="aria-[sort=ascending]:bg-[url('/img/down-arrow.svg')] aria-[sort=descending]:bg-[url('/img/up-arrow.svg')]"      >        Invoice #      </th>      <!-- ... -->    </tr>  </thead>  <!-- ... --></table>
```

ARIA state variant는 `group-aria-*` 및 `peer-aria-*` variant를 사용해 부모 및 형제 요소도 대상으로 지정할 수 있습니다:

HTML

생성된 CSS

```
    <table>  <thead>    <tr>    <th aria-sort="ascending" class="group">      Invoice #      <svg class="group-aria-[sort=ascending]:rotate-0 group-aria-[sort=descending]:rotate-180"><!-- ... --></svg>    </th>    <!-- ... -->    </tr>  </thead>  <!-- ... --></table>
```

- 데이터 속성

`data-*` variant를 사용하면 [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)를 기준으로 조건부 스타일을 적용할 수 있습니다.

데이터 속성이 존재하는지(특정 값이 아닌지) 확인하려면 속성 이름만 지정하면 됩니다:

```
    <!-- Will apply --><div data-active class="border border-gray-300 data-active:border-purple-500">  <!-- ... --></div><!-- Will not apply --><div class="border border-gray-300 data-active:border-purple-500">  <!-- ... --></div>
```

특정 값을 확인해야 한다면 임의 값을 사용할 수 있습니다:

```
    <!-- Will apply --><div data-size="large" class="data-[size=large]:p-8">  <!-- ... --></div><!-- Will not apply --><div data-size="medium" class="data-[size=large]:p-8">  <!-- ... --></div>
```

또는 `data-*` 네임스페이스에 새 variant를 만들어 프로젝트에서 자주 쓰는 데이터 속성에 대한 단축키를 구성할 수 있습니다:

app.css

```
    @import "tailwindcss";@custom-variant data-checked (&[data-ui~="checked"]);
```

그다음 프로젝트에서 이 사용자 정의 `data-*` variant를 사용할 수 있습니다:

```
    <div data-ui="checked active" class="data-checked:underline">  <!-- ... --></div>
```

- RTL 지원

다중 방향 레이아웃을 만들 때 `rtl` 및 `ltr` variant를 사용하면 각각 오른쪽-왼쪽, 왼쪽-오른쪽 모드에서 조건부로 스타일을 추가할 수 있습니다:

왼쪽에서 오른쪽

![](https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Tom Cook

운영 이사

오른쪽에서 왼쪽

![](https://images.unsplash.com/photo-1563833717765-00462801314e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

تامر كرم

الرئيس التنفيذي

```
    <div class="group flex items-center">  <img class="h-12 w-12 shrink-0 rounded-full" src="..." alt="" />  <div class="ltr:ml-3 rtl:mr-3">    <p class="text-gray-700 group-hover:text-gray-900 ...">...</p>    <p class="text-gray-500 group-hover:text-gray-700 ...">...</p>  </div></div>
```

이 variant는 왼쪽-오른쪽과 오른쪽-왼쪽 레이아웃을 _모두_ 지원해야 하는 사이트를 만들 때만 유용하다는 점을 기억하세요. 한 방향만 지원하면 되는 사이트라면 이 variant는 필요 없고, 콘텐츠에 맞는 스타일만 적용하면 됩니다.

- 열림/닫힘 상태

`open` variant를 사용하면 `<details>` 또는 `<dialog>` 요소가 열린 상태일 때 조건부로 스타일을 추가할 수 있습니다:

공개 영역을 토글해 스타일이 바뀌는지 확인해 보세요

왜 이름이 Ovaltine일까요?

머그컵도 둥글고 병도 둥근데, Roundtine이라고 불러야 하지 않을까요.

```
    <details class="border border-transparent open:border-black/10 open:bg-gray-100 ..." open>  <summary class="text-sm leading-6 font-semibold text-gray-900 select-none">Why do they call it Ovaltine?</summary>  <div class="mt-3 text-sm leading-6 text-gray-600">    <p>The mug is round. The jar is round. They should call it Roundtine.</p>  </div></details>
```

이 variant는 popover의 `:popover-open` 의사 클래스도 대상으로 합니다:

```
    <div>  <button popovertarget="my-popover">Open Popover</button>  <div popover id="my-popover" class="opacity-0 open:opacity-100 ...">    <!-- ... -->  </div></div>
```

- inert 요소 스타일링

`inert` variant를 사용하면 `inert` 속성이 지정된 요소를 스타일링할 수 있습니다:

알림 설정

사용자 지정

댓글

누군가 게시물에 댓글을 달면 알림을 받습니다.

멘션

누군가 나를 멘션하면 알림을 받습니다.

모두

```
    <form>  <legend>Notification preferences</legend>  <fieldset>    <input type="radio" />    <label> Custom </label>    <fieldset inert class="inert:opacity-50">      <!-- ... -->    </fieldset>    <input type="radio" />    <label> Everything </label>  </fieldset></form>
```

이는 콘텐츠의 일부가 상호작용 불가 상태임을 시각적으로 명확하게 보여주는 단서를 추가할 때 유용합니다.

## 자식 선택자

- 직계 자식 스타일링

일반적으로는 유틸리티 클래스를 자식 요소에 직접 두는 것이 더 좋지만, 제어할 수 없는 직계 자식을 스타일링해야 하는 상황에서는 `*` variant를 사용할 수 있습니다:

## 카테고리

영업

마케팅

SEO

분석

디자인

전략

보안

성장

모바일

UX/UI

```
    <div>  <h2>Categories<h2>  <ul class="*:rounded-full *:border *:border-sky-100 *:bg-sky-50 *:px-2 *:py-0.5 dark:text-sky-300 dark:*:border-sky-500/15 dark:*:bg-sky-500/10 ...">    <li>Sales</li>    <li>Marketing</li>    <li>SEO</li>    <!-- ... -->  </ul></div>
```

중요한 점은 자식 자체에 유틸리티를 직접 적용해도 스타일을 덮어쓸 수 없다는 것입니다. 자식 규칙은 일반 규칙 뒤에 생성되고, specificity도 동일하기 때문입니다:

작동하지 않습니다. 자식은 부모가 지정한 스타일을 덮어쓸 수 없습니다.

```
    <ul class="*:bg-sky-50 ...">  <li class="bg-red-50 ...">Sales</li>  <li>Marketing</li>  <li>SEO</li>  <!-- ... --></ul>
```

- 모든 하위 요소 스타일링

`*`와 마찬가지로 `**` variant도 요소의 자식을 스타일링하는 데 사용할 수 있습니다. 핵심 차이는 `**`가 직계 자식뿐 아니라 _모든_ 하위 요소에 스타일을 적용한다는 점입니다. 특히 다른 variant와 결합해 선택 대상을 좁힐 때 매우 유용합니다:

- ![](https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

[Leslie Abbott](https://tailwindcss.com/docs/hover-focus-and-other-states)

공동 창립자 / CEO

- ![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

[Hector Adams](https://tailwindcss.com/docs/hover-focus-and-other-states)

마케팅 부사장

- ![](https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

[Blake Alexander](https://tailwindcss.com/docs/hover-focus-and-other-states)

어카운트 코디네이터

```
    <ul class="**:data-avatar:size-12 **:data-avatar:rounded-full ...">  {#each items as item}    <li>      <img src={item.src} data-avatar />      <p>{item.name}</p>    </li>  {/each}</ul>
```

## 사용자 정의 variants

- 임의 variants 사용하기

[arbitrary values](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values)를 사용하면 유틸리티 클래스에 사용자 정의 값을 쓸 수 있는 것처럼, arbitrary variants를 사용하면 HTML에서 사용자 정의 selector variant를 직접 작성할 수 있습니다.

Arbitrary variant는 selector를 나타내는 형식 문자열(format string)이며, 대괄호로 감쌉니다. 예를 들어 다음 arbitrary variant는 요소에 `is-dragging` 클래스가 있을 때 커서를 `grabbing`으로 변경합니다:

HTML

생성된 CSS

```
    <ul role="list">  {#each items as item}    <li class="[&.is-dragging]:cursor-grabbing">{item}</li>  {/each}</ul>
```

Arbitrary variant는 Tailwind의 다른 variant와 마찬가지로 내장 variant와, 또는 arbitrary variant끼리 서로 쌓아 사용할 수 있습니다:

HTML

생성된 CSS

```
    <ul role="list">  {#each items as item}    <li class="[&.is-dragging]:active:cursor-grabbing">{item}</li>  {/each}</ul>
```

selector에 공백이 필요하다면 밑줄을 사용할 수 있습니다. 예를 들어 다음 arbitrary variant는 클래스를 추가한 요소 내부의 모든 `p` 요소를 선택합니다:

HTML

생성된 CSS

```
    <div class="[&_p]:mt-4">  <p>Lorem ipsum...</p>  <ul>    <li>      <p>Lorem ipsum...</p>    </li>    <!-- ... -->  </ul></div>
```

Arbitrary variant에서 `@media`나 `@supports` 같은 at-rule도 사용할 수 있습니다:

HTML

생성된 CSS

```
    <div class="flex [@supports(display:grid)]:grid">  <!-- ... --></div>
```

at-rule 사용자 정의 variant에서는 전처리기 중첩과 마찬가지로 `&` 플레이스홀더가 필요하지 않습니다.

- 사용자 정의 variant 등록하기

프로젝트에서 같은 arbitrary variant를 여러 번 사용한다면, `@custom-variant` 지시어를 사용해 사용자 정의 variant를 만드는 것이 좋습니다:

```
    @custom-variant theme-midnight (&:where([data-theme="midnight"] *));
```

이제 HTML에서 `theme-midnight:<utility>` variant를 사용할 수 있습니다:

```
    <html data-theme="midnight">  <button class="theme-midnight:bg-black ..."></button></html>
```

사용자 정의 variant 추가에 대한 자세한 내용은 [adding custom variants documentation](https://tailwindcss.com/docs/adding-custom-styles#adding-custom-variants)에서 확인하세요.

## 부록

- 빠른 참조

Tailwind에 기본 포함된 모든 variant의 빠른 참조 표입니다.

| 변형                                                                                                   | CSS                                   |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| [hover](https://tailwindcss.com/docs/hover-focus-and-other-states#hover)                               | `@media (hover: hover) {  &:hover  }` |
| [focus](https://tailwindcss.com/docs/hover-focus-and-other-states#focus)                               | `&:focus`                             |
| [focus-within](https://tailwindcss.com/docs/hover-focus-and-other-states#focus-within)                 | `&:focus-within`                      |
| [focus-visible](https://tailwindcss.com/docs/hover-focus-and-other-states#focus-visible)               | `&:focus-visible`                     |
| [active](https://tailwindcss.com/docs/hover-focus-and-other-states#active)                             | `&:active`                            |
| [visited](https://tailwindcss.com/docs/hover-focus-and-other-states#visited)                           | `&:visited`                           |
| [target](https://tailwindcss.com/docs/hover-focus-and-other-states#target)                             | `&:target`                            |
| [\*](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-direct-children)                | `:is(& > *)`                          |
| [\*\*](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-all-descendants)              | `:is(& *)`                            |
| [has-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#has)                             | `&:has(...)`                          |
| [group-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-parent-state) | `&:is(:where(.group)... *)`           |
| [peer-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-sibling-state) | `&:is(:where(.peer)... ~ *)`          |
| [in-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#implicit-groups)                  | `:where(...) &`                       |
| [not-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#not)                             | `&:not(...)`                          |
| [inert](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-inert-elements)              | `&:is([inert], [inert] *)`            |
| [first](https://tailwindcss.com/docs/hover-focus-and-other-states#first)                               | `&:first-child`                       |
| [last](https://tailwindcss.com/docs/hover-focus-and-other-states#last)                                 | `&:last-child`                        |
| [only](https://tailwindcss.com/docs/hover-focus-and-other-states#only)                                 | `&:only-child`                        |
| [odd](https://tailwindcss.com/docs/hover-focus-and-other-states#odd)                                   | `&:nth-child(odd)`                    |
| [even](https://tailwindcss.com/docs/hover-focus-and-other-states#even)                                 | `&:nth-child(even)`                   |
| [first-of-type](https://tailwindcss.com/docs/hover-focus-and-other-states#first-of-type)               | `&:first-of-type`                     |
| [last-of-type](https://tailwindcss.com/docs/hover-focus-and-other-states#last-of-type)                 | `&:last-of-type`                      |
| [only-of-type](https://tailwindcss.com/docs/hover-focus-and-other-states#only-of-type)                 | `&:only-of-type`                      |
| [nth-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#nth)                             | `&:nth-child(...)`                    |
| [nth-last-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#nth-last)                   | `&:nth-last-child(...)`               |
| [nth-of-type-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#nth-of-type)             | `&:nth-of-type(...)`                  |
| [nth-last-of-type-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#nth-last-of-type)   | `&:nth-last-of-type(...)`             |
| [empty](https://tailwindcss.com/docs/hover-focus-and-other-states#empty)                               | `&:empty`                             |
| [disabled](https://tailwindcss.com/docs/hover-focus-and-other-states#disabled)                         | `&:disabled`                          |
| [enabled](https://tailwindcss.com/docs/hover-focus-and-other-states#enabled)                           | `&:enabled`                           |
| [checked](https://tailwindcss.com/docs/hover-focus-and-other-states#checked)                           | `&:checked`                           |
| [indeterminate](https://tailwindcss.com/docs/hover-focus-and-other-states#indeterminate)               | `&:indeterminate`                     |
| [default](https://tailwindcss.com/docs/hover-focus-and-other-states#default)                           | `&:default`                           |
| [optional](https://tailwindcss.com/docs/hover-focus-and-other-states#optional)                         | `&:optional`                          |
| [required](https://tailwindcss.com/docs/hover-focus-and-other-states#required)                         | `&:required`                          |
| [valid](https://tailwindcss.com/docs/hover-focus-and-other-states#valid)                               | `&:valid`                             |
| [invalid](https://tailwindcss.com/docs/hover-focus-and-other-states#invalid)                           | `&:invalid`                           |
| [user-valid](https://tailwindcss.com/docs/hover-focus-and-other-states#user-valid)                     | `&:user-valid`                        |
| [user-invalid](https://tailwindcss.com/docs/hover-focus-and-other-states#user-invalid)                 | `&:user-invalid`                      |
| [in-range](https://tailwindcss.com/docs/hover-focus-and-other-states#in-range)                         | `&:in-range`                          |
| [out-of-range](https://tailwindcss.com/docs/hover-focus-and-other-states#out-of-range)                 | `&:out-of-range`                      |
| [placeholder-shown](https://tailwindcss.com/docs/hover-focus-and-other-states#placeholder-shown)       | `&:placeholder-shown`                 |
| [details-content](https://tailwindcss.com/docs/hover-focus-and-other-states#placeholder-shown)         | `&:details-content`                   |
| [autofill](https://tailwindcss.com/docs/hover-focus-and-other-states#autofill)                         | `&:autofill`                          |
| [read-only](https://tailwindcss.com/docs/hover-focus-and-other-states#read-only)                       | `&:read-only`                         |
| [before](https://tailwindcss.com/docs/hover-focus-and-other-states#before-and-after)                   | `&::before`                           |
| [after](https://tailwindcss.com/docs/hover-focus-and-other-states#before-and-after)                    | `&::after`                            |
| [first-letter](https://tailwindcss.com/docs/hover-focus-and-other-states#first-line-and-first-letter)  | `&::first-letter`                     |
| [first-line](https://tailwindcss.com/docs/hover-focus-and-other-states#first-line-and-first-letter)    | `&::first-line`                       |
| [marker](https://tailwindcss.com/docs/hover-focus-and-other-states#marker)                             | `&::marker, & *::marker`              |
| [selection](https://tailwindcss.com/docs/hover-focus-and-other-states#selection)                       | `&::selection`                        |
| [file](https://tailwindcss.com/docs/hover-focus-and-other-states#file)                                 | `&::file-selector-button`             |
| [backdrop](https://tailwindcss.com/docs/hover-focus-and-other-states#backdrop)                         | `&::backdrop`                         |
| [placeholder](https://tailwindcss.com/docs/hover-focus-and-other-states#placeholder)                   | `&::placeholder`                      |

[sm](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width >= 40rem)`
[md](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width >= 48rem)`
[lg](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width >= 64rem)`
[xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width >= 80rem)`
[2xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width >= 96rem)`
[min-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width >=  ...)`
[max-sm](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width < 40rem)`
[max-md](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width < 48rem)`
[max-lg](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width < 64rem)`
[max-xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width < 80rem)`
[max-2xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width < 96rem)`
[max-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@media (width < ...)`
[@3xs](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 16rem)`
[@2xs](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 18rem)`
[@xs](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 20rem)`
[@sm](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 24rem)`
[@md](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 28rem)`
[@lg](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 32rem)`
[@xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 36rem)`
[@2xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 42rem)`
[@3xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 48rem)`
[@4xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 56rem)`
[@5xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 64rem)`
[@6xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 72rem)`
[@7xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >= 80rem)`
[@min-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width >=  ...)`
[@max-3xs](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 16rem)`
[@max-2xs](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 18rem)`
[@max-xs](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 20rem)`
[@max-sm](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 24rem)`
[@max-md](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 28rem)`
[@max-lg](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 32rem)`
[@max-xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 36rem)`
[@max-2xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 42rem)`
[@max-3xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 48rem)`
[@max-4xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 56rem)`
[@max-5xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 64rem)`
[@max-6xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 72rem)`
[@max-7xl](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < 80rem)`
[@max-[...]](https://tailwindcss.com/docs/hover-focus-and-other-states#responsive-breakpoints)| `@container (width < ...)`
[dark](https://tailwindcss.com/docs/hover-focus-and-other-states#prefers-color-scheme)| `@media (prefers-color-scheme: dark)`
[motion-safe](https://tailwindcss.com/docs/hover-focus-and-other-states#prefers-reduced-motion)| `@media (prefers-reduced-motion: no-preference)`
[motion-reduce](https://tailwindcss.com/docs/hover-focus-and-other-states#prefers-reduced-motion)| `@media (prefers-reduced-motion: reduce)`
[contrast-more](https://tailwindcss.com/docs/hover-focus-and-other-states#prefers-contrast)| `@media (prefers-contrast: more)`
[contrast-less](https://tailwindcss.com/docs/hover-focus-and-other-states#prefers-contrast)| `@media (prefers-contrast: less)`
[forced-colors](https://tailwindcss.com/docs/hover-focus-and-other-states#forced-colors)| `@media (forced-colors: active)`
[inverted-colors](https://tailwindcss.com/docs/hover-focus-and-other-states#inverted-colors)| `@media (inverted-colors: inverted)`
[pointer-fine](https://tailwindcss.com/docs/hover-focus-and-other-states#pointer-and-any-pointer)| `@media (pointer: fine)`
[pointer-coarse](https://tailwindcss.com/docs/hover-focus-and-other-states#pointer-and-any-pointer)| `@media (pointer: coarse)`
[pointer-none](https://tailwindcss.com/docs/hover-focus-and-other-states#pointer-and-any-pointer)| `@media (pointer: none)`
[any-pointer-fine](https://tailwindcss.com/docs/hover-focus-and-other-states#pointer-and-any-pointer)| `@media (any-pointer: fine)`
[any-pointer-coarse](https://tailwindcss.com/docs/hover-focus-and-other-states#pointer-and-any-pointer)| `@media (any-pointer: coarse)`
[any-pointer-none](https://tailwindcss.com/docs/hover-focus-and-other-states#pointer-and-any-pointer)| `@media (any-pointer: none)`
[portrait](https://tailwindcss.com/docs/hover-focus-and-other-states#orientation)| `@media (orientation: portrait)`
[landscape](https://tailwindcss.com/docs/hover-focus-and-other-states#orientation)| `@media (orientation: landscape)`
[noscript](https://tailwindcss.com/docs/hover-focus-and-other-states#scripting)| `@media (scripting: none)`
[print](https://tailwindcss.com/docs/hover-focus-and-other-states#print)| `@media print`
[supports-[…]](https://tailwindcss.com/docs/hover-focus-and-other-states#supports)| `@supports (…)`
[aria-busy](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-busy="true"]`
[aria-checked](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-checked="true"]`
[aria-disabled](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-disabled="true"]`
[aria-expanded](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-expanded="true"]`
[aria-hidden](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-hidden="true"]`
[aria-pressed](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-pressed="true"]`
[aria-readonly](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-readonly="true"]`
[aria-required](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-required="true"]`
[aria-selected](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-selected="true"]`
[aria-[…]](https://tailwindcss.com/docs/hover-focus-and-other-states#aria-states)| `&[aria-…]`
[data-[…]](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes)| `&[data-…]`
[rtl](https://tailwindcss.com/docs/hover-focus-and-other-states#rtl-support)| `&:where(:dir(rtl), [dir="rtl"], [dir="rtl"] *)`
[ltr](https://tailwindcss.com/docs/hover-focus-and-other-states#rtl-support)| `&:where(:dir(ltr), [dir="ltr"], [dir="ltr"] *)`
[open](https://tailwindcss.com/docs/hover-focus-and-other-states#openclosed-state)| `&:is([open], :popover-open, :open)`
[starting](https://tailwindcss.com/docs/hover-focus-and-other-states#starting-style)| `@starting-style`

- 의사 클래스 레퍼런스

이 가이드 앞부분의 [의사 클래스 문서](https://tailwindcss.com/docs/hover-focus-and-other-states#pseudo-classes)를 보완하기 위해, Tailwind에 포함된 모든 의사 클래스 variant 예시를 종합해 정리한 목록입니다.

#

- :hover

`hover` variant를 사용해 사용자가 마우스 커서를 요소 위에 올렸을 때 스타일을 적용합니다:

```
    <div class="bg-black hover:bg-white ...">  <!-- ... --></div>
```

#

- :focus

`focus` variant를 사용해 요소에 포커스가 있을 때 스타일을 적용합니다:

```
    <input class="border-gray-300 focus:border-blue-400 ..." />
```

#

- :focus-within

`focus-within` variant를 사용해 요소 자신 또는 하위 요소 중 하나에 포커스가 있을 때 스타일을 적용합니다:

```
    <div class="focus-within:shadow-lg ...">  <input type="text" /></div>
```

#

- :focus-visible

`focus-visible` variant를 사용해 키보드로 포커스된 요소에 스타일을 적용합니다:

```
    <button class="focus-visible:outline-2 ...">Submit</button>
```

#

- :active

`active` variant를 사용해 요소가 눌리고 있는 동안 스타일을 적용합니다:

```
    <button class="bg-blue-500 active:bg-blue-600 ...">Submit</button>
```

#

- :visited

`visited` variant를 사용해 이미 방문한 링크에 스타일을 적용합니다:

```
    <a href="https://seinfeldquotes.com" class="text-blue-600 visited:text-purple-600 ..."> Inspiration </a>
```

#

- :target

`target` variant를 사용해 요소의 ID가 현재 URL fragment와 일치할 때 스타일을 적용합니다:

```
    <div id="about" class="target:shadow-lg ...">  <!-- ... --></div>
```

#

- :first-child

`first` variant를 사용해 요소가 첫 번째 자식일 때 스타일을 적용합니다:

```
    <ul>  {#each people as person}    <li class="py-4 first:pt-0 ...">      <!-- ... -->    </li>  {/each}</ul>
```

#

- :last-child

`last` variant를 사용해 요소가 마지막 자식일 때 스타일을 적용합니다:

```
    <ul>  {#each people as person}    <li class="py-4 last:pb-0 ...">      <!-- ... -->    </li>  {/each}</ul>
```

#

- :only-child

`only` variant를 사용해 요소가 유일한 자식일 때 스타일을 적용합니다:

```
    <ul>  {#each people as person}    <li class="py-4 only:py-0 ...">      <!-- ... -->    </li>  {/each}</ul>
```

#

- :nth-child(odd)

`odd` variant를 사용해 요소가 홀수 번째 자식일 때 스타일을 적용합니다:

```
    <table>  {#each people as person}    <tr class="bg-white odd:bg-gray-100 ...">      <!-- ... -->    </tr>  {/each}</table>
```

#

- :nth-child(even)

`even` variant를 사용해 요소가 짝수 번째 자식일 때 스타일을 적용합니다:

```
    <table>  {#each people as person}    <tr class="bg-white even:bg-gray-100 ...">      <!-- ... -->    </tr>  {/each}</table>
```

#

- :first-of-type

`first-of-type` variant를 사용해 요소가 해당 타입의 첫 번째 자식일 때 스타일을 적용합니다:

```
    <nav>  <img src="/logo.svg" alt="Vandelay Industries" />  {#each links as link}    <a href="#" class="ml-2 first-of-type:ml-6 ...">      <!-- ... -->    </a>  {/each}</nav>
```

#

- :last-of-type

`last-of-type` variant를 사용해 요소가 해당 타입의 마지막 자식일 때 스타일을 적용합니다:

```
    <nav>  <img src="/logo.svg" alt="Vandelay Industries" />  {#each links as link}    <a href="#" class="mr-2 last-of-type:mr-6 ...">      <!-- ... -->    </a>  {/each}  <button>More</button></nav>
```

#

- :only-of-type

`only-of-type` variant를 사용해 요소가 해당 타입의 유일한 자식일 때 스타일을 적용합니다:

```
    <nav>  <img src="/logo.svg" alt="Vandelay Industries" />  {#each links as link}    <a href="#" class="mx-2 only-of-type:mx-6 ...">      <!-- ... -->    </a>  {/each}  <button>More</button></nav>
```

#

- :nth-child()

`nth` variant를 사용해 특정 위치의 요소에 스타일을 적용합니다:

```
    <nav>  <img src="/logo.svg" alt="Vandelay Industries" />  {#each links as link}    <a href="#" class="mx-2 nth-3:mx-6 nth-[3n+1]:mx-7 ...">      <!-- ... -->    </a>  {/each}  <button>More</button></nav>
```

#

- :nth-last-child()

`nth-last` variant를 사용해 끝에서 특정 위치의 요소에 스타일을 적용합니다:

```
    <nav>  <img src="/logo.svg" alt="Vandelay Industries" />  {#each links as link}    <a href="#" class="mx-2 nth-last-3:mx-6 nth-last-[3n+1]:mx-7 ...">      <!-- ... -->    </a>  {/each}  <button>More</button></nav>
```

#

- :nth-of-type()

`nth-of-type` variant를 사용해 같은 타입 중 특정 위치의 요소에 스타일을 적용합니다:

```
    <nav>  <img src="/logo.svg" alt="Vandelay Industries" />  {#each links as link}    <a href="#" class="mx-2 nth-of-type-3:mx-6 nth-of-type-[3n+1]:mx-7 ...">      <!-- ... -->    </a>  {/each}  <button>More</button></nav>
```

#

- :nth-last-of-type()

`nth-last-of-type` variant를 사용해 같은 타입 중 끝에서 특정 위치의 요소에 스타일을 적용합니다:

```
    <nav>  <img src="/logo.svg" alt="Vandelay Industries" />  {#each links as link}    <a href="#" class="mx-2 nth-last-of-type-3:mx-6 nth-last-of-type-[3n+1]:mx-7 ...">      <!-- ... -->    </a>  {/each}  <button>More</button></nav>
```

#

- :empty

`empty` variant를 사용해 내용이 없는 요소에 스타일을 적용합니다:

```
    <ul>  {#each people as person}    <li class="empty:hidden ...">{person.hobby}</li>  {/each}</ul>
```

#

- :disabled

`disabled` variant를 사용해 비활성화된 input에 스타일을 적용합니다:

```
    <input class="disabled:opacity-75 ..." />
```

#

- :enabled

`enabled` variant를 사용해 활성화된 input에 스타일을 적용합니다. 이는 요소가 비활성화되지 않았을 때만 다른 스타일을 적용하고 싶을 때 특히 유용합니다:

```
    <input class="enabled:hover:border-gray-400 disabled:opacity-75 ..." />
```

#

- :checked

`checked` variant를 사용해 체크된 checkbox 또는 radio button에 스타일을 적용합니다:

```
    <input type="checkbox" class="appearance-none checked:bg-blue-500 ..." />
```

#

- :indeterminate

`indeterminate` variant를 사용해 indeterminate 상태의 checkbox 또는 radio button에 스타일을 적용합니다:

```
    <input type="checkbox" class="appearance-none indeterminate:bg-gray-300 ..." />
```

#

- :default

페이지가 처음 로드되었을 때 기본값이었던 option, checkbox 또는 radio button은 `default` variant를 사용해 스타일링합니다:

```
    <input type="checkbox" class="default:outline-2 ..." />
```

#

- :optional

선택 사항인 input은 `optional` variant를 사용해 스타일링합니다:

```
    <input class="border optional:border-red-500 ..." />
```

#

- :required

필수인 input은 `required` variant를 사용해 스타일링합니다:

```
    <input required class="border required:border-red-500 ..." />
```

#

- :valid

유효한 input은 `valid` variant를 사용해 스타일링합니다:

```
    <input required class="border valid:border-green-500 ..." />
```

#

- :invalid

유효하지 않은 input은 `invalid` variant를 사용해 스타일링합니다:

```
    <input required class="border invalid:border-red-500 ..." />
```

#

- :user-valid

유효하고 사용자가 상호작용한 input은 `user-valid` variant를 사용해 스타일링합니다:

```
    <input required class="border user-valid:border-green-500" />
```

#

- :user-invalid

유효하지 않고 사용자가 상호작용한 input은 `user-invalid` variant를 사용해 스타일링합니다:

```
    <input required class="border user-invalid:border-red-500" />
```

#

- :in-range

값이 지정된 범위 제한 내에 있는 input은 `in-range` variant를 사용해 스타일링합니다:

```
    <input min="1" max="5" class="in-range:border-green-500 ..." />
```

#

- :out-of-range

값이 지정된 범위 제한을 벗어난 input은 `out-of-range` variant를 사용해 스타일링합니다:

```
    <input min="1" max="5" class="out-of-range:border-red-500 ..." />
```

#

- :placeholder-shown

placeholder가 표시되고 있는 input은 `placeholder-shown` variant를 사용해 스타일링합니다:

```
    <input class="placeholder-shown:border-gray-500 ..." placeholder="you@example.com" />
```

#

- :details-content

`<details>` 요소의 콘텐츠는 `details-content` variant를 사용해 스타일링합니다:

```
    <details class="details-content:bg-gray-100 ...">  <summary>Details</summary>  This is a secret.</details>
```

#

- :autofill

브라우저가 자동 완성한 input은 `autofill` variant를 사용해 스타일링합니다:

```
    <input class="autofill:bg-yellow-200 ..." />
```

#

- :read-only

읽기 전용인 input은 `read-only` variant를 사용해 스타일링합니다:

```
    <input class="read-only:bg-gray-100 ..." />
```
