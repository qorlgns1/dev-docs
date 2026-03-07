---
title: "Next.js"
description: "Next.js 애플리케이션에서 Prisma ORM을 사용할 때의 모범 사례와 문제 해결 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/more/troubleshooting/nextjs

# Next.js

Next.js 애플리케이션에서 Prisma ORM을 사용할 때의 모범 사례와 문제 해결 방법

Prisma ORM과 Next.js는 최신 웹 애플리케이션을 구축하기 위한 강력한 조합입니다. 이 가이드에서는 모범 사례, 일반적인 문제, 그리고 해결 방법을 다룹니다.

## 개발 환경에서 Prisma Client 사용 모범 사례

- 여러 Prisma Client 인스턴스 피하기

Next.js 애플리케이션을 개발할 때 흔한 문제 중 하나는 의도치 않게 Prisma Client 인스턴스를 여러 개 생성하는 것입니다. 이는 개발 환경에서 Next.js의 hot-reloading 기능 때문에 자주 발생합니다.

#

- 이 문제가 발생하는 이유

Next.js의 hot-reloading 기능은 코드 변경 사항을 즉시 반영하기 위해 모듈을 자주 다시 로드합니다. 하지만 이로 인해 Prisma Client 인스턴스가 여러 개 생성될 수 있으며, 리소스를 소모하고 예기치 않은 동작을 유발할 수 있습니다.

#

- 권장 해결 방법

이를 방지하려면 전역 변수를 사용해 Prisma Client 인스턴스를 하나만 생성하세요:

```
    // lib/prisma.ts
    import { PrismaClient } from "../prisma/generated/client";

    const globalForPrisma = global as unknown as { prisma: PrismaClient };

    export const prisma = globalForPrisma.prisma || new PrismaClient();

    if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

이 접근 방식을 사용하면 개발 중 hot-reloading이 발생하더라도 Prisma Client 인스턴스가 하나만 유지됩니다.

## 모노레포에서 Prisma ORM 설정하기

- 모노레포에서 Prisma ORM 사용 시 과제

모노레포는 여러 프로젝트가 코드와 의존성을 공유할 수 있게 해 주어 현대 개발에서 널리 사용됩니다. 하지만 모노레포에서 Prisma ORM을 사용하면 의존성 해석 및 스키마 관리와 관련된 문제가 생길 수 있습니다.

#

- 핵심 이슈
  1. **의존성 해석** : 모노레포의 여러 패키지가 서로 다른 버전의 Prisma ORM을 사용하면 충돌이 발생할 수 있습니다.
  2. **스키마 중앙화** : 여러 프로젝트에서 단일 Prisma Schema를 관리하는 일은 복잡할 수 있습니다.

#

- 모노레포 통합 모범 사례
  - **Prisma Schema 중앙화** : 일관성을 위해 `schema.prisma` 파일을 `@myorg/db` 같은 공유 패키지에 배치하세요.

  - **생성된 클라이언트에 사용자 지정 출력 디렉터리 사용** : 패키지 전반의 일관성을 유지하려면 생성된 Prisma Client에 대해 [사용자 지정 출력 디렉터리](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#fields-for-prisma-client-provider)를 정의하세요.

  - **루트에 의존성 설치** : 버전 충돌을 방지하려면 모노레포 루트에 Prisma ORM을 설치하세요.

  - **생성을 위해 NPM Scripts 사용** :

```
{
          "scripts": {
            "prisma:generate": "prisma generate --schema=./packages/db/schema.prisma"
          }
        }
