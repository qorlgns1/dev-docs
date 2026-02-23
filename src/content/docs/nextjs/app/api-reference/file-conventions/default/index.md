---
title: '파일 시스템 규칙: default.js'
description: '파일은 Next.js가 전체 페이지 로드 후 슬롯의 활성 상태를 복구하지 못할 때 병렬 라우트 내에서 폴백을 렌더링하는 데 사용됩니다.'
---

# 파일 시스템 규칙: default.js | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/file-conventions/default

# default.js

마지막 업데이트 2026년 2월 20일

`default.js` 파일은 Next.js가 전체 페이지 로드 후 [슬롯](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#slots)의 활성 상태를 복구하지 못할 때 [병렬 라우트](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes) 내에서 폴백을 렌더링하는 데 사용됩니다.

[소프트 내비게이션](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) 동안에는 Next.js가 각 슬롯의 활성 _상태_ (하위 페이지)를 추적합니다. 그러나 하드 내비게이션(전체 페이지 로드)의 경우 Next.js는 활성 상태를 복구할 수 없습니다. 이때 현재 URL과 일치하지 않는 하위 페이지에 대해 `default.js` 파일을 렌더링할 수 있습니다.

다음 폴더 구조를 고려하세요. `@team` 슬롯에는 `settings` 페이지가 있지만 `@analytics`에는 없습니다.

`/settings`로 이동하면 `@team` 슬롯은 현재 활성 페이지를 유지하면서 `@analytics` 슬롯에 대해 `settings` 페이지를 렌더링합니다.

새로 고침 시 Next.js는 `@analytics`에 대해 `default.js`를 렌더링합니다. `default.js`가 없으면 명명된 슬롯(`@team`, `@analytics` 등)에 대해 오류가 반환되며 계속하려면 `default.js`를 정의해야 합니다. 이러한 상황에서 404를 반환하는 기존 동작을 유지하려면 다음을 포함하는 `default.js`를 만들 수 있습니다.

app/@team/default.js
[code]
    import { notFound } from 'next/navigation'

    export default function Default() {
      notFound()
    }
[/code]

또한 `children`은 암시적 슬롯이므로 Next.js가 상위 페이지의 활성 상태를 복구할 수 없을 때 `children`에 대한 폴백을 렌더링할 `default.js` 파일도 만들어야 합니다. `children` 슬롯에 대한 `default.js`를 만들지 않으면 해당 경로에 대해 404 페이지가 반환됩니다.

## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/default#reference)

### `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/default#params-optional)

루트 세그먼트부터 슬롯의 하위 페이지까지의 [동적 라우트 매개변수](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)를 포함하는 객체로 해소되는 프라미스입니다. 예:

app/[artist]/@sidebar/default.js

JavaScriptTypeScript
[code]
    export default async function Default({
      params,
    }: {
      params: Promise<{ artist: string }>
    }) {
      const { artist } = await params
    }
[/code]

예시| URL| `params`
---|---|---
`app/[artist]/@sidebar/default.js`| `/zack`| `Promise<{ artist: 'zack' }>`
`app/[artist]/[album]/@sidebar/default.js`| `/zack/next`| `Promise<{ artist: 'zack', album: 'next' }>`

  * `params` prop은 프라미스이므로 값을 사용하려면 `async/await` 또는 React의 [`use`](https://react.dev/reference/react/use) 함수를 사용해야 합니다.
    * 버전 14 및 이전에서는 `params`가 동기 prop이었습니다. 하위 호환성을 위해 Next.js 15에서도 동기적으로 접근할 수 있지만, 이 동작은 미래에 더 이상 지원되지 않을 예정입니다.

## 병렬 라우트 더 알아보기

- [Parallel Routes동일한 뷰에서 하나 이상의 페이지를 동시에 렌더링하고 독립적으로 탐색할 수 있게 하는 패턴으로, 매우 동적인 애플리케이션에 적합합니다.](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)

지원됩니다.
