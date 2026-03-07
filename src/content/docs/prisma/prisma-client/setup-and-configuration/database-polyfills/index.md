---
title: "데이터베이스 polyfill"
description: 'Prisma Client는 관계형 데이터베이스로는 구현할 수 없는 기능을 제공합니다. 이러한 기능을 "polyfill"이라고 하며, 이 페이지에서 설명합니다.'
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/database-polyfills

# 데이터베이스 polyfill

Prisma Client는 관계형 데이터베이스로는 구현할 수 없는 기능을 제공합니다. 이러한 기능을 "polyfill"이라고 하며, 이 페이지에서 설명합니다.

Prisma Client는 특정 데이터베이스에서는 일반적으로 구현할 수 없거나 확장이 필요한 기능을 제공합니다. 이러한 기능을 *polyfills*라고 합니다. 모든 데이터베이스에서 여기에 포함되는 것은 다음과 같습니다.

- `cuid` 및 `uuid` 값을 사용해 [ID](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-an-id-field) 값을 초기화
- 레코드가 마지막으로 업데이트된 시간을 저장하기 위해 [`@updatedAt`](https://docs.prisma.io/docs/orm/prisma-schema/data-model/models#defining-attributes) 사용

관계형 데이터베이스의 경우 여기에 포함되는 것은 다음과 같습니다.

- 암시적 다대다 관계

MongoDB의 경우 여기에 포함되는 것은 다음과 같습니다.

- [관계 전반](https://docs.prisma.io/docs/orm/prisma-schema/data-model/relations) \- MongoDB에서는 문서 간 foreign key 관계가 강제되지 않음
