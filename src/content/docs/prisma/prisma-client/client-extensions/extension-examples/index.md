---
title: "공유 패키지 및 예시"
description: "Prisma와 커뮤니티가 구축한 Prisma Client 확장을 살펴보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/extension-examples

# 공유 패키지 및 예시

마크다운 복사열기

Prisma와 커뮤니티가 구축한 Prisma Client 확장을 살펴보세요.

## Prisma에서 만든 확장

다음은 Prisma에서 만든 확장 목록입니다:

| Extension                                                                              | Description                                   |
| -------------------------------------------------------------------------------------- | --------------------------------------------- |
| [`@prisma/extension-read-replicas`](https://github.com/prisma/extension-read-replicas) | Prisma Client에 읽기 복제본 지원을 추가합니다 |

## Prisma 커뮤니티에서 만든 확장

다음은 커뮤니티에서 만든 확장 목록입니다. 직접 패키지를 만들고 싶다면 [Shared Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions) 문서를 참고하세요.

| Extension                                                                                      | Description                                                                                              |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [`prisma-extension-supabase-rls`](https://github.com/dthyresson/prisma-extension-supabase-rls) | Prisma에서 Supabase Row Level Security를 지원하도록 추가합니다                                           |
| [`prisma-extension-bark`](https://github.com/adamjkb/bark)                                     | Prisma에서 트리 구조를 쉽게 생성하고 상호작용할 수 있도록 Materialized Path 패턴을 구현합니다            |
| [`prisma-cursorstream`](https://github.com/etabits/prisma-cursorstream)                        | 커서 기반 스트리밍을 추가합니다                                                                          |
| [`prisma-gpt`](https://github.com/aliyeysides/prisma-gpt)                                      | 자연어로 데이터베이스를 쿼리할 수 있게 해줍니다                                                          |
| [`prisma-extension-caching`](https://github.com/isaev-the-poetry/prisma-extension-caching)     | 복잡한 쿼리를 캐시하는 기능을 추가합니다                                                                 |
| [`prisma-extension-cache-manager`](https://github.com/random42/prisma-extension-cache-manager) | 모든 [cache-manager](https://www.npmjs.com/package/cache-manager) 호환 캐시로 모델 쿼리를 캐시합니다     |
| [`prisma-extension-random`](https://github.com/nkeil/prisma-extension-random)                  | 데이터베이스에서 임의의 행을 쿼리할 수 있게 해줍니다                                                     |
| [`prisma-paginate`](https://github.com/sandrewTx08/prisma-paginate)                            | 읽기 쿼리 페이지네이션 지원을 추가합니다                                                                 |
| [`prisma-extension-streamdal`](https://github.com/streamdal/prisma-extension-streamdal)        | Streamdal을 사용한 코드 네이티브 데이터 파이프라인 지원을 추가합니다                                     |
| [`prisma-rbac`](https://github.com/multipliedtwice/prisma-rbac)                                | 사용자 정의 가능한 역할 기반 접근 제어를 추가합니다                                                      |
| [`prisma-extension-redis`](https://github.com/yxx4c/prisma-extension-redis)                    | Redis 및 Dragonfly Databases를 사용해 효율적인 캐싱과 캐시 무효화를 위해 설계된 확장형 Prisma 확장입니다 |
| [`prisma-cache-extension`](https://github.com/Shikhar97/prisma-cache)                          | Redis로 캐시 및 캐시 무효화를 수행하는 Prisma 확장(다른 스토리지 옵션도 지원 예정)                       |
| [`prisma-extension-casl`](https://github.com/dennemark/prisma-extension-casl)                  | CASL을 활용해 대부분의 단순/중첩 쿼리에 권한 부여 로직을 적용하는 Prisma 클라이언트 확장입니다.          |
| [`prisma-emitter-extension`](https://github.com/feggaa/prisma-emitter-extension)               | 설정 가능한 리스너를 기반으로 CRUD 작업 시 이벤트를 발행하는 Prisma 확장입니다.                          |

확장을 만들었고 여기에 소개되길 원한다면 pull request를 열어 목록에 자유롭게 추가해 주세요.

## 예시

다음 예시 확장은 예시 용도로만 제공되며 어떠한 보증도 없습니다. 여기 문서화된 접근 방식을 사용해 Prisma Client 확장을 만드는 방법을 보여주기 위한 것입니다. 자체 확장을 만들 때 영감을 얻기 위한 참고 자료로 활용하는 것을 권장합니다.

| Example                                                                                                                          | Description                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [`audit-log-context`](https://github.com/prisma/prisma-client-extensions/tree/main/audit-log-context)                            | Postgres 감사 로그 트리거에 컨텍스트로 현재 사용자 ID를 제공합니다                                    |
| [`callback-free-itx`](https://github.com/prisma/prisma-client-extensions/tree/main/callback-free-itx)                            | 콜백 없이 대화형 트랜잭션을 시작하는 메서드를 추가합니다                                              |
| [`computed-fields`](https://github.com/prisma/prisma-client-extensions/tree/main/computed-fields)                                | 결과 객체에 가상/계산 필드를 추가합니다                                                               |
| [`input-transformation`](https://github.com/prisma/prisma-client-extensions/tree/main/input-transformation)                      | 결과 집합을 필터링하기 위해 Prisma Client 쿼리에 전달된 입력 인수를 변환합니다                        |
| [`input-validation`](https://github.com/prisma/prisma-client-extensions/tree/main/input-validation)                              | mutation 메서드에 전달된 입력 인수에 사용자 정의 검증 로직을 실행합니다                               |
| [`instance-methods`](https://github.com/prisma/prisma-client-extensions/tree/main/instance-methods)                              | 결과 객체에 `save()` 및 `delete()` 같은 Active Record 스타일 메서드를 추가합니다                      |
| [`json-field-types`](https://github.com/prisma/prisma-client-extensions/tree/main/json-field-types)                              | JSON 컬럼에 저장된 데이터에 대해 강타입 런타임 파싱을 사용합니다                                      |
| [`model-filters`](https://github.com/prisma/prisma-client-extensions/tree/main/model-filters)                                    | 모델의 복잡한 `where` 조건으로 조합할 수 있는 재사용 가능한 필터를 추가합니다                         |
| [`obfuscated-fields`](https://github.com/prisma/prisma-client-extensions/tree/main/obfuscated-fields)                            | 민감한 데이터(예: `password` 필드)가 결과에 포함되지 않도록 방지합니다                                |
| [`query-logging`](https://github.com/prisma/prisma-client-extensions/tree/main/query-logging)                                    | Prisma Client 쿼리를 간단한 쿼리 시간 측정 및 로깅으로 래핑합니다                                     |
| [`readonly-client`](https://github.com/prisma/prisma-client-extensions/tree/main/readonly-client)                                | 읽기 작업만 허용하는 클라이언트를 생성합니다                                                          |
| [`retry-transactions`](https://github.com/prisma/prisma-client-extensions/tree/main/retry-transactions)                          | 지수 백오프와 지터를 적용한 트랜잭션 재시도 메커니즘을 추가합니다                                     |
| [`row-level-security`](https://github.com/prisma/prisma-client-extensions/tree/main/row-level-security)                          | Postgres 행 수준 보안 정책을 사용해 멀티 테넌트 애플리케이션의 데이터를 격리합니다                    |
| [`static-methods`](https://github.com/prisma/prisma-client-extensions/tree/main/static-methods)                                  | Prisma Client 모델에 사용자 정의 쿼리 메서드를 추가합니다                                             |
| [`transformed-fields`](https://github.com/prisma/prisma-client-extensions/tree/main/transformed-fields)                          | 결과 확장을 사용해 쿼리 결과를 변환하고 앱에 i18n을 추가하는 방법을 보여줍니다                        |
| [`exists-method`](https://github.com/prisma/prisma-client-extensions/tree/main/exists-fn)                                        | 모든 모델에 `exists` 메서드를 추가하는 방법을 보여줍니다                                              |
| [`update-delete-ignore-not-found `](https://github.com/prisma/prisma-client-extensions/tree/main/update-delete-ignore-not-found) | 모든 모델에 `updateIgnoreOnNotFound` 및 `deleteIgnoreOnNotFound` 메서드를 추가하는 방법을 보여줍니다. |

## 더 알아보기

- [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)에 대해 더 알아보세요.
