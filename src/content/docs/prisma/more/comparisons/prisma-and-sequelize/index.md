---
title: "Sequelize"
description: "Prisma ORM이 Sequelize와 어떻게 비교되는지 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/more/comparisons/prisma-and-sequelize

# Sequelize

Prisma ORM이 Sequelize와 어떻게 비교되는지 알아보세요

이 페이지에서는 Prisma ORM과 [Sequelize](https://sequelize.org/docs/v6/) API를 비교합니다.

## Sequelize vs Prisma ORM

Prisma ORM과 Sequelize는 비슷한 문제를 해결하지만, 작동 방식은 매우 다릅니다.

**Sequelize**는 *테이블*을 *모델 클래스*에 매핑하는 전통적인 ORM입니다. 이후 모델 클래스의 인스턴스가 런타임에서 애플리케이션에 CRUD 쿼리 인터페이스를 제공합니다.

**Prisma ORM**은 bloated model instances, 비즈니스 로직과 저장소 로직의 혼합, type-safety 부족, lazy loading 등으로 인해 발생하는 예측 불가능한 쿼리 같은 전통적 ORM의 많은 문제를 완화하는 새로운 종류의 ORM입니다.

[Prisma schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)를 사용해 선언적으로 애플리케이션 모델을 정의합니다. 그런 다음 Prisma Migrate가 Prisma schema로부터 SQL 마이그레이션을 생성하고 데이터베이스에 실행할 수 있게 해줍니다. CRUD 쿼리는 Node.js와 TypeScript를 위한 가볍고 완전한 type-safe 데이터베이스 클라이언트인 Prisma Client에서 제공합니다.

## API comparison

- 단일 객체 조회

**Prisma ORM**

```
    const user = await prisma.user.findUnique({
      where: {
        id: 1,
      },
    });
```

**Sequelize**

```
    const user = await User.findByPk(id);
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

**Sequelize**

```
    const user = await User.findByPk(1, { attributes: ["name"], raw: true });
```

일반 JavaScript 객체를 반환하려면 `raw: true` 쿼리 옵션을 사용하세요.

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

**Sequelize**

```
    const user = await User.findByPk(id, {
      include: [
        {
          model: Post,
        },
      ],
    });
```

`User`와 `Post` 사이의 관계를 정의할 때 별칭을 사용했다면 `model: Post as "Post"`를 사용하세요 \- 예: `User.hasMany(Post, { as: "Post", foreignKey: "authorId" });`

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

**Sequelize**

```
    const post = await Post.findAll({
      raw: true,
      where: {
        title: {
          [Op.like]: "%Hello%",
        },
      },
    });
```

- 기타 필터 기준

**Prisma ORM**

Prisma ORM은 현대 애플리케이션 개발에서 일반적으로 사용되는 많은 [추가 필터](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting)를 생성합니다.

**Sequelize**

Sequelize는 [광범위한 연산자 세트](https://sequelize.org/docs/v6/core-concepts/model-querying-basics/#operators)를 제공합니다.

- 관계 필터

**Prisma ORM**

Prisma ORM을 사용하면 조회 중인 목록의 모델뿐 아니라 해당 모델의 *관계*에도 적용되는 기준으로 목록을 필터링할 수 있습니다.

예를 들어, 다음 쿼리는 제목에 "Hello"가 포함된 게시물이 하나 이상 있는 사용자를 반환합니다:

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

**Sequelize**

Sequelize는 [관계 필터를 위한 전용 API를 제공하지 않습니다](https://github.com/sequelize/sequelize/issues/10943). 데이터베이스에 raw SQL 쿼리를 보내 유사한 기능을 구현할 수 있습니다.

- 페이지네이션

**Prisma ORM**

커서 스타일 페이지네이션:

```
    const page = await prisma.post.findMany({
      before: {
        id: 242,
      },
      last: 20,
    });
```

오프셋 페이지네이션:

```
    const cc = await prisma.post.findMany({
      skip: 200,
      first: 20,
    });
```

**Sequelize**

커서 페이지네이션:

```
    const posts = await Post.findAll({
      limit: 20,
      where: {
        id: {
          [Op.gt]: 242,
        },
      },
    });
```

> **참고** : Sequelize는 커서 페이지네이션을 수행하기 위해 [Sequelize operators](https://sequelize.org/docs/v6/core-concepts/model-querying-basics/#operators)를 사용합니다.

오프셋 페이지네이션:

```
    const posts = await Post.findAll({
      offset: 5,
      limit: 10,
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

**Sequelize**

save 사용

create 사용

```
    const user = User.build({
      name: 'Alice',
      email: 'alice@prisma,io',
    })
    await user.save()
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

**Sequelize**

save 사용

update 사용

```
    user.name = 'James'
    user.email = ' alice@prisma.com'
    await user.save()
```

- 객체 삭제

**Prisma ORM**

```
    const user = await prisma.user.delete({
      where: {
        id: 10,
      },
    });
```

**Sequelize**

```
    await user.destroy();
```

- 배치 업데이트

**Prisma ORM**

```
    const user = await prisma.user.updateMany({
      data: {
        name: "Published author!",
      },
      where: {
        email: {
          contains: "prisma.io",
        },
      },
    });
```

**Sequelize**

```
    const updatedUsers = await User.update({
      { role: "Admin" },
      where: {
        email: {
          [Op.like]: "%@prisma.io"
        }
      },
    })
```

- 배치 삭제

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

**Sequelize**

```
    await User.destroy({
      where: {
        id: {
          [Op.in]: [id1, id2, id3],
        },
      },
    });
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

**Sequelize**

수동

자동

```
    return sequelize.$transaction(async (t) => {
      const user = await User.create(
        {
          name: 'Alice',
          email: 'alice@prisma,io',
        },
        {
          transaction: t,
        }
      )
      const post1 = await Post.create(
        {
          title: 'Join us for GraphQL Conf in 2019',
        },
        {
          transaction: t,
        }
      )
      const post2 = await Post.create(
        {
          title: 'Subscribe to GraphQL Weekly for GraphQL news',
        },
        {
          transaction: t,
        }
      )
      await user.setPosts([post1, post2])
    })
```
