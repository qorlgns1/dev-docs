---
title: "모범 사례"
description: "Prisma ORM으로 스키마 설계, 쿼리 최적화, 타입 안정성, 보안, 배포를 위한 프로덕션 준비 패턴을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/more/best-practices

# 모범 사례

Prisma ORM으로 스키마 설계, 쿼리 최적화, 타입 안정성, 보안, 배포를 위한 프로덕션 준비 패턴을 알아보세요.

## 스키마 설계 및 모델링

- 네이밍 규칙

모델 이름(단수형)에는 **PascalCase**를, 필드 이름에는 **camelCase**를 사용하세요. `@map` 및 `@@map`으로 레거시 데이터베이스 네이밍에 매핑할 수 있습니다:

prisma/schema.prisma

```
    model Comment {
      id      Int    @id @default(autoincrement())
      content String @map("comment_text")
      email   String @map("commenter_email")

      @@map("comments")
    }
```

이렇게 하면 어떤 데이터베이스 네이밍 규칙을 지원하더라도 Prisma 스키마의 가독성을 유지할 수 있습니다.

- 모델 관계를 명시적으로 정의

스키마를 명확하고 유지보수 가능하게 유지하려면 관계의 양쪽을 항상 모두 정의하세요:

prisma/schema.prisma

```
    model User {
      id    Int    @id @default(autoincrement())
      posts Post[]
    }

    model Post {
      id       Int  @id @default(autoincrement())
      author   User @relation(fields: [authorId], references: [id])
      authorId Int
    }
```

외래 키를 강제하지 않는 데이터베이스(예: PlanetScale)의 경우 Prisma ORM이 관계를 에뮬레이션하므로, 전체 테이블 스캔을 피하기 위해 관계 스칼라 필드에 인덱스를 수동으로 추가해야 합니다:

prisma/schema.prisma

```
    model Comment {
      postId Int
      post   Post @relation(fields: [postId], references: [id])

      @@index([postId])
    }
```

- 인덱스 전략

`where`, `orderBy`, 관계에서 사용하는 필드에 인덱스를 추가하세요. 인덱스가 없으면 데이터베이스가 일치하는 행을 찾기 위해 전체 테이블을 스캔해야 할 수 있으며, 테이블이 커질수록 성능이 느려집니다.

prisma/schema.prisma

```
    model Comment {
      id      Int    @id @default(autoincrement())
      postId  Int
      status  String
      post    Post   @relation(fields: [postId], references: [id])

      @@index([postId])
      @@index([status])
    }
```

- Enum vs string 필드

Enum은 타입 안전한 유한 값 집합을 제공합니다. enum 값을 데이터베이스 네이밍에 맞게 매핑할 수 있습니다:

prisma/schema.prisma

```
    enum Role {
      USER  @map("user")
      ADMIN @map("admin")

      @@map("user_role")
    }

    model User {
      id   Int  @id @default(autoincrement())
      role Role @default(USER)
    }
```

값이 자주 변경되거나 사용자가 생성하는 경우에는 `String`이 스키마 변경을 피할 수 있습니다.

- 멀티 파일 스키마 구성

대규모 프로젝트에서는 멀티 파일 Prisma 스키마(v6.7.0부터 지원)를 사용하세요:

```
    prisma/
    ├── schema.prisma        # Main schema with generator and datasource
    ├── migrations/          # Migration files
    ├── user.prisma         # User-related models
    ├── product.prisma      # Product-related models
    └── order.prisma        # Order-related models
```

`schema.prisma` 파일(`generator` 블록 포함)과 `migrations/` 디렉터리는 같은 수준에 있어야 합니다. `prisma/models/` 같은 하위 디렉터리에 추가 스키마 파일을 그룹화할 수도 있습니다.

## 쿼리 최적화

- 연결 풀링

전역 `PrismaClient` 인스턴스를 하나만 생성해 애플리케이션 전체에서 재사용하세요. 인스턴스를 여러 개 만들면 연결 풀도 여러 개 생성되어 데이터베이스 연결 한도를 소진하고 쿼리 성능이 저하될 수 있습니다.

lib/prisma.ts

```
    import { PrismaClient } from '../generated/prisma/client'
    import { PrismaPg } from '@prisma/adapter-pg'

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL
    })

    export const prisma = new PrismaClient({ adapter })
```

**서버리스 환경:**

