---
title: "시스템 요구 사항"
description: "Prisma ORM 실행을 위한 시스템 요구 사항"
---

출처 URL: https://docs.prisma.io/docs/orm/reference/system-requirements

# 시스템 요구 사항

Prisma ORM 실행을 위한 시스템 요구 사항

이 섹션에서는 Prisma ORM에 필요한 소프트웨어, 지원되는 운영 체제, 그리고 특정 운영 체제의 런타임 종속성 요구 사항을 나열합니다.

- 소프트웨어 요구 사항

최신 버전의 Prisma ORM에는 다음 소프트웨어가 필요합니다:

| Tool                   | 최소 요구 버전                   |
| ---------------------- | -------------------------------- |
| Node.js                | ^20.19.0, ^22.12.0, 또는 ^24.0.0 |
| TypeScript (선택 사항) | 5.4+                             |
| Yarn (선택 사항)       | 1.19.2                           |

- Prisma ORM은 모든 _Active LTS_ 및 _Maintenance LTS_ **Node.js** 릴리스를 지원하고 테스트합니다. [_Current_ 같은 이러한 상태가 아닌 릴리스와 홀수 버전](https://nodejs.org/en/about/releases/)도 동작할 가능성이 높지만, 프로덕션 사용은 권장되지 않습니다.
- **TypeScript**는 TypeScript 사용자에게만 필요합니다.
- **Yarn 1**을 사용할 때 `1.19.2`가 Prisma Client와 호환되는 최소 버전입니다.

참고: [지원되는 데이터베이스 버전](https://docs.prisma.io/docs/orm/reference/supported-databases)

이전 버전 펼치기

- Prisma ORM v6

Prisma ORM v6에는 다음 소프트웨어가 필요합니다:

| 최소 요구 버전
---|---
Node.js| 16.13 / 18.X / 20.X
TypeScript (선택 사항)| 4.7+
Yarn (선택 사항)| 1.19.2

- 운영 체제

Prisma ORM은 macOS, Windows 및 대부분의 Linux 배포판에서 지원됩니다.

#

- Linux 런타임 종속성

Prisma ORM이 동작하려면 다음 시스템 라이브러리가 설치되어 있어야 합니다:

- OpenSSL 1.0.x, 1.1.x 또는 3.x
- zlib (`libz.so.1`)
- libgcc (`libgcc_s.so.1`)
- C 표준 라이브러리(대부분의 Linux 배포판에서는 glibc, Alpine Linux에서는 musl libc)

다음 두 표는 CPU 아키텍처별로 지원되는 Linux 배포판 계열, OpenSSL 버전, C 표준 라이브러리를 보여줍니다.

`AMD64` (`x86_64`) 아키텍처의 경우:

| Distro family    | OpenSSL version   | libc version |
| ---------------- | ----------------- | ------------ |
| Alpine           | 1.1.x, 3.x        | musl 1.2.x   |
| RHEL             | 1.0.x, 1.1.x, 3.x | glibc 2.17+  |
| Debian or others | 1.0.x             | glibc 2.19+  |
| Debian or others | 1.1.x, 3.x        | glibc 2.24+  |

`ARM64` (`aarch64`) 아키텍처의 경우:

| Distro family    | OpenSSL version   | libc version |
| ---------------- | ----------------- | ------------ |
| Alpine           | 1.1.x, 3.x        | musl 1.2.x   |
| RHEL             | 1.0.x, 1.1.x, 3.x | glibc 2.24+  |
| Debian or others | 1.0.x, 1.1.x, 3.x | glibc 2.24+  |

Prisma ORM이 시스템에서 OpenSSL 버전을 확인할 수 없는 경우(예: 설치되어 있지 않은 경우), 기본값으로 OpenSSL 1.1.x를 사용합니다.

지원되는 Node.js 버전을 실행할 수 있는 시스템이라면 대체로 zlib와 libgcc를 사용할 수 있습니다. 주목할 만한 예외는 Google Distroless 이미지이며, 이 경우 `libz.so.1`을 호환되는 Debian 시스템에서 복사해야 합니다.

#

- Windows 런타임 종속성

Windows에서는 [Microsoft Visual C++ Redistributable 2015](https://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x64.exe) 이상이 설치되어 있어야 합니다(대부분의 최신 설치 환경에서는 기본적으로 충족됨).

#

- macOS 런타임 종속성

Prisma ORM은 macOS 10.15 이상을 지원합니다. macOS에서는 모든 플랫폼 공통 요구 사항인 [소프트웨어 요구 사항](https://docs.prisma.io/docs/orm/reference/system-requirements#software-requirements) 섹션에 나열된 항목 외에 추가적인 플랫폼별 요구 사항이 없습니다.

## 문제 해결

시스템 요구 사항의 오래된 버전을 사용하여 발생하는 일반적인 문제가 몇 가지 있습니다:

- `@prisma/client`로 TypeScript 프로젝트를 빌드할 수 없음

#

- 문제

`prisma generate`를 실행한 뒤 프로젝트 타입 체크를 시도하면 다음 오류가 표시됩니다.

```
    ./node_modules/.prisma/client/index.d.ts:10:33
    Type error: Type expected.
       8 | export type PrismaPromise<A> = Promise<A> & {[prisma]: true}
       9 | type UnwrapTuple<Tuple extends readonly unknown[]> = {
    > 10 |   [K in keyof Tuple]: K extends `${number}` ? Tuple[K] extends PrismaPromise<infer X> ? X : never : never
         |                                 ^
      11 | };
      12 |
      13 |
```

#

- 해결 방법

프로젝트의 TypeScript 종속성을 [Prisma ORM이 지원하는 버전](https://docs.prisma.io/docs/orm/reference/system-requirements#software-requirements)으로 업그레이드하세요. `npm install -D typescript`.

- `groupBy` 프리뷰 기능을 사용할 수 없음

#

- 문제

`groupBy` 프리뷰 기능을 사용하는 앱을 실행하려고 하면 다음 콘솔 오류가 표시됩니다:

```
    server.ts:6:25 - error TS2615: Type of property 'OR' circularly references itself in mapped type '{ [K in keyof { AND?: Enumerable<ProductScalarWhereWithAggregatesInput>; OR?: Enumerable<ProductScalarWhereWithAggregatesInput>; ... 4 more ...; category?: string | StringWithAggregatesFilter; }]: Or<...> extends 1 ? { ...; }[K] extends infer TK ? GetHavingFields<...> : never : {} extends FieldPaths<...> ? never : K...'.
    6   const grouped = await prisma.product.groupBy({
                              ~~~~~~~~~~~~~~~~~~~~~~~~
    7     by: ['category']
      ~~~~~~~~~~~~~~~~~~~~
    8   });
      ~~~~
    server.ts:6:48 - error TS2554: Expected 0 arguments, but got 1.
    6   const grouped = await prisma.product.groupBy({
                                                     ~
    7     by: ['category']
      ~~~~~~~~~~~~~~~~~~~~
    8   });
      ~~~
```

#

- 해결 방법

프로젝트의 TypeScript 종속성을 [Prisma ORM이 지원하는 버전](https://docs.prisma.io/docs/orm/reference/system-requirements#software-requirements)으로 업그레이드하세요. `npm install -D typescript`.
