---
title: "GraphQL 자동완성"
description: "일반 JavaScript 환경의 GraphQL resolver에서 Prisma Client 쿼리 자동완성을 사용하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/more/troubleshooting/graphql-autocompletion

# GraphQL 자동완성

일반 JavaScript 환경의 GraphQL resolver에서 Prisma Client 쿼리 자동완성을 사용하는 방법

TypeScript와 함께 GraphQL을 사용할 때는 `context` 객체에 타입을 지정할 수 있으므로 GraphQL resolver에서 Prisma Client 인스턴스에 대한 자동완성이 제공됩니다. 일반 JavaScript에서는 이를 위해 약간의 추가 작업이 필요합니다.

## 문제

다음과 같은 resolver가 있을 때:

```
    filterPosts: (parent, args, ctx) => {
      return ctx.prisma.post.findMany({
        where: {
          OR: [
            { title: { contains: args.searchString } },
            { content: { contains: args.searchString } },
          ],
        },
      });
    };
```

VS Code는 `context` 객체의 타입을 알 수 없기 때문에 intellisense를 제공할 수 없습니다.

## 해결 방법

올바른 타입을 "import"하기 위해 `typedef`라는 이름의 [JSDoc](https://jsdoc.app/) 주석을 추가합니다:

```
    // Add this to the top of the file
    /**
     * @typedef { import("../prisma/generated/client").PrismaClient } Prisma
     */
```

그런 다음 resolver 인자에 타입을 지정합니다:

```
    /**
     * @param {any} parent
     * @param {{ searchString: string }} args
     * @param {{ prisma: Prisma }} ctx
     */
    filterPosts: (parent, args, ctx) => {
      return ctx.prisma.post.findMany({
        where: {
          OR: [
            { title: { contains: args.searchString } },
            { content: { contains: args.searchString } },
          ],
        },
      });
    };
```

이렇게 하면 VS Code에 `context`가 `Prisma` 타입의 `prisma`라는 속성을 가진다는 것을 알려주어 자동완성이 활성화됩니다.

## 완전한 예시

```
    /**
     * @typedef { import("../prisma/generated/client").PrismaClient } Prisma
     * @typedef { import("../prisma/generated/client").UserCreateArgs } UserCreateArgs
     */

    const { makeExecutableSchema } = require("graphql-tools");

    const resolvers = {
      Query: {
        /**
         * @param {any} parent
         * @param {any} args
         * @param {{ prisma: Prisma }} ctx
         */
        feed: (parent, args, ctx) => {
          return ctx.prisma.post.findMany({
            where: { published: true },
          });
        },
        /**
         * @param {any} parent
         * @param {{ searchString: string }} args
         * @param {{ prisma: Prisma }} ctx
         */
        filterPosts: (parent, args, ctx) => {
          return ctx.prisma.post.findMany({
            where: {
              OR: [
                { title: { contains: args.searchString } },
                { content: { contains: args.searchString } },
              ],
            },
          });
        },
      },
    };
```
