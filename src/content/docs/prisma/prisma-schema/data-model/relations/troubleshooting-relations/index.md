---
title: "관계 문제 해결"
description: "스키마를 모델링하다 보면 때때로 예상치 못한 결과가 나올 수 있습니다. 이 섹션에서는 그중 가장 대표적인 사례를 다룹니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/troubleshooting-relations

# 관계 문제 해결

스키마를 모델링하다 보면 때때로 예상치 못한 결과가 나올 수 있습니다. 이 섹션에서는 그중 가장 대표적인 사례를 다룹니다.

## 관계 필드 순서가 바뀌면 암시적 다대다 self-relation이 잘못된 데이터를 반환함

- 문제

다음 암시적 다대다 self-relation에서 `a_eats` (1)와 `b_eatenBy` (2)의 관계 필드 사전식 순서는 다음과 같습니다:

```
    model Animal {
      id        Int      @id @default(autoincrement())
      name      String
      a_eats    Animal[] @relation(name: "FoodChain")
      b_eatenBy Animal[] @relation(name: "FoodChain")
    }
```

그 결과 생성되는 SQL의 relation table은 아래와 같으며, 여기서 `A`는 먹이(`a_eats`), `B`는 포식자(`b_eatenBy`)를 나타냅니다:

| A            | B          |
| ------------ | ---------- |
| 8 (Plankton) | 7 (Salmon) |
| 7 (Salmon)   | 9 (Bear)   |

다음 쿼리는 salmon의 먹이와 포식자를 반환합니다:

```
    const getAnimals = await prisma.animal.findMany({
      where: {
        name: "Salmon",
      },
      include: {
        b_eats: true,
        a_eatenBy: true,
      },
    });
```

```
    {
      "id": 7,
      "name": "Salmon",
      "b_eats": [
        {
          "id": 8,
          "name": "Plankton"
        }
      ],
      "a_eatenBy": [
        {
          "id": 9,
          "name": "Bear"
        }
      ]
    }
```

이제 relation field의 순서를 변경해 보겠습니다:

```
    model Animal {
      id        Int      @id @default(autoincrement())
      name      String
      b_eats    Animal[] @relation(name: "FoodChain")
      a_eatenBy Animal[] @relation(name: "FoodChain")
    }
```

변경 사항을 마이그레이션하고 Prisma Client를 다시 생성하세요. 업데이트된 필드 이름으로 동일한 쿼리를 실행하면 Prisma Client가 잘못된 데이터를 반환합니다(salmon이 이제 bear를 먹고 plankton에게 먹힙니다):

```
    const getAnimals = await prisma.animal.findMany({
      where: {
        name: "Salmon",
      },
      include: {
        b_eats: true,
        a_eatenBy: true,
      },
    });
```

```
    {
      "id": 1,
      "name": "Salmon",
      "b_eats": [
        {
          "id": 3,
          "name": "Bear"
        }
      ],
      "a_eatenBy": [
        {
          "id": 2,
          "name": "Plankton"
        }
      ]
    }
```

Prisma schema에서 relation field의 사전식 순서는 바뀌었지만, 데이터베이스의 `A`와 `B` 컬럼은 **바뀌지 않았습니다**(이름이 변경되지 않았고 데이터도 이동되지 않았습니다). 따라서 이제 `A`는 포식자(`a_eatenBy`), `B`는 먹이(`b_eats`)를 나타냅니다:

| A            | B          |
| ------------ | ---------- |
| 8 (Plankton) | 7 (Salmon) |
| 7 (Salmon)   | 9 (Bear)   |

- 해결 방법

암시적 다대다 self-relation에서 relation field의 이름을 바꿀 때는 필드의 알파벳 순서를 유지해야 합니다. 예를 들어 `a_`, `b_` 접두사를 사용하세요.

## 다대다 관계에서 relation table 사용하는 방법

