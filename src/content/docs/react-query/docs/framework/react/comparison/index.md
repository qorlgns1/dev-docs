---
title: '비교 | React Query vs SWR vs Apollo vs RTK Query vs React Router'
description: '> 이 비교 표는 가능한 한 정확하고 편향 없이 작성되었습니다. 위 라이브러리들을 사용 중이고 정보 개선이 필요하다고 느끼면, 근거 자료와 함께 이 페이지 하단의 "Edit this page on Github" 링크를 통해 변경 사항을 제안해 주세요.'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/comparison

# 비교 | React Query vs SWR vs Apollo vs RTK Query vs React Router

> 이 비교 표는 가능한 한 정확하고 편향 없이 작성되었습니다. 위 라이브러리들을 사용 중이고 정보 개선이 필요하다고 느끼면, 근거 자료와 함께 이 페이지 하단의 "Edit this page on Github" 링크를 통해 변경 사항을 제안해 주세요.

기능/역량 키:

- ✅ 추가 설정이나 코드 없이 즉시 사용할 수 있는 1급 내장 기능
- 🟡 비공식 서드파티 또는 커뮤니티 라이브러리/기여 형태로 지원
- 🔶 문서화되어 있으나 구현을 위해 추가 사용자 코드가 필요한 기능
- 🛑 공식적으로 지원되거나 문서화되지 않은 기능

|                                                    | React Query                              | SWR [_(Website)_][swr]                   | Apollo Client [_(Website)_][apollo]        | RTK-Query [_(Website)_][rtk-query]   | React Router [_(Website)_][react-router]                                  |
| -------------------------------------------------- | ---------------------------------------- | ---------------------------------------- | ------------------------------------------ | ------------------------------------ | ------------------------------------------------------------------------- |
| Github Repo / Stars                                | [![][stars-react-query]][gh-react-query] | [![][stars-swr]][gh-swr]                 | [![][stars-apollo]][gh-apollo]             | [![][stars-rtk-query]][gh-rtk-query] | [![][stars-react-router]][gh-react-router]                                |
| 플랫폼 요구사항                                   | React                                    | React                                    | React, GraphQL                             | Redux                                | React                                                                     |
| 자체 비교 자료                                    |                                          | (없음)                                   | (없음)                                     | [Comparison][rtk-query-comparison]   | (없음)                                                                    |
| 지원 쿼리 구문                                    | Promise, REST, GraphQL                   | Promise, REST, GraphQL                   | GraphQL, Any (Reactive Variables)          | Promise, REST, GraphQL               | Promise, REST, GraphQL                                                    |
| 지원 프레임워크                                   | React                                    | React                                    | React + Others                             | Any                                  | React                                                                     |
| 캐시 전략                                         | Hierarchical Key -> Value                | Unique Key -> Value                      | Normalized Schema                          | Unique Key -> Value                  | Nested Route -> value                                                     |
| 캐시 키 전략                                      | JSON                                     | JSON                                     | GraphQL Query                              | JSON                                 | Route Path                                                                |
| 캐시 변경 감지                                    | Deep Compare Keys (Stable Serialization) | Deep Compare Keys (Stable Serialization) | Deep Compare Keys (Unstable Serialization) | Key Referential Equality (===)       | Route Change                                                              |
| 데이터 변경 감지                                  | Deep Comparison + Structural Sharing     | Deep Compare (via `stable-hash`)         | Deep Compare (Unstable Serialization)      | Key Referential Equality (===)       | Loader Run                                                                |
| 데이터 메모이제이션                               | Full Structural Sharing                  | Identity (===)                           | Normalized Identity                        | Identity (===)                       | Identity (===)                                                            |
| 번들 크기                                         | [![][bp-react-query]][bpl-react-query]   | [![][bp-swr]][bpl-swr]                   | [![][bp-apollo]][bpl-apollo]               | [![][bp-rtk-query]][bpl-rtk-query]   | [![][bp-react-router]][bpl-react-router] + [![][bp-history]][bpl-history] |
| API 정의 위치                                     | Component, External Config               | Component                                | GraphQL Schema                             | External Config                      | Route Tree Configuration                                                  |
| Queries                                            | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Cache Persistence                                  | ✅                                       | ✅                                       | ✅                                         | ✅                                   | 🛑 활성 라우트만 <sup>8</sup>                                             |
| Devtools                                           | ✅                                       | ✅                                       | ✅                                         | ✅                                   | 🛑                                                                        |
| Polling/Intervals                                  | ✅                                       | ✅                                       | ✅                                         | ✅                                   | 🛑                                                                        |
| Parallel Queries                                   | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Dependent Queries                                  | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Paginated Queries                                  | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Infinite Queries                                   | ✅                                       | ✅                                       | ✅                                         | ✅                                   | 🛑                                                                        |
| Bi-directional Infinite Queries                    | ✅                                       | 🔶                                       | 🔶                                         | ✅                                   | 🛑                                                                        |
| Infinite Query Refetching                          | ✅                                       | ✅                                       | 🛑                                         | ✅                                   | 🛑                                                                        |
| Lagged Query Data<sup>1</sup>                      | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Selectors                                          | ✅                                       | 🛑                                       | ✅                                         | ✅                                   | N/A                                                                       |
| Initial Data                                       | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Scroll Recovery                                    | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Cache Manipulation                                 | ✅                                       | ✅                                       | ✅                                         | ✅                                   | 🛑                                                                        |
| Outdated Query Dismissal                           | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Render Batching & Optimization<sup>2</sup>         | ✅                                       | ✅                                       | 🛑                                         | ✅                                   | ✅                                                                        |
| Auto Garbage Collection                            | ✅                                       | 🛑                                       | 🛑                                         | ✅                                   | N/A                                                                       |
| Mutation Hooks                                     | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Offline Mutation Support                           | ✅                                       | 🛑                                       | 🟡                                         | 🛑                                   | 🛑                                                                        |
| Prefetching APIs                                   | ✅                                       | ✅                                       | ✅                                         | ✅                                   | ✅                                                                        |
| Query Cancellation                                 | ✅                                       | 🛑                                       | 🛑                                         | 🛑                                   | ✅                                                                        |
| Partial Query Matching<sup>3</sup>                 | ✅                                       | 🔶                                       | ✅                                         | ✅                                   | N/A                                                                       |

