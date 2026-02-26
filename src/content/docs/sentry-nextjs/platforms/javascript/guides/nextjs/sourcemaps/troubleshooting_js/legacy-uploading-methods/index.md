---
title: '레거시 업로드 방법 | Sentry for Next.js'
description: 'Sentry는 source map 처리를 위한 새로운 프로세스로 전환했습니다. 이 프로세스를 "source mapping with debug IDs"라고 부릅니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods

# 레거시 업로드 방법 | Sentry for Next.js

Sentry는 source map 처리를 위한 새로운 프로세스로 전환했습니다. 이 프로세스를 "source mapping with debug IDs"라고 부릅니다.

이 프로세스를 사용하려면 업데이트된 Sentry 의존성이 필요합니다. 항상 가능한 것은 아니라는 점을 알고 있으므로, 이 페이지에서는 debug ID 없이 source map을 업로드하는 방법을 설명합니다.

## [이 가이드를 사용해야 하는 경우](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#when-to-use-this-guide)

다음 중 하나를 사용 중이라면 이 페이지의 가이드를 사용하세요.

* JavaScript SDK 버전 `7.46.0` 이하
* `@sentry/webpack-plugin` 패키지 버전 `1.x` 이하
* `sentry-cli` 버전 `2.16.1` 이하
* 버전 `23.6.1` 이하의 Sentry self-hosted 또는 single-tenant

Sentry 의존성이 모두 위 목록보다 최신 버전이라면, 일반 [Source Maps](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps.md) 가이드를 사용하는 것을 권장합니다.

