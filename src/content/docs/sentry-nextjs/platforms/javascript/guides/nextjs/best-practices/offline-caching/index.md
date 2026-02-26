---
title: '오프라인 캐싱 | Next.js용 Sentry'
description: 'JavaScript 애플리케이션이 오프라인에서도 계속 동작하도록 설계된 경우, 연결이 없을 때 이벤트를 드롭하고 오프라인 이벤트를 놓치면 중요한 정보를 놓치게 될 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/offline-caching

# 오프라인 캐싱 | Next.js용 Sentry

JavaScript 애플리케이션이 오프라인에서도 계속 동작하도록 설계된 경우, 연결이 없을 때 이벤트를 드롭하고 오프라인 이벤트를 놓치면 중요한 정보를 놓치게 될 수 있습니다.

오프라인 이벤트 캐싱을 활성화하려면 `makeBrowserOfflineTransport`를 사용해 기존 전송 레이어를 감싸고, 브라우저의 IndexedDB 저장소를 사용해 이벤트를 큐에 저장하세요. 애플리케이션이 다시 온라인 상태가 되면 모든 이벤트가 함께 전송됩니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  transport: Sentry.makeBrowserOfflineTransport(Sentry.makeFetchTransport)
  transportOptions: {
    // see below
  }
})
```

다음은 `transportOptions`에 추가할 수 있는 몇 가지 선택적 속성입니다:

```javascript
transportOptions:{
  /**
   * Name of IndexedDb database to store events
   * Default: 'sentry-offline'
   */
  dbName: string;
  /**
   * Name of IndexedDb object store to store events
   * Default: 'queue'
   */
  storeName: string;
  /**
   * Maximum number of events to store
   * Default: 30
   */
  maxQueueSize: number;
  /**
   * Flush the store shortly after startup.
   * Default: false
   */
  flushAtStartup: boolean;
  /**
   * Called before an event is stored.
   * Return false to drop the envelope rather than store it.
   *
   * @param envelope The envelope that failed to send.
   * @param error The error that occurred.
   * @param retryDelay The current retry delay in milliseconds.
   */
  shouldStore: (envelope: Envelope, error: Error, retryDelay: number) => boolean | Promise<boolean>;
}
```

#
- [브라우저 지원](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/offline-caching.md#browser-support)

IndexedDB 기능이 부족하기 때문에 IE에서는 오프라인 캐싱이 지원되지 않습니다.

