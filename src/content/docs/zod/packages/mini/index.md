---
title: '[기본 로케일 없음](https://zod.dev/packages/mini?id=no-default-locale)'
description: 'Zod Mini 문서는 일반 Zod 문서와 탭 코드 블록을 통해 섞여 있습니다. 이 페이지는 Zod Mini가 왜 존재하며, 언제 사용해야 하고, 일반 Zod와 어떤 주요 차이가 있는지 설명합니다.'
---

**Zod Mini 개요**

Zod Mini 문서는 일반 Zod 문서와 탭 코드 블록을 통해 섞여 있습니다. 이 페이지는 Zod Mini가 왜 존재하며, 언제 사용해야 하고, 일반 Zod와 어떤 주요 차이가 있는지 설명합니다.

Zod Mini는 Zod 4 릴리스와 함께 도입되었습니다. 사용하려면:
```
    npm install zod@^4.0.0
```

가져오기:
```
    import * as z from "zod/mini";
```

Zod Mini는 `zod`와 정확히 동일한 기능을 제공하지만 _함수형_이고 _tree-shakable_한 API를 사용합니다. `zod`에서 온 경우 일반적으로 메서드 대신 _함수_를 사용하게 됩니다.
```
    // regular Zod
    const mySchema = z.string().optional().nullable();

    // Zod Mini
    const mySchema = z.nullable(z.optional(z.string()));
```

**Tree-shaking**

Tree-shaking은 최신 번들러가 최종 번들에서 사용하지 않는 코드를 제거하는 기술로, _죽은 코드 제거(dead-code elimination)_라고도 합니다.

일반 Zod에서는 스키마에서 `.min()` 같은 간편한 메서드를 제공합니다. 번들러는 일반적으로 사용하지 않는 메서드 구현을 제거할 수 없지만, 사용하지 않는 최상위 함수는 제거할 수 있습니다. 따라서 Zod Mini API는 메서드보다 함수 사용이 더 많습니다.
```
    // regular Zod
    z.string().min(5).max(10).trim()

    // Zod Mini
    z.string().check(z.minLength(5), z.maxLength(10), z.trim());
```

번들 크기 감소 예시:
```
    z.boolean().parse(true)
```

Zod와 Zod Mini로 번들링하면 다음과 같은 크기가 됩니다. Zod Mini는 64% 감소합니다.

Package| Bundle size (gzip)
---|---
Zod Mini| `2.12kb`
Zod| `5.91kb`

보다 복잡한 객체 스키마:
```
    const schema = z.object({ a: z.string(), b: z.number(), c: z.boolean() });

    schema.parse({
      a: "asdf",
      b: 123,
      c: true,
    });
```

Package| Bundle size (gzip)
---|---
Zod Mini| `4.0kb`
Zod| `13.1kb`

이 숫자를 보면 bundle 크기에 대해 감을 잡을 수 있습니다. Zod Mini 사용 여부는 직접 벤치마크해 확실히 판단하세요.

**언제 Zod Mini를 쓰지 말아야 하나**

일반적으로 번들 크기에 대해 매우 엄격한 제약이 없다면 일반 Zod를 사용하는 편이 낫습니다. 많은 개발자가 번들 크기의 중요성을 지나치게 평가합니다. 실전에서는 Zod 규모(`5-10kb` 정도)의 번들 크기는 오히려 농촌 또는 개발 도상 지역의 느린 모바일 네트워크 사용자처럼 특별히 정교하게 최적화해야 하는 경우에만 의미가 있습니다.

몇 가지 고려사항:

- **DX**

Zod Mini API는 더 장황하고 발견하기 어렵습니다. Zod의 메서드는 Intellisense를 통한 발견 및 자동 완성이 훨씬 쉽고, 체이닝 API로 빠르게 스키마를 만들 수 있습니다. (Zod 제작자로서: Zod Mini API를 최대한 편리하게 만들려고 했지만 표준 Zod API를 더 선호합니다.)

- **백엔드 개발**

