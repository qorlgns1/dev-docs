---
title: 'API | Sentry for Next.js'
description: '이 페이지는 SDK에서 사용할 수 있는 모든 최상위 API를 보여줍니다. 이 API들은 다음을 위한 기본 방법으로 사용할 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis

# API | Sentry for Next.js

이 페이지는 SDK에서 사용할 수 있는 모든 최상위 API를 보여줍니다. 이 API들은 다음을 위한 기본 방법으로 사용할 수 있습니다.

* 초기화 후 SDK 구성
* 다양한 유형의 이벤트 수동 캡처
* 추가 데이터로 이벤트 보강
* ... 그 외 더 많은 작업

이 API들은 다음과 같이 사용할 수 있는 함수들이며, 모두 최상위 `Sentry` 객체에서 사용할 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.setTag("tag", "value");
```

## [사용 가능한 API](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#available-apis)

## [Core API](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#core-apis)

- [init](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#init)

```
function init(options: InitOptions): Client | undefined
```

주어진 옵션으로 SDK를 초기화합니다. `init`에 전달할 수 있는 옵션은 [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md)를 참고하세요.

- [getClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getClient)

```
function getClient(): Client | undefined
```

현재 활성화된 클라이언트를 반환합니다.

- [setCurrentClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setCurrentClient)

```
function setCurrentClient(client: Client): void
```

지정한 클라이언트를 현재 클라이언트로 설정합니다. `init()`를 사용한다면 이것은 필요하지 않으며, 클라이언트를 수동으로 설정할 때만 필요합니다.

- [lastEventId](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#lastEventId)

```
function lastEventId(): string | undefined
```

마지막으로 전송된 오류 이벤트의 ID를 반환합니다. 다만 이 이벤트 ID가 실제로 존재함을 보장하지는 않으며, 전송 과정에서 드롭되었을 수 있습니다.

- [flush](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#flush)

```
function flush(timeout?: number): Promise<boolean>
```

매개변수

timeout

```
number
```

클라이언트가 이벤트 큐를 flush하기 위해 대기할 최대 시간(ms)입니다. 이 매개변수를 생략하면 모든 이벤트가 전송될 때까지 대기한 뒤 promise를 resolve합니다.

대기 중인 모든 이벤트를 flush합니다.

- [isEnabled](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#isEnabled)

```
function isEnabled(): boolean
```

SDK가 초기화되고 활성화되어 있으면 true를 반환합니다.

- [close](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#close)

```
function close(timeout?: number): Promise<boolean>
```

매개변수

timeout

```
number
```

클라이언트가 이벤트 큐를 flush하기 위해 대기할 최대 시간(ms)입니다. 이 매개변수를 생략하면 모든 이벤트가 전송될 때까지 대기한 뒤 promise를 resolve합니다.

대기 중인 모든 이벤트를 flush하고 SDK를 비활성화합니다. 이때 SDK가 설정했을 수 있는 리스너는 제거되지 않습니다. `close` 호출 후에는 현재 클라이언트를 더 이상 사용할 수 없습니다. `close`는 애플리케이션 종료 직전에만 호출하는 것이 중요합니다.

대안으로, [`flush`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#flush) 메서드는 이벤트 큐를 비우면서 클라이언트를 계속 활성화된 상태로 유지합니다.

- [addEventProcessor](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#addEventProcessor)

```
function addEventProcessor(processor: EventProcessor): void
```

매개변수

processor

```
(event: Event, hint: EventHint) => Event | null | Promise<Event | null>
```

SDK에 이벤트 프로세서를 추가합니다. 이벤트 프로세서는 Sentry로 전송되기 전의 모든 이벤트를 받습니다. 이벤트를 변경한 뒤 반환하거나, 이벤트를 버리기 위해 `null`을 반환할 수 있습니다. 이벤트 프로세서는 promise도 반환할 수 있지만, 이벤트 처리 속도가 느려지므로 꼭 필요한 경우에만 사용하는 것이 권장됩니다.

`Sentry.addEventProcessor()`로 추가된 이벤트 프로세서는 현재 요청의 모든 이벤트에 적용됩니다.

특정 이벤트에만 적용되는 이벤트 프로세서를 추가하려면, 다음과 같이 scope에 추가할 수도 있습니다.

```javascript
Sentry.withScope((scope) => {
  scope.addEventProcessor((event) => {
    // this will only be applied to events captured within this scope
    return event;
  });

  Sentry.captureException(new Error("test"));
});
```

\`beforeSend\` / \`beforeSendTransaction\`과의 차이는 무엇인가요?

`beforeSend`와 `beforeSendTransaction`은 다른 모든 이벤트 프로세서 이후, 즉 가장 마지막에 실행되는 것이 보장됩니다(이름 그대로 전송 직전의 최종 이벤트 버전을 받습니다). `addEventProcessor`로 추가한 이벤트 프로세서는 실행 순서가 결정되어 있지 않으므로, 해당 프로세서가 실행된 뒤에도 이벤트가 변경될 수 있습니다.

`beforeSend` / `beforeSendTransaction` 프로세서는 하나만 둘 수 있지만, `addEventProcessor()`를 통해서는 여러 이벤트 프로세서를 추가할 수 있습니다.

- [addIntegration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#addIntegration)

```
function addIntegration(integration: Integration): void
```

SDK에 integration을 추가합니다. `Sentry.init()` 호출 이후에 조건부로 integration을 추가할 때 사용할 수 있습니다. 가능하다면 이 메서드를 호출하는 대신 `init`에 integration을 전달하는 방식이 권장됩니다.

integration 사용 방법에 대한 자세한 내용은 [Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md)를 참고하세요.

- [lazyLoadIntegration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#lazyLoadIntegration)

Client에서만 사용 가능

```
function lazyLoadIntegration(name: string, scriptNonce?: string): Promise<IntegrationFn>
```

integration을 지연 로드합니다. 여기서는 이름으로 예를 들어 `replayIntegration`을 기대합니다. CDN에서 스크립트를 로드하고, integration 함수를 resolve하는 promise를 반환합니다. 이후 해당 함수를 호출해 `addIntegration`으로 SDK에 추가할 수 있습니다.

```javascript
Sentry.lazyLoadIntegration("replayIntegration")
  .then((replayIntegration) => {
    Sentry.addIntegration(replayIntegration());
  })
  .catch((error) => {
    // Make sure to handle errors here!
    // This rejects e.g. if the CDN bundle cannot be loaded
  });
