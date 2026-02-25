---
title: '공유 환경 / 브라우저 확장 프로그램 | Sentry for Next.js'
description: '공유 환경에서 SDK를 사용할 때는 JavaScript SDK  이상 사용을 권장합니다. 이전 SDK 버전에서  이상으로 업그레이드하려면 마이그레이션 문서를 확인하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments

# 공유 환경 / 브라우저 확장 프로그램 | Sentry for Next.js

공유 환경에서 SDK를 사용할 때는 JavaScript SDK `8.x` 이상 사용을 권장합니다. 이전 SDK 버전에서 `8.x` 이상으로 업그레이드하려면 [마이그레이션 문서](https://docs.sentry.io/platforms/javascript/migration.md)를 확인하세요.

다음 사용 사례 중 하나로 Sentry를 설정했다면, 아래 모범 사례가 해당됩니다.

* 브라우저 확장 프로그램
* VSCode 확장 프로그램
* 서드파티 위젯
* 플러그인 아키텍처
* 라이브러리
* 동일한 환경에서 여러 Sentry 인스턴스가 실행될 수 있는 기타 모든 시나리오

여러 Sentry 인스턴스가 실행될 수 있는 공유 환경에서 Sentry를 설정할 때는 전역 상태를 오염시키므로 **`Sentry.init()`를 사용하면 안 됩니다**. 예를 들어 브라우저 확장 프로그램이 `Sentry.init()`를 사용하고 웹사이트도 Sentry를 사용하는 경우, 확장 프로그램 이벤트가 웹사이트의 Sentry 프로젝트로 전송되거나 그 반대로 전송될 수 있습니다.

## [공유 환경 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#shared-environment-setup)

위에 나열한 사용 사례에서는 아래 예시처럼 클라이언트를 수동으로 설정하세요. 또한 `Breadcrumbs`나 `GlobalHandlers`처럼 전역 상태를 사용하는 통합은 추가하지 마세요(아래 코드 스니펫 참고). 더불어 전역 상태를 사용하는 일부 기본 통합은 아래 예시처럼 필터링해야 합니다. 이런 시나리오에서는 어떤 통합도 사용하지 않고, 오류를 수동으로 캡처하는 방식에 의존하는 것이 모범 사례입니다.

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
    return ![
      "BrowserApiErrors",
      "BrowserSession",
      "Breadcrumbs",
      "ConversationId",
      "GlobalHandlers",
      "FunctionToString",
    ].includes(defaultIntegration.name);
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

설정을 조금 더 단순하게 하면서도 어느 정도 "Let Sentry handle unhandled errors"를 유지하려면 다음 코드를 사용할 수 있습니다.

```javascript
// Init Sentry as shown above

try {
  // Your goes code here
  // as in import and execute your code here
  // and if an error occurs, Sentry will capture it
} catch (error) {
  scope.captureException(error);
}
```

## [공유 환경에서 로그 전송하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#sending-logs-from-shared-environments)

공유 환경에서 동작하도록 logger API 메서드에 scope를 직접 전달할 수 있습니다.

```js
const scope = new Scope();
scope.setClient(client);

client.init(); // initializing has to be done after setting the client on the scope

Sentry.logger.info("my logger message", {}, { scope });
```

## [브라우저 확장 프로그램 필터](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#browser-extension-filter)

브라우저 확장 프로그램에서 발생한 오류 이벤트를 Sentry가 캡처하지 않는다면 Inbound Filter가 활성화되어 있을 수 있습니다. **Project Settings > Inbound Filters**로 이동해 브라우저 확장 프로그램으로 인해 발생한 것으로 알려진 오류를 필터링하는 옵션을 비활성화하면 됩니다.

Inbound Filters에 대한 자세한 내용은 제품 문서의 [Inbound filters](https://docs.sentry.io/concepts/data-management/filtering.md#inbound-data-filters)를 참고하세요.

## [브라우저 확장 프로그램 검사 건너뛰기](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/shared-environments.md#skipping-the-browser-extension-check)

*`8.37.0` 버전부터 모든 브라우저 기반 SDK에서 사용 가능*

어떤 이유로 SDK가 브라우저 확장 프로그램에서 초기화되었다고 잘못 감지하는 경우, SDK 초기화 시 `skipBrowserExtensionCheck` 옵션을 지정해 해당 검사를 건너뛸 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  skipBrowserExtensionCheck: true,
  // ...
});
```

실제로 브라우저 확장 프로그램이나 다른 공유 환경에서 SDK를 사용 중이라면 이 옵션을 사용하면 안 됩니다. 이 페이지에서 설명한 것처럼 클라이언트와 scope를 수동으로 설정하는 것에 비해 `Sentry.init`로 SDK를 초기화할 때의 장점은 없습니다. 그렇게 하면 조치 불가능한 이슈로 인한 할당량 증가, 다른 Sentry SDK와의 간섭, 데이터 유출 위험이 생깁니다.

이 옵션은 브라우저 확장 프로그램 검사에서 브라우저 확장 프로그램을 잘못 감지했을 때를 위한 순수한 예외 탈출구입니다. 예를 들어 브라우저 확장 프로그램과 유사한 전역 API를 노출하는 크로스 플랫폼 애플리케이션 프레임워크에서 이런 상황이 발생할 수 있습니다.

