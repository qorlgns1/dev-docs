---
title: "font-size - 타이포그래피 - Tailwind CSS"
description: "요소의 글꼴 크기를 설정하려면 text-sm, text-lg 같은 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/font-size

# font-size - 타이포그래피 - Tailwind CSS

| 클래스                            | 스타일                                                                                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `text-xs`                         | `font-size: var(--text-xs); /* 0.75rem (12px) */ line-height: var(--text-xs--line-height); /* calc(1 / 0.75) */`        |
| `text-sm`                         | `font-size: var(--text-sm); /* 0.875rem (14px) */ line-height: var(--text-sm--line-height); /* calc(1.25 / 0.875) */`   |
| `text-base`                       | `font-size: var(--text-base); /* 1rem (16px) */ line-height: var(--text-base--line-height); /* calc(1.5 / 1) */`        |
| `text-lg`                         | `font-size: var(--text-lg); /* 1.125rem (18px) */ line-height: var(--text-lg--line-height); /* calc(1.75 / 1.125) */`   |
| `text-xl`                         | `font-size: var(--text-xl); /* 1.25rem (20px) */ line-height: var(--text-xl--line-height); /* calc(1.75 / 1.25) */`     |
| `text-2xl`                        | `font-size: var(--text-2xl); /* 1.5rem (24px) */ line-height: var(--text-2xl--line-height); /* calc(2 / 1.5) */`        |
| `text-3xl`                        | `font-size: var(--text-3xl); /* 1.875rem (30px) */ line-height: var(--text-3xl--line-height); /* calc(2.25 / 1.875) */` |
| `text-4xl`                        | `font-size: var(--text-4xl); /* 2.25rem (36px) */ line-height: var(--text-4xl--line-height); /* calc(2.5 / 2.25) */`    |
| `text-5xl`                        | `font-size: var(--text-5xl); /* 3rem (48px) */ line-height: var(--text-5xl--line-height); /* 1 */`                      |
| `text-6xl`                        | `font-size: var(--text-6xl); /* 3.75rem (60px) */ line-height: var(--text-6xl--line-height); /* 1 */`                   |
| `text-7xl`                        | `font-size: var(--text-7xl); /* 4.5rem (72px) */ line-height: var(--text-7xl--line-height); /* 1 */`                    |
| `text-8xl`                        | `font-size: var(--text-8xl); /* 6rem (96px) */ line-height: var(--text-8xl--line-height); /* 1 */`                      |
| `text-9xl`                        | `font-size: var(--text-9xl); /* 8rem (128px) */ line-height: var(--text-9xl--line-height); /* 1 */`                     |
| `text-(length:<custom-property>)` | `font-size: var(<custom-property>);`                                                                                    |
| `text-[<value>]`                  | `font-size: <value>;`                                                                                                   |

## 예제

- 기본 예제

요소의 글꼴 크기를 설정하려면 `text-sm`, `text-lg` 같은 유틸리티를 사용하세요:

text-sm

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

text-base

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

text-lg

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

text-xl

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

text-2xl

빠른 갈색 여우가 게으른 개를 뛰어넘습니다.

```
    <p class="text-sm ...">The quick brown fox ...</p><p class="text-base ...">The quick brown fox ...</p><p class="text-lg ...">The quick brown fox ...</p><p class="text-xl ...">The quick brown fox ...</p><p class="text-2xl ...">The quick brown fox ...</p>
```

- line-height 설정

`text-sm/6`, `text-lg/7` 같은 유틸리티를 사용하면 요소의 글꼴 크기와 line-height를 동시에 설정할 수 있습니다:

text-sm/6

그래서 나는 물속으로 걸어 들어가기 시작했다. 솔직히 말하면, 얘들아, 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 파도를 지나쳐 가는 동안 이상할 정도의 평온함이 밀려왔다. 그것이 신의 개입이었는지, 모든 생명체 사이의 유대감이었는지는 모르겠지만, Jerry, 바로 그 순간 나는 _정말_ 해양생물학자였다.

text-sm/7

그래서 나는 물속으로 걸어 들어가기 시작했다. 솔직히 말하면, 얘들아, 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 파도를 지나쳐 가는 동안 이상할 정도의 평온함이 밀려왔다. 그것이 신의 개입이었는지, 모든 생명체 사이의 유대감이었는지는 모르겠지만, Jerry, 바로 그 순간 나는 _정말_ 해양생물학자였다.

text-sm/8

그래서 나는 물속으로 걸어 들어가기 시작했다. 솔직히 말하면, 얘들아, 나는 겁에 질려 있었다. 하지만 계속 나아갔고, 파도를 지나쳐 가는 동안 이상할 정도의 평온함이 밀려왔다. 그것이 신의 개입이었는지, 모든 생명체 사이의 유대감이었는지는 모르겠지만, Jerry, 바로 그 순간 나는 _정말_ 해양생물학자였다.

```
    <p class="text-sm/6 ...">So I started to walk into the water...</p><p class="text-sm/7 ...">So I started to walk into the water...</p><p class="text-sm/8 ...">So I started to walk into the water...</p>
```

- 사용자 지정 값 사용

완전히 사용자 지정한 값으로 글꼴 크기를 설정하려면 `text-[<value>]` 문법을 사용하세요:

```
    <p class="text-[14px] ...">  Lorem ipsum dolor sit amet...</p>
```

CSS 변수의 경우 `text-(length:<custom-property>)` 문법도 사용할 수 있습니다:

```
    <p class="text-(length:--my-text-size) ...">  Lorem ipsum dolor sit amet...</p>
```

이는 `var()` 함수를 자동으로 추가해 주는 `text-[length:var(<custom-property>)]`의 축약형입니다.

- 반응형 디자인

`font-size` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <p class="text-sm md:text-base ...">  Lorem ipsum dolor sit amet...</p>
```

variant 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.

## 테마 커스터마이징

프로젝트에서 글꼴 크기 유틸리티를 커스터마이징하려면 `--text-*` 테마 변수를 사용하세요:

```
    @theme {  --text-tiny: 0.625rem; }
```

이제 마크업에서 `text-tiny` 유틸리티를 사용할 수 있습니다:

```
    <div class="text-tiny">  <!-- ... --></div>
```

글꼴 크기에 대한 기본 `line-height`, `letter-spacing`, `font-weight` 값도 함께 제공할 수 있습니다:

```
    @theme {  --text-tiny: 0.625rem;  --text-tiny--line-height: 1.5rem;   --text-tiny--letter-spacing: 0.125rem;   --text-tiny--font-weight: 500; }
```

테마 커스터마이징에 대한 자세한 내용은 [theme 문서](https://tailwindcss.com/docs/theme#customizing-your-theme)를 참고하세요.
