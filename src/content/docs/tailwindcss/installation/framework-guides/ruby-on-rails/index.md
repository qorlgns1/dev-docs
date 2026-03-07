---
title: "Ruby on Rails와 함께 Tailwind CSS 설치하기 - Tailwind CSS"
description: "아직 프로젝트가 없다면 새 Rails 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 Rails Command Line을 사용하는 것입니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/ruby-on-rails

# Ruby on Rails와 함께 Tailwind CSS 설치하기 - Tailwind CSS

01

#### 프로젝트 생성하기

아직 프로젝트가 없다면 새 Rails 프로젝트를 먼저 생성하세요. 가장 일반적인 방법은 [Rails Command Line](https://guides.rubyonrails.org/command_line.html)을 사용하는 것입니다.

터미널

```
    rails new my-projectcd my-project
```

02

#### Tailwind CSS 설치하기

`tailwindcss-rails` gem을 설치한 다음 install 명령을 실행해 프로젝트에 Tailwind CSS를 설정하세요.

터미널

```
    bundle add tailwindcss-rails./bin/rails tailwindcss:install
```

03

#### 빌드 프로세스 시작하기

`./bin/dev`로 빌드 프로세스를 실행하세요.

터미널

```
    ./bin/dev
```

04

#### 프로젝트에서 Tailwind 사용 시작하기

Tailwind의 유틸리티 클래스를 사용해 콘텐츠 스타일링을 시작하세요.

index.html.erb

```
    <h1 class="text-3xl font-bold underline">  Hello world!</h1>
```
