---
title: '옵션 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options

# 옵션 | Next.js용 Sentry

## [사용 가능한 옵션](https://docs.sentry.io/platforms/javascript/configuration/options.md#available-options)

## [핵심 옵션](https://docs.sentry.io/platforms/javascript/configuration/options.md#core-options)

- [dsn](https://docs.sentry.io/platforms/javascript/configuration/options.md#dsn)

| 유형 | `string` |
| ---- | -------- |

DSN은 SDK가 이벤트를 어디로 전송할지 알려줍니다. 이 값이 설정되지 않으면 SDK는 어떤 이벤트도 전송하지 않습니다. 자세한 내용은 [DSN utilization](https://docs.sentry.io/product/sentry-basics/dsn-explainer.md#dsn-utilization)을 참고하세요.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
});
```

- [orgId](https://docs.sentry.io/platforms/javascript/configuration/options.md#orgId)

| 유형              | `` `${number}` \| number `` |
| ----------------- | --------------------------- |
| 사용 가능 환경    | `Server`                    |

Sentry 프로젝트의 organization ID입니다.

SDK는 DSN에서 organization ID를 추출하려고 시도합니다. 찾을 수 없거나 값을 재정의해야 하는 경우, 이 옵션으로 ID를 제공할 수 있습니다. organization ID는 trace propagation 및 `strictTraceContinuation` 같은 기능에 사용됩니다.

organization ID는 [strict trace continuation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#strictTraceContinuation) 같은 기능에 사용됩니다.

- [debug](https://docs.sentry.io/platforms/javascript/configuration/options.md#debug)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값  | `false`   |

디버그 모드를 켜거나 끕니다. debug가 활성화되면 SDK가 수행 중인 작업에 대한 유용한 디버깅 정보를 출력하려고 시도합니다.

- [release](https://docs.sentry.io/platforms/javascript/configuration/options.md#release)

| 유형 | `string` |
| ---- | -------- |

릴리스를 설정합니다. 릴리스 이름은 문자열이지만, 일부 형식은 Sentry가 감지하여 다르게 렌더링할 수 있습니다. 릴리스 간 회귀를 알려주고 잠재적 원인을 식별할 수 있도록 릴리스 데이터를 전송하는 방법은 [the releases documentation](https://docs.sentry.io/product/releases.md) 또는 [sandbox](https://sandbox.sentry.io/?scenario=releases\&projectSlug=react\&source=docs)에서 확인하세요.

서버에서는 SDK가 `SENTRY_RELEASE` 환경 변수에서 이 값을 읽으려고 시도합니다.

브라우저에서는 가능할 경우 SDK가 `window.SENTRY_RELEASE.id`에서 이 값을 읽으려고 시도합니다.

- [environment](https://docs.sentry.io/platforms/javascript/configuration/options.md#environment)

| 유형    | `string`     |
| ------- | ------------ |
| 기본값  | `production` |

환경을 설정합니다. 애플리케이션이 패키징되었는지 여부에 따라 기본값은 `development` 또는 `production`입니다.

환경은 오류가 발생한 위치가 프로덕션 시스템인지, 스테이징 서버인지, 또는 그 외의 위치인지 알려줍니다.

Sentry는 environment 파라미터가 설정된 이벤트를 수신하면 자동으로 환경을 생성합니다.

환경은 대소문자를 구분합니다. 환경 이름에는 줄바꿈, 공백, 슬래시(`/`)를 포함할 수 없고, "None" 문자열일 수 없으며, 64자를 초과할 수 없습니다. 환경은 삭제할 수 없지만 숨길 수는 있습니다.

- [tunnel](https://docs.sentry.io/platforms/javascript/configuration/options.md#tunnel)

| 유형 | `string` |
| ---- | -------- |

수집된 이벤트를 전송할 때 사용할 URL을 설정합니다. 이 옵션은 광고 차단기를 우회하거나 Sentry로 전송되는 이벤트를 더 세밀하게 제어할 때 사용할 수 있습니다. 생성되는 Sentry 데이터에 필요한 속성을 설정하려면 이 옵션을 사용하더라도 DSN을 추가해야 합니다. 이 옵션은 **커스텀 서버 엔드포인트 구현이 필요**합니다. 자세한 내용과 예시는 [Dealing with Ad-Blockers](https://docs.sentry.io/platforms/javascript/troubleshooting.md#dealing-with-ad-blockers)를 참고하세요.

- [sendDefaultPii](https://docs.sentry.io/platforms/javascript/configuration/options.md#sendDefaultPii)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값  | `false`   |

기본 PII 데이터를 Sentry로 전송하려면 이 옵션을 `true`로 설정하세요. 이 옵션을 활성화하면 무엇보다 이벤트에서 IP 주소 자동 수집이 활성화됩니다.

- [maxBreadcrumbs](https://docs.sentry.io/platforms/javascript/configuration/options.md#maxBreadcrumbs)

| 유형    | `number` |
| ------- | -------- |
| 기본값  | `100`    |

이 변수는 수집할 breadcrumb의 총량을 제어합니다. Sentry에는 [maximum payload size](https://develop.sentry.dev/sdk/data-model/envelopes/#size-limits)가 있으며, 이 크기를 초과하는 이벤트는 폐기된다는 점에 유의하세요.

- [attachStacktrace](https://docs.sentry.io/platforms/javascript/configuration/options.md#attachStacktrace)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값  | `false`   |

활성화하면 기록되는 모든 메시지에 스택 트레이스가 자동으로 첨부됩니다. 예외에는 항상 스택 트레이스가 첨부되지만, 이 옵션을 설정하면 메시지에도 스택 트레이스가 함께 전송됩니다. 예를 들어 `Sentry.captureMessage()`로 수집한 모든 메시지 옆에 스택 트레이스가 표시됩니다.

Sentry의 그룹화는 스택 트레이스가 있는 이벤트와 없는 이벤트에서 다르게 동작합니다. 따라서 특정 이벤트에 대해 이 플래그를 켜거나 끄면 새로운 그룹이 생성됩니다.

- [serverName](https://docs.sentry.io/platforms/javascript/configuration/options.md#serverName)

| 유형              | `string` |
| ----------------- | -------- |
| 사용 가능 환경    | `Server` |

이 옵션으로 서버 이름을 제공할 수 있습니다. 값이 제공되면 서버 이름이 함께 전송되어 이벤트에 저장됩니다. 많은 통합에서 서버 이름은 실제로 서버가 아닌 장비에서도 장치 호스트명에 해당합니다.

대부분의 SDK는 이 값을 자동으로 탐지하려고 시도합니다.

- [initialScope](https://docs.sentry.io/platforms/javascript/configuration/options.md#initialScope)

| 유형 | `CaptureContext` |
| ---- | ---------------- |

초기 스코프에 설정할 데이터입니다. 아래와 같이 초기 스코프는 객체 또는 콜백 함수로 정의할 수 있습니다.

```javascript
// Using an object
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  initialScope: {
    tags: { "my-tag": "my value" },
    user: { id: 42, email: "john.doe@example.com" },
  },
});