백엔드에서 Zod를 사용한다면 Zod 수준의 번들 크기는 의미가 없습니다. Lambda 같은 리소스 제약 환경에서도 마찬가지입니다. [이 글](https://medium.com/@adtanasa/size-is-almost-all-that-matters-for-optimizing-aws-lambda-cold-starts-cad54f65cbb)은 다양한 크기의 번들로 콜드 스타트 시간을 벤치마크합니다. 일부 결과는 다음과 같습니다:

Bundle size| Lambda cold start time
---|---
`1kb`| `171ms`
`17kb` (비-Mini Zod의 gzipped 크기)| `171.6ms` (보간)
`128kb`| `176ms`
`256kb`| `182ms`
`512kb`| `279ms`
`1mb`| `557ms`

`1kb` 번들의 최소 콜드 스타트는 `171ms`이며, 다음 테스트 번들 `128kb`는 단지 `5ms` 증가합니다. 일반 Zod 전체를 gzip하면 약 `17kb`이며 시작 시간은 `0.6ms` 정도 증가합니다.

- **인터넷 속도**

서버 왕복 시간(`100-200ms`)이 추가 `10kb` 다운로드 시간보다 훨씬 큽니다. 느린 3G 연결(1Mbps 이하)에서는 추가 `10kb`가 더 중요한 차이를 만들지만, 농촌이나 개발 도상 지역 사용자를 특별히 최적화하지 않는 한 다른 개선에 시간을 쓰는 것이 나을 수 있습니다.

**`ZodMiniType`**

모든 Zod Mini 스키마는 `z.ZodMiniType`을 확장하며, 이는 [`zod/v4/core`](https://zod.dev/packages/core)의 `z.core.$ZodType`를 확장합니다. 이 클래스는 `zod`의 `ZodType`보다 메서드가 적지만 여전히 유용한 메서드 몇 가지를 제공합니다.

- **`.parse`**

모든 Zod Mini 스키마는 `zod`와 동일한 파싱 메서드를 구현합니다.
```
    import * as z from "zod/mini"

    const mySchema = z.string();

    mySchema.parse('asdf')
    await mySchema.parseAsync('asdf')
    mySchema.safeParse('asdf')
    await mySchema.safeParseAsync('asdf')
```

- **`.check()`**

일반 Zod에서는 각 스키마 하위 클래스에 일반 검증 메서드가 있습니다.
```
    import * as z from "zod";

    z.string()
      .min(5)
      .max(10)
      .refine(val => val.includes("@"))
      .trim()
```

Zod Mini에서는 이러한 메서드가 없으며 대신 `.check()`에 전달합니다.
```
    import * as z from "zod/mini"

    z.string().check(
      z.minLength(5),
      z.maxLength(10),
      z.refine(val => val.includes("@")),
      z.trim()
    );
```

다음 검증이 구현되어 있으며, 특정 타입(예: 문자열/숫자)에만 적용되는 것도 있습니다. API는 타입 안전하며 TypeScript는 지원되지 않는 검증을 막습니다.
```
    z.lt(value);
    z.lte(value); // alias: z.maximum()
    z.gt(value);
    z.gte(value); // alias: z.minimum()
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
    z.property(key, schema);
    z.mime(value);

    // custom checks
    z.refine()
    z.check()   // replaces .superRefine()

    // mutations (these do not change the inferred types)
    z.overwrite(value => newValue);
    z.normalize();
    z.trim();
    z.toLowerCase();
    z.toUpperCase();

    // metadata (registers schema in z.globalRegistry)
    z.meta({ title: "...", description: "..." });
    z.describe("...");
```

- **`.register()`**

[레지스트리](https://zod.dev/metadata#registries)에 스키마 등록:
```
    const myReg = z.registry<{title: string}>();

    z.string().register(myReg, { title: "My cool string schema" });
```

- **`.brand()`**

스키마를 _브랜딩_합니다. 자세한 내용은 [Branded types](https://zod.dev/api#branded-types)를 참조하세요.
```
    import * as z from "zod/mini"

    const USD = z.string().brand("USD");
```

- **`.clone(def)`**

현재 스키마를 제공한 `def`로 동일하게 복제합니다.
```
    const mySchema = z.string()

    mySchema.clone(mySchema._zod.def);
```

## [기본 로케일 없음](https://zod.dev/packages/mini?id=no-default-locale)

일반 Zod는 자동으로 영어(`en`) 로케일을 로드하지만, Zod Mini는 그렇지 않습니다. 이는 오류 메시지가 필요 없거나 영어가 아닌 언어로 현지화되어 있거나 별도로 커스텀된 상황에서 번들 크기를 줄이는 데 도움이 됩니다.

따라서 기본적으로 모든 issue의 `message` 속성은 단순히 `"Invalid input"`로 표시됩니다. 영어 로케일을 로드하려면:
```
    import * as z from "zod/mini"

    z.config(z.locales.en());
```

로컬라이제이션에 관한 자세한 내용은 [Locales](https://zod.dev/error-customization#internationalization) 문서를 참고하세요.

