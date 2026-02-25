---
title: 'WebWorker | Next.js용 Sentry'
description: '이 통합은 와 함께 브라우저의 메인 스레드와 하나 이상의 WebWorkers 간 통신을 설정합니다. 전달된 워커들의 메시지를 수신하고 이를 메인 스레드로 전달합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker

# WebWorker | Next.js용 Sentry

*Import name: `Sentry.webWorkerIntegration`*

이 통합은 `Sentry.registerWebWorker()`와 함께 브라우저의 메인 스레드와 하나 이상의 [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) 간 통신을 설정합니다. 전달된 워커들의 메시지를 수신하고 이를 메인 스레드로 전달합니다.

자세한 내용은 [Web Worker Guide](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md)를 참고하세요.

이 통합은 어떤 일을 하나요?

이 통합은 워커가 `Sentry.registerWebWorker({ self })`를 호출할 때 전송하는 메시지를 수신합니다. 목적은 메인 스레드와 워커 간에 source map 정보(`debugIds`)를 동기화하여, 메인 스레드 SDK가 포착한 워커 오류가 워커의 소스 코드에 올바르게 매핑되도록 하는 것입니다.

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#options)

- [`worker`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#worker)

*타입: `Worker | Array<Worker>`*

수신할 웹 워커입니다. 모든 워커는 SDK에 자신을 등록하기 위해 `Sentry.registerWebWorker({ self })`를 호출해야 합니다.

## [메서드](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#methods)

- [`addWorker(worker: Worker)`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#addworkerworker-worker)

통합이 이미 초기화되어 SDK에 추가된 이후에 워커를 통합에 추가합니다. 이는 애플리케이션 생명주기의 더 나중 시점에 초기화되는 워커가 있을 때 유용합니다. 모든 워커는 SDK에 자신을 등록하기 위해 `Sentry.registerWebWorker({ self })`를 호출해야 한다는 점에 유의하세요.

