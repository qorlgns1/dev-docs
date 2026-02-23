---
title: 'index'
description: '이 접근 방식은 입력이 실제로 어떤 서브클래스인지(이 경우 )에 대한 타입 정보를 잃습니다. 즉  결과에서  같은 문자열 전용 메서드를 사용할 수 없습니다. 대신 제네릭 매개변수는 핵심 Zod 스키마 인터페이스를 확장해야 합니다:'
---

- **번역**  
  - 전체 마크다운 구조와 링크는 그대로 두고, 텍스트를 자연스럽고 기술적으로 정확한 한국어로 번역했습니다.  
  - 코드 블록, URLs, CLI 플래그, 파일 경로, API 엔드포인트, 모델 ID 등은 원문 그대로 유지했습니다.

이 접근 방식은 입력이 실제로 어떤 **서브클래스**인지(이 경우 `ZodString`)에 대한 타입 정보를 잃습니다. 즉 `inferSchema` 결과에서 `.min()` 같은 문자열 전용 메서드를 사용할 수 없습니다. 대신 제네릭 매개변수는 핵심 Zod 스키마 인터페이스를 확장해야 합니다:

```
    function inferSchema<T extends z4.$ZodType>(schema: T) {
      return schema;
    }

    inferSchema(z.string());
    // => ZodString ✅
```

입력 스키마를 특정 서브클래스로 제한하려면:

```

    import * as z4 from "zod/v4/core";

    // 오직 객체 스키마만 허용
    function inferSchema<T extends z4.$ZodObject>(schema: T) {
      return schema;
    }
```

입력 스키마의 추론된 출력 타입을 제한하려면:

```

    import * as z4 from "zod/v4/core";

    // 오직 문자열 스키마만 허용
    function inferSchema<T extends z4.$ZodType<string>>(schema: T) {
      return schema;
    }

    inferSchema(z.string()); // ✅

    inferSchema(z.number());
    // ❌ '_zod.output'의 타입이 두 타입 간에 호환되지 않습니다.
    // // Type 'number' is not assignable to type 'string'
```

스키마로 데이터를 파싱하려면 최상위 `z4.parse`/`z4.safeParse`/`z4.parseAsync`/`z4.safeParseAsync` 함수를 사용하세요. `z4.$ZodType` 서브클래스에는 메서드가 없습니다. 일반 파싱 메서드는 Zod와 Zod Mini가 구현하지만 Zod Core에서는 사용할 수 없습니다.

```
    function parseData<T extends z4.$ZodType>(data: unknown, schema: T): z4.output<T> {
      return z.parse(schema, data);
    }

    parseData("sup", z.string());
    // => string
```

