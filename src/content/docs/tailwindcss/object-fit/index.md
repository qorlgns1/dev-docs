---
title: "object-fit - 레이아웃 - Tailwind CSS"
description: "요소의 콘텐츠가 컨테이너를 덮도록 크기를 조정하려면 object-cover 유틸리티를 사용하세요:"
---

Source URL: https://tailwindcss.com/docs/object-fit

# object-fit - 레이아웃 - Tailwind CSS

| 클래스              | 스타일                    |
| ------------------- | ------------------------- |
| `object-contain`    | `object-fit: contain;`    |
| `object-cover`      | `object-fit: cover;`      |
| `object-fill`       | `object-fit: fill;`       |
| `object-none`       | `object-fit: none;`       |
| `object-scale-down` | `object-fit: scale-down;` |

## 예제

- 덮도록 크기 조정

요소의 콘텐츠가 컨테이너를 덮도록 크기를 조정하려면 `object-cover` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-cover ..." src="/img/mountains.jpg" />
```

- 내부에 맞춰 포함

요소의 콘텐츠가 컨테이너 내부에 포함된 상태를 유지하도록 크기를 조정하려면 `object-contain` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-contain ..." src="/img/mountains.jpg" />
```

- 맞게 늘리기

요소의 콘텐츠를 컨테이너에 맞게 늘리려면 `object-fill` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-fill ..." src="/img/mountains.jpg" />
```

- 축소하기

요소의 콘텐츠를 원래 크기로 표시하되 필요하면 컨테이너에 맞게 축소하려면 `object-scale-down` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=128&h=160&q=80)

```
    <img class="h-48 w-96 object-scale-down ..." src="/img/mountains.jpg" />
```

- 원래 크기 사용

컨테이너 크기를 무시하고 요소의 콘텐츠를 원래 크기로 표시하려면 `object-none` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-none ..." src="/img/mountains.jpg" />
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `object-fit` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <img class="object-contain md:object-cover" src="/img/mountains.jpg" />
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
