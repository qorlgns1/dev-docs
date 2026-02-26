---
title: "Prisma"
description: "원본 URL: https://next-auth.js.org/v3/adapters/prisma"
---

원본 URL: https://next-auth.js.org/v3/adapters/prisma

버전: v3

# Prisma

새로운 실험적 [Prisma](https://www.prisma.io/docs/)용 Adapter와 함께 NextAuth.js를 사용할 수도 있습니다. 이 Prisma Adapter 버전은 핵심 `next-auth` 패키지에 포함되어 있지 않으므로 별도로 설치해야 합니다.

info

`prisma`와 `prisma-legacy` adapter가 있는 것을 보셨을 수 있습니다. 이는 역사적인 이유 때문이지만, 코드는 대부분 수렴되어 현재 두 가지 사이에 큰 차이는 없습니다. 다만 legacy adapter는 최신 버전에는 없는 테이블 이름 변경 기능을 제공합니다.

이 Adapter를 사용하려면 Prisma Client, Prisma CLI, 그리고 별도 `@next-auth/prisma-adapter` 패키지를 설치해야 합니다:

```
    npm install @prisma/client @next-auth/prisma-adapter
    npm install prisma --save-dev

```

Prisma Adapter를 사용하도록 NextAuth.js를 구성하세요:

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"
    import { PrismaAdapter } from "@next-auth/prisma-adapter"
    import { PrismaClient } from "@prisma/client"

    const prisma = new PrismaClient()

    export default NextAuth({
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_CLIENT_ID,
          clientSecret: process.env.GOOGLE_CLIENT_SECRET,
        }),
      ],
      adapter: PrismaAdapter(prisma),
    })

```

tip

Prisma의 migration 명령에는 스키마에서 SQL을 생성할 수 있는 실험적 기능이 포함되어 있지만, 현재는 Prisma가 자동 생성한 SQL 스키마가 권장 스키마와 다를 수 있으므로 제공된 SQL을 사용해 테이블과 컬럼을 생성하는 방식을 대신 권장합니다.

Prisma Adapter (`@next-auth/prisma-adapter`)용 스키마

## 설정[​](https://next-auth.js.org/v3/adapters/prisma#setup "Direct link to heading")

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
      id                 String    @id @default(cuid())
      userId             String
      providerType       String
      providerId         String
      providerAccountId  String
      refreshToken       String?
      accessToken        String?
      accessTokenExpires DateTime?
      createdAt          DateTime  @default(now())
      updatedAt          DateTime  @updatedAt
      user               User      @relation(fields: [userId], references: [id])

      @@unique([providerId, providerAccountId])
    }

    model Session {
      id           String   @id @default(cuid())
      userId       String
      expires      DateTime
      sessionToken String   @unique
      accessToken  String   @unique
      createdAt    DateTime @default(now())
      updatedAt    DateTime @updatedAt
      user         User     @relation(fields: [userId], references: [id])
    }

    model User {
      id            String    @id @default(cuid())
      name          String?
      email         String?   @unique
      emailVerified DateTime?
      image         String?
      createdAt     DateTime  @default(now())
      updatedAt     DateTime  @updatedAt
      accounts      Account[]
      sessions      Session[]
    }

    model VerificationRequest {
      id         String   @id @default(cuid())
      identifier String
      token      String   @unique
      expires    DateTime
      createdAt  DateTime @default(now())
      updatedAt  DateTime @updatedAt

      @@unique([identifier, token])
    }

```

### 클라이언트 생성[​](https://next-auth.js.org/v3/adapters/prisma#generate-client "Direct link to heading")

스키마를 저장한 후 Prisma CLI를 사용해 Prisma Client를 생성하세요:

```
    npx prisma generate

```

데이터베이스가 새 스키마를 사용하도록(즉, 테이블과 컬럼을 생성하도록) 구성하려면 `prisma migrate` 명령을 사용하세요:

```
    npx prisma migrate dev

```

