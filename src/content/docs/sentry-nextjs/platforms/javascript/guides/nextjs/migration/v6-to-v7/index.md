---
title: '6.x에서 7.x로 마이그레이션 | Sentry for Next.js'
description: 'JavaScript SDK의  버전을 사용하려면 자체 호스팅 Sentry 버전이  이상이어야 합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v6-to-v7

# `6.x`에서 `7.x`로 마이그레이션 | Sentry for Next.js

JavaScript SDK의 `v7` 버전을 사용하려면 자체 호스팅 Sentry 버전이 `20.6.0` 이상이어야 합니다.

버전 7의 주요 목표는 번들 크기를 줄이는 것입니다. 이번 버전은 더 이상 사용되지 않는 API를 제거하고, 빌드 도구를 업그레이드했으며, npm 패키지 콘텐츠를 재구성했기 때문에 호환성이 깨지는 변경이 포함됩니다. 아래에서 업그레이드 시 고려해야 할 모든 주요 변경 사항을 설명합니다.

**TL;DR** Sentry의 기본 기능만 사용하거나, 문서의 설정 예시를 그대로 복사해 사용했다면 다음이 변경되었습니다:

* Sentry SDK(예: `@sentry/react` 또는 `@sentry/node`)와 함께 `@sentry/tracing` 같은 추가 Sentry 패키지를 설치했다면, 모든 패키지를 버전 7로 업그레이드하세요.
* CDN 번들이 이제 ES6 기반입니다. 새 SDK 버전에서도 ES5와 IE11을 계속 지원하려면 script 태그를 다시 구성해야 합니다.
* 배포되는 CommonJS 파일도 ES6이 됩니다. 오래된 node 버전을 지원해야 한다면 트랜스파일러를 사용하세요.
* 타입 생성에 사용하는 TypeScript 버전을 `3.8.3`으로 상향했습니다. TypeScript 버전이 `3.7` 이하인 프로젝트가 여전히 컴파일되는지 확인하세요. 컴파일되지 않으면 TypeScript 버전을 업그레이드하세요.
* `Sentry.init()` 옵션에서 `whitelistUrls`와 `blacklistUrls`는 각각 `allowUrls`와 `denyUrls`로 이름이 변경되었습니다.
* `UserAgent` integration의 이름이 이제 `HttpContext`입니다.
* Tracing을 사용하고 tracing이 활성화되어 있다면, 서버의 CORS 설정을 조정해야 할 수 있습니다.

`6.x`에서 `7.x`로 마이그레이션하는 방법에 대한 자세한 내용은 [상세 마이그레이션 가이드](https://github.com/getsentry/sentry-javascript/blob/develop/docs/migration/v6-to-v7.md)를 참조하세요.

