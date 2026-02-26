---
title: "ElementHandle"
description: "ElementHandle는 페이지 내 DOM 요소를 나타냅니다. ElementHandle은 page.$() 메서드로 생성할 수 있습니다."
---

Source URL: https://playwright.dev/docs/api/class-elementhandle

# ElementHandle | Playwright

- 확장: [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")

ElementHandle는 페이지 내 DOM 요소를 나타냅니다. ElementHandle은 [page.$()](https://playwright.dev/docs/api/class-page#page-query-selector) 메서드로 생성할 수 있습니다.

권장되지 않음

ElementHandle 사용은 권장되지 않습니다. 대신 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 객체와 웹 우선 assertion을 사용하세요.

```
    const hrefElement = await page.$('a');
    await hrefElement.click();

```

ElementHandle은 [jsHandle.dispose()](https://playwright.dev/docs/api/class-jshandle#js-handle-dispose)로 핸들을 해제하지 않는 한 DOM 요소가 가비지 컬렉션되지 않도록 막습니다. ElementHandle은 원본 프레임이 탐색되면 자동으로 해제됩니다.

ElementHandle 인스턴스는 [page.$eval()](https://playwright.dev/docs/api/class-page#page-eval-on-selector) 및 [page.evaluate()](https://playwright.dev/docs/api/class-page#page-evaluate) 메서드의 인수로 사용할 수 있습니다.

[Locator](https://playwright.dev/docs/api/class-locator "Locator")와 ElementHandle의 차이는, ElementHandle은 특정 요소를 가리키는 반면 [Locator](https://playwright.dev/docs/api/class-locator "Locator")는 요소를 조회하는 로직을 캡처한다는 점입니다.

아래 예시에서 handle은 페이지의 특정 DOM 요소를 가리킵니다. 해당 요소의 텍스트가 바뀌거나 React가 완전히 다른 컴포넌트를 렌더링하는 데 사용되더라도 handle은 여전히 바로 그 DOM 요소를 가리킵니다. 이로 인해 예기치 않은 동작이 발생할 수 있습니다.

```
    const handle = await page.$('text=Submit');
    // ...
    await handle.hover();
    await handle.click();

```

locator를 사용하면 `element`를 사용할 때마다 선택자를 이용해 페이지에서 최신 DOM 요소를 찾습니다. 따라서 아래 스니펫에서는 기반 DOM 요소를 두 번 찾게 됩니다.

```
    const locator = page.getByText('Submit');
    // ...
    await locator.hover();
    await locator.click();

```

---

## 메서드[​](https://playwright.dev/docs/api/class-elementhandle#methods "Direct link to Methods")

### boundingBox[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-bounding-box "Direct link to boundingBox")

v1.9 이전에 추가됨 elementHandle.boundingBox

이 메서드는 요소의 바운딩 박스를 반환하며, 요소가 보이지 않으면 `null`을 반환합니다. 바운딩 박스는 메인 프레임 뷰포트를 기준으로 계산되며, 일반적으로 브라우저 창과 동일합니다.

스크롤은 [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect)와 유사하게 반환되는 바운딩 박스에 영향을 줍니다. 즉 `x` 및/또는 `y`가 음수일 수 있습니다.

자식 프레임의 요소는 [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect)와 달리 메인 프레임 기준의 바운딩 박스를 반환합니다.

페이지가 정적이라고 가정하면, 입력 수행에 바운딩 박스 좌표를 사용해도 안전합니다. 예를 들어 아래 스니펫은 요소의 중앙을 클릭해야 합니다.

**사용법**

```
    const box = await elementHandle.boundingBox();
    await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2);

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-bounding-box-return)
  - `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소의 x 좌표(픽셀)입니다.

    * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소의 y 좌표(픽셀)입니다.

    * `width` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소의 너비(픽셀)입니다.

    * `height` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소의 높이(픽셀)입니다.

---

### contentFrame[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-content-frame "Direct link to contentFrame")

v1.9 이전에 추가됨 elementHandle.contentFrame

iframe 노드를 참조하는 element handle에 대해 content frame을 반환하고, 그 외에는 `null`을 반환합니다.

**사용법**

```
    await elementHandle.contentFrame();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Frame](https://playwright.dev/docs/api/class-frame "Frame")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-content-frame-return)

---

### ownerFrame[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-owner-frame "Direct link to ownerFrame")

v1.9 이전에 추가됨 elementHandle.ownerFrame

주어진 요소를 포함하는 프레임을 반환합니다.

**사용법**

```
    await elementHandle.ownerFrame();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [Frame](https://playwright.dev/docs/api/class-frame "Frame")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-owner-frame-return)

---

### waitForElementState[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-element-state "Direct link to waitForElementState")

v1.9 이전에 추가됨 elementHandle.waitForElementState

요소가 [state](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-element-state-option-state)를 만족하면 반환됩니다.

[state](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-element-state-option-state) 파라미터에 따라 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사 중 하나가 통과될 때까지 대기합니다. `"hidden"` 상태를 기다리는 경우를 제외하면, 대기 중 요소가 분리(detached)되면 이 메서드는 예외를 발생시킵니다.

- `"visible"` 요소가 [visible](https://playwright.dev/docs/actionability#visible) 상태가 될 때까지 대기합니다.
- `"hidden"` 요소가 [not visible](https://playwright.dev/docs/actionability#visible) 상태이거나 연결되지 않을 때까지 대기합니다. hidden 대기는 요소가 분리되어도 예외를 발생시키지 않습니다.
- `"stable"` 요소가 [visible](https://playwright.dev/docs/actionability#visible) 및 [stable](https://playwright.dev/docs/actionability#stable) 상태를 모두 만족할 때까지 대기합니다.
- `"enabled"` 요소가 [enabled](https://playwright.dev/docs/actionability#enabled) 상태가 될 때까지 대기합니다.
- `"disabled"` 요소가 [not enabled](https://playwright.dev/docs/actionability#enabled) 상태가 될 때까지 대기합니다.
- `"editable"` 요소가 [editable](https://playwright.dev/docs/actionability#editable) 상태가 될 때까지 대기합니다.

요소가 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-element-state-option-timeout) 밀리초 내에 조건을 만족하지 않으면, 이 메서드는 예외를 발생시킵니다.

**사용법**

```
    await elementHandle.waitForElementState(state);
    await elementHandle.waitForElementState(state, options);

```

**인수**

- `state` "visible" | "hidden" | "stable" | "enabled" | "disabled" | "editable"[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-element-state-option-state)

대기할 상태입니다. 자세한 내용은 아래를 참조하세요.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-element-state-option-timeout)

최대 대기 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-element-state-return)

---

## 사용 중단됨[​](https://playwright.dev/docs/api/class-elementhandle#deprecated "Direct link to Deprecated")

### $[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-query-selector "Direct link to $")

추가됨: v1.9 elementHandle.$

권장되지 않음

대신 locator 기반 [page.locator()](https://playwright.dev/docs/api/class-page#page-locator)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

이 메서드는 `ElementHandle`의 하위 트리에서 지정된 선택자와 일치하는 요소를 찾습니다. 선택자와 일치하는 요소가 없으면 `null`을 반환합니다.

**사용법**

```
    await elementHandle.$(selector);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-query-selector-option-selector)

조회할 선택자입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-query-selector-return)

---

### $$[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-query-selector-all "Direct link to $$")

추가됨: v1.9 elementHandle.$$

권장되지 않음

대신 locator 기반 [page.locator()](https://playwright.dev/docs/api/class-page#page-locator)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서를 참고하세요.

이 메서드는 `ElementHandle`의 하위 트리에서 지정된 선택자와 일치하는 모든 요소를 찾습니다. 선택자와 일치하는 요소가 없으면 빈 배열을 반환합니다.

**사용법**

```
    await elementHandle.$$(selector);

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-query-selector-all-option-selector)

조회할 선택자입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-query-selector-all-return)

---

### $eval[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector "Direct link to $eval")

추가됨: v1.9 elementHandle.$eval

권장되지 않음

이 메서드는 요소가 actionability 검사를 통과할 때까지 기다리지 않으므로 flaky 테스트를 유발할 수 있습니다. 대신 [locator.evaluate()](https://playwright.dev/docs/api/class-locator#locator-evaluate), 다른 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 헬퍼 메서드 또는 웹 우선 assertion을 사용하세요.

[pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-option-expression)의 반환값을 반환합니다.

이 메서드는 `ElementHandle`의 하위 트리에서 지정된 선택자와 일치하는 요소를 찾아 첫 번째 인수로 [pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-option-expression)에 전달합니다. 선택자와 일치하는 요소가 없으면 이 메서드는 오류를 발생시킵니다.

[pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-option-expression)이 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [elementHandle.$eval()](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector)은 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

**사용법**

```
    const tweetHandle = await page.$('.tweet');
    expect(await tweetHandle.$eval('.like', node => node.innerText)).toBe('100');
    expect(await tweetHandle.$eval('.retweets', node => node.innerText)).toBe('10');

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-option-selector)

조회할 selector입니다.

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([Element](https://developer.mozilla.org/en-US/docs/Web/API/element "Element")) | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-option-expression)

페이지 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-return)

---

### $$eval[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all "Direct link to $$eval")

추가된 버전: v1.9 elementHandle.$$eval

권장되지 않음

대부분의 경우 [locator.evaluateAll()](https://playwright.dev/docs/api/class-locator#locator-evaluate-all), 기타 [Locator](https://playwright.dev/docs/api/class-locator "Locator") 헬퍼 메서드 및 웹 우선 assertion이 더 적합합니다.

[pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-option-expression)의 반환값을 반환합니다.

이 메서드는 `ElementHandle`의 하위 트리에서 지정한 selector와 일치하는 모든 요소를 찾고, 일치한 요소 배열을 첫 번째 인수로 [pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-option-expression)에 전달합니다.

[pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-option-expression)이 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, [elementHandle.$$eval()](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all)은 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

**사용법**

```
      <div class="tweet">Hello!</div>
      <div class="tweet">Hi!</div>

```

```
    const feedHandle = await page.$('.feed');
    expect(await feedHandle.$$eval('.tweet', nodes =>
      nodes.map(n => n.innerText))).toEqual(['Hello!', 'Hi!'],
    );

```

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-option-selector)

조회할 selector입니다.

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")([Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Element](https://developer.mozilla.org/en-US/docs/Web/API/element "Element")>) | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-option-expression)

페이지 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-eval-on-selector-all-return)

---

### check[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-check "Direct link to check")

v1.9 이전에 추가됨 elementHandle.check

권장되지 않음

대신 locator 기반 [locator.check()](https://playwright.dev/docs/api/class-locator#locator-check)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 요소를 체크합니다.

1. 요소가 checkbox 또는 radio input인지 확인합니다. 아니면 이 메서드는 예외를 발생시킵니다. 요소가 이미 체크되어 있으면 이 메서드는 즉시 반환합니다.
2. [force](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-option-force) 옵션이 설정되지 않은 경우, 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사 대기합니다.
3. 필요한 경우 요소를 화면에 보이도록 스크롤합니다.
4. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소 중앙을 클릭합니다.
5. 요소가 이제 체크되었는지 확인합니다. 그렇지 않으면 이 메서드는 예외를 발생시킵니다.

동작 중 어느 시점이든 요소가 DOM에서 분리되면, 이 메서드는 예외를 발생시킵니다.

지정된 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-option-timeout) 내에 모든 단계가 완료되지 않으면, 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이를 비활성화합니다.

**사용법**

```
    await elementHandle.check();
    await elementHandle.check(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-option-no-wait-after)

지원 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding box의 좌상단을 기준으로 사용할 좌표입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-option-timeout)

밀리초 단위 최대 시간입니다. 기본값은 `0`이며 timeout이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 동작 준비 상태가 될 때까지 기다릴 때 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-check-return)

---

### click[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-click "Direct link to click")

v1.9 이전에 추가됨 elementHandle.click

권장되지 않음

대신 locator 기반 [locator.click()](https://playwright.dev/docs/api/class-locator#locator-click)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 요소를 클릭합니다.

1. [force](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-force) 옵션이 설정되지 않은 경우, 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사 대기합니다.
2. 필요한 경우 요소를 화면에 보이도록 스크롤합니다.
3. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소 중앙 또는 지정된 [position](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-position)을 클릭합니다.
4. [noWaitAfter](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-no-wait-after) 옵션이 설정되지 않은 경우, 시작된 navigation이 성공하거나 실패할 때까지 기다립니다.

동작 중 어느 시점이든 요소가 DOM에서 분리되면, 이 메서드는 예외를 발생시킵니다.

지정된 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-timeout) 내에 모든 단계가 완료되지 않으면, 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이를 비활성화합니다.

**사용법**

```
    await elementHandle.click();
    await elementHandle.click(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `button` "left" | "right" | "middle" _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-button)

기본값은 `left`입니다.

    * `clickCount` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-click-count)

기본값은 1입니다. [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail")을 참고하세요.

    * `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-delay)

`mousedown`과 `mouseup` 사이에 대기할 시간(밀리초)입니다. 기본값은 0입니다.

    * `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

- `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-modifiers)

누를 수정자 키입니다. 작업 중에는 이 수정자들만 눌리도록 보장한 다음, 현재 수정자 상태를 다시 복원합니다. 지정하지 않으면 현재 눌려 있는 수정자가 사용됩니다. "ControlOrMeta"는 Windows와 Linux에서는 "Control"로, macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-no-wait-after)

지원 중단됨

이 옵션은 향후 기본값이 `true`가 됩니다.

탐색을 시작하는 액션은 해당 탐색이 발생하고 페이지 로딩이 시작될 때까지 기다립니다. 이 플래그를 설정하면 대기를 건너뛸 수 있습니다. 접근할 수 없는 페이지로 이동하는 등의 예외적인 경우에만 이 옵션이 필요합니다. 기본값은 `false`입니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding 박스의 왼쪽 위 모서리를 기준으로 사용할 지점입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `steps` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.57[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-steps)

기본값은 1입니다. Playwright의 현재 커서 위치에서 제공된 목적지까지의 이동을 나타내기 위해 `n`개의 보간된 `mousemove` 이벤트를 전송합니다. 1로 설정하면 목적지 위치에서 단일 `mousemove` 이벤트를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경할 수 있고, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수도 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 액션은 건너뜁니다. 기본값은 `false`입니다. 실제로 수행하지 않고 요소가 액션 준비 상태가 될 때까지 기다릴 때 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-click-return)

---

### dblclick[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick "Direct link to dblclick")

v1.9 이전에 추가됨 elementHandle.dblclick

권장되지 않음

대신 locator 기반 [locator.dblclick()](https://playwright.dev/docs/api/class-locator#locator-dblclick)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대한 자세한 내용도 참고하세요.

이 메서드는 다음 단계를 수행하여 요소를 더블 클릭합니다:

1. [force](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-force) 옵션이 설정되지 않은 경우, 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다.
2. 필요하면 요소를 뷰포트로 스크롤합니다.
3. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소의 중앙 또는 지정된 [position](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-position)에서 더블 클릭합니다.

액션 도중 어느 시점에서든 요소가 DOM에서 분리되면 이 메서드는 예외를 발생시킵니다.

지정된 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-timeout) 내에 전체 단계가 완료되지 않으면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. 타임아웃을 0으로 전달하면 이를 비활성화합니다.

note

`elementHandle.dblclick()`은 두 개의 `click` 이벤트와 하나의 `dblclick` 이벤트를 디스패치합니다.

**사용법**

```
    await elementHandle.dblclick();
    await elementHandle.dblclick(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `button` "left" | "right" | "middle" _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-button)

기본값은 `left`입니다.

    * `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-delay)

`mousedown`과 `mouseup` 사이에 기다릴 시간(밀리초)입니다. 기본값은 0입니다.

    * `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-modifiers)

누를 수정자 키입니다. 작업 중에는 이 수정자들만 눌리도록 보장한 다음, 현재 수정자 상태를 다시 복원합니다. 지정하지 않으면 현재 눌려 있는 수정자가 사용됩니다. "ControlOrMeta"는 Windows와 Linux에서는 "Control"로, macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-no-wait-after)

지원 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 padding 박스의 왼쪽 위 모서리를 기준으로 사용할 지점입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `steps` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.57[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-steps)

기본값은 1입니다. Playwright의 현재 커서 위치에서 제공된 목적지까지의 이동을 나타내기 위해 `n`개의 보간된 `mousemove` 이벤트를 전송합니다. 1로 설정하면 목적지 위치에서 단일 `mousemove` 이벤트를 발생시킵니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경할 수 있고, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수도 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 액션은 건너뜁니다. 기본값은 `false`입니다. 실제로 수행하지 않고 요소가 액션 준비 상태가 될 때까지 기다릴 때 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dblclick-return)

---

### dispatchEvent[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-dispatch-event "Direct link to dispatchEvent")

v1.9 이전에 추가됨 elementHandle.dispatchEvent

권장되지 않음

대신 locator 기반 [locator.dispatchEvent()](https://playwright.dev/docs/api/class-locator#locator-dispatch-event)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대한 자세한 내용도 참고하세요.

아래 스니펫은 요소에 `click` 이벤트를 디스패치합니다. 요소의 가시성 상태와 관계없이 `click`이 디스패치됩니다. 이는 [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)을 호출하는 것과 동일합니다.

**사용법**

```
    await elementHandle.dispatchEvent('click');

```

내부적으로는 주어진 [type](https://playwright.dev/docs/api/class-elementhandle#element-handle-dispatch-event-option-type)을 기반으로 이벤트 인스턴스를 생성하고, [eventInit](https://playwright.dev/docs/api/class-elementhandle#element-handle-dispatch-event-option-event-init) 속성으로 초기화한 뒤 요소에 디스패치합니다. 이벤트는 기본적으로 `composed`, `cancelable`이며 버블링됩니다.

[eventInit](https://playwright.dev/docs/api/class-elementhandle#element-handle-dispatch-event-option-event-init)은 이벤트별로 다르므로, 초기 속성 목록은 이벤트 문서를 참고하세요:

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

이벤트에 라이브 객체를 전달하려면 속성 값으로 `JSHandle`을 지정할 수도 있습니다:

```
    // Note you can only create DataTransfer in Chromium and Firefox
    const dataTransfer = await page.evaluateHandle(() => new DataTransfer());
    await elementHandle.dispatchEvent('dragstart', { dataTransfer });

```

**인수**

- `type` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dispatch-event-option-type)

DOM 이벤트 타입: `"click"`, `"dragstart"` 등.

- `eventInit` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dispatch-event-option-event-init)

선택적인 이벤트별 초기화 속성입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-dispatch-event-return)

---

### fill[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-fill "Direct link to fill")

v1.9 이전에 추가됨 `elementHandle.fill`

권장되지 않음

대신 locator 기반 [locator.fill()](https://playwright.dev/docs/api/class-locator#locator-fill)을 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사를 기다리고, 요소에 포커스를 맞춘 뒤, 값을 채우고, 채운 후 `input` 이벤트를 트리거합니다. 입력 필드를 비우려면 빈 문자열을 전달할 수 있습니다.

대상 요소가 `<input>`, `<textarea>`, `[contenteditable]` 요소가 아니면 이 메서드는 오류를 발생시킵니다. 단, 요소가 연결된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)을 가진 `<label>` 요소 내부에 있다면 해당 control이 대신 채워집니다.

더 세밀한 키보드 이벤트를 보내려면 [locator.pressSequentially()](https://playwright.dev/docs/api/class-locator#locator-press-sequentially)를 사용하세요.

**사용법**

```
    await elementHandle.fill(value);
    await elementHandle.fill(value, options);

```

**인수**

- `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-fill-option-value)

`<input>`, `<textarea>`, `[contenteditable]` 요소에 설정할 값입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ Added in: v1.13[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-fill-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-fill-option-no-wait-after)

지원 중단됨

이 옵션은 아무런 효과가 없습니다.

이 옵션은 아무런 효과가 없습니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-fill-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-fill-return)

