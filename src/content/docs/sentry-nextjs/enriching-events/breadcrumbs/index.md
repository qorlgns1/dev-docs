---
title: '브레드크럼 | Next.js용 Sentry'
description: "수동 브레드크럼도 충분히 잘해왔지만, 이제 Sentry's got logs를 사용할 수 있습니다. 구조화되어 있고, 검색 가능하며, 알림 설정이나 쿼리도 훨씬 쉽습니다. 확인해 보세요!"
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs

# 브레드크럼 | Next.js용 Sentry

##### 잠깐... 혹시 Logs를 말하려던 건가요? 이제 Sentry에 있습니다!

수동 브레드크럼도 충분히 잘해왔지만, 이제 [Sentry's got logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md)를 사용할 수 있습니다. 구조화되어 있고, 검색 가능하며, 알림 설정이나 쿼리도 훨씬 쉽습니다. 확인해 보세요!

Sentry는 이슈가 발생하기 전에 어떤 일이 있었는지의 흐름을 만들기 위해 *breadcrumbs*를 사용합니다. 이러한 이벤트는 전통적인 로그와 매우 유사하지만, 더 풍부한 구조화 데이터를 기록할 수 있습니다.

이 페이지에서는 수동 브레드크럼 기록과 커스터마이징을 개괄적으로 설명합니다. **Issue Details** 페이지에 표시되는 정보와 브레드크럼을 필터링해 이슈를 빠르게 해결하는 방법은 [Using Breadcrumbs](https://docs.sentry.io/product/error-monitoring/breadcrumbs.md)에서 자세히 확인하세요.

##### SDK 사용법 알아보기

브레드크럼 인터페이스를 수정하려는 개발자는 [Breadcrumbs Interface에 대한 개발자 문서](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/breadcrumbs/)에서 더 자세히 확인할 수 있습니다.

## [수동 브레드크럼](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md#manual-breadcrumbs)

흥미로운 일이 발생할 때마다 브레드크럼을 수동으로 추가할 수 있습니다. 예를 들어, 사용자가 인증을 완료했거나 다른 상태 변화가 발생했을 때 브레드크럼을 수동으로 기록할 수 있습니다.

먼저, 평소처럼 SDK를 import해야 합니다:

```javascript
import * as Sentry from "@sentry/nextjs";
```

브레드크럼을 수동으로 기록합니다:

```javascript
Sentry.addBreadcrumb({
  category: "auth",
  message: "Authenticated user " + user.email,
  level: "info",
});
```

사용 가능한 브레드크럼 키는 `type`, `category`, `message`, `level`, `timestamp`(많은 SDK에서 자동으로 설정), `data`입니다. `data`에는 브레드크럼에 포함하고 싶은 추가 정보를 넣으면 됩니다. 이 여섯 가지 외의 키를 사용해도 오류가 발생하지는 않지만, 이벤트가 Sentry에서 처리될 때 해당 데이터는 버려집니다.

브레드크럼 로그 레벨은 `"fatal"`, `"error"`, `"warning"`, `"log"`, `"info"`, `"debug"` 중에서 선택할 수 있습니다.

## [자동 브레드크럼](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md#automatic-breadcrumbs)

SDK와 관련 통합은 다양한 유형의 브레드크럼을 자동으로 기록합니다. 예를 들어, 브라우저 JavaScript SDK는 DOM 요소의 클릭 및 키 입력, XHR/fetch 요청, console API 호출, 모든 위치 변경을 자동으로 기록합니다.

## [브레드크럼 커스터마이즈](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md#customize-breadcrumbs)

SDK는 `beforeBreadcrumb` hook을 통해 브레드크럼을 커스터마이즈할 수 있게 해줍니다.

먼저, 평소처럼 SDK를 import해야 합니다:

```javascript
import * as Sentry from "@sentry/nextjs";
```

이 hook에는 이미 구성된 브레드크럼과, 일부 SDK의 경우 선택적 힌트가 전달됩니다. 이 함수는 브레드크럼을 수정하거나 `null`을 반환해 완전히 폐기하도록 결정할 수 있습니다:

```javascript
Sentry.init({
  // ...
  beforeBreadcrumb(breadcrumb, hint) {
    return breadcrumb.category === "ui.click" ? null : breadcrumb;
  },
});
```

힌트로 무엇을 할 수 있는지에 대한 정보는 [Filtering Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints)를 참고하세요.

