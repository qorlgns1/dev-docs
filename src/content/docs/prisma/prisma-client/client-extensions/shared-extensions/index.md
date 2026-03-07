---
title: "공유 Prisma Client 확장"
description: "확장을 공유하거나 Prisma 프로젝트로 공유 확장을 가져오기"
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/shared-extensions

# 공유 Prisma Client 확장

확장을 공유하거나 Prisma 프로젝트로 공유 확장을 가져오기

[Prisma Client 확장](https://docs.prisma.io/docs/orm/prisma-client/client-extensions)을 다른 사용자와 패키지 또는 모듈 형태로 공유할 수 있으며, 다른 사용자가 만든 확장을 프로젝트에 가져올 수도 있습니다.

공유 가능한 확장을 만들고 싶다면 [`prisma-client-extension-starter`](https://github.com/prisma/prisma-client-extension-starter) 템플릿 사용도 권장합니다.

Prisma 공식 Client 확장 예제와 커뮤니티에서 만든 확장을 살펴보려면 [이 페이지](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/extension-examples)를 방문하세요.

## 공유된 패키지형 확장 설치하기

프로젝트에서는 다른 사용자가 `npm`에 게시한 모든 Prisma Client 확장을 설치할 수 있습니다. 설치하려면 다음 명령어를 실행하세요:

npm

pnpm

yarn

bun

```
    npm install prisma-extension-<package-name>
```

예를 들어, 사용 가능한 확장의 패키지 이름이 `prisma-extension-find-or-create`라면 다음과 같이 설치할 수 있습니다:

npm

pnpm

yarn

bun

```
    npm install prisma-extension-find-or-create
```

위 예제의 `find-or-create` 확장을 가져와 클라이언트 인스턴스를 감싸려면 다음 코드를 사용할 수 있습니다. 이 예제에서는 확장 이름이 `findOrCreate`라고 가정합니다.

```
    import findOrCreate from "prisma-extension-find-or-create";
    import { PrismaClient } from "../generated/prisma/client";
    const prisma = new PrismaClient();
    const xprisma = prisma.$extends(findOrCreate);
    const user = await xprisma.user.findOrCreate();
```

확장에서 메서드를 호출할 때는 `prisma`가 아니라 `$extends` 구문에서 사용한 상수 이름을 사용하세요. 위 예제에서는 `xprisma.user.findOrCreate`는 동작하지만 `prisma.user.findOrCreate`는 동작하지 않습니다. 원본 `prisma`는 수정되지 않기 때문입니다.

## 공유 가능한 확장 만들기

다른 사용자도 사용할 수 있고, 특정 스키마에만 맞춰지지 않은 확장을 만들고 싶다면 Prisma ORM은 공유 가능한 확장을 만들 수 있도록 유틸리티를 제공합니다.

공유 가능한 확장을 만들려면:

1. `Prisma.defineExtension`을 사용해 확장을 모듈로 정의합니다.
2. [`$allModels`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/model#add-a-custom-method-to-all-models-in-your-schema) 또는 [`$allOperations`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/query#modify-all-prisma-client-operations)처럼 `$all` 접두사로 시작하는 메서드 중 하나를 사용합니다.

- 확장 정의하기

확장을 공유 가능하게 만들려면 `Prisma.defineExtension` 메서드를 사용하세요. 이를 사용하면 확장을 별도 파일로 분리하거나 다른 사용자와 npm 패키지로 공유할 수 있도록 패키징할 수 있습니다.

`Prisma.defineExtension`의 장점은 개발 중인 확장 작성자와 공유 확장 사용자를 위해 엄격한 타입 검사와 자동 완성을 제공한다는 점입니다.

- 제네릭 메서드 사용하기

`$allModels` 아래 메서드를 포함한 확장은 특정 모델이 아닌 모든 모델에 적용됩니다. 마찬가지로 `$allOperations` 아래 메서드는 `result`나 `query` 같은 이름 있는 컴포넌트가 아니라 클라이언트 인스턴스 전체에 적용됩니다.

[`client`](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/client) 컴포넌트에는 `$all` 접두사를 사용할 필요가 없습니다. `client` 컴포넌트는 항상 클라이언트 인스턴스에 적용되기 때문입니다.

예를 들어, 제네릭 확장은 다음과 같은 형태가 될 수 있습니다:

```
    export default Prisma.defineExtension({
      name: "prisma-extension-find-or-create", //Extension name
      model: {
        $allModels: {
          // new method
          findOrCreate(/* args */) {
            /* code for the new method */
            return query(args);
          },
        },
      },
    });
```

Prisma Client 작업을 수정하는 다양한 방법은 다음 페이지를 참고하세요:

- 모든 Prisma Client 작업 수정
- 스키마의 모든 모델에서 특정 작업 수정
- 스키마의 모든 모델에서 모든 작업 수정

* 공유 가능한 확장을 npm에 게시하기

그다음 이 확장을 `npm`에 공유할 수 있습니다. 패키지 이름을 정할 때는 찾기와 설치를 쉽게 하기 위해 `prisma-extension-<package-name>` 규칙을 사용하는 것을 권장합니다.

- 패키지 확장에서 클라이언트 레벨 메서드 호출하기

현재 `PrismaClient`를 참조하고 클라이언트 레벨 메서드를 호출하는 확장에는 아래 예시와 같은 제한이 있습니다.

[트랜잭션](https://docs.prisma.io/docs/orm/prisma-client/queries/transactions)(interactive 또는 batched) 내부에서 확장을 트리거하면, 확장 코드는 새 연결에서 쿼리를 실행하고 현재 트랜잭션 컨텍스트를 무시합니다.

자세한 내용은 GitHub 이슈를 참고하세요: [클라이언트 레벨 메서드 사용이 필요한 Client 확장이 트랜잭션을 조용히 무시하는 문제](https://github.com/prisma/prisma/issues/20678).

다음 상황에서는 확장이 감싸는 Prisma Client 인스턴스를 참조해야 합니다:

- 패키지 확장에서 `$queryRaw` 같은 [클라이언트 레벨 메서드](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods)를 사용하려는 경우
- 패키지 확장에서 여러 `$extends` 호출을 체이닝하려는 경우

하지만 누군가가 당신의 패키지 확장을 프로젝트에 포함하면, 코드에서는 해당 Prisma Client 인스턴스의 세부 정보를 알 수 없습니다.

다음과 같이 이 클라이언트 인스턴스를 참조할 수 있습니다:

```
    Prisma.defineExtension((client) => {
      // The Prisma Client instance that the extension user applies the extension to
      return client.$extends({
        name: "prisma-extension-<extension-name>",
      });
    });
```

예시:

```
    export default Prisma.defineExtension((client) => {
      return client.$extends({
        name: "prisma-extension-find-or-create",
        query: {
          $allModels: {
            async findOrCreate({ args, query, operation }) {
              return (await client.$transaction([query(args)]))[0];
            },
          },
        },
      });
    });
```

- 고급 타입 안정성: 제네릭 확장 정의를 위한 타입 유틸리티

[type utilities](https://docs.prisma.io/docs/orm/prisma-client/client-extensions/type-utilities)를 사용하면 공유 확장의 타입 안정성을 높일 수 있습니다.
