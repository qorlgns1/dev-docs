---
title: '소스 맵 문제 해결 | Sentry for Next.js'
description: '이전에 소스 맵을 설정했다면 도구(SDK, bundler plugins, Sentry CLI)를 업데이트하는 것을 권장합니다. 일반적으로는 오래된 버전으로 문제를 해결하려고 하기보다 최신 버전으로 업그레이드하고 현재 프로세스를 따르는 편이 더 쉽습니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js

# 소스 맵 문제 해결 | Sentry for Next.js

이전에 소스 맵을 설정했다면 도구(SDK, bundler plugins, Sentry CLI)를 업데이트하는 것을 권장합니다. 일반적으로는 오래된 버전으로 문제를 해결하려고 하기보다 최신 버전으로 업그레이드하고 현재 프로세스를 따르는 편이 더 쉽습니다.

소스 맵 업로드의 레거시 방식에 대한 정보는 [레거시 업로드 방법](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md) 가이드를 참고하세요.

소스 맵 업로드 레거시 방식을 요구하는 의존성 버전은 다음과 같습니다.

* JavaScript SDK 버전 `7.46.0` 이하

* `@sentry/webpack-plugin` 패키지 버전 `1.x` 이하

* `sentry-cli` 버전 `2.16.1` 이하

* 버전 `23.6.1` 이하의 Sentry self-hosted 또는 single-tenant

소스 맵 설정은 까다로울 수 있지만, 제대로 설정할 가치가 충분합니다. 아래 단계에 따라 소스 맵 설정을 문제 해결할 수 있습니다.

## [문제 해결 단계](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#troubleshooting-steps)

"Sentry not part of build pipeline" 오류

이 오류는 배포된 JavaScript에 Debug ID가 포함되어 있지 않아, Sentry가 이를 업로드된 소스 맵과 매칭할 수 없다는 뜻입니다.

**해결 방법:**

1. wizard를 실행해 bundler에 대한 소스 맵 업로드를 구성합니다.

   ```bash
   npx @sentry/wizard@latest -i sourcemaps
   ```

2. **production build**로 실행 중인지 확인합니다(개발/dev/watch 모드 아님).

3. [Source Maps](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/:projectId/source-maps/) 설정에서 아티팩트가 업로드되었는지 확인합니다.

- [아티팩트 업로드 여부 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-artifacts-are-uploaded)

아티팩트가 Sentry에 업로드되고 있는지 확인하세요. **\[Settings] > Projects > Select your project > Source Maps**에서 확인할 수 있습니다. Sentry가 스택 트레이스를 de-minify하려면 minified 파일(예: app.min.js)과 해당 소스 맵을 모두 제공해야 합니다.

- [소스 맵 빌드 여부 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-that-youre-building-source-maps)

코드를 생성하는 bundler 및 도구(예: `tsc`)는 소스 맵 생성을 위해 특정 옵션을 수동으로 설정해야 하는 경우가 많습니다.

도구별 가이드를 따랐다면, 도구가 소스 맵을 출력하도록 구성했는지와 소스 맵의 `sourcesContent` 필드에 원본 소스 코드가 포함되어 있는지 확인하세요.

- [production build 실행 여부 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-that-youre-running-a-production-build)

JavaScript 빌드 도구(예: webpack, Vite, ...)를 development-mode/watch-mode로 실행하면, 생성된 코드가 소스 맵 업로드 프로세스와 호환되지 않는 경우가 있습니다.

특히 로컬 테스트 시에는 source maps 업로드 설정 검증을 위해 production build 실행을 권장합니다.

- [소스 파일에 Debug ID 주입 스니펫이 포함되어 있는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-your-source-files-contain-debug-id-injection-snippets)

Sentry에 업로드한 JavaScript 파일에서 `e._sentryDebugIds=e._sentryDebugIds||{}`와 대략 유사한 코드를 검색하세요. 이 코드 스니펫의 형태는 코드 처리 방식에 따라 다를 수 있습니다.

