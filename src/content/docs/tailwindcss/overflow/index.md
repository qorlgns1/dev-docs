---
title: "overflow - 레이아웃 - Tailwind CSS"
description: "요소 내부의 콘텐츠가 잘리지 않도록 하려면 `overflow-visible` 유틸리티를 사용하세요:"
---

Source URL: https://tailwindcss.com/docs/overflow

# overflow - 레이아웃 - Tailwind CSS

| 클래스               | 스타일                 |
| -------------------- | ---------------------- |
| `overflow-auto`      | `overflow: auto;`      |
| `overflow-hidden`    | `overflow: hidden;`    |
| `overflow-clip`      | `overflow: clip;`      |
| `overflow-visible`   | `overflow: visible;`   |
| `overflow-scroll`    | `overflow: scroll;`    |
| `overflow-x-auto`    | `overflow-x: auto;`    |
| `overflow-y-auto`    | `overflow-y: auto;`    |
| `overflow-x-hidden`  | `overflow-x: hidden;`  |
| `overflow-y-hidden`  | `overflow-y: hidden;`  |
| `overflow-x-clip`    | `overflow-x: clip;`    |
| `overflow-y-clip`    | `overflow-y: clip;`    |
| `overflow-x-visible` | `overflow-x: visible;` |
| `overflow-y-visible` | `overflow-y: visible;` |
| `overflow-x-scroll`  | `overflow-x: scroll;`  |
| `overflow-y-scroll`  | `overflow-y: scroll;`  |

## 예제

- 넘치는 콘텐츠 표시하기

요소 내부의 콘텐츠가 잘리지 않도록 `overflow-visible` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Andrew Alfred** 기술 고문

```
    <div class="overflow-visible ...">  <!-- ... --></div>
```

요소 경계를 넘친 모든 콘텐츠는 보이게 됩니다.

- 넘치는 콘텐츠 숨기기

요소 경계를 넘치는 요소 내부의 콘텐츠를 잘라내려면 `overflow-hidden` 유틸리티를 사용하세요:

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Andrew Alfred** 기술 고문

```
    <div class="overflow-hidden ...">  <!-- ... --></div>
```

- 필요할 때 스크롤하기

콘텐츠가 요소 경계를 넘칠 때 스크롤바를 추가하려면 `overflow-auto` 유틸리티를 사용하세요:

세로로 스크롤

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Andrew Alfred** 기술 고문

![](https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Debra Houston** 분석가

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Jane White** 마케팅 이사

![](https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Ray Flint** 기술 고문

```
    <div class="overflow-auto ...">  <!-- ... --></div>
```

항상 스크롤바를 표시하는 `overflow-scroll`과 달리, 이 유틸리티는 스크롤이 필요할 때만 스크롤바를 표시합니다.

- 필요할 때 가로로 스크롤하기

필요한 경우 가로 스크롤을 허용하려면 `overflow-x-auto` 유틸리티를 사용하세요:

가로로 스크롤

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Andrew**

![](https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Emily**

![](https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Whitney**

![](https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**David**

![](https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Kristin**

![](https://images.unsplash.com/photo-1605405748313-a416a1b84491?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Sarah**

```
     <div class="overflow-x-auto ...">  <!-- ... --></div>
```

- 필요할 때 세로로 스크롤하기

필요한 경우 세로 스크롤을 허용하려면 `overflow-y-auto` 유틸리티를 사용하세요:

세로로 스크롤

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Andrew Alfred** 기술 고문

![](https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Debra Houston** 분석가

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Jane White** 마케팅 이사

![](https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Ray Flint** 기술 고문

```
    <div class="h-32 overflow-y-auto ...">  <!-- ... --></div>
```

- 항상 가로로 스크롤하기

`overflow-x-scroll` 유틸리티를 사용하면 가로 스크롤을 허용하고, 운영 체제에서 항상 표시되는 스크롤바를 비활성화하지 않은 한 스크롤바를 항상 표시합니다:

가로로 스크롤

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Andrew**

![](https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Emily**

![](https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Whitney**

![](https://images.unsplash.com/photo-1519345182560-3f2917c472ef?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**David**

![](https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Kristin**

![](https://images.unsplash.com/photo-1605405748313-a416a1b84491?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Sarah**

```
     <div class="overflow-x-scroll ...">  <!-- ... --></div>
```

- 항상 세로로 스크롤하기

`overflow-y-scroll` 유틸리티를 사용하면 세로 스크롤을 허용하고, 운영 체제에서 항상 표시되는 스크롤바를 비활성화하지 않은 한 스크롤바를 항상 표시합니다:

세로로 스크롤

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Andrew Alfred** 기술 고문

![](https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Debra Houston** 분석가

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Jane White** 마케팅 이사

![](https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)

**Ray Flint** 기술 고문

```
    <div class="overflow-y-scroll ...">  <!-- ... --></div>
```

- 모든 방향으로 스크롤하기

요소에 스크롤바를 추가하려면 `overflow-scroll` 유틸리티를 사용하세요:

세로 및 가로로 스크롤

일

월

화

수

목

금

토

오전 5시

오전 6시

오전 7시

오전 8시

오전 9시

오전 10시

오전 11시

오후 12시

오후 1시

오후 2시

오후 3시

오후 4시

오후 5시

오후 6시

오후 7시

오후 8시

오전 5시밴쿠버행 항공편토론토 YYZ

오전 6시아침 식사Mel's Diner

오후 5시🎉 파티 파티 🎉우리 파티를 좋아해요!

```
    <div class="overflow-scroll ...">  <!-- ... --></div>
```

필요할 때만 스크롤바를 표시하는 `overflow-auto`와 달리, 이 유틸리티는 스크롤바를 항상 표시합니다. 다만 macOS 같은 일부 운영 체제에서는 이 설정과 관계없이 불필요한 스크롤바를 숨깁니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `overflow` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="overflow-auto md:overflow-scroll ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
