---
title: 'next.config.js: distDir'
description: '마지막 업데이트: 2026년 2월 20일'
---

# next.config.js: distDir | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)distDir

페이지 복사

# distDir

마지막 업데이트: 2026년 2월 20일

`.next` 대신 사용할 사용자 지정 빌드 디렉터리 이름을 지정할 수 있습니다.

`next.config.js`를 열고 `distDir` 설정을 추가합니다:

next.config.js
```
    module.exports = {
      distDir: 'build',
    }
```

이제 `next build`를 실행하면 Next.js는 기본 `.next` 폴더 대신 `build`를 사용합니다.

> `distDir`은 프로젝트 디렉터리를 벗어나면 **안 됩니다**. 예를 들어 `../build`는 **잘못된** 디렉터리입니다.

도움이 되었나요?

지원됨.

보내기
