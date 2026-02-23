---
title: 'CLI: create-next-app CLI'
description: '2026년 2월 20일에 마지막으로 업데이트됨'
---

# CLI: create-next-app CLI | Next.js
출처 URL: https://nextjs.org/docs/pages/api-reference/cli/create-next-app

[API Reference](https://nextjs.org/docs/pages/api-reference)[CLI](https://nextjs.org/docs/pages/api-reference/cli)create-next-app CLI

# create-next-app CLI

2026년 2월 20일에 마지막으로 업데이트됨

`create-next-app` CLI는 기본 템플릿이나 공개 GitHub 저장소의 [예제](https://github.com/vercel/next.js/tree/canary/examples)를 사용해 새로운 Next.js 애플리케이션을 생성할 수 있도록 도와줍니다. Next.js를 시작하는 가장 쉬운 방법입니다.

기본 사용법:

pnpmnpmyarnbun

Terminal
```
    pnpm create next-app [project-name] [options]
```

## Reference[](https://nextjs.org/docs/pages/api-reference/cli/create-next-app#reference)

다음 옵션을 사용할 수 있습니다:

Options| Description
---|---
`-h` 또는 `--help`| 사용 가능한 모든 옵션 표시
`-v` 또는 `--version`| 버전 번호 출력
`--no-*`| 기본 옵션을 비활성화합니다. 예: `--no-ts`
`--ts` 또는 `--typescript`| TypeScript 프로젝트로 초기화(기본값)
`--js` 또는 `--javascript`| JavaScript 프로젝트로 초기화
`--tailwind`| Tailwind CSS 설정과 함께 초기화(기본값)
`--react-compiler`| React Compiler를 활성화하여 초기화
`--eslint`| ESLint 설정과 함께 초기화
`--biome`| Biome 설정과 함께 초기화
`--no-linter`| 린터 구성을 건너뜀
`--app`| App Router 프로젝트로 초기화
`--api`| 라우트 핸들러만 있는 프로젝트로 초기화
`--src-dir`| `src/` 디렉터리 안에서 초기화
`--turbopack`| 생성된 package.json에서 Turbopack을 강제로 활성화(기본적으로 활성화됨)
`--webpack`| 생성된 package.json에서 Webpack을 강제로 활성화
`--import-alias <alias-to-configure>`| 사용할 import 별칭 지정(기본값 "@/*")
`--empty`| 빈 프로젝트로 초기화
`--use-npm`| npm으로 애플리케이션을 부트스트랩하도록 명시
`--use-pnpm`| pnpm으로 애플리케이션을 부트스트랩하도록 명시
`--use-yarn`| Yarn으로 애플리케이션을 부트스트랩하도록 명시
`--use-bun`| Bun으로 애플리케이션을 부트스트랩하도록 명시
`-e` 또는 `--example [name] [github-url]`| 앱을 부트스트랩할 예제를 지정
`--example-path <path-to-example>`| 예제 경로를 별도로 지정
`--reset-preferences`| 저장된 모든 기본 설정을 재설정하도록 명시
`--skip-install`| 패키지 설치를 건너뛰도록 명시
`--disable-git`| git 초기화를 비활성화하도록 명시
`--yes`| 이전 기본 설정 또는 기본값을 모든 옵션에 사용

## Examples[](https://nextjs.org/docs/pages/api-reference/cli/create-next-app#examples)

### 기본 템플릿 사용[](https://nextjs.org/docs/pages/api-reference/cli/create-next-app#with-the-default-template)

기본 템플릿으로 새 앱을 만들려면 터미널에서 다음 명령을 실행하세요:

pnpmnpmyarnbun

Terminal
```
    pnpm create next-app
```

설치 중에 아래 프롬프트가 표시됩니다:

Terminal
```
    What is your project named? my-app
    Would you like to use the recommended Next.js defaults?
        Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, Turbopack
        No, reuse previous settings
        No, customize settings - Choose your own preferences
```

`customize settings`를 선택하면 다음 프롬프트가 표시됩니다:

Terminal
```
    Would you like to use TypeScript? No / Yes
    Which linter would you like to use? ESLint / Biome / None
    Would you like to use React Compiler? No / Yes
    Would you like to use Tailwind CSS? No / Yes
    Would you like your code inside a `src/` directory? No / Yes
    Would you like to use App Router? (recommended) No / Yes
    Would you like to customize the import alias (`@/*` by default)? No / Yes
    What import alias would you like configured? @/*
```

프롬프트를 완료하면 `create-next-app`이 프로젝트 이름의 폴더를 만들고 필요한 종속성을 설치합니다.

### Linter 옵션[](https://nextjs.org/docs/pages/api-reference/cli/create-next-app#linter-options)

**ESLint** : 전통적이면서 가장 인기 있는 JavaScript 린터입니다. `@next/eslint-plugin-next`의 Next.js 전용 규칙이 포함되어 있습니다.

**Biome** : ESLint와 Prettier 기능을 결합한 빠르고 현대적인 린터이자 포매터입니다. 최적의 성능을 위해 Next.js와 React 도메인 지원이 내장되어 있습니다.

**None** : 린터 구성을 완전히 건너뜁니다. 나중에 언제든 린터를 추가할 수 있습니다.

프롬프트에 답하면 선택한 구성으로 새로운 프로젝트가 생성됩니다.

### 공식 Next.js 예제 사용[](https://nextjs.org/docs/pages/api-reference/cli/create-next-app#with-an-official-nextjs-example)

공식 Next.js 예제로 새 앱을 만들려면 `--example` 플래그를 사용하세요. 예:

pnpmnpmyarnbun

Terminal
```
    pnpm create next-app --example [example-name] [your-project-name]
```

모든 사용 가능한 예제와 설정 안내는 [Next.js 저장소](https://github.com/vercel/next.js/tree/canary/examples)에서 확인할 수 있습니다.

### 모든 공개 GitHub 예제 사용[](https://nextjs.org/docs/pages/api-reference/cli/create-next-app#with-any-public-github-example)

공개 GitHub 예제로 새 앱을 만들려면 GitHub 저장소 URL과 함께 `--example` 옵션을 사용하세요. 예:

pnpmnpmyarnbun

Terminal
```
    pnpm create next-app --example "https://github.com/.../" [your-project-name]
```