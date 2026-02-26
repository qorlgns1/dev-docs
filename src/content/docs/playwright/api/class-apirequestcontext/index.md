---
title: "APIRequestContext"
description: "이 API는 Web API 테스트에 사용됩니다. 이를 사용해 API 엔드포인트를 트리거하고, 마이크로서비스를 구성하며, e2e 테스트를 위한 환경 또는 서비스를 준비할 수 있습니다."
---

Source URL: https://playwright.dev/docs/api/class-apirequestcontext

# APIRequestContext | Playwright

이 API는 Web API 테스트에 사용됩니다. 이를 사용해 API 엔드포인트를 트리거하고, 마이크로서비스를 구성하며, e2e 테스트를 위한 환경 또는 서비스를 준비할 수 있습니다.

각 Playwright 브라우저 컨텍스트에는 쿠키 저장소를 브라우저 컨텍스트와 공유하는 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext") 인스턴스가 연결되어 있으며, [browserContext.request](https://playwright.dev/docs/api/class-browsercontext#browser-context-request) 또는 [page.request](https://playwright.dev/docs/api/class-page#page-request)를 통해 접근할 수 있습니다. 또한 [apiRequest.newContext()](https://playwright.dev/docs/api/class-apirequest#api-request-new-context)를 호출해 새 APIRequestContext 인스턴스를 수동으로 생성할 수도 있습니다.

**쿠키 관리**

[browserContext.request](https://playwright.dev/docs/api/class-browsercontext#browser-context-request) 및 [page.request](https://playwright.dev/docs/api/class-page#page-request)에서 반환되는 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")는 해당 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")와 쿠키 저장소를 공유합니다. 각 API 요청은 브라우저 컨텍스트의 값으로 채워진 `Cookie` 헤더를 포함합니다. API 응답에 `Set-Cookie` 헤더가 있으면 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext") 쿠키가 자동으로 업데이트되고, 페이지에서 보내는 요청도 이를 반영합니다. 즉, 이 API를 사용해 로그인하면 e2e 테스트도 로그인된 상태가 되며, 그 반대도 마찬가지입니다.

API 요청이 브라우저 쿠키에 영향을 주지 않게 하려면 [apiRequest.newContext()](https://playwright.dev/docs/api/class-apirequest#api-request-new-context)를 호출해 새 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")를 생성해야 합니다. 이렇게 생성된 `APIRequestContext` 객체는 자체적으로 격리된 쿠키 저장소를 가집니다.

---

## 메서드[​](https://playwright.dev/docs/api/class-apirequestcontext#methods "메서드로 바로 가기")

### delete[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete "delete로 바로 가기")

추가된 버전: v1.16 apiRequestContext.delete

HTTP(S) [DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) 요청을 보내고 응답을 반환합니다. 이 메서드는 컨텍스트에서 요청 쿠키를 채우고 응답의 쿠키로 컨텍스트 쿠키를 업데이트합니다. 또한 리다이렉트를 자동으로 따라갑니다.

**사용법**

```
    await apiRequestContext.delete(url);
    await apiRequestContext.delete(url, options);

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-url)

대상 URL.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `data` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") | [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_ Added in: v1.17[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-data)

요청의 post data를 설정할 수 있습니다. `data` 파라미터가 객체이면 json 문자열로 직렬화되며, 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/json`으로 설정됩니다. 그렇지 않으면 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/octet-stream`으로 설정됩니다.

    * `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-fail-on-status-code)

2xx 및 3xx 이외의 응답 코드에서 예외를 던질지 여부입니다. 기본값은 모든 상태 코드에 대해 응답 객체를 반환합니다.

    * `form` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") _(optional)_ Added in: v1.17[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-form)

`application/x-www-form-urlencoded` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 파라미터가 지정되면 명시적으로 제공하지 않는 한 `content-type` 헤더가 `application/x-www-form-urlencoded`로 설정됩니다.

    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-headers)

