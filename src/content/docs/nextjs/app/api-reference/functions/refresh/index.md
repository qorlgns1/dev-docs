---
title: 'Functions: refresh'
description: '는 서버 액션 내부에서 클라이언트 라우터를 새로 고칠 수 있게 해줍니다.'
---

# Functions: refresh | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/refresh

Copy page

# refresh

마지막 업데이트 2026년 2월 20일

`refresh`는 [서버 액션](https://nextjs.org/docs/app/getting-started/updating-data) 내부에서 클라이언트 라우터를 새로 고칠 수 있게 해줍니다.

## 사용법[](https://nextjs.org/docs/app/api-reference/functions/refresh#usage)

`refresh`는 **오직** 서버 액션 내부에서만 호출할 수 있습니다. 라우트 핸들러, 클라이언트 컴포넌트 또는 다른 어떤 컨텍스트에서도 사용할 수 없습니다.

## 매개변수[](https://nextjs.org/docs/app/api-reference/functions/refresh#parameters)
[code]
    refresh(): void;
[/code]

## 반환값[](https://nextjs.org/docs/app/api-reference/functions/refresh#returns)

`refresh`는 값을 반환하지 않습니다.

## 예제[](https://nextjs.org/docs/app/api-reference/functions/refresh#examples)

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { refresh } from 'next/cache'

    export async function createPost(formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')

      // Create the post in your database
      const post = await db.post.create({
        data: { title, content },
      })

      refresh()
    }
[/code]

### 서버 액션 외부에서 사용하면 발생하는 오류[](https://nextjs.org/docs/app/api-reference/functions/refresh#error-when-used-outside-server-actions)

app/api/posts/route.ts

JavaScriptTypeScript
[code]
    import { refresh } from 'next/cache'

    export async function POST() {
      // This will throw an error
      refresh()
    }
[/code]

supported.

Send
