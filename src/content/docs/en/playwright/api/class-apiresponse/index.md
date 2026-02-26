---
title: "APIResponse"
description: "Added in: v1.16 apiResponse.body"
---

Source URL: https://playwright.dev/docs/api/class-apiresponse

# APIResponse | Playwright

[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse") class represents responses returned by [apiRequestContext.get()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get) and similar methods.

---

## Methods[​](https://playwright.dev/docs/api/class-apiresponse#methods "Direct link to Methods")

### body[​](https://playwright.dev/docs/api/class-apiresponse#api-response-body "Direct link to body")

Added in: v1.16 apiResponse.body

Returns the buffer with response body.

**Usage**

```
    await apiResponse.body();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-body-return)

---

### dispose[​](https://playwright.dev/docs/api/class-apiresponse#api-response-dispose "Direct link to dispose")

Added in: v1.16 apiResponse.dispose

Disposes the body of this response. If not called then the body will stay in memory until the context closes.

**Usage**

```
    await apiResponse.dispose();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-dispose-return)

---

### headers[​](https://playwright.dev/docs/api/class-apiresponse#api-response-headers "Direct link to headers")

Added in: v1.16 apiResponse.headers

An object with all the response HTTP headers associated with this response.

**Usage**

```
    apiResponse.headers();

```

**Returns**

- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-headers-return)

---

### headersArray[​](https://playwright.dev/docs/api/class-apiresponse#api-response-headers-array "Direct link to headersArray")

Added in: v1.16 apiResponse.headersArray

An array with all the response HTTP headers associated with this response. Header names are not lower-cased. Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.

**Usage**

```
    apiResponse.headersArray();

```

**Returns**

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-headers-array-return)
  - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

Name of the header.

    * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

Value of the header.

---

### json[​](https://playwright.dev/docs/api/class-apiresponse#api-response-json "Direct link to json")

Added in: v1.16 apiResponse.json

Returns the JSON representation of response body.

This method will throw if the response body is not parsable via `JSON.parse`.

**Usage**

```
    await apiResponse.json();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-json-return)

---

### ok[​](https://playwright.dev/docs/api/class-apiresponse#api-response-ok "Direct link to ok")

Added in: v1.16 apiResponse.ok

Contains a boolean stating whether the response was successful (status in the range 200-299) or not.

**Usage**

```
    apiResponse.ok();

```

**Returns**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-ok-return)

---

### status[​](https://playwright.dev/docs/api/class-apiresponse#api-response-status "Direct link to status")

Added in: v1.16 apiResponse.status

Contains the status code of the response (e.g., 200 for a success).

**Usage**

```
    apiResponse.status();

```

**Returns**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-status-return)

---

### statusText[​](https://playwright.dev/docs/api/class-apiresponse#api-response-status-text "Direct link to statusText")

Added in: v1.16 apiResponse.statusText

Contains the status text of the response (e.g. usually an "OK" for a success).

**Usage**

```
    apiResponse.statusText();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-status-text-return)

---

### text[​](https://playwright.dev/docs/api/class-apiresponse#api-response-text "Direct link to text")

Added in: v1.16 apiResponse.text

Returns the text representation of response body.

**Usage**

```
    await apiResponse.text();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")>[#](https://playwright.dev/docs/api/class-apiresponse#api-response-text-return)

---

### url[​](https://playwright.dev/docs/api/class-apiresponse#api-response-url "Direct link to url")

Added in: v1.16 apiResponse.url

Contains the URL of the response.

**Usage**

```
    apiResponse.url();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apiresponse#api-response-url-return)