HTTP 헤더를 설정할 수 있습니다. 이 헤더는 해당 요청과, 그 요청으로 인해 발생하는 모든 리다이렉트에 적용됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-max-redirects)

자동으로 따라갈 요청 리다이렉트의 최대 횟수입니다. 이 수를 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리다이렉트를 따라가지 않으려면 `0`을 전달하세요.

    * `maxRetries` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.46[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-max-retries)

네트워크 오류 재시도의 최대 횟수입니다. 현재는 `ECONNRESET` 오류만 재시도합니다. HTTP 응답 코드 기준으로는 재시도하지 않습니다. 한도를 초과하면 오류가 발생합니다. 기본값은 `0` \- 재시도 없음입니다.

    * `multipart` [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [ReadStream](https://nodejs.org/api/fs.html#class-fsreadstream "ReadStream") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_ Added in: v1.17[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-multipart)

      * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

      * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 유형

      * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

`multipart/form-data` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 파라미터가 지정되면 명시적으로 제공하지 않는 한 `content-type` 헤더가 `multipart/form-data`로 설정됩니다. 파일 값은 [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 또는 파일 이름, mime-type, 내용이 포함된 파일 유사 객체로 전달할 수 있습니다.

    * `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams "URLSearchParams") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-params)

URL과 함께 전송할 쿼리 파라미터입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-option-timeout)

요청 타임아웃(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-delete-return)

---

### dispose[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-dispose "dispose로 바로 가기")

추가된 버전: v1.16 apiRequestContext.dispose

[apiRequestContext.get()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get) 및 유사 메서드가 반환한 모든 응답은 이후 [apiResponse.body()](https://playwright.dev/docs/api/class-apiresponse#api-response-body)를 호출할 수 있도록 메모리에 저장됩니다. 이 메서드는 해당 리소스를 모두 폐기하며, 폐기된 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")에서 어떤 메서드든 호출하면 예외가 발생합니다.

**사용법**

```
    await apiRequestContext.dispose();
    await apiRequestContext.dispose(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `reason` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_ Added in: v1.45[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-dispose-option-reason)

컨텍스트 폐기로 인해 중단되는 작업에 보고할 사유입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-dispose-return)

---

### fetch[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch "fetch로 바로 가기")

추가된 버전: v1.16 apiRequestContext.fetch

HTTP(S) 요청을 보내고 해당 응답을 반환합니다. 이 메서드는 컨텍스트에서 요청 쿠키를 채우고, 응답의 쿠키로 컨텍스트 쿠키를 업데이트합니다. 또한 리디렉션을 자동으로 따라갑니다.

**사용법**

JSON 객체는 요청에 직접 전달할 수 있습니다:

```
    await request.fetch('https://example.com/api/createBook', {
      method: 'post',
      data: {
        title: 'Book Title',
        author: 'John Doe',
      }
    });

```

요청 본문에 파일을 보내는 일반적인 방법은 `multipart` 파라미터를 지정해 `multipart/form-data` 인코딩의 form 필드로 업로드하는 것입니다:

```
    const form = new FormData();
    form.set('name', 'John');
    form.append('name', 'Doe');
    // Send two file fields with the same name.
    form.append('file', new File(['console.log(2024);'], 'f1.js', { type: 'text/javascript' }));
    form.append('file', new File(['hello'], 'f2.txt', { type: 'text/plain' }));
    await request.fetch('https://example.com/api/uploadForm', {
      multipart: form
    });

```

**인수**

- `urlOrRequest` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Request](https://playwright.dev/docs/api/class-request "Request")[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-url-or-request)

모든 파라미터를 가져올 대상 URL 또는 Request입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `data` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") | [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-data)

요청의 post data를 설정할 수 있습니다. `data` 파라미터가 객체이면 json 문자열로 직렬화되며, 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/json`으로 설정됩니다. 그렇지 않으면 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/octet-stream`으로 설정됩니다.

    * `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-fail-on-status-code)

2xx 및 3xx가 아닌 응답 코드에서 오류를 발생시킬지 여부입니다. 기본적으로 모든 상태 코드에 대해 response 객체를 반환합니다.

    * `form` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-form)

`application/x-www-form-urlencoded` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 파라미터를 지정하면 명시적으로 제공하지 않는 한 `content-type` 헤더는 `application/x-www-form-urlencoded`로 설정됩니다.

    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-headers)

HTTP 헤더를 설정할 수 있습니다. 이 헤더는 fetch된 요청과 해당 요청이 시작한 모든 리디렉션에 적용됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-max-redirects)

자동으로 따라갈 요청 리디렉션의 최대 횟수입니다. 이 횟수를 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리디렉션을 따르지 않으려면 `0`을 전달하세요.

    * `maxRetries` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.46[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-max-retries)

네트워크 오류를 재시도할 최대 횟수입니다. 현재는 `ECONNRESET` 오류만 재시도합니다. HTTP 응답 코드를 기준으로는 재시도하지 않습니다. 한도를 초과하면 오류가 발생합니다. 기본값은 `0` \- 재시도 없음입니다.

    * `method` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-method)

설정하면 fetch 메서드를 변경합니다(예: [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT), [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)). 지정하지 않으면 GET 메서드가 사용됩니다.

    * `multipart` [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [ReadStream](https://nodejs.org/api/fs.html#class-fsreadstream "ReadStream") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-multipart)

      * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

      * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 유형

      * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

`multipart/form-data` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 파라미터를 지정하면 명시적으로 제공하지 않는 한 `content-type` 헤더는 `multipart/form-data`로 설정됩니다. 파일 값은 [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 또는 파일 이름, mime-type, 콘텐츠를 포함한 파일 유사 객체로 전달할 수 있습니다.

    * `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams "URLSearchParams") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-params)

URL과 함께 전송할 쿼리 파라미터입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-option-timeout)

