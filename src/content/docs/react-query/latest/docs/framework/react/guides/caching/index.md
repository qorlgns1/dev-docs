---
title: '캐싱 예시'
description: '> 이 가이드를 읽기 전에 반드시 Important Defaults를 꼼꼼히 읽어 주세요.'
---

# 캐싱 예시

> 이 가이드를 읽기 전에 반드시 [Important Defaults](https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults.md)를 꼼꼼히 읽어 주세요.

## 기본 예시

이 캐싱 예시는 다음과 같은 이야기와 라이프사이클을 보여 줍니다.

- 캐시 데이터가 있는/없는 쿼리 인스턴스
- 백그라운드 리패칭
- 비활성 쿼리
- 가비지 컬렉션

기본 `gcTime`이 **5분**, 기본 `staleTime`이 `0`이라고 가정합니다.

- `useQuery({ queryKey: ['todos'], queryFn: fetchTodos })`의 새 인스턴스가 마운트됩니다.
  - `['todos']` 쿼리 키로 실행된 다른 쿼리가 없으므로, 이 쿼리는 하드 로딩 상태를 표시하고 데이터를 가져오기 위한 네트워크 요청을 보냅니다.
  - 네트워크 요청이 완료되면 반환된 데이터는 `['todos']` 키 아래에 캐싱됩니다.
  - 구성된 `staleTime`(기본값 `0`, 즉 즉시)이 지나면 훅은 데이터를 오래된 상태로 표시합니다.
- 다른 곳에서 `useQuery({ queryKey: ['todos'], queryFn: fetchTodos })`의 두 번째 인스턴스가 마운트됩니다.
  - 첫 번째 쿼리에서 `['todos']` 키에 대한 데이터가 이미 캐시에 있으므로, 해당 데이터는 즉시 캐시에서 반환됩니다.
  - 새 인스턴스는 자신의 쿼리 함수를 사용해 새로운 네트워크 요청을 트리거합니다.
    - 두 `fetchTodos` 쿼리 함수가 동일하든 아니든, 동일한 쿼리 키를 사용하기 때문에 두 쿼리의 [`status`](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)(`isFetching`, `isPending`, 기타 관련 값 포함)가 모두 업데이트됩니다.
  - 요청이 성공적으로 완료되면 캐시의 `['todos']` 키 아래 데이터가 새 데이터로 업데이트되고, 두 인스턴스 모두 새 데이터로 갱신됩니다.
- `useQuery({ queryKey: ['todos'], queryFn: fetchTodos })` 쿼리의 두 인스턴스가 모두 언마운트되어 더 이상 사용되지 않습니다.
  - 이 쿼리의 활성 인스턴스가 없으므로, `gcTime`을 사용해 쿼리를 삭제하고 가비지 컬렉션하기 위한 타임아웃이 설정됩니다(기본값 **5분**).
- 캐시 타임아웃(`gcTime`)이 완료되기 전에 또 다른 `useQuery({ queryKey: ['todos'], queryFn: fetchTodos })` 인스턴스가 마운트됩니다. 쿼리는 `fetchTodos` 함수가 백그라운드에서 실행되는 동안 즉시 사용 가능한 캐시 데이터를 반환합니다. 성공적으로 완료되면 최신 데이터로 캐시를 채웁니다.
- 마지막 `useQuery({ queryKey: ['todos'], queryFn: fetchTodos })` 인스턴스가 언마운트됩니다.
- **5분** 이내에 `useQuery({ queryKey: ['todos'], queryFn: fetchTodos })`의 다른 인스턴스가 나타나지 않습니다.
  - `['todos']` 키 아래 캐시된 데이터가 삭제되고 가비지 컬렉션됩니다.

