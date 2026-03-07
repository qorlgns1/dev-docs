---
title: "caption-side - 테이블 - Tailwind CSS"
description: "caption-top 유틸리티를 사용해 캡션 요소를 테이블의 상단에 배치하세요:"
---

# caption-side - 테이블 - Tailwind CSS

| 클래스           | 스타일                  |
| ---------------- | ----------------------- |
| `caption-top`    | `caption-side: top;`    |
| `caption-bottom` | `caption-side: bottom;` |

## 예제

- 테이블 상단에 배치하기

`caption-top` 유틸리티를 사용해 캡션 요소를 테이블의 상단에 배치하세요:

표 3.1: 프로레슬러와 그들의 시그니처 기술.
레슬러| 시그니처 기술
---|---
"Stone Cold" Steve Austin| Stone Cold Stunner, Lou Thesz Press
Bret "The Hitman" Hart| The Sharpshooter
Razor Ramon| Razor's Edge, Fallaway Slam

```
    <table>  <caption class="caption-top">    Table 3.1: Professional wrestlers and their signature moves.  </caption>  <thead>    <tr>      <th>Wrestler</th>      <th>Signature Move(s)</th>    </tr>  </thead>  <tbody>    <tr>      <td>"Stone Cold" Steve Austin</td>      <td>Stone Cold Stunner, Lou Thesz Press</td>    </tr>    <tr>      <td>Bret "The Hitman" Hart</td>      <td>The Sharpshooter</td>    </tr>    <tr>      <td>Razor Ramon</td>      <td>Razor's Edge, Fallaway Slam</td>    </tr>  </tbody></table>
```

- 테이블 하단에 배치하기

`caption-bottom` 유틸리티를 사용해 캡션 요소를 테이블의 하단에 배치하세요:

표 3.1: 프로레슬러와 그들의 시그니처 기술.
레슬러| 시그니처 기술
---|---
"Stone Cold" Steve Austin| Stone Cold Stunner, Lou Thesz Press
Bret "The Hitman" Hart| The Sharpshooter
Razor Ramon| Razor's Edge, Fallaway Slam

```
    <table>  <caption class="caption-bottom">    Table 3.1: Professional wrestlers and their signature moves.  </caption>  <thead>    <tr>      <th>Wrestler</th>      <th>Signature Move(s)</th>    </tr>  </thead>  <tbody>    <tr>      <td>"Stone Cold" Steve Austin</td>      <td>Stone Cold Stunner, Lou Thesz Press</td>    </tr>    <tr>      <td>Bret "The Hitman" Hart</td>      <td>The Sharpshooter</td>    </tr>    <tr>      <td>Razor Ramon</td>      <td>Razor's Edge, Fallaway Slam</td>    </tr>  </tbody></table>
```

- 반응형 디자인

`caption-side` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면, 중간 화면 크기 이상에서만 해당 유틸리티가 적용됩니다:

```
    <caption class="caption-top md:caption-bottom ...">  <!-- ... --></caption>
```

변형 사용법은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.
