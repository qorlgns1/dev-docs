---
title: "Mongoose"
description: "Markdown 복사Markdown 열기"
---

출처 URL: https://docs.prisma.io/docs/orm/more/comparisons/prisma-and-mongoose

# Mongoose

Markdown 복사Markdown 열기

Prisma ORM이 Mongoose와 어떻게 비교되는지 알아보세요

이 페이지에서는 Prisma ORM과 [Mongoose](https://mongoosejs.com/docs/guide.html) API를 비교합니다. Mongoose에서 Prisma로 마이그레이션하는 방법을 알아보려면 이 [guide](https://docs.prisma.io/docs/guides/switch-to-prisma-orm/from-mongoose)를 확인하세요.

## 단일 객체 가져오기

**Prisma ORM**

```
    const user = await prisma.user.findUnique({
      where: {
        id: 1,
      },
    });
```

**Mongoose**

```
    const result = await User.findById(1);
```

## 단일 객체에서 선택한 스칼라 값 가져오기

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

**Mongoose**

```
    const user = await User.findById(1).select(["name"]);
```

## 관계 가져오기

**Prisma ORM**

include 사용

Fluent API

```
    const userWithPost = await prisma.user.findUnique({
      where: {
        id: 2,
      },
      include: {
        post: true,
      },
    })
```

**Mongoose**

```
    const userWithPost = await User.findById(2).populate("post");
```

## 구체적인 값으로 필터링

**Prisma ORM**

```
    const posts = await prisma.post.findMany({
      where: {
        title: {
          contains: "Hello World",
        },
      },
    });
```

**Mongoose**

```
    const posts = await Post.find({
      title: "Hello World",
    });
```

## 기타 필터 기준

**Prisma ORM**

Prisma ORM은 최신 애플리케이션 개발에서 일반적으로 사용되는 많은 [additional filters](https://docs.prisma.io/docs/v6/orm/prisma-client/queries/filtering-and-sorting)를 생성합니다.

**Mongoose**

Mongoose는 필터 기준으로 [MongoDB query selectors](https://www.mongodb.com/docs/manual/reference/mql/query-predicates/logical/)를 제공합니다.

## 관계 필터

**Prisma ORM**

Prisma ORM을 사용하면, 조회 중인 목록의 모델뿐 아니라 해당 모델의 *relation*에도 적용되는 기준을 기반으로 목록을 필터링할 수 있습니다.

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

**Mongoose**

Mongoose는 관계 필터를 위한 전용 API를 제공하지 않습니다. 쿼리 결과를 필터링하는 추가 단계를 넣어 유사한 기능을 구현할 수 있습니다.

## 페이지네이션

**Prisma ORM**

커서 스타일 페이지네이션:

```
    const page = prisma.post.findMany({
      before: {
        id: 242,
      },
      last: 20,
    });
```

오프셋 페이지네이션:

```
    const cc = prisma.post.findMany({
      skip: 200,
      first: 20,
    });
```

**Mongoose**

```
    const posts = await Post.find({
      skip: 200,
      limit: 20,
    });
```

## 객체 생성

**Prisma ORM**

```
    const user = await prisma.user.create({
      data: {
        name: "Alice",
        email: "alice@prisma.io",
      },
    });
```

**Mongoose**

create 사용

save 사용

```
    const user = await User.create({
      name: 'Alice',
      email: 'alice@prisma.io',
    })
```

## 객체 업데이트

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

**Mongoose**

findOneAndUpdate 사용

save 사용

```
    const updatedUser = await User.findOneAndUpdate(
      { _id: 2 },
      {
        $set: {
          name: 'Alicia',
        },
      }
    )
```

## 객체 삭제

**Prisma ORM**

```
    const user = prisma.user.delete({
      where: {
        id: 10,
      },
    });
```

**Mongoose**

```
    await User.deleteOne({ _id: 10 });
```

## 일괄 삭제

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

**Mongoose**

```
    await User.deleteMany({ id: { $in: [1, 2, 6, 6, 22, 21, 25] } });
```
