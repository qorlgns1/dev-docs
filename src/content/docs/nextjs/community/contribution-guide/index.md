---
title: '커뮤니티: 기여 가이드'
description: 'Next.js 문서 기여 가이드에 오신 것을 환영합니다! 함께하게 되어 기쁩니다.'
---

# 커뮤니티: 기여 가이드 | Next.js

출처 URL: https://nextjs.org/docs/community/contribution-guide

[Next.js Docs](https://nextjs.org/docs)[Community](https://nextjs.org/docs/community)기여 가이드

# 문서 기여 가이드

마지막 업데이트 2026년 2월 20일

Next.js 문서 기여 가이드에 오신 것을 환영합니다! 함께하게 되어 기쁩니다.

이 페이지는 Next.js 문서를 편집하는 방법을 안내합니다. 모든 커뮤니티 구성원이 문서를 개선하고 성장시킬 수 있도록 힘을 실어 주는 것이 우리의 목표입니다.

## 왜 기여하나요?[](https://nextjs.org/docs/community/contribution-guide#why-contribute)

오픈 소스 작업은 끝이 없고, 문서 작업도 마찬가지입니다. 문서에 기여하면 초보자는 오픈 소스에 참여할 수 있고, 숙련된 개발자는 복잡한 주제를 정리하며 커뮤니티와 지식을 공유할 수 있습니다.

Next.js 문서에 기여하면 모든 개발자를 위한 더 탄탄한 학습 자료를 만드는 데 도움이 됩니다. 오타를 발견했든, 혼란스러운 섹션을 찾았든, 특정 주제가 비어 있음을 깨달았든, 여러분의 기여를 환영하고 감사히 여깁니다.

## 어떻게 기여하나요?[](https://nextjs.org/docs/community/contribution-guide#how-to-contribute)

문서 콘텐츠는 [Next.js repo](https://github.com/vercel/next.js/tree/canary/docs)에서 찾을 수 있습니다. 기여하려면 GitHub에서 직접 파일을 편집하거나 저장소를 클론해 로컬에서 편집하면 됩니다.

### GitHub 워크플로우[](https://nextjs.org/docs/community/contribution-guide#github-workflow)

GitHub가 처음이라면 저장소를 포크하고 브랜치를 만든 뒤 풀 리퀘스트를 제출하는 방법을 배우기 위해 [GitHub Open Source Guide](https://opensource.guide/how-to-contribute/#opening-a-pull-request)를 읽어 보세요.

> **알아두면 좋아요** : 기본 문서 코드는 Next.js 공개 저장소와 동기화되는 비공개 코드베이스에 있습니다. 따라서 로컬에서 문서를 미리 볼 수 없습니다. 하지만 풀 리퀘스트가 머지되면 [nextjs.org](https://nextjs.org/docs)에서 변경 사항을 볼 수 있습니다.

### MDX 작성[](https://nextjs.org/docs/community/contribution-guide#writing-mdx)

문서는 JSX 구문을 지원하는 마크다운 형식인 [MDX](https://mdxjs.com/)로 작성됩니다. 덕분에 문서 안에 React 컴포넌트를 삽입할 수 있습니다. 마크다운 구문을 빠르게 훑어보려면 [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)를 참고하세요.

### VSCode[](https://nextjs.org/docs/community/contribution-guide#vscode)

#### 로컬에서 변경 사항 미리 보기[](https://nextjs.org/docs/community/contribution-guide#previewing-changes-locally)

VSCode에는 편집 내용을 로컬에서 확인할 수 있는 기본 마크다운 미리 보기 기능이 있습니다. MDX 파일에서 미리 보기를 사용하려면 사용자 설정에 구성 옵션을 추가해야 합니다.

명령 팔레트(`⌘ + ⇧ + P` on Mac or `Ctrl + Shift + P` on Windows)를 열고 `Preferences: Open User Settings (JSON)`을 검색하세요.

그런 다음 `settings.json` 파일에 다음 줄을 추가합니다.

settings.json
[code]
    {
      "files.associations": {
        "*.mdx": "markdown"
      }
    }
[/code]

이후 명령 팔레트를 다시 열고 `Markdown: Preview File` 또는 `Markdown: Open Preview to the Side`를 검색합니다. 그러면 서식이 적용된 변경 사항을 볼 수 있는 미리 보기 창이 열립니다.

#### 확장 프로그램[](https://nextjs.org/docs/community/contribution-guide#extensions)

VSCode 사용자에게 다음 확장을 권장합니다.

  * [MDX](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx): MDX에 대한 IntelliSense와 구문 하이라이트.
  * [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): 저장 시 MDX 파일을 포맷합니다.

### 검토 프로세스[](https://nextjs.org/docs/community/contribution-guide#review-process)

기여를 제출하면 Next.js 팀 또는 Developer Experience 팀이 변경 사항을 검토하고 피드백을 제공한 뒤 준비가 되면 풀 리퀘스트를 머지합니다.

풀 리퀘스트 댓글에서 질문이나 추가 지원이 필요하면 알려 주세요. Next.js 문서에 기여해 주시고 커뮤니티의 일원이 되어 주셔서 감사합니다!

> **팁:** PR을 제출하기 전에 `pnpm prettier-fix`를 실행해 Prettier를 돌리세요.

## 파일 구조[](https://nextjs.org/docs/community/contribution-guide#file-structure)

문서는 **파일 시스템 라우팅**을 사용합니다. [`/docs`](https://github.com/vercel/next.js/tree/canary/docs)의 각 폴더와 파일은 라우트 세그먼트를 나타내며, 이 세그먼트로 URL 경로, 내비게이션, 브레드크럼을 생성합니다.

파일 구조는 사이트에서 볼 수 있는 내비게이션을 반영하며, 기본적으로 내비게이션 항목은 알파벳 순으로 정렬됩니다. 다만 폴더나 파일 이름 앞에 두 자리 숫자(`00-`)를 붙이면 정렬 순서를 바꿀 수 있습니다.

예를 들어 [functions API Reference](https://nextjs.org/docs/app/api-reference/functions)에서는 개발자가 특정 함수를 찾기 쉽도록 페이지가 알파벳 순으로 정렬됩니다:
[code]
    04-functions
    ├── after.mdx
    ├── cacheLife.mdx
    ├── cacheTag.mdx
    └── ...
[/code]

하지만 [app router 섹션](https://nextjs.org/docs/app)에서는 파일 이름에 두 자리 숫자를 붙여 개발자가 학습해야 하는 순서대로 정렬합니다:
[code]
    01-getting-started
    ├── 01-installation.mdx
    ├── 02-project-structure.mdx
    ├── 03-layouts-and-pages.mdx
    └── ...
[/code]

VSCode에서 `⌘ + P`(Mac) 또는 `Ctrl + P`(Windows)를 눌러 검색 창을 연 뒤 찾고 싶은 페이지의 슬러그를 입력하면 원하는 페이지를 빠르게 찾을 수 있습니다. 예: `installation`

> **왜 매니페스트를 사용하지 않나요?**
>
> 내비게이션을 생성하는 또 다른 일반적인 방법인 매니페스트 파일 사용을 검토했지만, 파일과 쉽게 동기화가 어긋난다는 점을 발견했습니다. 파일 시스템 라우팅을 사용하면 문서 구조를 지속적으로 고민하게 되고 Next.js 방식과도 더 자연스럽게 맞습니다.

## 메타데이터[](https://nextjs.org/docs/community/contribution-guide#metadata)

각 페이지는 파일 상단에 세 개의 대시로 구분된 메타데이터 블록을 가집니다.

### 필수 필드[](https://nextjs.org/docs/community/contribution-guide#required-fields)

다음 필드는 **필수**입니다:

필드|설명
---|---
`title`| 페이지의 `<h1>` 제목으로, SEO와 OG 이미지에 사용됩니다.
`description`| 페이지 설명으로, SEO를 위한 `<meta name="description">` 태그에 사용됩니다.

required-fields.mdx
[code]
    ---
    title: Page Title
    description: Page Description
    ---
[/code]

페이지 제목은 2~3단어(예: Optimizing Images), 설명은 1~2문장(예: Learn how to optimize images in Next.js)으로 제한하는 것이 좋습니다.

### 선택 필드[](https://nextjs.org/docs/community/contribution-guide#optional-fields)

다음 필드는 **선택 사항**입니다:

필드|설명
---|---
`nav_title`| 내비게이션에서 페이지 제목을 덮어씁니다. 제목이 길어 들어가지 않을 때 유용합니다. 지정하지 않으면 `title` 필드가 사용됩니다.
`source`| 콘텐츠를 공유 페이지로 끌어옵니다. [Shared Pages](https://nextjs.org/docs/community/contribution-guide#shared-pages)를 참조하세요.
`related`| 문서 하단에 표시되는 관련 페이지 목록입니다. 자동으로 카드로 변환됩니다. [Related Links](https://nextjs.org/docs/community/contribution-guide#related-links)를 참조하세요.
`version`| 개발 단계입니다. 예: `experimental`,`legacy`,`unstable`,`RC`

optional-fields.mdx
[code]
    ---
    nav_title: Nav Item Title
    source: app/building-your-application/optimizing/images
    related:
      description: See the image component API reference.
      links:
        - app/api-reference/components/image
    version: experimental
    ---
[/code]

## `App` 및 `Pages` 문서[](https://nextjs.org/docs/community/contribution-guide#app-and-pages-docs)

**App Router**와 **Pages Router**의 기능 대부분은 완전히 다르기 때문에 각 문서는 별도 섹션(`02-app`과 `03-pages`)으로 나누어 관리합니다. 다만 일부 기능은 두 라우터가 공유합니다.

### 공유 페이지[](https://nextjs.org/docs/community/contribution-guide#shared-pages)

콘텐츠를 중복 작성하다 보면 동기화가 어긋날 위험이 있으므로 `source` 필드를 사용해 한 페이지의 콘텐츠를 다른 페이지로 끌어옵니다. 예를 들어 `<Link>` 컴포넌트는 **App**과 **Pages**에서 _대부분_ 동일하게 동작합니다. 콘텐츠를 복제하는 대신 `app/.../link.mdx`의 내용을 `pages/.../link.mdx`로 가져올 수 있습니다:

app/.../link.mdx
[code]
    ---
    title: <Link>
    description: API reference for the <Link> component.
    ---

    This API reference will help you understand how to use the props
    and configuration options available for the Link Component.
[/code]

pages/.../link.mdx
[code]
    ---
    title: <Link>
    description: API reference for the <Link> component.
    source: app/api-reference/components/link
    ---

    {/* DO NOT EDIT THIS PAGE. */}
    {/* The content of this page is pulled from the source above. */}
[/code]

이렇게 하면 한 곳에서 콘텐츠를 수정해도 두 섹션에 모두 반영됩니다.

### 공유 콘텐츠[](https://nextjs.org/docs/community/contribution-guide#shared-content)

공유 페이지에는 **App Router** 또는 **Pages Router**에만 해당하는 콘텐츠가 있을 수 있습니다. 예를 들어 `<Link>` 컴포넌트의 `shallow` prop은 **Pages**에서만 제공되고 **App**에는 없습니다.

콘텐츠가 올바른 라우터에만 표시되도록 `<AppOnly>` 또는 `<PagesOnly>` 컴포넌트로 블록을 감쌀 수 있습니다:

app/.../link.mdx
[code]
    This content is shared between App and Pages.

    <PagesOnly>

    This content will only be shown on the Pages docs.

    </PagesOnly>

    This content is shared between App and Pages.
[/code]

이 컴포넌트는 예시나 코드 블록에 자주 사용하게 될 것입니다.

## 코드 블록[](https://nextjs.org/docs/community/contribution-guide#code-blocks)

코드 블록에는 복사해 붙여넣을 수 있는 최소 실행 예제가 있어야 합니다. 즉, 추가 설정 없이도 실행 가능한 코드여야 합니다.

예를 들어 `<Link>` 컴포넌트 사용법을 보여줄 때는 `import` 문과 `<Link>` 컴포넌트를 함께 포함해야 합니다.

app/page.tsx
[code]
    import Link from 'next/link'

    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

커밋하기 전에 항상 예제를 로컬에서 실행해 최신 상태이며 동작하는지 확인하세요.

### 언어와 파일 이름[](https://nextjs.org/docs/community/contribution-guide#language-and-filename)

코드 블록 헤더에는 언어와 `filename`이 포함되어야 합니다. 예:

code-example.mdx
[code]
    ```tsx filename="app/page.tsx"
    export default function Page() {
      return <h1>Hello, Next.js!</h1>
    }
    ```
[/code]

CLI 명령어의 경우 `package` prop을 사용해 각 패키지 관리자의 명령을 보여 주세요:

code-example.mdx
[code]
    ```bash package="pnpm"
    pnpm create next-app
    ```

    ```bash package="npm"
    npx create-next-app@latest
    ```

    ```bash package="yarn"
    yarn create next-app
    ```

    ```bash package="bun"
    bun create next-app
    ```
[/code]

문서의 대부분 예시는 `tsx`와 `jsx`, 일부는 `bash`로 작성됩니다. 하지만 지원되는 언어라면 무엇이든 사용할 수 있습니다. 전체 목록은 [여기](https://github.com/shikijs/shiki/blob/main/docs/languages.md#all-languages)에서 확인하세요.

JavaScript 코드 블록을 작성할 때는 다음 언어와 확장자 조합을 사용합니다.

유형| 언어| 확장자
---|---|---
JSX 코드를 포함한 JavaScript 파일| ```jsx| .js
JSX가 없는 JavaScript 파일| ```js| .js
JSX를 포함한 TypeScript 파일| ```tsx| .tsx
JSX가 없는 TypeScript 파일| ```ts| .ts

> **알아두면 좋아요** :
>

>   * **JSX** 코드가 포함된 JavaScript 파일에는 반드시 **`.js`** 확장자를 사용하세요.
>   * 예를 들어, ```jsx filename="app/layout.js"
>

### TS and JS Switcher[](https://nextjs.org/docs/community/contribution-guide#ts-and-js-switcher)

TypeScript와 JavaScript 간 토글이 가능한 언어 전환 스위처를 추가하세요. 코드 블록은 TypeScript 버전을 먼저 보여 주고, 이어서 JavaScript 버전을 제공해 사용자를 배려합니다.

현재는 TS 예제와 JS 예제를 순차적으로 작성하고 `switcher` 프롭으로 연결합니다:

code-example.mdx
[code]
    ```tsx filename="app/page.tsx" switcher

    ```

    ```jsx filename="app/page.js" switcher

    ```
[/code]

> **참고**: 향후 TypeScript 스니펫을 자동으로 JavaScript로 컴파일할 예정입니다. 그때까지는 [transform.tools](https://transform.tools/typescript-to-javascript)를 사용할 수 있습니다.

### Line Highlighting[](https://nextjs.org/docs/community/contribution-guide#line-highlighting)

코드 줄을 하이라이트할 수 있습니다. 특정 코드 부분을 강조하고 싶을 때 유용합니다. `highlight` 프롭에 숫자를 전달해 줄을 지정하세요.

**단일 줄:** `highlight={1}`

app/page.tsx
[code]
    import Link from 'next/link'

    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

**여러 줄:** `highlight={1,3}`

app/page.tsx
[code]
    import Link from 'next/link'

    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

**구간:** `highlight={1-5}`

app/page.tsx
[code]
    import Link from 'next/link'

    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

## Icons[](https://nextjs.org/docs/community/contribution-guide#icons)

문서에서 사용할 수 있는 아이콘은 다음과 같습니다:

mdx-icon.mdx
[code]
    <Check size={18} />
    <Cross size={18} />
[/code]

**출력:**

문서에서는 이모지를 사용하지 않습니다.

## Notes[](https://nextjs.org/docs/community/contribution-guide#notes)

중요하지만 치명적이지 않은 정보를 전달할 때 노트를 사용하세요. 노트는 본문을 방해하지 않고 정보를 추가하기 좋은 방법입니다.

notes.mdx
[code]
    > **Good to know**: This is a single line note.

    > **Good to know**:
    >
    > - We also use this format for multi-line notes.
    > - There are sometimes multiple items worth knowing or keeping in mind.
[/code]

**출력:**

> **Good to know** : This is a single line note.

> **Good to know** :
>
>   * We also use this format for multi-line notes.
>   * There are sometimes multiple items worth knowing or keeping in mind.
>

## Related Links[](https://nextjs.org/docs/community/contribution-guide#related-links)

Related Links는 사용자에게 논리적인 다음 단계를 안내하는 링크를 추가해 학습 여정을 이끕니다.

  * 링크는 페이지 본문 아래의 카드에 표시됩니다.
  * 자식 페이지가 있는 경우 자동으로 링크가 생성됩니다.

페이지 메타데이터의 `related` 필드를 사용해 관련 링크를 생성하세요.

example.mdx
[code]
    ---
    related:
      description: Learn how to quickly get started with your first application.
      links:
        - app/building-your-application/routing/defining-routes
        - app/building-your-application/data-fetching
        - app/api-reference/file-conventions/page
    ---
[/code]

### Nested Fields[](https://nextjs.org/docs/community/contribution-guide#nested-fields)

Field| Required?| Description
---|---|---
`title`| Optional| 카드 목록의 제목입니다. 기본값은 **Next Steps**입니다.
`description`| Optional| 카드 목록에 대한 설명입니다.
`links`| Required| 다른 문서 페이지로 연결되는 링크 목록입니다. 각 목록 항목은 상대 URL 경로(선행 슬래시 없이)여야 합니다. 예: `app/api-reference/file-conventions/page`

## Diagrams[](https://nextjs.org/docs/community/contribution-guide#diagrams)

도표는 복잡한 개념을 설명하기에 훌륭한 수단입니다. 우리는 Vercel 디자인 가이드를 따라 [Figma](https://www.figma.com/)에서 도표를 만듭니다.

도표는 현재 비공개 Next.js 사이트의 `/public` 폴더에 있습니다. 도표를 업데이트하거나 추가하고 싶다면 아이디어와 함께 [GitHub 이슈](https://github.com/vercel/next.js/issues/new?assignees=&labels=template%3A+documentation&projects=&template=4.docs_request.yml&title=Docs%3A+)를 열어 주세요.

## Custom Components and HTML[](https://nextjs.org/docs/community/contribution-guide#custom-components-and-html)

문서에서 사용할 수 있는 React 컴포넌트는 `<Image />`(next/image), `<PagesOnly />`, `<AppOnly />`, `<Cross />`, `<Check />`입니다. `<details>` 태그를 제외한 순수 HTML은 허용되지 않습니다.

새로운 컴포넌트 아이디어가 있다면 [GitHub 이슈](https://github.com/vercel/next.js/issues/new/choose)를 열어 주세요.

## Style Guide[](https://nextjs.org/docs/community/contribution-guide#style-guide)

이 섹션은 기술 문서 작성에 익숙하지 않은 분들을 위한 가이드라인입니다.

### Page Templates[](https://nextjs.org/docs/community/contribution-guide#page-templates)

엄격한 페이지 템플릿은 없지만, 문서 전반에서 반복되는 섹션이 있습니다:

  * **Overview:** 페이지의 첫 문단은 기능이 무엇이며 어떤 용도로 쓰이는지 알려야 합니다. 이어서 최소 실행 예제나 API 레퍼런스를 제공합니다.
  * **Convention:** 기능이 따르는 규약이 있다면 여기에서 설명하세요.
  * **Examples** : 기능을 여러 사용 사례와 함께 보여 주세요.
  * **API Tables** : API 페이지는 가능하다면 페이지 상단에 섹션 이동 링크가 포함된 개요 표가 있어야 합니다.
  * **Next Steps (Related Links)** : 사용자의 학습 여정을 안내하기 위해 관련 페이지 링크를 추가하세요.

필요에 따라 이러한 섹션을 자유롭게 추가하세요.

### Page Types[](https://nextjs.org/docs/community/contribution-guide#page-types)

문서 페이지는 개념형과 레퍼런스형 두 가지 범주로 나뉩니다.

  * **Conceptual** 페이지는 개념이나 기능을 설명합니다. 일반적으로 더 길고 정보량이 많습니다. Next.js 문서에서는 **Building Your Application** 섹션에서 찾을 수 있습니다.
  * **Reference** 페이지는 특정 API를 설명합니다. 보통 더 짧고 집중적입니다. Next.js 문서에서는 **API Reference** 섹션에 있습니다.

> **참고** : 기여하려는 페이지에 따라 다른 음성과 스타일을 따라야 할 수 있습니다. 예를 들어, 개념형 페이지는 더 설명적이며 사용자에게 _you_를 사용합니다. 레퍼런스 페이지는 더 기술적이며 "create, update, accept"처럼 명령형 단어를 사용하고 _you_를 생략하는 경향이 있습니다.

### Voice[](https://nextjs.org/docs/community/contribution-guide#voice)

문서 전반에 일관된 스타일과 음성을 유지하기 위한 가이드라인입니다:

  * 명확하고 간결한 문장을 작성하세요. 곁가지를 피하세요.
    * 쉼표가 많다고 느껴지면 문장을 나누거나 목록을 사용하세요.
    * 복잡한 단어를 더 단순한 단어로 바꾸세요. 예: _utilize_ 대신 _use_.
  * _this_라는 단어 사용에 주의하세요. 모호할 수 있으므로 불명확하면 주어를 반복해도 좋습니다.
    * 예: _Next.js uses React_ (O), _Next.js uses this_ (X).
  * 수동태 대신 능동태를 사용하세요. 능동태가 읽기 쉽습니다.
    * 예: _Next.js uses React_ (O), _React is used by Next.js_ (X). _was_, _by_ 같은 단어를 사용한다면 수동태일 수 있습니다.
  * _easy_, _quick_, _simple_, _just_ 등 주관적 표현을 피하세요. 사용자를 좌절하게 할 수 있습니다.
  * _don't_, _can't_, _won't_ 같은 부정 표현을 피하세요. 독자에게 부정적으로 들릴 수 있습니다.
    * 예: _"You can use the`Link` component to create links between pages"_처럼 긍정적으로 표현하세요.
  * 2인칭(you/your)으로 작성하세요. 더 개인적이고 참여감을 줍니다.
  * 성 중립적 언어를 사용하세요. 독자를 지칭할 때 _developers_, _users_, _readers_ 등을 사용하세요.
  * 코드 예제를 추가할 경우 올바른 포맷과 작동 여부를 확인하세요.

이 가이드라인이 전부는 아니지만 시작하는 데 도움이 될 것입니다. 기술 문서 작성에 대해 더 깊이 배우고 싶다면 [Google Technical Writing Course](https://developers.google.com/tech-writing/overview)를 참고하세요.

* * *

Next.js 커뮤니티의 일원이 되어 문서에 기여해 주셔서 감사합니다!

supported.

Send
