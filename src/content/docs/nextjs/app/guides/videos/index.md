---
title: '가이드: 비디오'
description: '이 페이지에서는 Next.js 애플리케이션에서 비디오를 사용하는 방법을 설명하며, 성능에 영향을 주지 않고 비디오 파일을 저장하고 표시하는 방법을 보여 줍니다.'
---

# 가이드: 비디오 | Next.js

출처 URL: https://nextjs.org/docs/app/guides/videos

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)비디오

페이지 복사

# 비디오 사용 및 최적화 방법

마지막 업데이트 2026년 2월 20일

이 페이지에서는 Next.js 애플리케이션에서 비디오를 사용하는 방법을 설명하며, 성능에 영향을 주지 않고 비디오 파일을 저장하고 표시하는 방법을 보여 줍니다.

## `<video>` 및 `<iframe>` 사용하기[](https://nextjs.org/docs/app/guides/videos#using-video-and-iframe)

HTML **`<video>`** 태그는 직접 제공하는 비디오 파일을, **`<iframe>`** 태그는 외부 플랫폼에 호스팅된 비디오를 페이지에 임베드할 때 사용합니다.

### `<video>`[](https://nextjs.org/docs/app/guides/videos#video)

HTML [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) 태그를 사용하면 자체 호스팅 또는 직접 제공되는 비디오 콘텐츠를 임베드하여 재생과 모양을 완전히 제어할 수 있습니다.

app/ui/video.jsx
[code]
    export function Video() {
      return (
        <video width="320" height="240" controls preload="none">
          <source src="/path/to/video.mp4" type="video/mp4" />
          <track
            src="/path/to/captions.vtt"
            kind="subtitles"
            srcLang="en"
            label="English"
          />
          Your browser does not support the video tag.
        </video>
      )
    }
[/code]

### 일반적인 `<video>` 태그 속성[](https://nextjs.org/docs/app/guides/videos#common-video-tag-attributes)

Attribute| Description| Example Value  
---|---|---  
`src`| 비디오 파일의 소스를 지정합니다.| `<video src="/path/to/video.mp4" />`  
`width`| 비디오 플레이어의 너비를 설정합니다.| `<video width="320" />`  
`height`| 비디오 플레이어의 높이를 설정합니다.| `<video height="240" />`  
`controls`| 존재하면 기본 재생 컨트롤 세트를 표시합니다.| `<video controls />`  
`autoPlay`| 페이지가 로드될 때 비디오를 자동으로 재생합니다. 참고: 자동 재생 정책은 브라우저마다 다릅니다.| `<video autoPlay />`  
`loop`| 비디오 재생을 반복합니다.| `<video loop />`  
`muted`| 기본적으로 오디오를 음소거합니다. 종종 `autoPlay`와 함께 사용됩니다.| `<video muted />`  
`preload`| 비디오를 미리 불러오는 방식을 지정합니다. 값: `none`, `metadata`, `auto`.| `<video preload="none" />`  
`playsInline`| iOS 기기에서 인라인 재생을 활성화하며, iOS Safari에서 자동 재생이 작동하는 데 자주 필요합니다.| `<video playsInline />`  
  
> **알아 두면 좋은 정보** : `autoPlay` 속성을 사용할 때 대부분의 브라우저에서 자동 재생이 작동하도록 `muted` 속성을 함께 추가하고, iOS 기기와의 호환성을 위해 `playsInline` 속성을 포함하는 것이 중요합니다.

