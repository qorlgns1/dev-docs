---
title: "border-collapse - 테이블 - Tailwind CSS"
description: "가능한 경우 인접한 셀의 테두리를 하나의 테두리로 합치려면 border-collapse 유틸리티를 사용하세요:"
---

출처 URL: https://tailwindcss.com/docs/border-collapse

# border-collapse - 테이블 - Tailwind CSS

| Class             | Styles                       |
| ----------------- | ---------------------------- |
| `border-collapse` | `border-collapse: collapse;` |
| `border-separate` | `border-collapse: separate;` |

## 예제

- 테이블 테두리 병합

가능한 경우 인접한 셀의 테두리를 하나의 테두리로 합치려면 `border-collapse` 유틸리티를 사용하세요:

| State    | City         |
| -------- | ------------ |
| Indiana  | Indianapolis |
| Ohio     | Columbus     |
| Michigan | Detroit      |

```
    <table class="border-collapse border border-gray-400 ...">  <thead>    <tr>      <th class="border border-gray-300 ...">State</th>      <th class="border border-gray-300 ...">City</th>    </tr>  </thead>  <tbody>    <tr>      <td class="border border-gray-300 ...">Indiana</td>      <td class="border border-gray-300 ...">Indianapolis</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Ohio</td>      <td class="border border-gray-300 ...">Columbus</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Michigan</td>      <td class="border border-gray-300 ...">Detroit</td>    </tr>  </tbody></table>
```

최상위 `<table>` 태그의 테두리 병합도 여기에 포함된다는 점에 유의하세요.

- 테이블 테두리 분리

각 셀이 자체적으로 분리된 테두리를 표시하도록 강제하려면 `border-separate` 유틸리티를 사용하세요:

| State    | City         |
| -------- | ------------ |
| Indiana  | Indianapolis |
| Ohio     | Columbus     |
| Michigan | Detroit      |

```
    <table class="border-separate border border-gray-400 ...">  <thead>    <tr>      <th class="border border-gray-300 ...">State</th>      <th class="border border-gray-300 ...">City</th>    </tr>  </thead>  <tbody>    <tr>      <td class="border border-gray-300 ...">Indiana</td>      <td class="border border-gray-300 ...">Indianapolis</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Ohio</td>      <td class="border border-gray-300 ...">Columbus</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Michigan</td>      <td class="border border-gray-300 ...">Detroit</td>    </tr>  </tbody></table>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `border-collapse` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이세요:

```
    <table class="border-collapse md:border-separate ...">  <!-- ... --></table>
```

variant 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
