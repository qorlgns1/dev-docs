---
title: 'Query Keys'
description: 'Skipping  skill because the user only requested a standalone translation and not the full add-doc workflow (frontmatter, sidebar config, deployment).'
---

Skipping `add-doc` skill because the user only requested a standalone translation and not the full add-doc workflow (frontmatter, sidebar config, deployment).

# Query Keys

기본적으로 TanStack Query는 쿼리 키를 기반으로 쿼리 캐시를 관리합니다. 쿼리 키는 최상위에서 배열이어야 하며, 단일 문자열을 담은 간단한 배열일 수도 있고 여러 문자열과 중첩 객체를 담은 복잡한 배열일 수도 있습니다. 쿼리 키가 `JSON.stringify`로 직렬화 가능하고 **특정 쿼리 데이터에 고유하다면** 사용할 수 있습니다!

## Simple Query Keys

키의 가장 단순한 형태는 상수 값들로 이루어진 배열입니다. 이 형식은 다음에 유용합니다:

- 일반적인 목록/색인 리소스
- 계층 구조가 없는 리소스

[//]: # 'Example'

```tsx
// A list of todos
useQuery({ queryKey: ['todos'], ... })

// Something else, whatever!
useQuery({ queryKey: ['something', 'special'], ... })
```

[//]: # 'Example'

## Array Keys with variables

쿼리가 고유하게 데이터를 설명하기 위해 더 많은 정보가 필요할 때는 문자열과 직렬화 가능한 객체들을 함께 포함한 배열을 사용할 수 있습니다. 이는 다음과 같은 경우에 유용합니다:

- 계층적 또는 중첩된 리소스
  - 항목을 고유하게 식별하기 위해 ID, 인덱스, 기타 원시값을 전달하는 것이 일반적입니다
- 추가 매개변수가 있는 쿼리
  - 추가 옵션 객체를 전달하는 것이 일반적입니다

[//]: # 'Example2'

```tsx
// An individual todo
useQuery({ queryKey: ['todo', 5], ... })

// An individual todo in a "preview" format
useQuery({ queryKey: ['todo', 5, { preview: true }], ...})

// A list of todos that are "done"
useQuery({ queryKey: ['todos', { type: 'done' }], ... })
```

[//]: # 'Example2'

## Query Keys are hashed deterministically!

즉, 객체 안의 키 순서와 관계없이 아래 모든 쿼리는 동일하게 간주됩니다:

[//]: # 'Example3'

```tsx
useQuery({ queryKey: ['todos', { status, page }], ... })
useQuery({ queryKey: ['todos', { page, status }], ...})
useQuery({ queryKey: ['todos', { page, status, other: undefined }], ... })
```

[//]: # 'Example3'

하지만 아래 쿼리 키는 동일하지 않습니다. 배열 항목의 순서는 중요합니다!

[//]: # 'Example4'

```tsx
useQuery({ queryKey: ['todos', status, page], ... })
useQuery({ queryKey: ['todos', page, status], ...})
useQuery({ queryKey: ['todos', undefined, page, status], ...})
```

[//]: # 'Example4'

## If your query function depends on a variable, include it in your query key

쿼리 키는 가져오는 데이터를 고유하게 설명하므로, 쿼리 함수에서 **변하는** 변수는 모두 쿼리 키에 포함해야 합니다. 예:

[//]: # 'Example5'

```tsx
function Todos({ todoId }) {
  const result = useQuery({
    queryKey: ['todos', todoId],
    queryFn: () => fetchTodoById(todoId),
  })
}
```

[//]: # 'Example5'

쿼리 키는 쿼리 함수의 의존성처럼 동작한다는 점에 주의하세요. 의존 변수를 쿼리 키에 추가하면 쿼리가 독립적으로 캐시되고, 변수가 바뀔 때마다 _쿼리가 자동으로 다시 요청_ 됩니다 (`staleTime` 설정에 따라 다름). 자세한 정보와 예시는 [exhaustive-deps](https://tanstack.com/query/latest/docs/eslint/exhaustive-deps.md) 섹션을 참고하세요.

[//]: # 'Materials'

## Further reading

더 큰 애플리케이션에서 Query Key를 구성하는 팁이 궁금하다면 [Effective React Query Keys](https://tkdodo.eu/blog/effective-react-query-keys)를 살펴보고 [Community Resources](https://tanstack.com/query/latest/docs/community-resources)에서 [Query Key Factory Package](https://github.com/lukemorales/query-key-factory)도 확인해 보세요.

[//]: # 'Materials'