---

### focus[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-focus "Direct link to focus")

v1.9 이전에 추가됨 `elementHandle.focus`

권장되지 않음

대신 locator 기반 [locator.focus()](https://playwright.dev/docs/api/class-locator#locator-focus)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

요소에서 [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus)를 호출합니다.

**사용법**

```
    await elementHandle.focus();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-focus-return)

---

### getAttribute[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-get-attribute "Direct link to getAttribute")

v1.9 이전에 추가됨 `elementHandle.getAttribute`

권장되지 않음

대신 locator 기반 [locator.getAttribute()](https://playwright.dev/docs/api/class-locator#locator-get-attribute)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

요소의 속성 값을 반환합니다.

**사용법**

```
    await elementHandle.getAttribute(name);

```

**인수**

- `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-get-attribute-option-name)

값을 가져올 속성 이름입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-get-attribute-return)

---

### hover[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover "Direct link to hover")

v1.9 이전에 추가됨 `elementHandle.hover`

권장되지 않음

대신 locator 기반 [locator.hover()](https://playwright.dev/docs/api/class-locator#locator-hover)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

이 메서드는 다음 단계를 수행하여 요소 위로 호버합니다.

1. [force](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-force) 옵션이 설정되지 않은 경우, 요소의 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다.
2. 필요하면 요소를 뷰포트에 스크롤해 보이게 합니다.
3. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소의 중앙 또는 지정된 [position](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-position) 위치에 호버합니다.

동작 중 어느 시점에서든 요소가 DOM에서 분리되면 이 메서드는 예외를 발생시킵니다.

지정된 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-timeout) 동안 모든 단계가 완료되지 않으면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. 타임아웃에 0을 전달하면 이 동작이 비활성화됩니다.