- 워밍된 호출 간 연결을 재사용할 수 있도록 핸들러 함수 **외부**에서 `PrismaClient`를 인스턴스화하세요
- 내장 연결 풀링을 위해 [Prisma Postgres](https://docs.prisma.io/docs/postgres) 또는 PgBouncer 같은 외부 풀러를 고려하세요

* N+1 쿼리 방지

N+1 문제는 목록을 가져오기 위한 쿼리 1개를 실행한 뒤, 목록의 각 항목마다 추가 쿼리 1개를 실행할 때 발생합니다. 이로 인해 소수의 효율적인 쿼리 대신 데이터베이스와의 불필요한 왕복이 많이 발생합니다.

n-plus-one.ts

```
    // ❌ Bad: N+1 queries (1 + N queries)
    const users = await prisma.user.findMany()
    for (const user of users) {
      const posts = await prisma.post.findMany({
        where: { authorId: user.id }
      })
    }

    // ✅ Good: Single query with include
    const users = await prisma.user.findMany({
      include: { posts: true }
    })

    // ✅ Good: Batch with IN filter
    const users = await prisma.user.findMany()
    const posts = await prisma.post.findMany({
      where: { authorId: { in: users.map(u => u.id) } }
    })
```

- 필요한 필드만 선택

기본적으로 Prisma ORM은 모든 스칼라 필드를 반환합니다. 반환할 필드를 화이트리스트로 지정하려면 `select`를 사용하세요:

select.ts

```
    const user = await prisma.user.findFirst({
      select: {
        id: true,
        email: true,
        role: true
      }
    })
```

제외할 필드를 블랙리스트로 지정하려면 `omit`을 사용하세요(민감한 데이터에 유용):

omit.ts

```
    import { PrismaClient } from '../generated/prisma/client'
    import { PrismaPg } from '@prisma/adapter-pg'

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL
    })

    const prisma = new PrismaClient({
      adapter,
      omit: {
        user: { secretValue: true }
      }
    })
```

같은 쿼리에서 `select`와 `omit`을 함께 사용할 수는 없습니다.

- 페이지네이션

임의 페이지로 이동이 필요한 소규모 데이터셋에는 **offset pagination**을 사용하세요:

offset-pagination.ts

```
    const posts = await prisma.post.findMany({
      skip: 40,
      take: 10,
      where: { email: { contains: 'prisma.io' } },
    })
```

대규모 데이터셋이나 무한 스크롤에는 **cursor-based pagination**을 사용하세요. cursor 기반 페이지네이션은 건너뛴 행을 순회하는 대신 인덱스된 컬럼으로 시작 위치를 찾기 때문에 확장성이 더 좋습니다:

cursor-pagination.ts

```
    const posts = await prisma.post.findMany({
      take: 10,
      skip: 1,
      cursor: {
        id: lastPost.id,
      },
      orderBy: {
        id: 'asc',
      },
    })
```

- 배치 작업

여러 레코드를 처리할 때는 벌크 메서드를 사용하세요:

batch-operations.ts

```
    await prisma.user.createMany({
      data: [
        { email: 'alice@prisma.io' },
        { email: 'bob@prisma.io' }
      ]
    })

    await prisma.post.updateMany({
      where: { published: false },
      data: { published: true }
    })
```

벌크 작업(`createMany`, `createManyAndReturn`, `updateMany`, `updateManyAndReturn`, `deleteMany`)은 [자동으로 트랜잭션으로 실행](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions#batch-operations)되므로, 모든 쓰기가 함께 성공하거나 실패 시 모두 롤백됩니다.

- Raw 쿼리

Prisma ORM의 쿼리 API를 우선 사용하세요. Prisma ORM이 지원하지 않는 기능이 필요하거나 고도로 최적화된 쿼리가 필요한 경우에만 raw SQL을 사용하세요:

raw-query.ts

```
    const email = 'user@example.com'
    const users = await prisma.$queryRaw`
      SELECT * FROM "User" WHERE email = ${email}
    `
```

사용자 입력을 SQL 문자열에 절대 연결하지 마세요. SQL 인젝션을 방지하려면 항상 파라미터화된 쿼리 또는 태그드 템플릿을 사용하세요.

## 타입 안정성 및 검증

- 생성된 타입 활용

인터페이스를 중복 정의하는 대신 Prisma ORM이 생성한 타입을 사용하세요:

generated-types.ts

```
    import type { User } from '../generated/prisma/client'

    async function getAdminEmails(): Promise<string[]> {
      const admins: User[] = await prisma.user.findMany({
        where: { role: 'ADMIN' }
      })

      return admins.map(a => a.email)
    }
```

- 입력 검증

데이터베이스 작업 전에 사용자 입력을 항상 검증하고 정제하세요:

input-validation.ts

```
    import { z } from 'zod'

    const createUserSchema = z.object({
      email: z.string().email(),
      name: z.string().min(1).max(100)
    })

    async function createUser(input: unknown) {
      const data = createUserSchema.parse(input)
      return prisma.user.create({ data })
    }
```

## 보안

- SQL 인젝션 방지

Prisma ORM API는 기본적으로 안전합니다. raw 쿼리에서는 항상 파라미터화된 쿼리를 사용하세요. 신뢰할 수 없는 입력을 문자열 연결하면 공격자가 쿼리에 임의의 SQL을 주입할 수 있습니다.

sql-injection-prevention.ts

```
    // ✅ Safe: tagged template
    const result = await prisma.$queryRaw`
      SELECT * FROM "User" WHERE email = ${email}
    `

    // ✅ Safe: parameterized
    const result = await prisma.$queryRawUnsafe(
      'SELECT * FROM "User" WHERE email = $1',
      email
    )

    // ❌ Unsafe: string concatenation
    const query = `SELECT * FROM "User" WHERE email = '${email}'`
    const result = await prisma.$queryRawUnsafe(query)
```

- 민감 데이터 처리

쿼리 결과에서 민감 필드를 제외하세요:

sensitive-data.ts

```
    import { PrismaClient } from '../generated/prisma/client'
    import { PrismaPg } from '@prisma/adapter-pg'

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL
    })

    // Global exclusion
    const prisma = new PrismaClient({
      adapter,
      omit: {
        user: { secretValue: true }
      }
    })

    // Per-query exclusion
    const user = await prisma.user.findUnique({
      where: { id: 1 },
      omit: { secretValue: true }
    })
```

## 테스트

- 데이터베이스 설정

자유롭게 초기화할 수 있는 전용 테스트 데이터베이스를 사용하세요:

1. 테스트 데이터베이스 시작(대개 Docker)
2. 마이그레이션으로 스키마 적용
3. 테스트 데이터 시드
4. 테스트 실행
5. 데이터베이스 정리 또는 초기화

- `mocking`을 사용한 단위 테스트

`jest-mock-extended`로 Prisma ORM을 mock 처리하세요:

unit-test.ts

```
    import { PrismaClient } from '../generated/prisma/client'
    import { mockDeep } from 'jest-mock-extended'

    const prismaMock = mockDeep<PrismaClient>()

    test('finds user by email', async () => {
      prismaMock.user.findUnique.mockResolvedValue({
        id: 1,
        email: 'test@example.com',
        name: 'Test User'
      })

      const user = await prismaMock.user.findUnique({
        where: { email: 'test@example.com' }
      })

      expect(user).toBeDefined()
    })
```

- 실제 데이터베이스를 사용한 통합 테스트

Prisma Migrate와 함께 실제 데이터베이스를 사용하세요:

integration-test.ts

```
    import { PrismaClient } from '../generated/prisma/client'
    import { PrismaPg } from '@prisma/adapter-pg'

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL
    })

    const prisma = new PrismaClient({ adapter })

    beforeEach(async () => {
      await prisma.user.create({
        data: { email: 'test@example.com', name: 'Test' }
      })
    })

    afterEach(async () => {
      await prisma.user.deleteMany()
    })

    test('creates user', async () => {
      const user = await prisma.user.create({
        data: { email: 'new@example.com', name: 'New User' }
      })

      expect(user.email).toBe('new@example.com')
    })
```

## 프로덕션 배포

- 마이그레이션 전략

**개발 환경:**

- 마이그레이션 생성 및 적용에는 `prisma migrate dev`를 사용하세요
- 빠른 프로토타이핑에만 `prisma db push`를 사용하세요(데이터가 초기화될 수 있음)

**프로덕션 환경:**

- 커밋된 마이그레이션과 함께 **오직** `prisma migrate deploy`만 사용하세요
- `migrate dev`(DB 리셋 프롬프트 가능)나 `db push`(파괴적일 수 있고 migration 없는 워크플로에 고정됨)는 절대 사용하지 마세요

`prisma migrate deploy`는 기존 마이그레이션을 비대화형 방식으로 적용하고, 동시 실행을 방지하기 위해 advisory locking을 사용하며, 프로덕션 데이터에 안전합니다.

CI/CD 워크플로 예시:

.github/workflows/deploy.yml

```
    - name: Apply migrations
      run: npx prisma migrate deploy
      env:
        DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

- 서버리스 고려사항

AWS Lambda, Vercel, Cloudflare Workers 또는 유사한 플랫폼의 경우:

1. 워밍된 호출 간 연결 재사용을 위해 핸들러 함수 **외부**에서 `PrismaClient`를 인스턴스화하세요
2. 각 호출 끝에서 `$disconnect()`를 호출하지 마세요(컨테이너가 재사용될 수 있음)
3. 고동시성 워크로드에서는 PgBouncer 같은 외부 연결 풀러를 고려하세요

serverless-handler.ts

```
    import { PrismaClient } from '../generated/prisma/client'
    import { PrismaPg } from '@prisma/adapter-pg'

    const adapter = new PrismaPg({
      connectionString: process.env.DATABASE_URL
    })

    const prisma = new PrismaClient({ adapter })

    export async function handler(event) {
      const users = await prisma.user.findMany()
      return {
        statusCode: 200,
        body: JSON.stringify(users)
      }
    }
```

매 호출마다 핸들러 내부에서 새 클라이언트를 생성하면 데이터베이스 연결이 고갈될 위험이 있습니다. 동시 실행되는 각 함수가 자체 연결 풀을 만들어 연결 수가 빠르게 증가합니다.

## 다음 단계

- 쿼리 최적화
- Raw 쿼리
- Prisma Migrate 워크플로
