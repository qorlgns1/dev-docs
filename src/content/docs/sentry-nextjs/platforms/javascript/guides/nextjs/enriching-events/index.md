---
title: '이벤트 보강 | Next.js용 Sentry'
description: 'Sentry SDK가 자동으로 수집하는 데이터에 더해, 디버깅에 도움이 되도록 이벤트에 추가 데이터를 넣을 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events

# 이벤트 보강 | Next.js용 Sentry

Sentry SDK가 자동으로 수집하는 데이터에 더해, 디버깅에 도움이 되도록 이벤트에 추가 데이터를 넣을 수 있습니다.

## [추가 이벤트 데이터 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-additional-event-data)

추가 데이터로 이벤트를 보강하는 방법은 여러 가지가 있습니다.

- [사용자 식별](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#identifying-users)

문제를 겪는 사용자를 식별할 수 있도록 이벤트에 사용자 정보를 추가할 수 있습니다. Sentry 이벤트에 사용자를 설정하는 방법은 [setUser](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setUser)를 참고하세요.

- [태그 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#setting-tags)

태그는 이벤트에 추가 메타데이터를 넣는 방법입니다. Sentry UI에서 이벤트를 필터링하는 데 사용할 수 있습니다. 태그에 대해 더 알아보려면 [Tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/tags.md)를, Sentry 이벤트에 태그를 설정하는 방법은 [setTag](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setTag) 및 [setTags](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setTags)를 참고하세요.

- [컨텍스트 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#setting-context)

컨텍스트는 이벤트에 추가 메타데이터를 넣는 방법입니다. Sentry UI에서 컨텍스트로 필터링할 수는 없지만, 컨텍스트 정보는 이벤트 상세 정보에 표시됩니다. Sentry 이벤트에 컨텍스트 데이터를 설정하는 방법은 [setContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setContext)를 참고하세요.

- [Breadcrumb 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-breadcrumbs)

Breadcrumb는 이벤트가 발생하기 전에 있었던 단계 정보를 추가하는 방법입니다. Sentry 이벤트에 breadcrumb를 추가하는 방법은 [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md)를 참고하세요.

- [첨부파일 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-attachments)

첨부파일은 이벤트에 추가 파일을 넣는 방법입니다. Sentry 이벤트에 첨부파일을 추가하는 방법은 [Attachments](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md)를 참고하세요.

- [이벤트 프로세서](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#event-processors)

이벤트 프로세서는 이벤트가 Sentry로 전송되기 전에 이벤트를 변경하는 방법입니다. 이벤트 프로세서 사용 방법은 [Event Processors](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/event-processors.md)를 참고하세요.

## [특정 이벤트에만 추가 이벤트 데이터 적용](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#adding-additional-event-data-to-certain-events-only)

위에서 설명한 모든 API는 현재 요청의 모든 이벤트에 데이터를 붙입니다.

특정 이벤트에만 데이터를 붙이고 싶다면 [withScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#using-withscope)를 사용해 새 스코프를 만들고 해당 스코프에만 데이터를 붙일 수 있습니다.

## [커스텀 핑거프린팅](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#custom-fingerprinting)

모든 이벤트에는 fingerprint가 있습니다. 같은 fingerprint를 가진 이벤트는 하나의 이슈로 함께 그룹화됩니다. 특정 이벤트 유형에 기본 그룹화가 맞지 않는다면 커스텀 fingerprint를 설정해 이를 조정할 수 있습니다. 커스텀 fingerprint 설정 방법은 [Event Fingerprinting](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md)를 참고하세요.

## [스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#scopes)

이벤트가 캡처되어 Sentry로 전송될 때, SDK는 해당 이벤트 데이터와 현재 스코프의 추가 정보를 병합합니다. 프레임워크 통합에서는 보통 SDK가 스코프를 자동으로 관리하므로 이를 직접 신경 쓸 필요가 없습니다. 하지만 스코프의 동작 방식과 사용 사례에 맞게 활용하는 방법을 더 잘 이해하고 싶다면 [스코프에 대해 자세히 알아보세요](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md).

## [요청 격리](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#request-isolation)

설정한 데이터가 요청 간에 누출되지 않도록 요청을 [격리하는 방법](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation.md)을 확인하세요.

## [크기 제한](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events.md#size-limitations)

컨텍스트를 전송할 때는 *payload 크기 제한을 고려하세요*. Sentry는 컨텍스트에 전체 애플리케이션 상태나 큰 데이터 블롭을 보내는 것을 권장하지 않습니다. 최대 payload 크기를 초과하면 Sentry는 HTTP 오류 `413 Payload Too Large`를 반환하고 이벤트를 거부합니다. `keepalive: true`를 사용하는 경우 요청이 추가로 무기한 대기 상태로 남을 수도 있습니다.

Sentry SDK는 전송한 데이터를 최대한 수용하고 큰 컨텍스트 payload를 잘라내려고 시도합니다. 일부 SDK는 이벤트의 일부를 잘라낼 수 있습니다. 자세한 내용은 [SDK 데이터 처리에 관한 개발자 문서](https://develop.sentry.dev/sdk/expected-features/data-handling/)를 참고하세요.

## 이 섹션의 페이지

- [첨부파일](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md)
- [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/breadcrumbs.md)
- [이벤트 핑거프린팅](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/fingerprinting.md)
- [이벤트 레벨](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/level.md)
- [이벤트 프로세서](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/event-processors.md)
- [요청 격리](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation.md)
- [스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md)
- [태그](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/tags.md)

