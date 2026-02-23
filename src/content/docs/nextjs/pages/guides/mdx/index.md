---
title: '가이드: MDX'
description: 'Next.js는 애플리케이션 내부의 로컬 MDX 콘텐츠뿐 아니라 서버에서 동적으로 가져오는 원격 MDX 파일도 지원합니다. Next.js 플러그인은 마크다운과 React 컴포넌트를 HTML로 변환하며, App Router에서 기본인 서버 컴포넌트 사용도 지원합니다.'
---

# 가이드: MDX | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/mdx

# Next.js에서 Markdown과 MDX를 사용하는 방법

마지막 업데이트 2026년 2월 20일

[Markdown](https://daringfireball.net/projects/markdown/syntax)은 텍스트를 서식화하기 위한 경량 마크업 언어입니다. 일반 텍스트 문법으로 작성한 뒤 구조적으로 유효한 HTML로 변환할 수 있으며, 웹사이트나 블로그 콘텐츠를 작성할 때 자주 사용됩니다.

You write...
[code]
    I **love** using [Next.js](https://nextjs.org/)
[/code]

Output:
[code]
    <p>I <strong>love</strong> using <a href="https://nextjs.org/">Next.js</a></p>
[/code]

[MDX](https://mdxjs.com/)는 마크다운의 상위 집합으로서 마크다운 파일 안에서 [JSX](https://react.dev/learn/writing-markup-with-jsx)를 직접 작성할 수 있게 해 줍니다. 콘텐츠 안에 동적 상호작용을 추가하고 React 컴포넌트를 임베드하기 위한 강력한 방법입니다.

Next.js는 애플리케이션 내부의 로컬 MDX 콘텐츠뿐 아니라 서버에서 동적으로 가져오는 원격 MDX 파일도 지원합니다. Next.js 플러그인은 마크다운과 React 컴포넌트를 HTML로 변환하며, App Router에서 기본인 서버 컴포넌트 사용도 지원합니다.

> **알아두면 좋아요** : 완전한 작동 예시는 [Portfolio Starter Kit](https://vercel.com/templates/next.js/portfolio-starter-kit) 템플릿에서 확인하세요.

## 설치해야 할 의존성[](https://nextjs.org/docs/pages/guides/mdx#install-dependencies)

`@next/mdx` 패키지와 관련 패키지는 Next.js가 마크다운과 MDX를 처리하도록 구성하는 데 사용됩니다. **로컬 파일에서 데이터를 가져오므로** `/pages`나 `/app` 디렉터리에서 `.md` 또는 `.mdx` 확장자를 가진 페이지를 직접 만들 수 있습니다.

Next.js에서 MDX를 렌더링하려면 다음 패키지를 설치하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm add @next/mdx @mdx-js/loader @mdx-js/react @types/mdx
[/code]

## `next.config.mjs` 구성하기[](https://nextjs.org/docs/pages/guides/mdx#configure-nextconfigmjs)

프로젝트 루트에 있는 `next.config.mjs` 파일을 업데이트해 MDX를 사용하도록 구성하세요:

next.config.mjs
[code]
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
[/code]

이렇게 하면 `.mdx` 파일을 애플리케이션의 페이지, 라우트, 혹은 import로 사용할 수 있습니다.

### `.md` 파일 처리하기[](https://nextjs.org/docs/pages/guides/mdx#handling-md-files)

기본적으로 `next/mdx`는 `.mdx` 확장자를 가진 파일만 컴파일합니다. webpack으로 `.md` 파일을 처리하려면 `extension` 옵션을 업데이트하세요:

next.config.mjs
[code]
    const withMDX = createMDX({
      extension: /\.(md|mdx)$/,
    })
[/code]

## `mdx-components.tsx` 파일 추가하기[](https://nextjs.org/docs/pages/guides/mdx#add-an-mdx-componentstsx-file)

프로젝트 루트(예: `pages` 또는 `app`과 동일한 수준, 혹은 해당된다면 `src` 내부)에 `mdx-components.tsx`(또는 `.js`) 파일을 생성해 전역 MDX 컴포넌트를 정의하세요.

mdx-components.tsx

JavaScriptTypeScript
[code]
    import type { MDXComponents } from 'mdx/types'

    const components: MDXComponents = {}

    export function useMDXComponents(): MDXComponents {
      return components
    }
[/code]

> **알아두면 좋아요** :
>
>   * App Router에서 `@next/mdx`를 사용하려면 `mdx-components.tsx`가 **필수**이며 없으면 작동하지 않습니다.
>   * [`mdx-components.tsx` 파일 관례](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components)에 대해 자세히 알아보세요.
>   * [사용자 정의 스타일과 컴포넌트](https://nextjs.org/docs/pages/guides/mdx#using-custom-styles-and-components) 적용 방법을 확인하세요.
>

## MDX 렌더링[](https://nextjs.org/docs/pages/guides/mdx#rendering-mdx)

Next.js의 파일 기반 라우팅을 사용하거나 다른 페이지로 MDX 파일을 import하여 MDX를 렌더링할 수 있습니다.

### 파일 기반 라우팅 사용하기[](https://nextjs.org/docs/pages/guides/mdx#using-file-based-routing)

파일 기반 라우팅을 사용할 때는 다른 페이지와 동일하게 MDX 페이지를 사용할 수 있습니다.

`/pages` 디렉터리 안에 새로운 MDX 페이지를 만드세요:
[code]
      my-project
      |── mdx-components.(tsx/js)
      ├── pages
      │   └── mdx-page.(mdx/md)
      └── package.json
[/code]

이 파일들 안에서 MDX를 사용할 수 있으며, React 컴포넌트를 직접 import해 MDX 페이지 안에 넣을 수도 있습니다:
[code]
    import { MyComponent } from 'my-component'

    # Welcome to my MDX page!

    This is some **bold** and _italics_ text.

    This is a list in markdown:

    - One
    - Two
    - Three

    Checkout my React component:

    <MyComponent />
[/code]

`/mdx-page` 라우트로 이동하면 렌더링된 MDX 페이지가 표시되어야 합니다.

### import 사용하기[](https://nextjs.org/docs/pages/guides/mdx#using-imports)

`/pages` 디렉터리 안에 새 페이지를 만들고 원하는 위치에 MDX 파일을 생성하세요:
[code]
      .
      ├── markdown/
      │   └── welcome.(mdx/md)
      ├── pages/
      │   └── mdx-page.(tsx/js)
      ├── mdx-components.(tsx/js)
      └── package.json
[/code]

이 파일들 안에서 MDX를 사용할 수 있으며, React 컴포넌트를 직접 import해 MDX 페이지에 넣을 수도 있습니다.

페이지 안에서 MDX 파일을 import해 콘텐츠를 표시하세요:

pages/mdx-page.tsx

JavaScriptTypeScript
[code]
    import Welcome from '@/markdown/welcome.mdx'

    export default function Page() {
      return <Welcome />
    }
[/code]

`/mdx-page` 라우트로 이동하면 렌더링된 MDX 페이지가 표시되어야 합니다.

## 사용자 정의 스타일과 컴포넌트 사용하기[](https://nextjs.org/docs/pages/guides/mdx#using-custom-styles-and-components)

렌더링된 마크다운은 네이티브 HTML 요소에 매핑됩니다. 예를 들어 아래와 같은 마크다운을 작성하면:
[code]
    ## This is a heading

    This is a list in markdown:

    - One
    - Two
    - Three
[/code]

다음과 같은 HTML이 생성됩니다:
[code]
    <h2>This is a heading</h2>

    <p>This is a list in markdown:</p>

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
    </ul>
[/code]

마크다운에 스타일을 적용하려면 생성된 HTML 요소에 매핑되는 사용자 정의 컴포넌트를 제공하면 됩니다. 스타일과 컴포넌트는 전역, 로컬, 공유 레이아웃 레벨에서 구현할 수 있습니다.

### 전역 스타일과 컴포넌트[](https://nextjs.org/docs/pages/guides/mdx#global-styles-and-components)

`mdx-components.tsx`에 스타일과 컴포넌트를 추가하면 애플리케이션의 _모든_ MDX 파일에 영향을 줍니다.

mdx-components.tsx

JavaScriptTypeScript
[code]
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
[/code]

### 로컬 스타일과 컴포넌트[](https://nextjs.org/docs/pages/guides/mdx#local-styles-and-components)

import한 MDX 컴포넌트에 전달해 특정 페이지에 로컬 스타일과 컴포넌트를 적용할 수 있습니다. 이렇게 전달한 컴포넌트는 [전역 스타일과 컴포넌트](https://nextjs.org/docs/pages/guides/mdx#global-styles-and-components)와 병합되고 이를 덮어씁니다.

pages/mdx-page.tsx

JavaScriptTypeScript
[code]
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
[/code]

### 공유 레이아웃[](https://nextjs.org/docs/pages/guides/mdx#shared-layouts)

MDX 페이지에 공통 레이아웃을 적용하려면 레이아웃 컴포넌트를 만드세요:

components/mdx-layout.tsx

JavaScriptTypeScript
[code]
    export default function MdxLayout({ children }: { children: React.ReactNode }) {
      // Create any shared layout or styles here
      return <div style={{ color: 'blue' }}>{children}</div>
    }
[/code]

그다음, MDX 페이지에 레이아웃 컴포넌트를 import하고 MDX 콘텐츠를 레이아웃으로 감싼 뒤 export하세요:
[code]
    import MdxLayout from '../components/mdx-layout'

    # Welcome to my MDX page!

    export default function MDXPage({ children }) {
      return <MdxLayout>{children}</MdxLayout>

    }
[/code]

### Tailwind Typography 플러그인 사용하기[](https://nextjs.org/docs/pages/guides/mdx#using-tailwind-typography-plugin)

애플리케이션 스타일링에 [Tailwind](https://tailwindcss.com)를 사용한다면 [`@tailwindcss/typography` 플러그인](https://tailwindcss.com/docs/plugins#typography)을 이용해 Tailwind 구성과 스타일을 마크다운 파일에서 재사용할 수 있습니다.

이 플러그인은 `prose` 클래스를 추가하여 마크다운과 같은 소스에서 온 콘텐츠 블록에 타이포그래피 스타일을 적용할 수 있게 합니다.

[Tailwind typography를 설치](https://github.com/tailwindlabs/tailwindcss-typography?tab=readme-ov-file#installation)하고 [공유 레이아웃](https://nextjs.org/docs/pages/guides/mdx#shared-layouts)과 함께 사용해 원하는 `prose` 스타일을 추가하세요.

MDX 페이지에 공통 레이아웃을 적용하려면 레이아웃 컴포넌트를 만드세요:

components/mdx-layout.tsx

JavaScriptTypeScript
[code]
    export default function MdxLayout({ children }: { children: React.ReactNode }) {
      // Create any shared layout or styles here
      return (
        <div className="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
          {children}
        </div>
      )
    }
[/code]

그다음, MDX 페이지에 레이아웃 컴포넌트를 import하고 MDX 콘텐츠를 레이아웃으로 감싼 뒤 export하세요:
[code]
    import MdxLayout from '../components/mdx-layout'

    # Welcome to my MDX page!

    export default function MDXPage({ children }) {
      return <MdxLayout>{children}</MdxLayout>

    }
[/code]

## Frontmatter[](https://nextjs.org/docs/pages/guides/mdx#frontmatter)

Frontmatter는 페이지에 대한 데이터를 저장할 수 있는 YAML 형태의 키/값 쌍입니다. `@next/mdx`는 기본적으로 frontmatter를 지원하지 않지만, 다음과 같이 MDX 콘텐츠에 frontmatter를 추가할 수 있는 다양한 솔루션이 있습니다:

  * [remark-frontmatter](https://github.com/remarkjs/remark-frontmatter)
  * [remark-mdx-frontmatter](https://github.com/remcohaszing/remark-mdx-frontmatter)
  * [gray-matter](https://github.com/jonschlinkert/gray-matter)

`@next/mdx`는 다른 JavaScript 컴포넌트처럼 export를 사용할 수 있도록 **지원**합니다:

이제 MDX 파일 외부에서 메타데이터를 참조할 수 있습니다:

pages/blog.tsx

JavaScriptTypeScript
[code]
    import BlogPost, { metadata } from '@/content/blog-post.mdx'

    export default function Page() {
      console.log('metadata: ', metadata)
      //=> { author: 'John Doe' }
      return <BlogPost />
    }
[/code]

MDX 컬렉션을 반복하면서 데이터를 추출하고 싶을 때 흔히 사용하는 방법입니다. 예를 들어 모든 블로그 게시물로 블로그 인덱스 페이지를 생성하는 경우입니다. 게시물 디렉터리를 읽고 메타데이터를 추출하려면 [Node의 `fs` 모듈](https://nodejs.org/api/fs.html)이나 [globby](https://www.npmjs.com/package/globby) 같은 패키지를 사용할 수 있습니다.

> **알아두면 좋아요** :
>
>   * `fs`, `globby` 등은 서버 측에서만 사용할 수 있습니다.
>   * 전체 동작 예제는 [Portfolio Starter Kit](https://vercel.com/templates/next.js/portfolio-starter-kit) 템플릿을 참고하세요.
>

## remark and rehype Plugins[](https://nextjs.org/docs/pages/guides/mdx#remark-and-rehype-plugins)

선택적으로 remark와 rehype 플러그인을 제공해 MDX 콘텐츠를 변환할 수 있습니다.

예를 들어 [`remark-gfm`](https://github.com/remarkjs/remark-gfm)을 사용하면 GitHub Flavored Markdown을 지원할 수 있습니다.

remark와 rehype 생태계는 ESM 전용이므로 구성 파일로 `next.config.mjs` 또는 `next.config.ts`를 사용해야 합니다.

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

### Using Plugins with Turbopack[](https://nextjs.org/docs/pages/guides/mdx#using-plugins-with-turbopack)

[Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)과 함께 플러그인을 사용하려면 최신 `@next/mdx`로 업그레이드하고 문자열로 플러그인 이름을 지정하세요:

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
> 직렬화 가능한 옵션이 없는 remark 및 rehype 플러그인은 아직 [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)에서 사용할 수 없습니다. JavaScript 함수를 Rust로 전달할 수 없기 때문입니다.

## Deep Dive: How do you transform markdown into HTML?[](https://nextjs.org/docs/pages/guides/mdx#deep-dive-how-do-you-transform-markdown-into-html)

React는 기본적으로 마크다운을 이해하지 못합니다. 마크다운 일반 텍스트를 먼저 HTML로 변환해야 하며, 이는 `remark`와 `rehype`로 수행할 수 있습니다.

`remark`는 마크다운을 둘러싼 도구 생태계이고, `rehype`는 HTML을 위한 동일한 생태계입니다. 예를 들어 다음 코드 스니펫은 마크다운을 HTML로 변환합니다:
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

`remark`와 `rehype` 생태계에는 [syntax highlighting](https://github.com/atomiks/rehype-pretty-code), [linking headings](https://github.com/rehypejs/rehype-autolink-headings), [generating a table of contents](https://github.com/remarkjs/remark-toc) 등 다양한 플러그인이 포함되어 있습니다.

위와 같이 `@next/mdx`를 사용할 때는 `remark`나 `rehype`를 직접 사용할 필요가 없습니다. `@next/mdx` 패키지가 내부에서 처리하기 때문이며, 여기서는 해당 패키지가 내부적으로 무엇을 하는지 더 깊이 이해할 수 있도록 설명하고 있습니다.

## Using the Rust-based MDX compiler (experimental)[](https://nextjs.org/docs/pages/guides/mdx#using-the-rust-based-mdx-compiler-experimental)

Next.js는 Rust로 작성된 새로운 MDX 컴파일러를 지원합니다. 이 컴파일러는 아직 실험 단계이므로 프로덕션 사용은 권장되지 않습니다. 새로운 컴파일러를 사용하려면 `withMDX`에 전달할 때 `next.config.js`를 구성해야 합니다:

next.config.js
```
module.exports = withMDX({
  experimental: {
    mdxRs: true,
  },
})
```

`mdxRs`에는 mdx 파일을 변환하는 방법을 구성할 수 있는 객체도 전달할 수 있습니다.

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

## Helpful Links[](https://nextjs.org/docs/pages/guides/mdx#helpful-links)

  * [MDX](https://mdxjs.com)
  * [`@next/mdx`](https://www.npmjs.com/package/@next/mdx)
  * [remark](https://github.com/remarkjs/remark)
  * [rehype](https://github.com/rehypejs/rehype)
  * [Markdoc](https://markdoc.dev/docs/nextjs)

보내기
