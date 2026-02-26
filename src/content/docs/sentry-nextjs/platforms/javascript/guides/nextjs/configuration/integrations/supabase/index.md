---
title: 'Supabase | Next.js용 Sentry'
description: '은 Supabase 클라이언트에 계측(instrumentation)을 추가하여 인증 및 데이터베이스 작업 모두에 대한 span을 수집합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase

# Supabase | Next.js용 Sentry

*Import name: `Sentry.supabaseIntegration`*

`supabaseIntegration`은 Supabase 클라이언트에 계측(instrumentation)을 추가하여 인증 및 데이터베이스 작업 모두에 대한 span을 수집합니다.

## [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#installation)

Sentry SDK와 Supabase 라이브러리가 모두 설치되어 있어야 합니다. Supabase 설치 방법은 [Supabase JavaScript documentation](https://supabase.com/docs/reference/javascript/introduction)을 참고하세요.

## [구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#configuration)

이 방법은 대부분의 사용 사례에서 권장되며, Sentry의 표준 통합 패턴을 따릅니다.

```javascript
import { createClient } from "@supabase/supabase-js";

const supabaseClient = createClient(
  "YOUR_SUPABASE_URL",
  "YOUR_SUPABASE_KEY",
);

Sentry.init({
  dsn: "YOUR_DSN",
  integrations: [Sentry.supabaseIntegration({ supabaseClient })],
  tracesSampleRate: 1.0,
});
```

## [생성되는 Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#generated-spans)

이 통합은 인증 및 데이터베이스 작업 모두에 대해 포괄적인 모니터링을 제공합니다.

- [인증 Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#authentication-spans)

이 통합은 다음 인증 작업을 자동으로 계측합니다.

* `signInWithPassword`
* `signOut`
* `signInAnonymously`
* `signInWithOAuth`
* `signInWithIdToken`
* `signInWithOtp`
* `signInWithSSO`
* `signUp`
* `verifyOtp`
* `reauthenticate`

관리자 작업도 계측됩니다.

* `createUser`
* `deleteUser`
* `listUsers`
* `getUserById`
* `updateUserById`
* `inviteUserByEmail`

- [데이터베이스 작업 Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#database-operation-spans)

이 span은 Sentry의 [Query Insights](https://docs.sentry.io/product/insights/backend/queries.md) 기능을 채우는 데 사용되며, 데이터베이스 작업에 대한 성능 지표와 분석을 제공합니다. Query Insights를 사용하면 느린 쿼리를 식별하고, 쿼리 빈도를 추적하며, 데이터베이스 상호작용을 최적화할 수 있습니다.

* `db.table`: 조회 중인 테이블
* `db.schema`: 데이터베이스 스키마
* `db.url`: Supabase 인스턴스 URL
* `db.sdk`: 클라이언트 정보
* `db.system`: 'postgresql'로 설정
* `db.query`: 쿼리 파라미터
* `db.body`: 요청 본문(변경 작업의 경우)

- [큐 작업 Span (진행 중)](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#queue-operation-spans-in-progress)

곧 Sentry SDK는 Supabase 큐와의 상호작용에 대한 span 생성도 지원할 예정입니다. 자세한 내용은 [this GitHub issue](https://github.com/getsentry/sentry-javascript/issues/14611)를 확인하세요.

## [오류 추적](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#error-tracking)

이 통합은 자동으로 다음을 수행합니다.

* 실패한 작업에서 오류 수집
* 데이터베이스 작업에 대한 breadcrumb 추가
* 실패한 작업에 대한 상세 컨텍스트 포함

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md#supported-versions)

* `@supabase/supabase-js`: `>=2.0.0`

