---
title: 'InboundFilters | Next.js용 Sentry'
description: '이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 여기를 읽어보세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters

# InboundFilters | Next.js용 Sentry

*Import name: `Sentry.inboundFiltersIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

이 통합을 사용하면 주어진 예외에서 타입, 메시지 또는 URL을 기준으로 특정 오류를 무시할 수 있습니다.

기본적으로 `Script error` 또는 `JavaScript error: Script error`로 시작하는 오류를 무시합니다.

이 통합을 구성하려면 `ignoreErrors`, `ignoreTransactions`, `denyUrls`, `allowUrls` SDK 옵션을 직접 사용하세요. 예:

```javascript
Sentry.init({
  ignoreErrors: ["ignore-this-error"],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#options)

이 옵션들은 통합이 아니라 루트 `Sentry.init` 호출에 전달해야 한다는 점을 기억하세요!

- [`ignoreErrors`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#ignoreerrors)

*Type: `(string|RegExp)[]`*

Sentry로 전송되지 않아야 하는 오류 메시지와 일치하는 문자열 또는 정규식 패턴 목록입니다. 이 문자열 또는 정규식과 일치하는 메시지는 Sentry로 전송되기 전에 필터링됩니다. 문자열을 사용할 경우 부분 일치도 필터링되므로, 정확히 일치하는 항목만 필터링해야 한다면 대신 정규식 패턴을 사용하세요. 기본값은 모든 오류를 전송하는 것입니다.

- [`ignoreTransactions`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#ignoretransactions)

*Type: `(string|RegExp)[]`*

Sentry로 전송되지 않아야 하는 트랜잭션 이름과 일치하는 문자열 또는 정규식 패턴 목록입니다. 이 문자열 또는 정규식과 일치하는 트랜잭션은 Sentry로 전송되기 전에 필터링됩니다. 문자열을 사용할 경우 부분 일치도 필터링되므로, 정확히 일치하는 항목만 필터링해야 한다면 대신 정규식 패턴을 사용하세요. 기본적으로 일반적인 API 상태 확인 요청에 해당하는 트랜잭션은 필터링됩니다.

- [`allowUrls`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#allowurls)

*Type: `(string|RegExp)[]`*

오류가 생성된 스크립트 URL과 일치하는 문자열 또는 정규식 패턴의 배열입니다. 이 URL들에서 생성된 오류만 Sentry로 전송됩니다. 이 옵션을 사용하면 상단 스택 프레임 파일 URL이 allowUrls 배열의 항목 중 하나 이상을 포함하거나 일치할 때만 오류가 전송됩니다. 배열의 모든 문자열 항목은 `stackFrameUrl.contains(entry)`로, 모든 RegEx 항목은 `stackFrameUrl.match(entry)`로 매칭됩니다.

예를 들어 배열에 `'foo.com'`을 추가하면, URL이 "contains" 로직으로 매칭되고 URL의 마지막 세그먼트에 `foo.com`이 포함되어 있으므로 `https://bar.com/myfile/foo.com`에서 생성된 오류가 수집됩니다.

이 매칭 로직은 raw message 이벤트가 아니라 캡처된 예외에 적용됩니다. 기본값은 모든 오류를 전송하는 것입니다.

스크립트가 `cdn.example.com`에서 로드되고 사이트가 `example.com`인 경우, 다음과 같이 `allowUrls`를 설정하면 이 위치들의 스크립트에서 생성된 오류만 선택적으로 수집할 수 있습니다:

```javascript
Sentry.init({
  allowUrls: [/https?:\/\/((cdn|www)\.)?example\.com/],
});
```

- [`denyUrls`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md#denyurls)

*Type: `(string|RegExp)[]`*

오류가 생성된 스크립트 URL과 일치하는 문자열 또는 정규식 패턴의 배열입니다. 이 URL들에서 생성된 오류는 Sentry로 전송되지 않습니다. 이 옵션을 사용하면 상단 스택 프레임 파일 URL이 `denyUrls` 배열의 항목 중 하나 이상을 포함하거나 일치할 때 오류가 전송되지 않습니다. 배열의 모든 문자열 항목은 `stackFrameUrl.contains(entry)`로, 모든 RegEx 항목은 `stackFrameUrl.match(entry)`로 매칭됩니다.

이 옵션은 오류가 보고된 HTTP URL이 아니라 스택 트레이스의 소스 파일 URL을 확인합니다. 더 세밀한 필터링이 필요하면 [beforeSend](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#beforeSend)를 참고하세요.

이 매칭 로직은 raw message 이벤트가 아니라 캡처된 예외에 적용됩니다. 기본값은 모든 오류를 전송하는 것입니다.