// Using a callback function
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  initialScope: (scope) => {
    scope.setTags({ a: "b" });
    return scope;
  },
});
```

- [maxValueLength](https://docs.sentry.io/platforms/javascript/configuration/options.md#maxValueLength)

| 유형 | `number` |
| ---- | -------- |

Sentry로 전송되는 이벤트의 각 문자열 속성이 잘리기 전까지 가질 수 있는 최대 문자 수입니다.

- [normalizeDepth](https://docs.sentry.io/platforms/javascript/configuration/options.md#normalizeDepth)

| 유형    | `number` |
| ------- | -------- |
| 기본값  | `3`      |

Sentry SDK는 모든 컨텍스트 데이터를 지정된 깊이까지 정규화합니다. 이 깊이를 넘는 데이터는 트리를 더 이상 순회하지 않고 타입 표시(`[Object]` 또는 `[Array]`)로 잘려 표시됩니다. 기본적으로 3단계 깊이까지 순회합니다.

- [normalizeMaxBreadth](https://docs.sentry.io/platforms/javascript/configuration/options.md#normalizeMaxBreadth)

| 유형    | `number` |
| ------- | -------- |
| 기본값  | `1000`   |

SDK가 컨텍스트 데이터를 정규화할 때, 각 객체 또는 배열에 포함할 속성 또는 항목의 최대 개수입니다. 이 범위를 넘는 데이터는 버려집니다.

- [enabled](https://docs.sentry.io/platforms/javascript/configuration/options.md#enabled)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값  | `true`    |

이 SDK가 Sentry로 이벤트를 전송할지 여부를 지정합니다. `enabled: false`로 설정해도 Sentry 계측으로 인한 모든 오버헤드가 사라지지는 않습니다. 환경에 따라 Sentry를 완전히 비활성화하려면 `Sentry.init`을 조건부로 호출하세요.

- [sendClientReports](https://docs.sentry.io/platforms/javascript/configuration/options.md#sendClientReports)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값  | `true`    |

클라이언트 리포트 전송을 비활성화하려면 이 옵션을 `false`로 설정하세요. 클라이언트 리포트는 클라이언트가 자신의 상태 리포트를 Sentry로 전송할 수 있게 해주는 프로토콜 기능입니다. 현재는 주로 실제로 전송되지 않은 이벤트의 outcome을 내보내는 데 사용됩니다.

- [includeLocalVariables](https://docs.sentry.io/platforms/javascript/configuration/options.md#includeLocalVariables)

| 유형              | `boolean` |
| ----------------- | --------- |
| 기본값            | `false`   |
| 사용 가능 환경    | `Server`  |

스택 트레이스에 스택 로컬 변수를 추가하려면 이 옵션을 `true`로 설정하세요.

고급 구성 옵션은 [Local Variables integration options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md) 문서를 참고하세요.

- [integrations](https://docs.sentry.io/platforms/javascript/configuration/options.md#integrations)

| 유형    | `Array<Integration> \| (integrations: Array<Integration>) => Array<Integration>` |
| ------- | -------------------------------------------------------------------------------- |
| 기본값  | `[]`                                                                             |

SDK와 함께 초기화해야 하는 추가 통합을 전달합니다. 통합은 SDK 기능을 확장하는 데 사용할 수 있는 코드 조각입니다. 커스텀 이벤트 프로세서, 컨텍스트 제공자를 추가하거나 SDK 라이프사이클에 훅을 걸 때 사용할 수 있습니다.

자세한 내용은 [integration docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md)를 참고하세요.

- [defaultIntegrations](https://docs.sentry.io/platforms/javascript/configuration/options.md#defaultIntegrations)

| 유형 | `undefined \| false` |
| ---- | -------------------- |

기본으로 추가되는 통합을 비활성화할 때 사용할 수 있습니다. `false`로 설정하면 기본 통합이 추가되지 않습니다.

기본 통합을 수정하는 방법은 [integration docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

- [beforeBreadcrumb](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeBreadcrumb)

| 유형 | `(breadcrumb: Breadcrumb, hint?: BreadcrumbHint) => Breadcrumb \| null` |
| ---- | ----------------------------------------------------------------------- |

breadcrumb가 스코프에 추가되기 전에 breadcrumb 객체와 함께 이 함수가 호출됩니다. 함수에서 아무것도 반환하지 않으면 breadcrumb는 폐기됩니다. breadcrumb를 그대로 전달하려면 breadcrumb 객체를 담고 있는 첫 번째 인자를 반환하세요. 콜백은 두 번째 인자("hint")도 받는데, 여기에는 breadcrumb가 생성된 원본 객체가 들어 있어 breadcrumb 모양을 추가로 커스터마이즈할 수 있습니다.

- [transport](https://docs.sentry.io/platforms/javascript/configuration/options.md#transport)

| 유형 | `(transportOptions: TransportOptions) => Transport` |
| ---- | --------------------------------------------------- |

JavaScript SDK는 이벤트를 Sentry로 전송하기 위해 transport를 사용합니다. 최신 브라우저에서 대부분의 transport는 브라우저의 fetch API를 사용해 이벤트를 전송합니다. 연결이 없어 전송에 실패하면 transport는 이벤트를 폐기합니다.

브라우저에서는 기본적으로 `fetch` 기반 transport가 사용됩니다.

서버에서는 기본적으로 `https` 기반 transport가 사용됩니다.

- [transportOptions](https://docs.sentry.io/platforms/javascript/configuration/options.md#transportOptions)

| 유형 | `TransportOptions` |
| ---- | ------------------ |

transport를 구성할 때 사용하는 옵션입니다. 다음과 같은 선택적 키를 가질 수 있는 객체입니다.

**node `httpTransport` transport 옵션:**

* `headers`: 모든 요청과 함께 전송할 헤더를 담은 객체.
* `proxy`: 아웃바운드 요청에 사용할 프록시. http 또는 https 사용 가능.
* `caCerts`: CA 인증서 경로 또는 경로 목록, 혹은 CA 인증서 버퍼.
* `httpModule`: 요청에 사용할 커스텀 HTTP 모듈. 기본값은 네이티브 `http` 및 `https` 모듈.
* `keepAlive`: 요청 사이에 소켓을 유지할지 여부를 결정합니다. 기본값은 `false`.

**브라우저 `fetch` transport 옵션:**

* `headers`: 모든 요청과 함께 전송할 헤더를 담은 객체입니다.
* `fetchOptions`: `fetch` 호출에 전달할 옵션을 담은 객체입니다. SDK의 fetch 전송 계층에서 사용됩니다.

- [shutdownTimeout](https://docs.sentry.io/platforms/javascript/configuration/options.md#shutdownTimeout)

| Type              | `number` |
| ----------------- | -------- |
| Default           | `2000`   |
| Only available on | `Server` |

종료 전에 얼마나 오래 대기할지(초)를 제어합니다. Sentry SDK는 백그라운드 큐에서 이벤트를 전송합니다. 이 큐에는 대기 중인 이벤트를 비울 수 있도록 일정 시간이 주어집니다. 기본값은 SDK마다 다르지만 일반적으로 약 2초입니다. 이 값을 너무 낮게 설정하면 커맨드라인 애플리케이션에서 이벤트 전송에 문제가 생길 수 있습니다. 값을 너무 높게 설정하면 네트워크 연결 문제가 있는 사용자 환경에서 애플리케이션이 오랫동안 블로킹될 수 있습니다.

- [disableInstrumentationWarnings](https://docs.sentry.io/platforms/javascript/configuration/options.md#disableInstrumentationWarnings)

| Type              | `boolean` |
| ----------------- | --------- |
| Default           | `false`   |
| Only available on | `Server`  |

설정 방식에 따라 Sentry SDK는 올바르지 않게 설정되었는지 감지하려고 시도합니다. 이로 인해 다음과 같은 경고가 기록될 수 있습니다.

> \[Sentry] < libraryName > is not instrumented. This is likely because you required/imported < libraryName > before calling `Sentry.init()`.

또는

> \[Sentry] < libraryName > is not instrumented. Please make sure to initialize Sentry in a separate file that you \`--import\` when running node, see: < docs link >.

이는 SDK가 해당 라이브러리가 자동 성능 계측을 위해 래핑되지 않았다고 감지했다는 의미입니다. 그 결과 일부 스팬이 올바르게 보고되지 않을 수 있습니다. 이 문제가 영향이 없다면(예: 경고가 false positive이거나 해당 특정 스팬이 중요하지 않은 경우) 이 옵션을 `true`로 설정해 경고를 비활성화할 수 있습니다.

## [Error Monitoring Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#error-monitoring-options)

- [sampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#sampleRate)

| Type    | `number` |
| ------- | -------- |
| Default | `1.0`    |

오류 이벤트의 샘플링 비율을 `0.0`~`1.0` 범위에서 설정합니다. 기본값은 `1.0`이며, 이는 오류 이벤트의 100%가 전송됨을 의미합니다. `0.1`로 설정하면 오류 이벤트의 10%만 전송됩니다. 이벤트는 무작위로 선택됩니다.

- [beforeSend](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSend)

| Type | `(event: Event, hint: EventHint) => Event \| null` |
| ---- | -------------------------------------------------- |

이 함수는 SDK별 메시지 또는 오류 이벤트 객체를 인자로 받아, 수정된 이벤트 객체를 반환하거나 이벤트 보고를 건너뛰기 위해 `null`을 반환할 수 있습니다. 예를 들어 전송 전에 수동으로 PII를 제거하는 데 사용할 수 있습니다.

`beforeSend`가 실행될 시점에는 모든 스코프 데이터가 이미 이벤트에 적용된 상태입니다. 이후 스코프를 추가로 수정해도 효과가 없습니다.

- [enhanceFetchErrorMessages](https://docs.sentry.io/platforms/javascript/configuration/options.md#enhanceFetchErrorMessages)

| Available since | `10.34.0`                            |
| --------------- | ------------------------------------ |
| Type            | `'always' \| 'report-only' \| false` |
| Default         | `always`                             |

요청의 호스트네임을 덧붙여 fetch 오류 메시지를 강화할지 제어합니다. 활성화하면 "Failed to fetch" 같은 일반적인 fetch 오류가 호스트네임을 포함하도록 강화되어(예: "Failed to fetch (example.com)") Sentry에서 더 나은 컨텍스트를 제공합니다.

사용 가능한 옵션:

* `'always'` (기본값): 실제 오류 메시지를 직접 수정합니다. 이 경우 정확한 메시지 일치에 의존하는 서드파티 패키지(예: `is-network-error`, `p-retry`)가 깨질 수 있습니다.
* `'report-only'`: Sentry로 전송할 때만 메시지를 강화합니다. 원본 오류 메시지는 변경되지 않아, 오류 메시지를 확인하는 서드파티 패키지와의 호환성을 유지합니다.
* `false`: 호스트네임 강화 기능을 완전히 비활성화합니다.

- [ignoreErrors](https://docs.sentry.io/platforms/javascript/configuration/options.md#ignoreErrors)

| Type    | `Array<string \| RegExp>` |
| ------- | ------------------------- |
| Default | `[]`                      |

Sentry로 전송하지 않을 오류 메시지와 일치하는 문자열 또는 정규식 패턴 목록입니다. 이 문자열/정규식과 일치하는 메시지는 Sentry로 전송되기 전에 필터링됩니다. 문자열을 사용할 경우 부분 일치도 필터링되므로, 정확히 일치하는 항목만 필터링하려면 정규식 패턴을 사용하세요. 기본적으로 모든 오류가 전송됩니다.

- [denyUrls](https://docs.sentry.io/platforms/javascript/configuration/options.md#denyUrls)

| Type              | `Array<string \| RegExp>` |
| ----------------- | ------------------------- |
| Default           | `[]`                      |
| Only available on | `Client`                  |

오류가 생성된 스크립트 URL과 일치하는 문자열 또는 정규식 패턴 배열입니다. 이 URL에서 생성된 오류는 Sentry로 전송되지 않습니다. 이 옵션을 사용하면 최상위 스택 프레임 파일 URL이 `denyUrls` 배열의 항목 하나 이상을 포함하거나 일치할 때 해당 오류는 전송되지 않습니다. 배열의 문자열 항목은 모두 `stackFrameUrl.contains(entry)`로 매칭되고, RegEx 항목은 모두 `stackFrameUrl.match(entry)`로 매칭됩니다.

이 옵션은 오류가 보고된 HTTP URL이 아니라 스택 트레이스의 소스 파일 URL을 확인합니다. 더 세밀한 필터링은 [beforeSend](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#beforeSend)를 참고하세요.

이 매칭 로직은 raw message 이벤트가 아니라 캡처된 예외에 적용됩니다. 기본적으로 모든 오류가 전송됩니다.

- [allowUrls](https://docs.sentry.io/platforms/javascript/configuration/options.md#allowUrls)

| Type              | `Array<string \| RegExp>` |
| ----------------- | ------------------------- |
| Default           | `[]`                      |
| Only available on | `Client`                  |

오류가 생성된 스크립트 URL과 일치하는 문자열 또는 정규식 패턴 배열입니다. 이 URL에서 생성된 오류만 Sentry로 전송됩니다. 이 옵션을 사용하면 최상위 스택 프레임 파일 URL이 allowUrls 배열의 항목 하나 이상을 포함하거나 일치할 때만 오류가 전송됩니다. 배열의 문자열 항목은 모두 `stackFrameUrl.contains(entry)`로 매칭되고, RegEx 항목은 모두 `stackFrameUrl.match(entry)`로 매칭됩니다.

예를 들어 배열에 `'foo.com'`을 추가하면 URL의 마지막 세그먼트에 `foo.com`이 포함되어 있으므로 `https://bar.com/myfile/foo.com`에서 생성된 오류가 캡처됩니다. URL 매칭은 "contains" 로직을 사용하기 때문입니다.

