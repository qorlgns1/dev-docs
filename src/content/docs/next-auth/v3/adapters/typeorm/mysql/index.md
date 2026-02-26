---
title: "MySQL"
description: "MySQL 데이터베이스용 스키마입니다."
---

Source URL: https://next-auth.js.org/v3/adapters/typeorm/mysql

# MySQL | NextAuth.js

버전: v3

MySQL 데이터베이스용 스키마입니다.

참고

기본 어댑터(TypeORM)와 함께 MySQL 데이터베이스를 사용할 때, 모든 타임스탬프 컬럼은 6자리 정밀도를 사용하며(스키마에서 `precision`에 다른 값을 지정하지 않은 경우), 타임존은 `Z`(즉 Zulu Time / UTC)로 설정되고 모든 타임스탬프는 UTC로 저장됩니다.

```
    CREATE TABLE accounts
      (
        id                   INT NOT NULL AUTO_INCREMENT,
        compound_id          VARCHAR(255) NOT NULL,
        user_id              INTEGER NOT NULL,
        provider_type        VARCHAR(255) NOT NULL,
        provider_id          VARCHAR(255) NOT NULL,
        provider_account_id  VARCHAR(255) NOT NULL,
        refresh_token        TEXT,
        access_token         TEXT,
        access_token_expires TIMESTAMP(6),
        created_at           TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
        updated_at           TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
        PRIMARY KEY (id)
      );

    CREATE TABLE sessions
      (
        id            INT NOT NULL AUTO_INCREMENT,
        user_id       INTEGER NOT NULL,
        expires       TIMESTAMP(6) NOT NULL,
        session_token VARCHAR(255) NOT NULL,
        access_token  VARCHAR(255) NOT NULL,
        created_at    TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
        updated_at    TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
        PRIMARY KEY (id)
      );

    CREATE TABLE users
      (
        id             INT NOT NULL AUTO_INCREMENT,
        name           VARCHAR(255),
        email          VARCHAR(255),
        email_verified TIMESTAMP(6),
        image          VARCHAR(255),
        created_at     TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
        updated_at     TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
        PRIMARY KEY (id)
      );

    CREATE TABLE verification_requests
      (
        id         INT NOT NULL AUTO_INCREMENT,
        identifier VARCHAR(255) NOT NULL,
        token      VARCHAR(255) NOT NULL,
        expires    TIMESTAMP(6) NOT NULL,
        created_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
        updated_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
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
