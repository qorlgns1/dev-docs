---
title: '수집되는 데이터 | Next.js용 Sentry'
description: 'Sentry는 데이터 프라이버시를 매우 중요하게 여기며, 특히 개인 식별 정보(PII) 데이터와 관련해 데이터 안전을 우선하는 기본 설정을 제공합니다. 애플리케이션에 Sentry SDK를 추가하면, 애플리케이션의 런타임 및 빌드 타임 동안 데이터를 수집하여 Sentry...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected

# 수집되는 데이터 | Next.js용 Sentry

Sentry는 데이터 프라이버시를 매우 중요하게 여기며, 특히 개인 식별 정보(PII) 데이터와 관련해 데이터 안전을 우선하는 기본 설정을 제공합니다. 애플리케이션에 Sentry SDK를 추가하면, 애플리케이션의 런타임 및 빌드 타임 동안 데이터를 수집하여 Sentry로 전송하도록 허용하게 됩니다.

수집되는 데이터의 카테고리 유형과 양은 Sentry SDK에서 활성화한 통합에 따라 달라집니다. 이 페이지는 Sentry JavaScript SDK가 수집하는 데이터 카테고리를 나열합니다.

여기에 나열된 많은 카테고리는 [sendDefaultPii 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii)을 활성화해야 합니다.

## [HTTP 헤더](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#http-headers)

기본적으로 Sentry SDK는 HTTP 응답 또는 요청 헤더를 전송합니다.

## [쿠키](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#cookies)

기본적으로 Sentry SDK는 쿠키를 전송하지 않습니다.

쿠키를 전송하려면 `Sentry.init()` 호출에서 `sendDefaultPii: true`를 설정하세요. 그러면 fetch 및 XHR 요청의 `Cookie` 및 `Set-Cookie` 쿠키 헤더가 전송됩니다.

## [로그인한 사용자 정보](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#information-about-logged-in-user)

기본적으로 Sentry SDK는 이메일 주소, 사용자 ID, 사용자명과 같은 로그인한 사용자 정보를 전송하지 않습니다.

전송할 수 있는 로그인 사용자 정보의 유형은 Sentry SDK에서 활성화한 통합에 따라 달라집니다. 대부분의 통합은 사용자 정보를 전송하지 않습니다. 일부 통합(예: [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md))은 사용자 ID, 사용자명, 이메일 주소 같은 데이터를 전송할 수 있게 합니다.

## [사용자 IP 주소 및 위치](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#users-ip-address-and-location)

기본적으로 Sentry SDK는 사용자 IP 주소를 전송하지 않습니다.