이 매칭 로직은 raw message 이벤트가 아니라 캡처된 예외에 적용됩니다. 기본적으로 모든 오류가 전송됩니다.

스크립트가 `cdn.example.com`에서 로드되고 사이트가 `example.com`인 경우, 해당 위치의 스크립트에서 생성된 오류만 선택적으로 캡처하도록 `allowUrls`를 다음과 같이 설정할 수 있습니다.

```javascript
Sentry.init({
  allowUrls: [/https?:\/\/((cdn|www)\.)?example\.com/],
});
```

## [Tracing Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracing-options)

- [tracesSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracesSampleRate)

| Type | `number` |
| ---- | -------- |

`0`에서 `1` 사이의 숫자로, 특정 트랜잭션이 Sentry로 전송될 확률(퍼센트)을 제어합니다. (`0`은 0%, `1`은 100%를 의미합니다.) 앱에서 생성되는 모든 트랜잭션에 동일하게 적용됩니다. 트레이싱을 활성화하려면 이 옵션 또는 `tracesSampler` 중 하나를 반드시 정의해야 합니다.

- [tracesSampler](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracesSampler)

| Type | `(samplingContext: SamplingContext) => number \| boolean` |
| ---- | --------------------------------------------------------- |

특정 트랜잭션이 Sentry로 전송될 확률(퍼센트)을 결정하는 함수입니다. 트랜잭션 정보와 생성 컨텍스트가 자동으로 전달되며, 함수는 `0`(전송 확률 0%)과 `1`(전송 확률 100%) 사이의 숫자를 반환해야 합니다. 원치 않는 트랜잭션에 대해 0을 반환해 필터링하는 용도로도 사용할 수 있습니다. 트레이싱을 활성화하려면 이 옵션 또는 `tracesSampleRate` 중 하나를 반드시 정의해야 합니다.

