---
title: "TypeORM 커스텀 모델"
description: "원본 URL: https://next-auth.js.org/v3/tutorials/typeorm-custom-models"
---

원본 URL: https://next-auth.js.org/v3/tutorials/typeorm-custom-models

# TypeORM 커스텀 모델 | NextAuth.js

버전: v3

NextAuth.js는 내장 TypeORM 어댑터용 [모델 및 스키마](https://authjs.dev/reference/adapters#models) 세트를 제공하며, 이를 쉽게 확장할 수 있습니다.

이 모델들은 MySQL, MariaDB, Postgres, MongoDB, SQLite와 함께 사용할 수 있습니다.

## 커스텀 모델 생성하기[​](https://next-auth.js.org/v3/tutorials/typeorm-custom-models#creating-custom-models "헤딩으로 바로 가기")

models/User.js

```
    import Adapters from "next-auth/adapters"

    // Extend the built-in models using class inheritance
    export default class User extends Adapters.TypeORM.Models.User.model {
      // You can extend the options in a model but you should not remove the base
      // properties or change the order of the built-in options on the constructor
      constructor(name, email, image, emailVerified) {
        super(name, email, image, emailVerified)
      }
    }

    export const UserSchema = {
      name: "User",
      target: User,
      columns: {
        ...Adapters.TypeORM.Models.User.schema.columns,
        // Adds a phoneNumber to the User schema
        phoneNumber: {
          type: "varchar",
          nullable: true,
        },
      },
    }

```

models/index.js

```
    // To make importing them easier, you can export all models from single file
    import User, { UserSchema } from "./User"

    export default {
      User: {
        model: User,
        schema: UserSchema,
      },
    }

```

참고

[내장 TypeORM 모델 및 스키마 소스 보기](https://github.com/nextauthjs/adapters/tree/canary/packages/typeorm-legacy/src/models)

## 커스텀 모델 사용하기[​](https://next-auth.js.org/v3/tutorials/typeorm-custom-models#using-custom-models "헤딩으로 바로 가기")

TypeORM 어댑터를 명시적으로 지정하고 옵션으로 전달하여 커스텀 모델을 사용할 수 있습니다.

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"
    import Adapters from "next-auth/adapters"

    import Models from "../../../models"

    export default NextAuth({
      providers: [
        // Your providers
      ],

      adapter: Adapters.TypeORM.Adapter(
        // The first argument should be a database connection string or TypeORM config object
        "mysql://username:password@127.0.0.1:3306/database_name",
        // The second argument can be used to pass custom models and schemas
        {
          models: {
            User: Models.User,
          },
        }
      ),
    })

```
