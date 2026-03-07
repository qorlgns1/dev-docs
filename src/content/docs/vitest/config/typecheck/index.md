---
title: "typecheck {#typecheck}"
description: "일반 테스트와 함께 typechecking을 활성화합니다."
---

출처 URL: https://vitest.dev/config/typecheck

# typecheck {#typecheck}

[typechecking](https://vitest.dev/guide/testing-types) 테스트 환경을 구성하기 위한 옵션입니다.

## typecheck.enabled {#typecheck-enabled}

- **Type**: `boolean`
- **Default**: `false`
- **CLI**: `--typecheck`, `--typecheck.enabled`

일반 테스트와 함께 typechecking을 활성화합니다.

## typecheck.only {#typecheck-only}

- **Type**: `boolean`
- **Default**: `false`
- **CLI**: `--typecheck.only`

typechecking이 활성화된 경우 typecheck 테스트만 실행합니다. CLI를 사용할 때 이 옵션은 typechecking을 자동으로 활성화합니다.

## typecheck.checker

- **Type**: `'tsc' | 'vue-tsc' | string`
- **Default**: `tsc`

타입 검사를 위해 사용할 도구를 지정합니다. Vitest는 타입에 따라 더 쉽게 파싱할 수 있도록 특정 파라미터로 프로세스를 생성합니다. Checker는 `tsc`와 동일한 출력 형식을 구현해야 합니다.

typechecker를 사용하려면 패키지가 설치되어 있어야 합니다:

- `tsc`에는 `typescript` 패키지가 필요합니다
- `vue-tsc`에는 `vue-tsc` 패키지가 필요합니다

`tsc --noEmit --pretty false`와 동일한 출력을 생성하는 커스텀 바이너리 경로나 명령어 이름을 전달할 수도 있습니다.

## typecheck.include

- **Type**: `string[]`
- **Default**: `['**/*.{test,spec}-d.?(c|m)[jt]s?(x)']`

테스트 파일로 처리되어야 하는 파일의 glob 패턴입니다.

## typecheck.exclude

- **Type**: `string[]`
- **Default**: `['**/node_modules/**', '**/dist/**', '**/cypress/**', '**/.{idea,git,cache,output,temp}/**']`

테스트 파일로 처리되지 않아야 하는 파일의 glob 패턴입니다.

## typecheck.allowJs

- **Type**: `boolean`
- **Default**: `false`

`@ts-check` 주석이 있는 JS 파일을 검사합니다. tsconfig에서 이미 활성화되어 있다면 이를 덮어쓰지 않습니다.

## typecheck.ignoreSourceErrors

- **Type**: `boolean`
- **Default**: `false`

Vitest가 테스트 파일 외부에서 오류를 찾아도 실패하지 않도록 합니다. 이 경우 테스트가 아닌 오류는 전혀 표시되지 않습니다.

기본적으로 Vitest가 소스 오류를 찾으면 테스트 스위트가 실패합니다.

## typecheck.tsconfig

- **Type**: `string`
- **Default**: _가장 가까운 tsconfig.json을 찾으려고 시도함_

프로젝트 루트를 기준으로 한 커스텀 tsconfig 경로입니다.

## typecheck.spawnTimeout

- **Type**: `number`
- **Default**: `10_000`

typechecker를 시작(spawn)하는 데 걸리는 최소 시간(밀리초)입니다.
