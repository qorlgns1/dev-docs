---
title: 'useMutation'
---

# useMutation

```tsx
const {
  data,
  error,
  isError,
  isIdle,
  isPending,
  isPaused,
  isSuccess,
  failureCount,
  failureReason,
  mutate,
  mutateAsync,
  reset,
  status,
  submittedAt,
  variables,
} = useMutation(
  {
    mutationFn,
    gcTime,
    meta,
    mutationKey,
    networkMode,
    onError,
    onMutate,
    onSettled,
    onSuccess,
    retry,
    retryDelay,
    scope,
    throwOnError,
  },
  queryClient,
)

mutate(variables, {
  onError,
  onSettled,
  onSuccess,
})
```

**Parameter1 (Options)**

- `mutationFn: (variables: TVariables, context: MutationFunctionContext) => Promise<TData>`
  - **기본 mutation 함수가 정의되어 있지 않은 경우 필수**
  - 비동기 작업을 수행하고 프로미스를 반환하는 함수입니다.
  - `variables`는 `mutate`가 `mutationFn`에 전달하는 객체입니다.
  - `context`는 `mutate`가 `mutationFn`에 전달하는 객체로, `QueryClient`, `mutationKey`, 선택적인 `meta` 객체에 대한 참조를 포함합니다.
- `gcTime: number | Infinity`
  - 사용되지 않거나 비활성화된 캐시 데이터가 메모리에 남아 있는 시간(밀리초)입니다. mutation의 캐시가 사용되지 않거나 비활성화되면 해당 캐시 데이터는 이 기간이 지난 후 가비지 컬렉션됩니다. 서로 다른 캐시 시간이 지정되면 가장 긴 시간이 사용됩니다.
  - `Infinity`로 설정하면 가비지 컬렉션이 비활성화됩니다.
  - 참고: 허용되는 최대 시간은 약 [24일](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout#maximum_delay_value)이며, [timeoutManager.setTimeoutProvider](https://tanstack.com/query/latest/docs/reference/timeoutManager.md#timeoutmanagersettimeoutprovider)를 사용해 이 제한을 우회할 수 있습니다.
- `mutationKey: unknown[]`
  - 선택 사항
  - `queryClient.setMutationDefaults`로 설정된 기본값을 상속하도록 mutation 키를 설정할 수 있습니다.
- `networkMode: 'online' | 'always' | 'offlineFirst'`
  - 선택 사항
  - 기본값은 `'online'`입니다.
  - 자세한 내용은 [Network Mode](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode.md)를 참고하세요.
- `onMutate: (variables: TVariables, context: MutationFunctionContext) => Promise<TOnMutateResult | void> | TOnMutateResult | void`
  - 선택 사항
  - mutation 함수가 실행되기 전에 호출되며 mutation 함수가 받는 것과 동일한 variables를 전달받습니다.
  - mutation 성공을 기대하며 리소스에 대한 낙관적 업데이트를 수행하는 데 유용합니다.
  - 이 함수에서 반환된 값은 mutation 실패 시 `onError` 및 `onSettled` 함수에 전달되어 낙관적 업데이트를 롤백하는 데 활용할 수 있습니다.
- `onSuccess: (data: TData, variables: TVariables, onMutateResult: TOnMutateResult | undefined, context: MutationFunctionContext) => Promise<unknown> | unknown`
  - 선택 사항
  - mutation이 성공하면 호출되며 결과가 전달됩니다.
  - 프로미스를 반환하면 다음 단계로 진행하기 전에 해당 프로미스가 완료될 때까지 기다립니다.
- `onError: (err: TError, variables: TVariables, onMutateResult: TOnMutateResult | undefined, context: MutationFunctionContext) => Promise<unknown> | unknown`
  - 선택 사항
  - mutation에서 오류가 발생하면 호출되며 오류가 전달됩니다.
  - 프로미스를 반환하면 다음 단계로 진행하기 전에 해당 프로미스가 완료될 때까지 기다립니다.
- `onSettled: (data: TData, error: TError, variables: TVariables, onMutateResult: TOnMutateResult | undefined, context: MutationFunctionContext) => Promise<unknown> | unknown`
  - 선택 사항
  - mutation이 성공하거나 오류가 발생한 후 호출되며 데이터나 오류 중 하나를 전달받습니다.
  - 프로미스를 반환하면 다음 단계로 진행하기 전에 해당 프로미스가 완료될 때까지 기다립니다.
- `retry: boolean | number | (failureCount: number, error: TError) => boolean`
  - 기본값은 `0`입니다.
  - `false`이면 실패한 mutation을 재시도하지 않습니다.
  - `true`이면 실패한 mutation을 무한히 재시도합니다.
  - `3`과 같은 `number`로 설정하면 실패 횟수가 해당 숫자에 도달할 때까지 재시도합니다.
- `retryDelay: number | (retryAttempt: number, error: TError) => number`
  - `retryAttempt` 정수와 실제 Error를 입력으로 받아 다음 시도 전까지의 지연 시간(밀리초)을 반환합니다.
  - `attempt => Math.min(attempt > 1 ? 2 ** attempt * 1000 : 1000, 30 * 1000)`과 같은 함수는 지수 백오프를 적용합니다.
  - `attempt => attempt * 1000`과 같은 함수는 선형 백오프를 적용합니다.
- `scope: { id: string }`
  - 선택 사항
  - 기본값은 고유 id입니다(모든 mutation이 병렬 실행).
  - 동일한 scope id를 가진 mutation은 직렬로 실행됩니다.
- `throwOnError: undefined | boolean | (error: TError) => boolean`
  - 렌더 단계에서 mutation 오류를 throw하여 가장 가까운 오류 경계까지 전파하려면 `true`로 설정하세요.
  - 오류를 오류 경계로 던지는 동작을 비활성화하려면 `false`로 설정하세요.
  - 함수로 설정하면 오류가 전달되며 오류 경계에서 표시할지(`true`) 상태로 반환할지(`false`) 여부를 결정하는 boolean을 반환해야 합니다.
- `meta: Record<string, unknown>`
  - 선택 사항
  - 설정하면 mutation 캐시 항목에 추가 정보를 저장하며 필요 시 사용할 수 있습니다. `mutation`을 사용할 수 있는 곳 어디에서든(예: `MutationCache`의 `onError`, `onSuccess` 함수) 접근 가능합니다.

**Parameter2 (QueryClient)**

- `queryClient?: QueryClient`
  - 커스텀 QueryClient를 사용하려면 지정하세요. 지정하지 않으면 가장 가까운 컨텍스트의 QueryClient가 사용됩니다.

**Returns**

- `mutate: (variables: TVariables, { onSuccess, onSettled, onError }) => void`
  - variables와 함께 호출하여 mutation을 트리거할 수 있는 mutation 함수이며, 추가 콜백 옵션을 전달할 수 있습니다.
  - `variables: TVariables`
    - 선택 사항
    - `mutationFn`에 전달할 variables 객체입니다.
  - `onSuccess: (data: TData, variables: TVariables, onMutateResult: TOnMutateResult | undefined, context: MutationFunctionContext) => void`
    - 선택 사항
    - mutation이 성공하면 호출되며 결과를 전달받습니다.
    - 반환 값은 무시됩니다.
  - `onError: (err: TError, variables: TVariables, onMutateResult: TOnMutateResult | undefined, context: MutationFunctionContext) => void`
    - 선택 사항
    - mutation에서 오류가 발생하면 호출되며 오류를 전달받습니다.
    - 반환 값은 무시됩니다.
  - `onSettled: (data: TData | undefined, error: TError | null, variables: TVariables, onMutateResult: TOnMutateResult | undefined, context: MutationFunctionContext) => void`
    - 선택 사항
    - mutation이 성공하거나 오류가 발생한 후 호출되며 데이터 또는 오류를 전달받습니다.
    - 반환 값은 무시됩니다.
  - 여러 요청을 수행하면 `onSuccess`는 가장 최근 호출 이후에만 실행됩니다.
- `mutateAsync: (variables: TVariables, { onSuccess, onSettled, onError }) => Promise<TData>`
  - `mutate`와 유사하지만 await 가능한 프로미스를 반환합니다.
- `status: MutationStatus`
  - 다음 중 하나입니다.
    - `idle`: mutation 함수가 실행되기 전 초기 상태.
    - `pending`: mutation이 현재 실행 중일 때.
    - `error`: 마지막 mutation 시도가 오류로 끝났을 때.
    - `success`: 마지막 mutation 시도가 성공했을 때.
- `isIdle`, `isPending`, `isSuccess`, `isError`: `status`에서 파생된 boolean 변수입니다.
- `isPaused: boolean`
  - mutation이 `paused` 상태이면 `true`입니다.
  - 자세한 내용은 [Network Mode](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode.md)를 참고하세요.
- `data: undefined | unknown`
  - 기본값은 `undefined`입니다.
  - mutation에서 마지막으로 성공적으로 반환된 데이터를 나타냅니다.
- `error: null | TError`
  - 오류가 발생했을 때의 오류 객체입니다.
- `reset: () => void`
  - mutation의 내부 상태를 초기 상태로 리셋하는 함수입니다.
- `failureCount: number`
  - mutation 실패 횟수입니다.
  - mutation이 실패할 때마다 증가합니다.
  - mutation이 성공하면 `0`으로 리셋됩니다.
- `failureReason: null | TError`
  - mutation 재시도 실패의 원인입니다.
  - mutation이 성공하면 `null`로 리셋됩니다.
- `submittedAt: number`
  - mutation이 제출된 시점의 타임스탬프입니다.
  - 기본값은 `0`입니다.
- `variables: undefined | TVariables`
  - `mutationFn`에 전달된 `variables` 객체입니다.
  - 기본값은 `undefined`입니다.

