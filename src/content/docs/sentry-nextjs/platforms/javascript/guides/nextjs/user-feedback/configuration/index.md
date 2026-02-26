---
title: '설정 | Next.js용 Sentry'
description: '사용자 피드백 위젯은 다양한 사용자 지정 옵션을 제공하며, 제공되는 옵션이 충분하지 않다면 자체 UI를 사용할 수 있습니다.'
---

소스 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration

# 설정 | Next.js용 Sentry

## [사용자 피드백 위젯](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#user-feedback-widget)

사용자 피드백 위젯은 다양한 사용자 지정 옵션을 제공하며, 제공되는 옵션이 충분하지 않다면 [자체 UI를 사용할 수 있습니다](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#bring-your-own-widget).

다음 설정 옵션은 JavaScript SDK 8.0.0 이상 버전에 적용됩니다. SDK 버전 7의 피드백 위젯은 베타 릴리스였으며 현재는 더 이상 사용되지 않습니다.

- [일반](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#general)

다음 옵션은 `feedbackIntegration({})`의 통합 설정에서 구성할 수 있습니다:

| Key            | Type                                                                                   | Default           | Description                                                                                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `autoInject`   | `boolean`                                                                              | `true`            | 통합이 추가될 때 피드백 위젯을 애플리케이션에 주입합니다. `feedback.attachTo()` 또는 `feedback.createWidget()`을 직접 호출하려는 경우, 또는 특정 뷰에서만 위젯을 표시하려는 경우 `autoInject: false`로 설정하세요. |
| `showBranding` | `boolean`                                                                              | `true`            | 폼 내부에 Sentry 로고를 표시합니다.                                                                                                                                                                                               |
| `colorScheme`  | `"system" \| "light" \| "dark"`                                                        | `"system"`        | 색상 테마 선택을 표시합니다. `"system"`은 OS 색상 구성표를 사용합니다.                                                                                                                                                                   |
| `id`           | `string`                                                                               | `sentry-feedback` | 피드백 위젯을 포함하는 `<div>`의 `id` 속성입니다. 자세한 내용은 [CSS 사용자 지정](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#css-customization)을 참조하세요.                         |
| `tags`         | `Record<string, number \| string \| boolean \| bigint \| symbol \| null \| undefined>` | `{}`              | 피드백 이벤트에 설정할 [태그](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/tags.md)입니다.                                                                                                                   |

- [자동 주입 vs. 수동 주입](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#auto-inject-vs-manual-injection)

자동 주입을 사용할지, 수동으로 제어할지는 별개로, 먼저 `integrations` 배열을 통해 통합을 `Sentry.init()`에 전달해야 합니다.

`autoInject: true`인 경우 사용자가 피드백을 입력할 수 있도록 폼 팝업을 트리거하는 버튼이 페이지에 삽입됩니다. 반대로 이 주입 시점을 직접 제어하려면 `feedback.createWidget()` 메서드를 호출해 `Actor` 객체 참조를 얻은 뒤, `appendToDom()`을 호출해 페이지에 삽입하세요.

```jsx
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.feedbackIntegration({
      // Disable the injection of the default widget
      autoInject: false,
    }),
  ],
});

function ToggleFeedbackButton() {
  const [feedback, setFeedback] = useState();
  // Read `getFeedback` on the client only, to avoid hydration errors during server rendering
  useEffect(() => {
    setFeedback(Sentry.getFeedback());
  }, []);

  const [widget, setWidget] = useState();
  return (
    <button
      type="button"
      onClick={async () => {
        if (widget) {
          widget.removeFromDom();
          setWidget(null);
        } else {
          setWidget(feedback?.createWidget());
        }
      }}
    >
      {widget ? "Remove Widget" : "Create Widget"}
    </button>
  );
}
```

아래에서 [자체 UI 사용 방법](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#bring-your-own-button)에 대해 더 알아보세요.

- [사용자 및 폼](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#user-and-form)

다음 옵션은 `feedbackIntegration({})`의 통합 설정에서 구성할 수 있습니다:

| Key                | Type                     | Default                               | Description                                                                                                            |
| ------------------ | ------------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `showName`         | `boolean`                | `true`                                | 피드백 폼에 이름 필드를 표시합니다.                                                                          |
| `showEmail`        | `boolean`                | `true`                                | 피드백 폼에 이메일 필드를 표시합니다.                                                                         |
| `enableScreenshot` | `boolean`                | `true`                                | 사용자가 피드백과 함께 스크린샷 첨부 파일을 전송할 수 있게 합니다. self-hosted 환경에서는 릴리스 24.4.2도 필요합니다. |
| `isNameRequired`   | `boolean`                | `false`                               | 피드백 폼의 이름 필드를 필수 입력으로 설정합니다.                                                          |
| `isEmailRequired`  | `boolean`                | `false`                               | 피드백 폼의 이메일 필드를 필수 입력으로 설정합니다.                                                         |
| `useSentryUser`    | `Record<string, string>` | `{ email: 'email', name: 'username'}` | `Sentry.setUser`로 설정한 Sentry SDK 사용자 필드에 맞춰 `email` 및 `name` 필드를 설정합니다. |

#
- [사용자 컨텍스트](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#user-context)

[`Sentry.setUser()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/identify-user.md)를 호출해 사용자 컨텍스트를 설정했다면, 해당 값이 `name` 및 `email` 필드의 기본값으로 사용됩니다. 이 필드들이 사용자에게 숨겨져 있어도 기본값은 피드백 메시지와 함께 전송됩니다.

아래는 기본값이 아닌 사용자 필드를 사용하는 설정 예시입니다.

```javascript
Sentry.setUser({
  fullName: "Jane Doe",
  email: "foo@example.com",
});

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.feedbackIntegration({
      useSentryUser: {
        name: "fullName",
        email: "email",
      },
    }),
  ],
});
```

- [텍스트 사용자 지정](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#text-customization)

기본 피드백 위젯에서 보이는 대부분의 텍스트는 사용자 지정할 수 있습니다.

다음 옵션은 `feedbackIntegration({})`의 통합 설정에서 구성할 수 있습니다:

| Key                           | Default                                  | Description                                                                                                               |
| ----------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `triggerLabel`                | `"Report a Bug"`                         | 클릭 시 피드백 폼을 여는 주입된 버튼의 레이블입니다.                                            |
| `triggerAriaLabel`            | `triggerLabel` \|\| `"Report a Bug"`     | 클릭 시 피드백 폼을 여는 주입된 버튼의 aria 레이블입니다. SDK v8.20.0부터 사용할 수 있습니다.    |
| `formTitle`                   | `"Report a Bug"`                         | 피드백 폼 상단의 제목입니다.                                                                                |
| `submitButtonLabel`           | `"Send Bug Report"`                      | 피드백 폼에서 사용하는 제출 버튼의 레이블입니다.                                                                 |
| `cancelButtonLabel`           | `"Cancel"`                               | 피드백 폼에서 사용하는 취소 버튼의 레이블입니다.                                                                    |
| `confirmButtonLabel`          | `"Confirm"`                              | 피드백 폼에서 사용하는 확인 버튼의 레이블입니다.                                                                   |
| `addScreenshotButtonLabel`    | `"Add a screenshot"`                     | 폼에 스크린샷을 추가하는 버튼의 레이블입니다.                                                                  |
| `removeScreenshotButtonLabel` | `"Remove screenshot"`                    | 폼에서 스크린샷을 제거하는 버튼의 레이블입니다.                                                           |
| `nameLabel`                   | `"Name"`                                 | 이름 입력 필드의 레이블입니다.                                                                                        |
| `namePlaceholder`             | `"Your Name"`                            | 이름 입력 필드의 플레이스홀더입니다.                                                                                 |
| `emailLabel`                  | `"Email"`                                | 이메일 입력 필드의 레이블입니다.                                                                                       |
| `emailPlaceholder`            | `"your.email@example.org"`               | 이메일 입력 필드의 플레이스홀더입니다.                                                                                |
| `isRequiredLabel`             | `"(required)"`                           | 필수 입력 필드 옆에 표시되는 레이블입니다.                                                                  |
| `messageLabel`                | `"Description"`                          | 피드백 설명 입력 필드의 레이블입니다.                                                                       |
| `messagePlaceholder`          | `"What's the bug? What did you expect?"` | 피드백 설명 입력 필드의 플레이스홀더입니다.                                                                 |
| `successMessageText`          | `"Thank you for your report!"`           | 피드백 제출이 성공한 뒤 표시되는 메시지입니다.                                                             |
| `highlightToolText`           | `"Highlight"`                            | 스크린샷의 일부 영역을 강조하는 버튼의 레이블입니다. SDK v10.10.0부터 사용할 수 있습니다.                  |
| `hideToolText`                | `"Hide"`                                 | 스크린샷의 일부 영역을 숨기는 버튼의 레이블입니다. SDK v10.10.0부터 사용할 수 있습니다.                       |
| `removeHighlightText`         | `"Remove"`                               | 스크린샷에서 강조/숨김 처리된 영역을 제거하는 버튼의 레이블입니다. SDK v10.10.0부터 사용할 수 있습니다. |

사용자 지정 예시:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.feedbackIntegration({
      buttonLabel: "Feedback",
      submitButtonLabel: "Send Feedback",
      formTitle: "Send Feedback",
    }),
  ],
});
```

- [CSS 사용자 지정](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#css-customization)

페이지에서 피드백 컴포넌트의 배치뿐 아니라, 라이트/다크 모드용 글꼴과 테마 색상도 사용자 지정할 수 있습니다.

모든 경우에 CSS 변수를 설정해 원하는 값을 재정의할 수 있습니다. 기본적으로 `<div>` 컨테이너에는 `id="sentry-feedback"` 속성이 있으므로, `#sentry-feedback` 선택자를 사용해 CSS 변수를 정의하고 기본값을 재정의할 수 있습니다.

아래 예시는 CSS 변수를 재정의하여 라이트/다크 테마의 배경색을 사용자 지정하는 방법을 보여줍니다:

```css
#sentry-feedback {
  --trigger-background: #cccccc;
}
@media (prefers-color-scheme: dark) {
  #sentry-feedback {
    --trigger-background: #222222;
  }
}
```

또는 JavaScript에서 theme 값을 설정해 동일한 작업을 할 수도 있습니다:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.feedbackIntegration({
      themeLight: {
        background: "#cccccc",
      },
      themeDark: {
        background: "#222222",
      },
    }),
  ],
});
```

다음 값들은 CSS 변수로만 사용할 수 있으며, 다크 및 라이트 테마 모두에 적용됩니다.

| CSS Variable    | Default                                            | 설명                                                                                                                                                                  |
| --------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--font-family` | `"system-ui, 'Helvetica Neue', Arial, sans-serif"` | 사용할 기본 font-family입니다.                                                                                                                                         |
| `--font-size`   | `14px`                                             | 폰트 크기입니다.                                                                                                                                                       |
| `--z-index`     | `100000`                                           | 위젯의 z-index입니다.                                                                                                                                                  |
| `--inset`       | `auto 0 0 auto`                                    | 기본적으로 위젯은 고정 위치이며 오른쪽 하단에 배치됩니다.                                                                                                              |
| `--page-margin` | `16px`                                             | 위젯이 배치될 화면 가장자리로부터의 여백입니다. `10px 20px 30px 10px`처럼 top/right/bottom/left 여백에 대한 shorthand 값도 허용됩니다. |

기본값을 덮어쓰는 CSS 변수를 정의하거나, `feedbackIntegration({})`에 `themeLight` 및/또는 `themeDark`를 전달하여 색상을 커스터마이즈할 수 있습니다.

| CSS Variable          | Configuration Key  | Default Light Mode                        | Default Dark Mode                         | 설명                                                                                                      |
| --------------------- | ------------------ | ----------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `--foreground`        | `foreground`       | `#2b2233`                                 | `#ebe6ef`                                 | 전경(텍스트) 색상입니다.                                                                                  |
| `--background`        | `background`       | `#ffffff`                                 | `#29232f`                                 | 위젯(삽입된 버튼 및 폼)의 배경 색상입니다.                                                                |
| `--accent-foreground` | `accentForeground` | `#ffffff`                                 | `#ffffff`                                 | 제출 버튼의 전경 색상입니다.                                                                              |
| `--accent-background` | `accentBackground` | `rgba(88, 74, 192, 1)`                    | `rgba(88, 74, 192, 1)`                    | 제출 버튼의 배경 색상입니다.                                                                              |
| `--success-color`     | `successColor`     | `#268d75`                                 | `#2da98c`                                 | 성공 관련 컴포넌트에 사용되는 색상입니다(예: 피드백이 성공적으로 제출되었을 때의 텍스트 색상).          |
| `--error-color`       | `errorColor`       | `#df3338`                                 | `#f55459`                                 | 오류 관련 컴포넌트에 사용되는 색상입니다(예: 피드백 제출 중 오류가 발생했을 때의 텍스트 색상).          |
| `--box-shadow`        | `boxShadow`        | `0px 4px 24px 0px rgba(43, 34, 51, 0.12)` | `0px 4px 24px 0px rgba(43, 34, 51, 0.12)` | 위젯(삽입된 버튼 및 폼)에 사용되는 box shadow 스타일입니다.                                               |
| `--outline`           | `outline`          | `1px auto var(--accent-background)`       | `1px auto var(--accent-background)`       | 포커스 상태일 때 폼 입력 요소의 아웃라인입니다.                                                           |

#
- [테마 우선순위](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#theme-priority)

CSS 변수는 `feedbackIntegration()`의 설정 값보다 우선합니다. 이 예시에서는 설정상 텍스트가 `white` 또는 `black`일 수 있어 보이지만, CSS 변수가 설정되어 있기 때문에 텍스트는 항상 `red`가 됩니다.

```html
<script>
  Sentry.init({
    dsn: "___PUBLIC_DSN___",
    integrations: [
      Sentry.feedbackIntegration({
        themeLight: {
          foreground: "#000",
        },
        themeDark: {
          foreground: "#fff",
        },
      }),
    ],
  });
</script>

<style>
  #sentry-feedback {
    --foreground: "red"; /* overrides both `#fff` and `#000` above */
  }
</style>
```

#
- [커스텀 ID selector](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#custom-id-selector)

`id` 설정 값을 기본값 `sentry-feedback`이 아닌 다른 값으로 설정하고, CSS 변수를 덮어쓸 때 selector로 사용할 수 있습니다.

```html
<script>
  Sentry.init({
    dsn: "___PUBLIC_DSN___",
    integrations: [
      Sentry.feedbackIntegration({
        id: "feedback-theme", // The default is 'sentry-feedback'
      }),
    ],
  });
</script>

<style>
  /* Target the custom id */
  #feedback-theme {
    --foreground: "red";
  }
</style>
```

- [이벤트 콜백](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#event-callbacks)

사용자가 피드백 폼과 상호작용을 시작한 시점을 아는 것이 유용한 경우가 있어, 커스텀 로깅을 추가하거나 사용자가 완료했는지 알려주는 백그라운드 타이머를 페이지에서 시작 및 중지할 수 있도록 했습니다.

다음 옵션들은 `feedbackIntegration({})`에서 integration에 대해 설정할 수 있습니다:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.feedbackIntegration({
      onFormOpen: () => {},
      onFormClose: () => {},
      onSubmitSuccess: (data: FeedbackFormData, eventID: string) => {},
      onSubmitError: (error: Error) => {},
    }),
  ],
});
```

`onSubmitSuccess` 콜백을 구현하면 저장된 피드백 항목으로 직접 연결할 수 있습니다. 구성해야 하는 URL은 `https://${orgSlug}.sentry.io/issues/feedback/?projectSlug=${projectSlug}&eventId=${eventId}`입니다.

*참고:* SDK v9 이하에서는 `onSubmitSuccess`의 시그니처가 `(data: FeedbackFormData) => {}`였습니다.

- [사용자 정의 버튼 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#bring-your-own-button)

`feedback.attachTo()`를 호출해 SDK가 버튼에 click listener를 연결하도록 하면, 기본 삽입 버튼 대신 직접 만든 버튼으로 폼 표시를 트리거할 수 있습니다. 생성자가 받는 것과 동일한 커스터마이즈 옵션(예: 텍스트 레이블, 색상)도 제공할 수 있습니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.feedbackIntegration({
      // Disable the injection of the default widget
      autoInject: false,
    }),
  ],
});

