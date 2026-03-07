---
title: "Install Tailwind CSS with Parcel - Tailwind CSS"
description: "Start by creating a new Parcel project if you don’t have one set up already. The most common approach is to add Parcel as a dev-dependency to your pro..."
---

Source URL: https://tailwindcss.com/docs/installation/framework-guides/parcel

# Install Tailwind CSS with Parcel - Tailwind CSS

01

#### Create your project

Start by creating a new Parcel project if you don’t have one set up already. The most common approach is to add Parcel as a dev-dependency to your project as outlined in their [getting started guide](https://parceljs.org/getting-started/webapp/).

Terminal

```
    mkdir my-projectcd my-projectnpm init -ynpm install parcelmkdir srctouch src/index.html
```

02

#### Install Tailwind CSS

Install `@tailwindcss/postcss` and its peer dependencies via npm.

Terminal

```
    npm install tailwindcss @tailwindcss/postcss
```

03

#### Configure PostCSS

Create a `.postcssrc` file in your project root, and enable the `@tailwindcss/postcss` plugin.

.postcssrc

```
    {  "plugins": {    "@tailwindcss/postcss": {}  }}
```

04

#### Import Tailwind CSS

Create a `./src/index.css` file and add an `@import` for Tailwind CSS.

index.css

```
    @import "tailwindcss";
```

05

#### Start your build process

Run your build process with `npx parcel src/index.html`.

Terminal

```
    npx parcel src/index.html
```

06

#### Start using Tailwind in your project

Add your CSS file to the `<head>` and start using Tailwind’s utility classes to style your content.

index.html

```
    <!doctype html><html>  <head>    <meta charset="UTF-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <link href="./index.css" type="text/css" rel="stylesheet" />  </head>  <body>    <h1 class="text-3xl font-bold underline">      Hello world!    </h1>  </body></html>
```
