---
title: '문제 해결 | Next.js용 Sentry'
description: 'Sentry SDK를 설정했는데 Sentry로 데이터가 전송되지 않는다면:'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting

# 문제 해결 | Next.js용 Sentry

SDK가 어떤 데이터도 전송하지 않음

Sentry SDK를 설정했는데 Sentry로 데이터가 전송되지 않는다면:

* DSN을 구성했고, 이를 `Sentry.init()`의 `dsn` 옵션에 전달하고 있는지 확인하세요.

  환경 변수를 사용해 DSN을 전달하는 경우, 관련된 모든 환경에서 해당 환경 변수가 설정되어 있는지 확인하세요. 또한 프레임워크 내부에서 환경 변수를 사용하는 경우, 프레임워크가 번들에 환경 변수를 포함하는지 확인하세요. 보통 이는 프레임워크에서 정의한 특수 접두사(`NEXT_PUBLIC_` in Next.js, `NUXT_` in Nuxt, `VITE_` for Vite projects, `REACT_APP_` for Create React App, ...)를 환경 변수에 붙여야 함을 의미합니다.

* ad-blocker가 비활성화되어 있는지 확인하세요.

* `Sentry.init()` 옵션에서 `debug: true`를 설정하고 애플리케이션 시작 시 콘솔 출력을 확인하세요. SDK가 왜 데이터를 전송하지 않는지 알려줄 수 있습니다.

