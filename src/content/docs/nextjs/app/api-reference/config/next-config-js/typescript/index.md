---
title: 'next.config.js: typescript'
description: '에서  옵션으로 TypeScript 동작을 구성하세요:'
---

# next.config.js: typescript | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript

# typescript

마지막 업데이트 2026년 2월 20일

`next.config.js`에서 `typescript` 옵션으로 TypeScript 동작을 구성하세요:

next.config.js
[code]
    module.exports = {
      typescript: {
        ignoreBuildErrors: false,
        tsconfigPath: 'tsconfig.json',
      },
    }
[/code]

## 옵션[](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript#options)

옵션| 유형| 기본값| 설명
---|---|---|---
`ignoreBuildErrors`| `boolean`| `false`| TypeScript 오류가 있어도 프로덕션 빌드를 완료하도록 허용합니다.
`tsconfigPath`| `string`| `'tsconfig.json'`| 사용자 지정 `tsconfig.json` 파일의 경로입니다.

## `ignoreBuildErrors`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript#ignorebuilderrors)

프로젝트에 TypeScript 오류가 있으면 Next.js는 **프로덕션 빌드**(`next build`)를 실패 처리합니다.

애플리케이션에 오류가 있어도 Next.js가 위험을 감수하고 프로덕션 코드를 생성하게 하려면, 내장된 타입 검사 단계를 비활성화할 수 있습니다.

비활성화한 경우 빌드나 배포 프로세스의 일부로 타입 검사를 실행해야 합니다. 그렇지 않으면 매우 위험할 수 있습니다.

next.config.js
[code]
    module.exports = {
      typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
      },
    }
[/code]

## `tsconfigPath`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript#tsconfigpath)

빌드나 도구를 위해 다른 TypeScript 구성 파일을 사용하세요:

next.config.js
[code]
    module.exports = {
      typescript: {
        tsconfigPath: 'tsconfig.build.json',
      },
    }
[/code]

자세한 내용은 [TypeScript 구성](https://nextjs.org/docs/app/api-reference/config/typescript#custom-tsconfig-path) 페이지를 참고하세요.

supported.

Send