m-n 관계를 정의하는 방법은 암시적 방식과 명시적 방식 두 가지가 있습니다. 암시적 방식은 Prisma ORM이 내부적으로 relation table(JOIN table)을 처리하도록 두는 것이며, 각 모델에서 non scalar type에 대해 배열/리스트만 정의하면 됩니다. 자세한 내용은 [implicit many-to-many relations](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#implicit-many-to-many-relations)를 참고하세요.

문제가 생기기 쉬운 지점은 [explicit m-n relationship](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#explicit-many-to-many-relations)을 만들 때, 즉 relation table을 직접 생성하고 관리할 때입니다. **Prisma ORM은 관계의 양쪽이 모두 존재해야 한다는 점을 놓치기 쉽습니다**.

다음 예제를 보세요. 여기서는 `Post`와 `Category` 테이블 사이의 JOIN 역할을 하도록 relation table을 생성합니다. 하지만 이 방식은 동작하지 않습니다. relation table(`PostCategories`)은 각각 다른 두 모델과 1대다 관계를 형성해야 하기 때문입니다.

`Post`에서 `PostCategories`로, 그리고 `Category`에서 `PostCategories`로의 역방향 relation field가 누락되어 있습니다.

```
    // This example schema shows how NOT to define an explicit m-n relation

    model Post {
      id             Int              @id @default(autoincrement())
      title          String
      categories     Category[] // This should refer to PostCategories
    }

    model PostCategories {
      post       Post     @relation(fields: [postId], references: [id])
      postId     Int
      category   Category @relation(fields: [categoryId], references: [id])
      categoryId Int
      @@id([postId, categoryId])
    }

    model Category {
      id             Int              @id @default(autoincrement())
      name           String
      posts          Post[] // This should refer to PostCategories
    }
```

이를 수정하려면 `Post` 모델에 relation table `PostCategories`와의 다중 relation field를 정의해야 합니다. `Category` 모델도 동일합니다.

이는 relation model이 자신이 연결하는 다른 두 모델과 1대다 관계를 형성하기 때문입니다.

```
    model Post {
      id             Int              @id @default(autoincrement())
      title          String
      categories     Category[]
      postCategories PostCategories[]
    }

    model PostCategories {
      post       Post     @relation(fields: [postId], references: [id])
      postId     Int
      category   Category @relation(fields: [categoryId], references: [id])
      categoryId Int

      @@id([postId, categoryId])
    }

    model Category {
      id             Int              @id @default(autoincrement())
      name           String
      posts          Post[]
      postCategories PostCategories[]
    }
```

## 다대다 관계에서 `@relation` 속성 사용하기

암시적 다대다 관계를 구성할 때 모델의 relation field에 `@relation("Post")` 어노테이션을 추가하는 것이 논리적으로 보일 수 있습니다.

```
    model Post {
      id         Int        @id @default(autoincrement())
      title      String
      categories Category[] @relation("Category")
      Category   Category?  @relation("Post", fields: [categoryId], references: [id])
      categoryId Int?
    }

    model Category {
      id     Int    @id @default(autoincrement())
      name   String
      posts  Post[] @relation("Post")
      Post   Post?  @relation("Category", fields: [postId], references: [id])
      postId Int?
    }
```

하지만 이렇게 하면 Prisma ORM은 별개의 1대다 관계가 **두 개** 있다고 기대하게 됩니다. `@relation` 속성 사용에 대한 자세한 내용은 [disambiguating relations](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#disambiguating-relations)를 참고하세요.

다음 예제는 암시적 다대다 관계를 정의하는 올바른 방법입니다.

```
    model Post {
      id         Int        @id @default(autoincrement())
      title      String
      categories Category[] @relation("Category")
      categories Category[]
    }

    model Category {
      id    Int    @id @default(autoincrement())
      name  String
      posts Post[] @relation("Post")
      posts Post[]
    }
```

`@relation` 어노테이션은 암시적 다대다 관계에서 생성되는 [기본 relation table의 이름 지정](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#configuring-relation-table-name)에도 사용할 수 있습니다.

```
    model Post {
      id         Int        @id @default(autoincrement())
      title      String
      categories Category[] @relation("CategoryPostRelation")
    }

    model Category {
      id    Int    @id @default(autoincrement())
      name  String
      posts Post[] @relation("CategoryPostRelation")
    }
```

## 기본 키 강제가 있는 데이터베이스에서 m-n 관계 사용하기

- 문제

일부 클라우드 제공자는 모든 테이블에 기본 키가 존재하도록 강제합니다. 하지만 암시적 문법을 사용한 다대다 관계에서 Prisma ORM이(`@relation`을 통해) 생성하는 relation table(JOIN table)에는 기본 키가 없습니다.

- 해결 방법

[명시적 relation 문법](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/many-to-many-relations#explicit-many-to-many-relations)을 사용해 join model을 수동으로 만들고, 이 join model에 기본 키가 있는지 확인해야 합니다.
