---
title: "Prisma (레거시)"
description: "내장된 Prisma용 Adapter를 사용해 NextAuth.js를 함께 사용할 수도 있습니다. 현재 이 기능은 코어  패키지에 포함되어 있습니다. 다른 adapter는 별도의 추가 패키지에서 설치해야 합니다."
---

Source URL: https://next-auth.js.org/v3/adapters/prisma-legacy

버전: v3

# Prisma (레거시)

내장된 [Prisma](https://www.prisma.io/docs/)용 Adapter를 사용해 NextAuth.js를 함께 사용할 수도 있습니다. 현재 이 기능은 코어 `next-auth` 패키지에 포함되어 있습니다. 다른 adapter는 별도의 추가 패키지에서 설치해야 합니다.

info

`prisma`와 `prisma-legacy` adapter가 있다는 점을 눈치채셨을 수 있습니다. 이는 역사적인 이유 때문이지만, 코드가 대부분 수렴되어 현재는 둘 사이에 큰 차이가 없습니다. 다만 legacy adapter는 테이블 이름을 변경할 수 있는 기능이 있고, 최신 버전에는 이 기능이 없습니다.

이 Adapter를 사용하려면 Prisma Client와 Prisma CLI를 설치해야 합니다:

```
    npm install @prisma/client
    npm install prisma --save-dev

```

Prisma Adapter를 사용하도록 NextAuth.js를 구성하세요:

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"
    import Adapters from "next-auth/adapters"
    import { PrismaClient } from "@prisma/client"

    const prisma = new PrismaClient()

    export default NextAuth({
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_CLIENT_ID,
          clientSecret: process.env.GOOGLE_CLIENT_SECRET,
        }),
      ],
      adapter: Adapters.Prisma.Adapter({ prisma }),
    })

```

tip

Prisma의 migration 명령에는 스키마에서 SQL을 생성할 수 있는 실험적 기능이 포함되어 있지만, 현재는 Prisma가 자동 생성한 SQL 스키마가 권장 스키마와 다를 수 있으므로 제공된 SQL을 사용해 테이블과 컬럼을 생성하는 방법을 대신 권장합니다.

Prisma Adapter용 스키마

## Setup[​](https://next-auth.js.org/v3/adapters/prisma-legacy#setup "Direct link to heading")

다음과 유사하게 `prisma/schema.prisma`에 스키마 파일을 생성하세요:

schema.prisma

```
    generator client {
      provider = "prisma-client-js"
    }

    datasource db {
      provider = "sqlite"
      url      = "file:./dev.db"
    }

    model Account {
      id                 Int       @id @default(autoincrement())
      compoundId         String    @unique @map(name: "compound_id")
      userId             Int       @map(name: "user_id")
      providerType       String    @map(name: "provider_type")
      providerId         String    @map(name: "provider_id")
      providerAccountId  String    @map(name: "provider_account_id")
      refreshToken       String?   @map(name: "refresh_token")
      accessToken        String?   @map(name: "access_token")
      accessTokenExpires DateTime? @map(name: "access_token_expires")
      createdAt          DateTime  @default(now()) @map(name: "created_at")
      updatedAt          DateTime  @default(now()) @map(name: "updated_at")

      @@index([providerAccountId], name: "providerAccountId")
      @@index([providerId], name: "providerId")
      @@index([userId], name: "userId")
      @@map(name: "accounts")
    }

    model Session {
      id           Int      @id @default(autoincrement())
      userId       Int      @map(name: "user_id")
      expires      DateTime
      sessionToken String   @unique @map(name: "session_token")
      accessToken  String   @unique @map(name: "access_token")
      createdAt    DateTime @default(now()) @map(name: "created_at")
      updatedAt    DateTime @default(now()) @map(name: "updated_at")

      @@map(name: "sessions")
    }

    model User {
      id            Int       @id @default(autoincrement())
      name          String?
      email         String?   @unique
      emailVerified DateTime? @map(name: "email_verified")
      image         String?
      createdAt     DateTime  @default(now()) @map(name: "created_at")
      updatedAt     DateTime  @default(now()) @map(name: "updated_at")

      @@map(name: "users")
    }

    model VerificationRequest {
      id         Int      @id @default(autoincrement())
      identifier String
      token      String   @unique
      expires    DateTime
      createdAt  DateTime @default(now()) @map(name: "created_at")
      updatedAt  DateTime @default(now()) @map(name: "updated_at")

      @@map(name: "verification_requests")
    }

```

### Generate Client[​](https://next-auth.js.org/v3/adapters/prisma-legacy#generate-client "Direct link to heading")

스키마를 저장한 뒤, Prisma CLI를 사용해 Prisma Client를 생성하세요:

```
    npx prisma generate

```

새 스키마를 사용하도록 데이터베이스를 구성하려면(즉, 테이블과 컬럼 생성) `prisma migrate` 명령을 사용하세요:

```
    npx prisma migrate dev

```

위 예시 코드 방식으로 스키마를 생성하려면 환경 변수 `DATABASE_URL`에 데이터베이스 연결 문자열을 지정해야 합니다. 프로젝트 루트의 `.env` 파일에 설정하면 됩니다.

이 기능은 Prisma에서 실험적 기능이므로 feature flag 뒤에 숨겨져 있습니다. 이 옵션을 사용한 뒤에는 데이터베이스 스키마를 수동으로 확인해야 합니다. `prisma migrate` 사용 방법은 [Prisma documentation](https://www.prisma.io/docs/)을 참고하세요.

tip

로컬 개발 모드에서 Prisma가 데이터베이스 연결을 너무 많이 여는 문제가 발생하면(예: Hot Module Reloading 때문), Prisma Client를 초기화할 때 다음과 같은 접근 방식을 사용할 수 있습니다:

pages/api/auth/[...nextauth].js

```
    let prisma

    if (process.env.NODE_ENV === "production") {
      prisma = new PrismaClient()
    } else {
      if (!global.prisma) {
        global.prisma = new PrismaClient()
      }
      prisma = global.prisma
    }

```

### Custom Models[​](https://next-auth.js.org/v3/adapters/prisma-legacy#custom-models "Direct link to heading")

스키마에 속성을 추가하고 원하는 데이터베이스 컬럼 이름에 매핑할 수 있지만, 예시 스키마에 정의된 기본 속성이나 타입은 변경하지 않아야 합니다.

모델 이름 자체는 구성 옵션으로 변경할 수 있으며, datasource는 Prisma가 지원하는 어떤 것이든 사용할 수 있습니다.

`modelMapping` 옵션을 사용하면 사용자 정의 모델 이름을 사용할 수 있습니다(여기서는 기본값을 보여줍니다).

pages/api/auth/[...nextauth].js

```
    ...
    adapter: Adapters.Prisma.Adapter({
      prisma,
      modelMapping: {
        User: 'user',
        Account: 'account',
        Session: 'session',
        VerificationRequest: 'verificationRequest'
      }
    })
    ...

```
