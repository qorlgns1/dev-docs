---
title: "animation - 전환 및 애니메이션 - Tailwind CSS"
description: "animate-spin 유틸리티를 사용하면 로딩 인디케이터 같은 요소에 선형 스핀 애니메이션을 추가할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/animation

# animation - 전환 및 애니메이션 - Tailwind CSS

| 클래스                        | 스타일                                                                                                                                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animate-spin`                | `animation: var(--animate-spin); /* spin 1s linear infinite */ @keyframes spin { to { transform: rotate(360deg); } }`                                                                                                                                               |
| `animate-ping`                | `animation: var(--animate-ping); /* ping 1s cubic-bezier(0, 0, 0.2, 1) infinite */ @keyframes ping { 75%, 100% { transform: scale(2); opacity: 0; } }`                                                                                                              |
| `animate-pulse`               | `animation: var(--animate-pulse); /* pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite */ @keyframes pulse { 50% { opacity: 0.5; } }`                                                                                                                                  |
| `animate-bounce`              | `animation: var(--animate-bounce); /* bounce 1s infinite */ @keyframes bounce { 0%, 100% { transform: translateY(-25%); animation-timing-function: cubic-bezier(0.8, 0, 1, 1); } 50% { transform: none; animation-timing-function: cubic-bezier(0, 0, 0.2, 1); } }` |
| `animate-none`                | `animation: none;`                                                                                                                                                                                                                                                  |
| `animate-(<custom-property>)` | `animation: var(<custom-property>);`                                                                                                                                                                                                                                |
| `animate-[<value>]`           | `animation: <value>;`                                                                                                                                                                                                                                               |

## 예제

- 스핀 애니메이션 추가하기

`animate-spin` 유틸리티를 사용하면 로딩 인디케이터 같은 요소에 선형 스핀 애니메이션을 추가할 수 있습니다:

처리 중…

```
    <button type="button" class="bg-indigo-500 ..." disabled>  <svg class="mr-3 size-5 animate-spin ..." viewBox="0 0 24 24">    <!-- ... -->  </svg>  Processing…</button>
```

- 핑 애니메이션 추가하기

`animate-ping` 유틸리티를 사용하면 요소가 레이더 핑이나 물결처럼 확대되고 사라지게 만들 수 있으며, 알림 배지 같은 경우에 유용합니다:

거래

```
    <span class="relative flex size-3">  <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-sky-400 opacity-75"></span>  <span class="relative inline-flex size-3 rounded-full bg-sky-500"></span></span>
```

- 펄스 애니메이션 추가하기

`animate-pulse` 유틸리티를 사용하면 요소가 부드럽게 나타났다 사라지도록 만들 수 있으며, 스켈레톤 로더 같은 경우에 유용합니다:

```
    <div class="mx-auto w-full max-w-sm rounded-md border border-blue-300 p-4">  <div class="flex animate-pulse space-x-4">    <div class="size-10 rounded-full bg-gray-200"></div>    <div class="flex-1 space-y-6 py-1">      <div class="h-2 rounded bg-gray-200"></div>      <div class="space-y-3">        <div class="grid grid-cols-3 gap-4">          <div class="col-span-2 h-2 rounded bg-gray-200"></div>          <div class="col-span-1 h-2 rounded bg-gray-200"></div>        </div>        <div class="h-2 rounded bg-gray-200"></div>      </div>    </div>  </div></div>
```

- 바운스 애니메이션 추가하기

`animate-bounce` 유틸리티를 사용하면 요소가 위아래로 튀도록 만들 수 있으며, "아래로 스크롤" 인디케이터 같은 경우에 유용합니다:

```
    <svg class="size-6 animate-bounce ...">  <!-- ... --></svg>
```

- 축소 모션 지원

사용자가 축소 모션을 선호하도록 설정한 경우에는 `motion-safe` 및 `motion-reduce` variant를 사용해 애니메이션과 트랜지션을 조건부로 적용할 수 있습니다:

```
    <button type="button" class="bg-indigo-600 ..." disabled>  <svg class="mr-3 size-5 motion-safe:animate-spin ..." viewBox="0 0 24 24">    <!-- ... -->  </svg>  Processing</button>
```

- 사용자 지정 값 사용하기

`animate-[<value>]` 문법을 사용하면 완전히 사용자 지정한 값으로 애니메이션을 설정할 수 있습니다:

```
    <div class="animate-[wiggle_1s_ease-in-out_infinite] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `animate-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <div class="animate-(--my-animation) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `animate-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`animation` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="animate-none md:animate-spin ...">  <!-- ... --></div>
```

variant 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.

## 테마 사용자 지정

`--animate-*` 테마 변수를 사용해 프로젝트의 애니메이션 유틸리티를 사용자 지정하세요:

```
    @theme {  --animate-wiggle: wiggle 1s ease-in-out infinite;  @keyframes wiggle {    0%,    100% {      transform: rotate(-3deg);    }    50% {      transform: rotate(3deg);    }  }}
```

이제 마크업에서 `animate-wiggle` 유틸리티를 사용할 수 있습니다:

```
    <div class="animate-wiggle">  <!-- ... --></div>
```

테마 사용자 지정에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