| Stale While Revalidate(재검증 중 만료 캐시 유지) | ✅                                       | ✅                                       | ✅                                         | ✅                                   | 🛑                                                                        |
| Stale Time 구성                                   | ✅                                       | 🛑<sup>7</sup>                           | 🛑                                         | ✅                                   | 🛑                                                                        |
| 사전 사용 쿼리/뮤테이션 구성<sup>4</sup>          | ✅                                       | 🛑                                       | ✅                                         | ✅                                   | ✅                                                                        |
| 창 포커스 재요청                                  | ✅                                       | ✅                                       | 🛑                                         | ✅                                   | 🛑                                                                        |
| 네트워크 상태 재요청                              | ✅                                       | ✅                                       | ✅                                         | ✅                                   | 🛑                                                                        |
| 일반 캐시 탈수/재수화                             | ✅                                       | 🛑                                       | ✅                                         | ✅                                   | ✅                                                                        |
| 오프라인 캐싱                                    | ✅                                       | 🛑                                       | ✅                                         | 🔶                                   | 🛑                                                                        |
| React Suspense                                   | ✅                                       | ✅                                       | ✅                                         | 🛑                                   | ✅                                                                        |
| 추상화/비종속 코어                                | ✅                                       | 🛑                                       | ✅                                         | ✅                                   | 🛑                                                                        |
| 뮤테이션 후 자동 재요청<sup>5</sup>              | 🔶                                       | 🔶                                       | ✅                                         | ✅                                   | ✅                                                                        |
| 정규화 캐싱<sup>6</sup>                           | 🛑                                       | 🛑                                       | ✅                                         | 🛑                                   | 🛑                                                                        |

### Notes

> **<sup>1</sup> 지연된 쿼리 데이터** - React Query는 다음 쿼리가 로드되는 동안 기존 쿼리의 데이터를 계속 볼 수 있는 방법을 제공하며, 이는 곧 Suspense가 기본적으로 제공할 동일한 UX와 유사합니다. 새로운 쿼리가 요청될 때마다 하드 로딩 상태를 표시하고 싶지 않은 페이지네이션 UI나 무한 로딩 UI를 작성할 때 매우 중요합니다. 다른 라이브러리는 이러한 기능이 없어 새로운 쿼리가 로드되는 동안(사전 패칭되지 않았다면) 새 쿼리에 대해 하드 로딩 상태를 렌더링합니다.

> **<sup>2</sup> 렌더링 최적화** - React Query는 뛰어난 렌더링 성능을 제공합니다. 기본적으로 접근된 필드를 자동으로 추적하고 그중 하나가 변경될 때만 다시 렌더링합니다. 이 최적화를 옵트아웃하고 싶다면 `notifyOnChangeProps`를 `'all'`로 설정해 쿼리가 업데이트될 때마다 컴포넌트를 다시 렌더링하도록 할 수 있습니다. 예를 들어 새 데이터가 있거나 패칭 중임을 표시하기 위함입니다. 또한 React Query는 동일한 쿼리를 사용하는 여러 컴포넌트가 있을 때 애플리케이션이 한 번만 다시 렌더링되도록 업데이트를 배치합니다. `data`나 `error` 속성만 관심이 있다면 `notifyOnChangeProps`를 `['data', 'error']`로 설정해 렌더 횟수를 더 줄일 수 있습니다.