이 도구들의 구버전 중 하나 이상을 사용 중이어도 source map 업로드는 가능합니다. 다만 프로세스가 다릅니다. debug ID 대신 [Releases](https://docs.sentry.io/product/releases.md)를 사용해 이벤트의 스택 프레임을 해당 minified source 및 source map 파일(artifact라고 부름)과 매칭합니다.

이 가이드를 사용하려면 아래에서 현재 사용하는 도구에 해당하는 섹션으로 이동해 그 섹션의 단계를 따르세요.

* `sentry-cli`
* Sentry webpack plugin Version 1.x
* Version 2.x의 Sentry Bundler Plugins

마지막 "[Verify Artifacts Were Uploaded](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-artifacts-were-uploaded)" 섹션은 모든 도구 유형에 공통으로 적용됩니다.

## [`sentry-cli`를 사용한 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#uploading-using-sentry-cli)

- [1. SDK 옵션 업데이트](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#1-update-sdk-options)

이벤트를 올바른 릴리스와 매칭하려면 SDK 옵션에 `release` 속성을 제공해야 합니다.

```javascript
Sentry.init({
  // This value must be identical to the name you give the release that you
  // create below using `sentry-cli`.
  release: "<release_name>",
});
```

- [2. 새 릴리스 생성](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#2-create-a-new-release)

먼저 `sentry-cli`로 릴리스를 생성해야 합니다. 릴리스 이름은 조직 내에서 고유해야 합니다.

```bash
sentry-cli releases new <release_name>
```

- [3. Artifact 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#3-upload-artifacts)

다음으로 artifact(minified source와 source map)를 업로드하세요.

```bash
sentry-cli sourcemaps upload --release=<release_name> /path/to/directory
```

## [Sentry Webpack Plugin Version 1.x를 사용한 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#uploading-using-sentry-webpack-plugin-version-1x)

`@sentry/webpack` 패키지 버전 `1.x`가 설치되어 있다면, 플러그인 설정 방법은 [Sentry webpack plugin v1 documentation](https://github.com/getsentry/sentry-webpack-plugin#readme)에서 확인할 수 있습니다.

예시:

`webpack.config.js`

```javascript
const SentryWebpackPlugin = require("@sentry/webpack-plugin");

module.exports = {
  // ... other config above ...

  devtool: "hidden-source-map", // Source map generation must be turned on ("hidden-source-map", "source-map", etc.)
  plugins: [
    new SentryWebpackPlugin({
      org: "___ORG_SLUG___",
      project: "___PROJECT_SLUG___",

      // Specify the directory containing build artifacts
      include: "./dist",

      sourcemaps: {
        // As you're enabling client source maps, you probably want to delete them after they're uploaded to Sentry.
        // Set the appropriate glob pattern for your output folder - some glob examples below:
        filesToDeleteAfterUpload: [
          "./**/*.map",
          ".*/**/public/**/*.map",
          "./dist/**/client/**/*.map",
        ],
      },

      // Auth tokens can be obtained from
      // https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/
      authToken: process.env.SENTRY_AUTH_TOKEN,

      // Optionally uncomment the line below to override automatic release name detection
      // release: process.env.RELEASE,
    }),
  ],
};
```

Sentry webpack plugin은 SDK에 release 값을 자동으로 주입하므로, `Sentry.init`에서 `release` 옵션을 생략하거나 `Sentry.init`의 `release` 옵션이 플러그인의 `release` 옵션과 정확히 일치하도록 해야 합니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // When using the plugin, either remove the `release`` property here entirely or
  // make sure that the plugin's release option and the Sentry.init()'s release
  // option match exactly.
  // release: "my-example-release-1"
});
```

## [Version `2.x`의 Sentry Bundler Plugins를 사용한 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#uploading-using-sentry-bundler-plugins-on-version-2x)

다음 중 하나를 사용 중이라면

* 버전 `23.6.1` 이하의 Sentry self-hosted 또는 single-tenant
* 또는 버전 `7.46.0`의 Sentry JavaScript SDK
* 또는 `splitting: true`를 사용하는 esbuild

bundler plugins를 `release.uploadLegacySourcemaps` 옵션으로 설정해야 합니다.

이는 다음 패키지의 버전 `2.x` 이상을 사용할 때 적용됩니다.

* `@sentry/webpack-plugin`
* `@sentry/vite-plugin`
* `@sentry/esbuild-plugin`
* `@sentry/rollup-plugin`

`release.uploadLegacySourcemaps` 옵션 사용 예시:

`webpack.config.js`

```javascript
const { sentryWebpackPlugin } = require("@sentry/webpack-plugin");

module.exports = {
  // ... other config above ...

  devtool: "hidden-source-map", // Source map generation must be turned on ("hidden-source-map", "source-map", etc.)
  plugins: [
    sentryWebpackPlugin({
      org: "___ORG_SLUG___",
      project: "___PROJECT_SLUG___",

      // Auth tokens can be obtained from your User Settings
      // and need `project:releases` and `org:read` scopes
      authToken: process.env.SENTRY_AUTH_TOKEN,

      sourcemaps: {
        // As you're enabling client source maps, you probably want to delete them after they're uploaded to Sentry.
        // Set the appropriate glob pattern for your output folder - some glob examples below:
        filesToDeleteAfterUpload: [
          "./**/*.map",
          ".*/**/public/**/*.map",
          "./dist/**/client/**/*.map",
        ],
      },

      release: {
        uploadLegacySourcemaps: {
          paths: ["."],
          ignore: ["./node_modules"],
        },
      },
    }),
  ],
};
```

Sentry bundler plugins는 SDK에 release 값을 자동으로 주입하므로, `Sentry.init`에서 `release` 옵션을 생략하거나 `Sentry.init`의 `release` 옵션이 플러그인의 `release.name` 옵션과 정확히 일치하도록 해야 합니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // When using one of the plugins, either remove the `release`` property here entirely or
  // make sure that the plugin's `release.name` option and the Sentry.init()'s release
  // option match exactly.
  // release: "my-example-release-1"
});
```

## [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#troubleshooting)

위 단계를 모두 따랐는데도 레거시 방식으로 source map 설정에 문제가 있다면, 이 섹션이 설정 문제를 진단하는 데 도움이 됩니다.

- [SDK에 release가 설정되어 있는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-a-release-is-configured-in-your-sdk)

업로드된 source map을 찾아 적용하려면, release가 CLI 또는 API로 생성되어 있어야 하고(올바른 artifact가 함께 업로드되어야 함), 새로 생성된 release 이름이 SDK 설정에 지정되어 있어야 합니다.

확인하려면 Sentry UI에서 해당 이슈를 열고 release가 설정되어 있는지 확인하세요. 화면 오른쪽의 **Release** 옆에 "*not configured*" 또는 "*N/A*"가 표시되거나(또는 tag 목록에서 `release` tag가 보이지 않으면), 돌아가서 [tag your errors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md)를 해야 합니다. 올바르게 설정되었다면 "Release: my\_example\_release"가 표시됩니다.

- [artifact가 업로드되었는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-artifacts-are-uploaded)

release가 올바르게 설정되고 이슈에 tag가 지정되면, **\[Settings] > Projects > Select your project > Source Maps**로 이동해 Sentry에 업로드된 artifact를 확인할 수 있습니다.

또한 필요한 파일이 모두 있는지 확인하세요. Sentry가 스택 트레이스를 de-minify하려면 minified 파일(예: app.min.js)과 해당 source map이 모두 필요합니다. source map 파일에 원본 소스 코드(`sourcesContent`)가 포함되어 있지 않다면 원본 소스 파일도 추가로 제공해야 합니다. 또는 sentry-cli가 source map에 소스가 없을 경우 자동으로 소스를 임베드합니다.

- [`sourceMappingURL` 존재 여부 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-sourcemappingurl-is-present)

일부 CDN은 JavaScript 파일을 포함한 정적 파일에서 주석을 자동 제거합니다. 이 경우 주석으로 간주되는 `sourceMappingURL` 지시어도 JavaScript 파일에서 제거될 수 있습니다. 예를 들어 CloudFlare에는 [Auto-Minify](https://blog.cloudflare.com/an-all-new-and-improved-autominify/)라는 기능이 있으며, 활성화되면 `sourceMappingURL`이 제거됩니다.

배포된 최종 JavaScript 파일에 `sourceMappingURL`이 존재하는지 다시 확인하세요.

- [artifact distribution 값이 SDK에 설정된 값과 일치하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-artifact-distribution-value-matches-value-configured-in-your-sdk)

distribution 식별자(SDK의 `dist` 설정 옵션)를 사용하는 경우, source map 업로드 시에도 동일한 값을 사용해야 합니다. 반대로 source map이 `dist` 값과 함께 업로드된다면 SDK에도 동일한 값이 설정되어야 합니다. 업로드된 source map에 `dist` 값을 추가하려면 `sentry-cli`의 `--dist` 플래그 또는 [Sentry Bundler Plugins](https://github.com/getsentry/sentry-javascript-bundler-plugins)의 `dist` 옵션(예: `@sentry/webpack-plugin`)을 사용하세요. SDK에서 `dist` 값을 설정하려면 `Sentry.init()`의 `dist` 옵션을 사용하세요.

SDK에 distribution이 올바르게 설정되었는지 확인하려면 Sentry UI에서 이슈를 열고 `dist` tag가 있는지 확인하세요. artifact의 경우 프로젝트 설정의 `Source Maps` 페이지로 이동해 방금 확인한 이벤트에 표시된 release를 선택하고, `dist` 값(업로드 시간 옆의 작은 타원 배지)이 이벤트의 값과 일치하는지 확인하세요.

- [artifact 이름이 스택 트레이스 프레임과 일치하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-artifact-names-match-stack-trace-frames)

source map을 업로드했는데 Sentry 이슈에서 코드에 적용되지 않는다면, 이벤트의 JSON을 열어 `abs_path`를 확인해 파일을 정확히 어디서 해석하려는지 보세요. 예: `http://localhost:8000/scripts/script.js` (`abs_path`는 스택 트레이스의 각 프레임마다 한 번씩 나타납니다. 이를 deminified되지 않은 파일과 매칭하세요.) JSON 보기 링크는 이슈 페이지 상단의 이벤트 발생 날짜 옆에서 찾을 수 있습니다. 업로드된 artifact 이름은 이 값들과 일치해야 합니다.

경로에 **동적 값이 있는 경우**(예: `https://www.site.com/{some_value}/scripts/script.js`), `abs_path` 값을 변경하기 위해

[`rewriteFrames` integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md)

사용을 고려할 수 있습니다.

#
- [sentry-cli 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#using-sentry-cli)

`sourceMappingURL` 주석이 다음과 비슷하다면:

```javascript
// -- end script.min.js (located at http://localhost:8000/scripts/script.min.js)
//# sourceMappingURL=script.min.js.map
```

이 파일들을 올바르게 업로드하는 `sentry-cli` 명령 예시는 다음과 같습니다(현재 `/scripts` 디렉터리에 있고, 웹 서버는 한 단계 상위 디렉터리에서 실행 중이므로 `--url-prefix` 옵션을 사용합니다).

```shell
sentry-cli sourcemaps upload --url-prefix '~/scripts' .
```

이 명령은 현재 디렉터리의 모든 JavaScript 파일을 업로드합니다. 이제 Sentry의 Artifacts 페이지는 다음과 같아야 합니다.

```bash
~/scripts/script.js
~/scripts/script.min.js
~/scripts/script.min.js.map
```

또는 업로드할 파일을 지정할 수도 있습니다. 예:

```bash
sentry-cli sourcemaps upload --url-prefix '~/scripts' script.min.js script.min.js.map
```

전체 URL을 사용해 업로드할 수도 있습니다. 예:

```bash
sentry-cli sourcemaps upload --url-prefix 'http://localhost:8000/scripts' .
```

#
- [API 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#using-the-api)

동일한 이름 규칙을 따라 artifact를 업로드하려면, [use our API](https://docs.sentry.io/api/releases/update-an-organization-release-file.md)를 사용할 수도 있습니다.

```shell
curl -X POST \
  https://sentry.io/api/0/organizations/ORG_SLUG/releases/VERSION/files/ \
  -H 'Authorization: Bearer AUTH_TOKEN' \
  -H 'content-type: multipart/form-data' \
  -F file=@script.min.js.map \
  -F 'name=~/scripts/script.min.js.map'
```

#
- [`~` 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#using-the-)

`~`는 Sentry에서 스킴과 도메인을 대체하는 데 사용됩니다. glob이 아닙니다.

`http://example.com/dist/js/script.js`는 `~/dist/js/script.js` 또는 `http://example.com/dist/js/script.js`와 일치합니다.

하지만 `~/script.js`와는 일치하지 않습니다.

- [여러 Origin](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#multiple-origins)

웹 애플리케이션이 여러 origin에서 접근 가능한 경우는 드물지 않습니다. 예를 들면:

* 웹사이트가 `https`와 `http` 모두에서 동작
* 지역별 웹 주소: 예: `https://us.example.com`, `https://eu.example.com`
* 여러 정적 CDN: 예: `https://static1.example.com`, `https://static2.example.com`
* 고객별 도메인/서브도메인

이 상황에서는 **동일한** JavaScript 및 source map 파일이 두 개 이상의 서로 다른 origin에 존재할 수 있습니다. 이런 경우에는 경로에 특수 틸드(`~`) 접두사를 사용하는 것을 권장합니다.

예를 들어, 다음과 같은 파일이 있다면:

* <https://static1.example.com/js/app.js>
* <https://static2.example.com/js/app.js>

`~/js/app.js`의 URL로 업로드할 수 있습니다. 이렇게 하면 Sentry가 도메인을 무시하고 모든 origin에 대해 해당 artifact를 사용합니다.

또한 동일한 파일을 여러 이름으로 업로드할 수도 있습니다. 내부적으로 Sentry가 이를 중복 제거합니다.

`\~` 접두사는 주어진 URL에서 경로가 `/js/app.js`인 경우, **모든** protocol과 hostname 조합에 대해 이 artifact를 사용해야 함을 Sentry에 알립니다. 이 방법은 가능한 모든 protocol/hostname 조합에서 source/source map 파일이 동일할 때만 사용하세요. **전체 URL이 발견되면 Sentry는 틸드 접두사 경로보다 전체 URL을 우선합니다.**

- [`sourceMappingURL` 값과 artifact 이름이 일치하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-artifact-names-match-sourcemappingurl-value)

번들되었거나 minify된 JavaScript 파일의 마지막 줄에 있는 `sourceMappingURL` 주석은 해당 source map의 위치를 Sentry(또는 브라우저)에 알려줍니다. 이는 전체 URL, 상대 경로, 또는 파일명 자체일 수 있습니다. Sentry에 artifact를 업로드할 때는 파일이 최종적으로 해석되는 값으로 source map 파일 이름을 지정해야 합니다.

즉, 파일이 다음과 같고:

```javascript
// -- end script.min.js
//# sourceMappingURL=script.min.js.map
```

<http://example.com/js/script.min.js>에 호스팅되어 있다면, Sentry는 해당 source map 파일을 <http://example.com/js/script.min.js.map>에서 찾습니다. 따라서 업로드한 artifact 이름은 `http://example.com/js/script.min.js.map`(또는 `~/js/script.min.js.map`)이어야 합니다.

또는 파일이 다음과 같다면:

```javascript
//-- end script.min.js
//# sourceMappingURL=https://example.com/dist/js/script.min.js.map
```

업로드한 artifact 이름도 `https://example.com/dist/js/script.min.js.map`(또는 `~/dist/js/script.min.js.map`)이어야 합니다.

마지막으로 파일이 다음과 같다면:

```javascript
//-- end script.min.js
//# sourceMappingURL=../maps/script.min.js.map
```

업로드한 artifact 이름은 `https://example.com/dist/maps/script.min.js.map`(또는 `~/dist/maps/script.min.js.map`)이어야 합니다.

- [오류가 발생하기 전에 artifact가 업로드되는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-artifacts-are-uploaded-before-errors-occur)

Sentry는 특정 release의 source code와 source map이 해당 release에서 오류가 발생하기 **전에** Sentry에 업로드되어 있기를 기대합니다.

Sentry가 오류를 수집한 **후에** artifact를 업로드하면, Sentry는 이전 오류로 돌아가 source annotation을 소급 적용하지 않습니다. artifact 업로드 이후에 새로 발생한 오류에만 영향이 있습니다.

- [source map이 올바르게 빌드되었는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-your-source-maps-are-built-correctly)

**호스팅된** 소스와 source map을 테스트할 수 있는 온라인 검증 도구 [sourcemaps.io](https://sourcemaps.io)를 제공합니다.

또는 Sentry CLI로 source map을 Sentry에 업로드하는 경우, `--validate` 명령줄 옵션을 사용해 source map이 올바른지 검증할 수 있습니다.

- [source map이 로컬에서 동작하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-your-source-maps-work-locally)

Sentry가 filename, line, column 매핑을 올바르게 처리하지 못한다면, source map이 로컬에서 정상 동작하는지 확인해야 합니다. 이를 위해 Node.js와 Mozilla의 [source-map library](https://github.com/mozilla/source-map)를 함께 사용할 수 있습니다.

먼저 `source-map`을 npm 모듈로 전역 설치하세요:

```bash
npm install -g source-map
```

그다음 source map 파일을 읽고 매핑을 테스트하는 Node.js 스크립트를 작성합니다. 예시는 다음과 같습니다:

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

로컬에서도 Sentry와 동일한(잘못된) 결과가 나온다면, source map 생성 설정을 다시 확인하세요.

- [artifact가 gzip되지 않았는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-artifacts-are-not-gzipped)

현재 Sentry API는 일반 텍스트(UTF-8 인코딩)로 업로드된 source map 및 source 파일만 처리할 수 있습니다. 파일이 압축 형식(예: gzip)으로 업로드되면 올바르게 해석되지 않습니다.

`sentry-cli`로 artifact를 업로드하는 경우, `2.4.0` 버전부터 `sourcemaps upload` 명령에 `--decompress` 플래그를 추가할 수 있습니다.

빌드 스크립트나 플러그인이 사전 압축된 minify 파일(예: webpack의 [compression plugin](https://github.com/webpack/compression-webpack-plugin))을 생성하는 경우가 있습니다. 이런 경우 해당 플러그인을 비활성화하고, 생성된 source map/source 파일을 Sentry에 업로드한 **후에** 압축을 수행해야 합니다.

- [(Self-Hosted Sentry) `symbolicator` 서비스가 정상 동작하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#self-hosted-sentry-verify-the-symbolicator-service-is-operating-normally)

Self-hosted 버전의 Sentry를 운영 중이라면, 컨테이너 로그를 확인하여 `symbolicator` 서비스/컨테이너가 정상 동작하는지 검증할 수 있습니다.

- [(Docker 기반 Self-Hosted Sentry) workers가 web과 동일한 볼륨을 공유하는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#self-hosted-sentry-via-docker-verify-workers-are-sharing-the-same-volume-as-web)

Sentry는 worker에서 source map 계산을 수행합니다. 즉, worker가 프런트엔드를 통해 업로드된 파일에 접근할 수 있어야 합니다. cron worker와 web worker가 동일한 디스크에서 파일을 읽고/쓸 수 있는지 다시 확인하세요.

- [`source-map-support` 패키지를 사용하고 있지 않은지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/legacy-uploading-methods.md#verify-you-are-not-using-the-source-map-support-package)

Sentry Node.js SDK는 source map을 Sentry에 업로드하지 않은 경우 [source-map-support](https://www.npmjs.com/package/source-map-support) 패키지와 일반적으로 잘 동작합니다.

하지만 source map을 Sentry에 업로드하고 있거나 브라우저에서 Sentry SDK를 사용 중이라면, 코드에서 `source-map-support` 패키지를 사용할 수 없습니다. `source-map-support`가 캡처된 stack trace를 덮어써서 Sentry의 source map processor가 이를 올바르게 파싱하지 못하게 하기 때문입니다.

