---
title: "Frame"
description: "항상 모든 시점에서 page는 page.mainFrame() 및 frame.childFrames() 메서드를 통해 현재 frame 트리를 노출합니다."
---

Source URL: https://playwright.dev/docs/api/class-frame

# Frame | Playwright

항상 모든 시점에서 page는 [page.mainFrame()](https://playwright.dev/docs/api/class-page#page-main-frame) 및 [frame.childFrames()](https://playwright.dev/docs/api/class-frame#frame-child-frames) 메서드를 통해 현재 frame 트리를 노출합니다.

[Frame](https://playwright.dev/docs/api/class-frame "Frame") 객체의 수명 주기는 page 객체에서 디스패치되는 세 가지 이벤트로 제어됩니다.

- [page.on('frameattached')](https://playwright.dev/docs/api/class-page#page-event-frame-attached) \- frame이 page에 연결될 때 발생합니다. Frame은 page에 한 번만 연결될 수 있습니다.
- [page.on('framenavigated')](https://playwright.dev/docs/api/class-page#page-event-frame-navigated) \- frame이 다른 URL로의 탐색을 커밋할 때 발생합니다.
- [page.on('framedetached')](https://playwright.dev/docs/api/class-page#page-event-frame-detached) \- frame이 page에서 분리될 때 발생합니다. Frame은 page에서 한 번만 분리될 수 있습니다.

frame 트리를 출력하는 예시:

```
    const { firefox } = require('playwright');  // Or 'chromium' or 'webkit'.

    (async () => {
      const browser = await firefox.launch();
      const page = await browser.newPage();
      await page.goto('https://www.google.com/chrome/browser/canary.html');
      dumpFrameTree(page.mainFrame(), '');
      await browser.close();

      function dumpFrameTree(frame, indent) {
        console.log(indent + frame.url());
        for (const child of frame.childFrames())
          dumpFrameTree(child, indent + '  ');
      }
    })();

```

---

## Methods[​](https://playwright.dev/docs/api/class-frame#methods "Direct link to Methods")

### addScriptTag[​](https://playwright.dev/docs/api/class-frame#frame-add-script-tag "Direct link to addScriptTag")

v1.9 이전에 추가됨 frame.addScriptTag

스크립트의 onload가 발생하거나 스크립트 콘텐츠가 frame에 주입되면 추가된 태그를 반환합니다.

원하는 url 또는 content로 page에 `<script>` 태그를 추가합니다.

**사용법**

```
    await frame.addScriptTag();
    await frame.addScriptTag(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `content` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-add-script-tag-option-content)

frame에 주입할 원시 JavaScript 콘텐츠입니다.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-add-script-tag-option-path)

frame에 주입할 JavaScript 파일 경로입니다. `path`가 상대 경로인 경우 현재 작업 디렉터리를 기준으로 해석됩니다.

    * `type` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-add-script-tag-option-type)

스크립트 타입입니다. JavaScript ES6 모듈을 로드하려면 'module'을 사용하세요. 자세한 내용은 [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)를 참고하세요.

    * `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-add-script-tag-option-url)

추가할 스크립트의 URL입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>[#](https://playwright.dev/docs/api/class-frame#frame-add-script-tag-return)

---

### addStyleTag[​](https://playwright.dev/docs/api/class-frame#frame-add-style-tag "Direct link to addStyleTag")

v1.9 이전에 추가됨 frame.addStyleTag

스타일시트의 onload가 발생하거나 CSS 콘텐츠가 frame에 주입되면 추가된 태그를 반환합니다.

원하는 url이 있는 `<link rel="stylesheet">` 태그 또는 content가 있는 `<style type="text/css">` 태그를 page에 추가합니다.

**사용법**

```
    await frame.addStyleTag();
    await frame.addStyleTag(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `content` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-add-style-tag-option-content)

frame에 주입할 원시 CSS 콘텐츠입니다.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-add-style-tag-option-path)

frame에 주입할 CSS 파일 경로입니다. `path`가 상대 경로인 경우 현재 작업 디렉터리를 기준으로 해석됩니다.

    * `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-add-style-tag-option-url)

`<link>` 태그의 URL입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>[#](https://playwright.dev/docs/api/class-frame#frame-add-style-tag-return)

---

### childFrames[​](https://playwright.dev/docs/api/class-frame#frame-child-frames "Direct link to childFrames")

v1.9 이전에 추가됨 frame.childFrames

**사용법**

```
    frame.childFrames();

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Frame](https://playwright.dev/docs/api/class-frame "Frame")>[#](https://playwright.dev/docs/api/class-frame#frame-child-frames-return)

---

### content[​](https://playwright.dev/docs/api/class-frame#frame-content "Direct link to content")

v1.9 이전에 추가됨 frame.content

doctype을 포함한 frame의 전체 HTML 콘텐츠를 가져옵니다.

**사용법**

```
    await frame.content();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-frame#frame-content-return)

---

### dragAndDrop[​](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop "Direct link to dragAndDrop")

추가됨: v1.13 frame.dragAndDrop

**사용법**

```
    await frame.dragAndDrop(source, target);
    await frame.dragAndDrop(source, target, options);

```

**인수**

- `source` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-source)

드래그할 요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `target` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-target)

드롭할 대상 요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사 우회를 할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-no-wait-after)

사용 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `sourcePosition` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가됨: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-source-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소의 padding box 좌상단을 기준으로 이 지점에서 source 요소를 클릭합니다. 지정하지 않으면 요소의 보이는 지점 중 하나가 사용됩니다.

    * `steps` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ 추가됨: v1.57[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-steps)

기본값은 1입니다. 드래그의 `mousedown`과 `mouseup` 사이 이동을 표현하기 위해 보간된 `mousemove` 이벤트 `n`개를 전송합니다. 1로 설정하면 목적지 위치에서 단일 `mousemove` 이벤트 하나를 발생시킵니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가됨: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-strict)

true이면 selector가 단일 요소로 해석되어야 합니다. 주어진 selector가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `targetPosition` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가됨: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-target-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소의 padding box 좌상단을 기준으로 이 지점에 target 요소를 드롭합니다. 지정하지 않으면 요소의 보이는 지점 중 하나가 사용됩니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음. 기본값은 config의 `actionTimeout` 옵션 또는 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 실제 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 대기할 때 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-drag-and-drop-return)

---

### evaluate[​](https://playwright.dev/docs/api/class-frame#frame-evaluate "Direct link to evaluate")

v1.9 이전에 추가됨 frame.evaluate

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-evaluate-option-expression)의 반환값을 돌려줍니다.

[frame.evaluate()](https://playwright.dev/docs/api/class-frame#frame-evaluate)에 전달한 함수가 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [frame.evaluate()](https://playwright.dev/docs/api/class-frame#frame-evaluate)는 해당 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

[frame.evaluate()](https://playwright.dev/docs/api/class-frame#frame-evaluate)에 전달한 함수가 non-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") 값을 반환하면 [frame.evaluate()](https://playwright.dev/docs/api/class-frame#frame-evaluate)는 `undefined`를 반환합니다. Playwright는 `JSON`으로 직렬화할 수 없는 일부 추가 값도 전달을 지원합니다: `-0`, `NaN`, `Infinity`, `-Infinity`.

**사용법**

```
    const result = await frame.evaluate(([x, y]) => {
      return Promise.resolve(x * y);
    }, [7, 8]);
    console.log(result); // prints "56"

```

함수 대신 문자열을 전달할 수도 있습니다.

```
    console.log(await frame.evaluate('1 + 2')); // prints "3"

```

[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") 인스턴스를 [frame.evaluate()](https://playwright.dev/docs/api/class-frame#frame-evaluate)의 인수로 전달할 수 있습니다.

```
    const bodyHandle = await frame.evaluate('document.body');
    const html = await frame.evaluate(([body, suffix]) =>
      body.innerHTML + suffix, [bodyHandle, 'hello'],
    );
    await bodyHandle.dispose();

```

**인수**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-evaluate-option-expression)

page 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-evaluate-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-evaluate-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-frame#frame-evaluate-return)

---

### evaluateHandle[​](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle "Direct link to evaluateHandle")

v1.9 이전에 추가됨 frame.evaluateHandle

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle-option-expression)의 반환값을 [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")로 반환합니다.

[frame.evaluate()](https://playwright.dev/docs/api/class-frame#frame-evaluate)와 [frame.evaluateHandle()](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle)의 유일한 차이는 [frame.evaluateHandle()](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle)이 [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")을 반환한다는 점입니다.

[frame.evaluateHandle()](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle)에 전달된 함수가 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [frame.evaluateHandle()](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle)은 해당 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

**사용법**

```
    // Handle for the window object
    const aWindowHandle = await frame.evaluateHandle(() => Promise.resolve(window));

```

함수 대신 문자열을 전달할 수도 있습니다.

```
    const aHandle = await frame.evaluateHandle('document'); // Handle for the 'document'.

```

[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle") 인스턴스를 [frame.evaluateHandle()](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle)의 인수로 전달할 수 있습니다.

```
    const aHandle = await frame.evaluateHandle(() => document.body);
    const resultHandle = await frame.evaluateHandle(([body, suffix]) =>
      body.innerHTML + suffix, [aHandle, 'hello'],
    );
    console.log(await resultHandle.jsonValue());
    await resultHandle.dispose();

```

**인수**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle-option-expression)

page 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle-return)

---

### frameElement[​](https://playwright.dev/docs/api/class-frame#frame-frame-element "Direct link to frameElement")

v1.9 이전에 추가됨 frame.frameElement

이 frame에 해당하는 `frame` 또는 `iframe` element handle을 반환합니다.

이는 [elementHandle.contentFrame()](https://playwright.dev/docs/api/class-elementhandle#element-handle-content-frame)의 역연산입니다. 반환된 handle은 실제로 부모 frame에 속한다는 점에 유의하세요.

`frameElement()`가 반환되기 전에 frame이 분리되면 이 메서드는 에러를 발생시킵니다.

**사용법**

```
    const frameElement = await frame.frameElement();
    const contentFrame = await frameElement.contentFrame();
    console.log(frame === contentFrame);  // -> true

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>[#](https://playwright.dev/docs/api/class-frame#frame-frame-element-return)

---

### frameLocator[​](https://playwright.dev/docs/api/class-frame#frame-frame-locator "Direct link to frameLocator")

추가됨: v1.17 frame.frameLocator

iframe으로 작업할 때 iframe 내부로 진입하여 해당 iframe 안의 요소를 선택할 수 있는 frame locator를 만들 수 있습니다.

**사용법**

다음 스니펫은 id가 `my-frame`인 iframe(예: `<iframe id="my-frame">`)에서 텍스트가 "Submit"인 요소를 찾습니다.

```
    const locator = frame.frameLocator('#my-iframe').getByText('Submit');
    await locator.click();

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-frame-locator-option-selector)

DOM 요소를 해석할 때 사용할 selector입니다.

**반환값**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-frame#frame-frame-locator-return)

---

### getByAltText[​](https://playwright.dev/docs/api/class-frame#frame-get-by-alt-text "Direct link to getByAltText")

추가됨: v1.27 frame.getByAltText

alt 텍스트로 요소를 찾을 수 있습니다.

**사용법**

예를 들어 이 메서드는 alt 텍스트가 "Playwright logo"인 이미지를 찾습니다.

```
    <img alt='Playwright logo'>

```

```
    await page.getByAltText('Playwright logo').click();

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-alt-text-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-alt-text-option-exact)

정확히 일치하는 항목(대소문자 구분, 전체 문자열)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾을 때는 무시됩니다. 정확히 일치하더라도 공백은 trim됩니다.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-alt-text-return)

---

### getByLabel[​](https://playwright.dev/docs/api/class-frame#frame-get-by-label "Direct link to getByLabel")

추가됨: v1.27 frame.getByLabel

연결된 `<label>` 또는 `aria-labelledby` 요소의 텍스트, 혹은 `aria-label` 속성으로 input 요소를 찾을 수 있습니다.

**사용법**

예를 들어 다음 DOM에서 이 메서드는 라벨이 "Username" 및 "Password"인 input을 찾습니다.

```
    <input aria-label="Username">
    <label for="password-input">Password:</label>
    <input id="password-input">

```

```
    await page.getByLabel('Username').fill('john');
    await page.getByLabel('Password').fill('secret');

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-label-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-label-option-exact)

정확히 일치하는 항목(대소문자 구분, 전체 문자열)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾을 때는 무시됩니다. 정확히 일치하더라도 공백은 trim됩니다.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-label-return)