**사용법**

```
    await elementHandle.hover();
    await elementHandle.hover(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-modifiers)

누를 보조 키입니다. 작업 중에는 이 보조 키들만 눌리도록 보장하고, 이후 현재 보조 키 상태로 복원합니다. 지정하지 않으면 현재 눌린 보조 키를 사용합니다. "ControlOrMeta"는 Windows 및 Linux에서는 "Control", macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ Added in: v1.28[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-no-wait-after)

지원 중단됨

이 옵션은 아무런 효과가 없습니다.

이 옵션은 아무런 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 패딩 박스의 왼쪽 위 모서리를 기준으로 사용할 지점입니다. 지정하지 않으면 요소의 가시 영역 내 임의의 지점을 사용합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 실제 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고 요소가 준비될 때까지 기다릴 때 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-hover-return)

---

### innerHTML[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-inner-html "Direct link to innerHTML")

v1.9 이전에 추가됨 `elementHandle.innerHTML`

권장되지 않음

대신 locator 기반 [locator.innerHTML()](https://playwright.dev/docs/api/class-locator#locator-inner-html)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

`element.innerHTML`을 반환합니다.

**사용법**

```
    await elementHandle.innerHTML();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-inner-html-return)

---

### innerText[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-inner-text "Direct link to innerText")

