---
title: "환경 변수"
description: "Prisma ORM 프로젝트에서 환경 변수를 관리하는 방법을 알아보세요"
---

출처 URL: https://docs.prisma.io/docs/orm/more/dev-environment/environment-variables

# 환경 변수

Prisma ORM 프로젝트에서 환경 변수를 관리하는 방법을 알아보세요

환경 변수는 로컬 머신 환경에 저장되는 문자열 데이터의 키-값 쌍입니다. 자세한 내용은 [환경 변수 레퍼런스 문서](https://docs.prisma.io/docs/orm/reference/environment-variables-reference)를 참고하세요.

일반적으로 변수 이름은 대문자이며, 그 뒤에 등호와 변수 값이 옵니다:

```
    MY_VALUE=prisma
```

환경 변수는 프로세스가 실행되는 환경에 속합니다. 어떤 프로그램이든 이 환경 변수를 읽고 생성할 수 있습니다. 단순한 정보를 저장하는 저렴하고 효과적인 방법입니다.

Prisma ORM v6.4.0에서 `prisma.config.ts` 파일이 출시되었습니다. 이 파일을 사용하면 환경 변수와 설정을 더 유연하게 관리할 수 있습니다. 자세한 내용은 [레퍼런스](https://docs.prisma.io/docs/orm/reference/prisma-config-reference)를 확인하세요.

## Prisma ORM이 환경 변수를 사용하는 방법

Prisma ORM은 항상 시스템 환경에서 환경 변수를 읽습니다.

프로젝트에서 `prisma init`으로 Prisma ORM을 초기화하면, [`connection url`](https://docs.prisma.io/docs/orm/reference/connection-urls)을 환경 변수로 설정할 수 있도록 편의를 위한 `.env` 파일이 생성됩니다. Prisma CLI 또는 Prisma Client를 사용할 때 `.env` 파일 내용과 그 안에 정의된 변수는 [`process.env` object](https://nodejs.org/api/process.html#processenv)에 추가되며, Prisma ORM은 여기서 값을 읽어 사용할 수 있습니다.

- `.env` 파일 사용하기

**`.env` 파일을 버전 관리에 커밋하지 마세요**!

Prisma CLI는 다음 위치에서 순서대로 `.env` 파일을 찾습니다:

1. 프로젝트 루트 폴더 (`./.env`)
2. `--schema` 인수로 지정한 스키마와 같은 폴더
3. `package.json`의 `"prisma": {"schema": "/path/to/schema.prisma"}`에서 가져온 스키마와 같은 폴더
4. `./prisma` 폴더

1단계에 `.env` 파일이 있지만, 2~4단계에 충돌하는 추가 `.env` 변수가 있으면 CLI가 오류를 발생시킵니다. 예를 들어 서로 다른 두 `.env` 파일에 `DATABASE_URL` 변수를 지정하면 다음 오류가 발생합니다:

```
    Error: There is a conflict between env vars in .env and prisma/.env
    Conflicting env vars:
      DATABASE_URL

    We suggest to move the contents of prisma/.env to .env to consolidate your env vars.
```

다음 표는 Prisma CLI가 `.env` 파일을 찾는 위치를 설명합니다:

| **Command**        | **schema location**      | **`.env` file locations checked, in order** |
| ------------------ | ------------------------ | ------------------------------------------- |
| `prisma [command]` | `./prisma/schema.prisma` | `./.env`                                    |

`./prisma/.env`
`prisma [command] --schema=./a/b/schema.prisma`| `./a/b/schema.prisma`| `./.env`
`./a/b/.env`
`./prisma/.env`
`prisma [command]`| `"prisma": {"schema": "/path/to/schema.prisma"}`| `.env`
`./path/to/schema/.env`
`./prisma/.env`
`prisma [command]`| 스키마 없음(예: 빈 디렉터리에서 `prisma db pull` 실행 시)| `./.env`
`./prisma/.env`

해당 `.env` 파일에 정의된 모든 환경 변수는 Prisma CLI 명령 실행 시 자동으로 로드됩니다.

둘 이상의 `.env` 파일을 사용하고 싶으신가요? 애플리케이션에서 여러 `.env` 파일을 설정하고 사용하는 방법은 [여러 `.env` 파일 사용하기](https://docs.prisma.io/docs/orm/more/dev-environment/environment-variables#using-multiple-env-files)를 참고하세요.

환경 변수가 두 곳에 정의되어 있을 때 어떤 일이 발생하는지는 `dotenv` 문서의 [해당 설명](https://www.npmjs.com/package/dotenv#what-happens-to-environment-variables-that-were-already-set)을 참고하세요.

#

- `.env` 파일로 변수 확장하기

`.env` 파일에 저장된 변수는 [dotenv-expand](https://github.com/motdotla/dotenv-expand)에서 지정한 형식을 사용해 확장할 수 있습니다.

.env

```
    DATABASE_URL=postgresql://test:test@localhost:5432/test
    DATABASE_URL_WITH_SCHEMA=${DATABASE_URL}?schema=public
```

또한 `.env` 파일 _외부_ 에서 설정된 환경 변수도 확장에 사용할 수 있습니다. 예를 들어 Heroku 같은 PaaS에 설정된 데이터베이스 URL이 있을 수 있습니다:

```
    # environment variable already set in the environment of the system
    export DATABASE_URL=postgresql://test:test@localhost:5432/test
```

.env

```
    DATABASE_URL_WITH_SCHEMA=${DATABASE_URL}?schema=foo
```

이렇게 하면 값이 `postgresql://test:test@localhost:5432/test?schema=foo`인 환경 변수 `DATABASE_URL_WITH_SCHEMA`를 Prisma ORM에서 사용할 수 있습니다.

- 코드에서 환경 변수 사용하기

런타임에 환경 변수를 평가하려면 애플리케이션 코드에서 수동으로 로드해야 합니다(예: [`dotenv`](https://github.com/motdotla/dotenv) 사용):

```
    import * as dotenv from "dotenv";

    dotenv.config(); // Load the environment variables
    console.log(`The connection URL is ${process.env.DATABASE_URL}`);
```

환경 변수에 사용자 지정 파일 이름을 사용한다면, `dotenv`가 해당 파일명을 사용하도록 구성할 수 있습니다:

```
    import * as dotenv from "dotenv";

    var envFile = path.resolve(join(__dirname, "myenv.env"));
    dotenv.config({ path: envFile }); // Load the environment variables
    console.log(`The connection URL is ${process.env.DATABASE_URL}`);
```

환경 파일 간 변수 확장이 필요하다면 [`dotenv-expand`](https://github.com/motdotla/dotenv-expand)를 추가로 사용할 수 있습니다:

```
    import * as dotenv from "dotenv";
    const dotenvExpand = require("dotenv-expand");

    var envFile = path.resolve(join(__dirname, "myenv.env"));
    var mySqlEnv = dotenv.config({ path: envFile });
    dotenvExpand.expand(mySqlEnv);
```

여러 `.env` 파일을 사용하는 경우, 실행 중인 환경에 따라 프로젝트 코드에서 환경 파일을 참조할 수 있습니다.

```
    import { config } from "dotenv";

    const envFile = process.env.NODE_ENV === "development" ? ".env.development" : ".env.production";
    config({ path: envFile });
```

- 환경 변수 수동 설정

Prisma ORM은 환경 변수를 찾을 때 시스템 환경을 읽기 때문에, `.env`를 완전히 생략하고 로컬 시스템에 수동으로 생성할 수도 있습니다.

다음 예시는 데이터베이스 연결 URL에 자주 사용되는 `DATABASE_URL` 환경 변수 설정을 사용합니다.

#

- Mac/Linux 시스템에서 환경 변수 수동 설정

Unix 머신(Mac/Linux)의 터미널에서 키-값 쌍으로 변수를 export합니다.

```
    export DATABASE_URL=postgresql://test:test@localhost:5432/test?schema=public
```

그런 다음 `printenv`를 사용해 성공적으로 설정되었는지 확인합니다:

```
    printenv DATABASE_URL
```

```
    postgresql://test:test@localhost:5432/test?schema=public
```

#

- Windows 시스템에서 환경 변수 수동 설정

다음 예시는 선호에 따라 Command Prompt(`cmd.exe`)와 PowerShell 모두에서 환경 변수(현재 사용자 기준)를 설정하는 방법을 보여줍니다.

Command Prompt

PowerShell

```
    set "DATABASE_URL=postgresql://test:test@localhost:5432/test?schema=public"
```

그런 다음 성공적으로 설정되었는지 확인합니다:

Command Prompt

PowerShell

```
    set DATABASE_URL
```

- 여러 `.env` 파일 사용하기

여러 환경의 서로 다른 연결 URL을 단일 `.env` 파일에 저장하면, 운영 데이터베이스가 삭제될 위험이 있습니다.

한 가지 해결책은 각기 다른 환경을 나타내는 여러 `.env` 파일을 두는 것입니다. 실제로는 각 환경마다 파일을 생성한다는 의미입니다:

- `.env.development`
- `.env.sample`

그런 다음 [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli) 같은 패키지를 사용해, 작업 중인 환경에 맞는 연결 URL을 로드할 수 있습니다.

여기서는 애플리케이션 개발 중에 사용하는 전용 개발 데이터베이스가 있다고 가정합니다.

1. `.env` 파일 이름을 `.env.development`로 변경합니다.

.env.development

```
    DATABASE_URL="postgresql://prisma:prisma@localhost:5433/dev"
```

2. 새 `.env.sample` 파일을 만들고 데이터베이스 이름을 `sample`(또는 원하는 이름)로 변경합니다.

.env.sample

```
    DATABASE_URL="postgresql://prisma:prisma@localhost:5433/sample"
```

3. [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli)를 설치합니다.

Prisma ORM과 Jest가 어떤 `.env` 파일을 써야 하는지 알 수 있도록, `package.json` 스크립트를 수정해 `dotenv` 패키지를 포함해 호출하고, 실행 명령과 원하는 환경에 따라 사용할 파일을 지정하세요.

테스트와 마이그레이션을 실행하는 모든 최상위 스크립트 앞에는 `dotenv` 명령이 필요합니다. 이렇게 해야 `.env.sample`의 환경 변수가 Jest를 포함한 모든 명령에 전달됩니다.

#

- 서로 다른 환경에서 마이그레이션 실행

마이그레이션 실행 시 Prisma ORM이 사용할 환경 파일을 지정하려면 [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli) 패키지를 사용할 수 있습니다.

아래 스크립트는 `dotenv-cli`를 사용해 `.env.sample` 환경 파일(`DATABASE_URL` 연결 문자열 포함)을 Prisma ORM 마이그레이션 스크립트에 전달합니다.

#

- 마이그레이션 스크립트

package.json

```
      "scripts": {
        "migrate:postgres": "dotenv -e .env.sample -- npx prisma migrate deploy",
      },
```

#

- 서로 다른 환경에서 테스트 실행

테스트를 실행할 때는 [Prisma Client 모킹](https://docs.prisma.io/docs/orm/prisma-client/testing/unit-testing#mocking-prisma-client)을 권장합니다. 이 경우 Jest가 테스트 실행 시 어떤 환경을 사용할지 지정해야 합니다.

기본적으로 Prisma Client는 프로젝트 루트의 기본 `.env` 파일에 지정된 환경을 사용합니다.

테스트 데이터베이스를 지정하기 위해 별도의 `.env.sample` 파일을 만들었다면, 이 환경을 Jest에 전달해야 합니다.

아래 스크립트는 `dotenv-cli`를 사용해 `.env.sample` 환경 파일(`DATABASE_URL` 연결 문자열 포함)을 Jest에 전달합니다.

package.json

```
      "scripts": {
        "test": "dotenv -e .env.sample -- jest -i"
      },
```
