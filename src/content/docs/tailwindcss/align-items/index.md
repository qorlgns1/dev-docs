---
title: "align-items - Flexbox 및 Grid - Tailwind CSS"
description: "컨테이너의 교차 축을 채우도록 항목을 늘리려면 items-stretch 유틸리티를 사용하세요:"
---

# align-items - Flexbox 및 Grid - Tailwind CSS

| 클래스                | 스타일                        |
| --------------------- | ----------------------------- |
| `items-start`         | `align-items: flex-start;`    |
| `items-end`           | `align-items: flex-end;`      |
| `items-end-safe`      | `align-items: safe flex-end;` |
| `items-center`        | `align-items: center;`        |
| `items-center-safe`   | `align-items: safe center;`   |
| `items-baseline`      | `align-items: baseline;`      |
| `items-baseline-last` | `align-items: last baseline;` |
| `items-stretch`       | `align-items: stretch;`       |

## 예제

- 늘이기

컨테이너의 교차 축을 채우도록 항목을 늘리려면 `items-stretch` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex items-stretch ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

- 시작

컨테이너 교차 축의 시작 지점에 항목을 정렬하려면 `items-start` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex items-start ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

- 가운데

컨테이너 교차 축의 중앙을 따라 항목을 정렬하려면 `items-center` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex items-center ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

- 끝

컨테이너 교차 축의 끝 지점에 항목을 정렬하려면 `items-end` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex items-end ...">  <div class="py-4">01</div>  <div class="py-12">02</div>  <div class="py-8">03</div></div>
```

- 기준선

모든 항목의 기준선이 맞춰지도록 컨테이너 교차 축을 따라 항목을 정렬하려면 `items-baseline` 유틸리티를 사용하세요:

01

02

03

```
    <div class="flex items-baseline ...">  <div class="pt-2 pb-6">01</div>  <div class="pt-8 pb-12">02</div>  <div class="pt-12 pb-4">03</div></div>
```

- 마지막 기준선

컨테이너의 마지막 기준선에 맞춰 모든 항목의 기준선이 정렬되도록 컨테이너 교차 축을 따라 항목을 정렬하려면 `items-baseline-last` 유틸리티를 사용하세요:

![](https://spotlight.tailwindui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Favatar.51a13c67.jpg&w=128&q=80)

Spencer Sharp

Space Recruit에서 우주비행사 채용의 미래를 만들고 있습니다.

[spacerecruit.com](https://tailwindcss.com/docs/align-items)

![](https://images.unsplash.com/photo-1590895340509-793cb98788c9?q=80&w=256&h=256&&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

Alex Reed

다분야 디자이너입니다.

[alex-reed.com](https://tailwindcss.com/docs/align-items)

```
    <div class="grid grid-cols-[1fr_auto] items-baseline-last">  <div>    <img src="img/spencer-sharp.jpg" />    <h4>Spencer Sharp</h4>    <p>Working on the future of astronaut recruitment at Space Recruit.</p>  </div>  <p>spacerecruit.com</p></div>
```

이 방법은 텍스트 항목의 높이가 서로 달라도 서로 정렬되도록 보장하는 데 유용합니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `align-items` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="flex items-stretch md:items-center ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