요청 타임아웃(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-fetch-return)

---

### get[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get "Direct link to get")

추가된 버전: v1.16 apiRequestContext.get

HTTP(S) [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) 요청을 보내고 해당 응답을 반환합니다. 이 메서드는 컨텍스트에서 요청 쿠키를 채우고, 응답의 쿠키로 컨텍스트 쿠키를 업데이트합니다. 또한 리디렉션을 자동으로 따라갑니다.

**사용법**

요청 파라미터는 `params` 옵션으로 구성할 수 있으며 URL 검색 파라미터로 직렬화됩니다:

```
    // Passing params as object
    await request.get('https://example.com/api/getText', {
      params: {
        'isbn': '1234',
        'page': 23,
      }
    });

    // Passing params as URLSearchParams
    const searchParams = new URLSearchParams();
    searchParams.set('isbn', '1234');
    searchParams.append('page', 23);
    searchParams.append('page', 24);
    await request.get('https://example.com/api/getText', { params: searchParams });

    // Passing params as string
    const queryString = 'isbn=1234&page=23&page=24';
    await request.get('https://example.com/api/getText', { params: queryString });

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-url)

대상 URL입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `data` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") | [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-data)

요청의 post data를 설정할 수 있습니다. `data` 파라미터가 객체이면 json 문자열로 직렬화되며, 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/json`으로 설정됩니다. 그렇지 않으면 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/octet-stream`으로 설정됩니다.

    * `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-fail-on-status-code)

2xx 및 3xx가 아닌 응답 코드에서 오류를 발생시킬지 여부입니다. 기본적으로 모든 상태 코드에 대해 response 객체를 반환합니다.

    * `form` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-form)

`application/x-www-form-urlencoded` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 파라미터를 지정하면 명시적으로 제공하지 않는 한 `content-type` 헤더는 `application/x-www-form-urlencoded`로 설정됩니다.

