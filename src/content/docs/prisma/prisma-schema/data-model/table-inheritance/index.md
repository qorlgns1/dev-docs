---
title: "테이블 상속"
description: "애플리케이션에서 union type 또는 다형성 구조를 사용할 수 있게 해주는 Prisma ORM의 테이블 상속 사용 사례와 패턴을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-schema/data-model/table-inheritance

# 테이블 상속

애플리케이션에서 union type 또는 다형성 구조를 사용할 수 있게 해주는 Prisma ORM의 테이블 상속 사용 사례와 패턴을 알아보세요.

## 개요

테이블 상속은 엔티티 간의 계층적 관계를 모델링할 수 있게 해주는 소프트웨어 설계 패턴입니다. 데이터베이스 수준에서 테이블 상속을 사용하면 JavaScript/TypeScript 애플리케이션에서 union type을 사용할 수 있고, 여러 모델 간에 공통 속성 집합을 공유할 수도 있습니다.

이 페이지에서는 테이블 상속에 대한 두 가지 접근 방식을 소개하고, Prisma ORM과 함께 사용하는 방법을 설명합니다.

테이블 상속의 일반적인 사용 사례 중 하나는 애플리케이션에서 어떤 종류의 _피드(feed)_ 형태로 _콘텐츠 활동(content activities)_ 을 표시해야 하는 경우입니다. 이때 콘텐츠 활동은 _video_ 또는 _article_ 일 수 있습니다. 예시로 다음을 가정해 보겠습니다.

- 콘텐츠 활동은 항상 `id` 와 `url` 을 가집니다.
- video는 `id` 와 `url` 외에도 `duration`(`Int`로 모델링됨)을 가집니다.
- article은 `id` 와 `url` 외에도 `body`(`String`으로 모델링됨)를 가집니다.

* 사용 사례

#

- Union type

Union type은 TypeScript의 편리한 기능으로, 개발자가 데이터 모델의 타입을 더 유연하게 다룰 수 있게 해줍니다.

TypeScript에서 union type은 다음과 같습니다.

```
    type Activity = Video | Article;
```

