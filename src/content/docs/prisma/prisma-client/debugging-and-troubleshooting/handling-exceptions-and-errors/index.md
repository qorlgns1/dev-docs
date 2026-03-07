---
title: "예외 및 오류 처리"
description: "이 페이지에서는 예외와 오류를 처리하는 방법을 다룹니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/handling-exceptions-and-errors

# 예외 및 오류 처리

이 페이지에서는 예외와 오류를 처리하는 방법을 다룹니다.

서로 다른 유형의 오류를 처리하려면 `instanceof`를 사용해 오류가 무엇인지 확인하고, 그에 맞게 처리할 수 있습니다.

다음 예제는 이미 존재하는 이메일 레코드로 사용자를 생성하려고 시도합니다. `email` 필드에 `@unique` 속성이 적용되어 있으므로 오류가 발생합니다.

schema.prisma

```
    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
    }
```

오류 타입에 접근하려면 `Prisma` 네임스페이스를 사용하세요. 그런 다음 [error code](https://docs.prisma.io/docs/orm/reference/error-reference#error-codes)를 확인하고 메시지를 출력할 수 있습니다.

```
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient, Prisma } from "../generated/prisma/client";

    const connectionString = `${process.env.DATABASE_URL}`;
    const adapter = new PrismaPg({ connectionString });
    const prisma = new PrismaClient({ adapter });

    try {
      await client.user.create({ data: { email: "alreadyexisting@mail.com" } });
    } catch (e) {
      if (e instanceof Prisma.PrismaClientKnownRequestError) {
        // The .code property can be accessed in a type-safe manner
        if (e.code === "P2002") {
          console.log(
            "There is a unique constraint violation, a new user cannot be created with this email",
          );
        }
      }
      throw e;
    }
```

다양한 오류 유형과 해당 코드에 대한 자세한 설명은 [Errors reference](https://docs.prisma.io/docs/orm/reference/error-reference)를 참고하세요.
