---
title: 'API 레퍼런스: Edge Runtime'
description: '마지막 업데이트: 2026년 2월 20일'
---

# API 레퍼런스: Edge Runtime | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/edge

[Pages Router](https://nextjs.org/docs/pages)[API 레퍼런스](https://nextjs.org/docs/pages/api-reference)Edge Runtime

페이지 복사

# 엣지 런타임

마지막 업데이트: 2026년 2월 20일

Next.js 애플리케이션에서는 두 가지 서버 런타임을 사용할 수 있습니다.

  * **Node.js 런타임**(기본값): 모든 Node.js API에 접근할 수 있으며 애플리케이션을 렌더링할 때 사용됩니다.
  * **Edge Runtime**: [제한된 API 집합](https://nextjs.org/docs/pages/api-reference/edge#reference)을 제공하며 [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)에서 사용됩니다.



## 주의 사항[](https://nextjs.org/docs/pages/api-reference/edge#caveats)

  * Edge Runtime은 모든 Node.js API를 지원하지 않으므로 일부 패키지가 예상대로 동작하지 않을 수 있습니다.
  * Edge Runtime은 Incremental Static Regeneration(ISR)을 지원하지 않습니다.
  * 두 런타임 모두 배포 어댑터에 따라 [스트리밍](https://nextjs.org/docs/app/api-reference/file-conventions/loading)을 지원할 수 있습니다.



## 참조[](https://nextjs.org/docs/pages/api-reference/edge#reference)

Edge Runtime은 다음 API를 지원합니다.

### 네트워크 API[](https://nextjs.org/docs/pages/api-reference/edge#network-apis)

API| 설명  
---|---  
[`Blob`](https://developer.mozilla.org/docs/Web/API/Blob)| Blob을 나타냅니다  
[`fetch`](https://developer.mozilla.org/docs/Web/API/Fetch_API)| 리소스를 가져옵니다  
[`FetchEvent`](https://developer.mozilla.org/docs/Web/API/FetchEvent)| fetch 이벤트를 나타냅니다  
[`File`](https://developer.mozilla.org/docs/Web/API/File)| 파일을 나타냅니다  
[`FormData`](https://developer.mozilla.org/docs/Web/API/FormData)| 폼 데이터를 나타냅니다  
[`Headers`](https://developer.mozilla.org/docs/Web/API/Headers)| HTTP 헤더를 나타냅니다  
[`Request`](https://developer.mozilla.org/docs/Web/API/Request)| HTTP 요청을 나타냅니다  
[`Response`](https://developer.mozilla.org/docs/Web/API/Response)| HTTP 응답을 나타냅니다  
[`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams)| URL 검색 매개변수를 나타냅니다  
[`WebSocket`](https://developer.mozilla.org/docs/Web/API/WebSocket)| 웹소켓 연결을 나타냅니다  
  
### 인코딩 API[](https://nextjs.org/docs/pages/api-reference/edge#encoding-apis)

API| 설명  
---|---  
[`atob`](https://developer.mozilla.org/en-US/docs/Web/API/atob)| base-64로 인코딩된 문자열을 디코딩합니다  
[`btoa`](https://developer.mozilla.org/en-US/docs/Web/API/btoa)| 문자열을 base-64로 인코딩합니다  
[`TextDecoder`](https://developer.mozilla.org/docs/Web/API/TextDecoder)| Uint8Array를 문자열로 디코딩합니다  
[`TextDecoderStream`](https://developer.mozilla.org/docs/Web/API/TextDecoderStream)| 스트림을 위한 체이닝 가능한 디코더입니다  
[`TextEncoder`](https://developer.mozilla.org/docs/Web/API/TextEncoder)| 문자열을 Uint8Array로 인코딩합니다  
[`TextEncoderStream`](https://developer.mozilla.org/docs/Web/API/TextEncoderStream)| 스트림을 위한 체이닝 가능한 인코더입니다  
  
### 스트림 API[](https://nextjs.org/docs/pages/api-reference/edge#stream-apis)

API| 설명  
---|---  
[`ReadableStream`](https://developer.mozilla.org/docs/Web/API/ReadableStream)| 읽기 가능한 스트림을 나타냅니다  
[`ReadableStreamBYOBReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBReader)| ReadableStream의 리더를 나타냅니다  
[`ReadableStreamDefaultReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamDefaultReader)| ReadableStream의 리더를 나타냅니다  
[`TransformStream`](https://developer.mozilla.org/docs/Web/API/TransformStream)| 변환 스트림을 나타냅니다  
[`WritableStream`](https://developer.mozilla.org/docs/Web/API/WritableStream)| 쓰기 가능한 스트림을 나타냅니다  
[`WritableStreamDefaultWriter`](https://developer.mozilla.org/docs/Web/API/WritableStreamDefaultWriter)| WritableStream의 라이터를 나타냅니다  
  
### 암호화 API[](https://nextjs.org/docs/pages/api-reference/edge#crypto-apis)

API| 설명  
---|---  
[`crypto`](https://developer.mozilla.org/docs/Web/API/Window/crypto)| 플랫폼의 암호화 기능에 접근합니다  
[`CryptoKey`](https://developer.mozilla.org/docs/Web/API/CryptoKey)| 암호화 키를 나타냅니다  
[`SubtleCrypto`](https://developer.mozilla.org/docs/Web/API/SubtleCrypto)| 해시, 서명, 암호화 또는 복호화와 같은 일반적인 암호화 프리미티브에 접근합니다  
  
### 웹 표준 API[](https://nextjs.org/docs/pages/api-reference/edge#web-standard-apis)

API| 설명  
---|---  
[`AbortController`](https://developer.mozilla.org/docs/Web/API/AbortController)| 원하는 시점에 하나 이상의 DOM 요청을 중단할 수 있습니다  
[`Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)| 값의 배열을 나타냅니다  
[`ArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)| 고정 길이 원시 이진 데이터 버퍼를 나타냅니다  
[`Atomics`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Atomics)| 정적 메서드로 원자적 연산을 제공합니다  
[`BigInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt)| 임의 정밀도의 정수를 나타냅니다  
[`BigInt64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)| 64비트 부호 있는 정수의 타입 배열을 나타냅니다  
[`BigUint64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array)| 64비트 부호 없는 정수의 타입 배열을 나타냅니다  
[`Boolean`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)| 논리 값을 나타내며 `true` 또는 `false` 값을 가질 수 있습니다  
[`clearInterval`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearInterval)| `setInterval()`로 설정된 반복 동작을 취소합니다  
[`clearTimeout`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearTimeout)| `setTimeout()`으로 설정된 반복 동작을 취소합니다  
[`console`](https://developer.mozilla.org/docs/Web/API/Console)| 브라우저 디버깅 콘솔에 접근합니다  
[`DataView`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/DataView)| `ArrayBuffer`의 일반적인 뷰를 나타냅니다  
[`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date)| 플랫폼에 독립적인 형식의 특정 시점을 나타냅니다  
[`decodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)| `encodeURI` 또는 유사한 루틴으로 생성된 URI를 디코딩합니다  
[`decodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)| `encodeURIComponent` 또는 유사한 루틴으로 생성된 URI 구성 요소를 디코딩합니다  
[`DOMException`](https://developer.mozilla.org/docs/Web/API/DOMException)| DOM에서 발생하는 오류를 나타냅니다  
[`encodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)| 특정 문자를 UTF-8 이스케이프 시퀀스로 치환하여 URI를 인코딩합니다  
[`encodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)| 특정 문자를 UTF-8 이스케이프 시퀀스로 치환하여 URI 구성 요소를 인코딩합니다  
[`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error)| 구문 실행이나 속성 접근 중 발생하는 오류를 나타냅니다  
[`EvalError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/EvalError)| 전역 함수 `eval()`과 관련된 오류를 나타냅니다  
[`Float32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float32Array)| 32비트 부동소수점 수의 타입 배열을 나타냅니다  
[`Float64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float64Array)| 64비트 부동소수점 수의 타입 배열을 나타냅니다  
[`Function`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function)| 함수를 나타냅니다  
[`Infinity`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Infinity)| 수학적 무한대를 나타냅니다  
[`Int8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int8Array)| 8비트 부호 있는 정수의 타입 배열을 나타냅니다  
[`Int16Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int16Array)| 16비트 부호 있는 정수의 타입 배열을 나타냅니다  
[`Int32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int32Array)| 32비트 부호 있는 정수의 타입 배열을 나타냅니다  
[`Intl`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl)| 국제화 및 현지화 기능에 접근합니다  
[`isFinite`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isFinite)| 값이 유한한 숫자인지 판별합니다  
[`isNaN`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isNaN)| 값이 `NaN`인지 여부를 판별합니다  
[`JSON`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON)| JavaScript 값을 JSON 형식으로 변환하거나 그 반대로 변환하는 기능을 제공합니다  
[`Map`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map)| 각 값이 한 번만 나타나는 값의 컬렉션을 나타냅니다  
[`Math`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Math)| 수학 함수와 상수에 접근합니다  
[`Number`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)| 숫자 값을 나타냅니다  
[`Object`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)| 모든 JavaScript 객체의 기반이 되는 객체를 나타냅니다  
[`parseFloat`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)| 문자열 인수를 파싱하여 부동소수점 숫자를 반환합니다  
[`parseInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseInt)| 문자열 인수를 파싱하여 지정된 기수의 정수를 반환합니다  
[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)| 비동기 작업의 최종 완료(또는 실패)와 그 결과 값을 나타냅니다  
[`Proxy`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Proxy)| 속성 조회, 할당, 열거, 함수 호출 등 기본 연산의 동작을 사용자 정의하는 객체를 나타냅니다  
[`queueMicrotask`](https://developer.mozilla.org/docs/Web/API/queueMicrotask)| 실행할 마이크로태스크를 큐에 추가합니다  
[`RangeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RangeError)| 값이 허용된 집합 또는 범위를 벗어났을 때의 오류를 나타냅니다  
[`ReferenceError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)| 존재하지 않는 변수를 참조했을 때의 오류를 나타냅니다  
[`Reflect`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Reflect)| 가로챌 수 있는 JavaScript 연산을 위한 메서드를 제공합니다

[`RegExp`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RegExp)| 정규 표현식을 나타내며 문자 조합을 일치시킬 수 있습니다.  
[`Set`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Set)| 각 값이 한 번만 등장할 수 있는 값 컬렉션을 나타냅니다.  
[`setInterval`](https://developer.mozilla.org/docs/Web/API/setInterval)| 각 호출 사이에 고정된 시간 지연을 두고 함수를 반복 호출합니다.  
[`setTimeout`](https://developer.mozilla.org/docs/Web/API/setTimeout)| 지정한 밀리초 이후에 함수를 호출하거나 표현식을 평가합니다.  
[`SharedArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)| 일반적이며 고정 길이의 원시 이진 데이터 버퍼를 나타냅니다.  
[`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)| 문자 시퀀스를 나타냅니다.  
[`structuredClone`](https://developer.mozilla.org/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)| 값을 깊은 복사합니다.  
[`Symbol`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Symbol)| 객체 속성의 키로 사용되는 고유하고 불변의 데이터 타입을 나타냅니다.  
[`SyntaxError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)| 구문적으로 잘못된 코드를 해석하려 할 때 발생하는 오류를 나타냅니다.  
[`TypeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/TypeError)| 값이 예상한 타입이 아닐 때 발생하는 오류를 나타냅니다.  
[`Uint8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)| 8비트 부호 없는 정수로 구성된 타입 배열을 나타냅니다.  
[`Uint8ClampedArray`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)| 0-255 범위로 클램핑된 8비트 부호 없는 정수 타입 배열을 나타냅니다.  
[`Uint32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array)| 32비트 부호 없는 정수 타입 배열을 나타냅니다.  
[`URIError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/URIError)| 전역 URI 처리 함수가 잘못 사용되었을 때 발생하는 오류를 나타냅니다.  
[`URL`](https://developer.mozilla.org/docs/Web/API/URL)| 객체 URL을 생성하는 데 사용되는 정적 메서드를 제공하는 객체를 나타냅니다.  
[`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern)| URL 패턴을 나타냅니다.  
[`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams)| 키/값 쌍 컬렉션을 나타냅니다.  
[`WeakMap`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)| 키가 약하게 참조되는 키/값 쌍 컬렉션을 나타냅니다.  
[`WeakSet`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)| 각 객체가 한 번만 등장할 수 있는 객체 컬렉션을 나타냅니다.  
[`WebAssembly`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly)| WebAssembly에 접근할 수 있도록 제공합니다.  
  
### Next.js 전용 폴리필[](https://nextjs.org/docs/pages/api-reference/edge#nextjs-specific-polyfills)

  * [`AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage)



### 환경 변수[](https://nextjs.org/docs/pages/api-reference/edge#environment-variables)

`next dev`와 `next build` 모두에서 [Environment Variables](https://nextjs.org/docs/app/guides/environment-variables)에 접근하려면 `process.env`를 사용할 수 있습니다.

### 지원되지 않는 API[](https://nextjs.org/docs/pages/api-reference/edge#unsupported-apis)

Edge Runtime에는 다음과 같은 제한이 있습니다.

  * 네이티브 Node.js API는 **지원되지 않습니다**. 예를 들어 파일 시스템을 읽거나 쓸 수 없습니다.
  * `node_modules` _는_ ES Modules를 구현하고 네이티브 Node.js API를 사용하지 않는 한 사용할 _수 있습니다_.
  * `require`를 직접 호출하는 것은 **허용되지 않습니다**. 대신 ES Modules를 사용하세요.



다음 JavaScript 언어 기능은 비활성화되어 있으며, **작동하지 않습니다.**

API| 설명  
---|---  
[`eval`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/eval)| 문자열로 표현된 JavaScript 코드를 평가합니다.  
[`new Function(evalString)`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function)| 인자로 제공한 코드로 새 함수를 생성합니다.  
[`WebAssembly.compile`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/compile)| 버퍼 소스에서 WebAssembly 모듈을 컴파일합니다.  
[`WebAssembly.instantiate`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate)| 버퍼 소스에서 WebAssembly 모듈을 컴파일하고 인스턴스화합니다.  
  
드물게 코드가 (또는 import된 코드가) 런타임에 도달할 수 없고 treeshaking으로 제거할 수 없는 동적 코드 평가 구문을 포함할 수 있습니다. Proxy 구성을 사용해 특정 파일을 허용하도록 검사를 완화할 수 있습니다.

proxy.ts
[code]
    export const config = {
      unstable_allowDynamic: [
        // allows a single file
        '/lib/utilities.js',
        // use a glob to allow anything in the function-bind 3rd party module
        '**/node_modules/function-bind/**',
      ],
    }
[/code]

`unstable_allowDynamic`은 특정 파일에 대해 동적 코드 평가를 무시하는 [glob](https://github.com/micromatch/micromatch#matching-features)이거나 glob 배열입니다. glob은 애플리케이션 루트 폴더를 기준으로 합니다.

이 구문이 Edge에서 실행되면 _예외가 발생하여 런타임 오류를 일으킨다는_ 점에 유의하세요.

도움이 되었나요?

지원됨.

전송
