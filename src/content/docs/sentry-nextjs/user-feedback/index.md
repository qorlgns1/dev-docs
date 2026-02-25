---
title: '사용자 피드백 설정 | Sentry for Next.js'
description: 'User Feedback 기능을 사용하면 먼저 오류 이벤트가 발생하지 않아도, 애플리케이션 내부 어디에서나 언제든 사용자 피드백을 수집할 수 있습니다. 반면 Crash-Report Modal 기능은 오류 이벤트가 발생했을 때 사용자 피드백을 요청할 수 있게 해줍니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback

# 사용자 피드백 설정 | Sentry for Next.js

User Feedback 기능을 사용하면 먼저 오류 이벤트가 발생하지 않아도, 애플리케이션 내부 어디에서나 언제든 사용자 피드백을 수집할 수 있습니다. 반면 [Crash-Report Modal](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#crash-report-modal) 기능은 오류 이벤트가 발생했을 때 사용자 피드백을 요청할 수 있게 해줍니다.

셀프 호스팅 Sentry 인스턴스를 사용하는 경우, User Feedback 기능의 전체 기능을 사용하려면 버전 24.4.2 이상이어야 합니다. 더 낮은 버전에서는 기능이 제한될 수 있습니다.

## [User Feedback 위젯](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#user-feedback-widget)

임베드 가능한 JavaScript 위젯을 사용하면 애플리케이션 내부 어디에서나 사용자가 피드백을 제출할 수 있습니다. [Crash-Report Modal](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#crash-report-modal)은 오류 이벤트에 연결된 반응형 피드백을 수집합니다.

- [사전 요구 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#pre-requisites)

User Feedback 통합이 동작하려면 [Sentry browser SDK package](https://www.npmjs.com/package/@sentry/browser) 또는 동등한 프레임워크 SDK(예: [@sentry/react](https://www.npmjs.com/package/@sentry/react))가 설치되어 있어야 합니다. SDK의 최소 요구 버전은 [7.85.0](https://github.com/getsentry/sentry-javascript/releases/tag/7.85.0)입니다. 이전 SDK 버전을 사용 중이라면 이 [마이그레이션 문서](https://github.com/getsentry/sentry-javascript/blob/master/MIGRATION.md)를 확인하세요.

User Feedback는 [Shadow DOM](https://caniuse.com/shadowdomv1) 및 [Dialog element](https://caniuse.com/mdn-html_elements_dialog)를 지원하는 브라우저가 필요합니다.

- [설치](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#installation)

User Feedback 통합은 Sentry SDK에 이미 포함되어 있습니다. 설치 마법사를 통해 SDK를 설치하는 것을 권장합니다:

```bash
npx @sentry/wizard@latest -i nextjs
```

- [설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#set-up)

통합을 설정하려면 Sentry 초기화 코드에 다음을 추가하세요. 통합 생성자에는 전달할 수 있는 옵션이 많습니다. 자세한 내용은 [설정 문서](https://docs.sentry.io/platforms/javascript/user-feedback/configuration.md)를 참고하세요.

클라이언트 사이드 NextJS 앱에 다음을 추가하세요:

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.feedbackIntegration({
      // Additional SDK configuration goes in here, for example:
      colorScheme: "system",
    }),
  ],
});
```

기본적으로 위젯은 웹사이트의 오른쪽 하단에 삽입됩니다. 자체 UI로 완전히 교체하는 것을 포함해 위젯의 거의 모든 측면을 자유롭게 사용자 지정할 수 있습니다.

SDK 버전 8.0.0 이상에서는 사용자가 피드백과 함께 스크린샷을 보낼 수 있습니다. 셀프 호스팅의 경우에도 릴리스 24.4.2 이상이 필요합니다. 이는 `enableScreenshot` 옵션으로 구성할 수 있으며, 기본값은 `true`입니다. 모바일 기기에서는 스크린샷이 지원되지 않으므로 이 경우 스크린샷 버튼이 자동으로 숨겨집니다.

스크린샷은 [attachments quota](https://docs.sentry.io/pricing/quotas/manage-attachments-quota.md)를 사용합니다. 모든 플랜에는 1GB의 첨부 파일 용량이 제공되며, 이는 대략 스크린샷 2500장에 해당합니다.

- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#session-replay)

User Feedback 위젯은 [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md)와 쉽게 통합됩니다. 먼저 Session Replay 통합이 올바르게 설정되어 있고 `replaysOnErrorSampleRate`가 0보다 큰지 확인하세요. 이 설정이 완료되면 Replay SDK는 사용자가 User Feedback 위젯을 *열기* 전까지 최대 30초의 사용자 세션을 버퍼링합니다. 사용자가 피드백을 제출하면 sentry.io에서 피드백(리플레이 포함)을 확인할 수 있습니다.

## [User Feedback API](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#user-feedback-api)

user feedback API를 사용하면 자체 UI를 활용하면서 사용자 피드백을 수집할 수 있습니다. 앱에서 사용하는 동일한 프로그래밍 언어로 사용자 피드백을 전송할 수 있습니다. 이 경우 SDK가 HTTP 요청을 생성하므로 HTTP로 데이터를 게시하는 처리를 직접 할 필요가 없습니다.

선택적으로 `associatedEventId`를 전달해 사용자 피드백을 오류 이벤트와 연결할 수 있으며, 이를 통해 이슈에 대한 추가 인사이트를 얻을 수 있습니다. 이벤트 ID를 얻는 방법은 2가지입니다:

1. 이벤트를 캡처하는 메서드의 반환값을 사용합니다.
2. [`beforeSend`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#before-send)
   <!-- -->
   및 `Sentry.lastEventId()`를 사용합니다.

```javascript
// All feedback fields are optional, except `message`.
const userFeedback = {
  name: "John Doe",
  email: "john@doe.com",
  message: "I really like your App, thanks!",
};
Sentry.captureFeedback(userFeedback);
```

두 번째 인수로 hint를 전달하여 피드백 이벤트에 추가 데이터를 첨부할 수도 있습니다. 이는 다른 `capture` 메서드와 유사합니다:

```javascript
const base64ScreenShot = "data:image/jpeg;base64...";
const res = await fetch(base64ScreenShot);
const buffer = await res.arrayBuffer();

Sentry.captureFeedback(
  { message: "I really like your App, thanks!" },
  {
    captureContext: {
      tags: { key: "value" },
    },
    attachments: [
      {
        filename: "screenshot.png",
        data: new Uint8Array(buffer),
      },
    ],
  },
);
```

## [Crash-Report Modal](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#crash-report-modal)

임베드 가능한 JavaScript 기반 Crash-Report modal은 웹사이트에서 일반 오류 페이지(고전적인 `500.html`)를 렌더링하는 경우에 유용합니다.

피드백을 수집하기 위해 Crash-Report modal은 사용자 이름, 이메일 주소, 그리고 발생한 상황에 대한 설명을 요청하고 수집합니다. 피드백이 제공되면 Sentry는 해당 피드백을 원본 이벤트와 연결하여 이슈에 대한 추가 인사이트를 제공합니다.

아래 스크린샷은 Crash-Report modal의 예시를 보여주며, 사용자 지정 내용에 따라 실제 화면은 다를 수 있습니다:

- [통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback.md#integration)

modal은 공개 DSN으로 인증한 다음, 백엔드에서 생성된 Event ID를 전달받습니다.

[React](https://docs.sentry.io/platforms/javascript/guides/react.md) 또는 [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md) 같은 프레임워크를 사용한다면, 사용자 피드백을 수집하기 가장 좋은 위치는 오류 처리 컴포넌트 내부입니다. (예시는 플랫폼별 문서를 참고하세요.) 프레임워크를 사용하지 않는다면 `beforeSend`를 사용해 이벤트가 전송되기 직전에 피드백을 수집할 수 있습니다:

```html
<script>
  Sentry.init({
    dsn: "___PUBLIC_DSN___",
    beforeSend(event, hint) {
      // Check if it is an exception, and if so, show the report dialog
      if (event.exception && event.event_id) {
        Sentry.showReportDialog({ eventId: event.event_id });
      }
      return event;
    },
  });
</script>
```

## 이 섹션의 페이지

- [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md)
- [Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x.md)

