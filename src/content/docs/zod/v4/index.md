---
title: '릴리스 노트'
description: '1년간의 활발한 개발 끝에: Zod 4가 이제 안정화되었습니다! 더 빠르고, 가볍고,  효율이 더 좋으며 오랫동안 요청받았던 기능들을 구현했습니다.'
---

**번역**

# 릴리스 노트

Copy markdown

[이 페이지 편집](https://github.com/colinhacks/zod/edit/main/packages/docs/content/v4/index.mdx)

1년간의 활발한 개발 끝에: Zod 4가 이제 안정화되었습니다! 더 빠르고, 가볍고, `tsc` 효율이 더 좋으며 오랫동안 요청받았던 기능들을 구현했습니다.

❤️

매우 관대한 [OSS 펠로십](https://clerk.com/blog/zod-fellowship)을 통해 Zod 4 작업을 지원해준 [Clerk](https://go.clerk.com/zod-clerk)에게 큰 감사를 전합니다. 기대보다 훨씬 길어진 개발 과정 동안 훌륭한 파트너였습니다.

## [버전 관리](https://zod.dev/v4?id=versioning)

업그레이드하려면:
```
    npm install zod@^4.0.0
```

모든 주요 변경 사항 목록은 [Migration guide](https://zod.dev/v4/changelog)를 참고하세요. 이 게시물은 새로운 기능 및 개선 사항에 집중합니다.

## [왜 새로운 메이저 버전인가요?](https://zod.dev/v4?id=why-a-new-major-version)

Zod v3.0은 2021년 5월에 출시되었습니다(!). 당시 Zod는 GitHub에서 2,700개의 스타와 주간 60만 다운로드를 기록했습니다. 오늘날에는 37.8k의 스타와 주간 3,100만 다운로드(6주 전 베타 출시 당시 2,300만에서 증가)입니다. 24개의 마이너 버전 이후, Zod 3 코드베이스는 한계에 도달했고 가장 많이 요청된 기능과 개선 사항들은 호환성 깨짐을 수반했습니다.

Zod 4는 Zod 3의 오래된 설계 제약을 한 번에 해결하여 여러 오래 요청된 기능과 엄청난 성능 향상을 가능하게 했습니다. Zod의 [오픈 이슈 중 가장 많은 추천을 받은 10개 이슈](https://github.com/colinhacks/zod/issues?q=is%3Aissue%20state%3Aopen%20sort%3Areactions-%2B1-desc) 중 9개를 닫았습니다. 운이 따라준다면 앞으로 수년간의 기반이 되어줄 것입니다.

새로운 내용의 빠른 개요는 목차를 참고하세요. 원하는 항목을 클릭하면 해당 섹션으로 이동합니다.

## [벤치마크](https://zod.dev/v4?id=benchmarks)

이 벤치마크는 Zod 저장소에서 직접 실행할 수 있습니다:
```
    $ git clone [[email protected]](https://zod.dev/cdn-cgi/l/email-protection):colinhacks/zod.git
    $ cd zod
    $ git switch v4
    $ pnpm install
```

특정 벤치마크를 실행하려면:
```
    $ pnpm bench <name>
```

- [문자열 파싱 14배 빠름](https://zod.dev/v4?id=14x-faster-string-parsing)
```
    $ pnpm bench string
    runtime: node v22.13.0 (arm64-darwin)

    benchmark      time (avg)             (min … max)       p75       p99      p999
    ------------------------------------------------- -----------------------------
    • z.string().parse
    ------------------------------------------------- -----------------------------
    zod3          363 µs/iter       (338 µs … 683 µs)    351 µs    467 µs    572 µs
    zod4       24'674 ns/iter    (21'083 ns … 235 µs) 24'209 ns 76'125 ns    120 µs

    summary for z.string().parse
      zod4
       14.71x faster than zod3
```

- [배열 파싱 7배 빠름](https://zod.dev/v4?id=7x-faster-array-parsing)
```
    $ pnpm bench array
    runtime: node v22.13.0 (arm64-darwin)

    benchmark      time (avg)             (min … max)       p75       p99      p999
    ------------------------------------------------- -----------------------------
    • z.array() parsing
    ------------------------------------------------- -----------------------------
    zod3          147 µs/iter       (137 µs … 767 µs)    140 µs    246 µs    520 µs
    zod4       19'817 ns/iter    (18'125 ns … 436 µs) 19'125 ns 44'500 ns    137 µs

    summary for z.array() parsing
      zod4
       7.43x faster than zod3
```

- [객체 파싱 6.5배 빠름](https://zod.dev/v4?id=65x-faster-object-parsing)

이 벤치마크는 [Moltar 검증 라이브러리 벤치마크](https://moltar.github.io/typescript-runtime-type-benchmarks/)를 실행합니다.
```
    $ pnpm bench object-moltar
    benchmark      time (avg)             (min … max)       p75       p99      p999
    ------------------------------------------------- -----------------------------
    • z.object() safeParse
    ------------------------------------------------- -----------------------------
    zod3          805 µs/iter     (771 µs … 2'802 µs)    804 µs    928 µs  2'802 µs
    zod4          124 µs/iter     (118 µs … 1'236 µs)    119 µs    231 µs    329 µs

    summary for z.object() safeParse
      zod4
       6.5x faster than zod3
```

## [`tsc` 인스턴스화 100배 감소](https://zod.dev/v4?id=100x-reduction-in-tsc-instantiations)

다음 간단한 파일을 고려하세요:
```
    import * as z from "zod";

    export const A = z.object({
      a: z.string(),
      b: z.string(),
      c: z.string(),
      d: z.string(),
      e: z.string(),
    });

    export const B = A.extend({
      f: z.string(),
      g: z.string(),
      h: z.string(),
    });
```

`"zod/v3"`을 사용하는 `tsc --extendedDiagnostics`로 이 파일을 컴파일하면 25,000개 이상의 타입 인스턴스가 생성됩니다. `"zod/v4"`로는 약 175개만 생성됩니다.

Zod 저장소에는 `tsc` 벤치마크 플레이그라운드가 있습니다. `packages/tsc` 내의 컴파일러 벤치마크로 직접 확인해 보세요. 구현이 발전하면서 정확한 숫자는 달라질 수 있습니다.
```
    $ cd packages/tsc
    $ pnpm bench object-with-extend
```

더 중요한 점은, Zod 4가 `ZodObject`와 기타 스키마 클래스의 제네릭을 재설계하고 단순화하여 악명 높은 “인스턴스화 폭발” 문제를 피했다는 것입니다. 예를 들어 `.extend()`와 `.omit()`을 반복해서 체이닝하는 작업은 이전에는 컴파일러 문제를 일으켰습니다:
```
    import * as z from "zod";

    export const a = z.object({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const b = a.omit({
      a: true,
      b: true,
      c: true,
    });

    export const c = b.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const d = c.omit({
      a: true,
      b: true,
      c: true,
    });

    export const e = d.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const f = e.omit({
      a: true,
      b: true,
      c: true,
    });

    export const g = f.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const h = g.omit({
      a: true,
      b: true,
      c: true,
    });

    export const i = h.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const j = i.omit({
      a: true,
      b: true,
      c: true,
    });

    export const k = j.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const l = k.omit({
      a: true,
      b: true,
      c: true,
    });

    export const m = l.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const n = m.omit({
      a: true,
      b: true,
      c: true,
    });

    export const o = n.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });

    export const p = o.omit({
      a: true,
      b: true,
      c: true,
    });

    export const q = p.extend({
      a: z.string(),
      b: z.string(),
      c: z.string(),
    });
```

Zod 3에서는 이 컴파일이 `4000ms`가 걸렸고, 추가 `.extend()` 호출은 “무한 가능성” 오류를 유발했습니다. Zod 4에서는 `400ms`만에 컴파일되며 10배 빠릅니다.

다가오는 [`tsgo`](https://github.com/microsoft/typescript-go) 컴파일러와 함께, Zod 4의 에디터 성능은 훨씬 더 큰 스키마와 코드베이스에서도 확장됩니다.

## [코어 번들 크기 2배 감소](https://zod.dev/v4?id=2x-reduction-in-core-bundle-size)

다음과 같은 간단한 스크립트를 고려해 보세요.
```
    import * as z from "zod";

    const schema = z.boolean();

    schema.parse(true);
```

검증 측면에서 가장 단순한 예에 가까우며, 이건 _코어 번들 크기_ —즉, 간단한 경우에도 번들에 포함될 코드—를 측정하는 데 좋습니다. Zod 3과 Zod 4로 `rollup` 번들을 만들고 최종 번들을 비교해 보겠습니다.

패키지| 번들 (gzip)
---|---
Zod 3| `12.47kb`
Zod 4| `5.36kb`

Zod 4의 코어 번들은 약 57% 줄어들었으며(2.3배), 아주 좋은 결과입니다. 하지만 우리는 훨씬 더 개선할 수 있습니다.

## [Zod Mini 소개](https://zod.dev/v4?id=introducing-zod-mini)

Zod의 메서드 중심 API는 트리쉐이킹이 본질적으로 어렵습니다. 간단한 `z.boolean()` 스크립트조차도 `.optional()`, `.array()` 같은 사용하지 않은 여러 메서드 구현을 끌어옵니다. 더 슬림한 구현만으로는 한계가 있습니다. 바로 Zod Mini가 필요한 이유입니다.
```
    npm install zod@^4.0.0
```

Zod Mini는 `zod`와 1:1 대응하는, 함수형이며 트리쉐이커블한 API를 가진 Zod의 변형입니다. Zod가 메서드를 사용할 때 Zod Mini는 일반적으로 래퍼 함수를 사용합니다:

Zod MiniZod
```
    import * as z from "zod/mini";

    z.optional(z.string());

    z.union([z.string(), z.number()]);

    z.extend(z.object({ /* ... */ }), { age: z.number() });
```

모든 메서드를 없애지는 않았습니다! 파싱 관련 메서드들은 Zod와 Zod Mini에서 동일합니다:
```
    import * as z from "zod/mini";

    z.string().parse("asdf");
    z.string().safeParse("asdf");
    await z.string().parseAsync("asdf");
    await z.string().safeParseAsync("asdf");
```

또한 정제를 추가하는 데 사용하는 일반용 `.check()` 메서드도 있습니다.

Zod MiniZod
```
    import * as z from "zod/mini";

    z.array(z.number()).check(
      z.minLength(5),
      z.maxLength(10),
      z.refine(arr => arr.includes(5))
    );
```

다음의 최상위 정제 함수들이 Zod Mini에 제공되며, 어떤 Zod 메서드에 대응하는지는 쉽게 알 수 있습니다.
```
    import * as z from "zod/mini";

    // 사용자 정의 검사
    z.refine();

    // 일급 검사
    z.lt(value);
    z.lte(value); // 별칭: z.maximum()
    z.gt(value);
    z.gte(value); // 별칭: z.minimum()
    z.positive();
    z.negative();
    z.nonpositive();
    z.nonnegative();
    z.multipleOf(value);
    z.maxSize(value);
    z.minSize(value);
    z.size(value);
    z.maxLength(value);
    z.minLength(value);
    z.length(value);
    z.regex(regex);
    z.lowercase();
    z.uppercase();
    z.includes(value);
    z.startsWith(value);
    z.endsWith(value);
    z.property(key, schema); // 객체 스키마용; `input[key]`을 `schema`로 검사
    z.mime(value); // 파일 스키마용 (아래 참고)

    // 덮어쓰기 (이것들은 추론된 타입을 변경하지 않습니다!)
    z.overwrite(value => newValue);
    z.normalize();
    z.trim();
    z.toLowerCase();
    z.toUpperCase();
```

이처럼 함수형 API로 바뀌면 사용하지 않는 API를 번들러가 훨씬 쉽게 트리쉐이킹할 수 있습니다. 일반적인 사용 사례에는 여전히 정규 Zod가 추천되지만, 번들 크기를 매우 엄격하게 제한하는 프로젝트라면 Zod Mini를 고려할 만합니다.

- [코어 번들 크기 6.6배 감소](https://zod.dev/v4?id=66x-reduction-in-core-bundle-size)

아래는 앞서 보인 스크립트를 `"zod"` 대신 `"zod/mini"`를 사용하도록 수정한 것입니다.
```
    import * as z from "zod/mini";

    const schema = z.boolean();
    schema.parse(false);
```

이걸 `rollup`으로 빌드하면 gzip 된 번들 크기가 `1.88kb`입니다. `zod@3`과 비교하면 코어 번들 크기가 85%(6.6배) 줄어든 셈입니다.

Package| Bundle (gzip)
---|---
Zod 3| `12.47kb`
Zod 4 (regular)| `5.36kb`
Zod 4 (mini)| `1.88kb`

자세한 내용은 전용 [`zod/mini`](https://zod.dev/packages/mini) 문서 페이지를 참고하세요. 전체 API 세부사항은 기존 문서 페이지에 섞여 있으며, API가 달라지는 코드 블록에는 `"Zod"`와 `"Zod Mini"` 탭이 따로 있습니다.

## [메타데이터](https://zod.dev/v4?id=metadata)

Zod 4는 스키마에 강하게 타입화된 메타데이터를 추가하는 새로운 시스템을 도입합니다. 메타데이터는 스키마 자체에 저장되지 않고, 스키마와 일부 타입화된 메타데이터를 연결하는 “스키마 레지스트리”에 저장됩니다. `z.registry()`로 레지스트리를 생성하려면:
```
    import * as z from "zod";

    const myRegistry = z.registry<{ title: string; description: string }>();
```

레지스트리에 스키마를 추가하려면:
```
    const emailSchema = z.string().email();

    myRegistry.add(emailSchema, { title: "Email address", description: "..." });
    myRegistry.get(emailSchema);
    // => { title: "Email address", ... }
```

또는 편의를 위해 스키마의 `.register()` 메서드를 사용할 수도 있습니다:
```
    emailSchema.register(myRegistry, { title: "Email address", description: "..." })
    // => emailSchema 반환
```

- [전역 레지스트리](https://zod.dev/v4?id=the-global-registry)

Zod는 `z.globalRegistry`라는 전역 레지스트리도 내보내며, 여기에는 공통적인 JSON Schema 호환 메타데이터를 추가할 수 있습니다:
```
    z.globalRegistry.add(z.string(), {
      id: "email_address",
      title: "Email address",
      description: "Provide your email",
      examples: ["[[email protected]](https://zod.dev/cdn-cgi/l/email-protection)"],
      extraKey: "Additional properties are also allowed"
    });
```

- [`.meta()`](https://zod.dev/v4?id=meta)

`z.globalRegistry`에 스키마를 편리하게 추가하려면 `.meta()` 메서드를 사용하세요.
```
    z.string().meta({
      id: "email_address",
      title: "Email address",
      description: "Provide your email",
      examples: ["[[email protected]](https://zod.dev/cdn-cgi/l/email-protection)"],
      // ...
    });
```

Zod 3과의 호환성을 위해 `.describe()`도 여전히 있지만, `.meta()`가 더 선호됩니다.
```
    z.string().describe("An email address");

    // 다음과 동등
    z.string().meta({ description: "An email address" });
```

## [JSON Schema 변환](https://zod.dev/v4?id=json-schema-conversion)

Zod 4는 `z.toJSONSchema()`를 통해 공식 JSON Schema 변환을 도입합니다.
```
    import * as z from "zod";

    const mySchema = z.object({name: z.string(), points: z.number()});

    z.toJSONSchema(mySchema);
    // => {
    //   type: "object",
    //   properties: {
    //     name: {type: "string"},
    //     points: {type: "number"},
    //   },
    //   required: ["name", "points"],
    // }
```

`z.globalRegistry`에 있는 메타데이터는 JSON Schema 출력에 자동으로 포함됩니다.
```
    const mySchema = z.object({
      firstName: z.string().describe("Your first name"),
      lastName: z.string().meta({ title: "last_name" }),
      age: z.number().meta({ examples: [12, 99] }),
    });

    z.toJSONSchema(mySchema);
    // => {
    //   type: 'object',
    //   properties: {
    //     firstName: { type: 'string', description: 'Your first name' },
    //     lastName: { type: 'string', title: 'last_name' },
    //     age: { type: 'number', examples: [ 12, 99 ] }
    //   },
    //   required: [ 'firstName', 'lastName', 'age' ]
    // }
```

생성된 JSON Schema를 사용자화하는 방법은 [JSON Schema 문서](https://zod.dev/json-schema)를 참고하세요.

## [재귀 객체](https://zod.dev/v4?id=recursive-objects)

이건 예상 밖의 기능이었습니다. 이 문제를 풀기 위해 수년간 노력한 끝에, Zod에서 재귀 객체 타입을 제대로 추론하는 방법을 [찾았습니다](https://x.com/colinhacks/status/1919286275133378670). 재귀 타입을 정의하려면:
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

서로 재귀적인 타입(mutually recursive types)도 다음과 같이 표현할 수 있습니다:
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

Zod 3의 재귀 타입 패턴과 달리 타입 캐스팅이 필요 없습니다. 결과 스키마는 일반적인 `ZodObject` 인스턴스이며 모든 메서드를 사용할 수 있습니다.
```
    Post.pick({ title: true })
    Post.partial();
    Post.extend({ publishDate: z.date() });
```

## [파일 스키마](https://zod.dev/v4?id=file-schemas)

`File` 인스턴스를 검증하려면:
```
    const fileSchema = z.file();

    fileSchema.min(10_000); // 최소 .size (바이트)
    fileSchema.max(1_000_000); // 최대 .size (바이트)
    fileSchema.mime(["image/png"]); // MIME 타입
```

## [국제화](https://zod.dev/v4?id=internationalization)

Zod 4는 오류 메시지를 다양한 언어로 전역 번역할 수 있는 새로운 `locales` API를 도입했습니다.
```
    import * as z from "zod";

    // 영어 로케일 설정 (기본값)
    z.config(z.locales.en());
```

지원되는 전체 로케일 목록은 [Customizing errors](https://zod.dev/error-customization#locales)에서 확인하세요. 새로운 언어가 추가될 때마다 이 섹션이 업데이트됩니다.

## [오류 예쁘게 출력하기](https://zod.dev/v4?id=error-pretty-printing)

[`zod-validation-error`](https://www.npmjs.com/package/zod-validation-error) 패키지의 인기는 오류를 보기 좋게 출력하는 공식 API에 대한 수요가 상당함을 보여줍니다. 현재 해당 패키지를 사용 중이라면 계속 사용하셔도 됩니다.

Zod는 이제 `ZodError`를 사용자에게 친숙한 포맷된 문자열로 변환하는 최상위 함수 `z.prettifyError`를 제공합니다.
```
    const myError = new z.ZodError([
      {
        code: 'unrecognized_keys',
        keys: [ 'extraField' ],
        path: [],
        message: 'Unrecognized key: "extraField"'
      },
      {
        expected: 'string',
        code: 'invalid_type',
        path: [ 'username' ],
        message: 'Invalid input: expected string, received number'
      },
      {
        origin: 'number',
        code: 'too_small',
        minimum: 0,
        inclusive: true,
        path: [ 'favoriteNumbers', 1 ],
        message: 'Too small: expected number to be >=0'
      }
    ]);

    z.prettifyError(myError);
```

다음과 같은 예쁘게 출력 가능한 다중 줄 문자열을 반환합니다:
```
    ✖ Unrecognized key: "extraField"
    ✖ Invalid input: expected string, received number
      → at username
    ✖ Invalid input: expected number, received string
      → at favoriteNumbers[1]
```

현재 포맷은 구성할 수 없으며, 향후 바뀔 수 있습니다.

## [최상위 문자열 포맷](https://zod.dev/v4?id=top-level-string-formats)

모든 “문자열 포맷”(이메일 등)이 `z` 모듈의 최상위 함수로 승격되었습니다. 더 간결하고 tree-shake에 유리합니다. 메서드 버전(`z.string().email()` 등)은 여전히 사용 가능하지만 더 이상 권장되지 않으며 다음 메이저 버전에서 제거될 예정입니다.
```
    z.email();
    z.uuidv4();
    z.uuidv7();
    z.uuidv8();
    z.ipv4();
    z.ipv6();
    z.cidrv4();
    z.cidrv6();
    z.url();
    z.e164();
    z.base64();
    z.base64url();
    z.jwt();
    z.lowercase();
    z.iso.date();
    z.iso.datetime();
    z.iso.duration();
    z.iso.time();
```

- [사용자 정의 이메일 정규식](https://zod.dev/v4?id=custom-email-regex)

`z.email()` API는 이제 사용자 정의 정규식을 지원합니다. 이메일 정규식에는 표준이 없으므로 애플리케이션마다 더 엄격하거나 느슨하게 선택할 수 있습니다. 편의를 위해 Zod는 몇 가지 일반적인 정규식을 내보냅니다.
```
    // Zod의 기본 이메일 정규식 (Gmail 규칙)
    // colinhacks.com/essays/reasonable-email-regex 참고
    z.email(); // z.regexes.email

    // 브라우저가 input[type=email] 필드 유효성 검사용으로 사용하는 정규식
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email
    z.email({ pattern: z.regexes.html5Email });

    // classic emailregex.com 정규식 (RFC 5322)
    z.email({ pattern: z.regexes.rfc5322Email });

    // 유니코드를 허용하는 느슨한 정규식 (국제 이메일에 적합)
    z.email({ pattern: z.regexes.unicodeEmail });
```

## [템플릿 리터럴 타입](https://zod.dev/v4?id=template-literal-types)

Zod 4는 `z.templateLiteral()`을 구현합니다. 템플릿 리터럴 타입은 이전에는 표현할 수 없던 TypeScript 타입 시스템의 가장 큰 기능 중 하나입니다.
```
    const hello = z.templateLiteral(["hello, ", z.string()]);
    // `hello, ${string}`

    const cssUnits = z.enum(["px", "em", "rem", "%"]);
    const css = z.templateLiteral([z.number(), cssUnits]);
    // `${number}px` | `${number}em` | `${number}rem` | `${number}%`

    const email = z.templateLiteral([
      z.string().min(1),
      "@",
      z.string().max(64),
    ]);
    // `${string}@${string}` (min/max 정제도 적용됩니다!)
```

문자열화될 수 있는 모든 Zod 스키마 타입은 내부 정규식을 저장합니다: 문자열, `z.email()` 같은 문자열 포맷, 숫자, 불리언, bigint, 열거형, 리터럴, undefined/optional, null/nullable, 그리고 다른 템플릿 리터럴 등. `z.templateLiteral` 생성자는 이들을 슈퍼 정규식으로 이어붙이므로 문자열 포맷(`z.email()`) 같은 것들도 제대로 적용됩니다 (사용자 정의 정제는 적용되지 않습니다!).

자세한 내용은 [템플릿 리터럴 문서](https://zod.dev/api#template-literals)를 참고하세요.

## [숫자 포맷](https://zod.dev/v4?id=number-formats)

고정 너비 정수 및 부동소수점 타입을 표현하는 새로운 숫자 “포맷”이 추가되었습니다. 이는 이미 올바른 포함 최소/최대 제약이 적용된 `ZodNumber` 인스턴스를 반환합니다.
```
    z.int();      // [Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER]
    z.float32();  // [-3.4028234663852886e38, 3.4028234663852886e38]
    z.float64();  // [-1.7976931348623157e308, 1.7976931348623157e308]
    z.int32();    // [-2147483648, 2147483647]
    z.uint32();   // [0, 4294967295]
```

유사하게 다음 `bigint` 숫자 포맷도 추가되었습니다. 이 정수 타입들은 JavaScript의 `number`로 안전하게 표현할 수 있는 범위를 초과하므로, 이미 올바른 포함 최소/최대 제약이 적용된 `ZodBigInt` 인스턴스를 반환합니다.
```
    z.int64();    // [-9223372036854775808n, 9223372036854775807n]
    z.uint64();   // [0n, 18446744073709551615n]
```

## [Stringbool](https://zod.dev/v4?id=stringbool)

기존 `z.coerce.boolean()` API는 매우 단순합니다: falsy 값(`false`, `undefined`, `null`, `0`, `""`, `NaN` 등)은 `false`가 되고, truthy 값은 `true`가 됩니다.

이 API는 여전히 훌륭하며 다른 `z.coerce` API와도 일치합니다. 하지만 일부 사용자는 더 정교한 “env 스타일” 불리언 강제 변환을 요청했습니다. 이를 지원하기 위해 Zod 4는 `z.stringbool()`을 도입합니다.
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

진실 값과 거짓 값은 다음과 같이 커스터마이즈할 수 있습니다:
```
    z.stringbool({
      truthy: ["yes", "true"],
      falsy: ["no", "false"]
    })
```

자세한 내용은 [`z.stringbool()` 문서](https://zod.dev/api#stringbool)를 참고하세요.

## [단순화된 오류 커스터마이징](https://zod.dev/v4?id=simplified-error-customization)

Zod 4의 주요 붕괴 변경 사항 대부분은 _오류 커스터마이징_ API에 관련됩니다. Zod 3에서는 이 API들이 다소 엉켜 있었지만, Zod 4는 훨씬 더 우아하게 다듬어서 여기서 강조할 가치가 있다고 생각합니다.

간단히 말해, 이제 오류를 커스터마이즈하기 위한 단일 통합 `error` 매개변수가 생겼으며, 아래 API들을 대체합니다:

`message` 대신 `error`를 사용합니다. (`message` 매개변수는 여전히 지원되지만 더 이상 권장되지 않습니다.)
```
    - z.string().min(5, { message: "Too short." });
    + z.string().min(5, { error: "Too short." });
```

`invalid_type_error`와 `required_error`를 `error`(함수 구문)로 교체합니다:
```
    // Zod 3
    - z.string({
    -   required_error: "This field is required"
    -   invalid_type_error: "Not a string",
    - });

    // Zod 4
    + z.string({ error: (issue) => issue.input === undefined ?
    +  "This field is required" :
    +  "Not a string"
    + });
```

`errorMap`을 `error`(함수 구문)로 교체합니다:
```
    // Zod 3
    - z.string({
    -   errorMap: (issue, ctx) => {
    -     if (issue.code === "too_small") {
    -       return { message: `Value must be >${issue.minimum}` };
    -     }
    -     return { message: ctx.defaultError };
    -   },
    - });

    // Zod 4
    + z.string({
    +   error: (issue) => {
    +     if (issue.code === "too_small") {
    +       return `Value must be >${issue.minimum}`
    +     }
    +   },
    + });
```

## [업그레이드된 `z.discriminatedUnion()`](https://zod.dev/v4?id=upgraded-zdiscriminatedunion)

판별된 유니온은 이제 이전에 지원하지 않았던 여러 스키마 유형(유니온, 파이프 포함)을 지원합니다:
```
    const MyResult = z.discriminatedUnion("status", [
      // simple literal
      z.object({ status: z.literal("aaa"), data: z.string() }),
      // union discriminator
      z.object({ status: z.union([z.literal("bbb"), z.literal("ccc")]) }),
      // pipe discriminator
      z.object({ status: z.literal("fail").transform(val => val.toUpperCase()) }),
    ]);
```

아마도 가장 중요한 점은 판별된 유니온이 이제 서로 _compose_ 될 수 있다는 것입니다 — 하나의 판별된 유니온을 다른 판별된 유니온의 멤버로 사용할 수 있습니다.
```
    const BaseError = z.object({ status: z.literal("failed"), message: z.string() });

    const MyResult = z.discriminatedUnion("status", [
      z.object({ status: z.literal("success"), data: z.string() }),
      z.discriminatedUnion("code", [
        BaseError.extend({ code: z.literal(400) }),
        BaseError.extend({ code: z.literal(401) }),
        BaseError.extend({ code: z.literal(500) })
      ])
    ]);
```

## [ `z.literal()`의 다중 값](https://zod.dev/v4?id=multiple-values-in-zliteral)

`z.literal()` API는 이제 선택적으로 여러 값을 지원합니다.
```
    const httpCodes = z.literal([ 200, 201, 202, 204, 206, 207, 208, 226 ]);

    // previously in Zod 3:
    const httpCodes = z.union([
      z.literal(200),
      z.literal(201),
      z.literal(202),
      z.literal(204),
      z.literal(206),
      z.literal(207),
      z.literal(208),
      z.literal(226)
    ]);
```

## [스키마 내부에 위치한 정제](https://zod.dev/v4?id=refinements-live-inside-schemas)

Zod 3에서는 정제가 원본 스키마를 감싼 `ZodEffects` 클래스에 저장되어 있었습니다. 이로 인해 `.refine()`을 `.min()` 같은 다른 스키마 메서드 사이에 끼워 넣을 수 없어서 불편했습니다.
```
    z.string()
      .refine(val => val.includes("@"))
      .min(5);
    // ^ ❌ Property 'min' does not exist on type ZodEffects<ZodString, string, string>
```

Zod 4에서는 정제가 스키마 자체 안에 저장되므로 위 코드가 기대대로 작동합니다.
```
    z.string()
      .refine(val => val.includes("@"))
      .min(5); // ✅
```

- [`.overwrite()`](https://zod.dev/v4?id=overwrite)

`.transform()` 메서드는 매우 유용하지만 한 가지 큰 단점이 있습니다: 출력 타입을 런타임에 _살펴볼 수 없음_니다. 변환 함수는 어떤 값도 반환할 수 있는 블랙박스이기 때문에(다른 이유도 있지만) 스키마를 JSON Schema로 변환할 수 있는 건전한 방법이 없습니다.
```
    const Squared = z.number().transform(val => val ** 2);
    // => ZodPipe<ZodNumber, ZodTransform>
```

Zod 4는 _추론 타입을 변경하지 않는_ 변환을 표현하기 위한 새로운 `.overwrite()` 메서드를 도입합니다. `.transform()`과 달리 이 메서드는 원래 클래스의 인스턴스를 반환합니다. overwrite 함수는 정제로 저장되므로 추론된 타입을 변경하지도(변경할 수도) 않습니다.
```
    z.number().overwrite(val => val ** 2).max(100);
    // => ZodNumber
```

기존의 `.trim()`, `.toLowerCase()` 및 `.toUpperCase()` 메서드는 `.overwrite()`를 사용해 다시 구현되었습니다.

## [확장 가능한 기반: `zod/v4/core`](https://zod.dev/v4?id=an-extensible-foundation-zodv4core)

이 항목은 대부분의 Zod 사용자에게 직접적인 관련은 없겠지만, 강조할 가치가 있습니다. Zod Mini의 추가로 인해 Zod와 Zod Mini 사이에 공유되는 핵심 기능을 담은 `zod/v4/core`라는 하위 패키지를 만들어야 했습니다.

처음에는 이에 반대했지만, 이제 이것이 Zod 4의 가장 중요한 기능 중 하나라고 생각합니다. 이 기반 덕분에 Zod는 단순한 라이브러리에서 다른 라이브러리에 뿌려 넣을 수 있는 빠른 검증 "기판"으로 도약할 수 있게 되었습니다.

스키마 라이브러리를 구축 중이라면 `zod/v4/core`가 제공하는 기반 위에 어떻게 구성해야 하는지 확인하기 위해 Zod와 Zod Mini의 구현을 참고하세요. 도움이나 피드백이 필요하면 GitHub 토론 또는 [X](https://x.com/colinhacks)/[Bluesky](https://bsky.app/profile/colinhacks.com)를 통해 주저 말고 문의하세요.

## [마무리](https://zod.dev/v4?id=wrapping-up)

Zod Mini 같은 주요 기능의 설계 과정을 설명하는 추가 게시물을 시리즈로 작성할 계획입니다. 해당 글이 게시되는 대로 이 섹션을 업데이트하겠습니다.

라이브러리 작성자를 위해 이제 Zod 위에 구축할 때의 모범 사례를 설명하는 전용 [For library authors](https://zod.dev/library-authors) 가이드가 있습니다. 이 가이드는 Zod 3과 Zod 4(Mini 포함)를 동시에 지원하는 방법에 대한 일반적인 질문에 답합니다.
```
    pnpm upgrade zod@latest
```

즐거운 파싱 되세요!
— Colin McDonnell [@colinhacks](https://x.com/colinhacks)

[Migration guideComplete changelog and migration guide for upgrading from Zod 3 to Zod 4](https://zod.dev/v4/changelog)