v1.9 이전에 추가됨 `elementHandle.innerText`

권장되지 않음

대신 locator 기반 [locator.innerText()](https://playwright.dev/docs/api/class-locator#locator-inner-text)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 읽어보세요.

`element.innerText`를 반환합니다.

**사용법**

```
    await elementHandle.innerText();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-inner-text-return)

---

### inputValue[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-input-value "Direct link to inputValue")

추가된 버전: v1.13 elementHandle.inputValue

권장되지 않음

대신 locator 기반 [locator.inputValue()](https://playwright.dev/docs/api/class-locator#locator-input-value)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

선택된 `<input>`, `<textarea>`, 또는 `<select>` 요소의 `input.value`를 반환합니다.

input 요소가 아닌 경우 예외를 발생시킵니다. 단, 요소가 연결된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)을 가진 `<label>` 요소 내부에 있으면 control의 값을 반환합니다.

**사용법**

```
    await elementHandle.inputValue();
    await elementHandle.inputValue(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-input-value-option-timeout)

밀리초 단위의 최대 시간입니다. 기본값은 `0`이며, 시간 제한이 없습니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 통해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-input-value-return)

---

### isChecked[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-checked "Direct link to isChecked")

v1.9 이전에 추가됨 elementHandle.isChecked

권장되지 않음

대신 locator 기반 [locator.isChecked()](https://playwright.dev/docs/api/class-locator#locator-is-checked)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소가 체크되어 있는지 여부를 반환합니다. 요소가 checkbox 또는 radio input이 아니면 예외를 발생시킵니다.

**사용법**

```
    await elementHandle.isChecked();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-checked-return)

---

### isDisabled[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-disabled "Direct link to isDisabled")

v1.9 이전에 추가됨 elementHandle.isDisabled

권장되지 않음

대신 locator 기반 [locator.isDisabled()](https://playwright.dev/docs/api/class-locator#locator-is-disabled)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소가 비활성화되어 있는지 여부를 반환합니다. [enabled](https://playwright.dev/docs/actionability#enabled)의 반대입니다.

**사용법**

```
    await elementHandle.isDisabled();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-disabled-return)

