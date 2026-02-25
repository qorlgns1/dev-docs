---
title: '구성 | Sentry for Next.js'
description: '질문이나 피드백이 있거나 버그를 신고하려면, 관련 replay 링크 또는 가능하다면 replay 기록을 시도 중인 페이지의 공개 접근 가능한 URL과 함께 GitHub issue를 열어주세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration

# 구성 | Sentry for Next.js

질문이나 피드백이 있거나 버그를 신고하려면, 관련 replay 링크 또는 가능하다면 replay 기록을 시도 중인 페이지의 공개 접근 가능한 URL과 함께 [GitHub issue](https://github.com/getsentry/sentry/issues/new?assignees=\&labels=\&template=bug.yml)를 열어주세요.

## [일반 통합 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#general-integration-configuration)

다음 옵션은 브라우저 기반 Sentry SDK의 루트 레벨에서 `init({})`에 설정할 수 있습니다:

| Key                      | Type     | Default | Description                                                                                                                                                                                                                                                       |
| ------------------------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| replaysSessionSampleRate | `number` | `0`     | 즉시 기록을 시작하고 사용자 세션 전체 동안 지속되는 replay의 샘플링 비율입니다. `1.0`은 모든 replay를 수집하고, `0`은 아무것도 수집하지 않습니다.                                                                                                                   |
| replaysOnErrorSampleRate | `number` | `0`     | 오류가 발생했을 때 기록되는 replay의 샘플링 비율입니다. 이 유형의 replay는 오류 이전 최대 1분의 이벤트를 기록하고 세션이 끝날 때까지 계속 기록합니다. `1.0`은 오류가 있는 모든 세션을 캡처하고, `0`은 아무것도 캡처하지 않습니다. |

다음 항목은 `replayIntegration({})`의 통합 옵션으로 설정할 수 있습니다:

| Key                      | Type                     | Default     | Description                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| stickySession            | `boolean`                | `true`      | 페이지 새로고침과 관계없이 사용자를 계속 추적합니다. 탭을 닫으면 세션이 종료되므로, 한 사용자가 여러 탭을 사용하면 여러 세션으로 기록됩니다.                                                                                                                                                                                          |
| mutationLimit            | `number`                 | 10000       | 성능 영향으로 인해 Session Replay가 기록을 중지하기 전에 처리할 mutation의 상한입니다. [Mutation Limits](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#mutation-limits) 참고                                                                                                  |
| mutationBreadcrumbLimit  | `number`                 | 750         | 큰 mutation을 경고하는 breadcrumb를 Session Replay가 전송하기 전에 처리할 mutation의 상한입니다. [Mutation Limits](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#mutation-limits) 참고                                                                                        |
| minReplayDuration        | `number`                 | 5000        | SDK가 Sentry로 전송을 시작하기 전 replay 길이(**밀리초**)입니다. 최대값은 15000입니다. **참고:** 이 옵션은 세션 기반 샘플링(`replaysSessionSampleRate`)에만 적용됩니다. 오류/버퍼 기반 샘플링(`replaysOnErrorSampleRate`)의 경우, 오류가 샘플링되면 replay가 즉시 캡처됩니다. |
| maxReplayDuration        | `number`                 | 3600000     | SDK가 Sentry로 전송할 replay의 최대 길이(**밀리초**)입니다. 최대값은 3600000(1시간)입니다.                                                                                                                                                                                                                                       |
| workerUrl                | `string`                 | `undefined` | Replay 데이터 압축을 위한 self-hosted worker URL입니다. 자세한 내용은 [Using a Custom Compression Worker](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#using-a-custom-compression-worker)를 참고하세요.                                                                      |
| networkDetailAllowUrls   | `(string\|RegExp)[]`     | `[]`        | 지정된 URL과 일치하는 XHR 및 fetch 요청의 요청/응답 세부 정보를 캡처합니다.                                                                                                                                                                                                                 |
| networkDetailDenyUrls    | `(string\|RegExp)[]`     | `[]`        | 이 URL들의 요청/응답 세부 정보는 캡처하지 않습니다. `networkDetailAllowUrls`보다 우선합니다.                                                                                                                                                                                              |
| networkCaptureBodies     | `boolean`                | `true`      | `networkDetailAllowUrls`에 정의된 URL에 대해 요청/응답 본문을 캡처할지 결정합니다.                                                                                                                                                                                                         |
| networkRequestHeaders    | `string[]`               | `[]`        | `networkDetailAllowUrls`에 정의된 URL에 대해 캡처할 추가 요청 헤더입니다. 자세한 내용은 [Network Details](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details)를 참고하세요.                                                                                         |
| networkResponseHeaders   | `string[]`               | `[]`        | `networkDetailAllowUrls`에 정의된 URL에 대해 캡처할 추가 응답 헤더입니다. 자세한 내용은 [Network Details](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details)를 참고하세요.                                                                                         |
| beforeAddRecordingEvent  | `(event) => event\|null` | `i => i`    | console log 및 네트워크 요청/응답을 포함한 추가 기록 이벤트를 필터링합니다.                                                                                                                                                                                                               |
| beforeErrorSampling      | `(event) => boolean`     | `i => true` | 오류 샘플링에서 건너뛸 오류 이벤트를 필터링합니다. 이 오류 이벤트에 대해 샘플링을 건너뛰려면 `false`, 샘플링하려면 `true`를 반환하세요. `buffer` 모드에서만 호출됩니다.                                                                                                                       |
| slowClickIgnoreSelectors | `string[]`               | `[]`        | 지정된 CSS selector와 일치하는 요소에서는 느린 클릭/분노 클릭 감지를 무시합니다.                                                                                                                                                                                                           |

## [개인정보 보호 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#privacy-configuration)

저희는 개인정보 보호를 중요하게 생각하므로, 개인정보 보호 중심 설정을 여러 가지 제공합니다. 이에 대한 자세한 내용은 [Session Replay privacy documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)에서 확인하세요.

개인 식별 정보나 기타 비공개 데이터가 없는 정적 웹사이트에서 작업 중이라면, `maskAllText`와 `blockAllMedia` 구성 옵션을 각각 설정해 기본 텍스트 마스킹과 이미지 차단을 해제할 수 있습니다:

```javascript
Sentry.replayIntegration({
  // NOTE: This will disable built-in masking. Only use this if your site has no sensitive data, or if you've already set up other options for masking or blocking relevant data, such as 'ignore', 'block', 'mask' and 'maskFn'.
  maskAllText: false,
  blockAllMedia: false,
});
```

v8부터 `unblock` 및 `unmask` 옵션은 더 이상 기본 DOM selector를 추가하지 않습니다. 이전 버전의 기본 동작을 유지하려면 구성에서 이를 명시적으로 지정해야 합니다:

```javascript
Sentry.replayIntegration({
  unblock: [".sentry-unblock, [data-sentry-unblock]"],
  unmask: [".sentry-unmask, [data-sentry-unmask]"],
});
```

다음은 `replayIntegration({})`에서 사용할 수 있는 전체 옵션 목록입니다:

| key           | type                       | default                                      | description                                                                                                                                                                                                                                                              |
| ------------- | -------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mask          | `string[]`                 | `['.sentry-mask', '[data-sentry-mask]']`     | 지정된 DOM selector와 일치하는 모든 요소를 마스킹합니다. 예시는 [Masking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#masking) 섹션을 참고하세요. 구성한 selector는 기본값에 *추가로* 적용됩니다. |
| maskAllText   | `boolean`                  | `true`                                       | *모든* 텍스트 콘텐츠를 마스킹합니다. 서버로 전송하기 전에 텍스트 콘텐츠를 `maskFn`으로 처리합니다.                                                                                                                                                                          |
| maskAllInputs | `boolean`                  | `true`                                       | `<input>` 요소의 값을 마스킹합니다. 서버로 전송하기 전에 입력 값을 `maskFn`으로 처리합니다.                                                                                                                                                                                 |
| block         | `string[]`                 | `['.sentry-block', '[data-sentry-block]']`   | DOM selector와 일치하는 모든 요소를 편집해 제거합니다. 예시는 [Blocking](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#blocking) 섹션을 참고하세요. 구성한 selector는 기본값에 *추가로* 적용됩니다. |
| blockAllMedia | `boolean`                  | `true`                                       | *모든* 미디어 요소(`img`, `svg`, `video`, `object`, `picture`, `embed`, `map`, `audio`)를 차단합니다.                                                                                                                                                                       |

| ignore        | `string[]`                 | `['.sentry-ignore', '[data-sentry-ignore]']` | 일치하는 입력 필드의 모든 이벤트를 무시합니다. 예시는 위의 [Ignoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#ignoring)을 참고하세요. |
| maskFn        | `(text: string) => string` | `(s) => '*'.repeat(s.length)`                | 서버로 전송하기 전에 텍스트 콘텐츠를 어떻게 마스킹할지 커스터마이즈하는 함수입니다. 기본적으로 텍스트를 `*`로 마스킹합니다. |
| unblock       | `string[]`                 | `[]`                                         | DOM 선택자와 일치하는 요소를 레드랙트하지 않습니다. `blockAllMedia`로 차단된 특정 미디어 요소를 해제할 때 사용합니다. 이는 `password` 같은 민감한 요소에는 영향을 주지 않습니다. |
| unmask        | `string[]`                 | `[]`                                         | 지정한 DOM 선택자와 일치하는 모든 요소의 마스킹을 해제합니다. `maskAllText`로 마스킹된 특정 요소의 마스킹을 해제할 때 사용합니다. |

- [샘플링](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#sampling)

세션 샘플링이 동작하는 방식에 대해 더 알아보려면 [Default Session Initialization](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#default-session-initialization) 문서를 확인하세요.

- [네트워크 상세 정보](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details)

기본적으로 Replay는 애플리케이션의 모든 outgoing fetch 및 XHR 요청에 대한 기본 정보를 수집합니다. 여기에는 URL, 요청/응답 본문 크기, 메서드, 상태 코드가 포함됩니다. 목적은 비공개 데이터가 수집될 가능성을 줄이는 것입니다.

요청/응답 헤더나 본문 같은 추가 정보를 수집하려면 `networkDetailAllowUrls`를 통해 옵트인해야 합니다(SDK 버전 >= [7.50.0](https://github.com/getsentry/sentry-javascript/releases/tag/7.50.0) 필요). 이렇게 하면 본문 수집이 안전한 URL만 선택적으로 추가하고, 개인 식별 정보(PII)를 포함할 수 있는 엔드포인트는 제외할 수 있습니다.

본문 콘텐츠는 객체 키와 값을 기준으로 서버 측에서 PII 정제 처리됩니다. 자세한 내용은 [Replay Privacy section](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#network-request-and-response-bodies-and-headers)을 참고하세요.

주어진 패턴과 일치하는 모든 URL은 다음과 같이 추가 상세 정보와 함께 수집됩니다:

```javascript
replayIntegration({
  networkDetailAllowUrls: [window.location.origin],
});
```

문자열을 전달하면 해당 문자열을 포함하는 모든 URL과 매칭됩니다. 정확하거나 더 복잡한 매칭은 정규식을 사용할 수 있습니다.

설정한 패턴과 일치하는 URL로의 요청은 요청/응답 본문과 함께, 아래 기본 헤더가 추가로 포함됩니다:

* `Content-Type`
* `Content-Length`
* `Accept`

추가 헤더를 수집하려면 `networkRequestHeaders` 및 `networkResponseHeaders` 옵션으로 설정해야 합니다. 예:

```javascript
replayIntegration({
  networkDetailAllowUrls: [
    window.location.origin,
    "api.example.com",
    /^https:\/\/api\.example\.com/,
  ],

  networkRequestHeaders: ["Cache-Control"],
  networkResponseHeaders: ["Referrer-Policy"],

});
```

수집된 본문은 최대 150k자까지로 잘립니다.

## [사용자 식별](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#identifying-users)

Sentry SDK를 사용해 사용자를 세션에 연결하고, 이벤트에 사용자 정보를 추가하여 이슈를 겪는 사용자를 식별할 수 있습니다. Sentry 이벤트에 사용자를 설정하는 방법은 [setUser](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setUser)를 참고하세요.

```javascript
Sentry.setUser({ email: "jane.doe@example.com" });
```

## [커스텀 압축 워커 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#using-a-custom-compression-worker)

기본적으로 Session Replay는 네트워크로 전송하기 전에 Replay 데이터를 압축하기 위해 인라인 web worker 스크립트를 사용합니다. 이렇게 하면 전송 데이터 양이 크게 줄어 성능이 향상되고 네트워크 오버헤드가 감소합니다. 데이터 압축은 CPU 집약적이므로, 이 작업을 별도 스레드로 오프로딩하기 위해 web worker를 사용합니다.

인라인 워커는 대부분의 애플리케이션에서 잘 동작하지만, 다음 두 가지 주요 문제가 있습니다:

1. 워커 코드가 인라인되어 있으므로 애플리케이션의 메인 번들 크기가 증가합니다.
2. 애플리케이션에 매우 엄격한 CSP 정책이 있으면 인라인 워커 사용 시 CSP 위반이 발생할 수 있습니다. 자세한 내용은 [CSP](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#content-security-policy-csp) 문서를 참고하세요.

이 문제를 해결하기 위해 커스텀 워커 스크립트를 사용할 수 있습니다. 이렇게 하면 워커 스크립트를 자체 도메인에서 호스팅해 인라인 워커 관련 CSP 이슈를 피할 수 있습니다. 또한 워커 스크립트를 메인 애플리케이션 번들에서 제거하고 별도로 서빙 및 캐싱할 수 있습니다.

커스텀 압축 워커를 사용하려면 다음 단계를 따르세요:

1. GitHub 저장소에서 [example worker script](https://github.com/getsentry/sentry-javascript/blob/develop/packages/replay-worker/examples/worker.min.js)를 다운로드합니다.
2. 이 워커 스크립트를 애플리케이션과 동일한 도메인에 호스팅합니다. 예를 들어 애플리케이션이 `https://example.com`에서 호스팅된다면, 워커 스크립트는 `https://example.com/assets/worker.min.js`에 둘 수 있습니다.
3. Replay에서 커스텀 워커 스크립트를 설정합니다:

```javascript
replayIntegration({
  workerUrl: "/assets/worker.min.js",
});
```

4. (선택 사항) 번들 크기를 줄이기 위해 이제 기본 포함 워커 스크립트를 [Tree Shake](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md)할 수 있습니다. [Sentry Bundler Plugins](https://github.com/getsentry/sentry-javascript-bundler-plugins)(버전 2.10.0 이상)을 사용 중이라면:

```javascript
sentryPlugin({
  // other config
  bundleSizeOptimizations: {
    excludeReplayWorker: true,
  },
});
```

이 스크립트는 직접 호스팅하므로 최신 상태를 유지할 책임도 사용자에게 있습니다. 워커 스크립트 업데이트를 주기적으로 확인하고 필요 시 업데이트하는 것을 권장합니다. 워커 스크립트 API는 메이저 버전 내에서 안정성이 보장되므로, 모든 v7 워커 스크립트는 모든 v7 SDK 버전과 하위/상위 호환됩니다. 다만 워커 스크립트에 개선이나 버그 수정이 있을 수 있으며, 업데이트하지 않으면 이를 적용받지 못할 수 있습니다.

## [Mutation 한도](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#mutation-limits)

Session Replay는 웹 애플리케이션에서 발생하는 점진적 DOM 변경을 기록하는 방식으로 동작합니다. 일반적으로 이러한 변경은 작은 배치로 발생하며 오버헤드도 최소입니다. 하지만 한 번의 업데이트에서 대량의 DOM mutation이 발생하는 케이스를 놓치기 쉽습니다. 예를 들어 렌더링할 옵션 목록이 무제한인 커스텀 드롭다운 컴포넌트가 있습니다. 이는 Session Replay가 없어도 성능에 부정적 영향을 줄 수 있으며, Session Replay를 활성화하면 영향이 더 커집니다. 이런 시나리오를 피하기 위해 Session Replay는 많은 mutation(기본값: 10,000)을 감지하면 기록을 중단하며, 이 값은 `mutationLimit`으로 설정할 수 있습니다. 또한 많은 mutation이 감지되면 경고를 표시하도록 replay에 breadcrumb(기본값: 750)를 제공합니다.

```javascript
replayIntegration({
  mutationBreadcrumbLimit: 1000,
  mutationLimit: 1500,
});
```

## [커스텀 breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#custom-breadcrumbs)

SDK를 사용하면 커스텀 breadcrumb를 전송할 수 있으며, 이는 기존 breadcrumb와 함께 Replay Details UI에 표시됩니다. 커스텀 breadcrumb 전송 방법은 [문서](https://docs.sentry.io/platforms/javascript/enriching-events/breadcrumbs.md#customize-breadcrumbs)를 참고하세요. 전송한 커스텀 breadcrumb는 Issue Details breadcrumbs UI와 Replay Details breadcrumbs 탭 모두에 반영됩니다.

Replay Details의 모든 커스텀 breadcrumb는 회색으로 표시되며, 터미널 로고로 식별할 수 있습니다.

Replay Details에서는 breadcrumb의 `data` 속성보다 `message`가 우선합니다. `message` 속성이 설정되어 있으면 문자열이 다음과 같이 표시됩니다:

`message`가 설정되어 있지 않으면 기본적으로 breadcrumb는 `data` 속성을 표시합니다. 예:

breadcrumb 제목은 설정한 breadcrumb `category`가 됩니다. `category`가 없으면 breadcrumb `message`를 사용합니다. 그것도 없으면 `description`을 사용합니다. 마지막 폴백은 기본 제목인 "Custom"입니다.