함수에 전달되는 `samplingContext` 객체는 다음 속성을 가집니다.

* `parentSampled`: 부모 트랜잭션의 샘플링 결정입니다. 부모 트랜잭션이 샘플링되었으면 `true`, 아니면 `false`입니다.
* `name`: 스팬 시작 시의 이름입니다.
* `attributes`: 스팬의 초기 속성입니다.
  <!-- -->
  * `normalizedRequest`: 해당되는 경우, 현재 활성화된 HTTP 서버 요청의 요청 정보입니다.

- [tracePropagationTargets](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracePropagationTargets)

| Type | `Array<string \| RegExp>` |
| ---- | ------------------------- |

어떤 다운스트림 서비스가 트레이싱 데이터를 받을지 제어하는 선택적 속성입니다. 트레이싱 데이터는 모든 아웃바운드 HTTP 요청에 첨부되는 `sentry-trace` 및 `baggage` 헤더 형태로 전달됩니다.

이 옵션에는 아웃바운드 요청 URL과 매칭할 문자열 또는 정규식 목록을 넣을 수 있습니다. 목록 항목 중 하나가 아웃바운드 요청 URL과 일치하면 해당 요청에 trace 데이터가 첨부됩니다. 문자열 항목은 전체 일치일 필요가 없으며, 옵션에 제공한 문자열을 요청 URL이 *포함*하면 매칭됩니다.

