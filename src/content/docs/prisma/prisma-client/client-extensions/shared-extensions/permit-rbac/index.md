---
title: "세분화된 권한 부여 (Permit)"
description: "Prisma 애플리케이션에서 RBAC, ABAC, ReBAC 권한 부여를 구현하는 방법을 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions/permit-rbac

# 세분화된 권한 부여 (Permit)

Prisma 애플리케이션에서 RBAC, ABAC, ReBAC 권한 부여를 구현하는 방법을 알아보세요

빠른 요약

이 페이지에서는 `@permitio/permit-prisma` 확장을 사용해 Prisma ORM 애플리케이션에서 세분화된 권한 부여(FGA)를 구현하는 방법을 설명합니다. Permit.io가 지원하는 다양한 접근 제어 모델(RBAC, ABAC, ReBAC)을 소개하고, 정확하고 프로그래밍 가능한 권한으로 데이터베이스 작업을 보호하기 위해 적절한 모델을 선택하는 방법을 안내합니다.

데이터베이스 작업에서는 누가 어떤 데이터에 접근하거나 수정할 수 있는지 신중하게 제어해야 하는 경우가 많습니다. Prisma ORM은 데이터 모델링과 데이터베이스 접근에 강점이 있지만, 내장 권한 부여 기능은 포함되어 있지 않습니다. 이 가이드는 `@permitio/permit-prisma` 확장을 사용해 Prisma 애플리케이션에서 세분화된 권한 부여를 구현하는 방법을 보여줍니다.

세분화된 권한 부여(FGA)는 사용자가 어떤 데이터에 접근하거나 수정할 수 있는지를 세부 단위에서 정밀하게 제어합니다. 적절한 권한 부여가 없으면 애플리케이션이 민감한 데이터를 노출하거나 권한 없는 수정을 허용해 보안 취약점이 생길 수 있습니다.

## 접근 제어 모델

이 확장은 Permit.io의 세 가지 접근 제어 모델을 지원합니다.

- 역할 기반 접근 제어 (RBAC)

**정의** : 사용자에게 역할(Admin, Editor, Viewer)을 할당하고, 리소스 유형에 대해 수행할 수 있는 사전 정의된 권한을 부여합니다.

**예시** : "Editor" 역할은 시스템의 모든 문서를 업데이트할 수 있습니다.

**적합한 경우** : 직무 기능이나 사용자 수준으로 접근이 결정되는 단순한 권한 구조.

- 속성 기반 접근 제어 (ABAC)

**정의** : 사용자, 리소스 또는 환경의 속성을 기반으로 접근 결정을 내립니다.

**예시** :

- `user.department == document.department` 이면 접근 허용
- `document.status == "DRAFT"` 이면 업데이트 허용

**확장에서의 동작 방식** : `enableAttributeSync` 가 켜져 있으면 정책 평가를 위해 리소스 속성이 Permit.io에 자동으로 동기화됩니다.

**적합한 경우** : 컨텍스트나 데이터 속성에 따라 달라지는 동적 규칙.

- 관계 기반 접근 제어 (ReBAC)

**정의** : 사용자와 특정 리소스 인스턴스 간의 관계를 기반으로 권한을 결정합니다.

**예시** : 한 사용자가 document-123의 "Owner" 이지만 document-456에서는 단지 "Viewer" 일 수 있습니다.

**확장에서의 동작 방식** :

- 리소스 인스턴스가 Permit.io에 동기화됩니다 (`enableResourceSync: true`)
- 권한 확인 시 특정 리소스 인스턴스 ID가 포함됩니다

**적합한 경우** : 동일한 리소스 유형의 서로 다른 인스턴스에 대해 사용자별로 다른 권한이 필요한 협업 애플리케이션.

- 올바른 모델 선택하기
  - **RBAC** : 단순한 역할 기반 접근 제어가 필요할 때
  - **ABAC** : 결정이 데이터 속성이나 컨텍스트 정보에 의존할 때
  - **ReBAC** : 리소스 인스턴스별로 사용자에게 서로 다른 권한이 필요할 때

## 사용법

- 사전 요구 사항

Prisma로 세분화된 권한 부여를 구현하기 전에 다음을 준비하세요.

- 기존 모델과 쿼리가 있는 Prisma 애플리케이션
- 권한 부여 개념에 대한 기본 이해
- 설치된 Node.js 및 npm

* 설치

Prisma Client와 함께 확장을 설치합니다.

npm

pnpm

yarn

bun

```
    npm install @permitio/permit-prisma @prisma/client
```

