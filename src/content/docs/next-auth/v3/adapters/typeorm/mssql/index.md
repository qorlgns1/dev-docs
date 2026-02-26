---
title: "Microsoft SQL Server"
description: "Microsoft SQL Server(mssql) 데이터베이스용 스키마입니다."
---

소스 URL: https://next-auth.js.org/v3/adapters/typeorm/mssql

# Microsoft SQL Server | NextAuth.js

버전: v3

Microsoft SQL Server(mssql) 데이터베이스용 스키마입니다.

참고

기본 어댑터(TypeORM)와 함께 Microsoft SQL Server 데이터베이스를 사용할 때, `timestamp` 타입의 모든 속성은 `datetime`으로 변환됩니다.

이 변환은 커스텀 모델을 사용할 때 `timestamp` 타입의 모든 속성에도 동일하게 적용됩니다.

```
    CREATE TABLE accounts
      (
        id                    int IDENTITY(1,1) NOT NULL,
        compound_id           varchar(255) NOT NULL,
        user_id               int NOT NULL,
        provider_type         varchar(255) NOT NULL,
        provider_id           varchar(255) NOT NULL,
        provider_account_id   varchar(255) NOT NULL,
        refresh_token         text NULL,
        access_token          text NULL,
        access_token_expires  datetime NULL,
        created_at            datetime NOT NULL DEFAULT getdate(),
        updated_at            datetime NOT NULL DEFAULT getdate()
      );

    CREATE TABLE sessions
      (
        id            int IDENTITY(1,1) NOT NULL,
        user_id       int NOT NULL,
        expires       datetime NOT NULL,
        session_token varchar(255) NOT NULL,
        access_token  varchar(255) NOT NULL,
        created_at    datetime NOT NULL DEFAULT getdate(),
        updated_at    datetime NOT NULL DEFAULT getdate()
      );

    CREATE TABLE users
      (
        id              int IDENTITY(1,1) NOT NULL,
        name            varchar(255) NULL,
        email           varchar(255) NULL,
        email_verified  datetime NULL,
        image           varchar(255) NULL,
        created_at      datetime NOT NULL DEFAULT getdate(),
        updated_at      datetime NOT NULL DEFAULT getdate()
      );

    CREATE TABLE verification_requests
      (
        id          int IDENTITY(1,1) NOT NULL,
        identifier  varchar(255) NOT NULL,
        token       varchar(255) NOT NULL,
        expires     datetime NOT NULL,
        created_at  datetime NOT NULL DEFAULT getdate(),
        updated_at  datetime NOT NULL DEFAULT getdate()
      );

    CREATE UNIQUE INDEX compound_id
      ON accounts(compound_id);

    CREATE INDEX provider_account_id
      ON accounts(provider_account_id);

    CREATE INDEX provider_id
      ON accounts(provider_id);

    CREATE INDEX user_id
      ON accounts(user_id);

    CREATE UNIQUE INDEX session_token
      ON sessions(session_token);

    CREATE UNIQUE INDEX access_token
      ON sessions(access_token);

    CREATE UNIQUE INDEX email
      ON users(email);

    CREATE UNIQUE INDEX token
      ON verification_requests(token);

```

NextAuth.js를 SQL Server와 처음 함께 사용할 때는 연결 문자열에 `?synchronize=true`를 붙여 데이터베이스에 대해 NextAuth.js를 한 번 실행한 뒤, 생성된 스키마를 내보내세요. :::
