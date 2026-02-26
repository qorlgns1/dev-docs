---
title: "Postgres"
description: "Postgres 데이터베이스용 스키마입니다."
---

원문 URL: https://next-auth.js.org/v3/adapters/typeorm/postgres

# Postgres | NextAuth.js

버전: v3

Postgres 데이터베이스용 스키마입니다.

참고

기본 어댑터(TypeORM)와 함께 Postgres 데이터베이스를 사용할 때, `timestamp` 타입의 모든 속성은 `timestamp with time zone`/`timestamptz`로 변환되며 모든 타임스탬프는 UTC로 저장됩니다.

이 변환은 커스텀 모델을 사용할 때 `timestamp` 타입의 모든 속성에도 적용됩니다.

```
    CREATE TABLE accounts
      (
        id                   SERIAL,
        compound_id          VARCHAR(255) NOT NULL,
        user_id              INTEGER NOT NULL,
        provider_type        VARCHAR(255) NOT NULL,
        provider_id          VARCHAR(255) NOT NULL,
        provider_account_id  VARCHAR(255) NOT NULL,
        refresh_token        TEXT,
        access_token         TEXT,
        access_token_expires TIMESTAMPTZ,
        created_at           TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at           TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
      );

    CREATE TABLE sessions
      (
        id            SERIAL,
        user_id       INTEGER NOT NULL,
        expires       TIMESTAMPTZ NOT NULL,
        session_token VARCHAR(255) NOT NULL,
        access_token  VARCHAR(255) NOT NULL,
        created_at    TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at    TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
      );

    CREATE TABLE users
      (
        id             SERIAL,
        name           VARCHAR(255),
        email          VARCHAR(255),
        email_verified TIMESTAMPTZ,
        image          TEXT,
        created_at     TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at     TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
      );

    CREATE TABLE verification_requests
      (
        id         SERIAL,
        identifier VARCHAR(255) NOT NULL,
        token      VARCHAR(255) NOT NULL,
        expires    TIMESTAMPTZ NOT NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
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
