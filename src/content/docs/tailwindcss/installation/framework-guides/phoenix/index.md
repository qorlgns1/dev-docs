---
title: "Phoenix와 함께 Tailwind CSS 설치 - Tailwind CSS"
description: "아직 설정된 Phoenix 프로젝트가 없다면, 먼저 새 Phoenix 프로젝트를 생성하세요. 시작하려면 설치 가이드를 따라 진행할 수 있습니다."
---

출처 URL: https://tailwindcss.com/docs/installation/framework-guides/phoenix

# Phoenix와 함께 Tailwind CSS 설치 - Tailwind CSS

01

#### 프로젝트 생성

아직 설정된 Phoenix 프로젝트가 없다면, 먼저 새 Phoenix 프로젝트를 생성하세요. 시작하려면 [설치 가이드](https://hexdocs.pm/phoenix/installation.html)를 따라 진행할 수 있습니다.

터미널

```
    mix phx.new myprojectcd myproject
```

02

#### Tailwind 플러그인 설치

의존성에 Tailwind 플러그인을 추가하고, 설치를 위해 `mix deps.get`을 실행하세요.

mix.exs

```
    defp deps do  [    # …    {:tailwind, "~> 0.3", runtime: Mix.env() == :dev},  ]end
```

03

#### Tailwind 플러그인 구성

`config/config.exs` 파일에서 사용할 Tailwind CSS 버전을 설정하고 에셋 경로를 커스터마이즈할 수 있습니다.

config.exs

```
    config :tailwind,  version: "4.1.10",  myproject: [    args: ~w(      --input=assets/css/app.css      --output=priv/static/assets/app.css    ),    cd: Path.expand("..", __DIR__)  ]
```

04

#### 배포 스크립트 업데이트

배포 시 CSS를 빌드하도록 `assets.deploy` alias를 구성하세요.

mix.exs

```
    defp aliases do  [    # …    "assets.deploy": [      "tailwind myproject --minify",      "esbuild myproject --minify",      "phx.digest"    ]  ]end
```

05

#### 개발 환경에서 watcher 활성화

`./config/dev.exs` 파일의 watcher 목록에 Tailwind를 추가하세요.

dev.exs

```
    watchers: [  # Start the esbuild watcher by calling Esbuild.install_and_run(:default, args)  esbuild: {Esbuild, :install_and_run, [:myproject, ~w(--sourcemap=inline --watch)]},  tailwind: {Tailwind, :install_and_run, [:myproject, ~w(--watch)]}]
```

06

#### Tailwind CSS 설치

독립 실행형 Tailwind CLI를 다운로드하려면 설치 명령을 실행하세요.

터미널

```
    mix tailwind.install
```

07

#### Tailwind CSS 가져오기

Tailwind CSS를 가져오도록 `./assets/css/app.css`에 `@import`를 추가하세요.

app.css

```
    @import "tailwindcss";
```

08

#### 기본 CSS import 제거

이제 Tailwind가 이를 처리하므로 `./assets/js/app.js`에서 CSS import를 제거하세요.

app.js

```
    // Remove this line if you add your own CSS build pipeline (e.g postcss).import "../css/app.css"
```

09

#### 빌드 프로세스 시작

`mix phx.server`로 빌드 프로세스를 실행하세요.

터미널

```
    mix phx.server
```

10

#### 프로젝트에서 Tailwind 사용 시작

Tailwind의 유틸리티 클래스를 사용해 콘텐츠에 스타일을 적용해 보세요.

index.html.heex

```
    <h1 class="text-3xl font-bold underline">  Hello world!</h1>
```
