---
title: "place-items - Flexbox 및 Grid - Tailwind CSS"
description: "두 축 모두에서 그리드 영역의 시작 지점에 그리드 아이템을 배치하려면 place-items-start를 사용하세요:"
---

Source URL: https://tailwindcss.com/docs/place-items

# place-items - Flexbox 및 Grid - Tailwind CSS

| Class                     | Styles                      |
| ------------------------- | --------------------------- |
| `place-items-start`       | `place-items: start;`       |
| `place-items-end`         | `place-items: end;`         |
| `place-items-end-safe`    | `place-items: safe end;`    |
| `place-items-center`      | `place-items: center;`      |
| `place-items-center-safe` | `place-items: safe center;` |
| `place-items-baseline`    | `place-items: baseline;`    |
| `place-items-stretch`     | `place-items: stretch;`     |

## 예제

- 시작

두 축 모두에서 그리드 영역의 시작 지점에 그리드 아이템을 배치하려면 `place-items-start`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid grid-cols-3 place-items-start gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 끝

두 축 모두에서 그리드 영역의 끝 지점에 그리드 아이템을 배치하려면 `place-items-end`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid h-56 grid-cols-3 place-items-end gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 가운데

두 축 모두에서 그리드 영역의 중앙에 그리드 아이템을 배치하려면 `place-items-center`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid h-56 grid-cols-3 place-items-center gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

- 늘리기

두 축 모두에서 그리드 영역을 따라 아이템을 늘리려면 `place-items-stretch`를 사용하세요:

01

02

03

04

05

06

```
    <div class="grid h-56 grid-cols-3 place-items-stretch gap-4 ...">  <div>01</div>  <div>02</div>  <div>03</div>  <div>04</div>  <div>05</div>  <div>06</div></div>
```

## 반응형 디자인

`md:`와 같은 브레이크포인트 변형으로 `place-items` 유틸리티에 접두사를 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="grid place-items-start md:place-items-center ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
