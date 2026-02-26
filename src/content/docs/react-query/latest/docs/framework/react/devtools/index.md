---
title: 'Devtools'
description: 'React Query에는 전용 Devtools가 함께 제공되니 신나게 손을 흔들어 봅시다! 🥳'
---

# Devtools

React Query에는 전용 Devtools가 함께 제공되니 신나게 손을 흔들어 봅시다! 🥳

React Query 여정을 시작할 때 이 Devtools를 곁에 두면 내부 동작을 시각화하고 난관에 부딪혔을 때 디버깅 시간을 아껴 줄 거예요!

> Chrome, Firefox, Edge 사용자라면 브라우저 DevTools에서 TanStack Query를 직접 디버깅할 수 있는 서드파티 브라우저 확장 프로그램을 사용할 수 있습니다. 프레임워크 전용 Devtools 패키지와 동일한 기능을 제공합니다.
>
> - <img alt="Chrome logo" src="https://www.google.com/chrome/static/images/chrome-logo.svg" width="16" height="16" class="inline mr-1 not-prose" /> [Chrome용 Devtools](https://chromewebstore.google.com/detail/tanstack-query-devtools/annajfchloimdhceglpgglpeepfghfai)
> - <img alt="Firefox logo" src="https://upload.wikimedia.org/wikipedia/commons/a/a0/Firefox_logo%2C_2019.svg" width="16" height="16" class="inline mr-1 not-prose" /> [Firefox용 Devtools](https://addons.mozilla.org/en-US/firefox/addon/tanstack-query-devtools/)
> - <img alt="Edge logo" src="https://upload.wikimedia.org/wikipedia/commons/9/98/Microsoft_Edge_logo_%282019%29.svg" width="16" height="16" class="inline mr-1 not-prose" /> [Edge용 Devtools](https://microsoftedge.microsoft.com/addons/detail/tanstack-query-devtools/edmdpkgkacmjopodhfolmphdenmddobj)

> React Native 사용자라면 모든 JS 기반 애플리케이션에서 React Query를 디버깅할 수 있는 서드파티 macOS 네이티브 앱을 사용할 수 있습니다. 여러 기기의 쿼리를 실시간으로 모니터링하세요. 자세히 보기: [rn-better-dev-tools](https://github.com/LovesWorking/rn-better-dev-tools)

> 버전 5부터 Devtools는 뮤테이션 관찰도 지원합니다.

## Devtools 설치 및 임포트

Devtools는 별도 패키지이므로 설치해야 합니다.

```bash
npm i @tanstack/react-query-devtools
```

또는

```bash
pnpm add @tanstack/react-query-devtools
```

또는

```bash
yarn add @tanstack/react-query-devtools
```

또는

```bash
bun add @tanstack/react-query-devtools
```

Next 13+ App Dir에서는 dev dependency로 설치해야 작동합니다.

Devtools는 다음과 같이 임포트할 수 있습니다.

```tsx
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
```

기본적으로 React Query Devtools는 `process.env.NODE_ENV === 'development'`일 때만 번들에 포함되므로 프로덕션 빌드에서 제외할 걱정을 할 필요가 없습니다.

## 플로팅 모드

플로팅 모드는 Devtools를 앱 안의 고정된 플로팅 요소로 마운트하고 화면 모서리에 Devtools 표시/숨김 토글을 제공합니다. 토글 상태는 localStorage에 저장되어 새로고침 후에도 유지됩니다.

아래 코드를 React 앱에서 가능한 한 높은 위치에 배치하세요. 페이지 루트에 가까울수록 더 안정적으로 동작합니다!

```tsx
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      {/* The rest of your application */}
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  )
}
```

### 옵션

- `initialIsOpen: boolean`
  - Devtools를 기본적으로 열어 두고 싶다면 `true`로 설정
- `buttonPosition?: "top-left" | "top-right" | "bottom-left" | "bottom-right" | "relative"`
  - 기본값: `bottom-right`
  - Devtools 패널을 열고 닫는 React Query 로고의 위치
  - `relative`이면 Devtools를 렌더링하는 위치에 버튼이 배치됩니다.
- `position?: "top" | "bottom" | "left" | "right"`
  - 기본값: `bottom`
  - React Query Devtools 패널의 위치
- `client?: QueryClient`
  - 커스텀 QueryClient를 사용하려면 지정합니다. 없으면 가장 가까운 컨텍스트의 인스턴스를 사용합니다.
- `errorTypes?: { name: string; initializer: (query: Query) => TError}[]`
  - UI에서 토글할 수 있는 오류를 미리 정의합니다. 특정 오류가 켜질 때 해당 쿼리를 인자로 initializer가 호출되며 Error를 반환해야 합니다.
- `styleNonce?: string`
  - 문서 head에 추가되는 style 태그에 nonce를 전달합니다. CSP nonce로 인라인 스타일을 허용할 때 유용합니다.
- `shadowDOMTarget?: ShadowRoot`
  - 기본 동작은 DOM의 head 태그에 Devtools 스타일을 적용합니다.
  - Shadow DOM 내부에 스타일을 적용하려면 Devtools에 ShadowRoot 대상을 전달하세요.

## 임베디드 모드

임베디드 모드는 Devtools를 애플리케이션 안의 고정 요소로 표시하여 자체 개발 도구 환경에서 패널을 활용할 수 있게 합니다.

아래 코드를 React 앱에서 가능한 한 높은 위치에 배치하세요. 페이지 루트에 가까울수록 더 잘 동작합니다!

```tsx
import { ReactQueryDevtoolsPanel } from '@tanstack/react-query-devtools'

function App() {
  const [isOpen, setIsOpen] = React.useState(false)

  return (
    <QueryClientProvider client={queryClient}>
      {/* The rest of your application */}
      <button
        onClick={() => setIsOpen(!isOpen)}
      >{`${isOpen ? 'Close' : 'Open'} the devtools panel`}</button>
      {isOpen && <ReactQueryDevtoolsPanel onClose={() => setIsOpen(false)} />}
    </QueryClientProvider>
  )
}
```

### 옵션

- `style?: React.CSSProperties`
  - Devtools 패널에 적용할 커스텀 스타일
  - 기본값: `{ height: '500px' }`
  - 예시: `{ height: '100%' }`
  - 예시: `{ height: '100%', width: '100%' }`
- `onClose?: () => unknown`
  - Devtools 패널이 닫힐 때 호출되는 콜백
- `client?: QueryClient`
  - 커스텀 QueryClient를 사용하려면 지정합니다. 없으면 가장 가까운 컨텍스트의 인스턴스를 사용합니다.
- `errorTypes?: { name: string; initializer: (query: Query) => TError}[]`
  - UI에서 토글할 수 있는 오류를 미리 정의합니다. 특정 오류가 켜질 때 해당 쿼리를 인자로 initializer가 호출되며 Error를 반환해야 합니다.
- `styleNonce?: string`
  - 문서 head에 추가되는 style 태그에 nonce를 전달합니다. CSP nonce로 인라인 스타일을 허용할 때 유용합니다.
- `shadowDOMTarget?: ShadowRoot`
  - 기본 동작은 DOM의 head 태그에 Devtools 스타일을 적용합니다.
  - Shadow DOM 내부에 스타일을 적용하려면 Devtools에 ShadowRoot 대상을 전달하세요.

## 프로덕션에서의 Devtools

Devtools는 프로덕션 빌드에서 제외됩니다. 다만 프로덕션 환경에서도 지연 로딩하여 사용할 수 있습니다.

```tsx
import * as React from 'react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import { Example } from './Example'

const queryClient = new QueryClient()

const ReactQueryDevtoolsProduction = React.lazy(() =>
  import('@tanstack/react-query-devtools/build/modern/production.js').then(
    (d) => ({
      default: d.ReactQueryDevtools,
    }),
  ),
)

function App() {
  const [showDevtools, setShowDevtools] = React.useState(false)

  React.useEffect(() => {
    // @ts-expect-error
    window.toggleDevtools = () => setShowDevtools((old) => !old)
  }, [])

  return (
    <QueryClientProvider client={queryClient}>
      <Example />
      <ReactQueryDevtools initialIsOpen />
      {showDevtools && (
        <React.Suspense fallback={null}>
          <ReactQueryDevtoolsProduction />
        </React.Suspense>
      )}
    </QueryClientProvider>
  )
}

export default App
```

이렇게 설정하면 `window.toggleDevtools()`를 호출할 때 Devtools 번들이 다운로드되고 표시됩니다.

### 최신 번들러

번들러가 package exports를 지원한다면 다음 임포트 경로를 사용할 수 있습니다.

```tsx
const ReactQueryDevtoolsProduction = React.lazy(() =>
  import('@tanstack/react-query-devtools/production').then((d) => ({
    default: d.ReactQueryDevtools,
  })),
)
```

TypeScript를 사용할 경우 tsconfig에서 `moduleResolution: 'nodenext'`를 설정해야 하며, 최소 TypeScript v4.7이 필요합니다.

