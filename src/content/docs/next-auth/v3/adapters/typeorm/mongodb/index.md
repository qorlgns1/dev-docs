---
title: "MongoDB"
description: "MongoDB는 문서 데이터베이스이며, 대부분의 RDBMS 데이터베이스와 같은 방식으로 스키마를 사용하지 않습니다."
---

출처 URL: https://next-auth.js.org/v3/adapters/typeorm/mongodb

# MongoDB | NextAuth.js

버전: v3

MongoDB는 문서 데이터베이스이며, 대부분의 RDBMS 데이터베이스와 같은 방식으로 스키마를 사용하지 않습니다.

**MongoDB에서는 컬렉션과 인덱스가 자동으로 생성됩니다.**

## MongoDB의 객체[​](https://next-auth.js.org/v3/adapters/typeorm/mongodb#objects-in-mongodb "헤딩으로 바로 가기")

MongoDB에 저장되는 객체는 SQL과 유사한 데이터 타입을 사용하지만, 몇 가지 차이점이 있습니다.

1. ID 필드는 `int` 타입이 아니라 `ObjectID` 타입입니다.

2. 모든 컬렉션 이름과 속성 이름은 `snake_case`가 아니라 `camelCase`를 사용합니다.

3. 모든 타임스탬프는 MongoDB에서 `ISODate()`로 저장되며, 모든 날짜/시간 값은 UTC로 저장됩니다.

4. User의 `email` 속성에는 sparse index가 사용되어, 이 속성이 선택 사항일 수 있도록 하면서도 값이 지정된 경우 고유성이 유지되도록 합니다.

이는 ANSI SQL에서 `unique`이면서 `nullable`인 속성의 동작과 기능적으로 동일합니다.
