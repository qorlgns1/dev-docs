---
title: "Install Tailwind CSS with Ruby on Rails - Tailwind CSS"
description: "Start by creating a new Rails project if you don't have one set up already. The most common approach is to use the Rails Command Line."
---

Source URL: https://tailwindcss.com/docs/installation/framework-guides/ruby-on-rails

# Install Tailwind CSS with Ruby on Rails - Tailwind CSS

01

#### Create your project

Start by creating a new Rails project if you don't have one set up already. The most common approach is to use the [Rails Command Line](https://guides.rubyonrails.org/command_line.html).

Terminal

```
    rails new my-projectcd my-project
```

02

#### Install Tailwind CSS

Install the `tailwindcss-rails` gem then run the install command to set up Tailwind CSS in your project.

Terminal

```
    bundle add tailwindcss-rails./bin/rails tailwindcss:install
```

03

#### Start your build process

Run your build process with `./bin/dev`.

Terminal

```
    ./bin/dev
```

04

#### Start using Tailwind in your project

Start using Tailwind's utility classes to style your content.

index.html.erb

```
    <h1 class="text-3xl font-bold underline">  Hello world!</h1>
```
