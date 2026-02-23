---
title: '[Useful codecs](https://zod.dev/codecs?id=useful-codecs)'
description: 'API는 문자열 값(예: , , ,  등)을 으로 변환합니다. 기본적으로  시 는 로, 는 로 변환됩니다.'
---

- 모든 Zod 스키마는 “Forward”와 “Backward” 방향 모두에서 입력을 처리 가능하며, 기본적으로 타입이 같아 구분이 없지만 `z.codec()`처럼 입력과 출력이 달라지는 경우가 있음.
- Codec은 두 스키마 사이의 양방향 변환을 정의하는 특별한 스키마이며, `decode`는 입력을 파싱된 값으로, `encode`는 값을 직렬화로 변환함.
- 클라이언트와 서버가 동일한 Zod 스키마를 공유해 JSON 같은 네트워크 친화적 포맷과 풍부한 JS 표현 사이를 오가는 데 유용함; `z.encode()`/`z.decode()`는 모든 스키마에 사용할 수 있음.
- 일반 `parse()`와 달리 `z.decode()`/`z.encode()`는 입력에 강한 타입 검사를 하므로 앱 코드에서 오류를 컴파일 타임에 잡을 수 있음.
- Codec은 객체, 배열, 파이프 등 어디에도 중첩할 수 있고, async/ safe 변형도 지원됨 (`decodeAsync`, `safeDecode` 등).
- 인코딩 작동 방식: 코드 내부적으로 pipe 클래스의 하위 타입이며, 각 방향에서 스트림을 다른 스키마에 통과시킴; `.refine()` 등 검증도 양방향에서 실행되며, `z.encode()`는 타입 적합성과 refinement를 두 번 확인함.
- 기본값/사전 설정은 Forward 방향에서만 적용되고, `.catch()`도 Forward에서만 동작함; 따라서 `encode`에는 `undefined` 등의 기본값이 적용되지 않음.

**문서 번역**

