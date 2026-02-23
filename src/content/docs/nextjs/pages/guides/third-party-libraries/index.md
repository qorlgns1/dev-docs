---
title: '가이드: 서드파티 라이브러리'
description: '가 제공하는 모든 서드파티 통합은 성능과 사용 편의성을 위해 최적화되어 있습니다.'
---

# 가이드: 서드파티 라이브러리 | Next.js
Source URL: https://nextjs.org/docs/pages/guides/third-party-libraries

[페이지 라우터](https://nextjs.org/docs/pages)[가이드](https://nextjs.org/docs/pages/guides)서드파티 라이브러리

# 서드파티 라이브러리를 최적화하는 방법

마지막 업데이트 2026년 2월 20일

**`@next/third-parties`** 는 Next.js 애플리케이션에서 널리 사용되는 서드파티 라이브러리를 로드할 때 성능과 개발자 경험을 향상시키는 컴포넌트와 유틸리티 모음입니다.

`@next/third-parties` 가 제공하는 모든 서드파티 통합은 성능과 사용 편의성을 위해 최적화되어 있습니다.

## 시작하기[](https://nextjs.org/docs/pages/guides/third-party-libraries#getting-started)

시작하려면 `@next/third-parties` 라이브러리를 설치하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm add @next/third-parties@latest next@latest
[/code]

`@next/third-parties` 는 현재 활발히 개발 중인 **실험적** 라이브러리입니다. 더 많은 서드파티 통합을 추가하는 동안 **latest** 또는 **canary** 플래그로 설치하는 것을 권장합니다.

## Google 서드파티[](https://nextjs.org/docs/pages/guides/third-party-libraries#google-third-parties)

Google에서 지원되는 모든 서드파티 라이브러리는 `@next/third-parties/google` 에서 가져올 수 있습니다.

### Google Tag Manager[](https://nextjs.org/docs/pages/guides/third-party-libraries#google-tag-manager)

`GoogleTagManager` 컴포넌트를 사용하면 페이지에 [Google Tag Manager](https://developers.google.com/tag-platform/tag-manager) 컨테이너를 생성할 수 있습니다. 기본적으로 페이지에서 하이드레이션이 완료된 후 원본 인라인 스크립트를 가져옵니다.

모든 라우트에서 Google Tag Manager를 로드하려면 커스텀 `_app` 에 컴포넌트를 직접 포함하고 GTM 컨테이너 ID를 전달하세요:

pages/_app.js
[code]
    import { GoogleTagManager } from '@next/third-parties/google'

    export default function MyApp({ Component, pageProps }) {
      return (
        <>
          <Component {...pageProps} />
          <GoogleTagManager gtmId="GTM-XYZ" />
        </>
      )
    }
[/code]

단일 라우트에서 Google Tag Manager를 로드하려면 페이지 파일에 컴포넌트를 포함하세요:

pages/index.js
[code]
    import { GoogleTagManager } from '@next/third-parties/google'

    export default function Page() {
      return <GoogleTagManager gtmId="GTM-XYZ" />
    }
[/code]

#### 이벤트 전송[](https://nextjs.org/docs/pages/guides/third-party-libraries#sending-events)

`sendGTMEvent` 함수는 `dataLayer` 객체를 사용해 이벤트를 전송함으로써 페이지에서 사용자 상호작용을 추적할 수 있습니다. 이 함수가 작동하려면 `<GoogleTagManager />` 컴포넌트를 상위 레이아웃, 페이지, 컴포넌트 중 하나에 포함하거나 동일한 파일에 직접 포함해야 합니다.

pages/index.js
[code]
    import { sendGTMEvent } from '@next/third-parties/google'

    export function EventButton() {
      return (
        <div>
          <button
            onClick={() => sendGTMEvent({ event: 'buttonClicked', value: 'xyz' })}
          >
            Send Event
          </button>
        </div>
      )
    }
[/code]

함수에 전달할 수 있는 다양한 변수와 이벤트에 대해서는 Tag Manager [개발자 문서](https://developers.google.com/tag-platform/tag-manager/datalayer)를 참고하세요.

#### 서버 사이드 태깅[](https://nextjs.org/docs/pages/guides/third-party-libraries#server-side-tagging)

서버 사이드 태그 관리자에서 `gtm.js` 스크립트를 태깅 서버로부터 제공하는 경우 `gtmScriptUrl` 옵션으로 스크립트 URL을 지정할 수 있습니다.

#### 옵션[](https://nextjs.org/docs/pages/guides/third-party-libraries#options)

Google Tag Manager에 전달할 수 있는 옵션입니다. 전체 옵션 목록은 [Google Tag Manager 문서](https://developers.google.com/tag-platform/tag-manager/datalayer)를 참조하세요.

Name| Type| Description
---|---|---
`gtmId`| Required*| GTM 컨테이너 ID입니다. 일반적으로 `GTM-` 으로 시작합니다.
`gtmScriptUrl`| Optional*| GTM 스크립트 URL입니다. 기본값은 `https://www.googletagmanager.com/gtm.js` 입니다.
`dataLayer`| Optional| 컨테이너를 초기화할 데이터 레이어 객체입니다.
`dataLayerName`| Optional| 데이터 레이어 이름입니다. 기본값은 `dataLayer` 입니다.
`auth`| Optional| 환경 스니펫을 위한 인증 매개변수(`gtm_auth`) 값입니다.
`preview`| Optional| 환경 스니펫을 위한 미리보기 매개변수(`gtm_preview`) 값입니다.

*`gtmId` 는 [광고주용 Google 태그 게이트웨이](https://developers.google.com/tag-platform/tag-manager/gateway/setup-guide?setup=manual)를 지원하기 위해 `gtmScriptUrl` 이 제공될 때 생략할 수 있습니다.

### Google Analytics[](https://nextjs.org/docs/pages/guides/third-party-libraries#google-analytics)

`GoogleAnalytics` 컴포넌트는 Google 태그(`gtag.js`)를 통해 페이지에 [Google Analytics 4](https://developers.google.com/analytics/devguides/collection/ga4)를 포함할 수 있습니다. 기본적으로 페이지에서 하이드레이션이 완료된 후 원본 스크립트를 가져옵니다.

> **추천**: 애플리케이션에 이미 Google Tag Manager가 포함되어 있다면 별도의 컴포넌트를 추가하기보다 Tag Manager에서 직접 Google Analytics를 구성할 수 있습니다. Tag Manager와 `gtag.js` 의 차이점은 [문서](https://developers.google.com/analytics/devguides/collection/ga4/tag-options#what-is-gtm)를 참고하세요.

모든 라우트에서 Google Analytics를 로드하려면 커스텀 `_app` 에 컴포넌트를 직접 포함하고 측정 ID를 전달하세요:

pages/_app.js
[code]
    import { GoogleAnalytics } from '@next/third-parties/google'

    export default function MyApp({ Component, pageProps }) {
      return (
        <>
          <Component {...pageProps} />
          <GoogleAnalytics gaId="G-XYZ" />
        </>
      )
    }
[/code]

단일 라우트에서 Google Analytics를 로드하려면 페이지 파일에 컴포넌트를 포함하세요:

pages/index.js
[code]
    import { GoogleAnalytics } from '@next/third-parties/google'

    export default function Page() {
      return <GoogleAnalytics gaId="G-XYZ" />
    }
[/code]

#### 이벤트 전송[](https://nextjs.org/docs/pages/guides/third-party-libraries#sending-events-1)

`sendGAEvent` 함수는 `dataLayer` 객체를 사용해 이벤트를 전송함으로써 페이지에서 사용자 상호작용을 측정할 수 있습니다. 이 함수가 작동하려면 `<GoogleAnalytics />` 컴포넌트를 상위 레이아웃, 페이지, 컴포넌트 중 하나에 포함하거나 동일한 파일에 직접 포함해야 합니다.

pages/index.js
[code]
    import { sendGAEvent } from '@next/third-parties/google'

    export function EventButton() {
      return (
        <div>
          <button
            onClick={() => sendGAEvent('event', 'buttonClicked', { value: 'xyz' })}
          >
            Send Event
          </button>
        </div>
      )
    }
[/code]

이벤트 매개변수에 대해 더 알아보려면 Google Analytics [개발자 문서](https://developers.google.com/analytics/devguides/collection/ga4/event-parameters)를 참조하세요.

#### 페이지뷰 추적[](https://nextjs.org/docs/pages/guides/third-party-libraries#tracking-pageviews)

Google Analytics는 브라우저 히스토리 상태가 변경될 때 자동으로 페이지뷰를 추적합니다. 즉, Next.js 라우트 간 클라이언트 사이드 이동은 추가 구성 없이 페이지뷰 데이터를 전송합니다.

클라이언트 사이드 내비게이션이 정확히 측정되고 있는지 확인하려면 관리자 패널에서 [_“향상된 측정”_](https://support.google.com/analytics/answer/9216061#enable_disable) 속성이 활성화되어 있고 _“브라우저 히스토리 이벤트 기반 페이지 변경”_ 체크박스가 선택되어 있는지 검증하세요.

> **참고**: 페이지뷰 이벤트를 수동으로 전송하기로 결정했다면 중복 데이터를 피하기 위해 기본 페이지뷰 측정을 비활성화해야 합니다. 자세한 내용은 Google Analytics [개발자 문서](https://developers.google.com/analytics/devguides/collection/ga4/views?client_type=gtag#manual_pageviews)를 참고하세요.

#### 옵션[](https://nextjs.org/docs/pages/guides/third-party-libraries#options-1)

`<GoogleAnalytics>` 컴포넌트에 전달할 수 있는 옵션입니다.

Name| Type| Description
---|---|---
`gaId`| Required| [측정 ID](https://support.google.com/analytics/answer/12270356)입니다. 일반적으로 `G-` 로 시작합니다.
`dataLayerName`| Optional| 데이터 레이어 이름입니다. 기본값은 `dataLayer` 입니다.
`nonce`| Optional| [nonce](https://nextjs.org/docs/app/guides/content-security-policy#nonces) 입니다.

### Google Maps Embed[](https://nextjs.org/docs/pages/guides/third-party-libraries#google-maps-embed)

`GoogleMapsEmbed` 컴포넌트를 사용하면 페이지에 [Google Maps Embed](https://developers.google.com/maps/documentation/embed/embedding-map)를 추가할 수 있습니다. 기본적으로 `loading` 속성을 사용하여 화면 아래쪽에서 임베드를 지연 로드합니다.

pages/index.js
[code]
    import { GoogleMapsEmbed } from '@next/third-parties/google'

    export default function Page() {
      return (
        <GoogleMapsEmbed
          apiKey="XYZ"
          height={200}
          width="100%"
          mode="place"
          q="Brooklyn+Bridge,New+York,NY"
        />
      )
    }
[/code]

#### 옵션[](https://nextjs.org/docs/pages/guides/third-party-libraries#options-2)

Google Maps Embed에 전달할 수 있는 옵션입니다. 전체 옵션 목록은 [Google Map Embed 문서](https://developers.google.com/maps/documentation/embed/embedding-map)를 참고하세요.

Name| Type| Description
---|---|---
`apiKey`| Required| API 키입니다.
`mode`| Required| [지도 모드](https://developers.google.com/maps/documentation/embed/embedding-map#choosing_map_modes)입니다.
`height`| Optional| 임베드 높이입니다. 기본값은 `auto` 입니다.
`width`| Optional| 임베드 너비입니다. 기본값은 `auto` 입니다.
`style`| Optional| iframe에 적용할 스타일입니다.
`allowfullscreen`| Optional| 지도의 일부를 전체 화면으로 표시할 수 있게 하는 속성입니다.
`loading`| Optional| 기본값은 lazy입니다. 접힘선 위에 임베드가 위치한다면 변경을 고려하세요.
`q`| Optional| 지도 마커 위치를 정의합니다. _지도 모드에 따라 필수일 수 있습니다._
`center`| Optional| 지도 뷰의 중심을 정의합니다.
`zoom`| Optional| 지도 초기 줌 레벨을 설정합니다.
`maptype`| Optional| 로드할 지도 타일 유형을 정의합니다.
`language`| Optional| UI 요소와 지도 타일 레이블에 사용할 언어를 정의합니다.
`region`| Optional| 지정학적 민감도에 따라 적절한 경계와 레이블을 정의합니다.

### YouTube Embed[](https://nextjs.org/docs/pages/guides/third-party-libraries#youtube-embed)

`YouTubeEmbed` 컴포넌트는 YouTube 임베드를 로드하고 표시하는 데 사용할 수 있습니다. 이 컴포넌트는 내부적으로 [`lite-youtube-embed`](https://github.com/paulirish/lite-youtube-embed)를 사용해 더 빠르게 로드됩니다.

pages/index.js
[code]
    import { YouTubeEmbed } from '@next/third-parties/google'

    export default function Page() {
      return <YouTubeEmbed videoid="ogfYd705cRs" height={400} params="controls=0" />
    }
[/code]

#### 옵션[](https://nextjs.org/docs/pages/guides/third-party-libraries#options-3)

Name| Type| Description
---|---|---
`videoid`| Required| YouTube 비디오 ID입니다.
`width`| Optional| 비디오 컨테이너 너비입니다. 기본값은 `auto` 입니다.
`height`| Optional| 비디오 컨테이너 높이입니다. 기본값은 `auto` 입니다.
`playlabel`| Optional| 접근성을 위한 재생 버튼 시각 숨김 라벨입니다.
`params`| Optional| [여기](https://developers.google.com/youtube/player_parameters#Parameters)에 정의된 비디오 플레이어 매개변수입니다.
매개변수는 쿼리 파라미터 문자열로 전달됩니다.
예: `params="controls=0&start=10&end=30"`
`style`| Optional| 비디오 컨테이너에 스타일을 적용하는 데 사용됩니다.