- `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-headers)

HTTP 헤더를 설정할 수 있습니다. 이 헤더는 가져온 요청과 해당 요청으로 시작된 모든 리디렉션에 적용됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-ignore-https-errors)

네트워크 요청을 보낼 때 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-max-redirects)

자동으로 따라갈 요청 리디렉션의 최대 횟수입니다. 이 수를 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리디렉션을 따르지 않으려면 `0`을 전달하세요.

    * `maxRetries` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.46[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-max-retries)

네트워크 오류 재시도의 최대 횟수입니다. 현재는 `ECONNRESET` 오류만 재시도합니다. HTTP 응답 코드 기반으로는 재시도하지 않습니다. 한도를 초과하면 오류가 발생합니다. 기본값은 `0` \- 재시도 없음입니다.

    * `multipart` [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [ReadStream](https://nodejs.org/api/fs.html#class-fsreadstream "ReadStream") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-multipart)

      * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

      * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 유형

      * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

`multipart/form-data` 인코딩을 사용해 html form으로 직렬화되고 이 요청 본문으로 전송될 객체를 제공합니다. 이 매개변수가 지정되면, 명시적으로 제공되지 않은 경우 `content-type` 헤더가 `multipart/form-data`로 설정됩니다. 파일 값은 [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 또는 파일 이름, mime-type, 내용을 포함하는 파일 유사 객체로 전달할 수 있습니다.

    * `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams "URLSearchParams") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-params)

URL과 함께 전송할 쿼리 매개변수입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-option-timeout)

밀리초 단위 요청 타임아웃입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get-return)

---

### head[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head "Direct link to head")

추가된 버전: v1.16 apiRequestContext.head

HTTP(S) [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) 요청을 보내고 해당 응답을 반환합니다. 이 메서드는 컨텍스트에서 요청 쿠키를 채우고 응답으로 컨텍스트 쿠키를 업데이트합니다. 또한 자동으로 리디렉션을 따라갑니다.

**사용법**

```
    await apiRequestContext.head(url);
    await apiRequestContext.head(url, options);

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-url)

대상 URL.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `data` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") | [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-data)

요청의 post data를 설정할 수 있습니다. data 매개변수가 객체이면 JSON 문자열로 직렬화되며, 명시적으로 설정되지 않은 경우 `content-type` 헤더가 `application/json`으로 설정됩니다. 그렇지 않으면, 명시적으로 설정되지 않은 경우 `content-type` 헤더가 `application/octet-stream`으로 설정됩니다.

    * `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-fail-on-status-code)

2xx 및 3xx 이외의 응답 코드에서 예외를 발생시킬지 여부입니다. 기본적으로는 모든 상태 코드에 대해 응답 객체를 반환합니다.

    * `form` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-form)

`application/x-www-form-urlencoded` 인코딩을 사용해 html form으로 직렬화되고 이 요청 본문으로 전송될 객체를 제공합니다. 이 매개변수가 지정되면, 명시적으로 제공되지 않은 경우 `content-type` 헤더가 `application/x-www-form-urlencoded`로 설정됩니다.

    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-headers)

HTTP 헤더를 설정할 수 있습니다. 이 헤더는 가져온 요청과 해당 요청으로 시작된 모든 리디렉션에 적용됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-ignore-https-errors)

네트워크 요청을 보낼 때 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-max-redirects)

자동으로 따라갈 요청 리디렉션의 최대 횟수입니다. 이 수를 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리디렉션을 따르지 않으려면 `0`을 전달하세요.

    * `maxRetries` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.46[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-max-retries)

