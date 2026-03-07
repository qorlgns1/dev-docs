---
title: "API 패턴"
description: "REST API, GraphQL 서버, 그리고 풀스택 프레임워크에서 Prisma ORM을 사용하는 방법"
---

# API 패턴

REST API, GraphQL 서버, 그리고 풀스택 프레임워크에서 Prisma ORM을 사용하는 방법

Prisma Client는 모든 서버 사이드 JavaScript 또는 TypeScript 애플리케이션에서 데이터베이스를 쿼리하는 데 사용할 수 있습니다. 이 페이지에서는 REST API, GraphQL 서버, 그리고 풀스택 프레임워크를 위한 일반적인 패턴을 다룹니다.

## REST API

REST API를 구축할 때는 라우트 컨트롤러 내부에서 Prisma Client를 사용해 데이터베이스 쿼리를 실행하세요.

- 지원 프레임워크
  - Express
  - Fastify
  - hapi
  - koa
  - NestJS
  - Next.js API Routes

- 예제 라우트

```
    // GET /feed - fetch published posts
    app.get("/feed", async (req, res) => {
      const posts = await prisma.post.findMany({
        where: { published: true },
        include: { author: true },
      });
      res.json(posts);
    });

    // POST /post - create a post
    app.post("/post", async (req, res) => {
      const { title, content, authorEmail } = req.body;
      const result = await prisma.post.create({
        data: {
          title,
          content,
          author: { connect: { email: authorEmail } },
        },
      });
      res.json(result);
    });

    // PUT /publish/:id - publish a post
    app.put("/publish/:id", async (req, res) => {
      const post = await prisma.post.update({
        where: { id: Number(req.params.id) },
        data: { published: true },
      });
      res.json(post);
    });

    // DELETE /post/:id - delete a post
    app.delete("/post/:id", async (req, res) => {
      const post = await prisma.post.delete({
        where: { id: Number(req.params.id) },
      });
      res.json(post);
    });
```

## GraphQL

Prisma ORM은 어떤 GraphQL 라이브러리와도 함께 동작합니다. 리졸버 내부에서 Prisma Client를 사용해 데이터를 읽고 쓸 수 있습니다.

- 지원 도구

| 라이브러리      | 용도        |
| --------------- | ----------- |
| `graphql-yoga`  | HTTP 서버   |
| `apollo-server` | HTTP 서버   |
| `pothos`        | 스키마 빌더 |
| `nexus`         | 스키마 빌더 |
| `type-graphql`  | 스키마 빌더 |

- 프레임워크 통합
  - [Redwood.js](https://rwsdk.com/) \- Prisma ORM 기반

- Prisma의 역할

Prisma ORM은 GraphQL 리졸버 내부에서 다른 ORM을 사용하는 방식과 동일하게 사용됩니다.

- **쿼리** : 응답으로 반환할 데이터를 데이터베이스에서 읽기
- **뮤테이션** : 데이터베이스에 데이터 쓰기 (생성, 수정, 삭제)

## 풀스택 프레임워크

현대의 풀스택 프레임워크는 서버/클라이언트 경계를 흐리게 만듭니다. 애플리케이션의 서버 사이드 부분에서 Prisma Client를 사용하세요.

- 지원 프레임워크
  - Next.js
  - Remix
  - SvelteKit
  - Nuxt
  - Redwood
  - Wasp

- 지원 런타임
  - Node.js
  - Bun
  - Deno

- Next.js 예제

```
    // In getServerSideProps or API routes
    export const getServerSideProps = async () => {
      const feed = await prisma.post.findMany({
        where: { published: true },
      });
      return { props: { feed } };
    };
```

## 예제 프로젝트

[`prisma-examples`](https://github.com/prisma/prisma-examples/) 저장소에서 바로 실행 가능한 예제를 확인할 수 있습니다.

| 예제                                         | 유형    | 설명                               |
| -------------------------------------------- | ------- | ---------------------------------- |
| [Next.js](https://pris.ly/e/orm/nextjs)      | 풀스택  | Next.js 15 앱                      |
| [Express](https://pris.ly/e/ts/rest-express) | REST    | Express REST API                   |
| [Fastify](https://pris.ly/e/ts/rest-fastify) | REST    | Fastify REST API                   |
| [GraphQL Yoga](https://pris.ly/e/ts/graphql) | GraphQL | Pothos를 사용하는 GraphQL 서버     |
| [NestJS](https://pris.ly/e/ts/rest-nestjs)   | REST    | NestJS REST API                    |
| [Remix](https://pris.ly/e/ts/remix)          | 풀스택  | actions와 loaders를 사용하는 Remix |
| [SvelteKit](https://pris.ly/e/ts/sveltekit)  | 풀스택  | SvelteKit 앱                       |
