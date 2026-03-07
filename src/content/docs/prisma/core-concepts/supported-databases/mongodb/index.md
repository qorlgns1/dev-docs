---
title: "MongoDB"
description: "Prisma ORM이 MongoDB 데이터베이스에 연결하는 방법"
---

출처 URL: https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb

# MongoDB

Prisma ORM이 MongoDB 데이터베이스에 연결하는 방법

이 가이드는 Prisma ORM과 MongoDB를 함께 사용할 때의 핵심 개념을 설명하고, MongoDB와 다른 데이터베이스 제공자 간의 공통점과 차이점을 정리하며, Prisma ORM을 사용해 애플리케이션을 MongoDB와 통합하도록 설정하는 과정을 안내합니다.

Prisma ORM v7의 MongoDB 지원

**Prisma ORM v7의 MongoDB 지원은 가까운 시일 내에 제공될 예정입니다.** 그때까지는 MongoDB 작업 시 **Prisma ORM v6.19**(최신 v6 릴리스)를 사용해 주세요.

MongoDB에서 Prisma ORM v6.19를 사용하는 시작 가이드는 다음을 참고하세요:

- MongoDB 빠른 시작
- 기존 MongoDB 프로젝트에 추가

## MongoDB란 무엇인가요?

[MongoDB](https://www.mongodb.com/)는 [BSON](https://bsonspec.org/) 형식으로 데이터를 저장하는 NoSQL 데이터베이스입니다. BSON은 키-값 쌍으로 데이터를 저장하도록 설계된 JSON 유사 문서 형식입니다. 문서 모델이 애플리케이션 코드의 객체에 쉽게 매핑되고, 고가용성 및 수평 확장을 기본 지원하기 때문에 JavaScript 애플리케이션 개발에서 흔히 사용됩니다.

MongoDB는 관계형 데이터베이스의 테이블처럼 사전에 스키마를 정의할 필요가 없는 컬렉션에 데이터를 저장합니다. 각 컬렉션의 구조도 시간에 따라 변경할 수 있습니다. 이러한 유연성은 데이터 모델을 빠르게 반복 개선할 수 있게 해주지만, Prisma ORM으로 MongoDB 데이터베이스를 사용할 때 유의해야 할 여러 차이점이 있음을 의미합니다.

## 다른 데이터베이스 제공자와의 공통점

MongoDB에서 Prisma ORM을 사용하는 일부 측면은 관계형 데이터베이스에서 Prisma ORM을 사용할 때와 동일합니다. 여전히 다음이 가능합니다:

- [Prisma Schema Language](https://docs.prisma.io/docs/orm/prisma-schema/overview)로 데이터베이스 모델링
- [`mongodb` database connector](https://docs.prisma.io/docs/orm/core-concepts/supported-databases)를 사용해 데이터베이스 연결
- 이미 MongoDB 데이터베이스가 있는 기존 프로젝트에서 [Introspection](https://docs.prisma.io/docs/orm/prisma-schema/introspection) 사용
- [`db push`](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema)를 사용해 스키마 변경사항을 데이터베이스에 반영
- Prisma Schema 기반의 타입 안전한 방식으로 애플리케이션에서 데이터베이스를 조회하기 위해 [Prisma Client](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction) 사용

## 고려해야 할 차이점

MongoDB의 문서 기반 구조와 유연한 스키마 때문에, MongoDB에서 Prisma ORM을 사용하는 방식은 관계형 데이터베이스와 여러 면에서 다릅니다. 다음은 반드시 인지해야 할 차이 영역입니다:

- **ID 정의** : MongoDB 문서에는 `_id` 필드가 있습니다(대개 [ObjectID](https://www.mongodb.com/docs/manual/reference/bson-types/#std-label-objectid)를 포함). Prisma ORM은 `_`로 시작하는 필드를 지원하지 않으므로, `@map` 속성을 사용해 Prisma ORM 필드로 매핑해야 합니다. 자세한 내용은 [MongoDB에서 ID 정의하기](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-ids-in-mongodb)를 참고하세요.

- **Prisma 스키마에 맞게 기존 데이터 마이그레이션** : 관계형 데이터베이스에서는 모든 데이터가 스키마와 일치해야 합니다. 마이그레이션 시 스키마의 특정 필드 타입을 변경하면, 모든 데이터도 이에 맞게 업데이트되어야 합니다. 반면 MongoDB는 특정 스키마를 강제하지 않으므로 마이그레이션 시 주의가 필요합니다. 자세한 내용은 [기존 데이터를 새 스키마로 마이그레이션하는 방법](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb#how-to-migrate-existing-data-to-match-your-prisma-schema)을 참고하세요.

- **Introspection과 Prisma ORM 관계** : 기존 MongoDB 데이터베이스를 introspect하면 관계가 없는 스키마가 생성되며, 누락된 관계를 수동으로 추가해야 합니다. 자세한 내용은 [Introspection 후 누락된 관계를 추가하는 방법](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb#how-to-add-in-missing-relations-after-introspection)을 참고하세요.

- **`null` 및 누락 필드 필터링**: MongoDB는 필드를 `null`로 설정한 경우와 아예 설정하지 않은 경우를 구분하며, 이는 관계형 데이터베이스에는 없는 개념입니다. 현재 Prisma ORM은 이 구분을 표현하지 않으므로, `null` 및 누락 필드를 필터링할 때 주의해야 합니다. 자세한 내용은 [ `null` 및 누락 필드 필터링 방법](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb#how-to-filter-for-null-and-missing-fields)을 참고하세요.

- **복제 활성화** : Prisma ORM은 중첩 쿼리에서 부분 쓰기를 방지하기 위해 내부적으로 [MongoDB transactions](https://www.mongodb.com/docs/manual/core/transactions/)을 사용합니다. 트랜잭션 사용 시 MongoDB는 데이터셋 복제가 활성화되어 있어야 합니다. 이를 위해 동일한 데이터셋을 유지하는 MongoDB 프로세스 그룹인 [replica set](https://www.mongodb.com/docs/manual/replication/)을 구성해야 합니다. 노드 1개만 포함한 replica set을 구성하면 단일 데이터베이스도 사용할 수 있습니다. MongoDB의 [Atlas](https://www.mongodb.com/atlas/database) 호스팅 서비스를 사용하면 replica set이 자동 구성되지만, 로컬에서 MongoDB를 실행하는 경우에는 직접 replica set을 설정해야 합니다. 자세한 내용은 MongoDB의 [replica set 배포 가이드](https://www.mongodb.com/docs/manual/tutorial/deploy-replica-set/)를 참고하세요.

* 대규모 컬렉션의 성능 고려사항

#

- 문제

Prisma를 통해 대규모 MongoDB 컬렉션을 다룰 때 특정 작업이 느려지고 리소스를 많이 사용할 수 있습니다. 특히 `count()`처럼 전체 컬렉션 스캔이 필요한 작업은 쿼리 실행 시간 제한에 걸릴 수 있으며, 데이터셋이 커질수록 성능에 큰 영향을 줄 수 있습니다.

#

- 해결책

대규모 MongoDB 컬렉션의 성능 문제를 해결하기 위해 다음 접근 방식을 고려하세요:

1. 대규모 컬렉션에서는 `count()` 대신 MongoDB의 `estimatedDocumentCount()` 사용을 고려하세요. 이 메서드는 컬렉션 메타데이터를 사용하므로 훨씬 빠릅니다. Prisma의 `runCommandRaw` 메서드를 사용해 이 명령을 실행할 수 있습니다.

2. 자주 조회되는 카운트의 경우 카운터 캐시 구현을 고려하세요. 이는 사전 계산된 카운트를 별도 문서로 유지하고, 문서가 추가되거나 제거될 때마다 해당 값을 업데이트하는 방식입니다.

## MongoDB에서 Prisma ORM 사용하는 방법

이 섹션에서는 MongoDB에 특화된 단계가 필요한 작업을 수행하는 방법을 안내합니다.

- 기존 데이터를 Prisma 스키마에 맞게 마이그레이션하는 방법

시간이 지나며 데이터베이스를 마이그레이션하는 일은 개발 사이클의 중요한 부분입니다. 개발 중에는 Prisma 스키마를 업데이트하고(예: 새 필드 추가), 개발 환경 데이터베이스의 데이터를 업데이트한 뒤, 최종적으로 업데이트된 스키마와 새 데이터를 프로덕션 데이터베이스에 반영해야 합니다.

스키마와 데이터베이스를 반복적으로 업데이트하는 작업은 스키마와 실제 데이터 간 불일치를 초래할 수 있습니다. 이런 상황이 발생할 수 있는 한 가지 시나리오를 살펴보고, 이러한 불일치를 처리하기 위해 팀에서 고려할 수 있는 몇 가지 전략을 살펴보겠습니다.

**시나리오** : 사용자에 대해 이메일뿐 아니라 전화번호도 포함해야 합니다. 현재 `schema.prisma` 파일에는 다음과 같은 `User` 모델이 있습니다:

prisma/schema.prisma

```
    model User {
      id    String @id @default(auto()) @map("_id") @db.ObjectId
      email String
    }
```

이 스키마를 마이그레이션하기 위해 사용할 수 있는 전략은 여러 가지가 있습니다:

- **"On-demand" 업데이트** : 이 전략에서는 필요에 따라 스키마 업데이트를 진행하기로 팀이 합의합니다. 다만 데이터와 스키마 불일치로 인한 마이그레이션 실패를 방지하기 위해, 새로 추가되는 필드는 반드시 optional로 명시하기로 팀 내에서 합의합니다.

위 시나리오에서는 Prisma 스키마의 `User` 모델에 optional `phoneNumber` 필드를 추가할 수 있습니다:

prisma/schema.prisma

```
model User {
          id          String  @id @default(auto()) @map("_id") @db.ObjectId
          email       String
          phoneNumber String?
        }
```

그런 다음 `npx prisma generate` 명령으로 Prisma Client를 다시 생성합니다.

다음으로 애플리케이션을 새 필드에 맞게 업데이트하고 앱을 재배포합니다.

`phoneNumber` 필드는 optional이므로, 전화번호가 아직 정의되지 않은 기존 사용자도 계속 조회할 수 있습니다. 애플리케이션 사용자들이 새 필드에 전화번호를 입력하기 시작하면 데이터베이스 레코드는 "on demand" 방식으로 업데이트됩니다.

또 다른 방법은 required 필드에 기본값을 추가하는 것입니다. 예:

prisma/schema.prisma

```
model User {
          id          String @id @default(auto()) @map("_id") @db.ObjectId
          email       String
          phoneNumber String @default("000-000-0000")
        }
```

이후 누락된 `phoneNumber`를 만나면 값이 `000-000-0000`으로 강제 변환됩니다.

- **"No breaking changes" 업데이트** : 이 전략은 첫 번째 전략을 확장한 것으로, 팀 내에서 필드 이름 변경이나 삭제는 하지 않고 새 필드만 추가하며, 새 필드는 항상 optional로 정의한다는 추가 합의를 포함합니다. 이 정책은 CI/CD 프로세스에 검사 단계를 추가해 스키마에 하위 호환되지 않는 변경이 없는지 검증함으로써 강화할 수 있습니다.

- **"All-at-once" 업데이트** : 이 전략은 관계형 데이터베이스의 전통적인 마이그레이션과 유사하게, 새 스키마를 반영하도록 모든 데이터를 한 번에 업데이트합니다. 위 시나리오에서는 데이터베이스의 기존 모든 사용자에게 전화번호 필드 값을 추가하는 스크립트를 작성합니다. 그러면 스키마와 데이터가 일치하므로 애플리케이션에서 해당 필드를 required 필드로 만들 수 있습니다.

* Introspection 후 누락된 관계를 추가하는 방법

기존 MongoDB 데이터베이스를 introspect한 후에는 모델 간 관계를 수동으로 추가해야 합니다. MongoDB에는 관계형 데이터베이스처럼 외래 키를 통해 관계를 정의하는 개념이 없습니다. 그러나 MongoDB 컬렉션에 다른 컬렉션의 ID 필드와 일치하는 "foreign-key-like" 필드가 있다면, Prisma ORM을 통해 컬렉션 간 관계를 에뮬레이션할 수 있습니다.

예를 들어 `User`와 `Post` 두 컬렉션이 있는 MongoDB 데이터베이스를 보겠습니다. 이 컬렉션의 데이터는 `userId` 필드로 사용자와 게시물을 연결하며 다음 형식을 가집니다:

`User` 컬렉션:

- `objectId` 타입의 `_id` 필드
- `string` 타입의 `email` 필드

`Post` 컬렉션:

- `objectId` 타입의 `_id` 필드
- `string` 타입의 `title` 필드
- `objectID` 타입의 `userId`

`db pull`로 introspection하면 Prisma Schema에는 다음과 같이 반영됩니다:

prisma/schema.prisma

```
    model Post {
      id     String @id @default(auto()) @map("_id") @db.ObjectId
      title  String
      userId String @db.ObjectId
    }

    model User {
      id    String @id @default(auto()) @map("_id") @db.ObjectId
      email String
    }
```

여기에는 `User`와 `Post` 모델 간 관계가 누락되어 있습니다. 이를 해결하려면 `Post` 모델에 `userId`를 `fields` 값으로 사용하는 `@relation` 속성과 함께 `user` 필드를 수동으로 추가해 `User` 모델에 연결하고, `User` 모델에는 역참조 관계인 `posts` 필드를 추가하세요:

prisma/schema.prisma

```
    model Post {
      id     String @id @default(auto()) @map("_id") @db.ObjectId
      title  String
      userId String @db.ObjectId
      user   User   @relation(fields: [userId], references: [id])
    }

    model User {
      id    String @id @default(auto()) @map("_id") @db.ObjectId
      email String
      posts Post[]
    }
```

Prisma ORM에서 관계를 사용하는 방법에 대한 자세한 내용은 [공식 문서](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations)를 참고하세요.

- `null` 및 누락된 필드를 필터링하는 방법

MongoDB가 `null`과 누락된 필드를 어떻게 구분하는지 이해하려면, 선택적 `name` 필드가 있는 `User` 모델 예시를 살펴보세요:

```
    model User {
      id    String  @id @default(auto()) @map("_id") @db.ObjectId
      email String
      name  String?
    }
```

먼저 `name` 필드를 명시적으로 `null`로 설정한 레코드를 생성해 보세요. Prisma ORM은 예상대로 `name: null`을 반환합니다:

```
    const createNull = await prisma.user.create({
      data: {
        email: "user1@prisma.io",
        name: null,
      },
    });
    console.log(createNull);
```

```
    {
      id: '6242c4ae032bc76da250b207',
      email: 'user1@prisma.io',
      name: null
    }
```

MongoDB 데이터베이스를 직접 확인해 보면, `name`이 `null`로 설정된 새 레코드도 확인할 수 있습니다:

```
    {
      "_id": "6242c4af032bc76da250b207",
      "email": "user1@prisma.io",
      "name": null
    }
```

다음으로 `name` 필드를 명시적으로 설정하지 않고 레코드를 생성해 보세요:

```
    const createMissing = await prisma.user.create({
      data: {
        email: "user2@prisma.io",
      },
    });
    console.log(createMissing);
```

```
    {
      id: '6242c4ae032bc76da250b208',
      email: 'user2@prisma.io',
      name: null
    }
```

Prisma ORM은 여전히 `name: null`을 반환하지만, 데이터베이스를 직접 보면 해당 레코드에는 `name` 필드가 전혀 정의되어 있지 않음을 확인할 수 있습니다:

```
    {
      "_id": "6242c4af032bc76da250b208",
      "email": "user2@prisma.io"
    }
```

Prisma ORM이 두 경우 모두 동일한 결과를 반환하는 이유는, 현재 MongoDB에서 기본 데이터베이스 기준으로 `null`인 필드와 아예 정의되지 않은 필드를 구분해 지정할 방법이 없기 때문입니다. 자세한 내용은 [이 Github 이슈](https://github.com/prisma/prisma/issues/12555)를 참고하세요.

즉, 현재는 `null`과 누락된 필드를 필터링할 때 주의가 필요합니다. `name: null`로 레코드를 필터링하면 `name`이 명시적으로 `null`로 설정된 첫 번째 레코드만 반환됩니다:

```
    const findNulls = await prisma.user.findMany({
      where: {
        name: null,
      },
    });
    console.log(findNulls);
```

```
    [
      {
        id: '6242c4ae032bc76da250b207',
        email: 'user1@prisma.io',
        name: null
      }
    ]
```

이는 `name: null`이 동등성 검사를 수행하며, 존재하지 않는 필드는 `null`과 같지 않기 때문입니다.

누락된 필드도 포함하려면 [`isSet` 필터](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#isset)를 사용해 `null`이거나 설정되지 않은 필드를 명시적으로 검색하세요. 그러면 두 레코드가 모두 반환됩니다:

```
    const findNullOrMissing = await prisma.user.findMany({
      where: {
        OR: [
          {
            name: null,
          },
          {
            name: {
              isSet: false,
            },
          },
        ],
      },
    });
    console.log(findNullOrMissing);
```

```
    [
      {
        id: '6242c4ae032bc76da250b207',
        email: 'user1@prisma.io',
        name: null
      },
      {
        id: '6242c4ae032bc76da250b208',
        email: 'user2@prisma.io',
        name: null
      }
    ]
```

## Prisma ORM과 함께 MongoDB 사용하기 더 알아보기

MongoDB와 Prisma ORM을 가장 빠르게 시작하는 방법은 Getting Started 문서를 참고하는 것입니다:

- 처음부터 시작하기
- 기존 프로젝트에 추가하기

이 튜토리얼에서는 MongoDB 연결, 스키마 변경사항 푸시, Prisma Client 사용 과정을 안내합니다.

추가 참고 정보는 [MongoDB 커넥터 문서](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb)에서 확인할 수 있습니다.

MongoDB 데이터베이스 설정 및 관리에 대한 자세한 내용은 [Prisma Data Guide](https://www.prisma.io/dataguide#mongodb)를 참고하세요.

## 예시

MongoDB 서버에 연결하려면 [Prisma Schema](https://docs.prisma.io/docs/orm/prisma-schema/overview)에서 [`datasource`](https://docs.prisma.io/docs/orm/prisma-schema/overview/data-sources) 블록을 구성하세요:

schema.prisma

```
    datasource db {
      provider = "mongodb"
      url      = env("DATABASE_URL")
    }
```

`datasource` 블록에 전달되는 필드는 다음과 같습니다:

- `provider`: `mongodb` 데이터 소스 커넥터를 지정합니다.
- `url`: MongoDB 서버의 [연결 URL](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb#connection-url)을 지정합니다. 이 경우 연결 URL 제공을 위해 [환경 변수](https://docs.prisma.io/docs/orm/more/dev-environment/environment-variables)를 사용합니다.

MongoDB 데이터베이스 커넥터는 중첩 쓰기를 지원하기 위해 트랜잭션을 사용합니다. 트랜잭션에는 [복제본 세트](https://www.mongodb.com/docs/manual/tutorial/deploy-replica-set/) 배포가 **필수**입니다. 복제본 세트를 배포하는 가장 쉬운 방법은 [Atlas](https://www.mongodb.com/docs/atlas/getting-started/)를 사용하는 것입니다. 무료로 시작할 수 있습니다.

## 연결 세부 정보

- 연결 URL

MongoDB 연결 URL은 데이터베이스 호스팅 방식에 따라 다양한 방법으로 구성할 수 있습니다. 표준 구성은 다음 구성 요소로 이루어집니다:

![MongoDB 연결 URL 구조](https://docs.prisma.io/docs/img/orm/core-concepts/databases/mongodb.png?dpl=dpl_8ArR7Q6jiiF8wQkuTbJ4wnxZAnkX)

#

- 기본 URL 및 경로

연결 URL의 기본 URL 및 경로 섹션은 인증 자격 증명 뒤에 호스트(선택적으로 포트 번호 포함)와 데이터베이스가 이어지는 형태로 구성됩니다.

```
    mongodb://USERNAME:PASSWORD@HOST/DATABASE
```

다음 구성 요소가 데이터베이스의 _기본 URL_ 을 구성합니다:

| Name         | Placeholder | Description                                                                                                                                                                                                                                                                                                                                      |
| ------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 사용자       | `USERNAME`  | 데이터베이스 사용자 이름(예: `janedoe`)                                                                                                                                                                                                                                                                                                          |
| 비밀번호     | `PASSWORD`  | 데이터베이스 사용자 비밀번호                                                                                                                                                                                                                                                                                                                     |
| 호스트       | `HOST`      | [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) 인스턴스가 실행 중인 호스트입니다. 샤딩 클러스터를 실행 중인 경우 [`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#mongodb-binary-bin.mongos) 인스턴스입니다. 호스트명, IP 주소 또는 UNIX 도메인 소켓일 수 있습니다. |
| 포트         | `PORT`      | 데이터베이스 서버가 실행되는 포트(예: `1234`)입니다. 제공하지 않으면 기본값 `27017`이 사용됩니다.                                                                                                                                                                                                                                                |
| 데이터베이스 | `DATABASE`  | 사용할 데이터베이스 이름입니다. 지정하지 않았지만 `authSource` 옵션이 설정된 경우 `authSource` 데이터베이스 이름이 사용됩니다. 연결 문자열의 데이터베이스와 `authSource` 옵션 모두 지정하지 않으면 기본값은 `admin`입니다.                                                                                                                       |

[특수 문자를 퍼센트 인코딩](https://docs.prisma.io/docs/orm/reference/connection-urls#special-characters)해야 합니다.

#

- 인수

연결 URL에는 인수도 포함할 수 있습니다. 다음 예시는 세 가지 인수를 설정합니다:

- `ssl` 연결
- `connectTimeoutMS`
- 그리고 `maxPoolSize`

```
    mongodb://USERNAME:PASSWORD@HOST/DATABASE?ssl=true&connectTimeoutMS=5000&maxPoolSize=50
```

전체 연결 문자열 인수 목록은 [MongoDB 연결 문자열 문서](https://www.mongodb.com/docs/manual/reference/connection-string/)를 참고하세요. Prisma ORM 전용 인수는 없습니다.

## `ObjectId` 사용

MongoDB 문서의 `_id` 필드에 [ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#std-label-objectid)를 포함하는 것은 일반적인 관례입니다:

```
    {
      "_id": { "$oid": "60d599cb001ef98000f2cad2" },
      "createdAt": { "$date": { "$numberLong": "1624611275577" } },
      "email": "ella@prisma.io",
      "name": "Ella",
      "role": "ADMIN"
    }
```

기본 데이터베이스에서 `ObjectId`에 매핑되는 필드(가장 흔히 ID 및 관계 스칼라 필드)는 다음 조건을 충족해야 합니다:

- 타입이 `String` 또는 `Bytes`여야 합니다
- `@db.ObjectId` 속성을 포함해야 합니다
- 문서 생성 시 유효한 `ObjectId`를 자동 생성하려면 선택적으로 `@default(auto())`를 사용할 수 있습니다

다음은 `String`을 사용하는 예시입니다:

```
    model User {
      id String @id @default(auto()) @map("_id") @db.ObjectId
      // Other fields
    }
```

다음은 `Bytes`를 사용하는 또 다른 예시입니다:

```
    model User {
      id Bytes @id @default(auto()) @map("_id") @db.ObjectId
      // Other fields
    }
```

참고: [MongoDB에서 ID 필드 정의하기](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-ids-in-mongodb)

- `ObjectId` 생성

애플리케이션에서 유효한 `ObjectId`(테스트 목적 또는 ID 필드 값을 수동 설정하기 위해)를 생성하려면 [`bson`](https://www.npmjs.com/package/bson) 패키지를 사용하세요.

npm

pnpm

yarn

bun

```
    npm install --save bson
```

```
    import { ObjectId } from "bson";

    const id = new ObjectId();
```

## 관계형 데이터베이스 커넥터와의 차이점

이 섹션에서는 MongoDB 커넥터가 관계형 데이터베이스용 Prisma ORM 커넥터와 다른 점을 설명합니다.

- Prisma Migrate 미지원

현재로서는 MongoDB 프로젝트가 추가 도구로 변경사항을 관리해야 하는 내부 스키마에 의존하지 않기 때문에 [Prisma Migrate](https://docs.prisma.io/docs/orm/prisma-migrate) 지원을 추가할 계획이 없습니다. `@unique` 인덱스 관리는 `db push`를 통해 이루어집니다.

- `@@id` 및 `autoincrement()` 미지원

[`@@id`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference) 속성(여러 필드에 대한 ID)은 MongoDB의 기본 키가 항상 모델의 `_id` 필드에 있기 때문에 지원되지 않습니다.

[`autoincrement()`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#generate-autoincrementing-integers-as-ids-relational-databases-only) 함수(증가하는 `@id` 값을 생성)는 MongoDB에서 `_id` 필드가 갖는 `ObjectID` 타입과 호환되지 않기 때문에 지원되지 않습니다.

- 순환 참조와 참조 동작

모델에 자기 관계 또는 모델 간 관계 사이클로 인한 순환 참조가 있고 [referential actions](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions)을 사용하는 경우, 동작의 무한 루프를 방지하기 위해 참조 동작을 `NoAction`으로 설정해야 합니다.

자세한 내용은 [참조 동작에 대한 특별 규칙](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations/referential-actions#special-rules-for-sql-server-and-mongodb)을 참고하세요.

- 복제본 세트 구성

MongoDB는 복제본 세트에서만 트랜잭션 시작을 허용합니다. Prisma ORM은 중첩 쿼리에서 부분 쓰기를 방지하기 위해 내부적으로 트랜잭션을 사용합니다. 따라서 복제본 세트 구성이 필요하다는 요구사항을 그대로 따르게 됩니다.

복제본 세트가 구성되지 않은 배포에서 Prisma ORM의 MongoDB 커넥터를 사용하려고 하면 Prisma ORM은 `Error: Transactions are not supported by this deployment` 메시지를 표시합니다. 전체 오류 메시지 텍스트는 다음과 같습니다:

```
    PrismaClientUnknownRequestError2 [PrismaClientUnknownRequestError]:
    Invalid `prisma.post.create()` invocation in
    /index.ts:9:21

       6 await prisma.$connect()
       7
       8 // Create the first post
    →  9 await prisma.post.create(
      Error in connector: Database error. error code: unknown, error message: Transactions are not supported by this deployment
        at cb (/node_modules/@prisma/client/runtime/index.js:34804:17)
        at processTicksAndRejections (internal/process/task_queues.js:97:5) {
      clientVersion: '3.xx.0'
    }
```

이를 해결하려면 복제본 세트가 구성된 배포로 변경할 것을 권장합니다.

간단한 방법 중 하나는 [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)를 사용해 기본적으로 복제본 세트를 지원하는 무료 인스턴스를 실행하는 것입니다.

다음 가이드를 따라 로컬에서 복제본 세트를 실행하는 방법도 있습니다: <https://www.mongodb.com/docs/manual/tutorial/convert-standalone-to-replica-set>

## MongoDB와 Prisma schema 간 타입 매핑

MongoDB 커넥터는 Prisma ORM [데이터 모델](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models)의 [스칼라 타입](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields)을 다음과 같이 MongoDB 기본 컬럼 타입으로 매핑합니다:

> 또는 Prisma 타입별로 정리된 타입 매핑은 [Prisma schema reference](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#model-field-scalar-types)를 참고하세요.

- Prisma ORM에서 MongoDB로의 네이티브 타입 매핑

| Prisma ORM | MongoDB                                                             |
| ---------- | ------------------------------------------------------------------- |
| `String`   | `string`                                                            |
| `Boolean`  | `bool`                                                              |
| `Int`      | `int`                                                               |
| `BigInt`   | `long`                                                              |
| `Float`    | `double`                                                            |
| `Decimal`  | [현재 지원되지 않음](https://github.com/prisma/prisma/issues/12637) |
| `DateTime` | `timestamp`                                                         |
| `Bytes`    | `binData`                                                           |
| `Json`     |

현재 지원되지 않는 MongoDB 타입:

- `Decimal128`

- `Undefined`
  - `DBPointer`
  - `Null`
  - `Symbol`
  - `MinKey`
  - `MaxKey`
  - `Object`
  - `Javascript`
  - `JavascriptWithScope`
  - `Regex`

* 인트로스펙션 시 MongoDB에서 Prisma ORM 타입으로의 매핑

MongoDB 데이터베이스를 인트로스펙션할 때 Prisma ORM은 관련 [scalar types](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#scalar-fields)를 사용합니다. 일부 특수 타입에는 추가적인 네이티브 타입 어노테이션도 적용됩니다.

| MongoDB (Type | Aliases) | Prisma ORM | 지원 여부      | 네이티브 데이터베이스 타입 속성 | 참고 |
| ------------- | -------- | ---------- | -------------- | ------------------------------- | ---- |
| `objectId`    | `String` | ✔️         | `@db.ObjectId` |

[인트로스펙션](https://docs.prisma.io/docs/orm/prisma-schema/introspection)은 아직 **지원되지 않는** 네이티브 데이터베이스 타입을 [`Unsupported`](https://docs.prisma.io/docs/orm/reference/prisma-schema-reference#unsupported) 필드로 추가합니다:

schema.prisma

```
    model Example {
      id    String                           @id @default(auto()) @map("_id") @db.ObjectId
      name  String
      regex Unsupported("RegularExpression")
    }
```
