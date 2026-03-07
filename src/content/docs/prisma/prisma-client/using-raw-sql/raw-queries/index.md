---
title: "Raw queries"
description: "Prisma Client API의 raw() 메서드를 사용해 데이터베이스로 raw SQL 및 MongoDB 쿼리를 전송하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries

# Raw queries

Prisma Client API의 raw() 메서드를 사용해 데이터베이스로 raw SQL 및 MongoDB 쿼리를 전송하는 방법을 알아보세요.

아래에서 설명하는 raw query 대신, 타입 안전한 SQL 쿼리를 위해 [TypedSQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql)을 사용하는 것을 권장합니다.

Prisma Client는 데이터베이스로 raw query를 전송하는 기능을 지원합니다. 다음과 같은 경우 raw query를 사용하고 싶을 수 있습니다.

- 고도로 최적화된 쿼리를 실행하고 싶은 경우
- Prisma Client가 아직 지원하지 않는 기능이 필요한 경우([이슈 등록을 고려해 주세요](https://github.com/prisma/prisma/issues/new/choose))

Raw query는 Prisma ORM이 지원하는 모든 관계형 데이터베이스와 MongoDB에서 사용할 수 있습니다. 자세한 내용은 관련 섹션을 참고하세요.

- 관계형 데이터베이스에서의 Raw queries
- MongoDB에서의 Raw queries

## Raw queries with relational databases

관계형 데이터베이스의 경우 Prisma Client는 raw query를 전송할 수 있는 네 가지 메서드를 제공합니다. 다음을 사용할 수 있습니다.

- `$queryRaw`: 실제 레코드를 반환합니다(예: `SELECT` 사용 시).
- `$executeRaw`: 영향받은 행 수를 반환합니다(예: `UPDATE` 또는 `DELETE` 이후).
- `$queryRawUnsafe`: raw 문자열을 사용해 실제 레코드를 반환합니다(예: `SELECT` 사용 시).
- `$executeRawUnsafe`: raw 문자열을 사용해 영향받은 행 수를 반환합니다(예: `UPDATE` 또는 `DELETE` 이후).

이름에 "Unsafe"가 포함된 메서드는 훨씬 유연하지만, **코드가 SQL injection에 취약해질 중대한 위험**이 있습니다.

나머지 두 메서드는 단순한 템플릿 태그 사용, 문자열 빌드 없음, 문자열 연결 없음이라는 조건에서 안전하게 사용할 수 있습니다. **하지만** 더 복잡한 사용 사례에서는 주의가 필요하며, 특정 방식으로 사용하면 여전히 SQL injection이 발생할 수 있습니다. 자세한 내용은 아래의 [SQL injection prevention](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#sql-injection-prevention) 섹션을 참고하세요.

> **참고** : 위 목록의 모든 메서드는 한 번에 **하나의** 쿼리만 실행할 수 있습니다. 두 번째 쿼리를 이어 붙일 수 없으며, 예를 들어 `select 1; select 2;`로 호출해도 동작하지 않습니다.

- `$queryRaw`

`$queryRaw`는 실제 데이터베이스 레코드를 반환합니다. 예를 들어, 다음 `SELECT` 쿼리는 `User` 테이블의 각 레코드에 대해 모든 필드를 반환합니다.

```
    const result = await prisma.$queryRaw`SELECT * FROM User`;
```

이 메서드는 [tagged template](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)로 구현되어 있어, [variables](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#using-variables)를 쉽게 삽입할 수 있는 템플릿 리터럴을 전달할 수 있습니다. 그 결과 Prisma Client는 SQL injection으로부터 안전한 prepared statement를 생성합니다.

```
    const email = "emelie@prisma.io";
    const result = await prisma.$queryRaw`SELECT * FROM User WHERE email = ${email}`;
```

[`Prisma.sql`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#tagged-template-helpers) 헬퍼도 사용할 수 있으며, 실제로 `$queryRaw` 메서드는 템플릿 문자열 또는 `Prisma.sql` 헬퍼만 **허용**합니다.

```
    const email = "emelie@prisma.io";
    const result = await prisma.$queryRaw(Prisma.sql`SELECT * FROM User WHERE email = ${email}`);
```

신뢰할 수 없는 입력을 이 메서드에 전달하는 쿼리에 문자열 빌드 방식으로 포함하면 SQL injection 공격 가능성이 생깁니다. SQL injection 공격은 데이터 수정 또는 삭제로 이어질 수 있습니다. 권장되는 방식은 이 메서드를 실행하는 시점에 쿼리 텍스트를 포함하는 것입니다. 이 위험과 예방법 예시는 아래 [SQL injection prevention](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#sql-injection-prevention) 섹션을 참고하세요.

#

- Considerations

다음을 유의하세요.

- 템플릿 변수는 SQL 문자열 리터럴 내부에서 사용할 수 없습니다. 예를 들어, 다음 쿼리는 동작하지 **않습니다**.

```
const name = "Bob";
        await prisma.$queryRaw`SELECT 'My name is ${name}';`;
```

대신 전체 문자열을 변수로 전달하거나, 문자열 연결을 사용할 수 있습니다.

```
const name = "My name is Bob";
        await prisma.$queryRaw`SELECT ${name};`;
```

```
const name = "Bob";
        await prisma.$queryRaw`SELECT 'My name is ' || ${name};`;
```

- 템플릿 변수는 데이터 값(예: 위 예시의 `email`)에만 사용할 수 있습니다. 변수는 컬럼명, 테이블명, 데이터베이스명 같은 식별자나 SQL 키워드에 사용할 수 없습니다. 예를 들어, 다음 두 쿼리는 동작하지 **않습니다**.

```
const myTable = "user";
        await prisma.$queryRaw`SELECT * FROM ${myTable};`;
```

```
const ordering = "desc";
        await prisma.$queryRaw`SELECT * FROM Table ORDER BY ${ordering};`;
```

- Prisma는 `$queryRaw` 및 `$queryRawUnsafe`가 반환한 모든 데이터베이스 값을 대응되는 JavaScript 타입으로 매핑합니다. [자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#raw-query-type-mapping).

- `$queryRaw`는 PostgreSQL 데이터베이스에서 동적 테이블명을 지원하지 않습니다. [자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#dynamic-table-names-in-postgresql)

#

- Return type

`$queryRaw`는 배열을 반환합니다. 각 객체는 하나의 데이터베이스 레코드에 대응합니다.

```
    [
      { id: 1, email: "emelie@prisma.io", name: "Emelie" },
      { id: 2, email: "yin@prisma.io", name: "Yin" },
    ]
```

[`$queryRaw` 결과에 타입 지정](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#typing-queryraw-results)도 가능합니다.

#

- Signature

```
    $queryRaw<T = unknown>(query: TemplateStringsArray | Prisma.Sql, ...values: any[]): PrismaPromise<T>;
```

#

- Typing `$queryRaw` results

`PrismaPromise<T>`는 [generic type parameter `T`](https://www.typescriptlang.org/docs/handbook/generics.html)를 사용합니다. `$queryRaw` 메서드를 호출할 때 `T`의 타입을 결정할 수 있습니다. 다음 예시에서 `$queryRaw`는 `User[]`를 반환합니다.

```
    // import the generated `User` type from the `@prisma/client` module
    import { User } from "@prisma/client";

    const result = await prisma.$queryRaw<User[]>`SELECT * FROM User`;
    // result is of type: `User[]`
```

> **참고** : 타입을 제공하지 않으면 `$queryRaw`의 기본값은 `unknown`입니다.

모델의 **특정 필드**만 선택하거나 relation을 포함하려는 경우, 결과가 올바르게 타입 지정되도록 [Prisma Client가 생성한 타입 활용](https://docs.prisma.io/docs/orm/prisma-client/type-safety/operating-against-partial-structures-of-model-types#problem-using-variations-of-the-generated-model-type) 문서를 참고하세요.

#

- Type caveats when using raw SQL

`$queryRaw` 결과에 타입을 지정하더라도 raw 데이터가 제안된 TypeScript 타입과 항상 일치하지는 않을 수 있습니다. 예를 들어, 다음 Prisma 모델에는 `published`라는 `Boolean` 필드가 포함되어 있습니다.

```
    model Post {
      id        Int     @id @default(autoincrement())
      published Boolean @default(false)
      title     String
      content   String?
    }
```

다음 쿼리는 모든 게시물을 반환합니다. 이후 각 `Post`의 `published` 필드 값을 출력합니다.

```
    const result = await prisma.$queryRaw<Post[]>`SELECT * FROM Post`;

    result.forEach((x) => {
      console.log(x.published);
    });
```

일반적인 CRUD 쿼리의 경우 Prisma Client query engine은 모든 데이터베이스에서 반환 타입을 표준화합니다. 하지만 **raw query를 사용할 때는 그렇지 않습니다**. 데이터베이스 공급자가 MySQL이면 반환값은 `1` 또는 `0`입니다. 반면 데이터베이스 공급자가 PostgreSQL이면 값은 `true` 또는 `false`입니다.

> **참고** : Prisma는 JavaScript 정수를 PostgreSQL에 `INT8`로 전송합니다. 이는 입력으로 `INT4`만 받는 사용자 정의 함수와 충돌할 수 있습니다. PostgreSQL 데이터베이스와 함께 `$queryRaw`를 사용하는 경우 입력 타입을 `INT8`로 업데이트하거나, 쿼리 파라미터를 `INT4`로 캐스팅하세요.

#

- Dynamic table names in PostgreSQL

[테이블명은 보간할 수 없습니다](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#considerations). 즉, `$queryRaw`에서는 동적 테이블명을 사용할 수 없습니다. 대신 다음과 같이 [`$queryRawUnsafe`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#queryrawunsafe)를 사용해야 합니다.

```
    let userTable = "User";
    let result = await prisma.$queryRawUnsafe(`SELECT * FROM ${userTable}`);
```

`$queryRawUnsafe`를 사용자 입력과 함께 사용하면 SQL injection 공격 위험이 있다는 점에 유의하세요. [자세히 보기](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#queryrawunsafe).

- `$queryRawUnsafe()`

`$queryRawUnsafe()` 메서드는 데이터베이스에 raw 문자열(또는 템플릿 문자열)을 전달할 수 있게 해줍니다.

이 메서드를 사용자 입력과 함께 사용하면(즉, `SELECT * FROM table WHERE columnName = ${userInput}`) SQL injection 공격 가능성이 생깁니다. SQL injection 공격은 데이터 수정 또는 삭제로 이어질 수 있습니다.

가능한 경우 항상 `$queryRaw` 메서드를 대신 사용해야 합니다. 올바르게 사용하면 `$queryRaw` 메서드가 훨씬 더 안전하지만, 특정 상황에서는 `$queryRaw` 메서드 역시 취약해질 수 있다는 점에 유의하세요. 자세한 내용은 아래 [SQL injection prevention](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#sql-injection-prevention) 섹션을 참고하세요.

다음 쿼리는 `User` 테이블의 각 레코드에 대해 모든 필드를 반환합니다.

```
    // import the generated `User` type from the `@prisma/client` module
    import { User } from "@prisma/client";

    const result = await prisma.$queryRawUnsafe("SELECT * FROM User");
```

파라미터화된 쿼리도 실행할 수 있습니다. 다음 예시는 이메일에 `emelie@prisma.io` 문자열이 포함된 모든 사용자를 반환합니다.

```
    prisma.$queryRawUnsafe("SELECT * FROM users WHERE email = $1", "emelie@prisma.io");
```

> **참고** : Prisma는 JavaScript 정수를 PostgreSQL에 `INT8`로 전송합니다. 이는 입력으로 `INT4`만 받는 사용자 정의 함수와 충돌할 수 있습니다. PostgreSQL 데이터베이스와 함께 파라미터화된 `$queryRawUnsafe` 쿼리를 사용하는 경우 입력 타입을 `INT8`로 업데이트하거나, 쿼리 파라미터를 `INT4`로 캐스팅하세요.

파라미터화된 쿼리 사용에 대한 자세한 내용은 아래 [parameterized queries](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#parameterized-queries) 섹션을 참고하세요.

#

- Signature

```
    $queryRawUnsafe<T = unknown>(query: string, ...values: any[]): PrismaPromise<T>;
```

- `$executeRaw`

`$executeRaw`는 `UPDATE` 또는 `DELETE` 같은 _데이터베이스 작업의 영향받은 행 수_ 를 반환합니다. 이 함수는 데이터베이스 레코드를 반환하지 **않습니다**. 다음 쿼리는 데이터베이스의 레코드를 업데이트하고, 업데이트된 레코드 수를 반환합니다.

```
    const result: number =
      await prisma.$executeRaw`UPDATE User SET active = true WHERE emailValidated = true`;
```

이 메서드는 [tagged template](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)로 구현되어 있어, [variables](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#using-variables)를 쉽게 삽입할 수 있는 템플릿 리터럴을 전달할 수 있습니다. 그 결과 Prisma Client는 SQL injection으로부터 안전한 prepared statement를 생성합니다.

```
    const emailValidated = true;
    const active = true;

    const result: number =
      await prisma.$executeRaw`UPDATE User SET active = ${active} WHERE emailValidated = ${emailValidated};`;
```

신뢰할 수 없는 입력을 이 메서드에 전달하는 쿼리에 문자열 빌드 방식으로 포함하면 SQL injection 공격 가능성이 생깁니다. SQL injection 공격은 데이터 수정 또는 삭제로 이어질 수 있습니다. 권장되는 방식은 이 메서드를 실행하는 시점에 쿼리 텍스트를 포함하는 것입니다. 이 위험과 예방법 예시는 아래 [SQL injection prevention](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#sql-injection-prevention) 섹션을 참고하세요.

#

- Considerations

다음을 유의하세요.

- `$executeRaw`는 하나의 문자열에서 여러 쿼리를 지원하지 않습니다(예: `ALTER TABLE`과 `CREATE TABLE`을 함께 실행).

- Prisma Client는 prepared statement를 제출하며, prepared statement는 SQL 문의 일부만 허용합니다. 예를 들어 `START TRANSACTION`은 허용되지 않습니다. 자세한 내용은 [MySQL이 Prepared Statements에서 허용하는 구문](https://dev.mysql.com/doc/refman/8.0/en/sql-prepared-statements.html)을 참고하세요.
  - [`PREPARE`는 `ALTER`를 지원하지 않습니다](https://www.postgresql.org/docs/current/sql-prepare.html) \- [우회 방법](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#alter-limitation-postgresql)을 확인하세요.

  - 템플릿 변수는 SQL 문자열 리터럴 내부에서 사용할 수 없습니다. 예를 들어, 다음 쿼리는 작동하지 **않습니다**:

```
const name = "Bob";
        await prisma.$executeRaw`UPDATE user SET greeting = 'My name is ${name}';`;
```

대신 문자열 전체를 변수로 전달하거나 문자열 연결을 사용할 수 있습니다:

```
const name = "My name is Bob";
        await prisma.$executeRaw`UPDATE user SET greeting = ${name};`;
```

```
const name = "Bob";
        await prisma.$executeRaw`UPDATE user SET greeting = 'My name is ' || ${name};`;
```

- 템플릿 변수는 데이터 값(예: 위 예시의 `email`)에만 사용할 수 있습니다. 변수는 컬럼명, 테이블명, 데이터베이스명 같은 식별자나 SQL 키워드에는 사용할 수 없습니다. 예를 들어, 다음 두 쿼리는 작동하지 **않습니다**:

```
const myTable = "user";
        await prisma.$executeRaw`UPDATE ${myTable} SET active = true;`;
```

```
const ordering = "desc";
        await prisma.$executeRaw`UPDATE User SET active = true ORDER BY ${desc};`;
```

#

- Return type

`$executeRaw`는 `number`를 반환합니다.

#

- Signature

```
    $executeRaw<T = unknown>(query: TemplateStringsArray | Prisma.Sql, ...values: any[]): PrismaPromise<number>;
```

- `$executeRawUnsafe()`

`$executeRawUnsafe()` 메서드는 raw string(또는 template string)을 데이터베이스에 전달할 수 있게 해줍니다. `$executeRaw`와 마찬가지로 데이터베이스 레코드는 반환하지 않으며, 영향을 받은 행 수를 반환합니다.

이 메서드를 사용자 입력과 함께 사용하면(즉, `SELECT * FROM table WHERE columnName = ${userInput}`) SQL injection 공격 가능성이 열립니다. SQL injection 공격은 데이터를 수정하거나 삭제할 수 있게 만들 수 있습니다.

가능하면 `$executeRaw` 메서드를 대신 사용해야 합니다. `$executeRaw` 메서드는 올바르게 사용하면 훨씬 더 안전하지만, 특정 상황에서는 `$executeRaw` 메서드도 취약해질 수 있다는 점에 유의하세요. 자세한 내용은 아래 [SQL injection prevention](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#sql-injection-prevention) 섹션을 참고하세요.

다음 예시는 template string을 사용해 데이터베이스의 레코드를 업데이트합니다. 그런 다음 업데이트된 레코드 수를 반환합니다:

```
    const emailValidated = true;
    const active = true;

    const result = await prisma.$executeRawUnsafe(
      `UPDATE User SET active = ${active} WHERE emailValidated = ${emailValidated}`,
    );
```

동일한 내용은 parameterized query로도 작성할 수 있습니다:

```
    const result = prisma.$executeRawUnsafe(
      "UPDATE User SET active = $1 WHERE emailValidated = $2",
      "yin@prisma.io",
      true,
    );
```

parameterized query 사용에 대한 자세한 내용은 아래 [parameterized queries](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#parameterized-queries) 섹션을 참고하세요.

#

- Signature

```
    $executeRawUnsafe<T = unknown>(query: string, ...values: any[]): PrismaPromise<number>;
```

- Raw query type mapping

Prisma는 `$queryRaw` 및 `$queryRawUnsafe`가 반환하는 모든 데이터베이스 값을 해당하는 [JavaScript types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)로 매핑합니다. 이 동작은 `findMany()` 같은 일반 Prisma 쿼리 메서드와 동일합니다.

예를 들어, 테이블에서 `BigInt`, `Bytes`, `Decimal`, `Date` 타입 컬럼을 선택하는 raw query를 보겠습니다:

```
    const result = await prisma.$queryRaw`SELECT bigint, bytes, decimal, date FROM "Table";`;

    console.log(result);
```

```
    { bigint: BigInt("123"), bytes: <Buffer 01 02>), decimal: Decimal("12.34"), date: Date("<some_date>") }
```

`result` 객체에서 데이터베이스 값은 해당 JavaScript 타입으로 매핑됩니다.

다음 표는 데이터베이스에서 사용하는 타입과 raw query가 반환하는 JavaScript 타입 간 변환을 보여줍니다:

| Database type           | JavaScript type |
| ----------------------- | --------------- |
| Text                    | `String`        |
| 32-bit integer          | `Number`        |
| 32-bit unsigned integer | `BigInt`        |
| Floating point number   | `Number`        |
| Double precision number | `Number`        |
| 64-bit integer          | `BigInt`        |
| Decimal / numeric       | `Decimal`       |
| Bytes                   | `Uint8Array`    |
| Json                    | `Object`        |
| DateTime                | `Date`          |
| Date                    | `Date`          |
| Time                    | `Date`          |
| Uuid                    | `String`        |
| Xml                     | `String`        |

각 데이터베이스 타입의 정확한 이름은 데이터베이스마다 다를 수 있습니다. 예를 들어 boolean 타입은 PostgreSQL에서는 `boolean`, CockroachDB에서는 `STRING`으로 알려져 있습니다. 각 데이터베이스별 타입 이름의 전체 상세 정보는 [Scalar types reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)를 참고하세요.

- Raw query typecasting behavior

Prisma Client의 raw query는 SQL 함수 또는 쿼리가 기대하는 타입의 파라미터를 요구할 수 있습니다. Prisma Client는 미묘한 암시적 캐스팅을 수행하지 않습니다.

예를 들어, 입력으로 `text` 타입만 허용하는 PostgreSQL의 `LENGTH` 함수를 사용하는 다음 쿼리를 보겠습니다:

```
    await prisma.$queryRaw`SELECT LENGTH(${42});`;
```

이 쿼리는 오류를 반환합니다:

```
    // ERROR: function length(integer) does not exist
    // HINT: No function matches the given name and argument types. You might need to add explicit type casts.
```

이 경우 해결 방법은 `42`를 `text` 타입으로 명시적으로 캐스팅하는 것입니다:

```
    await prisma.$queryRaw`SELECT LENGTH(${42}::text);`;
```

- Transactions

[transaction](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions) 내부에서 `.$executeRaw()` 및 `.$queryRaw()`를 사용할 수 있습니다.

- Using variables

`$executeRaw`와 `$queryRaw`는 [**tagged templates**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)로 구현되어 있습니다. tagged template는 Prisma Client에서 raw SQL과 함께 변수를 사용하는 권장 방식입니다.

다음 예시에는 `${userId}`라는 placeholder가 포함되어 있습니다:

```
    const userId = 42;
    const result = await prisma.$queryRaw`SELECT * FROM User WHERE id = ${userId};`;
```

✔ `$queryRaw`와 `$executeRaw`의 tagged template 버전을 사용할 때의 장점은 다음과 같습니다:

- Prisma Client가 모든 변수를 이스케이프합니다.
- Tagged template는 데이터베이스에 종속되지 않습니다 - 변수를 `$1`(PostgreSQL)로 써야 하는지 `?`(MySQL)로 써야 하는지 기억할 필요가 없습니다.
- [SQL Template Tag](https://github.com/blakeembrey/sql-template-tag)는 [유용한 helper](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#tagged-template-helpers)에 대한 접근을 제공합니다.
- 내장된 named variable은 가독성이 더 좋습니다.

> **Note** : tagged template placeholder에 테이블명이나 컬럼명을 전달할 수 없습니다. 예를 들어, `SELECT ?`에 `*` 또는 조건에 따른 `id, name`을 전달할 수 없습니다.

#

- Tagged template helpers

Prisma Client는 구체적으로 [SQL Template Tag](https://github.com/blakeembrey/sql-template-tag)를 사용하며, 이 라이브러리는 여러 helper를 제공합니다. 예를 들어, 다음 쿼리는 `join()`을 사용해 ID 목록을 전달합니다:

```
    import { Prisma } from "@prisma/client";

    const ids = [1, 3, 5, 10, 20];
    const result = await prisma.$queryRaw`SELECT * FROM User WHERE id IN (${Prisma.join(ids)})`;
```

다음 예시는 `userName`이 비어 있는지 여부에 따라 쿼리를 변경하기 위해 `empty` 및 `sql` helper를 사용합니다:

```
    import { Prisma } from "@prisma/client";

    const userName = "";
    const result = await prisma.$queryRaw`SELECT * FROM User ${
      userName ? Prisma.sql`WHERE name = ${userName}` : Prisma.empty // Cannot use "" or NULL here!
    }`;
```

#

- `ALTER` limitation (PostgreSQL)

PostgreSQL은 [prepared statement에서 `ALTER` 사용을 지원하지 않기](https://www.postgresql.org/docs/current/sql-prepare.html) 때문에, 다음 쿼리는 **작동하지 않습니다**:

```
    await prisma.$executeRaw`ALTER USER prisma WITH PASSWORD "${password}"`;
    await prisma.$executeRaw(Prisma.sql`ALTER USER prisma WITH PASSWORD "${password}"`);
```

다음 쿼리를 사용할 수는 있지만, `${password}`가 이스케이프되지 않으므로 잠재적으로 **안전하지 않다**는 점에 유의하세요:

```
    await prisma.$executeRawUnsafe('ALTER USER prisma WITH PASSWORD "$1"', password})
```

- Unsupported types

[`Unsupported` types](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported)는 `$queryRaw` 또는 `$queryRawUnsafe`에서 사용하기 전에 Prisma Client가 지원하는 타입으로 캐스팅해야 합니다. 예를 들어, `Unsupported` 타입의 `location` 필드가 있는 다음 모델을 보겠습니다:

```
    model Country {
      location  Unsupported("point")?
    }
```

지원되지 않는 필드에 대한 다음 쿼리는 **작동하지 않습니다**:

```
    await prisma.$queryRaw`SELECT location FROM Country;`;
```

대신 `Unsupported` 필드를 Prisma Client가 지원하는 임의의 타입으로 캐스팅하세요. 단, **`Unsupported` 컬럼이 해당 캐스팅을 지원하는 경우에 한합니다**.

`Unsupported` 컬럼을 캐스팅하려는 가장 일반적인 대상 타입은 `String`입니다. 예를 들어 PostgreSQL에서는 `text` 타입에 매핑됩니다:

```
    await prisma.$queryRaw`SELECT location::text FROM Country;`;
```

이렇게 하면 데이터베이스가 Prisma Client가 지원하는 `String` 표현을 제공합니다.

지원되는 Prisma 타입의 자세한 내용은 해당 데이터베이스의 [Prisma connector overview](https://docs.prisma.io/docs/orm/core-concepts/supported-databases)를 참고하세요.

## SQL injection prevention

Prisma Client에서 SQL injection을 피하는 가장 이상적인 방법은 가능한 경우 ORM 모델을 사용해 쿼리를 수행하는 것입니다.

이것이 불가능하여 raw query가 필요할 때 Prisma Client는 다양한 raw method를 제공하지만, 이러한 메서드를 안전하게 사용하는 것이 중요합니다.

이 섹션에서는 이러한 메서드를 안전하게/안전하지 않게 사용하는 다양한 예시를 제공합니다. 이 예시는 [Prisma Playground](https://playground.prisma.io/examples)에서 테스트할 수 있습니다.

- In `$queryRaw` and `$executeRaw`

#

- Simple, safe use of `$queryRaw` and `$executeRaw`

이 메서드들은 tagged template를 사용할 때 모든 변수를 이스케이프하고 모든 쿼리를 prepared statement로 전송함으로써 SQL injection 위험을 완화할 수 있습니다.

```
    $queryRaw`...`; // Tagged template
    $executeRaw`...`; // Tagged template
```

다음 예시는 SQL Injection으로부터 안전합니다 ✅:

```
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`;
    const result = await prisma.$queryRaw`SELECT id, name FROM "User" WHERE name = ${inputString}`;

    console.log(result);
```

#

- Unsafe use of `$queryRaw` and `$executeRaw`

하지만 이 메서드들을 안전하지 않은 방식으로 사용하는 것도 가능합니다.

한 가지 방법은 사용자 입력을 안전하지 않게 연결(concatenate)하는 tagged template를 인위적으로 생성하는 것입니다.

다음 예시는 SQL Injection에 취약합니다 ❌:

```
    // Unsafely generate query text
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`; // SQL Injection
    const query = `SELECT id, name FROM "User" WHERE name = ${inputString}`;

    // Version for Typescript
    const stringsArray: any = [...[query]];

    // Version for Javascript
    const stringsArray = [...[query]];

    // Use the `raw` property to impersonate a tagged template
    stringsArray.raw = [query];

    // Use queryRaw
    const result = await prisma.$queryRaw(stringsArray);
    console.log(result);
```

이 메서드를 취약하게 만드는 또 다른 방법은 `Prisma.raw` 함수의 오용입니다.

다음 예시들은 모두 SQL Injection에 취약합니다 ❌:

```
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`;
    const result = await prisma.$queryRaw`SELECT id, name FROM "User" WHERE name = ${Prisma.raw(
      inputString,
    )}`;
    console.log(result);
```

```
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`;
    const result = await prisma.$queryRaw(
      Prisma.raw(`SELECT id, name FROM "User" WHERE name = ${inputString}`),
    );
    console.log(result);
```

```
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`;
    const query = Prisma.raw(`SELECT id, name FROM "User" WHERE name = ${inputString}`);
    const result = await prisma.$queryRaw(query);
    console.log(result);
```

#

- Safely using `$queryRaw` and `$executeRaw` in more complex scenarios

#

- Building raw queries separate to query execution

raw query를 다른 곳에서 빌드하거나 파라미터와 분리해 빌드하려면 다음 메서드 중 하나를 사용해야 합니다.

이 예시에서는 `sql` helper method를 사용해 변수를 안전하게 포함하면서 쿼리 텍스트를 빌드합니다. SQL Injection으로부터 안전합니다 ✅:

```
    // inputString can be untrusted input
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`;

    // Safe if the text query below is completely trusted content
    const query = Prisma.sql`SELECT id, name FROM "User" WHERE name = ${inputString}`;

    const result = await prisma.$queryRaw(query);
    console.log(result);
```

SQL Injection으로부터 안전한 ✅ 다음 예시에서는 `sql` helper method를 사용해 입력값을 위한 파라미터 마커를 포함한 쿼리 텍스트를 빌드합니다. 각 변수는 마커 기호(MySQL의 경우 `?`, PostgreSQL의 경우 `$1`, `$2` 등)로 표현됩니다. 예시는 PostgreSQL 쿼리만 보여준다는 점에 유의하세요.

```
    // Version for Typescript
    const query: any;

    // Version for Javascript
    const query;

    // Safe if the text query below is completely trusted content
    query = Prisma.sql`SELECT id, name FROM "User" WHERE name = $1`;

    // inputString can be untrusted input
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`;
    query.values = [inputString];

    const result = await prisma.$queryRaw(query);
    console.log(result);
```

> **Note** : PostgreSQL 변수는 `$1` 등으로 표현됩니다

#

- Building raw queries elsewhere or in stages

쿼리가 실행되는 위치가 아닌 다른 곳에서 raw query를 빌드하려면, 가장 이상적인 방법은 쿼리 세그먼트로 `Sql` 객체를 생성하고 파라미터 값을 전달하는 것입니다.

다음 예시에서는 파라미터화할 변수가 두 개입니다. `Prisma.sql`에 전달되는 쿼리 문자열이 신뢰할 수 있는 콘텐츠만 포함한다면, 이 예시는 SQL Injection으로부터 안전합니다 ✅:

```
    // Example is safe if the text query below is completely trusted content
    const query1 = `SELECT id, name FROM "User" WHERE name = `; // The first parameter would be inserted after this string
    const query2 = ` OR name = `; // The second parameter would be inserted after this string

    const inputString1 = "Fred";
    const inputString2 = `'Sarah' UNION SELECT id, title FROM "Post"`;

    const query = Prisma.sql([query1, query2, ""], inputString1, inputString2);
    const result = await prisma.$queryRaw(query);
    console.log(result);
```

> 참고: 첫 번째 매개변수로 전달되는 문자열 배열 `Prisma.sql` 은 `sql` 함수가 매개변수 개수보다 쿼리 세그먼트를 하나 더 기대하므로 끝에 빈 문자열이 있어야 합니다.

raw 쿼리를 하나의 큰 문자열로 구성하는 것도 가능하지만, 잠재적으로 위험한 `Prisma.raw` 메서드를 사용하므로 주의가 필요합니다. 또한 Prisma가 일반적으로 제공하듯 해당 데이터베이스에 맞는 매개변수 마커를 여기서는 제공할 수 없기 때문에, 데이터베이스에 맞는 올바른 매개변수 마커를 사용해 쿼리를 구성해야 합니다.

다음 예시는 `Prisma.raw` 에 전달되는 쿼리 문자열에 신뢰할 수 있는 콘텐츠만 포함되어 있다면 SQL Injection으로부터 안전합니다 ✅:

```
    // Version for Typescript
    const query: any;

    // Version for Javascript
    const query;

    // Example is safe if the text query below is completely trusted content
    const query1 = `SELECT id, name FROM "User" `;
    const query2 = `WHERE name = $1 `;

    query = Prisma.raw(`${query1}${query2}`);

    // inputString can be untrusted input
    const inputString = `'Sarah' UNION SELECT id, title FROM "Post"`;
    query.values = [inputString];

    const result = await prisma.$queryRaw(query);
    console.log(result);
```

- In `$queryRawUnsafe` and `$executeRawUnsafe`

#

- Using `$queryRawUnsafe` and `$executeRawUnsafe` unsafely

태그드 템플릿을 사용할 수 없다면 [`$queryRawUnsafe`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#queryrawunsafe) 또는 [`$executeRawUnsafe`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#executerawunsafe)를 대신 사용할 수 있습니다. 하지만 **이 함수들은 코드에서 SQL injection 취약점 위험을 크게 높인다는 점에 유의하세요**.

다음 예시는 `query` 와 `inputString` 을 연결합니다. 이 예시에서는 Prisma Client가 `inputString` 을 이스케이프할 수 ❌ **없기 때문에**, SQL injection에 취약합니다:

```
    const inputString = '"Sarah" UNION SELECT id, title, content FROM Post'; // SQL Injection
    const query = "SELECT id, name, email FROM User WHERE name = " + inputString;
    const result = await prisma.$queryRawUnsafe(query);

    console.log(result);
```

#

- Parameterized queries

태그드 템플릿의 대안으로, `$queryRawUnsafe` 는 표준 매개변수화 쿼리를 지원하며 각 변수는 기호(MySQL은 `?`, PostgreSQL은 `$1`, `$2` 등)로 표현됩니다. 예시는 PostgreSQL 쿼리만 보여준다는 점에 유의하세요.

다음 예시는 SQL Injection으로부터 안전합니다 ✅:

```
    const userName = "Sarah";
    const email = "sarah@prisma.io";
    const result = await prisma.$queryRawUnsafe(
      "SELECT * FROM User WHERE (name = $1 OR email = $2)",
      userName,
      email,
    );
```

> **참고** : PostgreSQL 변수는 `$1` 과 `$2` 로 표현됩니다

태그드 템플릿과 마찬가지로, 변수를 이 방식으로 제공하면 Prisma Client가 모든 변수를 이스케이프합니다.

> **참고** : 매개변수화 쿼리의 변수로 테이블명이나 컬럼명을 전달할 수 없습니다. 예를 들어 `SELECT ?` 를 사용하고 조건에 따라 `*` 또는 `id, name` 을 전달하는 방식은 불가능합니다.

#

- Parameterized PostgreSQL `ILIKE` query

`ILIKE` 를 사용할 때 `%` 와일드카드 문자는 쿼리(`string`)가 아니라 변수 자체에 포함되어야 합니다. 이 예시는 SQL Injection으로부터 안전합니다 ✅.

```
    const userName = "Sarah";
    const emailFragment = "prisma.io";
    const result = await prisma.$queryRawUnsafe(
      'SELECT * FROM "User" WHERE (name = $1 OR email ILIKE $2)',
      userName,
      `%${emailFragment}`,
    );
```

> **참고** : `%$2` 를 인수로 사용하는 방식은 동작하지 않습니다

## Raw queries with MongoDB

MongoDB의 경우 Prisma Client는 raw 쿼리를 보낼 수 있는 세 가지 메서드를 제공합니다. 다음을 사용할 수 있습니다:

- `$runCommandRaw`: 데이터베이스에 대해 명령을 실행
- `<model>.findRaw`: 필터와 일치하는 문서를 0개 이상 조회
- `<model>.aggregateRaw`: 컬렉션에서 집계 작업 수행

* `$runCommandRaw()`

`$runCommandRaw()` 는 데이터베이스에 raw MongoDB 명령을 실행합니다. 입력으로 모든 [MongoDB database commands](https://www.mongodb.com/docs/manual/reference/command/)를 받을 수 있지만, 다음은 예외입니다:

- `find` (`findRaw()` 사용: [`findRaw()`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#findraw))
- `aggregate` (`aggregateRaw()` 사용: [`aggregateRaw()`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#aggregateraw))

`$runCommandRaw()` 로 MongoDB 데이터베이스 명령을 실행할 때는 다음에 유의하세요:

- `$runCommandRaw()` 호출 시 전달하는 객체는 MongoDB 데이터베이스 명령의 문법을 따라야 합니다.
- 해당 MongoDB 데이터베이스 명령에 적절한 역할(role)로 데이터베이스에 연결해야 합니다.

다음 예시에서는 쿼리가 동일한 `_id` 를 가진 두 레코드를 삽입합니다. 이는 일반적인 문서 검증을 우회합니다.

```
    prisma.$runCommandRaw({
      insert: "Pets",
      bypassDocumentValidation: true,
      documents: [
        {
          _id: 1,
          name: "Felinecitas",
          type: "Cat",
          breed: "Russian Blue",
          age: 12,
        },
        {
          _id: 1,
          name: "Nao Nao",
          type: "Dog",
          breed: "Chow Chow",
          age: 2,
        },
      ],
    });
```

`"find"` 또는 `"aggregate"` 명령이 포함된 쿼리에는 `$runCommandRaw()` 를 사용하지 마세요. 모든 데이터를 가져오지 못할 수 있기 때문입니다. MongoDB는 [cursor](https://www.mongodb.com/docs/manual/tutorial/iterate-a-cursor/)를 반환하는데, 이 커서는 MongoDB 세션에 연결되어 있어 매번 동일한 MongoDB 세션에 도달하지 못할 수 있습니다. 이런 쿼리에는 전용 메서드인 [`findRaw()`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#findraw) 와 [`aggregateRaw()`](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries#aggregateraw) 를 대신 사용해야 합니다.

#

- Return type

`$runCommandRaw()` 는 입력에 따라 형태가 달라지는 `JSON` 객체를 반환합니다.

#

- Signature

```
    $runCommandRaw(command: InputJsonObject): PrismaPromise<JsonObject>;
```

- `findRaw()`

`<model>.findRaw()` 는 실제 데이터베이스 레코드를 반환합니다. `User` 컬렉션에서 필터와 일치하는 문서를 0개 이상 찾습니다:

```
    const result = await prisma.user.findRaw({
      filter: { age: { $gt: 25 } },
      options: { projection: { _id: false } },
    });
```

#

- Return type

`<model>.findRaw()` 는 입력에 따라 형태가 달라지는 `JSON` 객체를 반환합니다.

#

- Signature

```
    <model>.findRaw(args?: {filter?: InputJsonObject, options?: InputJsonObject}): PrismaPromise<JsonObject>;
```

- `filter`: 쿼리 조건(predicate) 필터입니다. 지정하지 않으면 컬렉션의 모든 문서가 [predicate](https://www.mongodb.com/docs/manual/reference/mql/query-predicates/)와 일치합니다.
- `options`: [`find` command](https://www.mongodb.com/docs/manual/reference/command/find/#command-fields)에 전달할 추가 옵션입니다.

* `aggregateRaw()`

`<model>.aggregateRaw()` 는 집계된 데이터베이스 레코드를 반환합니다. `User` 컬렉션에서 집계 작업을 수행합니다:

```
    const result = await prisma.user.aggregateRaw({
      pipeline: [
        { $match: { status: "registered" } },
        { $group: { _id: "$country", total: { $sum: 1 } } },
      ],
    });
```

#

- Return type

`<model>.aggregateRaw()` 는 입력에 따라 형태가 달라지는 `JSON` 객체를 반환합니다.

#

- Signature

```
    <model>.aggregateRaw(args?: {pipeline?: InputJsonObject[], options?: InputJsonObject}): PrismaPromise<JsonObject>;
```

- `pipeline`: [aggregation pipeline](https://www.mongodb.com/docs/atlas/data-federation/supported-unsupported/supported-aggregation/)을 통해 문서 스트림을 처리하고 변환하는 집계 단계 배열입니다.
- `options`: [`aggregate` command](https://www.mongodb.com/docs/manual/reference/command/aggregate/#command-fields)에 전달할 추가 옵션입니다.

#

- Caveats

`ObjectId` 또는 `Date` 같은 커스텀 객체를 다룰 때는 [MongoDB extended JSON Spec](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/#type-representations)에 따라 전달해야 합니다. 예시:

```
    const result = await prisma.user.aggregateRaw({
      pipeline: [
        { $match: { _id: { $oid: id } } },
        //                     ^ notice the $oid convention here
      ],
    });
```
