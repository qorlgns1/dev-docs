---
title: "TypeScript 성능"
description: "대규모 Prisma 스키마로 작업할 때 TypeScript 컴파일 성능 최적화하기"
---

출처 URL: https://docs.prisma.io/docs/orm/more/troubleshooting/typescript-performance

# TypeScript 성능

대규모 Prisma 스키마로 작업할 때 TypeScript 컴파일 성능 최적화하기

대규모 데이터베이스 스키마로 작업할 때는 타입 정의 전략을 간단히 바꾸는 것만으로도 성능이 크게 향상될 수 있습니다.

| 접근 방식            | 타입                 | 인스턴스화           | 메모리               | 컴파일 시간          |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| **Direct Reference** | 269,597              | 2,772,929            | 395MB                | 1.86s                |
| **typeof technique** | 222 (**99.9% 감소**) | 152 (**99.9% 감소**) | 147MB (**62% 감소**) | 0.41s (**78% 감소**) |

## 문제

광범위한 데이터베이스 스키마를 사용하는 엔터프라이즈 애플리케이션에서는 Prisma가 생성하는 타입이 매우 커질 수 있습니다. 50개 이상의 테이블과 깊은 관계를 가진 스키마는 다음과 같은 문제를 초래할 수 있습니다.

- 컴파일 시간이 수분 이상으로 증가
- 타입 검사 중 높은 메모리 사용량
- IDE 반응성의 현저한 저하
- CI/CD 파이프라인에서 타입 검사 타임아웃 발생

## 해결 방법

PrismaClient 인스턴스를 받는 함수 파라미터를 정의할 때 직접 타입 참조 대신 TypeScript의 `typeof` 연산자를 사용하세요.

- 대규모 스키마에서 문제가 되는 접근 방식

```
    import { PrismaClient } from "../prisma/generated/client";

    const saveFn = async (prismaClient: PrismaClient) => {
      // Function implementation
    };

    const client = new PrismaClient();
    await saveFn(client);
```

- `typeof`를 사용한 최적화된 접근 방식

```
    import { PrismaClient } from "../prisma/generated/client";

    const saveFn = async (prismaClient: typeof client) => {
      // Function implementation
    };

    const client = new PrismaClient();
    await saveFn(client);
```

## `typeof`가 더 효율적인 이유

`typeof` 연산자는 더 효율적인 타입 해석 경로를 만듭니다.

1. **타입 쿼리 참조** : `typeof client`는 식별자 표현식의 확장된 타입을 얻는 타입 쿼리를 수행하므로, 복잡한 `PrismaClient` 타입 정의를 다시 확장할 필요가 없습니다.
2. **타입 인스턴스화 감소** : 컴파일러가 각 타입 검사마다 Prisma 전체 타입 계층을 확장하지 않으므로(인스턴스화 99.9% 감소) 성능이 향상됩니다.
3. **메모리 효율성** : 기존 인스턴스의 추론된 타입을 참조하는 방식은 복잡한 조건부 타입과 제네릭을 확장하는 방식보다 훨씬 적은 메모리를 사용합니다.

## 결론

대규모 Prisma 스키마로 작업할 때는 직접 타입 참조와 타입 쿼리 사이의 선택이 개발 속도를 유지하는 데 매우 중요합니다. 여기서 확인된 컴파일 시간 78% 감소 효과는 스키마 복잡도가 높아질수록 기하급수적으로 커집니다.

## 벤치마크

전체 벤치마크 코드는 다음에서 확인할 수 있습니다: <https://github.com/ToyB0x/ts-bench/pull/211>