권한 부여 정책을 정의하려면 [Permit account](https://app.permit.io) 에도 가입해야 합니다.

> **참고:**
> Permit PDP 컨테이너가 실행 중인지 확인하세요. 성능, 보안, 가용성을 위해 Docker로 실행하는 것을 권장합니다. 자세한 내용은 Permit 문서의 [Deploy Permit to Production](https://docs.permit.io/how-to/deploy/deploy-to-production/) 및 [PDP Overview](https://docs.permit.io/concepts/pdp/overview/) 를 참고하세요.

## 기본 설정

먼저 Permit 확장으로 Prisma Client를 확장합니다.

```
    import { PrismaClient } from "@prisma/client";
    import { createPermitClientExtension } from "@permitio/permit-prisma";

    const prisma = new PrismaClient().$extends(
      createPermitClientExtension({
        permitConfig: {
          token: process.env.PERMIT_API_KEY, // Your Permit API key
          pdp: "http://localhost:7766", // PDP address (local or cloud)
        },
        enableAutomaticChecks: true, // Automatically enforce permissions
      }),
    );
```

## RBAC 구현 (역할 기반 접근 제어)

RBAC는 역할을 사용해 접근 권한을 결정합니다. 예를 들어 "Admin" 역할은 모든 작업을 수행할 수 있고, "Viewer" 역할은 데이터 읽기만 가능합니다.

1. **Permit.io 대시보드에서 리소스와 액션 정의** :
   - Prisma 모델에 맞는 리소스를 생성합니다(예: "document")
   - 액션을 정의합니다(예: "create", "read", "update", "delete")
   - 권한 세트가 포함된 역할을 생성합니다(예: "admin", "editor", "viewer")
2. **코드에서 활성 사용자 설정** :

```
    // Set the current user context before performing operations
    prisma.$permit.setUser("john@example.com");

    // All subsequent operations will be checked against this user's permissions
    const documents = await prisma.document.findMany();
```

## ABAC 구현 (속성 기반 접근 제어)

ABAC는 사용자 속성, 리소스 속성, 컨텍스트를 고려해 접근 제어를 확장합니다.

1. **ABAC용 확장 설정** :

```
    const prisma = new PrismaClient().$extends(
      createPermitClientExtension({
        permitConfig: { token: process.env.PERMIT_API_KEY, pdp: "http://localhost:7766" },
        enableAutomaticChecks: true,
      }),
    );
```

2. **속성과 함께 사용자 설정:**

```
    prisma.$permit.setUser({
      key: "doctor@hospital.com",
      attributes: { department: "cardiology" },
    });

    // Will succeed only if user department matches record department (per policy)
    const records = await prisma.medicalRecord.findMany({
      where: { department: "cardiology" },
    });
```

## ReBAC 구현 (관계 기반 접근 제어)

ReBAC는 사용자와 특정 리소스 인스턴스 간 관계를 기반으로 권한을 모델링합니다.

1. **ReBAC용 확장 설정** :

```
    const prisma = new PrismaClient().$extends(
      createPermitClientExtension({
        permitConfig: { token: process.env.PERMIT_API_KEY, pdp: "http://localhost:7766" },
        accessControlModel: "rebac",
        enableAutomaticChecks: true,
        enableResourceSync: true, // Sync resource instances with Permit.io
        enableDataFiltering: true, // Filter queries by permissions
      }),
    );
```

2. ** 인스턴스별 리소스 접근:**

```
    prisma.$permit.setUser("owner@example.com");

    // Will only succeed if the user has permission on this specific file
    const file = await prisma.file.findUnique({
      where: { id: "file-123" },
    });
```

## 수동 권한 확인

더 세밀하게 제어하려면 명시적 권한 확인을 수행할 수 있습니다.

```
    // Check if user can update a document
    const canUpdate = await prisma.$permit.check(
      "john@example.com", // user
      "update", // action
      "document", // resource
    );

    if (canUpdate) {
      await prisma.document.update({
        where: { id: "doc-123" },
        data: { title: "Updated Title" },
      });
    }

    // Or enforce permissions (throws if denied)
    await prisma.$permit.enforceCheck("john@example.com", "delete", {
      type: "document",
      key: "doc-123",
    });
```

## 일반적인 사용 사례

다음은 세분화된 권한 부여가 특히 유용한 일반적인 시나리오입니다.

- **멀티 테넌트 애플리케이션** : 서로 다른 고객 간 데이터 격리
- **헬스케어 애플리케이션** : 환자 데이터에 권한이 있는 직원만 접근하도록 보장
- **협업 플랫폼** : 공유 리소스에 대해 서로 다른 권한 부여
- **콘텐츠 관리 시스템** : 누가 콘텐츠를 게시, 편집, 조회할 수 있는지 제어

## 요약

Prisma ORM 애플리케이션에 `@permitio/permit-prisma` 확장을 통합하면 데이터를 보호하고 사용자가 허용된 범위 내에서만 접근하도록 하는 정교한 권한 부여 정책을 구현할 수 있습니다. 이 확장은 주요 권한 부여 모델(RBAC, ABAC, ReBAC)을 모두 지원하며, 자동 및 수동 권한 강제를 모두 제공합니다.

## 다음 단계

- Create a free Permit.io account
- View the full extension documentation