비디오 속성의 전체 목록은 [MDN 문서](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#attributes)를 참고하세요.

### 비디오 모범 사례[](https://nextjs.org/docs/app/guides/videos#video-best-practices)

  * **대체 콘텐츠:** `<video>` 태그를 사용할 때는 비디오 재생을 지원하지 않는 브라우저를 위해 태그 내부에 대체 콘텐츠를 포함하세요.
  * **자막 또는 캡션:** 청각장애인 사용자를 위해 자막이나 캡션을 포함하세요. `<video>` 요소와 함께 [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track) 태그를 사용해 자막 파일 소스를 지정합니다.
  * **접근 가능한 컨트롤:** 표준 HTML5 비디오 컨트롤은 키보드 탐색 및 스크린 리더 호환성을 위해 권장됩니다. 고급 요구 사항이 있다면 접근 가능한 컨트롤과 일관된 브라우저 경험을 제공하는 [react-player](https://github.com/cookpete/react-player) 또는 [video.js](https://videojs.com/) 같은 서드파티 플레이어를 고려하세요.



### `<iframe>`[](https://nextjs.org/docs/app/guides/videos#iframe)

HTML `<iframe>` 태그를 사용하면 YouTube나 Vimeo 같은 외부 플랫폼의 비디오를 임베드할 수 있습니다.

app/page.jsx
[code]
    export default function Page() {
      return (
        <iframe src="https://www.youtube.com/embed/19g66ezsKAg" allowFullScreen />
      )
    }
[/code]

### 일반적인 `<iframe>` 태그 속성[](https://nextjs.org/docs/app/guides/videos#common-iframe-tag-attributes)

Attribute| Description| Example Value  
---|---|---  
`src`| 임베드할 페이지의 URL입니다.| `<iframe src="https://example.com" />`  
`width`| iframe의 너비를 설정합니다.| `<iframe width="500" />`  
`height`| iframe의 높이를 설정합니다.| `<iframe height="300" />`  
`allowFullScreen`| iframe 콘텐츠를 전체 화면으로 표시할 수 있게 합니다.| `<iframe allowFullScreen />`  
`sandbox`| iframe 내부 콘텐츠에 추가적인 제한을 적용합니다.| `<iframe sandbox />`  
`loading`| 로딩 동작을 최적화합니다(예: 지연 로딩).| `<iframe loading="lazy" />`  
`title`| 접근성을 지원하기 위해 iframe에 제목을 제공합니다.| `<iframe title="Description" />`  
  
iframe 속성의 전체 목록은 [MDN 문서](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attributes)를 참고하세요.

### 비디오 임베드 방식 선택하기[](https://nextjs.org/docs/app/guides/videos#choosing-a-video-embedding-method)

Next.js 애플리케이션에 비디오를 임베드하는 방법은 두 가지입니다.

  * **자체 호스팅 또는 직접 제공 비디오 파일:** 플레이어 기능과 모양을 세밀하게 제어해야 하는 경우 `<video>` 태그로 자체 호스팅 비디오를 임베드하세요. 이 방법은 Next.js 내에서 비디오 콘텐츠를 원하는 대로 사용자 지정하고 제어할 수 있습니다.
  * **비디오 호스팅 서비스 사용(YouTube, Vimeo 등):** YouTube나 Vimeo 같은 서비스는 `<iframe>` 태그를 사용해 그들의 iframe 기반 플레이어를 임베드합니다. 이 방식은 플레이어 제어가 일부 제한되지만, 사용 편의성과 플랫폼에서 제공하는 기능을 제공합니다.



애플리케이션 요구 사항과 제공하고자 하는 사용자 경험에 가장 잘 맞는 임베드 방식을 선택하세요.

### 외부 호스팅 비디오 임베드하기[](https://nextjs.org/docs/app/guides/videos#embedding-externally-hosted-videos)

외부 플랫폼의 비디오를 임베드하려면 Next.js로 비디오 정보를 가져오고 React Suspense로 로딩 중 상태를 처리할 수 있습니다.

**1\. 비디오 임베드를 위한 서버 컴포넌트 만들기**

첫 단계는 비디오를 임베드할 적절한 iframe을 생성하는 [서버 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)를 만드는 것입니다. 이 컴포넌트는 비디오의 소스 URL을 가져와 iframe을 렌더링합니다.

app/ui/video-component.jsx
[code]
    export default async function VideoComponent() {
      const src = await getVideoSrc()
     
      return <iframe src={src} allowFullScreen />
    }
[/code]

**2\. React Suspense를 사용해 비디오 컴포넌트 스트리밍하기**

비디오를 임베드하는 서버 컴포넌트를 만든 뒤에는 [React Suspense](https://react.dev/reference/react/Suspense)를 사용해 컴포넌트를 [스트리밍](https://nextjs.org/docs/app/api-reference/file-conventions/loading)합니다.

app/page.jsx
[code]
    import { Suspense } from 'react'
    import VideoComponent from '../ui/VideoComponent.jsx'
     
    export default function Page() {
      return (
        <section>
          <Suspense fallback={<p>Loading video...</p>}>
            <VideoComponent />
          </Suspense>
          {/* Other content of the page */}
        </section>
      )
    }
[/code]

> **알아 두면 좋은 정보** : 외부 플랫폼의 비디오를 임베드할 때 다음 모범 사례를 고려하세요:
> 
>   * 비디오 임베드가 반응형인지 확인하세요. CSS로 iframe이나 비디오 플레이어가 다양한 화면 크기에 맞게 조정되도록 합니다.
>   * 특히 데이터 요금제에 제한이 있는 사용자를 위해 네트워크 상태에 따라 [비디오 로딩 전략](https://yoast.com/site-speed-tips-for-faster-video/)을 구현하세요.
> 


이 접근 방식은 페이지가 블로킹되지 않아 비디오 컴포넌트가 스트리밍되는 동안에도 사용자가 페이지와 상호작용할 수 있으므로 더 나은 사용자 경험을 제공합니다.

더 몰입감 있고 유익한 로딩 경험을 제공하려면 대체 UI로 로딩 스켈레톤을 사용하는 것을 고려하세요. 간단한 로딩 메시지 대신 비디오 플레이어와 유사한 스켈레톤을 표시할 수 있습니다.

app/page.jsx
[code]
    import { Suspense } from 'react'
    import VideoComponent from '../ui/VideoComponent.jsx'
    import VideoSkeleton from '../ui/VideoSkeleton.jsx'
     
    export default function Page() {
      return (
        <section>
          <Suspense fallback={<VideoSkeleton />}>
            <VideoComponent />
          </Suspense>
          {/* Other content of the page */}
        </section>
      )
    }
[/code]

## 자체 호스팅 비디오[](https://nextjs.org/docs/app/guides/videos#self-hosted-videos)

자체 호스팅은 다음과 같은 이유로 선호될 수 있습니다.

  * **완전한 제어와 독립성** : 자체 호스팅은 재생부터 모양까지 비디오 콘텐츠를 직접 관리할 수 있어 외부 플랫폼 제약 없이 완전한 소유와 제어를 보장합니다.
  * **특정 요구 사항에 맞춘 사용자 지정** : 동적 배경 비디오 같은 고유한 요구 사항에 이상적이며, 디자인과 기능적 요구 사항에 맞게 맞춤 설정할 수 있습니다.
  * **성능 및 확장성 고려 사항** : 증가하는 트래픽과 콘텐츠 규모를 효과적으로 지원할 수 있도록 고성능이면서 확장 가능한 스토리지 솔루션을 선택하세요.
  * **비용과 통합** : 스토리지 및 대역폭 비용과 Next.js 프레임워크 및 더 넓은 기술 생태계에 쉽게 통합해야 하는 요구 사항을 균형 있게 고려하세요.



### Vercel Blob을 사용한 비디오 호스팅[](https://nextjs.org/docs/app/guides/videos#using-vercel-blob-for-video-hosting)

[Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site&utm_medium=docs&utm_campaign=next-website)은 Next.js와 잘 작동하는 확장 가능한 클라우드 스토리지를 제공하여 비디오를 호스팅하는 효율적인 방법입니다. 다음은 Vercel Blob을 사용해 비디오를 호스팅하는 방법입니다.

**1\. Vercel Blob에 비디오 업로드하기**

Vercel 대시보드에서 "Storage" 탭으로 이동해 [Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site&utm_medium=docs&utm_campaign=next-website) 스토어를 선택합니다. Blob 표의 우측 상단에서 "Upload" 버튼을 찾아 클릭하고 업로드할 비디오 파일을 선택하세요. 업로드가 완료되면 비디오 파일이 Blob 표에 표시됩니다.

또는 서버 액션을 사용해 비디오를 업로드할 수 있습니다. 자세한 지침은 [server-side uploads](https://vercel.com/docs/storage/vercel-blob/server-upload)에 대한 Vercel 문서를 참고하세요. Vercel은 [client-side uploads](https://vercel.com/docs/storage/vercel-blob/client-upload)도 지원하므로 특정 사용 사례에 따라 이 방법이 더 적합할 수 있습니다.

**2\. Next.js에서 비디오 표시하기**

비디오가 업로드되어 저장되면 Next.js 애플리케이션에서 이를 표시할 수 있습니다. 다음은 `<video>` 태그와 React Suspense를 사용해 이를 구현하는 예시입니다.

app/page.jsx
[code]
    import { Suspense } from 'react'
    import { list } from '@vercel/blob'
     
    export default function Page() {
      return (
        <Suspense fallback={<p>Loading video...</p>}>
          <VideoComponent fileName="my-video.mp4" />
        </Suspense>
      )
    }
     
    async function VideoComponent({ fileName }) {
      const { blobs } = await list({
        prefix: fileName,
        limit: 1,
      })
      const { url } = blobs[0]
     
      return (
        <video controls preload="none" aria-label="Video player">
          <source src={url} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      )
    }
[/code]

이 방식에서는 페이지가 `@vercel/blob` URL을 사용해 `VideoComponent`로 비디오를 표시합니다. React Suspense가 비디오 URL을 가져와 비디오가 표시될 준비가 될 때까지 대체 UI를 보여 줍니다.

### 비디오에 자막 추가하기[](https://nextjs.org/docs/app/guides/videos#adding-subtitles-to-your-video)

비디오에 자막이 있다면 `<video>` 태그 안에서 `<track>` 요소를 사용해 손쉽게 추가할 수 있습니다. 비디오 파일과 마찬가지 방식으로 [Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site&utm_medium=docs&utm_campaign=next-website)에서 자막 파일을 가져올 수 있습니다. 다음은 자막을 포함하도록 `<VideoComponent>`를 업데이트하는 방법입니다.

app/page.jsx
```jsx
    async function VideoComponent({ fileName }) {
      const { blobs } = await list({
        prefix: fileName,
        limit: 2,
      })
      const { url } = blobs[0]
      const { url: captionsUrl } = blobs[1]
     
      return (
        <video controls preload="none" aria-label="Video player">
          <source src={url} type="video/mp4" />
          <track src={captionsUrl} kind="subtitles" srcLang="en" label="English" />
          Your browser does not support the video tag.
        </video>
      )
    }
```

이 접근 방식을 따르면 Next.js 애플리케이션에 비디오를 직접 호스팅하고 통합할 수 있습니다.

## Resources[](https://nextjs.org/docs/app/guides/videos#resources)

영상 최적화와 모범 사례에 대해 계속 학습하려면 다음 자료를 참고하세요.

  * **Understanding video formats and codecs** : 요구 사항에 맞게 MP4처럼 호환성이 좋은 형식이나 웹 최적화에 적합한 WebM 등을 선택하세요. 자세한 내용은 [Mozilla's guide on video codecs](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Video_codecs)를 확인하세요.
  * **Video compression** : FFmpeg 같은 도구를 사용해 품질과 파일 크기 사이의 균형을 맞추며 효과적으로 비디오를 압축하세요. 압축 기법은 [FFmpeg's official website](https://www.ffmpeg.org/)에서 알아볼 수 있습니다.
  * **Resolution and bitrate adjustment** : 시청 플랫폼에 맞춰 [resolution and bitrate](https://www.dacast.com/blog/bitrate-vs-resolution/#:~:text=The%20two%20measure%20different%20aspects,yield%20different%20qualities%20of%20video)를 조정하고, 모바일 기기에는 더 낮은 설정을 적용하세요.
  * **Content Delivery Networks (CDNs)** : CDN을 활용해 비디오 전송 속도를 높이고 대규모 트래픽을 처리하세요. Vercel Blob 같은 일부 스토리지 솔루션을 사용하면 CDN 기능이 자동으로 처리됩니다. CDN과 그 이점에 대해 [Learn more](https://vercel.com/docs/edge-network/overview?utm_source=next-site&utm_medium=docs&utm_campaign=next-website)에서 확인하세요.



Next.js 프로젝트에 비디오를 통합할 수 있는 다음 스트리밍 플랫폼도 살펴보세요.

### Open source `next-video` component[](https://nextjs.org/docs/app/guides/videos#open-source-next-video-component)

  * `<Video>` 컴포넌트를 제공하며, [Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site&utm_medium=docs&utm_campaign=next-website), S3, Backblaze, Mux 등 다양한 호스팅 서비스와 호환됩니다.
  * 여러 호스팅 서비스와 함께 `next-video.dev`를 사용하는 [Detailed documentation](https://next-video.dev/docs)가 준비되어 있습니다.



### Cloudinary Integration[](https://nextjs.org/docs/app/guides/videos#cloudinary-integration)

  * Cloudinary를 Next.js와 함께 사용하는 공식 [documentation and integration guide](https://next.cloudinary.dev/)가 제공됩니다.
  * [drop-in video support](https://next.cloudinary.dev/cldvideoplayer/basic-usage)를 위한 `<CldVideoPlayer>` 컴포넌트를 포함합니다.
  * [Adaptive Bitrate Streaming](https://github.com/cloudinary-community/cloudinary-examples/tree/main/examples/nextjs-cldvideoplayer-abr)을 포함해 Cloudinary와 Next.js를 통합하는 [examples](https://github.com/cloudinary-community/cloudinary-examples/?tab=readme-ov-file#nextjs)를 확인하세요.
  * Node.js SDK를 포함한 기타 [Cloudinary libraries](https://cloudinary.com/documentation)도 사용할 수 있습니다.



### Mux Video API[](https://nextjs.org/docs/app/guides/videos#mux-video-api)

  * Mux는 Next.js와 함께 비디오 강의를 제작할 수 있는 [starter template](https://github.com/muxinc/video-course-starter-kit)을 제공합니다.
  * Next.js 애플리케이션에 [high-performance video](https://www.mux.com/for/nextjs)를 임베드하는 Mux의 권장 사항을 알아보세요.
  * Mux와 Next.js를 시연하는 [example project](https://with-mux-video.vercel.app/)도 살펴보세요.



### Fastly[](https://nextjs.org/docs/app/guides/videos#fastly)

  * Fastly의 [video on demand](https://www.fastly.com/products/streaming-media/video-on-demand) 및 스트리밍 미디어 솔루션을 Next.js에 통합하는 방법을 알아보세요.



### ImageKit.io Integration[](https://nextjs.org/docs/app/guides/videos#imagekitio-integration)

  * ImageKit을 Next.js에 통합하는 [official quick start guide](https://imagekit.io/docs/integration/nextjs)를 확인하세요.
  * 통합은 [seamless video support](https://imagekit.io/docs/integration/nextjs#rendering-videos)를 제공하는 `<IKVideo>` 컴포넌트를 제공합니다.
  * Node.js SDK 등을 포함한 다른 [ImageKit libraries](https://imagekit.io/docs)도 살펴볼 수 있습니다.



도움이 되었나요?

supported.

Send
