---
title: "타입 안전성 개요"
description: "Prisma Client는 부분 쿼리나 포함된 relation에도 전체 타입 안전성을 제공합니다. 이 페이지에서는 생성된 타입과 유틸리티를 활용하는 방법을 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/type-safety

# 타입 안전성 개요

Prisma Client는 부분 쿼리나 포함된 relation에도 전체 타입 안전성을 제공합니다. 이 페이지에서는 생성된 타입과 유틸리티를 활용하는 방법을 설명합니다.

Prisma Client용으로 생성된 코드에는 애플리케이션을 더 타입 안전하게 만드는 데 사용할 수 있는 여러 유용한 타입과 유틸리티가 포함되어 있습니다. 이 페이지에서는 이를 활용하는 패턴을 설명합니다.

> **참고** : Prisma ORM의 고급 타입 안전성 주제에 관심이 있다면, 새로운 TypeScript `satisfies` 키워드로 Prisma Client 워크플로를 개선하는 방법을 다룬 이 [블로그 글](https://www.prisma.io/blog/satisfies-operator-ur8ys8ccq7zb)을 확인해 보세요.

## 생성된 타입 가져오기

`Prisma` 네임스페이스를 import하고 점 표기법으로 타입과 유틸리티에 접근할 수 있습니다. 다음 예제는 `Prisma` 네임스페이스를 import한 뒤 이를 사용해 `Prisma.UserSelect` [generated type](https://docs.prisma.io/docs/orm/prisma-client/type-safety#what-are-generated-types)에 접근하고 사용하는 방법을 보여줍니다:

```
    import { Prisma } from "../path/to/generated/prisma/client";

    // Build 'select' object
    const userEmail: Prisma.UserSelect = {
      email: true,
    };

    // Use select object
    const createUser = await prisma.user.create({
      data: {
        email: "bob@prisma.io",
      },
      select: userEmail,
    });
```

참고: [`Prisma.UserCreateInput` generated type 사용하기](https://docs.prisma.io/docs/orm/prisma-client/queries/crud#create-a-single-record)

## 생성된 타입이란?

생성된 타입은 모델에서 파생된 TypeScript 타입입니다. 이를 사용해 `prisma.user.create(...)` 또는 `prisma.user.update(...)` 같은 최상위 메서드나 `select`, `include` 같은 옵션에 전달할 typed object를 만들 수 있습니다.

예를 들어 `select`는 `UserSelect` 타입의 객체를 받습니다. 이 객체의 속성은 모델 기준으로 `select` 문에서 지원되는 항목과 일치합니다.

아래 첫 번째 탭은 `UserSelect` generated type과 객체의 각 속성에 타입 주석이 어떻게 지정되는지를 보여줍니다. 두 번째 탭은 해당 타입이 생성된 원본 스키마를 보여줍니다.

Generated type

Model

```
    type Prisma.UserSelect = {
        id?: boolean | undefined;
        email?: boolean | undefined;
        name?: boolean | undefined;
        posts?: boolean | Prisma.PostFindManyArgs | undefined;
        profile?: boolean | Prisma.ProfileArgs | undefined;
    }
```

TypeScript에서 [type annotations](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-annotations-on-variables) 개념은 변수를 선언하고 해당 변수의 타입을 설명하기 위해 타입 주석을 추가하는 것입니다. 아래 예제를 참고하세요.

```
    const myAge: number = 37;
    const myName: string = "Rich";
```

이 두 변수 선언에는 각각 어떤 원시 타입인지 지정하는 타입 주석이 부여되어 있으며, 각각 `number`, `string`입니다. 대부분의 경우 이런 주석은 필요하지 않은데, TypeScript가 초기화 방식에 따라 변수 타입을 추론하기 때문입니다. 위 예제에서 `myAge`는 숫자로 초기화되었으므로 TypeScript는 이를 숫자 타입으로 추론합니다.

다시 `UserSelect` 타입으로 돌아가서, 생성된 객체 `userEmail`에 점 표기법을 사용하면 `select` 문으로 상호작용할 수 있는 `User` 모델의 모든 필드에 접근할 수 있습니다.

```
    model User {
      id      Int      @id @default(autoincrement())
      email   String   @unique
      name    String?
      posts   Post[]
      profile Profile?
    }
```

```
    import { Prisma } from "../path/to/generated/prisma/client";

    const userEmail: Prisma.UserSelect = {
      email: true,
    };

    // properties available on the typed object
    userEmail.id;
    userEmail.email;
    userEmail.name;
    userEmail.posts;
    userEmail.profile;
```

같은 방식으로 `include` generated type으로 객체에 타입을 지정하면, `include` 문을 사용할 수 있는 해당 속성들에 접근할 수 있습니다.

```
    import { Prisma } from "../path/to/generated/prisma/client";

    const userPosts: Prisma.UserInclude = {
      posts: true,
    };

    // properties available on the typed object
    userPosts.posts;
    userPosts.profile;
```

> 사용 가능한 다양한 타입에 대한 자세한 내용은 [model query options](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#model-query-options) 레퍼런스를 참고하세요.

- Generated `UncheckedInput` types

`UncheckedInput` 타입은 Prisma Client가 "unsafe"하다고 간주하는 일부 작업(예: [relation scalar fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations) 직접 쓰기)을 수행할 수 있게 해주는 특별한 생성 타입 집합입니다. `create`, `update`, `upsert` 같은 작업을 할 때 "safe" `Input` 타입 또는 "unsafe" `UncheckedInput` 타입 중 하나를 선택할 수 있습니다.

예를 들어, 이 Prisma 스키마에는 `User`와 `Post` 사이에 one-to-many relation이 있습니다:

```
    model Post {
      id       Int     @id @default(autoincrement())
      title    String  @db.VarChar(255)
      content  String?
      author   User    @relation(fields: [authorId], references: [id])
      authorId Int
    }

    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
      posts Post[]
    }
```

첫 번째 탭은 `PostUncheckedCreateInput` generated type을 보여줍니다. 여기에는 relation scalar field인 `authorId` 속성이 포함됩니다. 두 번째 탭은 `PostUncheckedCreateInput` 타입을 사용하는 예제 쿼리를 보여줍니다. 이 쿼리는 `id`가 `1`인 사용자가 존재하지 않으면 오류가 발생합니다.

Generated type

Example query

```
    type PostUncheckedCreateInput = {
      id?: number;
      title: string;
      content?: string | null;
      authorId: number;
    };
```

같은 쿼리는 더 "safer"한 `PostCreateInput` 타입을 사용하도록 다시 작성할 수 있습니다. 이 타입에는 `authorId` 필드가 없고 대신 `author` relation 필드가 있습니다.

Generated type

Example query

```
    type PostCreateInput = {
      title: string;
      content?: string | null;
      author: UserCreateNestedOneWithoutPostsInput;
    };

    type UserCreateNestedOneWithoutPostsInput = {
      create?: XOR<UserCreateWithoutPostsInput, UserUncheckedCreateWithoutPostsInput>;
      connectOrCreate?: UserCreateOrConnectWithoutPostsInput;
      connect?: UserWhereUniqueInput;
    };
```

이 쿼리 역시 `id`가 `1`인 작성자가 존재하지 않으면 오류가 발생합니다. 이 경우 Prisma Client는 더 설명적인 오류 메시지를 제공합니다. 또한 [`connectOrCreate`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#connectorcreate) API를 사용해 주어진 `id`를 가진 사용자가 아직 없을 때 안전하게 새 사용자를 생성할 수 있습니다.

가능하면 항상 "safe" `Input` 타입을 사용하는 것을 권장합니다.

## 타입 유틸리티

고도로 타입 안전한 애플리케이션을 만들 수 있도록 Prisma Client는 input/output 타입을 활용하는 타입 유틸리티 세트를 제공합니다. 이 타입들은 완전히 동적이므로 주어진 모델과 스키마에 맞게 적응합니다. 이를 통해 프로젝트의 자동 완성과 개발자 경험을 개선할 수 있습니다.

이는 특히 [shared Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions)에서 유용합니다.

Prisma Client에서 사용 가능한 타입 유틸리티는 다음과 같습니다:

- `Exact<Input, Shape>`: `Input`에 엄격한 타입 안전성을 강제합니다. `Exact`는 제네릭 타입 `Input`이 `Shape`에서 지정한 타입을 엄격히 준수하도록 보장합니다. 또한 `Input`을 가장 정밀한 타입으로 [narrow](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)합니다.
- `Args<Type, Operation>`: 주어진 모델과 operation의 입력 인수를 가져옵니다. 이는 특히 다음을 원하는 extension 작성자에게 유용합니다:
  - 기존 타입을 재사용해 확장하거나 수정합니다.
  - 기존 operation과 동일한 자동 완성 경험을 누립니다.
- `Result<Type, Arguments, Operation>`: 입력 인수를 받아 주어진 모델과 operation의 결과를 제공합니다. 일반적으로 `Args`와 함께 사용합니다. `Args`와 마찬가지로 `Result`도 기존 타입을 재사용해 확장하거나 수정하는 데 도움이 됩니다.
- `Payload<Type, Operation>`: 주어진 모델과 operation에 대해 scalar 및 relation object를 포함한 전체 결과 구조를 가져옵니다. 예를 들어 타입 수준에서 어떤 키가 scalar인지 object인지 판단할 때 사용할 수 있습니다.

예를 들어, 함수 인수가 `post.create`에 전달할 내용과 일치하도록 강제하는 빠른 방법은 다음과 같습니다:

```
    type PostCreateBody = Prisma.Args<typeof prisma.post, "create">["data"];

    const addPost = async (postBody: PostCreateBody) => {
      const post = await prisma.post.create({ data: postBody });
      return post;
    };

    await addPost(myData);
    //              ^ guaranteed to match the input of `post.create`
```
