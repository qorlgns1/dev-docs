---
title: '[에러 커스터마이징](https://zod.dev/v4/changelog?id=error-customization)'
description: 'Zod 4는 에러 커스터마이징 API를 단일 통합된  매개변수로 표준화했습니다. 이전에는 API가 분산되고 일관성이 부족했는데, Zod 4에서 정리되었습니다.'
---

**Migration guide**
- 이 문서는 Zod 4에서의 주요 breaking change들을 중요도 순으로 정리합니다. Zod 4의 성능 개선 및 새 기능은 [첫 글](https://zod.dev/v4)을 읽어보세요.  
- 설치:  
  ```bash
  npm install zod@^4.0.0
  ```

- Zod의 동작과 API가 훨씬 직관적이고 일관되게 정리되었습니다. 여기서 정리한 breaking change는 Zod 사용자를 위한 큰 품질 향상으로 작용하므로, 반드시 꼼꼼히 읽으시길 권합니다.  
- **참고** — Zod 3에는 문서화되지 않은 준내부 유틸리티 타입과 함수들이 있었으며, 이는 공개 API로 간주되지 않습니다. 해당 변경사항은 이 문서에 다루지 않습니다.  
- **비공식 코드모드** — 커뮤니티에서 유지보수하는 코드모드 [`zod-v3-to-v4`](https://github.com/nicoespeon/zod-v3-to-v4)를 사용하실 수 있습니다.

## [에러 커스터마이징](https://zod.dev/v4/changelog?id=error-customization)

Zod 4는 에러 커스터마이징 API를 단일 통합된 `error` 매개변수로 표준화했습니다. 이전에는 API가 분산되고 일관성이 부족했는데, Zod 4에서 정리되었습니다.

- [ `message` 매개변수 deprecated](https://zod.dev/v4/changelog?id=deprecates-message-parameter)  
  `message`를 `error`로 대체합니다. 기존 `message` 매개변수는 여전히 지원되나 deprecated입니다.

- [ `invalid_type_error`와 `required_error` 제거](https://zod.dev/v4/changelog?id=drops-invalid_type_error-and-required_error)  
  `invalid_type_error` / `required_error`는 더 이상 지원되지 않습니다. 예전에는 `errorMap`보다 간결한 커스터마이징 수단으로 급하게 도입되었지만, 다양한 부작용(특히 `errorMap`과 병행 사용할 수 없음)과 Zod의 실제 issue 코드와 맞지 않아서 제거되었습니다.  
  이 기능은 새로운 `error` 매개변수로 명확히 표현할 수 있습니다.

  ```ts
  z.string({
    error: (issue) => issue.input === undefined
      ? "This field is required"
      : "Not a string"
  });
  ```

- [ `errorMap` 이름 변경](https://zod.dev/v4/changelog?id=drops-errormap)  
  이제 `error`라고 부릅니다.  
  에러 맵은 `{ message: string }` 대신 `string`을 직접 반환할 수도 있고, `undefined`를 반환하면 다음 에러 맵에 처리를 넘깁니다.

  ```ts
  z.string().min(5, {
    error: (issue) => {
      if (issue.code === "too_small") {
        return `Value must be >${issue.minimum}`
      }
    },
  });
  ```

## [`ZodError`](https://zod.dev/v4/changelog?id=zoderror)

- [이슈 포맷 업데이트](https://zod.dev/v4/changelog?id=updates-issue-formats)  
  이슈 포맷이 크게 간소화되었습니다.

  ```ts
  import * as z from "zod"; // v4

  type IssueFormats =
    | z.core.$ZodIssueInvalidType
    | z.core.$ZodIssueTooBig
    | z.core.$ZodIssueTooSmall
    | z.core.$ZodIssueInvalidStringFormat
    | z.core.$ZodIssueNotMultipleOf
    | z.core.$ZodIssueUnrecognizedKeys
    | z.core.$ZodIssueInvalidValue
    | z.core.$ZodIssueInvalidUnion
    | z.core.$ZodIssueInvalidKey // new: used for z.record/z.map
    | z.core.$ZodIssueInvalidElement // new: used for z.map/z.set
    | z.core.$ZodIssueCustom;
  ```

  아래는 Zod 3의 이슈 타입과 Zod 4 대응 항목입니다.

  ```ts
  import * as z from "zod"; // v3

  export type IssueFormats =
    | z.ZodInvalidTypeIssue // ♻️ renamed to z.core.$ZodIssueInvalidType
    | z.ZodTooBigIssue  // ♻️ renamed to z.core.$ZodIssueTooBig
    | z.ZodTooSmallIssue // ♻️ renamed to z.core.$ZodIssueTooSmall
    | z.ZodInvalidStringIssue // ♻️ z.core.$ZodIssueInvalidStringFormat
    | z.ZodNotMultipleOfIssue // ♻️ renamed to z.core.$ZodIssueNotMultipleOf
    | z.ZodUnrecognizedKeysIssue // ♻️ renamed to z.core.$ZodIssueUnrecognizedKeys
    | z.ZodInvalidUnionIssue // ♻️ renamed to z.core.$ZodIssueInvalidUnion
    | z.ZodCustomIssue // ♻️ renamed to z.core.$ZodIssueCustom
    | z.ZodInvalidEnumValueIssue // ❌ merged in z.core.$ZodIssueInvalidValue
    | z.ZodInvalidLiteralIssue // ❌ merged into z.core.$ZodIssueInvalidValue
    | z.ZodInvalidUnionDiscriminatorIssue // ❌ throws an Error at schema creation time
    | z.ZodInvalidArgumentsIssue // ❌ z.function throws ZodError directly
    | z.ZodInvalidReturnTypeIssue // ❌ z.function throws ZodError directly
    | z.ZodInvalidDateIssue // ❌ merged into invalid_type
    | z.ZodInvalidIntersectionTypesIssue // ❌ removed (throws regular Error)
    | z.ZodNotFiniteIssue // ❌ infinite values no longer accepted (invalid_type)
  ```

  몇몇 Zod 4 이슈 타입은 병합, 제거, 수정되었지만, 대부분의 경우 Zod 3과 구조적으로 거의 동일하며 동일한 기본 인터페이스를 따르므로 기존 에러 처리 로직 대부분은 수정 없이 작동합니다.

  ```ts
  export interface $ZodIssueBase {
    readonly code?: string;
    readonly input?: unknown;
    readonly path: PropertyKey[];
    readonly message: string;
  }
  ```

- [에러 맵 우선순위 변경](https://zod.dev/v4/changelog?id=changes-error-map-precedence)  
  `.parse()`에 전달되는 에러 맵이 스키마 수준 에러 맵보다 우선하지 않도록 바뀌었습니다.

  ```ts
  const mySchema = z.string({ error: () => "Schema-level error" });

  // Zod 3
  mySchema.parse(12, { error: () => "Contextual error" }); // => "Contextual error"

  // Zod 4
  mySchema.parse(12, { error: () => "Contextual error" }); // => "Schema-level error"
  ```

- [`.format()` deprecated](https://zod.dev/v4/changelog?id=deprecates-format)  
  `ZodError`의 `.format()`은 deprecated 되었습니다. 대신 최상위 `z.treeifyError()`를 사용하세요. 자세한 내용은 [Formatting errors docs](https://zod.dev/error-formatting)를 참조하세요.

- [`.flatten()` deprecated](https://zod.dev/v4/changelog?id=deprecates-flatten)  
  `.flatten()` 역시 deprecated 되었으며, 동일하게 `z.treeifyError()`를 사용하세요. 자세한 내용은 [Formatting errors docs](https://zod.dev/error-formatting)를 참조하세요.

- [`.formErrors` 제거](https://zod.dev/v4/changelog?id=drops-formerrors)  
  이 API는 `.flatten()`과 동일했으며, 역사적인 이유로 존재했지만 문서화되어 있지 않습니다.

- [`.addIssue()` 및 `.addIssues()` deprecated](https://zod.dev/v4/changelog?id=deprecates-addissue-and-addissues)  
  필요하다면 직접 `err.issues` 배열에 푸시하세요.

  ```ts
  myError.issues.push({
    // new issue
  });
  ```

## [`z.number()`](https://zod.dev/v4/changelog?id=znumber)

- [무한 값 금지](https://zod.dev/v4/changelog?id=no-infinite-values)  
  `POSITIVE_INFINITY`와 `NEGATIVE_INFINITY`는 더 이상 `z.number()`의 유효한 값으로 간주되지 않습니다.

- [`.safe()`가 float를 받지 않음](https://zod.dev/v4/changelog?id=safe-no-longer-accepts-floats)  
  Zod 3에서 `z.number().safe()`는 deprecated 상태로, 이제 `.int()`와 동일하게 동작합니다(아래 참조). 이 말은 곧 float를 더 이상 허용하지 않는다는 뜻입니다.

- [`.int()`는 safe integer만 허용](https://zod.dev/v4/changelog?id=int-accepts-safe-integers-only)  
  `z.number().int()`는 이제 `Number.MIN_SAFE_INTEGER`와 `Number.MAX_SAFE_INTEGER` 범위를 벗어난 unsafe integer를 허용하지 않습니다. 범위를 벗어난 정수를 쓰면 반올림 오류가 발생할 수 있습니다. (`z.int()` 사용 고려)

## [`z.string()` 업데이트](https://zod.dev/v4/changelog?id=zstring-updates)

- [`.email()` 등 deprecated](https://zod.dev/v4/changelog?id=deprecates-email-etc)

**번역**
- String 형식은 이제 내부 refinement가 아닌 `ZodString`의 서브클래스로 표현되며, 이 API들이 최상위 `z` 네임스페이스로 옮겨졌고 더 간결하며 트리 쉐이킹에 유리합니다.
```
    z.email();
    z.uuid();
    z.url();
    z.emoji();         // 단일 이모지 문자 검증
    z.base64();
    z.base64url();
    z.nanoid();
    z.cuid();
    z.cuid2();
    z.ulid();
    z.ipv4();
    z.ipv6();
    z.cidrv4();          // IP 범위
    z.cidrv6();          // IP 범위
    z.iso.date();
    z.iso.time();
    z.iso.datetime();
    z.iso.duration();
```
- `z.string().email()` 같은 메서드 형태도 여전히 존재하지만 이제 deprecated입니다.
```
    z.string().email(); // ❌ deprecated
    z.email(); // ✅
```

- [.uuid() 강화](https://zod.dev/v4/changelog?id=stricter-uuid): `z.uuid()`가 이제 RFC 9562/4122 규격을 더 엄격하게 따릅니다(variant 비트가 사양대로 `10`이어야 함). 더 관대한 “UUID 유사” 검증이 필요하면 `z.guid()`를 사용하세요.
```
    z.uuid(); // RFC 9562/4122 호환 UUID
    z.guid(); // 8-4-4-4-12 16진수 패턴
```

- [.base64url()에서 padding 제거](https://zod.dev/v4/changelog?id=no-padding-in-base64url): 예전 `z.string().base64url()`처럼 raise padding은 허용되지 않으며, base64url 문자열은 대개 padding 없이 URL 안전해야 합니다.

- [`z.string().ip()` 제거](https://zod.dev/v4/changelog?id=drops-zstringip): 이제 `.ipv4()`와 `.ipv6()`로 대체되며 둘 다 허용하려면 `z.union()`을 사용하세요.
```
    z.string().ip() // ❌
    z.ipv4() // ✅
    z.ipv6() // ✅
```

- [`z.string().ipv6()` 업데이트](https://zod.dev/v4/changelog?id=updates-zstringipv6): `new URL()` 생성자를 사용해 검증하므로 이전 정규표현식보다 훨씬 탄탄합니다. 이전에 통과되던 일부 잘못된 값이 이제 실패할 수 있습니다.

- [`z.string().cidr()` 제거](https://zod.dev/v4/changelog?id=drops-zstringcidr): `.cidrv4()`/`.cidrv6()`로 분리되었으니 `z.union()`으로 둘을 합치세요.
```
    z.string().cidr() // ❌
    z.cidrv4() // ✅
    z.cidrv6() // ✅
```

## [`z.coerce` 업데이트](https://zod.dev/v4/changelog?id=zcoerce-updates)
모든 `z.coerce` 스키마 입력 타입이 이제 `unknown`입니다.
```
    const schema = z.coerce.string();
    type schemaInput = z.input<typeof schema>;

    // Zod 3: string;
    // Zod 4: unknown;
```

## [`.default()` 업데이트](https://zod.dev/v4/changelog?id=default-updates)
입력이 `undefined`면 `ZodDefault`가 파싱을 중단하고 기본값을 반환하며, 기본값은 _출력 타입_에 할당 가능해야 합니다.
```
    const schema = z.string()
      .transform(val => val.length)
      .default(0); // 숫자여야 함
    schema.parse(undefined); // => 0
```

Zod 3에서는 `.default()`가 _입력 타입_에 맞는 값을 기대했고, `ZodDefault`가 기본값을 파싱했으므로 기본값은 스키마의 _입력 타입_에 할당 가능해야 했습니다.
```
    // Zod 3
    const schema = z.string()
      .transform(val => val.length)
      .default("tuna");
    schema.parse(undefined); // => 4
```

이전 동작을 재현하려면 `.prefault()` API를 사용합니다(“pre-parse default”).
```
    // Zod 3
    const schema = z.string()
      .transform(val => val.length)
      .prefault("tuna");
    schema.parse(undefined); // => 4
```

## [`z.object()`](https://zod.dev/v4/changelog?id=zobject)

- [선택적 필드 내부에서도 기본값 적용](https://zod.dev/v4/changelog?id=defaults-applied-within-optional-fields): 속성 내부 기본값이 선택적 필드 안에서도 적용됩니다; 이는 Zod 3의 장기적인 사용성 문제를 해결하며, 키 존재 여부에 의존한 코드에서 눈에 띄는 변화가 있을 수 있습니다.
```
    const schema = z.object({
      a: z.string().default("tuna").optional(),
    });

    schema.parse({});
    // Zod 4: { a: "tuna" }
    // Zod 3: {}
```

- [.strict()/.passthrough() deprecated](https://zod.dev/v4/changelog?id=deprecates-strict-and-passthrough): 이제 최상위 `z.strictObject()`/`z.looseObject()`를 사용하세요.
```
    // Zod 3
    z.object({ name: z.string() }).strict();
    z.object({ name: z.string() }).passthrough();

    // Zod 4
    z.strictObject({ name: z.string() });
    z.looseObject({ name: z.string() });
```
이 메서드들은 하위 호환성을 위해 여전히 존재하며 제거되지 않습니다(레거시).

- [.strip() 제거](https://zod.dev/v4/changelog?id=deprecates-strip): `z.object()` 기본 동작이어서 유용성이 적었으며, strict 객체를 “일반” 객체로 바꾸려면 `z.object(A.shape)`를 사용하세요.

- [.nonstrict() 제거](https://zod.dev/v4/changelog?id=drops-nonstrict): `.strip()`의 오래된 별칭으로 제거되었습니다.

- [.deepPartial() 제거](https://zod.dev/v4/changelog?id=drops-deeppartial): Zod 3에서 오래전부터 deprecated였으며 이제 제거되었습니다. 직접적인 대체 API가 없으며 구현상 함정이 많아 일반적으로 안티 패턴입니다.

- [z.unknown() 선택성 변경](https://zod.dev/v4/changelog?id=changes-zunknown-optionality): `z.unknown()`과 `z.any()` 타입은 추론된 타입에서 더 이상 “키가 optional”로 표시되지 않습니다.
```
    const mySchema = z.object({
      a: z.any(),
      b: z.unknown()
    });
    // Zod 3: { a?: any; b?: unknown };
    // Zod 4: { a: any; b: unknown };
```

- [.merge() deprecated](https://zod.dev/v4/changelog?id=deprecates-merge): `ZodObject`의 `.merge()`는 `.extend()`로 대체되어 ambiguous strictness 상속을 피하고 TypeScript 성능을 개선합니다.
```
    // .merge (deprecated)
    const ExtendedSchema = BaseSchema.merge(AdditionalSchema);

    // .extend (권장)
    const ExtendedSchema = BaseSchema.extend(AdditionalSchema.shape);

    // 또는 구조 분해 (TSC 성능 최상)
    const ExtendedSchema = z.object({
      ...BaseSchema.shape,
      ...AdditionalSchema.shape,
    });
```
**참고**: TypeScript 성능을 더 개선하려면 `.extend()` 대신 구조 분해를 고려하세요. 자세한 내용은 [API 문서](https://zod.dev/api?id=extend)를 참조하세요.

## [`z.nativeEnum()` deprecated](https://zod.dev/v4/changelog?id=znativeenum-deprecated)
`z.nativeEnum()`는 이제 deprecated이며, `z.enum()`이 enum 유사 입력을 지원하도록 오버로드되었습니다.
```
    enum Color {
      Red = "red",
      Green = "green",
      Blue = "blue",
    }

    const ColorSchema = z.enum(Color); // ✅
```
`ZodEnum` 리팩토링의 일환으로 오래된 redundant 기능들이 제거되었습니다. 이들은 모두 동일하고 역사적 이유로만 존재했습니다.
```
    ColorSchema.enum.Red; // ✅ => "Red" (정식 API)
    ColorSchema.Enum.Red; // ❌ 제거됨
    ColorSchema.Values.Red; // ❌ 제거됨
```

## [`z.array()`](https://zod.dev/v4/changelog?id=zarray)

- [.nonempty() 타입 변경](https://zod.dev/v4/changelog?id=changes-nonempty-type): 이제 `z.array().min(1)`과 동일하게 동작하며, 추론된 타입은 변하지 않습니다.
```
    const NonEmpty = z.array(z.string()).nonempty();

    type NonEmpty = z.infer<typeof NonEmpty>;
    // Zod 3: [string, ...string[]]
    // Zod 4: string[]
```
기존 동작은 `z.tuple()`과 rest 인자를 통해 더 잘 표현됩니다. 이는 TypeScript 타입 시스템과 더 밀접하게 맞아떨어집니다.
```
    z.tuple([z.string()], z.string());
    // => [string, ...string[]]
```

## [`z.promise()` deprecated](https://zod.dev/v4/changelog?id=zpromise-deprecated)

`z.promise()` 를 사용할 이유는 거의 없습니다. 입력이 `Promise` 일 수 있다면, Zod로 파싱하기 전에 그냥 `await` 하세요.

`z.function()` 으로 비동기 함수를 정의하기 위해 `z.promise` 를 쓰고 있다면, 이제 더 이상 필요 없습니다; 아래 [`ZodFunction`](https://zod.dev/v4/changelog#function) 섹션을 참고하세요.

## [`z.function()`](https://zod.dev/v4/changelog?id=zfunction)

`z.function()` 의 결과는 더 이상 Zod 스키마가 아닙니다. 대신, Zod 유효성 검사를 적용한 함수를 정의하기 위한 독립적인 “함수 팩토리” 역할을 합니다. API도 바뀌었으며, 이제는 `args()` 와 `.returns()` 를 쓰는 대신에 `input` 과 `output` 스키마를 미리 정의합니다.

Zod 4Zod 3
```
    const myFunction = z.function({
      input: [z.object({
        name: z.string(),
        age: z.number().int(),
      })],
      output: z.string(),
    });

    myFunction.implement((input) => {
      return `Hello ${input.name}, you are ${input.age} years old.`;
    });
```

함수 타입을 가진 Zod 스키마를 정말로 써야 한다면, [이 해결책](https://github.com/colinhacks/zod/issues/4143#issuecomment-2845134912)을 고려하세요.

- [`.implementAsync()` 추가](https://zod.dev/v4/changelog?id=adds-implementasync)

비동기 함수를 정의하려면 `implement()` 대신 `implementAsync()` 를 사용하세요.
```
    myFunction.implementAsync(async (input) => {
      return `Hello ${input.name}, you are ${input.age} years old.`;
    });
```

## [`.refine()`](https://zod.dev/v4/changelog?id=refine)

- [타입 술어 무시](https://zod.dev/v4/changelog?id=ignores-type-predicates)

Zod 3에서는 [타입 술어](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates) 를 refine 함수로 넘기면 스키마 타입을 좁힐 수 있었지만, 문서화되지 않았고 일부 이슈에서만 언급되었으며 이제는 더 이상 그렇지 않습니다.
```
    const mySchema = z.unknown().refine((val): val is string => {
      return typeof val === "string"
    });

    type MySchema = z.infer<typeof mySchema>;
    // Zod 3: `string`
    // Zod 4: 여전히 `unknown`
```

- [ctx.path 제거](https://zod.dev/v4/changelog?id=drops-ctxpath)

Zod의 새로운 파싱 아키텍처에서는 `path` 배열을 미리 계산하지 않습니다. 이는 Zod 4의 획기적인 성능 향상을 가능하게 하는 필수 변경이었습니다.
```
    z.string().superRefine((val, ctx) => {
      ctx.path; // ❌ 더 이상 없음
    });
```

- [두 번째 인자로 함수 삭제](https://zod.dev/v4/changelog?id=drops-function-as-second-argument)

다음과 같은 무시무시한 오버로드는 제거되었습니다.
```
    const longString = z.string().refine(
      (val) => val.length > 10,
      (val) => ({ message: `${val} is not more than 10 characters` })
    );
```

## [`z.ostring()`, 기타 제거됨](https://zod.dev/v4/changelog?id=zostring-etc-dropped)

문서화되지 않은 편의 메서드 `z.ostring()`, `z.onumber()` 등은 제거되었습니다. 이들은 선택적 문자열 스키마를 간단히 정의하는 단축 메서드였습니다.

## [`z.literal()`](https://zod.dev/v4/changelog?id=zliteral)

- [`symbol` 지원 제거](https://zod.dev/v4/changelog?id=drops-symbol-support)

심볼은 리터럴 값으로 간주되지 않으며, `===` 로 간단히 비교할 수 없습니다. 이는 Zod 3에서 놓친 부분이었습니다.

## [정적 `.create()` 팩토리 제거됨](https://zod.dev/v4/changelog?id=static-create-factories-dropped)

이전에는 모든 Zod 클래스가 정적 `.create()` 메서드를 정의했지만, 이제는 독립적인 팩토리 함수로 구현됩니다.
```
    z.ZodString.create(); // ❌
```

## [`z.record()`](https://zod.dev/v4/changelog?id=zrecord)

- [단일 인자 사용 제거](https://zod.dev/v4/changelog?id=drops-single-argument-usage)

이전에는 `z.record()` 를 단일 인자로 사용할 수 있었지만, 이제는 지원하지 않습니다.
```
    // Zod 3
    z.record(z.string()); // ✅

    // Zod 4
    z.record(z.string()); // ❌
    z.record(z.string(), z.string()); // ✅
```

- [enum 지원 강화](https://zod.dev/v4/changelog?id=improves-enum-support)

Record가 훨씬 똑똑해졌습니다. Zod 3에서는 enum을 `z.record()` 의 키 스키마로 넣으면 부분 타입이 되어
```
    const myRecord = z.record(z.enum(["a", "b", "c"]), z.number());
    // { a?: number; b?: number; c?: number; }
```

Zod 4에서는 더 이상 그렇지 않습니다. 추론된 타입은 기대한 그대로고, Zod는 모든 enum 키가 파싱 중 입력에 존재하는지를 검사하는 종합성을 보장합니다.
```
    const myRecord = z.record(z.enum(["a", "b", "c"]), z.number());
    // { a: number; b: number; c: number; }
```

예전처럼 선택적 키를 원하면 `z.partialRecord()` 를 사용하세요:
```
    const myRecord = z.partialRecord(z.enum(["a", "b", "c"]), z.number());
    // { a?: number; b?: number; c?: number; }
```

## [`z.intersection()`](https://zod.dev/v4/changelog?id=zintersection)

- [병합 충돌 시 `Error` 발생](https://zod.dev/v4/changelog?id=throws-error-on-merge-conflict)

Zod intersection은 입력을 두 스키마로 파싱한 후 결과를 병합하려고 시도합니다. Zod 3에서는 결과가 병합 불가능할 경우 `invalid_intersection_types` 이슈가 있는 `ZodError` 를 던졌습니다.

Zod 4에서는 일반 `Error` 를 던집니다. 병합 불가능한 결과가 존재한다는 것은 구조적으로 호환되지 않는 두 타입의 교차(intersection)을 의미하므로, 검증 오류보다는 일반 오류가 더 적절합니다.

## [내부 변경 사항](https://zod.dev/v4/changelog?id=internal-changes)

Zod의 일반 사용자는 이 아래 내용을 대부분 무시해도 됩니다. 이 변경은 사용자 인터페이스 `z` API에는 영향을 주지 않습니다.

여기에 나열하기에는 내부 변경 사항이 너무 많지만, 특정 구현 세부 사항에 의도적으로나 무심코 의존하고 있는 사용자에게는 일부가 관련 있을 수 있습니다. 이 변경은 Zod 위에 도구를 만드는 라이브러리 저자에게 특히 중요합니다.

- [제네릭 업데이트](https://zod.dev/v4/changelog?id=updates-generics)

몇몇 클래스의 제네릭 구조가 바뀌었습니다. 아마도 가장 중요한 변화는 `ZodType` 기본 클래스의 변화입니다:
```
    // Zod 3
    class ZodType<Output, Def extends z.ZodTypeDef, Input = Output> {
      // ...
    }

    // Zod 4
    class ZodType<Output = unknown, Input = unknown> {
      // ...
    }
```

두 번째 제네릭인 `Def` 는 완전히 사라졌습니다. 대신 기본 클래스는 이제 `Output` 과 `Input` 만 추적합니다. 이전에는 `Input` 값이 `Output` 으로 기본값이 설정되어 있었지만, 이제는 `unknown` 으로 기본값이 설정됩니다. 이는 `z.ZodType` 을 포함하는 제네릭 함수들이 많은 경우에 더 직관적으로 동작하게 만듭니다.
```
    function inferSchema<T extends z.ZodType>(schema: T): T {
      return schema;
    };

    inferSchema(z.string()); // z.ZodString
```

`z.ZodTypeAny` 의 필요성이 사라졌습니다; 그냥 `z.ZodType` 을 사용하세요.

- [`z.core` 추가](https://zod.dev/v4/changelog?id=adds-zcore)

많은 유틸리티 함수와 타입이 새로운 `zod/v4/core` 서브 패키지로 이동하여 Zod와 Zod Mini 간 코드 공유를 용이하게 했습니다.
```
    import * as z from "zod/v4/core";

    function handleError(iss: z.$ZodError) {
      // do stuff
    }
```

편의를 위해 `zod/v4/core` 의 내용은 `z` 와 `zod/mini` 에서도 `z.core` 네임스페이스를 통해 다시 내보냅니다.
```
    import * as z from "zod";

    function handleError(iss: z.core.$ZodError) {
      // do stuff
    }
```

핵심 하위 라이브러리의 내용에 대해서는 [Zod Core](https://zod.dev/packages/core) 문서를 참고하세요.

- [`._def` 이동](https://zod.dev/v4/changelog?id=moves-_def)

`._def` 속성이 이제 `._zod.def` 로 이동했습니다. 모든 내부 정의(def)의 구조는 변경될 수 있으며, 이는 라이브러리 저자에게 관련되지만 여기서 모두 문서화되지는 않습니다.

- [`ZodEffects` 제거](https://zod.dev/v4/changelog?id=drops-zodeffects)

이것은 사용자 인터페이스 API에는 영향을 주지 않지만, 강조할 가치가 있는 내부 변경입니다. Zod가 _refinements_ 를 처리하는 방식 전체를 재구성한 일부입니다.

이전에는 refinement와 transform이 `ZodEffects`라는 래퍼 클래스 내부에 함께 존재했습니다. 즉 스키마에 어느 하나를 추가하면 원본 스키마가 `ZodEffects` 인스턴스로 감싸졌습니다. Zod 4에서는 refinement가 이제 스키마 자체에 내장되어 있습니다. 좀 더 정확히 말하면, 각 스키마는 "체크" 배열을 포함하며, “체크”라는 개념은 Zod 4에서 새로 도입되어 `z.toLowerCase()`처럼 부작용이 있을 수 있는 transform도 refinement 범주에 포함되도록 일반화합니다.

이 점은 `.check()` 메서드로 다양한 검증을 조합하는 Zod Mini API에서 특히 잘 드러납니다.
```
    import * as z from "zod/mini";

    z.string().check(
      z.minLength(10),
      z.maxLength(100),
      z.toLowerCase(),
      z.trim(),
    );
```

- [adds `ZodTransform`](https://zod.dev/v4/changelog?id=adds-zodtransform)

한편 transform은 전용 `ZodTransform` 클래스로 이동했습니다. 이 스키마 클래스는 입력 변환을 나타내며, 현재는 단독 변환도 정의할 수 있습니다:
```
    import * as z from "zod";

    const schema = z.transform(input => String(input));

    schema.parse(12); // => "12"
```

이것은 주로 `ZodPipe`와 함께 사용됩니다. `.transform()` 메서드는 이제 `ZodPipe` 인스턴스를 반환합니다.
```
    z.string().transform(val => val); // ZodPipe<ZodString, ZodTransform>
```

- [drops `ZodPreprocess`](https://zod.dev/v4/changelog?id=drops-zodpreprocess)

`.transform()`과 마찬가지로 `z.preprocess()` 함수는 이제 전용 `ZodPreprocess` 인스턴스 대신 `ZodPipe` 인스턴스를 반환합니다.
```
    z.preprocess(val => val, z.string()); // ZodPipe<ZodTransform, ZodString>
```

- [drops `ZodBranded`](https://zod.dev/v4/changelog?id=drops-zodbranded)

브랜딩은 이제 전용 `ZodBranded` 클래스 대신 추론된 타입 자체를 직접 수정하여 처리합니다. 사용자에게 노출되는 API는 그대로 유지됩니다.

