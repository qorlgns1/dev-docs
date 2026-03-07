---
title: "테스트 프로젝트 [​](https://vitest.dev/guide/workspace#test-projects)"
description: "이 기능은 라고도 알려져 있습니다. 는 3.2부터 더 이상 사용되지 않으며  구성으로 대체되었습니다. 기능적으로는 동일합니다."
---

출처 URL: https://vitest.dev/guide/workspace

# 테스트 프로젝트 [​](https://vitest.dev/guide/workspace#test-projects)

샘플 프로젝트

[GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/projects) - [온라인에서 실행](https://stackblitz.com/fork/github/vitest-dev/vitest/tree/main/examples/projects?initialPath=__vitest__/)

WARNING

이 기능은 `workspace`라고도 알려져 있습니다. `workspace`는 3.2부터 더 이상 사용되지 않으며 `projects` 구성으로 대체되었습니다. 기능적으로는 동일합니다.

Vitest는 단일 Vitest 프로세스 내에서 여러 프로젝트 구성을 정의할 수 있는 방법을 제공합니다. 이 기능은 특히 모노레포 설정에서 유용하지만, `resolve.alias`, `plugins`, `test.browser` 등 서로 다른 구성으로 테스트를 실행할 때도 사용할 수 있습니다.

## 프로젝트 정의 [​](https://vitest.dev/guide/workspace#defining-projects)

루트 [config](https://vitest.dev/config/)에서 프로젝트를 정의할 수 있습니다:

vitest.config.ts

ts

```
    import { defineConfig } from 'vitest/config'

    export default defineConfig({
      test: {
        projects: ['packages/*'],
      },
    })
```

프로젝트 구성은 인라인 config, 파일, 또는 프로젝트를 참조하는 glob 패턴입니다. 예를 들어, 프로젝트가 들어 있는 `packages`라는 폴더가 있다면 루트 Vitest config에 배열을 정의할 수 있습니다:

vitest.config.ts

ts

```
    import { defineConfig } from 'vitest/config'

    export default defineConfig({
      test: {
        projects: ['packages/*'],
      },
    })
```

Vitest는 `packages` 안의 각 폴더를, 내부에 config 파일이 없더라도 별도의 프로젝트로 취급합니다. glob 패턴이 파일과 일치하면, Vitest 구성 파일인지 확인하기 위해 이름이 `vitest.config`/`vite.config`로 시작하거나 `(vite|vitest).*.config.*` 패턴과 일치하는지 검증합니다. 예를 들어 다음 config 파일은 유효합니다:

- `vitest.config.ts`
- `vite.config.js`
- `vitest.unit.config.ts`
- `vite.e2e.config.js`
- `vitest.config.unit.js`
- `vite.config.e2e.js`

폴더와 파일을 제외하려면 negation 패턴을 사용할 수 있습니다:

vitest.config.ts

ts

```
    import { defineConfig } from 'vitest/config'

    export default defineConfig({
      test: {
        // include all folders inside "packages" except "excluded"
        projects: [
          'packages/*',
          '!packages/excluded'
        ],
      },
    })
```

일부 폴더는 프로젝트여야 하고 다른 폴더는 자체 하위 폴더를 가지는 중첩 구조라면, 상위 폴더가 매칭되지 않도록 괄호를 사용해야 합니다:

vitest.config.ts

ts

```
    import { defineConfig } from 'vitest/config'

    // For example, this will create projects:
    // packages/a
    // packages/b
    // packages/business/c
    // packages/business/d
    // Notice that "packages/business" is not a project itself

    export default defineConfig({
      test: {
        projects: [
          // matches every folder inside "packages" except "business"
          'packages/!(business)',
          // matches every folder inside "packages/business"
          'packages/business/*',
        ],
      },
    })
```

WARNING

Vitest는 루트 `vitest.config` 파일이 구성에서 명시적으로 지정되지 않는 한 이를 프로젝트로 취급하지 않습니다. 따라서 루트 구성은 `reporters`, `coverage` 같은 전역 옵션에만 영향을 줍니다. 또한 Vitest는 루트 config 파일에 지정된 `apply`, `config`, `configResolved`, `configureServer` 같은 특정 플러그인 훅을 항상 실행합니다. Vitest는 전역 setup과 커스텀 coverage provider를 실행할 때도 동일한 플러그인을 사용합니다.

config 파일로 프로젝트를 참조할 수도 있습니다:

vitest.config.ts

ts

```
    import { defineConfig } from 'vitest/config'

    export default defineConfig({
      test: {
        projects: ['packages/*/vitest.config.{e2e,unit}.ts'],
      },
    })
```

이 패턴은 확장자 앞에 `e2e` 또는 `unit`이 포함된 `vitest.config` 파일이 있는 프로젝트만 포함합니다.

인라인 구성으로도 프로젝트를 정의할 수 있습니다. 이 구성은 두 문법을 동시에 지원합니다.

vitest.config.ts

ts

```
    import { defineConfig } from 'vitest/config'

    export default defineConfig({
      test: {
        projects: [
          // matches every folder and file inside the `packages` folder
          'packages/*',
          {
            // add "extends: true" to inherit the options from the root config
            extends: true,
            test: {
              include: ['tests/**/*.{browser}.test.{ts,js}'],
              // it is recommended to define a name when using inline configs
              name: 'happy-dom',
              environment: 'happy-dom',
            }
          },
          {
            test: {
              include: ['tests/**/*.{node}.test.{ts,js}'],
              // color of the name label can be changed
              name: { label: 'node', color: 'green' },
              environment: 'node',
            }
          }
        ]
      }
    })
```

WARNING

모든 프로젝트는 고유한 이름을 가져야 하며, 그렇지 않으면 Vitest가 오류를 발생시킵니다. 인라인 구성에서 이름을 제공하지 않으면 Vitest가 번호를 할당합니다. glob 문법으로 정의된 프로젝트 구성의 경우, Vitest는 가장 가까운 `package.json` 파일의 "name" 속성을 기본값으로 사용하며, 없으면 폴더 이름을 사용합니다.

프로젝트는 모든 구성 속성을 지원하지 않습니다. 더 나은 타입 안정성을 위해 프로젝트 구성 파일에서는 `defineConfig` 대신 `defineProject` 메서드를 사용하세요:

packages/a/vitest.config.ts

ts

```
    import {

    defineProject

     } from 'vitest/config'

    export default

    defineProject

    ({

    test

    : {

    environment

    : 'jsdom',
        // "reporters" is not supported in a project config,
        // so it will show an error
        reporters: ['json']

    No overload matches this call.
      The last overload gave the following error.
        Object literal may only specify known properties, and 'reporters' does not exist in type 'ProjectConfig'.

      }
    })
```

## 테스트 실행 [​](https://vitest.dev/guide/workspace#running-tests)

테스트를 실행하려면 루트 `package.json`에 스크립트를 정의하세요:

package.json

json

```
    {
      "scripts": {
        "test": "vitest"
      }
    }
```

이제 패키지 매니저를 사용해 테스트를 실행할 수 있습니다:

npmyarnpnpmbun

bash

```
    npm run test
```

bash

```
    yarn test
```

bash

```
    pnpm run test
```

bash

```
    bun run test
```

단일 프로젝트 내부에서만 테스트를 실행해야 한다면 `--project` CLI 옵션을 사용하세요:

npmyarnpnpmbun

bash

```
    npm run test --project e2e
```

bash

```
    yarn test --project e2e
```

bash

```
    pnpm run test --project e2e
```

bash

```
    bun run test --project e2e
```

TIP

여러 프로젝트를 필터링하기 위해 `--project` CLI 옵션을 여러 번 사용할 수 있습니다:

npmyarnpnpmbun

bash

```
    npm run test --project e2e --project unit
```

bash

```
    yarn test --project e2e --project unit
```

bash

```
    pnpm run test --project e2e --project unit
```

bash

```
    bun run test --project e2e --project unit
```

## 구성 [​](https://vitest.dev/guide/workspace#configuration)

구성 옵션 중 어떤 것도 루트 레벨 config 파일에서 상속되지 않습니다. 공유 config 파일을 만든 뒤, 이를 프로젝트 config와 직접 병합할 수 있습니다:

packages/a/vitest.config.ts

ts

```
    import { defineProject, mergeConfig } from 'vitest/config'
    import configShared from '../vitest.shared.js'

    export default mergeConfig(
      configShared,
      defineProject({
        test: {
          environment: 'jsdom',
        }
      })
    )
```

또한 `extends` 옵션을 사용해 루트 레벨 구성을 상속할 수 있습니다. 모든 옵션이 병합됩니다.

vitest.config.ts

ts

```
    import { defineConfig } from 'vitest/config'
    import react from '@vitejs/plugin-react'

    export default defineConfig({
      plugins: [react()],
      test: {
        pool: 'threads',
        projects: [
          {
            // will inherit options from this config like plugins and pool
            extends: true,
            test: {
              name: 'unit',
              include: ['**/*.unit.test.ts'],
            },
          },
          {
            // won't inherit any options from this config
            // this is the default behaviour
            extends: false,
            test: {
              name: 'integration',
              include: ['**/*.integration.test.ts'],
            },
          },
        ],
      },
    })
```

지원되지 않는 옵션

일부 구성 옵션은 프로젝트 config에서 허용되지 않습니다. 대표적으로:

- `coverage`: coverage는 전체 프로세스 기준으로 수행됩니다
- `reporters`: 루트 레벨 reporters만 지원됩니다
- `resolveSnapshotPath`: 루트 레벨 resolver만 반영됩니다
- 테스트 러너에 영향을 주지 않는 기타 모든 옵션

프로젝트 구성 내부에서 지원되지 않는 모든 구성 옵션은 이름 옆의 아이콘으로 표시됩니다. 이러한 옵션은 루트 config 파일에서 한 번만 정의할 수 있습니다.
