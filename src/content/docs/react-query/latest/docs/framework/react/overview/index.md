---
title: '이제 설명은 충분하니, 코드부터 보여 주세요!'
description: 'TanStack Query(이전 이름: React Query)는 웹 애플리케이션을 위한 누락된 데이터 페칭 라이브러리로 자주 소개되지만, 좀 더 기술적으로 말하면 웹 애플리케이션에서 서버 상태를 가져오고(fetching), 캐싱하고, 동기화하고, 업데이트하는 작업을 아...'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/overview

# 개요

TanStack Query(이전 이름: React Query)는 웹 애플리케이션을 위한 누락된 데이터 페칭 라이브러리로 자주 소개되지만, 좀 더 기술적으로 말하면 웹 애플리케이션에서 **서버 상태를 가져오고(fetching), 캐싱하고, 동기화하고, 업데이트하는** 작업을 아주 손쉽게 만들어 줍니다.

## 동기

대부분의 핵심 웹 프레임워크는 데이터를 포괄적으로 가져오거나 업데이트하는 방식에 대해 **명확한 의견을 제공하지 않습니다**. 그래서 개발자들은 데이터 페칭에 대해 엄격한 의견을 캡슐화한 메타 프레임워크를 만들거나, 데이터를 가져오는 자신만의 방식을 만들어 내곤 합니다. 이는 보통 컴포넌트 기반 상태와 부작용을 억지로 조합하거나, 더 범용적인 상태 관리 라이브러리를 사용해 앱 전반에 비동기 데이터를 저장하고 제공한다는 뜻이기도 합니다.

대부분의 전통적인 상태 관리 라이브러리는 클라이언트 상태를 다루는 데에는 훌륭하지만, **비동기 또는 서버 상태를 다루는 데에는 그다지 뛰어나지 않습니다**. 이는 **서버 상태가 완전히 다르기 때문**입니다. 우선 서버 상태는 다음과 같습니다:

- 여러분이 통제하거나 소유하지 않을 수 있는 원격 위치에 영구 저장됩니다.
- 가져오기와 업데이트를 위해 비동기 API가 필요합니다.
- 공유 소유권을 내포하며 여러분이 모르는 사이 다른 사람에 의해 변경될 수 있습니다.
- 주의를 기울이지 않으면 애플리케이션에서 “구식(out of date)” 상태가 될 수 있습니다.

애플리케이션에서 서버 상태의 본질을 이해하고 나면, 진행하면서 **더 많은 도전 과제가 나타납니다**. 예를 들어:

- 캐싱…(프로그래밍에서 아마 가장 어려운 일)
- 동일한 데이터에 대한 중복 요청을 하나의 요청으로 통합
- 배경에서 “구식” 데이터를 업데이트
- 데이터가 “구식”인지 판단
- 가능한 한 빨리 데이터 업데이트를 반영
- 페이지네이션, 지연 로딩 같은 성능 최적화
- 서버 상태의 메모리 및 가비지 컬렉션 관리
- 구조적 공유를 통한 쿼리 결과 메모이징

그 목록이 부담스럽지 않다면 이미 모든 서버 상태 문제를 해결했고 상을 받아야 할지도 모릅니다. 하지만 대부분의 사람처럼 아직 이러한 문제 대부분을 다루지 않았다면, 지금 소개한 것은 빙산의 일각일 뿐입니다!

TanStack Query는 서버 상태를 관리하는 데 있어 손꼽히는 _최고_의 라이브러리입니다. **제로 구성으로 바로 사용 가능**하며, 애플리케이션이 성장함에 따라 원하는 대로 커스터마이즈할 수 있습니다.

TanStack Query는 _서버 상태_가 만들어 내는 까다로운 도전과 장벽을 무너뜨리고, 애플리케이션 데이터가 여러분을 지배하기 전에 여러분이 그 데이터를 제어할 수 있게 도와줍니다.

좀 더 기술적으로 살펴보면, TanStack Query는 다음을 가능하게 합니다:

- 애플리케이션에서 오해를 불러오는 복잡한 코드 **다수를 제거**하고 소수의 TanStack Query 로직으로 대체
- 새로운 서버 상태 데이터 소스를 연결하는 걱정 없이 애플리케이션을 더 유지 보수하기 쉽고 새로운 기능을 만들기 쉽게 개선
- 애플리케이션을 이전보다 더 빠르고 반응성 있게 느껴지도록 만들어 최종 사용자 경험에 직접적인 영향
- 대역폭을 절약하고 메모리 성능을 향상할 잠재력

[//]: # 'Example'

## 이제 설명은 충분하니, 코드부터 보여 주세요!

아래 예제에서는 TanStack Query가 가장 기본적이고 단순한 형태로 TanStack Query GitHub 프로젝트 자체의 GitHub 통계를 가져오는 데 사용되는 모습을 볼 수 있습니다:

[StackBlitz에서 열기](https://stackblitz.com/github/TanStack/query/tree/main/examples/react/simple)

```tsx
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from '@tanstack/react-query'

const queryClient = new QueryClient()

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Example />
    </QueryClientProvider>
  )
}

function Example() {
  const { isPending, error, data } = useQuery({
    queryKey: ['repoData'],
    queryFn: () =>
      fetch('https://api.github.com/repos/TanStack/query').then((res) =>
        res.json(),
      ),
  })

  if (isPending) return 'Loading...'

  if (error) return 'An error has occurred: ' + error.message

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.description}</p>
      <strong>👀 {data.subscribers_count}</strong>{' '}
      <strong>✨ {data.stargazers_count}</strong>{' '}
      <strong>🍴 {data.forks_count}</strong>
    </div>
  )
}
```

[//]: # 'Example'
[//]: # 'Materials'

## 설득됐습니다. 이제 무엇을 하면 될까요?

- 공식 [TanStack Query Course](https://query.gg?s=tanstack)를 수강해 보세요(팀 전체가 함께 구매하는 것도 좋습니다!)
- 아주 꼼꼼한 [Walkthrough Guide](https://tanstack.com/query/latest/docs/framework/react/installation.md)와 [API Reference](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)를 통해 자율 학습을 진행하세요.
- [Why You Want React Query](https://tkdodo.eu/blog/why-you-want-react-query) 글을 읽어 보세요.

[//]: # 'Materials'

