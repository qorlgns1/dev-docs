---
title: "Download"
description: "브라우저 컨텍스트에 속한 모든 다운로드 파일은 브라우저 컨텍스트가 닫힐 때 삭제됩니다."
---

Source URL: https://playwright.dev/docs/api/class-download

# Download | Playwright

[Download](https://playwright.dev/docs/api/class-download "Download") 객체는 [page.on('download')](https://playwright.dev/docs/api/class-page#page-event-download) 이벤트를 통해 page에서 전달됩니다.

브라우저 컨텍스트에 속한 모든 다운로드 파일은 브라우저 컨텍스트가 닫힐 때 삭제됩니다.

다운로드 이벤트는 다운로드가 시작되면 발생합니다. 다운로드 경로는 다운로드가 완료되면 사용할 수 있습니다.

```
    // Start waiting for download before clicking. Note no await.
    const downloadPromise = page.waitForEvent('download');
    await page.getByText('Download file').click();
    const download = await downloadPromise;

    // Wait for the download process to complete and save the downloaded file somewhere.
    await download.saveAs('/path/to/save/at/' + download.suggestedFilename());

```

---

## Methods[​](https://playwright.dev/docs/api/class-download#methods "Direct link to Methods")

### cancel[​](https://playwright.dev/docs/api/class-download#download-cancel "Direct link to cancel")

추가된 버전: v1.13 download.cancel

다운로드를 취소합니다. 다운로드가 이미 완료되었거나 취소된 상태여도 실패하지 않습니다. 취소가 성공하면 `download.failure()` 는 `'canceled'` 로 resolve됩니다.

**사용법**

```
    await download.cancel();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-download#download-cancel-return)

---

### createReadStream[​](https://playwright.dev/docs/api/class-download#download-create-read-stream "Direct link to createReadStream")

v1.9 이전에 추가됨 download.createReadStream

성공한 다운로드에 대해 읽기 가능한 스트림을 반환하고, 실패/취소된 다운로드의 경우 예외를 발생시킵니다.

참고

읽기 가능한 스트림이 필요하지 않다면, 보통 다운로드 완료 후 디스크에서 파일을 읽는 편이 더 간단합니다. [download.path()](https://playwright.dev/docs/api/class-download#download-path)를 참고하세요.

**사용법**

```
    await download.createReadStream();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Readable](https://nodejs.org/api/stream.html#stream_class_stream_readable "Readable")>[#](https://playwright.dev/docs/api/class-download#download-create-read-stream-return)

---

### delete[​](https://playwright.dev/docs/api/class-download#download-delete "Direct link to delete")

v1.9 이전에 추가됨 download.delete

다운로드된 파일을 삭제합니다. 필요하면 다운로드가 완료될 때까지 대기합니다.

**사용법**

```
    await download.delete();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-download#download-delete-return)

---

### failure[​](https://playwright.dev/docs/api/class-download#download-failure "Direct link to failure")

v1.9 이전에 추가됨 download.failure

다운로드 오류가 있으면 반환합니다. 필요하면 다운로드가 완료될 때까지 대기합니다.

**사용법**

```
    await download.failure();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-download#download-failure-return)

---

### page[​](https://playwright.dev/docs/api/class-download#download-page "Direct link to page")

추가된 버전: v1.12 download.page

다운로드가 속한 page를 가져옵니다.

**사용법**

```
    download.page();

```

**반환값**

- [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-download#download-page-return)

---

### path[​](https://playwright.dev/docs/api/class-download#download-path "Direct link to path")

v1.9 이전에 추가됨 download.path

성공한 다운로드에 대한 파일 경로를 반환하고, 실패/취소된 다운로드의 경우 예외를 발생시킵니다. 필요하면 다운로드가 완료될 때까지 대기합니다. 원격으로 연결된 경우 이 메서드는 예외를 발생시킵니다.

다운로드 파일명은 임의의 GUID이므로, 제안된 파일명을 얻으려면 [download.suggestedFilename()](https://playwright.dev/docs/api/class-download#download-suggested-filename)을 사용하세요.

**사용법**

```
    await download.path();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-download#download-path-return)

---

### saveAs[​](https://playwright.dev/docs/api/class-download#download-save-as "Direct link to saveAs")

v1.9 이전에 추가됨 download.saveAs

사용자가 지정한 경로로 다운로드를 복사합니다. 다운로드가 진행 중일 때도 이 메서드를 안전하게 호출할 수 있습니다. 필요하면 다운로드가 완료될 때까지 대기합니다.

**사용법**

```
    await download.saveAs('/path/to/save/at/' + download.suggestedFilename());

```

**인수**

- `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-download#download-save-as-option-path)

다운로드를 복사할 경로입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-download#download-save-as-return)

---

### suggestedFilename[​](https://playwright.dev/docs/api/class-download#download-suggested-filename "Direct link to suggestedFilename")

v1.9 이전에 추가됨 download.suggestedFilename

이 다운로드에 대해 제안된 파일명을 반환합니다. 일반적으로 브라우저가 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) 응답 헤더 또는 `download` 속성을 바탕으로 계산합니다. [whatwg](https://html.spec.whatwg.org/#downloading-resources)의 명세를 참고하세요. 브라우저마다 계산 로직이 다를 수 있습니다.

**사용법**

```
    download.suggestedFilename();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-download#download-suggested-filename-return)

---

### url[​](https://playwright.dev/docs/api/class-download#download-url "Direct link to url")

v1.9 이전에 추가됨 download.url

다운로드된 URL을 반환합니다.

**사용법**

```
    download.url();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-download#download-url-return)