// Get the instance returned by `feedbackIntegration()`
const feedback = Sentry.getFeedback();

feedback?.attachTo(document.querySelector("#your-button"), {
  formTitle: "Report a Bug!",
});
```

또는 `feedback.createForm()`을 호출하여 폼이 로드되고, dom에 추가되고, 최종적으로 사용자에게 표시되는 시점을 완전히 제어할 수 있습니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.feedbackIntegration({
      // Disable the injection of the default widget
      autoInject: false,
    }),
  ],
});

// Get the instance returned by `feedbackIntegration()`
const feedback = Sentry.getFeedback();

const form = await feedback?.createForm();
form.appendToDom();
form.open();
```

- [사용자 정의 위젯 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#bring-your-own-widget)

직접 만든 UI 컴포넌트로 피드백을 수집하고, 피드백 데이터 객체를 `captureFeedback()` 함수에 전달할 수도 있습니다. `captureFeedback` 함수는 두 개의 매개변수를 받습니다:

* 필수 `message` 속성과 선택적 `name`, `email` 속성을 포함하는 JavaScript 객체
* 선택적 "hints" 객체

```javascript
Sentry.captureFeedback(
  {
    name: "Jane Doe", // optional
    email: "email@example.org", // optional
    message: "This is an example feedback", // required
  },
  {
    includeReplay: true, // optional
    attachments: [], // optional
  },
);
```

다음은 간단한 예시입니다:

```html
<form id="my-feedback-form">
  <input name="name" placeholder="Your Name" />
  <input name="email" placeholder="Your Email" />
  <textarea name="message" placeholder="What's the issue?" />
  <input type="file" name="attachment" />
  <button type="submit">Submit</button>
</form>
```

- [로딩 전략](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#loading-strategies)

`feedbackIntegration`은 사용자 대면 integration이므로, 번들 크기에 영향을 주는 두 가지 로딩 전략을 제공합니다.

대부분의 사용자에게는 `Sentry.init` 호출에서 `feedbackIntegration`을 사용하는 것을 권장합니다. 이렇게 하면 환경에 맞는 적절한 기본값으로 사용자 피드백이 설정됩니다.

이 페이지의 모든 코드 예시는 기본적으로 `feedbackIntegration`을 사용합니다. 이는 CDN 또는 NPM 설치 방식을 선택했는지와 관계없이 사용할 수 있기 때문입니다. 다만 설치 방식에 따라 `feedbackIntegration`의 구현은 다릅니다. NPM 사용자의 경우 `feedbackIntegration`은 `feedbackSyncIntegration`의 alias입니다. CDN 사용자의 경우 `feedbackIntegration`은 `feedbackAsyncIntegration`의 alias입니다.

#
- [`feedbackSyncIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#feedbacksyncintegration)

SDK를 NPM으로 설치했다면 이 로딩 전략이 기본으로 사용됩니다. CDN을 통해 SDK를 설치한 경우에는 이 전략을 사용할 수 없습니다.

이 integration에는 "Send Feedback" 버튼을 렌더링하는 데 필요한 모든 코드와, 버튼 클릭 시 트리거되는 폼 코드가 포함됩니다. 이 로딩 전략을 선택하면 애플리케이션에서 가장 큰 초기 번들 크기를 감수해야 합니다. 장점은 사용자가 위젯과 상호작용할 때 피드백 위젯이 확실히 열린다는 점이며, 어느 경우든 피드백 메시지를 전송하려면 네트워크 연결이 필요합니다.

#
- [`feedbackAsyncIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#feedbackasyncintegration)

SDK를 CDN으로 설치했다면 이 로딩 전략이 기본으로 사용됩니다. NPM을 사용한 경우에도 `Sentry.init` 호출에 이 integration을 추가해 이 로딩 전략을 선택할 수 있습니다.

이 integration에는 페이지 로드 시 화면에 "Send Feedback" 버튼을 표시하기 위해 필요한 최소한의 코드만 처음에 포함됩니다. 사용자가 해당 버튼을 클릭하면 integration이 `https://browser.sentry-cdn.com`에서 내부 integration을 비동기로 로드해 폼을 표시하고 사용자가 피드백 메시지를 입력할 수 있게 합니다. 장점은 번들 크기가 가장 작다는 점입니다. 단점은 예를 들어 사용자가 ad-blocker를 사용하는 경우 비동기 로딩이 실패할 수 있다는 점입니다.

#
- [CDN으로 설치한 경우](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#when-installed-via-cdn)

CDN 사용자의 경우 `feedbackIntegration`은 `feedbackAsyncIntegration`의 alias입니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Use the default strategy, an alias for `feedbackAsyncIntegration`
    Sentry.feedbackIntegration({
      // Additional SDK configuration goes in here, for example:
      colorScheme: "system",
    }),
  ],
});
```

#
- [NPM으로 설치한 경우](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#when-installed-via-npm)

NPM 사용자의 경우 `feedbackIntegration`은 `feedbackSyncIntegration`의 alias입니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // Use the default strategy, an alias for `feedbackSyncIntegration`
    Sentry.feedbackIntegration({
      // Additional SDK configuration goes in here, for example:
      colorScheme: "system",
    }),
  ],
});
```

## [Crash-Report Modal](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration.md#crash-report-modal)

조직의 요구사항에 맞게 Crash-Report modal을 커스터마이즈할 수 있습니다(예: 현지화 목적). 모든 옵션은 `Sentry.showReportDialog` 호출을 통해 전달할 수 있습니다.

| Param            | Default                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| `eventId`        | 이벤트의 id를 수동으로 설정합니다.                                                                   |
| `dsn`            | 리포트 대상 dsn을 수동으로 설정합니다.                                                                |
| `user`           | 사용자 데이터를 수동으로 설정합니다 *\[아래에 나열된 키를 가진 객체]*.                                |
| `user.email`     | 사용자 이메일 주소.                                                                                  |
| `user.name`      | 사용자 이름.                                                                                         |
| `lang`           | *\[automatic]* – (**Sentry 언어 코드를 재정의합니다.**)                                               |
| `title`          | 문제가 발생한 것 같습니다.                                                                           |
| `subtitle`       | 저희 팀에 알림이 전달되었습니다.                                                                      |
| `subtitle2`      | 도와주고 싶다면, 아래에 어떤 일이 있었는지 알려주세요. – (**작은 화면 해상도에서는 표시되지 않습니다.**) |
| `labelName`      | 이름                                                                                                 |

| `labelEmail`     | 이메일                                                                                               |
| `labelComments`  | 어떤 일이 있었나요?                                                                                  |
| `labelClose`     | 닫기                                                                                                  |
| `labelSubmit`    | 제출                                                                                                  |
| `errorGeneric`   | 보고서를 제출하는 중 알 수 없는 오류가 발생했습니다. 다시 시도해 주세요.                             |
| `errorFormEntry` | 일부 필드가 올바르지 않습니다. 오류를 수정한 후 다시 시도해 주세요.                                  |
| `successMessage` | 피드백이 전송되었습니다. 감사합니다!                                                                  |
| `onLoad`         | n/a - (**위젯이 열릴 때 호출되는 선택적 콜백입니다.**)                                                |
| `onClose`        | n/a - (**위젯이 닫힐 때 호출되는 선택적 콜백입니다.**)                                                |

선택적 콜백 `onLoad`는 사용자가 위젯을 볼 때 호출됩니다. 이를 사용해 사용자 정의 로직을 실행할 수 있으며, 예를 들어 분석 이벤트를 기록할 수 있습니다:

```javascript
Sentry.showReportDialog({
  // ...
  onLoad() {
    // Log an event to amplitude when the report dialog opens
    amplitude.logEvent("report_dialog_seen");
  },
});
```

선택적 콜백 `onClose`는 사용자가 위젯을 닫을 때 호출됩니다. 이를 사용해 사용자 정의 로직을 실행할 수 있으며, 예를 들어 페이지를 다시 로드할 수 있습니다:

*JS SDK 버전 v7.82.0 이상이 필요합니다.*

```javascript
Sentry.showReportDialog({
  // ...
  onClose() {
    // Refresh the page after the user closes the report dialog
    location.reload();
  },
});
```

