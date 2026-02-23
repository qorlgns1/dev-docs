---
title: '업그레이드: 버전 14'
description: '선호하는 패키지 관리자를 사용해 아래 명령어를 실행하면 Next.js 14 버전으로 업데이트할 수 있습니다.'
---

# 업그레이드: 버전 14 | Next.js

Source URL: https://nextjs.org/docs/app/guides/upgrading/version-14

[가이드](https://nextjs.org/docs/app/guides)[업그레이드](https://nextjs.org/docs/app/guides/upgrading)버전 14

# 버전 14로 업그레이드하는 방법

최종 업데이트 2026년 2월 20일

## 13에서 14로 업그레이드[](https://nextjs.org/docs/app/guides/upgrading/version-14#upgrading-from-13-to-14)

선호하는 패키지 관리자를 사용해 아래 명령어를 실행하면 Next.js 14 버전으로 업데이트할 수 있습니다.

터미널
```
    npm i next@next-14 react@18 react-dom@18 && npm i eslint-config-next@next-14 -D
```

터미널
```
    yarn add next@next-14 react@18 react-dom@18 && yarn add eslint-config-next@next-14 -D
```

터미널
```
    pnpm i next@next-14 react@18 react-dom@18 && pnpm i eslint-config-next@next-14 -D
```

터미널
```
    bun add next@next-14 react@18 react-dom@18 && bun add eslint-config-next@next-14 -D
```

> **알아두면 좋아요:** TypeScript를 사용 중이라면 `@types/react`와 `@types/react-dom`도 최신 버전으로 함께 업그레이드하세요.

### v14 요약[](https://nextjs.org/docs/app/guides/upgrading/version-14#v14-summary)

  * Node.js 최소 버전이 16.14에서 18.17로 상향되었습니다. 16.x는 수명이 종료되었습니다.
  * `next export` 명령은 `output: 'export'` 설정으로 교체되어 제거되었습니다. 자세한 내용은 [문서](https://nextjs.org/docs/app/guides/static-exports)를 확인하세요.
  * `ImageResponse`를 위한 `next/server` 임포트가 `next/og`로 이름이 바뀌었습니다. 임포트를 안전하게 자동 변경할 수 있도록 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#next-og-import)가 제공됩니다.
  * 내장 `next/font`를 사용하도록 `@next/font` 패키지가 완전히 제거되었습니다. 임포트를 안전하게 자동 변경할 수 있도록 [코드모드](https://nextjs.org/docs/app/guides/upgrading/codemods#built-in-next-font)가 제공됩니다.
  * `next-swc`의 WASM 타깃이 제거되었습니다.

보내기