---

### getByPlaceholder[​](https://playwright.dev/docs/api/class-frame#frame-get-by-placeholder "Direct link to getByPlaceholder")

추가됨: v1.27 frame.getByPlaceholder

placeholder 텍스트로 input 요소를 찾을 수 있습니다.

**사용법**

예를 들어 다음 DOM 구조를 보세요.

```
    <input type="email" placeholder="name@example.com" />

```

placeholder 텍스트로 input을 찾은 뒤 값을 채울 수 있습니다.

```
    await page
        .getByPlaceholder('name@example.com')
        .fill('playwright@microsoft.com');

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-placeholder-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-placeholder-option-exact)

정확히 일치하는 항목(대소문자 구분, 전체 문자열)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾을 때는 무시됩니다. 정확히 일치하더라도 공백은 trim됩니다.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-placeholder-return)

---

### getByRole[​](https://playwright.dev/docs/api/class-frame#frame-get-by-role "Direct link to getByRole")

추가됨: v1.27 frame.getByRole

[ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles), [ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes), [accessible name](https://w3c.github.io/accname/#dfn-accessible-name)으로 요소를 찾을 수 있습니다.

**사용법**

다음 DOM 구조를 보세요.

```
    <h3>Sign up</h3>
    <label>
      <input type="checkbox" /> Subscribe
    </label>
    <button>Submit</button>

```

암시적 role로 각 요소를 찾을 수 있습니다.

```
    await expect(page.getByRole('heading', { name: 'Sign up' })).toBeVisible();

    await page.getByRole('checkbox', { name: 'Subscribe' }).check();

    await page.getByRole('button', { name: /submit/i }).click();

```

**인수**

- `role` "alert" | "alertdialog" | "application" | "article" | "banner" | "blockquote" | "button" | "caption" | "cell" | "checkbox" | "code" | "columnheader" | "combobox" | "complementary" | "contentinfo" | "definition" | "deletion" | "dialog" | "directory" | "document" | "emphasis" | "feed" | "figure" | "form" | "generic" | "grid" | "gridcell" | "group" | "heading" | "img" | "insertion" | "link" | "list" | "listbox" | "listitem" | "log" | "main" | "marquee" | "math" | "meter" | "menu" | "menubar" | "menuitem" | "menuitemcheckbox" | "menuitemradio" | "navigation" | "none" | "note" | "option" | "paragraph" | "presentation" | "progressbar" | "radio" | "radiogroup" | "region" | "row" | "rowgroup" | "rowheader" | "scrollbar" | "search" | "searchbox" | "separator" | "slider" | "spinbutton" | "status" | "strong" | "subscript" | "superscript" | "switch" | "tab" | "table" | "tablist" | "tabpanel" | "term" | "textbox" | "time" | "timer" | "toolbar" | "tooltip" | "tree" | "treegrid" | "treeitem"[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-role)

필수 aria role입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `checked` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-checked)

보통 `aria-checked` 또는 네이티브 `<input type=checkbox>` 컨트롤로 설정되는 속성입니다.

[`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked)에 대해 자세히 알아보세요.

    * `disabled` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-disabled)

보통 `aria-disabled` 또는 `disabled`로 설정되는 속성입니다.

note

대부분의 다른 속성과 달리 `disabled`는 DOM 계층 전체에 걸쳐 상속됩니다. [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled)에 대해 자세히 알아보세요.

    * `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가됨: v1.28[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-exact)

[name](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-name)을 정확히 일치(대소문자 구분, 전체 문자열)로 매칭할지 여부입니다. 기본값은 false입니다. [name](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-name)이 정규식이면 무시됩니다. 정확히 일치하더라도 공백은 trim됩니다.

    * `expanded` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-expanded)

보통 `aria-expanded`로 설정되는 속성입니다.

[`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded)에 대해 자세히 알아보세요.

    * `includeHidden` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-include-hidden)

숨김 요소를 매칭할지 제어하는 옵션입니다. 기본적으로 role selector는 ARIA에서 [정의한](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion) 숨김이 아닌 요소만 매칭합니다.

[`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden)에 대해 자세히 알아보세요.

    * `level` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-level)

보통 `heading`, `listitem`, `row`, `treeitem` role에 존재하는 숫자 속성이며, `<h1>-<h6>` 요소에는 기본값이 있습니다.

[`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level)에 대해 자세히 알아보세요.

    * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-name)

[accessible name](https://w3c.github.io/accname/#dfn-accessible-name)을 매칭하기 위한 옵션입니다. 기본적으로 대소문자를 구분하지 않고 부분 문자열 검색을 수행하며, 이 동작은 [exact](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-exact)로 제어할 수 있습니다.

[accessible name](https://w3c.github.io/accname/#dfn-accessible-name)에 대해 자세히 알아보세요.

    * `pressed` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-pressed)

보통 `aria-pressed`로 설정되는 속성입니다.

[`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed)에 대해 자세히 알아보세요.

    * `selected` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-option-selected)

보통 `aria-selected`로 설정되는 속성입니다.

[`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected)에 대해 자세히 알아보세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-role-return)

**세부 정보**

Role selector는 접근성 감사 및 적합성 테스트를 **대체하지 않으며**, ARIA 가이드라인에 대한 초기 피드백을 제공합니다.

많은 html 요소는 role selector가 인식하는 암시적으로 [정의된 role](https://w3c.github.io/html-aam/#html-element-role-mappings)을 가집니다. 지원되는 모든 role은 [여기](https://www.w3.org/TR/wai-aria-1.2/#role_definitions)에서 확인할 수 있습니다. ARIA 가이드라인은 `role` 및/또는 `aria-*` 속성에 기본값을 설정해 암시적 role과 속성을 중복하는 것을 **권장하지 않습니다**.

---

### getByTestId[​](https://playwright.dev/docs/api/class-frame#frame-get-by-test-id "Direct link to getByTestId")

추가됨: v1.27 frame.getByTestId

test id로 요소를 찾습니다.

**사용법**

다음 DOM 구조를 보세요.

```
    <button data-testid="directions">Itinéraire</button>

```

test id로 요소를 찾을 수 있습니다.

```
    await page.getByTestId('directions').click();

```

**인수**

- `testId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-test-id-option-test-id)

요소를 찾는 데 사용할 id입니다.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-test-id-return)

**세부 정보**

기본적으로 `data-testid` 속성이 test id로 사용됩니다. 필요하면 [selectors.setTestIdAttribute()](https://playwright.dev/docs/api/class-selectors#selectors-set-test-id-attribute)를 사용해 다른 test id 속성을 설정하세요.

```
    // Set custom test id attribute from @playwright/test config:
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        testIdAttribute: 'data-pw'
      },
    });

```

---

### getByText[​](https://playwright.dev/docs/api/class-frame#frame-get-by-text "Direct link to getByText")

추가됨: v1.27 frame.getByText

주어진 텍스트를 포함하는 요소를 찾을 수 있습니다.

접근 가능한 역할 같은 다른 기준으로 매칭한 뒤 텍스트 내용으로 필터링할 수 있게 해주는 [locator.filter()](https://playwright.dev/docs/api/class-locator#locator-filter)도 참고하세요.

**사용법**

다음 DOM 구조를 가정해 보겠습니다:

```
    <div>Hello <span>world</span></div>
    <div>Hello</div>

```

텍스트 부분 문자열, 정확한 문자열 또는 정규식으로 찾을 수 있습니다:

```
    // Matches <span>
    page.getByText('world');

    // Matches first <div>
    page.getByText('Hello world');

    // Matches second <div>
    page.getByText('Hello', { exact: true });

    // Matches both <div>s
    page.getByText(/Hello/);

    // Matches second <div>
    page.getByText(/^hello$/i);

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-text-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-text-option-exact)

정확히 일치하는 항목(대소문자 구분, 전체 문자열 일치)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾을 때는 무시됩니다. 정확 일치에서도 공백은 여전히 트리밍된다는 점에 유의하세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-text-return)

**세부 사항**

텍스트 매칭은 정확 일치일 때도 항상 공백을 정규화합니다. 예를 들어 여러 공백을 하나로 바꾸고, 줄바꿈을 공백으로 바꾸며, 앞뒤 공백을 무시합니다.

`button` 및 `submit` 타입의 input 요소는 텍스트 내용 대신 `value`로 매칭됩니다. 예를 들어 텍스트 `"Log in"`으로 찾으면 `<input type=button value="Log in">`과 매칭됩니다.

