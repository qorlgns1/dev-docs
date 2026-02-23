---
title: 'Community: Contribution Guide'
description: "Welcome to the Next.js Docs Contribution Guide! We're excited to have you here."
---

# Community: Contribution Guide | Next.js

Source URL: https://nextjs.org/docs/community/contribution-guide

[Next.js Docs](https://nextjs.org/docs)[Community](https://nextjs.org/docs/community)Contribution Guide

Copy page

# Docs Contribution Guide

Last updated February 20, 2026

Welcome to the Next.js Docs Contribution Guide! We're excited to have you here.

This page provides instructions on how to edit the Next.js documentation. Our goal is to ensure that everyone in the community feels empowered to contribute and improve our docs.

## Why Contribute?[](https://nextjs.org/docs/community/contribution-guide#why-contribute)

Open-source work is never done, and neither is documentation. Contributing to docs is a good way for beginners to get involved in open-source and for experienced developers to clarify more complex topics while sharing their knowledge with the community.

By contributing to the Next.js docs, you're helping us build a more robust learning resource for all developers. Whether you've found a typo, a confusing section, or you've realized that a particular topic is missing, your contributions are welcomed and appreciated.

## How to Contribute[](https://nextjs.org/docs/community/contribution-guide#how-to-contribute)

The docs content can be found on the [Next.js repo](https://github.com/vercel/next.js/tree/canary/docs). To contribute, you can edit the files directly on GitHub or clone the repo and edit the files locally.

### GitHub Workflow[](https://nextjs.org/docs/community/contribution-guide#github-workflow)

If you're new to GitHub, we recommend reading the [GitHub Open Source Guide](https://opensource.guide/how-to-contribute/#opening-a-pull-request) to learn how to fork a repository, create a branch, and submit a pull request.

> **Good to know** : The underlying docs code lives in a private codebase that is synced to the Next.js public repo. This means that you can't preview the docs locally. However, you'll see your changes on [nextjs.org](https://nextjs.org/docs) after merging a pull request.

### Writing MDX[](https://nextjs.org/docs/community/contribution-guide#writing-mdx)

The docs are written in [MDX](https://mdxjs.com/), a markdown format that supports JSX syntax. This allows us to embed React components in the docs. See the [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) for a quick overview of markdown syntax.

### VSCode[](https://nextjs.org/docs/community/contribution-guide#vscode)

#### Previewing Changes Locally[](https://nextjs.org/docs/community/contribution-guide#previewing-changes-locally)

VSCode has a built-in markdown previewer that you can use to see your edits locally. To enable the previewer for MDX files, you'll need to add a configuration option to your user settings.

Open the command palette (`⌘ + ⇧ + P` on Mac or `Ctrl + Shift + P` on Windows) and search from `Preferences: Open User Settings (JSON)`.

Then, add the following line to your `settings.json` file:

settings.json
[code]
    {
      "files.associations": {
        "*.mdx": "markdown"
      }
    }
[/code]

Next, open the command palette again, and search for `Markdown: Preview File` or `Markdown: Open Preview to the Side`. This will open a preview window where you can see your formatted changes.

#### Extensions[](https://nextjs.org/docs/community/contribution-guide#extensions)

We also recommend the following extensions for VSCode users:

  * [MDX](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx): Intellisense and syntax highlighting for MDX.
  * [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Format MDX files on save.



### Review Process[](https://nextjs.org/docs/community/contribution-guide#review-process)

Once you've submitted your contribution, the Next.js or Developer Experience teams will review your changes, provide feedback, and merge the pull request when it's ready.

Please let us know if you have any questions or need further assistance in your PR's comments. Thank you for contributing to the Next.js docs and being a part of our community!

> **Tip:** Run `pnpm prettier-fix` to run Prettier before submitting your PR.

## File Structure[](https://nextjs.org/docs/community/contribution-guide#file-structure)

The docs use **file-system routing**. Each folder and files inside [`/docs`](https://github.com/vercel/next.js/tree/canary/docs) represent a route segment. These segments are used to generate the URL paths, navigation, and breadcrumbs.

The file structure reflects the navigation that you see on the site, and by default, navigation items are sorted alphabetically. However, we can change the order of the items by prepending a two-digit number (`00-`) to the folder or file name.

For example, in the [functions API Reference](https://nextjs.org/docs/app/api-reference/functions), the pages are sorted alphabetically because it makes it easier for developers to find a specific function:
[code] 
    04-functions
    ├── after.mdx
    ├── cacheLife.mdx
    ├── cacheTag.mdx
    └── ...
[/code]

But, in the [app router section](https://nextjs.org/docs/app), the files are prefixed with a two-digit number, sorted in the order developers should learn these concepts:
[code] 
    01-getting-started
    ├── 01-installation.mdx
    ├── 02-project-structure.mdx
    ├── 03-layouts-and-pages.mdx
    └── ...
[/code]

To quickly find a page, you can use `⌘ + P` (Mac) or `Ctrl + P` (Windows) to open the search bar on VSCode. Then, type the slug of the page you're looking for. E.g. `installation`

> **Why not use a manifest?**
> 
> We considered using a manifest file (another popular way to generate the docs navigation), but we found that a manifest would quickly get out of sync with the files. File-system routing forces us to think about the structure of the docs and feels more native to Next.js.

## Metadata[](https://nextjs.org/docs/community/contribution-guide#metadata)

Each page has a metadata block at the top of the file separated by three dashes.

### Required Fields[](https://nextjs.org/docs/community/contribution-guide#required-fields)

The following fields are **required** :

Field| Description  
---|---  
`title`| The page's `<h1>` title, used for SEO and OG Images.  
`description`| The page's description, used in the `<meta name="description">` tag for SEO.  
  
required-fields.mdx
[code]
    ---
    title: Page Title
    description: Page Description
    ---
[/code]

It's good practice to limit the page title to 2-3 words (e.g. Optimizing Images) and the description to 1-2 sentences (e.g. Learn how to optimize images in Next.js).

### Optional Fields[](https://nextjs.org/docs/community/contribution-guide#optional-fields)

The following fields are **optional** :

Field| Description  
---|---  
`nav_title`| Overrides the page's title in the navigation. This is useful when the page's title is too long to fit. If not provided, the `title` field is used.  
`source`| Pulls content into a shared page. See [Shared Pages](https://nextjs.org/docs/community/contribution-guide#shared-pages).  
`related`| A list of related pages at the bottom of the document. These will automatically be turned into cards. See [Related Links](https://nextjs.org/docs/community/contribution-guide#related-links).  
`version`| A stage of development. e.g. `experimental`,`legacy`,`unstable`,`RC`  
  
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

## `App` and `Pages` Docs[](https://nextjs.org/docs/community/contribution-guide#app-and-pages-docs)

Since most of the features in the **App Router** and **Pages Router** are completely different, their docs for each are kept in separate sections (`02-app` and `03-pages`). However, there are a few features that are shared between them.

### Shared Pages[](https://nextjs.org/docs/community/contribution-guide#shared-pages)

To avoid content duplication and risk the content becoming out of sync, we use the `source` field to pull content from one page into another. For example, the `<Link>` component behaves _mostly_ the same in **App** and **Pages**. Instead of duplicating the content, we can pull the content from `app/.../link.mdx` into `pages/.../link.mdx`:

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

We can therefore edit the content in one place and have it reflected in both sections.

### Shared Content[](https://nextjs.org/docs/community/contribution-guide#shared-content)

In shared pages, sometimes there might be content that is **App Router** or **Pages Router** specific. For example, the `<Link>` component has a `shallow` prop that is only available in **Pages** but not in **App**.

To make sure the content only shows in the correct router, we can wrap content blocks in an `<AppOnly>` or `<PagesOnly>` components:

app/.../link.mdx
[code]
    This content is shared between App and Pages.
     
    <PagesOnly>
     
    This content will only be shown on the Pages docs.
     
    </PagesOnly>
     
    This content is shared between App and Pages.
[/code]

You'll likely use these components for examples and code blocks.

## Code Blocks[](https://nextjs.org/docs/community/contribution-guide#code-blocks)

Code blocks should contain a minimum working example that can be copied and pasted. This means that the code should be able to run without any additional configuration.

For example, if you're showing how to use the `<Link>` component, you should include the `import` statement and the `<Link>` component itself.

app/page.tsx
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

Always run examples locally before committing them. This will ensure that the code is up-to-date and working.

### Language and Filename[](https://nextjs.org/docs/community/contribution-guide#language-and-filename)

Code blocks should have a header that includes the language and the `filename`. For example:

code-example.mdx
[code]
    ```tsx filename="app/page.tsx"
    export default function Page() {
      return <h1>Hello, Next.js!</h1>
    }
    ```
[/code]

For CLI commands, use the `package` prop to show the command for each package manager:

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

Most examples in the docs are written in `tsx` and `jsx`, and a few in `bash`. However, you can use any supported language, here's the [full list](https://github.com/shikijs/shiki/blob/main/docs/languages.md#all-languages).

When writing JavaScript code blocks, we use the following language and extension combinations.

| Language| Extension  
---|---|---  
JavaScript files with JSX code| ```jsx| .js  
JavaScript files without JSX| ```js| .js  
TypeScript files with JSX| ```tsx| .tsx  
TypeScript files without JSX| ```ts| .ts  
  
> **Good to know** :
> 
>   * Make sure to use **`.js`** extension for JavaScript files with **JSX** code.
>   * For example, ```jsx filename="app/layout.js"
> 


### TS and JS Switcher[](https://nextjs.org/docs/community/contribution-guide#ts-and-js-switcher)

Add a language switcher to toggle between TypeScript and JavaScript. Code blocks should be TypeScript first with a JavaScript version to accommodate users.

Currently, we write TS and JS examples one after the other, and link them with `switcher` prop:

code-example.mdx
[code]
    ```tsx filename="app/page.tsx" switcher
     
    ```
     
    ```jsx filename="app/page.js" switcher
     
    ```
[/code]

> **Good to know** : We plan to automatically compile TypeScript snippets to JavaScript in the future. In the meantime, you can use [transform.tools](https://transform.tools/typescript-to-javascript).

### Line Highlighting[](https://nextjs.org/docs/community/contribution-guide#line-highlighting)

Code lines can be highlighted. This is useful when you want to draw attention to a specific part of the code. You can highlight lines by passing a number to the `highlight` prop.

**Single Line:** `highlight={1}`

app/page.tsx
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

**Multiple Lines:** `highlight={1,3}`

app/page.tsx
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

**Range of Lines:** `highlight={1-5}`

app/page.tsx
[code]
    import Link from 'next/link'
     
    export default function Page() {
      return <Link href="/about">About</Link>
    }
[/code]

## Icons[](https://nextjs.org/docs/community/contribution-guide#icons)

The following icons are available for use in the docs:

mdx-icon.mdx
[code]
    <Check size={18} />
    <Cross size={18} />
[/code]

**Output:**

We do not use emojis in the docs.

## Notes[](https://nextjs.org/docs/community/contribution-guide#notes)

For information that is important but not critical, use notes. Notes are a good way to add information without distracting the user from the main content.

notes.mdx
[code]
    > **Good to know**: This is a single line note.
     
    > **Good to know**:
    >
    > - We also use this format for multi-line notes.
    > - There are sometimes multiple items worth knowing or keeping in mind.
[/code]

**Output:**

> **Good to know** : This is a single line note.

> **Good to know** :
> 
>   * We also use this format for multi-line notes.
>   * There are sometimes multiple items worth knowing or keeping in mind.
> 


## Related Links[](https://nextjs.org/docs/community/contribution-guide#related-links)

Related Links guide the user's learning journey by adding links to logical next steps.

  * Links will be displayed in cards under the main content of the page.
  * Links will be automatically generated for pages that have child pages.



Create related links using the `related` field in the page's metadata.

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
`title`| Optional| The title of the card list. Defaults to **Next Steps**.  
`description`| Optional| The description of the card list.  
`links`| Required| A list of links to other doc pages. Each list item should be a relative URL path (without a leading slash) e.g. `app/api-reference/file-conventions/page`  
  
## Diagrams[](https://nextjs.org/docs/community/contribution-guide#diagrams)

Diagrams are a great way to explain complex concepts. We use [Figma](https://www.figma.com/) to create diagrams, following Vercel's design guide.

The diagrams currently live in the `/public` folder in our private Next.js site. If you'd like to update or add a diagram, please open a [GitHub issue](https://github.com/vercel/next.js/issues/new?assignees=&labels=template%3A+documentation&projects=&template=4.docs_request.yml&title=Docs%3A+) with your ideas.

## Custom Components and HTML[](https://nextjs.org/docs/community/contribution-guide#custom-components-and-html)

These are the React Components available for the docs: `<Image />` (next/image), `<PagesOnly />`, `<AppOnly />`, `<Cross />`, and `<Check />`. We do not allow raw HTML in the docs besides the `<details>` tag.

If you have ideas for new components, please open a [GitHub issue](https://github.com/vercel/next.js/issues/new/choose).

## Style Guide[](https://nextjs.org/docs/community/contribution-guide#style-guide)

This section contains guidelines for writing docs for those who are new to technical writing.

### Page Templates[](https://nextjs.org/docs/community/contribution-guide#page-templates)

While we don't have a strict template for pages, there are page sections you'll see repeated across the docs:

  * **Overview:** The first paragraph of a page should tell the user what the feature is and what it's used for. Followed by a minimum working example or its API reference.
  * **Convention:** If the feature has a convention, it should be explained here.
  * **Examples** : Show how the feature can be used with different use cases.
  * **API Tables** : API Pages should have an overview table at the of the page with jump-to-section links (when possible).
  * **Next Steps (Related Links)** : Add links to related pages to guide the user's learning journey.



Feel free to add these sections as needed.

### Page Types[](https://nextjs.org/docs/community/contribution-guide#page-types)

Docs pages are also split into two categories: Conceptual and Reference.

  * **Conceptual** pages are used to explain a concept or feature. They are usually longer and contain more information than reference pages. In the Next.js docs, conceptual pages are found in the **Building Your Application** section.
  * **Reference** pages are used to explain a specific API. They are usually shorter and more focused. In the Next.js docs, reference pages are found in the **API Reference** section.



> **Good to know** : Depending on the page you're contributing to, you may need to follow a different voice and style. For example, conceptual pages are more instructional and use the word _you_ to address the user. Reference pages are more technical, they use more imperative words like "create, update, accept" and tend to omit the word _you_.

### Voice[](https://nextjs.org/docs/community/contribution-guide#voice)

Here are some guidelines to maintain a consistent style and voice across the docs:

  * Write clear, concise sentences. Avoid tangents.
    * If you find yourself using a lot of commas, consider breaking the sentence into multiple sentences or use a list.
    * Swap out complex words for simpler ones. For example, _use_ instead of _utilize_.
  * Be mindful with the word _this_. It can be ambiguous and confusing, don't be afraid to repeat the subject of the sentence if unclear.
    * For example, _Next.js uses React_ instead of _Next.js uses this_.
  * Use an active voice instead of passive. An active sentence is easier to read.
    * For example, _Next.js uses React_ instead of _React is used by Next.js_. If you find yourself using words like _was_ and _by_ you may be using a passive voice.
  * Avoid using words like _easy_ , _quick_ , _simple_ , _just_ , etc. This is subjective and can be discouraging to users.
  * Avoid negative words like _don't_ , _can't_ , _won't_ , etc. This can be discouraging to readers.
    * For example, _"You can use the`Link` component to create links between pages"_ instead of _"Don't use the`<a>` tag to create links between pages"_.
  * Write in second person (you/your). This is more personal and engaging.
  * Use gender-neutral language. Use _developers_ , _users_ , or _readers_ , when referring to the audience.
  * If adding code examples, ensure they are properly formatted and working.



While these guidelines are not exhaustive, they should help you get started. If you'd like to dive deeper into technical writing, check out the [Google Technical Writing Course](https://developers.google.com/tech-writing/overview).

* * *

Thank you for contributing to the docs and being part of the Next.js community!

Was this helpful?

supported.

Send
