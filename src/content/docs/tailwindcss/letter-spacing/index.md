---
title: "letter-spacing - 타이포그래피 - Tailwind CSS"
description: "tracking-tight 및 tracking-wide 같은 유틸리티를 사용해 요소의 자간을 설정할 수 있습니다:"
---

# letter-spacing - 타이포그래피 - Tailwind CSS

| 클래스                         | 스타일                                                   |
| ------------------------------ | -------------------------------------------------------- |
| `tracking-tighter`             | `letter-spacing: var(--tracking-tighter); /* -0.05em */` |
| `tracking-tight`               | `letter-spacing: var(--tracking-tight); /* -0.025em */`  |
| `tracking-normal`              | `letter-spacing: var(--tracking-normal); /* 0em */`      |
| `tracking-wide`                | `letter-spacing: var(--tracking-wide); /* 0.025em */`    |
| `tracking-wider`               | `letter-spacing: var(--tracking-wider); /* 0.05em */`    |
| `tracking-widest`              | `letter-spacing: var(--tracking-widest); /* 0.1em */`    |
| `tracking-(<custom-property>)` | `letter-spacing: var(<custom-property>);`                |
| `tracking-[<value>]`           | `letter-spacing: <value>;`                               |

## 예제

- 기본 예제

`tracking-tight` 및 `tracking-wide` 같은 유틸리티를 사용해 요소의 자간을 설정할 수 있습니다:

tracking-tight

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

tracking-normal

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

tracking-wide

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="tracking-tight ...">The quick brown fox ...</p><p class="tracking-normal ...">The quick brown fox ...</p><p class="tracking-wide ...">The quick brown fox ...</p>
```

- 음수 값 사용하기

Tailwind가 기본으로 제공하는 이름 기반 자간 스케일에서는 음수 값을 쓰는 것이 크게 의미 있지는 않지만, 스케일을 숫자 기반으로 커스터마이징했다면 유용할 수 있습니다:

```
    @theme {  --tracking-1: 0em;  --tracking-2: 0.025em;  --tracking-3: 0.05em;  --tracking-4: 0.1em;}
```

음수 자간 값을 사용하려면 클래스 이름 앞에 대시를 붙여 음수 값으로 변환하세요:

```
    <p class="-tracking-2">The quick brown fox ...</p>
```

- 사용자 지정 값 사용하기

`tracking-[<value>]` 구문을 사용하면 완전히 사용자 지정한 값으로 자간을 설정할 수 있습니다:

```
    <p class="tracking-[.25em] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `tracking-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <p class="tracking-(--my-tracking) ...">  Lorem ipsum dolor sit amet...</p>
```

이는 `tracking-[var(<custom-property>)]`의 단축 표기이며, `var()` 함수를 자동으로 추가해 줍니다.

- 반응형 디자인

`letter-spacing` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <p class="tracking-tight md:tracking-wide ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

`--tracking-*` 테마 변수를 사용해 프로젝트의 자간 유틸리티를 커스터마이징할 수 있습니다:

```
    @theme {  --tracking-tightest: -0.075em; }
```

이제 마크업에서 `tracking-tightest` 유틸리티를 사용할 수 있습니다:

```
    <p class="tracking-tightest">  Lorem ipsum dolor sit amet...</p>
```

테마 커스터마이징에 대한 자세한 내용은 [theme 문서](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.
