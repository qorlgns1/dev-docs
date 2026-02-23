---
title: '[z.fromJSONSchema()](https://zod.dev/json-schema?id=zfromjsonschema)'
description: '💎 Zod 4는 새로운 기능인 네이티브 JSON Schema 변환을 도입합니다. JSON Schema는 JSON의 구조를 기술하는 표준으로, OpenAPI 정의나 AI용 구조화된 출력 정의에 널리 사용됩니다.'
---

💎 **Zod 4는 새로운 기능인 네이티브 [JSON Schema](https://json-schema.org/) 변환을 도입합니다. JSON Schema는 JSON의 구조를 기술하는 표준으로, [OpenAPI](https://www.openapis.org/) 정의나 AI용 [구조화된 출력](https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat) 정의에 널리 사용됩니다.**

## [`z.fromJSONSchema()`](https://zod.dev/json-schema?id=zfromjsonschema)

**실험적** — `z.fromJSONSchema()` 함수는 실험 단계이며 Zod의 안정된 API의 일부로 간주되지 않습니다. 향후 릴리스에서 구현이 변경될 가능성이 높습니다.

Zod는 `z.fromJSONSchema()`를 제공하여 JSON Schema를 Zod 스키마로 변환합니다.
```
    import * as z from "zod";

    const jsonSchema = {
      type: "object",
      properties: {
        name: { type: "string" },
        age: { type: "number" },
      },
      required: ["name", "age"],
    };

    const zodSchema = z.fromJSONSchema(jsonSchema);
```

## [`z.toJSONSchema()`](https://zod.dev/json-schema?id=ztojsonschema)

Zod 스키마를 JSON Schema로 변환하려면 `z.toJSONSchema()` 함수를 사용하세요.
```
    import * as z from "zod";

    const schema = z.object({
      name: z.string(),
      age: z.number(),
    });

    z.toJSONSchema(schema)
    // => {
    //   type: 'object',
    //   properties: { name: { type: 'string' }, age: { type: 'number' } },
    //   required: [ 'name', 'age' ],
    //   additionalProperties: false,
    // }
```

모든 스키마와 검사 조건은 가능한 가장 가까운 JSON Schema 대응으로 변환됩니다. 일부 타입은 대응할 수 없으며 합리적으로 표현할 수 없습니다. 아래 [`unrepresentable`](https://zod.dev/json-schema#unrepresentable) 섹션에서 이러한 경우를 처리하는 방법을 확인하세요.
```
    z.bigint(); // ❌
    z.int64(); // ❌
    z.symbol(); // ❌
    z.undefined(); // ❌
    z.void(); // ❌
    z.date(); // ❌
    z.map(); // ❌
    z.set(); // ❌
    z.transform(); // ❌
    z.nan(); // ❌
    z.custom(); // ❌
```

두 번째 인수로 변환 로직을 사용자 정의할 수 있습니다.
```
    z.toJSONSchema(schema, {
      // ...params
    })
```

아래는 지원되는 매개변수별 간단한 참고입니다. 각 항목은 아래에서 더 자세히 설명합니다.
```
    interface ToJSONSchemaParams {
      /** The JSON Schema version to target.
       * - `"draft-2020-12"` — Default. JSON Schema Draft 2020-12
       * - `"draft-07"` — JSON Schema Draft 7
       * - `"draft-04"` — JSON Schema Draft 4
       * - `"openapi-3.0"` — OpenAPI 3.0 Schema Object */
      target?:
        | "draft-04"
        | "draft-4"
        | "draft-07"
        | "draft-7"
        | "draft-2020-12"
        | "openapi-3.0"
        | ({} & string)
        | undefined;

      /** A registry used to look up metadata for each schema.
       * Any schema with an `id` property will be extracted as a $def. */
      metadata?: $ZodRegistry<Record<string, any>>;

      /** How to handle unrepresentable types.
       * - `"throw"` — Default. Unrepresentable types throw an error
       * - `"any"` — Unrepresentable types become `{}` */
      unrepresentable?: "throw" | "any";

      /** How to handle cycles.
       * - `"ref"` — Default. Cycles will be broken using $defs
       * - `"throw"` — Cycles will throw an error if encountered */
      cycles?: "ref" | "throw";

      /* How to handle reused schemas.
       * - `"inline"` — Default. Reused schemas will be inlined
       * - `"ref"` — Reused schemas will be extracted as $defs */
      reused?: "ref" | "inline";

      /** A function used to convert `id` values to URIs to be used in *external* $refs.
       *
       * Default is `(id) => id`.
       */
      uri?: (id: string) => string;
    }
```

- [`io`](https://zod.dev/json-schema?id=io)

일부 스키마 타입은 입력 타입과 출력 타입이 다릅니다(예: `ZodPipe`, `ZodDefault`, 강제 변환된 기본 타입). 기본적으로 `z.toJSONSchema`의 결과는 _출력 타입_을 나타냅니다; 입력 타입을 추출하려면 `"io": "input"`을 사용하세요.
```
    const mySchema = z.string().transform(val => val.length).pipe(z.number());
    // ZodPipe

    const jsonSchema = z.toJSONSchema(mySchema);
    // => { type: "number" }

    const jsonSchema = z.toJSONSchema(mySchema, { io: "input" });
    // => { type: "string" }
```

- [`target`](https://zod.dev/json-schema?id=target)

대상 JSON Schema 버전을 설정하려면 `target` 매개변수를 사용하세요. 기본값은 Draft 2020-12입니다.
```
    z.toJSONSchema(schema, { target: "draft-07" });
    z.toJSONSchema(schema, { target: "draft-2020-12" });
    z.toJSONSchema(schema, { target: "draft-04" });
    z.toJSONSchema(schema, { target: "openapi-3.0" });
```

- [`metadata`](https://zod.dev/json-schema?id=metadata)

아직 읽지 않았다면 Zod에서 메타데이터를 저장하는 방법에 대한 맥락으로 [Metadata and registries](https://zod.dev/metadata) 페이지를 먼저 참고하세요.

Zod에서는 메타데이터를 레지스트리에 저장합니다. Zod는 `id`, `title`, `description`, `examples` 같은 공통 메타데이터 필드를 저장할 수 있는 전역 레지스트리 `z.globalRegistry`를 내보냅니다.

ZodZod Mini
```
    import * as z from "zod";

    // `.meta()`는 `z.globalRegistry`에 스키마를 등록하는 편의 메서드입니다.
    const emailSchema = z.string().meta({
      title: "Email address",
      description: "Your email address",
    });

    z.toJSONSchema(emailSchema);
    // => { type: "string", title: "Email address", description: "Your email address", ... }
```

모든 메타데이터 필드는 결과 JSON Schema에 복사됩니다.
```
    const schema = z.string().meta({
      whatever: 1234
    });

    z.toJSONSchema(schema);
    // => { type: "string", whatever: 1234 }
```

- [`unrepresentable`](https://zod.dev/json-schema?id=unrepresentable)

다음 API는 JSON Schema로 표현할 수 없습니다. 기본적으로 Zod는 이들을 만나면 오류를 던집니다. JSON에서 대응되는 것이 없으므로 변환을 시도하는 것은 부적절합니다. 다음 중 하나를 만나면 오류가 발생합니다.
```
    z.bigint(); // ❌
    z.int64(); // ❌
    z.symbol(); // ❌
    z.undefined(); // ❌
    z.void(); // ❌
    z.date(); // ❌
    z.map(); // ❌
    z.set(); // ❌
    z.transform(); // ❌
    z.nan(); // ❌
    z.custom(); // ❌
```

기본적으로 Zod는 이러한 타입을 만나면 오류를 던집니다.
```
    z.toJSONSchema(z.bigint());
    // => throws Error
```

`unrepresentable` 옵션을 `"any"`로 설정하면 이 동작을 변경할 수 있습니다. 그러면 표현할 수 없는 모든 타입을 JSON Schema에서 `{}`(`unknown`과 동등함)로 변환합니다.
```
    z.toJSONSchema(z.bigint(), { unrepresentable: "any" });
    // => {}
```

- [`cycles`](https://zod.dev/json-schema?id=cycles)

순환을 처리하는 방법입니다. `z.toJSONSchema()`가 스키마를 순회하면서 순환을 만나면 `$ref`로 표현됩니다.
```
    const User = z.object({
      name: z.string(),
      get friend() {
        return User;
      },
    });

    z.toJSONSchema(User);
    // => {
    //   type: 'object',
    //   properties: { name: { type: 'string' }, friend: { '$ref': '#' } },
    //   required: [ 'name', 'friend' ],
    //   additionalProperties: false,
    // }
```

대신 오류를 발생시키고 싶다면 `cycles` 옵션을 `"throw"`로 설정하세요.
```
    z.toJSONSchema(User, { cycles: "throw" });
    // => throws Error
```

- [`reused`](https://zod.dev/json-schema?id=reused)

동일한 스키마가 한 스키마 내에서 여러 번 등장할 때의 처리 방식입니다. 기본적으로 Zod는 이러한 스키마를 인라인합니다.
```
    const name = z.string();
    const User = z.object({
      firstName: name,
      lastName: name,
    });

    z.toJSONSchema(User);
    // => {
    //   type: 'object',
    //   properties: {
    //     firstName: { type: 'string' },
    //     lastName: { type: 'string' }
    //   },
    //   required: [ 'firstName', 'lastName' ],
    //   additionalProperties: false,
    // }
```

`reused` 옵션을 `"ref"`로 설정하여 이 스키마들을 `$defs`로 추출할 수 있습니다.
```
    z.toJSONSchema(User, { reused: "ref" });
    // => {
    //   type: 'object',
    //   properties: {
    //     firstName: { '$ref': '#/$defs/__schema0' },
    //     lastName: { '$ref': '#/$defs/__schema0' }
    //   },
    //   required: [ 'firstName', 'lastName' ],
    //   additionalProperties: false,
    //   '$defs': { __schema0: { type: 'string' } }
    // }
```

- [`override`](https://zod.dev/json-schema?id=override)

`override`를 사용해 맞춤 덮어쓰기 로직을 정의할 수 있습니다. 제공된 콜백은 원래 Zod 스키마와 기본 JSON Schema에 접근할 수 있습니다. _이 함수는 `ctx.jsonSchema`를 직접 수정해야 합니다._
```
    const mySchema = /* ... */
    z.toJSONSchema(mySchema, {
      override: (ctx)=>{
        ctx.zodSchema; // the original Zod schema
        ctx.jsonSchema; // the default JSON Schema

        // directly modify
        ctx.jsonSchema.whatever = "sup";
      }
    });
```

표현할 수 없는 타입은 이 함수가 호출되기 전에 `Error`를 던집니다. 표현할 수 없는 타입에 대해 사용자 정의 동작을 정의하려면 `override`와 함께 `unrepresentable: "any"`를 설정해야 합니다.
```
    // support z.date() as ISO datetime strings
    const result = z.toJSONSchema(z.date(), {
      unrepresentable: "any",
      override: (ctx) => {
        const def = ctx.zodSchema._zod.def;
        if(def.type ==="date"){
          ctx.jsonSchema.type = "string";
          ctx.jsonSchema.format = "date-time";
        }
      },
    });
```

## [Conversion](https://zod.dev/json-schema?id=conversion)

다음은 Zod의 JSON Schema 변환 로직에 대한 추가 설명입니다.

- [String formats](https://zod.dev/json-schema?id=string-formats)

Zod는 다음 스키마 타입들을 동등한 JSON Schema `format`으로 변환합니다.
```
    // Supported via `format`
    z.email(); // => { type: "string", format: "email" }
    z.iso.datetime(); // => { type: "string", format: "date-time" }
    z.iso.date(); // => { type: "string", format: "date" }
    z.iso.time(); // => { type: "string", format: "time" }
    z.iso.duration(); // => { type: "string", format: "duration" }
    z.ipv4(); // => { type: "string", format: "ipv4" }
    z.ipv6(); // => { type: "string", format: "ipv6" }
    z.uuid(); // => { type: "string", format: "uuid" }
    z.guid(); // => { type: "string", format: "uuid" }
    z.url(); // => { type: "string", format: "uri" }
```

이 스키마들은 `contentEncoding`을 통해 지원됩니다.
```
    z.base64(); // => { type: "string", contentEncoding: "base64" }
```

다른 모든 문자열 형식은 `pattern`을 통해 지원됩니다.
```
    z.base64url();
    z.cuid();
    z.emoji();
    z.nanoid();
    z.cuid2();
    z.ulid();
    z.cidrv4();
    z.cidrv6();
    z.mac();
```

- [Numeric types](https://zod.dev/json-schema?id=numeric-types)

Zod는 다음 숫자 타입을 JSON Schema로 변환합니다.
```
    // number
    z.number(); // => { type: "number" }
    z.float32(); // => { type: "number", exclusiveMinimum: ..., exclusiveMaximum: ... }
    z.float64(); // => { type: "number", exclusiveMinimum: ..., exclusiveMaximum: ... }

    // integer
    z.int(); // => { type: "integer" }
    z.int32(); // => { type: "integer", exclusiveMinimum: ..., exclusiveMaximum: ... }
```

- [Object schemas](https://zod.dev/json-schema?id=object-schemas)

기본적으로 `z.object()` 스키마는 `additionalProperties: "false"`를 포함합니다. 이는 평범한 `z.object()` 스키마가 추가 속성을 제거하는 Zod의 기본 동작을 정확히 반영한 것입니다.
```
    import * as z from "zod";

    const schema = z.object({
      name: z.string(),
      age: z.number(),
    });

    z.toJSONSchema(schema)
    // => {
    //   type: 'object',
    //   properties: { name: { type: 'string' }, age: { type: 'number' } },
    //   required: [ 'name', 'age' ],
    //   additionalProperties: false,
    // }
```

`"input"` 모드로 JSON Schema로 변환할 때는 `additionalProperties`가 설정되지 않습니다. 자세한 내용은 [`io` 문서](https://zod.dev/json-schema#io)를 참고하세요.
```
    import * as z from "zod";

    const schema = z.object({
      name: z.string(),
      age: z.number(),
    });

    z.toJSONSchema(schema, { io: "input" });
    // => {
    //   type: 'object',
    //   properties: { name: { type: 'string' }, age: { type: 'number' } },
    //   required: [ 'name', 'age' ],
    // }
```

반면:

  * `z.looseObject()`는 `additionalProperties: false`를 절대 설정하지 않습니다.
  * `z.strictObject()`는 항상 `additionalProperties: false`를 설정합니다.

- [File schemas](https://zod.dev/json-schema?id=file-schemas)

Zod는 `z.file()`을 다음 OpenAPI 친화적인 스키마로 변환합니다.
```
    z.file();
    // => { type: "string", format: "binary", contentEncoding: "binary" }
```

크기 및 MIME 검사도 표현됩니다.
```
    z.file().min(1).max(1024 * 1024).mime("image/png");
    // => {
    //   type: "string",
    //   format: "binary",
    //   contentEncoding: "binary",
    //   contentMediaType: "image/png",
    //   minLength: 1,
    //   maxLength: 1048576,
    // }
```

- [Nullability](https://zod.dev/json-schema?id=nullability)

Zod는 `z.null()`을 JSON Schema에서 `{ type: "null" }`로 변환합니다.
```
    z.null();
    // => { type: "null" }
```

`z.undefined()`는 JSON Schema에서 표현할 수 없음을 참고하세요 ([아래](https://zod.dev/json-schema#unrepresentable) 참조).

비슷하게, `nullable`은 `null`과의 유니언으로 표현됩니다.
```
    z.nullable(z.string());
    // => { oneOf: [{ type: "string" }, { type: "null" }] }
```

`optional` 스키마는 그대로 표현되지만 `optional` 주석이 붙습니다.
```
    z.optional(z.string());
    // => { type: "string" }
```

## [Registries](https://zod.dev/json-schema?id=registries)

스키마를 `z.toJSONSchema()`에 전달하면 _자체 포함_ JSON Schema가 반환됩니다.

또 다른 경우에는 여러 연결된 JSON Schema로 표현하려는 Zod 스키마 세트를 `.json` 파일로 작성하여 웹 서버에서 제공하려는 경우가 있을 수 있습니다.
```
    import * as z from "zod";

    const User = z.object({
      name: z.string(),
      get posts(){
        return z.array(Post);
      }
    });

    const Post = z.object({
      title: z.string(),
      content: z.string(),
      get author(){
        return User;
      }
    });

    z.globalRegistry.add(User, {id: "User"});
    z.globalRegistry.add(Post, {id: "Post"});
```

이를 위해 `z.toJSONSchema()`에 [registry](https://zod.dev/metadata#registries)를 전달할 수 있습니다.

**중요** — 모든 스키마는 레지스트리에 등록된 `id` 속성을 가져야 합니다! `id`가 없는 스키마는 무시됩니다.
```
    z.toJSONSchema(z.globalRegistry);
    // => {
    //   schemas: {
    //     User: {
    //       id: 'User',
    //       type: 'object',
    //       properties: {
    //         name: { type: 'string' },
    //         posts: { type: 'array', items: { '$ref': 'Post' } }
    //       },
    //       required: [ 'name', 'posts' ],
    //       additionalProperties: false,
    //     },
    //     Post: {
    //       id: 'Post',
    //       type: 'object',
    //       properties: {
    //         title: { type: 'string' },
    //         content: { type: 'string' },
    //         author: { '$ref': 'User' }
    //       },
    //       required: [ 'title', 'content', 'author' ],
    //       additionalProperties: false,
    //     }
    //   }
    // }
```

기본적으로 `$ref` URI는 `"User"`처럼 간단한 상대 경로입니다. 이러한 경로를 절대 URI로 만들려면 `uri` 옵션을 사용하세요. 이 옵션은 `id`를 완전한 URI로 변환하는 함수를 기대합니다.
```
    z.toJSONSchema(z.globalRegistry, {
      uri: (id) => `https://example.com/${id}.json`
    });
    // => {
    //   schemas: {
    //     User: {
    //       id: 'User',
    //       type: 'object',
    //       properties: {
    //         name: { type: 'string' },
    //         posts: {
    //           type: 'array',
    //           items: { '$ref': 'https://example.com/Post.json' }
    //         }
    //       },
    //       required: [ 'name', 'posts' ],
    //       additionalProperties: false,
    //     },
    //     Post: {
    //       id: 'Post',
    //       type: 'object',
    //       properties: {
    //         title: { type: 'string' },
    //         content: { type: 'string' },
    //         author: { '$ref': 'https://example.com/User.json' }
    //       },
    //       required: [ 'title', 'content', 'author' ],
    //       additionalProperties: false,
    //     }
    //   }
    // }
```