> **<sup>3</sup> 부분 쿼리 매칭** - React Query는 결정적 쿼리 키 직렬화를 사용하기 때문에, 일치시키고 싶은 각 쿼리 키를 알 필요 없이 다양한 쿼리 그룹을 조작할 수 있습니다. 예를 들어 변수와 관계없이 키가 `todos`로 시작하는 모든 쿼리를 재요청하거나, 변수 또는 중첩 속성 유무에 따라 특정 쿼리를 타겟팅하고, 특정 조건을 통과하는 쿼리만 매칭하도록 필터 함수를 사용할 수도 있습니다.

> **<sup>4</sup> 사전 사용 쿼리 구성** - 이는 단지 쿼리와 뮤테이션이 사용되기 전에 어떻게 동작할지 구성할 수 있다는 의미를 멋지게 표현한 것입니다. 예를 들어 쿼리를 미리 기본값으로 완전히 구성해두면 사용할 때 `useQuery({ queryKey })`만 호출하면 되고, 매번 페처나 옵션을 전달할 필요가 없습니다. SWR도 기본 페처를 사전 구성하여 이 기능의 일부를 제공하지만 전역 페처만 허용하며 쿼리별로는 불가능하고 뮤테이션에는 전혀 적용되지 않습니다.

> **<sup>5</sup> 뮤테이션 후 자동 재요청** - 뮤테이션 후 진정한 자동 재요청이 일어나려면, 라이브러리가 개별 엔티티와 스키마 내 엔티티 타입을 식별하는 방법을 아는 데 도움을 주는 휴리스틱과 함께 GraphQL이 제공하는 것 같은 스키마가 필요합니다.

> **<sup>6</sup> 정규화 캐싱** - React Query, SWR, RTK-Query는 현재 엔티티를 평면 구조로 저장해 상위 수준의 데이터 중복을 피하는 자동 정규화 캐싱을 지원하지 않습니다.

> **<sup>7</sup> SWR의 Immutable 모드** - SWR에는 캐시 수명 동안 쿼리를 한 번만 페치하도록 해주는 "immutable" 모드가 있지만, 여전히 stale-time 개념이나 조건부 자동 재검증을 지원하지 않습니다.

> **<sup>8</sup> React Router 캐시 지속성** - React Router는 현재 매치된 라우트를 넘어 데이터를 캐시하지 않습니다. 라우트를 벗어나면 해당 데이터는 사라집니다.

[bpl-react-query]: https://bundlephobia.com/result?p=@tanstack/react-query
[bp-react-query]: https://badgen.net/bundlephobia/minzip/@tanstack/react-query?label=💾
[gh-react-query]: https://github.com/tannerlinsley/react-query
[stars-react-query]: https://img.shields.io/github/stars/tannerlinsley/react-query?label=%F0%9F%8C%9F
[swr]: https://github.com/vercel/swr
[bp-swr]: https://badgen.net/bundlephobia/minzip/swr?label=💾
[gh-swr]: https://github.com/vercel/swr
[stars-swr]: https://img.shields.io/github/stars/vercel/swr?label=%F0%9F%8C%9F
[bpl-swr]: https://bundlephobia.com/result?p=swr
[apollo]: https://github.com/apollographql/apollo-client
[bp-apollo]: https://badgen.net/bundlephobia/minzip/@apollo/client?label=💾
[gh-apollo]: https://github.com/apollographql/apollo-client
[stars-apollo]: https://img.shields.io/github/stars/apollographql/apollo-client?label=%F0%9F%8C%9F
[bpl-apollo]: https://bundlephobia.com/result?p=@apollo/client
[rtk-query]: https://redux-toolkit.js.org/rtk-query/overview
[rtk-query-comparison]: https://redux-toolkit.js.org/rtk-query/comparison
[rtk-query-bundle-size]: https://redux-toolkit.js.org/rtk-query/comparison#bundle-size
[bp-rtk]: https://badgen.net/bundlephobia/minzip/@reduxjs/toolkit?label=💾
[bp-rtk-query]: https://badgen.net/bundlephobia/minzip/@reduxjs/toolkit?label=💾
[gh-rtk-query]: https://github.com/reduxjs/redux-toolkit
[stars-rtk-query]: https://img.shields.io/github/stars/reduxjs/redux-toolkit?label=🌟
[bpl-rtk]: https://bundlephobia.com/result?p=@reduxjs/toolkit
[bpl-rtk-query]: https://bundlephobia.com/package/@reduxjs/toolkit
[react-router]: https://github.com/remix-run/react-router
[bp-react-router]: https://badgen.net/bundlephobia/minzip/react-router-dom?label=💾
[gh-react-router]: https://github.com/remix-run/react-router
[stars-react-router]: https://img.shields.io/github/stars/remix-run/react-router?label=%F0%9F%8C%9F
[bpl-react-router]: https://bundlephobia.com/result?p=react-router-dom
[bp-history]: https://badgen.net/bundlephobia/minzip/history?label=💾
[bpl-history]: https://bundlephobia.com/result?p=history