브라우저에서는 기본적으로 동일 출처로 향하는 모든 아웃바운드 요청에 전파됩니다.

서버에서는 기본적으로 모든 아웃바운드 요청에 전파됩니다.

트레이스 전파를 비활성화하려면 이 옵션을 `[]`로 설정하면 됩니다.

- [strictTraceContinuation](https://docs.sentry.io/platforms/javascript/configuration/options.md#strictTraceContinuation)

| Type              | `boolean` |
| ----------------- | --------- |
| Default           | `false`   |
| Only available on | `Server`  |

`true`로 설정하면 SDK는 `baggage` 헤더에서 찾은 들어오는 트레이스의 organization ID가 현재 Sentry 클라이언트의 organization ID와 일치할 때만 트레이스를 이어갑니다.

클라이언트의 organization ID는 DSN에서 추출되거나 [`orgId` option](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#orgId)으로 설정할 수 있습니다.

organization ID가 일치하지 않으면 SDK는 들어오는 트레이스를 이어가지 않고 새 트레이스를 시작합니다. 이는 알 수 없는 서드파티 서비스의 트레이스가 애플리케이션에서 이어지는 것을 방지하는 데 유용합니다.

- [beforeSendTransaction](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendTransaction)

| Type | `(event: TransactionEvent, hint: EventHint) => TransactionEvent \| null` |
| ---- | ------------------------------------------------------------------------ |

이 함수는 트랜잭션 이벤트 객체를 인자로 받아, 수정된 트랜잭션 이벤트 객체를 반환하거나 이벤트 보고를 건너뛰기 위해 `null`을 반환할 수 있습니다. 예를 들어 전송 전에 수동으로 PII를 제거하는 데 사용할 수 있습니다.

- [beforeSendSpan](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendSpan)

| Type | `(span: SpanJSON) => SpanJSON` |
| ---- | ------------------------------ |

이 함수는 직렬화된 스팬 객체를 인자로 받아 수정된 스팬 객체를 반환할 수 있습니다. 스팬에서 PII를 수동으로 제거할 때 유용할 수 있습니다. 이 함수는 루트 스팬과 모든 자식 스팬에 대해 호출됩니다. 루트 스팬과 그 자식 스팬 전체를 드롭하려면 [`beforeSendTransaction`](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendTransaction)을 대신 사용하세요.

인수로 받는 `span`은 `Span` 클래스 인스턴스가 아니라 직렬화된 객체라는 점에 유의하세요.

- [ignoreTransactions](https://docs.sentry.io/platforms/javascript/configuration/options.md#ignoreTransactions)

| Type    | `Array<string \| RegExp>` |
| ------- | ------------------------- |
| Default | `[]`                      |

Sentry로 전송하면 안 되는 transaction 이름과 일치하는 문자열 또는 정규식 패턴 목록입니다. 이 문자열이나 정규식과 일치하는 transaction은 Sentry로 전송되기 전에 필터링됩니다. 문자열을 사용할 경우 부분 일치도 필터링되므로, 정확히 일치하는 항목만 필터링해야 한다면 대신 정규식 패턴을 사용하세요. 기본적으로 일반적인 API 헬스 체크 요청에 해당하는 transaction은 필터링됩니다.

- [ignoreSpans](https://docs.sentry.io/platforms/javascript/configuration/options.md#ignoreSpans)

| Available since | `10.2.0`                                                                      |
| --------------- | ----------------------------------------------------------------------------- |
| Type            | `Array<string \| RegExp \| {name?: string \| RegExp, op?: string \| RegExp}>` |
| Default         | `[]`                                                                          |

Sentry로 전송하면 안 되는 span 이름과 일치하는 문자열 또는 정규식 패턴 목록입니다. 문자열을 사용할 경우 부분 일치도 필터링되므로, 정확히 일치하는 항목만 필터링해야 한다면 대신 정규식 패턴을 사용하세요. 또한 `name` 및 `op` 속성이 있는 객체를 제공해 span 이름과 operation 이름을 함께 매칭할 수 있습니다. 이때 최소한 `name` 또는 `op` 중 하나는 반드시 제공해야 합니다.

루트 span이 지정된 패턴 중 하나와 일치하면 해당 로컬 trace 전체가 폐기됩니다. 자식 span이 일치하면, 그 자식들의 부모는 폐기된 span의 부모 span으로 재지정됩니다.

기본적으로 무시되는 span은 없습니다.

시작에 도움이 되도록, 자주 사용되는 span에 대한 사전 정의된 매칭은 다음과 같습니다:

```javascript
Sentry.init({
  ignoreSpans: [
    // Browser connection events
    { op: /^browser\.(cache|connect|DNS)$/ },

    // Fonts
    { op: "resource.other", name: /.+\.(woff2|woff|ttf|eot)$/ },

    // CSS files
    { op: "resource.link", name: /.+\.css.*$/ },

    // JS files
    { op: /resource\.(link|script)/, name: /.+\.js.*$/ },

    // Images
    {
      op: /resource\.(other|img)/,
      name: /.+\.(png|svg|jpe?g|gif|bmp|tiff?|webp|avif|heic?|ico).*$/,
    },

    // Measure spans
    { op: "measure" },
  ],
});
```

- [propagateTraceparent](https://docs.sentry.io/platforms/javascript/configuration/options.md#propagateTraceparent)

| Available since | `10.10.0` |
| --------------- | --------- |
| Type            | `boolean` |
| Default         | `false`   |

`true`로 설정하면 SDK가 `fetch` 또는 `XMLHttpRequest`를 통해 발생하는 outbound Http 요청에 [W3C `traceparent` header](https://www.w3.org/TR/trace-context/)를 추가합니다. 이 헤더는 `sentry-trace` 및 `baggage` 헤더에 더해 함께 첨부됩니다. 백엔드 서비스가 예를 들어 OpenTelemetry 또는 기타 W3C Trace Context 호환 라이브러리로 계측되어 있고, 클라이언트에서 trace를 계속 이어가고 싶다면 이 옵션을 `true`로 설정하세요.

**중요:** 백엔드 서비스의 CORS 설정에서 `traceparent` header를 허용하는지 반드시 확인하세요. 그렇지 않으면 요청이 차단될 수 있습니다. [`tracePropagationTargets` option](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracepropagationtargets)을 사용해 어떤 요청에 `traceparent` header를 붙일지 제어하세요. 자세한 내용은 [Dealing with CORS Issues](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md)를 참고하세요.

## [로그 옵션](https://docs.sentry.io/platforms/javascript/configuration/options.md#logs-options)

- [enableLogs](https://docs.sentry.io/platforms/javascript/configuration/options.md#enableLogs)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Sentry에서 로그 수집을 활성화하려면 이 옵션을 `true`로 설정하세요. 이 설정이 활성화된 경우에만 `logger` API가 실제로 로그를 Sentry로 전송합니다.

- [beforeSendLog](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendLog)

| Type | `(log: Log) => Log \| null` |
| ---- | --------------------------- |

이 함수는 log 객체를 인수로 호출되며, 수정된 log 객체를 반환하거나 `null`을 반환해 이 log를 Sentry로 보내지 않도록 할 수 있습니다. 예를 들어 전송 전 수동 PII 제거 또는 모든 로그에 커스텀 속성 추가에 사용할 수 있습니다.

## [세션 리플레이 옵션](https://docs.sentry.io/platforms/javascript/configuration/options.md#session-replay-options)

- [replaysSessionSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#replaysSessionSampleRate)

| Type              | `number` |
| ----------------- | -------- |
| Only available on | `Client` |

기록이 즉시 시작되어 사용자 세션 전체 동안 지속되는 리플레이의 샘플링 비율입니다. `1.0`은 모든 리플레이를 수집하고, `0`은 아무것도 수집하지 않습니다.

- [replaysOnErrorSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#replaysOnErrorSampleRate)

| Type              | `number` |
| ----------------- | -------- |
| Only available on | `Client` |

에러가 발생했을 때 기록되는 리플레이의 샘플링 비율입니다. 이 유형의 리플레이는 에러 이전 최대 1분의 이벤트를 기록하고, 세션이 종료될 때까지 계속 기록합니다. `1.0`은 에러가 있는 모든 세션을 수집하고, `0`은 아무것도 수집하지 않습니다.

## [프로파일링 옵션](https://docs.sentry.io/platforms/javascript/configuration/options.md#profiling-options)

- [profileSessionSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#profileSessionSampleRate)

| Available since | `10.27.0` |
| --------------- | --------- |
| Type            | `number`  |

`0`과 `1` 사이의 숫자로, 몇 퍼센트의 세션에서 프로파일링을 활성화할지 설정합니다. `1.0`은 모든 세션에서 프로파일링을 활성화하고, `0.5`는 세션의 50%에서 활성화하며, `0`은 전혀 활성화하지 않습니다. 샘플링 결정은 세션 시작 시 한 번 이루어집니다. 이 옵션은 프로파일링 활성화에 필수입니다.

서버 환경에서는 프로파일링 세션이 Sentry SDK 초기화 시 시작되고 서비스 종료 시 중지됩니다. 따라서 서비스 재시작 또는 재배포 시 샘플링 결정이 다시 평가됩니다.

브라우저 환경에서는 프로파일링 세션이 사용자 세션에 해당합니다. 사용자 세션은 페이지 로드 시 SDK를 새로 초기화하면서 시작되고 브라우저 탭을 닫으면 종료됩니다.

- [profileLifecycle](https://docs.sentry.io/platforms/javascript/configuration/options.md#profileLifecycle)

| Available since | `10.27.0`             |
| --------------- | --------------------- |
| Type            | `"trace" \| "manual"` |
| Default         | `"manual"`            |

프로파일링 세션 제어 방식을 결정합니다. 두 가지 모드가 있습니다:

* `'manual'` (기본값): `startProfiler()` 및 `stopProfiler()` 함수를 사용해 프로파일링 시작/중지를 직접 제어합니다. 이 모드에서는 프로파일 샘플링이 `profileSessionSampleRate`의 영향만 받습니다.

  이 함수들에 대한 자세한 내용은 [profiling API documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling.md)을 참고하세요.
* `'trace'`: tracing이 활성화되어 있는 동안 transaction에 맞춰 프로파일링이 자동으로 시작/중지됩니다. 최소 하나 이상의 샘플링된 transaction이 있는 동안 profiler가 실행됩니다. 이 모드에서는 프로파일링이 `profileSessionSampleRate`와 tracing 샘플링 비율(`tracesSampleRate` 또는 `tracesSampler`)의 영향을 모두 받습니다.

- [profilesSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#profilesSampleRate)

| Type | `number` |
| ---- | -------- |

**Deprecated:** `10.27.0` 버전부터는 연속 프로파일링 설정에 대신 `profileSessionSampleRate`를 사용하세요.

`0`과 `1` 사이의 숫자로, 샘플링된 특정 transaction이 프로파일링될 확률(백분율)을 제어합니다. (`0`은 0%, `1`은 100%를 의미합니다.) 앱에서 생성된 모든 transaction에 동일하게 적용됩니다. 이 값은 tracing 샘플링 비율에 대한 상대값이며, 예를 들어 `0.5`는 샘플링된 transaction의 50%가 프로파일링됨을 의미합니다.

