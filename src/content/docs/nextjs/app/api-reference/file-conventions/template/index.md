---
title: '파일 시스템 규칙: template.js'
description: '파일에서 기본 React 컴포넌트를 export하여 템플릿을 정의할 수 있다. 이 컴포넌트는  prop을 받아야 한다.'
---

# 파일 시스템 규칙: template.js | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/template

[API Reference](https://nextjs.org/docs/app/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)template.js

페이지 복사

# template.js

최종 업데이트 2026년 2월 20일

**template** 파일은 레이아웃이나 페이지를 감싼다는 점에서 [layout](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-layout)과 유사하다. 라우트 전반에 걸쳐 지속되고 상태를 유지하는 레이아웃과 달리 템플릿에는 고유한 키가 부여되므로 자식 Client Components는 내비게이션 시 상태가 초기화된다.

다음과 같은 상황에서 유용하다:

  * 내비게이션 시 `useEffect`를 다시 동기화해야 할 때.
  * 내비게이션 시 하위 Client Components의 상태를 초기화해야 할 때. 예: 입력 필드.
  * 기본 프레임워크 동작을 변경하려는 경우. 예: 레이아웃 내부 Suspense 경계는 최초 로드에서만 폴백을 표시하지만 템플릿은 모든 내비게이션마다 표시한다.



## 규칙[](https://nextjs.org/docs/app/api-reference/file-conventions/template#convention)

`template.js` 파일에서 기본 React 컴포넌트를 export하여 템플릿을 정의할 수 있다. 이 컴포넌트는 `children` prop을 받아야 한다.

app/template.tsx

JavaScriptTypeScript
[code]
    export default function Template({ children }: { children: React.ReactNode }) {
      return <div>{children}</div>
    }
[/code]

중첩 관점에서 `template.js`는 레이아웃과 그 자식 사이에 렌더링된다. 다음은 단순화된 출력이다.

출력
[code]
    <Layout>
      {/* Note that the template is given a unique key. */}
      <Template key={routeParam}>{children}</Template>
    </Layout>
[/code]

## Props[](https://nextjs.org/docs/app/api-reference/file-conventions/template#props)

### `children` (필수)[](https://nextjs.org/docs/app/api-reference/file-conventions/template#children-required)

Template은 `children` prop을 받는다.

출력
[code]
    <Layout>
      {/* Note that the template is automatically given a unique key. */}
      <Template key={routeParam}>{children}</Template>
    </Layout>
[/code]

## 동작[](https://nextjs.org/docs/app/api-reference/file-conventions/template#behavior)

  * **Server Components**: 템플릿은 기본적으로 Server Components이다.
  * **With navigation**: 템플릿은 자체 세그먼트 레벨에 대해 고유 키를 받는다. 해당 세그먼트(동적 매개변수를 포함)가 바뀌면 다시 마운트된다. 더 깊은 세그먼트 내 내비게이션은 상위 템플릿을 다시 마운트하지 않는다. 검색 매개변수는 다시 마운트를 트리거하지 않는다.
  * **State reset**: 템플릿 내부의 모든 Client Component는 내비게이션 시 상태가 초기화된다.
  * **Effect re-run**: `useEffect` 등 효과는 컴포넌트가 다시 마운트되면서 재동기화된다.
  * **DOM reset**: 템플릿 내부의 DOM 요소는 완전히 다시 생성된다.



### 내비게이션 및 재마운트 시 템플릿 동작[](https://nextjs.org/docs/app/api-reference/file-conventions/template#templates-during-navigation-and-remounting)

이 섹션은 템플릿이 내비게이션 동안 어떻게 동작하는지 보여준다. 각 라우트 변경에서 어떤 템플릿이 왜 다시 마운트되는지 단계별로 설명한다.

다음 프로젝트 트리를 예로 들자:
[code] 
    app
    ├── about
    │   ├── page.tsx
    ├── blog
    │   ├── [slug]
    │   │   └── page.tsx
    │   ├── page.tsx
    │   └── template.tsx
    ├── layout.tsx
    ├── page.tsx
    └── template.tsx
    
[/code]

`/`에서 시작하면 React 트리는 대략 다음과 같다.

> 참고: 예시의 `key` 값은 설명을 위한 것으로, 실제 애플리케이션에서는 다를 수 있다.

출력
[code]
    <RootLayout>
      {/* app/template.tsx */}
      <Template key="/">
        <Page />
      </Template>
    </RootLayout>
[/code]

`/about`으로 이동하면(첫 번째 세그먼트 변경) 루트 템플릿 키가 바뀌고 다시 마운트된다.

출력
[code]
    <RootLayout>
      {/* app/template.tsx */}
      <Template key="/about">
        <AboutPage />
      </Template>
    </RootLayout>
[/code]

`/blog`로 이동하면(첫 번째 세그먼트 변경) 루트 템플릿 키가 바뀌어 다시 마운트되고, 블로그 레벨 템플릿이 마운트된다.

출력
[code]
    <RootLayout>
      {/* app/template.tsx (root) */}
      <Template key="/blog">
        {/* app/blog/template.tsx */}
        <Template key="/blog">
          <BlogIndexPage />
        </Template>
      </Template>
    </RootLayout>
[/code]

같은 첫 번째 세그먼트 내에서 `/blog/first-post`로 이동하면(자식 세그먼트 변경) 루트 템플릿 키는 그대로지만 블로그 레벨 템플릿 키가 바뀌어 다시 마운트된다.

출력
[code]
    <RootLayout>
      {/* app/template.tsx (root) */}
      <Template key="/blog">
        {/* app/blog/template.tsx */}
        {/* remounts because the child segment at this level changed */}
        <Template key="/blog/first-post">
          <BlogPostPage slug="first-post" />
        </Template>
      </Template>
    </RootLayout>
[/code]

`/blog/second-post`로 이동하면(같은 첫 번째 세그먼트, 다른 자식 세그먼트) 루트 템플릿 키는 그대로지만 블로그 레벨 템플릿 키가 바뀌어 다시 마운트된다.

출력
[code]
    <RootLayout>
      {/* app/template.tsx (root) */}
      <Template key="/blog">
        {/* app/blog/template.tsx */}
        {/* remounts again due to changed child segment */}
        <Template key="/blog/second-post">
          <BlogPostPage slug="second-post" />
        </Template>
      </Template>
    </RootLayout>
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/template#version-history)

버전| 변경 사항  
---|---  
`v13.0.0`| `template` 도입.  
  
도움이 되었나요?

지원됨.

보내기
