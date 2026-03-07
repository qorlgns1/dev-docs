---
title: "table-layout - 테이블 - Tailwind CSS"
description: "`table-auto` 유틸리티를 사용하면 셀 콘텐츠에 맞게 테이블 열 크기가 자동으로 조정됩니다:"
---

Source URL: https://tailwindcss.com/docs/table-layout

# table-layout - 테이블 - Tailwind CSS

| Class         | Styles                 |
| ------------- | ---------------------- |
| `table-auto`  | `table-layout: auto;`  |
| `table-fixed` | `table-layout: fixed;` |

## 예제

- 열 크기 자동 조정

`table-auto` 유틸리티를 사용하면 셀 콘텐츠에 맞게 테이블 열 크기가 자동으로 조정됩니다:

| Song                                            | Artist                | Year |
| ----------------------------------------------- | --------------------- | ---- |
| The Sliding Mr. Bones (Next Stop, Pottersville) | Malcolm Lockyer       | 1961 |
| Witchy Woman                                    | The Eagles            | 1972 |
| Shining Star                                    | Earth, Wind, and Fire | 1975 |

```
    <table class="table-auto">  <thead>    <tr>      <th>Song</th>      <th>Artist</th>      <th>Year</th>    </tr>  </thead>  <tbody>    <tr>      <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>      <td>Malcolm Lockyer</td>      <td>1961</td>    </tr>    <tr>      <td>Witchy Woman</td>      <td>The Eagles</td>      <td>1972</td>    </tr>    <tr>      <td>Shining Star</td>      <td>Earth, Wind, and Fire</td>      <td>1975</td>    </tr>  </tbody></table>
```

- 고정 열 너비 사용

`table-fixed` 유틸리티를 사용하면 테이블 셀의 콘텐츠를 무시하고 각 열에 고정 너비를 사용합니다:

| Song                                            | Artist                | Year |
| ----------------------------------------------- | --------------------- | ---- |
| The Sliding Mr. Bones (Next Stop, Pottersville) | Malcolm Lockyer       | 1961 |
| Witchy Woman                                    | The Eagles            | 1972 |
| Shining Star                                    | Earth, Wind, and Fire | 1975 |

```
    <table class="table-fixed">  <thead>    <tr>      <th>Song</th>      <th>Artist</th>      <th>Year</th>    </tr>  </thead>  <tbody>    <tr>      <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>      <td>Malcolm Lockyer</td>      <td>1961</td>    </tr>    <tr>      <td>Witchy Woman</td>      <td>The Eagles</td>      <td>1972</td>    </tr>    <tr>      <td>Shining Star</td>      <td>Earth, Wind, and Fire</td>      <td>1975</td>    </tr>  </tbody></table>
```

일부 열의 너비를 수동으로 설정할 수 있으며, 나머지 가용 너비는 명시적 너비가 없는 열에 균등하게 분배됩니다. 첫 번째 행에서 설정한 너비가 전체 테이블의 열 너비를 결정합니다.

- 반응형 디자인

`md:` 같은 브레이크포인트 변형으로 `table-layout` 유틸리티에 접두사를 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <div class="table-auto md:table-fixed ...">  <!-- ... --></div>
```

변형 사용법에 대한 자세한 내용은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 확인하세요.