네트워크 오류 재시도의 최대 횟수입니다. 현재는 `ECONNRESET` 오류만 재시도합니다. HTTP 응답 코드 기반으로는 재시도하지 않습니다. 한도를 초과하면 오류가 발생합니다. 기본값은 `0` \- 재시도 없음입니다.

    * `multipart` [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [ReadStream](https://nodejs.org/api/fs.html#class-fsreadstream "ReadStream") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-multipart)

      * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

      * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 유형

      * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

`multipart/form-data` 인코딩을 사용해 html form으로 직렬화되고 이 요청 본문으로 전송될 객체를 제공합니다. 이 매개변수가 지정되면, 명시적으로 제공되지 않은 경우 `content-type` 헤더가 `multipart/form-data`로 설정됩니다. 파일 값은 [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 또는 파일 이름, mime-type, 내용을 포함하는 파일 유사 객체로 전달할 수 있습니다.

- `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams "URLSearchParams") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-params)

URL과 함께 전송할 쿼리 파라미터입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-option-timeout)

요청 제한 시간을 밀리초 단위로 지정합니다. 기본값은 `30000`(30초)입니다. 제한 시간을 비활성화하려면 `0`을 전달하세요.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-head-return)

---

### patch[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch "Direct link to patch")

추가됨: v1.16 apiRequestContext.patch

HTTP(S) [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) 요청을 보내고 해당 응답을 반환합니다. 이 메서드는 컨텍스트의 요청 쿠키를 채워 넣고, 응답의 쿠키로 컨텍스트 쿠키를 업데이트합니다. 또한 리디렉션을 자동으로 따라갑니다.

**Usage**

```
    await apiRequestContext.patch(url);
    await apiRequestContext.patch(url, options);

```

**Arguments**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-url)

대상 URL.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `data` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") | [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-data)

요청의 post 데이터를 설정할 수 있습니다. `data` 파라미터가 객체이면 JSON 문자열로 직렬화되며, 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/json`으로 설정됩니다. 그렇지 않으면, 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/octet-stream`으로 설정됩니다.

    * `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-fail-on-status-code)

2xx 및 3xx 이외의 응답 코드에서 예외를 발생시킬지 여부입니다. 기본적으로는 모든 상태 코드에 대해 응답 객체를 반환합니다.

    * `form` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-form)

`application/x-www-form-urlencoded` 인코딩을 사용한 HTML form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 파라미터가 지정되면, 명시적으로 제공하지 않는 한 `content-type` 헤더는 `application/x-www-form-urlencoded`로 설정됩니다.

    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-headers)

HTTP 헤더를 설정할 수 있습니다. 이 헤더는 가져온 요청과 해당 요청으로 시작된 모든 리디렉션에 적용됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-max-redirects)

자동으로 따라갈 요청 리디렉션의 최대 횟수입니다. 이 수를 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리디렉션을 따르지 않으려면 `0`을 전달하세요.

    * `maxRetries` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.46[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-max-retries)

