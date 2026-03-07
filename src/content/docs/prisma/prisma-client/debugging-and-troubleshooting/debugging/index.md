---
title: "DEBUG 환경 변수 설정"
description: "이 페이지에서는  환경 변수를 설정하여 Prisma Client의 디버깅 출력을 활성화하는 방법을 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging

# 디버깅

이 페이지에서는 `DEBUG` 환경 변수를 설정하여 Prisma Client의 디버깅 출력을 활성화하는 방법을 설명합니다.

Prisma Client와 Prisma CLI에서는 [`DEBUG`](https://docs.prisma.io/docs/orm/reference/environment-variables-reference#debug) 환경 변수를 통해 디버깅 출력을 활성화할 수 있습니다. 이 변수는 디버깅 출력을 표시하기 위해 두 가지 네임스페이스를 받습니다.

- `prisma:engine`: Prisma ORM [engine](https://github.com/prisma/prisma-engines/)에서 발생하는 관련 디버그 메시지를 출력합니다.
- `prisma:client`: Prisma Client 런타임에서 발생하는 관련 디버그 메시지를 출력합니다.
- `prisma*`: Prisma Client 또는 CLI의 모든 디버그 메시지를 출력합니다.
- `*`: 모든 디버그 메시지를 출력합니다.

Prisma Client는 데이터베이스로 전송된 쿼리와 관련된 경고, 오류, 정보 로그를 남기도록 구성할 수 있습니다. 자세한 내용은 [로깅 구성](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/logging)을 참고하세요.

## `DEBUG` 환경 변수 설정

다음은 bash에서 이러한 디버깅 옵션을 설정하는 예시입니다.

```
    # enable only `prisma:engine`-level debugging output
    export DEBUG="prisma:engine"

    # enable only `prisma:client`-level debugging output
    export DEBUG="prisma:client"

    # enable both `prisma-client`- and `engine`-level debugging output
    export DEBUG="prisma:client,prisma:engine"
```

모든 `prisma` 디버깅 옵션을 활성화하려면 `DEBUG`를 `prisma*`로 설정하세요.

```
    export DEBUG="prisma*"
```

Windows에서는 `export` 대신 `set`을 사용하세요.

```
    set DEBUG="prisma*"
```

_모든_ 디버깅 옵션을 활성화하려면 `DEBUG`를 `*`로 설정하세요.

```
    export DEBUG="*"
```