---

### isEditable[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-editable "Direct link to isEditable")

v1.9 이전에 추가됨 elementHandle.isEditable

권장되지 않음

대신 locator 기반 [locator.isEditable()](https://playwright.dev/docs/api/class-locator#locator-is-editable)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소가 [editable](https://playwright.dev/docs/actionability#editable)한지 여부를 반환합니다.

**사용법**

```
    await elementHandle.isEditable();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-editable-return)

---

### isEnabled[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-enabled "Direct link to isEnabled")

v1.9 이전에 추가됨 elementHandle.isEnabled

권장되지 않음

대신 locator 기반 [locator.isEnabled()](https://playwright.dev/docs/api/class-locator#locator-is-enabled)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소가 [enabled](https://playwright.dev/docs/actionability#enabled) 상태인지 여부를 반환합니다.

**사용법**

```
    await elementHandle.isEnabled();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-enabled-return)

---

### isHidden[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-hidden "Direct link to isHidden")

v1.9 이전에 추가됨 elementHandle.isHidden

권장되지 않음

대신 locator 기반 [locator.isHidden()](https://playwright.dev/docs/api/class-locator#locator-is-hidden)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소가 숨겨져 있는지 여부를 반환합니다. [visible](https://playwright.dev/docs/actionability#visible)의 반대입니다.

**사용법**

```
    await elementHandle.isHidden();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-hidden-return)

---

### isVisible[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-visible "Direct link to isVisible")

v1.9 이전에 추가됨 elementHandle.isVisible

권장되지 않음

대신 locator 기반 [locator.isVisible()](https://playwright.dev/docs/api/class-locator#locator-is-visible)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소가 [visible](https://playwright.dev/docs/actionability#visible) 상태인지 여부를 반환합니다.

**사용법**

```
    await elementHandle.isVisible();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-is-visible-return)

---

### press[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-press "Direct link to press")

v1.9 이전에 추가됨 elementHandle.press

권장되지 않음

대신 locator 기반 [locator.press()](https://playwright.dev/docs/api/class-locator#locator-press)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

요소에 포커스를 준 다음 [keyboard.down()](https://playwright.dev/docs/api/class-keyboard#keyboard-down)과 [keyboard.up()](https://playwright.dev/docs/api/class-keyboard#keyboard-up)을 사용합니다.

[key](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-key)에는 의도한 [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) 값 또는 텍스트 생성을 위한 단일 문자를 지정할 수 있습니다. [key](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-key) 값의 상위 집합은 [여기](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values)에서 확인할 수 있습니다. 키 예시는 다음과 같습니다.

`F1` \- `F12`, `Digit0`\- `Digit9`, `KeyA`\- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp` 등.

다음 수정 키 단축키도 지원됩니다: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`.

`Shift`를 누른 채로 있으면 [key](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-key)에 해당하는 텍스트가 대문자로 입력됩니다.

[key](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-key)가 단일 문자라면 대소문자를 구분하므로 `a`와 `A`는 각각 서로 다른 텍스트를 생성합니다.

`key: "Control+o"`, `key: "Control++` 또는 `key: "Control+Shift+T"` 같은 단축키도 지원됩니다. 수정 키와 함께 지정하면, 이후 키를 누르는 동안 수정 키를 누른 상태로 유지합니다.

**사용법**

```
    await elementHandle.press(key);
    await elementHandle.press(key, options);

```

**인수**

- `key` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-key)

누를 키 이름 또는 생성할 문자입니다. 예: `ArrowLeft`, `a`.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(선택 사항)_
  - `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-delay)

`keydown`과 `keyup` 사이의 대기 시간(밀리초)입니다. 기본값은 0입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-no-wait-after)

지원 중단 예정

이 옵션은 향후 기본값이 `true`가 됩니다.

탐색(navigation)을 시작하는 액션은 해당 탐색이 발생하고 페이지 로딩이 시작될 때까지 기다립니다. 이 플래그를 설정해 대기를 건너뛸 수 있습니다. 접근 불가능한 페이지로 이동하는 등 예외적인 경우에만 필요합니다. 기본값은 `false`입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(선택 사항)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-option-timeout)

밀리초 단위의 최대 시간입니다. 기본값은 `0`이며, 시간 제한이 없습니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 통해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-press-return)

---

### screenshot[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot "Direct link to screenshot")

v1.9 이전에 추가됨 elementHandle.screenshot

권장되지 않음

대신 locator 기반 [locator.screenshot()](https://playwright.dev/docs/api/class-locator#locator-screenshot)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 페이지의 스크린샷을 캡처하되, 해당 요소의 크기와 위치로 잘라냅니다. 요소가 다른 요소에 가려져 있으면 스크린샷에서 실제로 보이지 않을 수 있습니다. 요소가 스크롤 가능한 컨테이너라면 현재 스크롤된 콘텐츠만 스크린샷에 표시됩니다.

이 메서드는 스크린샷을 찍기 전에 [actionability](https://playwright.dev/docs/actionability) 검사를 기다린 뒤 요소를 뷰포트에 보이도록 스크롤합니다. 요소가 DOM에서 분리되어 있으면 오류를 발생시킵니다.

캡처된 스크린샷이 담긴 버퍼를 반환합니다.

**사용법**

```
    await elementHandle.screenshot();
    await elementHandle.screenshot(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `animations` "disabled" | "allow" _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-animations)

`"disabled"`로 설정하면 CSS 애니메이션, CSS 트랜지션, Web Animations를 중지합니다. 애니메이션은 지속 시간에 따라 다르게 처리됩니다.

      * 유한 애니메이션은 완료 시점까지 빨리 감기되어 `transitionend` 이벤트를 발생시킵니다.
      * 무한 애니메이션은 초기 상태로 취소된 뒤, 스크린샷 이후 다시 재생됩니다.

기본값은 애니메이션을 그대로 두는 `"allow"`입니다.

    * `caret` "hide" | "initial" _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-caret)

