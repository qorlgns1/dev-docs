---
title: "번들러 이슈"
description: "vercel/pkg 및 기타 번들러에서 ENOENT 패키지 오류 해결하기"
---

출처 URL: https://docs.prisma.io/docs/orm/more/troubleshooting/bundler-issues

# 번들러 이슈

vercel/pkg 및 기타 번들러에서 ENOENT 패키지 오류 해결하기

## vercel/pkg 관련 문제

Node.js 프로젝트를 패키징하기 위해 [vercel/pkg](https://github.com/vercel/pkg)를 사용하면, 다음과 같은 `ENOENT` 오류가 발생할 수 있습니다:

```
    spawn /snapshot/enoent-problem/node_modules/.prisma/client/query-engine-debian-openssl-1.1.x ENOENT
```

## 해결 방법

`package.json` 파일의 `pkg/assets` 섹션에 Prisma 쿼리 엔진 바이너리 경로를 추가하세요:

```
    {
      "pkg": {
        "assets": ["node_modules/.prisma/client/*.node"]
      }
    }
```

자세한 논의는 [이 GitHub 이슈](https://github.com/prisma/prisma/issues/8449)를 참고하세요.
