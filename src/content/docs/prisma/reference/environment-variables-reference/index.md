---
title: "환경 변수"
description: "이 문서는 다양한 환경 변수와 그 사용 사례를 설명합니다."
---

출처 URL: https://docs.prisma.io/docs/orm/reference/environment-variables-reference

# 환경 변수

Prisma 환경 변수 레퍼런스

이 문서는 다양한 환경 변수와 그 사용 사례를 설명합니다.

## Prisma Client

- `DEBUG`

`DEBUG`는 Prisma Client에서 디버깅 출력을 활성화하는 데 사용됩니다.

Prisma Client 수준의 디버깅 출력을 설정하는 예시:

```
    # enable only `prisma:client`-level debugging output
    export DEBUG="prisma:client"
```

자세한 내용은 [Debugging](https://docs.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging)을 참고하세요.

- `NO_COLOR`

`NO_COLOR`가 [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy) 값이면 오류 포맷팅에 `colorless` 설정이 활성화되고 오류 메시지에서 색상이 제거됩니다.

자세한 내용은 [Formatting via environment variables](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/error-formatting#formatting-via-environment-variables)를 참고하세요.

## Prisma Studio

- `BROWSER`

`BROWSER`는 Prisma Studio에서 어떤 브라우저로 열지 강제하는 데 사용되며, 설정하지 않으면 기본 브라우저로 열립니다.

```
    BROWSER=firefox prisma studio --port 5555
```

또는 CLI에서 Studio를 시작할 때도 이를 설정할 수 있습니다:

```
    prisma studio --browser firefox
```

자세한 내용은 [Studio](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#studio) 문서를 참고하세요.

## Prisma CLI

- `PRISMA_HIDE_PREVIEW_FLAG_WARNINGS`

`PRISMA_HIDE_PREVIEW_FLAG_WARNINGS`는 preview 기능 플래그를 제거할 수 있다는 경고 메시지를 숨깁니다. truthy 값입니다.

- `PRISMA_HIDE_UPDATE_MESSAGE`

`PRISMA_HIDE_UPDATE_MESSAGE`는 더 최신 Prisma CLI 버전을 사용할 수 있을 때 표시되는 업데이트 알림 메시지를 숨기는 데 사용됩니다. truthy 값입니다.

- `PRISMA_DISABLE_WARNINGS`

`logger.warn`에서 생성되는 모든 CLI 경고를 비활성화합니다.

- `PRISMA_SCHEMA_DISABLE_ADVISORY_LOCK`

Prisma Migrate에서 사용하는 [advisory locking](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production#advisory-locking)을 비활성화합니다. Percona-XtraDB-Cluster 또는 MariaDB Galera Cluster 같은 특정 데이터베이스 구성에서 유용합니다.

## 프록시 환경 변수

Prisma CLI는 Prisma 엔진을 다운로드하기 위해 사용자 지정 HTTP(S) 프록시를 지원합니다. 이는 기업 방화벽 뒤에서 작업할 때 유용할 수 있습니다. 자세한 내용은 [Using a HTTP proxy for the CLI](https://docs.prisma.io/docs/orm/reference/prisma-cli-reference#using-a-http-proxy-for-the-cli)를 참고하세요.

- `NO_PROXY`

`NO_PROXY`는 프록시가 필요하지 않은 호스트명 또는 IP 주소의 쉼표로 구분된 목록입니다.

```
    NO_PROXY=myhostname.com,10.11.12.0/16,172.30.0.0/16
```

- `HTTP_PROXY`

`HTTP_PROXY`는 프록시 서버의 호스트명 또는 IP 주소로 설정됩니다.

```
    HTTP_PROXY=http://proxy.example.com
```

- `HTTPS_PROXY`

`HTTPS_PROXY`는 프록시 서버의 호스트명 또는 IP 주소로 설정됩니다.

```
    HTTPS_PROXY=https://proxy.example.com
```
