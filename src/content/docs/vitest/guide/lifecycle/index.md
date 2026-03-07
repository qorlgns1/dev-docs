---
title: "테스트 실행 라이프사이클"
description: "테스트 실행 라이프사이클을 이해하는 것은 효과적인 테스트 작성, 이슈 디버깅, 테스트 스위트 최적화에 필수적입니다. 이 가이드는 초기화부터 teardown까지, Vitest에서 서로 다른 라이프사이클 단계가 언제 어떤 순서로 발생하는지 설명합니다."
---

출처 URL: https://vitest.dev/guide/lifecycle

# 테스트 실행 라이프사이클

테스트 실행 라이프사이클을 이해하는 것은 효과적인 테스트 작성, 이슈 디버깅, 테스트 스위트 최적화에 필수적입니다. 이 가이드는 초기화부터 teardown까지, Vitest에서 서로 다른 라이프사이클 단계가 언제 어떤 순서로 발생하는지 설명합니다.

## 개요

일반적인 Vitest 테스트 실행은 다음 주요 단계를 거칩니다:

1. **초기화(Initialization)** - 설정 로딩 및 프로젝트 준비
1. **전역 설정(Global Setup)** - 테스트 실행 전 1회 설정
1. **워커 생성(Worker Creation)** - [pool](https://vitest.dev/config/pool) 설정에 따라 테스트 워커 생성
1. **테스트 파일 수집(Test File Collection)** - 테스트 파일 탐색 및 구성
1. **테스트 실행(Test Execution)** - 훅과 assertion과 함께 테스트 실행
1. **리포팅(Reporting)** - 결과 수집 및 보고
1. **전역 해제(Global Teardown)** - 모든 테스트 완료 후 최종 정리

4–6단계는 테스트 파일마다 한 번씩 실행되므로, 전체 테스트 스위트에서는 여러 번 실행되며 [1 worker](https://vitest.dev/config/maxworkers)보다 많이 사용할 경우 서로 다른 파일 간 병렬로도 실행될 수 있습니다.

## 상세 라이프사이클 단계

### 1. 초기화 단계

`vitest`를 실행하면 프레임워크는 먼저 설정을 로드하고 테스트 환경을 준비합니다.

**발생하는 일:**

- [명령줄](https://vitest.dev/guide/cli) 인자를 파싱합니다
- [설정 파일](https://vitest.dev/config/)을 로드합니다
- 프로젝트 구조를 검증합니다

설정 파일 또는 해당 import 중 하나가 변경되면 이 단계가 다시 실행될 수 있습니다.

**범위:** 메인 프로세스(테스트 워커 생성 전)

### 2. 전역 설정 단계

[`globalSetup`](https://vitest.dev/config/globalsetup) 파일을 설정한 경우, 테스트 워커가 생성되기 전에 한 번 실행됩니다.

**발생하는 일:**

- 전역 설정 파일의 `setup()` 함수(또는 export된 `default` 함수)가 순차적으로 실행됩니다
- 여러 전역 설정 파일은 정의된 순서대로 실행됩니다

**범위:** 메인 프로세스(테스트 워커와 분리됨)

**중요 참고사항:**

- 전역 설정은 테스트와 **다른 전역 스코프**에서 실행됩니다
- 테스트는 전역 설정에서 정의된 변수에 접근할 수 없습니다(대신 [`provide`/`inject`](https://vitest.dev/config/provide) 사용)
- 전역 설정은 큐에 최소 하나의 테스트가 있을 때만 실행됩니다

```ts [globalSetup.ts]
export function setup(project) {
  // Runs once before all tests
  console.log("Global setup");

  // Share data with tests
  project.provide("apiUrl", "http://localhost:3000");
}

export function teardown() {
  // Runs once after all tests
  console.log("Global teardown");
}
```

### 3. 워커 생성 단계

전역 설정이 완료되면 Vitest는 [pool configuration](https://vitest.dev/config/pool)에 따라 테스트 워커를 생성합니다.

**발생하는 일:**

- `browser.enabled` 또는 `pool` 설정(`threads`, `forks`, `vmThreads`, `vmForks`)에 따라 워커가 생성됩니다
- 각 워커는 자체 격리 환경을 가집니다([isolation](https://vitest.dev/config/isolate)이 비활성화된 경우 제외)
- 기본적으로 격리를 위해 워커는 재사용되지 않습니다. 다음 경우에만 워커가 재사용됩니다:
  - [isolation](https://vitest.dev/config/isolate)이 비활성화된 경우
  - 또는 [VM](https://nodejs.org/api/vm.html)이 충분한 격리를 제공하므로 pool이 `vmThreads` 또는 `vmForks`인 경우

**범위:** 워커 프로세스/스레드

### 4. 테스트 파일 설정 단계

각 테스트 파일이 실행되기 전에 [setup files](https://vitest.dev/config/setupfiles)가 실행됩니다.

**발생하는 일:**

- Setup 파일은 테스트와 동일한 프로세스에서 실행됩니다
- 기본적으로 setup 파일은 **병렬** 실행됩니다([`sequence.setupFiles`](https://vitest.dev/config/sequence#sequence-setupfiles)로 설정 가능)
- Setup 파일은 **각 테스트 파일마다** 실행됩니다
- 전역 _state_ 또는 설정을 여기서 초기화할 수 있습니다

**범위:** 워커 프로세스(테스트와 동일)

**중요 참고사항:**

- [isolation](https://vitest.dev/config/isolate)이 비활성화되어 있어도, setup 파일은 부수 효과를 발생시키기 위해 각 테스트 파일 전에 다시 실행되지만 import된 모듈은 캐시됩니다
- watch mode에서 setup 파일을 수정하면 모든 테스트가 다시 실행됩니다

```ts [setupFile.ts]
import { afterEach } from "vitest";

// Runs before each test file
console.log("Setup file executing");

// Register hooks that apply to all tests
afterEach(() => {
  cleanup();
});
```

### 5. 테스트 수집 및 실행 단계

실제로 테스트가 실행되는 핵심 단계입니다.

#### 테스트 파일 실행 순서

테스트 파일은 설정에 따라 실행됩니다:

- 워커 내에서는 기본적으로 **순차 실행**
- 서로 다른 워커 간 파일은 [`maxWorkers`](https://vitest.dev/config/maxworkers) 설정에 따라 **병렬 실행**
- [`sequence.shuffle`](https://vitest.dev/config/sequence#sequence-shuffle)로 순서를 무작위화하거나 [`sequence.sequencer`](https://vitest.dev/config/sequence#sequence-sequencer)로 세밀하게 조정 가능
- 일반적으로(캐시 기반) 장시간 실행 테스트가 먼저 시작되며, shuffle이 활성화된 경우는 예외입니다

#### 각 테스트 파일 내부

실행 순서는 다음과 같습니다:

1. **파일 레벨 코드** - `describe` 블록 외부의 모든 코드는 즉시 실행됩니다
1. **테스트 수집** - `describe` 블록이 처리되고, 테스트 파일 import의 부수 효과로 테스트가 등록됩니다
1. **`beforeAll` 훅** - 스위트 내 어떤 테스트보다 먼저 1회 실행됩니다
1. **각 테스트마다:**
   - `beforeEach` 훅 실행(정의 순서 또는 [`sequence.hooks`](https://vitest.dev/config/sequence#sequence-hooks)에 따름)
   - 테스트 함수 실행
   - `afterEach` 훅 실행(기본적으로 `sequence.hooks: 'stack'`일 때 역순)
   - [`onTestFinished`](https://vitest.dev/api/#ontestfinished) 콜백 실행(항상 역순)
   - 테스트 실패 시: [`onTestFailed`](https://vitest.dev/api/#ontestfailed) 콜백 실행
   - 참고: `repeats` 또는 `retry`가 설정되어 있으면 위 모든 단계가 다시 실행됩니다
1. **`afterAll` 훅** - 스위트 내 모든 테스트 완료 후 1회 실행됩니다

**실행 흐름 예시:**

```ts
// This runs immediately (collection phase)
console.log("File loaded");

describe("User API", () => {
  // This runs immediately (collection phase)
  console.log("Suite defined");

  beforeAll(() => {
    // Runs once before all tests in this suite
    console.log("beforeAll");
  });

  beforeEach(() => {
    // Runs before each test
    console.log("beforeEach");
  });

  test("creates user", () => {
    // Test executes
    console.log("test 1");
  });

  test("updates user", () => {
    // Test executes
    console.log("test 2");
  });

  afterEach(() => {
    // Runs after each test
    console.log("afterEach");
  });

  afterAll(() => {
    // Runs once after all tests in this suite
    console.log("afterAll");
  });
});

// Output:
// File loaded
// Suite defined
// beforeAll
// beforeEach
// test 1
// afterEach
// beforeEach
// test 2
// afterEach
// afterAll
```

#### 중첩 스위트

중첩된 `describe` 블록을 사용할 때 훅은 계층적 패턴을 따릅니다:

```ts
describe("outer", () => {
  beforeAll(() => console.log("outer beforeAll"));
  beforeEach(() => console.log("outer beforeEach"));

  test("outer test", () => console.log("outer test"));

  describe("inner", () => {
    beforeAll(() => console.log("inner beforeAll"));
    beforeEach(() => console.log("inner beforeEach"));

    test("inner test", () => console.log("inner test"));

    afterEach(() => console.log("inner afterEach"));
    afterAll(() => console.log("inner afterAll"));
  });

  afterEach(() => console.log("outer afterEach"));
  afterAll(() => console.log("outer afterAll"));
});

// Output:
// outer beforeAll
// outer beforeEach
// outer test
// outer afterEach
// inner beforeAll
// outer beforeEach
// inner beforeEach
// inner test
// inner afterEach (with stack mode)
// outer afterEach (with stack mode)
// inner afterAll
// outer afterAll
```

#### 동시성 테스트

`test.concurrent` 또는 [`sequence.concurrent`](https://vitest.dev/config/sequence#sequence-concurrent)를 사용할 때:

- 동일 파일 내 테스트를 병렬 실행할 수 있습니다
- 각 동시성 테스트는 여전히 자체 `beforeEach` 및 `afterEach` 훅을 실행합니다
- 동시성 스냅샷에는 [test context](https://vitest.dev/guide/test-context)를 사용하세요: `test.concurrent('name', async ({ expect }) => {})`

### 6. 리포팅 단계

테스트 실행 전반에 걸쳐 reporter는 라이프사이클 이벤트를 수신하고 결과를 표시합니다.

**발생하는 일:**

- 테스트 진행에 따라 reporter가 이벤트를 수신합니다
- 결과를 수집하고 형식화합니다
- 테스트 요약을 생성합니다
- 커버리지 리포트를 생성합니다(활성화된 경우)

reporter 라이프사이클에 대한 자세한 내용은 [Reporters](https://vitest.dev/api/advanced/reporters) 가이드를 참고하세요.

### 7. 전역 해제 단계

모든 테스트 완료 후 전역 teardown 함수가 실행됩니다.

**발생하는 일:**

- [`globalSetup`](https://vitest.dev/config/globalsetup) 파일의 `teardown()` 함수가 실행됩니다
- 여러 teardown 함수는 setup의 **역순**으로 실행됩니다
- watch mode에서는 테스트 재실행 사이가 아니라 프로세스 종료 전에 teardown이 실행됩니다

**범위:** 메인 프로세스

```ts [globalSetup.ts]
export function teardown() {
  // Clean up global resources
  console.log("Global teardown complete");
}
```

## 서로 다른 스코프에서의 라이프사이클

코드가 어디서 실행되는지 이해하는 것은 흔한 함정을 피하는 데 매우 중요합니다:

| 단계                       | 스코프              | 테스트 컨텍스트 접근              | 실행 횟수                         |
| -------------------------- | ------------------- | --------------------------------- | --------------------------------- |
| Config File                | 메인 프로세스       | ❌ 불가                           | Vitest 실행당 1회                 |
| Global Setup               | 메인 프로세스       | ❌ 불가 (`provide`/`inject` 사용) | Vitest 실행당 1회                 |
| Setup Files                | 워커(테스트와 동일) | ✅ 가능                           | 각 테스트 파일 이전               |
| 파일 레벨 코드             | 워커                | ✅ 가능                           | 테스트 파일당 1회                 |
| `beforeAll` / `afterAll`   | 워커                | ✅ 가능                           | 스위트당 1회                      |
| `beforeEach` / `afterEach` | 워커                | ✅ 가능                           | 테스트마다                        |
| 테스트 함수                | 워커                | ✅ 가능                           | 1회(또는 retry/repeats로 더 많이) |
| Global Teardown            | 메인 프로세스       | ❌ 불가                           | Vitest 실행당 1회                 |

## Watch Mode 라이프사이클

watch mode에서는 일부 차이와 함께 라이프사이클이 반복됩니다:

1. **초기 실행** - 위에서 설명한 전체 라이프사이클 실행
1. **파일 변경 시:**
   - 새로운 [test run](https://vitest.dev/api/advanced/reporters#ontestrunstart) 시작
   - 영향받은 테스트 파일만 재실행
   - 해당 테스트 파일에 대해 [Setup files](https://vitest.dev/config/setupfiles) 다시 실행
   - [Global setup](https://vitest.dev/config/globalsetup)은 **다시 실행되지 않음**(재실행 전용 로직은 [`project.onTestsRerun`](https://vitest.dev/config/globalsetup#handling-test-reruns) 사용)
1. **종료 시:**
   - Global teardown 실행
   - 프로세스 종료

## 성능 고려사항

라이프사이클을 이해하면 테스트 성능 최적화에 도움이 됩니다:

- **Global setup**은 비용이 큰 1회성 작업(데이터베이스 시드, 서버 시작)에 이상적입니다
- **Setup files**는 각 테스트 파일 전에 실행됩니다. 테스트 파일이 많다면 여기서 무거운 작업을 피하세요
- 격리가 필요 없는 비용 큰 설정에는 **`beforeAll`**이 `beforeEach`보다 낫습니다
- **[isolation](https://vitest.dev/config/isolate) 비활성화**는 성능을 높이지만, setup 파일은 여전히 파일마다 실행됩니다
- **[Pool configuration](https://vitest.dev/config/pool)**은 병렬화와 사용 가능한 API에 영향을 줍니다

성능 개선 팁은 [Improving Performance](https://vitest.dev/guide/improving-performance) 가이드를 참고하세요.

## 관련 문서

- Global Setup Configuration
- Setup Files Configuration
- Test Sequencing Options
- Isolation Configuration
- Pool Configuration
- [Extending Reporters](https://vitest.dev/guide/advanced/reporters) - reporter 라이프사이클 이벤트용
- [Test API Reference](https://vitest.dev/api/) - 훅 API 및 테스트 함수용
