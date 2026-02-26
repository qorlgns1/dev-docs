---
title: '구성 | Sentry for Next.js'
description: 'JavaScript SDK 버전 7에서는 User Feedback이 베타 통합으로 출시되었습니다. migration guide를 따라 SDK를 최신 버전으로 업데이트하는 것을 권장합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x

# 구성 | Sentry for Next.js

##### 지원 중단 경고

JavaScript SDK 버전 7에서는 User Feedback이 베타 통합으로 출시되었습니다. [migration guide](https://github.com/getsentry/sentry-javascript/blob/develop/docs/migration/feedback.md)를 따라 SDK를 최신 버전으로 업데이트하는 것을 권장합니다.

## [User Feedback Widget](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#user-feedback-widget)

User Feedback Widget은 다양한 사용자 지정 옵션을 제공하며, 제공되는 옵션이 충분하지 않다면 [use your own UI](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#bring-your-own-widget)를 사용할 수 있습니다. 아래 이미지는 어떤 요소를 사용자 지정할 수 있는지 보여줍니다. 이미지 왼쪽의 구성 키는 [text customization](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#text-customization)에 해당하고, 오른쪽의 키는 [theme customizations](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#theme-customization)에 해당합니다.

- [일반](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#general)

다음 옵션은 `feedbackIntegration({})`에서 통합에 대해 구성할 수 있습니다:

| Key            | Type                            | Default    | Description                                                                                                                                                                                                                              |
| -------------- | ------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `autoInject`   | `boolean`                       | `true`     | 통합이 추가될 때 Feedback 위젯을 애플리케이션에 주입합니다. `feedback.attachTo()` 또는 `feedback.openDialog()`를 직접 호출하려는 경우, 또는 특정 뷰에서만 위젯을 표시하려는 경우 `autoInject: false`로 설정하세요. |
| `showBranding` | `boolean`                       | `true`     | 폼 내부에 Sentry 로고를 표시합니다.                                                                                                                                                                                              |
| `colorScheme`  | `"system" \| "light" \| "dark"` | `"system"` | 색상 테마 선택을 표시합니다. `"system"`은 OS 색상 구성표를 사용합니다.                                                                                                                                                                 |

- [사용자 및 폼](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#user-and-form)

| Key               | Type                     | Default                               | Description                                                                                                            |
| ----------------- | ------------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `showName`        | `boolean`                | `true`                                | 피드백 폼에 이름 필드를 표시합니다.                                                                          |
| `showEmail`       | `boolean`                | `true`                                | 피드백 폼에 이메일 필드를 표시합니다.                                                                         |
| `isNameRequired`  | `boolean`                | `false`                               | 피드백 폼에서 이름 필드를 필수로 입력하도록 합니다.                                                          |
| `isEmailRequired` | `boolean`                | `false`                               | 피드백 폼에서 이메일 필드를 필수로 입력하도록 합니다.                                                         |
| `useSentryUser`   | `Record<string, string>` | `{ email: 'email', name: 'username'}` | `Sentry.setUser`로 설정한 Sentry SDK 사용자 필드에 맞춰 `email` 및 `name` 필드를 매핑합니다. |

기본적으로 Feedback 통합은 [`Sentry.setUser()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/identify-user.md)를 통해 사용자 컨텍스트를 설정한 경우 이름과 이메일 필드를 자동으로 채우려고 시도합니다. 이메일과 이름 필드는 각각 `email`, `username`이어야 합니다. 아래는 기본값이 아닌 사용자 필드를 사용하는 구성 예시입니다:

```javascript
Sentry.setUser({
  email: "foo@example.com",
  fullName: "Jane Doe",
});

feedbackIntegration({
  useSentryUser: {
    email: "email",
    name: "fullName",
  },
});
```

- [텍스트 사용자 지정](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#text-customization)

기본 Feedback 위젯에 표시되는 대부분의 텍스트는 사용자 지정할 수 있습니다.

| Key                  | Default                                | Description                                                         |
| -------------------- | -------------------------------------- | ------------------------------------------------------------------- |
| `buttonLabel`        | `Report a Bug`                         | 주입된 버튼의 라벨입니다.                                   |
| `submitButtonLabel`  | `Send Bug Report`                      | 피드백 폼에서 사용하는 제출 버튼의 라벨입니다.           |
| `cancelButtonLabel`  | `Cancel`                               | 피드백 폼에서 사용하는 취소 버튼의 라벨입니다.           |
| `formTitle`          | `Report a Bug`                         | 피드백 폼 상단의 제목입니다.                          |
| `nameLabel`          | `Name`                                 | 이름 입력 필드의 라벨입니다.                                  |
| `namePlaceholder`    | `Your Name`                            | 이름 입력 필드의 플레이스홀더입니다.                           |
| `emailLabel`         | `Email`                                | 이메일 입력 필드의 라벨입니다.                                 |
| `emailPlaceholder`   | `your.email@example.org`               | 이메일 입력 필드의 플레이스홀더입니다.                          |
| `messageLabel`       | `Description`                          | 피드백 설명 입력 필드의 라벨입니다.                 |
| `messagePlaceholder` | `What's the bug? What did you expect?` | 피드백 설명 입력 필드의 플레이스홀더입니다.           |
| `successMessageText` | `Thank you for your report!`           | 피드백이 성공적으로 제출된 후 표시할 메시지입니다. |
| `isRequiredText`     | `(required)`                           | 필수 필드 옆에 표시되는 텍스트입니다.                        |

사용자 지정 예시:

```javascript
feedbackIntegration({
  buttonLabel: "Feedback",
  submitButtonLabel: "Send Feedback",
  formTitle: "Send Feedback",
});
```

- [테마 사용자 지정](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#theme-customization)

색상은 Feedback 클래스 생성자를 통해 사용자 지정하거나, 주입된 버튼에 CSS 변수를 정의하여 사용자 지정할 수 있습니다. 기본 버튼을 사용하는 경우 `id="sentry-feedback` 속성이 있으므로, `#sentry-feedback` 선택자를 사용해 CSS 변수를 정의하여 재정의할 수 있습니다.

| Key                       | CSS Variable                   | Light                                     | Dark                                      | Description                                                                                            |
| ------------------------- | ------------------------------ | ----------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `background`              | `--background`                 | `#ffffff`                                 | `#29232f`                                 | 위젯(주입된 버튼 및 폼)의 배경색입니다.                                             |
| `backgroundHover`         | `--background-hover`           | `#f6f6f7`                                 | `#352f3b`                                 | 호버 상태일 때 주입된 버튼의 배경색입니다.                                         |
| `foreground`              | `--foreground`                 | `#2b2233`                                 | `#ebe6ef`                                 | 전경색(예: 텍스트 색상)입니다.                                                                     |
| `error`                   | `--error`                      | `#df3338`                                 | `#f55459`                                 | 오류 관련 구성 요소에 사용되는 색상입니다(예: 피드백 제출 오류 시 텍스트 색상). |
| `success`                 | `--success`                    | `#268d75`                                 | `#2da98c`                                 | 성공 관련 구성 요소에 사용되는 색상입니다(예: 피드백이 성공적으로 제출되었을 때의 텍스트 색상).   |
| `border`                  | `--border`                     | `1.5px solid rgba(41, 35, 47, 0.13)`      | `1.5px solid rgba(235, 230, 239, 0.15)`   | 위젯(주입된 버튼 및 폼)에 사용되는 테두리 스타일입니다.                                       |
| `borderRadius`            | `--border-radius`              | `12px`                                    | `12px`                                    | 위젯(주입된 버튼 및 성공 메시지)에 사용되는 테두리 반경 스타일입니다.                         |
| `boxShadow`               | `--box-shadow`                 | `0px 4px 24px 0px rgba(43, 34, 51, 0.12)` | `0px 4px 24px 0px rgba(43, 34, 51, 0.12)` | 위젯(주입된 버튼 및 폼)에 사용되는 박스 섀도 스타일입니다.                                   |
| `submitBackground`        | `--submit-background`          | `rgba(88, 74, 192, 1)`                    | `rgba(88, 74, 192, 1)`                    | 제출 버튼의 배경색입니다.                                                                |
| `submitBackgroundHover`   | `--submit-background-hover`    | `rgba(108, 95, 199, 1)`                   | `rgba(108, 95, 199, 1)`                   | 제출 버튼에 호버했을 때의 배경색입니다.                                                 |
| `submitBorder`            | `--submit-border`              | `rgba(108, 95, 199, 1)`                   | `rgba(108, 95, 199, 1)`                   | 제출 버튼의 테두리 스타일입니다.                                                                    |
| `submitOutlineFocus`      | `--submit-outline-focus`       | `rgba(108, 95, 199, 1)`                   | `rgba(108, 95, 199, 1)`                   | 포커스 상태에서 제출 버튼의 아웃라인 색상입니다.                                             |
| `submitForeground`        | `--submit-foreground`          | `#ffffff`                                 | `#ffffff`                                 | 제출 버튼의 전경색입니다.                                                                |
| `submitForegroundHover`   | `--submit-foreground-hover`    | `#ffffff`                                 | `#ffffff`                                 | 제출 버튼에 호버했을 때의 전경색입니다.                                                  |
| `cancelBackground`        | `--cancel-background`          | `transparent`                             | `transparent`                             | 취소 버튼의 배경색입니다.                                                                |

| `cancelBackgroundHover`   | `--cancel-background-hover`    | `var(--background-hover)`                 | `var(--background-hover)`                 | 취소 버튼에 마우스를 올렸을 때의 배경색입니다.                                                         |
| `cancelBorder`            | `--cancel-border`              | `var(--border)`                           | `var(--border)`                           | 취소 버튼의 테두리 스타일입니다.                                                                        |
| `cancelOutlineFocus`      | `--cancel-outline-focus`       | `var(--input-outline-focus)`              | `var(--input-outline-focus)`              | 취소 버튼이 포커스 상태일 때의 아웃라인 색상입니다.                                                     |
| `cancelForeground`        | `--cancel-foreground`          | `var(--foreground)`                       | `var(--foreground)`                       | 취소 버튼의 전경색입니다.                                                                               |
| `cancelForegroundHover`   | `--cancel-foreground-hover`    | `var(--foreground)`                       | `var(--foreground)`                       | 취소 버튼에 마우스를 올렸을 때의 전경색입니다.                                                          |
| `inputBackground`         | `--input-background`           | `inherit`                                 | `inherit`                                 | 폼 입력 필드의 배경색입니다.                                                                            |
| `inputForeground`         | `--input-foreground`           | `inherit`                                 | `inherit`                                 | 폼 입력 필드의 전경색입니다.                                                                            |
| `inputBorder`             | `--input-border`               | `var(--border)`                           | `var(--border)`                           | 폼 입력 필드의 테두리 스타일입니다.                                                                     |
| `inputOutlineFocus`       | `--input-outline-focus`        | `rgba(108, 95, 199, 1)`                   | `rgba(108, 95, 199, 1)`                   | 폼 입력 필드가 포커스 상태일 때의 아웃라인 색상입니다.                                                  |
| `formBorderRadius`        | `--form-border-radius`         | `20px`                                    | `20px`                                    | 폼의 테두리 반경 스타일입니다.                                                                          |
| `formContentBorderRadius` | `--form-content-border-radius` | `6px`                                     | `6px`                                     | 폼 콘텐츠(예: 입력 필드, 버튼)의 테두리 반경 스타일입니다.                                              |

다음은 Feedback 생성자 설정을 사용해 라이트 테마의 배경색만 커스터마이즈하는 예시입니다:

```javascript
feedbackIntegration({
  themeLight: {
    background: "#cccccc",
  },
});
```

또는 위와 같은 예시를 CSS 변수 방식으로 적용하면 다음과 같습니다:

```css
#sentry-feedback {
  --background: #cccccc;
}
```

- [추가 UI 커스터마이징](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#additional-ui-customization)

아래는 위의 테마 커스터마이징과 유사하게 재정의할 수 있는 추가 CSS 변수입니다. 생성자에서는 지원되지 않습니다.

| 변수            | 기본값                                  | 설명                                                                               |
| --------------- | --------------------------------------- | ---------------------------------------------------------------------------------- |
| `--bottom`      | `1rem`                                  | 기본적으로 위젯은 `fixed` 위치이며, 오른쪽 하단에 배치됩니다.                      |
| `--right`       | `1rem`                                  | 기본적으로 위젯은 `fixed` 위치이며, 오른쪽 하단에 배치됩니다.                      |
| `--top`         | `auto`                                  | 기본적으로 위젯은 `fixed` 위치이며, 오른쪽 하단에 배치됩니다.                      |
| `--left`        | `auto`                                  | 기본적으로 위젯은 `fixed` 위치이며, 오른쪽 하단에 배치됩니다.                      |
| `--z-index`     | `100000`                                | 위젯의 z-index입니다.                                                              |
| `--font-family` | `"'Helvetica Neue', Arial, sans-serif"` | 사용할 기본 글꼴 패밀리입니다.                                                     |
| `--font-size`   | `14px`                                  | 글꼴 크기입니다.                                                                   |

- [이벤트 콜백](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#event-callbacks)

사용자가 피드백 폼과 상호작용을 시작한 시점을 파악하는 것이 유용한 경우가 있으므로, 커스텀 로깅을 추가하거나 사용자가 완료했는지 알 수 있도록 페이지의 백그라운드 타이머를 시작/중지할 수 있게 했습니다.

Feedback 통합을 초기화할 때 다음 콜백을 전달하세요:

```javascript
feedbackIntegration({
  onFormOpen: () => {},
  onFormClose: () => {},
  onSubmitSuccess: () => {},
  onSubmitError: () => {},
});
```

- [사용자 정의 버튼 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#bring-your-own-button)

기본으로 삽입되는 버튼 대신 직접 만든 버튼으로 폼 표시를 트리거할 수 있습니다. `feedback.attachTo()`를 호출하면 SDK가 해당 버튼에 클릭 리스너를 연결합니다. 생성자가 받는 동일한 커스터마이징 옵션(예: 텍스트 라벨, 색상)도 함께 전달할 수 있습니다.

```javascript
const feedback = feedbackIntegration({
  // Disable the injection of the default widget
  autoInject: false,
});

feedback.attachTo(document.querySelector("#your-button"), {
  formTitle: "Report a Bug!",
});
```

또는 `feedback.openDialog()`를 호출할 수도 있습니다:

```typescript
import { BrowserClient, Feedback, getClient } from "@sentry/react";

function MyFeedbackButton() {
  const client = getClient<BrowserClient>();
  const feedback = client?.getIntegration(Feedback);

  // Don't render custom feedback button if Feedback integration isn't installed
  if (!feedback) {
    return null;
  }

  return (
    <button type="button" onClick={() => feedback.openDialog()}>
      Give me feedback
    </button>
  );
}
```

- [사용자 정의 위젯 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#bring-your-own-widget)

직접 만든 UI 컴포넌트로 피드백을 수집한 뒤, 피드백 데이터 객체를 `sendFeedback()` 함수에 전달할 수도 있습니다. `sendFeedback` 함수는 두 개의 매개변수를 받습니다:

* 필수 `message` 속성과 선택적 `name`, `email` 속성을 가진 JavaScript 객체 또는 동일한 속성을 가진 `FormData` 인스턴스
* 선택적 "options" 객체

```javascript
Sentry.sendFeedback(
  {
    name: "Jane Doe", // optional
    email: "email@example.org", // optional
    message: "This is an example feedback", // required
  },
  {
    includeReplay: true, // optional
  },
);
```

다음은 간단한 예시입니다:

```html
<form id="my-feedback-form">
  <input name="name" />
  <input name="email" />
  <textarea name="message" placeholder="What's the issue?" />
</form>
```

## [크래시 리포트 모달](https://docs.sentry.io/platforms/javascript/guides/nextjs/user-feedback/configuration__v7.x/#crash-report-modal)

조직의 요구사항에 맞게 Crash-Report 모달을 커스터마이즈할 수 있습니다(예: 현지화 목적). 모든 옵션은 `Sentry.showReportDialog` 호출을 통해 전달할 수 있습니다.

| 매개변수         | 기본값                                                                                               |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| `eventId`        | 이벤트 ID를 수동으로 설정합니다.                                                                     |
| `dsn`            | 리포트를 보낼 dsn을 수동으로 설정합니다.                                                             |
| `user`           | 사용자 데이터를 수동으로 설정합니다 *\[아래 키를 포함한 객체]*.                                      |
| `user.email`     | 사용자의 이메일 주소입니다.                                                                          |
| `user.name`      | 사용자의 이름입니다.                                                                                 |
| `lang`           | *\[자동]* – (**Sentry의 언어 코드 재정의**)                                                          |
| `title`          | 문제가 발생한 것 같습니다.                                                                           |
| `subtitle`       | 저희 팀에 알림이 전송되었습니다.                                                                     |
| `subtitle2`      | 도움을 주시려면 아래에 어떤 일이 있었는지 알려주세요. – (**작은 화면 해상도에서는 표시되지 않습니다.**) |
| `labelName`      | 이름                                                                                                 |
| `labelEmail`     | 이메일                                                                                                |
| `labelComments`  | 무슨 일이 있었나요?                                                                                  |
| `labelClose`     | 닫기                                                                                                 |
| `labelSubmit`    | 제출                                                                                                 |
| `errorGeneric`   | 리포트를 제출하는 중 알 수 없는 오류가 발생했습니다. 다시 시도해 주세요.                              |
| `errorFormEntry` | 일부 필드가 유효하지 않습니다. 오류를 수정한 뒤 다시 시도해 주세요.                                   |
| `successMessage` | 피드백이 전송되었습니다. 감사합니다!                                                                 |
| `onLoad`         | 해당 없음 - (**위젯이 열릴 때 호출되는 선택적 콜백입니다.**)                                          |
| `onClose`        | 해당 없음 - (**위젯이 닫힐 때 호출되는 선택적 콜백입니다.**)                                          |

선택적 콜백 `onLoad`는 사용자가 위젯을 볼 때 호출됩니다. 예를 들어 분석 이벤트를 기록하는 등의 커스텀 로직을 실행하는 데 사용할 수 있습니다:

```javascript
Sentry.showReportDialog({
  // ...
  onLoad() {
    // Log an event to amplitude when the report dialog opens
    amplitude.logEvent("report_dialog_seen");
  },
});
```

선택적 콜백 `onClose`는 사용자가 위젯을 닫을 때 호출됩니다. 예를 들어 페이지를 다시 로드하는 등의 커스텀 로직을 실행하는 데 사용할 수 있습니다:

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

