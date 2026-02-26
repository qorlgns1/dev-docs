---
title: 'FileSystem | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs

# FileSystem | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 동작합니다.

*가져오기 이름: `Sentry.fsIntegration`*

`fsIntegration`은 파일 읽기/쓰기와 같은 `fs` API 작업에 대한 span을 생성합니다. 이 통합은 [`@opentelemetry/instrumentation-fs`](https://www.npmjs.com/package/@opentelemetry/instrumentation-fs) 패키지를 사용합니다.

##### 잠재적인 성능 오버헤드

`fsIntegration`은 애플리케이션에 상당한 오버헤드를 추가할 수 있습니다. 특히 프레임워크 개발 서버를 실행하는 경우처럼 파일 I/O가 많은 시나리오에서는, 이 통합을 포함하면 애플리케이션이 크게 느려질 수 있습니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.fsIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md#options)

- [`recordFilePaths`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md#recordfilepaths)

*유형: `boolean | undefined`*

이 옵션을 `true`로 설정하면 `fs` API 호출의 파일 경로 인수가 span 속성에 포함됩니다. 기본값은 `false`입니다.

- [`recordErrorMessagesAsSpanAttributes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md#recorderrormessagesasspanattributes)

*유형: `boolean | undefined`*

이 옵션을 `true`로 설정하면 실패한 `fs` API 호출의 오류 메시지가 span 속성에 포함됩니다. 기본값은 `false`입니다.

