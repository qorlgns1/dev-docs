---
title: "font-weight - 타이포그래피 - Tailwind CSS"
description: "font-thin, font-bold 같은 유틸리티를 사용해 요소의 글꼴 두께를 설정합니다:"
---

출처 URL: https://tailwindcss.com/docs/font-weight

# font-weight - 타이포그래피 - Tailwind CSS

| 클래스                     | 스타일                                 |
| -------------------------- | -------------------------------------- |
| `font-thin`                | `font-weight: 100;`                    |
| `font-extralight`          | `font-weight: 200;`                    |
| `font-light`               | `font-weight: 300;`                    |
| `font-normal`              | `font-weight: 400;`                    |
| `font-medium`              | `font-weight: 500;`                    |
| `font-semibold`            | `font-weight: 600;`                    |
| `font-bold`                | `font-weight: 700;`                    |
| `font-extrabold`           | `font-weight: 800;`                    |
| `font-black`               | `font-weight: 900;`                    |
| `font-(<custom-property>)` | `font-weight: var(<custom-property>);` |
| `font-[<value>]`           | `font-weight: <value>;`                |

## 예시

- 기본 예시

`font-thin`, `font-bold` 같은 유틸리티를 사용해 요소의 글꼴 두께를 설정합니다:

font-light

The quick brown fox jumps over the lazy dog.

font-normal

The quick brown fox jumps over the lazy dog.

font-medium

The quick brown fox jumps over the lazy dog.

font-semibold

The quick brown fox jumps over the lazy dog.

font-bold

The quick brown fox jumps over the lazy dog.

```
    <p class="font-light ...">The quick brown fox ...</p><p class="font-normal ...">The quick brown fox ...</p><p class="font-medium ...">The quick brown fox ...</p><p class="font-semibold ...">The quick brown fox ...</p><p class="font-bold ...">The quick brown fox ...</p>
```

- 사용자 정의 값 사용하기

완전히 사용자 정의한 값으로 글꼴 두께를 설정하려면 `font-[<value>]` 구문을 사용하세요:

```
    <p class="font-[1000] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `font-(weight:<custom-property>)` 구문도 사용할 수 있습니다:

```
    <p class="font-(weight:--my-font-weight) ...">  Lorem ipsum dolor sit amet...</p>
```

이 구문은 `font-[weight:var(<custom-property>)]`의 단축형으로, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`font-weight` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <p class="font-normal md:font-bold ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

프로젝트에서 글꼴 두께 유틸리티를 커스터마이징하려면 `--font-weight-*` 테마 변수를 사용하세요:

```
    @theme {  --font-weight-extrablack: 1000; }
```

이제 마크업에서 `font-extrablack` 유틸리티를 사용할 수 있습니다:

```
    <div class="font-extrablack">  <!-- ... --></div>
```

테마 커스터마이징에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
