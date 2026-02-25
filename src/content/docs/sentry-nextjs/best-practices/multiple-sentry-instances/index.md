---
title: '여러 Sentry 인스턴스 | Next.js용 Sentry'
description: '여러 Sentry 클라이언트를 만드는 것은 예기치 않은 동작을 유발할 수 있으므로 일반적으로 권장되지 않습니다. Micro Frontends 또는 유사한 구성을 사용 중이라면, 여러 클라이언트를 사용하는 것보다 멀티플렉싱이 더 나은 해결책일 수 있습니다. 자세한 내용은...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/multiple-sentry-instances

# 여러 Sentry 인스턴스 | Next.js용 Sentry

여러 Sentry 클라이언트를 만드는 것은 예기치 않은 동작을 유발할 수 있으므로 일반적으로 **권장되지 않습니다**. Micro Frontends 또는 유사한 구성을 사용 중이라면, 여러 클라이언트를 사용하는 것보다 멀티플렉싱이 더 나은 해결책일 수 있습니다. 자세한 내용은 Best Practices의 [Micro Frontends](https://docs.sentry.io/platforms/javascript/best-practices/micro-frontends.md)를 확인하세요.

여러 Sentry 인스턴스를 서로 충돌 없이 관리하려면 직접 `Client`를 만들어야 합니다. 이렇게 하면 애플리케이션이 상위 애플리케이션 내부에 통합된 경우, 상위 애플리케이션의 오류가 추적되는 것도 방지할 수 있습니다. 상위 애플리케이션과의 충돌을 피하려면 전역 상태에 의존하는 통합도 제거해야 합니다.

이 예제에서는 `@sentry/browser`의 `BrowserClient`를 사용하지만, `@sentry/node`의 `NodeClient`에도 동일하게 적용할 수 있습니다.

```javascript
import {
  BrowserClient,
  defaultStackParser,
  getDefaultIntegrations,
  makeFetchTransport,
  Scope,
} from "@sentry/browser";

// filter integrations that use the global variable
const integrations = getDefaultIntegrations({}).filter(
  (defaultIntegration) => {
    return !["BrowserApiErrors", "Breadcrumbs", "GlobalHandlers"].includes(
      defaultIntegration.name,
    );
  },
);

const client = new BrowserClient({
  dsn: "___PUBLIC_DSN___",
  transport: makeFetchTransport,
  stackParser: defaultStackParser,
  integrations: integrations,
});

const scope = new Scope();
scope.setClient(client);

client.init(); // initializing has to be done after setting the client on the scope

// You can capture exceptions manually for this client like this:
scope.captureException(new Error("example"));
```

이제 다른 클라이언트에 영향을 주지 않고 원하는 대로 scope를 사용자 지정할 수 있습니다.

## [통합 처리하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/multiple-sentry-instances.md#dealing-with-integrations)

통합은 `Client`에서 설정됩니다. 여러 클라이언트를 다뤄야 한다면 통합 처리 방식이 올바르게 설정되어 있는지 반드시 확인해야 합니다.

브라우저 확장 프로그램이나 유사한 시나리오에서 Sentry를 사용하는 경우에는 이 방식을 권장하지 않습니다. 전역 통합 사용을 피할 수 없다면(예: 마이크로 프런트엔드 애플리케이션), 전역 통합을 실행하는 여러 scope와 함께 여러 클라이언트를 사용하는 동작 예제는 다음과 같습니다.

```javascript
import * as Sentry from "@sentry/browser";

// Very happy integration that'll prepend and append very happy stick figure to the message
function happyIntegration() {
  return {
    name: "Happy",
    setupOnce() {
      Sentry.addEventProcessor((event) => {
        const self = Sentry.getClient().getIntegration(HappyIntegration);
        // Run the integration ONLY if it was installed on the current client
        if (self) {
          event.message = `\\o/ ${event.message} \\o/`;
        }
        return event;
      });
    },
  };
}

// filter integrations that use the global variable
const integrations = Sentry.getDefaultIntegrations({}).filter(
  (defaultIntegration) => {
    return !["BrowserApiErrors", "Breadcrumbs", "GlobalHandlers"].includes(
      defaultIntegration.name,
    );
  },
);

const client1 = new Sentry.BrowserClient({
  dsn: "___PUBLIC_DSN___",
  transport: Sentry.makeFetchTransport,
  stackParser: Sentry.defaultStackParser,
  integrations: [...integrations, happyIntegration()],
  beforeSend(event) {
    console.log("client 1", event);
    return null; // Returning `null` prevents the event from being sent
  },
});
const scope1 = new Sentry.Scope();
scope1.setClient(client1);

const client2 = new Sentry.BrowserClient({
  dsn: "___PUBLIC_DSN___", // Can be a different DSN
  transport: Sentry.makeFetchTransport,
  stackParser: Sentry.defaultStackParser,
  integrations: [...integrations, happyIntegration()],
  beforeSend(event) {
    console.log("client 2", event);
    return null; // Returning `null` prevents the event from being sent
  },
});
const scope2 = new Sentry.Scope();
scope2.setClient(client2);

scope1.captureMessage("a");
scope1.setTag("a", "b");

scope2.captureMessage("x");
scope2.setTag("c", "d");
```

## [여러 클라이언트에서 `withScope` 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/multiple-sentry-instances.md#using-withscope-with-multiple-clients)

기본적으로 `Sentry.withScope()`는 현재 scope를 분기하고, 제공된 콜백 내부에만 적용되는 데이터를 추가할 수 있게 해줍니다. 멀티 클라이언트 구성에서 이를 활용하려면 `withScope`를 다음과 같이 사용할 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

// Multiple clients setup as described above
const scopeA = new Sentry.Scope();
const clientA = new Sentry.BrowserClient(clientOptions);
scopeA.setClient(clientA);
clientA.init();

// Want to fork scopeA?
const scopeA2 = scopeA.clone();
Sentry.withScope(scopeA2, () => {
  // scopeA2 is active in this callback
  // it is still attached to clientA
  scopeA2.setTag("key", "value");
  scopeA2.captureMessage("message");
  // Any event captured inside of this callback will have scopeA2 applied to it
});
```