사용자 IP 주소 전송 및 위치 추론을 활성화하려면 [`sendDefaultPii: true`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii)를 설정하세요. Astro의 [`handleRequest`](https://docs.sentry.io/platforms/javascript/guides/nextjs/guides/astro.md#customize-server-instrumentation) 같은 일부 통합에서는 `trackClientIp`를 활성화하여 사용자 IP 주소를 전송할 수 있습니다.

IP 주소 전송이 활성화되면 IP 주소를 추론하거나 [`Sentry.setUser()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#setUser)의 `ip_address`로 제공된 IP 주소를 사용하려고 시도합니다. `ip_address: null`로 설정하면 IP 주소는 추론되지 않습니다.

## [요청 URL](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#request-url)

송신 및 수신 HTTP 요청의 전체 요청 URL은 **항상 Sentry로 전송됩니다**. 애플리케이션에 따라 이 URL에는 PII 데이터가 포함될 수 있습니다. 예를 들어 `/users/1234/details` 같은 URL에서 `1234`는 사용자 ID(PII로 간주될 수 있음)일 수 있습니다.

## [요청 쿼리 문자열](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#request-query-string)

송신 및 수신 HTTP 요청의 전체 요청 쿼리 문자열은 **항상 Sentry로 전송됩니다**. 애플리케이션에 따라 이 문자열에는 PII 데이터가 포함될 수 있습니다. 예를 들어 `?user_id=1234` 같은 쿼리 문자열에서 `1234`는 사용자 ID(PII로 간주될 수 있음)일 수 있습니다.

하지만 Sentry에는 쿼리 문자열에서 민감한 데이터를 제거하기 위한 기본 [서버 측 데이터 스크러빙](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md)이 적용되어 있습니다. 예를 들어 `apiKey` 및 `token` 쿼리 파라미터는 기본적으로 제거됩니다.

## [요청 본문](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#request-body)

기본적으로 Sentry는 수신 HTTP 요청의 본문 콘텐츠 크기를 전송합니다. 이는 `content-length` 헤더를 통해 추론됩니다. Sentry는 클라이언트 측에서 요청 본문 자체를 전송하지 않습니다.

서버 측에서는 수신 요청 본문이 기본적으로 캡처됩니다. [HTTP Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md)에서 `ignoreIncomingRequestBody`를 설정하면 수신 요청 본문 전송을 비활성화할 수 있습니다.

## [서버 측 요청 데이터](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#server-side-request-data)

서버 측에서 [RequestData Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)은 쿠키, 헤더, 쿼리 문자열, 요청 본문(`data`), URL, 사용자 정보를 포함한 수신 요청 데이터를 캡처합니다. 기본적으로 이러한 필드의 대부분이 캡처됩니다(IP 주소 제외).

##### v11의 예정된 변경 사항

버전 11에서는 RequestData 통합의 기본 동작이 프라이버시를 더 고려하는 방향으로 변경될 가능성이 높습니다. `cookies`, `data`, `headers`, `query_string`, `user` 같은 필드는 기본값이 `true`에서 `false`로 바뀔 예정입니다. v11로 업그레이드한 뒤에도 이 데이터를 계속 캡처하려면 [RequestData Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)을 명시적으로 구성하거나 [`sendDefaultPii: true`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii)를 설정해야 합니다.

## [응답 본문](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#response-body)

기본적으로 Sentry SDK는 송신 요청으로부터 받은 응답의 본문 콘텐츠를 전송하지 않습니다. 기본적으로 SDK는 `content-length` 헤더를 기반으로 응답 본문 크기를 전송합니다.

## [소스 컨텍스트](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#source-context)

기본적으로 Sentry CLI Wizard(`@sentry/wizard`)로 설정된 SDK는 소스 맵을 Sentry에 업로드하도록 활성화됩니다.

소스 맵 업로드를 비활성화하려면 [Source Maps 문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md)를 참고하세요.

## [스택 트레이스의 로컬 변수](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#local-variables-in-stack-trace)

Sentry SDK는 클라이언트 측 JavaScript SDK에서 오류 스택 트레이스의 로컬 변수를 전송하지 않습니다.

`Sentry.init()` 호출에서 `includeLocalVariables: true`를 설정하면 로컬 변수 전송을 활성화할 수 있습니다. 그러면 [Local Variables Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md)이 활성화됩니다. 이 통합은 Node.js 기반 런타임에서 기본적으로 추가됩니다.

## [디바이스, 브라우저, OS 및 런타임 정보](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#device-browser-os-and-runtime-information)

기본적으로 Sentry SDK는 디바이스 및 런타임 정보를 Sentry로 전송합니다.

브라우저 환경에서는 이 정보가 User Agent 문자열을 통해 획득됩니다. User Agent 문자열에는 브라우저, 운영체제, 디바이스 유형에 대한 정보가 포함됩니다.

서버 측 환경에서는 Sentry SDK가 운영체제 및 아키텍처 정보를 가져오기 위해 `os` 모듈을 사용합니다.

## [세션 리플레이](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#session-replay)

기본적으로 Session Replay SDK는 모든 텍스트 콘텐츠, 이미지, 웹 뷰, 사용자 입력을 마스킹합니다. 이는 민감한 데이터 노출을 방지하는 데 도움이 됩니다. 자세한 내용은 [Session Replay 문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md)에서 확인할 수 있습니다.

Session Replay는 애플리케이션의 모든 송신 fetch 및 XHR 요청에 대한 기본 정보도 캡처합니다. 여기에는 URL, 요청 및 응답 본문 크기, 메서드, 상태 코드가 포함됩니다. [`networkDetailAllowUrls`](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#network-details)가 정의되어 있으면 요청 및 응답 본문도 Sentry로 전송됩니다. 요청 또는 응답 본문에 PII 정보가 포함되어 있으면 PII 데이터가 포함될 수 있습니다.

Session Replay에서는 기본적으로 콘솔 메시지도 캡처됩니다. 콘솔 메시지를 스크러빙하려면 [`beforeAddRecordingEvent`](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#custom-scrubbing) 옵션을 사용해 메시지가 Sentry로 전송되기 전에 필터링할 수 있습니다.

## [콘솔 로그](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#console-logs)

기본적으로 Sentry SDK는 JS 콘솔 로그를 브레드크럼으로 Sentry에 전송하며, 여기에는 PII 데이터가 포함될 수 있습니다.

콘솔 메시지 전송을 비활성화하려면 `Sentry.breadcrumbsIntegration` 구성에서 `console: false`를 설정하세요. 자세한 내용은 [Breadcrumbs 문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md)를 참고하세요.

## [리퍼러 URL](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#referrer-url)

기본적으로 Sentry SDK는 리퍼러 URL을 Sentry로 전송합니다. 이는 현재 페이지로 연결한 페이지의 URL입니다.

## [스택 트레이스 컨텍스트 라인](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#stack-trace-context-lines)

기본적으로 [Context Lines Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)이 활성화되어 있습니다. 이 통합은 스택 트레이스의 각 프레임에 대해 주변 코드 라인을 전송합니다. 코드에 PII 정보가 있으면 PII 데이터가 포함될 수 있습니다.

## [LLM 입력 및 응답](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#llm-inputs-and-responses)

[Vercel AI Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)을 사용할 때, 사용된 프롬프트는 모델 ID 및 사용된 토큰 같은 메타데이터와 함께 Sentry로 전송됩니다. 전체 속성 목록은 [코드](https://github.com/getsentry/sentry-javascript/blob/master/packages/node/src/integrations/tracing/vercelai/index.ts)에서 확인하세요.

## [데이터베이스 쿼리](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#database-queries)

기본적으로 Sentry SDK는 SQL 쿼리를 Sentry로 전송합니다. SQL 문이 파라미터화되지 않은 경우 SQL 쿼리에 PII 정보가 포함될 수 있습니다.

MongoDB 쿼리도 전송되지만, Sentry SDK는 전체 MongoDB 쿼리를 전송하지 않습니다. 대신 쿼리의 파라미터화된 버전을 전송합니다.

## [tRPC 컨텍스트](https://docs.sentry.io/platforms/javascript/guides/nextjs/data-management/data-collected.md#trpc-context)

기본적으로 Sentry SDK는 tRPC 컨텍스트의 tRPC 입력을 전송하지 않습니다.

tRPC 입력을 전송하려면 `Sentry.init()` 호출에서 `sendDefaultPii: true`를 설정하거나 [`Sentry.trpcMiddleware()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md) 옵션에서 `attachRpcInput: true`를 설정해 활성화할 수 있습니다.

