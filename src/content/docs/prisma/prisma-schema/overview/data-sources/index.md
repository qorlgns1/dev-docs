---
title: "데이터 소스"
description: "데이터 소스를 사용하면 Prisma가 데이터베이스에 연결할 수 있습니다. 이 페이지에서는 Prisma 스키마에서 데이터 소스를 구성하는 방법을 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/overview/data-sources

# 데이터 소스

데이터 소스를 사용하면 Prisma가 데이터베이스에 연결할 수 있습니다. 이 페이지에서는 Prisma 스키마에서 데이터 소스를 구성하는 방법을 설명합니다.

데이터 소스는 Prisma ORM이 데이터베이스에 연결하는 방식을 결정하며, Prisma 스키마의 [`datasource`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#datasource) 블록으로 표현됩니다. 연결 세부 정보(예: 데이터베이스 URL)는 [Prisma Config](https://docs.prisma.io/docs/orm/reference/prisma-config-reference)에서 구성합니다. 다음 데이터 소스는 `postgresql` provider를 사용합니다:

```
    datasource db {
      provider = "postgresql"
    }
```

Prisma 스키마에는 데이터 소스를 _하나만_ 가질 수 있습니다. 하지만 다음은 가능합니다:

- `PrismaClient`를 생성할 때 데이터베이스 연결 재정의
- 클라우드 호스팅 개발 데이터베이스를 사용하는 경우 Prisma Migrate의 섀도 데이터베이스에 대해 다른 **database** 지정

## 데이터베이스 연결 보안

일부 데이터 소스 `provider`는 **연결 구성에서 인증서 위치를 지정**하여 SSL/TLS로 연결을 구성할 수 있습니다.

- PostgreSQL에서 SSL 연결 구성
- MySQL에서 SSL 연결 구성
- Microsoft SQL Server에서 TLS 연결 구성

Prisma Config에서 SSL/TLS 연결을 구성하는 예시는 위의 데이터베이스별 문서를 참고하세요.
