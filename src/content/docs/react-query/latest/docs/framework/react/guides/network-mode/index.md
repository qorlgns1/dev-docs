---
title: '네트워크 모드'
description: 'TanStack Query는 네트워크 연결이 없을 때 Queries와 Mutations이 어떻게 동작해야 하는지를 구분하기 위해 세 가지 네트워크 모드를 제공합니다. 이 모드는 각 Query / Mutation별로 개별 설정하거나, 전역 query / mutation ...'
---

# 네트워크 모드

TanStack Query는 네트워크 연결이 없을 때 [Queries](https://tanstack.com/query/latest/docs/framework/react/guides/queries.md)와 [Mutations](https://tanstack.com/query/latest/docs/framework/react/guides/mutations.md)이 어떻게 동작해야 하는지를 구분하기 위해 세 가지 네트워크 모드를 제공합니다. 이 모드는 각 Query / Mutation별로 개별 설정하거나, 전역 query / mutation 기본값으로 설정할 수 있습니다.

TanStack Query는 데이터를 가져오는 라이브러리와 함께 데이터 패칭에 가장 많이 사용되므로 기본 네트워크 모드는 [online](#network-mode-online)입니다.

## Network Mode: online

이 모드에서는 네트워크 연결이 없으면 Queries와 Mutations가 실행되지 않습니다. 기본 모드입니다. 쿼리에 대한 fetch가 시작되면 네트워크 연결이 없어 fetch를 진행할 수 없더라도 해당 쿼리는 현재 `state`(`pending`, `error`, `success`)를 유지합니다. 대신 [fetchStatus](https://tanstack.com/query/latest/docs/framework/react/guides/queries.md#fetchstatus)가 추가로 노출되며, 값은 다음 중 하나입니다.

- `fetching`: `queryFn`이 실제로 실행 중이며 요청이 진행 중입니다.
- `paused`: 쿼리가 실행되지 않으며 연결이 복구될 때까지 `paused` 상태입니다.
- `idle`: 쿼리가 fetching 중도 아니고 paused 상태도 아닙니다.

`isFetching`과 `isPaused` 플래그는 이 상태에서 파생되어 편의상 노출됩니다.

> 로딩 스피너를 표시하기 위해 `pending` 상태만 확인하는 것은 충분하지 않을 수 있습니다. 첫 마운트 시 네트워크 연결이 없으면 Query가 `state: 'pending'`이면서 `fetchStatus: 'paused'` 일 수 있습니다.

온라인 상태에서 쿼리가 실행 중일 때 fetch가 진행되는 도중 오프라인이 되면 TanStack Query는 재시도 메커니즘도 일시 중지합니다. 일시 중지된 쿼리는 네트워크 연결이 다시 활성화되면 실행을 이어갑니다. 이는 `refetchOnReconnect`(이 모드에서 기본값이 `true`)와는 독립적이며, 재요청이 아니라 “계속 실행”이기 때문입니다. 그 사이에 쿼리가 [cancelled](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md) 상태가 되었다면 이어서 실행되지 않습니다.

## Network Mode: always

이 모드에서는 TanStack Query가 항상 fetch를 수행하며 온라인 / 오프라인 상태를 무시합니다. Queries가 동작하는 데 활성 네트워크 연결이 필요 없는 환경(예: `AsyncStorage`에서 읽기만 하거나 `queryFn`에서 `Promise.resolve(5)`를 반환하는 경우 등)에서 사용하기 적합한 모드입니다.

- 네트워크 연결이 없어도 Queries는 `paused` 상태가 되지 않습니다.
- 재시도도 일시 중지되지 않으며 실패하면 Query는 `error` 상태로 전환됩니다.
- `refetchOnReconnect` 기본값은 `false`입니다. 네트워크 재연결이 더 이상 staled 쿼리를 리패치해야 한다는 좋은 신호가 아니기 때문입니다. 필요하다면 수동으로 활성화할 수 있습니다.

## Network Mode: offlineFirst

이 모드는 앞선 두 옵션의 중간 지점으로, TanStack Query가 `queryFn`을 한 번 실행한 뒤 재시도를 일시 중지합니다. 서비스 워커가 [offline-first PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Offline_Service_workers)처럼 요청을 가로채 캐싱하는 경우나, [Cache-Control 헤더](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching#the_cache-control_header)를 사용한 HTTP 캐싱을 활용하는 경우 매우 유용합니다.

이러한 상황에서는 첫 fetch가 오프라인 저장소 / 캐시에서 제공되므로 성공할 수 있습니다. 그러나 캐시 미스가 발생하면 네트워크 요청이 나가고 실패하며, 이때는 `online` 쿼리처럼 작동해 재시도가 일시 중지됩니다.

## Devtools

[TanStack Query Devtools](https://tanstack.com/query/latest/docs/framework/react/devtools.md)는 fetch를 해야 하지만 네트워크 연결이 없어 실행되지 못하는 Queries를 `paused` 상태로 표시합니다. 또한 _Mock offline behavior_ 토글 버튼이 있습니다. 이 버튼은 실제 네트워크 연결을 변경하지 않고(브라우저 devtools에서 조작 가능), [OnlineManager](https://tanstack.com/query/latest/docs/reference/onlineManager.md)를 오프라인 상태로 설정합니다.

## Signature

- `networkMode: 'online' | 'always' | 'offlineFirst'`
  - 선택 사항
  - 기본값은 `'online'`

