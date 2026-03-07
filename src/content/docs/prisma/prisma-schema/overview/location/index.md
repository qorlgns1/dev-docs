---
title: "스키마 위치"
description: "기본 네이밍과 여러 파일 구성을 포함해 Prisma Schema의 올바른 위치에 대한 문서입니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/overview/location

# 스키마 위치

마크다운 복사열기

기본 네이밍과 여러 파일 구성을 포함해 Prisma Schema의 올바른 위치에 대한 문서입니다.

Prisma Schema의 기본 이름은 `prisma` 폴더에 있는 단일 파일 `schema.prisma`입니다. 스키마 이름이 이렇게 되어 있으면 Prisma CLI가 자동으로 감지합니다.

## Prisma Schema 위치

Prisma CLI는 다음 순서대로 아래 위치에서 Prisma Schema를 찾습니다.

1. `introspect`, `generate`, `migrate`, `studio`에서 사용할 수 있는 [`--schema` flag](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference)로 지정한 위치:

```
prisma generate --schema=./alternative/schema.prisma
```

2. `prisma.config.ts` 파일에 지정한 위치:

prisma.config.ts

```
import { defineConfig } from "prisma/config";

         export default defineConfig({
           schema: "prisma/",
           ...
         });
```

3. 기본 위치:
   - `./prisma/schema.prisma`
   - `./schema.prisma`

Prisma CLI는 사용될 스키마의 경로를 출력합니다. 다음 예시는 `prisma db pull`의 터미널 출력입니다.

```
    Environment variables loaded from .env
    Prisma Schema loaded from prisma/schema.prisma // [!code highlight]

    Introspecting based on datasource defined in prisma/schema.prisma …

    ✔ Introspected 4 models and wrote them into prisma/schema.prisma in 239ms

    Run prisma generate to generate Prisma Client.
```

## 다중 파일 Prisma 스키마

### 영상 보기: 다중 파일 Prisma 스키마

Prisma 스키마를 여러 파일로 분리하고 싶다면, 다음과 같은 구성을 사용할 수 있습니다.

```
    prisma/
    ├── migrations
    ├── models
    │   ├── posts.prisma
    │   ├── users.prisma
    │   └── ... other `.prisma` files
    └── schema.prisma
```

- 사용법

다중 파일 Prisma 스키마를 사용할 때는 스키마 파일(여기에는 `generator` 블록이 있는 기본 `schema.prisma` 파일 포함)이 들어 있는 디렉터리 위치를 항상 명시적으로 지정해야 합니다.

다음 두 가지 방법으로 지정할 수 있습니다.

- Prisma CLI 명령에 `--schema` 옵션 전달 (예: `prisma migrate dev --schema ./prisma`)

- (Prisma ORM v7 기준) [`prisma.config.ts`](https://docs.prisma.io/docs/orm/reference/prisma-config-reference#schema)에서 `schema` 속성 설정:

prisma.config.ts

```
import { defineConfig, env } from "prisma/config";
        import "dotenv/config";

        export default defineConfig({
          schema: "prisma/",
          migrations: {
            path: "prisma/migrations",
            seed: "tsx prisma/seed.ts",
          },
          datasource: {
            url: env("DATABASE_URL"),
          },
        });
```

Prisma 스키마 위치를 지정할 때는 [Prisma Config 파일](https://docs.prisma.io/docs/orm/reference/prisma-config-reference#schema) 사용을 권장합니다. 다른 설정 옵션과 함께 Prisma 스키마 위치를 지정할 수 있는 가장 유연한 방법입니다.

`schema.prisma` 파일(`generator` 블록 포함)은 스키마 설정에서 지정한 동일한 디렉터리에 있어야 합니다. 예를 들어 `schema: 'prisma'`로 설정했다면 `schema.prisma` 파일은 `prisma/schema.prisma`에 있어야 하며, `prisma/models/schema.prisma` 같은 하위 디렉터리에 있으면 안 됩니다.

또한 `migrations` 디렉터리도 `schema.prisma` 파일과 같은 레벨에 배치해야 합니다.

예를 들어 `schema.prisma`에 `generator` 블록이 정의되어 있다면, 올바른 디렉터리 구조는 다음과 같습니다.

```
    # All files must be inside the `prisma/` directory
    # `migrations` and `schema.prisma` must be at the same level
    prisma/
    ├── migrations
    ├── models
    │   ├── posts.prisma
    │   └── users.prisma
    └── schema.prisma  # Contains generator block
```

스키마 파일이 `prisma/` 디렉터리(위 예시와 동일)에 있다면, `./prisma/schema.prisma`가 기본 위치이므로 `prisma generate`, `prisma migrate dev` 같은 Prisma CLI 명령은 추가 설정 없이 동작합니다.

- 다중 파일 Prisma 스키마를 위한 팁

이 기능을 사용할 때 잘 맞는 몇 가지 패턴이 있으며, 이를 따르면 기능을 더욱 효과적으로 활용할 수 있습니다.

- 도메인별로 파일 구성: 관련된 모델을 같은 파일에 그룹화하세요. 예를 들어 사용자 관련 모델은 `user.prisma`에, 게시물 관련 모델은 `post.prisma`에 둡니다.
- 명확한 네이밍 규칙 사용: 스키마 파일 이름은 명확하고 간결해야 합니다. `user.prisma`, `post.prisma` 같은 이름을 사용하고, `myModels.prisma`, `CommentFeaturesSchema.prisma` 같은 이름은 피하세요.
- 눈에 띄는 "메인" 스키마 파일 두기: 이제 원하는 만큼 스키마 파일을 가질 수 있지만, 여전히 `generator` 블록을 정의할 위치는 필요합니다. 이 블록을 쉽게 찾을 수 있도록 명확한 단일 "메인" 파일을 두는 것을 권장합니다. `main.prisma`, `schema.prisma`, `base.prisma`는 실제로 잘 작동하는 이름들입니다.
