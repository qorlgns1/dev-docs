---
title: 'next.config.js 옵션: optimizePackageImports'
description: '이 기능은 현재 실험적이며 추후 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. 자유롭게 시도해 보고 GitHub에서 피드백을 공유해주세요.'
---

# next.config.js 옵션: optimizePackageImports | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports

Copy page

# optimizePackageImports

이 기능은 현재 실험적이며 추후 변경될 수 있으므로 프로덕션에서는 권장되지 않습니다. 자유롭게 시도해 보고 [GitHub](https://github.com/vercel/next.js/issues)에서 피드백을 공유해주세요.

Last updated February 20, 2026

일부 패키지는 수백 혹은 수천 개의 모듈을 export하여 개발 및 프로덕션 환경 모두에서 성능 문제를 일으킬 수 있습니다.

`experimental.optimizePackageImports`에 패키지를 추가하면 실제로 사용하는 모듈만 로드하면서도 다수의 named export를 사용하는 import 문을 그대로 작성할 수 있는 편의를 제공합니다.

next.config.js
[code]
    module.exports = {
      experimental: {
        optimizePackageImports: ['package-name'],
      },
    }
[/code]

다음 라이브러리는 기본적으로 최적화됩니다:

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

Was this helpful?

supported.

Send