```

번들러를 사용한다면, 예를 들어 `const { replayIntegration } = await import('@sentry/browser')` 같은 방식 사용이 대신 권장됩니다.

integration 사용 방법에 대한 자세한 내용은 [Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md)를 참고하세요.

## [이벤트 캡처](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#capturing-events)

- [captureException](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureException)

```
function captureException(
exception: unknown,
captureContext?: CaptureContext
): EventId
```

매개변수

exception\*

```
unknown
```

캡처할 예외입니다. 최상의 결과를 위해 \`Error\` 객체를 전달하는 것이 좋지만, 어떤 값이든 허용됩니다.

captureContext

```
CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
```

Sentry 이벤트에 첨부할 선택적 추가 데이터입니다.

예외 이벤트를 캡처해 Sentry로 전송합니다. `exception`으로 `Error` 객체뿐 아니라 다른 객체도 전달할 수 있습니다. 이 경우 SDK가 객체 직렬화를 시도하며, 스택 트레이스는 SDK가 생성하므로 정확도가 다소 낮을 수 있습니다.

- [captureMessage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureMessage)

```
function captureMessage(
message: string,
captureContext?: CaptureContext | SeverityLevel
): EventId
```

매개변수

message\*

```
string
```

캡처할 메시지입니다.

captureContext

```
CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
```

Sentry 이벤트에 첨부할 선택적 추가 데이터입니다.

메시지 이벤트를 캡처해 Sentry로 전송합니다. 선택적으로 두 번째 인자에 `CaptureContext` 대신 `SeverityLevel`도 전달할 수 있습니다(예: `"error"` 또는 `"warning"`).

메시지는 이슈 스트림에 메시지를 이슈 이름으로 하여 이슈로 표시됩니다.

## [이벤트 보강](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#enriching-events)

- [setTag](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setTag)

```
function setTag(key: string, value: string): void
```

Sentry 이벤트와 함께 전송할 태그를 설정합니다.

* 태그 키의 최대 길이는 32자이며, 문자(`a-zA-Z`), 숫자(`0-9`), 밑줄(`_`), 마침표(`.`), 콜론(`:`), 대시(`-`)만 포함할 수 있습니다.
* 태그 값의 최대 길이는 200자이며, 줄바꿈(`\n`) 문자를 포함할 수 없습니다.

- [setTags](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setTags)

```
function setTags(tags: Record<string, string>): void
```

Sentry 이벤트와 함께 전송할 여러 태그를 설정합니다.

- [setContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setContext)

```
function setContext(name: string, context: Record<string, unknown>): void
```

Sentry 이벤트와 함께 전송할 컨텍스트를 설정합니다. 사용자 지정 컨텍스트를 사용하면 이벤트에 임의의 데이터를 첨부할 수 있습니다. 이 데이터는 검색할 수 없지만 이슈 페이지에서 확인할 수 있습니다. 특정 데이터로 필터링해야 한다면 대신 [tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setTag)를 사용하세요. 이전에 설정한 컨텍스트를 지우려면 컨텍스트 값으로 `null`을 전달하세요.

컨텍스트 이름에는 제한이 없습니다. 컨텍스트 객체에서는 내부적으로 사용되는 `type`을 제외한 모든 키를 사용할 수 있습니다.

기본적으로 Sentry SDK는 중첩된 구조화 컨텍스트 데이터를 최대 3단계 깊이까지 정규화합니다. 이 깊이를 초과하는 데이터는 잘리고 타입으로 표시됩니다. 이 기본값을 조정하려면 [`normalizeDepth`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#normalize-depth) SDK 옵션을 사용하세요.

일반적인 컨텍스트에 대한 규칙은 [contexts interface developer documentation](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/contexts/)에서 자세히 확인할 수 있습니다.

예시

컨텍스트 데이터는 구조화되어 있으며 원하는 어떤 데이터든 포함할 수 있습니다.

```javascript
Sentry.setContext("character", {
  name: "Mighty Fighter",
  age: 19,
  attack_type: "melee",
});
```

- [setExtra](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setExtra)

```
function setExtra(name: string, extra: unknown): void
```

Sentry 이벤트와 함께 전송할 추가 데이터를 설정합니다.

- [setExtras](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setExtras)

```
function setExtras(extras: Record<string, unknown>): void
```

Sentry 이벤트와 함께 전송할 여러 추가 데이터 항목을 설정합니다.

- [setUser](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setUser)

```
function setUser(user: User | null): void
```

매개변수

user

```
User {
// Your internal identifier for the user
id?: string | number,
// Sentry is aware of email addresses and can display things such as Gravatars and unlock messaging capabilities
email?: string,
// Typically used as a better label than the internal id
username?: string,
// The user's IP address. If the user is unauthenticated, Sentry uses the IP address as a unique identifier for the user
ip_address?: string,
}
```

Sentry 이벤트와 함께 전송할 사용자를 설정합니다. 사용자 설정을 해제하려면 `null`로 설정하세요. `User` 객체의 지정된 속성 외에도 임의의 추가 키/값 쌍을 더할 수 있습니다.

사용자 IP 주소 캡처

서버에서는 가능할 경우 들어오는 HTTP 요청으로부터 IP 주소를 추론합니다. [SDK configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii)에서 `sendDefaultPii: true`를 설정했다면 이 작업은 자동으로 수행됩니다.

브라우저에서는 사용자의 `ip_address`가 `"{{ auto }}"`로 설정된 경우, Sentry가 앱과 Sentry 서버 간 연결에서 IP 주소를 추론합니다. [SDK configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii)에서 `sendDefaultPii: true`를 설정했다면 `{{auto}}`는 자동으로 설정됩니다.

사용자 IP 주소가 이벤트 데이터에 절대 저장되지 않도록 하려면 프로젝트 설정에서 "Security & Privacy"를 클릭한 뒤 "Prevent Storing of IP Addresses"를 활성화하거나, Sentry의 [server-side data scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing.md)을 사용해 `$user.ip_address`를 제거할 수 있습니다. 이런 규칙을 추가하면 결국 다른 모든 로직보다 우선 적용됩니다.

현재 요청의 사용자 설정

`Sentry.setUser()`는 현재 활성 요청의 사용자를 설정합니다. 자세한 내용은 [Request Isolation](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation.md)을 참고하세요. 예를 들어 단일 요청에 대해서만 사용자를 설정하려면 다음과 같이 할 수 있습니다.

```javascript
// Your route handler, for example:
app.get("/my-route", (req, res) => {
  // Get the user from somewhere
  const user = req.user;

  // Set the user data for this request only
  Sentry.setUser({
    id: user.id,
    email: user.email,
    username: user.username,
  });

  res.send("Hello World");
});
```

또는 모든 요청에 대해 사용자를 설정하려면 다음과 같은 미들웨어를 사용할 수 있습니다.

```javascript
// Add a middleware, for example:
app.use((req, res, next) => {
  // Get the user from somewhere
  const user = req.user;

  // Set the user data for all requests
  if (user) {
    Sentry.setUser({
      id: user.id,
      email: user.email,
      username: user.username,
    });
  } else {
    Sentry.setUser(null);
  }

  next();
});
```

- [addBreadcrumb](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#addBreadcrumb)

```
function addBreadcrumb(breadcrumb: Breadcrumb, hint?: Hint): void
```

매개변수

breadcrumb\*

```
Breadcrumb {
// If a message is provided, it is rendered as text with all whitespace preserved.
message?: string,
// The type influences how a breadcrumb is rendered in Sentry. When in doubt, leave it at `default`.
type?: "default" | "debug" | "error" | "info" | "navigation" | "http" | "query" | "ui" | "user",
// The level is used in the UI to emphasize or deemphasize the breadcrumb.
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Typically it is a module name or a descriptive string. For instance, `ui.click` could be used to indicate that a click happened
category?: string,
// Additional data that should be sent with the breadcrumb.
data?: Record<string, unknown>,
}
```

hint

```
Record<string, unknown>
```

breadcrumb에 대한 추가 정보를 담은 힌트 객체입니다.

흥미로운 일이 발생할 때마다 breadcrumb를 수동으로 추가할 수 있습니다. 예를 들어 사용자가 인증했거나 다른 상태 변화가 발생했을 때 breadcrumb를 수동으로 기록할 수 있습니다.

## [트레이싱](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#tracing)

- [startSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpan)

```
function startSpan<T>(options: StartSpanOptions, callback: (span: Span) => T): T
```

매개변수

options\*

```
StartSpanOptions {
name: string,
// Attributes to add to the span.
attributes?: Record<string, string | number | boolean | null | undefined>,
// The timestamp to use for the span start. If not provided, the current time will be used.
startTime?: number,
// The operation name for the span. This is used to group spans in the UI
op?: string,
// If true, the span will be forced to be sent as a transaction, even if it is not the root span.
forceTransaction?: boolean,
// The parent span for the new span. If not provided, the current span will be used.
parentSpan?: Span | null,
// If true, the span will only be created if there is an active span.
onlyIfParent?: boolean,
}
```

callback\*

```
(span: Span) => T
```

제공된 callback에서 활성 상태인 새 span을 시작합니다. 현재 활성 span이 있다면, 이 span은 해당 span의 자식이 됩니다.

callback 내부에서 생성되는 모든 span은 이 span의 자식이 됩니다.

시작된 span은 callback이 반환될 때 자동으로 종료되며, 따라서 callback의 실행 시간을 측정합니다. callback은 async 함수일 수도 있습니다.

예제

```javascript
// Synchronous example
Sentry.startSpan({ name: "my-span" }, (span) => {
  measureThis();
});

