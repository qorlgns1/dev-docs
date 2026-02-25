---
title: 'RewriteFrames | Next.js용 Sentry'
description: '이 통합을 사용하면 스택 트레이스의 각 프레임에 변환을 적용할 수 있습니다. 단순한 시나리오에서는 프레임이 시작된 파일 이름을 변경하는 데 사용할 수 있으며, 반복 함수(iteratee)를 전달해 임의의 변환을 적용할 수도 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes

# RewriteFrames | Next.js용 Sentry

*Import name: `Sentry.rewriteFramesIntegration`*

이 통합을 사용하면 스택 트레이스의 각 프레임에 변환을 적용할 수 있습니다. 단순한 시나리오에서는 프레임이 시작된 파일 이름을 변경하는 데 사용할 수 있으며, 반복 함수(iteratee)를 전달해 임의의 변환을 적용할 수도 있습니다.

Windows 환경에서는 이를 활성화하려면 `root` 옵션에 Unix 경로를 사용하고 드라이브 문자를 제외해야 합니다. 예를 들어 `C:\\Program Files\\Apache\\www`는 동작하지 않지만, `/Program Files/Apache/www`는 동작합니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.rewriteFramesIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#options)

- [`root`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#root)

*Type: `string`*

filename이 절대 경로인 경우, 기본 iteratee가 현재 프레임의 filename에서 제거할 루트 경로입니다.

- [`prefix`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#prefix)

*Type: `string`*

기본 iteratee가 사용할 사용자 지정 접두사입니다. 기본값: `app://`

- [`iteratee`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#iteratee)

*Type: `(frame) => frame`*

프레임을 받아 변환을 적용한 뒤 반환하는 함수입니다.

## [사용 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md#usage-examples)

예를 들어 파일의 전체 경로가 `/www/src/app/file.js`인 경우:

| 사용법                                       | 스택 트레이스 경로         | 설명                                                                                                                            |
| -------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `rewriteFramesIntegration()`                 | `app:///file.js`           | 기본 동작은 filename을 제외한 절대 경로를 치환하고, 기본 접두사(`app:///`)를 붙이는 것입니다.                                  |
| `rewriteFramesIntegration({prefix: 'foo/'})` | `foo/file.js`              | 기본 접두사 `app:///` 대신 접두사 `foo/`를 사용합니다.                                                                          |
| `rewriteFramesIntegration({root: '/www'})`   | `app:///src/app/file.js`   | `root`를 `/www`로 지정했기 때문에 경로 시작 부분에서 해당 부분만 잘라냅니다.                                                    |

