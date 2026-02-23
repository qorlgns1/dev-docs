---
title: '함수: useLinkStatus'
description: '마지막 업데이트 2026년 2월 20일'
---

# 함수: useLinkStatus | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/functions/use-link-status

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[함수](https://nextjs.org/docs/app/api-reference/functions)useLinkStatus

페이지 복사

# useLinkStatus

마지막 업데이트 2026년 2월 20일

`useLinkStatus` 훅을 사용하면 `<Link>`의 **pending** 상태를 추적할 수 있습니다. 클릭한 링크 위에 쉬머 효과처럼 미묘하고 인라인 피드백을 제공해 내비게이션이 완료될 때까지 사용자에게 상태를 알려 주세요. 즉각적인 전환에는 `loading.js`를 이용한 라우트 수준 폴백과 프리패칭을 우선 고려하세요.

`useLinkStatus`는 다음 상황에서 유용합니다:

  * [프리패칭](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching)이 비활성화되었거나 진행 중이라 내비게이션이 막혀 있을 때
  * 목적지 라우트가 동적이고 [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) 파일이 없어 즉시 내비게이션을 제공하지 못할 때



app/hint.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import Link from 'next/link'
    import { useLinkStatus } from 'next/link'
     
    function Hint() {
      const { pending } = useLinkStatus()
      return (
        <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
      )
    }
     
    export default function Header() {
      return (
        <header>
          <Link href="/dashboard" prefetch={false}>
            <span className="label">Dashboard</span> <Hint />
          </Link>
        </header>
      )
    }
[/code]

> **참고하면 좋아요** :
> 
>   * `useLinkStatus`는 반드시 `Link` 컴포넌트 하위 컴포넌트 안에서 사용해야 합니다
>   * `prefetch={false}`가 `Link` 컴포넌트에 설정된 경우 이 훅이 가장 유용합니다
>   * 연결된 라우트가 이미 프리패치된 경우 pending 상태는 건너뜁니다
>   * 짧은 시간 안에 여러 링크를 클릭하면 마지막 링크의 pending 상태만 표시됩니다
>   * 이 훅은 Pages Router에서는 지원되지 않으며 항상 `{ pending: false }`를 반환합니다
>   * 인라인 지표는 레이아웃 시프트를 유발하기 쉽습니다. 고정 크기로 항상 렌더링되는 힌트 요소를 두고 불투명도만 토글하거나 애니메이션을 사용하세요.
> 


## `useLinkStatus`가 필요하지 않을 수도 있음[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#you-might-not-need-uselinkstatus)

인라인 피드백을 추가하기 전에 다음을 고려하세요:

  * 목적지가 정적이고 프로덕션에서 프리패치되는 경우 pending 단계가 건너뛰어질 수 있습니다.
  * 라우트에 `loading.js` 파일이 있어 라우트 수준 폴백으로 즉시 전환할 수 있습니다.



내비게이션은 보통 빠릅니다. 느린 전환을 발견했을 때 `useLinkStatus`로 재빨리 보완하고, 이후 프리패칭이나 `loading.js` 폴백으로 근본 원인을 해결하세요.

## 매개변수[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#parameters)
[code] 
    const { pending } = useLinkStatus()
[/code]

`useLinkStatus`는 매개변수를 받지 않습니다.

## 반환값[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#returns)

`useLinkStatus`는 단일 속성을 가진 객체를 반환합니다:

속성| 유형| 설명  
---|---|---  
pending| boolean| 기록이 업데이트되기 전에는 `true`, 이후에는 `false`  
  
## 예시[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#example)

### 인라인 링크 힌트[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#inline-link-hint)

프리패칭이 완료되지 않았을 때 클릭을 확인할 수 있도록 레이아웃에 영향을 주지 않는 미묘한 고정 크기 힌트를 추가하세요.

app/components/loading-indicator.tsx

JavaScriptTypeScript
[code]
    'use client'
     
    import { useLinkStatus } from 'next/link'
     
    export default function LoadingIndicator() {
      const { pending } = useLinkStatus()
      return (
        <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
      )
    }
[/code]

app/shop/layout.tsx

JavaScriptTypeScript
[code]
    import Link from 'next/link'
    import LoadingIndicator from './components/loading-indicator'
     
    const links = [
      { href: '/shop/electronics', label: 'Electronics' },
      { href: '/shop/clothing', label: 'Clothing' },
      { href: '/shop/books', label: 'Books' },
    ]
     
    function Menubar() {
      return (
        <div>
          {links.map((link) => (
            <Link key={link.label} href={link.href}>
              <span className="label">{link.label}</span> <LoadingIndicator />
            </Link>
          ))}
        </div>
      )
    }
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <div>
          <Menubar />
          {children}
        </div>
      )
    }
[/code]

## 빠른 내비게이션을 우아하게 처리하기[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#gracefully-handling-fast-navigation)

새 라우트로의 내비게이션이 빠르면 불필요한 힌트 깜박임이 보일 수 있습니다. 사용자 경험을 개선하고 내비게이션 완료에 시간이 걸릴 때만 힌트를 표시하려면 초깃값 애니메이션 지연(예: 100ms)을 추가하고 애니메이션을 투명 상태(예: `opacity: 0`)에서 시작하세요.

app/styles/global.css
[code]
    .link-hint {
      display: inline-block;
      width: 0.6em;
      height: 0.6em;
      margin-left: 0.25rem;
      border-radius: 9999px;
      background: currentColor;
      opacity: 0;
      visibility: hidden; /* reserve space without showing the hint */
    }
     
    .link-hint.is-pending {
      /* Animation 1: fade in after 100ms and keep final opacity */
      /* Animation 2: subtle pulsing while pending */
      visibility: visible;
      animation-name: fadeIn, pulse;
      animation-duration: 200ms, 1s;
      /* Appear only if navigation actually takes time */
      animation-delay: 100ms, 100ms;
      animation-timing-function: ease, ease-in-out;
      animation-iteration-count: 1, infinite;
      animation-fill-mode: forwards, none;
    }
     
    @keyframes fadeIn {
      to {
        opacity: 0.35;
      }
    }
    @keyframes pulse {
      50% {
        opacity: 0.15;
      }
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#version-history)

버전| 변경 사항  
---|---  
`v15.3.0`| `useLinkStatus` 도입.  
  
## 다음 단계

API 레퍼런스를 읽고 이 페이지에서 언급한 기능을 더 알아보세요.

### [Link Component내장된 `next/link` 컴포넌트로 빠른 클라이언트 측 내비게이션을 활성화합니다.](https://nextjs.org/docs/app/api-reference/components/link)### [loading.js`loading.js` 파일에 대한 API 레퍼런스.](https://nextjs.org/docs/app/api-reference/file-conventions/loading)

도움이 되었나요?

지원됨.

보내기