네트워크 오류 재시도 최대 횟수입니다. 현재는 `ECONNRESET` 오류만 재시도합니다. HTTP 응답 코드를 기준으로는 재시도하지 않습니다. 제한을 초과하면 오류가 발생합니다. 기본값은 `0` \- 재시도 없음입니다.

    * `multipart` [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [ReadStream](https://nodejs.org/api/fs.html#class-fsreadstream "ReadStream") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-multipart)

      * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

      * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 타입

      * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

`multipart/form-data` 인코딩을 사용한 HTML form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 파라미터가 지정되면, 명시적으로 제공하지 않는 한 `content-type` 헤더는 `multipart/form-data`로 설정됩니다. 파일 값은 [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 또는 파일 이름, mime-type, 내용을 포함한 파일 유사 객체로 전달할 수 있습니다.

    * `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams "URLSearchParams") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-params)

URL과 함께 전송할 쿼리 파라미터입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-option-timeout)

요청 제한 시간을 밀리초 단위로 지정합니다. 기본값은 `30000`(30초)입니다. 제한 시간을 비활성화하려면 `0`을 전달하세요.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-patch-return)

---

### post[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post "Direct link to post")

추가됨: v1.16 apiRequestContext.post

HTTP(S) [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) 요청을 보내고 해당 응답을 반환합니다. 이 메서드는 컨텍스트의 요청 쿠키를 채워 넣고, 응답의 쿠키로 컨텍스트 쿠키를 업데이트합니다. 또한 리디렉션을 자동으로 따라갑니다.

**Usage**

JSON 객체는 요청에 직접 전달할 수 있습니다:

```
    await request.post('https://example.com/api/createBook', {
      data: {
        title: 'Book Title',
        author: 'John Doe',
      }
    });

```

서버에 form 데이터를 보내려면 `form` 옵션을 사용하세요. 이 값은 `application/x-www-form-urlencoded` 인코딩으로 요청 본문에 인코딩됩니다(파일 전송을 위해 `multipart/form-data` form 인코딩을 사용하는 방법은 아래 참고):

```
    await request.post('https://example.com/api/findBook', {
      form: {
        title: 'Book Title',
        author: 'John Doe',
      }
    });

```

요청 본문에 파일을 보내는 일반적인 방법은 `multipart/form-data` 인코딩의 form 필드로 업로드하는 것입니다. 요청 본문을 구성하려면 [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData")를 사용하고, 이를 `multipart` 파라미터로 요청에 전달하세요:

```
    const form = new FormData();
    form.set('name', 'John');
    form.append('name', 'Doe');
    // Send two file fields with the same name.
    form.append('file', new File(['console.log(2024);'], 'f1.js', { type: 'text/javascript' }));
    form.append('file', new File(['hello'], 'f2.txt', { type: 'text/plain' }));
    await request.post('https://example.com/api/uploadForm', {
      multipart: form
    });

```

**Arguments**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-url)

대상 URL.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `data` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") | [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-data)

요청의 post 데이터를 설정할 수 있습니다. `data` 파라미터가 객체이면 JSON 문자열로 직렬화되며, 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/json`으로 설정됩니다. 그렇지 않으면, 명시적으로 설정하지 않은 경우 `content-type` 헤더는 `application/octet-stream`으로 설정됩니다.

- `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-fail-on-status-code)

응답 코드가 2xx 및 3xx 이외일 때 예외를 throw할지 여부입니다. 기본적으로는 모든 상태 코드에 대해 response 객체가 반환됩니다.

    * `form` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-form)

`application/x-www-form-urlencoded` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 매개변수가 지정되면 명시적으로 제공되지 않은 경우 `content-type` 헤더는 `application/x-www-form-urlencoded`로 설정됩니다.

    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-headers)

HTTP 헤더를 설정할 수 있습니다. 이 헤더는 가져온 요청뿐 아니라 해당 요청으로 시작된 모든 리디렉션에도 적용됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-max-redirects)

자동으로 따라갈 요청 리디렉션의 최대 횟수입니다. 횟수를 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리디렉션을 따르지 않으려면 `0`을 전달하세요.

    * `maxRetries` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.46[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-max-retries)

네트워크 오류 재시도의 최대 횟수입니다. 현재는 `ECONNRESET` 오류만 재시도합니다. HTTP 응답 코드를 기준으로 재시도하지는 않습니다. 한도를 초과하면 오류가 발생합니다. 기본값은 `0` \- 재시도 없음입니다.

    * `multipart` [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [ReadStream](https://nodejs.org/api/fs.html#class-fsreadstream "ReadStream") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-multipart)

      * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

      * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 유형

      * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

`multipart/form-data` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 매개변수가 지정되면 명시적으로 제공되지 않은 경우 `content-type` 헤더는 `multipart/form-data`로 설정됩니다. 파일 값은 [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 또는 파일 이름, mime-type, 내용을 포함하는 파일 유사 객체로 전달할 수 있습니다.

    * `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams "URLSearchParams") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-params)

URL과 함께 전송할 쿼리 매개변수입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-option-timeout)

요청 타임아웃(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post-return)

---

### put[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put "Direct link to put")

추가된 버전: v1.16 apiRequestContext.put

HTTP(S) [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) 요청을 보내고 해당 응답을 반환합니다. 이 메서드는 컨텍스트의 요청 쿠키를 채우고, 응답의 쿠키로 컨텍스트 쿠키를 업데이트합니다. 또한 리디렉션을 자동으로 따릅니다.

**사용법**

```
    await apiRequestContext.put(url);
    await apiRequestContext.put(url, options);

```

