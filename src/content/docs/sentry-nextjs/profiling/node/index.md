---
title: 'Node Profiling | Next.js용 Sentry'
description: '기본적으로 아래 예시처럼 트랜잭션으로 scope를 구성하지 않으면 Sentry 오류 이벤트에 trace 컨텍스트가 포함되지 않습니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node

# Node Profiling | Next.js용 Sentry

기본적으로 아래 예시처럼 트랜잭션으로 scope를 구성하지 않으면 Sentry 오류 이벤트에 trace 컨텍스트가 포함되지 않습니다.

고처리량 환경에서 Profiling을 도입하는 경우, 배포 전에 테스트하여 서비스의 성능 특성이 기대치를 유지하는지 확인할 것을 권장합니다.

## [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#installation)

메인 SDK 패키지 외에 `@sentry/profiling-node` 패키지도 설치해야 합니다:

```bash
npm install @sentry/profiling-node --save
```

`@sentry/profiling-node` 패키지의 버전은 메인 SDK 패키지 버전과 정확히 일치해야 합니다.

## [Profiling 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#enabling-profiling)

Profiling은 `manual`과 `trace` 두 가지 모드를 지원합니다. 이 모드들은 서로 배타적이며 동시에 사용할 수 없습니다.

`manual` 모드에서는 `Sentry.profiler.startProfiler` 및 `Sentry.profiler.stopProfiler` 호출로 profiling 데이터 수집을 관리할 수 있습니다. 프로파일러가 언제 실행될지 완전히 직접 제어합니다.

`trace` 모드에서는 프로파일러가 spans를 기준으로 자체적으로 시작/중지 호출을 관리합니다. 활성 span이 하나 이상 있는 동안 프로파일러는 계속 실행되며, 활성 span이 없으면 중지됩니다.

