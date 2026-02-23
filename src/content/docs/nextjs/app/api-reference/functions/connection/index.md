---
title: '함수: connection'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/functions/connection'
---

# 함수: connection | Next.js

원본 URL: https://nextjs.org/docs/app/api-reference/functions/connection

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)connection

페이지 복사

# connection

2026년 2월 20일 업데이트

`connection()` 함수는 렌더링을 계속하기 전에 들어오는 사용자 요청을 기다려야 함을 명시할 수 있게 해 줍니다.

컴포넌트가 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)를 사용하지 않지만, 빌드 타임이 아닌 런타임에 동적으로 렌더링되길 원할 때 유용합니다. 이는 `Math.random()`이나 `new Date()`처럼 렌더링 결과를 의도적으로 바꾸고 싶은 외부 정보를 액세스할 때 주로 발생합니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import { connection } from 'next/server'
     
    export default async function Page() {
      await connection()
      // Everything below will be excluded from prerendering
      const rand = Math.random()
      return <span>{rand}</span>
    }
[/code]

## Reference[](https://nextjs.org/docs/app/api-reference/functions/connection#reference)

### Type[](https://nextjs.org/docs/app/api-reference/functions/connection#type)
[code] 
    function connection(): Promise<void>
[/code]

### Parameters[](https://nextjs.org/docs/app/api-reference/functions/connection#parameters)

  * 이 함수는 어떤 매개변수도 받지 않습니다.



### Returns[](https://nextjs.org/docs/app/api-reference/functions/connection#returns)

  * 이 함수는 `void` Promise를 반환하며, 이를 소비하도록 설계되지 않았습니다.



## Good to know[](https://nextjs.org/docs/app/api-reference/functions/connection#good-to-know)

  * `connection`은 Next.js의 미래 방향에 맞추기 위해 [`unstable_noStore`](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)를 대체합니다.
  * 동적 렌더링이 필요하면서 일반적인 Dynamic API를 사용하지 않을 때만 이 함수가 필요합니다.



### Version History[](https://nextjs.org/docs/app/api-reference/functions/connection#version-history)

버전| 변경 사항  
---|---  
`v15.0.0`| `connection`이 안정화되었습니다.  
`v15.0.0-RC`| `connection`이 도입되었습니다.  
  
도움이 되었나요?

지원됨.

전송
