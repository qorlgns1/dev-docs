---
title: "font-stretch - 타이포그래피 - Tailwind CSS"
description: "font-stretch-condensed 및 font-stretch-expanded 같은 유틸리티를 사용해 글꼴 페이스의 너비를 설정하세요:"
---

# font-stretch - 타이포그래피 - Tailwind CSS

| 클래스                             | 스타일                                       |
| ---------------------------------- | -------------------------------------------- |
| `font-stretch-ultra-condensed`     | `font-stretch: ultra-condensed; /* 50% */`   |
| `font-stretch-extra-condensed`     | `font-stretch: extra-condensed; /* 62.5% */` |
| `font-stretch-condensed`           | `font-stretch: condensed; /* 75% */`         |
| `font-stretch-semi-condensed`      | `font-stretch: semi-condensed; /* 87.5% */`  |
| `font-stretch-normal`              | `font-stretch: normal; /* 100% */`           |
| `font-stretch-semi-expanded`       | `font-stretch: semi-expanded; /* 112.5% */`  |
| `font-stretch-expanded`            | `font-stretch: expanded; /* 125% */`         |
| `font-stretch-extra-expanded`      | `font-stretch: extra-expanded; /* 150% */`   |
| `font-stretch-ultra-expanded`      | `font-stretch: ultra-expanded; /* 200% */`   |
| `font-stretch-<percentage>`        | `font-stretch: <percentage>;`                |
| `font-stretch-(<custom-property>)` | `font-stretch: var(<custom-property>);`      |
| `font-stretch-[<value>]`           | `font-stretch: <value>;`                     |

## 예제

- 기본 예제

`font-stretch-condensed` 및 `font-stretch-expanded` 같은 유틸리티를 사용해 글꼴 페이스의 너비를 설정하세요:

font-stretch-extra-condensed

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

font-stretch-condensed

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

font-stretch-normal

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

font-stretch-expanded

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

font-stretch-extra-expanded

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="font-stretch-extra-condensed">The quick brown fox...</p><p class="font-stretch-condensed">The quick brown fox...</p><p class="font-stretch-normal">The quick brown fox...</p><p class="font-stretch-expanded">The quick brown fox...</p><p class="font-stretch-extra-expanded">The quick brown fox...</p>
```

이 기능은 너비 변형이 여러 개인 글꼴에만 적용되며, 그렇지 않으면 브라우저가 가장 가까운 매치를 선택합니다.

- 백분율 사용하기

`font-stretch-50%` 및 `font-stretch-125%` 같은 `font-stretch-<percentage>` 유틸리티를 사용해 백분율로 글꼴 페이스의 너비를 설정하세요:

font-stretch-50%

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

font-stretch-100%

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

font-stretch-150%

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="font-stretch-50%">The quick brown fox...</p><p class="font-stretch-100%">The quick brown fox...</p><p class="font-stretch-150%">The quick brown fox...</p>
```

- 사용자 정의 값 사용하기

`font-stretch-[<value>]` 문법을 사용하면 완전히 사용자 정의한 값을 기준으로 글꼴 너비를 설정할 수 있습니다:

```
    <p class="font-stretch-[66.66%] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `font-stretch-(<custom-property>)` 문법도 사용할 수 있습니다:

```
    <p class="font-stretch-(--my-font-width) ...">  Lorem ipsum dolor sit amet...</p>
```

이는 `var()` 함수를 자동으로 추가해 주는 `font-stretch-[var(<custom-property>)]`의 단축 문법입니다.

- 반응형 디자인

`font-stretch` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="font-stretch-normal md:font-stretch-expanded ...">  <!-- ... --></div>
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 더 알아보세요.
