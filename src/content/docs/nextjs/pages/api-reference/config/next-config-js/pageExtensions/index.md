---
title: 'next.config.js 옵션: pageExtensions'
description: '마지막 업데이트 2026년 2월 20일'
---

# next.config.js 옵션: pageExtensions | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)pageExtensions

페이지 복사

# pageExtensions

마지막 업데이트 2026년 2월 20일

Next.js가 사용하는 기본 페이지 확장자(`.tsx`, `.ts`, `.jsx`, `.js`)를 확장할 수 있습니다. `next.config.js` 안에 `pageExtensions` 구성을 추가하세요:

next.config.js
[code]
    module.exports = {
      pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
    }
[/code]

이 값을 변경하면 다음을 포함한 모든 Next.js 페이지에 영향을 줍니다.

  * [`proxy.js`](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)
  * [`instrumentation.js`](https://nextjs.org/docs/pages/guides/instrumentation)
  * `pages/_document.js`
  * `pages/_app.js`
  * `pages/api/`



예를 들어 `.ts` 페이지 확장자를 `.page.ts`로 재구성하면 `proxy.page.ts`, `instrumentation.page.ts`, `_app.page.ts`처럼 페이지 이름을 변경해야 합니다.

## `pages` 디렉터리에 페이지가 아닌 파일 포함하기[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions#including-non-page-files-in-the-pages-directory)

`pages` 디렉터리 안에 테스트 파일이나 컴포넌트에서 사용하는 다른 파일을 함께 둘 수 있습니다. `next.config.js` 안에 `pageExtensions` 구성을 추가하세요:

next.config.js
[code]
    module.exports = {
      pageExtensions: ['page.tsx', 'page.ts', 'page.jsx', 'page.js'],
    }
[/code]

그런 다음 페이지 파일 이름에 `.page`가 포함되도록 확장자를 바꾸세요(예: `MyPage.tsx`를 `MyPage.page.tsx`로 변경). 앞서 언급한 파일을 포함해 _모든_ Next.js 페이지의 이름을 변경했는지 확인하세요.

도움이 되었나요?

지원됨.

전송
