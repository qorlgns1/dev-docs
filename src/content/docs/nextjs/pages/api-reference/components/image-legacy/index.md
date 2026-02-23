---
title: '컴포넌트: Image (Legacy)'
description: '이는 더 이상 권장되지 않는 레거시 API입니다. 하위 호환성을 위해 계속 지원됩니다.'
---

# 컴포넌트: Image (Legacy) | Next.js

소스 URL: https://nextjs.org/docs/pages/api-reference/components/image-legacy

[API 참고](https://nextjs.org/docs/pages/api-reference)[컴포넌트](https://nextjs.org/docs/pages/api-reference/components)Image (Legacy)

# Image (Legacy)

이는 더 이상 권장되지 않는 레거시 API입니다. 하위 호환성을 위해 계속 지원됩니다.

마지막 업데이트: 2026년 2월 20일

Next.js 13부터 `next/image` 컴포넌트가 성능과 개발자 경험을 모두 향상시키도록 다시 작성되었습니다. 하위 호환 업그레이드 경로를 제공하기 위해 기존 `next/image`는 `next/legacy/image`로 이름이 변경되었습니다.

> **경고** : `next/legacy/image`는 사용 중단(deprecated) 상태이며 향후 Next.js 버전에서 제거됩니다. [`next/image`](https://nextjs.org/docs/app/api-reference/components/image)를 대신 사용하세요.

## 비교[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#comparison)

`next/legacy/image`와 비교했을 때 새로운 `next/image` 컴포넌트는 다음과 같이 변경되었습니다.

  * [네이티브 계산 종횡비](https://caniuse.com/mdn-html_elements_img_aspect_ratio_computed_from_attributes)를 사용하도록 `<img>` 요소 주위의 `<span>` 래퍼를 제거합니다.
  * 표준 `style` prop 지원을 추가합니다.
    * `style` 또는 `className`을 사용하도록 `layout` prop을 제거합니다.
    * `style` 또는 `className`을 사용하도록 `objectFit` prop을 제거합니다.
    * `style` 또는 `className`을 사용하도록 `objectPosition` prop을 제거합니다.
  * [네이티브 지연 로딩](https://caniuse.com/loading-lazy-attr)을 사용하도록 `IntersectionObserver` 구현을 제거합니다.
    * 네이티브 대응이 없으므로 `lazyBoundary` prop을 제거합니다.
    * 네이티브 대응이 없으므로 `lazyRoot` prop을 제거합니다.
  * [`loader`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) prop을 사용하도록 `loader` 구성(config)을 제거합니다.
  * `alt` prop을 선택 사항에서 필수로 변경했습니다.
  * `<img>` 요소 참조를 받도록 `onLoadingComplete` 콜백을 변경했습니다.

## 필수 Props[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#required-props)

`<Image />` 컴포넌트에는 다음 속성이 필요합니다.

### src[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src)

다음 중 하나여야 합니다.

  * [정적으로 import된](https://nextjs.org/docs/pages/api-reference/components/image#src) 이미지 파일
  * 경로 문자열. 이는 [`loader`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) prop 또는 [loader 구성](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader-configuration)에 따라 절대 외부 URL이거나 내부 경로일 수 있습니다.

기본 [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader)를 사용할 때 소스 이미지에 대해 다음 사항을 고려하세요.

  * src가 외부 URL이면 [remotePatterns](https://nextjs.org/docs/pages/api-reference/components/image-legacy#remote-patterns)도 구성해야 합니다.
  * src가 [애니메이션](https://nextjs.org/docs/pages/api-reference/components/image-legacy#animated-images)이거나 알려진 형식(JPEG, PNG, WebP, AVIF, GIF, TIFF)이 아니면 이미지는 있는 그대로 제공됩니다.
  * src가 SVG 형식이면 `unoptimized` 또는 `dangerouslyAllowSVG`가 활성화되지 않는 한 차단됩니다.

### width[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#width)

`width` 속성은 [`layout`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#layout) 및 [`sizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#sizes)에 따라 픽셀 단위의 _렌더링된_ 너비 또는 _원본_ 너비를 나타낼 수 있습니다.

`layout="intrinsic"` 또는 `layout="fixed"`를 사용할 때 `width` 속성은 픽셀 단위의 _렌더링된_ 너비를 의미하므로 이미지 표시 크기에 영향을 줍니다.

`layout="responsive"` 또는 `layout="fill"`을 사용할 때 `width` 속성은 픽셀 단위의 _원본_ 너비를 의미하므로 종횡비에만 영향을 줍니다.

`width` 속성은 [정적으로 import된 이미지](https://nextjs.org/docs/pages/api-reference/components/image#src) 또는 `layout="fill"`을 사용하는 경우를 제외하면 필수입니다.

### height[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#height)

`height` 속성은 [`layout`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#layout) 및 [`sizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#sizes)에 따라 픽셀 단위의 _렌더링된_ 높이 또는 _원본_ 높이를 나타낼 수 있습니다.

`layout="intrinsic"` 또는 `layout="fixed"`를 사용할 때 `height` 속성은 픽셀 단위의 _렌더링된_ 높이를 의미하므로 이미지 표시 크기에 영향을 줍니다.

`layout="responsive"` 또는 `layout="fill"`을 사용할 때 `height` 속성은 픽셀 단위의 _원본_ 높이를 의미하므로 종횡비에만 영향을 줍니다.

`height` 속성은 [정적으로 import된 이미지](https://nextjs.org/docs/pages/api-reference/components/image#src) 또는 `layout="fill"`을 사용하는 경우를 제외하면 필수입니다.

## 선택 Props[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#optional-props)

`<Image />` 컴포넌트는 필수 속성 외에도 여러 추가 속성을 허용합니다. 이 섹션에서는 Image 컴포넌트에서 가장 일반적으로 사용하는 속성을 설명합니다. 드물게 사용하는 속성에 대한 자세한 내용은 [고급 Props](https://nextjs.org/docs/pages/api-reference/components/image-legacy#advanced-props) 섹션을 참고하세요.

### layout[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#layout)

뷰포트 크기가 변할 때 이미지의 레이아웃 동작입니다.

`layout`| 동작| `srcSet`| `sizes`| 래퍼 및 사이저 존재
---|---|---|---|---
`intrinsic` (default)| 컨테이너 너비에 맞도록 _축소_하며 이미지 크기까지 확장| `1x`, `2x` ( [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)에 기반)| 해당 없음| yes
`fixed`| `width`와 `height`에 정확히 맞게 설정| `1x`, `2x` ( [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)에 기반)| 해당 없음| yes
`responsive`| 컨테이너 너비에 맞게 크기 조절| `640w`, `750w`, ... `2048w`, `3840w` ( [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)와 [deviceSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)에 기반)| `100vw`| yes
`fill`| 컨테이너를 채우도록 X, Y 축 모두에서 확장| `640w`, `750w`, ... `2048w`, `3840w` ( [imageSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)와 [deviceSizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)에 기반)| `100vw`| yes

  * [`intrinsic` 레이아웃(기본값) 데모](https://image-legacy-component.nextjs.gallery/layout-intrinsic)
    * `intrinsic`일 때 이미지는 작은 뷰포트에서는 크기를 줄이고 큰 뷰포트에서는 원래 크기를 유지합니다.
  * [`fixed` 레이아웃 데모](https://image-legacy-component.nextjs.gallery/layout-fixed)
    * `fixed`일 때 이미지는 뷰포트가 변해도 크기가 변하지 않아 네이티브 `img` 요소와 비슷하게 반응형이 아닙니다.
  * [`responsive` 레이아웃 데모](https://image-legacy-component.nextjs.gallery/layout-responsive)
    * `responsive`일 때 이미지는 작은 뷰포트에서는 크기를 줄이고 큰 뷰포트에서는 크기를 늘립니다.
    * 부모 요소가 스타일시트에서 `display: block`을 사용하도록 하세요.
  * [`fill` 레이아웃 데모](https://image-legacy-component.nextjs.gallery/layout-fill)
    * `fill`일 때 이미지는 부모 요소가 relative인 경우 부모 요소의 너비와 높이를 모두 채우도록 늘어납니다.
    * 보통 [`objectFit`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#objectfit) 속성과 함께 사용됩니다.
    * 부모 요소의 스타일시트에 `position: relative`를 지정하세요.
  * [배경 이미지 데모](https://image-legacy-component.nextjs.gallery/background)

### loader[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader)

URL을 해석하는 데 사용하는 커스텀 함수입니다. Image 컴포넌트에 loader를 prop으로 설정하면 [`next.config.js`의 `images` 섹션](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader-configuration)에 정의된 기본 loader를 재정의합니다.

`loader`는 다음 매개변수를 받아 이미지에 대한 URL 문자열을 반환하는 함수입니다.

  * [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src)
  * [`width`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#width)
  * [`quality`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#quality)

커스텀 loader를 사용하는 예시는 다음과 같습니다.
```
    import Image from 'next/legacy/image'

    const myLoader = ({ src, width, quality }) => {
      return `https://example.com/${src}?w=${width}&q=${quality || 75}`
    }

    const MyImage = (props) => {
      return (
        <Image
          loader={myLoader}
          src="me.png"
          alt="Picture of the author"
          width={500}
          height={500}
        />
      )
    }
```

### sizes[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#sizes)

다양한 분기점에서 이미지가 얼마나 넓어질지에 대한 정보를 제공하는 문자열입니다. `sizes` 값은 `layout="responsive"` 또는 `layout="fill"`을 사용하는 이미지의 성능에 큰 영향을 줍니다. `layout="intrinsic"` 또는 `layout="fixed"`를 사용하는 이미지에는 무시됩니다.

`sizes` 속성은 이미지 성능과 관련하여 두 가지 중요한 역할을 합니다.

첫째, 브라우저는 `next/legacy/image`가 자동으로 생성한 소스 집합에서 어떤 크기의 이미지를 다운로드할지 결정할 때 `sizes` 값을 사용합니다. 브라우저가 선택할 때는 페이지에서 이미지의 크기를 아직 알지 못하므로 뷰포트와 같거나 더 큰 이미지를 선택합니다. `sizes` 속성을 사용하면 실제로 전체 화면보다 작은 이미지일 것임을 브라우저에 알려줄 수 있습니다. `sizes` 값을 지정하지 않으면 기본값 `100vw`(전체 화면 너비)가 사용됩니다.

둘째, `sizes` 값이 구문 분석되어 자동 생성된 소스 집합의 값을 잘라내는 데 사용됩니다. 뷰포트 너비의 비율을 나타내는 `50vw`와 같은 값이 `sizes`에 포함되어 있으면, 소스 집합에서 필요 이상으로 작은 값은 제거됩니다.

예를 들어 스타일링으로 인해 모바일에서는 전체 너비, 태블릿에서는 2열, 데스크톱에서는 3열 레이아웃을 사용할 것임을 알고 있다면 아래와 같은 sizes 속성을 포함해야 합니다.
```
    import Image from 'next/legacy/image'
    const Example = () => (
      <div className="grid-element">
        <Image
          src="/example.png"
          layout="fill"
          sizes="(max-width: 768px) 100vw,
                  (max-width: 1200px) 50vw,
                  33vw"
        />
      </div>
    )
```

이 예시 `sizes`는 성능 지표에 큰 영향을 줄 수 있습니다. `33vw` 사이즈가 없으면 서버에서 선택되는 이미지는 실제 필요 크기보다 3배 넓습니다. 파일 크기는 너비의 제곱에 비례하므로 `sizes` 없이 이미지는 필요보다 9배 큰 용량으로 다운로드됩니다.

`srcset`과 `sizes`에 대해 더 알아보기:

  * [web.dev](https://web.dev/learn/design/responsive-images/#sizes)
  * [mdn](https://developer.mozilla.org/docs/Web/HTML/Element/img#attr-sizes)

### quality[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#quality)

최적화된 이미지의 품질로, `1`에서 `100` 사이의 정수입니다. `100`이 가장 높은 품질이며 기본값은 `75`입니다.

### priority[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#priority)

`true`일 때 이미지는 고우선순위로 간주되어 [preload](https://web.dev/preload-responsive-images/)됩니다. `priority`를 사용하는 이미지의 경우 지연 로딩이 자동으로 비활성화됩니다.

[LCP(Largest Contentful Paint)](https://nextjs.org/learn/seo/web-performance/lcp) 요소로 감지된 모든 이미지에는 `priority` 속성을 사용하는 것이 좋습니다. 뷰포트 크기에 따라 LCP 요소가 달라질 수 있으므로 여러 개의 우선순위 이미지를 두어도 괜찮습니다.

이미지가 퍼스트 뷰 영역(above the fold)에 표시될 때만 사용해야 하며, 기본값은 `false`입니다.

### placeholder[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#placeholder)

이미지가 로딩되는 동안 사용할 플레이스홀더입니다. 가능한 값은 `blur` 또는 `empty`이며, 기본값은 `empty`입니다.

`blur`인 경우 [`blurDataURL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#blurdataurl) 속성이 플레이스홀더로 사용됩니다. [정적 import](https://nextjs.org/docs/pages/api-reference/components/image#src)에서 가져온 `src` 객체가 `.jpg`, `.png`, `.webp`, `.avif` 이미지라면 `blurDataURL`이 자동으로 채워집니다.

동적 이미지에는 반드시 [`blurDataURL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#blurdataurl) 속성을 제공해야 합니다. [Plaiceholder](https://github.com/joe-bell/plaiceholder)와 같은 솔루션을 활용해 `base64`를 생성할 수 있습니다.

`empty`인 경우 이미지가 로딩되는 동안 플레이스홀더 없이 빈 공간만 표시됩니다.

직접 사용해 보세요:

  * [`blur` 플레이스홀더 데모](https://image-legacy-component.nextjs.gallery/placeholder)
  * `blurDataURL` prop으로 셔머 효과 데모(https://image-legacy-component.nextjs.gallery/shimmer)
  * `blurDataURL` prop으로 색상 효과 데모(https://image-legacy-component.nextjs.gallery/color)

## 고급 Props[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#advanced-props)

일부 상황에서는 더 고급 기능이 필요할 수 있습니다. `<Image />` 컴포넌트는 다음 고급 속성을 선택적으로 받습니다.

### style[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#style)

기본 이미지 요소에 [CSS 스타일을 전달](https://developer.mozilla.org/docs/Web/HTML/Element/style)할 수 있습니다.

모든 `layout` 모드는 이미지 요소에 자체 스타일을 적용하며, 이러한 자동 스타일이 `style` prop보다 우선합니다.

필수 `width` 및 `height` prop이 스타일과 상호작용할 수 있다는 점도 염두에 두세요. 스타일로 이미지의 `width`를 수정하면 `height="auto"` 스타일도 함께 설정해야 이미지 왜곡을 피할 수 있습니다.

### objectFit[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#objectfit)

`layout="fill"`을 사용할 때 이미지가 부모 컨테이너에 맞춰지는 방식을 정의합니다.

이 값은 `src` 이미지의 [object-fit CSS 속성](https://developer.mozilla.org/docs/Web/CSS/object-fit)에 전달됩니다.

### objectPosition[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#objectposition)

`layout="fill"`을 사용할 때 이미지가 부모 요소 내에서 배치되는 방식을 정의합니다.

이 값은 이미지에 적용되는 [object-position CSS 속성](https://developer.mozilla.org/docs/Web/CSS/object-position)에 전달됩니다.

### onLoadingComplete[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#onloadingcomplete)

이미지가 완전히 로드되고 [플레이스홀더](https://nextjs.org/docs/pages/api-reference/components/image-legacy#placeholder)가 제거된 후 호출되는 콜백 함수입니다.

`onLoadingComplete` 함수는 다음 속성을 가진 객체 하나를 매개변수로 받습니다:

  * [`naturalWidth`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/naturalWidth)
  * [`naturalHeight`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/naturalHeight)

### loading[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loading)

이미지의 로딩 동작입니다. 기본값은 `lazy`입니다.

`lazy`인 경우 뷰포트에서 계산된 거리까지 도달할 때까지 이미지 로딩을 지연합니다.

`eager`인 경우 이미지를 즉시 로딩합니다.

[자세히 알아보기](https://developer.mozilla.org/docs/Web/HTML/Element/img#attr-loading)

### blurDataURL[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#blurdataurl)

`src` 이미지가 성공적으로 로드되기 전까지 플레이스홀더로 사용할 [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)입니다. [`placeholder="blur"`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#placeholder)와 함께 사용할 때만 효과가 있습니다.

`base64`로 인코딩된 이미지여야 하며, 확대 후 블러 처리되기 때문에 10px 이하의 매우 작은 이미지를 권장합니다. 더 큰 이미지를 플레이스홀더로 사용하면 애플리케이션 성능이 저하될 수 있습니다.

직접 사용해 보세요:

  * 기본 `blurDataURL` prop 데모(https://image-legacy-component.nextjs.gallery/placeholder)
  * `blurDataURL` prop으로 셔머 효과 데모(https://image-legacy-component.nextjs.gallery/shimmer)
  * `blurDataURL` prop으로 색상 효과 데모(https://image-legacy-component.nextjs.gallery/color)

이미지와 어울리는 [단색 Data URL을 생성](https://png-pixel.com)할 수도 있습니다.

### lazyBoundary[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#lazyboundary)

뷰포트와 이미지의 교차를 감지해 지연 [로딩](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loading)을 트리거할 때 사용되는 경계 상자입니다(문법은 margin 속성과 유사). 기본값은 `"200px"`입니다.

이미지가 루트 문서 외의 스크롤 가능한 부모 요소 안에 중첩되어 있다면 [lazyRoot](https://nextjs.org/docs/pages/api-reference/components/image-legacy#lazyroot) prop도 지정해야 합니다.

[자세히 알아보기](https://developer.mozilla.org/docs/Web/API/IntersectionObserver/rootMargin)

### lazyRoot[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#lazyroot)

스크롤 가능한 부모 요소를 가리키는 React [Ref](https://react.dev/learn/referencing-values-with-refs)입니다. 기본값은 `null`(문서 뷰포트)입니다.

Ref는 DOM 요소이거나, 기본 DOM 요소로 [전달된 Ref를 전달](https://react.dev/reference/react/forwardRef)하는 React 컴포넌트를 가리켜야 합니다.

**DOM 요소를 가리키는 예시**
```
    import Image from 'next/legacy/image'
    import React from 'react'

    const Example = () => {
      const lazyRoot = React.useRef(null)

      return (
        <div ref={lazyRoot} style={{ overflowX: 'scroll', width: '500px' }}>
          <Image lazyRoot={lazyRoot} src="/one.jpg" width="500" height="500" />
          <Image lazyRoot={lazyRoot} src="/two.jpg" width="500" height="500" />
        </div>
      )
    }
```

**React 컴포넌트를 가리키는 예시**
```
    import Image from 'next/legacy/image'
    import React from 'react'

    const Container = React.forwardRef((props, ref) => {
      return (
        <div ref={ref} style={{ overflowX: 'scroll', width: '500px' }}>
          {props.children}
        </div>
      )
    })

    const Example = () => {
      const lazyRoot = React.useRef(null)

      return (
        <Container ref={lazyRoot}>
          <Image lazyRoot={lazyRoot} src="/one.jpg" width="500" height="500" />
          <Image lazyRoot={lazyRoot} src="/two.jpg" width="500" height="500" />
        </Container>
      )
    }
```

[자세히 알아보기](https://developer.mozilla.org/docs/Web/API/IntersectionObserver/root)

### unoptimized[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#unoptimized)

`true`일 때 원본 이미지가 품질, 크기, 형식 변경 없이 `src`에서 그대로 제공됩니다. 기본값은 `false`입니다.

1KB 미만의 작은 이미지, 벡터 이미지(SVG), 애니메이션 이미지(GIF)처럼 최적화 이점이 없는 이미지에 유용합니다.
```
    import Image from 'next/image'

    const UnoptimizedImage = (props) => {
      return <Image {...props} unoptimized />
    }
```

Next.js 12.3.0부터는 `next.config.js`를 다음 설정으로 업데이트하여 모든 이미지에 이 prop을 적용할 수 있습니다:

next.config.js
```
    module.exports = {
      images: {
        unoptimized: true,
      },
    }
```

## 기타 Props[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#other-props)

`<Image />` 컴포넌트의 다른 속성은 다음 항목을 제외하고 기본 `img` 요소에 전달됩니다:

  * `srcSet`. 대신 [Device Sizes](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)를 사용하세요.
  * `ref`. 대신 [`onLoadingComplete`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#onloadingcomplete)를 사용하세요.
  * `decoding`. 항상 `"async"`입니다.

## 구성 옵션[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#configuration-options)

### Remote Patterns[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#remote-patterns)

애플리케이션을 악의적인 사용자로부터 보호하려면 외부 이미지를 사용하기 위한 구성이 필요합니다. 이렇게 하면 Next.js Image Optimization API가 귀하의 계정에서 허용한 외부 이미지만 제공하도록 보장합니다. 아래와 같이 `next.config.js` 파일의 `remotePatterns` 속성으로 외부 이미지를 구성할 수 있습니다:

next.config.js
```
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
```

> **알아두면 좋아요**: 위 예시는 `next/legacy/image`의 `src` 속성이 `https://example.com/account123/`로 시작하고 쿼리 문자열을 포함하지 않아야 함을 보장합니다. 다른 protocol, hostname, port 또는 일치하지 않는 경로는 400 Bad Request로 응답합니다.

다음은 `hostname`에 와일드카드 패턴을 사용하는 `next.config.js`의 `remotePatterns` 예시입니다:

next.config.js
```
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
```

> **알아두면 좋아요**: 위 예시는 `next/legacy/image`의 `src`가 `https://img1.example.com`이나 `https://me.avatar.example.com` 등 임의의 서브도메인으로 시작해야 하며, port나 쿼리 문자열을 포함할 수 없도록 합니다. 다른 protocol이나 일치하지 않는 hostname은 400 Bad Request로 응답합니다.

와일드카드 패턴은 `pathname`과 `hostname` 모두에서 사용할 수 있으며 다음 문법을 가집니다:

  * `*`는 하나의 경로 세그먼트 또는 서브도메인과 일치
  * `**`는 끝부분의 여러 경로 세그먼트 또는 시작 부분의 여러 서브도메인과 일치

`**` 문법은 패턴 중간에서는 작동하지 않습니다.

> **알아두면 좋아요**: `protocol`, `port`, `pathname`, `search`를 생략하면 와일드카드 `**`가 암묵적으로 적용됩니다. 의도하지 않은 URL까지 최적화하도록 허용될 수 있으므로 권장되지 않습니다.

다음은 `search`를 사용하는 `next.config.js`의 `remotePatterns` 예시입니다:

next.config.js
```
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
```

> **알아두면 좋아요**: 위 예시는 `next/legacy/image`의 `src`가 `https://assets.example.com`으로 시작하고 정확히 `?v=1727111025337` 쿼리 문자열을 포함해야 함을 보장합니다. 다른 protocol이나 쿼리 문자열은 400 Bad Request로 응답합니다.

### Domains[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#domains)

> **경고** : 악의적인 사용자를 막기 위해 Next.js 14부터는 엄격한 [`remotePatterns`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#remote-patterns)를 권장합니다. 해당 도메인에서 제공되는 모든 콘텐츠를 직접 소유하고 있을 때만 `domains` 를 사용하세요.

[`remotePatterns`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#remote-patterns)와 유사하게 `domains` 구성은 외부 이미지에 허용할 호스트 이름 목록을 제공하는 데 사용할 수 있습니다.

그러나 `domains` 구성은 와일드카드 패턴 매칭을 지원하지 않으며 프로토콜, 포트 또는 경로 이름을 제한할 수 없습니다.

아래는 `next.config.js` 파일에서 `domains` 속성을 사용하는 예시입니다.

next.config.js
```
    module.exports = {
      images: {
        domains: ['assets.acme.com'],
      },
    }
```

### 로더 구성[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader-configuration)

Next.js 기본 Image Optimization API 대신 클라우드 공급자를 사용해 이미지를 최적화하려면 `next.config.js` 파일에서 `loader` 와 `path` 접두사를 설정할 수 있습니다. 그러면 Image [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src)에 상대 URL을 사용할 수 있고, 공급자에 맞는 올바른 절대 URL이 자동으로 생성됩니다.

next.config.js
```
    module.exports = {
      images: {
        loader: 'imgix',
        path: 'https://example.com/myaccount/',
      },
    }
```

#### 기본 이미지 경로 사용자 지정[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#customizing-the-built-in-image-path)

기본 Next.js 이미지 최적화 경로나 접두사를 변경하고 싶다면 `path` 속성으로 설정할 수 있습니다. `path` 의 기본값은 `/_next/image` 입니다.

next.config.js
```
    module.exports = {
      images: {
        path: '/my-prefix/_next/image',
      },
    }
```

### 기본 제공 로더[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#built-in-loaders)

다음 이미지 최적화 클라우드 공급자가 포함되어 있습니다.

  * Default: `next dev`, `next start`, 또는 커스텀 서버에서 자동으로 동작
  * [Vercel](https://vercel.com): Vercel에 배포하면 자동으로 동작하며 추가 설정이 필요 없습니다. [자세히 알아보기](https://vercel.com/docs/concepts/image-optimization?utm_source=next-site&utm_medium=docs&utm_campaign=next-website)
  * [Imgix](https://www.imgix.com): `loader: 'imgix'`
  * [Cloudinary](https://cloudinary.com): `loader: 'cloudinary'`
  * [Akamai](https://www.akamai.com): `loader: 'akamai'`
  * Custom: `loader: 'custom'` 으로 `next/legacy/image` 컴포넌트의 [`loader`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) prop을 구현해 커스텀 클라우드 공급자를 사용할 수 있습니다.

다른 공급자가 필요하다면 `next/legacy/image`에서 [`loader`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) prop을 사용하세요.

> [`output: 'export'`](https://nextjs.org/docs/pages/guides/static-exports)를 사용할 때는 이미지를 빌드 시점이 아니라 온디맨드로만 최적화할 수 있습니다. `next/legacy/image` 를 `output: 'export'` 와 함께 사용하려면 기본값이 아닌 다른 로더를 사용해야 합니다. [토론에서 자세히 읽어보세요.](https://github.com/vercel/next.js/discussions/19065)

## 고급[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#advanced)

아래 구성은 고급 사용 사례를 위한 것이며 일반적으로 필요하지 않습니다. 이 속성들을 설정하면 이후 업데이트에서 Next.js 기본값이 변경되더라도 이를 재정의하게 됩니다.

### 디바이스 크기[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)

사용자 디바이스의 예상 너비를 알고 있다면 `next.config.js` 의 `deviceSizes` 속성으로 디바이스 너비 브레이크포인트 목록을 지정할 수 있습니다. 이 너비는 `next/legacy/image` 컴포넌트가 `layout="responsive"` 또는 `layout="fill"` 을 사용할 때 올바른 이미지를 사용자 디바이스에 맞춰 제공하도록 활용됩니다.

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
```
    module.exports = {
      images: {
        deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
      },
    }
```

### 이미지 크기[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)

`next.config.js` 파일에서 `images.imageSizes` 속성으로 이미지 너비 목록을 지정할 수 있습니다. 이 너비 배열은 [디바이스 크기](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes) 배열과 이어 붙여져 이미지 [srcset](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/srcset)을 생성하는 전체 사이즈 배열이 됩니다.

별도의 두 목록이 있는 이유는 `imageSizes` 가 [`sizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#sizes) prop을 제공하는 이미지에만 사용되기 때문이며, 이는 이미지가 화면 전체 너비보다 작다는 것을 의미합니다. **따라서 `imageSizes` 의 값은 모두 `deviceSizes` 에서 가장 작은 값보다 작아야 합니다.**

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
```
    module.exports = {
      images: {
        imageSizes: [32, 48, 64, 96, 128, 256, 384],
      },
    }
```

### 허용 가능한 포맷[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#acceptable-formats)

기본 [Image Optimization API](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader-configuration)는 요청의 `Accept` 헤더를 통해 브라우저가 지원하는 이미지 포맷을 자동으로 감지하여 가장 적합한 출력 포맷을 결정합니다.

`Accept` 헤더가 구성된 포맷 중 둘 이상과 일치하면 배열에서 첫 번째 일치 항목을 사용하므로 배열 순서가 중요합니다. 일치하는 항목이 없거나 원본 이미지가 [애니메이션](https://nextjs.org/docs/pages/api-reference/components/image-legacy#animated-images)인 경우 Image Optimization API는 원본 이미지 포맷으로 되돌아갑니다.

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
```
    module.exports = {
      images: {
        formats: ['image/webp'],
      },
    }
```

브라우저가 [AVIF를 지원하지 않는](https://caniuse.com/avif) 경우 `src` 이미지의 원본 포맷으로 돌아가도록 AVIF 지원을 활성화할 수 있습니다.

next.config.js
```
    module.exports = {
      images: {
        formats: ['image/avif'],
      },
    }
```

AVIF와 WebP를 함께 활성화할 수도 있습니다. 지원하는 브라우저에서는 AVIF가 우선이며, WebP는 폴백으로 사용됩니다.

next.config.js
```
    module.exports = {
      images: {
        formats: ['image/avif', 'image/webp'],
      },
    }
```

> **알아두면 좋아요** :
>
>   * 대부분의 사용 사례에서는 여전히 WebP 사용을 권장합니다.
>   * AVIF는 일반적으로 인코딩에 50% 더 오래 걸리지만 WebP보다 20% 더 작게 압축됩니다. 즉, 이미지가 처음 요청될 때는 보통 더 느리지만 캐시된 이후의 요청은 더 빠릅니다.
>   * 여러 포맷을 사용할 때 Next.js는 각 포맷을 별도로 캐시합니다. 따라서 단일 포맷을 사용할 때보다 저장 공간이 더 필요하며, 브라우저별 지원을 위해 AVIF와 WebP 버전 모두 저장됩니다.
>   * Next.js 앞에 Proxy/CDN을 두고 자체 호스팅한다면 Proxy가 `Accept` 헤더를 전달하도록 설정해야 합니다.
>

## 캐싱 동작[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#caching-behavior)

다음은 기본 [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader)에 대한 캐싱 알고리즘 설명입니다. 다른 로더에 대해서는 해당 클라우드 공급자의 문서를 참조하세요.

이미지는 요청 시 동적으로 최적화되며 `<distDir>/cache/images` 디렉터리에 저장됩니다. 최적화된 이미지 파일은 만료 시점까지 이후 요청에 제공됩니다. 캐시되어 있지만 만료된 파일에 대한 요청이 들어오면 만료된 이미지가 즉시 제공되고, 백그라운드에서 다시 최적화(재검증)되어 새 만료일과 함께 캐시에 저장됩니다.

이미지의 캐시 상태는 응답 헤더 `x-nextjs-cache` (Vercel 배포 시 `x-vercel-cache`) 값으로 확인할 수 있으며, 가능한 값은 다음과 같습니다.

  * `MISS` - 경로가 캐시에 없음(첫 방문 시 최대 한 번 발생)
  * `STALE` - 경로가 캐시에 있지만 재검증 시간이 지났으므로 백그라운드에서 업데이트됨
  * `HIT` - 경로가 캐시에 있고 재검증 시간을 초과하지 않음

만료(또는 Max Age)는 [`minimumCacheTTL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#minimum-cache-ttl) 구성 또는 업스트림 이미지의 `Cache-Control` 헤더 중 더 큰 값으로 정의됩니다. 특히 `Cache-Control` 헤더의 `max-age` 값이 사용되며, `s-maxage` 와 `max-age` 가 모두 있으면 `s-maxage` 가 우선합니다. `max-age` 는 CDN과 브라우저를 포함한 다운스트림 클라이언트에도 그대로 전달됩니다.

  * 업스트림 이미지에 `Cache-Control` 헤더가 없거나 값이 매우 낮다면 [`minimumCacheTTL`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#minimum-cache-ttl)을 설정해 캐시 기간을 늘릴 수 있습니다.
  * [`deviceSizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#device-sizes)와 [`imageSizes`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#image-sizes)를 구성해 생성될 수 있는 이미지 수를 줄일 수 있습니다.
  * [formats](https://nextjs.org/docs/pages/api-reference/components/image-legacy#acceptable-formats)을 구성해 여러 포맷 대신 단일 이미지 포맷만 사용하도록 설정할 수 있습니다.

### 최소 캐시 TTL[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#minimum-cache-ttl)

캐시된 최적화 이미지의 TTL(Time to Live, 초 단위)을 설정할 수 있습니다. 많은 경우 [Static Image Import](https://nextjs.org/docs/pages/api-reference/components/image#src)를 사용하는 것이 더 좋은데, 이는 파일 내용을 자동으로 해시하고 `Cache-Control` 헤더를 `immutable` 로 설정해 이미지를 영구 캐시합니다.

구성을 제공하지 않으면 아래 기본값이 사용됩니다.

next.config.js
```
    module.exports = {
      images: {
        minimumCacheTTL: 14400, // 4 hours
      },
    }
```

TTL을 늘려 재검증 횟수를 줄이고 비용을 낮출 수도 있습니다.

next.config.js
```
    module.exports = {
      images: {
        minimumCacheTTL: 2678400, // 31 days
      },
    }
```

최적화된 이미지의 만료(Max Age)는 `minimumCacheTTL` 과 업스트림 이미지의 `Cache-Control` 헤더 중 더 큰 값으로 정의됩니다.

이미지별로 캐싱 동작을 변경해야 한다면 [`headers`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)를 구성해 업스트림 이미지(예: `/some-asset.jpg`, `/_next/image` 가 아님)의 `Cache-Control` 헤더를 설정하세요.

현재 캐시를 무효화하는 메커니즘이 없으므로 `minimumCacheTTL` 을 낮게 유지하는 것이 좋습니다. 그렇지 않으면 [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src) prop을 수동으로 변경하거나 `<distDir>/cache/images` 를 삭제해야 할 수 있습니다.

### 정적 임포트 비활성화[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#disable-static-imports)

기본 동작에서는 `import icon from './icon.png'` 과 같이 정적 파일을 임포트한 뒤 `src` 속성에 전달할 수 있습니다.

특정 플러그인과 충돌해 임포트가 다른 방식으로 동작해야 한다면 이 기능을 비활성화하고 싶을 수 있습니다.

`next.config.js` 에서 정적 이미지 임포트를 비활성화할 수 있습니다:

next.config.js
```
    module.exports = {
      images: {
        disableStaticImages: true,
      },
    }
```

### Dangerously Allow SVG[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#dangerously-allow-svg)

기본 [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader)는 몇 가지 이유로 SVG 이미지를 최적화하지 않습니다. 첫째, SVG는 벡터 형식이라서 손실 없이 크기 조절이 가능합니다. 둘째, SVG는 HTML/CSS와 동일한 기능을 많이 포함하므로 적절한 [Content Security Policy (CSP) 헤더](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#content-security-policy)가 없으면 취약점이 발생할 수 있습니다.

따라서 [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src) prop이 SVG임이 확실할 때 [`unoptimized`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#unoptimized) prop을 사용하는 것이 좋습니다. `src`가 `".svg"`로 끝나면 자동으로 적용됩니다.

하지만 기본 Image Optimization API로 SVG 이미지를 제공해야 한다면 `next.config.js` 내에서 `dangerouslyAllowSVG`를 설정할 수 있습니다:

next.config.js
```
    module.exports = {
      images: {
        dangerouslyAllowSVG: true,
        contentDispositionType: 'attachment',
        contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
      },
    }
```

또한 브라우저가 이미지를 다운로드하도록 강제하는 `contentDispositionType`과 이미지에 포함된 스크립트 실행을 차단하기 위한 `contentSecurityPolicy`를 함께 설정하는 것이 강력히 권장됩니다.

### `contentDispositionType`[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#contentdispositiontype)

기본 [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader)는 API가 임의의 원격 이미지를 제공할 수 있기 때문에 추가 보호를 위해 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) 헤더를 기본적으로 `attachment`로 설정합니다.

기본값은 `attachment`이며, 이를 통해 사용자가 이미지를 직접 방문할 때 브라우저가 다운로드하도록 강제합니다. 이는 [`dangerouslyAllowSVG`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#dangerously-allow-svg)가 true일 때 특히 중요합니다.

필요하다면 `inline`으로 구성하여 사용자가 이미지를 직접 방문할 때 다운로드 없이 렌더링되도록 허용할 수 있습니다.

next.config.js
```
    module.exports = {
      images: {
        contentDispositionType: 'inline',
      },
    }
```

### Animated Images[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#animated-images)

기본 [loader](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader)는 애니메이션 이미지에 대해서는 자동으로 Image Optimization을 건너뛰고 원본 그대로 제공합니다.

애니메이션 파일 자동 감지는 가능한 범위 내에서 수행되며 GIF, APNG, WebP를 지원합니다. 특정 애니메이션 이미지에 대해 명시적으로 Image Optimization을 건너뛰고 싶다면 [unoptimized](https://nextjs.org/docs/pages/api-reference/components/image-legacy#unoptimized) prop을 사용하세요.

## Version History[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#version-history)

Version| Changes
---|---
`v16.0.0`| `next/legacy/image`는 사용 중단되었으며 향후 Next.js 버전에서 제거될 예정입니다. 대신 `next/image`를 사용하세요.
`v13.0.0`| `next/image`가 `next/legacy/image`로 이름이 변경되었습니다.

보내기