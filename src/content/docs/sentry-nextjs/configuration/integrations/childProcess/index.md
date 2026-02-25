---
title: 'Child Process 통합 | Next.js용 Sentry'
description: '이 통합은 Node.js 에서만 작동하며 SDK 버전  이상이 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess

# Child Process 통합 | Next.js용 Sentry

이 통합은 Node.js `>=20`에서만 작동하며 SDK 버전 `8.39.0` 이상이 필요합니다.

*Import 이름: `Sentry.childProcessIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [기본 통합 수정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`childProcessIntegration`은 `child_process` 및 `worker_threads` 오류, 그리고 `child_process`의 0이 아닌 종료 코드에 대한 breadcrumb와 이벤트를 수집합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.childProcessIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md#options)

- [`includeChildProcessArgs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md#includechildprocessargs)

*유형: `boolean`*

`true`로 설정하면 이 통합은 child process 시작 시 사용된 인수를 포함합니다.

- [`captureWorkerErrors`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md#captureworkererrors)

*유형: `boolean`*

기본적으로 이 옵션은 `true`입니다. `false`로 설정하면 이 통합은 worker thread의 오류를 수집하지 않습니다.

