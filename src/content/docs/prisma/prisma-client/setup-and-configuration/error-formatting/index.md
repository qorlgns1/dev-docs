---
title: "오류 포맷팅 구성하기"
description: "이 페이지에서는 Prisma Client를 사용할 때 오류 포맷팅을 구성하는 방법을 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/error-formatting

# 오류 포맷팅 구성하기

이 페이지에서는 Prisma Client를 사용할 때 오류 포맷팅을 구성하는 방법을 설명합니다.

기본적으로 Prisma Client는 오류 스택을 보기 좋게 출력하고 문제를 해결하는 방법을 추천하기 위해 [ANSI 이스케이프 문자](https://en.wikipedia.org/wiki/ANSI_escape_code)를 사용합니다. 이는 터미널에서 Prisma Client를 사용할 때 매우 유용하지만, GraphQL API 같은 컨텍스트에서는 추가 포맷팅 없이 최소한의 오류만 필요할 수 있습니다.

이 페이지에서는 Prisma Client에서 오류 포맷팅을 구성하는 방법을 설명합니다.

## 포맷팅 수준

오류 포맷팅 수준은 3가지가 있습니다.

1. **Pretty Error** (기본값): 색상, 코드 구문 하이라이팅, 전체 스택 트레이스, 그리고 문제에 대한 가능한 해결책이 포함된 확장 오류 메시지를 제공합니다.
2. **Colorless Error** : pretty error와 동일하지만 색상이 없습니다.
3. **Minimal Error** : 원시 오류 메시지입니다.

이러한 오류 포맷팅 수준을 구성하는 방법은 두 가지입니다.

- 환경 변수를 통해 구성 옵션 설정
- `PrismaClient` 생성자에 구성 옵션 전달

## 환경 변수를 통한 포맷팅

- [`NO_COLOR`](https://docs.prisma.io/docs/orm/reference/environment-variables-reference#no_color): 이 env var가 제공되면 오류 메시지에서 색상이 제거됩니다. 따라서 **colorless error**가 됩니다. `NO_COLOR` 환경 변수는 [여기](https://no-color.org/)에 설명된 표준입니다.
- `NODE_ENV=production`: env var `NODE_ENV`가 `production`으로 설정되면 **minimal error**만 출력됩니다. 이를 통해 프로덕션 환경에서 로그를 더 쉽게 파악할 수 있습니다.

* `PrismaClient` 생성자를 통한 포맷팅

대안으로, `PrismaClient`의 [`errorFormat`](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#errorformat) 파라미터를 사용해 오류 포맷을 설정할 수 있습니다:

```
    const prisma = new PrismaClient({
      errorFormat: "pretty",
    });
```
