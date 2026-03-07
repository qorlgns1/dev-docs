---
title: "position - 레이아웃 - Tailwind CSS"
description: "문서의 일반 흐름에 따라 요소를 배치하려면 `static` 유틸리티를 사용하세요:"
---

원문 URL: https://tailwindcss.com/docs/position

# position - 레이아웃 - Tailwind CSS

| Class      | Styles                |
| ---------- | --------------------- |
| `static`   | `position: static;`   |
| `fixed`    | `position: fixed;`    |
| `absolute` | `position: absolute;` |
| `relative` | `position: relative;` |
| `sticky`   | `position: sticky;`   |

## 예제

- 요소를 정적으로 배치하기

문서의 일반 흐름에 따라 요소를 배치하려면 `static` 유틸리티를 사용하세요:

정적 부모

절대 위치 자식

```
    <div class="static ...">  <p>Static parent</p>  <div class="absolute bottom-0 left-0 ...">    <p>Absolute child</p>  </div></div>
```

정적으로 배치된 요소에서는 [offsets](https://tailwindcss.com/docs/top-right-bottom-left)가 무시되며, 절대 위치 자식 요소의 위치 기준으로 동작하지 않습니다.

- 요소를 상대적으로 배치하기

문서의 일반 흐름에 따라 요소를 배치하려면 `relative` 유틸리티를 사용하세요:

상대 위치 부모

절대 위치 자식

```
    <div class="relative ...">  <p>Relative parent</p>  <div class="absolute bottom-0 left-0 ...">    <p>Absolute child</p>  </div></div>
```

상대 위치 요소에서는 [offsets](https://tailwindcss.com/docs/top-right-bottom-left)가 요소의 기본 위치를 기준으로 계산되며, 요소는 절대 위치 자식의 위치 기준으로 동작합니다.

- 요소를 절대 위치로 배치하기

`absolute` 유틸리티를 사용하면 문서의 일반 흐름 _외부_ 에 요소를 배치할 수 있으며, 이로 인해 주변 요소들은 해당 요소가 존재하지 않는 것처럼 동작합니다:

정적 배치 사용 시

상대 위치 부모

정적 부모

정적 자식?

정적 형제 요소

절대 배치 사용 시

상대 위치 부모

정적 부모

절대 위치 자식

정적 형제 요소

```
    <div class="static ...">  <!-- Static parent -->  <div class="static ..."><p>Static child</p></div>  <div class="inline-block ..."><p>Static sibling</p></div>  <!-- Static parent -->  <div class="absolute ..."><p>Absolute child</p></div>  <div class="inline-block ..."><p>Static sibling</p></div></div>
```

절대 위치 요소에서는 [offsets](https://tailwindcss.com/docs/top-right-bottom-left)가 `static` 이 아닌 position을 가진 가장 가까운 부모를 기준으로 계산되며, 요소는 다른 절대 위치 자식의 위치 기준으로 동작합니다.

- 요소를 고정 위치로 배치하기

브라우저 창을 기준으로 요소를 배치하려면 `fixed` 유틸리티를 사용하세요:

이 요소를 스크롤하여 고정 위치 동작을 확인하세요

연락처

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Andrew Alfred**

![](https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Debra Houston**

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Jane White**

![](https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Ray Flint**

![](https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Mindy Albrect**

![](https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**David Arnold**

```
     <div class="relative">  <div class="fixed top-0 right-0 left-0">Contacts</div>  <div>    <div>      <img src="/img/andrew.jpg" />      <strong>Andrew Alfred</strong>    </div>    <div>      <img src="/img/debra.jpg" />      <strong>Debra Houston</strong>    </div>    <!-- ... -->  </div></div>
```

고정 위치 요소에서는 [offsets](https://tailwindcss.com/docs/top-right-bottom-left)가 뷰포트를 기준으로 계산되며, 요소는 절대 위치 자식의 위치 기준으로 동작합니다:

- 요소를 스티키 위치로 배치하기

`sticky` 유틸리티를 사용하면 요소가 지정된 임계값을 넘기 전까지는 `relative` 로 배치되고, 부모 요소가 화면 밖으로 나갈 때까지 `fixed` 처럼 동작합니다:

이 요소를 스크롤하여 스티키 위치 동작을 확인하세요

A

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Andrew Alfred**

![](https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Aisha Houston**

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Anna White**

![](https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Andy Flint**

B

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Bob Alfred**

![](https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Bianca Houston**

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Brianna White**

![](https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Bert Flint**

C

![](https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Colton Alfred**

![](https://images.unsplash.com/photo-1531123897727-8f129e1688ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Cynthia Houston**

![](https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Cheyenne White**

![](https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=4&w=256&h=256&q=80)**Charlie Flint**

```
     <div>  <div>    <div class="sticky top-0 ...">A</div>    <div>      <div>        <img src="/img/andrew.jpg" />        <strong>Andrew Alfred</strong>      </div>      <div>        <img src="/img/aisha.jpg" />        <strong>Aisha Houston</strong>      </div>      <!-- ... -->    </div>  </div>  <div>    <div class="sticky top-0">B</div>    <div>      <div>        <img src="/img/bob.jpg" />        <strong>Bob Alfred</strong>      </div>      <!-- ... -->    </div>  </div>  <!-- ... --></div>
```

스티키 위치 요소에서는 [offsets](https://tailwindcss.com/docs/top-right-bottom-left)가 요소의 기본 위치를 기준으로 계산되며, 요소는 절대 위치 자식의 위치 기준으로 동작합니다.

- 반응형 디자인

`position` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 접두사로 붙이면, 중간 크기 화면 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="relative md:absolute ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
