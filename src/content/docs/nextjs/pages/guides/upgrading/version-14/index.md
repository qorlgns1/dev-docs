---
title: '업그레이드: 버전 14'
description: '선호하는 패키지 관리자를 사용해 Next.js 버전 14로 업데이트하려면 다음 명령을 실행하세요.'
---

# 업그레이드: 버전 14 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/upgrading/version-14

[Guides](https://nextjs.org/docs/pages/guides)[Upgrading](https://nextjs.org/docs/pages/guides/upgrading)Version 14

Copy page

# 버전 14로 업그레이드하는 방법

마지막 업데이트 2026년 2월 20일

## 13에서 14로 업그레이드[](https://nextjs.org/docs/pages/guides/upgrading/version-14#upgrading-from-13-to-14)

선호하는 패키지 관리자를 사용해 Next.js 버전 14로 업데이트하려면 다음 명령을 실행하세요.

Terminal
```
    npm i next@next-14 react@18 react-dom@18 && npm i eslint-config-next@next-14 -D
```

Terminal
```
    yarn add next@next-14 react@18 react-dom@18 && yarn add eslint-config-next@next-14 -D
```

Terminal
```
    pnpm i next@next-14 react@18 react-dom@18 && pnpm i eslint-config-next@next-14 -D
```

Terminal
```
    bun add next@next-14 react@18 react-dom@18 && bun add eslint-config-next@next-14 -D
```

> **알아두면 좋아요:** TypeScript를 사용 중이라면 `@types/react`와 `@types/react-dom`도 최신 버전으로 업그레이드하세요.

### v14 요약[](https://nextjs.org/docs/pages/guides/upgrading/version-14#v14-summary)

  * Node.js 최소 버전이 16.14에서 18.17로 올라갔습니다. 16.x는 지원 종료(EOL)에 도달했기 때문입니다.
  * `next export` 명령이 제거되고 `output: 'export'` 설정으로 대체되었습니다. 자세한 내용은 [문서](https://nextjs.org/docs/app/guides/static-exports)를 확인하세요.
  * `ImageResponse`를 위한 `next/server` 임포트가 `next/og`로 이름이 변경되었습니다. 임포트를 안전하게 자동으로 바꾸는 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#next-og-import)가 제공됩니다.
  * 내장된 `next/font`를 사용하도록 `@next/font` 패키지가 완전히 제거되었습니다. 임포트를 안전하게 자동으로 바꾸는 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#built-in-next-font)가 제공됩니다.
  * `next-swc`의 WASM 타깃이 제거되었습니다.

Was this helpful?

supported.

Send