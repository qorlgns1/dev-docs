---
title: '이벤트 핑거프린팅 | Next.js용 Sentry'
description: '모든 이벤트에는 핑거프린트가 있습니다. 동일한 핑거프린트를 가진 이벤트는 하나의 이슈로 함께 그룹화됩니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting

# 이벤트 핑거프린팅 | Next.js용 Sentry

모든 이벤트에는 핑거프린트가 있습니다. 동일한 핑거프린트를 가진 이벤트는 하나의 이슈로 함께 그룹화됩니다.

기본적으로 Sentry는 `stacktrace`, `exception`, `message` 같은 이벤트 내에서 사용 가능한 정보를 바탕으로 핑거프린트를 생성하기 위해 내장된 그룹화 알고리즘 중 하나를 실행합니다. 기본 그룹화 동작을 확장하거나 완전히 변경하려면 다음 옵션을 조합해 사용할 수 있습니다.

1. 아래 문서에 설명된 대로 SDK에서 SDK Fingerprinting 사용
2. 프로젝트에서 [Fingerprint Rules](https://docs.sentry.io/concepts/data-management/event-grouping/fingerprint-rules.md) 또는 [Stack Trace Rules](https://docs.sentry.io/concepts/data-management/event-grouping/stack-trace-rules.md) 사용

지원되는 SDK에서는 핑거프린트 속성을 문자열 배열로 전달하여 Sentry의 기본 그룹화를 재정의할 수 있습니다. 핑거프린트 배열의 길이에는 제한이 없습니다. 이는 항상 사용 가능하며 유사한 결과를 얻을 수 있는 [fingerprint rules functionality](https://docs.sentry.io/concepts/data-management/event-grouping/fingerprint-rules.md)와 비슷하게 동작합니다.

## [기본 예제](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md#basic-example)

가장 기본적인 경우에는 값을 직접 전달합니다.

```javascript
function makeRequest(method, path, options) {
  return fetch(method, path, options).catch(function (err) {
    Sentry.withScope(function (scope) {
      // group errors together based on their request and response
      scope.setFingerprint([method, path, String(err.statusCode)]);
      Sentry.captureException(err);
    });
  });
}
```

일반적으로 서버에서 계산되는 핑거프린트에 동적 값을 채우기 위해 변수 치환을 사용할 수 있습니다. 예를 들어, `{{ default }}` 값을 추가하면 일반적으로 생성되는 전체 그룹화 해시를 핑거프린트에 포함할 수 있습니다. 이 값들은 서버 측 핑거프린팅에서 사용하는 값과 동일합니다. 자세한 내용은 [Variables](https://docs.sentry.io/concepts/data-management/event-grouping/fingerprint-rules.md#variables)를 참조하세요.

## [더 세밀하게 오류 그룹화하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md#group-errors-with-greater-granularity)

일부 시나리오에서는 오류를 더 세밀하게 그룹화하고 싶을 수 있습니다.

예를 들어, 애플리케이션이 Remote Procedure Call Model (RPC) 인터페이스나 외부 Application Programming Interface (API) 서비스를 조회하는 경우, 나가는 요청이 매우 다르더라도 스택 트레이스는 일반적으로 동일합니다.

다음 예제는 Sentry가 기본적으로 생성하는 그룹(`{{ default }}`로 표시됨)을 오류 객체의 일부 속성을 고려해 더 세분화합니다.

```javascript
class MyRPCError extends Error {
  constructor(message, functionName, errorCode) {
    super(message);

    // The name of the RPC function that was called (e.g. "getAllBlogArticles")
    this.functionName = functionName;

    // For example a HTTP status code returned by the server.
    this.errorCode = errorCode;
  }
}

Sentry.init({
  // ...
  beforeSend: function (event, hint) {
    const exception = hint.originalException;

    if (exception instanceof MyRPCError) {
      event.fingerprint = [
        "{{ default }}",
        String(exception.functionName),
        String(exception.errorCode),
      ];
    }

    return event;
  },
});
```

## [오류를 더 공격적으로 그룹화하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md#group-errors-more-aggressively)

Sentry의 그룹화를 완전히 덮어쓸 수도 있습니다.

예를 들어, 데이터베이스 연결 오류 같은 일반적인 오류에 서로 다른 스택 트레이스가 많아 하나로 그룹화되지 않는다면, 배열에서 `{{ default }}`를 생략해 Sentry의 그룹화를 덮어쓸 수 있습니다.

```javascript
class DatabaseConnectionError extends Error {}

Sentry.init({
  // ...
  beforeSend: function (event, hint) {
    const exception = hint.originalException;

    if (exception instanceof DatabaseConnectionError) {
      event.fingerprint = ["database-connection-error"];
    }

    return event;
  },
});
```