위 예제 코드로 이런 방식의 스키마를 생성하려면 환경 변수 `DATABASE_URL`에 데이터베이스 연결 문자열을 지정해야 합니다. 프로젝트 루트의 `.env` 파일에 이를 설정하면 됩니다.

이 기능은 Prisma에서 실험적 기능이므로 feature flag 뒤에 있습니다. 이 옵션을 사용한 후에는 데이터베이스 스키마를 수동으로 확인해야 합니다. `prisma migrate` 사용 방법은 [Prisma 문서](https://www.prisma.io/docs/)를 참고하세요.

## 스키마 히스토리[​](https://next-auth.js.org/v3/adapters/prisma#schema-history "Direct link to heading")

원래 Prisma Adapter에서 변경된 내용

```
     model Account {
    -  id                 Int       @default(autoincrement()) @id
    +  id                 String    @id @default(cuid())
    -  compoundId         String    @unique @map(name: "compound_id")
    -  userId             Int       @map(name: "user_id")
    +  userId             String
    +  user               User      @relation(fields: [userId], references: [id])
    -  providerType       String    @map(name: "provider_type")
    +  providerType       String
    -  providerId         String    @map(name: "provider_id")
    +  providerId         String
    -  providerAccountId  String    @map(name: "provider_account_id")
    +  providerAccountId  String
    -  refreshToken       String?   @map(name: "refresh_token")
    +  refreshToken       String?
    -  accessToken        String?   @map(name: "access_token")
    +  accessToken        String?
    -  accessTokenExpires DateTime? @map(name: "access_token_expires")
    +  accessTokenExpires DateTime?
    -  createdAt          DateTime  @default(now()) @map(name: "created_at")
    +  createdAt          DateTime  @default(now())
    -  updatedAt          DateTime  @default(now()) @map(name: "updated_at")
    +  updatedAt          DateTime  @updatedAt

    -  @@index([providerAccountId], name: "providerAccountId")
    -  @@index([providerId], name: "providerId")
    -  @@index([userId], name: "userId")
    -  @@map(name: "accounts")
    +  @@unique([providerId, providerAccountId])
     }

     model Session {
    -  id           Int      @default(autoincrement()) @id
    +  id           String   @id @default(cuid())
    -  userId       Int      @map(name: "user_id")
    +  userId       String
    +  user         User     @relation(fields: [userId], references: [id])
       expires      DateTime
    -  sessionToken String   @unique @map(name: "session_token")
    +  sessionToken String   @unique
    -  accessToken  String   @unique @map(name: "access_token")
    +  accessToken  String   @unique
    -  createdAt    DateTime @default(now()) @map(name: "created_at")
    +  createdAt    DateTime @default(now())
    -  updatedAt    DateTime @default(now()) @map(name: "updated_at")
    +  updatedAt    DateTime @updatedAt
    -
    -  @@map(name: "sessions")
     }

     model User {
    -  id            Int       @default(autoincrement()) @id
    +  id            String    @id @default(cuid())
       name          String?
       email         String?   @unique
    -  emailVerified DateTime? @map(name: "email_verified")
    +  emailVerified DateTime?
       image         String?
    +  accounts      Account[]
    +  sessions      Session[]
    -  createdAt     DateTime  @default(now()) @map(name: "created_at")
    +  createdAt     DateTime  @default(now())
    -  updatedAt     DateTime  @default(now()) @map(name: "updated_at")
    +  updatedAt     DateTime  @updatedAt

    -  @@map(name: "users")
     }

     model VerificationRequest {
    -  id         Int      @default(autoincrement()) @id
    +  id         String   @id @default(cuid())
       identifier String
       token      String   @unique
       expires    DateTime
    -  createdAt  DateTime  @default(now()) @map(name: "created_at")
    +  createdAt  DateTime @default(now())
    -  updatedAt  DateTime  @default(now()) @map(name: "updated_at")
    +  updatedAt  DateTime @updatedAt

    -  @@map(name: "verification_requests")
    +  @@unique([identifier, token])
     }

```
