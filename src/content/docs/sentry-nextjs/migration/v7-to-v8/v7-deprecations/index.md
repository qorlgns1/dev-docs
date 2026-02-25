---
title: '7.x의 사용 중단 항목 | Sentry for Next.js'
description: '의 대부분 사용 중단 항목은  codemod를 사용해 SDK 사용 방식을 자동으로 업데이트하여 해결할 수 있습니다. 는 Node 18+가 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations

# `7.x`의 사용 중단 항목 | Sentry for Next.js

`7.x`의 대부분 사용 중단 항목은 [`@sentry/migr8`](https://www.npmjs.com/package/@sentry/migr8) codemod를 사용해 SDK 사용 방식을 자동으로 업데이트하여 해결할 수 있습니다. `@sentry/migr8`는 Node 18+가 필요합니다.

```bash
npx @sentry/migr8@latest
```

마이그레이션 도구를 사용하면 실행할 업데이트를 선택할 수 있고, 코드도 자동으로 업데이트됩니다. 일부 경우에는 코드를 자동으로 변경할 수 없습니다. 이런 부분은 대신 `TODO(sentry)` 주석으로 표시됩니다. `@sentry/migr8` 실행 후에는 모든 코드 변경 사항을 반드시 검토하세요!

## [사용 중단 항목 목록](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#list-of-deprecations)

아래는 `7.x`에서 발생한 가장 중요한 사용 중단 항목 목록입니다. 모든 사용 중단 항목의 전체 목록은 GitHub의 [상세 마이그레이션 문서](https://github.com/getsentry/sentry-javascript/blob/develop/MIGRATION.md#deprecations-in-7x)를 참고하세요.

- [클래스 기반 integration 사용 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-class-based-integrations)

*`7.100.0`에서 사용 중단 도입.*

v7에서 integration은 클래스이며, 예를 들어 `integrations: [new Sentry.Integrations.ContextLines()]`처럼 추가할 수 있습니다. v8에서는 integration이 더 이상 클래스가 아니라 함수가 됩니다. 클래스로 사용하는 방식과 `Integrations.XXX` 해시를 통해 integration에 접근하는 방식 모두, 새로운 함수형 integration 사용을 권장하며 사용 중단되었습니다.

* 예를 들어 `new Integrations.LinkedErrors()`는 `linkedErrorsIntegration()`으로 바뀝니다.

아래 목록은 integration을 어떻게 마이그레이션해야 하는지 보여줍니다.

클라이언트 측 Integrations:

| Old                                 | New                              |
| ----------------------------------- | -------------------------------- |
| `new BrowserTracing()`              | `browserTracingIntegration()`    |
| `new InboundFilters()`              | `inboundFiltersIntegration()`    |
| `new FunctionToString()`            | `functionToStringIntegration()`  |
| `new LinkedErrors()`                | `linkedErrorsIntegration()`      |
| `new ModuleMetadata()`              | `moduleMetadataIntegration()`    |
| `new Replay()`                      | `replayIntegration()`            |
| `new ReplayCanvas()`                | `replayCanvasIntegration()`      |
| `new Feedback()`                    | `feedbackIntegration()`          |
| `new CaptureConsole()`              | `captureConsoleIntegration()`    |
| `new Debug()`                       | `debugIntegration()`             |
| `new Dedupe()`                      | `dedupeIntegration()`            |
| `new ExtraErrorData()`              | `extraErrorDataIntegration()`    |
| `new ReportingObserver()`           | `reportingObserverIntegration()` |
| `new RewriteFrames()`               | `rewriteFramesIntegration()`     |
| `new SessionTiming()`               | `sessionTimingIntegration()`     |
| `new HttpClient()`                  | `httpClientIntegration()`        |
| `new ContextLines()`                | `contextLinesIntegration()`      |
| `new Breadcrumbs()`                 | `breadcrumbsIntegration()`       |
| `new GlobalHandlers()`              | `globalHandlersIntegration()`    |
| `new HttpContext()`                 | `httpContextIntegration()`       |
| `new TryCatch()`                    | `browserApiErrorsIntegration()`  |
| `new BrowserProfilingIntegration()` | `browserProfilingIntegration()`  |

서버 측 Integrations:

| Old                          | New                                 |
| ---------------------------- | ----------------------------------- |
| `new InboundFilters()`       | `inboundFiltersIntegration()`       |
| `new FunctionToString()`     | `functionToStringIntegration()`     |
| `new LinkedErrors()`         | `linkedErrorsIntegration()`         |
| `new RequestData()`          | `requestDataIntegration()`          |
| `new CaptureConsole()`       | `captureConsoleIntegration()`       |
| `new Debug()`                | `debugIntegration()`                |
| `new Dedupe()`               | `dedupeIntegration()`               |
| `new ExtraErrorData()`       | `extraErrorDataIntegration()`       |
| `new RewriteFrames()`        | `rewriteFramesIntegration()`        |
| `new SessionTiming()`        | `sessionTimingIntegration()`        |
| `new Console()`              | `consoleIntegration()`              |
| `new Context()`              | `nodeContextIntegration()`          |
| `new Modules()`              | `modulesIntegration()`              |
| `new OnUncaughtException()`  | `onUncaughtExceptionIntegration()`  |
| `new OnUnhandledRejection()` | `onUnhandledRejectionIntegration()` |
| `new ContextLines()`         | `contextLinesIntegration()`         |
| `new LocalVariables()`       | `localVariablesIntegration()`       |
| `new Spotlight()`            | `spotlightIntegration()`            |
| `new Anr()`                  | `anrIntegration()`                  |
| `new Hapi()`                 | `hapiIntegration()`                 |
| `new Undici()`               | `nativeNodeFetchIntegration()`      |
| `new Http()`                 | `httpIntegration()`                 |
| `new ProfilingIntegration()` | `nodeProfilingIntegration()`        |

- [`BrowserTracing` integration 사용 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecated-browsertracing-integration)

*`7.100.0`에서 사용 중단 도입.*

`BrowserTracing` integration과 여기에 전달되는 커스텀 라우팅 instrumentation은 v8에서 사용 중단되었습니다.

대신 `Sentry.browserTracingIntegration()`을 사용해야 합니다.

브라우저 트레이싱은 이 패키지들에서 자동으로 설정되므로, `BrowserTracing` 클래스를 직접 사용하고 있지 않았다면 코드를 변경할 필요가 없습니다.

`instrumentation-client.js`

```JavaScript
 import * as Sentry from "@sentry/nextjs";

 Sentry.init({
   dsn: "___PUBLIC_DSN___",
-  integrations: [new Sentry.BrowserTracing()],
+  integrations: [Sentry.browserTracingIntegration()],
 });
```

- [`getIntegration()` 및 `getIntegrationById()` 사용 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-getintegration-and-getintegrationbyid)

*`7.94.0`에서 사용 중단 도입.*

클라이언트의 `getIntegrationById()`와 `getIntegration()`이 사용 중단됩니다. 대신 `getIntegrationByName()`을 사용하세요. 선택적으로 integration generic을 전달하면 작업이 더 쉬워집니다.

```TypeScript
const replay = getClient().getIntegrationByName<Replay>("Replay");
```

- [`Hub` 사용 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-hub)

*`7.110.0`에서 사용 중단 도입.*

`Hub`는 지금까지 Sentry SDK API에서 매우 중요한 부분이었습니다. Hub는 스레드 전반의 데이터를 추적하고 코드의 특정 부분으로 데이터를 범위 지정하기 위한 SDK의 "동시성 단위"였습니다. 하지만 고급 사용자에게도 지나치게 복잡하고 혼란스러워, 새로운 API 세트인 "새 Scope API"로 대체될 예정입니다.

`Scope`는 이전부터 SDK에 존재했지만, 이제는 `Hub` API를 완전히 대체할 만큼 충분히 강력하다는 판단에 따라 이를 확장하고 있습니다.

현재 `Hub`를 사용 중이라면, 아래 표를 참고해 새 API로 마이그레이션하세요.

| Old `Hub` API          | New `Scope` API                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------ |
| `new Hub()`            | `withScope()`, `withIsolationScope()` 또는 `new Scope()`                               |
| hub.isOlderThan()      | REMOVED - 제거될 `Hub` 인스턴스를 비교하는 데 사용됨                                    |
| hub.bindClient()       | `scope.setClient()`와 `client.init()`의 조합                                          |
| hub.pushScope()        | `Sentry.withScope()`                                                                 |
| hub.popScope()         | `Sentry.withScope()`                                                                 |
| hub.withScope()        | `Sentry.withScope()`                                                                 |
| getClient()            | `Sentry.getClient()`                                                                 |
| getScope()             | 현재 활성 scope를 가져오려면 `Sentry.getCurrentScope()` 사용                            |
| getIsolationScope()    | `Sentry.getIsolationScope()`                                                         |
| getStack()             | REMOVED - 예전에는 stack이 scope를 보관했지만, 이제는 scope를 직접 사용                  |
| getStackTop()          | REMOVED - 예전에는 stack이 scope를 보관했지만, 이제는 scope를 직접 사용                  |
| captureException()     | `Sentry.captureException()`                                                          |
| captureMessage()       | `Sentry.captureMessage()`                                                            |
| captureEvent()         | `Sentry.captureEvent()`                                                              |
| addBreadcrumb()        | `Sentry.addBreadcrumb()`                                                             |
| setUser()              | `Sentry.setUser()`                                                                   |
| setTags()              | `Sentry.setTags()`                                                                   |
| setExtras()            | `Sentry.setExtras()`                                                                 |
| setTag()               | `Sentry.setTag()`                                                                    |
| setExtra()             | `Sentry.setExtra()`                                                                  |
| setContext()           | `Sentry.setContext()`                                                                |
| configureScope()       | REMOVED - 이제 scope가 동시성의 단위임                                                 |
| run()                  | `Sentry.withScope()` 또는 `Sentry.withIsolationScope()`                                |
| getIntegration()       | `client.getIntegration()`                                                            |
| startTransaction()     | `Sentry.startSpan()`, `Sentry.startInactiveSpan()` 또는 `Sentry.startSpanManual()`     |
| traceHeaders()         | REMOVED - 가장 가까운 대체는 `spanToTraceHeader(getActiveSpan())`                     |
| captureSession()       | `Sentry.captureSession()`                                                            |
| startSession()         | `Sentry.startSession()`                                                              |
| endSession()           | `Sentry.endSession()`                                                                |
| shouldSendDefaultPii() | REMOVED - 가장 가까운 대체는 `Sentry.getClient().getOptions().sendDefaultPii`         |

`Hub` 생성자도 사용 중단되었으며 다음 메이저 버전에서 제거될 예정입니다. 아래처럼 멀티 클라이언트 용도로 Hub를 생성하고 있다면:

```TypeScript
// OLD
const hub = new Hub();
hub.bindClient(client);
makeMain(hub);
```

대신 다음과 같이 클라이언트를 초기화하세요:

```TypeScript
// NEW
Sentry.withIsolationScope(() => {
  Sentry.setCurrentClient(client);
  client.init();
});
```

Hub를 사용해 아래처럼 이벤트를 캡처하고 있다면:

```TypeScript
// OLD
const client = new Client();
const hub = new Hub(client);
hub.captureException();
```

대신 다음과 같이 격리된 이벤트를 캡처하세요:

```TypeScript
// NEW
const client = new Client();
const scope = new Scope();
scope.setClient(client);
scope.captureException();
```

- [`addGlobalEventProcessor`를 사용 중단하고 `addEventProcessor` 권장](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-addglobaleventprocessor-in-favor-of-addeventprocessor)

*`7.85.0`에서 사용 중단 도입.*

`addGlobalEventProcessor` 대신 `addEventProcessor`를 사용하세요. 이는 이벤트 프로세서를 전역으로 추가하지 않고 현재 클라이언트에 추가합니다.

대부분의 경우 이들의 동작은 동일합니다. 여러 클라이언트를 사용하는 경우에만 차이가 있으며, 이 경우에도 어차피 전역이 아니라 클라이언트별로 이벤트 프로세서를 추가하는 것이 일반적으로 더 적절합니다.

v8에서는 전역 이벤트 프로세서를 전반적으로 제거할 예정이며, 이를 통해 필요하지 않은 전역 상태를 유지하지 않아도 됩니다.

- [`configureScope` 대신 `getCurrentScope()` 사용으로 전환](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-configurescope-in-favor-of-using-getcurrentscope)

*`7.89.0`에서 지원 중단이 도입되었습니다.*

`configureScope()`를 통해 콜백에서 scope를 업데이트하는 대신, `getCurrentScope()`로 scope에 접근해 직접 설정해야 합니다.

```js
Sentry.getCurrentScope().setTag("xx", "yy");
```

- [`pushScope` 및 `popScope` 대신 `withScope` 사용으로 전환](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-pushscope--popscope-in-favor-of-withscope)

*`7.89.0`에서 지원 중단이 도입되었습니다.*

scope를 수동으로 push/pop하는 대신 `Sentry.withScope(callback: (scope: Scope))`를 사용해야 합니다.

- [`startSpan()` API 인자 지원 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-arguments-for-startspan-apis)

*`7.93.0`에서 지원 중단이 도입되었습니다.*

v8에서는 새 span 시작 API가 현재 제공되는 옵션보다 축소됩니다. 앞으로 `startSpan()`, `startSpanManual()`, `startInactiveSpan()`에는 아래 인자만 전달할 수 있습니다.

* `name`
* `attributes`
* `origin`
* `op`
* `startTime`
* `scope`

- [`startTransaction()` 및 `span.startChild()` 지원 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-starttransaction--spanstartchild)

*`7.93.0`에서 지원 중단이 도입되었습니다.*

v8에서는 기존 성능 API인 `startTransaction()`(및 `hub.startTransaction()`), 그리고 `span.startChild()`가 제거됩니다. 대신 새 성능 API를 사용하세요.

* `startSpan()`
* `startSpanManual()`
* `startInactiveSpan()`

- [`tracesSampler`에 전달되던 `transactionContext` 지원 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecated-transactioncontext-passed-to-tracessampler)

*`7.100.0`에서 지원 중단이 도입되었습니다.*

앞으로 `tracesSampler` 콜백에는 `transactionContext` 대신 `name`과 `attributes`가 직접 전달됩니다. 이를 사용해 샘플링 결정을 내릴 수 있으며, `transactionContext`는 `8.x`에서 제거됩니다. `attributes`는 span 생성 시점의 속성만 포함하며, 일부 속성은 span 수명 주기 중 나중에 설정될 수 있으므로(즉, 샘플링 시점에는 사용할 수 없을 수 있음) 유의하세요.

- [`scope.getSpan()` 및 `scope.setSpan()` 지원 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-scopegetspan-and-scopesetspan)

*`7.93.0`에서 지원 중단이 도입되었습니다.*

대신 `Sentry.getActiveSpan()`을 통해 현재 활성 span을 가져올 수 있습니다. 새 성능 API인 `startSpan()`과 `startSpanManual()`을 사용하면 scope에 span을 설정하는 작업은 자동으로 처리됩니다.

- [`scope.getTransaction()` 및 `getActiveTransaction()` 지원 중단](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-scopegettransaction-and-getactivetransaction)

*`7.93.0`에서 지원 중단이 도입되었습니다.*

대신 활성 transaction에 의존하지 말고, 이를 대신 처리해 주는 `startSpan()` API를 사용해야 합니다.

