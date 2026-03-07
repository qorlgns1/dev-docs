---
title: "사용자 지정 모델 및 필드 이름"
description: "생성된 Prisma Client API의 사용성을 개선하기 위해 Prisma 모델 이름을 데이터베이스 테이블 이름과 분리하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names

# 사용자 지정 모델 및 필드 이름

생성된 Prisma Client API의 사용성을 개선하기 위해 Prisma 모델 이름을 데이터베이스 테이블 이름과 분리하는 방법을 알아보세요.

Prisma Client API는 [Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)의 모델을 기반으로 생성됩니다. 모델은 _일반적으로_ 데이터베이스 테이블과 1

매핑됩니다.

특히 [introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection)을 사용할 때는, 데이터베이스 테이블 및 컬럼의 이름을 Prisma Client API에서 사용하는 이름과 _분리_ 하는 것이 유용할 수 있습니다. 이는 Prisma schema의 [`@map` and `@@map`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#mapping-model-names-to-tables-or-collections) 속성을 통해 수행할 수 있습니다.

`@map`과 `@@map`을 사용해 각각 MongoDB 필드와 컬렉션의 이름을 변경할 수 있습니다. 이 페이지에서는 관계형 데이터베이스 예제를 사용합니다.

## 예시: 관계형 데이터베이스

다음과 유사한 PostgreSQL 관계형 데이터베이스 스키마가 있다고 가정해 보겠습니다:

```
    CREATE TABLE users (
    	user_id SERIAL PRIMARY KEY NOT NULL,
    	name VARCHAR(256),
    	email VARCHAR(256) UNIQUE NOT NULL
    );
    CREATE TABLE posts (
    	post_id SERIAL PRIMARY KEY NOT NULL,
    	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    	title VARCHAR(256) NOT NULL,
    	content TEXT,
    	author_id INTEGER REFERENCES users(user_id)
    );
    CREATE TABLE profiles (
    	profile_id SERIAL PRIMARY KEY NOT NULL,
    	bio TEXT,
    	user_id INTEGER NOT NULL UNIQUE REFERENCES users(user_id)
    );
    CREATE TABLE categories (
    	category_id SERIAL PRIMARY KEY NOT NULL,
    	name VARCHAR(256)
    );
    CREATE TABLE post_in_categories (
    	post_id INTEGER NOT NULL REFERENCES posts(post_id),
    	category_id INTEGER NOT NULL REFERENCES categories(category_id)
    );
    CREATE UNIQUE INDEX post_id_category_id_unique ON post_in_categories(post_id int4_ops,category_id int4_ops);
```

해당 스키마가 있는 데이터베이스를 introspection하면, 다음과 유사한 Prisma schema를 얻게 됩니다:

```
    model categories {
      category_id        Int                  @id @default(autoincrement())
      name               String?              @db.VarChar(256)
      post_in_categories post_in_categories[]
    }

    model post_in_categories {
      post_id     Int
      category_id Int
      categories  categories @relation(fields: [category_id], references: [category_id], onDelete: NoAction, onUpdate: NoAction)
      posts       posts      @relation(fields: [post_id], references: [post_id], onDelete: NoAction, onUpdate: NoAction)

      @@unique([post_id, category_id], map: "post_id_category_id_unique")
    }

    model posts {
      post_id            Int                  @id @default(autoincrement())
      created_at         DateTime?            @default(now()) @db.Timestamptz(6)
      title              String               @db.VarChar(256)
      content            String?
      author_id          Int?
      users              users?               @relation(fields: [author_id], references: [user_id], onDelete: NoAction, onUpdate: NoAction)
      post_in_categories post_in_categories[]
    }

    model profiles {
      profile_id Int     @id @default(autoincrement())
      bio        String?
      user_id    Int     @unique
      users      users   @relation(fields: [user_id], references: [user_id], onDelete: NoAction, onUpdate: NoAction)
    }

    model users {
      user_id  Int       @id @default(autoincrement())
      name     String?   @db.VarChar(256)
      email    String    @unique @db.VarChar(256)
      posts    posts[]
      profiles profiles?
    }
```

이 Prisma schema로 Prisma Client API를 생성하면 몇 가지 "문제"가 있습니다:

**Prisma ORM 명명 규칙 준수**

Prisma ORM은 Prisma 모델에 대해 **camelCasing**과 **단수형** 사용이라는 [명명 규칙](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#naming-conventions)을 따릅니다. 이 명명 규칙이 지켜지지 않으면 Prisma schema를 해석하기가 더 어려워지고, 생성된 Prisma Client API도 덜 자연스럽게 느껴질 수 있습니다. 다음과 같이 생성된 모델을 살펴보세요:

```
    model users {
      user_id  Int       @id @default(autoincrement())
      name     String?   @db.VarChar(256)
      email    String    @unique @db.VarChar(256)
      posts    posts[]
      profiles profiles?
    }
```

`profiles`는 1

관계를 가리키지만, 현재 타입 이름이 복수형인 `profiles`로 되어 있어 이 관계에 `profiles`가 여러 개 있을 수 있다는 인상을 줍니다. Prisma ORM 규칙에 따르면 모델과 필드 이름은 _이상적으로_ 다음과 같아야 합니다:

```
    model User {
      user_id Int      @id @default(autoincrement())
      name    String?  @db.VarChar(256)
      email   String   @unique @db.VarChar(256)
      posts   Post[]
      profile Profile?
    }
```

이 필드들은 실제로 데이터베이스에 나타나지 않는 Prisma ORM 수준의 [relation fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields)이므로, Prisma schema에서 수동으로 이름을 변경할 수 있습니다.

**어노테이션된 relation field의 이름 지정**

외래 키는 Prisma schema에서 [annotated relation fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields)와 이에 대응하는 relation scalar field의 조합으로 표현됩니다. 현재 SQL schema의 모든 relation은 다음과 같이 표현됩니다:

```
    model categories {
      category_id        Int                  @id @default(autoincrement())
      name               String?              @db.VarChar(256)
      post_in_categories post_in_categories[] // virtual relation field
    }

    model post_in_categories {
      post_id     Int // relation scalar field
      category_id Int // relation scalar field
      categories  categories @relation(fields: [category_id], references: [category_id], onDelete: NoAction, onUpdate: NoAction) // virtual relation field
      posts       posts      @relation(fields: [post_id], references: [post_id], onDelete: NoAction, onUpdate: NoAction)

      @@unique([post_id, category_id], map: "post_id_category_id_unique")
    }

    model posts {
      post_id            Int                  @id @default(autoincrement())
      created_at         DateTime?            @default(now()) @db.Timestamptz(6)
      title              String               @db.VarChar(256)
      content            String?
      author_id          Int?
      users              users?               @relation(fields: [author_id], references: [user_id], onDelete: NoAction, onUpdate: NoAction)
      post_in_categories post_in_categories[]
    }

    model profiles {
      profile_id Int     @id @default(autoincrement())
      bio        String?
      user_id    Int     @unique
      users      users   @relation(fields: [user_id], references: [user_id], onDelete: NoAction, onUpdate: NoAction)
    }

    model users {
      user_id  Int       @id @default(autoincrement())
      name     String?   @db.VarChar(256)
      email    String    @unique @db.VarChar(256)
      posts    posts[]
      profiles profiles?
    }
```

## Prisma Client API에서 @map과 @@map을 사용해 필드와 모델 이름 바꾸기

`@map`과 `@@map` 속성을 사용해 데이터베이스의 "원래" 이름에 매핑함으로써, Prisma Client에서 사용되는 필드와 모델 이름을 "변경"할 수 있습니다. 위 예시의 경우, 예를 들어 모델에 다음과 같이 어노테이션할 수 있습니다.

`prisma db pull`로 데이터베이스를 introspection한 _후_, 결과로 생성된 Prisma schema를 다음과 같이 수동 조정할 수 있습니다:

```
    model Category {
      id                 Int                @id @default(autoincrement()) @map("category_id")
      name               String?            @db.VarChar(256)
      post_in_categories PostInCategories[]

      @@map("categories")
    }

    model PostInCategories {
      post_id     Int
      category_id Int
      categories  Category @relation(fields: [category_id], references: [id], onDelete: NoAction, onUpdate: NoAction)
      posts       Post     @relation(fields: [post_id], references: [id], onDelete: NoAction, onUpdate: NoAction)

      @@unique([post_id, category_id], map: "post_id_category_id_unique")
      @@map("post_in_categories")
    }

    model Post {
      id                 Int                @id @default(autoincrement()) @map("post_id")
      created_at         DateTime?          @default(now()) @db.Timestamptz(6)
      title              String             @db.VarChar(256)
      content            String?
      author_id          Int?
      users              User?              @relation(fields: [author_id], references: [id], onDelete: NoAction, onUpdate: NoAction)
      post_in_categories PostInCategories[]

      @@map("posts")
    }

    model Profile {
      id      Int     @id @default(autoincrement()) @map("profile_id")
      bio     String?
      user_id Int     @unique
      users   User    @relation(fields: [user_id], references: [id], onDelete: NoAction, onUpdate: NoAction)

      @@map("profiles")
    }

    model User {
      id       Int      @id @default(autoincrement()) @map("user_id")
      name     String?  @db.VarChar(256)
      email    String   @unique @db.VarChar(256)
      posts    Post[]
      profiles Profile?

      @@map("users")
    }
```

이 변경을 통해 Prisma ORM 명명 규칙을 따르게 되며, 생성된 Prisma Client API도 더 "자연스럽게" 느껴집니다:

```
    // Nested writes
    const profile = await prisma.profile.create({
      data: {
        bio: "Hello World",
        users: {
          create: {
            name: "Alice",
            email: "alice@prisma.io",
          },
        },
      },
    });

    // Fluent API
    const userByProfile = await prisma.profile
      .findUnique({
        where: { id: 1 },
      })
      .users();
```

`prisma db pull`은 데이터베이스를 다시 introspection할 때, Prisma schema에서 `@map`과 `@@map`으로 정의한 사용자 지정 이름을 유지합니다.

## relation field 이름 변경

Prisma ORM 수준의 [relation fields](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations#relation-fields)(때로는 "virtual relation fields"라고도 함)는 Prisma schema에만 존재하며, 실제 기반 데이터베이스에는 나타나지 않습니다. 따라서 이 필드들의 이름은 원하는 대로 지정할 수 있습니다.

SQL 데이터베이스에서의 모호한 relation 예시를 살펴보겠습니다:

```
    CREATE TABLE "User" (
        id SERIAL PRIMARY KEY
    );
    CREATE TABLE "Post" (
        id SERIAL PRIMARY KEY,
        "author" integer NOT NULL,
        "favoritedBy" INTEGER,
        FOREIGN KEY ("author") REFERENCES "User"(id),
        FOREIGN KEY ("favoritedBy") REFERENCES "User"(id)
    );
```

Prisma ORM의 introspection은 다음 Prisma schema를 출력합니다:

```
    model Post {
      id                          Int   @id @default(autoincrement())
      author                      Int
      favoritedBy                 Int?
      User_Post_authorToUser      User  @relation("Post_authorToUser", fields: [author], references: [id], onDelete: NoAction, onUpdate: NoAction)
      User_Post_favoritedByToUser User? @relation("Post_favoritedByToUser", fields: [favoritedBy], references: [id], onDelete: NoAction, onUpdate: NoAction)
    }

    model User {
      id                          Int    @id @default(autoincrement())
      Post_Post_authorToUser      Post[] @relation("Post_authorToUser")
      Post_Post_favoritedByToUser Post[] @relation("Post_favoritedByToUser")
    }
```

virtual relation field인 `Post_Post_authorToUser`와 `Post_Post_favoritedByToUser`의 이름은 생성된 relation 이름을 기반으로 하기 때문에, Prisma Client API에서 그다지 친숙해 보이지 않습니다. 이런 경우 relation field의 이름을 바꿀 수 있습니다. 예를 들면:

```
    model Post {
      id                          Int   @id @default(autoincrement())
      author                      Int
      favoritedBy                 Int?
      User_Post_authorToUser      User  @relation("Post_authorToUser", fields: [author], references: [id], onDelete: NoAction, onUpdate: NoAction)
      User_Post_favoritedByToUser User? @relation("Post_favoritedByToUser", fields: [favoritedBy], references: [id], onDelete: NoAction, onUpdate: NoAction)
    }

    model User {
      id             Int    @id @default(autoincrement())
      //edit-start
      writtenPosts   Post[] @relation("Post_authorToUser")
      favoritedPosts Post[] @relation("Post_favoritedByToUser")
      //edit-end
    }
```

`prisma db pull`은 데이터베이스를 다시 introspection할 때, Prisma schema에 정의된 사용자 지정 relation field를 유지합니다.
