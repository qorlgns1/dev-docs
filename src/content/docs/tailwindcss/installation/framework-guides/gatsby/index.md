---
title: "Gatsby와 함께 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 프로젝트가 없다면 먼저 새 Gatsby 프로젝트를 만드세요. 가장 일반적인 방법은 Gatsby CLI를 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/gatsby

# Gatsby와 함께 Tailwind CSS 설치 - Tailwind CSS

01

#### 프로젝트 만들기

아직 프로젝트가 없다면 먼저 새 Gatsby 프로젝트를 만드세요. 가장 일반적인 방법은 [Gatsby CLI](https://www.gatsbyjs.com/docs/reference/gatsby-cli/#how-to-use-gatsby-cli)를 사용하는 것입니다.

터미널

```
    gatsby new my-projectcd my-project
```

02

#### Tailwind CSS 설치

npm을 사용해 `@tailwindcss/postcss`, 해당 peer dependencies, 그리고 `gatsby-plugin-postcss`를 설치하세요.

터미널

```
    npm install @tailwindcss/postcss tailwindcss postcss gatsby-plugin-postcss
```

03

#### Gatsby PostCSS 플러그인 활성화

`gatsby-config.js` 파일에서 `gatsby-plugin-postcss`를 활성화하세요. 자세한 내용은 [플러그인 문서](https://www.gatsbyjs.com/plugins/gatsby-plugin-postcss/)를 참고하세요.

gatsby-config.js

```
    module.exports = {  plugins: [    'gatsby-plugin-postcss',    // ...  ],}
```

04

#### PostCSS 플러그인 구성

프로젝트 루트에 `postcss.config.js` 파일을 만들고, PostCSS 설정에 `@tailwindcss/postcss` 플러그인을 추가하세요.

postcss.config.js

```
    module.exports = {  plugins: {    "@tailwindcss/postcss": {},  },};
```

05

#### Tailwind CSS 가져오기

`./src/styles/global.css` 파일을 만들고 Tailwind CSS에 대한 `@import`를 추가하세요.

global.css

```
    @import "tailwindcss";
```

06

#### CSS 파일 가져오기

아직 없다면 프로젝트 루트에 `gatsby-browser.js` 파일을 만들고, 새로 만든 `./src/styles/global.css` 파일을 import하세요.

gatsby-browser.js

```
    import './src/styles/global.css';
```

07

#### 빌드 프로세스 시작

`gatsby develop`로 빌드 프로세스를 실행하세요.

터미널

```
    gatsby develop
```

08

#### 프로젝트에서 Tailwind 사용 시작

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용해 보세요.

index.js

```
    export default function IndexPage() {  return (    <Layout>      <h1 className="text-3xl font-bold underline">        Hello world!      </h1>    </Layout>  )}
```
