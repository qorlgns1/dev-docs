---
title: 'broadcastQueryClient (실험적 기능)'
description: '> 매우 중요: 이 유틸리티는 현재 실험 단계입니다. 이는 부 버전과 패치 버전에서도 호환성 파괴 변경 사항이 발생할 수 있음을 의미합니다. 사용은 전적으로 본인 책임입니다. 실험 단계에서 프로덕션에 도입하려면 예기치 않은 깨짐을 피하기 위해 반드시 패치 수준 버전에 ...'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/plugins/broadcastQueryClient

# broadcastQueryClient (실험적 기능)

> 매우 중요: 이 유틸리티는 현재 실험 단계입니다. 이는 부 버전과 패치 버전에서도 호환성 파괴 변경 사항이 발생할 수 있음을 의미합니다. 사용은 전적으로 본인 책임입니다. 실험 단계에서 프로덕션에 도입하려면 예기치 않은 깨짐을 피하기 위해 반드시 패치 수준 버전에 고정해 두세요.

`broadcastQueryClient`는 동일한 오리진의 브라우저 탭/창 사이에서 queryClient 상태를 브로드캐스트하고 동기화하기 위한 유틸리티입니다.

## 설치

이 유틸리티는 별도 패키지로 제공되며 `'@tanstack/query-broadcast-client-experimental'`에서 임포트할 수 있습니다.

## 사용법

`broadcastQueryClient` 함수를 임포트한 뒤 `QueryClient` 인스턴스를 전달하고, 선택적으로 `broadcastChannel`을 설정합니다.

```tsx
import { broadcastQueryClient } from '@tanstack/query-broadcast-client-experimental'

const queryClient = new QueryClient()

broadcastQueryClient({
  queryClient,
  broadcastChannel: 'my-app',
})
```

## API

### `broadcastQueryClient`

이 함수에 `QueryClient` 인스턴스를 전달하고, 필요하다면 `broadcastChannel`을 추가로 전달합니다.

```tsx
broadcastQueryClient({ queryClient, broadcastChannel })
```

### `Options`

옵션 객체입니다.

```tsx
interface BroadcastQueryClientOptions {
  /** The QueryClient to sync */
  queryClient: QueryClient
  /** This is the unique channel name that will be used
   * to communicate between tabs and windows */
  broadcastChannel?: string
  /** Options for the BroadcastChannel API */
  options?: BroadcastChannelOptions
}
```

기본 옵션은 다음과 같습니다.

```tsx
{
  broadcastChannel = 'tanstack-query',
}
```

