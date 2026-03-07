---
title: "align-self - Flexbox & Grid - Tailwind CSS"
description: "self-auto 유틸리티를 사용해 컨테이너의 align-items 속성 값에 따라 아이템을 정렬합니다:"
---

# align-self - Flexbox & Grid - Tailwind CSS

| 클래스               | 스타일                       |
| -------------------- | ---------------------------- |
| `self-auto`          | `align-self: auto;`          |
| `self-start`         | `align-self: flex-start;`    |
| `self-end`           | `align-self: flex-end;`      |
| `self-end-safe`      | `align-self: safe flex-end;` |
| `self-center`        | `align-self: center;`        |
| `self-center-safe`   | `align-self: safe center;`   |
| `self-stretch`       | `align-self: stretch;`       |
| `self-baseline`      | `align-self: baseline;`      |
| `self-baseline-last` | `align-self: last baseline;` |

## 예제

- 자동

`self-auto` 유틸리티를 사용해 컨테이너의 `align-items` 속성 값에 따라 아이템을 정렬합니다:

01

02

03

```
    <div class="flex items-stretch ...">  <div>01</div>  <div class="self-auto ...">02</div>  <div>03</div></div>
```

- 시작

컨테이너의 `align-items` 값과 관계없이 `self-start` 유틸리티를 사용해 아이템을 컨테이너 교차 축의 시작 지점에 정렬합니다:

01

02

03

```
    <div class="flex items-stretch ...">  <div>01</div>  <div class="self-start ...">02</div>  <div>03</div></div>
```

- 가운데

컨테이너의 `align-items` 값과 관계없이 `self-center` 유틸리티를 사용해 아이템을 컨테이너 교차 축의 중앙에 정렬합니다:

01

02

03

```
    <div class="flex items-stretch ...">  <div>01</div>  <div class="self-center ...">02</div>  <div>03</div></div>
```

- 끝

컨테이너의 `align-items` 값과 관계없이 `self-end` 유틸리티를 사용해 아이템을 컨테이너 교차 축의 끝 지점에 정렬합니다:

01

02

03

```
    <div class="flex items-stretch ...">  <div>01</div>  <div class="self-end ...">02</div>  <div>03</div></div>
```

- 늘이기

컨테이너의 `align-items` 값과 관계없이 `self-stretch` 유틸리티를 사용해 아이템을 컨테이너 교차 축을 채우도록 늘입니다:

01

02

03

```
    <div class="flex items-stretch ...">  <div>01</div>  <div class="self-stretch ...">02</div>  <div>03</div></div>
```

- 베이스라인

`self-baseline` 유틸리티를 사용해 아이템의 베이스라인이 flex 컨테이너 교차 축의 베이스라인과 정렬되도록 합니다:

01

02

03

```
    <div class="flex ...">  <div class="self-baseline pt-2 pb-6">01</div>  <div class="self-baseline pt-8 pb-12">02</div>  <div class="self-baseline pt-12 pb-4">03</div></div>
```

- 마지막 베이스라인

`self-baseline-last` 유틸리티를 사용해 아이템의 베이스라인이 컨테이너의 마지막 베이스라인과 정렬되도록 컨테이너 교차 축을 따라 정렬합니다:

![](https://spotlight.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Favatar.51a13c67.jpg&w=128&q=80)

Spencer Sharp

Space Recruit에서 우주비행사 채용의 미래를 만들어가고 있습니다.

[spacerecruit.com](https://tailwindcss.com/docs/align-self)

![](https://images.unsplash.com/photo-1590895340509-793cb98788c9?q=80&w=256&h=256&&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

Alex Reed

다학제 디자이너입니다.

[alex-reed.com](https://tailwindcss.com/docs/align-self)

```
    <div class="grid grid-cols-[1fr_auto]">  <div>    <img src="img/spencer-sharp.jpg" />    <h4>Spencer Sharp</h4>    <p class="self-baseline-last">Working on the future of astronaut recruitment at Space Recruit.</p>  </div>  <p class="self-baseline-last">spacerecruit.com</p></div>
```

이는 높이가 서로 다른 텍스트 항목도 서로 정렬되도록 보장하는 데 유용합니다.

- 반응형 디자인

`align-self` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티를 적용할 수 있습니다:

```
    <div class="self-auto md:self-end ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
