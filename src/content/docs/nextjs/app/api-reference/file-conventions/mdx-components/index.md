---
title: '파일 시스템 규칙: mdx-components.js'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components'
---

# 파일 시스템 규칙: mdx-components.js | Next.js

원본 URL: https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components

# mdx-components.js

마지막 업데이트: 2026년 2월 20일

`mdx-components.js|tsx` 파일은 [`@next/mdx`를 App Router와 함께](https://nextjs.org/docs/app/guides/mdx) 사용하기 위해 **필수**이며, 이 파일 없이는 동작하지 않습니다. 추가로, [스타일을 커스터마이징](https://nextjs.org/docs/app/guides/mdx#using-custom-styles-and-components)하는 데도 활용할 수 있습니다.

프로젝트 루트(`pages` 또는 `app`과 동일한 계층, 필요하다면 `src` 내부 등)에 `mdx-components.tsx`(또는 `.js`) 파일을 두고 MDX 컴포넌트를 정의하세요.

mdx-components.tsx

JavaScriptTypeScript
[code]
    import type { MDXComponents } from 'mdx/types'

    const components: MDXComponents = {}

    export function useMDXComponents(): MDXComponents {
      return components
    }
[/code]

## 내보내기[](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components#exports)

### `useMDXComponents` 함수[](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components#usemdxcomponents-function)

파일은 `useMDXComponents`라는 단일 함수를 내보내야 하며, 이 함수는 어떤 인수도 받지 않습니다.

mdx-components.tsx

JavaScriptTypeScript
[code]
    import type { MDXComponents } from 'mdx/types'

    const components: MDXComponents = {}

    export function useMDXComponents(): MDXComponents {
      return components
    }
[/code]

## 버전 기록[](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components#version-history)

버전| 변경 사항
---|---
`v13.1.2`| MDX 컴포넌트 추가

## MDX 컴포넌트 더 알아보기

- [MDXNext.js 앱에서 MDX를 구성하고 사용하는 방법을 알아보세요.](https://nextjs.org/docs/app/guides/mdx)

보내기
