---
title: '민감 데이터 스크러빙 | Next.js용 Sentry'
description: '모든 서드파티 서비스와 마찬가지로, 어떤 데이터가 Sentry로 전송되는지 이해하고, 관련이 있다면 민감한 데이터가 Sentry 서버에 아예 도달하지 않도록 하거나 최소한 저장되지 않도록 보장하는 것이 중요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/sensitive-data

# 민감 데이터 스크러빙 | Next.js용 Sentry

모든 서드파티 서비스와 마찬가지로, 어떤 데이터가 Sentry로 전송되는지 이해하고, 관련이 있다면 민감한 데이터가 Sentry 서버에 아예 도달하지 않도록 하거나 최소한 저장되지 않도록 보장하는 것이 중요합니다.

모든 회사가 데이터 스크러빙을 고려해야 하는 대표적인 예시는 다음과 같습니다.

* 사용자의 이름이나 이메일 주소 같은 PII(개인 식별 정보). GDPR 이후에는 모든 회사가 반드시 신경 써야 합니다.
* AWS 비밀번호나 키 같은 인증 자격 증명.
* 좋아하는 색깔이나 세계 정복 계획처럼 기밀 IP(지적 재산).

법적 및 운영 요구사항에 따라 다음과 같은 옵션을 제공합니다.

* SDK 내부에서 민감 데이터를 필터링하거나 스크러빙하여 데이터가 Sentry로 *전송되지 않도록* 합니다. SDK마다 지원 기능이 다르며, 설정 변경 시 애플리케이션 재배포가 필요합니다.
* [서버 사이드 스크러빙 구성](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md)을 통해 Sentry가 데이터를 *저장하지 않도록* 보장합니다. 설정 변경은 Sentry UI에서 수행되며 새 이벤트에 즉시 적용됩니다.
* SDK와 Sentry 사이에 자체 서버에서 [로컬 Relay 실행](https://docs.sentry.io/product/relay.md)하여 데이터가 Sentry로 *전송되지 않도록* 하면서도 배포 없이 설정을 적용할 수 있습니다.

팀이 회사의 Sentry 전송 가능/불가 데이터 정책을 인지하고 있도록 하세요. 구현 초기 단계에서 이 정책을 결정하고, 팀에 공유하며 코드 리뷰를 통해 강제하는 것을 권장합니다.

모바일 앱에서 Sentry를 사용 중이라면, Apple App Store 및 Google Play 앱 개인정보 보호 항목 작성을 위해 [모바일 데이터 프라이버시에 관한 자주 묻는 질문](https://docs.sentry.io/security-legal-pii/security/mobile-privacy.md)을 확인하세요.

기본 PII 동작을 원하지 않는다면, [사용자 식별 컨텍스트](https://docs.sentry.io/platforms/javascript/guides/koa/enriching-events/identify-user.md)를 사용해 더 통제된 방식으로 사용자를 식별할 수도 있습니다.

## [데이터 스크러빙](https://docs.sentry.io/platforms/javascript/guides/koa/data-management/sensitive-data.md#scrubbing-data)

- [`beforeSend` & `beforeSendTransaction`](https://docs.sentry.io/platforms/javascript/guides/koa/data-management/sensitive-data.md#before-send-before-send-transaction)

SDK는 오류 또는 메시지 이벤트가 전송되기 전에 호출되는 `beforeSend` 훅을 제공하며, 이를 사용해 이벤트 데이터를 수정하여 민감 정보를 제거할 수 있습니다. 일부 SDK는 트랜잭션에 대해 동일한 작업을 수행하는 `beforeSendTransaction` 훅도 제공합니다. 민감 데이터가 로컬 환경을 절대 벗어나지 않도록, SDK의 `beforeSend` 및 `beforeSendTransaction`을 사용해 **전송 전에 모든 데이터를 스크러빙**할 것을 권장합니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSend(event) {
    if (event.user) {
      // Don't send user's email address
      delete event.user.email;
    }
    return event;
  },
});
```

민감 데이터는 다음 영역에 나타날 수 있습니다.

* Stack-locals → 일부 SDK(Python, PHP, Node)는 스택 트레이스 내 변수 값을 수집합니다. 이 값들은 스크러빙할 수 있으며, 필요하다면 이 동작 자체를 비활성화할 수도 있습니다.
* Breadcrumbs → 일부 SDK(예: JavaScript, Java 로깅 통합)는 이전에 실행된 로그 구문을 수집합니다. 이 기능을 사용해 로그 구문을 이벤트의 breadcrumb로 포함한다면 **PII를 로그에 남기지 마세요**. 일부 백엔드 SDK는 데이터베이스 쿼리도 기록하며, 이 역시 스크러빙이 필요할 수 있습니다. 대부분의 SDK는 HTTP 쿼리 문자열과 프래그먼트를 breadcrumb의 데이터 속성으로 추가하므로, 이것도 스크러빙이 필요할 수 있습니다.
* User context → 자동 동작은 `sendDefaultPii`로 제어됩니다.
* HTTP context → 일부 프레임워크에서는 HTTP 요청 컨텍스트의 일부로 쿼리 문자열이 수집될 수 있습니다.
* Transaction Names → 특정 상황에서는 트랜잭션 이름에 민감 데이터가 포함될 수 있습니다. 예를 들어 브라우저의 pageload 트랜잭션 이름이 `/users/1234/details` 같은 원시 URL일 수 있습니다(`1234`는 사용자 ID이며 PII로 간주될 수 있음). 대부분의 경우 SDK가 URL과 라우트를 파라미터화하여 `/users/1234/details`를 `/users/:userid/details`로 변환할 수 있습니다. 하지만 프레임워크, 라우팅 설정, 경쟁 상태, 기타 요인에 따라 SDK가 모든 URL을 완전히 파라미터화하지 못할 수도 있습니다.
* HTTP Spans → 대부분의 SDK는 HTTP 쿼리 문자열과 프래그먼트를 데이터 속성으로 포함하므로, HTTP span도 스크러빙이 필요할 수 있습니다.

자세한 내용과 데이터 필터링 방법은 [이벤트 필터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md)을 참고하세요.

- [예시](https://docs.sentry.io/platforms/javascript/guides/koa/data-management/sensitive-data.md#examples)

**컨텍스트 정보**

기밀 정보를 평문으로 전송하는 대신, 해시 처리하는 것을 고려하세요.

```javascript
Sentry.setTag("birthday", checksumOrHash("08/12/1990"));
```

이렇게 하면 필요 시 내부 시스템에서 상호 연관 지을 수 있으면서도, Sentry에는 기밀 상태를 유지할 수 있습니다.

**사용자 상세 정보**

조직 정책상 이메일을 기밀로 보지 않을 수도 있지만, 기밀이라면 내부 식별자를 대신 전송하는 것을 고려하세요.

```javascript
Sentry.setUser({ id: user.id });

// or

Sentry.setUser({ username: user.username });
```

이렇게 하면 사용자 영향 관련 기능의 이점은 그대로 유지할 수 있습니다.

**로깅 통합**

모범 사례로서 기밀 정보를 로그에 남기지 않는 것이 항상 바람직합니다. 레거시 시스템 때문에 우회가 필요하다면 다음을 고려하세요.

* 로그 구문 내 기밀 정보를 익명화합니다(예: 이메일 주소를 내부 식별자로 교체).
* `beforeBreadcrumb`를 사용해 breadcrumb에 첨부되기 전에 필터링합니다.
* 로깅 breadcrumb 통합을 비활성화합니다(예: [여기](https://docs.sentry.io/platforms/javascript/configuration/integrations/breadcrumbs.md) 설명된 방식).

