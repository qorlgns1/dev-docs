---
title: "border-spacing - 테이블 - Tailwind CSS"
description: "border-spacing-2, border-spacing-x-3 같은 border-spacing-<number> 유틸리티를 사용해 분리된 테두리가 적용된 테이블 셀의 테두리 사이 간격을 제어할 수 있습니다:"
---

출처 URL: https://tailwindcss.com/docs/border-spacing

# border-spacing - 테이블 - Tailwind CSS

| 클래스                                 | 스타일                                                                        |
| -------------------------------------- | ----------------------------------------------------------------------------- |
| `border-spacing-<number>`              | `border-spacing: calc(var(--spacing) * <number>);`                            |
| `border-spacing-(<custom-property>)`   | `border-spacing: var(<custom-property>);`                                     |
| `border-spacing-[<value>]`             | `border-spacing: <value>;`                                                    |
| `border-spacing-x-<number>`            | `border-spacing: calc(var(--spacing) * <number>) var(--tw-border-spacing-y);` |
| `border-spacing-x-(<custom-property>)` | `border-spacing: var(<custom-property>) var(--tw-border-spacing-y);`          |
| `border-spacing-x-[<value>]`           | `border-spacing: <value> var(--tw-border-spacing-y);`                         |
| `border-spacing-y-<number>`            | `border-spacing: var(--tw-border-spacing-x) calc(var(--spacing) * <number>);` |
| `border-spacing-y-(<custom-property>)` | `border-spacing: var(--tw-border-spacing-x) var(<custom-property>);`          |
| `border-spacing-y-[<value>]`           | `border-spacing: var(--tw-border-spacing-x) <value>;`                         |

## 예제

- 기본 예제

`border-spacing-2`, `border-spacing-x-3` 같은 `border-spacing-<number>` 유틸리티를 사용해 [분리된 테두리](https://tailwindcss.com/docs/border-collapse#separating-table-borders)가 적용된 테이블 셀의 테두리 사이 간격을 제어할 수 있습니다:

| 주       | 도시         |
| -------- | ------------ |
| Indiana  | Indianapolis |
| Ohio     | Columbus     |
| Michigan | Detroit      |

```
    <table class="border-separate border-spacing-2 border border-gray-400 dark:border-gray-500">  <thead>    <tr>      <th class="border border-gray-300 dark:border-gray-600">State</th>      <th class="border border-gray-300 dark:border-gray-600">City</th>    </tr>  </thead>  <tbody>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Indiana</td>      <td class="border border-gray-300 dark:border-gray-700">Indianapolis</td>    </tr>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Ohio</td>      <td class="border border-gray-300 dark:border-gray-700">Columbus</td>    </tr>    <tr>      <td class="border border-gray-300 dark:border-gray-700">Michigan</td>      <td class="border border-gray-300 dark:border-gray-700">Detroit</td>    </tr>  </tbody></table>
```

- 사용자 정의 값 사용하기

`border-spacing-[<value>]` 구문을 사용해 완전히 사용자 정의한 값으로 테두리 간격을 설정할 수 있습니다:

```
    <table class="border-spacing-[7px] ...">  <!-- ... --></table>
```

CSS 변수의 경우 `border-spacing-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <table class="border-spacing-(--my-border-spacing) ...">  <!-- ... --></table>
```

이는 `var()` 함수를 자동으로 추가해 주는 `border-spacing-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`border-spacing` 유틸리티 앞에 `md:` 같은 브레이크포인트 variant를 붙이면, 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <table class="border-spacing-2 md:border-spacing-4 ...">  <!-- ... --></table>
```

variant 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.

## 테마 커스터마이징

`border-spacing-<number>` 유틸리티는 `--spacing` 테마 변수에 의해 동작하며, 이 변수는 사용자 테마에서 커스터마이징할 수 있습니다:

```
    @theme {  --spacing: 1px; }
```

간격 스케일 커스터마이징에 대한 자세한 내용은 [테마 변수 문서](https://tailwindcss.com/docs/theme)를 참고하세요.
