---
title: 'OpenTelemetry 지원 | Next.js용 Sentry'
description: 'Sentry SDK는 내부적으로 OpenTelemetry를 사용합니다. 즉, span을 내보내는 모든 OpenTelemetry 계측은 추가 설정 없이 자동으로 Sentry에 수집됩니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry

# OpenTelemetry 지원 | Next.js용 Sentry

Sentry SDK는 내부적으로 [OpenTelemetry](https://opentelemetry.io/)를 사용합니다. 즉, span을 내보내는 모든 OpenTelemetry 계측은 추가 설정 없이 자동으로 Sentry에 수집됩니다.

trace와 span 수집을 시작하려면 [Sentry SDK로 Tracing 및 Performance Monitoring 설정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)를 참고하세요. tracing을 사용하지 않더라도, 컨텍스트 격리와 trace 전파가 올바르게 동작하도록 Sentry는 내부적으로 OpenTelemetry와 계속 연결됩니다.

기본적으로 Sentry가 OpenTelemetry를 자동으로 설정해 주지만, 자체 OpenTelemetry 설정을 사용할 수도 있습니다. 아래 가이드를 통해 커스텀 OpenTelemetry 설정을 사용하는 방법과 Sentry-OpenTelemetry 통합을 최대한 활용하는 방법을 확인하세요.

*
- [기존 OpenTelemetry 설정 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md)

  Sentry와 함께 기존의 커스텀 OpenTelemetry 설정을 사용하는 방법을 알아보세요.

*
- [OpenTelemetry API 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis.md)

  Sentry와 함께 OpenTelemetry API를 사용하는 방법을 알아보세요.

## 이 섹션의 페이지

- [기존 OpenTelemetry 설정 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md)
- [OpenTelemetry API 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis.md)

