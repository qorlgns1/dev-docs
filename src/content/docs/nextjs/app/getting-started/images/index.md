---
title: '시작하기: 이미지 최적화'
description: '마지막 업데이트 2026년 2월 20일'
---

# 시작하기: 이미지 최적화 | Next.js

Source URL: https://nextjs.org/docs/app/getting-started/images

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Image Optimization

Copy page

# 이미지 최적화

마지막 업데이트 2026년 2월 20일

Next.js [`<Image>`](https://nextjs.org/docs/app/api-reference/components/image) 컴포넌트는 HTML `<img>` 요소를 확장해 다음과 같은 기능을 제공합니다:

  * **크기 최적화:** WebP 같은 최신 이미지 포맷을 사용해 각 기기에 맞는 크기의 이미지를 자동으로 제공합니다.
  * **시각적 안정성:** 이미지 로딩 중 [레이아웃 시프트](https://web.dev/articles/cls)를 자동으로 방지합니다.
  * **더 빠른 페이지 로드:** 네이티브 브라우저 지연 로딩을 사용해 뷰포트에 들어올 때만 이미지를 로드하며, 선택적으로 블러 업 플레이스홀더를 제공합니다.
  * **에셋 유연성:** 원격 서버에 있는 이미지까지 포함해 필요할 때마다 이미지 크기를 조정합니다.



`<Image>` 사용을 시작하려면 `next/image`에서 import한 뒤 컴포넌트 안에서 렌더링하세요.

app/page.tsx

JavaScriptTypeScript
[code]
    import Image from 'next/image'
     
    export default function Page() {
      return <Image src="" alt="" />
    }
[/code]

`src` 속성은 [로컬](https://nextjs.org/docs/app/getting-started/images#local-images) 이미지나 [원격](https://nextjs.org/docs/app/getting-started/images#remote-images) 이미지가 될 수 있습니다.

> **🎥 Watch:** `next/image` 사용법을 더 알아보세요 → [YouTube (9 minutes)](https://youtu.be/IU_qq_c_lKA).

## 로컬 이미지[](https://nextjs.org/docs/app/getting-started/images#local-images)

이미지와 폰트 같은 정적 파일은 루트 디렉터리에 있는 [`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) 폴더 아래에 저장할 수 있습니다. `public` 내부의 파일은 기본 URL(`/`)을 기준으로 코드에서 참조할 수 있습니다.

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

이미지를 정적으로 import하면 Next.js가 고유한 [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)와 [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height)를 자동으로 계산합니다. 이 값은 이미지 비율을 결정하고 이미지 로딩 중 [누적 레이아웃 시프트](https://web.dev/articles/cls)를 방지하는 데 사용됩니다.

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

## 원격 이미지[](https://nextjs.org/docs/app/getting-started/images#remote-images)

원격 이미지를 사용하려면 `src` 속성에 URL 문자열을 전달하면 됩니다.

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

Next.js는 빌드 과정에서 원격 파일에 접근할 수 없으므로 [`width`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), [`height`](https://nextjs.org/docs/app/api-reference/components/image#width-and-height), 선택적인 [`blurDataURL`](https://nextjs.org/docs/app/api-reference/components/image#blurdataurl) prop을 직접 제공해야 합니다. `width`와 `height`는 올바른 이미지 종횡비를 유추하고 로딩 중 발생할 수 있는 레이아웃 시프트를 방지하는 데 사용됩니다. 또는 [`fill` 속성](https://nextjs.org/docs/app/api-reference/components/image#fill)을 사용해 부모 요소의 크기를 채우도록 이미지 크기를 지정할 수 있습니다.

원격 서버의 이미지를 안전하게 허용하려면 [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js)에 지원할 URL 패턴 목록을 정의해야 합니다. 악의적인 사용을 막기 위해 가능한 한 구체적으로 작성하세요. 예를 들어 아래 설정은 특정 AWS S3 버킷의 이미지만 허용합니다:

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

## API 참조

Next.js Image의 전체 기능은 API Reference에서 확인하세요.

### [Image ComponentOptimize Images in your Next.js Application using the built-in `next/image` Component.](https://nextjs.org/docs/app/api-reference/components/image)

도움이 되었나요?

supported.

Send