// Asynchronous example
const status = await Sentry.startSpan(
  { name: "my-span" },
  async (span) => {
    const status = await doSomething();
    return status;
  },
);
```

span 작업 방법에 대한 자세한 내용은 [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md)을 참고하세요.

- [startInactiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startInactiveSpan)

```
function startInactiveSpan<T>(options: StartSpanOptions): Span
```

매개변수

options\*

```
StartSpanOptions {
name: string,
// Attributes to add to the span.
attributes?: Record<string, string | number | boolean | null | undefined>,
// The timestamp to use for the span start. If not provided, the current time will be used.
startTime?: number,
// The operation name for the span. This is used to group spans in the UI
op?: string,
// If true, the span will be forced to be sent as a transaction, even if it is not the root span.
forceTransaction?: boolean,
// The parent span for the new span. If not provided, the current span will be used.
parentSpan?: Span | null,
// If true, the span will only be created if there is an active span.
onlyIfParent?: boolean,
}
```

새 span을 시작합니다. 현재 활성 span이 있다면, 이 span은 해당 span의 자식이 됩니다. 반환된 span은 작업이 끝났을 때 `span.end()`를 통해 수동으로 종료해야 합니다.

예제

```javascript
const span = Sentry.startInactiveSpan({ name: "my-span" });
doSomething();
span.end();
```

span 작업 방법에 대한 자세한 내용은 [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md)을 참고하세요.

- [startSpanManual](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpanManual)

```
function startSpanManual<T>(options: StartSpanOptions, callback: (span: Span) => T): T
```

매개변수

options\*

```
StartSpanOptions {
name: string,
// Attributes to add to the span.
attributes?: Record<string, string | number | boolean | null | undefined>,
// The timestamp to use for the span start. If not provided, the current time will be used.
startTime?: number,
// The operation name for the span. This is used to group spans in the UI
op?: string,
// If true, the span will be forced to be sent as a transaction, even if it is not the root span.
forceTransaction?: boolean,
// The parent span for the new span. If not provided, the current span will be used.
parentSpan?: Span | null,
// If true, the span will only be created if there is an active span.
onlyIfParent?: boolean,
}
```

callback\*

```
(span: Span) => T
```

제공된 callback에서 활성 상태인 새 span을 시작합니다. 현재 활성 span이 있다면, 이 span은 해당 span의 자식이 됩니다.

callback 내부에서 생성되는 모든 span은 이 span의 자식이 됩니다.

시작된 span은 자동으로 종료되지 *않습니다* - span 작업이 끝나면 `span.end()`를 호출해야 합니다. 단, callback이 활성화되어 있는 동안에만 callback 내부에서 생성되는 span의 부모 span이 된다는 점에 유의하세요. 대부분의 경우 대신 `startSpan` 또는 `startInactiveSpan`을 사용하는 것이 좋습니다.

예제

```javascript
const status = await Sentry.startSpanManual(
  { name: "my-span" },
  async (span) => {
    const status = await doSomething();
    span.end();
    return status;
  },
);
```

span 작업 방법에 대한 자세한 내용은 [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md)을 참고하세요.

- [setActiveSpanInBrowser](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setActiveSpanInBrowser)

클라이언트에서만 사용 가능

```
function setActiveSpanInBrowser(span: Span): void
```

사용 가능 버전: `v10.15.0`

전달된 span을 현재 scope의 활성 span으로 설정합니다. 대부분의 경우 이 기능은 필요하지 않으며 대신 [`startSpan` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpan)을 권장합니다. 하지만 일부 상황에서는 callback 외부에서 span을 활성 상태로 유지하고 싶을 수 있습니다. 이 경우 [`startInactiveSpan`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startInactiveSpan)과 이 함수를 함께 사용하면 span을 시작하고 참조를 유지하면서, 활성 기간이 callback에 묶이지 않게( [`startSpanManual`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpanManual)과 달리) 종료 시점까지 활성 상태를 유지할 수 있습니다.

예제

```javascript
let checkoutSpan;