현재 [Prisma schema에서 union type을 모델링하는 것은 불가능](https://github.com/prisma/prisma/issues/2505)하지만, 테이블 상속과 몇 가지 추가 타입 정의를 사용하면 Prisma ORM에서 활용할 수 있습니다.

#

- 여러 모델 간 속성 공유

여러 모델이 특정 속성 집합을 공유해야 하는 사용 사례가 있다면, 이 역시 테이블 상속으로 모델링할 수 있습니다.

예를 들어, 위의 `Video` 와 `Article` 모델이 모두 공통 `title` 속성을 가져야 한다면, 테이블 상속으로 이를 구현할 수 있습니다.

- 예시

간단한 Prisma schema에서는 다음과 같이 보일 수 있습니다. 관계(relations)와 함께 어떻게 동작하는지 보여주기 위해 `User` 모델도 추가합니다.

schema.prisma

```
    model Video {
      id       Int    @id
      url      String @unique
      duration Int

      user   User @relation(fields: [userId], references: [id])
      userId Int
    }

    model Article {
      id   Int    @id
      url  String @unique
      body String

      user   User @relation(fields: [userId], references: [id])
      userId Int
    }

    model User {
      id       Int       @id
      name     String
      videos   Video[]
      articles Article[]
    }
```

이제 이를 테이블 상속으로 어떻게 모델링할 수 있는지 살펴보겠습니다.

- Single-table vs multi-table inheritance

다음은 테이블 상속의 두 가지 주요 접근 방식에 대한 간단한 비교입니다.

- **Single-table inheritance (STI)** : _하나의_ 테이블에 _모든_ 엔티티의 데이터를 한곳에 저장합니다. 이 예시에서는 `id`, `url`뿐 아니라 `duration`, `body` 컬럼까지 포함된 단일 `Activity` 테이블이 있습니다. 또한 _activity_ 가 _video_ 인지 _article_ 인지 나타내는 `type` 컬럼을 사용합니다.
- **Multi-table inheritance (MTI)** : _여러_ 테이블에 각기 다른 엔티티의 데이터를 분리해서 저장하고 외래 키로 연결합니다. 이 예시에서는 `id`, `url` 컬럼을 가진 `Activity` 테이블, `duration` 과 `Activity` 를 가리키는 외래 키를 가진 `Video` 테이블, `body` 와 외래 키를 가진 `Article` 테이블이 있습니다. 또한 구분자 역할을 하는 `type` 컬럼이 있어 _activity_ 가 _video_ 인지 _article_ 인지 나타냅니다. multi-table inheritance는 _delegated types_ 라고도 불립니다.

두 접근 방식의 트레이드오프는 [아래](https://docs.prisma.io/docs/orm/prisma-schema/data-model/table-inheritance#tradeoffs-between-sti-and-mti)에서 확인할 수 있습니다.

## Single-table inheritance (STI)

- 데이터 모델

STI를 사용하면 위 시나리오는 다음과 같이 모델링할 수 있습니다.

```
    model Activity {
      id       Int          @id // shared
      url      String       @unique // shared
      duration Int? // video-only
      body     String? // article-only
      type     ActivityType // discriminator

      owner   User @relation(fields: [ownerId], references: [id])
      ownerId Int
    }

    enum ActivityType {
      Video
      Article
    }

    model User {
      id         Int        @id @default(autoincrement())
      name       String?
      activities Activity[]
    }
```

참고할 점은 다음과 같습니다.

- 모델별 속성인 `duration` 과 `body` 는 optional(`?`)로 표시해야 합니다. _video_ 를 나타내는 `Activity` 테이블 레코드는 `body` 값을 가져서는 안 되기 때문입니다. 반대로 _article_ 을 나타내는 `Activity` 레코드에는 `duration` 이 설정될 수 없습니다.
- `type` 구분자 컬럼은 각 레코드가 _video_ 항목인지 _article_ 항목인지 나타냅니다.

* Prisma Client API

Prisma ORM이 데이터 모델에 대해 타입과 API를 생성하는 방식 때문에, `Activity` 타입 하나와 해당 CRUD 쿼리(`create`, `update`, `delete`, ...)만 사용할 수 있습니다.

#

- video와 article 조회

이제 `type` 컬럼으로 필터링하여 _video_ 또는 _article_ 만 조회할 수 있습니다. 예를 들면 다음과 같습니다.

```
    // Query all videos
    const videos = await prisma.activity.findMany({
      where: { type: "Video" },
    });

    // Query all articles
    const articles = await prisma.activity.findMany({
      where: { type: "Article" },
    });
```

#

- 전용 타입 정의

이처럼 video와 article을 조회해도 TypeScript는 여전히 `Activity` 타입으로만 인식합니다. 이는 `videos` 객체에도 (optional) `body` 가 있고 `articles` 객체에도 (optional) `duration` 필드가 있게 되어 번거로울 수 있습니다.

이 객체들에 대해 타입 안정성을 확보하려면 전용 타입을 정의해야 합니다. 예를 들어 생성된 `Activity` 타입과 TypeScript의 `Omit` 유틸리티 타입을 사용해 속성을 제거할 수 있습니다.

```
    import { Activity } from "../prisma/generated/client";

    type Video = Omit<Activity, "body" | "type">;
    type Article = Omit<Activity, "duration" | "type">;
```

또한 `Activity` 타입 객체를 `Video` 및 `Article` 타입으로 변환하는 매핑 함수를 만들어 두면 유용합니다.

```
    function activityToVideo(activity: Activity): Video {
      return {
        url: activity.url,
        duration: activity.duration ? activity.duration : -1,
        ownerId: activity.ownerId,
      } as Video;
    }

    function activityToArticle(activity: Activity): Article {
      return {
        url: activity.url,
        body: activity.body ? activity.body : "",
        ownerId: activity.ownerId,
      } as Article;
    }
```

이제 조회 후 `Activity` 를 더 구체적인 타입(즉, `Article` 또는 `Video`)으로 변환할 수 있습니다.

```
    const videoActivities = await prisma.activity.findMany({
      where: { type: "Video" },
    });
    const videos: Video[] = videoActivities.map(activityToVideo);
```

#

- 더 편리한 API를 위한 Prisma Client extension 사용

[Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)를 사용해 데이터베이스의 테이블 구조에 대해 더 편리한 API를 만들 수 있습니다.

## Multi-table inheritance (MTI)

- 데이터 모델

MTI를 사용하면 위 시나리오는 다음과 같이 모델링할 수 있습니다.

```
    model Activity {
      id   Int          @id @default(autoincrement())
      url  String // shared
      type ActivityType // discriminator

      video   Video? // model-specific 1-1 relation
      article Article? // model-specific 1-1 relation

      owner   User @relation(fields: [ownerId], references: [id])
      ownerId Int
    }

    model Video {
      id         Int      @id @default(autoincrement())
      duration   Int // video-only
      activityId Int      @unique
      activity   Activity @relation(fields: [activityId], references: [id])
    }

    model Article {
      id         Int      @id @default(autoincrement())
      body       String // article-only
      activityId Int      @unique
      activity   Activity @relation(fields: [activityId], references: [id])
    }

    enum ActivityType {
      Video
      Article
    }

    model User {
      id         Int        @id @default(autoincrement())
      name       String?
      activities Activity[]
    }
```

참고할 점은 다음과 같습니다.

- `Activity` 와 `Video`, 그리고 `Activity` 와 `Article` 사이에는 1-1 관계가 필요합니다. 이 관계는 필요할 때 레코드의 구체적인 정보를 가져오는 데 사용됩니다.
- 이 접근 방식에서는 모델별 속성인 `duration` 과 `body` 를 _required_ 로 만들 수 있습니다.
- `type` 구분자 컬럼은 각 레코드가 _video_ 항목인지 _article_ 항목인지 나타냅니다.

* Prisma Client API

이번에는 `PrismaClient` 인스턴스의 `video` 및 `article` 속성을 통해 video와 article을 직접 조회할 수 있습니다.

#

- video와 article 조회

공유 속성에 접근하려면 `include` 를 사용해 `Activity` 와의 관계를 함께 가져와야 합니다.

```
    // Query all videos
    const videos = await prisma.video.findMany({
      include: { activity: true },
    });

    // Query all articles
    const articles = await prisma.article.findMany({
      include: { activity: true },
    });
```

필요에 따라 `type` 구분자 컬럼으로 필터링해 반대 방향으로도 조회할 수 있습니다.

```
    // Query all videos
    const videoActivities = await prisma.activity.findMany({
      where: { type: 'Video' }
      include: { video: true }
    })
```

#

- 전용 타입 정의

타입 측면에서 STI보다 조금 더 편리하긴 하지만, 생성된 타입 정의가 모든 요구 사항을 충족하지는 않을 수 있습니다.

다음은 Prisma ORM이 생성한 `Video`, `Article` 타입을 `Activity` 타입과 결합해 `Video` 및 `Article` 타입을 정의하는 방법입니다. 이러한 결합을 통해 원하는 속성을 가진 새 타입을 만들 수 있습니다. 또한 구체 타입에서는 더 이상 필요 없으므로 `type` 구분자 컬럼도 제거하고 있다는 점에 유의하세요.

```
    import { Video as VideoDB, Article as ArticleDB, Activity } from "../prisma/generated/client";

    type Video = Omit<VideoDB & Activity, "type">;
    type Article = Omit<ArticleDB & Activity, "type">;
```

이 타입들을 정의한 뒤에는, 위 쿼리에서 받은 타입을 원하는 `Video`, `Article` 타입으로 변환하는 매핑 함수를 정의할 수 있습니다. 아래는 `Video` 타입 예시입니다.

```
    import { Prisma, Video as VideoDB, Activity } from "../prisma/generated/client";

    type Video = Omit<VideoDB & Activity, "type">;

    // Create `VideoWithActivity` typings for the objects returned above
    const videoWithActivity = Prisma.validator<Prisma.VideoDefaultArgs>()({
      include: { activity: true },
    });
    type VideoWithActivity = Prisma.VideoGetPayload<typeof videoWithActivity>;

    // Map to `Video` type
    function toVideo(a: VideoWithActivity): Video {
      return {
        id: a.id,
        url: a.activity.url,
        ownerId: a.activity.ownerId,
        duration: a.duration,
        activityId: a.activity.id,
      };
    }
```

이제 위 쿼리 결과 객체를 `toVideo` 로 변환할 수 있습니다.

```
    const videoWithActivities = await prisma.video.findMany({
      include: { activity: true },
    });
    const videos: Video[] = videoWithActivities.map(toVideo);
```

#

- 더 편리한 API를 위한 Prisma Client extension 사용

[Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)를 사용해 데이터베이스의 테이블 구조에 대해 더 편리한 API를 만들 수 있습니다.

## STI와 MTI의 트레이드오프

- **데이터 모델** : MTI가 데이터 모델 측면에서 더 깔끔하게 느껴질 수 있습니다. STI에서는 행이 매우 넓어지고 `NULL` 값을 가진 컬럼이 많아질 수 있습니다.
- **성능** : MTI는 모델에 관련된 _모든_ 속성에 접근하려면 부모/자식 테이블을 조인해야 하므로 성능 비용이 발생할 수 있습니다.
- **타입 정의** : Prisma ORM에서 MTI는 특정 모델(즉, 위 예시의 `Article`, `Video`)에 대한 적절한 타입 정의를 기본으로 제공합니다. 반면 STI에서는 이를 직접 만들어야 합니다.
- **ID / 기본 키** : MTI에서는 레코드가 두 개의 ID(부모 테이블 하나, 자식 테이블 하나)를 가지며 서로 일치하지 않을 수 있습니다. 애플리케이션의 비즈니스 로직에서 이를 고려해야 합니다.

## 서드파티 솔루션

현재 Prisma ORM은 union type이나 다형성을 네이티브로 지원하지 않지만, Prisma schema에 추가 기능 레이어를 제공하는 [Zenstack](https://github.com/zenstackhq/zenstack)을 확인해볼 수 있습니다. 자세한 내용은 [Prisma ORM의 다형성에 대한 블로그 글](https://zenstack.dev/blog/polymorphism)을 참고하세요.
