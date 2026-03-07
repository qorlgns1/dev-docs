---
title: "데이터 모델링"
description: "Prisma를 사용한 데이터 모델링이 SQL 또는 ORM을 사용한 데이터 모델링과 어떻게 다른지 알아보세요. Prisma는 데이터베이스 스키마를 설명하기 위해 선언형 데이터 모델링 언어를 사용합니다."
---

# 데이터 모델링

Prisma를 사용한 데이터 모델링이 SQL 또는 ORM을 사용한 데이터 모델링과 어떻게 다른지 알아보세요. Prisma는 데이터베이스 스키마를 설명하기 위해 선언형 데이터 모델링 언어를 사용합니다.

## 데이터 모델링이란?

_데이터 모델링_ 이라는 용어는 **애플리케이션 내 객체의 형태와 구조를 정의하는 과정**을 의미합니다. 이러한 객체는 종종 "애플리케이션 모델"이라고 불립니다. 관계형 데이터베이스(예: PostgreSQL)에서는 이들이 _테이블_ 에 저장됩니다. 문서 데이터베이스(예: MongoDB)를 사용할 때는 _컬렉션_ 에 저장됩니다.

애플리케이션의 도메인에 따라 모델은 달라집니다. 예를 들어 블로깅 애플리케이션을 만든다면 _blog_ , _author_ , _article_ 같은 모델이 있을 수 있습니다. 카셰어링 앱을 만든다면 _driver_ , _car_ , _route_ 같은 모델이 있을 가능성이 큽니다. 애플리케이션 모델을 사용하면 각 엔티티에 해당하는 _데이터 구조_ 를 만들어 코드에서 이러한 서로 다른 엔티티를 표현할 수 있습니다.

데이터를 모델링할 때는 일반적으로 다음과 같은 질문을 하게 됩니다.

- 내 애플리케이션의 핵심 엔티티/개념은 무엇인가?
- 이들은 서로 어떻게 연관되는가?
- 주요 특성/속성은 무엇인가?
- 내 기술 스택으로 어떻게 표현할 수 있는가?

## Prisma ORM 없이 데이터 모델링하기

데이터 모델링은 일반적으로 (최소) 두 수준에서 이루어져야 합니다.

- **데이터베이스** 수준
- **애플리케이션** 수준(즉, 프로그래밍 언어 내)

두 수준에서 애플리케이션 모델이 표현되는 방식은 몇 가지 이유로 다를 수 있습니다.

- 데이터베이스와 프로그래밍 언어는 서로 다른 데이터 타입을 사용합니다.
- 관계는 데이터베이스와 프로그래밍 언어에서 표현 방식이 다릅니다.
- 데이터베이스는 일반적으로 인덱스, 연쇄 삭제(cascading deletes), 다양한 추가 제약 조건(예: unique, not null, ...)처럼 더 강력한 데이터 모델링 기능을 가집니다.
- 데이터베이스와 프로그래밍 언어는 기술적 제약이 다릅니다.

* 데이터베이스 수준에서의 데이터 모델링

#

- 관계형 데이터베이스

관계형 데이터베이스에서 모델은 _테이블_ 로 표현됩니다. 예를 들어 애플리케이션 사용자 정보를 저장하기 위해 `users` 테이블을 정의할 수 있습니다. PostgreSQL에서는 다음과 같이 정의합니다.

```
    CREATE TABLE users (
      user_id SERIAL PRIMARY KEY NOT NULL,
      name VARCHAR(255),
      email VARCHAR(255) UNIQUE NOT NULL,
      isAdmin BOOLEAN NOT NULL DEFAULT false
    );
```

일부 임의 데이터를 포함한 `users` 테이블의 시각적 표현은 다음과 같습니다.

| `user_id` | `name`  | `email`           | `isAdmin` |
| --------- | ------- | ----------------- | --------- |
| `1`       | `Alice` | `alice@prisma.io` | `false`   |
| `2`       | `Bob`   | `bob@prisma.io`   | `false`   |
| `3`       | `Sarah` | `sarah@prisma.io` | `true`    |