on("startCheckout", () => {
  checkoutSpan = Sentry.startInactiveSpan({ name: "checkout-flow" });
  Sentry.setActiveSpanInBrowser(checkoutSpan);
});

doSomeWork();

on("endCheckout", () => {
  // Ending the span automatically removes it as the active span on the scope
  checkoutSpan.end();
});
```

span 작업 방법에 대한 자세한 내용은 [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md)을 참고하세요.

- [continueTrace](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#continueTrace)

```
function continueTrace<T>(options: TraceOptions, callback: () => T): T
```

매개변수

options

```
TraceOptions {
// The sentry-trace header.
sentryTrace?: string,
// The baggage header.
baggage?: string,
}
```

callback

```
() => T
```

추적을 이어갈 callback입니다.

제공된 callback에서 trace를 이어갑니다. callback 내부에서 생성되는 모든 span은 해당 trace에 연결됩니다.

- [suppressTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#suppressTracing)

```
function suppressTracing<T>(callback: () => T): T
```

제공된 callback 내부에서 생성되는 모든 span이 Sentry로 전송되지 않도록 합니다.

- [startNewTrace](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startNewTrace)

```
function startNewTrace<T>(callback: () => T): T
```

제공된 callback에서 활성 상태인 새 trace를 시작합니다.

- [startBrowserTracingPageLoadSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startBrowserTracingPageLoadSpan)

클라이언트에서만 사용 가능

```
function startBrowserTracingPageLoadSpan(client: Client, options: StartSpanOptions): Span | undefined
```

페이지가 유휴 상태로 간주되면 자동으로 종료되는 pageload span을 시작합니다. 현재 pageload/navigation span이 진행 중이면 먼저 자동으로 종료됩니다. 대부분의 경우 `browserTracingIntegration`이 자동으로 처리하므로 이를 직접 호출할 필요가 없습니다. 다만 pageload span을 opt-out한 경우에는 이 메서드로 해당 span을 수동 시작할 수 있습니다. `browserTracingIntegration`이 활성화되지 않았다면 이 함수는 아무 동작도 하지 않습니다.

- [startBrowserTracingNavigationSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startBrowserTracingNavigationSpan)

클라이언트에서만 사용 가능

```
function startBrowserTracingNavigationSpan(client: Client, options: StartSpanOptions): Span | undefined
```

페이지가 유휴 상태로 간주되면 자동으로 종료되는 navigation span을 시작합니다. 현재 pageload/navigation span이 진행 중이면 먼저 자동으로 종료됩니다. 대부분의 경우 `browserTracingIntegration`이 자동으로 처리하므로 이를 직접 호출할 필요가 없습니다. 다만 navigation span을 opt-out한 경우에는 이 메서드로 해당 span을 수동 시작할 수 있습니다. `browserTracingIntegration`이 활성화되지 않았다면 이 함수는 아무 동작도 하지 않습니다.

- [reportPageLoaded](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#reportPageLoaded)

클라이언트에서만 사용 가능

```
function reportPageLoaded(): void
```

사용 가능 버전: `v10.13.0`

초기 페이지가 완전히 로드되었음을 Sentry SDK에 알립니다. `browserTracingIntegration`에서 [`enableReportPageLoaded` 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableReportPageLoaded)이 `true`로 설정되어 있어야 합니다. 호출되면 SDK가 pageload span을 자동으로 종료합니다,

기본적으로 SDK는 pageload trace에 새로운 자식 span이 추가되지 않는 비활성 기간을 기준으로 pageload span을 자동 종료합니다. `browserTracingIntegration`의 비활성 휴리스틱이 사용 사례에 잘 맞지 않는다면, 대신 명시적 pageload 보고를 사용할 수 있습니다. 다만 모든 상황에서 `reportPageLoaded`를 호출해야 합니다. `reportPageLoaded`가 호출되지 않으면 pageload span은 30초 후 또는 [`finalTimeout` 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableReportPageLoaded)에 설정된 사용자 지정 값 이후에 종료됩니다.

예제

```javascript
Sentry.init({
  // 1. Enable manual page load reporting:
  integrations: [
    browserTracingIntegration({ enableReportPageLoaded: true }),
  ],
});

