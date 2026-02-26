---
title: "JSHandle"
description: "JSHandle은 페이지 내 JavaScript 객체를 나타냅니다. JSHandle은 page.evaluateHandle() 메서드로 생성할 수 있습니다."
---

Source URL: https://playwright.dev/docs/api/class-jshandle

# JSHandle | Playwright

JSHandle은 페이지 내 JavaScript 객체를 나타냅니다. JSHandle은 [page.evaluateHandle()](https://playwright.dev/docs/api/class-page#page-evaluate-handle) 메서드로 생성할 수 있습니다.

```
    const windowHandle = await page.evaluateHandle(() => window);
    // ...

```

JSHandle은 [jsHandle.dispose()](https://playwright.dev/docs/api/class-jshandle#js-handle-dispose)로 핸들을 해제하지 않는 한, 참조된 JavaScript 객체가 가비지 컬렉션되지 않도록 합니다. JSHandle은 원본 프레임이 탐색되거나 부모 컨텍스트가 파괴되면 자동으로 해제됩니다.

JSHandle 인스턴스는 [page.$eval()](https://playwright.dev/docs/api/class-page#page-eval-on-selector), [page.evaluate()](https://playwright.dev/docs/api/class-page#page-evaluate), [page.evaluateHandle()](https://playwright.dev/docs/api/class-page#page-evaluate-handle) 메서드의 인수로 사용할 수 있습니다.

---

## 메서드[​](https://playwright.dev/docs/api/class-jshandle#methods "Direct link to Methods")

### asElement[​](https://playwright.dev/docs/api/class-jshandle#js-handle-as-element "Direct link to asElement")

v1.9 이전에 추가됨 jsHandle.asElement

객체 핸들이 [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")의 인스턴스인 경우 `null` 또는 객체 핸들 자체를 반환합니다.

**사용법**

```
    jsHandle.asElement();

```

**반환값**

- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") | [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")[#](https://playwright.dev/docs/api/class-jshandle#js-handle-as-element-return)

---

### dispose[​](https://playwright.dev/docs/api/class-jshandle#js-handle-dispose "Direct link to dispose")

v1.9 이전에 추가됨 jsHandle.dispose

`jsHandle.dispose` 메서드는 element handle에 대한 참조를 중지합니다.

**사용법**

```
    await jsHandle.dispose();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-jshandle#js-handle-dispose-return)

---

### evaluate[​](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate "Direct link to evaluate")

v1.9 이전에 추가됨 jsHandle.evaluate

[pageFunction](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-option-expression)의 반환값을 반환합니다.

이 메서드는 이 핸들을 [pageFunction](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-option-expression)의 첫 번째 인수로 전달합니다.

[pageFunction](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-option-expression)이 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, `handle.evaluate`는 해당 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

**사용법**

```
    const tweetHandle = await page.$('.tweet .retweets');
    expect(await tweetHandle.evaluate(node => node.innerText)).toBe('10 retweets');

```

**인수**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-option-expression)

페이지 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-return)

---

### evaluateHandle[​](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-handle "Direct link to evaluateHandle")

v1.9 이전에 추가됨 jsHandle.evaluateHandle

[pageFunction](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-handle-option-expression)의 반환값을 [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")로 반환합니다.

이 메서드는 이 핸들을 [pageFunction](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-handle-option-expression)의 첫 번째 인수로 전달합니다.

`jsHandle.evaluate`와 `jsHandle.evaluateHandle`의 유일한 차이는 `jsHandle.evaluateHandle`이 [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")을 반환한다는 점입니다.

`jsHandle.evaluateHandle`에 전달된 함수가 [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")를 반환하면, `jsHandle.evaluateHandle`은 해당 promise가 resolve될 때까지 기다린 뒤 그 값을 반환합니다.

자세한 내용은 [page.evaluateHandle()](https://playwright.dev/docs/api/class-page#page-evaluate-handle)을 참고하세요.

**사용법**

```
    await jsHandle.evaluateHandle(pageFunction);
    await jsHandle.evaluateHandle(pageFunction, arg);

```

**인수**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-handle-option-expression)

페이지 컨텍스트에서 평가할 함수입니다.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-handle-option-arg)

[pageFunction](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-handle-option-expression)에 전달할 선택적 인수입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate-handle-return)

---

### getProperties[​](https://playwright.dev/docs/api/class-jshandle#js-handle-get-properties "Direct link to getProperties")

v1.9 이전에 추가됨 jsHandle.getProperties

이 메서드는 **자체 속성 이름(own property names)** 을 키로 하고, 해당 속성 값의 JSHandle 인스턴스를 값으로 하는 맵을 반환합니다.

**사용법**

```
    const handle = await page.evaluateHandle(() => ({ window, document }));
    const properties = await handle.getProperties();
    const windowHandle = properties.get('window');
    const documentHandle = properties.get('document');
    await handle.dispose();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map "Map")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>>[#](https://playwright.dev/docs/api/class-jshandle#js-handle-get-properties-return)

---

### getProperty[​](https://playwright.dev/docs/api/class-jshandle#js-handle-get-property "Direct link to getProperty")

v1.9 이전에 추가됨 jsHandle.getProperty

참조된 객체에서 단일 속성을 가져옵니다.

**사용법**

```
    await jsHandle.getProperty(propertyName);

```

**인수**

- `propertyName` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-jshandle#js-handle-get-property-option-property-name)

가져올 속성

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-jshandle#js-handle-get-property-return)

---

### jsonValue[​](https://playwright.dev/docs/api/class-jshandle#js-handle-json-value "Direct link to jsonValue")

v1.9 이전에 추가됨 jsHandle.jsonValue

객체의 JSON 표현을 반환합니다. 객체에 `toJSON` 함수가 있어도 **호출되지 않습니다**.

note

참조된 객체를 문자열화할 수 없는 경우 이 메서드는 빈 JSON 객체를 반환합니다. 객체에 순환 참조가 있으면 오류를 발생시킵니다.

**사용법**

```
    await jsHandle.jsonValue();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-jshandle#js-handle-json-value-return)
