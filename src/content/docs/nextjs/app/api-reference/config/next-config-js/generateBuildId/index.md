---
title: 'next.config.js: generateBuildId'
description: 'Next.js는 애플리케이션에서 제공 중인 버전을 식별하기 위해  중에 ID를 생성합니다. 동일한 빌드를 재사용하여 여러 컨테이너를 부팅해야 합니다.'
---

# next.config.js: generateBuildId | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId

[구성](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)generateBuildId

페이지 복사

# generateBuildId

마지막 업데이트: 2026년 2월 20일

Next.js는 애플리케이션에서 제공 중인 버전을 식별하기 위해 `next build` 중에 ID를 생성합니다. 동일한 빌드를 재사용하여 여러 컨테이너를 부팅해야 합니다.

환경의 각 단계를 다시 빌드하는 경우, 컨테이너 간에 사용할 일관된 빌드 ID를 만들어야 합니다. `next.config.js`에서 `generateBuildId` 명령을 사용하세요:

next.config.js
```
    module.exports = {
      generateBuildId: async () => {
        // This could be anything, using the latest git hash
        return process.env.GIT_HASH
      },
    }
```

도움이 되었나요?

지원됨.

보내기
