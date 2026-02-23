---
title: 'next.config.js 옵션: typescript'
description: '의  옵션으로 TypeScript 동작을 구성하세요:'
---

# next.config.js 옵션: typescript | Next.js

출처 URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript

# typescript

마지막 업데이트 2026년 2월 20일

`next.config.js`의 `typescript` 옵션으로 TypeScript 동작을 구성하세요:

next.config.js
```
    module.exports = {
      typescript: {
        ignoreBuildErrors: false,
        tsconfigPath: 'tsconfig.json',
      },
    }
```

## Options[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript#options)

옵션| 타입| 기본값| 설명
---|---|---|---
`ignoreBuildErrors`| `boolean`| `false`| TypeScript 오류가 있어도 프로덕션 빌드를 완료하도록 허용합니다.
`tsconfigPath`| `string`| `'tsconfig.json'`| 커스텀 `tsconfig.json` 파일 경로입니다.

## `ignoreBuildErrors`[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript#ignorebuilderrors)

프로젝트에 TypeScript 오류가 있으면 Next.js는 **프로덕션 빌드**(`next build`)를 실패 처리합니다.

애플리케이션에 오류가 있어도 Next.js가 위험을 감수하고 프로덕션 코드를 생성하도록 하려면 내장 타입 검사 단계를 비활성화할 수 있습니다.

비활성화하는 경우 반드시 빌드나 배포 프로세스의 일부로 타입 검사를 실행하세요. 그렇지 않으면 매우 위험할 수 있습니다.

next.config.js
```
    module.exports = {
      typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
      },
    }
```

## `tsconfigPath`[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript#tsconfigpath)

빌드나 도구용으로 다른 TypeScript 구성 파일을 사용하세요:

next.config.js
```
    module.exports = {
      typescript: {
        tsconfigPath: 'tsconfig.build.json',
      },
    }
```

자세한 내용은 [TypeScript configuration](https://nextjs.org/docs/app/api-reference/config/typescript#custom-tsconfig-path) 페이지를 참조하세요.

보내기