---

### getByTitle[​](https://playwright.dev/docs/api/class-frame#frame-get-by-title "Direct link to getByTitle")

추가됨: v1.27 frame.getByTitle

title 속성으로 요소를 찾을 수 있습니다.

**사용법**

다음 DOM 구조를 가정해 보겠습니다.

```
    <span title='Issues count'>25 issues</span>

```

title 텍스트로 찾은 뒤 이슈 개수를 확인할 수 있습니다:

```
    await expect(page.getByTitle('Issues count')).toHaveText('25 issues');

```

**인수**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-title-option-text)

요소를 찾기 위한 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-by-title-option-exact)

정확히 일치하는 항목(대소문자 구분, 전체 문자열 일치)을 찾을지 여부입니다. 기본값은 false입니다. 정규식으로 찾을 때는 무시됩니다. 정확 일치에서도 공백은 여전히 트리밍된다는 점에 유의하세요.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-get-by-title-return)

---

### goto[​](https://playwright.dev/docs/api/class-frame#frame-goto "Direct link to goto")

v1.9 이전에 추가됨 frame.goto

메인 리소스 응답을 반환합니다. 리다이렉트가 여러 번 발생한 경우 마지막 리다이렉트의 응답으로 내비게이션이 resolve됩니다.

다음 경우 이 메서드는 오류를 발생시킵니다:

- SSL 오류가 있는 경우(예: 자체 서명 인증서).
- 대상 URL이 유효하지 않은 경우.
- 내비게이션 중 [timeout](https://playwright.dev/docs/api/class-frame#frame-goto-option-timeout)을 초과한 경우.
- 원격 서버가 응답하지 않거나 접근할 수 없는 경우.
- 메인 리소스 로드에 실패한 경우.

원격 서버가 404 "Not Found", 500 "Internal Server Error"를 포함한 유효한 HTTP 상태 코드를 반환하면 이 메서드는 오류를 발생시키지 않습니다. 이러한 응답의 상태 코드는 [response.status()](https://playwright.dev/docs/api/class-response#response-status)를 호출해 가져올 수 있습니다.

note

이 메서드는 오류를 발생시키거나 메인 리소스 응답을 반환합니다. 유일한 예외는 `about:blank`로의 내비게이션 또는 해시만 다른 동일 URL로의 내비게이션이며, 이 경우 성공하고 `null`을 반환합니다.

note

Headless 모드는 PDF 문서로의 내비게이션을 지원하지 않습니다. [upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295)를 참고하세요.

**사용법**

```
    await frame.goto(url);
    await frame.goto(url, options);

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-goto-option-url)

프레임이 이동할 URL입니다. URL에는 `https://` 같은 스킴이 포함되어야 합니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `referer` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-goto-option-referer)

Referer 헤더 값입니다. 제공되면 [page.setExtraHTTPHeaders()](https://playwright.dev/docs/api/class-page#page-set-extra-http-headers)로 설정된 referer 헤더 값보다 우선합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-goto-option-timeout)

최대 작업 시간(밀리초)입니다. 기본값은 `0` \- 제한 없음입니다. 기본값은 config의 `navigationTimeout` 옵션 또는 [browserContext.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

    * `waitUntil` "load" | "domcontentloaded" | "networkidle" | "commit" _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-goto-option-wait-until)

작업을 성공으로 간주할 시점이며 기본값은 `load`입니다. 이벤트는 다음 중 하나입니다:

      * `'domcontentloaded'` \- `DOMContentLoaded` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'load'` \- `load` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'networkidle'` \- **DISCOURAGED** 최소 `500` ms 동안 네트워크 연결이 없으면 작업이 완료된 것으로 간주합니다. 테스트에는 이 방법을 사용하지 말고, 준비 상태 평가는 웹 assertion에 의존하세요.
      * `'commit'` \- 네트워크 응답을 받고 문서 로딩이 시작되면 작업이 완료된 것으로 간주합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Response](https://playwright.dev/docs/api/class-response "Response")>[#](https://playwright.dev/docs/api/class-frame#frame-goto-return)

---

### isDetached[​](https://playwright.dev/docs/api/class-frame#frame-is-detached "Direct link to isDetached")

v1.9 이전에 추가됨 frame.isDetached

프레임이 분리(detached)된 경우 `true`, 아니면 `false`를 반환합니다.

**사용법**

```
    frame.isDetached();

```

**반환값**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-frame#frame-is-detached-return)

---

### isEnabled[​](https://playwright.dev/docs/api/class-frame#frame-is-enabled "Direct link to isEnabled")

v1.9 이전에 추가됨 frame.isEnabled

요소가 [enabled](https://playwright.dev/docs/actionability#enabled) 상태인지 반환합니다.

**사용법**

```
    await frame.isEnabled(selector);
    await frame.isEnabled(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-is-enabled-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-is-enabled-option-strict)

true이면 selector가 단일 요소로 resolve되어야 합니다. selector가 둘 이상의 요소로 resolve되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-is-enabled-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 제한 없음입니다. 기본값은 config의 `actionTimeout` 옵션 또는 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-frame#frame-is-enabled-return)

---

### locator[​](https://playwright.dev/docs/api/class-frame#frame-locator "Direct link to locator")

추가됨: v1.14 frame.locator

이 메서드는 이 페이지/프레임에서 동작을 수행하는 데 사용할 수 있는 element locator를 반환합니다. Locator는 동작 수행 직전에 요소로 resolve되므로, 같은 locator에 대한 일련의 동작이 실제로는 서로 다른 DOM 요소에서 수행될 수 있습니다. 이는 해당 동작들 사이에 DOM 구조가 변경되었을 때 발생합니다.

[Learn more about locators](https://playwright.dev/docs/locators).

[Learn more about locators](https://playwright.dev/docs/locators).

**사용법**

```
    frame.locator(selector);
    frame.locator(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-locator-option-selector)

DOM 요소 resolve 시 사용할 selector입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `has` [Locator](https://playwright.dev/docs/api/class-locator "Locator") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-locator-option-has)

이 상대 locator와 매칭되는 요소를 포함하는 결과만 남기도록 메서드 결과를 좁힙니다. 예를 들어 `text=Playwright`를 가진 `article`은 `<article><div>Playwright</div></article>`와 매칭됩니다.

내부 locator는 **반드시 외부 locator에 대한 상대 경로**여야 하며, 문서 루트가 아니라 외부 locator 매치 지점부터 조회됩니다. 예를 들어 `<article><content><div>Playwright</div></content></article>`에서 `div`를 가진 `content`를 찾을 수 있습니다. 하지만 `article div`를 가진 `content`를 찾는 것은 실패합니다. 내부 locator는 상대적이어야 하며 `content` 밖의 요소를 사용하면 안 되기 때문입니다.

외부 locator와 내부 locator는 같은 frame에 속해야 합니다. 내부 locator에는 [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")가 포함되면 안 됩니다.

    * `hasNot` [Locator](https://playwright.dev/docs/api/class-locator "Locator") _(optional)_ Added in: v1.33[#](https://playwright.dev/docs/api/class-frame#frame-locator-option-has-not)

내부 locator와 매칭되는 요소를 포함하지 않는 요소와 매칭됩니다. 내부 locator는 외부 locator를 기준으로 조회됩니다. 예를 들어 `div`가 없는 `article`은 `<article><span>Playwright</span></article>`와 매칭됩니다.

외부 locator와 내부 locator는 같은 frame에 속해야 합니다. 내부 locator에는 [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")가 포함되면 안 됩니다.

    * `hasNotText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_ Added in: v1.33[#](https://playwright.dev/docs/api/class-frame#frame-locator-option-has-not-text)

자식 또는 하위 요소를 포함해 내부 어딘가에 지정된 텍스트를 포함하지 않는 요소와 매칭됩니다. [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")이 전달되면 대소문자를 구분하지 않고 부분 문자열을 검색합니다.

    * `hasText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-locator-option-has-text)

자식 또는 하위 요소를 포함해 내부 어딘가에 지정된 텍스트를 포함하는 요소와 매칭됩니다. [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")이 전달되면 대소문자를 구분하지 않고 부분 문자열을 검색합니다. 예를 들어 `"Playwright"`는 `<article><div>Playwright</div></article>`와 매칭됩니다.

**반환값**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-frame#frame-locator-return)

---

### name[​](https://playwright.dev/docs/api/class-frame#frame-name "Direct link to name")

v1.9 이전에 추가됨 frame.name

태그에 지정된 프레임의 name 속성을 반환합니다.

name이 비어 있으면 대신 id 속성을 반환합니다.

note

이 값은 프레임 생성 시 한 번 계산되며, 이후 속성이 변경되어도 업데이트되지 않습니다.

**사용법**

```
    frame.name();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-name-return)

---

### page[​](https://playwright.dev/docs/api/class-frame#frame-page "Direct link to page")

v1.9 이전에 추가됨 frame.page

이 프레임을 포함하는 페이지를 반환합니다.

**사용법**

```
    frame.page();

```

**반환값**

- [Page](https://playwright.dev/docs/api/class-page "Page")[#](https://playwright.dev/docs/api/class-frame#frame-page-return)

---

### parentFrame[​](https://playwright.dev/docs/api/class-frame#frame-parent-frame "Direct link to parentFrame")

v1.9 이전에 추가됨 frame.parentFrame

상위 프레임(있는 경우)입니다. 분리된 프레임과 메인 프레임은 `null`을 반환합니다.

**사용법**

```
    frame.parentFrame();

```

**반환값**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Frame](https://playwright.dev/docs/api/class-frame "Frame")[#](https://playwright.dev/docs/api/class-frame#frame-parent-frame-return)

---

### setContent[​](https://playwright.dev/docs/api/class-frame#frame-set-content "Direct link to setContent")

v1.9 이전에 추가됨 frame.setContent

이 메서드는 내부적으로 [document.write()](https://developer.mozilla.org/en-US/docs/Web/API/Document/write)를 호출하며, 해당 메서드의 고유한 특성과 동작을 모두 상속합니다.

**사용법**

```
    await frame.setContent(html);
    await frame.setContent(html, options);

```

**인수**

- `html` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-set-content-option-html)

페이지에 할당할 HTML 마크업입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-content-option-timeout)

최대 작업 시간(밀리초)입니다. 기본값은 `0` \- 제한 없음입니다. 기본값은 config의 `navigationTimeout` 옵션 또는 [browserContext.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

    * `waitUntil` "load" | "domcontentloaded" | "networkidle" | "commit" _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-content-option-wait-until)

작업을 성공으로 간주할 시점이며 기본값은 `load`입니다. 이벤트는 다음 중 하나입니다:

      * `'domcontentloaded'` \- `DOMContentLoaded` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'load'` \- `load` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'networkidle'` \- **DISCOURAGED** 최소 `500` ms 동안 네트워크 연결이 없으면 작업이 완료된 것으로 간주합니다. 테스트에는 이 방법을 사용하지 말고, 준비 상태 평가는 웹 assertion에 의존하세요.
      * `'commit'` \- 네트워크 응답을 받고 문서 로딩이 시작되면 작업이 완료된 것으로 간주합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-set-content-return)

---

### title[​](https://playwright.dev/docs/api/class-frame#frame-title "Direct link to title")

v1.9 이전에 추가됨 frame.title

페이지 제목을 반환합니다.

**사용법**

```
    await frame.title();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-frame#frame-title-return)

---

### url[​](https://playwright.dev/docs/api/class-frame#frame-url "Direct link to url")

v1.9 이전에 추가됨 frame.url

프레임의 url을 반환합니다.

**사용법**

```
    frame.url();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-url-return)

---

### waitForFunction[​](https://playwright.dev/docs/api/class-frame#frame-wait-for-function "Direct link to waitForFunction")

v1.9 이전에 추가됨 frame.waitForFunction

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-expression)이 truthy 값을 반환하면 완료되며, 그 값을 반환합니다.

**사용법**

[frame.waitForFunction()](https://playwright.dev/docs/api/class-frame#frame-wait-for-function)을 사용해 viewport 크기 변화를 관찰할 수 있습니다:

```
    const { firefox } = require('playwright');  // Or 'chromium' or 'webkit'.

    (async () => {
      const browser = await firefox.launch();
      const page = await browser.newPage();
      const watchDog = page.mainFrame().waitForFunction('window.innerWidth < 100');
      await page.setViewportSize({ width: 50, height: 50 });
      await watchDog;
      await browser.close();
    })();

```

`frame.waitForFunction` 함수의 predicate에 인수를 전달하려면:

```
    const selector = '.foo';
    await frame.waitForFunction(selector => !!document.querySelector(selector), selector);

```

**인수**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-expression)

페이지 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-expression)에 전달할 선택적 인수입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `polling` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | "raf" _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-polling)

[polling](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-polling)이 `'raf'`이면 [pageFunction](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-expression)이 `requestAnimationFrame` 콜백에서 계속 실행됩니다. [polling](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-polling)이 숫자이면 함수 실행 간격(밀리초)으로 처리됩니다. 기본값은 `raf`입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-option-timeout)

대기할 최대 시간(밀리초)입니다. 기본값은 `0` \- 제한 없음입니다. 기본값은 config의 `actionTimeout` 옵션 또는 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-function-return)

---

### waitForLoadState[​](https://playwright.dev/docs/api/class-frame#frame-wait-for-load-state "Direct link to waitForLoadState")

v1.9 이전에 추가됨 frame.waitForLoadState

필요한 로드 상태에 도달할 때까지 기다립니다.

프레임이 필요한 로드 상태(기본값 `load`)에 도달하면 반환됩니다. 이 메서드를 호출할 때 내비게이션은 이미 commit되어 있어야 합니다. 현재 문서가 이미 필요한 상태에 도달했다면 즉시 resolve됩니다.

note

대부분의 경우 Playwright가 [모든 액션 전에 자동 대기](https://playwright.dev/docs/actionability)하므로 이 메서드는 필요하지 않습니다.

**사용법**

```
    await frame.click('button'); // Click triggers navigation.
    await frame.waitForLoadState(); // Waits for 'load' state by default.

```

**인수**

- `state` "load" | "domcontentloaded" | "networkidle" _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-load-state-option-state)

대기할 선택적 로드 상태이며 기본값은 `load`입니다. 현재 문서 로딩 중 상태가 이미 충족되었다면 메서드는 즉시 resolve됩니다. 다음 중 하나일 수 있습니다:

    * `'load'` \- `load` 이벤트가 발생할 때까지 대기합니다.
    * `'domcontentloaded'` \- `DOMContentLoaded` 이벤트가 발생할 때까지 대기합니다.
    * `'networkidle'` \- **DISCOURAGED** 최소 `500` ms 동안 네트워크 연결이 없을 때까지 대기합니다. 테스트에는 이 방법을 사용하지 말고, 준비 상태 평가는 웹 assertion에 의존하세요.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-load-state-option-timeout)

최대 작업 시간(밀리초)입니다. 기본값은 `0` \- 제한 없음입니다. 기본값은 config의 `navigationTimeout` 옵션 또는 [browserContext.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-load-state-return)

---

### waitForURL[​](https://playwright.dev/docs/api/class-frame#frame-wait-for-url "Direct link to waitForURL")

추가됨: v1.11 frame.waitForURL

프레임이 지정된 URL로 이동할 때까지 기다립니다.

**사용법**

```
    await frame.click('a.delayed-navigation'); // Clicking the link will indirectly cause a navigation
    await frame.waitForURL('**/target.html');

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([URL](https://nodejs.org/api/url.html "URL")):[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-url-option-url)

내비게이션 대기 중 매칭할 glob 패턴, 정규식 패턴 또는 [URL](https://nodejs.org/api/url.html "URL")을 받는 predicate입니다. 매개변수가 와일드카드 없는 문자열이면, 해당 문자열과 정확히 같은 URL로 내비게이션할 때까지 기다립니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-url-option-timeout)

최대 작업 시간(밀리초)입니다. 기본값은 `0` \- 제한 없음입니다. 기본값은 config의 `navigationTimeout` 옵션 또는 [browserContext.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

    * `waitUntil` "load" | "domcontentloaded" | "networkidle" | "commit" _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-url-option-wait-until)

작업을 성공으로 간주할 시점이며 기본값은 `load`입니다. 이벤트는 다음 중 하나입니다:

      * `'domcontentloaded'` \- `DOMContentLoaded` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'load'` \- `load` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'networkidle'` \- **DISCOURAGED** 최소 `500` ms 동안 네트워크 연결이 없으면 작업이 완료된 것으로 간주합니다. 테스트에는 이 방법을 사용하지 말고, 준비 상태 평가는 웹 assertion에 의존하세요.
      * `'commit'` \- 네트워크 응답을 받고 문서 로딩이 시작되면 작업이 완료된 것으로 간주합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-url-return)

---

## Deprecated[​](https://playwright.dev/docs/api/class-frame#deprecated "Direct link to Deprecated")

### $[​](https://playwright.dev/docs/api/class-frame#frame-query-selector "Direct link to $")

추가됨: v1.9 frame.$

권장되지 않음

대신 locator 기반 [frame.locator()](https://playwright.dev/docs/api/class-frame#frame-locator)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

프레임 요소를 가리키는 ElementHandle을 반환합니다.

caution

[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") 사용은 권장되지 않습니다. 대신 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 객체와 web-first assertion을 사용하세요.

이 메서드는 프레임 내에서 지정한 selector와 일치하는 요소를 찾습니다. 일치하는 요소가 없으면 `null`을 반환합니다.

**사용법**

```
    await frame.$(selector);
    await frame.$(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-query-selector-option-selector)

조회할 selector입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-query-selector-option-strict)

true이면 selector가 단일 요소로 resolve되어야 합니다. selector가 둘 이상의 요소로 resolve되면 예외를 발생시킵니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>[#](https://playwright.dev/docs/api/class-frame#frame-query-selector-return)

---

### $$[​](https://playwright.dev/docs/api/class-frame#frame-query-selector-all "Direct link to $$")

추가된 버전: v1.9 frame.$$

권장되지 않음

대신 locator 기반 [frame.locator()](https://playwright.dev/docs/api/class-frame#frame-locator)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

프레임 요소를 가리키는 ElementHandles를 반환합니다.

주의

[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")의 사용은 권장되지 않으며, 대신 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 객체를 사용하세요.

이 메서드는 프레임 내에서 지정한 selector와 일치하는 모든 요소를 찾습니다. selector와 일치하는 요소가 없으면 빈 배열을 반환합니다.

**사용법**

```
    await frame.$$(selector);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-query-selector-all-option-selector)

조회할 selector입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>>[#](https://playwright.dev/docs/api/class-frame#frame-query-selector-all-return)

---

### $eval[​](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector "Direct link to $eval")

추가된 버전: v1.9 frame.$eval

권장되지 않음

이 메서드는 요소가 actionability 검사 통과를 기다리지 않으므로 flaky 테스트로 이어질 수 있습니다. [locator.evaluate()](https://playwright.dev/docs/api/class-locator#locator-evaluate), 다른 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 헬퍼 메서드 또는 web-first assertion을 사용하세요.

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-expression)의 반환값을 반환합니다.

이 메서드는 프레임 내에서 지정한 selector와 일치하는 요소를 찾아 첫 번째 인수로 [pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-expression)에 전달합니다. selector와 일치하는 요소가 없으면 에러를 발생시킵니다.

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-expression)이 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [frame.$eval()](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector)는 해당 promise가 resolve될 때까지 기다린 뒤 값을 반환합니다.

**사용법**

```
    const searchValue = await frame.$eval('#search', el => el.value);
    const preloadHref = await frame.$eval('link[rel=preload]', el => el.href);
    const html = await frame.$eval('.main-container', (e, suffix) => e.outerHTML + suffix, 'hello');

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-selector)

조회할 selector입니다.

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([Element](https://developer.mozilla.org/en-US/docs/Web/API/element "Element")) | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-expression)

페이지 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-expression)에 전달할 선택적 인수입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-option-strict)

`true`이면 selector가 단일 요소로 해석되어야 합니다. 주어진 selector가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-return)

---

### $$eval[​](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all "Direct link to $$eval")

추가된 버전: v1.9 frame.$$eval

권장되지 않음

대부분의 경우 [locator.evaluateAll()](https://playwright.dev/docs/api/class-locator#locator-evaluate-all), 다른 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 헬퍼 메서드 및 web-first assertion이 더 적합합니다.

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-option-expression)의 반환값을 반환합니다.

이 메서드는 프레임 내에서 지정한 selector와 일치하는 모든 요소를 찾아, 일치한 요소 배열을 첫 번째 인수로 [pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-option-expression)에 전달합니다.

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-option-expression)이 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [frame.$$eval()](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all)는 해당 promise가 resolve될 때까지 기다린 뒤 값을 반환합니다.

**사용법**

```
    const divsCounts = await frame.$$eval('div', (divs, min) => divs.length >= min, 10);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-option-selector)

조회할 selector입니다.

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Element](https://developer.mozilla.org/en-US/docs/Web/API/element "Element")>) | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-option-expression)

페이지 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-frame#frame-eval-on-selector-all-return)

---

### check[​](https://playwright.dev/docs/api/class-frame#frame-check "Direct link to check")

v1.9 이전에 추가됨 frame.check

권장되지 않음

대신 locator 기반 [locator.check()](https://playwright.dev/docs/api/class-locator#locator-check)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 [selector](https://playwright.dev/docs/api/class-frame#frame-check-option-selector)와 일치하는 요소를 체크합니다.

1. [selector](https://playwright.dev/docs/api/class-frame#frame-check-option-selector)와 일치하는 요소를 찾습니다. 없으면 일치하는 요소가 DOM에 연결될 때까지 기다립니다.
2. 일치한 요소가 checkbox 또는 radio input인지 확인합니다. 아니면 이 메서드는 예외를 발생시킵니다. 요소가 이미 체크되어 있으면 즉시 반환합니다.
3. [force](https://playwright.dev/docs/api/class-frame#frame-check-option-force) 옵션이 설정되지 않았다면 일치한 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 동작을 재시도합니다.
4. 필요하면 요소를 화면에 보이도록 스크롤합니다.
5. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소의 중앙을 클릭합니다.
6. 요소가 이제 체크되었는지 확인합니다. 아니라면 이 메서드는 예외를 발생시킵니다.

모든 단계를 합친 실행이 지정된 [timeout](https://playwright.dev/docs/api/class-frame#frame-check-option-timeout) 내에 완료되지 않으면, 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이를 비활성화합니다.

**사용법**

```
    await frame.check(selector);
    await frame.check(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-check-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소를 사용합니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-check-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-check-option-no-wait-after)

사용 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-check-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding box의 왼쪽 상단 기준으로 사용할 점입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-check-option-strict)

`true`이면 selector가 단일 요소로 해석되어야 합니다. 주어진 selector가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-check-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음입니다. 기본값은 config의 `actionTimeout` 옵션 또는 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-check-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 기다리는 데 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-check-return)

---

### click[​](https://playwright.dev/docs/api/class-frame#frame-click "Direct link to click")

v1.9 이전에 추가됨 frame.click

권장되지 않음

대신 locator 기반 [locator.click()](https://playwright.dev/docs/api/class-locator#locator-click)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 [selector](https://playwright.dev/docs/api/class-frame#frame-click-option-selector)와 일치하는 요소를 클릭합니다.

1. [selector](https://playwright.dev/docs/api/class-frame#frame-click-option-selector)와 일치하는 요소를 찾습니다. 없으면 일치하는 요소가 DOM에 연결될 때까지 기다립니다.
2. [force](https://playwright.dev/docs/api/class-frame#frame-click-option-force) 옵션이 설정되지 않았다면 일치한 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 동작을 재시도합니다.
3. 필요하면 요소를 화면에 보이도록 스크롤합니다.
4. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소의 중앙 또는 지정한 [position](https://playwright.dev/docs/api/class-frame#frame-click-option-position)을 클릭합니다.
5. [noWaitAfter](https://playwright.dev/docs/api/class-frame#frame-click-option-no-wait-after) 옵션이 설정되지 않았다면, 시작된 탐색이 성공하거나 실패할 때까지 기다립니다.

모든 단계를 합친 실행이 지정된 [timeout](https://playwright.dev/docs/api/class-frame#frame-click-option-timeout) 내에 완료되지 않으면, 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이를 비활성화합니다.

**사용법**

```
    await frame.click(selector);
    await frame.click(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-click-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소를 사용합니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `button` "left" | "right" | "middle" _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-button)

기본값은 `left`입니다.

    * `clickCount` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-click-count)

기본값은 1입니다. [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail")을 참조하세요.

    * `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-delay)

`mousedown`과 `mouseup` 사이 대기 시간(밀리초)입니다. 기본값은 0입니다.

    * `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-modifiers)

누를 modifier 키입니다. 작업 중 이 modifier들만 눌리도록 보장하고, 이후 현재 modifier 상태를 복원합니다. 지정하지 않으면 현재 눌린 modifier를 사용합니다. "ControlOrMeta"는 Windows와 Linux에서는 "Control", macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-no-wait-after)

사용 중단됨

이 옵션은 앞으로 기본값이 `true`가 됩니다.

탐색을 시작하는 동작은 해당 탐색이 발생하고 페이지 로딩이 시작될 때까지 기다립니다. 이 플래그를 설정하면 대기를 건너뛸 수 있습니다. 접근할 수 없는 페이지로 이동하는 예외적인 경우에만 필요합니다. 기본값은 `false`입니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding box의 왼쪽 상단 기준으로 사용할 점입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-click-option-strict)

`true`이면 selector가 단일 요소로 해석되어야 합니다. 주어진 selector가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-click-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음입니다. 기본값은 config의 `actionTimeout` 옵션 또는 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-click-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 기다리는 데 유용합니다. `modifiers` 키를 눌렀을 때만 보이는 요소 테스트를 위해 `trial` 여부와 관계없이 키보드 `modifiers`는 눌리게 됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-click-return)

---

### dblclick[​](https://playwright.dev/docs/api/class-frame#frame-dblclick "Direct link to dblclick")

v1.9 이전에 추가됨 frame.dblclick

권장되지 않음

대신 locator 기반 [locator.dblclick()](https://playwright.dev/docs/api/class-locator#locator-dblclick)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 [selector](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-selector)와 일치하는 요소를 더블클릭합니다.

1. [selector](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-selector)와 일치하는 요소를 찾습니다. 없으면 일치하는 요소가 DOM에 연결될 때까지 기다립니다.
2. [force](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-force) 옵션이 설정되지 않았다면 일치한 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 동작을 재시도합니다.
3. 필요하면 요소를 화면에 보이도록 스크롤합니다.
4. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소의 중앙 또는 지정한 [position](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-position)을 더블클릭합니다. `dblclick()`의 첫 번째 클릭이 탐색 이벤트를 트리거하면 이 메서드는 예외를 발생시킵니다.

모든 단계를 합친 실행이 지정된 [timeout](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-timeout) 내에 완료되지 않으면, 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이를 비활성화합니다.

참고

`frame.dblclick()`은 두 개의 `click` 이벤트와 하나의 `dblclick` 이벤트를 디스패치합니다.

**사용법**

```
    await frame.dblclick(selector);
    await frame.dblclick(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소를 사용합니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `button` "left" | "right" | "middle" _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-button)

기본값은 `left`입니다.

    * `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-delay)

`mousedown`과 `mouseup` 사이 대기 시간(밀리초)입니다. 기본값은 0입니다.

    * `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-modifiers)

누를 modifier 키입니다. 작업 중 이 modifier들만 눌리도록 보장하고, 이후 현재 modifier 상태를 복원합니다. 지정하지 않으면 현재 눌린 modifier를 사용합니다. "ControlOrMeta"는 Windows와 Linux에서는 "Control", macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-no-wait-after)

사용 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding box의 왼쪽 상단 기준으로 사용할 점입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-strict)

`true`이면 selector가 단일 요소로 해석되어야 합니다. 주어진 selector가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음입니다. 기본값은 config의 `actionTimeout` 옵션 또는 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 기다리는 데 유용합니다. `modifiers` 키를 눌렀을 때만 보이는 요소 테스트를 위해 `trial` 여부와 관계없이 키보드 `modifiers`는 눌리게 됩니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-dblclick-return)

---

### dispatchEvent[​](https://playwright.dev/docs/api/class-frame#frame-dispatch-event "Direct link to dispatchEvent")

v1.9 이전에 추가됨 frame.dispatchEvent

권장되지 않음

대신 locator 기반 [locator.dispatchEvent()](https://playwright.dev/docs/api/class-locator#locator-dispatch-event)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

아래 스니펫은 요소에 `click` 이벤트를 디스패치합니다. 요소의 가시성 상태와 무관하게 `click`이 디스패치됩니다. 이는 [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)을 호출하는 것과 동일합니다.

**사용법**

```
    await frame.dispatchEvent('button#submit', 'click');

```

내부적으로는 주어진 [type](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-type)에 따라 이벤트 인스턴스를 생성하고, [eventInit](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-event-init) 속성으로 초기화한 뒤 요소에 디스패치합니다. 이벤트는 기본적으로 `composed`, `cancelable`이며 버블링됩니다.

[eventInit](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-event-init)은 이벤트별로 다르므로, 초기 속성 목록은 이벤트 문서를 참조하세요.

- [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/DeviceMotionEvent)
- [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/DeviceOrientationEvent)
- [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
- [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)
- [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
- [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
- [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
- [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
- [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
- [WheelEvent](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/WheelEvent)

이벤트에 라이브 객체를 전달하려면 속성 값으로 `JSHandle`을 지정할 수도 있습니다.

```
    // Note you can only create DataTransfer in Chromium and Firefox
    const dataTransfer = await frame.evaluateHandle(() => new DataTransfer());
    await frame.dispatchEvent('#source', 'dragstart', { dataTransfer });

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소를 사용합니다.

- `type` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-type)

DOM 이벤트 타입: `"click"`, `"dragstart"` 등.

- `eventInit` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-event-init)

선택적 이벤트별 초기화 속성입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-strict)

`true`이면 selector가 단일 요소로 해석되어야 합니다. 주어진 selector가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-dispatch-event-return)

---

### fill[​](https://playwright.dev/docs/api/class-frame#frame-fill "Direct link to fill")

v1.9 이전에 추가됨 frame.fill

권장되지 않음

대신 locator 기반 [locator.fill()](https://playwright.dev/docs/api/class-locator#locator-fill)을 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

이 메서드는 [selector](https://playwright.dev/docs/api/class-frame#frame-fill-option-selector)와 일치하는 요소를 기다리고, [actionability](https://playwright.dev/docs/actionability) 검사를 기다린 뒤, 요소에 포커스를 주고 값을 채운 다음 `input` 이벤트를 트리거합니다. 입력 필드를 비우려면 빈 문자열을 전달할 수 있습니다.

대상 요소가 `<input>`, `<textarea>`, `[contenteditable]` 요소가 아니면 이 메서드는 오류를 발생시킵니다. 다만 요소가 연결된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)을 가진 `<label>` 요소 내부에 있으면, 대신 해당 control이 채워집니다.

세밀한 키보드 이벤트를 전송하려면 [locator.pressSequentially()](https://playwright.dev/docs/api/class-locator#locator-press-sequentially)를 사용하세요.

**사용법**

```
    await frame.fill(selector, value);
    await frame.fill(selector, value, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-fill-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-fill-option-value)

`<input>`, `<textarea>`, `[contenteditable]` 요소에 채울 값입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.13[#](https://playwright.dev/docs/api/class-frame#frame-fill-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 건너뛸지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-fill-option-no-wait-after)

사용 중단됨

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-fill-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-fill-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-fill-return)

---

### focus[​](https://playwright.dev/docs/api/class-frame#frame-focus "Direct link to focus")

v1.9 이전에 추가됨 frame.focus

권장되지 않음

대신 locator 기반 [locator.focus()](https://playwright.dev/docs/api/class-locator#locator-focus)을 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

이 메서드는 [selector](https://playwright.dev/docs/api/class-frame#frame-focus-option-selector)로 요소를 가져와 포커스를 맞춥니다. [selector](https://playwright.dev/docs/api/class-frame#frame-focus-option-selector)와 일치하는 요소가 없으면 DOM에 일치하는 요소가 나타날 때까지 기다립니다.

**사용법**

```
    await frame.focus(selector);
    await frame.focus(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-focus-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-focus-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-focus-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-focus-return)

---

### getAttribute[​](https://playwright.dev/docs/api/class-frame#frame-get-attribute "Direct link to getAttribute")

v1.9 이전에 추가됨 frame.getAttribute

권장되지 않음

대신 locator 기반 [locator.getAttribute()](https://playwright.dev/docs/api/class-locator#locator-get-attribute)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

요소의 attribute 값을 반환합니다.

**사용법**

```
    await frame.getAttribute(selector, name);
    await frame.getAttribute(selector, name, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-get-attribute-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-get-attribute-option-name)

값을 가져올 attribute 이름입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-get-attribute-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-get-attribute-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-frame#frame-get-attribute-return)

---

### hover[​](https://playwright.dev/docs/api/class-frame#frame-hover "Direct link to hover")

v1.9 이전에 추가됨 frame.hover

권장되지 않음

대신 locator 기반 [locator.hover()](https://playwright.dev/docs/api/class-locator#locator-hover)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

이 메서드는 다음 단계를 수행하여 [selector](https://playwright.dev/docs/api/class-frame#frame-hover-option-selector)와 일치하는 요소 위로 hover합니다.

1. [selector](https://playwright.dev/docs/api/class-frame#frame-hover-option-selector)와 일치하는 요소를 찾습니다. 없으면 일치하는 요소가 DOM에 연결될 때까지 기다립니다.
2. [force](https://playwright.dev/docs/api/class-frame#frame-hover-option-force) 옵션이 설정되지 않은 경우, 일치한 요소에 대해 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 동작을 다시 시도합니다.
3. 필요하면 요소를 화면에 보이도록 스크롤합니다.
4. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소의 중앙 또는 지정된 [position](https://playwright.dev/docs/api/class-frame#frame-hover-option-position) 위로 hover합니다.

지정된 [timeout](https://playwright.dev/docs/api/class-frame#frame-hover-option-timeout) 내에 모든 단계를 완료하지 못하면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이를 비활성화합니다.

**사용법**

```
    await frame.hover(selector);
    await frame.hover(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 건너뛸지 여부입니다. 기본값은 `false`입니다.

    * `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-modifiers)

누를 modifier 키입니다. 작업 중에는 이 modifier만 눌리도록 보장하고, 이후 현재 modifier 상태를 복원합니다. 지정하지 않으면 현재 눌린 modifier가 사용됩니다. "ControlOrMeta"는 Windows와 Linux에서는 "Control", macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.28[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-no-wait-after)

사용 중단됨

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 패딩 박스의 왼쪽 위 모서리를 기준으로 사용할 좌표입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-hover-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 실제 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 준비될 때까지 기다릴 때 유용합니다. `trial`과 관계없이, 해당 키를 눌렀을 때만 보이는 요소를 테스트할 수 있도록 키보드 `modifiers`는 눌립니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-hover-return)

---

### innerHTML[​](https://playwright.dev/docs/api/class-frame#frame-inner-html "Direct link to innerHTML")

v1.9 이전에 추가됨 frame.innerHTML

권장되지 않음

대신 locator 기반 [locator.innerHTML()](https://playwright.dev/docs/api/class-locator#locator-inner-html)을 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

`element.innerHTML`을 반환합니다.

**사용법**

```
    await frame.innerHTML(selector);
    await frame.innerHTML(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-inner-html-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-inner-html-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-inner-html-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-frame#frame-inner-html-return)

---

### innerText[​](https://playwright.dev/docs/api/class-frame#frame-inner-text "Direct link to innerText")

v1.9 이전에 추가됨 frame.innerText

권장되지 않음

대신 locator 기반 [locator.innerText()](https://playwright.dev/docs/api/class-locator#locator-inner-text)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

`element.innerText`를 반환합니다.

**사용법**

```
    await frame.innerText(selector);
    await frame.innerText(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-inner-text-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-inner-text-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-inner-text-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-frame#frame-inner-text-return)

---

### inputValue[​](https://playwright.dev/docs/api/class-frame#frame-input-value "Direct link to inputValue")

추가됨: v1.13 frame.inputValue

권장되지 않음

대신 locator 기반 [locator.inputValue()](https://playwright.dev/docs/api/class-locator#locator-input-value)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

선택된 `<input>`, `<textarea>`, `<select>` 요소의 `input.value`를 반환합니다.

입력 요소가 아니면 예외를 발생시킵니다. 다만 요소가 연결된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)을 가진 `<label>` 요소 내부에 있으면, 해당 control의 값을 반환합니다.

**사용법**

```
    await frame.inputValue(selector);
    await frame.inputValue(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-input-value-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-input-value-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-input-value-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-frame#frame-input-value-return)

---

### isChecked[​](https://playwright.dev/docs/api/class-frame#frame-is-checked "Direct link to isChecked")

v1.9 이전에 추가됨 frame.isChecked

권장되지 않음

대신 locator 기반 [locator.isChecked()](https://playwright.dev/docs/api/class-locator#locator-is-checked)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

요소가 체크되었는지 여부를 반환합니다. 요소가 체크박스 또는 라디오 입력이 아니면 예외를 발생시킵니다.

**사용법**

```
    await frame.isChecked(selector);
    await frame.isChecked(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-is-checked-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-is-checked-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-is-checked-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-frame#frame-is-checked-return)

---

### isDisabled[​](https://playwright.dev/docs/api/class-frame#frame-is-disabled "Direct link to isDisabled")

v1.9 이전에 추가됨 frame.isDisabled

권장되지 않음

대신 locator 기반 [locator.isDisabled()](https://playwright.dev/docs/api/class-locator#locator-is-disabled)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

요소가 비활성화되었는지 여부를 반환하며, [enabled](https://playwright.dev/docs/actionability#enabled)의 반대입니다.

**사용법**

```
    await frame.isDisabled(selector);
    await frame.isDisabled(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-is-disabled-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-is-disabled-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-is-disabled-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-frame#frame-is-disabled-return)

---

### isEditable[​](https://playwright.dev/docs/api/class-frame#frame-is-editable "Direct link to isEditable")

v1.9 이전에 추가됨 frame.isEditable

권장되지 않음

대신 locator 기반 [locator.isEditable()](https://playwright.dev/docs/api/class-locator#locator-is-editable)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

요소가 [editable](https://playwright.dev/docs/actionability#editable) 상태인지 여부를 반환합니다.

**사용법**

```
    await frame.isEditable(selector);
    await frame.isEditable(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-is-editable-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-is-editable-option-strict)

true이면 selector가 단일 요소로 확인되어야 합니다. 제공된 selector가 둘 이상의 요소로 확인되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-is-editable-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-frame#frame-is-editable-return)

---

### isHidden[​](https://playwright.dev/docs/api/class-frame#frame-is-hidden "Direct link to isHidden")

v1.9 이전에 추가됨 frame.isHidden

권장되지 않음

대신 locator 기반 [locator.isHidden()](https://playwright.dev/docs/api/class-locator#locator-is-hidden)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

요소가 숨겨져 있는지 여부를 반환하며, [visible](https://playwright.dev/docs/actionability#visible)의 반대입니다. 어떤 요소와도 일치하지 않는 [selector](https://playwright.dev/docs/api/class-frame#frame-is-hidden-option-selector)는 숨김으로 간주됩니다.

**사용법**

```
    await frame.isHidden(selector);
    await frame.isHidden(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-is-hidden-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-is-hidden-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-is-hidden-option-timeout)

지원 중단됨

이 옵션은 무시됩니다. [frame.isHidden()](https://playwright.dev/docs/api/class-frame#frame-is-hidden)은 요소가 숨겨질 때까지 대기하지 않으며 즉시 반환합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-frame#frame-is-hidden-return)

---

### isVisible[​](https://playwright.dev/docs/api/class-frame#frame-is-visible "Direct link to isVisible")

v1.9 이전에 추가됨 frame.isVisible

권장되지 않음

대신 locator 기반 [locator.isVisible()](https://playwright.dev/docs/api/class-locator#locator-is-visible)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소가 [visible](https://playwright.dev/docs/actionability#visible) 상태인지 반환합니다. 어떤 요소와도 일치하지 않는 [selector](https://playwright.dev/docs/api/class-frame#frame-is-visible-option-selector)는 보이지 않는 것으로 간주됩니다.

**사용법**

```
    await frame.isVisible(selector);
    await frame.isVisible(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-is-visible-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개라면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-is-visible-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-is-visible-option-timeout)

지원 중단됨

이 옵션은 무시됩니다. [frame.isVisible()](https://playwright.dev/docs/api/class-frame#frame-is-visible)은 요소가 보이게 될 때까지 대기하지 않으며 즉시 반환합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-frame#frame-is-visible-return)

---

### press[​](https://playwright.dev/docs/api/class-frame#frame-press "Direct link to press")

v1.9 이전에 추가됨 frame.press

권장되지 않음

대신 locator 기반 [locator.press()](https://playwright.dev/docs/api/class-locator#locator-press)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

[key](https://playwright.dev/docs/api/class-frame#frame-press-option-key)는 의도한 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 값을 지정하거나 텍스트를 생성할 단일 문자를 지정할 수 있습니다. [key](https://playwright.dev/docs/api/class-frame#frame-press-option-key) 값의 상위 집합은 [여기](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values)에서 확인할 수 있습니다. 키 예시는 다음과 같습니다.

`F1` \- `F12`, `Digit0`\- `Digit9`, `KeyA`\- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp` 등.

다음 수정 키 단축키도 지원됩니다: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta`는 Windows와 Linux에서는 `Control`, macOS에서는 `Meta`로 해석됩니다.

`Shift`를 누른 상태로 유지하면 [key](https://playwright.dev/docs/api/class-frame#frame-press-option-key)에 해당하는 텍스트가 대문자로 입력됩니다.

[key](https://playwright.dev/docs/api/class-frame#frame-press-option-key)가 단일 문자이면 대소문자를 구분하므로 `a`와 `A`는 각각 다른 텍스트를 생성합니다.

`key: "Control+o"`, `key: "Control++` 또는 `key: "Control+Shift+T"` 같은 단축키도 지원됩니다. 수정 키와 함께 지정하면, 이후 키를 누르는 동안 수정 키가 눌린 채 유지됩니다.

**사용법**

```
    await frame.press(selector, key);
    await frame.press(selector, key, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-press-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개라면 첫 번째 요소가 사용됩니다.

- `key` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-press-option-key)

누를 키 이름 또는 생성할 문자(예: `ArrowLeft`, `a`)입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-press-option-delay)

`keydown`과 `keyup` 사이에 대기할 시간(밀리초)입니다. 기본값은 `0`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-press-option-no-wait-after)

지원 중단됨

이 옵션의 기본값은 향후 `true`가 됩니다.

탐색을 시작하는 액션은 해당 탐색이 발생하고 페이지 로딩이 시작될 때까지 대기합니다. 이 플래그를 설정하면 대기를 건너뛸 수 있습니다. 접근 불가능한 페이지로 이동하는 예외적인 경우에만 이 옵션이 필요합니다. 기본값은 `false`입니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-press-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-press-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-press-return)

---

### selectOption[​](https://playwright.dev/docs/api/class-frame#frame-select-option "Direct link to selectOption")

v1.9 이전에 추가됨 frame.selectOption

권장되지 않음

대신 locator 기반 [locator.selectOption()](https://playwright.dev/docs/api/class-locator#locator-select-option)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 [selector](https://playwright.dev/docs/api/class-frame#frame-select-option-option-selector)와 일치하는 요소를 기다리고, [actionability](https://playwright.dev/docs/actionability) 검사를 기다리며, 지정된 모든 옵션이 `<select>` 요소에 존재할 때까지 기다린 후 해당 옵션들을 선택합니다.

대상 요소가 `<select>` 요소가 아니면 이 메서드는 오류를 발생시킵니다. 단, 요소가 연관된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)을 가진 `<label>` 요소 내부에 있으면 대신 그 control을 사용합니다.

성공적으로 선택된 옵션 값의 배열을 반환합니다.

제공된 모든 옵션이 선택되면 `change` 및 `input` 이벤트를 트리거합니다.

**사용법**

```
    // Single selection matching the value or label
    frame.selectOption('select#colors', 'blue');

    // single selection matching both the value and the label
    frame.selectOption('select#colors', { label: 'Blue' });

    // multiple selection
    frame.selectOption('select#colors', 'red', 'green', 'blue');

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-select-option-option-selector)

조회할 selector입니다.

- `values` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")> | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-frame#frame-select-option-option-values)
  - `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

`option.value`로 일치시킵니다. 선택 사항입니다.

    * `label` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

`option.label`로 일치시킵니다. 선택 사항입니다.

    * `index` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

인덱스로 일치시킵니다. 선택 사항입니다.

선택할 옵션입니다. `<select>`에 `multiple` 속성이 있으면 일치하는 모든 옵션을 선택하고, 그렇지 않으면 전달된 옵션 중 하나와 일치하는 첫 번째 옵션만 선택합니다. 문자열 값은 value와 label 모두에 대해 일치합니다. 지정된 모든 속성이 일치하면 옵션이 일치하는 것으로 간주됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.13[#](https://playwright.dev/docs/api/class-frame#frame-select-option-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-select-option-option-no-wait-after)

지원 중단됨

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-select-option-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-select-option-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>>[#](https://playwright.dev/docs/api/class-frame#frame-select-option-return)

---

### setChecked[​](https://playwright.dev/docs/api/class-frame#frame-set-checked "Direct link to setChecked")

v1.15에 추가됨 frame.setChecked

권장되지 않음

대신 locator 기반 [locator.setChecked()](https://playwright.dev/docs/api/class-locator#locator-set-checked)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 [selector](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-selector)와 일치하는 요소를 체크하거나 체크 해제합니다.

1. [selector](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-selector)와 일치하는 요소를 찾습니다. 없으면 일치하는 요소가 DOM에 연결될 때까지 기다립니다.
2. 일치한 요소가 체크박스 또는 라디오 input인지 확인합니다. 아니면 이 메서드는 예외를 발생시킵니다.
3. 요소가 이미 올바른 체크 상태이면 이 메서드는 즉시 반환합니다.
4. [force](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-force) 옵션이 설정되지 않았다면, 일치한 요소에 대해 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 작업을 재시도합니다.
5. 필요하면 요소를 화면에 스크롤합니다.
6. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소 중앙을 클릭합니다.
7. 요소가 이제 체크 또는 체크 해제 상태인지 확인합니다. 아니면 이 메서드는 예외를 발생시킵니다.

모든 단계를 합친 실행이 지정된 [timeout](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-timeout) 내에 끝나지 않으면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이 기능이 비활성화됩니다.

**사용법**

```
    await frame.setChecked(selector, checked);
    await frame.setChecked(selector, checked, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개라면 첫 번째 요소가 사용됩니다.

- `checked` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-checked)

체크박스를 체크할지 또는 체크 해제할지 여부입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-no-wait-after)

지원 중단됨

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding box의 좌상단 모서리를 기준으로 사용할 점입니다. 지정하지 않으면 요소의 보이는 점 중 하나를 사용합니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 실제 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 기다리는 데 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-set-checked-return)

---

### setInputFiles[​](https://playwright.dev/docs/api/class-frame#frame-set-input-files "Direct link to setInputFiles")

v1.9 이전에 추가됨 frame.setInputFiles

권장되지 않음

대신 locator 기반 [locator.setInputFiles()](https://playwright.dev/docs/api/class-locator#locator-set-input-files)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

파일 input의 값을 이 파일 경로 또는 파일들로 설정합니다. `filePaths` 중 일부가 상대 경로라면 현재 작업 디렉터리를 기준으로 해석됩니다. 빈 배열이면 선택된 파일을 지웁니다.

이 메서드는 [selector](https://playwright.dev/docs/api/class-frame#frame-set-input-files-option-selector)가 [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)를 가리킨다고 가정합니다. 단, 요소가 연관된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)을 가진 `<label>` 요소 내부에 있으면 대신 그 control을 대상으로 합니다.

**사용법**

```
    await frame.setInputFiles(selector, files);
    await frame.setInputFiles(selector, files, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-set-input-files-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개라면 첫 번째 요소가 사용됩니다.

- `files` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-frame#frame-set-input-files-option-files)
  - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

    * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 형식

    * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-input-files-option-no-wait-after)

지원 중단됨

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-set-input-files-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-set-input-files-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-set-input-files-return)

---

### tap[​](https://playwright.dev/docs/api/class-frame#frame-tap "Direct link to tap")

v1.9 이전에 추가됨 frame.tap

권장되지 않음

대신 locator 기반 [locator.tap()](https://playwright.dev/docs/api/class-locator#locator-tap)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 [selector](https://playwright.dev/docs/api/class-frame#frame-tap-option-selector)와 일치하는 요소를 탭합니다.

1. [selector](https://playwright.dev/docs/api/class-frame#frame-tap-option-selector)와 일치하는 요소를 찾습니다. 없으면 일치하는 요소가 DOM에 연결될 때까지 기다립니다.
2. [force](https://playwright.dev/docs/api/class-frame#frame-tap-option-force) 옵션이 설정되지 않았다면, 일치한 요소에 대해 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 작업을 재시도합니다.
3. 필요하면 요소를 화면에 스크롤합니다.
4. [page.touchscreen](https://playwright.dev/docs/api/class-page#page-touchscreen)을 사용해 요소 중앙 또는 지정된 [position](https://playwright.dev/docs/api/class-frame#frame-tap-option-position)을 탭합니다.

모든 단계를 합친 실행이 지정된 [timeout](https://playwright.dev/docs/api/class-frame#frame-tap-option-timeout) 내에 끝나지 않으면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이 기능이 비활성화됩니다.

참고

`frame.tap()`을 사용하려면 browser context의 `hasTouch` 옵션이 `true`로 설정되어 있어야 합니다.

**사용법**

```
    await frame.tap(selector);
    await frame.tap(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개라면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-modifiers)

누를 modifier 키입니다. 작업 중에는 이 modifier만 눌리도록 보장한 뒤, 완료 후 현재 modifier 상태를 복원합니다. 지정하지 않으면 현재 눌린 modifier를 사용합니다. "ControlOrMeta"는 Windows와 Linux에서는 "Control", macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-no-wait-after)

지원 중단됨

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding box의 좌상단 모서리를 기준으로 사용할 점입니다. 지정하지 않으면 요소의 보이는 점 중 하나를 사용합니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-tap-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 실제 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 기다리는 데 유용합니다. `trial`과 관계없이 keyboard `modifiers`는 눌리는데, 이는 해당 키를 눌렀을 때만 보이는 요소를 테스트할 수 있게 하기 위함입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-tap-return)

---

### textContent[​](https://playwright.dev/docs/api/class-frame#frame-text-content "Direct link to textContent")

v1.9 이전에 추가됨 frame.textContent

권장되지 않음

대신 locator 기반 [locator.textContent()](https://playwright.dev/docs/api/class-locator#locator-text-content)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

`element.textContent`를 반환합니다.

**사용법**

```
    await frame.textContent(selector);
    await frame.textContent(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-text-content-option-selector)

요소를 찾기 위한 selector입니다. selector를 만족하는 요소가 여러 개라면 첫 번째 요소가 사용됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-text-content-option-strict)

`true`이면 호출에서 selector가 단일 요소로 해석되어야 합니다. 지정된 selector가 둘 이상의 요소로 해석되면 호출은 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-frame#frame-text-content-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`으로, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 통해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-frame#frame-text-content-return)

---

### type[​](https://playwright.dev/docs/api/class-frame#frame-type "Direct link to type")

v1.9 이전에 추가됨 frame.type

지원 중단(Deprecated)

대부분의 경우 대신 [locator.fill()](https://playwright.dev/docs/api/class-locator#locator-fill)을 사용해야 합니다. 페이지에 특수한 키보드 처리 로직이 있을 때만 키를 하나씩 눌러야 하며, 이 경우 [locator.pressSequentially()](https://playwright.dev/docs/api/class-locator#locator-press-sequentially)를 사용하세요.

텍스트의 각 문자마다 `keydown`, `keypress`/`input`, `keyup` 이벤트를 전송합니다. `frame.type`은 세밀한 키보드 이벤트를 전송할 때 사용할 수 있습니다. 폼 필드에 값을 채우려면 [frame.fill()](https://playwright.dev/docs/api/class-frame#frame-fill)을 사용하세요.

`Control`이나 `ArrowDown` 같은 특수 키를 누르려면 [keyboard.press()](https://playwright.dev/docs/api/class-keyboard#keyboard-press)를 사용하세요.

**사용법**

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-type-option-selector)

요소를 찾기 위한 선택자입니다. 선택자에 일치하는 요소가 여러 개면 첫 번째 요소를 사용합니다.

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-type-option-text)

포커스된 요소에 입력할 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-type-option-delay)

키 입력 사이에 대기할 시간(밀리초)입니다. 기본값은 0입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-type-option-no-wait-after)

지원 중단(Deprecated)

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-type-option-strict)

true이면 호출 시 선택자가 단일 요소로 해석되어야 합니다. 전달된 선택자가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-type-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`으로, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 통해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-type-return)

---

### uncheck[​](https://playwright.dev/docs/api/class-frame#frame-uncheck "Direct link to uncheck")

v1.9 이전에 추가됨 frame.uncheck

권장되지 않음(Discouraged)

대신 locator 기반 [locator.uncheck()](https://playwright.dev/docs/api/class-locator#locator-uncheck)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

이 메서드는 [selector](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-selector)에 일치하는 요소를 대상으로 다음 단계를 수행해 체크를 해제합니다.

1. [selector](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-selector)에 일치하는 요소를 찾습니다. 없으면 일치하는 요소가 DOM에 연결될 때까지 대기합니다.
2. 일치한 요소가 체크박스 또는 라디오 input인지 확인합니다. 아니면 이 메서드는 예외를 발생시킵니다. 요소가 이미 체크 해제된 상태면 즉시 반환합니다.
3. [force](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-force) 옵션이 설정되지 않은 경우, 일치한 요소에 대해 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 동작을 재시도합니다.
4. 필요하면 요소를 화면에 보이도록 스크롤합니다.
5. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소 중앙을 클릭합니다.
6. 요소가 이제 체크 해제되었는지 확인합니다. 아니라면 이 메서드는 예외를 발생시킵니다.

모든 단계를 합친 실행이 지정된 [timeout](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-timeout) 내에 끝나지 않으면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이를 비활성화합니다.

**사용법**

```
    await frame.uncheck(selector);
    await frame.uncheck(selector, options);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-selector)

요소를 찾기 위한 선택자입니다. 선택자에 일치하는 요소가 여러 개면 첫 번째 요소를 사용합니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-no-wait-after)

지원 중단(Deprecated)

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding box의 왼쪽 위 모서리를 기준으로 사용할 좌표입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-strict)

true이면 호출 시 선택자가 단일 요소로 해석되어야 합니다. 전달된 선택자가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`으로, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 통해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 기다릴 때 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-uncheck-return)

---

### waitForNavigation[​](https://playwright.dev/docs/api/class-frame#frame-wait-for-navigation "Direct link to waitForNavigation")

v1.9 이전에 추가됨 frame.waitForNavigation

지원 중단(Deprecated)

이 메서드는 본질적으로 레이스 컨디션에 취약하므로, 대신 [frame.waitForURL()](https://playwright.dev/docs/api/class-frame#frame-wait-for-url)을 사용하세요.

프레임의 navigation을 기다린 뒤 메인 리소스 응답을 반환합니다. 리디렉션이 여러 번 발생하면 마지막 리디렉션의 응답으로 resolve됩니다. 다른 앵커로 이동하거나 History API 사용으로 인한 navigation의 경우 `null`로 resolve됩니다.

**사용법**

이 메서드는 프레임이 새 URL로 navigation할 때까지 기다립니다. 프레임 navigation을 간접적으로 유발하는 코드를 실행할 때 유용합니다. 다음 예시를 보세요:

```
    // Start waiting for navigation before clicking. Note no await.
    const navigationPromise = page.waitForNavigation();
    await page.getByText('Navigate after timeout').click();
    await navigationPromise;

```

note

URL을 변경하기 위해 [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API)를 사용하는 것도 navigation으로 간주됩니다.

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-navigation-option-timeout)

최대 작업 시간(밀리초)입니다. 기본값은 `0`으로, 타임아웃이 없습니다. 기본값은 config의 `navigationTimeout` 옵션이나 [browserContext.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 통해 변경할 수 있습니다.

    * `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([URL](https://nodejs.org/api/url.html "URL")):[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-navigation-option-url)

navigation을 기다리는 동안 매칭할 대상 URL을 지정하는 glob 패턴, regex 패턴 또는 [URL](https://nodejs.org/api/url.html "URL")을 받는 predicate입니다. 매개변수가 와일드카드 문자가 없는 문자열인 경우, 메서드는 해당 문자열과 정확히 같은 URL로 navigation할 때까지 기다립니다.

    * `waitUntil` "load" | "domcontentloaded" | "networkidle" | "commit" _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-navigation-option-wait-until)

작업 성공으로 간주할 시점을 지정하며 기본값은 `load`입니다. 이벤트는 다음 중 하나입니다.

      * `'domcontentloaded'` \- `DOMContentLoaded` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'load'` \- `load` 이벤트가 발생하면 작업이 완료된 것으로 간주합니다.
      * `'networkidle'` \- **권장되지 않음(DISCOURAGED)** 최소 `500`ms 동안 네트워크 연결이 없으면 작업이 완료된 것으로 간주합니다. 테스트에는 이 방법을 사용하지 말고, 대신 준비 상태 평가는 웹 assertion에 의존하세요.
      * `'commit'` \- 네트워크 응답을 수신하고 문서 로딩이 시작되면 작업이 완료된 것으로 간주합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Response](https://playwright.dev/docs/api/class-response "Response")>[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-navigation-return)

---

### waitForSelector[​](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector "Direct link to waitForSelector")

v1.9 이전에 추가됨 frame.waitForSelector

권장되지 않음(Discouraged)

대신 가시성을 검증하는 웹 assertion 또는 locator 기반 [locator.waitFor()](https://playwright.dev/docs/api/class-locator#locator-wait-for)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

선택자로 지정된 요소가 [state](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-state) 옵션을 만족하면 반환합니다. `hidden` 또는 `detached`를 기다리는 경우 `null`을 반환합니다.

note

Playwright는 동작을 수행하기 전에 요소가 준비될 때까지 자동으로 대기합니다. [Locator](https://playwright.dev/docs/api/class-locator "Locator") 객체와 web-first assertion을 사용하면 wait-for-selector가 없는 코드를 만들 수 있습니다.

[selector](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-selector)가 [state](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-state) 옵션(예: dom에 나타남/사라짐, 또는 visible/hidden 상태 전환)을 만족할 때까지 기다립니다. 메서드 호출 시점에 [selector](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-selector)가 이미 조건을 만족하면 즉시 반환합니다. 선택자가 [timeout](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-timeout) 밀리초 동안 조건을 만족하지 않으면 함수는 예외를 발생시킵니다.

**사용법**

이 메서드는 navigation 전반에서 동작합니다:

```
    const { chromium } = require('playwright');  // Or 'firefox' or 'webkit'.

    (async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      for (const currentURL of ['https://google.com', 'https://bbc.com']) {
        await page.goto(currentURL);
        const element = await page.mainFrame().waitForSelector('img');
        console.log('Loaded image: ' + await element.getAttribute('src'));
      }
      await browser.close();
    })();

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-selector)

조회할 선택자입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `state` "attached" | "detached" | "visible" | "hidden" _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-state)

기본값은 `'visible'`입니다. 다음 중 하나를 사용할 수 있습니다.

      * `'attached'` \- 요소가 DOM에 존재할 때까지 기다립니다.
      * `'detached'` \- 요소가 DOM에 존재하지 않을 때까지 기다립니다.
      * `'visible'` \- 요소가 비어 있지 않은 bounding box를 가지고 `visibility:hidden`이 아닐 때까지 기다립니다. 콘텐츠가 없거나 `display:none`인 요소는 bounding box가 비어 있으므로 visible로 간주되지 않습니다.
      * `'hidden'` \- 요소가 DOM에서 분리되었거나, bounding box가 비어 있거나, `visibility:hidden`일 때까지 기다립니다. 이는 `'visible'` 옵션의 반대입니다.
    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ 추가된 버전: v1.14[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-strict)

true이면 호출 시 선택자가 단일 요소로 해석되어야 합니다. 전달된 선택자가 둘 이상의 요소로 해석되면 예외를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`으로, 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 통해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector-return)

---

### waitForTimeout[​](https://playwright.dev/docs/api/class-frame#frame-wait-for-timeout "Direct link to waitForTimeout")

v1.9 이전에 추가됨 frame.waitForTimeout

권장되지 않음(Discouraged)

프로덕션에서는 절대 timeout 대기를 사용하지 마세요. 시간 대기에 의존하는 테스트는 본질적으로 flaky합니다. 자동 대기하는 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 동작과 웹 assertion을 사용하세요.

주어진 [timeout](https://playwright.dev/docs/api/class-frame#frame-wait-for-timeout-option-timeout)(밀리초) 동안 대기합니다.

`frame.waitForTimeout()`은 디버깅 용도로만 사용해야 합니다. 프로덕션에서 타이머를 사용하는 테스트는 flaky해집니다. 대신 네트워크 이벤트, 선택자의 visible 상태 전환 같은 신호를 사용하세요.

**사용법**

```
    await frame.waitForTimeout(timeout);

```

**인수**

- `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-timeout-option-timeout)

대기할 timeout 값

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-frame#frame-wait-for-timeout-return)