// 2. Whenever you consider the page loaded:
Sentry.reportPageLoaded();
```

## [Tracing Utilities](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#tracing-utilities)

이 유틸리티는 더 고급 tracing 사용 사례에 사용할 수 있습니다.

- [spanToJSON](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#spanToJSON)

```
function spanToJSON(span: Span): SpanJSON
```

span을 JSON 객체로 변환합니다.

- [updateSpanName](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#updateSpanName)

```
function updateSpanName(span: Span, name: string): void
```

span의 이름을 업데이트합니다. 모든 백엔드에서 span이 업데이트되도록 `span.updateName(name)` 대신 이것을 사용하세요.

- [setHttpStatus](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setHttpStatus)

```
function setHttpStatus(span: Span, httpStatus: number): void
```

주어진 http status code를 기반으로 span의 상태를 설정합니다.

- [getActiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getActiveSpan)

```
function getActiveSpan(): Span | undefined
```

현재 활성 span을 가져옵니다.

- [getRootSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getRootSpan)

```
function getRootSpan(span: Span): Span
```

span의 루트 span을 가져옵니다.

- [withActiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withActiveSpan)

```
function withActiveSpan<T>(span: Span | null, callback: (scope: Scope) => T): T
```

제공된 callback을, 주어진 span을 활성 span으로 설정한 상태에서 실행합니다. `null`이 제공되면 callback에는 활성 span이 없습니다.

- [setConversationId](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setConversationId)

```
function setConversationId(conversationId: string | null): void
```

현재 scope 내의 이후 모든 AI span에 자동 적용될 conversation ID를 설정합니다. 이는 동일한 대화에 속한 여러 AI API 호출을 추적하여 Sentry에서 전체 대화 흐름을 분석하는 데 유용합니다.

conversation ID는 isolation scope에 저장되며, 모든 AI 관련 span에 `gen_ai.conversation.id` 속성으로 자동 추가됩니다. conversation ID를 해제하려면 `null`을 전달하세요.

예제

```javascript
import * as Sentry from '@sentry/node';

