---
title: 'Sentry Testkit | Next.js용 Sentry'
description: '애플리케이션 테스트를 작성할 때는 올바른 flow-tracking 또는 오류가 Sentry로 전송되는지 검증하고 싶지만, 실제로 Sentry 서버로 전송되게 하지는 않아야 합니다. 이렇게 하면 테스트 실행이나 기타 CI 작업 중에 잘못된 리포트로 Sentry가 과부하되...'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/sentry-testkit

# Sentry Testkit | Next.js용 Sentry

애플리케이션 테스트를 작성할 때는 올바른 flow-tracking 또는 오류가 Sentry로 전송되는지 검증하고 싶지만, 실제로 Sentry 서버로 전송되게 하지는 않아야 합니다. 이렇게 하면 테스트 실행이나 기타 CI 작업 중에 잘못된 리포트로 Sentry가 과부하되는 일을 막을 수 있습니다.

[Sentry Testkit](https://zivl.github.io/sentry-testkit/)은 추가 데이터 검토를 위해 Sentry 리포트를 가로챌 수 있게 해주는 커뮤니티 유지보수 Sentry 플러그인입니다. Sentry의 기본 전송 메커니즘을 재정의해, 리포트가 실제로 전송되지 않고 로컬 메모리에 기록되도록 함으로써 애플리케이션에서 Sentry가 네이티브하게 동작하도록 해줍니다. 이렇게 기록된 리포트는 이후에 로컬 개발 또는 테스트 환경에서 사용, 검증, 또는 기타 목적을 위해 가져올 수 있습니다.

Sentry Testkit은 커뮤니티에서 유지보수되며 Sentry의 공식 지원 대상이 아닙니다. 질문이나 피드백이 있다면 [Sentry Testkit repository](https://zivl.github.io/sentry-testkit/)에 이슈를 등록해 주세요.

## [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/sentry-testkit.md#installation)

```bash
npm install sentry-testkit --save-dev
```

- [테스트에서 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/sentry-testkit.md#using-in-tests)

```javascript
import sentryTestkit from "sentry-testkit";

const { testkit, sentryTransport } = sentryTestkit();

// initialize your Sentry instance with sentryTransport
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  transport: sentryTransport,
  //... other configurations
});

test("collect error events", function () {
  // run any scenario that eventually calls Sentry.captureException(...)
  expect(testkit.reports()).toHaveLength(1);
  const report = testkit.reports()[0];
  expect(report).toHaveProperty(/*...*/);
});

// Similarly for performance events
test("collect performance events", function () {
  // run any scenario that eventually calls Sentry.startTransaction(...)
  expect(testkit.transactions()).toHaveLength(1);
});
```

sentry-testkit 저장소의 [testing section](https://github.com/zivl/sentry-testkit/tree/master/__tests__)에서도 더 많은 사용 예제를 확인할 수 있습니다.

- [Testkit API](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/sentry-testkit.md#testkit-api)

Sentry Testkit은 매우 단순하고 직관적인 API로 구성되어 있습니다. 전체 API 설명과 문서는 [Sentry Testkit Docs](https://zivl.github.io/sentry-testkit/docs/api)에서 확인하세요.

