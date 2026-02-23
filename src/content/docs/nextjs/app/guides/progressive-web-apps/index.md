---
title: '가이드: PWAs'
description: 'Progressive Web Application(PWA)는 웹 애플리케이션의 도달성과 접근성을 네이티브 모바일 앱의 기능 및 사용자 경험과 결합합니다. Next.js를 사용하면 여러 코드베이스나 앱 스토어 승인 없이 모든 플랫폼에서 매끄럽고 앱 같은 경험을 제공하는 ...'
---

# 가이드: PWAs | Next.js

Source URL: https://nextjs.org/docs/app/guides/progressive-web-apps

Copy page

# Next.js로 Progressive Web Application(PWA) 빌드하기

마지막 업데이트 2026년 2월 20일

Progressive Web Application(PWA)는 웹 애플리케이션의 도달성과 접근성을 네이티브 모바일 앱의 기능 및 사용자 경험과 결합합니다. Next.js를 사용하면 여러 코드베이스나 앱 스토어 승인 없이 모든 플랫폼에서 매끄럽고 앱 같은 경험을 제공하는 PWA를 만들 수 있습니다.

PWA를 사용하면 다음을 수행할 수 있습니다:

  * 앱 스토어 승인을 기다리지 않고 즉시 업데이트 배포
  * 단일 코드베이스로 크로스플랫폼 애플리케이션 구축
  * 홈 화면 설치 및 푸시 알림과 같은 네이티브 수준의 기능 제공

## Next.js로 PWA 만들기[](https://nextjs.org/docs/app/guides/progressive-web-apps#creating-a-pwa-with-nextjs)

### 1\. Web App Manifest 생성[](https://nextjs.org/docs/app/guides/progressive-web-apps#1-creating-the-web-app-manifest)

Next.js는 App Router를 사용해 [web app manifest](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)를 만들 수 있는 기본 지원을 제공합니다. 정적 또는 동적 manifest 파일을 생성할 수 있습니다.

예를 들어 `app/manifest.ts` 또는 `app/manifest.json` 파일을 만듭니다:

app/manifest.ts

JavaScriptTypeScript
```
    import type { MetadataRoute } from 'next'

    export default function manifest(): MetadataRoute.Manifest {
      return {
        name: 'Next.js PWA',
        short_name: 'NextPWA',
        description: 'A Progressive Web App built with Next.js',
        start_url: '/',
        display: 'standalone',
        background_color: '#ffffff',
        theme_color: '#000000',
        icons: [
          {
            src: '/icon-192x192.png',
            sizes: '192x192',
            type: 'image/png',
          },
          {
            src: '/icon-512x512.png',
            sizes: '512x512',
            type: 'image/png',
          },
        ],
      }
    }
```

이 파일에는 이름, 아이콘, 사용자 기기에서 아이콘으로 표시되는 방식 등의 정보가 포함되어야 합니다. 이를 통해 사용자는 홈 화면에 PWA를 설치하고 네이티브 앱과 유사한 경험을 얻을 수 있습니다.

