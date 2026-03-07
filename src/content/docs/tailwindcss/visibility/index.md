---
title: "visibility - 레이아웃 - Tailwind CSS"
description: "invisible 유틸리티를 사용하면 요소를 숨기면서도 문서에서의 자리는 유지되어, 다른 요소의 레이아웃에는 계속 영향을 줍니다:"
---

출처 URL: https://tailwindcss.com/docs/visibility

# visibility - 레이아웃 - Tailwind CSS

| 클래스      | 스타일                  |
| ----------- | ----------------------- |
| `visible`   | `visibility: visible;`  |
| `invisible` | `visibility: hidden;`   |
| `collapse`  | `visibility: collapse;` |

## 예제

- 요소를 보이지 않게 만들기

`invisible` 유틸리티를 사용하면 요소를 숨기면서도 문서에서의 자리는 유지되어, 다른 요소의 레이아웃에는 계속 영향을 줍니다:

01

02

03

```
    <div class="grid grid-cols-3 gap-4">  <div>01</div>  <div class="invisible ...">02</div>  <div>03</div></div>
```

요소를 문서에서 완전히 제거하려면 대신 [display](https://tailwindcss.com/docs/display#hidden) 속성을 사용하세요.

- 요소 접기

`collapse` 유틸리티를 사용하면 테이블 행, 행 그룹, 열, 열 그룹을 `display: none`으로 설정한 것처럼 숨길 수 있으며, 다른 행과 열의 크기에는 영향을 주지 않습니다:

모든 행 표시

| Invoice # | Client                      | Amount     |
| --------- | --------------------------- | ---------- |
| #100      | Pendant Publishing          | $2,000.00  |
| #101      | Kruger Industrial Smoothing | $545.00    |
| #102      | J. Peterman                 | $10,000.25 |

`collapse`를 사용해 행 숨기기

| Invoice # | Client                      | Amount     |
| --------- | --------------------------- | ---------- |
| #100      | Pendant Publishing          | $2,000.00  |
| #101      | Kruger Industrial Smoothing | $545.00    |
| #102      | J. Peterman                 | $10,000.25 |

`hidden`을 사용해 행 숨기기

| Invoice # | Client                      | Amount     |
| --------- | --------------------------- | ---------- |
| #100      | Pendant Publishing          | $2,000.00  |
| #101      | Kruger Industrial Smoothing | $545.00    |
| #102      | J. Peterman                 | $10,000.25 |

```
    <table>  <thead>    <tr>      <th>Invoice #</th>      <th>Client</th>      <th>Amount</th>    </tr>  </thead>  <tbody>    <tr>      <td>#100</td>      <td>Pendant Publishing</td>      <td>$2,000.00</td>    </tr>    <tr class="collapse">      <td>#101</td>      <td>Kruger Industrial Smoothing</td>      <td>$545.00</td>    </tr>    <tr>      <td>#102</td>      <td>J. Peterman</td>      <td>$10,000.25</td>    </tr>  </tbody></table>
```

이렇게 하면 테이블 레이아웃에 영향을 주지 않고 행과 열을 동적으로 토글할 수 있습니다.

- 요소를 보이게 만들기

요소를 보이게 하려면 `visible` 유틸리티를 사용하세요:

01

02

03

```
    <div class="grid grid-cols-3 gap-4">  <div>01</div>  <div class="visible ...">02</div>  <div>03</div></div>
```

이는 주로 서로 다른 화면 크기에서 `invisible` 유틸리티를 되돌릴 때 유용합니다.

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `visibility` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <div class="visible md:invisible ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
