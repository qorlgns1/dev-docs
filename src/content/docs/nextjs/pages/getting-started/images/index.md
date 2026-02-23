---
title: '시작하기: Images'
description: '마지막 업데이트 2026년 2월 20일'
---

# 시작하기: Images | Next.js

Source URL: https://nextjs.org/docs/pages/getting-started/images

[Pages Router](https://nextjs.org/docs/pages)[Getting Started](https://nextjs.org/docs/pages/getting-started)Images

페이지 복사

# 이미지 최적화

마지막 업데이트 2026년 2월 20일

Next.js [`<Image>`](https://nextjs.org/docs/app/api-reference/components/image) 컴포넌트는 HTML `<img>` 요소를 확장해 다음을 제공합니다:

  * **크기 최적화:** WebP와 같은 최신 이미지 포맷을 활용해 각 기기에 맞는 크기의 이미지를 자동으로 제공합니다.
  * **시각적 안정성:** 이미지를 로딩할 때 [레이아웃 시프트](https://web.dev/articles/cls)를 자동으로 방지합니다.
  * **더 빠른 페이지 로드:** 네이티브 브라우저 지연 로딩과 선택형 블러 업 플레이스홀더로 뷰포트에 들어올 때만 이미지를 로드합니다.
  * **에셋 유연성:** 원격 서버에 저장된 이미지를 포함해 필요할 때마다 이미지를 리사이징합니다.

`<Image>`를 사용하려면 `next/image`에서 임포트하여 컴포넌트 내부에서 렌더링하세요.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return <Image src="" alt="" />
    }
[/code]

`src` 속성에는 [로컬](https://nextjs.org/docs/pages/getting-started/images#local-images) 또는 [원격](https://nextjs.org/docs/pages/getting-started/images#remote-images) 이미지를 지정할 수 있습니다.

> **🎥 시청:** `next/image` 사용 방법 자세히 알아보기 → [YouTube (9분)](https://youtu.be/IU_qq_c_lKA).

## 로컬 이미지[](https://nextjs.org/docs/pages/getting-started/images#local-images)

이미지, 폰트 같은 정적 파일은 루트 디렉터리의 [`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) 폴더 아래에 저장할 수 있습니다. `public` 내부의 파일은 기본 URL(`/`)에서 시작해 코드에서 참조할 수 있습니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return (
        <Image
          src="/profile.png"
          alt="Picture of the author"
          width={500}
          height={500}
        />
      )
    }
[/code]

이미지를 정적으로 임포트하면 Next.js가 고유의 [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)와 [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)를 자동으로 파악합니다. 이 값은 이미지 비율을 계산하고 이미지 로딩 중 [누적 레이아웃 시프트](https://web.dev/articles/cls)를 방지하는 데 사용됩니다.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
    import ProfileImage from './profile.png'
     
    export default function Page() {
      return (
        <Image
          src={ProfileImage}
          alt="Picture of the author"
          // width={500} automatically provided
          // height={500} automatically provided
          // blurDataURL="data:..." automatically provided
          // placeholder="blur" // Optional blur-up while loading
        />
      )
    }
[/code]

## 원격 이미지[](https://nextjs.org/docs/pages/getting-started/images#remote-images)

원격 이미지를 사용하려면 `src` 속성에 URL 문자열을 제공하면 됩니다.

app/page.tsx

JavaScriptTypeScript
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

Next.js는 빌드 과정에서 원격 파일에 접근할 수 없으므로 [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), 선택형 [`blurDataURL`](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl) 프롭을 직접 지정해야 합니다. `width`와 `height`는 올바른 종횡비를 추론하고 이미지 로딩 시 발생할 수 있는 레이아웃 시프트를 방지하는 데 사용됩니다. 또는 [`fill` 속성](https://nextjs.org/docs/app/api-reference/components/image#fill)을 사용해 이미지를 부모 요소 크기에 맞게 채울 수도 있습니다.

원격 서버의 이미지를 안전하게 허용하려면 [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js)에 지원되는 URL 패턴 목록을 정의해야 합니다. 악의적인 사용을 막기 위해 가능한 구체적으로 설정하세요. 예를 들어 아래 구성은 특정 AWS S3 버킷의 이미지만 허용합니다:

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'
     
    const config: NextConfig = {
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
     
    export default config
[/code]

## API 레퍼런스

Next.js Image의 전체 기능 세트는 API 레퍼런스에서 확인하세요.

### [ImageNext.js 애플리케이션에서 기본 제공 `next/image` 컴포넌트로 이미지를 최적화하세요.](https://nextjs.org/docs/pages/api-reference/components/image)

도움이 되었나요?

지원됨.

전송