**Note** — [Stringbool](https://zod.dev/api#stringbool)는 Zod에 codec이 도입되기 이전에 만들어졌으며, 이후 내부적으로 codec으로 재구현되었습니다.

`z.stringbool()` API는 문자열 값(예: `"true"`, `"false"`, `"yes"`, `"no"` 등)을 `boolean`으로 변환합니다. 기본적으로 `z.encode()` 시 `true`는 `"true"`로, `false`는 `"false"`로 변환됩니다.
```
    const stringbool = z.stringbool();

    stringbool.decode("true");  // => true
    stringbool.decode("false"); // => false

    stringbool.encode(true);    // => "true"
    stringbool.encode(false);   // => "false"
```

사용자 지정 `truthy`/`falsy` 값을 설정하면 _배열의 첫 번째 요소_가 대신 사용됩니다.
```
    const stringbool = z.stringbool({ truthy: ["yes", "y"], falsy: ["no", "n"] });

    stringbool.encode(true);    // => "yes"
    stringbool.encode(false);   // => "no"
```

- [Transforms](https://zod.dev/codecs?id=transforms)

⚠️ — `.transform()` API는 _단방향_ 변환을 수행합니다. 스키마 어딘가에 `.transform()`이 있다면, `z.encode()`를 호출할 경우 _런타임 오류_(`ZodError` 아님)가 발생합니다.
```
    const schema = z.string().transform(val => val.length);

    schema.encode(1234);
    // ❌ Error: Encountered unidirectional transform during encode: ZodTransform
```

## [Useful codecs](https://zod.dev/codecs?id=useful-codecs)

아래는 자주 필요한 codec들의 구현 예시입니다. 커스터마이징을 위해, 이들은 Zod의 공식 API로 포함되지 않으므로 프로젝트에 복사해서 필요에 따라 수정해서 사용해야 합니다.

**Note** — 아래 codec 구현은 모두 정확성 검증이 되어 있습니다.

- [`stringToNumber`](https://zod.dev/codecs?id=stringtonumber)

문자열로 표현된 숫자를 `parseFloat()`를 통해 JavaScript `number` 타입으로 변환합니다.
```
    const stringToNumber = z.codec(z.string().regex(z.regexes.number), z.number(), {
      decode: (str) => Number.parseFloat(str),
      encode: (num) => num.toString(),
    });

    stringToNumber.decode("42.5");  // => 42.5
    stringToNumber.encode(42.5);    // => "42.5"
```

- [`stringToInt`](https://zod.dev/codecs?id=stringtoint)

정수 형태 문자열을 `parseInt()`로 JavaScript `number` 타입으로 변환합니다.
```
    const stringToInt = z.codec(z.string().regex(z.regexes.integer), z.int(), {
      decode: (str) => Number.parseInt(str, 10),
      encode: (num) => num.toString(),
    });

    stringToInt.decode("42");  // => 42
    stringToInt.encode(42);    // => "42"
```

- [`stringToBigInt`](https://zod.dev/codecs?id=stringtobigint)

문자열 표현을 JavaScript `bigint` 타입으로 변환합니다.
```
    const stringToBigInt = z.codec(z.string(), z.bigint(), {
      decode: (str) => BigInt(str),
      encode: (bigint) => bigint.toString(),
    });

    stringToBigInt.decode("12345");  // => 12345n
    stringToBigInt.encode(12345n);   // => "12345"
```

- [`numberToBigInt`](https://zod.dev/codecs?id=numbertobigint)

JavaScript `number`를 `bigint` 타입으로 변환합니다.
```
    const numberToBigInt = z.codec(z.int(), z.bigint(), {
      decode: (num) => BigInt(num),
      encode: (bigint) => Number(bigint),
    });

    numberToBigInt.decode(42);   // => 42n
    numberToBigInt.encode(42n);  // => 42
```

- [`isoDatetimeToDate`](https://zod.dev/codecs?id=isodatetimetodate)

ISO 날짜/시간 문자열을 JavaScript `Date` 객체로 변환합니다.
```
    const isoDatetimeToDate = z.codec(z.iso.datetime(), z.date(), {
      decode: (isoString) => new Date(isoString),
      encode: (date) => date.toISOString(),
    });

    isoDatetimeToDate.decode("2024-01-15T10:30:00.000Z");  // => Date object
    isoDatetimeToDate.encode(new Date("2024-01-15"));       // => "2024-01-15T00:00:00.000Z"
```

- [`epochSecondsToDate`](https://zod.dev/codecs?id=epochsecondstodate)

에포크 기준 초 단위 Unix 타임스탬프를 JavaScript `Date` 객체로 변환합니다.
```
    const epochSecondsToDate = z.codec(z.int().min(0), z.date(), {
      decode: (seconds) => new Date(seconds * 1000),
      encode: (date) => Math.floor(date.getTime() / 1000),
    });

    epochSecondsToDate.decode(1705314600);  // => Date object
    epochSecondsToDate.encode(new Date());  // => Unix timestamp in seconds
```

- [`epochMillisToDate`](https://zod.dev/codecs?id=epochmillistodate)

에포크 기준 밀리초 단위 Unix 타임스탬프를 JavaScript `Date` 객체로 변환합니다.
```
    const epochMillisToDate = z.codec(z.int().min(0), z.date(), {
      decode: (millis) => new Date(millis),
      encode: (date) => date.getTime(),
    });

    epochMillisToDate.decode(1705314600000);  // => Date object
    epochMillisToDate.encode(new Date());     // => Unix timestamp in milliseconds
```

- [`json(schema)`](https://zod.dev/codecs?id=jsonschema)

JSON 문자열을 구조화된 데이터로 파싱하고 다시 JSON으로 직렬화합니다. 이 제네릭 함수는 파싱한 JSON 데이터를 검증할 출력 스키마를 인자로 받습니다.
```
    const jsonCodec = <T extends z.core.$ZodType>(schema: T) =>
      z.codec(z.string(), schema, {
        decode: (jsonString, ctx) => {
          try {
            return JSON.parse(jsonString);
          } catch (err: any) {
            ctx.issues.push({
              code: "invalid_format",
              format: "json",
              input: jsonString,
              message: err.message,
            });
            return z.NEVER;
          }
        },
        encode: (value) => JSON.stringify(value),
      });
```

특정 스키마 사용 예:
```
    const jsonToObject = jsonCodec(z.object({ name: z.string(), age: z.number() }));

    jsonToObject.decode('{"name":"Alice","age":30}');
    // => { name: "Alice", age: 30 }

    jsonToObject.encode({ name: "Bob", age: 25 });
    // => '{"name":"Bob","age":25}'

    jsonToObject.decode('~~invalid~~');
    // ZodError: [
    //   {
    //     "code": "invalid_format",
    //     "format": "json",
    //     "path": [],
    //     "message": "Unexpected token '~', \"~~invalid~~\" is not valid JSON"
    //   }
    // ]
```

- [`utf8ToBytes`](https://zod.dev/codecs?id=utf8tobytes)

UTF-8 문자열을 `Uint8Array` 바이트 배열로 변환합니다.
```
    const utf8ToBytes = z.codec(z.string(), z.instanceof(Uint8Array), {
      decode: (str) => new TextEncoder().encode(str),
      encode: (bytes) => new TextDecoder().decode(bytes),
    });

    utf8ToBytes.decode("Hello, 世界!");  // => Uint8Array
    utf8ToBytes.encode(bytes);          // => "Hello, 世界!"
```

- [`bytesToUtf8`](https://zod.dev/codecs?id=bytestoutf8)

`Uint8Array` 바이트 배열을 UTF-8 문자열로 변환합니다.
```
    const bytesToUtf8 = z.codec(z.instanceof(Uint8Array), z.string(), {
      decode: (bytes) => new TextDecoder().decode(bytes),
      encode: (str) => new TextEncoder().encode(str),
    });

    bytesToUtf8.decode(bytes);          // => "Hello, 世界!"
    bytesToUtf8.encode("Hello, 世界!");  // => Uint8Array
```

- [`base64ToBytes`](https://zod.dev/codecs?id=base64tobytes)

base64 문자열과 `Uint8Array` 바이트 배열을 상호 변환합니다.
```
    const base64ToBytes = z.codec(z.base64(), z.instanceof(Uint8Array), {
      decode: (base64String) => z.util.base64ToUint8Array(base64String),
      encode: (bytes) => z.util.uint8ArrayToBase64(bytes),
    });

    base64ToBytes.decode("SGVsbG8=");  // => Uint8Array([72, 101, 108, 108, 111])
    base64ToBytes.encode(bytes);       // => "SGVsbG8="
```

- [`base64urlToBytes`](https://zod.dev/codecs?id=base64urltobytes)

URL 안전(base64url) 문자열과 `Uint8Array` 바이트 배열을 변환합니다.
```
    const base64urlToBytes = z.codec(z.base64url(), z.instanceof(Uint8Array), {
      decode: (base64urlString) => z.util.base64urlToUint8Array(base64urlString),
      encode: (bytes) => z.util.uint8ArrayToBase64url(bytes),
    });

    base64urlToBytes.decode("SGVsbG8");  // => Uint8Array([72, 101, 108, 108, 111])
    base64urlToBytes.encode(bytes);      // => "SGVsbG8"
```

- [`hexToBytes`](https://zod.dev/codecs?id=hextobytes)

**번역**
- 16진수 문자열을 `Uint8Array` 바이트 배열로, 또는 반대로 변환합니다.
```
    const hexToBytes = z.codec(z.hex(), z.instanceof(Uint8Array), {
      decode: (hexString) => z.util.hexToUint8Array(hexString),
      encode: (bytes) => z.util.uint8ArrayToHex(bytes),
    });

    hexToBytes.decode("48656c6c6f");     // => Uint8Array([72, 101, 108, 108, 111])
    hexToBytes.encode(bytes);            // => "48656c6c6f"
```

- [`stringToURL`](https://zod.dev/codecs?id=stringtourl)

URL 문자열을 JavaScript `URL` 객체로 변환합니다.
```
    const stringToURL = z.codec(z.url(), z.instanceof(URL), {
      decode: (urlString) => new URL(urlString),
      encode: (url) => url.href,
    });

    stringToURL.decode("https://example.com/path");  // => URL object
    stringToURL.encode(new URL("https://example.com"));  // => "https://example.com/"
```

- [`stringToHttpURL`](https://zod.dev/codecs?id=stringtohttpurl)

HTTP/HTTPS URL 문자열을 JavaScript `URL` 객체로 변환합니다.
```
    const stringToHttpURL = z.codec(z.httpUrl(), z.instanceof(URL), {
      decode: (urlString) => new URL(urlString),
      encode: (url) => url.href,
    });

    stringToHttpURL.decode("https://api.example.com/v1");  // => URL object
    stringToHttpURL.encode(url);                           // => "https://api.example.com/v1"
```

- [`uriComponent`](https://zod.dev/codecs?id=uricomponent)

`encodeURIComponent()`와 `decodeURIComponent()`를 사용해 URI 구성 요소를 인코딩 및 디코딩합니다.
```
    const uriComponent = z.codec(z.string(), z.string(), {
      decode: (encodedString) => decodeURIComponent(encodedString),
      encode: (decodedString) => encodeURIComponent(decodedString),
    });

    uriComponent.decode("Hello%20World%21");  // => "Hello World!"
    uriComponent.encode("Hello World!");      // => "Hello%20World!"
```