이 테이블에는 다음 열이 있습니다.

- `user_id`: `users` 테이블에 새 레코드가 추가될 때마다 증가하는 정수입니다. 또한 각 레코드의 [기본 키](https://en.wikipedia.org/wiki/Primary_key)를 나타냅니다.
- `name`: 최대 255자의 문자열입니다.
- `email`: 최대 255자의 문자열입니다. 또한 추가된 제약 조건은 `email` 열에서 두 레코드가 중복 값을 가질 수 없고, _모든_ 레코드에 이 값이 반드시 있어야 함을 나타냅니다.
- `isAdmin`: 사용자가 관리자 권한을 가졌는지 나타내는 불리언 값입니다(기본값: `false`)

#

- MongoDB

MongoDB 데이터베이스에서는 모델이 _컬렉션_ 으로 표현되며, 컬렉션에는 어떤 구조든 가질 수 있는 _문서_ 가 포함됩니다.

```
    {
      _id: '607ee94800bbe41f001fd568',
      slug: 'prisma-loves-mongodb',
      title: 'Prisma <3 MongoDB',
      body: "This is my first post. Isn't MongoDB + Prisma awesome?!"
    }
```

Prisma Client는 현재 일관된 모델과 [정규화된 모델 설계](https://www.mongodb.com/docs/manual/data-modeling/best-practices/#std-label-data-modeling-best-practices)를 기대합니다. 이는 다음을 의미합니다.

- Prisma 스키마에 없는 모델이나 필드는 무시됩니다.
- 필드가 필수인데 MongoDB 데이터셋에 존재하지 않으면 오류가 발생합니다.

* 애플리케이션 수준에서의 데이터 모델링

애플리케이션 도메인의 엔티티를 표현하는 테이블을 생성하는 것 외에도, 프로그래밍 언어에서 애플리케이션 모델을 만들어야 합니다. 객체 지향 언어에서는 보통 모델을 표현하기 위해 _클래스_ 를 생성합니다. 프로그래밍 언어에 따라 _인터페이스_ 또는 _struct_ 로도 표현할 수 있습니다.

데이터베이스의 테이블과 코드에서 정의한 모델 사이에는 강한 상관관계가 있는 경우가 많습니다. 예를 들어 앞서 언급한 `users` 테이블의 레코드를 애플리케이션에서 표현하려면, 다음과 유사한 JavaScript (ES6) 클래스를 정의할 수 있습니다.

```
    class User {
      constructor(user_id, name, email, isAdmin) {
        this.user_id = user_id;
        this.name = name;
        this.email = email;
        this.isAdmin = isAdmin;
      }
    }
```

TypeScript를 사용할 때는 대신 인터페이스를 정의할 수 있습니다.

```
    interface User {
      user_id: number
      name: string
      email: string
      isAdmin: boolean
    }
```

두 경우 모두 `User` 모델이 이전 예시의 `users` 테이블과 동일한 속성을 가지는 점에 주목하세요. 데이터베이스 테이블과 애플리케이션 모델이 1:1로 매핑되는 경우가 많지만, 데이터베이스와 애플리케이션에서 모델이 완전히 다르게 표현되는 경우도 있습니다.

이 구성을 사용하면 `users` 테이블에서 레코드를 가져와 `User` 타입의 인스턴스로 저장할 수 있습니다. 다음 코드 스니펫은 PostgreSQL 드라이버로 [`pg`](https://node-postgres.com/)를 사용하고, 위에서 정의한 JavaScript 클래스를 기반으로 `User` 인스턴스를 생성합니다.

```
    const resultRows = await client.query("SELECT * FROM users WHERE user_id = 1");
    const userData = resultRows[0];
    const user = new User(userData.user_id, userData.name, userData.email, userData.isAdmin);
    // user = {
    //   user_id: 1,
    //   name: "Alice",
    //   email: "alice@prisma.io",
    //   isAdmin: false
    // }
```

이 예시들에서 애플리케이션 모델은 "dumb"하다는 점에 주목하세요. 즉, 로직을 구현하지 않고 _plain old JavaScript objects_ 형태로 데이터를 담는 것이 유일한 목적입니다.

- ORM을 사용한 데이터 모델링

ORM은 개발자가 데이터베이스를 더 쉽게 다룰 수 있도록 객체 지향 언어에서 흔히 사용됩니다. ORM의 핵심 특징은 애플리케이션 데이터를 _클래스_ 로 모델링하고, 이를 기반 데이터베이스의 _테이블_ 에 매핑할 수 있게 해준다는 점입니다.

앞서 설명한 접근 방식과의 주요 차이점은, 이 클래스들이 데이터를 담는 것뿐 아니라 상당한 양의 로직도 구현한다는 것입니다. 주로 저장, 조회, 직렬화, 역직렬화를 위한 로직이며, 때로는 애플리케이션에 특화된 비즈니스 로직도 구현합니다.

즉, 데이터베이스에서 데이터를 읽고 쓰기 위해 SQL 구문을 직접 작성하는 대신, 모델 클래스의 인스턴스가 데이터를 저장하고 조회하는 API를 제공합니다.

[Sequelize](https://sequelize.org/)는 Node.js 생태계에서 인기 있는 ORM입니다. 이전 섹션의 동일한 `User` 모델을 Sequelize의 모델링 방식으로 정의하면 다음과 같습니다.

```
    class User extends Model {}
    User.init(
      {
        user_id: {
          type: Sequelize.INTEGER,
          primaryKey: true,
          autoIncrement: true,
        },
        name: Sequelize.STRING(255),
        email: {
          type: Sequelize.STRING(255),
          unique: true,
        },
        isAdmin: Sequelize.BOOLEAN,
      },
      { sequelize, modelName: "user" },
    );
```

이 `User` 클래스를 사용한 예시를 동작시키려면, 여전히 데이터베이스에 해당 테이블을 생성해야 합니다. Sequelize에서는 두 가지 방법이 있습니다.

- `User.sync()` 실행(일반적으로 프로덕션에는 권장되지 않음)
- 데이터베이스 스키마를 변경하기 위해 [Sequelize migrations](https://sequelize.org/v5/manual/migrations.html) 사용

이전 섹션에서 보였던 것처럼 `User` 클래스를 직접 인스턴스화(`new User(...)`)하지 않고, 대신 `User` 클래스의 _정적(static)_ 메서드를 호출하면 `User` 모델 인스턴스가 반환된다는 점에 유의하세요.

```
    const user = await User.findByPk(42);
```

`findByPk` 호출은 ID 값 `42`로 식별되는 `User` 레코드를 조회하기 위한 SQL 구문을 생성합니다.

결과로 얻는 `user` 객체는 Sequelize의 `Model` 클래스 인스턴스입니다(`User`가 `Model`을 상속하기 때문). 이는 POJO(Plain Old JavaScript Object)가 아니라 Sequelize의 추가 동작을 구현한 객체입니다.

## Prisma ORM으로 데이터 모델링하기

애플리케이션에서 Prisma ORM의 어떤 부분을 사용할지에 따라 데이터 모델링 흐름이 약간 달라집니다. 아래 두 섹션에서는 [**Prisma Client만 사용하는 경우**](https://docs.prisma.io/docs/orm/core-concepts/data-modeling#using-only-prisma-client)와 [**Prisma Client와 Prisma Migrate를 함께 사용하는 경우**](https://docs.prisma.io/docs/orm/core-concepts/data-modeling#using-prisma-client-and-prisma-migrate)의 워크플로를 설명합니다.

어떤 접근 방식을 쓰든, Prisma ORM에서는 프로그래밍 언어에서 클래스, 인터페이스, struct를 수동으로 정의해 애플리케이션 모델을 만들지 않습니다. 대신 애플리케이션 모델은 [Prisma 스키마](https://docs.prisma.io/docs/orm/prisma-schema/overview)에 정의됩니다.

- **Prisma Client만 사용** : Prisma 스키마의 애플리케이션 모델은 _데이터베이스 스키마 인트로스펙션을 기반으로 생성_ 됩니다. 데이터 모델링은 주로 데이터베이스 수준에서 이루어집니다.
- **Prisma Client와 Prisma Migrate 사용** : Prisma 스키마에 _애플리케이션 모델을 수동으로 추가_ 하여 데이터 모델링이 이루어집니다. Prisma Migrate는 이러한 애플리케이션 모델을 기반 데이터베이스의 테이블로 매핑합니다(현재 관계형 데이터베이스에서만 지원).

예를 들어, 이전 예시의 `User` 모델은 Prisma 스키마에서 다음과 같이 표현됩니다.

```
    model User {
      user_id Int     @id @default(autoincrement())
      name    String?
      email   String  @unique
      isAdmin Boolean @default(false)
    }
```

Prisma 스키마에 애플리케이션 모델이 들어가면(인트로스펙션으로 추가했든 수동으로 추가했든), 다음 단계는 일반적으로 Prisma Client를 생성하는 것입니다. Prisma Client는 애플리케이션 모델 형태에 맞춰 데이터를 읽고 쓸 수 있는 프로그래밍 가능하고 타입 안전한 API를 제공합니다.

Prisma Client는 코드에서 애플리케이션 모델을 표현하기 위해 TypeScript [type aliases](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)를 사용합니다. 예를 들어 `User` 모델은 생성된 Prisma Client 라이브러리에서 다음과 같이 표현됩니다.

```
    export type User = {
      id: number;
      name: string | null;
      email: string;
      isAdmin: boolean;
    };
```

생성된 타입 외에도, Prisma Client는 `@prisma/client` 패키지를 설치하면 사용할 수 있는 데이터 접근 API를 제공합니다.

```
    import { PrismaClient } from '../prisma/generated/client'
    // or
    // const { PrismaClient } = require('../prisma/generated/client')

    const prisma = new PrismaClient()

    // use inside an `async` function to `await` the result
    await prisma.user.findUnique(...)
    await prisma.user.findMany(...)
    await prisma.user.create(...)
    await prisma.user.update(...)
    await prisma.user.delete(...)
    await prisma.user.upsert(...)
```

- Prisma Client만 사용하기

애플리케이션에서 Prisma Client만 사용하고 Prisma Migrate를 _사용하지 않는_ 경우, 데이터 모델링은 SQL을 통해 데이터베이스 수준에서 이루어져야 합니다. SQL 스키마가 준비되면 Prisma의 인트로스펙션 기능을 사용해 Prisma 스키마에 애플리케이션 모델을 추가합니다. 마지막으로 Prisma Client를 생성하면 데이터베이스에서 데이터를 읽고 쓸 수 있는 타입과 프로그래밍 API가 생성됩니다.

주요 워크플로 개요는 다음과 같습니다.

1. SQL을 사용해 데이터베이스 스키마를 변경합니다(예: `CREATE TABLE`, `ALTER TABLE`, ...).
2. `prisma db pull`을 실행해 데이터베이스를 인트로스펙션하고 Prisma 스키마에 애플리케이션 모델을 추가합니다.
3. `prisma generate`를 실행해 Prisma Client API를 업데이트합니다.

- Prisma Client와 Prisma Migrate 사용하기

[Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate)를 사용할 때는 Prisma 스키마에 애플리케이션 모델을 정의하고, 관계형 데이터베이스에서는 `prisma migrate` 하위 명령을 사용해 일반 SQL 마이그레이션 파일을 생성합니다. 이 파일은 적용 전에 편집할 수 있습니다. MongoDB에서는 대신 `prisma db push`를 사용하며, 변경 사항이 데이터베이스에 직접 적용됩니다.

주요 워크플로 개요는 다음과 같습니다.

1. Prisma 스키마에서 애플리케이션 모델을 수동으로 변경합니다(예: 새 모델 추가, 기존 모델 제거, ...).
2. `prisma migrate dev`를 실행해 마이그레이션을 생성 및 적용하거나 `prisma db push`를 실행해 변경 사항을 직접 적용합니다(두 경우 모두 Prisma Client가 자동 생성됨).
