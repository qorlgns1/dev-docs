---
title: 'Zod Core'
description: '이 서브 패키지는 Zod 및 Zod Mini에서 사용하는 핵심 클래스와 유틸리티를 내보냅니다. 직접 사용할 목적으로 만들어진 것이 아니라 다른 패키지에서 확장하도록 설계되었습니다. 다음을 구현합니다:'
---

- 번역 요청의 주제는 **Zod Core**에 대한 기술 문서입니다.
- 완성된 답변은 영어 기술 Markdown의 구조, 헤더 계층, 리스트, 테이블을 그대로 유지한 한국어 번역본입니다.

# Zod Core

Copy markdown

[Edit this page](https://github.com/colinhacks/zod/edit/main/packages/docs/content/packages/core.mdx)

이 서브 패키지는 Zod 및 Zod Mini에서 사용하는 핵심 클래스와 유틸리티를 내보냅니다. 직접 사용할 목적으로 만들어진 것이 아니라 다른 패키지에서 확장하도록 설계되었습니다. 다음을 구현합니다:
```
    import * as z from "zod/v4/core";

    // 모든 Zod 스키마의 기반 클래스
    z.$ZodType;

    // 일반적인 파서를 구현하는 $ZodType의 하위 클래스
    z.$ZodString
    z.$ZodObject
    z.$ZodArray
    // ...

    // 모든 Zod 체크의 기반 클래스
    z.$ZodCheck;

    // 일반적인 체크를 구현하는 $ZodCheck의 하위 클래스
    z.$ZodCheckMinLength
    z.$ZodCheckMaxLength

    // 모든 Zod 오류의 기반 클래스
    z.$ZodError;

    // 이슈 형식(타입만)
    {} as z.$ZodIssue;

    // 유틸
    z.util.isValidJWT(...);
```

## [Schemas](https://zod.dev/packages/core?id=schemas)

모든 Zod 스키마의 기반 클래스는 `$ZodType`입니다. `Output`과 `Input`이라는 두 개의 제네릭 매개변수를 받습니다.
```
    export class $ZodType<Output = unknown, Input = unknown> {
      _zod: { /* internals */}
    }
```

`zod/v4/core`는 여러 일반 파서를 구현하는 하위 클래스를 내보냅니다. 모든 공식 하위 클래스의 합집합은 `z.$ZodTypes`로 내보내집니다.
```
    export type $ZodTypes =
      | $ZodString
      | $ZodNumber
      | $ZodBigInt
      | $ZodBoolean
      | $ZodDate
      | $ZodSymbol
      | $ZodUndefined
      | $ZodNullable
      | $ZodNull
      | $ZodAny
      | $ZodUnknown
      | $ZodNever
      | $ZodVoid
      | $ZodArray
      | $ZodObject
      | $ZodUnion // $ZodDiscriminatedUnion extends this
      | $ZodIntersection
      | $ZodTuple
      | $ZodRecord
      | $ZodMap
      | $ZodSet
      | $ZodLiteral
      | $ZodEnum
      | $ZodPromise
      | $ZodLazy
      | $ZodOptional
      | $ZodDefault
      | $ZodTemplateLiteral
      | $ZodCustom
      | $ZodTransform
      | $ZodNonOptional
      | $ZodReadonly
      | $ZodNaN
      | $ZodPipe // $ZodCodec extends this
      | $ZodSuccess
      | $ZodCatch
      | $ZodFile;
```

### Inheritance diagram

## [Internals](https://zod.dev/packages/core?id=internals)

모든 `zod/v4/core` 하위 클래스는 단일 프로퍼티 `_zod`만 포함합니다. 이 프로퍼티는 스키마의 내부 정보를 담은 객체입니다. `zod/v4/core`를 가능한 한 확장 가능하고 거칠지 않게 만들려는 목적입니다. 다른 라이브러리는 `zod/v4/core`가 인터페이스를 복잡하게 만들지 않은 이 클래스들을 기반으로 자체적인 Zod를 구성할 수 있습니다. 이러한 클래스들을 확장하는 예시는 `zod`와 `zod/mini` 구현을 참고하세요.

`_zod` 내부에는 다음과 같은 주목할 만한 프로퍼티가 포함됩니다:

  * `.def` — 스키마의 _정의_ : 이 객체를 클래스 생성자에 전달하여 인스턴스를 만듭니다. 스키마를 완전히 기술하며 JSON 직렬화가 가능합니다.
    * `.def.type` — 스키마의 타입을 나타내는 문자열, 예: `"string"`, `"object"`, `"array"` 등.
    * `.def.checks` — 파싱 후 실행되는 _체크_ 목록.
  * `.input` — 스키마의 _추론된 입력 타입_을 "저장"하는 가상 프로퍼티.
  * `.output` — 스키마의 _추론된 출력 타입_을 "저장"하는 가상 프로퍼티.
  * `.run()` — 스키마의 내부 파서 구현.

Zod 스키마를 순회해야 하는 도구(예: 코드 생성기)를 구현하는 경우, 어떤 스키마든 `$ZodTypes`로 캐스팅하고 `def` 프로퍼티를 사용해 해당 클래스를 판별할 수 있습니다.
```
    export function walk(_schema: z.$ZodType) {
      const schema = _schema as z.$ZodTypes;
      const def = schema._zod.def;
      switch (def.type) {
        case "string": {
          // ...
          break;
        }
        case "object": {
          // ...
          break;
        }
      }
    }
```

다양한 _문자열 포맷_을 구현하는 `$ZodString`의 하위 클래스가 여러 개 있습니다. 이들은 `z.$ZodStringFormatTypes`로 내보내집니다.
```
    export type $ZodStringFormatTypes =
      | $ZodGUID
      | $ZodUUID
      | $ZodEmail
      | $ZodURL
      | $ZodEmoji
      | $ZodNanoID
      | $ZodCUID
      | $ZodCUID2
      | $ZodULID
      | $ZodXID
      | $ZodKSUID
      | $ZodISODateTime
      | $ZodISODate
      | $ZodISOTime
      | $ZodISODuration
      | $ZodIPv4
      | $ZodIPv6
      | $ZodCIDRv4
      | $ZodCIDRv6
      | $ZodBase64
      | $ZodBase64URL
      | $ZodE164
      | $ZodJWT
```

## [Parsing](https://zod.dev/packages/core?id=parsing)

Zod Core 스키마 클래스에는 메서드가 없으므로 최상위 함수를 통해 데이터를 파싱합니다.
```
    import * as z from "zod/v4/core";

    const schema = new z.$ZodString({ type: "string" });
    z.parse(schema, "hello");
    z.safeParse(schema, "hello");
    await z.parseAsync(schema, "hello");
    await z.safeParseAsync(schema, "hello");
```

## [Checks](https://zod.dev/packages/core?id=checks)

모든 Zod 스키마에는 _체크_ 배열이 포함됩니다. 이는 파싱 이후 개선(때때로 변형)을 수행하지만 추론된 타입에는 영향을 주지 않습니다.
```
    const schema = z.string().check(z.email()).check(z.min(5));
    // => $ZodString

    schema._zod.def.checks;
    // => [$ZodCheckEmail, $ZodCheckMinLength]
```

모든 Zod 체크의 기반 클래스는 `$ZodCheck`입니다. 이 클래스는 하나의 제네릭 매개변수 `T`를 받습니다.
```
    export class $ZodCheck<in T = unknown> {
      _zod: { /* internals */}
    }
```

`_zod` 내부에는 다음과 같은 주목할 만한 프로퍼티가 포함됩니다:

  * `.def` — 체크의 _정의_ : 이 객체를 생성자에 전달하여 체크를 생성합니다. 체크를 완전히 기술하며 JSON 직렬화가 가능합니다.
    * `.def.check` — 체크의 타입을 나타내는 문자열, 예: `"min_length"`, `"less_than"`, `"string_format"` 등.
  * `.check()` — 체크의 검증 로직을 포함합니다.

`zod/v4/core`는 여러 일반적인 개선을 수행하는 하위 클래스를 내보냅니다. 모든 공식 하위 클래스는 `z.$ZodChecks`라는 공약집합으로 내보냅니다.
```
    export type $ZodChecks =
      | $ZodCheckLessThan
      | $ZodCheckGreaterThan
      | $ZodCheckMultipleOf
      | $ZodCheckNumberFormat
      | $ZodCheckBigIntFormat
      | $ZodCheckMaxSize
      | $ZodCheckMinSize
      | $ZodCheckSizeEquals
      | $ZodCheckMaxLength
      | $ZodCheckMinLength
      | $ZodCheckLengthEquals
      | $ZodCheckProperty
      | $ZodCheckMimeType
      | $ZodCheckOverwrite
      | $ZodCheckStringFormat
```

이러한 클래스들을 구분하려면 `._zod.def.check` 프로퍼티를 사용할 수 있습니다.
```
    const check = {} as z.$ZodChecks;
    const def = check._zod.def;

    switch (def.check) {
      case "less_than":
      case "greater_than":
        // ...
        break;
    }
```

스키마 타입과 마찬가지로, 다양한 _문자열 포맷_을 구현하는 `$ZodCheckStringFormat`의 하위 클래스들도 존재합니다.
```
    export type $ZodStringFormatChecks =
      | $ZodCheckRegex
      | $ZodCheckLowerCase
      | $ZodCheckUpperCase
      | $ZodCheckIncludes
      | $ZodCheckStartsWith
      | $ZodCheckEndsWith
      | $ZodGUID
      | $ZodUUID
      | $ZodEmail
      | $ZodURL
      | $ZodEmoji
      | $ZodNanoID
      | $ZodCUID
      | $ZodCUID2
      | $ZodULID
      | $ZodXID
      | $ZodKSUID
      | $ZodISODateTime
      | $ZodISODate
      | $ZodISOTime
      | $ZodISODuration
      | $ZodIPv4
      | $ZodIPv6
      | $ZodCIDRv4
      | $ZodCIDRv6
      | $ZodBase64
      | $ZodBase64URL
      | $ZodE164
      | $ZodJWT;
```

다양한 문자열 포맷 체크를 구분하려면 중첩된 `switch`를 사용하세요.
```
    const check = {} as z.$ZodChecks;
    const def = check._zod.def;

    switch (def.check) {
      case "less_than":
      case "greater_than":
      // ...
      case "string_format":
        {
          const formatCheck = check as z.$ZodStringFormatChecks;
          const formatCheckDef = formatCheck._zod.def;

          switch (formatCheckDef.format) {
            case "email":
            case "url":
              // do stuff
          }
        }
        break;
    }
```

위 문자열 형식 _체크_들 중 일부는 위에서 설명한 문자열 형식 _유형_과 겹칩니다. 이는 해당 클래스들이 `$ZodCheck`와 `$ZodType` 인터페이스를 모두 구현하기 때문입니다. 즉, 체크나 유형 둘 다로 사용할 수 있다는 뜻입니다. 이러한 경우에는 `._zod.parse`(스키마 파서)와 `._zod.check`(체크 검증) 모두 파싱 과정에서 실행됩니다. 사실상 인스턴스가 자신의 `checks` 배열 앞에 추가되지만(`._zod.def.checks`에는 실제로 존재하지 않습니다).
```
    // 유형으로
    z.email().parse("[[email protected]](https://zod.dev/cdn-cgi/l/email-protection)");

    // 체크로
    z.string().check(z.email()).parse("[[email protected]](https://zod.dev/cdn-cgi/l/email-protection)")
```

## [오류](https://zod.dev/packages/core?id=errors)

Zod의 모든 오류의 기본 클래스는 `$ZodError`입니다.

성능 상의 이유로 `$ZodError`는 기본 제공 `Error` 클래스를 _상속하지 않습니다!_ 따라서 `instanceof Error`는 `false`를 반환합니다.

  * `zod` 패키지는 몇 가지 편의 메서드를 추가한 `$ZodError`의 하위 클래스 `ZodError`를 구현합니다.
  * `zod/mini` 서브패키지는 `$ZodError`를 직접 사용합니다.

```
    export class $ZodError<T = unknown> implements Error {
     public issues: $ZodIssue[];
    }
```

## [이슈](https://zod.dev/packages/core?id=issues)

`issues` 속성은 `$ZodIssue` 객체 배열에 대응합니다. 모든 이슈는 `z.$ZodIssueBase` 인터페이스를 확장합니다.
```
    export interface $ZodIssueBase {
      readonly code?: string;
      readonly input?: unknown;
      readonly path: PropertyKey[];
      readonly message: string;
    }
```

Zod는 다음과 같은 이슈 하위 타입들을 정의합니다:
```
    export type $ZodIssue =
      | $ZodIssueInvalidType
      | $ZodIssueTooBig
      | $ZodIssueTooSmall
      | $ZodIssueInvalidStringFormat
      | $ZodIssueNotMultipleOf
      | $ZodIssueUnrecognizedKeys
      | $ZodIssueInvalidUnion
      | $ZodIssueInvalidKey
      | $ZodIssueInvalidElement
      | $ZodIssueInvalidValue
      | $ZodIssueCustom;
```

각 타입에 대한 자세한 내용은 [구현부](https://github.com/colinhacks/zod/blob/main/packages/zod/src/v4/core/errors.ts)를 참고하세요.

[Zod MiniZod Mini - 트리 쉐이커블 Zod](https://zod.dev/packages/mini)