```

## Next.js에서 Prisma Client 동적 사용

- 동적 시나리오 처리

테넌트별 데이터베이스 작업과 같은 동적 사용 사례는 Next.js와 함께 Prisma ORM을 사용할 때 추가적인 고려가 필요합니다.

#

- 문제

각 테넌트가 자체 데이터베이스를 가질 수 있으므로 런타임에 별도의 Prisma Client를 생성해야 할 수 있습니다. Next.js의 하이브리드 렌더링 모델 때문에 이는 더 복잡해질 수 있습니다.

#

- 해결 방법

테넌트별 구성에 따라 Prisma Client를 동적으로 생성하는 팩토리 함수를 사용하세요:

```
    // lib/prismaDynamic.ts
    import { PrismaClient } from "../prisma/generated/client";

    type TenantConfig = {
      databaseUrl: string;
    };

    export function createPrismaClient(config: TenantConfig): PrismaClient {
      return new PrismaClient({
        datasources: {
          db: {
            url: config.databaseUrl,
          },
        },
      });
    }
```

리소스 고갈을 방지하려면 동적으로 생성된 Prisma Clients의 라이프사이클을 적절히 관리해야 합니다.

## Vercel 빌드 의존성 캐싱

- 문제

Prisma ORM을 사용하는 애플리케이션을 [Vercel](https://vercel.com/)에 배포하면, 배포 시 다음과 같은 오류 메시지가 나타날 수 있습니다:

```
    Prisma has detected that this project was built on Vercel, which caches dependencies.
    This leads to an outdated Prisma Client because Prisma's auto-generation isn't triggered.
    To fix this, make sure to run the `prisma generate` command during the build process.

    Learn how: https://pris.ly/d/vercel-build
```

이는 Vercel이 프로젝트의 의존성 중 하나가 변경될 때까지 의존성을 캐시하기 때문에 발생합니다. Prisma ORM은 의존성이 설치될 때 Prisma Client를 생성하기 위해 `postinstall` hook을 사용합니다. Vercel이 캐시된 모듈을 사용하기 때문에 초기 배포 이후의 후속 배포에서는 이 `postinstall` hook이 실행되지 않습니다.

- 해결 방법

이 문제는 모든 배포에서 Prisma Client를 명시적으로 생성하면 해결할 수 있습니다. 각 배포 전에 `prisma generate`를 실행하면 Prisma Client가 최신 상태로 유지됩니다.

#

- 옵션 1: 사용자 지정 `postinstall` 스크립트 (권장)

프로젝트의 `package.json` 파일 `scripts` 섹션에서 `postinstall` 스크립트에 `prisma generate`를 추가하세요:

```
    {
      "scripts": {
        "postinstall": "prisma generate"
      }
    }
```

#

- 옵션 2: 빌드 스크립트에 추가

빌드 명령 앞에 `prisma generate`를 추가하세요:

```
    {
      "scripts": {
        "build": "prisma generate && <actual-build-command>"
      }
    }
```

#

- 옵션 3: Vercel UI 빌드 설정

프로젝트 대시보드에서 **Settings** > **General** > **Build & Development Settings**로 이동한 뒤, Build Command 필드의 앞부분에 `prisma generate`를 추가하세요.

## Netlify 빌드 의존성 캐싱

- 문제

Prisma ORM을 사용하는 애플리케이션을 [Netlify](https://www.netlify.com/)에 배포하면 유사한 캐싱 오류가 발생할 수 있습니다:

```
    Prisma has detected that this project was built on Netlify, which caches dependencies.
    This leads to an outdated Prisma Client because Prisma's auto-generation isn't triggered.
    To fix this, make sure to run the `prisma generate` command during the build process.

    Learn how: https://pris.ly/d/netlify-build
```

- 해결 방법

Vercel과 동일한 해결 방법이 적용됩니다:

#

- 옵션 1: 사용자 지정 `postinstall` 스크립트 (권장)

```
    {
      "scripts": {
        "postinstall": "prisma generate"
      }
    }
```

#

- 옵션 2: 빌드 스크립트에 추가

```
    {
      "scripts": {
        "build": "prisma generate && <actual-build-command>"
      }
    }
```

#

- 옵션 3: Netlify UI 빌드 설정

프로젝트 대시보드에서 **Site Settings** > **Build & deploy** > **Continuous deployment** > **Build settings**로 이동한 뒤, Build command 필드의 앞부분에 `prisma generate`를 추가하세요.
