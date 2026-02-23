---
title: 'next.config.js: optimizePackageImports'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports'
---

# next.config.js: optimizePackageImports | Next.js

원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports

복사 페이지

# optimizePackageImports

이 기능은 현재 실험 단계이며 변경될 수 있으므로 프로덕션 사용은 권장되지 않습니다. [GitHub](https://github.com/vercel/next.js/issues)에서 사용해 보고 피드백을 공유해주세요.

마지막 업데이트 2026년 2월 20일

일부 패키지는 수백 또는 수천 개의 모듈을 내보낼 수 있으며, 이는 개발과 프로덕션에서 성능 문제를 유발할 수 있습니다.

패키지를 `experimental.optimizePackageImports`에 추가하면 실제로 사용하는 모듈만 로드하면서도 다수의 이름이 지정된 export를 사용하는 import 문 작성의 편의성을 유지할 수 있습니다.

next.config.js
```
    module.exports = {
      experimental: {
        optimizePackageImports: ['package-name'],
      },
    }
```

다음 라이브러리는 기본적으로 최적화됩니다.

  * `lucide-react`
  * `date-fns`
  * `lodash-es`
  * `ramda`
  * `antd`
  * `react-bootstrap`
  * `ahooks`
  * `@ant-design/icons`
  * `@headlessui/react`
  * `@headlessui-float/react`
  * `@heroicons/react/20/solid`
  * `@heroicons/react/24/solid`
  * `@heroicons/react/24/outline`
  * `@visx/visx`
  * `@tremor/react`
  * `rxjs`
  * `@mui/material`
  * `@mui/icons-material`
  * `recharts`
  * `react-use`
  * `@material-ui/core`
  * `@material-ui/icons`
  * `@tabler/icons-react`
  * `mui-core`
  * `react-icons/*`
  * `effect`
  * `@effect/*`