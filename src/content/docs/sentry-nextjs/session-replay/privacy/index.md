---
title: '개인정보 보호 | Next.js용 Sentry'
description: '질문이나 피드백이 있거나 버그를 신고하고 싶다면, 관련 리플레이 링크 또는 가능하면 리플레이를 기록하려는 페이지의 공개 접근 가능한 URL과 함께 GitHub issue를 열어 주세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/privacy

# 개인정보 보호 | Next.js용 Sentry

질문이나 피드백이 있거나 버그를 신고하고 싶다면, 관련 리플레이 링크 또는 가능하면 리플레이를 기록하려는 페이지의 공개 접근 가능한 URL과 함께 [GitHub issue](https://github.com/getsentry/sentry/issues/new?assignees=\&labels=\&template=bug.yml)를 열어 주세요.

프로덕션에서 Session Replay를 활성화하기 전에, 민감한 데이터가 수집되지 않도록 마스킹 구성을 확인하세요. 기본 설정은 잠재적으로 민감한 데이터를 강하게 마스킹하지만, 이 설정을 수정하거나 UI 프레임워크 또는 시스템 SDK를 업데이트한 경우에는 애플리케이션을 반드시 충분히 테스트해야 합니다. 마스킹 이슈를 발견했거나 마스킹되어야 하지만 마스킹되지 않은 민감한 데이터가 있다면 [GitHub issue](https://github.com/getsentry/sentry-javascript/issues/new/choose)를 생성하고, 문제가 해결될 때까지 Session Replay를 활성화한 상태로 프로덕션에 배포하지 마세요.

개인 식별 정보(PII)를 처리하는 방법은 여러 가지가 있습니다. 기본적으로 Session Replay SDK는 서버로 전송되기 전에 클라이언트에서 모든 텍스트 콘텐츠를 `*`로 마스킹하고 모든 미디어 요소(`img`, `svg`, `video`, `object`, `picture`, `embed`, `map`, `audio`)를 차단합니다. 이는 `maskAllText`를 `false`로 설정해 비활성화할 수 있습니다. 또한 특정 DOM 요소에 다음 CSS 클래스를 추가해 해당 콘텐츠 기록을 방지할 수 있습니다: `sentry-block`, `sentry-ignore`, `sentry-mask`. 아래 섹션에서는 각 방법에 따라 콘텐츠가 어떻게 처리되는지 예시를 보여줍니다.

## [마스킹](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#masking)

마스킹은 텍스트 콘텐츠를 다른 값으로 대체합니다. 기본 마스킹 동작은 각 문자를 `*`로 바꾸는 것입니다. 클래스 이름이 `sentry-mask`이거나 속성이 `data-sentry-mask`인 요소는 차단됩니다. 이 예시에서 관련 HTML 코드는 `<table class="sentry-mask">...</table>`입니다.

다음 [configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration)을 통해 무엇을 마스킹/언마스킹할지 설정할 수 있습니다:

```javascript
replayIntegration({
  mask: [".mask-me"],
  unmask: [".unmask-me"],
});
```

## [차단](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#blocking)

차단은 요소를 동일한 크기의 플레이스홀더로 대체합니다. 기록에서는 콘텐츠 대신 빈 공간이 표시됩니다. 클래스 이름이 `sentry-block`이거나 속성이 `data-sentry-block`인 요소는 차단됩니다. 이 예시에서 관련 HTML 코드는 `<table data-sentry-block>...</table>`입니다.

다음 [configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration)을 통해 무엇을 차단/차단 해제할지 설정할 수 있습니다:

```javascript
replayIntegration({
  block: [".block-me"],
  unblock: [".unblock-me"],
});
```

## [무시](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#ignoring)

무시는 폼 입력에만 적용됩니다. 리플레이에 입력 내부에서 일어나는 일이 보이지 않도록, 입력 요소에서 발생한 이벤트를 무시합니다. 클래스 이름이 `sentry-ignore`이거나 속성이 `data-sentry-ignore`인 입력 요소에서 발생한 모든 이벤트는 무시됩니다. 아래 표 결과를 보면 입력 변경은 표시되지만, 텍스트는 보이지 않는 것을 확인할 수 있습니다.

다음 [configuration](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration)을 통해 무엇을 무시할지 설정할 수 있습니다:

```javascript
replayIntegration({
  ignore: [".ignore-me"],
});
```

## [개인정보 보호 구성](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#privacy-configuration)

개인 식별 정보나 기타 비공개 데이터가 없는 정적 웹사이트를 운영한다면, `maskAllText`와 `blockAllMedia` 구성 옵션을 각각 설정하여 기본 텍스트 마스킹 및 이미지 차단을 비활성화할 수 있습니다:

```javascript
Sentry.replayIntegration({
  // NOTE: This will disable built-in masking. Only use this if your site has no sensitive data, or if you've already set up other options for masking or blocking relevant data, such as 'ignore', 'block', 'mask' and 'maskFn'.
  maskAllText: false,
  blockAllMedia: false,
});
```

v8부터 `unblock`와 `unmask` 옵션은 더 이상 기본 DOM selector를 추가하지 않습니다. 이전 버전의 기본 동작을 유지하려면 구성에서 이를 명시적으로 지정해야 합니다:

```javascript
Sentry.replayIntegration({
  unblock: [".sentry-unblock, [data-sentry-unblock]"],
  unmask: [".sentry-unmask, [data-sentry-unmask]"],
});
```

다음은 `replayIntegration({})`에서 사용할 수 있는 옵션 전체 목록입니다:

| key           | type                       | default                                      | description                                                                                                                                                                                                                                          |
| ------------- | -------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mask          | `string[]`                 | `['.sentry-mask', '[data-sentry-mask]']`     | 지정된 DOM selector와 일치하는 모든 요소를 마스킹합니다. 예시는 [마스킹](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#masking) 섹션을 참고하세요. 설정한 selector는 기본값에 *추가*로 적용됩니다. |
| maskAllText   | `boolean`                  | `true`                                       | *모든* 텍스트 콘텐츠를 마스킹합니다. 서버로 보내기 전에 텍스트 콘텐츠를 `maskFn`에 전달합니다.                                                                                                                                                           |
| maskAllInputs | `boolean`                  | `true`                                       | `<input>` 요소의 값을 마스킹합니다. 서버로 보내기 전에 입력 값을 `maskFn`에 전달합니다.                                                                                                                                                    |
| block         | `string[]`                 | `['.sentry-block', '[data-sentry-block]']`   | DOM selector와 일치하는 모든 요소를 가립니다(redact). 예시는 [차단](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#blocking) 섹션을 참고하세요. 설정한 selector는 기본값에 *추가*로 적용됩니다. |
| blockAllMedia | `boolean`                  | `true`                                       | *모든* 미디어 요소(`img`, `svg`, `video`, `object`, `picture`, `embed`, `map`, `audio`)를 차단합니다.                                                                                                                                                    |
| ignore        | `string[]`                 | `['.sentry-ignore', '[data-sentry-ignore]']` | 일치하는 입력 필드에서 발생하는 모든 이벤트를 무시합니다. 예시는 위의 [무시](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#ignoring) 섹션을 참고하세요.                                                                                |
| maskFn        | `(text: string) => string` | `(s) => '*'.repeat(s.length)`                | 서버로 전송하기 전에 텍스트 콘텐츠를 어떻게 마스킹할지 사용자 지정하는 함수입니다. 기본값은 `*`로 마스킹합니다.                                                                                                                                          |
| unblock       | `string[]`                 | `[]`                                         | DOM selector와 일치하는 요소를 가리지 않습니다. `blockAllMedia`로 차단된 특정 미디어 요소의 차단을 해제하는 데 사용됩니다. `password` 같은 민감한 요소에는 영향을 주지 않습니다.                                                    |
| unmask        | `string[]`                 | `[]`                                         | 지정된 DOM selector와 일치하는 모든 요소의 마스킹을 해제합니다. `maskAllText`로 마스킹된 특정 요소의 마스킹 해제에 사용됩니다.                                                                                                                         |

## [네트워크 요청/응답 본문 및 헤더](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#network-request-and-response-bodies-and-headers)

요청 및 응답 본문 수집은 옵트인 기능입니다. PII가 Sentry로 들어가는 것을 피하는 가장 좋은 방법은 PII를 포함할 수 있는 endpoint URL을 추가하지 않는 것이기 때문입니다. 또한, 실수로 이런 데이터가 포함된 URL을 옵트인한 경우를 대비해 Sentry는 요청/응답 본문에서 특정 유형의 민감한 데이터를 [scrub](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md)하려고 시도합니다. 이 메커니즘은 데이터가 디스크에 기록되기 전에 수집 서비스에서 수행됩니다. 이는 신용카드 정보, 사회보장번호, [passwords](https://github.com/search?q=repo%3Agetsentry%2Frelay%20PASSWORD_KEY_REGEX\&type=code) 같은 항목을 패턴 매칭하는 최선의 노력 방식입니다.

이 기능에 대한 자세한 내용은 [configuration page](https://docs.sentry.io/platforms/javascript/session-replay/configuration.md#network-details)에서 확인할 수 있습니다.

## [커스텀 스크러빙](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#custom-scrubbing)

`beforeAddRecordingEvent`는 SDK 버전 7.53.0부터 추가되었습니다. 이를 사용하면 기록 이벤트가 브라우저를 떠나기 전에 수정하거나, PII 제거를 위해 scrub 하거나, 무시할 수 있습니다. 이러한 이벤트에는 console logs, network requests, response data가 포함됩니다.

```javascript
Sentry.replayIntegration({
  beforeAddRecordingEvent: (event) => {
    // Filter out specific events
    if (event.data.tag === "foo") {
      return null;
    }

    // Remember to return an event if you want to keep it!
    return event;
  },
});
```

- [예시: 500 상태 코드만 수집](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#example-capturing-500-status-codes-only)

다음은 500 상태 코드를 반환하는 fetch 요청만 수집하는 예시입니다. (fetch가 아닌 요청은 기존처럼 계속 수집됩니다.)

```javascript
Sentry.replayIntegration({
  beforeAddRecordingEvent: (event) => {
    // Do not capture fetch/xhr requests, unless the response code is 500
    if (
      event.data.tag === "performanceSpan" &&
      (event.data.payload.op === "resource.fetch" ||
        event.data.payload.op === "resource.xhr") &&
      event.data.payload.data.statusCode !== 500
    ) {
      return null;
    }

    return event;
  },
});
```

이 데이터에 대해서는 [server-side PII scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md)도 제공합니다. 미국 사회보장번호, 신용카드, 개인 키와 같은 특정 패턴을 탐지합니다.

- [예시: URL 스크러빙](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#example-scrubbing-urls)

기본적으로 URL은 recording event와 replay event 모두에 저장됩니다.

recording event에서 URL을 스크럽하려면 위의 `beforeAddRecordingEvent`를 사용하세요.

replay event에서 URL을 스크럽하려면 `addEventProcessor`를 사용하세요:

```javascript
Sentry.addEventProcessor((event) => {
  // Ensure that we specifically look at replay events
  if (event.type !== "replay_event") {
    // Return the event, otherwise the event will be dropped
    return event;
  }

  // Your URL scrubbing function
  function urlScrubber(url) {
    return url.replace(/([a-z0-9]{3}\.[a-z]{5}\.[a-z]{7})/, "[Filtered]");
  }

  // Scrub all URLs with your scrubbing function
  event.urls = event.urls && event.urls.map(urlScrubber);

  return event;
});
```

- [지원 중단된 옵션](https://docs.sentry.io/platforms/javascript/session-replay/privacy.md#deprecated-options)

버전 7.35.0 이전의 privacy API는 지원 중단(deprecated)되었으며 위 옵션으로 대체되었습니다. 자세한 내용은 [Replay migration guide](https://github.com/getsentry/sentry-javascript/blob/master/packages/replay/MIGRATION.md#upgrading-replay-from-7340-to-7350---6645)를 참고하세요.

