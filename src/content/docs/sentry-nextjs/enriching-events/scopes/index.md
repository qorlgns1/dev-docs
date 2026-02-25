---
title: '스코프 | Sentry for Next.js'
description: '이벤트가 캡처되어 Sentry로 전송되면, SDK는 해당 이벤트 데이터에 현재 스코프의 추가 정보를 병합합니다. SDK는 보통 프레임워크 통합에서 스코프를 자동으로 관리하므로, 일반적으로 이를 신경 쓸 필요는 없습니다. 다만 스코프가 무엇인지, 그리고 이를 어떻게 활용...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes

# 스코프 | Sentry for Next.js

이벤트가 캡처되어 Sentry로 전송되면, SDK는 해당 이벤트 데이터에 현재 스코프의 추가 정보를 병합합니다. SDK는 보통 프레임워크 통합에서 스코프를 자동으로 관리하므로, 일반적으로 이를 신경 쓸 필요는 없습니다. 다만 스코프가 무엇인지, 그리고 이를 어떻게 활용할 수 있는지는 알아두는 것이 좋습니다.

## [스코프란 무엇인가요?](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#whats-a-scope)

스코프에는 이벤트와 함께 전송되는 유용한 정보가 담깁니다. 예를 들어 [contexts](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/context.md)와 [breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md)는 스코프에 저장됩니다. 스코프가 포크되면 부모 스코프의 모든 데이터를 상속받습니다.

기본 SDK 통합은 스코프를 지능적으로 포크합니다. 예를 들어 웹 프레임워크 통합은 라우트나 요청 핸들러 단위로 스코프를 포크합니다.

## [스코프 동작 방식](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#how-scopes-work)

스코프는 기본적으로 이벤트에 연결되는 데이터 스택입니다. 이벤트가 캡처되면 SDK는 활성 스코프들의 데이터를 이벤트에 병합합니다. 이를 통해 이벤트가 캡처된 컨텍스트와 관련된 데이터를 이벤트에 첨부할 수 있습니다.

스코프는 일반적으로 콜백 또는 실행 컨텍스트 내부에서 유효합니다. 즉, 애플리케이션의 여러 부분에서 동시에 서로 다른 스코프가 활성화될 수 있습니다. 예를 들어 웹 서버는 동시에 여러 요청을 처리할 수 있으며, 각 요청은 이벤트에 적용할 서로 다른 스코프 데이터를 가질 수 있습니다.

## [스코프의 종류](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#different-kinds-of-scopes)

Sentry SDK에는 세 가지 종류의 스코프가 있습니다:

