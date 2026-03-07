---
title: "forced-color-adjust - 접근성 - Tailwind CSS"
description: "forced-color-adjust-none 유틸리티를 사용하면 요소를 강제 색상 모드에서 적용되는 색상에서 제외할 수 있습니다. 제한된 색상 팔레트를 강제로 적용하면 사용성이 저하되는 상황에서 유용합니다."
---

출처 URL: https://tailwindcss.com/docs/forced-color-adjust

# forced-color-adjust - 접근성 - Tailwind CSS

| 클래스                     | 스타일                       |
| -------------------------- | ---------------------------- |
| `forced-color-adjust-auto` | `forced-color-adjust: auto;` |
| `forced-color-adjust-none` | `forced-color-adjust: none;` |

## 예제

- 강제 색상 적용 제외하기

`forced-color-adjust-none` 유틸리티를 사용하면 요소를 강제 색상 모드에서 적용되는 색상에서 제외할 수 있습니다. 제한된 색상 팔레트를 강제로 적용하면 사용성이 저하되는 상황에서 유용합니다.

변경 사항을 확인하려면 개발자 도구에서 `forced-colors: active`를 에뮬레이션해 보세요.

![회색, 흰색, 검은색 셔츠가 각각 두 장씩 펼쳐져 놓여 있습니다.](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ft-shirt.250cd197.jpg&w=3840&q=75)

베이직 티

$35

색상을 선택하세요

화이트그레이블랙

```
    <form>  <img src="/img/shirt.jpg" />  <div>    <h3>Basic Tee</h3>    <h3>$35</h3>    <fieldset>      <legend class="sr-only">Choose a color</legend>      <div class="forced-color-adjust-none ...">        <label>          <input class="sr-only" type="radio" name="color-choice" value="White" />          <span class="sr-only">White</span>          <span class="size-6 rounded-full border border-black/10 bg-white"></span>        </label>        <!-- ... -->      </div>    </fieldset>  </div></form>
```

사용자가 강제 색상 모드를 활성화했을 때 조건부로 스타일을 추가하려면 [forced colors variant](https://tailwindcss.com/docs/hover-focus-and-other-states#forced-colors)를 사용할 수도 있습니다.

- 강제 색상 복원하기

`forced-color-adjust-auto` 유틸리티를 사용하면 요소가 강제 색상 모드에서 적용되는 색상을 따르도록 만들 수 있습니다.

```
    <form>  <fieldset class="forced-color-adjust-none lg:forced-color-adjust-auto ...">    <legend>Choose a color:</legend>    <select class="hidden lg:block">      <option value="White">White</option>      <option value="Gray">Gray</option>      <option value="Black">Black</option>    </select>    <div class="lg:hidden">      <label>        <input class="sr-only" type="radio" name="color-choice" value="White" />        <!-- ... -->      </label>      <!-- ... -->    </div>  </fieldset></form>
```

예를 들어 더 큰 화면 크기에서 `forced-color-adjust-none` 유틸리티를 되돌리고 싶을 때 유용합니다.

- 반응형 디자인

`forced-color-adjust` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다.

```
    <div class="forced-color-adjust-none md:forced-color-adjust-auto ...">  <!-- ... --></div>
```

variant 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
