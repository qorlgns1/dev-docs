---
title: '중요한 기본값'
description: '처음부터 TanStack Query는 공격적이지만 합리적인 기본값으로 구성되어 있습니다. 이 기본값들을 모르면 새 사용자에게 예상치 못한 상황이 생기거나 학습·디버깅이 어려울 수 있습니다. TanStack Query를 계속 학습하고 사용할 때 다음 내용을 염두에 두세요...'
---

# 중요한 기본값

처음부터 TanStack Query는 **공격적이지만 합리적인** 기본값으로 구성되어 있습니다. **이 기본값들을 모르면 새 사용자에게 예상치 못한 상황이 생기거나 학습·디버깅이 어려울 수 있습니다.** TanStack Query를 계속 학습하고 사용할 때 다음 내용을 염두에 두세요:

- `useQuery` 또는 `useInfiniteQuery`로 생성된 쿼리 인스턴스는 기본적으로 **캐시된 데이터를 오래된(stale) 상태**로 간주합니다.

> 이 동작을 바꾸려면 `staleTime` 옵션을 사용해 전역 또는 개별 쿼리 단위로 구성하면 됩니다. 더 긴 `staleTime`을 지정하면 쿼리가 데이터를 자주 다시 가져오지 않습니다.

- `staleTime`이 설정된 쿼리는 해당 `staleTime`이 지날 때까지 **최신(fresh)** 으로 간주됩니다.
  - `staleTime`을 `2 * 60 * 1000`처럼 설정하면 쿼리가 [수동으로 무효화](https://tanstack.com/query/latest/docs/framework/react/guides/query-invalidation.md)되기 전까지 2분 동안 모든 리페치를 유발하지 않고 캐시에서 데이터를 읽어옵니다.
  - `staleTime`을 `Infinity`로 설정하면 쿼리가 [수동으로 무효화](https://tanstack.com/query/latest/docs/framework/react/guides/query-invalidation.md)되기 전까지 리페치를 전혀 트리거하지 않습니다.
  - `staleTime`을 `'static'`으로 설정하면 쿼리가 [수동으로 무효화](https://tanstack.com/query/latest/docs/framework/react/guides/query-invalidation.md)되더라도 **절대** 리페치를 트리거하지 않습니다.

- 오래된 쿼리는 다음 상황에서 백그라운드로 자동 리페치됩니다:
  - 쿼리의 새 인스턴스가 마운트될 때
  - 창이 다시 포커스될 때
  - 네트워크가 재연결될 때

> 과도한 리페치를 피하는 가장 권장되는 방법은 `staleTime`을 설정하는 것이지만, `refetchOnMount`, `refetchOnWindowFocus`, `refetchOnReconnect` 같은 옵션으로 리페치 시점을 맞춤화할 수도 있습니다.

- 쿼리는 선택적으로 `refetchInterval`을 지정해 `staleTime` 설정과 관계없이 주기적으로 리페치를 트리거할 수 있습니다.

- `useQuery`, `useInfiniteQuery` 또는 쿼리 옵저버에 더 이상 활성 인스턴스가 없는 쿼리 결과는 “비활성”으로 표시되며, 나중에 다시 사용될 수 있도록 캐시에 유지됩니다.
- 기본적으로 “비활성” 쿼리는 **5분** 후 가비지 컬렉션됩니다.

  > 이를 변경하려면 기본 `gcTime` 값을 `1000 * 60 * 5` 밀리초가 아닌 다른 값으로 조정하면 됩니다.

- 실패한 쿼리는 UI에 오류를 표시하기 전에 **지수 백오프 지연과 함께 조용히 3번 재시도**됩니다.

  > 이를 변경하려면 기본 `retry`와 `retryDelay` 옵션을 `3`과 기본 지수 백오프 함수 대신 다른 값으로 바꿀 수 있습니다.

- 쿼리 결과는 기본적으로 **데이터가 실제로 변경되었는지 감지하기 위해 구조적 공유**를 사용하며, 변경되지 않았다면 **데이터 참조가 그대로 유지**되어 useMemo와 useCallback과 관련된 값 안정화에 도움이 됩니다. 이 개념이 낯설다면 걱정하지 마세요! 99.9%의 경우 이 기능을 비활성화할 필요가 없으며, 아무 비용 없이 앱 성능을 향상시킵니다.

  > 구조적 공유는 JSON 호환 값에서만 작동하므로, 그 외 타입은 항상 변경된 것으로 간주됩니다. 예를 들어 응답이 매우 커서 성능 문제가 발생한다면 `config.structuralSharing` 플래그로 이 기능을 비활성화할 수 있습니다. JSON 호환이 아닌 값을 다루면서도 데이터 변경 여부를 감지하고 싶다면, `config.structuralSharing`에 사용자 정의 함수를 제공해 이전·새 응답에서 값을 계산하고 필요한 참조를 유지할 수 있습니다.

[//]: # 'Materials'

## 추가 참고 자료

기본값에 대한 추가 설명은 [커뮤니티 리소스](https://tanstack.com/query/latest/docs/community-resources)의 다음 글을 참고하세요:

- [Practical React Query](https://tkdodo.eu/blog/practical-react-query)
- [React Query as a State Manager](https://tkdodo.eu/blog/react-query-as-a-state-manager)
- [Thinking in React Query](https://tkdodo.eu/blog/thinking-in-react-query)

[//]: # 'Materials'

