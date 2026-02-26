---
title: "FileChooser"
description: "// Start waiting for file chooser before clicking. Note no await."
---

Source URL: https://playwright.dev/docs/api/class-filechooser

# FileChooser | Playwright

[FileChooser](https://playwright.dev/docs/api/class-filechooser "FileChooser") 객체는 페이지에서 [page.on('filechooser')](https://playwright.dev/docs/api/class-page#page-event-file-chooser) 이벤트를 통해 전달됩니다.

```
    // Start waiting for file chooser before clicking. Note no await.
    const fileChooserPromise = page.waitForEvent('filechooser');
    await page.getByText('Upload file').click();
    const fileChooser = await fileChooserPromise;
    await fileChooser.setFiles(path.join(__dirname, 'myfile.pdf'));

```

---

## 메서드[​](https://playwright.dev/docs/api/class-filechooser#methods "Direct link to Methods")

### element[​](https://playwright.dev/docs/api/class-filechooser#file-chooser-element "Direct link to element")

v1.9 이전에 추가됨 fileChooser.element

이 파일 선택기와 연결된 input 요소를 반환합니다.

**사용법**

```
    fileChooser.element();

```

**반환값**

- [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")[#](https://playwright.dev/docs/api/class-filechooser#file-chooser-element-return)

---

### isMultiple[​](https://playwright.dev/docs/api/class-filechooser#file-chooser-is-multiple "Direct link to isMultiple")

v1.9 이전에 추가됨 fileChooser.isMultiple

이 파일 선택기가 여러 파일을 허용하는지 여부를 반환합니다.

**사용법**

```
    fileChooser.isMultiple();

```

**반환값**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-filechooser#file-chooser-is-multiple-return)

---

### page[​](https://playwright.dev/docs/api/class-filechooser#file-chooser-page "Direct link to page")

v1.9 이전에 추가됨 fileChooser.page

이 파일 선택기가 속한 페이지를 반환합니다.

**사용법**

```
    fileChooser.page();

```

**반환값**

- [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-filechooser#file-chooser-page-return)

---

### setFiles[​](https://playwright.dev/docs/api/class-filechooser#file-chooser-set-files "Direct link to setFiles")

v1.9 이전에 추가됨 fileChooser.setFiles

이 선택기와 연결된 파일 입력의 값을 설정합니다. `filePaths` 중 일부가 상대 경로인 경우 현재 작업 디렉터리를 기준으로 해석됩니다. 빈 배열이면 선택된 파일을 지웁니다.

**사용법**

```
    await fileChooser.setFiles(files);
    await fileChooser.setFiles(files, options);

```

**인수**

- `files` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-filechooser#file-chooser-set-files-option-files)
  - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

    * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 타입

    * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-filechooser#file-chooser-set-files-option-no-wait-after)

지원 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-filechooser#file-chooser-set-files-option-timeout)

밀리초 단위의 최대 시간입니다. 기본값은 `0` \- 제한 시간 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-filechooser#file-chooser-set-files-return)
