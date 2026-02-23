---
title: 'img 요소 없음'
description: '> 느린 LCP와 더 높은 대역폭 사용 때문에  요소 사용을 방지합니다.'
---

# img 요소 없음 | Next.js

출처 URL: https://nextjs.org/docs/messages/no-img-element

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)img 요소 없음

# img 요소 없음

> 느린 LCP와 더 높은 대역폭 사용 때문에 `<img>` 요소 사용을 방지합니다.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-img-element#why-this-error-occurred)

이미지를 표시하기 위해 `next/image`의 `<Image />` 대신 `<img>` 요소를 사용했습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-img-element#possible-ways-to-fix-it)

  1. 자동 [Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image)으로 성능을 개선하려면 [`next/image`](https://nextjs.org/docs/pages/api-reference/components/image)를 사용하세요.

> **참고**: [managed hosting provider](https://nextjs.org/docs/pages/getting-started/deploying)에 배포한다면, 최적화된 이미지가 원본과 다른 과금 체계를 가질 수 있으니 제공업체 요금을 확인하세요.
> 
> 일반적인 이미지 최적화 플랫폼 요금:
> 
>   * [Vercel 요금](https://vercel.com/pricing)
>   * [Cloudinary 요금](https://cloudinary.com/pricing)
        * [imgix 요금](https://imgix.com/pricing)

> **참고**: 셀프 호스팅 시 [`sharp`](https://www.npmjs.com/package/sharp)을 설치하고, 최적화된 이미지를 캐시할 충분한 스토리지가 있는지 확인하세요.

pages/index.js
[code]
    import Image from 'next/image'
     
    function Home() {
      return (
        <Image
          src="https://example.com/hero.jpg"
          alt="Landscape picture"
          width={800}
          height={500}
        />
      )
    }
     
    export default Home
[/code]

  2. 블러 업 플레이스홀더 같은 `next/image` 기능은 사용하되 Image Optimization만 비활성화하려면 [unoptimized](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized)를 사용하세요.

pages/index.js
[code]
    import Image from 'next/image'
     
    const UnoptimizedImage = (props) => {
      return <Image {...props} unoptimized />
    }
[/code]

  3. `<picture>` 요소와 그 안의 `<img>` 요소를 사용할 수도 있습니다.

pages/index.js
[code]
    function Home() {
      return (
        <picture>
          <source srcSet="https://example.com/hero.avif" type="image/avif" />
          <source srcSet="https://example.com/hero.webp" type="image/webp" />
          <img
            src="https://example.com/hero.jpg"
            alt="Landscape picture"
            width={800}
            height={500}
          />
        </picture>
      )
    }
[/code]

  4. 이미지를 최적화하기 위해 [custom image loader](https://nextjs.org/docs/pages/api-reference/components/image#loader)를 사용할 수 있습니다. [loaderFile](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile)을 커스텀 로더 경로로 설정하세요.

next.config.js
[code]
    module.exports = {
      images: {
        loader: 'custom',
        loaderFile: './my/image/loader.js',
      },
    }
[/code]

## 유용한 링크[](https://nextjs.org/docs/messages/no-img-element#useful-links)

  * [이미지 컴포넌트 및 Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image)
  * [`next/image` API 레퍼런스](https://nextjs.org/docs/pages/api-reference/components/image)
  * [Largest Contentful Paint(LCP)](https://nextjs.org/learn/seo/web-performance/lcp)
  * [Next.js 구성 loaderFile 옵션](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile)

도움이 되었나요?

지원됨.

보내기