**인수**

- `url` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-url)

대상 URL입니다.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `data` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") | [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-data)

요청의 post data를 설정할 수 있습니다. `data` 매개변수가 객체이면 JSON 문자열로 직렬화되며, 명시적으로 설정되지 않은 경우 `content-type` 헤더는 `application/json`으로 설정됩니다. 그렇지 않으면 명시적으로 설정되지 않은 경우 `content-type` 헤더는 `application/octet-stream`으로 설정됩니다.

    * `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-fail-on-status-code)

응답 코드가 2xx 및 3xx 이외일 때 예외를 throw할지 여부입니다. 기본적으로는 모든 상태 코드에 대해 response 객체가 반환됩니다.

    * `form` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-form)

`application/x-www-form-urlencoded` 인코딩을 사용해 html form으로 직렬화되어 요청 본문으로 전송될 객체를 제공합니다. 이 매개변수가 지정되면 명시적으로 제공되지 않은 경우 `content-type` 헤더는 `application/x-www-form-urlencoded`로 설정됩니다.

    * `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-headers)

HTTP 헤더를 설정할 수 있습니다. 이 헤더는 가져온 요청뿐 아니라 해당 요청으로 시작된 모든 리디렉션에도 적용됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.26[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-max-redirects)

자동으로 따라갈 요청 리디렉션의 최대 횟수입니다. 횟수를 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리디렉션을 따르지 않으려면 `0`을 전달하세요.

    * `maxRetries` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.46[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-max-retries)

네트워크 오류 재시도의 최대 횟수입니다. 현재는 `ECONNRESET` 오류만 재시도합니다. HTTP 응답 코드를 기준으로 재시도하지는 않습니다. 한도를 초과하면 오류가 발생합니다. 기본값은 `0` \- 재시도 없음입니다.

- `multipart` [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData "FormData") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") | [ReadStream](https://nodejs.org/api/fs.html#class-fsreadstream "ReadStream") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-multipart)

      * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 이름

      * `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

파일 타입

      * `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

파일 내용

이 요청 본문으로 전송되도록 `multipart/form-data` 인코딩을 사용하는 html form으로 직렬화될 객체를 제공합니다. 이 매개변수가 지정되면 명시적으로 제공되지 않은 경우 `content-type` 헤더가 `multipart/form-data`로 설정됩니다. 파일 값은 [`fs.ReadStream`](https://nodejs.org/api/fs.html#fs_class_fs_readstream) 또는 파일 이름, mime-type, 콘텐츠를 포함한 파일 유사 객체로 전달할 수 있습니다.

    * `params` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")> | [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams "URLSearchParams") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-params)

URL과 함께 전송할 쿼리 매개변수입니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-option-timeout)

밀리초 단위 요청 타임아웃입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIResponse](https://playwright.dev/docs/api/class-apiresponse "APIResponse")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-put-return)

---

### storageState[​](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-storage-state "Direct link to storageState")

추가된 버전: v1.16 apiRequestContext.storageState

이 request context의 storage state를 반환합니다. 생성자에 전달된 경우 현재 쿠키와 local storage 스냅샷을 포함합니다.

**사용법**

```
    await apiRequestContext.storageState();
    await apiRequestContext.storageState(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `indexedDB` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ 추가된 버전: v1.51[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-storage-state-option-indexed-db)

storage state 스냅샷에 IndexedDB를 포함하려면 `true`로 설정합니다.

    * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-storage-state-option-path)

storage state를 저장할 파일 경로입니다. [path](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-storage-state-option-path)가 상대 경로이면 현재 작업 디렉터리를 기준으로 해석됩니다. path를 제공하지 않아도 storage state는 반환되지만 디스크에는 저장되지 않습니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-storage-state-return)
  - `cookies` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>
    - `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    - `expires` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

초 단위 Unix 시간입니다.

      * `httpOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

      * `secure` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

      * `sameSite` "Strict" | "Lax" | "None"

    * `origins` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `localStorage` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")