- [Trace Lifecycle Profiling 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#enabling-trace-lifecycle-profiling)

Profiling을 활성화하려면 import에 `@sentry/profiling-node`를 추가하고 Sentry 설정에서 `nodeProfilingIntegration`을 구성하세요.

```javascript
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add our Profiling integration
+   nodeProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
+ profileSessionSampleRate: 1.0,
+ profileLifecycle: 'trace',
});

// Profiling happens automatically after setting it up with `Sentry.init()`.
// All spans (unless those discarded by sampling) will have profiling data attached to them.
Sentry.startSpan(
  {
    op: "rootSpan",
    name: "My root span",
  },
  () => {
    // The code executed here will be profiled
  }
);
```

- [Manual Lifecycle Profiling 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#enabling-manual-lifecycle-profiling)

Profiling을 활성화하려면 import에 `@sentry/profiling-node`를 추가하고 Sentry 설정에서 `nodeProfilingIntegration`을 구성하세요.

```javascript
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add our Profiling integration
+   nodeProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
+ profileSessionSampleRate: 1.0,
+ profileLifecycle: 'manual',
});

// All spans (unless those discarded by sampling) will have profiling data attached to them.
Sentry.profiler.startProfiler();
// Code executed between these two calls will be profiled
Sentry.profiler.stopProfiler();
```

- [프로파일 샘플링 비율 관리](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#managing-profile-sampling-rates)

Sentry SDK는 세션 전체에 대해 profiling 활성화 여부를 결정하는 추가 옵션 `profileSessionSampleRate`를 지원합니다. 샘플링 결정은 SDK 초기화 시 한 번만 평가되므로, 서비스 수준에서 세션 샘플링 비율을 제어하려는 경우 사용할 수 있습니다.

이는 서비스를 여러 번 배포하더라도 그중 일부 서비스에서만 profiling을 수행하고 싶을 때 유용합니다.

```javascript
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Add our Profiling integration
    nodeProfilingIntegration(),
  ],
  tracesSampleRate: 1.0,
+ profileSessionSampleRate: 0.0
});
```

## [어떻게 동작하나요?](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#how-does-it-work)

내부적으로 Sentry 프로파일러는 V8의 [CpuProfiler](https://v8docs.nodesource.com/node-18.2/d2/d34/classv8_1_1_cpu_profiler.html)를 사용해 스택 샘플을 수집합니다. 즉, `sentry/profiling-node`는 Node용 [native add-on](https://nodejs.org/docs/latest-v18.x/api/addons.html)으로 작성되어 Deno나 Bun 같은 환경에서는 실행되지 않습니다. Profiling은 개별 트랜잭션의 프로파일을 제공하여 tracing을 강화합니다. 이를 통해 프로파일을 깊게 분석하기 전에 트랜잭션 및 span duration 같은 상위 수준의 성능 정보를 먼저 확인할 수 있습니다.

## [런타임 플래그](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#runtime-flags)

프로파일러 동작을 제어하는 런타임 플래그는 세 가지입니다. 이 중 두 개는 SDK가 프로파일러 바이너리를 해석하는 방식과 관련되며, 나머지 하나는 내부 프로파일러가 [v8](https://v8docs.nodesource.com/)에 의해 초기화되는 방식을 변경합니다.

이 플래그들은 고급 사용 사례 전용입니다. 대부분의 경우 설정이 필요하지 않습니다.

* SENTRY\_PROFILER\_BINARY\_PATH

이 플래그는 프로파일러 바이너리 경로를 설정하고 아키텍처, 플랫폼, libc 검사를 우회합니다. 런타임에 어떤 바이너리를 사용할지 재정의하려는 일부 빌드 구성에서 유용할 수 있습니다.

* SENTRY\_PROFILER\_BINARY\_DIR

위 플래그와 유사하게 동작하지만, 이 플래그는 바이너리가 있는 디렉터리만 지정하고, 아키텍처/플랫폼/libc 버전에 따라 올바른 바이너리를 해석하는 작업은 런타임에 맡깁니다.

* SENTRY\_PROFILER\_LOGGING\_MODE

v8 CpuProfiler의 기본 모드는 [kEagerLogging](https://v8docs.nodesource.com/node-18.2/d2/dc3/namespacev8.html#a874b4921ddee43bef58d8538e3149374)이며, 이 모드에서는 활성 프로파일이 없어도 프로파일러가 켜집니다. 이는 지속적인 CPU 오버헤드가 발생하는 대신 startProfgiler 호출을 더 빠르게 만든다는 장점이 있습니다. 이 동작은 `SENTRY_PROFILER_LOGGING_MODE` 환경 변수에 `eager|lazy` 값을 설정해 제어할 수 있습니다. lazy-logging 모드를 선택하면 `startProfiler` 호출이 느릴 수 있습니다. (환경과 node 버전에 따라 수백 ms 수준일 수 있습니다.)

다음은 lazy-logging 모드로 서버를 시작하는 예시입니다:

```bash
# Run profiler in lazy mode
SENTRY_PROFILER_LOGGING_MODE=lazy node server.js
```

## [사전 컴파일된 바이너리](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling/node.md#precompiled-binaries)

`@sentry/profiling-node` 패키지는 여러 일반 아키텍처용 바이너리를 사전 컴파일해 제공합니다. 이를 통해 패키지 실행에 필요한 도구를 최소화하고, 대부분의 경우 소스에서 패키지를 컴파일할 필요를 줄여 설치 속도를 높입니다. 현재 다음 아키텍처와 Node 버전에 대해 사전 빌드 바이너리를 제공합니다:

* macOS x64: Node v18, v20, v22, v24
* Linux ARM64 (musl): Node v18, v20, v22, v24
* Linux x64 (glibc): Node v18, v20, v22, v24
* Windows x64: Node v18, v20, v22, v24

이러한 일반 아키텍처 구성은 다양한 사용 사례를 폭넓게 커버해야 하지만, 피드백이 있거나 다른 동작을 경험했다면 [Sentry JavaScript SDK](https://github.com/getsentry/sentry-javascript) 리포지토리에 이슈를 등록해 주세요.

