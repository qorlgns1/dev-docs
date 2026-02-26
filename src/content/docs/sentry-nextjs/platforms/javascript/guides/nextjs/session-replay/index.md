---
title: 'Session Replay 설정 | Next.js용 Sentry'
description: '질문이나 피드백이 있거나 버그를 신고하려면, 관련 리플레이 링크 또는 가능하다면 리플레이를 기록하려는 페이지의 공개 접근 가능한 URL을 포함해 GitHub issue를 열어 주세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay

# Session Replay 설정 | Next.js용 Sentry

질문이나 피드백이 있거나 버그를 신고하려면, 관련 리플레이 링크 또는 가능하다면 리플레이를 기록하려는 페이지의 공개 접근 가능한 URL을 포함해 [GitHub issue](https://github.com/getsentry/sentry/issues/new?assignees=\&labels=\&template=bug.yml)를 열어 주세요.

[Session Replay](https://docs.sentry.io/product/explore/session-replay.md)를 사용하면 문제 전, 중, 후에 사용자 브라우저에서 어떤 일이 있었는지 비디오처럼 재현하여 오류나 지연 이슈의 근본 원인을 더 빠르게 파악할 수 있습니다. 브라우저 DevTools에서 영감을 받은 단일 통합 UI에서 애플리케이션의 DOM 상태를 되감아 재생하고, 마우스 클릭, 스크롤, 네트워크 요청, 콘솔 항목 같은 주요 사용자 상호작용을 확인할 수 있습니다.

기본적으로 Session Replay SDK는 모든 DOM 텍스트 콘텐츠, 이미지, 사용자 입력을 마스킹하므로 민감한 데이터가 브라우저를 벗어나지 않는다는 점에서 더 높은 신뢰를 제공합니다. 자세한 내용은 [Session Replay Privacy](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)를 참고하세요.

## [사전 요구 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#prerequisites)

Session Replay를 사용하려면 SDK 버전이 `7.27.0` 이상이어야 합니다. 이전 버전을 사용 중이라면 [migration document](https://github.com/getsentry/sentry-javascript/blob/master/MIGRATION.md)를 확인하세요.

Session Replay는 Node 12+ 및 IE11보다 최신 브라우저가 필요합니다.

## [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#install)

Session Replay는 `@sentry/nextjs`에 포함되어 있습니다. 아직 Sentry를 설치하지 않았다면 wizard를 실행하세요:

```bash
npx @sentry/wizard@latest -i nextjs
```

이미 Sentry가 설치되어 있다면 아래 [Set Up](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#set-up)로 이동하세요.

## [설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#set-up)

통합을 설정하려면 Sentry 초기화 코드에 다음을 추가하세요. 통합 생성자에 전달할 수 있는 옵션은 여러 가지가 있습니다. 자세한 내용은 [configuration documentation](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md)을 참고하세요.

Session Replay는 브라우저에서만 실행되므로 `instrumentation-client.ts`에서만 설정하면 됩니다. 서버(`sentry.server.config.ts`) 및 edge(`sentry.edge.config.ts`) 엔트리 포인트는 Replay를 사용할 수 없는 Node.js 및 Edge 런타임에서 실행됩니다.

#
- [Replay 통합 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#add-replay-integration)

클라이언트 초기화에 `replayIntegration()`을 추가하고 샘플링 비율을 설정하세요.

**테스트 팁:** 개발 중에는 `replaysSessionSampleRate: 1.0`으로 설정해 모든 세션을 캡처하세요.

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // This sets the sample rate to be 10%. You may want this to be 100% while
  // in development and sample at a lower rate in production
  replaysSessionSampleRate: 0.1,

  // If the entire session is not sampled, use the below sample rate to sample
  // sessions when an error occurs.
  replaysOnErrorSampleRate: 1.0,

  integrations: [Sentry.replayIntegration()],
});
```

#
- [개인정보 보호 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#privacy-options)

기본적으로 Replay는 모든 텍스트를 마스킹하고 미디어를 차단합니다. 필요에 따라 개인정보 보호 설정을 사용자화하세요.

모든 옵션은 [Session Replay Privacy](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)에서 확인하세요.

`instrumentation-client.ts`

```typescript
Sentry.replayIntegration({
  // Text masking (default: true)
  maskAllText: true,

  // Block images/videos (default: true)
  blockAllMedia: true,

  // Mask specific inputs
  maskAllInputs: true,
}),
```

- [PII 및 개인정보 보호 고려 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#pii--privacy-considerations)

Session Replay를 활성화할 때는 개인 식별 정보(PII)와 개인정보 보호를 중요하게 고려해야 합니다. Sentry는 다음을 포함해 PII 수집을 피할 수 있도록 여러 방법을 제공합니다.

* [Masking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#masking): 텍스트 콘텐츠를 다른 값으로 대체합니다(기본 동작은 각 문자를 `*`로 대체).
* PII를 포함할 수 있는 엔드포인트 캡처를 피하기 위해 [network request and response bodies](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#network-request-and-response-bodies-and-headers)를 옵트인으로 제공.

민감한 데이터가 없는 정적 웹사이트의 경우 기본 마스킹 및 차단 설정을 비활성화할 수 있습니다.

#
- [Replay 지연 로딩](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#lazy-loading-replay)

시작 시점이 아니라 필요할 때만 Replay를 로드하세요. 초기 번들 크기를 줄이는 데 유용합니다.

`instrumentation-client.ts`

```typescript
// Don't add replayIntegration to init
Sentry.init({
  integrations: [],
});

// Later, when you want to start recording:
import("@sentry/nextjs").then((lazyLoadedSentry) => {
  Sentry.addIntegration(lazyLoadedSentry.replayIntegration());
});
```

- [Canvas 기록](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#canvas-recording)

현재 canvas 기록에는 PII 스크러빙이 없습니다!

#
- [Canvas 기록 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#enable-canvas-recording)

HTML canvas 요소를 기록하려면 `replayCanvasIntegration()`을 추가하세요. 이는 옵트인이며 사용하지 않으면 번들에서 tree-shaking 됩니다.

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,

  integrations: [
    // Keep the Replay integration as before
    Sentry.replayIntegration(),

    // The following is all you need to enable canvas recording with Replay

    Sentry.replayCanvasIntegration(),

  ],
});
```

#
- [3D 및 WebGL Canvas](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#3d-and-webgl-canvases)

3D/WebGL canvas의 경우 통합이 이미지를 내보내기 위해 `preserveDrawingBuffer`를 필요로 하며, 이는 성능에 영향을 줄 수 있습니다. 이를 피하려면 수동 스냅샷을 활성화하고 페인트 루프 내부에서 `snapshot()`을 호출하세요.

빈 버퍼가 캡처되지 않도록 draw 명령과 동일한 실행 루프에서 `snapshot()`을 호출하세요.

```javascript
// Step 1: Enable manual snapshotting
Sentry.replayCanvasIntegration({
  enableManualSnapshot: true,
});

// Step 2: Call snapshot in your paint loop
function paint() {
  const canvasRef = document.querySelector("#my-canvas");
  Sentry.getClient()
    ?.getIntegrationByName("ReplayCanvas")
    ?.snapshot(canvasRef);
}
```

#
- [WebGPU Canvas](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#webgpu-canvases)

WebGPU canvas 텍스처는 현재 task가 끝나면 만료됩니다. 렌더링 직후 캡처하려면 `skipRequestAnimationFrame: true`를 사용하세요.

```javascript
// Step 1: Enable manual snapshotting
Sentry.replayCanvasIntegration({
  enableManualSnapshot: true,
});

// Step 2: Snapshot immediately after rendering
function paint() {
  const canvasRef = document.querySelector("#my-canvas");
  const canvasIntegration =
    Sentry.getClient()?.getIntegrationByName("ReplayCanvas");

  // ... your WebGPU rendering commands ...

  // Capture immediately - required for WebGPU
  canvasIntegration?.snapshot(canvasRef, {
    skipRequestAnimationFrame: true,
  });
}
```

- [콘텐츠 보안 정책 (CSP)](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#content-security-policy-csp)

#
- [Replay용 CSP 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#configure-csp-for-replay)

Session Replay는 메인 UI 스레드 외부에서 압축을 수행하기 위해 WebWorker를 사용합니다. 워커 로딩을 허용하려면 다음 CSP 항목을 추가하세요.

Safari 버전 ≤ 15.4에서는 `child-src`도 필요합니다.

```text
worker-src 'self' blob:
child-src 'self' blob:
```

CSP 정책을 업데이트하여 인라인 웹 워커를 허용할 수 없다면, 대신 [use a custom compression worker](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#using-a-custom-compression-worker)를 사용할 수도 있습니다.

## [사용자 세션](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#user-session)

사용자 세션은 Session Replay SDK가 처음 로드되고 초기화될 때 시작됩니다. SDK가 매번 동일한 도메인과 동일한 브라우저 탭에서 재초기화되는 한, 세션은 모든 페이지 로드, 새로고침, 내비게이션을 캡처합니다. 사용자 상호작용이 5분간 없거나 **또는** 최대 60분이 지나면 세션의 데이터 캡처가 종료됩니다. [SessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) 규칙에 따라 브라우저 탭을 닫으면 세션이 즉시 종료됩니다.

여기서 *interaction*은 마우스 클릭 또는 브라우저 내비게이션 이벤트를 의미합니다.

- [오류 발생 시에만 Replay 캡처](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#replay-captures-on-errors-only)

전체 세션 기록을 원하지 않는 경우, 오류가 발생할 때만 리플레이를 캡처하도록 설정할 수 있습니다. 이 경우 통합은 오류가 발생하기 전 최대 1분의 이벤트를 버퍼링합니다. 이후에는 위의 세션 수명 및 활동 규칙에 따라 세션 기록을 계속합니다. 설정 옵션은 [sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#sampling) 섹션을 참고하세요.

## [샘플링](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#sampling)

샘플링은 Session Replay로 이어지는 트래픽 양을 제어합니다.

#
- [샘플링 비율 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#configure-sample-rates)

* `replaysSessionSampleRate` - 전체 세션을 기록할 비율
* `replaysOnErrorSampleRate` - 오류 발생 시 세션을 기록할 비율(오류 전 1분 버퍼링)

**팁:** `replaysOnErrorSampleRate`를 `1.0`으로 유지하세요. 오류 세션이 디버깅 가치가 가장 높습니다.

#
- [프로덕션 권장 샘플링 비율](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#recommended-production-sample-rates)

| 트래픽 규모 | 세션 비율 | 오류 비율 |
| ------------------------- | ------------ | ---------- |
| **높음** (100k+/일)      | `0.01` (1%)  | `1.0`      |
| **중간** (10k-100k/일) | `0.1` (10%)  | `1.0`      |
| **낮음** (10k/일 미만)   | `0.25` (25%) | `1.0`      |

`instrumentation-client.ts`

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Capture 10% of all sessions
  replaysSessionSampleRate: 0.1,

  // Capture 100% of sessions with errors
  replaysOnErrorSampleRate: 1.0,

  integrations: [Sentry.replayIntegration()],
});
```

- [샘플링 동작 방식](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#how-sampling-works)

샘플링은 세션이 시작되자마자 시작됩니다. 사용자가 애플리케이션에 방문하면 샘플링 결정은 다음 순서로 이루어집니다.

1. **먼저 `replaysSessionSampleRate`를 확인**

   * 샘플링됨: 전체 세션 기록이 시작되고 실시간으로 Sentry에 전송됨
   * 샘플링되지 않음: 기록은 메모리에만 버퍼링됨(최근 60초 유지)

2. **오류가 발생하면** (그리고 세션이 전체 기록으로 선택되지 않았으면):

   * `replaysOnErrorSampleRate`를 확인
   * 샘플링됨: 버퍼링된 60초 + 세션 나머지가 Sentry로 전송됨
   * 샘플링되지 않음: 버퍼가 폐기되고 아무것도 전송되지 않음

**데이터가 브라우저를 벗어나는 시점:**

| 시나리오 | Sentry로 전송되는 데이터 |
| ------------------------------------ | ------------------------------------------- |
| 세션 샘플링에 선택됨        | 즉시(실시간 청크)              |
| 선택되지 않고 오류도 없음        | 전송되지 않음(버퍼 폐기)                    |
| 선택되지 않았지만 오류 발생 & 샘플링됨 | 오류 후(이전 60초 + 이후 전체) |

자세한 내용은 [understanding sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md)를 참고하세요.

## [오류 연결](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#error-linking)

리플레이가 실행 중인 동안 페이지에서 발생한 오류는 해당 리플레이와 연결되므로, 관련 이슈와 리플레이 사이를 오가며 확인할 수 있습니다. 다만 일부 경우 **Replays Details** 페이지에 보고된 오류 수가 실제로 캡처된 오류 수와 일치하지 않을 **수도** 있습니다. 이는 오류가 유실될 수 있기 때문이며, 흔하지는 않지만 다음과 같은 이유로 발생할 수 있습니다.

* 리플레이가 rate-limited 되어 수락되지 못함
* 조직 멤버가 리플레이를 삭제함
* 네트워크 오류로 리플레이가 저장되지 않음

## [트레이스 연결](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#trace-linking)

[tracing](https://docs.sentry.io/product/explore/traces.md)이 활성화되면 Replay 타임라인에서 트레이스를 볼 수 있습니다. 이를 통해 사용자가 실제로 무엇을 하던 맥락에서 성능 데이터를 확인할 수 있습니다. 예를 들어 사용자가 버튼을 클릭하는 장면을 보고, 그에 대응하는 네트워크 요청과 소요 시간도 함께 확인할 수 있습니다.

Replay Details 페이지에서 타임라인의 trace span을 클릭하면 trace 보기로 바로 이동합니다. այնտեղ서 개별 span을 자세히 살펴보고, 데이터베이스 쿼리와 API 호출을 확인하며, 사용자 경험에 영향을 준 성능 병목을 식별할 수 있습니다.

이 연결은 양방향으로 작동합니다. trace를 보는 중에도 연결된 replay로 이동하여 해당 작업 중 사용자가 정확히 무엇을 경험했는지 확인할 수 있습니다.

## [검증](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#verify)

테스트 중에는 `replaysSessionSampleRate`를 `1.0`으로 설정하는 것을 권장합니다. 이렇게 하면 모든 사용자 세션이 Sentry로 전송됩니다.

테스트가 완료되면 **프로덕션에서는 이 값을 낮추는 것을 권장합니다**. `replaysOnErrorSampleRate`는 계속 `1.0`으로 유지하는 것을 권장합니다.

## [관련 기능](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#related-features)

* [Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) — 트레이스는 Replay 타임라인에 표시되어, 컨텍스트와 함께 성능 데이터를 보여줍니다.
* [Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md) — 리플레이 세션 중에 기록된 로그는 쉬운 탐색을 위해 자동으로 연결됩니다.

## [Replay 다음 단계](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#replay-next-steps)

*
- [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md)

  일반적인 Session Replay 구성 필드에 대해 알아보세요.

*
- [개인정보 보호](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)

  사용자 및 데이터 개인정보 보호를 유지하도록 Session Replay를 구성합니다.

*
- [Replay 이슈](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/issue-types.md)

  Session Replay가 감지할 수 있는 이슈 유형에 대해 알아보세요.

*
- [세션 이해하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md)

  Session Replay SDK로 세션을 커스터마이징하는 방법을 알아보세요.

*
- [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/troubleshooting.md)

  Session Replay 관련 이슈 문제 해결

## 이 섹션의 페이지

- [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md)
- [개인정보 보호](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)
- [Replay 이슈](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/issue-types.md)
- [세션 이해하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md)
- [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/troubleshooting.md)