`"hide"`로 설정하면 스크린샷에서 텍스트 캐럿을 숨깁니다. `"initial"`로 설정하면 텍스트 캐럿 동작을 변경하지 않습니다. 기본값은 `"hide"`입니다.

    * `mask` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Locator](https://playwright.dev/docs/api/class-locator "Locator")> _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-mask)

스크린샷 촬영 시 마스킹할 locator를 지정합니다. 마스킹된 요소는 해당 경계 상자를 완전히 덮는 분홍색 박스 `#FF00FF`( [maskColor](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-mask-color)로 사용자 지정 가능)로 오버레이됩니다. 마스크는 보이지 않는 요소에도 적용됩니다. 이를 비활성화하려면 [Matching only visible elements](https://playwright.dev/docs/locators#matching-only-visible-elements)를 참고하세요.

    * `maskColor` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ Added in: v1.35[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-mask-color)

마스킹된 요소에 덮어씌울 오버레이 박스의 색상을 [CSS color format](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)으로 지정합니다. 기본 색상은 분홍색 `#FF00FF`입니다.

    * `omitBackground` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-omit-background)

기본 흰색 배경을 숨기고 투명도가 있는 스크린샷을 캡처할 수 있게 합니다. `jpeg` 이미지에는 적용되지 않습니다. 기본값은 `false`입니다.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-path)

이미지를 저장할 파일 경로입니다. 스크린샷 유형은 파일 확장자로 추론됩니다. [path](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-path)가 상대 경로이면 현재 작업 디렉터리를 기준으로 해석됩니다. 경로를 제공하지 않으면 이미지는 디스크에 저장되지 않습니다.

    * `quality` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-quality)

이미지 품질(0-100)입니다. `png` 이미지에는 적용되지 않습니다.

    * `scale` "css" | "device" _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-scale)

`"css"`로 설정하면 페이지의 각 css 픽셀당 하나의 픽셀로 스크린샷이 생성됩니다. 고해상도(dpi) 디바이스에서는 스크린샷 크기를 작게 유지할 수 있습니다. `"device"` 옵션을 사용하면 디바이스 픽셀당 하나의 픽셀로 생성되므로, 고해상도 디바이스의 스크린샷은 2배 이상 커질 수 있습니다.

기본값은 `"device"`입니다.

    * `style` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ Added in: v1.41[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-style)

스크린샷을 만드는 동안 적용할 스타일시트의 텍스트입니다. 여기에서 동적인 요소를 숨기거나, 요소를 보이지 않게 하거나, 속성을 변경해 반복 가능한 스크린샷을 만드는 데 도움을 줄 수 있습니다. 이 스타일시트는 Shadow DOM을 관통하여 내부 프레임에도 적용됩니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `type` "png" | "jpeg" _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-option-type)

스크린샷 유형을 지정하며, 기본값은 `png`입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-screenshot-return)

---

### scrollIntoViewIfNeeded[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-scroll-into-view-if-needed "Direct link to scrollIntoViewIfNeeded")

v1.9 이전에 추가됨 elementHandle.scrollIntoViewIfNeeded

권장되지 않음

대신 locator 기반 [locator.scrollIntoViewIfNeeded()](https://playwright.dev/docs/api/class-locator#locator-scroll-into-view-if-needed)를 사용하세요. [locators](https://playwright.dev/docs/locators)도 참고하세요.

이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사를 기다린 다음, [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)의 `ratio` 기준으로 요소가 완전히 보이는 상태가 아니라면 요소를 화면에 보이도록 스크롤하려고 시도합니다.

`elementHandle`이 Document 또는 ShadowRoot에 [connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected)된 요소를 가리키지 않으면 예외를 발생시킵니다.

다른 스크롤 방법은 [scrolling](https://playwright.dev/docs/input#scrolling)을 참고하세요.

**사용법**

```
    await elementHandle.scrollIntoViewIfNeeded();
    await elementHandle.scrollIntoViewIfNeeded(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-scroll-into-view-if-needed-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0`이며 타임아웃이 없습니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-scroll-into-view-if-needed-return)

---

### selectOption[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-option "Direct link to selectOption")

v1.9 이전에 추가됨 elementHandle.selectOption

권장되지 않음

대신 locator 기반 [locator.selectOption()](https://playwright.dev/docs/api/class-locator#locator-select-option)를 사용하세요. [locators](https://playwright.dev/docs/locators)도 참고하세요.

이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사를 기다리고, 지정된 모든 옵션이 `<select>` 요소에 존재할 때까지 기다린 뒤 해당 옵션을 선택합니다.

대상 요소가 `<select>` 요소가 아니면 이 메서드는 오류를 발생시킵니다. 다만 요소가 연결된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)이 있는 `<label>` 요소 내부에 있다면, 대신 그 control을 사용합니다.

성공적으로 선택된 옵션 값의 배열을 반환합니다.

제공된 모든 옵션이 선택되면 `change` 및 `input` 이벤트를 트리거합니다.

**사용법**

```
    // Single selection matching the value or label
    handle.selectOption('blue');

    // single selection matching the label
    handle.selectOption({ label: 'Blue' });

    // multiple selection
    handle.selectOption(['red', 'green', 'blue']);

```

**인수**

- `values` [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")> | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-option-option-values)
  - `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

`option.value`로 매칭합니다. 선택 사항입니다.

    * `label` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

`option.label`로 매칭합니다. 선택 사항입니다.

    * `index` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

인덱스로 매칭합니다. 선택 사항입니다.

선택할 옵션입니다. `<select>`에 `multiple` 속성이 있으면 일치하는 모든 옵션이 선택되고, 그렇지 않으면 전달된 옵션 중 하나와 일치하는 첫 번째 옵션만 선택됩니다. 문자열 값은 value와 label 모두에 대해 매칭됩니다. 지정된 모든 속성이 일치하면 해당 옵션이 일치하는 것으로 간주됩니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.13[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-option-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 우회할지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-option-option-no-wait-after)

지원 중단됨

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-option-option-timeout)

밀리초 단위의 최대 시간입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-option-return)

---

### selectText[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-text "Direct link to selectText")

v1.9 이전에 추가됨 elementHandle.selectText

권장되지 않음

대신 locator 기반 [locator.selectText()](https://playwright.dev/docs/api/class-locator#locator-select-text)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서도 참고하세요.

이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사를 기다린 다음, 요소에 포커스를 맞추고 해당 요소의 모든 텍스트 콘텐츠를 선택합니다.

요소가 연결된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)이 있는 `<label>` 요소 내부에 있다면, 대신 해당 control에 포커스를 맞추고 텍스트를 선택합니다.

**사용법**

```
    await elementHandle.selectText();
    await elementHandle.selectText(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.13[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-text-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 건너뛸지 여부입니다. 기본값은 `false`입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-text-option-timeout)

밀리초 단위의 최대 시간입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-select-text-return)

---

### setChecked[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked "Direct link to setChecked")

Added in: v1.15 elementHandle.setChecked

권장되지 않음

대신 locator 기반 [locator.setChecked()](https://playwright.dev/docs/api/class-locator#locator-set-checked)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서도 참고하세요.

이 메서드는 다음 단계를 수행하여 요소를 체크하거나 체크 해제합니다:

1. 요소가 체크박스 또는 라디오 입력인지 확인합니다. 아니면 이 메서드는 예외를 발생시킵니다.
2. 요소가 이미 올바른 checked 상태라면, 이 메서드는 즉시 반환합니다.
3. [force](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-force) 옵션이 설정되지 않은 경우, 일치한 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다. 검사 중 요소가 분리되면 전체 작업을 재시도합니다.
4. 필요하면 요소를 뷰포트 안으로 스크롤합니다.
5. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소 중앙을 클릭합니다.
6. 이제 요소가 체크되었거나 체크 해제되었는지 확인합니다. 아니면 이 메서드는 예외를 발생시킵니다.

지정한 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-timeout) 동안 위의 모든 단계가 완료되지 않으면, 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout을 0으로 전달하면 이를 비활성화합니다.

**사용법**

```
    await elementHandle.setChecked(checked);
    await elementHandle.setChecked(checked, options);

```

**인수**

- `checked` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-checked)

체크박스를 체크할지 또는 체크 해제할지 여부입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 건너뛸지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-no-wait-after)

