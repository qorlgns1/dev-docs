---
title: '기본 사용법'
description: '이 페이지에서는 스키마 생성, 데이터 파싱, 추론된 타입 사용법의 기본을 안내합니다. Zod의 스키마 API에 대한 전체 문서는 Defining schemas를 참고하세요.'
---

# 기본 사용법

마크다운 복사

[이 페이지 수정](https://github.com/colinhacks/zod/edit/main/packages/docs/content/basics.mdx)

이 페이지에서는 스키마 생성, 데이터 파싱, 추론된 타입 사용법의 기본을 안내합니다. Zod의 스키마 API에 대한 전체 문서는 [Defining schemas](https://zod.dev/api)를 참고하세요.

## [스키마 정의하기](https://zod.dev/basics?id=defining-a-schema)

다음 작업을 하기 전에 먼저 스키마를 정의해야 합니다. 이 가이드에서는 간단한 객체 스키마를 사용합니다.

ZodZod Mini
```
    import * as z from "zod";

    const Player = z.object({
      username: z.string(),
      xp: z.number()
    });
```

## [데이터 파싱](https://zod.dev/basics?id=parsing-data)

어떤 Zod 스키마든 `.parse`를 사용해 입력을 검증할 수 있습니다. 유효하면 Zod는 입력의 강타입 _깊은 복사본_을 반환합니다.
```
    Player.parse({ username: "billie", xp: 100 });
    // => returns { username: "billie", xp: 100 }
```

**참고** — 스키마에서 `async` [refinements](https://zod.dev/api#refinements)나 [transforms](https://zod.dev/api#transforms) 같은 비동기 API를 사용하는 경우 `.parseAsync()` 메서드를 사용해야 합니다.
```
    await Player.parseAsync({ username: "billie", xp: 100 });
```

## [오류 처리](https://zod.dev/basics?id=handling-errors)

검증이 실패하면 `.parse()` 메서드는 상세한 검증 정보가 담긴 `ZodError` 인스턴스를 던집니다.

ZodZod Mini
```
    try {
      Player.parse({ username: 42, xp: "100" });
    } catch(error){
      if(error instanceof z.ZodError){
        error.issues;
        /* [
          {
            expected: 'string',
            code: 'invalid_type',
            path: [ 'username' ],
            message: 'Invalid input: expected string'
          },
          {
            expected: 'number',
            code: 'invalid_type',
            path: [ 'xp' ],
            message: 'Invalid input: expected number'
          }
        ] */
      }
    }
```

`try/catch` 블록을 피하고 싶다면 `.safeParse()` 메서드를 사용하면 성공적으로 파싱된 데이터 또는 `ZodError`가 포함된 평범한 결과 객체를 얻습니다. 결과 타입은 [판별 유니온](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)이므로 두 경우를 편리하게 처리할 수 있습니다.
```
    const result = Player.safeParse({ username: 42, xp: "100" });
    if (!result.success) {
      result.error;   // ZodError instance
    } else {
      result.data;    // { username: string; xp: number }
    }
```

**참고** — 스키마가 `async` [refinements](https://zod.dev/api#refinements)나 [transforms](https://zod.dev/api#transforms) 같은 비동기 API를 사용하는 경우 `.safeParseAsync()` 메서드를 사용해야 합니다.
```
    await schema.safeParseAsync("hello");
```

## [타입 추론](https://zod.dev/basics?id=inferring-types)

Zod는 스키마 정의에서 정적 타입을 추론합니다. `z.infer<>` 유틸리티로 이 타입을 추출하여 자유롭게 사용할 수 있습니다.
```
    const Player = z.object({
      username: z.string(),
      xp: z.number()
    });

    // 추론된 타입 추출
    type Player = z.infer<typeof Player>;

    // 코드에서 사용
    const player: Player = { username: "billie", xp: 100 };
```

경우에 따라 스키마의 입력 타입과 출력 타입이 달라질 수 있습니다. 예를 들어 `.transform()` API는 입력을 한 타입에서 다른 타입으로 변환할 수 있습니다. 이런 경우에는 입력과 출력 타입을 각각 추출할 수 있습니다.
```
    const mySchema = z.string().transform((val) => val.length);

    type MySchemaIn = z.input<typeof mySchema>;
    // => string

    type MySchemaOut = z.output<typeof mySchema>; // z.infer<typeof mySchema>와 동일
    // number
```

* * *

기본을 다뤘으니 이제 Schema API로 넘어가 보겠습니다.

