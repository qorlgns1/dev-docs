---
title: "pool"
description: "테스트를 실행하는 데 사용되는 풀입니다."
---

출처 URL: https://vitest.dev/config/pool

# pool

- **유형:** `'threads' | 'forks' | 'vmThreads' | 'vmForks'`
- **기본값:** `'forks'`
- **CLI:** `--pool=threads`

테스트를 실행하는 데 사용되는 풀입니다.

## threads

멀티스레딩을 활성화합니다. `threads`를 사용할 때는 `process.chdir()` 같은 프로세스 관련 API를 사용할 수 없습니다. Prisma, `bcrypt`, `canvas`처럼 네이티브 언어로 작성된 일부 라이브러리는 멀티스레드 환경에서 문제가 발생해 segfault가 날 수 있습니다. 이런 경우에는 대신 `forks` 풀을 사용하는 것이 권장됩니다.

## forks

`threads` 풀과 유사하지만 `worker_threads` 대신 `child_process`를 사용합니다. 테스트와 메인 프로세스 간 통신은 `threads` 풀보다 빠르지 않습니다. `process.chdir()` 같은 프로세스 관련 API는 `forks` 풀에서 사용할 수 있습니다.

## vmThreads

`threads` 풀에서 [VM context](https://nodejs.org/api/vm.html)(샌드박스 환경 내부)를 사용해 테스트를 실행합니다.

이 방식은 테스트를 더 빠르게 실행하게 해주지만, VM 모듈은 [ESM code](https://github.com/nodejs/node/issues/37648)를 실행할 때 불안정합니다. 또한 테스트에서 [메모리 누수](https://github.com/nodejs/node/issues/33439)가 발생합니다. 이를 완화하려면 [`vmMemoryLimit`](#vmMemorylimit) 값을 수동으로 조정하는 것을 고려하세요.

::: warning
샌드박스에서 코드를 실행하면 장점(더 빠른 테스트)이 있지만, 여러 단점도 함께 있습니다.

- (`fs`, `path` 등) 네이티브 모듈 내부의 전역 객체는 테스트 환경에 존재하는 전역 객체와 다릅니다. 그 결과, 이런 네이티브 모듈에서 발생한 에러는 코드에서 사용하는 Error 생성자와 다른 Error 생성자를 참조하게 됩니다.

```ts
try {
  fs.writeFileSync("/doesnt exist");
} catch (err) {
  console.log(err instanceof Error); // false
}
```

- ES 모듈을 import하면 무기한 캐시되어, 컨텍스트(테스트 파일)가 많을 경우 메모리 누수가 발생합니다. Node.js에는 해당 캐시를 지우는 API가 없습니다.
- 샌드박스 환경에서는 전역 객체 접근이 [더 오래 걸립니다](https://github.com/nodejs/node/issues/31658).

이 옵션을 사용할 때는 위 문제들을 반드시 인지해 주세요. Vitest 팀에서는 이 문제들을 자체적으로 해결할 수 없습니다.
:::

## vmForks

`vmThreads` 풀과 유사하지만 `worker_threads` 대신 `child_process`를 사용합니다. 테스트와 메인 프로세스 간 통신은 `vmThreads` 풀보다 빠르지 않습니다. `process.chdir()` 같은 프로세스 관련 API는 `vmForks` 풀에서 사용할 수 있습니다. 이 풀에도 `vmThreads`에 나열된 것과 동일한 함정이 있다는 점에 유의하세요.
