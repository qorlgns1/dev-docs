---
title: "vertical-align - 타이포그래피 - Tailwind CSS"
description: "요소의 기준선을 부모의 기준선에 맞춰 정렬하려면 align-baseline 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/vertical-align

# vertical-align - 타이포그래피 - Tailwind CSS

| 클래스                      | 스타일                                    |
| --------------------------- | ----------------------------------------- |
| `align-baseline`            | `vertical-align: baseline;`               |
| `align-top`                 | `vertical-align: top;`                    |
| `align-middle`              | `vertical-align: middle;`                 |
| `align-bottom`              | `vertical-align: bottom;`                 |
| `align-text-top`            | `vertical-align: text-top;`               |
| `align-text-bottom`         | `vertical-align: text-bottom;`            |
| `align-sub`                 | `vertical-align: sub;`                    |
| `align-super`               | `vertical-align: super;`                  |
| `align-(<custom-property>)` | `vertical-align: var(<custom-property>);` |
| `align-[<value>]`           | `vertical-align: <value>;`                |

## 예제

- 기준선에 맞춰 정렬하기

요소의 기준선을 부모의 기준선에 맞춰 정렬하려면 `align-baseline` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <span class="inline-block align-baseline">The quick brown fox...</span>
```

- 위쪽에 맞춰 정렬하기

요소와 그 자손의 위쪽을 전체 줄의 위쪽에 맞춰 정렬하려면 `align-top` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <span class="inline-block align-top">The quick brown fox...</span>
```

- 가운데에 맞춰 정렬하기

요소의 가운데를 부모의 기준선에 x-height의 절반을 더한 위치에 맞춰 정렬하려면 `align-middle` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <span class="inline-block align-middle">The quick brown fox...</span>
```

- 아래쪽에 맞춰 정렬하기

요소와 그 자손의 아래쪽을 전체 줄의 아래쪽에 맞춰 정렬하려면 `align-bottom` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <span class="inline-block align-bottom">The quick brown fox...</span>
```

- 부모의 위쪽에 맞춰 정렬하기

요소의 위쪽을 부모 요소 글꼴의 위쪽에 맞춰 정렬하려면 `align-text-top` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <span class="inline-block align-text-top">The quick brown fox...</span>
```

- 부모의 아래쪽에 맞춰 정렬하기

요소의 아래쪽을 부모 요소 글꼴의 아래쪽에 맞춰 정렬하려면 `align-text-bottom` 유틸리티를 사용하세요:

The quick brown fox jumps over the lazy dog.

```
    <span class="inline-block align-text-bottom">The quick brown fox...</span>
```

- 사용자 지정 값 사용하기

완전히 사용자 지정한 값으로 수직 정렬을 설정하려면 `align-[<value>]` 구문을 사용하세요:

```
    <span class="align-[4px] ...">  <!-- ... --></span>
```

CSS 변수의 경우 `align-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <span class="align-(--my-alignment) ...">  <!-- ... --></span>
```

이것은 `var()` 함수를 자동으로 추가해 주는 `align-[var(<custom-property>)]`의 단축 구문입니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 variant를 `vertical-align` 유틸리티 앞에 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <span class="align-middle md:align-top ...">  <!-- ... --></span>
```

variant 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
