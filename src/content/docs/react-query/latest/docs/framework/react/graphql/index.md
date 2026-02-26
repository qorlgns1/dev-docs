---
title: 'GraphQL'
description: 'React Query의 데이터 페칭 메커니즘은 프로미스를 기반으로 프레임워크에 구애받지 않도록 설계되었기 때문에, GraphQL을 포함한 어떤 비동기 데이터 페칭 클라이언트와도 React Query를 함께 사용할 수 있습니다!'
---

# GraphQL

React Query의 데이터 페칭 메커니즘은 프로미스를 기반으로 프레임워크에 구애받지 않도록 설계되었기 때문에, GraphQL을 포함한 어떤 비동기 데이터 페칭 클라이언트와도 React Query를 함께 사용할 수 있습니다!

> React Query는 정규화된 캐싱을 지원하지 않는다는 점을 기억하세요. 대부분의 사용자는 실제로 정규화된 캐시를 필요로 하지 않거나 생각만큼 큰 이점을 얻지 못하지만, 아주 드물게 필요한 상황이 있을 수 있으니 정말 필요한지 먼저 저희에게 확인해 주세요!

[//]: # 'Codegen'

## 타입 안전성과 코드 생성

React Query를 `graphql-request^5` 및 [GraphQL Code Generator](https://graphql-code-generator.com/)와 함께 사용하면 완전한 타입의 GraphQL 연산을 제공할 수 있습니다:

```tsx
import request from 'graphql-request'
import { useQuery } from '@tanstack/react-query'

import { graphql } from './gql/gql'

const allFilmsWithVariablesQueryDocument = graphql(/* GraphQL */ `
  query allFilmsWithVariablesQuery($first: Int!) {
    allFilms(first: $first) {
      edges {
        node {
          id
          title
        }
      }
    }
  }
`)

function App() {
  // `data` is fully typed!
  const { data } = useQuery({
    queryKey: ['films'],
    queryFn: async () =>
      request(
        'https://swapi-graphql.netlify.app/.netlify/functions/index',
        allFilmsWithVariablesQueryDocument,
        // variables are type-checked too!
        { first: 10 },
      ),
  })
  // ...
}
```

_[저장소에서 전체 예제를 확인하세요](https://github.com/dotansimha/graphql-code-generator/tree/7c25c4eeb77f88677fd79da557b7b5326e3f3950/examples/front-end/react/tanstack-react-query)_

[GraphQL Code Generator 문서의 전용 가이드](https://www.the-guild.dev/graphql/codegen/docs/guides/react-vue)로 시작해 보세요.

[//]: # 'Codegen'

