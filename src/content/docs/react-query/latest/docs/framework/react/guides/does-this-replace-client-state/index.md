---
title: 'TanStack Query가 Redux, MobX 또는 기타 전역 상태 관리자를 대체하나요?'
description: '먼저 몇 가지 중요한 사항부터 짚어봅시다:'
---

# TanStack Query가 Redux, MobX 또는 기타 전역 상태 관리자를 대체하나요?

먼저 몇 가지 중요한 사항부터 짚어봅시다:

- TanStack Query는 서버와 클라이언트 간의 비동기 작업을 관리하는 **서버 상태** 라이브러리입니다.
- Redux, MobX, Zustand 등은 **클라이언트 상태** 라이브러리이며, TanStack Query 같은 도구와 비교했을 때 비효율적이긴 하지만 비동기 데이터를 저장하는 데 _사용될 수는 있습니다._

이 점들을 염두에 두면, TanStack Query는 **클라이언트 상태에서 캐시 데이터를 관리하던 보일러플레이트 코드와 연결 작업을 제거하고, 이를 단 몇 줄의 코드로 대체한다**는 것이 짧은 답입니다.

대다수 애플리케이션에서는 비동기 코드를 모두 TanStack Query로 옮긴 뒤에 남는 **전역적으로 접근 가능한 클라이언트 상태**가 매우 적은 편입니다.

> 다만 시각적 디자이너나 음악 제작 애플리케이션처럼, 애플리케이션이 클라이언트 전용 동기 상태를 대량으로 갖는 상황도 있습니다. 이런 경우에는 여전히 클라이언트 상태 관리자가 필요할 수 있습니다. 이때 중요한 점은 **TanStack Query가 로컬/클라이언트 상태 관리를 대체하는 도구가 아니라는 것**입니다. 그러나 TanStack Query는 대부분의 클라이언트 상태 관리자와 문제 없이 함께 사용할 수 있습니다.

## 인위적인 예시

다음은 전역 상태 라이브러리로 관리되고 있는 “전역” 상태입니다:

```tsx
const globalState = {
  projects,
  teams,
  tasks,
  users,
  themeMode,
  sidebarStatus,
}
```

현재 전역 상태 관리자는 `projects`, `teams`, `tasks`, `users`라는 네 가지 유형의 서버 상태를 캐싱하고 있습니다. 이 서버 상태들을 TanStack Query로 옮긴다면 남는 전역 상태는 다음과 비슷해집니다:

```tsx
const globalState = {
  themeMode,
  sidebarStatus,
}
```

이는 또한 몇 번의 `useQuery`, `useMutation` 훅 호출로, 서버 상태를 관리하던 모든 보일러플레이트 코드를 제거할 수 있다는 뜻이기도 합니다. 예를 들면:

- Connectors
- Action Creators
- Middlewares
- Reducers
- Loading/Error/Result 상태
- Contexts

이 모든 것을 제거한 뒤에는, **“이렇게 작은 전역 상태를 위해 클라이언트 상태 관리자를 계속 써야 할까?”**라는 질문이 들 수 있습니다.

**그건 전적으로 여러분의 선택입니다!**

하지만 TanStack Query의 역할은 분명합니다. 애플리케이션에서 비동기 연결과 보일러플레이트를 걷어내고, 이를 단 몇 줄의 코드로 대체합니다.

무엇을 기다리시나요? 지금 바로 시도해 보세요!

