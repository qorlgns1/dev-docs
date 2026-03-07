---
title: "지원되지 않는 데이터베이스 기능 (Prisma Migrate)"
description: "Markdown 복사Markdown 열기"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-migrate/workflows/unsupported-database-features

# 지원되지 않는 데이터베이스 기능 (Prisma Migrate)

Markdown 복사Markdown 열기

Prisma Migrate를 사용하는 프로젝트에서 지원되지 않는 데이터베이스 기능을 포함하는 방법

Prisma Migrate는 데이터베이스에 어떤 기능을 생성할지 Prisma 스키마를 사용해 결정합니다. 하지만 일부 데이터베이스 기능은 [Prisma 스키마로 표현할 수 없으며](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features), 다음을 포함하되 이에 국한되지 않습니다.

- 저장 프로시저
- 트리거
- 뷰

지원되지 않는 기능을 데이터베이스에 추가하려면, 적용하기 전에 해당 기능이 포함되도록 [마이그레이션을 커스터마이징](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/customizing-migrations)해야 합니다.

이제 부분 인덱스는 `@@index`, `@@unique`, `@unique`의 `where` 인수를 통해 Prisma Schema Language에서 지원됩니다. 자세한 내용은 [부분 인덱스 구성](https://docs.prisma.io/docs/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where)을 참고하세요. 더 이상 부분 인덱스를 위해 마이그레이션을 커스터마이징할 필요가 없습니다.

Prisma 스키마는 [지원되지 않는 필드 타입](https://docs.prisma.io/docs/orm/prisma-schema/data-model/unsupported-database-features#unsupported-field-types)과 [네이티브 데이터베이스 함수](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/native-database-functions)도 표현할 수 있습니다.

이 가이드는 **MongoDB에는 적용되지 않습니다**.
MongoDB에서는 `migrate dev` 대신 [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용합니다([MongoDB](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb) 참고).

## 지원되지 않는 기능을 포함하도록 마이그레이션 커스터마이징하기

지원되지 않는 기능을 포함하도록 마이그레이션을 커스터마이징하려면 다음을 수행하세요.

- 적용하지 않고 새 마이그레이션을 생성하려면 `--create-only` 플래그를 사용합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev --create-only
```

- 생성된 `migration.sql` 파일을 열고 지원되지 않는 기능(예: 트리거 함수)을 추가합니다.

migration.sql

```
    CREATE OR REPLACE FUNCTION notify_on_insert()
    RETURNS TRIGGER AS $$
    BEGIN
      PERFORM pg_notify('new_record', NEW.id::text);
      RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
```

- 마이그레이션을 적용합니다.

npm

pnpm

yarn

bun

```
    npx prisma migrate dev
```

- 수정한 마이그레이션을 소스 제어에 커밋합니다.
