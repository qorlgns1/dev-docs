---
title: '안내서: OpenTelemetry'
description: '관측 가능성은 Next.js 앱의 동작과 성능을 이해하고 최적화하는 데 필수적입니다.'
---

# 안내서: OpenTelemetry | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/open-telemetry

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)OpenTelemetry

페이지 복사

# OpenTelemetry로 Next.js 앱 계측하기

마지막 업데이트: 2026년 2월 20일

관측 가능성은 Next.js 앱의 동작과 성능을 이해하고 최적화하는 데 필수적입니다.

애플리케이션이 복잡해질수록 문제를 식별하고 진단하기가 점점 어려워집니다. 로깅과 메트릭 같은 관측 도구를 활용하면 개발자는 앱의 동작을 파악하고 최적화가 필요한 영역을 찾을 수 있습니다. 관측 가능성을 갖추면 주요 문제가 되기 전에 사전 대응하고, 더 나은 사용자 경험을 제공할 수 있습니다. 따라서 Next.js 애플리케이션에서 퍼포먼스를 개선하고 리소스를 최적화하며 사용자 경험을 향상하기 위해 관측 가능성을 적극 권장합니다.

앱 계측에는 OpenTelemetry 사용을 권장합니다. 이는 특정 플랫폼에 종속되지 않은 계측 방식이므로 코드를 변경하지 않고도 관측 공급자를 교체할 수 있습니다. OpenTelemetry 및 작동 방식에 대한 자세한 내용은 [공식 OpenTelemetry 문서](https://opentelemetry.io/docs/)를 확인하세요.

이 문서 전반에서 _Span_, _Trace_, _Exporter_ 같은 용어를 사용하며, 모두 [OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/)에서 확인할 수 있습니다.

Next.js는 기본적으로 OpenTelemetry 계측을 지원하므로, Next.js 자체는 이미 계측되어 있습니다.

OpenTelemetry를 활성화하면 `getStaticProps` 같은 모든 코드를 유용한 속성과 함께 _스팬_ 으로 자동 감쌉니다.

## 시작하기[](https://nextjs.org/docs/pages/guides/open-telemetry#getting-started)

OpenTelemetry는 확장 가능하지만 올바르게 설정하려면 장황해질 수 있습니다. 그래서 빠르게 시작할 수 있도록 `@vercel/otel` 패키지를 준비했습니다.

### `@vercel/otel` 사용하기[](https://nextjs.org/docs/pages/guides/open-telemetry#using-vercelotel)

시작하려면 다음 패키지를 설치하세요:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add @vercel/otel @opentelemetry/sdk-logs @opentelemetry/api-logs @opentelemetry/instrumentation
[/code]

그다음 프로젝트 **루트 디렉터리**(또는 `src` 폴더를 사용 중이라면 `src` 내부)에 커스텀 [`instrumentation.ts`](https://nextjs.org/docs/pages/guides/instrumentation)(또는 `.js`) 파일을 만듭니다:

your-project/instrumentation.ts

JavaScriptTypeScript
[code]
    import { registerOTel } from '@vercel/otel'
     
    export function register() {
      registerOTel({ serviceName: 'next-app' })
    }
[/code]

추가 구성 옵션은 [`@vercel/otel` 문서](https://www.npmjs.com/package/@vercel/otel)를 참고하세요.

> **알아두면 좋은 점** :
> 
>   * `instrumentation` 파일은 프로젝트 루트에 있어야 하며 `app` 또는 `pages` 디렉터리 내부에 두면 안 됩니다. `src` 폴더를 사용한다면 `pages`, `app`과 나란히 `src` 내부에 파일을 두세요.
>   * [`pageExtensions` 구성 옵션](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions)으로 접미사를 추가했다면 `instrumentation` 파일 이름도 동일하게 업데이트해야 합니다.
>   * 활용할 수 있도록 기본 [with-opentelemetry](https://github.com/vercel/next.js/tree/canary/examples/with-opentelemetry) 예제를 제공했습니다.
> 


### 수동 OpenTelemetry 구성[](https://nextjs.org/docs/pages/guides/open-telemetry#manual-opentelemetry-configuration)

`@vercel/otel` 패키지는 많은 구성 옵션을 제공하며 대부분의 일반적인 사용 사례를 충족합니다. 그러나 필요에 맞지 않는다면 OpenTelemetry를 수동으로 구성할 수 있습니다.

먼저 OpenTelemetry 패키지를 설치해야 합니다:

pnpmnpmyarnbun

Terminal
[code]
    pnpm add @opentelemetry/sdk-node @opentelemetry/resources @opentelemetry/semantic-conventions @opentelemetry/sdk-trace-node @opentelemetry/exporter-trace-otlp-http
[/code]

이제 `instrumentation.ts`에서 `NodeSDK`를 초기화할 수 있습니다. `@vercel/otel`과 달리 `NodeSDK`는 엣지 런타임과 호환되지 않으므로 `process.env.NEXT_RUNTIME === 'nodejs'`일 때만 임포트하도록 해야 합니다. Node를 사용할 때만 조건부로 임포트하는 새 파일 `instrumentation.node.ts`를 만드는 것을 권장합니다:

instrumentation.ts

JavaScriptTypeScript
[code]
    export async function register() {
      if (process.env.NEXT_RUNTIME === 'nodejs') {
        await import('./instrumentation.node.ts')
      }
    }
[/code]

instrumentation.node.ts

JavaScriptTypeScript
[code]
    import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'
    import { resourceFromAttributes } from '@opentelemetry/resources'
    import { NodeSDK } from '@opentelemetry/sdk-node'
    import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node'
    import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions'
     
    const sdk = new NodeSDK({
      resource: resourceFromAttributes({
        [ATTR_SERVICE_NAME]: 'next-app',
      }),
      spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
    })
    sdk.start()
[/code]

이 방식은 `@vercel/otel`을 사용하는 것과 동일하지만, `@vercel/otel`에서 노출하지 않은 기능을 수정하거나 확장할 수 있습니다. 엣지 런타임 지원이 필요하다면 `@vercel/otel`을 사용해야 합니다.

## 계측 테스트하기[](https://nextjs.org/docs/pages/guides/open-telemetry#testing-your-instrumentation)

OpenTelemetry 트레이스를 로컬에서 테스트하려면 호환 백엔드를 갖춘 OpenTelemetry 컬렉터가 필요합니다. [OpenTelemetry 개발 환경](https://github.com/vercel/opentelemetry-collector-dev-setup)을 사용하는 것을 권장합니다.

모든 것이 정상이라면 루트 서버 스팬이 `GET /requested/pathname`으로 표시되는 것을 볼 수 있습니다. 해당 트레이스의 다른 모든 스팬은 그 아래에 중첩됩니다.

Next.js는 기본적으로 내보내는 것보다 더 많은 스팬을 추적합니다. 더 많은 스팬을 보려면 `NEXT_OTEL_VERBOSE=1`을 설정해야 합니다.

## 배포[](https://nextjs.org/docs/pages/guides/open-telemetry#deployment)

### OpenTelemetry Collector 사용하기[](https://nextjs.org/docs/pages/guides/open-telemetry#using-opentelemetry-collector)

OpenTelemetry Collector로 배포할 때는 `@vercel/otel`을 사용할 수 있습니다. Vercel과 셀프 호스팅 환경 모두에서 동작합니다.

#### Vercel에 배포하기[](https://nextjs.org/docs/pages/guides/open-telemetry#deploying-on-vercel)

Vercel에서 OpenTelemetry가 즉시 동작하도록 구성해 두었습니다.

[Vercel 문서](https://vercel.com/docs/concepts/observability/otel-overview/quickstart)를 따라 프로젝트를 관측 공급자에 연결하세요.

#### 셀프 호스팅[](https://nextjs.org/docs/pages/guides/open-telemetry#self-hosting)

다른 플랫폼에 배포하는 것도 간단합니다. Next.js 앱에서 전송되는 텔레메트리 데이터를 수신하고 처리할 자체 OpenTelemetry Collector를 구동해야 합니다.

이를 위해 [OpenTelemetry Collector 시작 가이드](https://opentelemetry.io/docs/collector/getting-started/)를 따라 컬렉터를 설정하고 Next.js 앱에서 데이터를 받을 수 있도록 구성하세요.

컬렉터를 실행한 뒤에는 선택한 플랫폼의 배포 가이드를 따라 Next.js 앱을 배포하면 됩니다.

### 커스텀 Exporter[](https://nextjs.org/docs/pages/guides/open-telemetry#custom-exporters)

OpenTelemetry Collector는 필수가 아닙니다. [`@vercel/otel`](https://nextjs.org/docs/pages/guides/open-telemetry#using-vercelotel)이나 [수동 OpenTelemetry 구성](https://nextjs.org/docs/pages/guides/open-telemetry#manual-opentelemetry-configuration)과 함께 커스텀 OpenTelemetry exporter를 사용할 수 있습니다.

## 커스텀 스팬[](https://nextjs.org/docs/pages/guides/open-telemetry#custom-spans)

[OpenTelemetry API](https://opentelemetry.io/docs/instrumentation/js/instrumentation)로 커스텀 스팬을 추가할 수 있습니다.

pnpmnpmyarnbun

Terminal
[code]
    pnpm add @opentelemetry/api
[/code]

다음 예시는 GitHub 스타를 가져오고 `fetchGithubStars` 커스텀 스팬을 추가해 fetch 요청 결과를 추적하는 함수를 보여줍니다:
[code] 
    import { trace } from '@opentelemetry/api'
     
    export async function fetchGithubStars() {
      return await trace
        .getTracer('nextjs-example')
        .startActiveSpan('fetchGithubStars', async (span) => {
          try {
            return await getValue()
          } finally {
            span.end()
          }
        })
    }
[/code]

`register` 함수는 새로운 환경에서 코드가 실행되기 전에 수행됩니다. 새로운 스팬을 생성하면 내보낸 트레이스에 올바르게 추가되어야 합니다.

## Next.js의 기본 스팬[](https://nextjs.org/docs/pages/guides/open-telemetry#default-spans-in-nextjs)

Next.js는 애플리케이션 성능에 대한 유용한 통찰을 제공하기 위해 여러 스팬을 자동으로 계측합니다.

스팬 속성은 [OpenTelemetry 시맨틱 컨벤션](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/)을 따릅니다. `next` 네임스페이스 아래에 몇 가지 커스텀 속성도 추가합니다:

  * `next.span_name` \- 스팬 이름을 복제합니다.
  * `next.span_type` \- 각 스팬 유형마다 고유 식별자가 있습니다.
  * `next.route` \- 요청의 라우트 패턴(예: `/[param]/user`).
  * `next.rsc` (true/false) - 프리페치 같은 RSC 요청인지 여부.
  * `next.page`
    * 앱 라우터에서 사용하는 내부 값입니다.
    * `page.ts`, `layout.ts`, `loading.ts` 등 특수 파일로 가는 라우트로 생각할 수 있습니다.
    * `/layout`은 `/(groupA)/layout.ts`와 `/(groupB)/layout.ts`를 모두 가리킬 수 있으므로 `next.route`와 함께 사용할 때만 고유 식별자로 활용할 수 있습니다.



### `[http.method] [next.route]`[](https://nextjs.org/docs/pages/guides/open-telemetry#httpmethod-nextroute)

  * `next.span_type`: `BaseServer.handleRequest`



이 스팬은 Next.js 애플리케이션으로 들어오는 각 요청의 루트 스팬을 나타냅니다. 요청의 HTTP 메서드, 라우트, 타깃, 상태 코드를 추적합니다.

속성:

  * [일반 HTTP 속성](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#common-attributes)
    * `http.method`
    * `http.status_code`
  * [서버 HTTP 속성](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#http-server-semantic-conventions)
    * `http.route`
    * `http.target`
  * `next.span_name`
  * `next.span_type`
  * `next.route`



### `render route (app) [next.route]`[](https://nextjs.org/docs/pages/guides/open-telemetry#render-route-app-nextroute)

  * `next.span_type`: `AppRender.getBodyResult`.



이 스팬은 앱 라우터에서 라우트를 렌더링하는 과정을 나타냅니다.

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.route`



### `fetch [http.method] [http.url]`[](https://nextjs.org/docs/pages/guides/open-telemetry#fetch-httpmethod-httpurl)

  * `next.span_type`: `AppRender.fetch`



이 스팬은 코드에서 실행된 fetch 요청을 나타냅니다.

속성:

  * [일반 HTTP 속성](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#common-attributes)
    * `http.method`
  * [클라이언트 HTTP 속성](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#http-client)
    * `http.url`
    * `net.peer.name`
    * `net.peer.port` (지정한 경우에만)
  * `next.span_name`
  * `next.span_type`



이 스팬은 환경에서 `NEXT_OTEL_FETCH_DISABLED=1`로 설정하면 끌 수 있습니다. 커스텀 fetch 계측 라이브러리를 사용하려는 경우에 유용합니다.

### `executing api route (app) [next.route]`[](https://nextjs.org/docs/pages/guides/open-telemetry#executing-api-route-app-nextroute)

  * `next.span_type`: `AppRouteRouteHandlers.runHandler`.

이 스팬은 앱 라우터에서 API Route Handler가 실행되는 과정을 나타냅니다.

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.route`



### `getServerSideProps [next.route]`[](https://nextjs.org/docs/pages/guides/open-telemetry#getserversideprops-nextroute)

  * `next.span_type`: `Render.getServerSideProps`.



이 스팬은 특정 라우트에 대한 `getServerSideProps` 실행을 나타냅니다.

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.route`



### `getStaticProps [next.route]`[](https://nextjs.org/docs/pages/guides/open-telemetry#getstaticprops-nextroute)

  * `next.span_type`: `Render.getStaticProps`.



이 스팬은 특정 라우트에 대한 `getStaticProps` 실행을 나타냅니다.

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.route`



### `render route (pages) [next.route]`[](https://nextjs.org/docs/pages/guides/open-telemetry#render-route-pages-nextroute)

  * `next.span_type`: `Render.renderDocument`.



이 스팬은 특정 라우트의 문서를 렌더링하는 과정을 나타냅니다.

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.route`



### `generateMetadata [next.page]`[](https://nextjs.org/docs/pages/guides/open-telemetry#generatemetadata-nextpage)

  * `next.span_type`: `ResolveMetadata.generateMetadata`.



이 스팬은 특정 페이지에 대한 메타데이터를 생성하는 과정을 나타냅니다(단일 라우트에 여러 개의 스팬이 존재할 수 있음).

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.page`



### `resolve page components`[](https://nextjs.org/docs/pages/guides/open-telemetry#resolve-page-components)

  * `next.span_type`: `NextNodeServer.findPageComponents`.



이 스팬은 특정 페이지의 페이지 컴포넌트를 해석하는 과정을 나타냅니다.

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.route`



### `resolve segment modules`[](https://nextjs.org/docs/pages/guides/open-telemetry#resolve-segment-modules)

  * `next.span_type`: `NextNodeServer.getLayoutOrPageModule`.



이 스팬은 레이아웃 또는 페이지를 위한 코드 모듈을 로드하는 과정을 나타냅니다.

속성:

  * `next.span_name`
  * `next.span_type`
  * `next.segment`



### `start response`[](https://nextjs.org/docs/pages/guides/open-telemetry#start-response)

  * `next.span_type`: `NextNodeServer.startResponse`.



이 길이 0의 스팬은 응답에서 첫 바이트가 전송된 시점을 나타냅니다.

도움이 되었나요?

지원됨.

보내기
