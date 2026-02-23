---
title: '스키마 정의하기'
description: '데이터를 검증하려면 먼저 _스키마_ 를 정의해야 합니다. 스키마는 간단한 원시 값부터 복잡한 중첩 객체와 배열까지를 나타내는 _타입_ 을 나타냅니다.'
---

# 스키마 정의하기

Copy markdown

[이 페이지 편집하기](https://github.com/colinhacks/zod/edit/main/packages/docs/content/api.mdx)

데이터를 검증하려면 먼저 _스키마_ 를 정의해야 합니다. 스키마는 간단한 원시 값부터 복잡한 중첩 객체와 배열까지를 나타내는 _타입_ 을 나타냅니다.

## [원시값](https://zod.dev/api?id=primitives)
```
    import * as z from "zod";

    // primitive types
    z.string();
    z.number();
    z.bigint();
    z.boolean();
    z.symbol();
    z.undefined();
    z.null();
```

- [강제 변환](https://zod.dev/api?id=coercion)

입력 데이터를 적절한 타입으로 강제 변환하려면 대신 `z.coerce` 를 사용하세요:
```
    z.coerce.string();    // String(input)
    z.coerce.number();    // Number(input)
    z.coerce.boolean();   // Boolean(input)
    z.coerce.bigint();    // BigInt(input)
```

이 스키마들의 강제 변환 버전은 입력 값을 적절한 타입으로 변환하려고 시도합니다.
```
    const schema = z.coerce.string();

    schema.parse("tuna");    // => "tuna"
    schema.parse(42);        // => "42"
    schema.parse(true);      // => "true"
    schema.parse(null);      // => "null"
```

이러한 강제 변환 스키마의 입력 타입은 기본적으로 `unknown` 입니다. 보다 구체적인 입력 타입을 지정하려면 제네릭 매개변수를 전달하세요:
```
    const A = z.coerce.number();
    type AInput = z.input<typeof A>; // => unknown

    const B = z.coerce.number<number>();
    type BInput = z.input<typeof B>; // => number
```

### Zod에서 강제 변환이 작동하는 방식

### 입력 타입 사용자 지정

## [리터럴](https://zod.dev/api?id=literals)

리터럴 스키마는 `"hello world"` 나 `5` 같은 [리터럴 타입](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types)을 나타냅니다.
```
    const tuna = z.literal("tuna");
    const twelve = z.literal(12);
    const twobig = z.literal(2n);
    const tru = z.literal(true);
```

JavaScript의 `null` 과 `undefined` 리터럴을 나타내려면:
```
    z.null();
    z.undefined();
    z.void(); // equivalent to z.undefined()
```

여러 리터럴 값을 허용하려면:
```
    const colors = z.literal(["red", "green", "blue"]);

    colors.parse("green"); // ✅
    colors.parse("yellow"); // ❌
```

리터럴 스키마에서 허용된 값의 집합을 추출하려면:

ZodZod Mini
```
    colors.values; // => Set<"red" | "green" | "blue">
```

## [문자열](https://zod.dev/api?id=strings)

Zod는 여러 기본 문자열 검증 및 변환 API를 제공합니다. 일반적인 문자열 검증을 수행하려면:

ZodZod Mini
```
    z.string().max(5);
    z.string().min(5);
    z.string().length(5);
    z.string().regex(/^[a-z]+$/);
    z.string().startsWith("aaa");
    z.string().endsWith("zzz");
    z.string().includes("---");
    z.string().uppercase();
    z.string().lowercase();
```

간단한 문자열 변환을 수행하려면:

ZodZod Mini
```
    z.string().trim(); // trim whitespace
    z.string().toLowerCase(); // toLowerCase
    z.string().toUpperCase(); // toUpperCase
    z.string().normalize(); // normalize unicode characters
```

## [문자열 형식](https://zod.dev/api?id=string-formats)

일반적인 문자열 형식에 대해 검증하려면:
```
    z.email();
    z.uuid();
    z.url();
    z.httpUrl();       // http or https URLs only
    z.hostname();
    z.emoji();         // validates a single emoji character
    z.base64();
    z.base64url();
    z.hex();
    z.jwt();
    z.nanoid();
    z.cuid();
    z.cuid2();
    z.ulid();
    z.ipv4();
    z.ipv6();
    z.mac();
    z.cidrv4();        // ipv4 CIDR block
    z.cidrv6();        // ipv6 CIDR block
    z.hash("sha256");  // or "sha1", "sha384", "sha512", "md5"
    z.iso.date();
    z.iso.time();
    z.iso.datetime();
    z.iso.duration();
```

- [이메일](https://zod.dev/api?id=emails)

이메일 주소를 검증하려면:
```
    z.email();
```

기본적으로 Zod는 일반적인 문자를 포함하는 일반적인 이메일 주소를 검증하도록 설계된 비교적 엄격한 이메일 정규식(regex)을 사용합니다. 이는 Gmail에서 사용하는 규칙과 대체로 동등합니다. 이 정규식에 대해 자세히 알아보려면 [이 글](https://colinhacks.com/essays/reasonable-email-regex)을 참조하세요.
```
    /^(?!\.)(?!.*\.\.)([a-z0-9_'+\-\.]*)[a-z0-9_+-]@([a-z0-9][a-z0-9\-]*\.)+[a-z]{2,}$/i
```

이메일 검증 동작을 사용자 지정하려면 `pattern` 매개변수에 사용자 정의 정규식을 전달할 수 있습니다.
```
    z.email({ pattern: /your regex here/ });
```

Zod는 사용할 수 있는 몇 가지 유용한 정규식을 내보냅니다.
```
    // Zod's default email regex
    z.email();
    z.email({ pattern: z.regexes.email }); // equivalent

    // the regex used by browsers to validate input[type=email] fields
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email
    z.email({ pattern: z.regexes.html5Email });

    // the classic emailregex.com regex (RFC 5322)
    z.email({ pattern: z.regexes.rfc5322Email });

    // a loose regex that allows Unicode (good for intl emails)
    z.email({ pattern: z.regexes.unicodeEmail });
```

- [UUID](https://zod.dev/api?id=uuids)

UUID를 검증하려면:
```
    z.uuid();
```

특정 UUID 버전을 지정하려면:
```
    // supports "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8"
    z.uuid({ version: "v4" });

    // for convenience
    z.uuidv4();
    z.uuidv6();
    z.uuidv7();
```

RFC 9562/4122 UUID 규격은 8바이트의 처음 두 비트가 `10`이어야 합니다. 다른 UUID 유사 식별자는 이 제약을 적용하지 않습니다. UUID 유사 식별자 전반을 검증하려면:
```
    z.guid();
```

- [URL](https://zod.dev/api?id=urls)

WHATWG 호환 URL을 검증하려면:
```
    const schema = z.url();

    schema.parse("https://example.com"); // ✅
    schema.parse("http://localhost"); // ✅
    schema.parse("mailto:[[email protected]](https://zod.dev/cdn-cgi/l/email-protection)"); // ✅
```

보시다시피 꽤 관대합니다. 내부적으로 입력을 검증하기 위해 `new URL()` 생성자를 사용하며, 이 동작은 플랫폼과 런타임에 따라 다를 수 있지만 모든 JS 런타임/엔진에서 URI/URL을 검증하는 데 있어 가장 엄격한 방법입니다.

호스트명을 특정 정규식으로 검증하려면:
```
    const schema = z.url({ hostname: /^example\.com$/ });

    schema.parse("https://example.com"); // ✅
    schema.parse("https://zombo.com"); // ❌
```

프로토콜을 특정 정규식으로 검증하려면 `protocol` 매개변수를 사용하세요.
```
    const schema = z.url({ protocol: /^https$/ });

    schema.parse("https://example.com"); // ✅
    schema.parse("http://example.com"); // ❌
```

**웹 URL** — 대부분의 경우 웹 URL을 구체적으로 검증하고 싶을 것입니다. 이를 위한 권장 스키마는 다음과 같습니다:
```
    const httpUrl = z.url({
      protocol: /^https?$/,
      hostname: z.regexes.domain
    });
```

이 스키마는 프로토콜을 `http`/`https`로 제한하고 hostname이 `z.regexes.domain` 정규식을 통해 유효한 도메인 이름인지 보장합니다:
```
    /^([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$/
```

URL을 정규화하려면 `normalize` 플래그를 사용하세요. 이것은 `new URL()` 에서 반환되는 [정규화된 URL](https://chatgpt.com/share/6881547f-bebc-800f-9093-f5981e277c2c)로 입력 값을 덮어씁니다.
```
    new URL("HTTP://ExAmPle.com:80/./a/../b?X=1#f oo").href
    // => "http://example.com/b?X=1#f%20oo"
```

- [ISO 날짜시간](https://zod.dev/api?id=iso-datetimes)

이미 눈치채셨겠지만, Zod 문자열에는 몇 가지 날짜/시간 관련 검증이 포함되어 있습니다. 이 검증들은 정규식 기반이므로 전체 날짜/시간 라이브러리만큼 엄격하지는 않습니다. 하지만 사용자 입력을 검증할 때 매우 편리합니다.

`z.iso.datetime()` 메서드는 ISO 8601을 강제하며 기본적으로 타임존 오프셋을 허용하지 않습니다:
```
    const datetime = z.iso.datetime();

    datetime.parse("2020-01-01T06:15:00Z"); // ✅
    datetime.parse("2020-01-01T06:15:00.123Z"); // ✅
    datetime.parse("2020-01-01T06:15:00.123456Z"); // ✅ (arbitrary precision)
    datetime.parse("2020-01-01T06:15:00+02:00"); // ❌ (offsets not allowed)
    datetime.parse("2020-01-01T06:15:00"); // ❌ (local not allowed)
```

타임존 오프셋을 허용하려면:
```
    const datetime = z.iso.datetime({ offset: true });

    // allows timezone offsets
    datetime.parse("2020-01-01T06:15:00+02:00"); // ✅

    // basic offsets not allowed
    datetime.parse("2020-01-01T06:15:00+02");    // ❌
    datetime.parse("2020-01-01T06:15:00+0200");  // ❌

    // Z is still supported
    datetime.parse("2020-01-01T06:15:00Z"); // ✅
```

다음과 같은 방식으로 지역(timezone 없는) 날짜-시간을 허용하려면:
```
    const schema = z.iso.datetime({ local: true });
    schema.parse("2020-01-01T06:15:01"); // ✅
    schema.parse("2020-01-01T06:15"); // ✅ 초 선택 가능
```

허용 가능한 시간 `precision`을 제한하려면. 기본적으로 초는 선택 사항이며 임의의 소수 초 정밀도를 허용합니다.
```
    const a = z.iso.datetime();
    a.parse("2020-01-01T06:15Z"); // ✅
    a.parse("2020-01-01T06:15:00Z"); // ✅
    a.parse("2020-01-01T06:15:00.123Z"); // ✅

    const b = z.iso.datetime({ precision: -1 }); // 분 정밀도(초 없음)
    b.parse("2020-01-01T06:15Z"); // ✅
    b.parse("2020-01-01T06:15:00Z"); // ❌
    b.parse("2020-01-01T06:15:00.123Z"); // ❌

    const c = z.iso.datetime({ precision: 0 }); // 초 정밀도만 허용
    c.parse("2020-01-01T06:15Z"); // ❌
    c.parse("2020-01-01T06:15:00Z"); // ✅
    c.parse("2020-01-01T06:15:00.123Z"); // ❌

    const d = z.iso.datetime({ precision: 3 }); // 밀리초 정밀도만 허용
    d.parse("2020-01-01T06:15Z"); // ❌
    d.parse("2020-01-01T06:15:00Z"); // ❌
    d.parse("2020-01-01T06:15:00.123Z"); // ✅
```

- [ISO 날짜](https://zod.dev/api?id=iso-dates)

`z.iso.date()` 메서드는 `YYYY-MM-DD` 형식의 문자열을 검증합니다.
```
    const date = z.iso.date();

    date.parse("2020-01-01"); // ✅
    date.parse("2020-1-1"); // ❌
    date.parse("2020-01-32"); // ❌
```

- [ISO 시간](https://zod.dev/api?id=iso-times)

`z.iso.time()` 메서드는 `HH:MM[:SS[.s+]]` 형식의 문자열을 검증합니다. 기본적으로 초와 소수 초는 선택 사항입니다.
```
    const time = z.iso.time();

    time.parse("03:15"); // ✅
    time.parse("03:15:00"); // ✅
    time.parse("03:15:00.9999999"); // ✅ (임의 정밀도)
```

어떠한 오프셋도 허용되지 않습니다.
```
    time.parse("03:15:00Z"); // ❌ (`Z` 불가)
    time.parse("03:15:00+02:00"); // ❌ (오프셋 불가)
```

`precision` 매개변수로 허용할 소수점 정밀도를 제한하세요.
```
    z.iso.time({ precision: -1 }); // HH:MM (분 정밀도)
    z.iso.time({ precision: 0 });  // HH:MM:SS (초 정밀도)
    z.iso.time({ precision: 1 });  // HH:MM:SS.s (데시초 정밀도)
    z.iso.time({ precision: 2 });  // HH:MM:SS.ss (센티초 정밀도)
    z.iso.time({ precision: 3 });  // HH:MM:SS.sss (밀리초 정밀도)
```

- [IP 주소](https://zod.dev/api?id=ip-addresses)
```
    const ipv4 = z.ipv4();
    ipv4.parse("192.168.0.0"); // ✅

    const ipv6 = z.ipv6();
    ipv6.parse("2001:db8:85a3::8a2e:370:7334"); // ✅
```

- [IP 블록(CIDR)](https://zod.dev/api?id=ip-blocks-cidr)

[CIDR 표기법](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)으로 지정된 IP 주소 범위를 검증합니다.
```
    const cidrv4 = z.cidrv4();
    cidrv4.parse("192.168.0.0/24"); // ✅

    const cidrv6 = z.cidrv6();
    cidrv6.parse("2001:db8::/32"); // ✅
```

- [MAC 주소](https://zod.dev/api?id=mac-addresses)

표준 48비트 MAC 주소 [IEEE 802](https://en.wikipedia.org/wiki/MAC_address)를 검증합니다.
```
    const mac = z.mac();
    mac.parse("00:1A:2B:3C:4D:5E");  // ✅
    mac.parse("00-1a-2b-3c-4d-5e");  // ❌ 기본값은 콜론 구분
    mac.parse("001A:2B3C:4D5E");     // ❌ 표준 형식만
    mac.parse("00:1A:2b:3C:4d:5E");  // ❌ 대/소문자 혼용 불가

    // 사용자 정의 구분자
    const dashMac = z.mac({ delimiter: "-" });
    dashMac.parse("00-1A-2B-3C-4D-5E"); // ✅
```

- [JWT](https://zod.dev/api?id=jwts)

[JSON Web Token](https://jwt.io/)을 검증합니다.
```
    z.jwt();
    z.jwt({ alg: "HS256" });
```

- [해시](https://zod.dev/api?id=hashes)

암호학적 해시 값을 검증하려면:
```
    z.hash("md5");
    z.hash("sha1");
    z.hash("sha256");
    z.hash("sha384");
    z.hash("sha512");
```

기본적으로 `z.hash()`는 일반적인 관례대로 16진수 인코딩을 기대합니다. `enc` 매개변수로 다른 인코딩을 지정할 수 있습니다:
```
    z.hash("sha256", { enc: "hex" });       // 기본값
    z.hash("sha256", { enc: "base64" });    // base64 인코딩
    z.hash("sha256", { enc: "base64url" }); // base64url 인코딩 (패딩 없음)
```

### 예상 길이와 패딩

- [커스텀 형식](https://zod.dev/api?id=custom-formats)

직접 문자열 형식을 정의하려면:
```
    const coolId = z.stringFormat("cool-id", ()=>{
      // 임의 검증 로직
      return val.length === 100 && val.startsWith("cool-");
    });

    // 정규식도 허용
    z.stringFormat("cool-id", /^cool-[a-z0-9]{95}$/);
```

이 스키마는 `z.custom()`이나 refinement에서 나오는 `"custom"` 오류보다 더 설명적인 `"invalid_format"` 문제를 생성합니다.
```
    myFormat.parse("invalid input!");
    // ZodError: [
    //   {
    //     "code": "invalid_format",
    //     "format": "cool-id",
    //     "path": [],
    //     "message": "Invalid cool-id"
    //   }
    // ]
```

## [템플릿 리터럴](https://zod.dev/api?id=template-literals)

**신규** — `[[email protected]](https://zod.dev/cdn-cgi/l/email-protection)`에서 도입되었습니다.

템플릿 리터럴 스키마를 정의하려면:
```
    const schema = z.templateLiteral([ "hello, ", z.string(), "!" ]);
    // `hello, ${string}!`
```

`z.templateLiteral` API는 문자열 리터럴(예: `"hello"`)과 스키마를 원하는 만큼 처리할 수 있습니다. `string | number | bigint | boolean | null | undefined`에 할당 가능한 추론된 타입을 가진 모든 스키마를 전달할 수 있습니다.
```
    z.templateLiteral([ "hi there" ]);
    // `hi there`

    z.templateLiteral([ "email: ", z.string() ]);
    // `email: ${string}`

    z.templateLiteral([ "high", z.literal(5) ]);
    // `high5`

    z.templateLiteral([ z.nullable(z.literal("grassy")) ]);
    // `grassy` | `null`

    z.templateLiteral([ z.number(), z.enum(["px", "em", "rem"]) ]);
    // `${number}px` | `${number}em` | `${number}rem`
```

## [숫자](https://zod.dev/api?id=numbers)

숫자를 검증하려면 `z.number()`를 사용합니다. 유한한 모든 숫자를 허용합니다.
```
    const schema = z.number();

    schema.parse(3.14);      // ✅
    schema.parse(NaN);       // ❌
    schema.parse(Infinity);  // ❌
```

Zod는 숫자 전용 검증도 지원합니다:

ZodZod Mini
```
    z.number().gt(5);
    z.number().gte(5);                     // 별칭 .min(5)
    z.number().lt(5);
    z.number().lte(5);                     // 별칭 .max(5)
    z.number().positive();                 // 별칭 .gt(0)
    z.number().nonnegative();
    z.number().negative();
    z.number().nonpositive();
    z.number().multipleOf(5);              // 별칭 .step(5)
```

`NaN`을 검증해야 하는 경우 `z.nan()`을 사용하세요.
```
    z.nan().parse(NaN);              // ✅
    z.nan().parse("anything else");  // ❌
```

## [정수](https://zod.dev/api?id=integers)

정수를 검증하려면:
```
    z.int();     // 안전 정수 범위로 제한
    z.int32();   // int32 범위로 제한
```

## [BigInt](https://zod.dev/api?id=bigints)

BigInt를 검증하려면:
```
    z.bigint();
```

Zod는 BigInt 전용 검증도 제공합니다.

ZodZod Mini
```
    z.bigint().gt(5n);
    z.bigint().gte(5n);                    // 별칭 `.min(5n)`
    z.bigint().lt(5n);
    z.bigint().lte(5n);                    // 별칭 `.max(5n)`
    z.bigint().positive();                 // 별칭 `.gt(0n)`
    z.bigint().nonnegative();
    z.bigint().negative();
    z.bigint().nonpositive();
    z.bigint().multipleOf(5n);             // 별칭 `.step(5n)`
```

## [불린](https://zod.dev/api?id=booleans)

불린 값을 검증하려면:
```
    z.boolean().parse(true); // => true
    z.boolean().parse(false); // => false
```

## [날짜](https://zod.dev/api?id=dates)

`Date` 인스턴스를 검증하려면 `z.date()`를 사용하세요.
```
    z.date().safeParse(new Date()); // success: true
    z.date().safeParse("2022-01-12T06:15:00.000Z"); // success: false
```

오류 메시지를 커스텀하려면:
```
    z.date({
      error: issue => issue.input === undefined ? "Required" : "Invalid date"
    });
```

Zod는 날짜 전용 검증도 제공합니다.

ZodZod Mini
```
    z.date().min(new Date("1900-01-01"), { error: "Too old!" });
    z.date().max(new Date(), { error: "Too young!" });

## [Enums](https://zod.dev/api?id=enums)

고정된 허용 _문자열_ 값 집합에 대해 입력을 검증하려면 `z.enum`을 사용하세요.
```
    const FishEnum = z.enum(["Salmon", "Tuna", "Trout"]);

    FishEnum.parse("Salmon"); // => "Salmon"
    FishEnum.parse("Swordfish"); // => ❌
```

주의 — 문자열 배열을 변수로 선언하면 Zod가 각 요소의 정확한 값을 제대로 추론하지 못합니다.
```
    const fish = ["Salmon", "Tuna", "Trout"];

    const FishEnum = z.enum(fish);
    type FishEnum = z.infer<typeof FishEnum>; // string
```

이를 해결하려면 배열을 `z.enum()` 함수에 바로 전달하거나 [`as const`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions)를 사용하세요.
```
    const fish = ["Salmon", "Tuna", "Trout"] as const;

    const FishEnum = z.enum(fish);
    type FishEnum = z.infer<typeof FishEnum>; // "Salmon" | "Tuna" | "Trout"
```

Enum과 유사한 객체 리터럴(`{ [key: string]: string | number }`)도 지원합니다.
```
    const Fish = {
      Salmon: 0,
      Tuna: 1
    } as const

    const FishEnum = z.enum(Fish)
    FishEnum.parse(Fish.Salmon); // => ✅
    FishEnum.parse(0); // => ✅
    FishEnum.parse(2); // => ❌
```

외부에 선언된 TypeScript enum을 전달할 수도 있습니다.
```
    enum Fish {
      Salmon = 0,
      Tuna = 1
    }

    const FishEnum = z.enum(Fish);
    FishEnum.parse(Fish.Salmon); // => ✅
    FishEnum.parse(0); // => ✅
    FishEnum.parse(2); // => ❌
```

**Zod 4** — Zod 3의 `z.nativeEnum()` API를 대체합니다.

TypeScript의 `enum` 키워드 사용은 [권장되지 않습니다](https://www.totaltypescript.com/why-i-dont-like-typescript-enums).
```
    enum Fish {
      Salmon = "Salmon",
      Tuna = "Tuna",
      Trout = "Trout",
    }

    const FishEnum = z.enum(Fish);
```

- [`.enum`](https://zod.dev/api?id=enum)

스키마의 값을 enum과 유사한 객체로 추출하려면:

ZodZod Mini
```
    const FishEnum = z.enum(["Salmon", "Tuna", "Trout"]);

    FishEnum.enum;
    // => { Salmon: "Salmon", Tuna: "Tuna", Trout: "Trout" }
```

- [`.exclude()`](https://zod.dev/api?id=exclude)

일부 값을 제외한 새로운 enum 스키마를 만들려면:

ZodZod Mini
```
    const FishEnum = z.enum(["Salmon", "Tuna", "Trout"]);
    const TunaOnly = FishEnum.exclude(["Salmon", "Trout"]);
```

- [`.extract()`](https://zod.dev/api?id=extract)

일부 값만 추출한 새로운 enum 스키마를 만들려면:

ZodZod Mini
```
    const FishEnum = z.enum(["Salmon", "Tuna", "Trout"]);
    const SalmonAndTroutOnly = FishEnum.extract(["Salmon", "Trout"]);
```

## [Stringbools](https://zod.dev/api?id=stringbool)

**💎 Zod 4에서 도입**

환경 변수 파싱처럼 특정 문자열 “boolish” 값을 일반 `boolean` 값으로 해석하는 것이 유용한 경우가 있습니다. 이를 위해 Zod 4는 `z.stringbool()`을 도입합니다:
```
    const strbool = z.stringbool();

    strbool.parse("true")         // => true
    strbool.parse("1")            // => true
    strbool.parse("yes")          // => true
    strbool.parse("on")           // => true
    strbool.parse("y")            // => true
    strbool.parse("enabled")      // => true

    strbool.parse("false");       // => false
    strbool.parse("0");           // => false
    strbool.parse("no");          // => false
    strbool.parse("off");         // => false
    strbool.parse("n");           // => false
    strbool.parse("disabled");    // => false

    strbool.parse(/* anything else */); // ZodError<[{ code: "invalid_value" }]>
```

참/거짓 값을 커스터마이징하려면:
```
    // these are the defaults
    z.stringbool({
      truthy: ["true", "1", "yes", "on", "y", "enabled"],
      falsy: ["false", "0", "no", "off", "n", "disabled"],
    });
```

기본적으로 스키마는 _대소문자를 구분하지 않으며_; 모든 입력은 `truthy`/`falsy` 값과 비교하기 전에 소문자로 변환됩니다. 대소문자 구분을 원하면:
```
    z.stringbool({
      case: "sensitive"
    });
```

## [Optionals](https://zod.dev/api?id=optionals)

스키마를 _optional_하게 만들려면 (`undefined` 입력을 허용):

ZodZod Mini
```
    z.optional(z.literal("yoda")); // or z.literal("yoda").optional()
```

이렇게 하면 원래 스키마를 감싸는 `ZodOptional` 인스턴스를 반환합니다. 내부 스키마를 추출하려면:

ZodZod Mini
```
    optionalYoda.unwrap(); // ZodLiteral<"yoda">
```

## [Nullables](https://zod.dev/api?id=nullables)

스키마를 _nullable_하게 만들려면 (`null` 입력을 허용):

ZodZod Mini
```
    z.nullable(z.literal("yoda")); // or z.literal("yoda").nullable()
```

이렇게 하면 원래 스키마를 감싸는 `ZodNullable` 인스턴스를 반환합니다. 내부 스키마를 추출하려면:

ZodZod Mini
```
    nullableYoda.unwrap(); // ZodLiteral<"yoda">
```

## [Nullish](https://zod.dev/api?id=nullish)

스키마를 _nullish_하게 만들려면 (optional + nullable):

ZodZod Mini
```
    const nullishYoda = z.nullish(z.literal("yoda"));
```

[nullish](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#nullish-coalescing) 개념은 TypeScript 설명서를 참고하세요.

## [Unknown](https://zod.dev/api?id=unknown)

Zod는 TypeScript 타입 시스템을 1:1로 반영하는 것을 목표로 하므로, 다음 특수 타입을 표현하는 API를 제공합니다:
```
    // allows any values
    z.any(); // inferred type: `any`
    z.unknown(); // inferred type: `unknown`
```

## [Never](https://zod.dev/api?id=never)

어떤 값도 검증을 통과하지 못합니다.
```
    z.never(); // inferred type: `never`
```

## [Objects](https://zod.dev/api?id=objects)

객체 타입을 정의하려면:
```
      // all properties are required by default
      const Person = z.object({
        name: z.string(),
        age: z.number(),
      });

      type Person = z.infer<typeof Person>;
      // => { name: string; age: number; }
```

기본적으로 모든 속성은 필수입니다. 특정 속성을 optional하게 만들려면:

ZodZod Mini
```
    const Dog = z.object({
      name: z.string(),
      age: z.number().optional(),
    });

    Dog.parse({ name: "Yeller" }); // ✅
```

기본적으로 인식되지 않은 키는 파싱 결과에서 _제거_됩니다:
```
    Dog.parse({ name: "Yeller", extraKey: true });
    // => { name: "Yeller" }
```

- [`z.strictObject`](https://zod.dev/api?id=zstrictobject)

알 수 없는 키가 들어오면 오류를 던지는 _strict_ 스키마를 정의하려면:
```
    const StrictDog = z.strictObject({
      name: z.string(),
    });

    StrictDog.parse({ name: "Yeller", extraKey: true });
    // ❌ throws
```

- [`z.looseObject`](https://zod.dev/api?id=zlooseobject)

알 수 없는 키를 그대로 통과시키는 _loose_ 스키마를 정의하려면:
```
    const LooseDog = z.looseObject({
      name: z.string(),
    });

    LooseDog.parse({ name: "Yeller", extraKey: true });
    // => { name: "Yeller", extraKey: true }
```

- [`.catchall()`](https://zod.dev/api?id=catchall)

알 수 없는 키를 검증하는 데 사용할 _catchall 스키마_를 정의하려면:

ZodZod Mini
```
    const DogWithStrings = z.object({
      name: z.string(),
      age: z.number().optional(),
    }).catchall(z.string());

    DogWithStrings.parse({ name: "Yeller", extraKey: "extraValue" }); // ✅
    DogWithStrings.parse({ name: "Yeller", extraKey: 42 }); // ❌
```

- [`.shape`](https://zod.dev/api?id=shape)

내부 스키마에 접근하려면:

ZodZod Mini
```
    Dog.shape.name; // => string schema
    Dog.shape.age; // => number schema
```

- [`.keyof()`](https://zod.dev/api?id=keyof)

객체 스키마의 키로 `ZodEnum` 스키마를 만들려면:

ZodZod Mini
```
    const keySchema = Dog.keyof();
    // => ZodEnum<["name", "age"]>
```

- [`.extend()`](https://zod.dev/api?id=extend)

객체 스키마에 필드를 추가하려면:

ZodZod Mini
```
    const DogWithBreed = Dog.extend({
      breed: z.string(),
    });
```

이 API는 기존 필드를 덮어쓸 수도 있습니다! 동일한 키가 두 스키마에 존재한다면 B가 A를 덮어씁니다.

**대안: spread 문법** — `.extend()`을 아예 사용하지 않고 새로운 객체 스키마를 만드는 방식도 있습니다. 이렇게 하면 결과 스키마의 엄격도 수준이 시각적으로 명확해집니다.
```
    const DogWithBreed = z.object({ // 또는 z.strictObject()나 z.looseObject()...
      ...Dog.shape,
      breed: z.string(),
    });
```

여러 객체를 한 번에 병합하는 데에도 이 방법을 사용할 수 있습니다.
```
    const DogWithBreed = z.object({
      ...Animal.shape,
      ...Pet.shape,
      breed: z.string(),
    });
```

이 접근에는 다음과 같은 장점이 있습니다:

  1. 라이브러리 전용 API 대신 언어 레벨 기능([스프레드 문법](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax))을 사용합니다.
  2. 동일한 문법이 Zod와 Zod Mini 모두에서 작동합니다.
  3. `tsc` 효율성이 높습니다 — `.extend()` 메서드는 큰 스키마에서 비용이 많이 들 수 있으며, [TypeScript 제약](https://github.com/microsoft/TypeScript/pull/61505)으로 인해 호출을 체인하면 비용이 제곱으로 증가합니다.
  4. 원한다면 `z.strictObject()`나 `z.looseObject()`를 사용해 결과 스키마의 엄격도를 바꿀 수 있습니다.

- [`.safeExtend()`](https://zod.dev/api?id=safeextend)

`.safeExtend()`는 `.extend()`와 유사하게 작동하지만, 기존 프로퍼티를 할당할 수 없는 스키마로 덮어쓸 수는 없습니다. 다시 말해, `.safeExtend()`의 결과는 원본을 TypeScript에서 [`extends`](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#conditional-type-constraints)하는 추론된 타입을 갖습니다.
```
    z.object({ a: z.string() }).safeExtend({ a: z.string().min(5) }); // ✅
    z.object({ a: z.string() }).safeExtend({ a: z.any() }); // ✅
    z.object({ a: z.string() }).safeExtend({ a: z.number() });
    //                                       ^  ❌ ZodNumber는 할당 불가능
```

`.safeExtend()`는 정제(refinement)를 포함하는 스키마를 확장할 때 사용하세요. (일반 `.extend()`는 정제가 있는 스키마에서 사용하면 에러를 던집니다.)

ZodZod Mini
```
    const Base = z.object({
      a: z.string(),
      b: z.string()
    }).refine(user => user.a === user.b);

    // Extended는 Base의 정제를 상속합니다.
    const Extended = Base.safeExtend({
      a: z.string().min(10)
    });
```

- [`.pick()`](https://zod.dev/api?id=pick)

TypeScript의 내장 유틸리티 타입 `Pick`과 `Omit`에서 영감을 받아, Zod는 객체 스키마에서 특정 키를 선택하거나 생략하는 전용 API를 제공합니다.

다음 초기 스키마에서:
```
    const Recipe = z.object({
      title: z.string(),
      description: z.string().optional(),
      ingredients: z.array(z.string()),
    });
    // { title: string; description?: string | undefined; ingredients: string[] }
```

특정 키를 선택하려면:

ZodZod Mini
```
    const JustTheTitle = Recipe.pick({ title: true });
```

- [`.omit()`](https://zod.dev/api?id=omit)

특정 키를 생략하려면:

ZodZod Mini
```
    const RecipeNoId = Recipe.omit({ id: true });
```

- [`.partial()`](https://zod.dev/api?id=partial)

편의를 위해, Zod는 일부 또는 모든 프로퍼티를 선택적으로 만드는 전용 API를 제공합니다. 이는 TypeScript 내장 유틸리티 타입 [`Partial`](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)에서 영감을 받았습니다.

모든 필드를 선택적으로 만들려면:

ZodZod Mini
```
    const PartialRecipe = Recipe.partial();
    // { title?: string | undefined; description?: string | undefined; ingredients?: string[] | undefined }
```

특정 속성만 선택적으로 만들려면:

ZodZod Mini
```
    const RecipeOptionalIngredients = Recipe.partial({
      ingredients: true,
    });
    // { title: string; description?: string | undefined; ingredients?: string[] | undefined }
```

- [`.required()`](https://zod.dev/api?id=required)

Zod는 일부 또는 모든 프로퍼티를 _필수_로 만드는 API를 제공합니다. 이는 TypeScript의 [`Required`](https://www.typescriptlang.org/docs/handbook/utility-types.html#requiredtype) 유틸리티 타입에서 영감을 받았습니다.

모든 프로퍼티를 필수로 만들려면:

ZodZod Mini
```
    const RequiredRecipe = Recipe.required();
    // { title: string; description: string; ingredients: string[] }
```

특정 프로퍼티만 필수로 만들려면:

ZodZod Mini
```
    const RecipeRequiredDescription = Recipe.required({description: true});
    // { title: string; description: string; ingredients: string[] }
```

## [재귀 객체](https://zod.dev/api?id=recursive-objects)

자기 참조 타입을 정의하려면 키에 [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)를 사용하세요. 이렇게 하면 JavaScript가 런타임에서 순환 스키마를 해결할 수 있습니다.
```
    const Category = z.object({
      name: z.string(),
      get subcategories(){
        return z.array(Category)
      }
    });

    type Category = z.infer<typeof Category>;
    // { name: string; subcategories: Category[] }
```

재귀 스키마는 지원되지만, 순환 데이터를 Zod에 전달하면 무한 루프가 발생합니다.

_상호 재귀 타입_도 표현할 수 있습니다:
```
    const User = z.object({
      email: z.email(),
      get posts(){
        return z.array(Post)
      }
    });

    const Post = z.object({
      title: z.string(),
      get author(){
        return User
      }
    });
```

모든 객체 API(`.pick()`, `.omit()`, `.required()`, `.partial()` 등)는 예상대로 작동합니다.

- [순환성(circularity) 에러](https://zod.dev/api?id=circularity-errors)

TypeScript 제약 때문에, 재귀 타입 추론은 까다로울 수 있으며 특정 상황에서만 작동합니다. 더 복잡한 타입은 다음과 같은 재귀 타입 에러를 발생시킬 수 있습니다:
```
    const Activity = z.object({
      name: z.string(),
      get subactivities() {
        // ^ ❌ 'subactivities'는 반환 타입 주석이 없고
        // 반환 표현식 중 하나에서 직접 또는 간접적으로 참조되기 때문에
        // 암묵적으로 'any' 반환 타입을 가지게 됩니다.ts(7023)

        return z.nullable(z.array(Activity));
      },
    });
```

이 경우 문제의 getter에 타입 주석을 추가해 에러를 해결할 수 있습니다:
```
    const Activity = z.object({
      name: z.string(),
      get subactivities(): z.ZodNullable<z.ZodArray<typeof Activity>> {
        return z.nullable(z.array(Activity));
      },
    });
```

## [배열](https://zod.dev/api?id=arrays)

배열 스키마를 정의하려면:

ZodZod Mini
```
    const stringArray = z.array(z.string()); // 또는 z.string().array()
```

배열 요소의 내부 스키마에 접근하려면:

ZodZod Mini
```
    stringArray.unwrap(); // => string 스키마
```

Zod는 다음과 같은 배열 전용 검증을 제공합니다:

ZodZod Mini
```
    z.array(z.string()).min(5); // 항목이 5개 이상이어야 함
    z.array(z.string()).max(5); // 항목이 5개 이하이어야 함
    z.array(z.string()).length(5); // 항목이 정확히 5개여야 함
```

## [튜플](https://zod.dev/api?id=tuples)

배열과 달리, 튜플은 일반적으로 고정 길이를 가지며 각 인덱스에 대해 서로 다른 스키마를 명시합니다.
```
    const MyTuple = z.tuple([
      z.string(),
      z.number(),
      z.boolean()
    ]);

    type MyTuple = z.infer<typeof MyTuple>;
    // [string, number, boolean]
```

가변("rest") 인수를 추가하려면:
```
    const variadicTuple = z.tuple([z.string()], z.number());
    // => [string, ...number[]];
```

## [유니온](https://zod.dev/api?id=unions)

유니온 타입(`A | B`)은 논리적 "OR"을 나타냅니다. Zod 유니온 스키마는 입력을 각 옵션에 차례로 검사합니다. 처음으로 성공적으로 검증되는 값을 반환합니다.
```
    const stringOrNumber = z.union([z.string(), z.number()]);
    // string | number

    stringOrNumber.parse("foo"); // 통과
    stringOrNumber.parse(14); // 통과
```

내부 옵션 스키마를 추출하려면:

ZodZod Mini
```
    stringOrNumber.options; // [ZodString, ZodNumber]
```

## [배타적 유니온 (XOR)](https://zod.dev/api?id=exclusive-unions-xor)

배타적 유니온(XOR)은 정확히 하나의 옵션만이 일치해야 하는 유니온입니다. 어떤 옵션이든 일치하면 성공하는 일반 유니온과 달리, `z.xor()`는 일치하는 옵션이 없거나 여러 개일 경우 실패합니다.
```
    const schema = z.xor([z.string(), z.number()]);

    schema.parse("hello"); // ✅ passes
    schema.parse(42);      // ✅ passes
    schema.parse(true);    // ❌ fails (zero matches)
```

옵션 간 상호배제를 보장하고 싶을 때 유용합니다:
```
    // 정확히 하나의 항목만 일치하는지 검증
    const payment = z.xor([
      z.object({ type: z.literal("card"), cardNumber: z.string() }),
      z.object({ type: z.literal("bank"), accountNumber: z.string() }),
    ]);

    payment.parse({ type: "card", cardNumber: "1234" }); // ✅ passes
```

입력이 여러 옵션과 일치할 수 있다면 `z.xor()`는 실패합니다:
```
    const overlapping = z.xor([z.string(), z.any()]);
    overlapping.parse("hello"); // ❌ fails (matches both string and any)
```

## [판별 유니온](https://zod.dev/api?id=discriminated-unions)

[판별 유니온](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)은 a) 모든 옵션이 객체 스키마이며 b) 특정 키(“판별자”)를 공유하는 특별한 유니온입니다. 판별자 키의 값에 따라 TypeScript는 예상대로 타입 서명을 “좁힐” 수 있습니다.
```
    type MyResult =
      | { status: "success"; data: string }
      | { status: "failed"; error: string };

    function handleResult(result: MyResult){
      if(result.status === "success"){
        result.data; // string
      } else {
        result.error; // string
      }
    }
```

일반 `z.union()`으로도 표현할 수 있지만, 일반 유니온은 _단순한_ 방식으로 입력을 순서대로 검사하고 먼저 통과한 옵션을 반환합니다. 대규모 유니온에서는 느릴 수 있습니다.

그래서 Zod는 구문 분석을 효율적으로 만드는 _판별자 키_를 사용하는 `z.discriminatedUnion()` API를 제공합니다.
```
    const MyResult = z.discriminatedUnion("status", [
      z.object({ status: z.literal("success"), data: z.string() }),
      z.object({ status: z.literal("failed"), error: z.string() }),
    ]);
```

각 옵션은 판별자 속성(`예에서는 status`)이 특정 리터럴 값 또는 값 집합(보통 `z.enum()`, `z.literal()`, `z.null()`, `z.undefined()`)에 해당하는 _객체 스키마_여야 합니다.

### 판별 유니온 중첩

## [교차점](https://zod.dev/api?id=intersections)

교차 타입(`A & B`)은 논리적 “AND”를 나타냅니다.
```
    const a = z.union([z.number(), z.string()]);
    const b = z.union([z.number(), z.boolean()]);
    const c = z.intersection(a, b);

    type c = z.infer<typeof c>; // => number
```

두 객체 타입을 교차할 때 유용합니다.
```
    const Person = z.object({ name: z.string() });
    type Person = z.infer<typeof Person>;

    const Employee = z.object({ role: z.string() });
    type Employee = z.infer<typeof Employee>;

    const EmployedPerson = z.intersection(Person, Employee);
    type EmployedPerson = z.infer<typeof EmployedPerson>;
    // Person & Employee
```

객체 스키마를 병합할 때는 교차보다 [`A.extend(B)`](https://zod.dev/api#extend)를 선호하세요. `.extend()`를 사용하면 새로운 객체 스키마를 얻지만, `z.intersection(A, B)`는 `pick`/`omit` 같은 일반 객체 메서드가 없는 `ZodIntersection` 인스턴스를 반환합니다.

## [레코드](https://zod.dev/api?id=records)

레코드 스키마는 `Record<string, string>`과 같은 타입을 검증하는 데 사용됩니다.

- [`z.record`](https://zod.dev/api?id=zrecord)
```
    const IdCache = z.record(z.string(), z.string());
    type IdCache = z.infer<typeof IdCache>; // Record<string, string>

    IdCache.parse({
      carlotta: "77d2586b-9e8e-4ecf-8b21-ea7e0530eadd",
      jimmie: "77d2586b-9e8e-4ecf-8b21-ea7e0530eadd",
    });
```

키 스키마는 `string | number | symbol`에 할당 가능한 모든 Zod 스키마일 수 있습니다.
```
    const Keys = z.union([z.string(), z.number(), z.symbol()]);
    const AnyObject = z.record(Keys, z.unknown());
    // Record<string | number | symbol, unknown>
```

열거형으로 정의된 키를 가진 객체 스키마를 만들려면:
```
    const Keys = z.enum(["id", "name", "email"]);
    const Person = z.record(Keys, z.string());
    // { id: string; name: string; email: string }
```

**신기능** — v4.2부터 Zod는 레코드 내부의 숫자 키를 TypeScript 자체와 유사하게 제대로 지원합니다. `number` 스키마를 레코드 키로 사용하면 해당 키가 유효한 “숫자 문자열”인지 검증합니다. 추가 숫자 제약조건(min, max, step 등)도 유효합니다.
```
    const numberKeys = z.record(z.number(), z.string());
    numberKeys.parse({
      1: "one", // ✅
      2: "two", // ✅
      "1.5": "one", // ✅
      "-3": "two", // ✅
      abc: "one" // ❌
    });

    // 추가 검증도 지원됩니다
    const intKeys = z.record(z.int().step(1).min(0).max(10), z.string());
    intKeys.parse({
      0: "zero", // ✅
      1: "one", // ✅
      2: "two", // ✅
      12: "twelve", // ❌
      abc: "one" // ❌
    });
```

- [`z.partialRecord`](https://zod.dev/api?id=zpartialrecord)

**Zod 4** — Zod 4에서 `z.record()`의 첫 번째 인자로 `z.enum`을 전달하면 Zod는 모든 enum 값이 입력 키로 존재하는지 철저히 확인합니다. 이 동작은 TypeScript와 일치합니다.
```
    type MyRecord = Record<"a" | "b", string>;
    const myRecord: MyRecord = { a: "foo", b: "bar" }; // ✅
    const myRecord: MyRecord = { a: "foo" }; // ❌ missing required key `b`
```

Zod 3에서는 전체 검사를 하지 않았습니다. 이전 동작을 재현하려면 `z.partialRecord()`를 사용하세요.

_부분적인_ 레코드 타입이 필요하면 `z.partialRecord()`를 사용하세요. 이 방식은 `z.enum()` 및 `z.literal()` 키 스키마에 대해 Zod가 일반적으로 실행하는 특수한 전체성 검사를 건너뜁니다.
```
    const Keys = z.enum(["id", "name", "email"]).or(z.never());
    const Person = z.partialRecord(Keys, z.string());
    // { id?: string; name?: string; email?: string }
```

- [`z.looseRecord`](https://zod.dev/api?id=zlooserecord)

기본적으로 `z.record()`는 키 스키마와 일치하지 않는 키에서 오류를 발생시킵니다. `z.looseRecord()`를 사용하면 일치하지 않는 키를 변경하지 않고 그대로 통과시킵니다. 이는 여러 패턴 속성을 모델링하기 위해 교차와 결합할 때 특히 유용합니다.
```
    const schema = z
      .object({ name: z.string() })
      .and(z.looseRecord(z.string().regex(/_phone$/), z.e164()));

    type schema = z.infer<typeof schema>;
    // => { name: string } & Record<string, string>

    schema.parse({
      name: "John",
      home_phone: "+12345678900",     // validated as phone number
      work_phone: "+12345678900",     // validated as phone number
    });
```

## [맵](https://zod.dev/api?id=maps)
```
    const StringNumberMap = z.map(z.string(), z.number());
    type StringNumberMap = z.infer<typeof StringNumberMap>; // Map<string, number>

    const myMap: StringNumberMap = new Map();
    myMap.set("one", 1);
    myMap.set("two", 2);

    StringNumberMap.parse(myMap);
```

## [셋](https://zod.dev/api?id=sets)
```
    const NumberSet = z.set(z.number());
    type NumberSet = z.infer<typeof NumberSet>; // Set<number>

    const mySet: NumberSet = new Set();
    mySet.add(1);
    mySet.add(2);
    NumberSet.parse(mySet);
```

셋 스키마는 다음 유틸리티 메서드로 추가 제약을 걸 수 있습니다.

ZodZod Mini
```
    z.set(z.string()).min(5); // must contain 5 or more items
    z.set(z.string()).max(5); // must contain 5 or fewer items
    z.set(z.string()).size(5); // must contain 5 items exactly
```

## [파일](https://zod.dev/api?id=files)

`File` 인스턴스를 검증하려면:

ZodZod Mini
```
    const fileSchema = z.file();

    fileSchema.min(10_000); // minimum .size (bytes)
    fileSchema.max(1_000_000); // maximum .size (bytes)
    fileSchema.mime("image/png"); // MIME type
    fileSchema.mime(["image/png", "image/jpeg"]); // multiple MIME types
```

## [Promises](https://zod.dev/api?id=promises)

**더 이상 사용되지 않음** — Zod 4에서 `z.promise()`는 더 이상 사용되지 않습니다. `Promise` 스키마에 적합한 유효한 사용 사례는 거의 없습니다. 값이 `Promise`일 수 있다고 의심되면 Zod로 파싱하기 전에 `await`로 먼저 해결하세요.

### See z.promise() documentation

## [Instanceof](https://zod.dev/api?id=instanceof)

`z.instanceof`를 사용하면 입력값이 특정 클래스의 인스턴스인지 확인할 수 있습니다. 이는 서드파티 라이브러리에서 내보낸 클래스에 대해 입력을 검증할 때 유용합니다.
```
    class Test {
      name: string;
    }

    const TestSchema = z.instanceof(Test);

    TestSchema.parse(new Test()); // ✅
    TestSchema.parse("whatever"); // ❌
```

- [Property](https://zod.dev/api?id=property)

클래스 인스턴스의 특정 속성을 Zod 스키마로 검증하려면:
```
    const blobSchema = z.instanceof(URL).check(
      z.property("protocol", z.literal("https:" as string, "Only HTTPS allowed"))
    );

    blobSchema.parse(new URL("https://example.com")); // ✅
    blobSchema.parse(new URL("http://example.com")); // ❌
```

`z.property()` API는 모든 데이터 유형과 함께 작동하지만 `z.instanceof()`와 함께 사용할 때 가장 유용합니다.
```
    const blobSchema = z.string().check(
      z.property("length", z.number().min(10))
    );

    blobSchema.parse("hello there!"); // ✅
    blobSchema.parse("hello."); // ❌
```

## [Refinements](https://zod.dev/api?id=refinements)

모든 Zod 스키마는 _refinements_ 배열을 저장합니다. Refinement는 Zod가 기본 API로 제공하지 않는 사용자 정의 검증을 수행하는 방법입니다.

- [`.refine()`](https://zod.dev/api?id=refine)

ZodZod Mini
```
    const myString = z.string().refine((val) => val.length <= 255);
```

Refinement 함수는 절대 예외를 던지면 안 됩니다. 대신 실패를 알리려면 falsy 값을 반환하세요. 던져진 오류는 Zod에서 잡히지 않습니다.

#
- [`error`](https://zod.dev/api?id=error)

오류 메시지를 사용자 정의하려면:

ZodZod Mini
```
    const myString = z.string().refine((val) => val.length > 8, {
      error: "Too short!"
    });
```

#
- [`abort`](https://zod.dev/api?id=abort)

기본적으로 체크에서 발생한 검증 문제는 _계속 가능한_ 것으로 간주됩니다. 즉, 한 검사에서 유효성 오류가 발생하더라도 Zod는 모두 순차적으로 실행합니다. 이는 한 번에 가능한 많은 오류를 모두 보여줄 수 있으므로 일반적으로 바람직합니다.

ZodZod Mini
```
    const myString = z.string()
      .refine((val) => val.length > 8, { error: "Too short!" })
      .refine((val) => val === val.toLowerCase(), { error: "Must be lowercase" });

    const result = myString.safeParse("OH NO");
    result.error?.issues;
    /* [
      { "code": "custom", "message": "Too short!" },
      { "code": "custom", "message": "Must be lowercase" }
    ] */
```

특정 refinement를 _계속 불가능한_ 것으로 표시하려면 `abort` 매개변수를 사용하세요. 검사가 실패하면 검증이 중단됩니다.

ZodZod Mini
```
    const myString = z.string()
      .refine((val) => val.length > 8, { error: "Too short!", abort: true })
      .refine((val) => val === val.toLowerCase(), { error: "Must be lowercase", abort: true });

    const result = myString.safeParse("OH NO");
    result.error?.issues;
    // => [{ "code": "custom", "message": "Too short!" }]
```

#
- [`path`](https://zod.dev/api?id=path)

오류 경로를 사용자 정의하려면 `path` 매개변수를 사용하세요. 이는 일반적으로 객체 스키마에서만 유용합니다.

ZodZod Mini
```
    const passwordForm = z
      .object({
        password: z.string(),
        confirm: z.string(),
      })
      .refine((data) => data.password === data.confirm, {
        message: "Passwords don't match",
        path: ["confirm"], // path of error
      });
```

이렇게 하면 관련 issue에 `path` 매개변수가 설정됩니다:

ZodZod Mini
```
    const result = passwordForm.safeParse({ password: "asdf", confirm: "qwer" });
    result.error.issues;
    /* [{
      "code": "custom",
      "path": [ "confirm" ],
      "message": "Passwords don't match"
    }] */
```

비동기 refinement를 정의하려면 `async` 함수를 전달하세요:
```
    const userId = z.string().refine(async (id) => {
      // verify that ID exists in database
      return true;
    });
```

비동기 refinement를 사용하면 반드시 `.parseAsync` 메서드로 데이터를 파싱해야 합니다! 그렇지 않으면 Zod가 오류를 던집니다.

ZodZod Mini
```
    const result = await userId.parseAsync("abc123");
```

#
- [`when`](https://zod.dev/api?id=when)

**참고** — 이 기능은 고급 사용자 기능이며, refinement 내부에서 발생하는 예외가 잡히지 않을 가능성을 높이는 방식으로 오용될 수 있습니다.

기본적으로 어떤 _계속 불가능한_ 문제가 이미 발생한 경우에는 refinement가 실행되지 않습니다. Zod는 refinement 함수에 값을 전달하기 전에 타입 시그니처가 올바른지 꼼꼼히 확인합니다.
```
    const schema = z.string().refine((val) => {
      return val.length > 8
    });

    schema.parse(1234); // invalid_type: refinement won't be executed
```

어떤 경우에는 refinement가 실행되는 시점을 더 세밀하게 제어하고 싶을 수 있습니다. 예를 들어 "비밀번호 확인" 검증을 고려하세요:

ZodZod Mini
```
    const schema = z
      .object({
        password: z.string().min(8),
        confirmPassword: z.string(),
        anotherField: z.string(),
      })
      .refine((data) => data.password === data.confirmPassword, {
        message: "Passwords do not match",
        path: ["confirmPassword"],
      });

    schema.parse({
      password: "asdf",
      confirmPassword: "asdf",
      anotherField: 1234 // ❌ this error will prevent the password check from running
    });
```

`anotherField`의 오류는 비밀번호 확인 검사가 실행되지 않도록 막습니다. 이 검사는 `anotherField`에 의존하지 않음에도 불구하고 그렇습니다. refinement가 언제 실행될지 제어하려면 `when` 매개변수를 사용하세요:

ZodZod Mini
```
    const schema = z
      .object({
        password: z.string().min(8),
        confirmPassword: z.string(),
        anotherField: z.string(),
      })
      .refine((data) => data.password === data.confirmPassword, {
        message: "Passwords do not match",
        path: ["confirmPassword"],

        // run if password & confirmPassword are valid
        when(payload) {
          return schema
            .pick({ password: true, confirmPassword: true })
            .safeParse(payload.value).success;
        },
      });

    schema.parse({
      password: "asdf",
      confirmPassword: "asdf",
      anotherField: 1234 // ❌ this error will not prevent the password check from running
    });
```

- [`.superRefine()`](https://zod.dev/api?id=superrefine)

일반 `.refine` API는 `"custom"` 오류 코드를 가진 단일 issue만 생성하지만, `.superRefine()`는 Zod의 [내부 issue 유형](https://github.com/colinhacks/zod/blob/main/packages/zod/src/v4/core/errors.ts)을 사용해 여러 개의 issue를 생성할 수 있도록 해줍니다.

ZodZod Mini
```
    const UniqueStringArray = z.array(z.string()).superRefine((val, ctx) => {
      if (val.length > 3) {
        ctx.addIssue({
          code: "too_big",
          maximum: 3,
          origin: "array",
          inclusive: true,
          message: "Too many items 😡",
          input: val,
        });
      }

      if (val.length !== new Set(val).size) {
        ctx.addIssue({
          code: "custom",
          message: `No duplicates allowed.`,
          input: val,
        });
      }
    });

```

- [`.check()`](https://zod.dev/api?id=check)

**참고** — `.check()` API는 일반적으로 `.superRefine()`보다 더 복잡한 저수준 API입니다. 성능이 중요한 코드 경로에서는 더 빨라질 수 있지만, 사용법은 더 장황합니다.

### View example

## [Codecs](https://zod.dev/api?id=codecs)

**새로운 기능** — Zod 4.1에서 도입되었습니다. 자세한 내용은 전용 [Codecs](https://zod.dev/codecs) 페이지를 참조하세요.

Codecs는 두 개의 다른 스키마 사이에서 _양방향 변환_을 구현하는 특수한 종류의 스키마입니다.
```
    const stringToDate = z.codec(
      z.iso.datetime(),  // input schema: ISO date string
      z.date(),          // output schema: Date object
      {
        decode: (isoString) => new Date(isoString), // ISO string → Date
        encode: (date) => date.toISOString(),       // Date → ISO string
      }
    );
```

- **translate**: 요청한 마크다운 전체를 자연스러운 한국어로 번역하고, 마크다운 구조와 코드는 그대로 유지했습니다.

**Translation**
- 영어 기술 마크다운을 자연스럽고 정확한 한국어로 번역했습니다. Markdown 구조, 헤딩 계층, 목록, 테이블을 그대로 유지했고 URL, 코드, CLI 플래그, 파일 경로, 변수, API 및 모델 ID는 변경하지 않았습니다.

