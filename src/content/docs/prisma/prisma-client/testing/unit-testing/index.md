---
title: "단위 테스트"
description: "Prisma Client로 단위 테스트를 설정하고 실행하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/testing/unit-testing

# 단위 테스트

Prisma Client로 단위 테스트를 설정하고 실행하는 방법을 알아보세요.

단위 테스트는 코드의 작은 부분(단위)을 분리하여 논리적으로 예측 가능한 동작을 테스트하는 것을 목표로 합니다. 일반적으로 실제 환경의 동작을 시뮬레이션하기 위해 객체나 서버 응답을 모킹합니다. 단위 테스트의 이점은 다음과 같습니다.

- 코드에서 버그를 빠르게 찾아 분리할 수 있습니다.
- 특정 코드 블록이 무엇을 해야 하는지 보여주는 방식으로 각 코드 모듈에 대한 문서를 제공합니다.
- 리팩터링이 잘 되었는지 판단하는 데 유용한 지표가 됩니다. 코드가 리팩터링된 후에도 테스트는 계속 통과해야 합니다.

Prisma ORM의 맥락에서는 일반적으로 Prisma Client를 사용해 데이터베이스 호출을 수행하는 함수를 테스트하는 것을 의미합니다.

단일 테스트는 함수 로직이 서로 다른 입력(예: null 값 또는 빈 리스트)을 어떻게 처리하는지에 집중해야 합니다.

즉, 테스트와 테스트 환경을 최대한 가볍게 유지하기 위해 외부 서비스 및 데이터베이스 같은 의존성을 가능한 한 많이 제거하는 것을 목표로 해야 합니다.

