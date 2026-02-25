---
title: '빌드 옵션 | Sentry for Next.js'
description: 'Sentry Next.js SDK는 Next.js 설정 파일( 또는 )에서  래퍼를 사용해, 앱 빌드 과정 중 자동 코드 주입과 소스맵 업로드를 지원합니다. 설정 업데이트에 대한 정보는 수동 설정 가이드를 참고하세요.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build

# 빌드 옵션 | Sentry for Next.js

Sentry Next.js SDK는 Next.js 설정 파일(`next.config.js` 또는 `next.config.mjs`)에서 `withSentryConfig` 래퍼를 사용해, 앱 빌드 과정 중 자동 코드 주입과 소스맵 업로드를 지원합니다. 설정 업데이트에 대한 정보는 [수동 설정 가이드](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#configure)를 참고하세요.

## [사용 가능한 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#available-options)

## [핵심 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#core-options)

- [org](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#org)

| 유형 | `string` |
| ---- | -------- |

앱과 연결된 Sentry 조직의 slug입니다.

- [project](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#project)

| 유형 | `string` |
| ---- | -------- |

앱과 연결된 Sentry 프로젝트의 slug입니다.

- [authToken](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#authToken)

| 유형 | `string` |
| ---- | -------- |

Sentry와의 모든 통신에 사용할 인증 토큰입니다. <https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/> 에서 발급할 수 있습니다.

- [sentryUrl](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sentryUrl)

| 유형    | `string`             |
| ------- | -------------------- |
| 기본값 | `https://sentry.io/` |

Sentry 인스턴스의 기본 URL입니다. self-hosted를 사용하거나 sentry.io 이외의 Sentry 인스턴스를 사용하는 경우 이 값을 사용하세요.

- [headers](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#headers)

| 유형 | `Record<string, string>` |
| ---- | ------------------------ |

모든 외부 네트워크 요청에 추가되는 헤더입니다.

- [telemetry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#telemetry)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `true`    |

`true`로 설정하면 내부 플러그인 오류와 성능 데이터가 Sentry로 전송됩니다.

Sentry는 더 빠르고 안정적인 제품 제공을 위해 자체적으로 Sentry를 사용합니다. 무엇을 전송하는지 매우 신중하게 관리합니다. 오류 데이터와 상위 수준의 성능 데이터 외에는 수집하지 않습니다. 이 플러그인을 사용하는 프로젝트의 코드나 세부 정보는 절대 수집하지 않습니다.

- [silent](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#silent)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `false`   |

Sentry SDK의 빌드 로그를 모두 숨깁니다.

- [debug](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#debug)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `false`   |

애플리케이션 빌드 시 SDK 및 소스맵 업로드에 대한 추가 디버그 정보를 출력합니다.

- [errorHandler](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#errorHandler)

| 유형 | `(error: Error) => void` |
| ---- | ------------------------ |

Sentry 빌드 과정에서 오류가 발생할 때 호출되는 콜백 함수입니다. 연결 문제로 CI/CD 파이프라인이 실패할 때 이를 우아하게 처리하는 데 특히 유용합니다. 빌드 프로세스를 실패시키기 위해 오류를 다시 throw할 수도 있습니다.

```javascript
withSentryConfig(nextConfig, {
  // ... other options
  errorHandler: (error) => {
    console.warn("Sentry build error occurred:", error);
    // Optionally, you can still fail the build by re-throwing the error
    // throw error;
  },
});
```

## [소스맵 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#source-maps-options)

- [sourcemaps.disable](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.disable)

| 유형 | `boolean` |
| ---- | --------- |

소스맵 관련 기능을 모두 비활성화합니다.

- [sourcemaps.assets](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.assets)

| 유형 | `string \| string[]` |
| ---- | -------------------- |

Sentry에 업로드할 빌드 아티팩트를 지정하는 glob 또는 glob 배열입니다. 지정하지 않으면 플러그인은 빌드 중 생성된 모든 JavaScript 파일과 소스맵 파일을 업로드하려고 시도합니다.

glob 패턴은 `glob` 패키지의 구현을 따릅니다.

- [sourcemaps.ignore](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.ignore)

| 유형    | `string \| string[]` |
| ------- | -------------------- |
| 기본값 | `[]`                 |

Sentry에 업로드하지 않을 빌드 아티팩트를 지정하는 glob 또는 glob 배열입니다.

- [sourcemaps.deleteSourcemapsAfterUpload](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.deleteSourcemapsAfterUpload)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `true`    |

Next.js 빌드 폴더 내에서 생성된 **클라이언트 측** 소스맵을 Sentry에 업로드한 뒤 자동 삭제할지 여부를 전환합니다. 활성화하면 `.next/static/`의 소스맵은 삭제되지만, **서버 측 소스맵**(`.next/server/`)은 의도적으로 유지됩니다. 이유는 다음과 같습니다.

* 런타임의 서버 측 오류 리포팅에 필요합니다.
* 사용자에게 공개 접근되지 않으므로 보안상 우려가 없습니다.

업로드 후 삭제할 파일을 커스터마이즈하려면(예: 추가 경로 포함), 대신 `sourcemaps.filesToDeleteAfterUpload` 옵션을 사용하세요.

- [sourcemaps.filesToDeleteAfterUpload](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#sourcemaps.filesToDeleteAfterUpload)

| 유형 | `string \| string[]` |
| ---- | -------------------- |

Sentry에 업로드된 뒤 삭제할 소스맵 파일을 지정하는 glob 패턴 배열입니다. 설정하면 `deleteSourcemapsAfterUpload`의 기본 삭제 동작을 덮어씁니다.

어떤 소스맵을 삭제할지 세밀하게 제어해야 할 때 이 옵션을 사용하세요. 삭제하려는 파일에 대해 [hidden source maps](https://webpack.js.org/configuration/devtool/)도 반드시 활성화해야 하며, 그렇지 않으면 빌드 결과물에 깨진 `sourceMappingURL` 참조가 포함됩니다.

```javascript
withSentryConfig(nextConfig, {
  sourcemaps: {
    filesToDeleteAfterUpload: [".next/static/**/*.map"],
  },
});
```

## [릴리스 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release-options)

- [release.name](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.name)

| 유형 | `string` |
| ---- | -------- |

생성하려는 릴리스의 고유 식별자입니다. 기본적으로 환경에 맞는 값이 자동 감지됩니다.

- [release.create](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.create)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `true`    |

빌드 중 플러그인이 Sentry에서 릴리스를 생성할지 여부입니다.

- [release.finalize](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.finalize)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `true`    |

빌드 종료 후 Sentry 릴리스를 자동으로 finalize할지 여부입니다.

- [release.dist](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#release.dist)

| 유형 | `string` |
| ---- | -------- |

배포판(distribution)의 고유 식별자로, 릴리스를 추가로 세분화하는 데 사용됩니다. 보통 빌드 번호를 사용합니다.

## [번들 크기 최적화](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#bundle-size-optimizations)

- [bundleSizeOptimizations.excludeDebugStatements](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#bundleSizeOptimizations.excludeDebugStatements)

| 유형 | `boolean` |
| ---- | --------- |

`true`로 설정하면 Sentry SDK는 빌드 중 자체 디버깅 코드를 tree-shake하려고 시도합니다.

- [bundleSizeOptimizations.excludeTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#bundleSizeOptimizations.excludeTracing)

| 유형 | `boolean` |
| ---- | --------- |

`true`로 설정하면 Sentry SDK는 tracing 및 성능 모니터링 관련 코드를 tree-shake하려고 시도합니다.

**주의:** 성능 모니터링 관련 SDK 기능을 사용하는 경우 이 옵션을 활성화하지 마세요.

## [Next.js 전용 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#nextjs-specific-options)

- [widenClientFileUpload](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#widenClientFileUpload)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `false`   |

소스맵 업로드 시 Next.js 내부 코드와 의존성의 코드를 포함합니다.

업로드 범위를 확장해야 하는 경우와 이유

클라이언트 측 스택 트레이스에서 일부 프레임만 소스맵이 적용되지 않고 대부분은 잘 적용된다면, 문제 프레임이 `static/chunks/pages/`가 아니라 `static/chunks/`의 파일에서 왔을 수 있습니다. 기본적으로 `static/chunks/`의 파일 대다수는 Next.js 또는 서드파티 코드만 포함하므로 업로드되지 않습니다. 서드파티 패키지 파일까지 포함해 모든 파일과 소스맵을 업로드하려면 `widenClientFileUpload` 옵션을 `true`로 설정하세요.

참고: 이 옵션을 활성화하면 빌드 시간이 길어질 수 있습니다.

- [tunnelRoute](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#tunnelRoute)

| 유형 | `string \| boolean` |
| ---- | ------------------- |

이 기능은 **Next.js version 11+**가 필요하며 현재 self-hosted Sentry 인스턴스에서는 동작하지 않습니다.

Sentry 이벤트 전송이 ad-blocker에 의해 차단되지 않도록, Next.js 서버의 이 경로를 통해 Sentry 요청을 터널링합니다.

이 옵션은 다음과 같이 설정할 수 있습니다.

* 자동 생성 경로용 `true` (배포마다 예측 불가능하게 변경됨)
* `/error-monitoring` 같은 사용자 지정 고정 문자열 경로

터널링에 대한 자세한 내용은 [troubleshooting 섹션](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md#dealing-with-ad-blockers)을 참고하세요.

Turbopack에서 Next.js middleware 사용

Turbopack을 사용 중이라면, Next.js middleware가 설정된 터널 경로를 가로채는 경우 클라이언트 측 이벤트 기록이 실패합니다. 이를 해결하려면 경로를 고정 문자열(예: `/error-monitoring`)로 설정하고 middleware에 `(?!error-monitoring)` 같은 negative matcher를 추가해 터널 경로를 제외하세요. Turbopack을 사용하지 않는 경우 Sentry가 middleware에서 터널 경로를 자동으로 건너뜁니다.

- [useRunAfterProductionCompileHook](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#useRunAfterProductionCompileHook)

| 유형    | `boolean`                         |
| ------- | --------------------------------- |
| 기본값 | `false(webpack)\|true(turbopack)` |

##### 버전 지원

이 옵션은 Next.js version 15.4.1 이상에서 사용할 수 있습니다.

빌드 완료 후 소스맵을 업로드하기 위해 [`runAfterProductionCompile` hook from Next.js](https://nextjs.org/docs/architecture/nextjs-compiler#runafterproductioncompile)를 사용하도록 활성화합니다.

* Turbopack에서는 소스맵 업로드를 위한 대체 방법이 없기 때문에 이 옵션이 기본적으로 `true`입니다.
* Webpack에서는 기본 동작이 [Sentry Webpack Plugin](https://github.com/getsentry/sentry-javascript-bundler-plugins)을 사용해 빌드 중 소스맵을 업로드하는 것이므로, 이 옵션이 `false`로 설정됩니다.

**중요:** 이 옵션을 활성화하면 Sentry CLI를 통해 [Debug IDs](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md)를 주입하므로 Next.js 빌드 결과물이 변경됩니다. 빌드 아티팩트 무결성 해시에 의존하고 있다면 이 옵션을 비활성화해야 합니다.

- [routeManifestInjection](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#routeManifestInjection)

| 유형    | `boolean\|object` |
| ------- | ----------------- |
| 기본값 | `true`            |

`v10.34.0`부터 사용 가능

##### App Router 전용

`routeManifestInjection` 옵션은 App Router에서만 지원됩니다.

클라이언트 번들에서 route manifest의 주입 및 필터링을 제어합니다.

route manifest는 빌드 시 생성되는 Next.js App Router 라우트 매핑으로, Sentry가 트랜잭션을 파라미터화된 라우트 이름(예: `/users/123` 또는 `/users/456` 대신 `/users/:id`)으로 그룹화할 수 있게 해줍니다.

이 옵션을 `false`로 설정하면 route manifest 주입을 비활성화할 수 있습니다.

**다음 경우 이 옵션을 비활성화하세요:**

* 클라이언트 번들 크기를 최소화하고 싶은 경우
* 라우트 스캔과 관련된 빌드 이슈가 발생하는 경우
* 트랜잭션 이름에 원시 URL을 선호하는 경우

또한 `exclude` 속성이 있는 객체를 전달해 route manifest에서 제외할 라우트를 제어할 수 있습니다. `exclude` 속성은 문자열 또는 정규식 배열, 혹은 라우트를 제외할 때 `true`를 반환하는 함수를 받습니다.

```javascript
withSentryConfig(nextConfig, {
  // Exclude specific routes using an array of strings or RegExps
  routeManifestInjection: {
    exclude: ["/api/health", "/api/excluded/[parameter]", /^\/internal\//],
  },
});
```

제외된 라우트는 파라미터화된 라우트 대신 트랜잭션 이름에 원시 URL로 표시됩니다.

**다음 경우 `exclude`를 사용하세요:**

* 내부용 또는 미공개 라우트가 클라이언트 번들에 나타나지 않게 하고 싶은 경우
* 파라미터화 그룹화의 이점이 없는 라우트(예: 동적 세그먼트가 없는 정적 라우트)를 제외해 번들 크기를 줄이고 싶은 경우

## [Next.js Webpack 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#nextjs-webpack-options)

이 옵션들은 Webpack을 사용할 때만 적용됩니다. Turbopack을 사용 중이면 이 옵션들은 효과가 없습니다.

- [webpack.autoInstrumentServerFunctions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.autoInstrumentServerFunctions)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `true`    |

오류 및 성능 모니터링을 위해 Next.js 데이터 페칭 메서드와 Next.js API 라우트를 자동으로 계측합니다.

- [webpack.autoInstrumentMiddleware](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.autoInstrumentMiddleware)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `true`    |

오류 및 성능 모니터링을 위해 Next.js 미들웨어를 자동으로 계측합니다.

- [webpack.autoInstrumentAppDirectory](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.autoInstrumentAppDirectory)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `true`    |

오류 모니터링을 위해 `app` 디렉터리의 컴포넌트를 자동으로 계측합니다.

- [webpack.excludeServerRoutes](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.excludeServerRoutes)

| 유형 | `Array<RegExp \| string>` |
| ---- | ------------------------- |

빌드 시 자동 Sentry 계측에서 특정 서버 측 API 라우트 또는 페이지를 제외합니다. 이 옵션은 문자열 또는 정규식 배열을 받으며 `pages` 및 `app` 디렉터리의 페이지에 영향을 줍니다.

라우트를 정의할 때 다음 사항에 유의하세요:

* 페이지는 파일 시스템 경로가 아니라 라우트로 지정하세요. 예를 들어 `pages/animals/index.js` 대신 `/animals`를 작성하세요.
* 제공한 문자열이 라우트와 정확히 일치하고, 앞에 슬래시가 있으며, 끝에 슬래시가 없도록 하세요.

```javascript
webpack.excludeServerRoutes: [
  "/some/excluded/route",
  "/excluded/route/with/[parameter]",
  /^\/route\/beginning\/with\/some\/prefix/,
  /\/routeContainingASpecificPathSegment\/?/,
];
```

- [webpack.automaticVercelMonitors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.automaticVercelMonitors)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `false`   |

`vercel.json`으로 구성된 경우 Vercel Cron Jobs에 대해 Sentry에서 cron monitor를 자동으로 생성합니다.

- [webpack.unstable\_sentryWebpackPluginOptions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.unstable_sentryWebpackPluginOptions)

| 유형 | `SentryWebpackPluginOptions` |
| ---- | ---------------------------- |

Sentry Next.js SDK와 함께 제공되는 [Sentry Webpack Plugin](https://www.npmjs.com/package/@sentry/webpack-plugin)에 구성 옵션을 직접 전달합니다. `withSentryConfig`에서 필요한 수정 옵션을 제공하지 않는 경우, 이 옵션으로 `sentryWebpackPluginOptions`를 재정의할 수 있습니다.

##### 중요

이 옵션은 불안정한 것으로 간주되며, 어떤 릴리스에서든 API가 호환되지 않게 변경될 수 있습니다.

- [webpack.reactComponentAnnotation.enabled](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.reactComponentAnnotation.enabled)

| 유형    | `boolean` |
| ------- | --------- |
| 기본값 | `false`   |

React 컴포넌트 이름 추적을 활성화합니다. 활성화하면 React 컴포넌트에 데이터 속성을 주석으로 추가하여, Session Replay 및 breadcrumbs 같은 기능에서 사용자가 어떤 컴포넌트와 상호작용했는지 Sentry가 추적할 수 있게 합니다.

- [webpack.reactComponentAnnotation.ignoredComponents](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.reactComponentAnnotation.ignoredComponents)

| 유형 | `string[] \| undefined` |
| ---- | ----------------------- |

컴포넌트 주석 처리에서 제외할 React 컴포넌트 이름 목록입니다.

- [webpack.treeshake](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#webpack.treeshake)

| 유형 | `object` |
| ---- | -------- |

tree shaking에 대한 구성 옵션입니다. 자세한 내용은 [tree shaking 문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md)를 참고하세요.