* [글로벌 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#global-scope)
* [격리 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#isolation-scope)
* [현재 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#current-scope)

- [글로벌 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#global-scope)

글로벌 스코프는 이벤트가 어디서 발생했는지와 관계없이 *모든* 이벤트에 적용됩니다. 환경 정보처럼 모든 이벤트에 적용되어야 하는 데이터를 저장하는 데 사용할 수 있습니다.

글로벌 스코프는 `Sentry.getGlobalScope()`로 접근할 수 있습니다.

글로벌 스코프는 이벤트 캡처가 아니라 데이터 쓰기에만 사용할 수 있다는 점에 유의하세요. 이벤트는 현재 스코프에서만 캡처할 수 있습니다(예: `getCurrentScope().captureException()` 및 유사 API).

- [격리 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#isolation-scope)

격리 스코프는 이벤트를 서로 분리하는 데 사용됩니다. 예를 들어 웹 서버의 각 요청은 자체 격리 스코프를 가질 수 있으므로, 한 요청의 이벤트가 다른 요청의 이벤트와 간섭하지 않습니다. 대부분의 경우 이벤트에 적용되어야 하는 데이터는 격리 스코프에 두는 것이 좋습니다. 이 때문에 `Sentry.setTag()` 같은 모든 `Sentry.setXXX` 메서드는 현재 활성화된 격리 스코프에 데이터를 기록합니다. 격리 스코프에 속하는 대표적인 데이터는 사용자입니다. 각 요청마다 사용자가 다를 수 있으므로, 사용자를 격리 스코프에 설정해야 합니다.

격리 스코프는 `Sentry.getIsolationScope()`로 접근할 수 있지만, 일반적으로는 현재 활성화된 격리 스코프에 데이터를 설정하는 `Sentry.setXXX` 메서드를 사용하면 됩니다:

```javascript
Sentry.setTag("my-tag", "my value");
// Is identical to:
Sentry.getIsolationScope().setTag("my-tag", "my value");
```

브라우저에서는 격리 스코프가 포크되지 않습니다. 격리 스코프가 어디에 속하는지 추적하는 것이 불가능하기 때문입니다. 따라서 브라우저에서 격리 스코프는 사실상 글로벌 스코프입니다.

격리 스코프 역시 이벤트 캡처가 아니라 데이터 쓰기에만 사용할 수 있다는 점에 유의하세요. 이벤트는 현재 스코프에서만 캡처할 수 있습니다(예: `getCurrentScope().captureException()` 및 유사 API).

- [현재 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#current-scope)

현재 스코프는 지금 활성화된 로컬 스코프입니다. 포크가 드문 격리 스코프와 달리, 현재 스코프는 내부적으로 더 자주 포크될 수 있습니다. 특정 이벤트에만 적용되어야 하는 데이터를 저장하는 데 사용할 수 있습니다. 대부분의 경우 이 스코프에 직접 접근하기보다, 코드의 특정 부분에서만 활성화되는 새 스코프를 만들기 위해 `Sentry.withScope`를 사용해야 합니다:

```javascript
Sentry.withScope((scope) => {
  // scope is the current scope inside of this callback!
  scope.setTag("my-tag", "my value");
  // this tag will only be applied to events captured inside of this callback
  // the following event will have the tag:
  Sentry.captureException(new Error("my error"));
});
// this event will not have the tag:
Sentry.captureException(new Error("my other error"));
```

현재 스코프는 `Sentry.getCurrentScope()`로 접근할 수 있지만, 대부분의 경우 이 API를 사용하기보다 `withScope`를 사용해 로컬 스코프를 생성하고 접근해야 합니다. 애플리케이션의 여러 부분에서 `getCurrentScope`의 일관성은 보장되지 않으며, 내부적으로 다양한 지점에서 스코프 포크가 발생할 수 있습니다.

## [스코프 데이터가 이벤트에 적용되는 방식](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#how-scope-data-is-applied-to-events)

이벤트(예: 오류 또는 트랜잭션)가 Sentry로 전송되기 전에, 현재 활성화된 스코프들이 이벤트에 적용됩니다.

먼저 글로벌 스코프가 적용되고, 그다음 격리 스코프, 마지막으로 현재 스코프가 적용됩니다. 즉 현재 스코프에 설정한 데이터가 격리 스코프와 글로벌 스코프의 데이터보다 우선합니다:

```javascript
Sentry.getGlobalScope().setExtras({
  shared: "global",
  global: "data",
});
Sentry.getIsolationScope().setExtras({
  shared: "isolation",
  isolation: "data",
});
Sentry.getCurrentScope().setExtras({
  shared: "current",
  current: "data",
});

Sentry.captureException(new Error("my error"));
// --> Will have the following extra:
// { shared: 'current', global: 'data', isolation: 'data', current: 'data' }
```

## [스코프 구성하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#configuring-the-scope)

대부분의 경우 `Sentry.setTag()` 같은 최상위 메서드를 직접 사용해야 하며, 이렇게 하면 데이터가 격리 스코프에 설정되어 현재 요청/프로세스와 관련된 모든 이벤트에 적용됩니다.

더 좁은 범위에 데이터를 적용하려면 `withScope`를 사용해 코드의 특정 부분에서만 활성화되는 새 스코프를 만들 수 있습니다. `withScope`는 콜백 인자로 스코프를 전달하며, 이를 사용해 스코프에 데이터를 설정할 수 있습니다.

```javascript
import * as Sentry from "@sentry/nextjs";
```

예를 들어 사용자 정의 태그를 추가하거나, 현재 인증된 사용자 정보를 Sentry에 알릴 수 있습니다.

```javascript
Sentry.setTag("my-tag", "my value");
Sentry.setUser({
  id: 42,
  email: "john.doe@example.com",
});

// Alternatively, you can use `withScope` as documented below.
```

스코프에 어떤 유용한 정보를 연결할 수 있는지 알아보려면 [context](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/context.md), [tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/tags.md), [users](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/identify-user.md), [breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md)를 참고하세요.

`getCurrentScope()`를 사용해 데이터를 설정하는 방식은 현재 스코프의 수명이 신뢰하기 어려울 수 있으므로 피하는 것을 권장합니다. 대신:

* 현재 요청/프로세스(Node) 또는 현재 페이지 뷰(브라우저)에 데이터를 적용하려면, `Sentry.setTag()` 같은 최상위 메서드를 사용하세요.
* 이벤트가 어디서 캡처되었는지와 상관없이 모든 이벤트에 데이터를 적용하려면, `getGlobalScope().setTag()` 같은 글로벌 스코프 메서드를 사용하세요.
* 더 좁은 범위에 데이터를 적용하려면, `withScope`를 사용해 코드의 특정 부분에서만 활성화되는 새 스코프를 만드세요.

## [`withScope` 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#using-withscope)

다음 예시에서는 `withScope`를 사용해 특정 오류 하나에만 `level`과 `tag`를 첨부합니다:

```javascript
Sentry.withScope(function (scope) {
  scope.setTag("my-tag", "my value");
  scope.setLevel("warning");
  // will be tagged with my-tag="my value"
  Sentry.captureException(new Error("my error"));
});

// will not be tagged with my-tag
Sentry.captureException(new Error("my other error"));
```

`withScope()` 콜백 내부의 스코프는 콜백 내부에서만 유효합니다. 콜백이 끝나면 해당 스코프는 제거되어 더 이상 적용되지 않습니다. 내부 스코프는 콜백 내부에서 캡처된 이벤트에만 적용됩니다. `withScope()`는 현재 스코프를 복제(또는 포크)하므로 현재 스코프 자체는 수정되지 않습니다. 이를 통해 코드의 특정 위치에 컨텍스트 정보를 더 쉽게 격리할 수 있고, 필요하면 `clear`를 호출해 모든 컨텍스트 정보를 잠시 제거할 수도 있습니다.

## [`withIsolationScope` 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#using-withisolationscope)

`withIsolationScope`는 기본적으로 `withScope`와 동일하게 동작하지만, 현재 스코프 대신 격리 스코프를 포크합니다. 일반적으로 격리 스코프는 현재 스코프보다 덜 자주 포크되도록 설계되어 있으며, 대부분의 경우 SDK가 이를 자동으로 처리합니다.

하지만 예를 들어 요청 기반이 아닌 프로세스(예: 백그라운드 작업)를 격리하고 싶다면, 콜백 실행 시간 동안만 활성화되는 새 격리 스코프를 만들기 위해 `withIsolationScope`를 사용할 수 있습니다:

```javascript
Sentry.withIsolationScope(function () {
  // This user & tag is set inside of this callback
  Sentry.setUser({ id: "123" });
  Sentry.setTag("my-tag", "my value");

  // will be tagged with my-tag="my value" & user
  Sentry.captureException(new Error("my error"));
});

// will not be tagged with my-tag & user
Sentry.captureException(new Error("my other error"));
```