bundle에 이 코드가 존재하면 해당 bundle은 소스 파일과 매칭될 수 있습니다. 앱에서 배포하는 모든 bundle에는 올바른 소스 매핑을 위해 이 스니펫이 포함되어야 합니다.

소스 코드에 이 스니펫이 없고 bundler용 Sentry plugin을 사용 중이라면, 최신 버전을 사용 중인지 확인하고 plugin이 파일을 올바르게 처리하는지 검증하세요. 유용한 디버깅 정보를 출력하려면 `debug` 옵션을 `true`로 설정하세요.

Sentry CLI를 사용 중이라면 Sentry에 업로드하기 **전** 그리고 파일 배포 **전**에 `inject` 명령을 실행하는지 확인하세요.

## [SDK가 최신인지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-your-sdk-is-up-to-date)

Sentry에서 이벤트 payload JSON 데이터를 확인할 때, 이벤트에 `debug_meta` 속성이 있는지 확인하세요. 이 속성이 없고 소스 파일에 debug ID 주입 스니펫이 있는 것을 이미 확인했다면, 오래된 SDK를 사용 중일 가능성이 큽니다.

일반적으로 최신 버전으로 업그레이드하는 것을 권장하며, 소스 맵이 동작하려면 최소 `7.47.0` 버전을 사용해야 합니다.

이벤트에 `debug_meta` 속성이 있는 것을 확인한 후 다음으로 확인할 것은, 이벤트 내부 `raw_stacktrace` 속성의 모든 frame에 있는 `abs_path` 속성이 `debug_meta` images 내부의 `code_file` 속성 중 하나와 정확히 일치하는지입니다.

스택 프레임이 `debug_meta` 항목과 일치하지 않으면, 관련 파일에 debug ID 주입 스니펫이 포함되어 있는지 확인하세요.

- [오류 발생 전에 아티팩트가 업로드되는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-artifacts-are-uploaded-before-errors-occur)

Sentry는 특정 release의 소스 코드와 소스 맵이 해당 release에서 오류가 발생하기 **전**에 Sentry로 업로드되기를 기대합니다.

오류가 Sentry에 수집된 **후**에 아티팩트를 업로드하면, Sentry는 해당 오류에 소스 주석을 소급 적용하지 않습니다. 아티팩트 업로드 이후에 새로 발생한 오류에만 반영됩니다.

- [소스 맵이 올바르게 빌드되었는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-your-source-maps-are-built-correctly)