// Set conversation ID for all subsequent spans
Sentry.setConversationId('conv_abc123');

// All AI spans will now include the gen_ai.conversation.id attribute
await openai.chat.completions.create({...});

// To unset it
Sentry.setConversationId(null);
```

AI 대화 추적에 대한 자세한 내용은 [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md)을 참고하세요.

## [Sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#sessions)

Sessions를 사용하면 애플리케이션의 릴리스 상태 건전성을 추적할 수 있습니다. 자세한 내용은 [Releases & Health](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#sessions) 페이지를 참고하세요.

- [startSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSession)

```
function startSession(): Session
```

새 session을 시작합니다.

- [endSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#endSession)

```
function endSession(): void
```

현재 session을 종료합니다(단, Sentry로 전송하지는 않음).

- [captureSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureSession)

```
function captureSession(end = false): void
```

scope의 현재 session을 Sentry로 전송합니다. 먼저 session을 종료하려면 인수로 `true`를 전달하세요.

## [Scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#scopes)

scope 사용 방법과 서로 다른 scope 유형(현재 scope, isolation scope, 전역 scope)에 대한 설명은 [Scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md)를 참고하세요.

- [withScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withScope)

```
function withScope(callback: (scope: Scope) => void): void
```

현재 scope를 포크하고, 포크된 scope로 callback을 호출합니다.

- [withIsolationScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withIsolationScope)

```
function withIsolationScope(callback: (scope: Scope) => void): void
```

현재 isolation scope를 포크하고, 포크된 scope로 callback을 호출합니다.

- [getCurrentScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getCurrentScope)

```
function getCurrentScope(): Scope
```

[현재 scope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#current-scope)를 반환합니다.

대부분의 경우 이 API를 사용하기보다는 `withScope`를 사용해 로컬 scope를 생성하고 접근해야 한다는 점에 유의하세요. 애플리케이션의 여러 지점에서 내부적으로 scope 포크가 일어날 수 있으므로, `getCurrentScope`의 일관성은 보장되지 않습니다.

- [getIsolationScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getIsolationScope)

```
function getIsolationScope(): Scope
```

현재<!-- -->

[isolation scope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#isolation-scope)

를 반환합니다.

- [getGlobalScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getGlobalScope)

```
function getGlobalScope(): Scope
```

<!-- -->

[global scope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#global-scope)

를 반환합니다.

## [사용자 피드백](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#user-feedback)

- [captureFeedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureFeedback)

```
function captureFeedback(feedback: Feedback, hint?: Hint): string
```

매개변수

feedback

```
Feedback {
message: string,
name?: string,
email?: string,
url?: string,
source?: string,
// The event id that this feedback is associated with.
associatedEventId?: string,
tags?: Record<string, string>,
}
```

캡처할 피드백입니다.

hint

```
Hint {
// Optional additional data to attach to the Sentry event.
captureContext?: CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
}
```

피드백에 대한 추가 정보를 포함하는 선택적 힌트 객체입니다.

사용자 피드백을 Sentry로 전송합니다.

- [getFeedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getFeedback)

```
function getFeedback(): ReturnType<feedbackIntegration> | undefined
```

추가된 경우 피드백 통합을 가져옵니다. 이를 통해 타입 안전한 방식으로 피드백 통합에 접근할 수 있습니다.

- [sendFeedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#sendFeedback)

```
function sendFeedback(feedback: Feedback, hint?: Hint): Promise<string>
```

매개변수

feedback

```
Feedback {
message: string,
name?: string,
email?: string,
url?: string,
source?: string,
// The event id that this feedback is associated with.
associatedEventId?: string,
tags?: Record<string, string>,
}
```

캡처할 피드백입니다.

hint

```
Hint {
// Optional additional data to attach to the Sentry event.
captureContext?: CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
}
```

피드백에 대한 추가 정보를 포함하는 선택적 힌트 객체입니다.

이 메서드는 [`captureFeedback`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#capturefeedback)와 유사하지만, 피드백이 Sentry로 성공적으로 전송되었을 때에만 resolve되는 promise를 반환합니다. 피드백을 전송할 수 없으면 reject됩니다.

## [Cron 모니터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#cron-monitoring)

- [captureCheckIn](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureCheckIn)

서버에서만 사용 가능

```
function captureCheckIn(checkIn: CheckIn, monitorConfig?: MonitorConfig): string
```

매개변수

checkIn\*

```
CheckIn {
status: "ok" | "error" | "in_progress",
monitorSlug: string,
checkInId?: string,
duration?: number,
}
```

monitorConfig

```
MonitorConfig {
schedule: { type: "crontab", value: string } | { type: "interval", value: number, unit: "year" | "month" | "day" | "hour" | "minute" },
checkinMargin?: number,
maxRuntime?: number,
timezone?: string,
failureIssueThreshold?: number,
recoveryThreshold?: number,
}
```

Cron 모니터 체크인을 생성하여 Sentry로 전송합니다.

- [withMonitor](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withMonitor)

서버에서만 사용 가능

```
function withMonitor(
monitorSlug: string,
callback: () => any,
monitorConfig?: MonitorConfig
): string
```

매개변수

monitorSlug\*

```
string
```

callback\*

```
() => any
```

monitorConfig

```
MonitorConfig {
schedule: { type: "crontab", value: string } | { type: "interval", value: number, unit: "year" | "month" | "day" | "hour" | "minute" },
checkinMargin?: number,
maxRuntime?: number,
timezone?: string,
failureIssueThreshold?: number,
recoveryThreshold?: number,
}
```

콜백을 Cron 모니터 체크인으로 감쌉니다. 체크인은 콜백이 완료되면 Sentry로 전송됩니다.

## [서버 액션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#server-actions)

- [withServerActionInstrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withServerActionInstrumentation)

```
function withServerActionInstrumentation(
serverActionName: string,
options?: Options,
callback: A
): Promise<ReturnType<A>>
```

Next.js Server Actions를 계측하려면, 서버 액션을 설명하는 이름과 함께 해당 내용물을 `withServerActionInstrumentation`으로 감싸세요. 필요에 따라 form data와 headers를 전달해 이를 기록할 수 있고, Server Action 응답을 기록하도록 래퍼를 구성할 수도 있습니다.

예제

```tsx
import * as Sentry from "@sentry/nextjs";
import { headers } from "next/headers";

