---
title: "TypeORM"
description: "Prisma와 TypeORM을 비교하는 방법 알아보기"
---

출처 URL: https://docs.prisma.io/docs/orm/more/comparisons/prisma-and-typeorm

# TypeORM

Prisma와 TypeORM을 비교하는 방법 알아보기

이 페이지에서는 Prisma ORM과 [TypeORM](https://typeorm.io/)을 비교합니다. TypeORM에서 Prisma ORM으로 마이그레이션하는 방법을 알고 싶다면 이 [가이드](https://docs.prisma.io/docs/guides/switch-to-prisma-orm/from-sql-orms)를 확인하세요.

## TypeORM vs Prisma ORM

Prisma ORM과 TypeORM은 비슷한 문제를 해결하지만, 동작 방식은 매우 다릅니다.

**TypeORM**은 _테이블_ 을 _모델 클래스_ 에 매핑하는 전통적인 ORM입니다. 이 모델 클래스는 SQL 마이그레이션 생성에 사용할 수 있습니다. 이후 모델 클래스 인스턴스는 런타임에 애플리케이션의 CRUD 쿼리를 위한 인터페이스를 제공합니다.

**Prisma ORM**은 bloated model instances, 비즈니스 로직과 저장소 로직의 혼합, type-safety 부족, lazy loading 등으로 인한 예측 불가능한 쿼리 같은 전통적인 ORM의 여러 문제를 완화하는 새로운 종류의 ORM입니다.

[Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)를 사용해 애플리케이션 모델을 선언적으로 정의합니다. 그런 다음 Prisma Migrate가 Prisma schema로부터 SQL 마이그레이션을 생성하고 데이터베이스에 실행합니다. CRUD 쿼리는 Node.js와 TypeScript를 위한 가볍고 완전한 type-safe 데이터베이스 클라이언트인 Prisma Client가 제공합니다.

## API design & Level of abstraction

TypeORM과 Prisma ORM은 서로 다른 추상화 수준에서 동작합니다. TypeORM은 API가 SQL을 더 직접적으로 반영하는 반면, Prisma Client는 애플리케이션 개발자의 일반적인 작업을 염두에 두고 신중하게 설계된 더 높은 수준의 추상화를 제공합니다. Prisma ORM의 API 설계는 [making the right thing easy](https://jason.energy/right-thing-easy-thing/)라는 아이디어에 크게 기반합니다.

Prisma Client는 더 높은 수준의 추상화에서 동작하지만, 기본 데이터베이스의 모든 기능을 드러내는 것을 목표로 하며, 사용 사례에 필요하면 언제든 [raw SQL](https://docs.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries)로 내려갈 수 있습니다.

다음 섹션에서는 특정 시나리오에서 Prisma ORM과 TypeORM의 API가 어떻게 다른지, 그리고 이러한 경우 Prisma ORM API 설계의 근거가 무엇인지 몇 가지 예시를 통해 살펴봅니다.

- 필터링

TypeORM은 목록이나 레코드를 필터링할 때 주로 SQL 연산자에 의존하며, 예를 들어 `find` 메서드를 사용합니다. 반면 Prisma ORM은 직관적으로 사용할 수 있는 더 [generic set of operators](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting#combining-operators)를 제공합니다. 또한 아래 type-safety 섹션([아래](https://docs.prisma.io/docs/orm/more/comparisons/prisma-and-typeorm#filtering-1))에서 설명하듯, TypeORM은 많은 시나리오에서 필터 쿼리의 type-safety를 잃는다는 점도 주목해야 합니다.

TypeORM과 Prisma ORM의 필터링 API 차이를 잘 보여주는 예시는 `string` 필터입니다. TypeORM은 주로 SQL에서 직접 온 `ILike` 연산자 기반 필터를 제공하는 반면, Prisma ORM은 개발자가 사용할 수 있는 더 구체적인 연산자(예: `contains`, `startsWith`, `endsWith`)를 제공합니다.

```
    const posts = await prisma.post.findMany({
      where: {
        title: "Hello World",
      },
    });
```

```
    const posts = await postRepository.find({
      where: {
        title: ILike("Hello World"),
      },
    });
```

```
    const posts = await prisma.post.findMany({
      where: {
        title: { contains: "Hello World" },
      },
    });
```

```
    const posts = await postRepository.find({
      where: {
        title: ILike("%Hello World%"),
      },
    });
```

```
    const posts = await prisma.post.findMany({
      where: {
        title: { startsWith: "Hello World" },
      },
    });
```

```
    const posts = await postRepository.find({
      where: {
        title: ILike("Hello World%"),
      },
    });
```

```
    const posts = await prisma.post.findMany({
      where: {
        title: { endsWith: "Hello World" },
      },
    });
```

```
    const posts = await postRepository.find({
      where: {
        title: ILike("%Hello World"),
      },
    });
```

- 페이지네이션

TypeORM은 limit-offset 페이지네이션만 제공하는 반면, Prisma ORM은 limit-offset뿐 아니라 cursor-based 방식까지 전용 API를 편리하게 제공합니다. 두 접근 방식은 문서의 [Pagination](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/pagination) 섹션 또는 아래 API 비교([아래](https://docs.prisma.io/docs/orm/more/comparisons/prisma-and-typeorm#pagination-1))에서 자세히 확인할 수 있습니다.

- 관계

외래 키로 연결된 레코드를 다루는 작업은 SQL에서 매우 복잡해질 수 있습니다. Prisma ORM의 [virtual relation field](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields) 개념은 애플리케이션 개발자가 관련 데이터를 직관적이고 편리하게 다룰 수 있게 해줍니다. Prisma ORM 접근 방식의 몇 가지 장점은 다음과 같습니다.

- fluent API를 통한 관계 탐색([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#fluent-api))
- 연결된 레코드의 업데이트/생성을 가능하게 하는 nested writes([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-writes))
- 관련 레코드에 필터 적용([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#relation-filters))
- JOIN을 신경 쓰지 않고도 nested data를 쉽고 type-safe하게 조회([docs](https://docs.prisma.io/docs/orm/prisma-client/queries/relation-queries#nested-reads))
- 모델과 그 관계를 기반으로 nested TypeScript typings 생성([docs](https://docs.prisma.io/docs/orm/prisma-client/type-safety))
- relation fields를 통한 데이터 모델 내 관계의 직관적 모델링([docs](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations))
- relation tables(때로는 JOIN, link, pivot, junction tables라고도 함)의 암시적 처리([docs](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations))

* 데이터 모델링 및 마이그레이션

Prisma 모델은 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)에서 정의되는 반면, TypeORM은 클래스와 실험적인 TypeScript decorators를 사용해 모델을 정의합니다. Active Record ORM 패턴에서 TypeORM 방식은 애플리케이션이 커질수록 유지보수하기 어려운 복잡한 모델 인스턴스로 이어지는 경우가 많습니다.

반면 Prisma ORM은 Prisma schema에 정의된 모델의 데이터 읽기/쓰기를 위해 맞춤형이고 완전한 type-safe API를 노출하는 경량 데이터베이스 클라이언트를 생성하며, Active Record보다 DataMapper ORM 패턴을 따릅니다.

Prisma ORM의 데이터 모델링 DSL은 간결하고 단순하며 직관적입니다. VS Code에서 데이터를 모델링할 때는 자동완성, quick fixes, 정의로 이동 등 개발자 생산성을 높이는 다양한 기능을 제공하는 Prisma ORM의 강력한 VS Code 확장도 활용할 수 있습니다.

```
    model User {
      id    Int     @id @default(autoincrement())
      name  String?
      email String  @unique
      posts Post[]
    }

    model Post {
      id        Int     @id @default(autoincrement())
      title     String
      content   String?
      published Boolean @default(false)
      authorId  Int?
      author    User?   @relation(fields: [authorId], references: [id])
    }
```

```
    import { Entity, PrimaryGeneratedColumn, Column, OneToMany, ManyToOne } from "typeorm";

    @Entity()
    export class User {
      @PrimaryGeneratedColumn()
      id: number;

      @Column({ nullable: true })
      name: string;

      @Column({ unique: true })
      email: string;

      @OneToMany((type) => Post, (post) => post.author)
      posts: Post[];
    }

    @Entity()
    export class Post {
      @PrimaryGeneratedColumn()
      id: number;

      @Column()
      title: string;

      @Column({ nullable: true })
      content: string;

      @Column({ default: false })
      published: boolean;

      @ManyToOne((type) => User, (user) => user.posts)
      author: User;
    }
```

TypeORM과 Prisma ORM의 마이그레이션 동작 방식은 유사합니다. 두 도구 모두 제공된 모델 정의를 기반으로 SQL 파일을 생성하고, 이를 데이터베이스에 실행하는 CLI를 제공합니다. 마이그레이션 실행 전에 SQL 파일을 수정할 수 있으므로, 어떤 커스텀 데이터베이스 작업도 두 마이그레이션 시스템 중 어느 쪽에서든 수행할 수 있습니다.

## Type safety

TypeORM은 Node.js 생태계에서 TypeScript를 완전히 수용한 초기 ORM 중 하나이며, 개발자가 데이터베이스 쿼리에 대해 일정 수준의 type safety를 확보할 수 있도록 훌륭한 작업을 해왔습니다.

하지만 TypeORM의 type safety 보장이 부족한 상황도 매우 많습니다. 다음 섹션에서는 Prisma ORM이 쿼리 결과 타입에 대해 더 강한 보장을 제공할 수 있는 시나리오를 설명합니다.

- 필드 선택

이 섹션에서는 쿼리에서 모델 필드의 일부만 선택할 때 type safety 차이를 설명합니다.

#

- TypeORM

TypeORM은 [`find`](https://typeorm.io/find-options) 메서드(`find`, `findByIds`, `findOne`, ...)에 대해 `select` 옵션을 제공합니다. 예:

select를 사용한 find

모델

```
    const postRepository = getManager().getRepository(Post);
    const publishedPosts: Post[] = await postRepository.find({
      where: { published: true },
      select: ["id", "title"],
    });
```

반환된 `publishedPosts` 배열의 각 객체는 런타임에서 선택된 `id`와 `title` 속성만 가지지만, TypeScript 컴파일러는 이를 알지 못합니다. 따라서 쿼리 후에도 `Post` 엔티티에 정의된 다른 속성에 접근하도록 허용합니다. 예:

```
    const post = publishedPosts[0];

    // The TypeScript compiler has no issue with this
    if (post.content.length > 0) {
      console.log(`This post has some content.`);
    }
```

이 코드는 런타임 에러를 발생시킵니다:

```
    TypeError: Cannot read property 'length' of undefined
```

TypeScript 컴파일러는 반환 객체의 `Post` 타입만 볼 뿐, 런타임에서 객체가 _실제로_ 어떤 필드를 담고 있는지는 알지 못합니다. 따라서 데이터베이스 쿼리에서 조회하지 않은 필드에 접근하는 실수를 막을 수 없어 런타임 에러로 이어집니다.

#

- Prisma ORM

Prisma Client는 동일한 상황에서 완전한 type safety를 보장할 수 있으며, 데이터베이스에서 조회하지 않은 필드 접근을 방지합니다.

Prisma Client 쿼리로 같은 예시를 보겠습니다.

select를 사용한 findMany

모델

```
    const publishedPosts = await prisma.post.findMany({
      where: { published: true },
      select: {
        id: true,
        title: true,
      },
    });
    const post = publishedPosts[0];

    // The TypeScript compiler will not allow this
    if (post.content.length > 0) {
      console.log(`This post has some content.`);
    }
```

이 경우 TypeScript 컴파일러는 컴파일 타임에 이미 다음 에러를 발생시킵니다:

```
    [ERROR] 14:03:39 ⨯ Unable to compile TypeScript:
    src/index.ts:36:12 - error TS2339: Property 'content' does not exist on type '{ id: number; title: string; }'.

    42   if (post.content.length > 0) {
```

이는 Prisma Client가 쿼리의 반환 타입을 _on the fly_ 로 생성하기 때문입니다. 이 경우 `publishedPosts`의 타입은 다음과 같습니다:

```
    const publishedPosts: {
      id: number;
      title: string;
    }[];
```

따라서 쿼리에서 조회하지 않은 모델 속성에 실수로 접근하는 일은 불가능합니다.

- 관계 로딩

이 섹션에서는 쿼리에서 모델의 관계를 로드할 때 type safety 차이를 설명합니다. 전통적인 ORM에서는 이를 _eager loading_ 이라고 부르기도 합니다.

#

- TypeORM

TypeORM은 [`find`](https://typeorm.io/find-options) 메서드에 전달할 수 있는 `relations` 옵션을 통해 데이터베이스에서 관계를 eager loading할 수 있습니다.

다음 예시를 보겠습니다.

relations를 사용한 find

모델들

```
    const postRepository = getManager().getRepository(Post);
    const publishedPosts: Post[] = await postRepository.find({
      where: { published: true },
      relations: ["author"],
    });
```

```
    @Entity()
    export class User {
      @PrimaryGeneratedColumn()
      id: number;

      @Column({ nullable: true })
      name: string;

      @Column({ unique: true })
      email: string;

      @OneToMany((type) => Post, (post) => post.author)
      posts: Post[];
    }
```

`select`와 달리, TypeORM은 `relations` 옵션에 전달하는 문자열에 대해 자동완성도 type-safety도 제공하지 _않습니다_. 즉, 이러한 관계를 쿼리할 때 발생한 오타를 TypeScript 컴파일러가 잡아낼 수 없습니다. 예를 들어 다음 쿼리를 허용합니다:

```
    const publishedPosts: Post[] = await postRepository.find({
      where: { published: true },
      // this query would lead to a runtime error because of a typo
      relations: ["authors"],
    });
```

이 미묘한 오타는 다음 런타임 에러로 이어집니다:

```
    UnhandledPromiseRejectionWarning: Error: Relation "authors" was not found; please check if it is correct and really exists in your entity.
```

#

- Prisma ORM

Prisma ORM은 이런 실수로부터 보호하여, 애플리케이션 런타임에서 발생할 수 있는 한 종류의 오류를 제거합니다. Prisma Client 쿼리에서 관계를 로드하기 위해 `include`를 사용하면, 자동완성으로 쿼리를 지정할 수 있을 뿐 아니라 쿼리 결과 타입도 올바르게 지정됩니다.

relations를 사용한 find

모델들

```
    const publishedPosts = await prisma.post.findMany({
      where: { published: true },
      include: { author: true },
    });
```

다시 말해 `publishedPosts` 타입은 on the fly로 생성되며 다음과 같습니다:

```
    const publishedPosts: (Post & {
      author: User;
    })[];
```

참고로, Prisma Client가 Prisma 모델에 대해 생성하는 `User`와 `Post` 타입은 다음과 같습니다.

User

Post

```
    // Generated by Prisma ORM
    export type User = {
      id: number;
      name: string | null;
      email: string;
    };
```

- 필터링

이 섹션에서는 `where`를 사용해 레코드 목록을 필터링할 때 type safety 차이를 설명합니다.

#

- TypeORM

TypeORM은 [`find`](https://typeorm.io/find-options) 메서드에 `where` 옵션을 전달해 특정 기준에 따라 반환 레코드 목록을 필터링할 수 있습니다. 이러한 기준은 모델 속성을 기준으로 정의할 수 있습니다.

#

- 연산자 사용 시 타입 안전성 상실

다음 예시를 살펴보세요:

select를 사용한 find

Model

```
    const postRepository = getManager().getRepository(Post);
    const publishedPosts: Post[] = await postRepository.find({
      where: {
        published: true,
        title: ILike("Hello World"),
        views: MoreThan(0),
      },
    });
```

이 코드는 정상적으로 실행되며 런타임에서 유효한 쿼리를 생성합니다. 하지만 다양한 시나리오에서 `where` 옵션은 실제로 타입 안전하지 않습니다. 특정 타입에서만 동작하는 `ILike` 또는 `MoreThan` 같은 `FindOperator`를 사용할 때(`ILike`는 문자열, `MoreThan`은 숫자), 모델 필드에 올바른 타입을 제공한다는 보장을 잃게 됩니다.

예를 들어 `MoreThan` 연산자에 문자열을 전달할 수 있습니다. TypeScript 컴파일러는 이를 문제로 인식하지 않으며, 애플리케이션은 런타임에서만 실패합니다:

```
    const postRepository = getManager().getRepository(Post);
    const publishedPosts: Post[] = await postRepository.find({
      where: {
        published: true,
        title: ILike("Hello World"),
        views: MoreThan("test"),
      },
    });
```

위 코드는 TypeScript 컴파일러가 잡아주지 못하는 다음 런타임 오류를 발생시킵니다:

```
    error: error: invalid input syntax for type integer: "test"
```

#

- 존재하지 않는 속성 지정

또한 TypeScript 컴파일러는 `where` 옵션에 모델에 존재하지 않는 속성을 지정하는 것도 허용하며, 이 역시 런타임 오류로 이어집니다:

```
    const publishedPosts: Post[] = await postRepository.find({
      where: {
        published: true,
        title: ILike("Hello World"),
        viewCount: 1,
      },
    });
```

이 경우에도 애플리케이션은 다음 오류와 함께 런타임에서 실패합니다:

```
    EntityColumnNotFound: No entity column "viewCount" was found.
```

#

- Prisma ORM

TypeORM에서 타입 안전성 측면에서 문제가 되는 두 필터링 시나리오는 Prisma ORM에서 완전한 타입 안전 방식으로 모두 처리됩니다.

#

- 타입 안전한 연산자 사용

Prisma ORM에서는 TypeScript 컴파일러가 필드별로 연산자를 올바르게 사용하도록 강제합니다:

```
    const publishedPosts = await prisma.post.findMany({
      where: {
        published: true,
        title: { contains: "Hello World" },
        views: { gt: 0 },
      },
    });
```

Prisma Client에서는 위에서 보여준 동일한 문제성 쿼리를 작성할 수 없습니다:

```
    const publishedPosts = await prisma.post.findMany({
      where: {
        published: true,
        title: { contains: "Hello World" },
        views: { gt: "test" }, // Caught by the TypeScript compiler
      },
    });
```

TypeScript 컴파일러가 이를 감지하고, 앱의 런타임 실패를 방지하기 위해 다음 오류를 발생시킵니다:

```
    [ERROR] 16:13:50 ⨯ Unable to compile TypeScript:
    src/index.ts:39:5 - error TS2322: Type '{ gt: string; }' is not assignable to type 'number | IntNullableFilter'.
      Type '{ gt: string; }' is not assignable to type 'IntNullableFilter'.
        Types of property 'gt' are incompatible.
          Type 'string' is not assignable to type 'number'.

    42     views: { gt: "test" }
```

#

- 모델 속성으로 필터를 타입 안전하게 정의

TypeORM에서는 모델 필드에 매핑되지 않는 속성을 `where` 옵션에 지정할 수 있습니다. 위 예시에서 `viewCount`로 필터링했을 때 런타임 오류가 발생한 이유는 실제 필드명이 `views`이기 때문입니다.

Prisma ORM에서는 TypeScript 컴파일러가 모델에 존재하지 않는 어떤 속성도 `where` 내부에서 참조하지 못하게 합니다:

```
    const publishedPosts = await prisma.post.findMany({
      where: {
        published: true,
        title: { contains: "Hello World" },
        viewCount: { gt: 0 }, // Caught by the TypeScript compiler
      },
    });
```

다시 말해, TypeScript 컴파일러는 다음 메시지로 이러한 실수를 방지합니다:

```
    [ERROR] 16:16:16 ⨯ Unable to compile TypeScript:
    src/index.ts:39:5 - error TS2322: Type '{ published: boolean; title: { contains: string; }; viewCount: { gt: number; }; }' is not assignable to type 'PostWhereInput'.
      Object literal may only specify known properties, and 'viewCount' does not exist in type 'PostWhereInput'.

    42     viewCount: { gt: 0 }
```

- 새 레코드 생성

이 섹션에서는 새 레코드를 생성할 때의 타입 안전성 차이를 설명합니다.

#

- TypeORM

TypeORM에서는 데이터베이스에 새 레코드를 생성하는 대표적인 방법이 `insert`와 `save` 두 가지입니다. 두 방법 모두 _필수_ 필드가 제공되지 않으면 런타임 오류로 이어질 수 있는 데이터를 제출할 수 있습니다.

다음 예시를 살펴보세요:

save로 생성

insert로 생성

Model

```
    const userRepository = getManager().getRepository(User);
    const newUser = new User();
    newUser.name = "Alice";
    userRepository.save(newUser);
```

TypeORM에서 레코드 생성 시 `save`를 사용하든 `insert`를 사용하든, 필수 필드 값을 제공하지 않으면 다음 런타임 오류가 발생합니다:

```
    QueryFailedError: null value in column "email" of relation "user" violates not-null constraint
```

`email` 필드는 `User` 엔터티에서 필수로 정의되어 있습니다(데이터베이스의 `NOT NULL` 제약으로 강제됨).

- Prisma ORM

Prisma ORM은 모델의 _모든_ 필수 필드 값 제출을 강제하여 이런 종류의 실수를 방지합니다.

예를 들어, 아래처럼 필수 `email` 필드가 누락된 `User`를 생성하려는 시도는 TypeScript 컴파일러가 감지합니다:

create로 생성

Model

```
    const newUser = await prisma.user.create({
      data: {
        name: "Alice",
      },
    });
```

이 경우 다음 컴파일 타임 오류가 발생합니다:

```
    [ERROR] 10:39:07 ⨯ Unable to compile TypeScript:
    src/index.ts:39:5 - error TS2741: Property 'email' is missing in type '{ name: string; }' but required in type 'UserCreateInput'.
```

## API 비교

- 단일 객체 조회

**Prisma ORM**

```
    const user = await prisma.user.findUnique({
      where: {
        id: 1,
      },
    });
```

**TypeORM**

```
    const userRepository = getRepository(User);
    const user = await userRepository.findOne(id);
```

- 단일 객체에서 선택한 스칼라 값 조회

**Prisma ORM**

```
    const user = await prisma.user.findUnique({
      where: {
        id: 1,
      },
      select: {
        name: true,
      },
    });
```

**TypeORM**

```
    const userRepository = getRepository(User);
    const user = await userRepository.findOne(id, {
      select: ["id", "email"],
    });
```

- 관계 조회

**Prisma ORM**

include 사용

Fluent API

```
    const posts = await prisma.user.findUnique({
      where: {
        id: 2,
      },
      include: {
        post: true,
      },
    });
```

> **참고** : `select`는 `post` 배열을 포함한 `user` 객체를 반환하는 반면, fluent API는 `post` 배열만 반환합니다.

**TypeORM**

relations 사용

JOIN 사용

eager relations 사용

```
    const userRepository = getRepository(User);
    const user = await userRepository.findOne(id, {
      relations: ["posts"],
    });
```

- 구체적인 값으로 필터링

**Prisma ORM**

```
    const posts = await prisma.post.findMany({
      where: {
        title: {
          contains: "Hello",
        },
      },
    });
```

**TypeORM**

```
    const userRepository = getRepository(User);
    const users = await userRepository.find({
      where: {
        name: "Alice",
      },
    });
```

- 기타 필터 기준

**Prisma ORM**

Prisma ORM은 현대 애플리케이션 개발에서 일반적으로 사용되는 많은 [추가 필터](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting)를 생성합니다.

**TypeORM**

TypeORM은 더 복잡한 비교를 수행할 수 있는 [내장 연산자](https://typeorm.io/find-options#advanced-options)를 제공합니다.

- 관계 필터

**Prisma ORM**

Prisma ORM은 조회 대상 목록의 모델뿐 아니라 해당 모델의 _관계_ 에 적용되는 기준을 기반으로 목록을 필터링할 수 있게 해줍니다.

예를 들어, 다음 쿼리는 제목에 "Hello"가 포함된 게시물을 하나 이상 가진 사용자를 반환합니다:

```
    const posts = await prisma.user.findMany({
      where: {
        Post: {
          some: {
            title: {
              contains: "Hello",
            },
          },
        },
      },
    });
```

**TypeORM**

TypeORM은 관계 필터 전용 API를 제공하지 않습니다. `QueryBuilder`를 사용하거나 쿼리를 직접 작성하면 유사한 기능을 구현할 수 있습니다.

- 페이지네이션

**Prisma ORM**

Cursor 스타일 페이지네이션:

```
    const page = await prisma.post.findMany({
      before: {
        id: 242,
      },
      last: 20,
    });
```

Offset 페이지네이션:

```
    const cc = await prisma.post.findMany({
      skip: 200,
      first: 20,
    });
```

**TypeORM**

```
    const postRepository = getRepository(Post);
    const posts = await postRepository.find({
      skip: 5,
      take: 10,
    });
```

- 객체 생성

**Prisma ORM**

```
    const user = await prisma.user.create({
      data: {
        email: "alice@prisma.io",
      },
    });
```

**TypeORM**

save 사용

create 사용

insert 사용

```
    const user = new User();
    user.name = "Alice";
    user.email = "alice@prisma.io";
    await user.save();
```

- 객체 업데이트

**Prisma ORM**

```
    const user = await prisma.user.update({
      data: {
        name: "Alicia",
      },
      where: {
        id: 2,
      },
    });
```

**TypeORM**

```
    const userRepository = getRepository(User);
    const updatedUser = await userRepository.update(id, {
      name: "James",
      email: "james@prisma.io",
    });
```

- 객체 삭제

**Prisma ORM**

```
    const deletedUser = await prisma.user.delete({
      where: {
        id: 10,
      },
    });
```

**TypeORM**

delete 사용

remove 사용

```
    const userRepository = getRepository(User);
    await userRepository.delete(id);
```

- 일괄 업데이트

**Prisma ORM**

```
    const user = await prisma.user.updateMany({
      data: {
        name: "Published author!",
      },
      where: {
        Post: {
          some: {
            published: true,
          },
        },
      },
    });
```

**TypeORM**

[query builder를 사용해 데이터베이스의 엔터티를 업데이트](https://typeorm.io/update-query-builder)할 수 있습니다.

- 일괄 삭제

**Prisma ORM**

```
    const users = await prisma.user.deleteMany({
      where: {
        id: {
          in: [1, 2, 6, 6, 22, 21, 25],
        },
      },
    });
```

**TypeORM**

delete 사용

remove 사용

```
    const userRepository = getRepository(User);
    await userRepository.delete([id1, id2, id3]);
```

- 트랜잭션

**Prisma ORM**

```
    const user = await prisma.user.create({
      data: {
        email: "bob.rufus@prisma.io",
        name: "Bob Rufus",
        Post: {
          create: [{ title: "Working at Prisma" }, { title: "All about databases" }],
        },
      },
    });
```

**TypeORM**

```
    await getConnection().$transaction(async (transactionalEntityManager) => {
      const user = getRepository(User).create({
        name: "Bob",
        email: "bob@prisma.io",
      });
      const post1 = getRepository(Post).create({
        title: "Join us for GraphQL Conf in 2019",
      });
      const post2 = getRepository(Post).create({
        title: "Subscribe to GraphQL Weekly for GraphQL news",
      });
      user.posts = [post1, post2];
      await transactionalEntityManager.save(post1);
      await transactionalEntityManager.save(post2);
      await transactionalEntityManager.save(user);
    });
```