사용 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 패딩 박스의 왼쪽 위 모서리를 기준으로 사용할 좌표점입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-timeout)

밀리초 단위의 최대 시간입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 동작은 건너뜁니다. 기본값은 `false`입니다. 동작을 수행하지 않고도 요소가 동작 준비가 될 때까지 기다릴 때 유용합니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-checked-return)

---

### setInputFiles[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-input-files "Direct link to setInputFiles")

v1.9 이전에 추가됨 elementHandle.setInputFiles

권장되지 않음

대신 locator 기반 [locator.setInputFiles()](https://playwright.dev/docs/api/class-locator#locator-set-input-files)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서도 참고하세요.

파일 입력의 값을 이 파일 경로 또는 파일로 설정합니다. `filePaths` 중 일부가 상대 경로라면 현재 작업 디렉터리를 기준으로 해석됩니다. 빈 배열이면 선택된 파일을 지웁니다. `[webkitdirectory]` 속성이 있는 입력의 경우 디렉터리 경로 하나만 지원됩니다.

이 메서드는 [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")가 [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)를 가리킨다고 가정합니다. 하지만 요소가 연결된 [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control)이 있는 `<label>` 요소 내부에 있다면, 대신 해당 control을 대상으로 합니다.

**사용법**

```
    await elementHandle.setInputFiles(files);
    await elementHandle.setInputFiles(files, options);

```

**인수**

- `files` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-input-files-option-files)
  - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

    * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 타입

    * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 콘텐츠

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-input-files-option-no-wait-after)

사용 중단됨

이 옵션은 효과가 없습니다.

이 옵션은 효과가 없습니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-input-files-option-timeout)

밀리초 단위의 최대 시간입니다. 기본값은 `0` \- 타임아웃 없음입니다. 기본값은 config의 `actionTimeout` 옵션이나 [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-set-input-files-return)

---

### tap[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap "Direct link to tap")

v1.9 이전에 추가됨 elementHandle.tap

권장되지 않음

대신 locator 기반 [locator.tap()](https://playwright.dev/docs/api/class-locator#locator-tap)를 사용하세요. [locators](https://playwright.dev/docs/locators) 문서도 참고하세요.

이 메서드는 다음 단계를 수행하여 요소를 탭합니다:

1. [force](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-force) 옵션이 설정되지 않은 경우, 요소에 대한 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다.
2. 필요하면 요소를 뷰포트 안으로 스크롤합니다.

3. [page.touchscreen](https://playwright.dev/docs/api/class-page#page-touchscreen)을 사용해 요소의 중앙 또는 지정된 [position](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-position)을 탭합니다.

동작 중 어느 시점에서든 요소가 DOM에서 분리되면 이 메서드는 예외를 발생시킵니다.

지정된 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-timeout) 내에 모든 단계가 완료되지 않으면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이 동작이 비활성화됩니다.

note

`elementHandle.tap()`을 사용하려면 브라우저 컨텍스트의 `hasTouch` 옵션이 `true`로 설정되어 있어야 합니다.

**Usage**

```
    await elementHandle.tap();
    await elementHandle.tap(options);

```

**Arguments**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 건너뛸지 여부입니다. 기본값은 `false`입니다.

    * `modifiers` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-modifiers)

누를 수정 키입니다. 작업 중에는 이 수정 키들만 눌린 상태가 되도록 보장하고, 이후 현재 수정 키 상태를 복원합니다. 지정하지 않으면 현재 눌려 있는 수정 키를 사용합니다. "ControlOrMeta"는 Windows와 Linux에서는 "Control", macOS에서는 "Meta"로 해석됩니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-no-wait-after)

Deprecated

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 패딩 박스의 좌상단을 기준으로 사용할 좌표입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 실제 동작은 건너뜁니다. 기본값은 `false`입니다. 실제로 동작을 수행하지 않고 요소가 준비될 때까지 기다릴 때 유용합니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-tap-return)

---

### textContent[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-text-content "Direct link to textContent")

v1.9 이전에 추가됨 elementHandle.textContent

권장되지 않음

