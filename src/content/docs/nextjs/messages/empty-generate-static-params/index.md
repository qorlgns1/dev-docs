---
title: 'Cache Components에서 비어 있는 generateStaticParams'
description: 'Next.js 애플리케이션에서 Cache Components를 사용 중이며,  함수 중 하나가 빈 배열을 반환하여 빌드 오류가 발생했습니다.'
---

# Cache Components에서 비어 있는 generateStaticParams | Next.js

Source URL: https://nextjs.org/docs/messages/empty-generate-static-params

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)Cache Components에서 비어 있는 generateStaticParams

# Cache Components에서 비어 있는 generateStaticParams

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/empty-generate-static-params#why-this-error-occurred)

Next.js 애플리케이션에서 [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components)를 사용 중이며, `generateStaticParams` 함수 중 하나가 빈 배열을 반환하여 빌드 오류가 발생했습니다.

Cache Components가 활성화되면 Next.js는 라우트가 런타임 동적 액세스 오류 없이 적절히 사전 렌더링될 수 있도록 빌드 시 유효성 검사를 수행합니다. `generateStaticParams`가 빈 배열을 반환하면 Next.js는 해당 라우트가 런타임에 `await cookies()`, `await headers()`, `await searchParams`와 같은 동적 값을 액세스하지 않을 것임을 검증할 수 없고, 이는 오류를 유발합니다.

이 엄격한 요구 사항은 다음을 보장합니다:

  * 빌드 시 유효성 검사가 잠재적인 런타임 오류를 조기에 포착
  * Cache Components를 사용하는 모든 라우트가 검증 가능한 최소 한 개의 정적 변형을 보유
  * 런타임에 실패하는 라우트를 실수로 배포하지 않음

## 가능한 해결 방법[](https://nextjs.org/docs/messages/empty-generate-static-params#possible-ways-to-fix-it)

### 옵션 1: 최소 한 개의 정적 매개변수를 반환[](https://nextjs.org/docs/messages/empty-generate-static-params#option-1-return-at-least-one-static-param)

`generateStaticParams` 함수가 최소 한 세트의 매개변수를 반환하도록 수정하세요. 가장 일반적인 해결책이며 빌드 시 유효성 검사가 정상적으로 작동하게 합니다.

app/blog/[slug]/page.tsx
```
    // This will cause an error with Cache Components
    export async function generateStaticParams() {
      return [] // Empty array not allowed
    }

    // Return at least one sample param
    export async function generateStaticParams() {
      return [{ slug: 'hello-world' }, { slug: 'getting-started' }]
    }
```

이러한 샘플은 두 가지 목적을 수행합니다:

  1. **빌드 시 유효성 검사** : 라우트 구조가 안전한지 확인
  2. **사전 렌더링** : 인기 라우트에 대해 즉시 로드되는 페이지 생성

빌드 과정은 샘플 매개변수로 실행되는 코드 경로만 검증합니다. 런타임 매개변수가 조건부 로직을 트리거해 Suspense 없이 `cookies()` 같은 런타임 API에 접근하거나 Suspense 또는 `use cache` 없이 동적 콘텐츠를 렌더링하면 해당 분기에서 런타임 오류가 발생합니다.

### 옵션 2: 플레이스홀더 매개변수 사용[](https://nextjs.org/docs/messages/empty-generate-static-params#option-2-use-a-placeholder-param)

빌드 시 실제 값을 모른다면 검증용 플레이스홀더를 사용할 수 있습니다. 다만 이는 빌드 시 유효성 검사의 목적을 무력화하므로 피해야 합니다:

app/blog/[slug]/page.tsx
```
    export async function generateStaticParams() {
      // Placeholder only validates one code path
      return [{ slug: '__placeholder__' }]
    }

    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params

      // Handle placeholder case
      if (slug === '__placeholder__') {
        notFound()
      }

      // Real params may trigger code paths
      // that access dynamic APIs incorrectly, causing
      // runtime errors that cannot be caught by error boundaries
      const post = await getPost(slug)
      return <div>{post.title}</div>
    }
```

플레이스홀더를 사용하면 빌드 시 유효성 검사가 최소한으로만 이루어져 실제 매개변수 값에서 런타임 오류가 발생할 위험이 커집니다.

## 유용한 링크[](https://nextjs.org/docs/messages/empty-generate-static-params#useful-links)

  * [Cache Components 문서](https://nextjs.org/docs/app/getting-started/cache-components)
  * [generateStaticParams API 레퍼런스](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)
  * [Cache Components와 함께 사용하는 동적 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components)

보내기