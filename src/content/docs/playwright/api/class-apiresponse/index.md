---
title: "APIResponse"
description: "추가된 버전: v1.16 apiResponse.body"
---

Source URL: https://playwright.dev/docs/api/class-apiresponse

# APIResponse | Playwright

[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse") 클래스는 [apiRequestContext.get()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get) 및 유사한 메서드가 반환하는 응답을 나타냅니다.

---

## 메서드[​](https://playwright.dev/docs/api/class-apiresponse#methods "Direct link to Methods")

### body[​](https://playwright.dev/docs/api/class-apiresponse#api-response-body "Direct link to body")

추가된 버전: v1.16 apiResponse.body

응답 본문이 담긴 buffer를 반환합니다.

**사용법**

```
    await apiResponse.body();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-body-return)

---

### dispose[​](https://playwright.dev/docs/api/class-apiresponse#api-response-dispose "Direct link to dispose")

추가된 버전: v1.16 apiResponse.dispose

이 응답의 본문을 해제합니다. 호출하지 않으면 컨텍스트가 닫힐 때까지 본문이 메모리에 유지됩니다.

**사용법**

```
    await apiResponse.dispose();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-dispose-return)

---

### headers[​](https://playwright.dev/docs/api/class-apiresponse#api-response-headers "Direct link to headers")

추가된 버전: v1.16 apiResponse.headers

이 응답과 연결된 모든 응답 HTTP 헤더를 담은 객체입니다.

**사용법**

```
    apiResponse.headers();

```

**반환값**

- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-headers-return)

---

### headersArray[​](https://playwright.dev/docs/api/class-apiresponse#api-response-headers-array "Direct link to headersArray")

추가된 버전: v1.16 apiResponse.headersArray

이 응답과 연결된 모든 응답 HTTP 헤더를 담은 배열입니다. 헤더 이름은 소문자로 변환되지 않습니다. `Set-Cookie`처럼 여러 항목을 갖는 헤더는 배열에 여러 번 나타납니다.

**사용법**

```
    apiResponse.headersArray();

```

**반환값**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-headers-array-return)
  - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

헤더 이름입니다.

    * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

헤더 값입니다.

---

### json[​](https://playwright.dev/docs/api/class-apiresponse#api-response-json "Direct link to json")

추가된 버전: v1.16 apiResponse.json

응답 본문의 JSON 표현을 반환합니다.

응답 본문을 `JSON.parse`로 파싱할 수 없으면 이 메서드는 예외를 발생시킵니다.

**사용법**

```
    await apiResponse.json();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-json-return)

---

### ok[​](https://playwright.dev/docs/api/class-apiresponse#api-response-ok "Direct link to ok")

추가된 버전: v1.16 apiResponse.ok

응답이 성공했는지(상태 코드가 200-299 범위) 여부를 나타내는 boolean 값을 포함합니다.

**사용법**

```
    apiResponse.ok();

```

**반환값**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-ok-return)

---

### status[​](https://playwright.dev/docs/api/class-apiresponse#api-response-status "Direct link to status")

추가된 버전: v1.16 apiResponse.status

응답의 상태 코드(예: 성공 시 200)를 포함합니다.

**사용법**

```
    apiResponse.status();

```

**반환값**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-status-return)

---

### statusText[​](https://playwright.dev/docs/api/class-apiresponse#api-response-status-text "Direct link to statusText")

추가된 버전: v1.16 apiResponse.statusText

응답의 상태 텍스트를 포함합니다(예: 성공 시 일반적으로 "OK").

**사용법**

```
    apiResponse.statusText();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-status-text-return)

---

### text[​](https://playwright.dev/docs/api/class-apiresponse#api-response-text "Direct link to text")

추가된 버전: v1.16 apiResponse.text

응답 본문의 텍스트 표현을 반환합니다.

**사용법**

```
    await apiResponse.text();

```

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-text-return)

---

### url[​](https://playwright.dev/docs/api/class-apiresponse#api-response-url "Direct link to url")

추가된 버전: v1.16 apiResponse.url

응답의 URL을 포함합니다.

**사용법**

```
    apiResponse.url();

```

**반환값**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-url-return)
