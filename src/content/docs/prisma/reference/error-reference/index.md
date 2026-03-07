---
title: "오류 참조"
description: "Prisma Client, Migrate, Introspection 오류 코드"
---

출처 URL: https://docs.prisma.io/docs/orm/reference/error-reference

# 오류 참조

Prisma Client, Migrate, Introspection 오류 코드

예외 및 오류 코드 처리 방법에 대한 자세한 내용은 [예외 및 오류 처리](https://docs.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/handling-exceptions-and-errors)를 참고하세요.

## Prisma Client 오류 유형

Prisma Client는 여러 종류의 오류를 발생시킵니다. 아래는 예외 유형과 문서화된 데이터 필드 목록입니다.

- `PrismaClientKnownRequestError`

요청과 관련된 알려진 오류를 쿼리 엔진이 반환하면 Prisma Client는 `PrismaClientKnownRequestError` 예외를 발생시킵니다. 예를 들어 고유 제약 조건 위반이 이에 해당합니다.

| **속성**        | **설명**                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| `code`          | Prisma 전용 [오류 코드](https://docs.prisma.io/docs/orm/reference/error-reference#error-codes)          |
| `meta`          | 오류에 대한 추가 정보. 예: 오류를 유발한 필드: `{ target: [ 'email' ] }`                                |
| `message`       | [오류 코드](https://docs.prisma.io/docs/orm/reference/error-reference#error-codes)와 연관된 오류 메시지 |
| `clientVersion` | Prisma Client 버전(예: `2.19.0`)                                                                        |

- `PrismaClientUnknownRequestError`

요청과 관련되어 있지만 오류 코드가 없는 오류를 쿼리 엔진이 반환하면 Prisma Client는 `PrismaClientUnknownRequestError` 예외를 발생시킵니다.

| **속성**        | **설명**                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| `message`       | [오류 코드](https://docs.prisma.io/docs/orm/reference/error-reference#error-codes)와 연관된 오류 메시지 |
| `clientVersion` | Prisma Client 버전(예: `2.19.0`)                                                                        |

- `PrismaClientRustPanicError`

기반 엔진이 크래시되어 0이 아닌 종료 코드로 종료되면 Prisma Client는 `PrismaClientRustPanicError` 예외를 발생시킵니다. 이 경우 Prisma Client 또는 전체 Node 프로세스를 재시작해야 합니다.

| **속성**        | **설명**                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| `message`       | [오류 코드](https://docs.prisma.io/docs/orm/reference/error-reference#error-codes)와 연관된 오류 메시지 |
| `clientVersion` | Prisma Client 버전(예: `2.19.0`)                                                                        |

- `PrismaClientInitializationError`

쿼리 엔진 시작 및 데이터베이스 연결 생성 과정에서 문제가 발생하면 Prisma Client는 `PrismaClientInitializationError` 예외를 발생시킵니다. 이는 다음 중 하나의 시점에 발생합니다.

- `prisma.$connect()` 호출 시 또는
- 첫 번째 쿼리 실행 시

발생할 수 있는 오류는 다음과 같습니다.

- 제공된 데이터베이스 자격 증명이 유효하지 않음
- 제공된 호스트명과 포트에서 실행 중인 데이터베이스 서버가 없음
- 쿼리 엔진 HTTP 서버가 바인딩하려는 포트를 이미 사용 중임
- 환경 변수가 없거나 접근할 수 없음
- 현재 플랫폼용 쿼리 엔진 바이너리를 찾을 수 없음(`generator` 블록)

| **속성**        | **설명**                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| `errorCode`     | Prisma 전용 오류 코드                                                                                   |
| `message`       | [오류 코드](https://docs.prisma.io/docs/orm/reference/error-reference#error-codes)와 연관된 오류 메시지 |
| `clientVersion` | Prisma Client 버전(예: `2.19.0`)                                                                        |

- `PrismaClientValidationError`

유효성 검사에 실패하면 Prisma Client는 `PrismaClientValidationError` 예외를 발생시킵니다. 예:

- 필드 누락 - 예: 새 레코드를 생성할 때 비어 있는 `data: {}` 속성
- 잘못된 필드 타입 제공(예: `Boolean` 필드에 `"Hello, I like cheese and gold!"` 설정)

| **속성**        | **설명**                         |
| --------------- | -------------------------------- |
| `message`       | 오류 메시지                      |
| `clientVersion` | Prisma Client 버전(예: `2.19.0`) |

## 오류 코드

- 공통

#

- `P1000`

"`{database_host}`의 데이터베이스 서버에 대한 인증에 실패했습니다. `{database_user}`에 대해 제공된 데이터베이스 자격 증명이 유효하지 않습니다. `{database_host}`의 데이터베이스 서버에 유효한 자격 증명을 제공했는지 확인하세요."

#

- `P1001`

"`{database_host}`:`{database_port}`의 데이터베이스 서버에 연결할 수 없습니다. 데이터베이스 서버가 `{database_host}`:`{database_port}`에서 실행 중인지 확인하세요."

#

- `P1002`

"`{database_host}`:`{database_port}`의 데이터베이스 서버에 연결되었지만 시간 초과되었습니다. 다시 시도하세요. 데이터베이스 서버가 `{database_host}`:`{database_port}`에서 실행 중인지 확인하세요. "

#

- `P1003`

"데이터베이스 {database_file_name}이(가) {database_file_path}에 존재하지 않습니다."

"데이터베이스 `{database_name}.{database_schema_name}`이(가) `{database_host}:{database_port}`의 데이터베이스 서버에 존재하지 않습니다."

"데이터베이스 `{database_name}`이(가) `{database_host}:{database_port}`의 데이터베이스 서버에 존재하지 않습니다."

#

- `P1008`

"`{time}` 이후 작업이 시간 초과되었습니다."

#

- `P1009`

"데이터베이스 `{database_name}`이(가) `{database_host}:{database_port}`의 데이터베이스 서버에 이미 존재합니다."

#

- `P1010`

"사용자 `{database_user}`에게 데이터베이스 `{database_name}`에 대한 접근이 거부되었습니다."

#

- `P1011`

"TLS 연결을 여는 중 오류 발생: {message}"

#

- `P1012`

Prisma ORM을 버전 4.0.0 이상으로 업그레이드한 뒤 P1012 오류 코드가 발생하면 [버전 4.0.0 업그레이드 가이드](https://docs.prisma.io/docs/guides/upgrade-prisma-orm/v4#update-schema)를 참고하세요. 4.0.0 이전에는 유효했던 스키마가 4.0.0 이상에서는 유효하지 않을 수 있습니다. 업그레이드 가이드에서는 스키마를 유효하게 업데이트하는 방법을 설명합니다.

"{full_error}"

가능한 P1012 오류 메시지:

- "Argument `{}` is missing."
- "Function `{}` takes arguments, but received ."
- "Argument `{}` is missing in attribute `@{}`."
- "Argument `{}` is missing in data source block `{}`."
- "Argument `{}` is missing in generator block `{}`."
- "Error parsing attribute `@{}`: "
- "Attribute `@{}` is defined twice."
- "The model with database name `{}` could not be defined because another model with this name exists: `{}`"
- "`{}` is a reserved scalar type name and can not be used."
- "The `{}` cannot be defined because a with that name already exists."
- "Key `{}` is already defined in ."
- "Argument `{}` is already specified as unnamed argument."
- "Argument `{}` is already specified."
- "No such argument.""
- "Field `{}` is already defined on model `{}`."
- "Field `{}` in model `{}` can't be a list. The current connector does not support lists of primitive types."
- "The index name `{}` is declared multiple times. With the current connector index names have to be globally unique."
- "Value `{}` is already defined on enum `{}`."
- "Attribute not known: `@{}`."
- "Function not known: `{}`."
- "Datasource provider not known: `{}`."
- "shadowDatabaseUrl is the same as url for datasource `{}`. Please specify a different database as shadow database."
- "The preview feature `{}` is not known. Expected one of: "
- "`{}` is not a valid value for ."
- "Type `{}` is neither a built-in type, nor refers to another model, custom type, or enum."
- "Type `{}` is not a built-in type."
- "Unexpected token. Expected one of: "
- "Environment variable not found: ."
- "Expected a value, but received value `{}`."
- "Expected a value, but failed while parsing `{}`: ."
- "Error validating model `{}`: "
- "Error validating field `{}` in model `{}`: "
- "Error validating datasource `{datasource}`: {message}"
- "Error validating enum `{}`: "
- "Error validating: "

#

- `P1013`

"제공된 데이터베이스 문자열이 유효하지 않습니다. {details}"

#

- `P1014`

"모델 `{model}`의 기본 {kind}이(가) 존재하지 않습니다."

#

- `P1015`

"Prisma 스키마가 현재 데이터베이스 버전에서 지원되지 않는 기능을 사용하고 있습니다.
데이터베이스 버전: {database_version}
오류:
{errors}"

#

- `P1016`

"raw 쿼리의 매개변수 개수가 올바르지 않습니다. 예상값: `{expected}`, 실제값: `{actual}`."

#

- `P1017`

"서버가 연결을 종료했습니다."

- Prisma Client (Query Engine)

#

- `P2000`

"컬럼에 제공된 값이 해당 컬럼 타입에 비해 너무 깁니다. 컬럼: {column_name}"

#

- `P2001`

"where 조건에서 조회한 레코드(`{model_name}.{argument_name} = {argument_value}`)가 존재하지 않습니다."

#

- `P2002`

"{constraint}에서 고유 제약 조건 위반이 발생했습니다."

#

- `P2003`

"필드 `{field_name}`에서 외래 키 제약 조건 위반이 발생했습니다."

#

- `P2004`

"데이터베이스에서 제약 조건 위반이 발생했습니다: `{database_error}`"

#

- `P2005`

"데이터베이스에 저장된 `{field_name}` 필드 값 `{field_value}`이(가) 해당 필드 타입에 유효하지 않습니다."

#

- `P2006`

"`{model_name}`의 `{field_name}` 필드에 제공된 값 `{field_value}`이(가) 유효하지 않습니다."

#

- `P2007`

"데이터 유효성 검사 오류 `{database_error}`"

#

- `P2008`

"`{query_position}`에서 쿼리 `{query_parsing_error}` 파싱에 실패했습니다."

#

- `P2009`

"`{query_position}`에서 쿼리 유효성 검사에 실패했습니다: `{query_validation_error}`"

#

- `P2010`

"Raw 쿼리 실패. 코드: `{code}`. 메시지: `{message}`"

#

- `P2011`

"{constraint}에서 Null 제약 조건 위반이 발생했습니다."

#

- `P2012`

"`{path}`에 필수 값이 누락되었습니다."

#

- `P2013`

"`{object_name}`의 `{field_name}` 필드에 필요한 인수 `{argument_name}`이(가) 누락되었습니다."

#

- `P2014`

"현재 변경 작업은 `{model_a_name}` 모델과 `{model_b_name}` 모델 사이의 필수 관계 `{relation_name}`를 위반하게 됩니다."

#

- `P2015`

"연관된 레코드를 찾을 수 없습니다. {details}"

#

- `P2016`

"쿼리 해석 오류. {details}"

#

- `P2017`

"`{parent_name}` 및 `{child_name}` 모델 사이의 `{relation_name}` 관계에 대한 레코드가 연결되어 있지 않습니다."

#

- `P2018`

"필수로 연결되어야 하는 레코드를 찾을 수 없습니다. {details}"

#

- `P2019`

"입력 오류. {details}"

#

- `P2020`

"값이 해당 타입의 범위를 벗어났습니다. {details}"

#

- `P2021`

"현재 데이터베이스에 `{table}` 테이블이 존재하지 않습니다."

#

- `P2022`

"현재 데이터베이스에 `{column}` 컬럼이 존재하지 않습니다."

#

- `P2023`

"일관되지 않은 컬럼 데이터: {message}"

#

- `P2024`

"connection pool에서 새 연결을 가져오는 중 시간이 초과되었습니다. (추가 정보: [http://pris.ly/d/connection-pool](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool) (현재 connection pool timeout: {timeout}, connection limit: {connection_limit})"

Prisma ORM v7에서는 pool 크기와 timeout이 [driver adapter](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-pool)별로 구성됩니다. adapter별 connection pool 레퍼런스를 확인하세요.

#

- `P2025`

"필수지만 찾을 수 없는 하나 이상의 레코드에 의존하기 때문에 작업이 실패했습니다. {cause}"

#

- `P2026`

"현재 데이터베이스 provider는 이 쿼리에서 사용한 기능을 지원하지 않습니다: {feature}"

#

- `P2027`

"쿼리 실행 중 데이터베이스에서 여러 오류가 발생했습니다: {errors}"

#

- `P2028`

"Transaction API 오류: {error}"

#

- `P2029`

"쿼리 파라미터 한도 초과 오류: {message}"

#

- `P2030`

"검색에 사용할 fulltext index를 찾을 수 없습니다. 스키마에 @@fulltext([Fields...])를 추가해 보세요"

#

- `P2031`

"Prisma가 transaction을 수행해야 하며, 이를 위해서는 MongoDB 서버가 replica set으로 실행되어야 합니다. 자세한 내용: [https://pris.ly/d/mongodb-replica-set](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mongodb#replica-set-configuration)"

#

- `P2033`

"쿼리에서 사용한 숫자가 64비트 signed integer에 맞지 않습니다. 큰 정수를 저장하려는 경우 필드 타입으로 `BigInt` 사용을 고려하세요"

#

- `P2034`

"쓰기 충돌 또는 deadlock으로 인해 transaction이 실패했습니다. transaction을 다시 시도하세요"

#

- `P2035`

"데이터베이스에서 assertion 위반이 발생했습니다: {database_error}"

#

- `P2036`

"외부 커넥터 오류 (id {id})"

#

- `P2037`

"열린 데이터베이스 연결 수가 너무 많습니다: {message}"

- Prisma Migrate (Schema Engine)

Schema Engine은 이전에 Migration Engine이라고 불렸습니다. 이 변경은 [5.0.0](https://github.com/prisma/prisma/releases/tag/5.0.0) 버전에서 도입되었습니다.

#

- `P3000`

"데이터베이스 생성에 실패했습니다: {database_error}"

#

- `P3001`

"파괴적 변경 및 잠재적 데이터 손실이 있는 migration이 가능합니다: {migration_engine_destructive_details}"

#

- `P3002`

"시도한 migration이 롤백되었습니다: {database_error}"

#

- `P3003`

"migration 형식이 변경되어 저장된 migration이 더 이상 유효하지 않습니다. 이 문제를 해결하려면 다음 단계들을 따르세요: [https://pris.ly/d/migrate](https://docs.prisma.io/docs/orm/prisma-migrate)"

#

- `P3004`

"`{database_name}` 데이터베이스는 시스템 데이터베이스이므로 prisma migrate로 변경하면 안 됩니다. 다른 데이터베이스에 연결하세요."

#

- `P3005`

"데이터베이스 스키마가 비어 있지 않습니다. 기존 프로덕션 데이터베이스를 baseline 처리하는 방법은 다음을 참고하세요: [https://pris.ly/d/migrate-baseline](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/baselining)"

#

- `P3006`

"Migration `{migration_name}`을 shadow database에 깔끔하게 적용하지 못했습니다.
{error_code}Error:
{inner_error}"

#

- `P3007`

"요청한 preview feature 중 일부는 아직 schema engine에서 허용되지 않습니다. migration을 사용하기 전에 데이터 모델에서 해당 항목을 제거하세요. (차단됨: {list_of_blocked_features})"

#

- `P3008`

"Migration `{migration_name}`은 이미 데이터베이스에 적용된 것으로 기록되어 있습니다."

#

- `P3009`

"migrate가 대상 데이터베이스에서 실패한 migration을 발견했으므로 새 migration은 적용되지 않습니다. 프로덕션 데이터베이스에서 migration 문제를 해결하는 방법은 다음을 참고하세요: [https://pris.ly/d/migrate-resolve](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting)
{details}"

#

- `P3010`

"migration 이름이 너무 깁니다. 200자(바이트)를 초과하면 안 됩니다."

#

- `P3011`

"Migration `{migration_name}`은 데이터베이스에 한 번도 적용된 적이 없어 롤백할 수 없습니다. 힌트: migration 전체 이름을 전달했나요? (예: "20201207184859_initial_migration")"

#

- `P3012`

"Migration `{migration_name}`은 실패 상태가 아니므로 롤백할 수 없습니다."

#

- `P3013`

"migrate에서는 datasource provider 배열이 더 이상 지원되지 않습니다. datasource를 단일 provider를 사용하도록 변경하세요. 자세한 내용: <https://pris.ly/multi-provider-deprecation>"

#

- `P3014`

"Prisma Migrate가 shadow database를 생성할 수 없었습니다. 데이터베이스 사용자가 데이터베이스 생성 권한을 가지고 있는지 확인하세요. shadow database(및 우회 방법)에 대한 자세한 내용: [https://pris.ly/d/migrate-shadow](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database).

원본 오류: {error_code}
{inner_error}"

#

- `P3015`

"{migration_file_path}에서 migration 파일을 찾을 수 없습니다. 디렉터리를 삭제하거나 migration 파일을 복원하세요."

#

- `P3016`

"데이터베이스 reset의 fallback 메서드가 실패했습니다. 즉, Migrate가 데이터베이스를 완전히 정리할 수 없었습니다. 원본 오류: {error_code}
{inner_error}"

#

- `P3017`

"migration {migration_name}을(를) 찾을 수 없습니다. migration이 존재하는지, 그리고 디렉터리의 전체 이름을 포함했는지 확인하세요. (예: "20201207184859_initial_migration")"

#

- `P3018`

"migration 적용에 실패했습니다. 오류가 복구되기 전에는 새 migration을 적용할 수 없습니다. 프로덕션 데이터베이스에서 migration 문제를 해결하는 방법은 다음을 참고하세요: [https://pris.ly/d/migrate-resolve](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting)"

Migration 이름: {migration_name}

데이터베이스 오류 코드: {database_error_code}

데이터베이스 오류:
{database_error} "

#

- `P3019`

"스키마에 지정된 datasource provider `{provider}`가 migration_lock.toml에 지정된 `{expected_provider}`와 일치하지 않습니다. 현재 migration 디렉터리를 제거하고 prisma migrate dev로 새 migration 히스토리를 시작하세요. 자세히 보기: [https://pris.ly/d/migrate-provider-switch](https://docs.prisma.io/docs/orm/prisma-migrate/workflows/troubleshooting)"

#

- `P3020`

"Azure SQL에서는 shadow database 자동 생성이 비활성화되어 있습니다. `shadowDatabaseUrl` datasource 속성을 사용해 shadow database를 설정하세요.
자세한 내용은 문서를 확인하세요: [https://pris.ly/d/migrate-shadow](https://docs.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/shadow-database)"

#

- `P3021`

"이 데이터베이스에서는 foreign key를 생성할 수 없습니다. 처리 방법은 다음을 참고하세요: [https://pris.ly/d/migrate-no-foreign-keys](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale)"

#

- `P3022`

"이 데이터베이스에서는 DDL (Data Definition Language) SQL 문을 직접 실행할 수 없습니다. 처리 방법은 다음을 참고하세요: [https://pris.ly/d/migrate-no-direct-ddl](https://docs.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale)"

#

- `P3023`

"현재 데이터베이스에서는 prisma config의 `externalTables` 및 `externalEnums`에 완전 수식 식별자(예: `schema_name.table_name`)만 포함되어야 합니다."

#

- `P3024`

"현재 데이터베이스에서는 prisma config의 `externalTables` 및 `externalEnums`에 스키마 이름 없는 단순 식별자만 포함되어야 합니다."

- `prisma db pull`

#

- `P4000`

"Introspection 작업이 스키마 파일을 생성하지 못했습니다: {introspection_error}"

#

- `P4001`

"Introspection된 데이터베이스가 비어 있었습니다."

#

- `P4002`

"Introspection된 데이터베이스의 스키마가 일관되지 않습니다: {explanation}"

- Prisma Accelerate

Prisma Accelerate 관련 오류는 [`P5011`](https://docs.prisma.io/docs/orm/reference/error-reference#p5011-too-many-requests)을 제외하고 `P6xxx`로 시작합니다.

#

- `P6000` (`ServerError`)

다른 모든 오류를 포괄적으로 처리하기 위한 일반 오류입니다.

#

- `P6001` (`InvalidDataSource`)

URL 형식이 올바르지 않습니다. 예를 들어 `prisma://` 프로토콜을 사용하지 않습니다.

#

- `P6002` (`Unauthorized`)

연결 문자열의 API Key가 유효하지 않습니다.

#

- `P6003` (`PlanLimitReached`)

현재 플랜에 포함된 사용량을 초과했습니다. 이는 [free plan](https://www.prisma.io/pricing)에서만 발생할 수 있습니다.

#

- `P6004` (`QueryTimeout`)

Accelerate의 전역 timeout을 초과했습니다.

> 자세한 내용은 [troubleshooting guide](https://docs.prisma.io/docs/accelerate/more/troubleshoot#p6004-querytimeout)도 참고하세요.

#

- `P6005` (`InvalidParameters`)

사용자가 유효하지 않은 파라미터를 제공했습니다. 현재는 transaction 메서드에만 해당합니다. 예를 들어, timeout 값을 너무 높게 설정한 경우입니다.

#

- `P6006` (`VersionNotSupported`)

선택한 Prisma 버전이 Accelerate와 호환되지 않습니다. 사용자가 가끔 정리되는 불안정한 개발 버전을 사용하는 경우 이런 문제가 발생할 수 있습니다.

#

- `P6008` (`ConnectionError|EngineStartError`)

엔진 시작에 실패했습니다. 예를 들어 데이터베이스에 연결을 수립하지 못한 경우입니다.

> 자세한 내용은 [troubleshooting guide](https://docs.prisma.io/docs/accelerate/more/troubleshoot#p6008-connectionerrorenginestarterror)도 참고하세요.

#

- `P6009` (`ResponseSizeLimitExceeded`)

Accelerate의 전역 응답 크기 제한을 초과했습니다.

> 자세한 내용은 [troubleshooting guide](https://docs.prisma.io/docs/accelerate/more/troubleshoot#p6009-responsesizelimitexceeded)도 참고하세요.

#

- `P6010` (`ProjectDisabledError`)

accelerate 프로젝트가 비활성화되었습니다. 사용하려면 다시 [enable](https://docs.prisma.io/docs/accelerate/getting-started#1-enable-accelerate)해 주세요.

#

- `P5011` (`Too Many Requests`)

이 오류는 요청량을 초과했음을 나타냅니다. back-off 전략을 구현하고 나중에 다시 시도하세요. 예상되는 높은 워크로드에 대한 지원이 필요하면 [support](https://docs.prisma.io/docs/console/more/support)에 문의하세요.