**호스팅된** 소스를 기준으로 소스 맵을 테스트할 수 있는 온라인 검증 도구를 제공합니다: [sourcemaps.io](https://sourcemaps.io).

또는 Sentry CLI로 소스 맵을 Sentry에 업로드하는 경우 `--validate` 커맨드라인 옵션을 사용해 소스 맵이 올바른지 검증할 수 있습니다.

- [로컬에서 소스 맵 동작 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-your-source-maps-work-locally)

Sentry가 filename, line, column 매핑을 올바르게 하지 못한다면, 소스 맵이 로컬에서 정상 동작하는지 확인해야 합니다. 이를 위해 Node.js와 Mozilla의 [source-map library](https://github.com/mozilla/source-map)를 함께 사용할 수 있습니다.

먼저 `source-map`을 npm 모듈로 전역 설치하세요.

```bash
npm install -g source-map
```

그다음 소스 맵 파일을 읽고 매핑을 테스트하는 Node.js 스크립트를 작성하세요. 예시는 다음과 같습니다.

```javascript
var fs = require("fs"),
  path = require("path"),
  sourceMap = require("source-map");

// Path to file that is generated by your build tool (webpack, tsc, ...)
var GENERATED_FILE = path.join(".", "app.min.js.map");

// Line and column located in your generated file (for example, the source
// of the error from your minified file)
var GENERATED_LINE_AND_COLUMN = { line: 1, column: 1000 };

var rawSourceMap = fs.readFileSync(GENERATED_FILE).toString();
new sourceMap.SourceMapConsumer(rawSourceMap).then(function (smc) {
  var pos = smc.originalPositionFor(GENERATED_LINE_AND_COLUMN);

  // You should see something like:
  // { source: 'original.js', line: 57, column: 9, name: 'myfunc' }
  console.log(pos);
});
```

로컬에서도 Sentry와 동일한(잘못된) 결과가 나온다면, 소스 맵 생성 설정을 다시 점검하세요.

- [아티팩트가 Gzip되지 않았는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-that-artifacts-arent-gzipped)

현재 Sentry API는 일반 텍스트(UTF-8 인코딩)로 업로드된 소스 맵과 소스 파일에서만 동작합니다. 압축 형식(예: gzip)으로 업로드되면 올바르게 해석되지 않습니다.

`sentry-cli`로 아티팩트를 업로드하는 경우, 버전 `2.4.0`부터 `sourcemaps upload` 명령에 `--decompress` 플래그를 추가할 수 있습니다.

빌드 스크립트나 plugin이 사전 압축된 minified 파일을 생성하는 경우가 있습니다(예: webpack의 [compression plugin](https://github.com/webpack/compression-webpack-plugin)). 이런 경우 해당 plugin을 비활성화하고, 생성된 소스 맵/소스 파일을 Sentry에 업로드한 **후** 압축을 수행해야 합니다.

- [(Self-Hosted Sentry) `symbolicator` 서비스가 정상 동작하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#self-hosted-sentry-verify-the-symbolicator-service-is-operating-normally)

self-hosted 버전의 Sentry를 운영 중이라면, 컨테이너 로그를 확인해 `symbolicator` 서비스/컨테이너가 정상 동작하는지 검증할 수 있습니다.

- [(Docker를 통한 Self-Hosted Sentry) workers가 web과 동일한 볼륨을 공유하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#self-hosted-sentry-via-docker-verify-workers-are-sharing-the-same-volume-as-web)

Sentry는 workers에서 소스 맵 계산을 수행합니다. 즉 workers가 프론트엔드를 통해 업로드된 파일에 접근할 수 있어야 합니다. cron workers와 web workers가 동일한 디스크에서 파일을 읽고/쓸 수 있는지 다시 확인하세요.

- [`source-map-support` 패키지를 사용하고 있지 않은지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#verify-you-arent-using-the-source-map-support-package)

Sentry Node.js SDK는 소스 맵을 Sentry에 업로드하지 않은 경우 [source-map-support](https://www.npmjs.com/package/source-map-support) 패키지와 대체로 잘 동작합니다.

소스 맵을 Sentry에 업로드하고 있거나 브라우저에서 Sentry SDK를 사용 중이라면, 코드에서 `source-map-support` 패키지를 사용할 수 없습니다. `source-map-support`는 캡처된 스택 트레이스를 덮어써서 소스 맵 프로세서가 이를 올바르게 파싱하지 못하게 만듭니다.

- [서드파티 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js.md#third-party-integrations)

드물게 결함이 있거나 오래된 서드파티 통합이 Sentry로 전송되는 오류를 수정해 핵심 정보가 유실되고, 그 결과 Sentry가 소스 맵을 표시하지 못할 수 있습니다. 서드파티 통합 또는 기타 커뮤니티 유지보수 패키지를 사용 중이라면, 이 가능성을 배제하기 위해 일시적으로 비활성화해 보세요.

충돌하는 것으로 알려진 서드파티 패키지 사례는 여기에 수집합니다.

* `posthog-js` 버전 `1.207.4`부터 `1.229.0`까지 (`posthog-js` 버전 `1.229.1`에서 수정됨)

## 이 섹션의 페이지

- [레거시 업로드 방법](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md)
- [Debug IDs란 무엇인가](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md)

