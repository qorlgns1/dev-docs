---
title: 'next.config.js: env'
description: '이 API는 레거시이며 더 이상 권장되지 않습니다. 하위 호환성을 위해 계속 지원됩니다.'
---

# next.config.js: env | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/env

# env

이 API는 레거시이며 더 이상 권장되지 않습니다. 하위 호환성을 위해 계속 지원됩니다.

마지막 업데이트 2026년 2월 20일

> [Next.js 9.4](https://nextjs.org/blog/next-9-4) 릴리스 이후 [환경 변수를 추가](https://nextjs.org/docs/app/guides/environment-variables)하는 더 직관적이고 인체공학적인 경험을 제공하고 있습니다. 한 번 사용해 보세요!

> **알아두면 좋아요**: 이 방식으로 지정된 환경 변수는 **항상** JavaScript 번들에 포함됩니다. 환경 변수 이름 앞에 `NEXT_PUBLIC_` 접두사를 붙이는 것은 [환경 또는 .env 파일을 통해](https://nextjs.org/docs/app/guides/environment-variables) 지정할 때만 효과가 있습니다.

환경 변수를 JavaScript 번들에 추가하려면 `next.config.js`를 열고 `env` 구성을 추가하세요:

next.config.js
```
    module.exports = {
      env: {
        customKey: 'my-value',
      },
    }
```

이제 코드에서 `process.env.customKey`에 접근할 수 있습니다. 예를 들어:
```
    function Page() {
      return <h1>The value of customKey is: {process.env.customKey}</h1>
    }

    export default Page
```

Next.js는 빌드 시점에 `process.env.customKey`를 `'my-value'`로 대체합니다. webpack [DefinePlugin](https://webpack.js.org/plugins/define-plugin/)의 특성상 `process.env` 변수를 구조 분해하려고 하면 작동하지 않습니다.

예를 들어, 다음 줄은:
```
    return <h1>The value of customKey is: {process.env.customKey}</h1>
```

결과적으로 이렇게 됩니다:
```
    return <h1>The value of customKey is: {'my-value'}</h1>
```

보내기