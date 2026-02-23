---
title: 'next.config.js: logging'
description: '개발 모드에서 Next.js를 실행할 때, 로그 수준과 전체 URL을 콘솔에 기록할지 여부를 구성할 수 있습니다.'
---

# next.config.js: logging | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/logging

# 로깅

마지막 업데이트 2026년 2월 20일

## 옵션[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#options)

### 가져오기[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#fetching)

개발 모드에서 Next.js를 실행할 때, 로그 수준과 전체 URL을 콘솔에 기록할지 여부를 구성할 수 있습니다.

현재 `logging`은 `fetch` API를 사용하는 데이터 가져오기에만 적용되며, 아직 Next.js 내부의 다른 로그에는 적용되지 않습니다.

next.config.js
```
    module.exports = {
      logging: {
        fetches: {
          fullUrl: true,
        },
      },
    }
```

[Server Components HMR 캐시](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)에서 복원되는 모든 `fetch` 요청은 기본적으로 로그에 기록되지 않습니다. 그러나 `logging.fetches.hmrRefreshes`를 `true`로 설정해 활성화할 수 있습니다.

next.config.js
```
    module.exports = {
      logging: {
        fetches: {
          hmrRefreshes: true,
        },
      },
    }
```

### 들어오는 요청[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#incoming-requests)

기본적으로 모든 들어오는 요청이 개발 중 콘솔에 기록됩니다. `incomingRequests` 옵션을 사용해 무시할 요청을 결정할 수 있습니다. 이 로그는 개발 환경에서만 출력되므로, 이 옵션은 프로덕션 빌드에는 영향을 주지 않습니다.

next.config.js
```
    module.exports = {
      logging: {
        incomingRequests: {
          ignore: [/\api\/v1\/health/],
        },
      },
    }
```

또는 `incomingRequests`를 `false`로 설정해 들어오는 요청 로그를 비활성화할 수 있습니다.

next.config.js
```
    module.exports = {
      logging: {
        incomingRequests: false,
      },
    }
```

### 로깅 비활성화[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#disabling-logging)

추가로, `logging`을 `false`로 설정해 개발 로깅 자체를 비활성화할 수도 있습니다.

next.config.js
```
    module.exports = {
      logging: false,
    }
```

보내기