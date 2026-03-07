---
title: "Ember.js와 함께 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 설정된 프로젝트가 없다면, 새 Ember.js 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 Ember CLI를 사용하는 것입니다."
---

# Ember.js와 함께 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 설정된 프로젝트가 없다면, 새 Ember.js 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 [Ember CLI](https://guides.emberjs.com/release/getting-started/quick-start/#toc_create-a-new-application)를 사용하는 것입니다.

Terminal

```
    npx ember-cli new my-project --embroider --no-welcomecd my-project
```

02

#### Tailwind CSS 설치하기

npm을 사용해 `@tailwindcss/postcss`와 해당 peer dependencies, 그리고 `postcss-loader`를 설치하세요.

Terminal

```
    npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

03

#### PostCSS 지원 활성화하기

`ember-cli-build.js` 파일에서 PostCSS가 CSS 파일을 처리하도록 설정하세요.

ember-cli-build.js

```
    'use strict';const EmberApp = require('ember-cli/lib/broccoli/ember-app');module.exports = function (defaults) {  const app = new EmberApp(defaults, {    // Add options here  });  const { Webpack } = require('@embroider/webpack');  return require('@embroider/compat').compatBuild(app, Webpack, {    skipBabel: [      {        package: 'qunit',      },    ],    packagerOptions: {      webpackConfig: {        module: {          rules: [            {              test: /\.css$/i,              use: ['postcss-loader'],            },          ],        },      },    },  });};
```

04

#### PostCSS Plugins 구성하기

프로젝트 루트에 `postcss.config.mjs` 파일을 만들고, PostCSS 설정에 `@tailwindcss/postcss` 플러그인을 추가하세요.

postcss.config.mjs

```
    export default {  plugins: {    "@tailwindcss/postcss": {},  },}
```

05

#### Tailwind CSS 가져오기

`./app/app.css` 파일을 생성하고 Tailwind CSS를 위한 `@import`를 추가하세요.

app.css

```
    @import "tailwindcss";
```

06

#### CSS 파일 가져오기

새로 생성한 `./app/app.css` 파일을 `./app/app.js` 파일에서 import하세요.

app.js

```
    import Application from '@ember/application';import Resolver from 'ember-resolver';import loadInitializers from 'ember-load-initializers';import config from 'my-project/config/environment';import 'my-project/app.css';export default class App extends Application {  modulePrefix = config.modulePrefix;  podModulePrefix = config.podModulePrefix;  Resolver = Resolver;}loadInitializers(App, config.modulePrefix);
```

07

#### 빌드 프로세스 시작하기

`npm run start`로 빌드 프로세스를 실행하세요.

Terminal

```
    npm run start
```

08

#### 프로젝트에서 Tailwind 사용 시작하기

Tailwind의 utility classes를 사용해 콘텐츠에 스타일을 적용해 보세요.

application.hbs

```
    {{page-title "MyProject"}}<h1 class="text-3xl font-bold underline">  Hello world!</h1>{{outlet}}
```
