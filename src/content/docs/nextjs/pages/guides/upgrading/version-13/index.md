---
title: '업그레이드: 버전 13'
description: '선호하는 패키지 매니저에서 다음 명령을 실행해 Next.js 13 버전으로 업데이트하세요:'
---

# 업그레이드: 버전 13 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/upgrading/version-13

[가이드](https://nextjs.org/docs/pages/guides)[업그레이드](https://nextjs.org/docs/pages/guides/upgrading)버전 13

# 버전 13으로 업그레이드하는 방법

최근 업데이트 2026년 2월 20일

## 12에서 13으로 업그레이드[](https://nextjs.org/docs/pages/guides/upgrading/version-13#upgrading-from-12-to-13)

선호하는 패키지 매니저에서 다음 명령을 실행해 Next.js 13 버전으로 업데이트하세요:

터미널
```
    npm i next@13 react@latest react-dom@latest eslint-config-next@13
```

터미널
```
    yarn add next@13 react@latest react-dom@latest eslint-config-next@13
```

터미널
```
    pnpm i next@13 react@latest react-dom@latest eslint-config-next@13
```

터미널
```
    bun add next@13 react@latest react-dom@latest eslint-config-next@13
```

> **참고:** TypeScript를 사용 중이라면 `@types/react`와 `@types/react-dom`도 최신 버전으로 업그레이드하세요.

### v13 요약[](https://nextjs.org/docs/pages/guides/upgrading/version-13#v13-summary)

  * [지원 브라우저](https://nextjs.org/docs/architecture/supported-browsers)가 Internet Explorer를 제외하고 최신 브라우저를 대상으로 하도록 변경되었습니다.
  * 최소 Node.js 버전이 12.22.0에서 16.14.0으로 상향되었습니다. 이는 12.x와 14.x가 지원 종료(EOL)에 도달했기 때문입니다.
  * 최소 React 버전이 17.0.2에서 18.2.0으로 상향되었습니다.
  * `swcMinify` 설정 속성의 기본값이 `false`에서 `true`로 변경되었습니다. 자세한 내용은 [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)를 참고하세요.
  * `next/image` 임포트가 `next/legacy/image`로 이름이 변경되었습니다. `next/future/image` 임포트는 `next/image`로 변경되었습니다. 임포트를 안전하게 자동으로 바꾸는 [코드모드가 제공](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-image-to-legacy-image)됩니다.
  * `next/link` 자식으로 더 이상 `<a>`를 사용할 수 없습니다. 레거시 동작이 필요하면 `legacyBehavior` 프롭을 추가하거나 `<a>`를 제거해 업그레이드하세요. 코드를 자동으로 업그레이드하는 [코드모드](https://nextjs.org/docs/pages/guides/upgrading/codemods#new-link)가 제공됩니다.
  * `target` 설정 속성이 제거되었으며 [Output File Tracing](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output)이 이를 대체합니다.

## 공유 기능 마이그레이션[](https://nextjs.org/docs/pages/guides/upgrading/version-13#migrating-shared-features)

Next.js 13은 새로운 [`app` 디렉터리](https://nextjs.org/docs/app)를 도입하며 새로운 기능과 규칙을 제공합니다. 그러나 Next.js 13으로 업그레이드한다고 해서 새로운 `app` 라우터를 반드시 사용해야 하는 것은 아닙니다.

업데이트된 [Image 컴포넌트](https://nextjs.org/docs/pages/guides/upgrading/version-13#image-component), [Link 컴포넌트](https://nextjs.org/docs/pages/guides/upgrading/version-13#link-component), [Script 컴포넌트](https://nextjs.org/docs/pages/guides/upgrading/version-13#script-component), [글꼴 최적화](https://nextjs.org/docs/pages/guides/upgrading/version-13#font-optimization) 등 두 디렉터리에서 모두 작동하는 새로운 기능과 함께 `pages`를 계속 사용할 수 있습니다.

### `<Image/>` 컴포넌트[](https://nextjs.org/docs/pages/guides/upgrading/version-13#image-component)

Next.js 12는 임시 임포트인 `next/future/image`를 통해 Image 컴포넌트에 많은 개선 사항을 도입했습니다. 여기에는 클라이언트 측 JavaScript 감소, 이미지 확장 및 스타일링을 쉽게 하는 방법, 향상된 접근성, 브라우저 기본 지연 로딩이 포함되었습니다.

Next.js 13부터는 이러한 새 동작이 `next/image`의 기본값이 됩니다.

새 Image 컴포넌트로 마이그레이션을 돕는 두 가지 코드모드가 있습니다:

  * [next-image-to-legacy-image](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-image-to-legacy-image): 이 코드모드는 `next/image` 임포트를 `next/legacy/image`로 안전하게 자동 이름 변경하여 Next.js 12와 동일한 동작을 유지합니다. Next.js 13으로 빠르게 자동 업데이트하려면 이 코드모드를 실행하는 것이 좋습니다.
  * [next-image-experimental](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-image-experimental): 이전 코드모드를 실행한 후 선택적으로 이 실험적 코드모드를 실행해 `next/legacy/image`를 새로운 `next/image`로 업그레이드할 수 있습니다. 이 작업은 사용되지 않는 프롭을 제거하고 인라인 스타일을 추가합니다. 이 코드모드는 실험적이며 `<Image src={img} layout="responsive" />` 같은 정적 사용만 다루고 `<Image {...props} />` 같은 동적 사용은 다루지 않는다는 점에 유의하세요.

또는 [마이그레이션 가이드](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-image-experimental)를 따라 수동으로 업데이트하고, [레거시 비교](https://nextjs.org/docs/pages/api-reference/components/image-legacy#comparison)도 확인할 수 있습니다.

### `<Link>` 컴포넌트[](https://nextjs.org/docs/pages/guides/upgrading/version-13#link-component)

[`<Link>` 컴포넌트](https://nextjs.org/docs/pages/api-reference/components/link)는 더 이상 자식으로 `<a>` 태그를 수동으로 추가할 필요가 없습니다. 이 동작은 [버전 12.2](https://nextjs.org/blog/next-12-2)에서 실험적 옵션으로 도입되었고 이제 기본값입니다. Next.js 13에서는 `<Link>`가 항상 `<a>`를 렌더링하며 기본 태그에 프롭을 전달할 수 있습니다.

예시:
```
    import Link from 'next/link'

    // Next.js 12: `<a>`를 중첩하지 않으면 제외됩니다
    <Link href="/about">
      <a>About</a>
    </Link>

    // Next.js 13: `<Link>`는 내부적으로 항상 `<a>`를 렌더링합니다
    <Link href="/about">
      About
    </Link>
```

링크를 Next.js 13에 맞게 업그레이드하려면 [`new-link` 코드모드](https://nextjs.org/docs/pages/guides/upgrading/codemods#new-link)를 사용할 수 있습니다.

### `<Script>` 컴포넌트[](https://nextjs.org/docs/pages/guides/upgrading/version-13#script-component)

[`next/script`](https://nextjs.org/docs/pages/api-reference/components/script)의 동작이 `pages`와 `app` 모두를 지원하도록 업데이트되었습니다. `app`을 점진적으로 도입하는 경우 [업그레이드 가이드](https://nextjs.org/docs/pages/guides/upgrading)를 참고하세요.

### 글꼴 최적화[](https://nextjs.org/docs/pages/guides/upgrading/version-13#font-optimization)

기존에는 Next.js가 글꼴 CSS를 인라인으로 삽입해 글꼴을 최적화했습니다. 버전 13에서는 새로운 [`next/font`](https://nextjs.org/docs/pages/api-reference/components/font) 모듈을 도입하여 뛰어난 성능과 프라이버시를 유지하면서 글꼴 로딩 경험을 원하는 대로 구성할 수 있습니다.

`next/font` 사용 방법은 [글꼴 최적화](https://nextjs.org/docs/pages/api-reference/components/font)를 참고하세요.