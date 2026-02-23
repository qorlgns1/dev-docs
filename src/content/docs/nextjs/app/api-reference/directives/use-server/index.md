---
title: '지시문: use server'
description: '지시문은 함수나 파일이 서버 측에서 실행되어야 함을 지정합니다. 파일 맨 위에 두면 해당 파일의 모든 함수가 서버 측 함수임을 나타내고, 함수의 상단에 인라인으로 추가하면 해당 함수를 Server Function으로 표시합니다. 이는 React 기능입니다.'
---

# 지시문: use server | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/directives/use-server

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[지시문](https://nextjs.org/docs/app/api-reference/directives)use server

페이지 복사

# use server

마지막 업데이트 2026년 2월 20일

`use server` 지시문은 함수나 파일이 **서버 측**에서 실행되어야 함을 지정합니다. 파일 맨 위에 두면 해당 파일의 모든 함수가 서버 측 함수임을 나타내고, 함수의 상단에 인라인으로 추가하면 해당 함수를 [Server Function](https://19.react.dev/reference/rsc/server-functions)으로 표시합니다. 이는 React 기능입니다.

## 파일 상단에서 `use server` 사용하기[](https://nextjs.org/docs/app/api-reference/directives/use-server#using-use-server-at-the-top-of-a-file)

다음 예제는 파일 맨 위에 `use server` 지시문이 있는 경우를 보여줍니다. 파일의 모든 함수가 서버에서 실행됩니다.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
    import { db } from '@/lib/db' // Your database client
     
    export async function createUser(data: { name: string; email: string }) {
      const user = await db.user.create({ data })
      return user
    }
[/code]

### 클라이언트 컴포넌트에서 Server Function 사용하기[](https://nextjs.org/docs/app/api-reference/directives/use-server#using-server-functions-in-a-client-component)

클라이언트 컴포넌트에서 Server Function을 사용하려면, 전용 파일을 만들고 파일 상단에 `use server` 지시문을 선언한 뒤 그 안에서 Server Function을 정의해야 합니다. 이렇게 만든 Server Function은 클라이언트 컴포넌트와 서버 컴포넌트 모두에서 import하여 실행할 수 있습니다.

`actions.ts`에 `fetchUsers` Server Function이 있다고 가정해 봅시다:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
    import { db } from '@/lib/db' // Your database client
     
    export async function fetchUsers() {
      const users = await db.user.findMany()
      return users
    }
[/code]

그런 다음 `fetchUsers` Server Function을 클라이언트 컴포넌트로 import하여 클라이언트 측에서 실행할 수 있습니다.

app/components/my-button.tsx

JavaScriptTypeScript
[code]
    'use client'
    import { fetchUsers } from '../actions'
     
    export default function MyButton() {
      return <button onClick={() => fetchUsers()}>Fetch Users</button>
    }
[/code]

## 인라인으로 `use server` 사용하기[](https://nextjs.org/docs/app/api-reference/directives/use-server#using-use-server-inline)

다음 예제에서는 함수 상단에 인라인으로 `use server`를 선언하여 해당 함수를 [Server Function](https://19.react.dev/reference/rsc/server-functions)으로 표시합니다:

app/posts/[id]/page.tsx

JavaScriptTypeScript
[code]
    import { EditPost } from './edit-post'
    import { revalidatePath } from 'next/cache'
     
    export default async function PostPage({ params }: { params: { id: string } }) {
      const post = await getPost(params.id)
     
      async function updatePost(formData: FormData) {
        'use server'
        await savePost(params.id, formData)
        revalidatePath(`/posts/${params.id}`)
      }
     
      return <EditPost updatePostAction={updatePost} post={post} />
    }
[/code]

## 보안 고려 사항[](https://nextjs.org/docs/app/api-reference/directives/use-server#security-considerations)

`use server` 지시문을 사용할 때는 모든 서버 측 로직이 안전하게 작성되었는지와 민감한 데이터가 보호되는지 반드시 확인해야 합니다.

### 인증 및 권한 부여[](https://nextjs.org/docs/app/api-reference/directives/use-server#authentication-and-authorization)

민감한 서버 측 작업을 수행하기 전에 항상 사용자 인증과 권한 부여를 수행하세요.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'
     
    import { db } from '@/lib/db' // Your database client
    import { authenticate } from '@/lib/auth' // Your authentication library
     
    export async function createUser(
      data: { name: string; email: string },
      token: string
    ) {
      const user = authenticate(token)
      if (!user) {
        throw new Error('Unauthorized')
      }
      const newUser = await db.user.create({ data })
      return newUser
    }
[/code]

## 참고자료[](https://nextjs.org/docs/app/api-reference/directives/use-server#reference)

`use server`에 대한 더 많은 정보는 [React 문서](https://react.dev/reference/rsc/use-server)를 참고하세요.

도움이 되었나요?

지원됨.

전송
