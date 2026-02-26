---
title: '세션 이해하기 | Sentry for Next.js'
description: '대부분의 경우, Replay 샘플링 비율만 설정하면 원하는 기록 데이터를 캡처하기 시작하기에 충분합니다. 더 복잡한 경우에는 세션이 어떻게 동작하는지와 이를 수동으로 제어하는 방법을 이해하는 것이 도움이 됩니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions

# 세션 이해하기 | Sentry for Next.js

대부분의 경우, Replay 샘플링 비율만 설정하면 원하는 기록 데이터를 캡처하기 시작하기에 충분합니다. 더 복잡한 경우에는 세션이 어떻게 동작하는지와 이를 수동으로 제어하는 방법을 이해하는 것이 도움이 됩니다.

## [기본 세션 초기화](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#default-session-initialization)

SDK에서 `replayIntegration()`을 활성화하면, 샘플링 비율 설정에 따라 replay 세션이 캡처를 시작합니다:

| 구성                                | 동작                                                                                                                                                                                            |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `replaysSessionSampleRate > 0`      | [**session mode**](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#session-mode)로 시작                                                   |
| `replaysOnErrorSampleRate > 0` only | [**buffer mode**](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#buffer-mode)로 시작                                                     |
| Both rates are `0`                  | Replay는 설치되지만 [**수동으로 시작**](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#manually-starting-replay)할 때까지 비활성 상태입니다 |

**권장 기본값:**

```javascript
replaysSessionSampleRate: 0.1,  // 10% of sessions
replaysOnErrorSampleRate: 1.0,  // 100% of all errors
```

이 설정은 세션의 10%를 전체 녹화하고, 나머지 90%에서는 모든 오류를 캡처합니다. 보안 카메라에 비유하면, 일부 카메라는 항상 녹화하고 다른 카메라는 경보가 울릴 때만 영상을 저장하는 것과 같습니다.

## [세션 모드](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#session-mode)

`session` 모드에서는 Replay가 데이터를 지속적으로 기록하고 Sentry로 전송합니다. 사용자가 15분 동안 비활성 상태이거나 최대 60분이 지나면 세션이 종료되고, 위 섹션의 규칙에 따라 새 세션이 초기화됩니다.

## [버퍼 모드](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#buffer-mode)

`buffer` 모드에서는 Replay가 데이터를 계속 기록하지만 전송하지는 않습니다. 마지막 60초의 이벤트 로그를 메모리 링 버퍼(약 2-5MB)에 저장합니다.

**저장되는 항목:** Web Session Replay는 비디오 파일이 아니라 가벼운 DOM 이벤트 로그(클릭, 스크롤, 변경)를 캡처합니다. 이 로그는 Sentry 서버에서 자동으로 비디오처럼 재생 가능한 형태로 변환됩니다.

오류가 발생하면 `replaysOnErrorSampleRate`를 확인하고, 샘플링되면 오류 *이전* 60초 버퍼와 *이후*의 모든 데이터가 Sentry로 업로드되며 기록은 정상적으로 계속됩니다. 사용자가 15분 동안 비활성 상태이거나 최대 60분이 지나면 세션이 종료되고 replay가 중지됩니다.

## [Replay 통합 수동 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#manually-add-replay-integration)

Replay 통합의 초기화와 로딩을 지연시키는 것도 가능합니다. 이는 SDK 초기화와 Replay 구성을 분리할 때 유용합니다. 예를 들어, 외부 샘플링 서비스를 즉시 사용할 수 없는 경우가 있습니다.

```javascript
async function init(sessionSampleRate, errorSampleRate) {
  const client = Sentry.getClient();
  const options = client.getOptions();
  options.replaysSessionSampleRate = sessionSampleRate;
  options.replaysOnErrorSampleRate = errorSampleRate;

  const replay = Sentry.replayIntegration({
    maskAllText: true,
    // additional SDK config, see https://docs.sentry.io/platforms/javascript/session-replay/configuration/
  });

  client.addIntegration(replay);
}
```

## [Replay 수동 시작](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#manually-starting-replay)

다음과 같이 Replay 세션을 수동으로 시작할 수 있습니다:

```javascript
Sentry.init({
  dsn: "...",
  // This initializes Replay without starting any session
  replaysSessionSampleRate: 0,
  replaysOnErrorSampleRate: 0,
  integrations: [Sentry.replayIntegration()],
});

// You can access the active replay instance from anywhere in your code like this:
const replay = Sentry.getReplay();

// This starts in `session` mode, regardless of sample rates
replay.start();

// OR

// This starts in `buffer` mode, regardless of sample rates
replay.startBuffering();
```

`replaysSessionSampleRate`와 `replaysOnErrorSampleRate`가 모두 `0`이면 위와 같이 세션 replay를 수동으로 시작해야 합니다. 이전에 세션을 중지했고 새 세션을 시작하려는 경우(아래 참고)에도 유용합니다. 세션이 이미 실행 중이면 `start()`와 `startBuffering()`은 안전하며 아무 동작도 하지 않습니다. 이 경우 [디버그 메시지](https://docs.sentry.io/platforms/javascript/configuration/options.md#debug)가 기록됩니다.

## [Replay 수동 중지](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#manually-stopping-replay)

다음과 같이 실행 중인 세션을 언제든지 중지할 수 있습니다:

```javascript
await replay.stop();
```

그러면 대기 중인 기록 데이터를 모두 flush하고, replay를 중지하며, 세션을 종료합니다.

## [기록 데이터 수동 flush](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#manually-flushing-recording-data)

다음과 같이 대기 중인 기록 데이터를 flush할 수 있습니다:

```javascript
await replay.flush();
```

`session` 모드에서는 대기 중인 기록 데이터를 Sentry로 업로드합니다. `buffer` 모드에서는 대기 중인 기록 데이터를 Sentry로 업로드한 뒤 기록을 계속하며, 이는 `replaysOnErrorSampleRate`로 오류가 샘플링될 때와 동일합니다.

Session Replay가 중지된 상태에서 `flush()`를 호출하면 새 세션 기록이 시작됩니다.

## [커스텀 샘플링 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#examples-of-custom-sampling)

특정 동작이나 그룹(예: 특정 사용자 세그먼트 또는 문제가 있는 URL)을 추적하고 싶다면 커스텀 샘플링을 활성화하는 방법이 있습니다.

- [특정 사용자에 대한 Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#replays-for-specific-users)

특정 사용자 그룹에 대해 replay를 자동으로 기록하도록 설정할 수 있습니다. 아래 예시는 직원인 모든 사용자에 대해 세션 기반 replay를 기록하려는 경우입니다. `user` 객체에는 직원 여부를 나타내는 `isEmployee` 필드가 있습니다.

```javascript
const replay = Sentry.replayIntegration();

/**
 * Initialize the Sentry SDK as normal.
 *
 * `replaysSessionSampleRate` is set to its default value of "0.1" so that only ~10% of users are sampled
 * `replaysOnErrorSampleRate` is set to its default value of "1.0" to always record a replay when an error occurs
 */
Sentry.init({
  dsn: "...",
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  integrations: [replay],
});

// ...
// After a user has been authenticated, check if they're an employee
// If they are, we'll call `replay.flush()` to either flush the replay as normal if it's a session-based replay, or if it's buffering due to error sampling, the flush will send the first segment of the replay.

// Since `replaysOnErrorSampleRate` is > 0, we know that a replay has been buffered and `flush()` will flush the contents of that buffer. If only `replaysSessionSampleRate` is > 0, then there is a chance that a replay has not been recording/buffering.
// In this case, you can check that `replay.getReplayId()` returns a value, if it does, it means replay is active and you can call `replay.flush()`, other call `replay.start()` to start recording a new replay.
// ...

// Check if user is an employee, if so, always record a replay
if (loggedInUser.isEmployee) {
  // You can get a reference to the Sentry Replay integration like so:
  const replay = Sentry.getReplay();

  replay.flush();
}
```

- [특정 URL에서 Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#replays-on-specific-urls)

사용자가 지정한 URL에 진입할 때마다 replay를 기록하도록 선택할 수도 있습니다. 이는 개발자가 문제가 있는 페이지를 디버깅하는 데 도움이 됩니다. 이를 위해 [Navigation API](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API)를 사용하면 특정 URL의 탐색 이벤트를 수신하고 replay 기록을 시작할 수 있습니다.

```javascript
const replay = Sentry.replayIntegration();

/**
 * Initialize the Sentry SDK as normal.
 *
 * `replaysSessionSampleRate` and `replaysOnErrorSampleRate` are both set to
 * "0" so that we have manual control over session-based replays
 */
Sentry.init({
  dsn: "...",
  replaysSessionSampleRate: 0,
  replaysOnErrorSampleRate: 0,
  integrations: [replay],
});

// Listen to navigation events for when users land on our buggy URL, appropriately named: "/buggy-page/"
// and then start recording a replay.
navigation.addEventListener("navigate", (event) => {
  const url = new URL(event.destination.url);

  if (url.pathname.startsWith("/buggy-page/")) {
    // User navigates to the buggy page, let's start recording
    replay.start();
  }
});
```

- [오류 샘플링에서 특정 오류 무시](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#ignore-certain-errors-for-error-sampling)

`replaysOnErrorSampleRate`를 사용할 때는 Sentry에 캡처되어 전송된 모든 Error에 대해 "확률적으로 샘플링"합니다. 특정 오류에 대해서는 Replay 캡처를 건너뛰고 싶다면 `beforeErrorSampling` 콜백을 사용할 수 있습니다:

```javascript
replayIntegration({
  beforeErrorSampling: (event) => {
    // Return false to skip capturing a Replay for this error
    return !event.exception?.values?.[0]?.value?.includes("drop me");
  },
});
```

특정 오류에 대해 이 메서드가 `false`를 반환하면, 해당 오류에 대해서는 오류 샘플링 비율을 확인하지 않습니다. `true`를 반환하면 평소처럼 오류 샘플링 비율 확인을 계속합니다. 이 훅은 `buffer` 모드에서만 실행된다는 점에 유의하세요. `session` 모드는 오류와 관계없이 지속적으로 기록합니다.

- [Replay를 지원 소프트웨어와 연결](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/understanding-sessions.md#connect-replays-with-support-software)

Replay는 애플리케이션 오류에만 연결할 필요가 없으며, 지원 티켓을 보완하는 용도로도 사용할 수 있습니다. 지원 위젯이 제공하는 커스터마이징 수준에 따라 사용자가 지원 위젯을 열 때 replay를 Sentry로 전송할 수 있습니다. 참고로 Sentry의 [User Feedback](https://docs.sentry.io/product/user-feedback.md#user-feedback-widget)은 이 기능을 기본으로 제공합니다. 그런 다음 사용자가 제출한 지원 티켓과 함께 replay ID를 전송할 수 있습니다. 이 ID를 사용해 Sentry에서 replay를 참조할 수 있습니다. 또는 이메일 같은 사용자 식별자로 replay를 검색할 수도 있습니다.

아래 예시는 Replay를 지원 위젯과 연결하는 방법의 템플릿을 제공합니다.

```javascript
/**
 * Initialize the Sentry SDK as normal.
 *
 * `replaysOnErrorSampleRate` needs to be > 0 so that replays are always buffering and only sent when necessary
 */
Sentry.init({
  dsn: "...",
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 0.5,
  integrations: [Sentry.replayIntegration()],
});

/**
 * Your widget will need to have an event/hook to trigger flushing the replay to
 * Sentry.
 */
MySupportWidget.on("open", () => {
  const replay = Sentry.getReplay();
  // Send replay to Sentry
  replay.flush();
  // Retrieve the replay id that was saved and attach it to your support widget
  const replayId = replay.getReplayId();
  MySupportWidget.setTag("replayId", replayId);
});

/**
 * If your support application allows you to send custom data with the support
 * ticket, you may want to include a link to the replay URL in Sentry. That
 * way, you'll be able to open the replay directly from the ticket itself.
 * Replay URLs have the following format:
 *
 *   https://<org-slug>.sentry.io/replays/<replay-id>/
 *
 */
```