* Sentry의 [Stats](https://sentry.io/orgredirect/organizations/:orgslug/stats/) 및 [Subscription](https://sentry.io/orgredirect/organizations/:orgslug/settings/billing/overview/) 페이지를 확인하세요. 할당량을 모두 소진했을 수 있습니다.

- `package.json`에 `sideEffects: false`를 설정하지 않았는지 확인하세요. `package.json`에서 `sideEffects`를 false로 설정하면 Next.js가 SDK 코드를 과도하게 tree shaking하여 사실상 `Sentry.init()` 호출을 삭제하게 됩니다. Sentry SDK를 사용할 때 `sideEffects: false` 설정은 올바르지 않습니다.

새 Sentry SDK 버전으로 업데이트하기

Sentry SDK를 새로운 메이저 버전으로 업데이트하면, 사용자 측에서 일부 조정이 필요한 브레이킹 체인지가 발생할 수 있습니다. 최신 Sentry 기능으로 다시 정상 동작시키는 데 필요한 모든 내용을 [migration guide](https://github.com/getsentry/sentry-javascript/blob/master/MIGRATION.md)에서 확인하세요.

추가 데이터 디버깅

이벤트의 JSON payload를 보면 Sentry가 이벤트의 추가 데이터를 어떻게 저장하는지 확인할 수 있습니다. 데이터의 형태는 설명과 정확히 일치하지 않을 수 있습니다.

자세한 내용은 [Event Payload 전체 문서](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/)를 참고하세요.

최대 JSON payload 크기

기본적으로 `maxValueLength`는 undefined이며 잘림이 발생하지 않지만, 메시지가 더 긴 경우 필요에 따라 이 값을 변경할 수 있습니다(예: `250`). 단, 모든 개별 값이 이 옵션의 영향을 받는 것은 아닙니다.

CORS 속성 및 헤더

서로 다른 origin에서 제공된 스크립트에서 발생한 JavaScript 예외를 가시화하려면 다음 두 가지를 수행하세요:

1. crossorigin=”anonymous” 스크립트 속성 추가

```bash
 <script src="http://another-domain.com/app.js" crossorigin="anonymous"></script>
```

이 스크립트 속성은 브라우저가 대상 파일을 “anonymously” 가져오도록 지시합니다. 이 파일 요청 시 쿠키나 HTTP 자격 증명 같은 잠재적 사용자 식별 정보는 브라우저에서 서버로 전송되지 않습니다.

2. Cross-Origin HTTP 헤더 추가

```bash
Access-Control-Allow-Origin: *
```

Cross-Origin Resource Sharing(CORS)은 origin 간에 파일을 어떻게 다운로드하고 제공해야 하는지를 규정하는 API 집합(대부분 HTTP 헤더)입니다.

`Access-Control-Allow-Origin: *`를 설정하면 서버는 브라우저에 어떤 origin이든 이 파일을 가져올 수 있음을 나타냅니다. 또는 사용자가 제어하는 알려진 origin으로 제한할 수도 있습니다:

```bash
 Access-Control-Allow-Origin: https://www.example.com
```

대부분의 커뮤니티 CDN은 `Access-Control-Allow-Origin` 헤더를 올바르게 설정합니다.

```bash
 $ curl --head https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.js | \
 grep -i "access-control-allow-origin"

 Access-Control-Allow-Origin: *
```

예상치 못한 OPTIONS 요청

추가 OPTIONS 요청 수행으로 인해 애플리케이션 동작이 비정상적으로 바뀌었다면, 브라우저 SDK의 Tracing Integration을 너무 포괄적으로 구성했을 때 발생할 수 있는 불필요한 `sentry-trace` 요청 헤더 문제일 가능성이 높습니다.

이를 해결하려면 SDK 초기화 중 `tracePropagationTargets` 옵션을 변경하세요. 자세한 내용은 Tracing 문서의 [Automatic Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#tracePropagationTarget)을 참고하세요.

\`instrument.js\` 콘솔 로그 구문의 줄 번호

디버깅 중 콘솔에 `instrument.js`가 표시된다면, 다음 패턴을 추가해 Sentry를 [Framework Ignore List](https://developer.chrome.com/docs/devtools/settings/ignore-list/#skip-extensions)에 추가하세요: `/@sentry/`

그러면 Chrome이 디버깅 시 SDK 스택 프레임을 무시합니다.

Ad-Blocker 대응

CDN을 사용하는 경우 ad-blocking 또는 script-blocking 확장 프로그램이 SDK를 정상적으로 가져오고 초기화하는 것을 막을 수 있습니다. 이 때문에 SDK API 호출이 실패하고 애플리케이션이 예기치 않게 동작할 수 있습니다.

또한 SDK가 정상적으로 다운로드되고 초기화되더라도, 캡처된 데이터를 수신해야 하는 Sentry endpoint가 차단될 수 있습니다. 이 경우 오류 리포트, 세션 상태, 성능 데이터가 전달되지 않아 [sentry.io](https://sentry.io)에서 사실상 사용 불가능해집니다.

더 나아가 [Brave](https://brave.com/) 같은 일부 브라우저는 내장 ad-blocker를 통해 endpoint로 전송된 요청을 차단할 수 있습니다. 사용자가 도메인 차단을 해제하더라도 Brave는 [service worker에서 발생한 요청](https://github.com/getsentry/sentry/issues/47912#issuecomment-1573714875)을 계속 차단할 수 있습니다.

CDN 번들 차단은 [NPM 패키지 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md#using-the-npm-package)과 앱 번들링으로 우회할 수 있습니다. 하지만 endpoint 차단은 아래 설명처럼 tunnel을 사용해야만 해결할 수 있습니다.

\`tunnel\` 옵션 사용하기

Sentry Next.js SDK에는 tunnel 설정을 매우 간단하게 해 주는 별도 옵션이 있어, 아래 설정 과정을 건너뛸 수 있습니다. Next.js에서 tunneling을 설정하는 방법은 [`tunnelRoute`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/build.md#tunnelRoute)를 참고하세요.

`tunnelRoute`를 구성하고 싶지 않다면 아래 가이드를 따르면 됩니다.

tunnel은 Sentry와 애플리케이션 사이에서 프록시 역할을 하는 HTTP endpoint입니다. 이 서버는 사용자가 제어하므로 여기에 전송되는 요청이 차단될 위험이 없습니다. endpoint가 동일 origin 아래에 있으면(터널 동작에 필수는 아님) 브라우저는 해당 endpoint로의 요청을 서드파티 요청으로 취급하지 않습니다. 그 결과 기본적으로 ad-blocker를 유발하지 않는 다른 보안 조치가 적용됩니다. 흐름 요약은 아래에서 확인할 수 있습니다.

JavaScript SDK `6.7.0` 버전부터는 `tunnel` 옵션을 사용해 SDK가 DSN 대신 구성된 URL로 이벤트를 전달하도록 할 수 있습니다. 이렇게 하면 SDK가 쿼리 파라미터에서 `sentry_key`를 제거할 수 있는데, 이것이 ad-blocker가 이벤트 전송을 막는 주요 원인 중 하나입니다. 이 옵션은 SDK가 preflight 요청을 보내는 것도 중단시키며, 이는 원래 쿼리 파라미터에 `sentry_key`를 보내야 했던 요구사항 중 하나였습니다.

`tunnel` 옵션을 활성화하려면 `Sentry.init` 호출에서 상대 URL 또는 절대 URL을 제공하세요. 상대 URL을 사용하면 현재 origin 기준으로 해석되며, 이것이 권장 방식입니다. 상대 URL은 preflight CORS 요청을 유발하지 않으므로 ad-blocker가 이벤트를 서드파티 요청으로 취급하지 않아 이벤트가 차단되지 않습니다. `@sentry/node` 또는 `@sentry/bun` 같은 서버 측 SDK에서 tunneling을 사용할 때는 절대 URL을 제공해야 합니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tunnel: "/tunnel",
});
```

구성 후에는 모든 이벤트가 `/tunnel` endpoint로 전송됩니다. 다만 이 방법은 서버에서 추가 구성이 필요합니다. 이제 이벤트를 파싱해 Sentry로 리디렉션해야 하기 때문입니다. 서버 컴포넌트 예시는 다음과 같습니다:

```csharp

// This functionality is now built-in to the Sentry.AspNetCore package.
// See https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/#tunnel
// docs for more information.

// This example shows how you could implement it yourself:

using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Text.Json;
using Microsoft.AspNetCore;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;

// Change host appropriately if you run your own Sentry instance.
const string host = "sentry.io";
// Set knownProjectIds to a list with your Sentry project IDs which you
// want to accept through this proxy.
var knownProjectIds = new HashSet<string>() {  };

var client = new HttpClient();
WebHost.CreateDefaultBuilder(args).Configure(a =>
    a.Run(async context =>
    {
        context.Request.EnableBuffering();
        using var reader = new StreamReader(context.Request.Body);
        var header = await reader.ReadLineAsync();
        var headerJson = JsonSerializer.Deserialize<Dictionary<string, object>>(header);
        if (headerJson.TryGetValue("dsn", out var dsnString)
            && Uri.TryCreate(dsnString.ToString(), UriKind.Absolute, out var dsn))
        {
            var projectId = dsn.AbsolutePath.Trim('/');
            if (knownProjectIds.Contains(projectId) && string.Equals(dsn.Host, host, StringComparison.OrdinalIgnoreCase)) {
              context.Request.Body.Position = 0;
              await client.PostAsync($"https://{dsn.Host}/api/{projectId}/envelope/",
                  new StreamContent(context.Request.Body));
            }
        }
    })).Build().Run();
```

사용 사례가 SDK 패키지 자체 차단과 관련되어 있다면, 다음 해결책 중 어느 것이든 도움이 됩니다.

- [NPM 패키지 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md#using-the-npm-package)

스크립트 차단 확장 프로그램에 대응하는 가장 좋은 방법은 `npm`을 통해 SDK 패키지를 직접 사용하고 애플리케이션과 함께 번들링하는 것입니다. 이렇게 하면 코드가 항상 기대한 대로 존재함을 보장할 수 있습니다.

- [CDN 번들 셀프 호스팅](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md#self-hosting-cdn-bundles)

두 번째 방법은 CDN에서 SDK를 다운로드해 직접 호스팅하는 것입니다. 이렇게 하면 SDK는 여전히 나머지 코드와 분리되지만, 웹사이트와 동일한 origin에서 제공되므로 차단되지 않음을 확신할 수 있습니다.

`curl` 또는 유사한 도구로 쉽게 가져올 수 있습니다:

```bash
curl https://browser.sentry-cdn.com/5.20.1/bundle.min.js -o sentry.browser.5.20.1.min.js -s
```

- [JavaScript Proxy API 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting.md#using-the-javascript-proxy-api)

마지막 옵션은 `Proxy` 가드를 사용하는 것입니다. 이렇게 하면 SDK가 차단된 상태에서 SDK API를 호출하더라도 코드가 깨지지 않도록 보장할 수 있습니다. `Proxy`는 Internet Explorer를 제외한 모든 브라우저에서 지원되며, 이 브라우저에는 확장 프로그램이 없습니다. 또한 사용자 브라우저에 `Proxy`가 없더라도 조용히 건너뛰므로 무언가가 깨질 걱정은 하지 않아도 됩니다.

이 스니펫은 CDN 번들을 포함하는 `<Expandable>` 태그 **바로 위**에 배치하세요. 가독성 있는 형식의 스니펫은 다음과 같습니다:

```javascript
if ("Proxy" in window) {
  var handler = {
    get: function (_, key) {
      return new Proxy(function (cb) {
        if (key === "flush" || key === "close") return Promise.resolve();
        if (typeof cb === "function") return cb(window.Sentry);
        return window.Sentry;
      }, handler);
    },
  };
  window.Sentry = new Proxy({}, handler);
}
```

스니펫을 바로 복사해 붙여넣고 싶다면, 아래는 minified 버전입니다:

```html
<script>
  if ("Proxy" in window) {
    var n = {
      get: function (o, e) {
        return new Proxy(function (n) {
          return "flush" === e || "close" === e
            ? Promise.resolve()
            : "function" == typeof n
              ? n(window.Sentry)
              : window.Sentry;
        }, n);
      },
    };
    window.Sentry = new Proxy({}, n);
  }
</script>
```

서드파티 promise 라이브러리

Sentry를 포함하고 구성하면, JavaScript SDK는 기본적으로 전역 핸들러를 자동으로 연결해 처리되지 않은 예외와 처리되지 않은 promise rejection을 *capture*합니다. 이 기본 동작은 GlobalHandlers integration에서 `onunhandledrejection` 옵션을 `false`로 바꿔 비활성화할 수 있으며, 각 이벤트 핸들러를 수동으로 연결한 뒤 `Sentry.captureException` 또는 `Sentry.captureMessage`를 직접 호출하면 됩니다.

promise 구현에 서드파티 라이브러리를 사용한다면 구성도 함께 관리해야 할 수 있습니다. 또한 브라우저는 서로 다른 origin에서 스크립트 파일을 제공할 때 오류 리포팅을 차단할 수 있는 보안 조치를 자주 적용한다는 점을 기억하세요.

'Non-Error Exception'이 포함된 이벤트

“Non-Error exception (or promise rejection) captured with keys: x, y, z.”라는 메시지의 오류가 보인다면, a) `Sentry.captureException()`을 일반 객체와 함께 호출했거나, b) 일반 객체를 throw했거나, c) 일반 객체로 promise를 reject했기 때문입니다.

문제가 되는 non-Error 객체의 내용은 “Additional Data” 섹션의 `__serialized__` 항목에서 확인할 수 있습니다.

이 오류 이벤트를 더 잘 파악하려면 `__serialized__` 데이터 내용을 바탕으로 일반 객체가 Sentry로 전달되거나 throw되는 위치를 찾은 다음, 해당 일반 객체를 Error 객체로 바꾸는 것을 권장합니다.

리소스 404 캡처하기

기본적으로 Sentry는 리소스(예: 이미지 또는 css 파일) 로드 실패 시 발생하는 오류를 캡처하지 않습니다. 이를 캡처하려면 다음 코드를 사용할 수 있습니다. (참고: 어떤 경우든 Sentry는 가능한 한 이르게 로드하는 것을 권장하지만, 특히 이 방법은 Sentry가 다른 리소스보다 먼저 로드된 경우에만 동작합니다.)

```javascript
document.body.addEventListener(
  "error",
  (event) => {
    if (!event.target) return;

    if (event.target.tagName === "IMG") {
      Sentry.captureException(
        new Error(`Failed to load image: ${event.target.src}`),
      );
    } else if (event.target.tagName === "LINK") {
      Sentry.captureException(
        new Error(`Failed to load css: ${event.target.href}`),
      );
    }
  },
  true, // useCapture - necessary for resource loading errors
);
```

`addEventListener()`의 두 번째 파라미터로 `true`를 전달하는 것을 잊지 마세요. 이를 생략하면 이벤트 핸들러가 호출되지 않습니다. 핸들러가 이벤트 타깃 자체가 아니라 조상에 추가되기 때문이며, JavaScript 런타임 오류와 달리 로드 실패로 인한 `error` 이벤트는 버블링되지 않아서 `capture` 단계에서 반드시 캡처해야 합니다. 자세한 내용은 [W3C 스펙](https://www.w3.org/TR/2003/NOTE-DOM-Level-3-Events-20031107/events.html#Events-phases)을 참고하세요.

SDK가 `addEventListener`를 이중 호출하게 만드는 문제(예: 클릭 이벤트 중복 발생)

아주 드문 경우, SDK로 인해 이벤트 대상(예: 버튼)에 `addEventListener`로 추가한 콜백이 두 번 호출될 수 있습니다. 이는 보통 페이지 라이프사이클에서 SDK가 너무 늦게 초기화되었다는 신호입니다. 가능하다면 애플리케이션에서 SDK를 더 이른 시점에 초기화해 보세요.

이것이 불가능하거나 현재 사용 사례에 해당하지 않는다면, [`browserApiErrors` integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md)의 `unregisterOriginalCallbacks` 옵션을 `true`로 설정하세요.

vite에서 발생하는 빌드 오류

[Vite Bundler](https://vitejs.dev/)와 Sentry NPM 패키지를 함께 사용 중이고, 아래와 같은 오류가 보인다면:

```bash
Error: Could not resolve './{}.js' from node_modules/@sentry/utils/esm/index.js
```

이는 Vite 설정의 [`define`](https://vitejs.dev/config/shared-options.html#define) 옵션이 `global` 같은 Sentry SDK 내부 변수를 문자열 치환하고 있어서 빌드 오류가 발생하는 경우일 수 있습니다. Vite는 `define`을 상수(CONSTANTS) 용도로만 사용하고, 옵션에 `process`나 `global`을 넣지 않기를 권장합니다. 이 빌드 오류를 해결하려면 아래 예시처럼 `define` 옵션을 제거하거나 수정하세요.

`vite.config.ts`

```javascript
export default defineConfig({
   build: {
     sourcemap: 'hidden'
   },
-  define: {
-    global: {}
-  },
   plugins: [react()]
})
```

`diagnostics_channel` 모듈 누락

JavaScript SDK 사용 중 "Cannot find module diagnostics_channel"와 유사한 빌드 오류가 발생한다면, 빌드 도구에서 `diagnostics_channel` 모듈을 external 처리하거나 무시하도록 설정해 보세요. Sentry Node.js SDK는 Node.js fetch 요청을 계측하기 위해 이 내장 모듈을 사용합니다. 일부 구버전 Node.js에는 `diagnostics_channel` API가 없어, 코드를 번들링할 때 빌드 오류가 발생할 수 있습니다.

대부분의 번들러는 특정 모듈(예: `diagnostics_channel`)을 external 처리하는 옵션을 제공합니다:

* [Externals in Webpack](https://webpack.js.org/configuration/externals/)
* [External in Vite](https://vitejs.dev/config/ssr-options.html#ssr-external)
* [External in esbuild](https://esbuild.github.io/api/#external)
* [External in Rollup](https://rollupjs.org/configuration-options/#external)

Terser 플러그인 빌드 오류

Terser 또는 다른 minifier를 사용하는 커스텀 webpack 플러그인을 쓰는 경우, 알려진 webpack 버그로 인해 빌드 오류가 발생할 수 있습니다. 이 문제는 webpack 5.85.1 이상에서 수정되었습니다.

이 이슈의 자세한 내용은 [webpack/terser-plugin build errors](https://github.com/getsentry/sentry-javascript/issues/14091)를 참고하세요.

pnpm: 'import-in-the-middle' external 패키지 오류 해결

pnpm 사용 시 external 처리할 수 없는 패키지 관련 오류가 발생할 수 있으며, 특히 `import-in-the-middle`, `require-in-the-middle` 같은 패키지에서 자주 나타납니다. 이러한 오류는 보통 pnpm의 엄격한 의존성 관리와 hoisting 동작 때문에 발생합니다.

이 패키지들을 직접 의존성으로 추가하면 경고 메시지는 사라질 수 있지만, 근본적인 기능 문제는 해결되지 않는 경우가 많습니다:

```bash
pnpm add import-in-the-middle require-in-the-middle
```

우회 방법으로, 프로젝트 루트의 `.npmrc`를 생성하거나 수정하세요. 먼저 문제 패키지만 선택적으로 hoist해 보세요:

`.npmrc`

```ini
public-hoist-pattern[]=*import-in-the-middle*
public-hoist-pattern[]=*require-in-the-middle*
```

그래도 해결되지 않으면, pnpm이 모든 의존성을 hoist하도록 설정할 수도 있습니다:

`.npmrc`

```ini
shamefully-hoist=true
```

**참고**: `shamefully-hoist=true`는 의존성 관리 관점에서 일반적으로 이상적인 해법은 아니지만, npm 또는 yarn과 유사한 Node.js 모듈 해석 동작을 기대하는 일부 패키지와의 호환성을 위해 필요한 경우가 있습니다.

빌드 중 Out of Memory (OOM) 오류

이 문제는 빌드 과정, 특히 소스맵 생성 시 메모리 사용량과 관련이 있습니다. 가능한 해결책과 우회 방법은 다음과 같습니다:

* `@sentry/nextjs` 패키지를 최신 버전으로 업데이트하세요.
* Node.js 메모리 한도 늘리기: 빌드 중 Node.js 메모리 제한을 높여 볼 수 있습니다. 빌드 명령에 다음을 추가하세요: `NODE_OPTIONS="--max-old-space-size=8192" next build`. 이 플래그는 node 프로세스가 사용할 수 있는 메모리를 8GB로 늘립니다. 대부분의 경우 Next.js는 약 4GB를 소비하는 것으로 확인되었습니다. 사용 가능한 메모리에 맞춰 값을 줄이세요.
* 소스맵 완전 비활성화: 최후의 수단으로 소스맵 생성을 완전히 끌 수 있습니다:

`next.config.js`

```js
  module.exports = withSentryConfig(module.exports, {
    sourcemaps: {
      disable: true,
    },
  }
```

Nx 모노레포에서 Sentry Next SDK 사용하기 (`@nx/next` 사용)

Nx 모노레포 환경에서 Sentry Next.js SDK를 설정하려면 다음 구성을 고려하세요:

`next.config.js`

```js
  const nextConfig = {
  // ...
  };

  const plugins = [
  // Your plugins excluding withNx
  ];

  module.exports = async (phase, context) => {
    let updatedConfig = plugins.reduce((acc, fn) => fn(acc), nextConfig);

    // Apply the async function that `withNx` returns.
    updatedConfig = await withNx(updatedConfig)(phase, context);

    return updatedConfig;
  };

  // The Sentry plugin should always be applied last
  const { withSentryConfig } = require('@sentry/nextjs');
  module.exports = withSentryConfig(module.exports)
```

Client Instrumentation Hook - 느린 실행 감지됨

개발 빌드에서 이 경고가 보이더라도 Next.js dev server 내부 동작 때문에 오해의 소지가 있을 수 있습니다.

Session Replay를 사용 중이고 client instrumentation hook에서 성능 문제가 있다면, [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#lazy-loading-replay)에 설명된 대로 session replay를 지연 로드해 보세요.

SDK 자체를 더 늦은 시점에 init하면 트레이싱 데이터 정확도가 떨어지고 SDK 초기화 전에 오류가 발생할 수 있습니다. 이는 사용 사례에 따라 감수해야 할 트레이드오프지만, 가능한 한 이른 시점에 SDK를 초기화하는 것을 권장합니다.

추가 도움이 필요하면 [GitHub에서 문의](https://github.com/getsentry/sentry-javascript/issues/new/choose)할 수 있습니다. 유료 플랜 고객은 지원팀에 직접 문의할 수도 있습니다.

## 이 섹션의 페이지

- [Supported Browsers](https://docs.sentry.io/platforms/javascript/guides/nextjs/troubleshooting/supported-browsers.md)

