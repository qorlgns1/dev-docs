---
title: 'Attachments | Next.js용 Sentry'
description: 'Sentry는 config 파일이나 로그 파일 같은 추가 파일을 첨부 파일로 저장하여, 추가 조사를 위해 이벤트를 더 풍부하게 만들 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments

# Attachments | Next.js용 Sentry

Sentry는 config 파일이나 로그 파일 같은 추가 파일을 첨부 파일로 저장하여, 추가 조사를 위해 이벤트를 더 풍부하게 만들 수 있습니다.

## [첨부 파일 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#uploading-attachments)

먼저 평소와 같이 SDK를 import해야 합니다:

```javascript
import * as Sentry from "@sentry/nextjs";
```

첨부 파일은 `Scope`에 속하며 모든 이벤트와 함께 전송됩니다.

```javascript
// Add an attachment
Sentry.getCurrentScope().addAttachment({
  filename: "attachment.txt",
  data: "Some content",
});

// Clear attachments
Sentry.getCurrentScope().clearAttachments();
```

첨부 파일에는 다음 필드가 있습니다:

`filename`

파일명은 필수이며 [sentry.io](https://sentry.io)에 표시됩니다.

`data`

첨부 파일의 내용은 필수이며 `string` 또는 `Uint8Array`입니다.

`contentType`

이 첨부 파일에 저장된 콘텐츠의 타입입니다. 어떤 [MIME type](https://www.iana.org/assignments/media-types/media-types.xhtml)이든 사용할 수 있으며, 기본값은 `application/octet-stream`입니다.

`mimetype`

Sentry UI에서 첨부 파일이 어떻게 렌더링되는지를 결정하는 구체적인 미디어 콘텐츠 타입입니다. 현재 다음 MIME 타입을 지원하고 렌더링할 수 있습니다:

* `text/plain`
* `text/css`
* `text/csv`
* `text/html`
* `text/javascript`
* `text/json` 또는 `text/x-json` 또는 `application/json` 또는 `application/ld+json`
* `image/jpeg`
* `image/png`
* `image/gif`
* `image/webp`
* `image/avif`
* `video/webm`
* `video/mp4`

## [전송 전에 첨부 파일 추가 또는 수정](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#add-or-modify-attachments-before-sending)

이벤트가 전송되기 전에 [`beforeSend`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#before-send)hook 또는 전역 이벤트 프로세서를 통해 첨부 파일을 추가, 제거, 수정할 수 있습니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSend: (event, hint) => {
    hint.attachments = [
      { filename: "screenshot.png", data: captureScreen() },
    ];
    return event;
  },
});

Sentry.addEventProcessor((event, hint) => {
  hint.attachments = [{ filename: "log.txt", data: readLogFile() }];
  return event;
});
```

Sentry는 압축된 요청 기준 최대 40MB, 그리고 이벤트당(해당하는 경우 크래시 리포트 파일 포함) 비압축 첨부 파일 기준 최대 200MB까지 허용합니다. 이 크기를 초과하는 업로드는 HTTP 오류 `413 Payload Too Large`로 거부되며 데이터는 즉시 삭제됩니다. 더 크거나 많은 파일을 추가하려면 보조 스토리지 옵션을 고려하세요.

첨부 파일은 30일 동안 유지됩니다. 할당량에 포함된 총 스토리지를 초과하면 첨부 파일은 저장되지 않습니다. 첨부 파일 또는 해당 첨부 파일을 포함하는 이벤트는 언제든지 삭제할 수 있습니다. 첨부 파일을 삭제해도 할당량에는 영향을 주지 않습니다. Sentry는 첨부 파일이 저장되는 즉시 해당 첨부 파일을 할당량에 반영합니다.

첨부 파일이 [quota](https://docs.sentry.io/pricing/quotas.md)에 어떤 영향을 주는지 자세히 알아보세요.

- [첨부 파일 접근 권한](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#access-to-attachments)

첨부 파일 접근을 제한하려면 조직의 **General Settings**로 이동한 다음 *Attachments Access* 드롭다운을 선택해 적절한 접근 권한을 설정하세요. 조직의 모든 구성원, 조직 결제 소유자, member, admin, manager, owner 중에서 지정할 수 있습니다.

기본적으로 스토리지가 활성화되어 있으면 모든 구성원에게 접근 권한이 부여됩니다. 구성원이 프로젝트 접근 권한이 없으면 첨부 파일 다운로드 기능은 사용할 수 없으며, Sentry에서 버튼이 회색으로 표시됩니다. 해당 구성원은 첨부 파일이 저장되어 있다는 사실만 볼 수 있습니다.

## [첨부 파일 보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/attachments.md#viewing-attachments)

첨부 파일은 표시된 이벤트의 **Issue Details** 페이지 하단에 표시됩니다.

또는 **Issue Details** 페이지의 *Attachments* 탭에서도 첨부 파일이 표시되며, 여기서 첨부 파일의 *Type*과 연결된 이벤트를 확인할 수 있습니다. Event ID를 클릭하면 해당 특정 이벤트의 **Issue Details**를 열 수 있습니다.

