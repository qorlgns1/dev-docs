---
title: '가이드: MDX'
description: 'Next.js는 애플리케이션 내부의 로컬 MDX 콘텐츠는 물론, 서버에서 동적으로 가져온 원격 MDX 파일도 지원합니다. Next.js 플러그인은 마크다운과 React 컴포넌트를 HTML로 변환하며, App Router에서 기본인 서버 컴포넌트에서도 사용할 수 있도록 ...'
---

# 가이드: MDX | Next.js

소스 URL: https://nextjs.org/docs/app/guides/mdx

# Next.js에서 마크다운과 MDX를 사용하는 방법

마지막 업데이트 2026년 2월 20일

[Markdown](https://daringfireball.net/projects/markdown/syntax)은 텍스트 서식을 지정할 수 있는 경량 마크업 언어입니다. 일반 텍스트 문법으로 작성한 뒤 구조적으로 유효한 HTML로 변환할 수 있으며, 웹사이트나 블로그의 콘텐츠 작성에 자주 쓰입니다.

You write...
```
    I **love** using [Next.js](https://nextjs.org/)
```

출력:
```
    <p>I <strong>love</strong> using <a href="https://nextjs.org/">Next.js</a></p>
```

[MDX](https://mdxjs.com/)는 마크다운의 상위 집합으로, 마크다운 파일 안에 [JSX](https://react.dev/learn/writing-markup-with-jsx)를 직접 작성할 수 있습니다. 콘텐츠에 동적 상호작용을 추가하고 React 컴포넌트를 삽입할 수 있는 강력한 방법입니다.

Next.js는 애플리케이션 내부의 로컬 MDX 콘텐츠는 물론, 서버에서 동적으로 가져온 원격 MDX 파일도 지원합니다. Next.js 플러그인은 마크다운과 React 컴포넌트를 HTML로 변환하며, App Router에서 기본인 서버 컴포넌트에서도 사용할 수 있도록 지원합니다.

> **알아두면 좋아요** : 완전한 예제를 확인하려면 [Portfolio Starter Kit](https://vercel.com/templates/next.js/portfolio-starter-kit) 템플릿을 살펴보세요.

## 종속성 설치[](https://nextjs.org/docs/app/guides/mdx#install-dependencies)

`@next/mdx` 패키지와 관련 패키지는 Next.js가 마크다운과 MDX를 처리하도록 구성하는 데 사용됩니다. **로컬 파일에서 데이터를 읽어와** `/pages` 또는 `/app` 디렉터리 내에 `.md` 또는 `.mdx` 확장자를 가진 페이지를 직접 만들 수 있습니다.

Next.js에서 MDX를 렌더링하려면 다음 패키지를 설치하세요:

pnpmnpmyarnbun

Terminal
```
    pnpm add @next/mdx @mdx-js/loader @mdx-js/react @types/mdx
```

## `next.config.mjs` 구성[](https://nextjs.org/docs/app/guides/mdx#configure-nextconfigmjs)

프로젝트 루트에 있는 `next.config.mjs` 파일을 업데이트해 MDX를 사용할 수 있도록 구성하세요:

next.config.mjs
```
    import createMDX from '@next/mdx'

    /** @type {import('next').NextConfig} */
    const nextConfig = {
      // Configure `pageExtensions` to include markdown and MDX files
      pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
      // Optionally, add any other Next.js config below
    }

    const withMDX = createMDX({
      // Add markdown plugins here, as desired
    })

    // Merge MDX config with Next.js config
    export default withMDX(nextConfig)
```

이렇게 하면 `.mdx` 파일을 애플리케이션에서 페이지, 라우트 또는 import로 사용할 수 있습니다.

### `.md` 파일 처리[](https://nextjs.org/docs/app/guides/mdx#handling-md-files)

기본적으로 `next/mdx`는 `.mdx` 확장자 파일만 컴파일합니다. `.md` 파일을 webpack으로 처리하려면 `extension` 옵션을 업데이트하세요:

next.config.mjs
```
    const withMDX = createMDX({
      extension: /\.(md|mdx)$/,
    })
```

## `mdx-components.tsx` 파일 추가[](https://nextjs.org/docs/app/guides/mdx#add-an-mdx-componentstsx-file)

프로젝트 루트(예: `pages` 또는 `app`와 같은 레벨, 필요 시 `src` 내부)에 `mdx-components.tsx`(또는 `.js`) 파일을 만들어 전역 MDX 컴포넌트를 정의하세요.

mdx-components.tsx

JavaScriptTypeScript
```
    import type { MDXComponents } from 'mdx/types'

    const components: MDXComponents = {}

    export function useMDXComponents(): MDXComponents {
      return components
    }
```

> **알아두면 좋아요** :
>
>   * App Router에서 `@next/mdx`를 사용하려면 `mdx-components.tsx`가 **필수**이며, 없으면 작동하지 않습니다.
>   * [`mdx-components.tsx` 파일 컨벤션](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components)에 대해 자세히 알아보세요.
>   * [사용자 정의 스타일과 컴포넌트를 사용하는 방법](https://nextjs.org/docs/app/guides/mdx#using-custom-styles-and-components)을 살펴보세요.
>

## MDX 렌더링[](https://nextjs.org/docs/app/guides/mdx#rendering-mdx)

Next.js의 파일 기반 라우팅을 사용하거나 MDX 파일을 다른 페이지로 import하여 MDX를 렌더링할 수 있습니다.

### 파일 기반 라우팅 사용[](https://nextjs.org/docs/app/guides/mdx#using-file-based-routing)

파일 기반 라우팅을 사용할 때는 다른 페이지와 동일하게 MDX 페이지를 사용할 수 있습니다.

App Router 앱에서는 [메타데이터](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)도 함께 사용할 수 있습니다.

`/app` 디렉터리 안에 새 MDX 페이지를 만드세요:
```
      my-project
      ├── app
      │   └── mdx-page
      │       └── page.(mdx/md)
      |── mdx-components.(tsx/js)
      └── package.json
```

이 파일들에서 MDX를 사용할 수 있으며, MDX 페이지 안에서 React 컴포넌트를 직접 import할 수도 있습니다:
```
    import { MyComponent } from 'my-component'

    # Welcome to my MDX page!

    This is some **bold** and _italics_ text.

    This is a list in markdown:

    - One
    - Two
    - Three

    Checkout my React component:

    <MyComponent />
```

`/mdx-page` 라우트로 이동하면 렌더링된 MDX 페이지가 표시되어야 합니다.

### import 사용[](https://nextjs.org/docs/app/guides/mdx#using-imports)

`/app` 디렉터리에 새 페이지를 만들고 원하는 위치에 MDX 파일을 추가하세요:
```
      .
      ├── app/
      │   └── mdx-page/
      │       └── page.(tsx/js)
      ├── markdown/
      │   └── welcome.(mdx/md)
      ├── mdx-components.(tsx/js)
      └── package.json
```

이 파일들에서 MDX를 사용할 수 있으며, MDX 페이지 안에서 React 컴포넌트를 직접 import할 수도 있습니다:

페이지 내부에서 MDX 파일을 import하여 콘텐츠를 표시하세요:

app/mdx-page/page.tsx

JavaScriptTypeScript
```
    import Welcome from '@/markdown/welcome.mdx'

    export default function Page() {
      return <Welcome />
    }
```

`/mdx-page` 라우트로 이동하면 렌더링된 MDX 페이지가 표시되어야 합니다.

### 동적 import 사용[](https://nextjs.org/docs/app/guides/mdx#using-dynamic-imports)

파일 시스템 라우팅 대신 동적 MDX 컴포넌트를 import할 수 있습니다.

예를 들어, 별도의 디렉터리에서 MDX 컴포넌트를 로드하는 동적 라우트 세그먼트를 가질 수 있습니다:

[`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)를 사용해 제공된 라우트를 사전 렌더링할 수 있습니다. `dynamicParams`를 `false`로 설정하면 `generateStaticParams`에 정의되지 않은 라우트에 접근할 때 404가 발생합니다.

app/blog/[slug]/page.tsx

JavaScriptTypeScript
```
    export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const { slug } = await params
      const { default: Post } = await import(`@/content/${slug}.mdx`)

      return <Post />
    }

    export function generateStaticParams() {
      return [{ slug: 'welcome' }, { slug: 'about' }]
    }

    export const dynamicParams = false
```

> **알아두면 좋아요** : import에서 `.mdx` 파일 확장자를 명시하세요. [모듈 경로 별칭](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases)(예: `@/content`)을 사용할 필요는 없지만, import 경로를 단순화하는 데 도움이 됩니다.

## 사용자 정의 스타일과 컴포넌트 사용[](https://nextjs.org/docs/app/guides/mdx#using-custom-styles-and-components)

마크다운이 렌더링되면 기본 HTML 요소에 매핑됩니다. 예를 들어, 다음 마크다운을 작성하면:
```
    ## This is a heading

    This is a list in markdown:

    - One
    - Two
    - Three
```

다음 HTML이 생성됩니다:
```
    <h2>This is a heading</h2>

    <p>This is a list in markdown:</p>

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
    </ul>
```

마크다운을 스타일링하려면 생성된 HTML 요소에 매핑되는 사용자 정의 컴포넌트를 제공하면 됩니다. 스타일과 컴포넌트는 전역, 로컬, 공유 레이아웃 차원에서 구현할 수 있습니다.

### 전역 스타일과 컴포넌트[](https://nextjs.org/docs/app/guides/mdx#global-styles-and-components)

`mdx-components.tsx`에 스타일과 컴포넌트를 추가하면 애플리케이션의 _모든_ MDX 파일에 영향을 줍니다.

mdx-components.tsx

JavaScriptTypeScript
```
    import type { MDXComponents } from 'mdx/types'
    import Image, { ImageProps } from 'next/image'

    // This file allows you to provide custom React components
    // to be used in MDX files. You can import and use any
    // React component you want, including inline styles,
    // components from other libraries, and more.

    const components = {
      // Allows customizing built-in components, e.g. to add styling.
      h1: ({ children }) => (
        <h1 style={{ color: 'red', fontSize: '48px' }}>{children}</h1>
      ),
      img: (props) => (
        <Image
          sizes="100vw"
          style={{ width: '100%', height: 'auto' }}
          {...(props as ImageProps)}
        />
      ),
    } satisfies MDXComponents

    export function useMDXComponents(): MDXComponents {
      return components
    }
```

### 로컬 스타일과 컴포넌트[](https://nextjs.org/docs/app/guides/mdx#local-styles-and-components)

특정 페이지에만 스타일과 컴포넌트를 적용하려면 import한 MDX 컴포넌트에 전달하면 됩니다. 이러한 설정은 [전역 스타일과 컴포넌트](https://nextjs.org/docs/app/guides/mdx#global-styles-and-components)와 병합되며, 필요한 부분만 재정의합니다.

app/mdx-page/page.tsx

JavaScriptTypeScript
```
    import Welcome from '@/markdown/welcome.mdx'

    function CustomH1({ children }) {
      return <h1 style={{ color: 'blue', fontSize: '100px' }}>{children}</h1>
    }

    const overrideComponents = {
      h1: CustomH1,
    }

    export default function Page() {
      return <Welcome components={overrideComponents} />
    }
```

### 공유 레이아웃[](https://nextjs.org/docs/app/guides/mdx#shared-layouts)

MDX 페이지에서 레이아웃을 공유하려면 App Router의 [빌트인 레이아웃 지원](https://nextjs.org/docs/app/api-reference/file-conventions/layout)을 사용하면 됩니다.

app/mdx-page/layout.tsx

JavaScriptTypeScript
```
    export default function MdxLayout({ children }: { children: React.ReactNode }) {
      // Create any shared layout or styles here
      return <div style={{ color: 'blue' }}>{children}</div>
    }
```

### Tailwind typography 플러그인 사용[](https://nextjs.org/docs/app/guides/mdx#using-tailwind-typography-plugin)

애플리케이션 스타일링에 [Tailwind](https://tailwindcss.com)를 사용한다면 [`@tailwindcss/typography` 플러그인](https://tailwindcss.com/docs/plugins#typography)을 통해 Tailwind 구성과 스타일을 마크다운 콘텐츠에도 재사용할 수 있습니다.

이 플러그인은 마크다운처럼 외부 소스에서 가져온 콘텐츠 블록에 타이포그래피 스타일을 적용할 수 있는 `prose` 클래스를 추가합니다.

[Tailwind typography를 설치](https://github.com/tailwindlabs/tailwindcss-typography?tab=readme-ov-file#installation)하고 [공유 레이아웃](https://nextjs.org/docs/app/guides/mdx#shared-layouts)과 함께 사용하여 원하는 `prose` 스타일을 추가하세요.

app/mdx-page/layout.tsx

JavaScriptTypeScript
```
    export default function MdxLayout({ children }: { children: React.ReactNode }) {
      // Create any shared layout or styles here
      return (
        <div className="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
          {children}
        </div>
      )
    }
```

## 프론트매터[](https://nextjs.org/docs/app/guides/mdx#frontmatter)

프론트매터는 페이지에 대한 데이터를 저장하는 YAML 유사 키/값 쌍입니다. `@next/mdx`는 기본적으로 프론트매터를 **지원하지 않지만**, 다음과 같이 MDX 콘텐츠에 프론트매터를 추가하는 다양한 솔루션이 있습니다:

  * [remark-frontmatter](https://github.com/remarkjs/remark-frontmatter)

* [remark-mdx-frontmatter](https://github.com/remcohaszing/remark-mdx-frontmatter)
  * [gray-matter](https://github.com/jonschlinkert/gray-matter)

`@next/mdx`는 다른 JavaScript 컴포넌트와 동일하게 export를 사용할 수 있도록 **지원합니다**:

이제 MDX 파일 바깥에서도 메타데이터를 참조할 수 있습니다:

app/blog/page.tsx

JavaScriptTypeScript
```
    import BlogPost, { metadata } from '@/content/blog-post.mdx'

    export default function Page() {
      console.log('metadata: ', metadata)
      //=> { author: 'John Doe' }
      return <BlogPost />
    }
```

이는 MDX 모음에서 반복 처리하며 데이터를 추출하고 싶을 때 흔히 사용됩니다. 예를 들어 모든 블로그 게시글에서 블로그 인덱스 페이지를 만드는 경우입니다. [Node의 `fs` 모듈](https://nodejs.org/api/fs.html)이나 [globby](https://www.npmjs.com/package/globby) 같은 패키지를 사용해 게시글 디렉터리를 읽고 메타데이터를 추출할 수 있습니다.

> **알아두면 좋아요** :
>
>   * `fs`, `globby` 등은 서버 측에서만 사용할 수 있습니다.
>   * 완전한 작동 예시는 [Portfolio Starter Kit](https://vercel.com/templates/next.js/portfolio-starter-kit) 템플릿을 참고하세요.
>

## remark 및 rehype 플러그인[](https://nextjs.org/docs/app/guides/mdx#remark-and-rehype-plugins)

원한다면 remark와 rehype 플러그인을 제공해 MDX 콘텐츠를 변환할 수 있습니다.

예를 들어 [`remark-gfm`](https://github.com/remarkjs/remark-gfm)을 사용하면 GitHub Flavored Markdown을 지원할 수 있습니다.

remark와 rehype 생태계는 ESM만 지원하므로, 구성 파일로 `next.config.mjs` 또는 `next.config.ts`를 사용해야 합니다.

next.config.mjs
```
    import remarkGfm from 'remark-gfm'
    import createMDX from '@next/mdx'

    /** @type {import('next').NextConfig} */
    const nextConfig = {
      // Allow .mdx extensions for files
      pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
      // Optionally, add any other Next.js config below
    }

    const withMDX = createMDX({
      // Add markdown plugins here, as desired
      options: {
        remarkPlugins: [remarkGfm],
        rehypePlugins: [],
      },
    })

    // Combine MDX and Next.js config
    export default withMDX(nextConfig)
```

### Turbopack과 함께 플러그인 사용하기[](https://nextjs.org/docs/app/guides/mdx#using-plugins-with-turbopack)

[Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)에서 플러그인을 사용하려면 최신 `@next/mdx`로 업그레이드한 뒤 문자열로 플러그인 이름을 지정하세요:

next.config.mjs
```
    import createMDX from '@next/mdx'

    /** @type {import('next').NextConfig} */
    const nextConfig = {
      pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
    }

    const withMDX = createMDX({
      options: {
        remarkPlugins: [
          // Without options
          'remark-gfm',
          // With options
          ['remark-toc', { heading: 'The Table' }],
        ],
        rehypePlugins: [
          // Without options
          'rehype-slug',
          // With options
          ['rehype-katex', { strict: true, throwOnError: true }],
        ],
      },
    })

    export default withMDX(nextConfig)
```

> **알아두면 좋아요** :
>
> 직렬화 가능한 옵션이 없는 remark와 rehype 플러그인은 JavaScript 함수를 Rust로 전달할 수 없기 때문에 아직 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)에서 사용할 수 없습니다.
>

## 심층 탐구: 마크다운을 HTML로 어떻게 변환하나요?[](https://nextjs.org/docs/app/guides/mdx#deep-dive-how-do-you-transform-markdown-into-html)

React는 기본적으로 마크다운을 이해하지 못합니다. 마크다운 평문은 먼저 HTML로 변환되어야 합니다. 이는 `remark`와 `rehype`로 수행할 수 있습니다.

`remark`는 마크다운을 중심으로 한 도구 생태계이며, `rehype`는 HTML을 위한 동일한 개념입니다. 예를 들어 다음 코드 스니펫은 마크다운을 HTML로 변환합니다:
```
    import { unified } from 'unified'
    import remarkParse from 'remark-parse'
    import remarkRehype from 'remark-rehype'
    import rehypeSanitize from 'rehype-sanitize'
    import rehypeStringify from 'rehype-stringify'

    main()

    async function main() {
      const file = await unified()
        .use(remarkParse) // Convert into markdown AST
        .use(remarkRehype) // Transform to HTML AST
        .use(rehypeSanitize) // Sanitize HTML input
        .use(rehypeStringify) // Convert AST into serialized HTML
        .process('Hello, Next.js!')

      console.log(String(file)) // <p>Hello, Next.js!</p>
    }
```

`remark`와 `rehype` 생태계에는 [syntax highlighting](https://github.com/atomiks/rehype-pretty-code), [linking headings](https://github.com/rehypejs/rehype-autolink-headings), [generating a table of contents](https://github.com/remarkjs/remark-toc) 등을 위한 플러그인이 포함되어 있습니다.

위에서 설명한 대로 `@next/mdx`를 사용할 때는 `remark`나 `rehype`를 직접 사용할 **필요가 없습니다**. 여기서는 `@next/mdx` 패키지가 내부적으로 무엇을 하는지 더 깊이 이해하기 위해 설명합니다.

## Rust 기반 MDX 컴파일러 사용하기(실험적)[](https://nextjs.org/docs/app/guides/mdx#using-the-rust-based-mdx-compiler-experimental)

Next.js는 Rust로 작성된 새로운 MDX 컴파일러를 지원합니다. 이 컴파일러는 아직 실험 단계이며 프로덕션 사용이 권장되지 않습니다. 새 컴파일러를 사용하려면 `withMDX`에 전달할 때 `next.config.js`를 구성해야 합니다:

next.config.js
```
    module.exports = withMDX({
      experimental: {
        mdxRs: true,
      },
    })
```

`mdxRs`는 mdx 파일을 어떻게 변환할지 구성하는 객체도 받을 수 있습니다.

next.config.js
```
    module.exports = withMDX({
      experimental: {
        mdxRs: {
          jsxRuntime?: string            // Custom jsx runtime
          jsxImportSource?: string       // Custom jsx import source,
          mdxType?: 'gfm' | 'commonmark' // Configure what kind of mdx syntax will be used to parse & transform
        },
      },
    })
```

## 유용한 링크[](https://nextjs.org/docs/app/guides/mdx#helpful-links)

  * [MDX](https://mdxjs.com)
  * [`@next/mdx`](https://www.npmjs.com/package/@next/mdx)
  * [remark](https://github.com/remarkjs/remark)
  * [rehype](https://github.com/rehypejs/rehype)
  * [Markdoc](https://markdoc.dev/docs/nextjs)

보내기