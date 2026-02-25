---
title: '문제 해결 | Sentry for Next.js'
description: '리플레이가 내 애플리케이션과 일치하지 않습니다'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/troubleshooting

# 문제 해결 | Sentry for Next.js

리플레이가 내 애플리케이션과 일치하지 않습니다

리플레이 재생 결과가 애플리케이션의 실제 모습과 일치하지 않을 수 있는 몇 가지 경우가 있습니다. 아래는 이런 문제가 발생할 때의 일반적인 원인과 해결 방법입니다.

- [리플레이에서 요소가 누락됨](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/troubleshooting.md#missing-elements-from-the-replay)

* `<frame>`( `<iframe>`와 혼동하지 마세요) 같은 지원되지 않거나 더 이상 권장되지 않는 요소를 사용하고 있을 수 있습니다.
* [privacy configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#blocking)에 의해 요소가 차단되었을 수 있습니다(기본적으로 `sentry-block` 클래스명 또는 `data-sentry-block` 속성을 가진 요소).

- [CSS가 잘못되었거나 누락됨](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/troubleshooting.md#css-is-wrong-or-missing)

* 복잡한 CSS 선택자에서 스타일이 깨지는 예외적인 경우가 있을 수 있습니다. 이 문제가 발생하면 [GitHub issue](https://github.com/getsentry/sentry-javascript/issues)를 등록해 주세요.

내 \`canvas\` 요소가 캡처되지 않습니다

Canvas는 SDK 버전 >= `7.98.0`에서 지원됩니다. canvas 기록을 시작하려면 [canvas setup documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#canvas-recording)를 참고하세요.

지원되는 SDK 버전을 사용 중인데도 `canvas` 요소가 캡처되지 않는다면, `canvas` 내부에 다른 출처(foreign origin)에서 로드된 이미지나 비디오가 있는지 확인하세요. CORS 승인이 없는 출처에서 로드된 데이터는 안전하지 않은 것으로 간주되며, replay canvas integration을 사용할 때 `SecurityError`가 발생합니다. 이 문제를 해결하려면 이미지나 비디오에 `crossorigin="anonymous"`를 설정하세요. 그러면 다른 출처에서 로드된 이미지도 현재 출처에서 로드된 것처럼 `canvas`에서 사용할 수 있습니다. 교차 출처 접근에 대한 자세한 내용은 [CORS documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_enabled_image#security_and_tainted_canvases)을 참고하세요.

Replay 때문에 내 \`canvas\`가 느려집니다

integration은 3D 및 WebGL canvas에서 이미지를 내보내기 위해 `preserveDrawingBuffer`를 활성화해야 합니다. 이로 인해 canvas 성능이 저하될 수 있습니다. `preserveDrawingBuffer` 활성화로 canvas 애플리케이션에 영향이 있다면 [enable manual snapshotting](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#canvas-recording-performance)을 설정하고 다시 그리는 루프 내부에서 `snapshot()` 메서드를 호출해야 합니다.

Replay를 볼 때 커스텀 CSS/images/fonts/media가 나타나지 않습니다

리플레이 'video'는 실제 비디오가 아니라 웹사이트 HTML을 비디오처럼 재현한 결과물입니다. 즉 사이트가 사용하는 모든 외부 리소스(CSS/Images/Fonts)는 사이트의 해당 \<style>, \<img>, \<video> 태그를 통해 렌더링됩니다. `sentry.io`에서 호스팅되는 iframe이 이 리소스를 가져와 표시할 수 있도록 CORS 정책에 `sentry.io`를 추가하세요.

Replay는 정적이고 공개적으로 호스팅된 비디오(예: `src="./my-video.mp4"`)만 캡처할 수 있습니다. 스트리밍 비디오 등은 지원되지 않습니다.

[브라우저 제한](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/use)으로 인해 `<use>` 태그가 포함되고 링크 대상이 사용자 도메인인 SVG는 CORS 정책에 `sentry.io`를 추가해도 다른 출처에서 접근할 수 없습니다. 이는 알려진 문제이며 해결 방법을 작업 중입니다.

왜 rage click이 너무 많거나 너무 적게 보이나요?

사용자가 사이트 응답을 7초 임계값 이전에 기다리기를 멈췄다면, 예상보다 rage click이 적게 보일 수 있습니다. 그래서 실제로 보이는 rage click 이슈는 매우 가치가 있습니다. 최소 3번 클릭하고 사이트 응답을 위해 최소 7초 이상 기다린 사용자는 상당히 불편을 겪고 있을 가능성이 높기 때문입니다.

DOM mutation이나 페이지 스크롤을 유발하지 않는 버튼(예: "Print", "Download")에서 예상보다 많은 rage click이 보일 수도 있습니다. SDK는 다운로드나 인쇄가 시작되었는지 신뢰성 있게 감지할 방법이 없기 때문에, 버튼이 실제로 "dead" 상태가 아니어도 slow click이 생성될 수 있습니다. 이런 경우 `slowClickIgnoreSelectors`를 통해 SDK를 설정할 수 있습니다. 자세한 내용은 [Configuration](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md)을 참고하세요.

예를 들어, 애플리케이션의 다운로드 링크에서 dead click 및 rage click 감지를 무시하려면:

```javascript
Sentry.replayIntegration({
  slowClickIgnoreSelectors: [
    ".download",
    // Any link with a label including "download" (case-insensitive)
    'a[label*="download" i]',
  ],
});
```

왜 전체 HTTP request body나 모든 headers를 볼 수 없나요?

기본적으로 Replay는 애플리케이션의 모든 outgoing fetch 및 XHR 요청에 대한 기본 정보를 캡처합니다. 여기에는 URL, 요청/응답 body 크기, method, status code가 포함됩니다. 이는 개인 데이터 수집 가능성을 줄이기 위한 목적입니다. [SDK를 설정해 body와 추가 headers를 캡처](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md)할 수 있습니다.

body가 보이지 않는 또 다른 이유는 형식이 지원되지 않기 때문일 수 있습니다. 우리는 JSON, XML, FormData 등 텍스트 기반 body만 캡처합니다. 캡처된 body는 최대 150k characters로 잘립니다. body를 JSON으로 식별하면 payload가 유효한 JSON으로 유지되도록 자르려고 시도합니다. byte, file, media 타입의 body는 캡처되지 않습니다.

이 기능에 대한 자세한 내용은 [configuration page](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md)에서 확인할 수 있습니다.

SDK 때문에 내 웹사이트가 느려집니다.

웹사이트에서 성능 저하가 발생한다면, 먼저 최신 버전 SDK를 사용 중인지 확인하세요. 최신 버전에는 가장 최근의 버그 수정과 성능 개선이 반영되어 있습니다.

성능에 영향을 줄 수 있는 주요 원인 두 가지를 확인했으며, 이에 따라 여러 성능 저하 방지 장치를 추가했습니다. 두 가지 원인은 대량의 mutations가 발생하는 웹사이트(자세한 내용은 아래 항목 참고)와 큰 console 메시지입니다.

이 문제를 완화하기 위해 SDK 버전 7.54.0에서는 [console messages를 truncate](https://github.com/getsentry/sentry-javascript/pull/7917)하고, mutations가 매우 많은 페이지에서는 Replay 기록을 비활성화합니다.

최신 SDK 버전에서도 문제가 있다면 알려주세요. [GitHub issue](https://github.com/getsentry/sentry-javascript/issues/new?assignees=\&labels=Type%3A+Bug\&projects=\&template=bug.yml)를 열어 상황을 설명해 주세요.

Session Replay를 사용하면 내 애플리케이션의 bundle size가 증가합니다.

브라우저 환경의 복잡성 때문에 Session Replay가 동작하려면 상당한 양의 코드가 필요합니다. Session Replay를 활성화하면 애플리케이션 번들에 약 50 kb(gzipped)가 추가되지만, 우리는 그 이점이 비용을 상회한다고 봅니다.

번들 크기를 줄이는 방법은 계속 개선하고 있습니다. 또한 사용 사례에 맞춰 Session Replay 크기를 줄이기 위해 취할 수 있는 단계도 있습니다. 자세한 내용은 [Tree Shaking](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md)을 참고하세요.

다음 메시지가 보입니다: "A large number of mutations was detected (N). This can slow down the Replay SDK and impact your customers."

Sentry SDK는 몇 가지 방법으로 잠재적인 [performance overhead](https://docs.sentry.io/product/explore/session-replay/performance-overhead.md#how-is-session-replay-optimized)를 최소화하려고 합니다. 예를 들어 발생 중인 DOM mutations 수를 추적하고, 변경이 과도하게 많아지면 기록을 비활성화합니다. 동시 mutations가 많으면 Session Replay 설치 여부와 관계없이 웹 페이지가 느려질 수 있지만, 대량의 mutations가 발생하면 Replay client가 각 변경을 기록해야 하므로 추가적인 지연이 생길 수 있습니다.

리플레이를 보는 중에 "A large number of mutations was detected" 메시지가 표시된다면 페이지를 최적화할 여지가 있다는 뜻입니다. 예를 들어 항목이 수천 개인 드롭다운 리스트는 화면에 보이는 행만 DOM에 렌더링하도록 virtualized 방식으로 리팩터링할 수 있습니다. 또 다른 해결책으로는 결과를 paginate하거나 사용자가 스크롤할 때 추가 데이터를 가져오는 방법이 있습니다. SDK에는 기록 중지 전 임계값을 설정할 수 있는 [configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/configuration.md#mutation-limits)이 있습니다.

iframe 내부 텍스트가 마스킹되지 않습니다

마스킹 로직은 `src`로 로드되는 iframe 콘텐츠에는 적용되지만, `srcdoc` 속성으로 제공되는 iframe 콘텐츠에는 적용되지 않습니다.

이 콘텐츠를 숨기려면 Session Replay [Privacy](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy.md#blocking) 문서에 설명된 대로 iframe을 차단하세요.

다음 오류가 발생합니다: Blocked a frame with origin '...' from accessing a frame with origin '...'. Protocols, domains, and ports must match.

replay SDK가 cross-origin frame에 접근하려 했지만 허용되지 않았습니다. 오류를 중지하려면 iframe을 차단해야 합니다:

```javascript
Sentry.init({
  dsn: "...",
  replaysSessionSampleRate: 1,
  integrations: [
    Sentry.replayIntegration({
      block: ["iframe"],
    }),
  ],
});
```

브라우저 확장에서 Replay가 동작하지 않습니다

이 사용 방식은 지원되지 않습니다. replay 패키지는 웹사이트에서 동작하도록 만들어졌으며, 브라우저 확장이나 기타 메커니즘으로 외부 로드되는 스크립트 방식은 지원하지 않습니다. 실제로 Sentry의 Session Replay 제품은 서드파티 Chrome 확장 프로그램이 웹사이트에서 디버깅/재현이 어려운 문제를 유발하는 상황을 개발자가 파악하는 데 도움이 됩니다.

Apollo GraphQL Client 네트워크 요청의 response data가 캡처되지 않습니다

Apollo Client는 쿼리가 완료될 때마다 `AbortController`를 통해 abort signal을 보내, 진행 중인 모든 쿼리를 정리하고 취소합니다. 이 경우 Replay가 응답에 접근하기 전에 요청이 중단된 것으로 처리되어 response body를 캡처할 수 없습니다.

이를 피하려면 자체 abort signal을 설정해 Apollo Client의 이 동작을 비활성화하세요:

```javascript
const abortController = new AbortController();

const httpLink = createHttpLink({
  // ... other options
  fetchOptions: {
    signal: abortController.signal, // overwrite the default abort signal
  },
});
```

이 설정을 사용하면 Replay가 Apollo Client 요청의 response body를 캡처할 수 있습니다.

\`console\` 호출이 리플레이 기록을 트리거합니다

[`captureConsoleIntegration`](https://docs.sentry.io/platforms/javascript/configuration/integrations/captureconsole.md)을 사용하면 예외를 트리거한 것처럼 리플레이 기록이 시작될 수 있습니다. 이 동작을 피하려면 [`beforeErrorSampling`](https://docs.sentry.io/platforms/javascript/guides/sveltekit/session-replay/understanding-sessions.md#ignore-certain-errors-for-error-sampling)을 사용할 수 있습니다.

클릭이 잘못 dead click 또는 rage click으로 처리됩니다

일부 경우(예: 오디오 클립 재생 버튼 클릭)에는 Sentry가 클릭을 dead click으로 잘못 기록할 수 있습니다(참고: rage click은 dead click의 하위 집합입니다). 우회 방법으로 [`slowClickIgnoreSelector`](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md#general-integration-configuration) 설정 옵션을 사용해 특정 selector의 dead click을 무시할 수 있습니다.

[rage click issues](https://docs.sentry.io/product/issues/issue-details/replay-issues.md)를 완전히 끄고 싶다면, Sentry의 **Settings** 페이지로 이동해 "Projects"를 클릭한 뒤 rage click을 비활성화할 프로젝트를 선택하세요. 여기서 "PROCESSING" 섹션 아래 "Replays"를 선택하고 "Create Rage Click Issues"를 끄면 됩니다.

클릭이 잘못된 위치에 표시됩니다

리플레이에서 클릭이 잘못된 위치에 표시될 수 있는데, 이는 애플리케이션과 리플레이어 간 렌더링 차이 때문입니다. 흔한 사례로 텍스트 렌더링이 있습니다. 리플레이어에서 커스텀 폰트가 제대로 로드되지 않으면, 프로덕션 환경과 리플레이 간 요소 높이가 달라질 수 있습니다. 그러면 스크롤 위치가 부정확해지고, 결과적으로 마우스 클릭이 잘못된 위치에 표시됩니다. 자체 호스팅 폰트를 사용 중이라면, `sentry.io` 호스트가 폰트를 로드할 수 있도록 `Access-Control-Allow-Origin` 헤더를 설정하세요. 그렇지 않으면 CORS로 인해 리플레이어가 폰트를 로드하지 못합니다.

가변 폭 폰트에서의 텍스트 마스킹도 같은 문제를 일으킬 수 있습니다. 마스킹 텍스트("\*")의 크기가 대체된 원래 문자와 동일한 치수를 갖는다는 보장이 없기 때문입니다. 현재는 우회 방법이 없으며, 업데이트는 [이 GitHub Issue를 확인해 주세요](https://github.com/getsentry/sentry-javascript/issues/15449).

리플레이가 수신되지 않습니다

Session Replay 데이터가 전혀 수신되지 않는다면, 원인은 Content Security Policy (CSP) 제한일 가능성이 큽니다. 이는 CSP 값을 명시적으로 설정한 모든 애플리케이션에서 발생할 수 있습니다. Session Replay 통합은 리플레이 데이터를 처리하기 위해 웹 워커를 사용하며, 이를 위해 특정 CSP 권한이 필요합니다.

이 문제를 해결하려면 `Content-Security-Policy` 헤더 또는 메타 태그에 `worker-src 'self' blob:`를 포함해야 합니다. 이 지시어는 통합이 동일 출처(`'self'`)와 blob URL(`blob:`)에서 웹 워커를 생성하고 사용할 수 있게 해주며, 이는 리플레이 기능이 정상적으로 동작하는 데 필요합니다.

예를 들어, 메타 태그로 CSP를 설정하는 경우:

```html
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'; worker-src 'self' blob:; ..."
/>
```

또는 HTTP 헤더로 설정하는 경우:

```bash
Content-Security-Policy: default-src 'self'; worker-src 'self' blob:; ...
```

적절한 `worker-src` 지시어가 없으면 브라우저가 웹 워커 생성을 차단하여, 애플리케이션에서 Session Replay가 정상적으로 동작하지 않게 됩니다.