> **참고** : 이 [블로그 게시물](https://www.prisma.io/blog/testing-series-2-xPhjjmIEsM)은 Prisma ORM과 함께 Express 프로젝트에 단위 테스트를 구현하는 종합 가이드를 제공합니다. 이 주제를 더 깊이 다루고 싶다면 꼭 읽어보세요!

## 사전 준비

이 가이드는 프로젝트에 JavaScript 테스트 라이브러리 [`Jest`](https://jestjs.io/)와 [`ts-jest`](https://github.com/kulshekhar/ts-jest)가 이미 설정되어 있다고 가정합니다.

## Prisma Client 모킹

단위 테스트가 외부 요인으로부터 분리되도록 Prisma Client를 모킹할 수 있습니다. 이는 테스트 실행 시 데이터베이스에 실제 호출을 하지 않으면서도 스키마(**_타입 안정성_**)를 활용할 수 있다는 의미입니다.

이 가이드에서는 Prisma Client를 모킹하는 두 가지 접근 방식, 즉 싱글톤 인스턴스와 의존성 주입을 다룹니다. 둘 다 사용 사례에 따라 장점이 있습니다. Prisma Client 모킹을 돕기 위해 [`jest-mock-extended`](https://github.com/marchaos/jest-mock-extended) 패키지를 사용합니다.

npm

pnpm

yarn

bun

```
    npm install jest-mock-extended@2.0.4 --save-dev
```

이 가이드를 작성하는 시점 기준으로 `jest-mock-extended` 버전 `^2.0.4`를 사용합니다.

- 싱글톤

다음 단계는 싱글톤 패턴을 사용해 Prisma Client를 모킹하는 방법을 안내합니다.

1. 프로젝트 루트에 `client.ts` 파일을 만들고 다음 코드를 추가합니다. 이렇게 하면 Prisma Client 인스턴스가 생성됩니다.

client.ts

```
import "dotenv/config";
         import { PrismaPg } from "@prisma/adapter-pg";
         import { PrismaClient } from "../generated/prisma/client";

         const connectionString = `${process.env.DATABASE_URL}`;

         const adapter = new PrismaPg({ connectionString });
         const prisma = new PrismaClient({ adapter });

         export { prisma };
```

2. 다음으로 프로젝트 루트에 `singleton.ts`라는 파일을 만들고 다음 내용을 추가합니다.

singleton.ts

```
import { PrismaClient } from "../generated/prisma/client";
         import { mockDeep, mockReset, DeepMockProxy } from "jest-mock-extended";

         import prisma from "./client";

         jest.mock("./client", () => ({
           __esModule: true,
           default: mockDeep<PrismaClient>(),
         }));

         beforeEach(() => {
           mockReset(prismaMock);
         });

         export const prismaMock = prisma as unknown as DeepMockProxy<PrismaClient>;
```

singleton 파일은 Jest에게 기본 export(`./client.ts`의 Prisma Client 인스턴스)를 모킹하도록 지시하며, `jest-mock-extended`의 `mockDeep` 메서드를 사용해 Prisma Client에서 사용할 수 있는 객체와 메서드에 접근할 수 있게 합니다. 그런 다음 각 테스트 실행 전에 모킹된 인스턴스를 재설정합니다.

다음으로 `jest.config.js` 파일에 `setupFilesAfterEnv` 속성을 추가하고, `singleton.ts` 파일 경로를 지정합니다.

jest.config.js

```
    module.exports = {
      clearMocks: true,
      preset: "ts-jest",
      testEnvironment: "node",
      setupFilesAfterEnv: ["<rootDir>/singleton.ts"], {/* [!code ++] */}
    };
```

- 의존성 주입

사용할 수 있는 또 다른 인기 패턴은 의존성 주입입니다.

1. `context.ts` 파일을 만들고 다음 내용을 추가합니다.

context.ts

```
import { PrismaClient } from "../generated/prisma/client";
         import { mockDeep, DeepMockProxy } from "jest-mock-extended";

         export type Context = {
           prisma: PrismaClient;
         };

         export type MockContext = {
           prisma: DeepMockProxy<PrismaClient>;
         };

         export const createMockContext = (): MockContext => {
           return {
             prisma: mockDeep<PrismaClient>(),
           };
         };
```

Prisma Client 모킹 중 순환 의존성 오류가 표시된다면, `tsconfig.json`에 `"strictNullChecks": true`를 추가해 보세요.

2. 컨텍스트를 사용하려면 테스트 파일에서 다음과 같이 작성합니다.

```
import { MockContext, Context, createMockContext } from "../context";

         let mockCtx: MockContext;
         let ctx: Context;

         beforeEach(() => {
           mockCtx = createMockContext();
           ctx = mockCtx as unknown as Context;
         });
```

이렇게 하면 `createMockContext` 함수를 통해 각 테스트 실행 전에 새로운 컨텍스트가 생성됩니다. 이 (`mockCtx`) 컨텍스트는 Prisma Client에 대한 모킹 호출을 수행하고 테스트할 쿼리를 실행하는 데 사용됩니다. `ctx` 컨텍스트는 테스트 대상이 되는 시나리오 쿼리를 실행하는 데 사용됩니다.

## 단위 테스트 예제

Prisma ORM 단위 테스트의 실제 사용 사례로는 회원가입 폼이 있을 수 있습니다. 사용자가 폼을 작성하면 함수가 호출되고, 이 함수는 다시 Prisma Client를 사용해 데이터베이스를 호출합니다.

아래의 모든 예제는 다음 스키마 모델을 사용합니다.

schema.prisma

```
    model User {
      id                       Int     @id @default(autoincrement())
      email                    String  @unique
      name                     String?
      acceptTermsAndConditions Boolean
    }
```

다음 단위 테스트에서는 아래 과정을 모킹합니다.

- 새 사용자 생성
- 사용자 이름 업데이트
- 약관에 동의하지 않은 경우 사용자 생성 실패

의존성 주입 패턴을 사용하는 함수는 컨텍스트를 주입받아(파라미터로 전달받아) 사용하고, 싱글톤 패턴을 사용하는 함수는 Prisma Client의 싱글톤 인스턴스를 사용합니다.

functions-with-context.ts

```
    import { Context } from "./context";

    interface CreateUser {
      name: string;
      email: string;
      acceptTermsAndConditions: boolean;
    }

    export async function createUser(user: CreateUser, ctx: Context) {
      if (user.acceptTermsAndConditions) {
        return await ctx.prisma.user.create({
          data: user,
        });
      } else {
        return new Error("User must accept terms!");
      }
    }

    interface UpdateUser {
      id: number;
      name: string;
      email: string;
    }

    export async function updateUsername(user: UpdateUser, ctx: Context) {
      return await ctx.prisma.user.update({
        where: { id: user.id },
        data: user,
      });
    }
```

functions-without-context.ts

```
    import prisma from "./client";

    interface CreateUser {
      name: string;
      email: string;
      acceptTermsAndConditions: boolean;
    }

    export async function createUser(user: CreateUser) {
      if (user.acceptTermsAndConditions) {
        return await prisma.user.create({
          data: user,
        });
      } else {
        return new Error("User must accept terms!");
      }
    }

    interface UpdateUser {
      id: number;
      name: string;
      email: string;
    }

    export async function updateUsername(user: UpdateUser) {
      return await prisma.user.update({
        where: { id: user.id },
        data: user,
      });
    }
```

각 방법론의 테스트는 꽤 유사하며, 차이점은 모킹된 Prisma Client를 사용하는 방식입니다.

**_의존성 주입_** 예제는 테스트 대상 함수에 컨텍스트를 전달하는 동시에, 모킹 구현을 호출할 때도 해당 컨텍스트를 사용합니다.

**_싱글톤_** 예제는 싱글톤 클라이언트 인스턴스를 사용해 모킹 구현을 호출합니다.

**tests**/with-singleton.ts

```
    import { createUser, updateUsername } from "../functions-without-context";
    import { prismaMock } from "../singleton";

    test("should create new user ", async () => {
      const user = {
        id: 1,
        name: "Rich",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      };

      prismaMock.user.create.mockResolvedValue(user);

      await expect(createUser(user)).resolves.toEqual({
        id: 1,
        name: "Rich",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      });
    });

    test("should update a users name ", async () => {
      const user = {
        id: 1,
        name: "Rich Haines",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      };

      prismaMock.user.update.mockResolvedValue(user);

      await expect(updateUsername(user)).resolves.toEqual({
        id: 1,
        name: "Rich Haines",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      });
    });

    test("should fail if user does not accept terms", async () => {
      const user = {
        id: 1,
        name: "Rich Haines",
        email: "hello@prisma.io",
        acceptTermsAndConditions: false,
      };

      prismaMock.user.create.mockImplementation();

      await expect(createUser(user)).resolves.toEqual(new Error("User must accept terms!"));
    });
```

**tests**/with-dependency-injection.ts

```
    import { MockContext, Context, createMockContext } from "../context";
    import { createUser, updateUsername } from "../functions-with-context";

    let mockCtx: MockContext;
    let ctx: Context;

    beforeEach(() => {
      mockCtx = createMockContext();
      ctx = mockCtx as unknown as Context;
    });

    test("should create new user ", async () => {
      const user = {
        id: 1,
        name: "Rich",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      };
      mockCtx.prisma.user.create.mockResolvedValue(user);

      await expect(createUser(user, ctx)).resolves.toEqual({
        id: 1,
        name: "Rich",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      });
    });

    test("should update a users name ", async () => {
      const user = {
        id: 1,
        name: "Rich Haines",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      };
      mockCtx.prisma.user.update.mockResolvedValue(user);

      await expect(updateUsername(user, ctx)).resolves.toEqual({
        id: 1,
        name: "Rich Haines",
        email: "hello@prisma.io",
        acceptTermsAndConditions: true,
      });
    });

    test("should fail if user does not accept terms", async () => {
      const user = {
        id: 1,
        name: "Rich Haines",
        email: "hello@prisma.io",
        acceptTermsAndConditions: false,
      };

      mockCtx.prisma.user.create.mockImplementation();

      await expect(createUser(user, ctx)).resolves.toEqual(new Error("User must accept terms!"));
    });
```
