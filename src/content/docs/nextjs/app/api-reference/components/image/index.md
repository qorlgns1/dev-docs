---
title: '컴포넌트: Image 컴포넌트'
description: '마지막 업데이트: 2026년 2월 20일'
---

# 컴포넌트: Image 컴포넌트 | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/components/image

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[컴포넌트](https://nextjs.org/docs/app/api-reference/components)Image 컴포넌트

페이지 복사

# Image 컴포넌트

마지막 업데이트: 2026년 2월 20일

Next.js Image 컴포넌트는 자동 이미지 최적화를 위해 HTML `<img>` 요소를 확장합니다.

app/page.js
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return (
        <Image
          src="/profile.png"
          width={500}
          height={500}
          alt="Picture of the author"
        />
      )
    }
[/code]

## 참고 자료[](https://nextjs.org/docs/app/api-reference/components/image#reference)

### 속성[](https://nextjs.org/docs/app/api-reference/components/image#props)

다음 속성을 사용할 수 있습니다:

속성| 예시| 타입| 상태  
---|---|---|---  
[`src`](https://nextjs.org/docs/app/api-reference/components/image#src)| `src="/profile.png"`| String| 필수  
[`alt`](https://nextjs.org/docs/app/api-reference/components/image#alt)| `alt="Picture of the author"`| String| 필수  
[`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)| `width={500}`| Integer (px)| -  
[`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)| `height={500}`| Integer (px)| -  
[`fill`](https://nextjs.org/docs/app/api-reference/components/image#fill)| `fill={true}`| Boolean| -  
[`loader`](https://nextjs.org/docs/app/api-reference/components/image#loader)| `loader={imageLoader}`| Function| -  
[`sizes`](https://nextjs.org/docs/app/api-reference/components/image#sizes)| `sizes="(max-width: 768px) 100vw, 33vw"`| String| -  
[`quality`](https://nextjs.org/docs/app/api-reference/components/image#quality)| `quality={80}`| Integer (1-100)| -  
[`preload`](https://nextjs.org/docs/app/api-reference/components/image#preload)| `preload={true}`| Boolean| -  
[`placeholder`](https://nextjs.org/docs/app/api-reference/components/image#placeholder)| `placeholder="blur"`| String| -  
[`style`](https://nextjs.org/docs/app/api-reference/components/image#style)| `style={{objectFit: "contain"}}`| Object| -  
[`onLoadingComplete`](https://nextjs.org/docs/app/api-reference/components/image#onloadingcomplete)| `onLoadingComplete={img => done())}`| Function| 사용 중단됨  
[`onLoad`](https://nextjs.org/docs/app/api-reference/components/image#onload)| `onLoad={event => done())}`| Function| -  
[`onError`](https://nextjs.org/docs/app/api-reference/components/image#onerror)| `onError(event => fail()}`| Function| -  
[`loading`](https://nextjs.org/docs/app/api-reference/components/image#loading)| `loading="lazy"`| String| -  
[`blurDataURL`](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl)| `blurDataURL="data:image/jpeg..."`| String| -  
[`unoptimized`](https://nextjs.org/docs/app/api-reference/components/image#unoptimized)| `unoptimized={true}`| Boolean| -  
[`overrideSrc`](https://nextjs.org/docs/app/api-reference/components/image#overridesrc)| `overrideSrc="/seo.png"`| String| -  
[`decoding`](https://nextjs.org/docs/app/api-reference/components/image#decoding)| `decoding="async"`| String| -  
  
#### `src`[](https://nextjs.org/docs/app/api-reference/components/image#src)

이미지의 소스입니다. 다음 중 하나일 수 있습니다:

내부 경로 문자열.
[code] 
    <Image src="/profile.png" />
[/code]

절대 외부 URL(반드시 [remotePatterns](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns)로 구성해야 함).
[code] 
    <Image src="https://example.com/profile.png" />
[/code]

정적 import.
[code] 
    import profile from './profile.png'
     
    export default function Page() {
      return <Image src={profile} />
    }
[/code]

> **알아두면 좋아요** : 보안상의 이유로 기본 [loader](https://nextjs.org/docs/app/api-reference/components/image#loader)를 사용하는 Image Optimization API는 `src` 이미지를 가져올 때 헤더를 전달하지 않습니다. `src` 이미지에 인증이 필요하다면 Image Optimization을 비활성화하기 위해 [unoptimized](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) 속성을 사용하는 것을 고려하세요.

#### `alt`[](https://nextjs.org/docs/app/api-reference/components/image#alt)

`alt` 속성은 스크린 리더와 검색 엔진을 위해 이미지를 설명하는 데 사용되며, 이미지가 비활성화되었거나 로딩 중 오류가 발생했을 때 대체 텍스트로 표시됩니다.

이미지가 [페이지의 의미를 바꾸지 않고](https://html.spec.whatwg.org/multipage/images.html#general-guidelines) 대체할 수 있는 텍스트를 포함해야 합니다. 이미지를 보완하기 위한 것이 아니며, 이미지 상하단 캡션에 이미 제공된 정보를 반복해서는 안 됩니다.

이미지가 [순수하게 장식 목적](https://html.spec.whatwg.org/multipage/images.html#a-purely-decorative-image-that-doesn't-add-any-information)이거나 [사용자에게 노출되지 않는 경우](https://html.spec.whatwg.org/multipage/images.html#an-image-not-intended-for-the-user), `alt` 속성은 빈 문자열(`alt=""`)이어야 합니다.

> [이미지 접근성 가이드라인](https://html.spec.whatwg.org/multipage/images.html#alt)을 더 알아보세요.

#### `width` 및 `height`[](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)

`width`와 `height` 속성은 픽셀 단위의 [고유(intrinsic)](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size) 이미지 크기를 나타냅니다. 이 속성은 브라우저가 이미지를 위한 올바른 **종횡비**를 추론해 로딩 중 레이아웃 시프트를 방지하도록 예약 공간을 확보할 때 사용됩니다. 이미지를 표시하는 실제 크기는 CSS가 제어하며, 이 속성으로 결정되지 않습니다.
[code] 
    <Image src="/profile.png" width={500} height={500} />
[/code]

다음과 같은 경우가 아니라면 `width`와 `height` 속성을 모두 **반드시** 설정해야 합니다:

  * 이미지가 정적으로 import된 경우.
  * 이미지에 [`fill` 속성](https://nextjs.org/docs/app/api-reference/components/image#fill)이 있는 경우.

높이와 너비를 모른다면 [`fill` 속성](https://nextjs.org/docs/app/api-reference/components/image#fill) 사용을 권장합니다.

#### `fill`[](https://nextjs.org/docs/app/api-reference/components/image#fill)

이미지가 부모 요소 크기까지 확장되도록 하는 boolean 값입니다.
[code] 
    <Image src="/profile.png" fill={true} />
[/code]

**위치 지정** :

  * 부모 요소는 반드시 `position: "relative"`, `"fixed"`, `"absolute"`를 지정해야 합니다.
  * 기본적으로 `<img>` 요소는 `position: "absolute"`를 사용합니다.

**오브젝트 핏** :

이미지에 스타일을 적용하지 않으면 컨테이너에 맞게 늘어납니다. 자르기와 스케일링은 `objectFit`으로 제어할 수 있습니다.

  * `"contain"`: 이미지를 컨테이너에 맞게 축소하면서 종횡비를 유지합니다.
  * `"cover"`: 이미지를 컨테이너에 맞게 채우고 넘어가는 부분을 자릅니다.

> [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position)과 [`object-fit`](https://developer.mozilla.org/docs/Web/CSS/object-fit)에 대해 더 알아보세요.

#### `loader`[](https://nextjs.org/docs/app/api-reference/components/image#loader)

이미지 URL을 생성하는 사용자 정의 함수입니다. 함수는 다음 매개변수를 받아 이미지의 URL 문자열을 반환합니다:

  * [`src`](https://nextjs.org/docs/app/api-reference/components/image#src)
  * [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)
  * [`quality`](https://nextjs.org/docs/app/api-reference/components/image#quality)

[code] 
    'use client'
     
    import Image from 'next/image'
     
    const imageLoader = ({ src, width, quality }) => {
      return `https://example.com/${src}?w=${width}&q=${quality || 75}`
    }
     
    export default function Page() {
      return (
        <Image
          loader={imageLoader}
          src="me.png"
          alt="Picture of the author"
          width={500}
          height={500}
        />
      )
    }
[/code]

> **알아두면 좋아요** : 함수를 받는 `onLoad` 같은 속성을 사용하려면 제공한 함수를 직렬화하기 위해 [Client Components](https://react.dev/reference/rsc/use-client)가 필요합니다.

또는 `next.config.js`의 [loaderFile](https://nextjs.org/docs/app/api-reference/components/image#loaderfile) 구성을 사용해 애플리케이션의 모든 `next/image` 인스턴스를 prop 없이 설정할 수 있습니다.

#### `sizes`[](https://nextjs.org/docs/app/api-reference/components/image#sizes)

다양한 브레이크포인트에서 이미지 크기를 정의합니다. 브라우저가 생성된 `srcset`에서 가장 적합한 크기를 선택할 때 사용됩니다.
[code] 
    import Image from 'next/image'
     
    export default function Page() {
      return (
        <div className="grid-element">
          <Image
            fill
            src="/example.png"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          />
        </div>
      )
    }
[/code]

`sizes`는 다음과 같을 때 사용해야 합니다:

  * 이미지가 [`fill`](https://nextjs.org/docs/app/api-reference/components/image#fill) 속성을 사용하는 경우
  * CSS로 이미지를 반응형으로 만드는 경우

`sizes`가 없으면 브라우저는 이미지가 뷰포트만큼 넓게(`100vw`) 표시된다고 가정합니다. 이로 인해 불필요하게 큰 이미지를 다운로드할 수 있습니다.

또한 `sizes`는 `srcset` 생성 방식에 영향을 줍니다:

  * `sizes`가 없으면: Next.js는 고정 크기 이미지에 적합한 제한된 `srcset`(예: 1x, 2x)을 생성합니다.
  * `sizes`가 있으면: Next.js는 반응형 레이아웃에 최적화된 전체 `srcset`(예: 640w, 750w 등)을 생성합니다.

> `srcset`과 `sizes`에 대해 [web.dev](https://web.dev/learn/design/responsive-images/#sizes)와 [mdn](https://developer.mozilla.org/docs/Web/HTML/Element/img#sizes)에서 더 알아보세요.

#### `quality`[](https://nextjs.org/docs/app/api-reference/components/image#quality)

최적화된 이미지의 품질을 설정하는 `1`~`100` 사이의 정수입니다. 값이 높을수록 파일 크기와 시각적 선명도가 증가하고, 낮을수록 파일 크기가 줄지만 선명도가 떨어질 수 있습니다.
[code] 
    // Default quality is 75
    <Image quality={75} />
[/code]

`next.config.js`에서 [qualities](https://nextjs.org/docs/app/api-reference/components/image#qualities)를 구성했다면, 해당 값은 허용된 항목 중 하나와 일치해야 합니다.

> **알아두면 좋아요** : 원본 이미지 품질이 이미 낮다면 높은 quality 값을 설정해도 외형은 개선되지 않고 파일 크기만 증가합니다.

#### `style`[](https://nextjs.org/docs/app/api-reference/components/image#style)

기본 이미지 요소에 CSS 스타일을 전달할 수 있습니다.
[code] 
    const imageStyle = {
      borderRadius: '50%',
      border: '1px solid #fff',
      width: '100px',
      height: 'auto',
    }
     
    export default function ProfileImage() {
      return <Image src="..." style={imageStyle} />
    }
[/code]

> **알아두면 좋아요** : `style` 속성으로 사용자 정의 너비를 설정하는 경우, 이미지 종횡비를 유지하려면 반드시 `height: 'auto'`도 설정하세요.

#### `preload`[](https://nextjs.org/docs/app/api-reference/components/image#preload)

이미지를 프리로드해야 하는지 여부를 나타내는 boolean 값입니다.
[code] 
    // Default preload is false
    <Image preload={false} />
[/code]

  * `true`: `<head>`에 `<link>`를 삽입해 이미지를 [프리로드](https://web.dev/preload-responsive-images/)합니다.
  * `false`: 이미지를 프리로드하지 않습니다.

**사용 시점:**

  * 이미지가 [Largest Contentful Paint(LCP)](https://nextjs.org/learn/seo/web-performance/lcp) 요소인 경우.
  * 이미지가 퍼스트 뷰(보이는 영역) 내에 있는 경우, 일반적으로 히어로 이미지.
  * `<body>`에서 나중에 발견되기 전에 `<head>`에서 이미지 로딩을 시작하고 싶은 경우.

**사용하지 말아야 할 시점:**

  * 뷰포트에 따라 [Largest Contentful Paint(LCP)](https://nextjs.org/learn/seo/web-performance/lcp) 요소가 될 수 있는 이미지가 여러 개일 때.
  * `loading` 속성을 사용하는 경우.
  * `fetchPriority` 속성을 사용하는 경우.

대부분의 경우 `preload` 대신 `loading="eager"` 또는 `fetchPriority="high"`를 사용해야 합니다.

#### `priority`[](https://nextjs.org/docs/app/api-reference/components/image#priority)

Next.js 16부터 동작을 명확히 하기 위해 `priority` 속성은 [`preload`](https://nextjs.org/docs/app/api-reference/components/image#preload) 속성으로 대체되어 더 이상 권장되지 않습니다.

#### `loading`[](https://nextjs.org/docs/app/api-reference/components/image#loading)

이미지가 로드를 시작할 시점을 제어합니다.
[code] 
    // Defaults to lazy
    <Image loading="lazy" />
[/code]

  * `lazy`: 이미지가 뷰포트에서 계산된 거리까지 도달할 때까지 로드를 지연합니다.
  * `eager`: 페이지에서의 위치와 상관없이 이미지를 즉시 로드합니다.



즉시 로드를 보장하고 싶은 경우에만 `eager`를 사용하세요.

> [`loading` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#loading)에 대해 더 알아보기.

#### `placeholder`[](https://nextjs.org/docs/app/api-reference/components/image#placeholder)

이미지가 로드되는 동안 사용할 플레이스홀더를 지정하여 체감 로딩 성능을 개선합니다.
[code] 
    // defaults to empty
    <Image placeholder="empty" />
[/code]

  * `empty`: 이미지가 로드되는 동안 플레이스홀더가 없습니다.
  * `blur`: 흐릿한 버전의 이미지를 플레이스홀더로 사용합니다. [`blurDataURL`](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl) 속성과 함께 사용해야 합니다.
  * `data:image/...`: [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)을 플레이스홀더로 사용합니다.



**예시:**

  * [`blur` placeholder](https://image-component.nextjs.gallery/placeholder)
  * [Data URL `placeholder` prop으로 구현한 Shimmer 효과](https://image-component.nextjs.gallery/shimmer)
  * [`blurDataURL` prop으로 구현한 Color 효과](https://image-component.nextjs.gallery/color)



> [`placeholder` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#placeholder)에 대해 더 알아보기.

#### `blurDataURL`[](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl)

이미지가 정상적으로 로드되기 전에 플레이스홀더 이미지로 사용할 [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)입니다. 자동으로 설정되거나 [`placeholder="blur"`](https://nextjs.org/docs/app/api-reference/components/image#placeholder) 속성과 함께 사용할 수 있습니다.
[code] 
    <Image placeholder="blur" blurDataURL="..." />
[/code]

이미지는 자동으로 확장되고 블러 처리되므로 10px 이하의 매우 작은 이미지를 권장합니다.

**자동**

`src`가 `jpg`, `png`, `webp`, `avif` 파일의 정적 import라면 이미지가 애니메이션이 아닌 한 `blurDataURL`이 자동으로 추가됩니다.

**수동 설정**

이미지가 동적이거나 원격이라면 직접 `blurDataURL`을 제공해야 합니다. 생성 방법 예시는 다음과 같습니다.

  * [png-pixel.com 같은 온라인 도구](https://png-pixel.com)
  * [Plaiceholder 같은 라이브러리](https://github.com/joe-bell/plaiceholder)



큰 blurDataURL은 성능을 저하시킬 수 있습니다. 작고 단순하게 유지하세요.

**예시:**

  * [기본 `blurDataURL` prop](https://image-component.nextjs.gallery/placeholder)
  * [`blurDataURL` prop으로 구현한 Color 효과](https://image-component.nextjs.gallery/color)



#### `onLoad`[](https://nextjs.org/docs/app/api-reference/components/image#onload)

이미지가 완전히 로드되어 [placeholder](https://nextjs.org/docs/app/api-reference/components/image#placeholder)가 제거되면 호출되는 콜백 함수입니다.
[code] 
    <Image onLoad={(e) => console.log(e.target.naturalWidth)} />
[/code]

콜백 함수는 `target`이 기본 `<img>` 요소를 가리키는 이벤트 하나를 인수로 받습니다.

> **알아두면 좋아요**: `onLoad`처럼 함수를 받는 prop을 사용하려면 제공된 함수를 직렬화하기 위해 [Client Components](https://react.dev/reference/rsc/use-client)를 사용해야 합니다.

#### `onError`[](https://nextjs.org/docs/app/api-reference/components/image#onerror)

이미지 로드에 실패하면 호출되는 콜백 함수입니다.
[code] 
    <Image onError={(e) => console.error(e.target.id)} />
[/code]

> **알아두면 좋아요**: `onError`처럼 함수를 받는 prop을 사용하려면 제공된 함수를 직렬화하기 위해 [Client Components](https://react.dev/reference/rsc/use-client)를 사용해야 합니다.

#### `unoptimized`[](https://nextjs.org/docs/app/api-reference/components/image#unoptimized)

이미지를 최적화할지 여부를 나타내는 불리언입니다. 1KB 미만의 작은 이미지, SVG 같은 벡터 이미지, GIF 같은 애니메이션 이미지처럼 최적화가 필요 없는 경우에 유용합니다.
[code] 
    import Image from 'next/image'
     
    const UnoptimizedImage = (props) => {
      // Default is false
      return <Image {...props} unoptimized />
    }
[/code]

  * `true`: 품질, 크기, 포맷을 변경하지 않고 `src`에서 원본 이미지를 그대로 제공합니다.
  * `false`: 원본 이미지를 최적화합니다.



Next.js 12.3.0부터 다음 구성으로 `next.config.js`를 업데이트하면 모든 이미지에 이 prop을 적용할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        unoptimized: true,
      },
    }
[/code]

#### `overrideSrc`[](https://nextjs.org/docs/app/api-reference/components/image#overridesrc)

`<Image>` 컴포넌트에 `src` prop을 제공하면 결과 `<img>`에 대해 `srcset`과 `src` 속성이 자동 생성됩니다.

input.js
[code]
    <Image src="/profile.jpg" />
[/code]

output.html
[code]
    <img
      srcset="
        /_next/image?url=%2Fprofile.jpg&w=640&q=75 1x,
        /_next/image?url=%2Fprofile.jpg&w=828&q=75 2x
      "
      src="/_next/image?url=%2Fprofile.jpg&w=828&q=75"
    />
[/code]

경우에 따라 `src` 속성이 자동 생성되는 것이 바람직하지 않을 수 있으며 `overrideSrc` prop을 사용해 이를 덮어쓰길 원할 수 있습니다.

예를 들어 기존 웹사이트를 `<img>`에서 `<Image>`로 마이그레이션할 때, 이미지 순위나 재크롤 방지 같은 SEO 목적으로 동일한 `src` 속성을 유지하고 싶을 수 있습니다.

input.js
[code]
    <Image src="/profile.jpg" overrideSrc="/override.jpg" />
[/code]

output.html
[code]
    <img
      srcset="
        /_next/image?url=%2Fprofile.jpg&w=640&q=75 1x,
        /_next/image?url=%2Fprofile.jpg&w=828&q=75 2x
      "
      src="/override.jpg"
    />
[/code]

#### `decoding`[](https://nextjs.org/docs/app/api-reference/components/image#decoding)

다른 콘텐츠 업데이트를 표시하기 전에 이미지가 디코딩될 때까지 기다릴지 여부를 브라우저에 알려주는 힌트입니다.
[code] 
    // Default is async
    <Image decoding="async" />
[/code]

  * `async`: 이미지를 비동기적으로 디코딩하고 완료되기 전에 다른 콘텐츠를 렌더링할 수 있도록 합니다.
  * `sync`: 다른 콘텐츠와 동시에 표시되도록 이미지를 동기적으로 디코딩합니다.
  * `auto`: 선호 없음. 브라우저가 최적의 방식을 선택합니다.



> [`decoding` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#decoding)에 대해 더 알아보기.

### Other Props[](https://nextjs.org/docs/app/api-reference/components/image#other-props)

다음 예외를 제외한 `<Image />` 컴포넌트의 다른 속성들은 기본 `img` 요소에 전달됩니다.

  * `srcSet`: [Device Sizes](https://nextjs.org/docs/app/api-reference/components/image#devicesizes)를 대신 사용하세요.



### Deprecated props[](https://nextjs.org/docs/app/api-reference/components/image#deprecated-props)

#### `onLoadingComplete`[](https://nextjs.org/docs/app/api-reference/components/image#onloadingcomplete)

> **경고**: Next.js 14에서 더 이상 사용되지 않습니다. 대신 [`onLoad`](https://nextjs.org/docs/app/api-reference/components/image#onload)를 사용하세요.

이미지가 완전히 로드되어 [placeholder](https://nextjs.org/docs/app/api-reference/components/image#placeholder)가 제거되면 호출되는 콜백 함수입니다.

콜백 함수는 기본 `<img>` 요소에 대한 참조 하나를 인수로 받습니다.
[code] 
    'use client'
     
    <Image onLoadingComplete={(img) => console.log(img.naturalWidth)} />
[/code]

> **알아두면 좋아요**: `onLoadingComplete`처럼 함수를 받는 prop을 사용하려면 제공된 함수를 직렬화하기 위해 [Client Components](https://react.dev/reference/rsc/use-client)를 사용해야 합니다.

### Configuration options[](https://nextjs.org/docs/app/api-reference/components/image#configuration-options)

`next.config.js`에서 Image 컴포넌트를 구성할 수 있습니다. 사용 가능한 옵션은 다음과 같습니다.

#### `localPatterns`[](https://nextjs.org/docs/app/api-reference/components/image#localpatterns)

특정 로컬 경로의 이미지만 최적화하고 나머지는 차단하려면 `next.config.js` 파일에서 `localPatterns`를 사용하세요.

next.config.js
[code]
    module.exports = {
      images: {
        localPatterns: [
          {
            pathname: '/assets/images/**',
            search: '',
          },
        ],
      },
    }
[/code]

위 예시는 `next/image`의 `src` 속성이 `/assets/images/`로 시작해야 하며 쿼리 문자열이 없어야 함을 보장합니다. 다른 경로를 최적화하려면 `400` Bad Request 오류가 발생합니다.

> **알아두면 좋아요**: `search` 속성을 생략하면 모든 검색 매개변수가 허용되어 악의적인 사용자가 의도하지 않은 URL을 최적화할 수 있습니다. 정확한 일치를 보장하려면 `search: '?v=2'`처럼 구체적인 값을 사용하는 것이 좋습니다.

#### `remotePatterns`[](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns)

특정 외부 경로의 이미지만 허용하고 나머지를 차단하려면 `next.config.js` 파일에서 `remotePatterns`를 사용하세요. 이렇게 하면 계정의 외부 이미지만 제공됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        remotePatterns: [new URL('https://example.com/account123/**')],
      },
    }
[/code]

아래와 같이 객체를 사용해 `remotePatterns`를 구성할 수도 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        remotePatterns: [
          {
            protocol: 'https',
            hostname: 'example.com',
            port: '',
            pathname: '/account123/**',
            search: '',
          },
        ],
      },
    }
[/code]

위 예시는 `next/image`의 `src` 속성이 `https://example.com/account123/`로 시작해야 하며 쿼리 문자열이 없어야 함을 보장합니다. 다른 프로토콜, 호스트명, 포트 또는 일치하지 않는 경로는 `400` Bad Request를 반환합니다.

**와일드카드 패턴:**

와일드카드 패턴은 `pathname`과 `hostname` 모두에 사용할 수 있으며 다음 구문을 가집니다.

  * `*`는 단일 경로 세그먼트 또는 서브도메인을 매칭합니다.
  * `**`는 끝부분의 경로 세그먼트 여러 개나 시작 부분의 서브도메인 여러 개를 매칭합니다. 패턴 중간에서는 작동하지 않습니다.



next.config.js
[code]
    module.exports = {
      images: {
        remotePatterns: [
          {
            protocol: 'https',
            hostname: '**.example.com',
            port: '',
            search: '',
          },
        ],
      },
    }
[/code]

이 설정은 `image.example.com` 같은 서브도메인을 허용합니다. 쿼리 문자열과 커스텀 포트는 여전히 차단됩니다.

> **알아두면 좋아요**: `protocol`, `port`, `pathname`, `search`를 생략하면 와일드카드 `**`가 암시됩니다. 이는 의도하지 않은 URL을 악의적인 사용자가 최적화할 수 있으므로 권장되지 않습니다.

**쿼리 문자열**:

`search` 속성을 사용해 쿼리 문자열도 제한할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        remotePatterns: [
          {
            protocol: 'https',
            hostname: 'assets.example.com',
            search: '?v=1727111025337',
          },
        ],
      },
    }
[/code]

위 예시는 `next/image`의 `src` 속성이 `https://assets.example.com`으로 시작해야 하며 정확히 `?v=1727111025337` 쿼리 문자열을 가져야 함을 보장합니다. 다른 프로토콜이나 쿼리 문자열은 `400` Bad Request를 반환합니다.

#### `loaderFile`[](https://nextjs.org/docs/app/api-reference/components/image#loaderfile)

`loaderFiles`를 사용하면 Next.js 대신 커스텀 이미지 최적화 서비스를 사용할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        loader: 'custom',
        loaderFile: './my/image/loader.js',
      },
    }
[/code]

경로는 프로젝트 루트 기준의 상대 경로여야 합니다. 해당 파일은 URL 문자열을 반환하는 기본 함수를 export해야 합니다.

my/image/loader.js
[code]
    'use client'
     
    export default function myImageLoader({ src, width, quality }) {
      return `https://example.com/${src}?w=${width}&q=${quality || 75}`
    }
[/code]

**예시:**

  * [Custom Image Loader Configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#example-loader-configuration)



> 대안으로, 각 `next/image` 인스턴스를 구성하려면 [`loader` prop](https://nextjs.org/docs/app/api-reference/components/image#loader)을 사용할 수 있습니다.

#### `path`[](https://nextjs.org/docs/app/api-reference/components/image#path)

Image Optimization API의 기본 경로를 변경하거나 접두사를 붙이려면 `path` 속성을 사용할 수 있습니다. `path`의 기본값은 `/_next/image`입니다.

next.config.js
[code]
    module.exports = {
      images: {
        path: '/my-prefix/_next/image',
      },
    }
[/code]

#### `deviceSizes`[](https://nextjs.org/docs/app/api-reference/components/image#devicesizes)

`deviceSizes`는 디바이스 너비 브레이크포인트 목록을 지정합니다. 이러한 너비는 `next/image` 컴포넌트가 [`sizes`](https://nextjs.org/docs/app/api-reference/components/image#sizes) prop을 사용할 때, 사용자 디바이스에 맞는 이미지를 제공하도록 활용됩니다.

구성이 없으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
      },
    }
[/code]

#### `imageSizes`[](https://nextjs.org/docs/app/api-reference/components/image#imagesizes)

`imageSizes`는 이미지 너비 목록을 지정합니다. 이 너비들은 [device sizes](https://nextjs.org/docs/app/api-reference/components/image#devicesizes) 배열과 결합되어 이미지 [srcset](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/srcset)을 생성할 전체 크기 배열이 됩니다.

구성이 없으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        imageSizes: [32, 48, 64, 96, 128, 256, 384],
      },
    }
[/code]

`imageSizes`는 이미지가 화면 전체 너비보다 작다는 것을 나타내는 [`sizes`](https://nextjs.org/docs/app/api-reference/components/image#sizes) prop을 제공하는 이미지에만 사용됩니다. 따라서 `imageSizes`에 포함된 크기는 모두 `deviceSizes`에서 가장 작은 크기보다 작아야 합니다.

#### `qualities`[](https://nextjs.org/docs/app/api-reference/components/image#qualities)

`qualities`는 이미지 품질 값 목록을 지정합니다.

구성이 없으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        qualities: [75],
      },
    }
[/code]

> **알아두면 좋아요**: Next.js 16부터는 권한 없는 접근이 의도보다 많은 품질을 최적화하지 못하도록 이 필드가 필수입니다.

다음과 같이 허용 목록에 더 많은 이미지 품질을 추가할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        qualities: [25, 50, 75, 100],
      },
    }
[/code]

위 예시에서는 25, 50, 75, 100 네 가지 품질만 허용됩니다.

[`quality`](https://nextjs.org/docs/app/api-reference/components/image#quality) prop이 이 배열의 값과 일치하지 않으면 가장 가까운 허용 값이 사용됩니다.

REST API에 이 배열에 없는 품질로 직접 접근하면 서버는 400 Bad Request를 반환합니다.

#### `formats`[](https://nextjs.org/docs/app/api-reference/components/image#formats)

`formats`는 사용할 이미지 포맷 목록을 지정합니다.

next.config.js
[code]
    module.exports = {
      images: {
        // Default
        formats: ['image/webp'],
      },
    }
[/code]

Next.js는 요청의 `Accept` 헤더를 통해 브라우저가 지원하는 이미지 포맷을 자동 감지하여 최적의 출력 포맷을 결정합니다.

`Accept` 헤더가 구성된 포맷 중 둘 이상과 일치하면 배열에서 먼저 일치한 포맷을 사용하므로 배열 순서가 중요합니다. 일치하는 항목이 없거나 원본 이미지가 애니메이션이라면 원본 포맷을 유지합니다.

브라우저가 [AVIF를 지원하지 않는 경우](https://caniuse.com/avif) src 이미지의 원본 포맷으로 폴백하도록 AVIF를 활성화할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        formats: ['image/avif'],
      },
    }
[/code]

AVIF와 WebP를 함께 활성화할 수도 있습니다. AVIF를 지원하는 브라우저에서는 AVIF가 우선이며, WebP가 폴백으로 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        formats: ['image/avif', 'image/webp'],
      },
    }
[/code]

> **알아두면 좋아요** :
> 
>   * 대부분의 사용 사례에서는 여전히 WebP 사용을 권장합니다.
>   * AVIF는 WebP 대비 인코딩이 일반적으로 50% 더 오래 걸리지만 압축률은 20% 더 높습니다. 즉, 이미지를 처음 요청할 때는 더 느릴 수 있지만 캐시된 후에는 더 빠르게 제공됩니다.
>   * 여러 포맷을 사용할 때 Next.js는 각 포맷을 별도로 캐시하므로 AVIF와 WebP 버전을 모두 저장해야 하며, 단일 포맷을 사용할 때보다 저장 공간이 더 필요합니다.
>   * Next.js 앞단에 Proxy/CDN을 두고 셀프 호스팅한다면 Proxy가 `Accept` 헤더를 전달하도록 구성해야 합니다.
> 

#### `minimumCacheTTL`[](https://nextjs.org/docs/app/api-reference/components/image#minimumcachettl)

`minimumCacheTTL`은 캐시된 최적화 이미지의 TTL(초)을 설정합니다. 많은 경우, [Static Image Import](https://nextjs.org/docs/app/getting-started/images#local-images)를 사용하는 것이 더 좋으며, 이 경우 파일 콘텐츠를 자동으로 해시하고 `immutable` `Cache-Control` 헤더와 함께 이미지를 영구 캐시합니다.

구성이 없으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        minimumCacheTTL: 14400, // 4 hours
      },
    }
[/code]

재검증 횟수를 줄이고 비용을 낮추기 위해 TTL을 늘릴 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        minimumCacheTTL: 2678400, // 31 days
      },
    }
[/code]

최적화된 이미지의 만료(또는 Max Age)는 `minimumCacheTTL`과 업스트림 이미지의 `Cache-Control` 헤더 중 더 큰 값으로 결정됩니다.

이미지별 캐시 동작을 바꿔야 한다면 [`headers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)를 구성하여 업스트림 이미지(예: `/some-asset.jpg`, `/_next/image` 아님)에 `Cache-Control` 헤더를 설정하세요.

현재 캐시를 무효화할 방법이 없으므로 `minimumCacheTTL`을 낮게 유지하는 것이 좋습니다. 그렇지 않으면 [`src`](https://nextjs.org/docs/app/api-reference/components/image#src) prop을 수동으로 변경하거나 `<distDir>/cache/images`에 있는 캐시 파일을 삭제해야 할 수 있습니다.

#### `disableStaticImages`[](https://nextjs.org/docs/app/api-reference/components/image#disablestaticimages)

`disableStaticImages`는 정적 이미지 임포트를 비활성화합니다.

기본 동작에서는 `import icon from './icon.png'`처럼 정적 파일을 임포트한 뒤 `src` 속성에 전달할 수 있습니다. 일부 플러그인은 이 임포트가 다른 방식으로 동작하길 기대하므로 이 기능이 충돌한다면 비활성화할 수 있습니다.

`next.config.js`에서 정적 이미지 임포트를 비활성화할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        disableStaticImages: true,
      },
    }
[/code]

#### `maximumRedirects`[](https://nextjs.org/docs/app/api-reference/components/image#maximumredirects)

기본 이미지 최적화 로더는 원격 이미지를 가져올 때 최대 3회까지 HTTP 리디렉션을 따릅니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumRedirects: 3,
      },
    }
[/code]

원격 이미지를 가져올 때 따를 리디렉션 횟수를 직접 구성할 수 있습니다. 값을 `0`으로 설정하면 리디렉션을 따라가지 않습니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumRedirects: 0,
      },
    }
[/code]

#### `maximumResponseBody`[](https://nextjs.org/docs/app/api-reference/components/image#maximumresponsebody)

기본 이미지 최적화 로더는 최대 50MB 크기의 원본 이미지를 가져옵니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumResponseBody: 50_000_000,
      },
    }
[/code]

모든 원본 이미지가 작다는 것을 알고 있다면, 메모리가 제한된 서버를 보호하기 위해 이 값을 5MB 같은 더 작은 값으로 낮출 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumResponseBody: 5_000_000,
      },
    }
[/code]

#### `dangerouslyAllowLocalIP`[](https://nextjs.org/docs/app/api-reference/components/image#dangerouslyallowlocalip)

사설 네트워크에서 Next.js를 셀프 호스팅하는 드문 경우, 동일한 네트워크의 로컬 IP 주소에서 이미지를 최적화하도록 허용하고 싶을 수 있습니다. 이는 내부 네트워크 콘텐츠에 악의적 접근이 가능해질 수 있으므로 대부분의 사용자에게는 권장되지 않습니다.

기본값은 false입니다.

next.config.js
[code]
    module.exports = {
      images: {
        dangerouslyAllowLocalIP: false,
      },
    }
[/code]

로컬 네트워크의 다른 위치에 호스팅된 원격 이미지를 최적화해야 한다면 값을 true로 설정할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        dangerouslyAllowLocalIP: true,
      },
    }
[/code]

#### `dangerouslyAllowSVG`[](https://nextjs.org/docs/app/api-reference/components/image#dangerouslyallowsvg)

`dangerouslyAllowSVG`는 SVG 이미지를 제공할 수 있게 합니다.

next.config.js
[code]
    module.exports = {
      images: {
        dangerouslyAllowSVG: true,
      },
    }
[/code]

기본적으로 Next.js는 몇 가지 이유로 SVG를 최적화하지 않습니다.

  * SVG는 벡터 포맷이므로 손실 없이 크기를 조정할 수 있습니다.
  * SVG는 HTML/CSS와 동일한 기능을 많이 포함하므로 적절한 [Content Security Policy (CSP) 헤더](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#content-security-policy)가 없으면 취약점으로 이어질 수 있습니다.



[`src`](https://nextjs.org/docs/app/api-reference/components/image#src) prop이 SVG임이 확실하다면 [`unoptimized`](https://nextjs.org/docs/app/api-reference/components/image#unoptimized) prop을 사용하는 것을 권장합니다. `src`가 `".svg"`로 끝나면 이 동작이 자동으로 적용됩니다.
[code] 
    <Image src="/my-image.svg" unoptimized />
[/code]

또한 브라우저가 이미지를 다운로드하도록 강제하는 `contentDispositionType`, 이미지에 포함된 스크립트 실행을 방지하는 `contentSecurityPolicy` 설정을 함께 적용하는 것을 강력히 권장합니다.

next.config.js
[code]
    module.exports = {
      images: {
        dangerouslyAllowSVG: true,
        contentDispositionType: 'attachment',
        contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
      },
    }
[/code]

#### `contentDispositionType`[](https://nextjs.org/docs/app/api-reference/components/image#contentdispositiontype)

`contentDispositionType`은 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) 헤더를 설정합니다.

next.config.js
[code]
    module.exports = {
      images: {
        contentDispositionType: 'inline',
      },
    }
[/code]

#### `contentSecurityPolicy`[](https://nextjs.org/docs/app/api-reference/components/image#contentsecuritypolicy)

`contentSecurityPolicy`는 이미지에 대한 [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) 헤더를 구성할 수 있게 합니다. 이는 이미지에 포함된 스크립트가 실행되는 것을 막기 위해 [`dangerouslyAllowSVG`](https://nextjs.org/docs/app/api-reference/components/image#dangerouslyallowsvg)를 사용할 때 특히 중요합니다.

next.config.js
[code]
    module.exports = {
      images: {
        contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
      },
    }
[/code]

기본적으로 [loader](https://nextjs.org/docs/app/api-reference/components/image#loader)는 API가 임의의 원격 이미지를 제공할 수 있기 때문에 추가 보호 차원에서 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) 헤더를 `attachment`로 설정합니다.

기본값은 `attachment`이며, 사용자가 이미지를 직접 방문할 때 브라우저가 이미지를 다운로드하도록 강제합니다. [`dangerouslyAllowSVG`](https://nextjs.org/docs/app/api-reference/components/image#dangerouslyallowsvg)가 true일 때 특히 중요합니다.

필요하다면 `inline`으로 설정해 브라우저가 직접 방문 시 다운로드 없이 이미지를 렌더링하도록 허용할 수 있습니다.

### 사용이 중단된 구성 옵션[](https://nextjs.org/docs/app/api-reference/components/image#deprecated-configuration-options)

#### `domains`[](https://nextjs.org/docs/app/api-reference/components/image#domains)

> **Warning** : 악의적인 사용자를 막기 위해 Next.js 14부터는 더 엄격한 [`remotePatterns`](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns)를 권장하며, `domains`는 더 이상 권장되지 않습니다.

[`remotePatterns`](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns)와 유사하게 `domains` 구성은 외부 이미지에 허용할 호스트 이름 목록을 제공하는 데 사용할 수 있습니다. 하지만 `domains` 구성은 와일드카드 패턴 매칭을 지원하지 않으며 프로토콜, 포트, pathname을 제한할 수 없습니다.

대부분의 원격 이미지 서버는 여러 테넌트가 공유하므로 의도한 이미지들만 최적화되도록 `remotePatterns`를 사용하는 것이 더 안전합니다.

아래는 `next.config.js` 파일에서 `domains` 속성을 사용하는 예시입니다.

next.config.js
[code]
    module.exports = {
      images: {
        domains: ['assets.acme.com'],
      },
    }
[/code]

## 함수[](https://nextjs.org/docs/app/api-reference/components/image#functions)

### `getImageProps`[](https://nextjs.org/docs/app/api-reference/components/image#getimageprops)

`getImageProps` 함수는 기본 `<img>` 요소로 전달될 props를 가져와 다른 컴포넌트나 스타일, 캔버스 등으로 전달할 때 사용할 수 있습니다.
[code] 
    import { getImageProps } from 'next/image'
     
    const { props } = getImageProps({
      src: 'https://example.com/image.jpg',
      alt: 'A scenic mountain view',
      width: 1200,
      height: 800,
    })
     
    function ImageWithCaption() {
      return (
        <figure>
          <img {...props} />
          <figcaption>A scenic mountain view</figcaption>
        </figure>
      )
    }
[/code]

이는 React `useState()` 호출을 피하므로 성능 향상에 도움이 될 수 있지만, [`placeholder`](https://nextjs.org/docs/app/api-reference/components/image#placeholder) prop과 함께 사용할 수는 없습니다. placeholder가 제거되지 않기 때문입니다.

## 알려진 브라우저 버그[](https://nextjs.org/docs/app/api-reference/components/image#known-browser-bugs)

이 `next/image` 컴포넌트는 브라우저 기본 [지연 로딩](https://caniuse.com/loading-lazy-attr)을 사용하며, Safari 15.4 이전 구버전에서는 eager 로딩으로 대체될 수 있습니다. blur-up placeholder를 사용할 때 Safari 12 이전 구버전에서는 빈 placeholder로 대체됩니다. `width`/`height`가 `auto`인 스타일을 사용하면, 속성에서 [종횡비를 유지](https://caniuse.com/mdn-html_elements_img_aspect_ratio_computed_from_attributes)하지 않는 Safari 15 이전 구형 브라우저에서 [Layout Shift](https://web.dev/cls/)가 발생할 수 있습니다. 자세한 내용은 [이 MDN 동영상](https://www.youtube.com/watch?v=4-d_SoCHeWE)을 참조하세요.

  * [Safari 15 - 16.3](https://bugs.webkit.org/show_bug.cgi?id=243601)은 로딩 중 회색 테두리를 표시합니다. Safari 16.4에서 [이 문제가 수정되었습니다](https://webkit.org/blog/13966/webkit-features-in-safari-16-4/#:~:text=Now%20in%20Safari%2016.4%2C%20a%20gray%20line%20no%20longer%20appears%20to%20mark%20the%20space%20where%20a%20lazy%2Dloaded%20image%20will%20appear%20once%20it%E2%80%99s%20been%20loaded.). 가능한 해결책:
    * CSS `@supports (font: -apple-system-body) and (-webkit-appearance: none) { img[loading="lazy"] { clip-path: inset(0.6px) } }` 사용
    * 이미지가 폴드 상단에 있다면 [`loading="eager"`](https://nextjs.org/docs/app/api-reference/components/image#loading) 사용
  * [Firefox 67+](https://bugzilla.mozilla.org/show_bug.cgi?id=1556156)는 로딩 중 흰색 배경을 표시합니다. 가능한 해결책:
    * [AVIF `formats`](https://nextjs.org/docs/app/api-reference/components/image#formats) 활성화
    * [`placeholder`](https://nextjs.org/docs/app/api-reference/components/image#placeholder) 사용



## 예시[](https://nextjs.org/docs/app/api-reference/components/image#examples)

### 이미지 스타일링[](https://nextjs.org/docs/app/api-reference/components/image#styling-images)

Image 컴포넌트를 스타일링하는 방식은 일반 `<img>` 요소와 유사하지만, 몇 가지 지침을 기억해야 합니다.

`styled-jsx` 대신 `className` 또는 `style`을 사용하세요. 대부분의 경우 `className` prop 사용을 권장합니다. 가져온 [CSS Module](https://nextjs.org/docs/app/getting-started/css), [전역 스타일시트](https://nextjs.org/docs/app/getting-started/css#global-css) 등 무엇이든 가능합니다.
[code] 
    import styles from './styles.module.css'
     
    export default function MyImage() {
      return <Image className={styles.image} src="/my-image.png" alt="My Image" />
    }
[/code]

`style` prop을 사용해 인라인 스타일을 지정할 수도 있습니다.
[code] 
    export default function MyImage() {
      return (
        <Image style={{ borderRadius: '8px' }} src="/my-image.png" alt="My Image" />
      )
    }
[/code]

`fill`을 사용할 때는 부모 요소에 `position: relative` 또는 `display: block`이 설정되어야 합니다. 해당 레이아웃 모드에서 이미지 요소가 올바르게 렌더링되도록 하기 위한 필수 조건입니다.
[code] 
    <div style={{ position: 'relative' }}>
      <Image fill src="/my-image.png" alt="My Image" />
    </div>
[/code]

[styled-jsx](https://nextjs.org/docs/app/guides/css-in-js)는 현재 컴포넌트 범위에만 적용되므로(`global`로 표시하지 않는 한) 사용할 수 없습니다.

### 정적 내보내기와 반응형 이미지[](https://nextjs.org/docs/app/api-reference/components/image#responsive-images-with-a-static-export)

정적 이미지를 import하면 Next.js가 파일을 기반으로 너비와 높이를 자동으로 설정합니다. 스타일을 지정해 이미지를 반응형으로 만들 수 있습니다.
[code] 
    import Image from 'next/image'
    import mountains from '../public/mountains.jpg'
     
    export default function Responsive() {
      return (
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          <Image
            alt="Mountains"
            // Importing an image will
            // automatically set the width and height
            src={mountains}
            sizes="100vw"
            // Make the image display full width
            // and preserve its aspect ratio
            style={{
              width: '100%',
              height: 'auto',
            }}
          />
        </div>
      )
    }
[/code]

### 원격 URL과 반응형 이미지[](https://nextjs.org/docs/app/api-reference/components/image#responsive-images-with-a-remote-url)

소스 이미지가 동적이거나 원격 URL이라면 Next.js가 종횡비를 계산할 수 있도록 width와 height props를 제공해야 합니다.

components/page.js
[code]
    import Image from 'next/image'
     
    export default function Page({ photoUrl }) {
      return (
        <Image
          src={photoUrl}
          alt="Picture of the author"
          sizes="100vw"
          style={{
            width: '100%',
            height: 'auto',
          }}
          width={500}
          height={300}
        />
      )
    }
[/code]

직접 확인해 보세요:

  * [뷰포트에 반응하는 이미지 데모](https://image-component.nextjs.gallery/responsive)



### `fill`로 반응형 이미지[](https://nextjs.org/docs/app/api-reference/components/image#responsive-image-with-fill)

이미지의 종횡비를 모를 때는 [`fill` prop](https://nextjs.org/docs/app/api-reference/components/image#fill)에 `objectFit` prop을 `cover`로 설정해 사용할 수 있습니다. 이렇게 하면 이미지가 부모 컨테이너의 전체 너비를 채웁니다.
[code] 
    import Image from 'next/image'
    import mountains from '../public/mountains.jpg'
     
    export default function Fill() {
      return (
        <div
          style={{
            display: 'grid',
            gridGap: '8px',
            gridTemplateColumns: 'repeat(auto-fit, minmax(400px, auto))',
          }}
        >
          <div style={{ position: 'relative', width: '400px' }}>
            <Image
              alt="Mountains"
              src={mountains}
              fill
              sizes="(min-width: 808px) 50vw, 100vw"
              style={{
                objectFit: 'cover', // cover, contain, none
              }}
            />
          </div>
          {/* And more images in the grid... */}
        </div>
      )
    }
[/code]

### 배경 이미지[](https://nextjs.org/docs/app/api-reference/components/image#background-image)

`fill` prop을 사용해 이미지가 화면 전체를 덮도록 만들 수 있습니다.
[code] 
    import Image from 'next/image'
    import mountains from '../public/mountains.jpg'
     
    export default function Background() {
      return (
        <Image
          alt="Mountains"
          src={mountains}
          placeholder="blur"
          quality={100}
          fill
          sizes="100vw"
          style={{
            objectFit: 'cover',
          }}
        />
      )
    }
[/code]

여러 스타일로 Image 컴포넌트를 사용하는 예시는 [Image Component Demo](https://image-component.nextjs.gallery)에서 확인하세요.

### 원격 이미지[](https://nextjs.org/docs/app/api-reference/components/image#remote-images)

원격 이미지를 사용하려면 `src` 속성에 URL 문자열을 지정해야 합니다.

app/page.js
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return (
        <Image
          src="https://s3.amazonaws.com/my-bucket/profile.png"
          alt="Picture of the author"
          width={500}
          height={500}
        />
      )
    }
[/code]

Next.js는 빌드 과정에서 원격 파일에 접근할 수 없으므로 [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), 선택적인 [`blurDataURL`](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl) props를 수동으로 제공해야 합니다.

`width`와 `height` 속성은 이미지의 올바른 종횡비를 추론하고 로딩 중 발생할 수 있는 레이아웃 시프트를 방지하는 데 사용됩니다. `width`와 `height`는 렌더링되는 이미지 파일의 실제 크기를 결정하지는 않습니다.

이미지를 안전하게 최적화하려면 `next.config.js`에서 지원할 URL 패턴 목록을 정의하세요. 악의적인 사용을 막기 위해 가능한 한 구체적으로 지정하세요. 예를 들어, 아래 구성은 특정 AWS S3 버킷의 이미지만 허용합니다.

next.config.js
[code]
    module.exports = {
      images: {
        remotePatterns: [
          {
            protocol: 'https',
            hostname: 's3.amazonaws.com',
            port: '',
            pathname: '/my-bucket/**',
            search: '',
          },
[/code]

],
      },
    }
[/code]

### Theme detection[](https://nextjs.org/docs/app/api-reference/components/image#theme-detection)

라이트 모드와 다크 모드에 서로 다른 이미지를 표시하려면 두 개의 `<Image>` 컴포넌트를 감싸고 CSS 미디어 쿼리를 기준으로 올바른 이미지를 노출하는 새 컴포넌트를 만들 수 있습니다.

components/theme-image.module.css
[code]
    .imgDark {
      display: none;
    }
     
    @media (prefers-color-scheme: dark) {
      .imgLight {
        display: none;
      }
      .imgDark {
        display: unset;
      }
    }
[/code]

components/theme-image.tsx

JavaScriptTypeScript
[code]
    import styles from './theme-image.module.css'
    import Image, { ImageProps } from 'next/image'
     
    type Props = Omit<ImageProps, 'src' | 'preload' | 'loading'> & {
      srcLight: string
      srcDark: string
    }
     
    const ThemeImage = (props: Props) => {
      const { srcLight, srcDark, ...rest } = props
     
      return (
        <>
          <Image {...rest} src={srcLight} className={styles.imgLight} />
          <Image {...rest} src={srcDark} className={styles.imgDark} />
        </>
      )
    }
[/code]

> **알아두면 좋은 점**: `loading="lazy"` 기본 동작 덕분에 올바른 이미지 한 장만 로드됩니다. 두 이미지를 모두 로드하게 되므로 `preload` 또는 `loading="eager"`는 사용할 수 없습니다. 대신 [`fetchPriority="high"`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/fetchPriority)를 사용할 수 있습니다.

바로 시도해 보기:

  * [라이트/다크 모드 테마 감지 데모](https://image-component.nextjs.gallery/theme)



### Art direction[](https://nextjs.org/docs/app/api-reference/components/image#art-direction)

모바일과 데스크톱에 서로 다른 이미지를 표시하고 싶다면, 일명 [Art Direction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#art_direction)이라고 부르는 접근 방식으로, `getImageProps()`에 서로 다른 `src`, `width`, `height`, `quality` props를 전달하면 됩니다.

app/page.js
[code]
    import { getImageProps } from 'next/image'
     
    export default function Home() {
      const common = { alt: 'Art Direction Example', sizes: '100vw' }
      const {
        props: { srcSet: desktop },
      } = getImageProps({
        ...common,
        width: 1440,
        height: 875,
        quality: 80,
        src: '/desktop.jpg',
      })
      const {
        props: { srcSet: mobile, ...rest },
      } = getImageProps({
        ...common,
        width: 750,
        height: 1334,
        quality: 70,
        src: '/mobile.jpg',
      })
     
      return (
        <picture>
          <source media="(min-width: 1000px)" srcSet={desktop} />
          <source media="(min-width: 500px)" srcSet={mobile} />
          <img {...rest} style={{ width: '100%', height: 'auto' }} />
        </picture>
      )
    }
[/code]

### Background CSS[](https://nextjs.org/docs/app/api-reference/components/image#background-css)

배경 이미지를 최적화하려면 `srcSet` 문자열을 [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/image/image-set) CSS 함수로 변환할 수도 있습니다.

app/page.js
[code]
    import { getImageProps } from 'next/image'
     
    function getBackgroundImage(srcSet = '') {
      const imageSet = srcSet
        .split(', ')
        .map((str) => {
          const [url, dpi] = str.split(' ')
          return `url("${url}") ${dpi}`
        })
        .join(', ')
      return `image-set(${imageSet})`
    }
     
    export default function Home() {
      const {
        props: { srcSet },
      } = getImageProps({ alt: '', width: 128, height: 128, src: '/img.png' })
      const backgroundImage = getBackgroundImage(srcSet)
      const style = { height: '100vh', width: '100vw', backgroundImage }
     
      return (
        <main style={style}>
          <h1>Hello World</h1>
        </main>
      )
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/components/image#version-history)

Version| Changes  
---|---  
`v16.1.2`| `maximumResponseBody` 설정이 추가되었습니다.  
`v16.0.0`| `qualities` 기본 설정이 `[75]`로 변경되고 `preload` prop이 추가되었으며 `priority` prop이 더 이상 권장되지 않습니다. `dangerouslyAllowLocalIP` 설정과 `maximumRedirects` 설정이 추가되었습니다.  
`v15.3.0`| `remotePatterns`가 `URL` 객체 배열을 지원합니다.  
`v15.0.0`| `contentDispositionType` 설정 기본값이 `attachment`로 변경되었습니다.  
`v14.2.23`| `qualities` 설정이 추가되었습니다.  
`v14.2.15`| `decoding` prop과 `localPatterns` 설정이 추가되었습니다.  
`v14.2.14`| `remotePatterns.search` prop이 추가되었습니다.  
`v14.2.0`| `overrideSrc` prop이 추가되었습니다.  
`v14.1.0`| `getImageProps()`가 안정화되었습니다.  
`v14.0.0`| `onLoadingComplete` prop과 `domains` 설정이 더 이상 권장되지 않습니다.  
`v13.4.14`| `placeholder` prop이 `data:/image...`를 지원합니다.  
`v13.2.0`| `contentDispositionType` 설정이 추가되었습니다.  
`v13.0.6`| `ref` prop이 추가되었습니다.  
`v13.0.0`| `next/image` import가 `next/legacy/image`로 이름이 변경되었습니다. `next/future/image` import는 `next/image`로 이름이 변경되었습니다. import를 안전하게 자동으로 바꾸기 위한 [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-to-legacy-image)가 제공됩니다. `<span>` 래퍼가 제거되었고 `layout`, `objectFit`, `objectPosition`, `lazyBoundary`, `lazyRoot` props가 제거되었습니다. `alt`가 필수입니다. `onLoadingComplete`가 `img` 요소 참조를 받습니다. 기본 제공 로더 설정이 제거되었습니다.  
`v12.3.0`| `remotePatterns`와 `unoptimized` 설정이 안정화되었습니다.  
`v12.2.0`| 실험적 `remotePatterns`와 실험적 `unoptimized` 설정이 추가되었습니다. `layout="raw"`가 제거되었습니다.  
`v12.1.1`| `style` prop이 추가되었습니다. `layout="raw"` 실험적 지원이 추가되었습니다.  
`v12.1.0`| `dangerouslyAllowSVG`와 `contentSecurityPolicy` 설정이 추가되었습니다.  
`v12.0.9`| `lazyRoot` prop이 추가되었습니다.  
`v12.0.0`| `formats` 설정이 추가되었습니다.  
AVIF 지원이 추가되었습니다.  
래퍼 `<div>`가 `<span>`으로 변경되었습니다.  
`v11.1.0`| `onLoadingComplete`와 `lazyBoundary` props가 추가되었습니다.  
`v11.0.0`| `src` prop이 정적 import를 지원합니다.  
`placeholder` prop이 추가되었습니다.  
`blurDataURL` prop이 추가되었습니다.  
`v10.0.5`| `loader` prop이 추가되었습니다.  
`v10.0.1`| `layout` prop이 추가되었습니다.  
`v10.0.0`| `next/image`가 도입되었습니다.  
   
이 정보가 도움이 되었나요?

supported.

Send