export default function ServerComponent() {
  async function myServerAction(formData: FormData) {
    "use server";
    return await Sentry.withServerActionInstrumentation(
      "myServerAction", // The name you want to associate this Server Action with in Sentry
      {
        formData, // Optionally pass in the form data
        headers: await headers(), // Optionally pass in headers
        recordResponse: true, // Optionally record the server action response
      },
      async () => {
        // ... Your Server Action code

        return { name: "John Doe" };
      },
    );
  }

  return (
    <form action={myServerAction}>
      <input type="text" name="some-input-value" />
      <button type="submit">Run Action</button>
    </form>
  );
}
```

## [라우트 및 데이터 페칭 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#route-and-data-fetching-instrumentation)

- [wrapApiHandlerWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapApiHandlerWithSentry)

```
function wrapApiHandlerWithSentry(
apiHandler: NextApiHandler,
parameterizedRoute: string
): NextApiHandler
```

제공된 API route handler를 Sentry 오류 및 성능 모니터링으로 계측합니다. 이 함수는 사용자의 API page route 파일에서 export된 handler를 감쌉니다(이미 `withSentry`로 감싸졌을 수도 있고 아닐 수도 있습니다).

- [wrapGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapGetInitialPropsWithSentry)

```
function wrapGetInitialPropsWithSentry(
origGetInitialProps: GetInitialProps
): GetInitialProps
```

`getInitialProps` 함수를 감싼 버전을 생성해 반환함으로써 Sentry 오류 및 성능 모니터링으로 계측합니다.

- [wrapGetServerSidePropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapGetServerSidePropsWithSentry)

```
function wrapGetServerSidePropsWithSentry(
origGetInitialProps: GetInitialProps,
parameterizedRoute: string
): GetServerSideProps
```

`getServerSideProps` 함수를 감싼 버전을 생성해 반환함으로써 Sentry 오류 및 성능 모니터링으로 계측합니다.

- [wrapGetStaticPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapGetStaticPropsWithSentry)

```
function wrapGetStaticPropsWithSentry(
origGetStaticPropsa: GetStaticProps<Props>,
_parameterizedRoute: string
): GetStaticProps<Props>
```

`getStaticProps` 함수를 감싼 버전을 생성해 반환함으로써 Sentry 오류 및 성능 모니터링으로 계측합니다.

- [wrapErrorGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapErrorGetInitialPropsWithSentry)

```
function wrapErrorGetInitialPropsWithSentry(
origErrorGetInitialProps: ErrorGetInitialProps
): ErrorGetInitialProps
```

커스텀 에러 페이지(`_error.js`)의 `getInitialProps` 함수를 감싼 버전을 생성해 반환함으로써 Sentry 오류 및 성능 모니터링으로 계측합니다.

- [wrapAppGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapAppGetInitialPropsWithSentry)

```
function wrapAppGetInitialPropsWithSentry(
origAppGetInitialProps: AppGetInitialProps
): AppGetInitialProps
```

커스텀 앱(`_app.js`)의 `getInitialProps` 함수를 감싼 버전을 생성해 반환함으로써 Sentry 오류 및 성능 모니터링으로 계측합니다.

- [wrapDocumentGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapDocumentGetInitialPropsWithSentry)

```
function wrapDocumentGetInitialPropsWithSentry(
origDocumentGetInitialProps: DocumentGetInitialProps
): DocumentGetInitialProps
```

커스텀 document(`_document.js`)의 `getInitialProps` 함수를 감싼 버전을 생성해 반환함으로써 Sentry 오류 및 성능 모니터링으로 계측합니다.

