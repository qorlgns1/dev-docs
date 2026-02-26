---
title: "APIRequest"
description: "Web API 테스트에 사용할 수 있는 API를 제공합니다. 이 클래스는 APIRequestContext 인스턴스를 생성하는 데 사용되며, 생성된 인스턴스는 웹 요청 전송에 사용할 수 있습니다. 이 클래스의 인스턴스는 playwright.request를 통해 얻을 수 ..."
---

소스 URL: https://playwright.dev/docs/api/class-apirequest

# APIRequest | Playwright

Web API 테스트에 사용할 수 있는 API를 제공합니다. 이 클래스는 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext") 인스턴스를 생성하는 데 사용되며, 생성된 인스턴스는 웹 요청 전송에 사용할 수 있습니다. 이 클래스의 인스턴스는 [playwright.request](https://playwright.dev/docs/api/class-playwright#playwright-request)를 통해 얻을 수 있습니다. 자세한 내용은 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")를 참고하세요.

---

## 메서드[​](https://playwright.dev/docs/api/class-apirequest#methods "Direct link to Methods")

### newContext[​](https://playwright.dev/docs/api/class-apirequest#api-request-new-context "Direct link to newContext")

추가된 버전: v1.16 apiRequest.newContext

새로운 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext") 인스턴스를 생성합니다.

**사용법**

```
    await apiRequest.newContext();
    await apiRequest.newContext(options);

```

**인수**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `baseURL` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-base-url)

[apiRequestContext.get()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-get) 같은 메서드는 해당 URL을 구성할 때 [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) 생성자를 사용하여 base URL을 고려합니다. 예시:

      * baseURL: `http://localhost:3000` 이고 요청을 `/bar.html` 로 보내면 결과는 `http://localhost:3000/bar.html`
      * baseURL: `http://localhost:3000/foo/` 이고 요청을 `./bar.html` 로 보내면 결과는 `http://localhost:3000/foo/bar.html`
      * baseURL: `http://localhost:3000/foo` (후행 슬래시 없음)이고 `./bar.html` 로 이동하면 결과는 `http://localhost:3000/bar.html`
    * `clientCertificates` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")> _(optional)_ Added in: 1.46[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-client-certificates)

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

인증서가 유효한 정확한 origin입니다. Origin에는 `https` 프로토콜, 호스트명, 그리고 선택적으로 포트가 포함됩니다.

      * `certPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PEM 형식 인증서가 들어 있는 파일 경로입니다.

      * `cert` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PEM 형식 인증서의 직접 값입니다.

      * `keyPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PEM 형식 개인 키가 들어 있는 파일 경로입니다.

      * `key` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PEM 형식 개인 키의 직접 값입니다.

      * `pfxPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

PFX 또는 PKCS12로 인코딩된 개인 키 및 인증서 체인 파일 경로입니다.

      * `pfx` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer") _(optional)_

PFX 또는 PKCS12로 인코딩된 개인 키 및 인증서 체인의 직접 값입니다.

      * `passphrase` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

개인 키(PEM 또는 PFX)의 암호문구입니다.

TLS 클라이언트 인증을 사용하면 서버가 클라이언트 인증서를 요청하고 이를 검증할 수 있습니다.

**세부사항**

사용할 클라이언트 인증서 배열입니다. 각 인증서 객체는 `certPath`와 `keyPath`를 모두 가지거나, 단일 `pfxPath`를 가지거나, 이에 해당하는 직접 값(`cert`와 `key` 또는 `pfx`)을 가져야 합니다. 인증서가 암호화되어 있다면 선택적으로 `passphrase` 속성을 제공해야 합니다. `origin` 속성은 인증서가 유효한 요청 origin과 정확히 일치하도록 제공해야 합니다.

클라이언트 인증서 인증은 클라이언트 인증서가 하나 이상 제공될 때만 활성화됩니다. 서버가 보내는 모든 클라이언트 인증서를 거부하려면, 방문할 도메인과 일치하지 않는 `origin`을 가진 클라이언트 인증서를 제공해야 합니다.

note

macOS에서 WebKit을 사용할 때 `localhost`에 접근하면 클라이언트 인증서가 적용되지 않습니다. `localhost`를 `local.playwright`로 바꾸면 동작하게 만들 수 있습니다.

    * `extraHTTPHeaders` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")> _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-extra-http-headers)

모든 요청과 함께 전송할 추가 HTTP 헤더를 담은 객체입니다. 기본값은 없음입니다.

    * `failOnStatusCode` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.51[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-fail-on-status-code)

2xx 및 3xx 외의 응답 코드에서 예외를 던질지 여부입니다. 기본적으로는 모든 상태 코드에 대해 응답 객체를 반환합니다.

    * `httpCredentials` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-http-credentials)

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

      * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

특정 origin(scheme://host:port)에서만 http 자격 증명을 전송하도록 제한합니다.

      * `send` "unauthorized" | "always" _(optional)_

이 옵션은 해당 [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")에서 전송되는 요청에만 적용되며 브라우저에서 전송되는 요청에는 영향을 주지 않습니다. `'always'` \- 각 API 요청마다 기본 인증 자격 증명이 포함된 `Authorization` 헤더가 전송됩니다. `'unauthorized` \- `WWW-Authenticate` 헤더가 있는 401 (Unauthorized) 응답을 받았을 때만 자격 증명이 전송됩니다. 기본값은 `'unauthorized'`입니다.

[HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)을 위한 자격 증명입니다. origin을 지정하지 않으면 인증되지 않은 응답 시 사용자 이름과 비밀번호가 모든 서버로 전송됩니다.

    * `ignoreHTTPSErrors` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-ignore-https-errors)

네트워크 요청 전송 시 HTTPS 오류를 무시할지 여부입니다. 기본값은 `false`입니다.

    * `maxRedirects` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_ Added in: v1.52[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-max-redirects)

자동으로 따라갈 요청 리디렉션의 최대 횟수입니다. 이 값을 초과하면 오류가 발생합니다. 기본값은 `20`입니다. 리디렉션을 따르지 않으려면 `0`을 전달하세요. 이 값은 각 요청별로 개별 재정의할 수 있습니다.

    * `proxy` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-proxy)

      * `server` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

모든 요청에 사용할 프록시입니다. HTTP 및 SOCKS 프록시를 지원하며, 예: `http://myproxy.com:3128` 또는 `socks5://myproxy.com:3128`. 축약형 `myproxy.com:3128`은 HTTP 프록시로 간주됩니다.

      * `bypass` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

프록시를 우회할 도메인 목록(쉼표로 구분)입니다. 예: `".com, chromium.org, .domain.com"`.

      * `username` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요할 때 사용할 선택적 사용자 이름입니다.

      * `password` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_

HTTP 프록시에 인증이 필요할 때 사용할 선택적 비밀번호입니다.

네트워크 프록시 설정입니다.

    * `storageState` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-storage-state)

      * `cookies` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `domain` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `expires` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

초 단위 Unix 시간입니다.

        * `httpOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

        * `secure` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")

        * `sameSite` "Strict" | "Lax" | "None"

      * `origins` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

        * `origin` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        * `localStorage` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>

          * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

          * `value` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

주어진 storage state로 컨텍스트를 채웁니다. 이 옵션은 [browserContext.storageState()](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state) 또는 [apiRequestContext.storageState()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-storage-state)에서 가져온 로그인 정보를 사용해 컨텍스트를 초기화하는 데 사용할 수 있습니다. 저장된 스토리지가 있는 파일 경로 또는 [browserContext.storageState()](https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state) / [apiRequestContext.storageState()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-storage-state) 메서드 중 하나가 반환한 값을 전달할 수 있습니다.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-timeout)

응답을 기다리는 최대 시간(밀리초)입니다. 기본값은 `30000`(30초)입니다. 타임아웃을 비활성화하려면 `0`을 전달하세요.

    * `userAgent` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") _(optional)_[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-option-user-agent)

이 컨텍스트에서 사용할 특정 user agent입니다.

**반환값**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")>[#](https://playwright.dev/docs/api/class-apirequest#api-request-new-context-return)
