---
title: 'Components: Image'
description: '마지막 업데이트 2026년 2월 20일'
---

# Components: Image | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/components/image

[API Reference](https://nextjs.org/docs/pages/api-reference)[Components](https://nextjs.org/docs/pages/api-reference/components)Image

Copy page

# Image

마지막 업데이트 2026년 2월 20일

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

> **알아두면 좋은 점**: Next.js 13 이전 버전을 사용한다면 컴포넌트 이름이 변경되기 전이므로 [next/legacy/image](https://nextjs.org/docs/pages/api-reference/components/image-legacy) 문서를 참고하세요.

## Reference[](https://nextjs.org/docs/pages/api-reference/components/image#reference)

### Props[](https://nextjs.org/docs/pages/api-reference/components/image#props)

다음 props를 사용할 수 있습니다:

Prop| Example| Type| Status  
---|---|---|---  
[`src`](https://nextjs.org/docs/pages/api-reference/components/image#src)| `src="/profile.png"`| String| Required  
[`alt`](https://nextjs.org/docs/pages/api-reference/components/image#alt)| `alt="Picture of the author"`| String| Required  
[`width`](https://nextjs.org/docs/pages/api-reference/components/image#width-and-height)| `width={500}`| Integer (px)| -  
[`height`](https://nextjs.org/docs/pages/api-reference/components/image#width-and-height)| `height={500}`| Integer (px)| -  
[`fill`](https://nextjs.org/docs/pages/api-reference/components/image#fill)| `fill={true}`| Boolean| -  
[`loader`](https://nextjs.org/docs/pages/api-reference/components/image#loader)| `loader={imageLoader}`| Function| -  
[`sizes`](https://nextjs.org/docs/pages/api-reference/components/image#sizes)| `sizes="(max-width: 768px) 100vw, 33vw"`| String| -  
[`quality`](https://nextjs.org/docs/pages/api-reference/components/image#quality)| `quality={80}`| Integer (1-100)| -  
[`preload`](https://nextjs.org/docs/pages/api-reference/components/image#preload)| `preload={true}`| Boolean| -  
[`placeholder`](https://nextjs.org/docs/pages/api-reference/components/image#placeholder)| `placeholder="blur"`| String| -  
[`style`](https://nextjs.org/docs/pages/api-reference/components/image#style)| `style={{objectFit: "contain"}}`| Object| -  
[`onLoadingComplete`](https://nextjs.org/docs/pages/api-reference/components/image#onloadingcomplete)| `onLoadingComplete={img => done())}`| Function| Deprecated  
[`onLoad`](https://nextjs.org/docs/pages/api-reference/components/image#onload)| `onLoad={event => done())}`| Function| -  
[`onError`](https://nextjs.org/docs/pages/api-reference/components/image#onerror)| `onError(event => fail()}`| Function| -  
[`loading`](https://nextjs.org/docs/pages/api-reference/components/image#loading)| `loading="lazy"`| String| -  
[`blurDataURL`](https://nextjs.org/docs/pages/api-reference/components/image#blurdataurl)| `blurDataURL="data:image/jpeg..."`| String| -  
[`unoptimized`](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized)| `unoptimized={true}`| Boolean| -  
[`overrideSrc`](https://nextjs.org/docs/pages/api-reference/components/image#overridesrc)| `overrideSrc="/seo.png"`| String| -  
[`decoding`](https://nextjs.org/docs/pages/api-reference/components/image#decoding)| `decoding="async"`| String| -  
  
#### `src`[](https://nextjs.org/docs/pages/api-reference/components/image#src)

이미지의 소스입니다. 다음 중 하나일 수 있습니다:

내부 경로 문자열.
[code] 
    <Image src="/profile.png" />
[/code]

[remotePatterns](https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns)로 구성된 절대 외부 URL.
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

> **알아두면 좋은 점**: 보안상의 이유로 기본 [loader](https://nextjs.org/docs/pages/api-reference/components/image#loader)를 사용하는 Image Optimization API는 `src` 이미지를 가져올 때 헤더를 전달하지 않습니다. `src` 이미지에 인증이 필요하다면 Image Optimization을 비활성화하기 위해 [unoptimized](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized) 속성 사용을 고려하세요.

#### `alt`[](https://nextjs.org/docs/pages/api-reference/components/image#alt)

`alt` 속성은 스크린 리더와 검색 엔진을 위한 이미지 설명이며, 이미지가 비활성화되었거나 로딩 중 오류가 발생했을 때의 대체 텍스트입니다.

페이지의 [의미를 바꾸지 않고 이미지를 대체할 수 있는](https://html.spec.whatwg.org/multipage/images.html#general-guidelines) 텍스트를 포함해야 합니다. 이미지를 보조하기 위한 것이 아니며 이미지 위나 아래의 캡션에서 이미 제공되는 정보를 반복해서는 안 됩니다.

이미지가 [순수 장식용](https://html.spec.whatwg.org/multipage/images.html#a-purely-decorative-image-that-doesn't-add-any-information)이거나 [사용자를 위한 것이 아닌](https://html.spec.whatwg.org/multipage/images.html#an-image-not-intended-for-the-user) 경우 `alt` 속성은 빈 문자열(`alt=""`)이어야 합니다.

> [이미지 접근성 지침](https://html.spec.whatwg.org/multipage/images.html#alt)에 대해 더 알아보세요.

#### `width` and `height`[](https://nextjs.org/docs/pages/api-reference/components/image#width-and-height)

`width`와 `height` 속성은 픽셀 단위의 [고유](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size) 이미지 크기를 나타냅니다. 이 속성은 브라우저가 이미지의 올바른 **종횡비**를 추론하여 로딩 중 레이아웃 이동을 방지하도록 공간을 예약하는 데 사용됩니다. 이미지의 _렌더링된 크기_ 는 CSS로 제어되며 이 속성이 결정하지 않습니다.
[code] 
    <Image src="/profile.png" width={500} height={500} />
[/code]

다음 경우를 제외하고는 `width`와 `height` 속성을 **모두** 설정해야 합니다:

  * 이미지가 정적으로 import된 경우
  * 이미지에 [`fill` 속성](https://nextjs.org/docs/pages/api-reference/components/image#fill)이 있는 경우



높이와 너비를 알 수 없다면 [`fill` 속성](https://nextjs.org/docs/pages/api-reference/components/image#fill) 사용을 권장합니다.

#### `fill`[](https://nextjs.org/docs/pages/api-reference/components/image#fill)

이미지가 부모 요소 크기만큼 확장되도록 하는 boolean입니다.
[code] 
    <Image src="/profile.png" fill={true} />
[/code]

**Positioning** :

  * 부모 요소는 반드시 `position: "relative"`, `"fixed"`, `"absolute"` 중 하나를 지정해야 합니다.
  * 기본적으로 `<img>` 요소는 `position: "absolute"`를 사용합니다.



**Object Fit** :

이미지에 스타일을 적용하지 않으면 컨테이너에 맞춰 늘어납니다. `objectFit`을 사용하여 자르기와 스케일링을 제어할 수 있습니다.

  * `"contain"`: 컨테이너에 맞게 축소하면서 종횡비를 유지합니다.
  * `"cover"`: 컨테이너를 채우며 잘릴 수 있습니다.



> [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position)과 [`object-fit`](https://developer.mozilla.org/docs/Web/CSS/object-fit)에 대해 자세히 알아보세요.

#### `loader`[](https://nextjs.org/docs/pages/api-reference/components/image#loader)

이미지 URL을 생성하는 사용자 정의 함수입니다. 함수는 다음 매개변수를 받고 이미지 URL 문자열을 반환합니다:

  * [`src`](https://nextjs.org/docs/pages/api-reference/components/image#src)
  * [`width`](https://nextjs.org/docs/pages/api-reference/components/image#width-and-height)
  * [`quality`](https://nextjs.org/docs/pages/api-reference/components/image#quality)


[code] 
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

대신 `next.config.js`에서 [loaderFile](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile) 구성을 사용해 애플리케이션의 모든 `next/image` 인스턴스를 prop 없이 설정할 수 있습니다.

#### `sizes`[](https://nextjs.org/docs/pages/api-reference/components/image#sizes)

브레이크포인트별 이미지 크기를 정의합니다. 브라우저는 이를 사용하여 생성된 `srcset` 중 가장 적절한 크기를 선택합니다.
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

`sizes`는 다음 상황에서 사용해야 합니다:

  * 이미지가 [`fill`](https://nextjs.org/docs/pages/api-reference/components/image#fill) prop을 사용하는 경우
  * CSS로 이미지를 반응형으로 만드는 경우



`sizes`가 없으면 브라우저는 이미지가 뷰포트(`100vw`)와 같은 너비라고 가정합니다. 이로 인해 불필요하게 큰 이미지를 다운로드할 수 있습니다.

또한 `sizes`는 `srcset` 생성 방식에 영향을 줍니다:

  * `sizes` 없음: Next.js는 고정 크기 이미지에 적합한 제한된 `srcset`(예: 1x, 2x)을 생성합니다.
  * `sizes` 있음: Next.js는 반응형 레이아웃에 최적화된 전체 `srcset`(예: 640w, 750w 등)을 생성합니다.



> `srcset`과 `sizes`에 대해 [web.dev](https://web.dev/learn/design/responsive-images/#sizes)와 [mdn](https://developer.mozilla.org/docs/Web/HTML/Element/img#sizes)에서 더 알아보세요.

#### `quality`[](https://nextjs.org/docs/pages/api-reference/components/image#quality)

최적화된 이미지 품질을 설정하는 `1`에서 `100` 사이의 정수입니다. 값이 높을수록 파일 크기와 시각적 선명도가 증가합니다. 값이 낮을수록 파일 크기가 줄지만 선명도에 영향을 줄 수 있습니다.
[code] 
    // Default quality is 75
    <Image quality={75} />
[/code]

`next.config.js`에서 [qualities](https://nextjs.org/docs/pages/api-reference/components/image#qualities)를 구성했다면 값은 허용된 항목 중 하나와 일치해야 합니다.

> **알아두면 좋은 점**: 원본 이미지 품질이 이미 낮다면 높은 quality 값을 설정해도 외관이 개선되지 않은 채 파일 크기만 증가합니다.

#### `style`[](https://nextjs.org/docs/pages/api-reference/components/image#style)

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

> **알아두면 좋은 점**: `style` prop으로 사용자 정의 너비를 설정하는 경우 이미지 종횡비를 유지하려면 `height: 'auto'`도 설정하세요.

#### `preload`[](https://nextjs.org/docs/pages/api-reference/components/image#preload)

이미지를 미리 로드할지 여부를 나타내는 boolean입니다.
[code] 
    // Default preload is false
    <Image preload={false} />
[/code]

  * `true`: `<head>`에 `<link>`를 삽입하여 이미지를 [미리 로드](https://web.dev/preload-responsive-images/)합니다.
  * `false`: 이미지를 미리 로드하지 않습니다.



**사용해야 하는 경우:**

  * 이미지가 [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) 요소인 경우
  * 이미지가 폴드 위, 일반적으로 히어로 이미지인 경우
  * `<body>`에서 나중에 발견되기 전에 `<head>`에서 이미지 로딩을 시작하려는 경우



**사용하지 말아야 하는 경우:**

  * 뷰포트에 따라 [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) 요소가 될 수 있는 이미지가 여러 개 있는 경우

* `loading` 속성을 사용할 때.
  * `fetchPriority` 속성을 사용할 때.



대부분의 경우 `preload` 대신 `loading="eager"` 또는 `fetchPriority="high"`를 사용해야 합니다.

#### `priority`[](https://nextjs.org/docs/pages/api-reference/components/image#priority)

Next.js 16부터 동작을 명확히 하기 위해 `priority` 속성이 [`preload`](https://nextjs.org/docs/pages/api-reference/components/image#preload) 속성으로 대체되어 사용 중단되었습니다.

#### `loading`[](https://nextjs.org/docs/pages/api-reference/components/image#loading)

이미지가 언제 로딩을 시작할지 제어합니다.
[code] 
    // Defaults to lazy
    <Image loading="lazy" />
[/code]

  * `lazy`: 뷰포트에서 계산된 거리 안에 들어올 때까지 이미지 로딩을 지연합니다.
  * `eager`: 페이지에서 위치와 관계없이 즉시 이미지를 로드합니다.



이미지를 즉시 로딩해야 할 때만 `eager`를 사용하세요.

> [`loading` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#loading)에 대해 자세히 알아보세요.

#### `placeholder`[](https://nextjs.org/docs/pages/api-reference/components/image#placeholder)

이미지가 로딩되는 동안 사용할 플레이스홀더를 지정하여 체감 로딩 성능을 개선합니다.
[code] 
    // defaults to empty
    <Image placeholder="empty" />
[/code]

  * `empty`: 이미지가 로딩되는 동안 플레이스홀더를 표시하지 않습니다.
  * `blur`: 이미지를 흐린 버전으로 플레이스홀더로 사용합니다. [`blurDataURL`](https://nextjs.org/docs/pages/api-reference/components/image#blurdataurl) 속성과 함께 사용해야 합니다.
  * `data:image/...`: [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)을 플레이스홀더로 사용합니다.



**예시:**

  * [`blur` placeholder](https://image-component.nextjs.gallery/placeholder)
  * [데이터 URL `placeholder` prop으로 구현한 쉬머 효과](https://image-component.nextjs.gallery/shimmer)
  * [`blurDataURL` prop으로 구현한 색상 효과](https://image-component.nextjs.gallery/color)



> [`placeholder` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#placeholder)에 대해 자세히 알아보세요.

#### `blurDataURL`[](https://nextjs.org/docs/pages/api-reference/components/image#blurdataurl)

이미지가 성공적으로 로드되기 전에 사용할 [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)입니다. 자동으로 설정되거나 [`placeholder="blur"`](https://nextjs.org/docs/pages/api-reference/components/image#placeholder) 속성과 함께 사용할 수 있습니다.
[code] 
    <Image placeholder="blur" blurDataURL="..." />
[/code]

이미지는 자동으로 확대되고 블러 처리되므로 10px 이하의 아주 작은 이미지를 사용하는 것이 좋습니다.

**Automatic**

`src`가 `jpg`, `png`, `webp`, `avif` 파일의 정적 import인 경우, 이미지가 애니메이션이 아니라면 `blurDataURL`이 자동으로 추가됩니다.

**Manually set**

이미지가 동적이거나 원격인 경우 `blurDataURL`을 직접 제공해야 합니다. 생성하려면 다음을 사용할 수 있습니다.

  * [png-pixel.com 같은 온라인 도구](https://png-pixel.com)
  * [Plaiceholder 같은 라이브러리](https://github.com/joe-bell/plaiceholder)



큰 blurDataURL은 성능을 저하시킬 수 있습니다. 작고 단순하게 유지하세요.

**예시:**

  * [기본 `blurDataURL` prop](https://image-component.nextjs.gallery/placeholder)
  * [`blurDataURL` prop으로 구현한 색상 효과](https://image-component.nextjs.gallery/color)



#### `onLoad`[](https://nextjs.org/docs/pages/api-reference/components/image#onload)

이미지가 완전히 로드되고 [placeholder](https://nextjs.org/docs/pages/api-reference/components/image#placeholder)가 제거되면 호출되는 콜백 함수입니다.
[code] 
    <Image onLoad={(e) => console.log(e.target.naturalWidth)} />
[/code]

콜백 함수는 `target`이 기본 `<img>` 요소를 참조하는 이벤트 객체 하나를 인수로 받습니다.

#### `onError`[](https://nextjs.org/docs/pages/api-reference/components/image#onerror)

이미지 로드에 실패했을 때 호출되는 콜백 함수입니다.
[code] 
    <Image onError={(e) => console.error(e.target.id)} />
[/code]

#### `unoptimized`[](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized)

이미지를 최적화할지 여부를 나타내는 불리언입니다. 1KB 미만의 작은 이미지, SVG 같은 벡터 이미지, GIF 같은 애니메이션 이미지처럼 최적화로 이득이 없는 경우에 유용합니다.
[code] 
    import Image from 'next/image'
     
    const UnoptimizedImage = (props) => {
      // Default is false
      return <Image {...props} unoptimized />
    }
[/code]

  * `true`: 소스 이미지는 품질, 크기, 형식을 변경하지 않고 `src` 그대로 제공합니다.
  * `false`: 소스 이미지를 최적화합니다.



Next.js 12.3.0부터는 `next.config.js`를 다음 설정으로 업데이트하여 모든 이미지에 이 prop을 일괄 적용할 수 있습니다:

next.config.js
[code]
    module.exports = {
      images: {
        unoptimized: true,
      },
    }
[/code]

#### `overrideSrc`[](https://nextjs.org/docs/pages/api-reference/components/image#overridesrc)

`<Image>` 컴포넌트에 `src` prop을 제공하면 결과 `<img>`에 대한 `srcset`과 `src` 속성이 자동으로 생성됩니다.

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

일부 경우에는 생성된 `src` 속성이 바람직하지 않아 `overrideSrc` prop으로 이를 대체하고 싶을 수 있습니다.

예를 들어 기존 웹사이트를 `<img>`에서 `<Image>`로 마이그레이션하는 동안 이미지 순위 유지나 재크롤 방지 같은 SEO 목적으로 동일한 `src` 속성을 유지하고 싶을 수 있습니다.

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

#### `decoding`[](https://nextjs.org/docs/pages/api-reference/components/image#decoding)

이미지를 디코딩할 때 브라우저가 다른 콘텐츠 업데이트를 기다릴지 여부에 대한 힌트를 제공합니다.
[code] 
    // Default is async
    <Image decoding="async" />
[/code]

  * `async`: 이미지를 비동기적으로 디코딩하여 완료되기 전에 다른 콘텐츠가 렌더링될 수 있도록 합니다.
  * `sync`: 다른 콘텐츠와 원자적으로 표시되도록 이미지를 동기적으로 디코딩합니다.
  * `auto`: 선호 설정이 없습니다. 브라우저가 최적의 방식을 선택합니다.



> [`decoding` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#decoding)에 대해 자세히 알아보세요.

### Other Props[](https://nextjs.org/docs/pages/api-reference/components/image#other-props)

`<Image />` 컴포넌트의 다른 속성은 `srcSet`을 제외하고 기본 `img` 요소로 전달됩니다.

  * `srcSet`: [Device Sizes](https://nextjs.org/docs/pages/api-reference/components/image#devicesizes)를 사용하세요.



### Deprecated props[](https://nextjs.org/docs/pages/api-reference/components/image#deprecated-props)

#### `onLoadingComplete`[](https://nextjs.org/docs/pages/api-reference/components/image#onloadingcomplete)

> **경고** : Next.js 14에서 사용 중단되었습니다. 대신 [`onLoad`](https://nextjs.org/docs/pages/api-reference/components/image#onload)를 사용하세요.

이미지가 완전히 로드되고 [placeholder](https://nextjs.org/docs/pages/api-reference/components/image#placeholder)가 제거되면 호출되는 콜백 함수입니다.

콜백 함수는 기본 `<img>` 요소에 대한 참조 하나를 인수로 받습니다.
[code] 
    <Image onLoadingComplete={(img) => console.log(img.naturalWidth)} />
[/code]

### Configuration options[](https://nextjs.org/docs/pages/api-reference/components/image#configuration-options)

`next.config.js`에서 Image 컴포넌트를 구성할 수 있습니다. 사용 가능한 옵션은 다음과 같습니다.

#### `localPatterns`[](https://nextjs.org/docs/pages/api-reference/components/image#localpatterns)

`next.config.js` 파일에서 `localPatterns`를 사용해 특정 로컬 경로의 이미지만 최적화하고 나머지는 차단합니다.

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

위 예시는 `next/image`의 `src` 속성이 `/assets/images/`로 시작하고 쿼리 문자열이 없어야 함을 보장합니다. 다른 경로를 최적화하려 하면 `400` Bad Request 오류가 발생합니다.

> **알아두면 좋아요** : `search` 속성을 생략하면 모든 검색 매개변수를 허용하게 되어 악의적인 사용자가 의도하지 않은 URL을 최적화할 수 있습니다. 정확히 일치하도록 `search: '?v=2'`처럼 구체적인 값을 사용하는 것이 좋습니다.

#### `remotePatterns`[](https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns)

`next.config.js`에서 `remotePatterns`를 사용하면 특정 외부 경로의 이미지만 허용하고 나머지는 차단할 수 있습니다. 이렇게 하면 계정에서 제공되는 외부 이미지만 서빙됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        remotePatterns: [new URL('https://example.com/account123/**')],
      },
    }
[/code]

객체 형태로도 `remotePatterns`를 설정할 수 있습니다:

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

위 예시는 `next/image`의 `src` 속성이 `https://example.com/account123/`로 시작하고 쿼리 문자열이 없어야 함을 보장합니다. 다른 프로토콜, 호스트명, 포트, 경로는 `400` Bad Request를 반환합니다.

**Wildcard Patterns:**

와일드카드 패턴은 `pathname`과 `hostname` 모두에 사용할 수 있으며 다음 구문을 갖습니다.

  * `*`: 하나의 경로 세그먼트 또는 서브도메인과 일치합니다.
  * `**`: 끝부분의 여러 경로 세그먼트 또는 시작 부분의 여러 서브도메인과 일치합니다. 패턴 중간에서는 사용할 수 없습니다.



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

이는 `image.example.com` 같은 서브도메인을 허용합니다. 쿼리 문자열과 사용자 지정 포트는 여전히 차단됩니다.

> **알아두면 좋아요** : `protocol`, `port`, `pathname`, `search`를 생략하면 와일드카드 `**`가 암묵적으로 적용됩니다. 의도하지 않은 URL이 최적화될 수 있으므로 권장하지 않습니다.

**Query Strings** :

`search` 속성을 사용해 쿼리 문자열도 제한할 수 있습니다:

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

위 예시는 `next/image`의 `src` 속성이 `https://assets.example.com`으로 시작하고 정확한 쿼리 문자열 `?v=1727111025337`을 가져야 함을 보장합니다. 다른 프로토콜이나 쿼리 문자열은 `400` Bad Request를 반환합니다.

#### `loaderFile`[](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile)

`loaderFiles`는 Next.js 대신 사용자 정의 이미지 최적화 서비스를 사용할 수 있게 해줍니다.

next.config.js
[code]
    module.exports = {
      images: {
        loader: 'custom',
        loaderFile: './my/image/loader.js',
      },
    }
[/code]

경로는 프로젝트 루트 기준이어야 합니다. 파일은 URL 문자열을 반환하는 기본 함수를 export해야 합니다:

my/image/loader.js
[code]
[/code]

export default function myImageLoader({ src, width, quality }) {
      return `https://example.com/${src}?w=${width}&q=${quality || 75}`
    }
[/code]

**예시:**

  * [커스텀 이미지 로더 구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#example-loader-configuration)



> 또는 [`loader` prop](https://nextjs.org/docs/pages/api-reference/components/image#loader)을 사용해 `next/image`의 각 인스턴스를 개별적으로 구성할 수 있습니다.

#### `path`[](https://nextjs.org/docs/pages/api-reference/components/image#path)

Image Optimization API의 기본 경로를 변경하거나 접두사를 추가하려면 `path` 속성을 사용하면 됩니다. `path`의 기본값은 `/_next/image`입니다.

next.config.js
[code]
    module.exports = {
      images: {
        path: '/my-prefix/_next/image',
      },
    }
[/code]

#### `deviceSizes`[](https://nextjs.org/docs/pages/api-reference/components/image#devicesizes)

`deviceSizes`는 디바이스 너비 분기점을 나열할 수 있습니다. 이 너비들은 `next/image` 컴포넌트가 [`sizes`](https://nextjs.org/docs/pages/api-reference/components/image#sizes) prop을 사용할 때 사용자 디바이스에 맞는 이미지를 제공하도록 활용됩니다.

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
      },
    }
[/code]

#### `imageSizes`[](https://nextjs.org/docs/pages/api-reference/components/image#imagesizes)

`imageSizes`는 이미지 너비 목록을 지정할 수 있습니다. 이 너비들은 [device sizes](https://nextjs.org/docs/pages/api-reference/components/image#devicesizes) 배열과 결합되어 이미지 [srcset](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/srcset)을 생성할 때 사용되는 전체 크기 배열을 만듭니다.

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        imageSizes: [32, 48, 64, 96, 128, 256, 384],
      },
    }
[/code]

`imageSizes`는 [`sizes`](https://nextjs.org/docs/pages/api-reference/components/image#sizes) prop을 제공하는 이미지에만 사용되며, 이는 해당 이미지가 화면 전체 너비보다 작음을 의미합니다. 따라서 `imageSizes`의 모든 값은 `deviceSizes`의 가장 작은 값보다 작아야 합니다.

#### `qualities`[](https://nextjs.org/docs/pages/api-reference/components/image#qualities)

`qualities`는 이미지 품질 값 목록을 지정할 수 있습니다.

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        qualities: [75],
      },
    }
[/code]

> **알아두면 좋아요**: Next.js 16부터는 이 필드가 필수입니다. 무제한 접근을 허용하면 악의적인 사용자가 의도한 것보다 더 많은 품질 값을 최적화할 수 있기 때문입니다.

허용 목록에 더 많은 이미지 품질 값을 추가할 수 있습니다. 예시는 다음과 같습니다.

next.config.js
[code]
    module.exports = {
      images: {
        qualities: [25, 50, 75, 100],
      },
    }
[/code]

위 예시에서는 25, 50, 75, 100 네 가지 품질만 허용됩니다.

[`quality`](https://nextjs.org/docs/pages/api-reference/components/image#quality) prop이 이 배열의 값과 일치하지 않으면 가장 가까운 허용 값이 사용됩니다.

REST API를 직접 호출할 때 이 배열에 없는 품질을 지정하면 서버는 400 Bad Request 응답을 반환합니다.

#### `formats`[](https://nextjs.org/docs/pages/api-reference/components/image#formats)

`formats`는 사용할 이미지 포맷 목록을 지정할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        // Default
        formats: ['image/webp'],
      },
    }
[/code]

Next.js는 요청의 `Accept` 헤더를 통해 브라우저가 지원하는 이미지 포맷을 자동으로 감지해 최적의 출력 포맷을 결정합니다.

`Accept` 헤더가 구성된 포맷 중 둘 이상과 일치하면 배열에서 첫 번째로 일치하는 포맷이 사용되므로 배열 순서가 중요합니다. 일치하는 포맷이 없거나 원본 이미지가 애니메이션인 경우 원본 포맷이 사용됩니다.

브라우저가 [AVIF를 지원하지 않는](https://caniuse.com/avif) 경우 원본 포맷으로 폴백하도록 AVIF 지원을 활성화할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        formats: ['image/avif'],
      },
    }
[/code]

AVIF와 WebP를 함께 활성화할 수도 있습니다. AVIF를 지원하는 브라우저에서는 AVIF가 우선이며 WebP가 폴백으로 사용됩니다.

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
>   * AVIF는 인코딩에 일반적으로 50% 더 오래 걸리지만 WebP보다 20% 더 작게 압축합니다. 즉, 이미지가 처음 요청될 때는 느릴 수 있지만, 캐시된 후의 후속 요청은 더 빠릅니다.
>   * 여러 포맷을 사용할 경우 Next.js는 각 포맷을 별도로 캐시합니다. 이는 단일 포맷을 사용할 때보다 저장 요구량이 늘어나며, 브라우저 호환성을 위해 AVIF와 WebP 버전이 모두 저장됩니다.
>   * Next.js 앞단에 Proxy/CDN을 두고 자체 호스팅하는 경우 Proxy가 `Accept` 헤더를 전달하도록 구성해야 합니다.
> 

#### `minimumCacheTTL`[](https://nextjs.org/docs/pages/api-reference/components/image#minimumcachettl)

`minimumCacheTTL`은 캐시된 최적화 이미지의 TTL(Time to Live, 초 단위)을 구성할 수 있습니다. 많은 경우 [Static Image Import](https://nextjs.org/docs/app/getting-started/images#local-images)를 사용하면 파일 내용을 해시하고 `Cache-Control` 헤더를 `immutable`로 설정해 이미지를 영구적으로 캐시하므로 더 적합합니다.

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
[code]
    module.exports = {
      images: {
        minimumCacheTTL: 14400, // 4 hours
      },
    }
[/code]

TTL을 늘리면 재검증 횟수를 줄이고 비용을 낮출 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        minimumCacheTTL: 2678400, // 31 days
      },
    }
[/code]

최적화된 이미지의 만료(또는 Max Age)는 `minimumCacheTTL`과 업스트림 이미지의 `Cache-Control` 헤더 중 더 큰 값으로 결정됩니다.

이미지별로 캐싱 동작을 변경해야 한다면 [`headers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)를 구성해 업스트림 이미지(예: `/some-asset.jpg`, `/_next/image` 자체가 아님)에 `Cache-Control` 헤더를 설정할 수 있습니다.

현재 캐시를 무효화하는 메커니즘이 없으므로 `minimumCacheTTL`을 낮게 유지하는 것이 가장 좋습니다. 그렇지 않으면 [`src`](https://nextjs.org/docs/pages/api-reference/components/image#src) prop을 수동으로 변경하거나 `<distDir>/cache/images`의 캐시 파일을 삭제해야 할 수 있습니다.

#### `disableStaticImages`[](https://nextjs.org/docs/pages/api-reference/components/image#disablestaticimages)

`disableStaticImages`는 정적 이미지 import를 비활성화할 수 있습니다.

기본 동작에서는 `import icon from './icon.png'`처럼 정적 파일을 import한 후 `src` 속성에 전달할 수 있습니다. 때로는 이 기능이 다른 플러그인과 충돌해 import가 다르게 동작해야 하는 경우 비활성화하고 싶을 수 있습니다.

`next.config.js`에서 정적 이미지 import를 비활성화할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        disableStaticImages: true,
      },
    }
[/code]

#### `maximumRedirects`[](https://nextjs.org/docs/pages/api-reference/components/image#maximumredirects)

기본 이미지 최적화 로더는 원격 이미지를 가져올 때 최대 3번까지 HTTP 리디렉션을 따릅니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumRedirects: 3,
      },
    }
[/code]

원격 이미지를 가져올 때 따라갈 리디렉션 횟수를 구성할 수 있습니다. 값을 `0`으로 설정하면 리디렉션을 따르지 않습니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumRedirects: 0,
      },
    }
[/code]

#### `maximumResponseBody`[](https://nextjs.org/docs/pages/api-reference/components/image#maximumresponsebody)

기본 이미지 최적화 로더는 최대 50MB 크기의 소스 이미지를 가져옵니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumResponseBody: 50_000_000,
      },
    }
[/code]

모든 소스 이미지가 작다는 것을 알고 있다면, 값을 5MB와 같은 작은 값으로 낮춰 메모리가 제한된 서버를 보호할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        maximumResponseBody: 5_000_000,
      },
    }
[/code]

#### `dangerouslyAllowLocalIP`[](https://nextjs.org/docs/pages/api-reference/components/image#dangerouslyallowlocalip)

사설 네트워크에서 Next.js를 자체 호스팅하는 드문 경우에는 동일 네트워크 내 로컬 IP 주소의 이미지를 최적화하도록 허용하고 싶을 수 있습니다. 내부 네트워크 콘텐츠에 악의적인 사용자가 접근할 수 있으므로 대부분의 사용자에게는 권장되지 않습니다.

기본값은 false입니다.

next.config.js
[code]
    module.exports = {
      images: {
        dangerouslyAllowLocalIP: false,
      },
    }
[/code]

로컬 네트워크의 다른 곳에 호스팅된 원격 이미지를 최적화해야 한다면 값을 true로 설정할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        dangerouslyAllowLocalIP: true,
      },
    }
[/code]

#### `dangerouslyAllowSVG`[](https://nextjs.org/docs/pages/api-reference/components/image#dangerouslyallowsvg)

`dangerouslyAllowSVG`는 SVG 이미지를 제공할 수 있도록 허용합니다.

next.config.js
[code]
    module.exports = {
      images: {
        dangerouslyAllowSVG: true,
      },
    }
[/code]

기본적으로 Next.js는 다음과 같은 이유로 SVG 이미지를 최적화하지 않습니다.

  * SVG는 벡터 포맷이므로 손실 없이 크기를 조정할 수 있습니다.
  * SVG는 HTML/CSS와 동일한 기능을 많이 제공하므로 적절한 [Content Security Policy (CSP) 헤더](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#content-security-policy)가 없으면 취약점이 발생할 수 있습니다.



[`src`](https://nextjs.org/docs/pages/api-reference/components/image#src) prop이 SVG임을 알고 있을 때는 [`unoptimized`](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized) prop을 사용하는 것이 좋습니다. `src`가 `".svg"`로 끝나면 자동으로 적용됩니다.
[code] 
    <Image src="/my-image.svg" unoptimized />
[/code]

또한 브라우저가 이미지를 다운로드하도록 강제하기 위해 `contentDispositionType`을 설정하고, 이미지에 포함된 스크립트 실행을 방지하기 위해 `contentSecurityPolicy`도 설정하는 것이 강력히 권장됩니다.

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

#### `contentDispositionType`[](https://nextjs.org/docs/pages/api-reference/components/image#contentdispositiontype)

`contentDispositionType`은 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) 헤더를 구성할 수 있습니다.

next.config.js
[code]
    module.exports = {
      images: {
        contentDispositionType: 'inline',
      },
    }
[/code]

#### `contentSecurityPolicy`[](https://nextjs.org/docs/pages/api-reference/components/image#contentsecuritypolicy)

`contentSecurityPolicy`는 이미지에 대한 [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) 헤더를 구성할 수 있습니다. 이는 이미지에 포함된 스크립트 실행을 방지하기 위한 [`dangerouslyAllowSVG`](https://nextjs.org/docs/pages/api-reference/components/image#dangerouslyallowsvg) 사용 시 특히 중요합니다.

next.config.js
[code]

module.exports = {
      images: {
        contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
      },
    }
[/code]

기본적으로 [loader](https://nextjs.org/docs/pages/api-reference/components/image#loader)는 API가 임의의 원격 이미지를 제공할 수 있으므로 추가적인 보호를 위해 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) 헤더를 `attachment`로 설정합니다.

기본값은 `attachment`이며, 이미지를 직접 방문할 때 브라우저가 해당 이미지를 다운로드하도록 강제합니다. 이는 [`dangerouslyAllowSVG`](https://nextjs.org/docs/pages/api-reference/components/image#dangerouslyallowsvg)가 true일 때 특히 중요합니다.

원한다면 `inline`을 구성하여 브라우저가 이미지를 직접 방문할 때 다운로드 없이 렌더링하도록 허용할 수 있습니다.

### Deprecated configuration options[](https://nextjs.org/docs/pages/api-reference/components/image#deprecated-configuration-options)

#### `domains`[](https://nextjs.org/docs/pages/api-reference/components/image#domains)

> **경고** : 악의적인 사용자로부터 애플리케이션을 보호하기 위해 엄격한 [`remotePatterns`](https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns)를 권장하면서 Next.js 14부터 더 이상 사용되지 않습니다.

[`remotePatterns`](https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns)와 유사하게 `domains` 구성은 외부 이미지에 대해 허용된 호스트 이름 목록을 제공하는 데 사용할 수 있습니다. 그러나 `domains` 구성은 와일드카드 패턴 매칭을 지원하지 않으며 프로토콜, 포트 또는 경로 이름을 제한할 수 없습니다.

대부분의 원격 이미지 서버는 여러 테넌트가 공유하므로, 의도한 이미지만 최적화되도록 `remotePatterns`를 사용하는 것이 더 안전합니다.

다음은 `next.config.js` 파일에서 `domains` 속성을 사용하는 예입니다:

next.config.js
[code]
    module.exports = {
      images: {
        domains: ['assets.acme.com'],
      },
    }
[/code]

## Functions[](https://nextjs.org/docs/pages/api-reference/components/image#functions)

### `getImageProps`[](https://nextjs.org/docs/pages/api-reference/components/image#getimageprops)

`getImageProps` 함수는 내부 `<img>` 요소에 전달될 props를 가져와 다른 컴포넌트, 스타일, 캔버스 등에 전달할 때 사용할 수 있습니다.
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

이는 React `useState()` 호출을 피하므로 성능 향상에 도움이 될 수 있지만, 플레이스홀더가 제거되지 않으므로 [`placeholder`](https://nextjs.org/docs/pages/api-reference/components/image#placeholder) prop과 함께 사용할 수 없습니다.

## Known browser bugs[](https://nextjs.org/docs/pages/api-reference/components/image#known-browser-bugs)

이 `next/image` 컴포넌트는 브라우저 네이티브 [지연 로딩](https://caniuse.com/loading-lazy-attr)을 사용하며, Safari 15.4 이전의 오래된 브라우저에서는 eager 로딩으로 폴백될 수 있습니다. blur-up 플레이스홀더를 사용할 때는 Safari 12 이전 브라우저에서 빈 플레이스홀더로 폴백합니다. `width`/`height`가 `auto`인 스타일을 사용할 경우, 속성에서 [종횡비를 유지](https://caniuse.com/mdn-html_elements_img_aspect_ratio_computed_from_attributes)하지 않는 Safari 15 이전 브라우저에서 [Layout Shift](https://web.dev/cls/)가 발생할 수 있습니다. 자세한 내용은 [이 MDN 동영상](https://www.youtube.com/watch?v=4-d_SoCHeWE)을 확인하세요.

  * [Safari 15 - 16.3](https://bugs.webkit.org/show_bug.cgi?id=243601)은 로딩 중 회색 테두리를 표시합니다. Safari 16.4에서 [이 문제가 수정되었습니다](https://webkit.org/blog/13966/webkit-features-in-safari-16-4/#:~:text=Now%20in%20Safari%2016.4%2C%20a%20gray%20line%20no%20longer%20appears%20to%20mark%20the%20space%20where%20a%20lazy%2Dloaded%20image%20will%20appear%20once%20it%E2%80%99s%20been%20loaded.). 가능한 해결책:
    * CSS `@supports (font: -apple-system-body) and (-webkit-appearance: none) { img[loading="lazy"] { clip-path: inset(0.6px) } }` 사용
    * 이미지가 퍼스트 뷰에 있다면 [`loading="eager"`](https://nextjs.org/docs/pages/api-reference/components/image#loading) 사용
  * [Firefox 67+](https://bugzilla.mozilla.org/show_bug.cgi?id=1556156)는 로딩 중 흰색 배경을 표시합니다. 가능한 해결책:
    * [AVIF `formats`](https://nextjs.org/docs/pages/api-reference/components/image#formats) 활성화
    * [`placeholder`](https://nextjs.org/docs/pages/api-reference/components/image#placeholder) 사용



## Examples[](https://nextjs.org/docs/pages/api-reference/components/image#examples)

### Styling images[](https://nextjs.org/docs/pages/api-reference/components/image#styling-images)

Image 컴포넌트 스타일링은 일반 `<img>` 요소 스타일링과 비슷하지만 몇 가지 지침을 기억해야 합니다:

`styled-jsx` 대신 `className` 또는 `style`을 사용하세요. 대부분의 경우 `className` prop 사용을 권장합니다. 이는 가져온 [CSS Module](https://nextjs.org/docs/app/getting-started/css), [전역 스타일시트](https://nextjs.org/docs/app/getting-started/css#global-css) 등일 수 있습니다.
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

`fill`을 사용할 때 부모 요소는 `position: relative` 또는 `display: block`이어야 합니다. 해당 레이아웃 모드에서 이미지 요소를 올바르게 렌더링하는 데 필요합니다.
[code] 
    <div style={{ position: 'relative' }}>
      <Image fill src="/my-image.png" alt="My Image" />
    </div>
[/code]

[styled-jsx](https://nextjs.org/docs/app/guides/css-in-js)는 현재 컴포넌트에 스코프되므로(`global`로 표시하지 않는 한) 사용할 수 없습니다.

### Responsive images with a static export[](https://nextjs.org/docs/pages/api-reference/components/image#responsive-images-with-a-static-export)

정적 이미지를 import하면 Next.js는 파일을 기반으로 너비와 높이를 자동으로 설정합니다. 스타일을 설정해 이미지를 반응형으로 만들 수 있습니다:
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

### Responsive images with a remote URL[](https://nextjs.org/docs/pages/api-reference/components/image#responsive-images-with-a-remote-url)

소스 이미지가 동적이거나 원격 URL이라면, Next.js가 종횡비를 계산할 수 있도록 width와 height props를 제공해야 합니다:

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

  * [Demo the image responsive to viewport](https://image-component.nextjs.gallery/responsive)



### Responsive image with `fill`[](https://nextjs.org/docs/pages/api-reference/components/image#responsive-image-with-fill)

이미지의 종횡비를 모를 경우 [`fill` prop](https://nextjs.org/docs/pages/api-reference/components/image#fill)에 `objectFit` prop을 `cover`로 설정해 부모 컨테이너의 전체 너비를 채우게 만들 수 있습니다.
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

### Background Image[](https://nextjs.org/docs/pages/api-reference/components/image#background-image)

`fill` prop을 사용해 이미지가 화면 전체 영역을 덮도록 만들 수 있습니다:
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

다양한 스타일로 Image 컴포넌트를 사용하는 예시는 [Image Component Demo](https://image-component.nextjs.gallery)에서 확인하세요.

### Remote images[](https://nextjs.org/docs/pages/api-reference/components/image#remote-images)

원격 이미지를 사용하려면 `src` 속성을 URL 문자열로 지정해야 합니다.

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

Next.js는 빌드 과정에서 원격 파일에 접근할 수 없으므로, [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), 선택적인 [`blurDataURL`](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl) props를 수동으로 제공해야 합니다.

`width`와 `height` 속성은 이미지의 올바른 종횡비를 추론해 로딩 중 레이아웃 시프트를 방지하는 데 사용됩니다. `width`와 `height`는 렌더링된 이미지 파일의 실제 크기를 결정하지 않습니다.

이미지를 안전하게 최적화하려면 `next.config.js`에 지원되는 URL 패턴 목록을 정의하세요. 악의적 사용을 방지하려면 가능한 한 구체적으로 지정해야 합니다. 예를 들어 아래 구성은 특정 AWS S3 버킷의 이미지만 허용합니다:

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
        ],
      },
    }
[/code]

### Theme detection[](https://nextjs.org/docs/pages/api-reference/components/image#theme-detection)

라이트 모드와 다크 모드에 서로 다른 이미지를 표시하고 싶다면, 두 개의 `<Image>` 컴포넌트를 감싼 새 컴포넌트를 만들고 CSS 미디어 쿼리에 따라 올바른 이미지를 노출할 수 있습니다.

components/theme-image.module.css
[code]
    .imgDark {
      display: none;
    }
     
    @media (prefers-color-scheme: dark) {
[/code]

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

> **알아두면 좋아요**: `loading="lazy"`의 기본 동작은 올바른 이미지 하나만 로드되도록 보장합니다. `preload`나 `loading="eager"`를 사용하면 두 이미지가 모두 로드되므로 사용할 수 없습니다. 대신 [`fetchPriority="high"`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/fetchPriority)를 사용할 수 있습니다.

직접 사용해 보세요:

  * [라이트/다크 모드 테마 감지 데모](https://image-component.nextjs.gallery/theme)



### 아트 디렉션[](https://nextjs.org/docs/pages/api-reference/components/image#art-direction)

모바일과 데스크톱에 서로 다른 이미지를 표시하고 싶다면(이를 종종 [Art Direction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#art_direction)이라고 부릅니다) `getImageProps()`에 서로 다른 `src`, `width`, `height`, `quality` prop을 전달하면 됩니다.

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

### 배경 CSS[](https://nextjs.org/docs/pages/api-reference/components/image#background-css)

배경 이미지를 최적화하기 위해 `srcSet` 문자열을 [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/image/image-set) CSS 함수로 변환할 수도 있습니다.

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

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/components/image#version-history)

Version| Changes  
---|---  
`v16.1.2`| `maximumResponseBody` 구성이 추가되었습니다.  
`v16.0.0`| `qualities` 기본 구성이 `[75]`로 변경되었고, `preload` prop이 추가되었으며, `priority` prop이 사용 중단되었습니다. `dangerouslyAllowLocalIP` 구성과 `maximumRedirects` 구성도 추가되었습니다.  
`v15.3.0`| `remotePatterns`가 `URL` 객체 배열을 지원합니다.  
`v15.0.0`| `contentDispositionType` 기본 구성 값이 `attachment`로 변경되었습니다.  
`v14.2.23`| `qualities` 구성이 추가되었습니다.  
`v14.2.15`| `decoding` prop과 `localPatterns` 구성이 추가되었습니다.  
`v14.2.14`| `remotePatterns.search` prop이 추가되었습니다.  
`v14.2.0`| `overrideSrc` prop이 추가되었습니다.  
`v14.1.0`| `getImageProps()`가 안정화되었습니다.  
`v14.0.0`| `onLoadingComplete` prop과 `domains` 구성이 사용 중단되었습니다.  
`v13.4.14`| `placeholder` prop이 `data:/image...`을 지원합니다.  
`v13.2.0`| `contentDispositionType` 구성이 추가되었습니다.  
`v13.0.6`| `ref` prop이 추가되었습니다.  
`v13.0.0`| `next/image` import가 `next/legacy/image`로 이름이 바뀌었고, `next/future/image` import가 `next/image`로 바뀌었습니다. import를 안전하게 자동 변경하기 위한 [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-to-legacy-image)가 제공됩니다. `<span>` 래퍼가 제거되었습니다. `layout`, `objectFit`, `objectPosition`, `lazyBoundary`, `lazyRoot` prop이 제거되었습니다. `alt`는 필수가 되었고 `onLoadingComplete`는 `img` 요소 참조를 받습니다. 내장 로더 구성도 제거되었습니다.  
`v12.3.0`| `remotePatterns`와 `unoptimized` 구성이 안정화되었습니다.  
`v12.2.0`| 실험적 `remotePatterns`와 실험적 `unoptimized` 구성이 추가되었고 `layout="raw"`가 제거되었습니다.  
`v12.1.1`| `style` prop이 추가되고, `layout="raw"`에 대한 실험적 지원이 추가되었습니다.  
`v12.1.0`| `dangerouslyAllowSVG`와 `contentSecurityPolicy` 구성이 추가되었습니다.  
`v12.0.9`| `lazyRoot` prop이 추가되었습니다.  
`v12.0.0`| `formats` 구성이 추가되었습니다.  
AVIF 지원이 추가되었습니다.  
래퍼 `<div>`가 `<span>`으로 변경되었습니다.  
`v11.1.0`| `onLoadingComplete`와 `lazyBoundary` prop이 추가되었습니다.  
`v11.0.0`| `src` prop이 정적 import를 지원합니다.  
`placeholder` prop이 추가되었습니다.  
`blurDataURL` prop이 추가되었습니다.  
`v10.0.5`| `loader` prop이 추가되었습니다.  
`v10.0.1`| `layout` prop이 추가되었습니다.  
`v10.0.0`| `next/image`가 도입되었습니다.  
  
도움이 되었나요?

지원됨.

보내기
