---
title: '파일 시스템 규칙: forbidden.js'
description: '이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 GitHub에 피드백을 공유해 주세요.'
---

# 파일 시스템 규칙: forbidden.js | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/forbidden

# forbidden.js

이 기능은 현재 실험적이며 변경될 수 있으므로 프로덕션 환경에서는 권장되지 않습니다. 사용해 보고 [GitHub](https://github.com/vercel/next.js/issues)에 피드백을 공유해 주세요.

마지막 업데이트: 2026년 2월 20일

인증 중에 [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden) 함수가 호출될 때 UI를 렌더링하기 위해 **forbidden** 파일을 사용합니다. UI를 사용자 정의할 수 있을 뿐만 아니라 Next.js는 `403` 상태 코드를 반환합니다.

app/forbidden.tsx

JavaScriptTypeScript
```
    import Link from 'next/link'

    export default function Forbidden() {
      return (
        <div>
          <h2>Forbidden</h2>
          <p>You are not authorized to access this resource.</p>
          <Link href="/">Return Home</Link>
        </div>
      )
    }
```

## 참고[](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden#reference)

### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden#props)

`forbidden.js` 컴포넌트는 어떠한 props도 받지 않습니다.

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden#version-history)

버전| 변경 사항
---|---
`v15.1.0`| `forbidden.js` 도입.

##

- [forbidden](https://nextjs.org/docs/app/api-reference/functions/forbidden)
  - 함수에 대한 API 레퍼런스입니다.