대신 locator 기반의 [locator.textContent()](https://playwright.dev/docs/api/class-locator#locator-text-content)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

`node.textContent`를 반환합니다.

**Usage**

```
    await elementHandle.textContent();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-text-content-return)

---

### type[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-type "Direct link to type")

v1.9 이전에 추가됨 elementHandle.type

Deprecated

대부분의 경우 대신 [locator.fill()](https://playwright.dev/docs/api/class-locator#locator-fill)을 사용해야 합니다. 페이지에 특별한 키보드 처리가 있을 때만 키를 하나씩 눌러야 하며, 이 경우 [locator.pressSequentially()](https://playwright.dev/docs/api/class-locator#locator-press-sequentially)를 사용하세요.

요소에 포커스를 준 다음, 텍스트의 각 문자마다 `keydown`, `keypress`/`input`, `keyup` 이벤트를 전송합니다.

`Control` 또는 `ArrowDown` 같은 특수 키를 누르려면 [elementHandle.press()](https://playwright.dev/docs/api/class-elementhandle#element-handle-press)를 사용하세요.

**Usage**

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-type-option-text)

포커스된 요소에 입력할 텍스트입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-type-option-delay)

키 입력 사이의 대기 시간(밀리초)입니다. 기본값은 0입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-type-option-no-wait-after)

Deprecated

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-type-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-type-return)

---

### uncheck[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck "Direct link to uncheck")

v1.9 이전에 추가됨 elementHandle.uncheck

권장되지 않음

대신 locator 기반의 [locator.uncheck()](https://playwright.dev/docs/api/class-locator#locator-uncheck)를 사용하세요. [locators](https://playwright.dev/docs/locators)에 대해 더 알아보세요.

이 메서드는 다음 단계를 수행하여 요소를 체크합니다.

1. 요소가 체크박스 또는 라디오 input인지 확인합니다. 그렇지 않으면 이 메서드는 예외를 발생시킵니다. 요소가 이미 체크 해제되어 있으면 즉시 반환합니다.
2. [force](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-option-force) 옵션이 설정되지 않은 경우, 요소에 대해 [actionability](https://playwright.dev/docs/actionability) 검사를 기다립니다.
3. 필요하면 요소를 화면에 보이도록 스크롤합니다.
4. [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse)를 사용해 요소 중앙을 클릭합니다.
5. 요소가 이제 체크 해제되었는지 확인합니다. 그렇지 않으면 이 메서드는 예외를 발생시킵니다.

동작 중 어느 시점에서든 요소가 DOM에서 분리되면 이 메서드는 예외를 발생시킵니다.

지정된 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-option-timeout) 내에 모든 단계가 완료되지 않으면 이 메서드는 [TimeoutError](https://playwright.dev/docs/api/class-timeouterror "TimeoutError")를 발생시킵니다. timeout에 0을 전달하면 이 동작이 비활성화됩니다.

**Usage**

```
    await elementHandle.uncheck();
    await elementHandle.uncheck(options);

```

**Arguments**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `force` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-option-force)

[actionability](https://playwright.dev/docs/actionability) 검사를 건너뛸지 여부입니다. 기본값은 `false`입니다.

    * `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-option-no-wait-after)

Deprecated

이 옵션은 아무 효과가 없습니다.

이 옵션은 아무 효과가 없습니다.

    * `position` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-option-position)

      * `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

      * `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

요소 패딩 박스의 좌상단을 기준으로 사용할 좌표입니다. 지정하지 않으면 요소의 보이는 지점 중 하나를 사용합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-option-timeout)

최대 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음입니다. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드를 사용해 변경할 수 있습니다.

    * `trial` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.11[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-option-trial)

설정하면 이 메서드는 [actionability](https://playwright.dev/docs/actionability) 검사만 수행하고 실제 동작은 건너뜁니다. 기본값은 `false`입니다. 실제로 동작을 수행하지 않고 요소가 준비될 때까지 기다릴 때 유용합니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-uncheck-return)

---

### waitForSelector[​](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector "Direct link to waitForSelector")

v1.9 이전에 추가됨 elementHandle.waitForSelector

비권장

대신 가시성을 검증하는 웹 assertion 또는 locator 기반 [locator.waitFor()](https://playwright.dev/docs/api/class-locator#locator-wait-for)를 사용하세요.

[state](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-state) 옵션을 만족할 때 selector로 지정된 element를 반환합니다. `hidden` 또는 `detached`를 기다리는 경우 `null`을 반환합니다.

element handle을 기준으로 한 [selector](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-selector)가 [state](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-state) 옵션(DOM에 나타남/사라짐 또는 visible/hidden 상태 전환)을 만족할 때까지 기다립니다. 메서드 호출 시점에 [selector](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-selector)가 이미 조건을 만족하면 즉시 반환됩니다. selector가 [timeout](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-timeout) 밀리초 동안 조건을 만족하지 않으면 함수가 예외를 발생시킵니다.

**사용법**

```
    await page.setContent(`<div><span></span></div>`);
    const div = await page.$('div');
    // Waiting for the 'span' selector relative to the div.
    const span = await div.waitForSelector('span', { state: 'attached' });

```

참고

이 메서드는 navigation 간에는 동작하지 않으므로, 대신 [page.waitForSelector()](https://playwright.dev/docs/api/class-page#page-wait-for-selector)를 사용하세요.

**인수**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-selector)

조회할 selector입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `state` "attached" | "detached" | "visible" | "hidden" _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-state)

기본값은 `'visible'`입니다. 가능한 값은 다음과 같습니다:

      * `'attached'` \- element가 DOM에 존재할 때까지 기다립니다.
      * `'detached'` \- element가 DOM에 존재하지 않을 때까지 기다립니다.
      * `'visible'` \- element가 비어 있지 않은 bounding box를 가지고 `visibility:hidden`이 아닐 때까지 기다립니다. 콘텐츠가 없거나 `display:none`인 element는 bounding box가 비어 있으므로 visible로 간주되지 않습니다.
      * `'hidden'` \- element가 DOM에서 분리되었거나, bounding box가 비어 있거나, `visibility:hidden` 상태일 때까지 기다립니다. 이는 `'visible'` 옵션의 반대입니다.
    * `strict` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.15[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-strict)

`true`인 경우 selector는 단일 element로 해석되어야 합니다. 전달된 selector가 둘 이상의 element로 해석되면 호출 시 예외가 발생합니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-option-timeout)

최대 대기 시간(밀리초)입니다. 기본값은 `0` \- timeout 없음. 기본값은 config의 `actionTimeout` 옵션으로 변경하거나, [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) 또는 [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) 메서드로 변경할 수 있습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")>[#](https://playwright.dev/docs/api/class-elementhandle#element-handle-wait-for-selector-return)