[파비콘 생성기](https://realfavicongenerator.net/)와 같은 도구를 사용해 다양한 아이콘 세트를 만들고 생성된 파일을 `public/` 폴더에 배치할 수 있습니다.

### 2\. 웹 푸시 알림 구현[](https://nextjs.org/docs/app/guides/progressive-web-apps#2-implementing-web-push-notifications)

웹 푸시 알림은 다음을 포함한 모든 최신 브라우저에서 지원됩니다:

  * 홈 화면에 설치된 애플리케이션용 iOS 16.4+
  * macOS 13 이상용 Safari 16
  * Chromium 기반 브라우저
  * Firefox

이 덕분에 PWA는 네이티브 앱의 실질적인 대안이 됩니다. 특히 오프라인 지원 없이도 설치 프롬프트를 트리거할 수 있습니다.

웹 푸시 알림을 사용하면 사용자가 앱을 적극적으로 사용하고 있지 않을 때도 다시 참여시킬 수 있습니다. Next.js 애플리케이션에서 이를 구현하는 방법은 다음과 같습니다:

먼저 `app/page.tsx`에서 메인 페이지 컴포넌트를 만듭니다. 더 잘 이해할 수 있도록 작은 부분으로 나눕니다. 처음에는 필요한 일부 import와 유틸리티를 추가합니다. 참조된 Server Action이 아직 없어도 괜찮습니다:
```
    'use client'

    import { useState, useEffect } from 'react'
    import { subscribeUser, unsubscribeUser, sendNotification } from './actions'

    function urlBase64ToUint8Array(base64String: string) {
      const padding = '='.repeat((4 - (base64String.length % 4)) % 4)
      const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/')

      const rawData = window.atob(base64)
      const outputArray = new Uint8Array(rawData.length)

      for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i)
      }
      return outputArray
    }
```

이제 구독, 구독 해제, 푸시 알림 전송을 관리하는 컴포넌트를 추가합니다.
```
    function PushNotificationManager() {
      const [isSupported, setIsSupported] = useState(false)
      const [subscription, setSubscription] = useState<PushSubscription | null>(
        null
      )
      const [message, setMessage] = useState('')

      useEffect(() => {
        if ('serviceWorker' in navigator && 'PushManager' in window) {
          setIsSupported(true)
          registerServiceWorker()
        }
      }, [])

      async function registerServiceWorker() {
        const registration = await navigator.serviceWorker.register('/sw.js', {
          scope: '/',
          updateViaCache: 'none',
        })
        const sub = await registration.pushManager.getSubscription()
        setSubscription(sub)
      }

      async function subscribeToPush() {
        const registration = await navigator.serviceWorker.ready
        const sub = await registration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey: urlBase64ToUint8Array(
            process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!
          ),
        })
        setSubscription(sub)
        const serializedSub = JSON.parse(JSON.stringify(sub))
        await subscribeUser(serializedSub)
      }

      async function unsubscribeFromPush() {
        await subscription?.unsubscribe()
        setSubscription(null)
        await unsubscribeUser()
      }

      async function sendTestNotification() {
        if (subscription) {
          await sendNotification(message)
          setMessage('')
        }
      }

      if (!isSupported) {
        return <p>Push notifications are not supported in this browser.</p>
      }

      return (
        <div>
          <h3>Push Notifications</h3>
          {subscription ? (
            <>
              <p>You are subscribed to push notifications.</p>
              <button onClick={unsubscribeFromPush}>Unsubscribe</button>
              <input
                type="text"
                placeholder="Enter notification message"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
              />
              <button onClick={sendTestNotification}>Send Test</button>
            </>
          ) : (
            <>
              <p>You are not subscribed to push notifications.</p>
              <button onClick={subscribeToPush}>Subscribe</button>
            </>
          )}
        </div>
      )
    }
```

마지막으로, iOS 기기에서 홈 화면에 설치하도록 안내하는 메시지를 보여 주고, 이미 설치된 경우에는 표시하지 않는 컴포넌트를 만듭니다.
```
    function InstallPrompt() {
      const [isIOS, setIsIOS] = useState(false)
      const [isStandalone, setIsStandalone] = useState(false)

      useEffect(() => {
        setIsIOS(
          /iPad|iPhone|iPod/.test(navigator.userAgent) && !(window as any).MSStream
        )

        setIsStandalone(window.matchMedia('(display-mode: standalone)').matches)
      }, [])

      if (isStandalone) {
        return null // Don't show install button if already installed
      }

      return (
        <div>
          <h3>Install App</h3>
          <button>Add to Home Screen</button>
          {isIOS && (
            <p>
              To install this app on your iOS device, tap the share button
              <span role="img" aria-label="share icon">
                {' '}
                ⎋{' '}
              </span>
              and then "Add to Home Screen"
              <span role="img" aria-label="plus icon">
                {' '}
                ➕{' '}
              </span>
              .
            </p>
          )}
        </div>
      )
    }

    export default function Page() {
      return (
        <div>
          <PushNotificationManager />
          <InstallPrompt />
        </div>
      )
    }
```

이제 이 파일에서 호출하는 Server Action을 만듭니다.

### 3\. Server Action 구현[](https://nextjs.org/docs/app/guides/progressive-web-apps#3-implementing-server-actions)

`app/actions.ts`라는 새 파일을 만들어 액션을 정의합니다. 이 파일은 구독 생성, 구독 삭제, 알림 전송을 처리합니다.

app/actions.ts

JavaScriptTypeScript
```
    'use server'

    import webpush from 'web-push'

    webpush.setVapidDetails(
      '<mailto:your-email@example.com>',
      process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!,
      process.env.VAPID_PRIVATE_KEY!
    )

    let subscription: PushSubscription | null = null

    export async function subscribeUser(sub: PushSubscription) {
      subscription = sub
      // In a production environment, you would want to store the subscription in a database
      // For example: await db.subscriptions.create({ data: sub })
      return { success: true }
    }

    export async function unsubscribeUser() {
      subscription = null
      // In a production environment, you would want to remove the subscription from the database
      // For example: await db.subscriptions.delete({ where: { ... } })
      return { success: true }
    }

    export async function sendNotification(message: string) {
      if (!subscription) {
        throw new Error('No subscription available')
      }

      try {
        await webpush.sendNotification(
          subscription,
          JSON.stringify({
            title: 'Test Notification',
            body: message,
            icon: '/icon.png',
          })
        )
        return { success: true }
      } catch (error) {
        console.error('Error sending push notification:', error)
        return { success: false, error: 'Failed to send notification' }
      }
    }
```

알림 전송은 5단계에서 만들 서비스 워커가 처리합니다.

프로덕션 환경에서는 구독 정보를 데이터베이스에 저장해 서버 재시작 후에도 유지하고 여러 사용자의 구독을 관리해야 합니다.

### 4\. VAPID 키 생성[](https://nextjs.org/docs/app/guides/progressive-web-apps#4-generating-vapid-keys)

Web Push API를 사용하려면 [VAPID](https://vapidkeys.com/) 키를 생성해야 합니다. 가장 간단한 방법은 web-push CLI를 직접 사용하는 것입니다:

먼저 web-push를 전역 설치합니다:

pnpmnpmyarnbun

Terminal
```
    pnpm add -g web-push
```

다음 명령으로 VAPID 키를 생성합니다:

Terminal
```
    web-push generate-vapid-keys
```

출력을 복사해 `.env` 파일에 키를 붙여 넣습니다:
```
    NEXT_PUBLIC_VAPID_PUBLIC_KEY=your_public_key_here
    VAPID_PRIVATE_KEY=your_private_key_here

```

### 5\. 서비스 워커 만들기[](https://nextjs.org/docs/app/guides/progressive-web-apps#5-creating-a-service-worker)

서비스 워커용 `public/sw.js` 파일을 만듭니다:

public/sw.js
```
    self.addEventListener('push', function (event) {
      if (event.data) {
        const data = event.data.json()
        const options = {
          body: data.body,
          icon: data.icon || '/icon.png',
          badge: '/badge.png',
          vibrate: [100, 50, 100],
          data: {
            dateOfArrival: Date.now(),
            primaryKey: '2',
          },
        }
        event.waitUntil(self.registration.showNotification(data.title, options))
      }
    })

    self.addEventListener('notificationclick', function (event) {
      console.log('Notification click received.')
      event.notification.close()
      event.waitUntil(clients.openWindow('<https://your-website.com>'))
    })
```

이 서비스 워커는 사용자 지정 이미지와 알림을 지원합니다. 푸시 이벤트 수신과 알림 클릭을 처리합니다.

  * `icon` 및 `badge` 속성을 사용해 알림용 사용자 지정 아이콘을 설정할 수 있습니다.

* 지원되는 기기에서 사용자 지정 진동 알림을 만들 수 있도록 `vibrate` 패턴을 조정할 수 있습니다.
  * `data` 속성을 사용해 알림에 추가 데이터를 첨부할 수 있습니다.

다양한 기기와 브라우저에서 예상대로 동작하는지 확인하려면 서비스 워커를 철저히 테스트하세요. 또한 `notificationclick` 이벤트 리스너에 있는 `'https://your-website.com'` 링크를 애플리케이션에 맞는 URL로 업데이트하세요.

### 6. 홈 화면에 추가하기[](https://nextjs.org/docs/app/guides/progressive-web-apps#6-adding-to-home-screen)

2단계에서 정의한 `InstallPrompt` 컴포넌트는 iOS 기기에서 홈 화면에 설치하도록 안내하는 메시지를 표시합니다.

애플리케이션을 모바일 홈 화면에 설치할 수 있도록 하려면 다음을 갖추어야 합니다:

  1. 유효한 웹 앱 매니페스트(1단계에서 생성)
  2. HTTPS로 제공되는 웹사이트

최신 브라우저는 이러한 기준을 충족하면 자동으로 설치 프롬프트를 표시합니다. [`beforeinstallprompt`](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeinstallprompt_event)를 사용해 사용자 정의 설치 버튼을 제공할 수 있지만, Safari iOS에서 작동하지 않아 브라우저와 플랫폼 간 호환성이 없으므로 권장하지 않습니다.

### 7. 로컬 테스트[](https://nextjs.org/docs/app/guides/progressive-web-apps#7-testing-locally)

로컬에서 알림을 확인하려면 다음을 만족해야 합니다:

  * [HTTPS로 로컬 실행](https://nextjs.org/docs/app/api-reference/cli/next#using-https-during-development) 중이어야 합니다
    * 테스트용으로 `next dev --experimental-https`를 사용하세요
  * 사용하는 브라우저(Chrome, Safari, Firefox)에 대한 알림이 활성화되어 있어야 합니다
    * 로컬에서 권한 요청이 뜨면 알림 사용을 허용하세요
    * 브라우저 전체에 대해 알림이 전역 비활성화되어 있지 않은지 확인하세요
    * 여전히 알림이 보이지 않으면 다른 브라우저에서 디버그해 보세요

### 8. 애플리케이션 보안 강화[](https://nextjs.org/docs/app/guides/progressive-web-apps#8-securing-your-application)

보안은 어떤 웹 애플리케이션, 특히 PWA에서 매우 중요한 요소입니다. Next.js에서는 `next.config.js` 파일을 사용해 보안 헤더를 구성할 수 있습니다. 예를 들면 다음과 같습니다:

next.config.js
```
    module.exports = {
      async headers() {
        return [
          {
            source: '/(.*)',
            headers: [
              {
                key: 'X-Content-Type-Options',
                value: 'nosniff',
              },
              {
                key: 'X-Frame-Options',
                value: 'DENY',
              },
              {
                key: 'Referrer-Policy',
                value: 'strict-origin-when-cross-origin',
              },
            ],
          },
          {
            source: '/sw.js',
            headers: [
              {
                key: 'Content-Type',
                value: 'application/javascript; charset=utf-8',
              },
              {
                key: 'Cache-Control',
                value: 'no-cache, no-store, must-revalidate',
              },
              {
                key: 'Content-Security-Policy',
                value: "default-src 'self'; script-src 'self'",
              },
            ],
          },
        ]
      },
    }
```

각 옵션을 살펴보면 다음과 같습니다:

  1. 전역 헤더(모든 라우트에 적용):
     1. `X-Content-Type-Options: nosniff`: MIME 유형 스니핑을 방지해 악성 파일 업로드 위험을 줄입니다.
     2. `X-Frame-Options: DENY`: 사이트가 iframe에 임베드되는 것을 막아 클릭재킹 공격을 방지합니다.
     3. `Referrer-Policy: strict-origin-when-cross-origin`: 요청에 포함되는 리퍼러 정보 수준을 제어해 보안과 기능 사이 균형을 맞춥니다.
  2. 서비스 워커 전용 헤더:
     1. `Content-Type: application/javascript; charset=utf-8`: 서비스 워커가 JavaScript로 올바르게 해석되도록 보장합니다.
     2. `Cache-Control: no-cache, no-store, must-revalidate`: 서비스 워커가 캐시되는 것을 막아 항상 최신 버전을 제공하도록 합니다.
     3. `Content-Security-Policy: default-src 'self'; script-src 'self'`: 서비스 워커에 대해 동일 출처 스크립트만 허용하는 엄격한 CSP를 적용합니다.

Next.js에서 [콘텐츠 보안 정책](https://nextjs.org/docs/app/guides/content-security-policy)을 정의하는 방법을 더 알아보세요.

## PWA 확장하기[](https://nextjs.org/docs/app/guides/progressive-web-apps#extending-your-pwa)

  1. **PWA 기능 탐색**: PWAs는 다양한 Web API를 활용해 고급 기능을 제공할 수 있습니다. 백그라운드 동기화, 주기적 백그라운드 동기화, File System Access API 같은 기능을 살펴보고 참고 자료로 [What PWA Can Do Today](https://whatpwacando.today/)에서 최신 정보를 확인하세요.
  2. **정적 내보내기:** 서버 없이 정적 파일로만 애플리케이션을 제공해야 한다면 Next.js 구성을 업데이트해 이 변경을 활성화할 수 있습니다. 자세한 내용은 [Next.js 정적 내보내기 문서](https://nextjs.org/docs/app/guides/static-exports)를 참고하세요. 단, Server Actions 대신 외부 API를 호출해야 하고 정의한 헤더를 프록시로 옮겨야 합니다.
  3. **오프라인 지원**: 오프라인 기능을 제공하는 한 가지 방법은 Next.js와 함께 [Serwist](https://github.com/serwist/serwist)를 사용하는 것입니다. 통합 예시는 [문서](https://github.com/serwist/serwist/tree/main/examples/next-basic)에서 확인할 수 있습니다. **참고:** 현재 이 플러그인은 webpack 구성이 필요합니다.
  4. **보안 고려 사항**: 서비스 워커를 적절히 보호하세요. HTTPS 사용, 푸시 메시지 출처 검증, 올바른 오류 처리를 포함합니다.
  5. **사용자 경험**: 특정 PWA 기능을 브라우저가 지원하지 않는 경우에도 앱이 잘 작동하도록 프로그레시브 인핸스먼트 기법을 고려하세요.

##

- [manifest.json](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
  - 파일을 위한 API Reference

보내기