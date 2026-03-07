---
title: "Deno Deploy에 배포하기"
description: "이 가이드를 통해 Deno Deploy에 REST API를 빌드하고 배포하는 방법을 배울 수 있습니다. 이 애플리케이션은 Prisma Postgres 데이터베이스에서 작업을 관리하기 위해 Prisma ORM을 사용합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-deno-deploy

# Deno Deploy에 배포하기

이 가이드를 통해 [Deno Deploy](https://deno.com/deploy)에 REST API를 빌드하고 배포하는 방법을 배울 수 있습니다. 이 애플리케이션은 [Prisma Postgres](https://docs.prisma.io/docs/postgres) 데이터베이스에서 작업을 관리하기 위해 Prisma ORM을 사용합니다.

이 가이드는 Deno CLI, Deno Deploy, Postgres 어댑터를 사용하는 Prisma Client, 그리고 Prisma Postgres를 다룹니다.

## 사전 요구 사항

- 무료 [Prisma Data Platform](https://console.prisma.io/login) 계정
- 무료 [Deno Deploy](https://deno.com/deploy) 계정
- [Deno](https://docs.deno.com/runtime/#install-deno) v2.0 이상 설치
- (권장) [VS Code용 Deno 확장](https://docs.deno.com/runtime/reference/vscode/)

## 1\. 애플리케이션 설정

새 디렉터리를 만들고 Prisma 프로젝트를 초기화합니다:

npm

pnpm

yarn

bun

```
    mkdir prisma-deno-deploy
    cd prisma-deno-deploy
    deno run -A npm:prisma@latest init --db
```

프로젝트 이름을 입력하고 데이터베이스 리전을 선택합니다.

이 명령은 다음을 수행합니다:

- [Prisma Data Platform](https://console.prisma.io)에 연결합니다(인증을 위해 브라우저 열림)
- 데이터베이스 모델용 `prisma/schema.prisma` 파일을 생성합니다
- `DATABASE_URL`이 포함된 `.env` 파일을 생성합니다
- `prisma.config.ts` 구성 파일을 생성합니다

## 2\. Deno 구성

다음 구성으로 `deno.json` 파일을 생성합니다:

deno.json

```
    {
      "nodeModulesDir": "auto",
      "compilerOptions": {
        "lib": ["deno.window"],
        "types": ["node"]
      },
      "imports": {
        "@prisma/adapter-pg": "npm:@prisma/adapter-pg@^7.0.0",
        "@prisma/client": "npm:@prisma/client@^7.0.0",
        "prisma": "npm:prisma@^7.0.0"
      },
      "tasks": {
        "dev": "deno run -A --env=.env --watch index.ts",
        "db:generate": "deno run -A --env=.env npm:prisma generate",
        "db:push": "deno run -A --env=.env npm:prisma db push",
        "db:migrate": "deno run -A --env=.env npm:prisma migrate dev",
        "db:studio": "deno run -A --env=.env npm:prisma studio"
      }
    }
```

`nodeModulesDir: "auto"` 설정은 Prisma가 Deno와 올바르게 작동하는 데 필요합니다. `compilerOptions`는 TypeScript가 Deno 전역 객체와 npm 패키지를 이해하도록 보장합니다. import map을 사용하면 `npm:@prisma/adapter-pg` 대신 `@prisma/adapter-pg` 같은 깔끔한 import 경로를 사용할 수 있습니다.

의존성을 설치합니다:

```
    deno install
    deno install --allow-scripts
```

## 3\. 데이터 모델 정의

Deno 런타임과 `Task` 모델을 추가하도록 `prisma/schema.prisma`를 수정합니다:

prisma/schema.prisma

```
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
      runtime  = "deno"
    }

    datasource db {
      provider = "postgresql"
    }

    model Task {
      id          Int      @id @default(autoincrement())
      title       String
      description String?
      completed   Boolean  @default(false)
      createdAt   DateTime @default(now())
      updatedAt   DateTime @updatedAt
    }
```

## 4\. 데이터베이스에 스키마 푸시

데이터베이스에 스키마를 적용하고 Prisma Client를 생성합니다:

```
    deno task db:push
```

이 명령은 다음을 수행합니다:

1. Prisma Postgres 데이터베이스에 `Task` 테이블을 생성합니다
2. 완전한 타입 안정성을 갖춘 Prisma Client를 생성합니다

생성 후 IDE에서 TypeScript 오류가 보이면, 타입을 새로고침하기 위해 Deno 언어 서버를 재시작하세요(`Cmd/Ctrl + Shift + P` → "Deno: Restart Language Server").

## 5\. 애플리케이션 생성

작업 관리를 위한 REST API가 포함된 `index.ts`를 생성합니다:

index.ts

```
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from "./generated/prisma/client.ts";

    // Initialize Prisma Client with the Postgres adapter
    const connectionString = Deno.env.get("DATABASE_URL")!;
    const adapter = new PrismaPg({ connectionString });
    const prisma = new PrismaClient({ adapter });

    // Helper to create JSON responses
    function json(data: unknown, status = 200): Response {
      return new Response(JSON.stringify(data, null, 2), {
        status,
        headers: { "Content-Type": "application/json" },
      });
    }

    // Request handler
    async function handler(request: Request): Promise<Response> {
      const url = new URL(request.url);
      const path = url.pathname;
      const method = request.method;

      try {
        // GET /tasks - List all tasks
        if (method === "GET" && path === "/tasks") {
          const tasks = await prisma.task.findMany({
            orderBy: { createdAt: "desc" },
          });
          return json(tasks);
        }

        // POST /tasks - Create a new task
        if (method === "POST" && path === "/tasks") {
          const body = await request.json();
          const task = await prisma.task.create({
            data: {
              title: body.title,
              description: body.description,
            },
          });
          return json(task, 201);
        }

        // GET /tasks/:id - Get a specific task
        const taskMatch = path.match(/^\/tasks\/(\d+)$/);
        if (taskMatch) {
          const id = parseInt(taskMatch[1]);

          if (method === "GET") {
            const task = await prisma.task.findUnique({ where: { id } });
            if (!task) return json({ error: "Task not found" }, 404);
            return json(task);
          }

          // PATCH /tasks/:id - Update a task
          if (method === "PATCH") {
            const body = await request.json();
            const task = await prisma.task.update({
              where: { id },
              data: body,
            });
            return json(task);
          }

          // DELETE /tasks/:id - Delete a task
          if (method === "DELETE") {
            await prisma.task.delete({ where: { id } });
            return json({ message: "Task deleted" });
          }
        }

        // GET / - API info
        if (method === "GET" && path === "/") {
          return json({
            name: "Prisma + Deno Task API",
            version: "1.0.0",
            endpoints: {
              "GET /tasks": "List all tasks",
              "POST /tasks": "Create a task",
              "GET /tasks/:id": "Get a task",
              "PATCH /tasks/:id": "Update a task",
              "DELETE /tasks/:id": "Delete a task",
            },
          });
        }

        return json({ error: "Not found" }, 404);
      } catch (error) {
        console.error(error);
        return json({ error: "Internal server error" }, 500);
      }
    }

    // Start the server
    Deno.serve({ port: 8000 }, handler);
```

다음 엔드포인트를 갖춘 전체 CRUD API가 생성됩니다:

| Method | Endpoint     | Description         |
| ------ | ------------ | ------------------- |
| GET    | `/`          | API 정보            |
| GET    | `/tasks`     | 모든 작업 목록 조회 |
| POST   | `/tasks`     | 새 작업 생성        |
| GET    | `/tasks/:id` | 특정 작업 조회      |
| PATCH  | `/tasks/:id` | 작업 업데이트       |
| DELETE | `/tasks/:id` | 작업 삭제           |

## 6\. 로컬에서 애플리케이션 테스트

개발 서버를 시작합니다:

```
    deno task dev
```

curl로 API를 테스트합니다:

```
    # Get API info
    curl http://localhost:8000/

    # Create a task
    curl -X POST http://localhost:8000/tasks \
      -H "Content-Type: application/json" \
      -d '{"title": "Learn Prisma", "description": "Complete the Deno guide"}'

    # List all tasks
    curl http://localhost:8000/tasks

    # Update a task (mark as completed)
    curl -X PATCH http://localhost:8000/tasks/1 \
      -H "Content-Type: application/json" \
      -d '{"completed": true}'

    # Delete a task
    curl -X DELETE http://localhost:8000/tasks/1
```

각 요청에 대해 JSON 응답이 표시되어야 합니다. 새 작업을 만들 때마다 작업 ID가 증가합니다.

## 7\. GitHub 리포지토리 생성

Deno Deploy에 배포하려면 GitHub 리포지토리가 필요합니다.

`.gitignore` 파일을 생성합니다:

.gitignore

```
    .env
    node_modules/
    generated/
    deno.lock
```

리포지토리를 초기화하고 푸시합니다:

```
    git init -b main
    git remote add origin https://github.com/<username>/prisma-deno-deploy
    git add .
    git commit -m "Initial commit"
    git push -u origin main
```

## 8\. Deno Deploy에 배포

1. <https://dash.deno.com/>으로 이동합니다
2. **New Project**를 클릭하고 GitHub 리포지토리를 선택합니다
3. 배포를 구성합니다:
   - **Framework preset** : No Preset
   - **Install command** : `deno install`
   - **Build command** : `deno run -A npm:prisma generate`
   - **Entrypoint** : `index.ts`
4. **Create & Deploy**를 클릭합니다

데이터베이스 연결 문자열을 추가해야 하므로 첫 번째 배포는 실패합니다.

- 환경 변수 추가
  1. 프로젝트의 **Settings** > **Environment Variables**로 이동합니다
  2. 새 변수를 추가합니다:
     - **Key** : `DATABASE_URL`
     - **Value** : Prisma Postgres 연결 문자열(`.env` 파일에서 복사)
  3. **Save**를 클릭합니다

**Redeploy**를 클릭하거나 새 커밋을 푸시해 새 배포를 트리거합니다.

## 9\. 배포된 API 테스트

배포가 완료되면 Deno Deploy URL에서 API를 테스트합니다:

```
    # Replace with your actual Deno Deploy URL
    curl https://your-project.deno.dev/

    # Create a task
    curl -X POST https://your-project.deno.dev/tasks \
      -H "Content-Type: application/json" \
      -d '{"title": "Deploy to production"}'

    # List tasks
    curl https://your-project.deno.dev/tasks
```

## 요약

다음을 사용해 REST API를 Deno Deploy에 성공적으로 배포했습니다:

- 네이티브 TypeScript 지원을 갖춘 런타임으로서의 **Deno**
- 타입 안전한 데이터베이스 접근을 위한 Postgres 어댑터와 함께 사용하는 **Prisma ORM**
- 관리형 데이터베이스인 **Prisma Postgres**

프로젝트 구조는 다음과 같아야 합니다:

```
    prisma-deno-deploy/
    ├── deno.json
    ├── index.ts
    ├── prisma/
    │   └── schema.prisma
    ├── prisma.config.ts
    ├── generated/
    │   └── prisma/
    │       └── ...
    └── .env
```

- 다음 단계
  - 세션을 위해 [Deno KV](https://deno.com/kv)를 사용해 인증 추가
  - [Zod](https://zod.dev/)로 요청 유효성 검사 추가
  - 사용자 정의 기능을 위해 [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions) 탐색
  - 프로덕션에서 스키마 버전 관리를 위해 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate) 설정
