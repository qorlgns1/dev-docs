---
title: '프록시 / 미들웨어'
description: '미들웨어는 를 통해 생성할 수 있습니다.'
---

Source URL: https://next-intl.dev/docs/routing/middleware

[문서](https://next-intl.dev/docs/getting-started "Docs")[라우팅](https://next-intl.dev/docs/routing "Routing")프록시 / 미들웨어

# 프록시 / 미들웨어

`next-intl` 미들웨어는 `createMiddleware`를 통해 생성할 수 있습니다.

이 미들웨어는 [`routing`](https://next-intl.dev/docs/routing/configuration#define-routing) 구성을 받아 다음을 처리합니다:

  1. 로케일 협상
  2. 관련 리디렉션 및 리라이트 적용
  3. 검색 엔진을 위한 [alternate links](https://next-intl.dev/docs/routing/configuration#alternate-links) 제공

**예시:**

proxy.ts
```
    import createMiddleware from 'next-intl/middleware';
    import {routing} from './i18n/routing';

    export default createMiddleware(routing);

    export const config = {
      // Match all pathnames except for
      // - … if they start with `/api`, `/trpc`, `/_next` or `/_vercel`
      // - … the ones containing a dot (e.g. `favicon.ico`)
      matcher: '/((?!api|trpc|_next|_vercel|.*\\..*).*)'
    };
```

**참고:** `proxy.ts`는 Next.js 16까지 `middleware.ts`라고 불렸습니다.

## 로케일 감지[](https://next-intl.dev/docs/routing/middleware#locale-detection)

로케일은 [`localePrefix`](https://next-intl.dev/docs/routing/configuration#locale-prefix), [`domains`](https://next-intl.dev/docs/routing/configuration#domains), [`localeDetection`](https://next-intl.dev/docs/routing/configuration#locale-detection), [`localeCookie`](https://next-intl.dev/docs/routing/configuration#locale-cookie)에 대한 설정을 고려해 협상됩니다.

### 프리픽스 기반 라우팅 (기본값)[](https://next-intl.dev/docs/routing/middleware#location-detection-prefix)

영상으로 보고 싶으신가요?

[프리픽스 기반 라우팅](https://learn.next-intl.dev/chapters/06-routing/07-prefix-based)

기본적으로 요청의 로케일을 결정하기 위해 [프리픽스 기반 라우팅](https://next-intl.dev/docs/routing/configuration#locale-prefix)을 사용합니다.

이 경우 로케일은 다음 우선순위에 따라 감지됩니다:

  1. pathname에 로케일 프리픽스가 있음 (예: `/en/about`)
  2. 이전에 감지된 로케일을 담고 있는 쿠키가 있음
  3. [`accept-language` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)를 기반으로 로케일을 매칭할 수 있음
  4. 마지막 수단으로 `defaultLocale` 사용

로케일을 변경하려면 사용자가 프리픽스가 있는 라우트를 방문하면 됩니다. 이는 쿠키 또는 `accept-language` header에 저장된 이전 매칭 결과보다 우선하며, 기존 쿠키 값도 업데이트합니다.

**예시 워크플로:**

  1. 사용자가 `/`를 요청하고 `accept-language` header를 기반으로 `en` 로케일이 매칭됩니다.
  2. 사용자는 `/en`으로 리디렉션됩니다.
  3. 앱은 사용자가 로케일을 `de`로 변경할 수 있도록 `<Link locale="de" href="/">Switch to German</Link>`를 렌더링합니다.
  4. 사용자가 링크를 클릭하면 `/de`로 요청이 시작됩니다.
  5. 미들웨어는 `de` 로케일 선호를 기억하기 위한 쿠키를 추가합니다.
  6. 이후 사용자가 다시 `/`를 요청하면, 미들웨어는 쿠키를 기반으로 `/de`로 리디렉션합니다.

[](https://next-intl.dev/docs/routing/middleware#accept-language-matching)`accept-language` header를 사용 가능한 로케일과 매칭할 때 어떤 알고리즘을 사용하나요?

앱에서 사용 가능한 옵션을 기준으로 최적의 로케일을 결정하기 위해, 미들웨어는 [`@formatjs/intl-localematcher`](https://www.npmjs.com/package/@formatjs/intl-localematcher)의 “best fit” 알고리즘을 사용합니다. 이 알고리즘은 [RFC 4647](https://www.rfc-editor.org/rfc/rfc4647.html#section-3.4)에 정의된 더 보수적인 “lookup” 알고리즘보다 더 나은 결과를 제공할 것으로 기대됩니다.

예시로, 앱이 다음 로케일을 지원한다고 가정해 봅시다:

  1. `en-US`
  2. `de-DE`

“lookup” 알고리즘은 사용자의 `accept-language` header에서 서브태그를 점진적으로 제거해 매칭을 찾는 방식으로 동작합니다. 따라서 사용자의 브라우저가 `accept-language` header로 `en-GB`를 보내면, “lookup” 알고리즘은 매칭을 찾지 못해 기본 로케일이 사용됩니다.

반면 “best fit” 알고리즘은 사용자의 `accept-language` header와 사용 가능한 로케일 사이의 _거리_를 비교하며, 지역 정보도 함께 고려합니다. 이 때문에 이 경우 “best fit” 알고리즘은 `en-US`를 최적 매칭 로케일로 선택할 수 있습니다.

### 도메인 기반 라우팅[](https://next-intl.dev/docs/routing/middleware#location-detection-domain)

영상으로 보고 싶으신가요?

[도메인 기반 라우팅](https://learn.next-intl.dev/chapters/06-routing/06-domain-based)

[`domains`](https://next-intl.dev/docs/routing/configuration#domains) 설정을 사용 중이라면, 미들웨어는 요청을 사용 가능한 도메인과 매칭하여 최적 로케일을 결정합니다. 도메인을 가져오기 위해 `x-forwarded-host` header에서 host를 읽고, 없으면 `host`를 대체로 사용합니다(호스팅 플랫폼은 일반적으로 이 헤더를 기본 제공함).

로케일은 다음 우선순위에 따라 감지됩니다:

  1. pathname에 로케일 프리픽스가 있음 (예: `ca.example.com/fr`)
  2. 쿠키에 저장된 로케일이 있으며 해당 도메인에서 지원됨
  3. 도메인이 지원하는 로케일이 [`accept-language` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)를 기반으로 매칭됨
  4. 대체 수단으로 도메인의 `defaultLocale` 사용

미들웨어는 모든 도메인을 인지하고 있으므로, 어떤 도메인이 지원하지 않는 로케일에 대한 요청을 받으면(예: `en.example.com/fr`) 해당 로케일을 지원하는 다른 도메인으로 리디렉션합니다.

**예시 워크플로:**

  1. 사용자가 `us.example.com`을 요청하고, 이 도메인의 `defaultLocale`에 따라 `en` 로케일이 매칭됩니다.
  2. 앱은 사용자가 로케일을 `fr`로 변경할 수 있도록 `<Link locale="fr" href="/">Switch to French</Link>`를 렌더링합니다.
  3. 링크를 클릭하면 `us.example.com/fr`로 요청이 시작됩니다.
  4. 미들웨어는 사용자가 다른 도메인으로 전환하려는 것을 인식하고 `ca.example.com/fr`로 리디렉션 응답을 반환합니다.

## Matcher 설정[](https://next-intl.dev/docs/routing/middleware#matcher-config)

미들웨어는 페이지에서만 실행되도록 의도되었으며, 사용자 로케일과 무관하게 독립적으로 제공되는 임의 파일(예: `/favicon.ico`)에서는 실행되지 않아야 합니다.

널리 쓰이는 전략은 특정 세그먼트(예: `/_next`)로 시작하지 않는 모든 라우트를 매칭하고, 점(`.`)을 포함하는 라우트는 제외하는 것입니다. 점이 포함되면 일반적으로 정적 파일을 의미하기 때문입니다. 다만 점이 예상되는 라우트(예: `/users/jane.doe`)가 있다면, 해당 라우트용 matcher를 명시적으로 제공해야 합니다.

proxy.ts
```
    export const config = {
      // Matcher entries are linked with a logical "or", therefore
      // if one of them matches, the middleware will be invoked.
      matcher: [
        // Match all pathnames except for
        // - … if they start with `/api`, `/_next` or `/_vercel`
        // - … the ones containing a dot (e.g. `favicon.ico`)
        '/((?!api|_next|_vercel|.*\\..*).*)',

        // However, match all pathnames within `/users`, optionally with a locale prefix
        '/([\\w-]+)?/users/(.+)'
      ]
    };
```

[Vercel Analytics](https://vercel.com/analytics) 같은 일부 서드파티 제공자는 일반적으로 내부 엔드포인트를 사용한 뒤 이를 외부 URL로 리라이트합니다(예: `/_vercel/insights/view`). 이런 요청이 실수로 리라이트되지 않도록 미들웨어 matcher에서 반드시 제외하세요.

## 다른 미들웨어와 조합하기[](https://next-intl.dev/docs/routing/middleware#composing-other-middlewares)

`createMiddleware`를 호출하면 다음 타입의 함수를 받게 됩니다:
```
    function middleware(request: NextRequest): NextResponse;
```

추가 동작을 포함해야 한다면, `next-intl` 미들웨어가 요청을 받기 전에 요청을 수정하거나, 응답을 수정하거나, 동적 구성을 기반으로 미들웨어를 생성할 수도 있습니다.

proxy.ts
```
    import createMiddleware from 'next-intl/middleware';
    import {NextRequest} from 'next/server';

    export default async function proxy(request: NextRequest) {
      // Step 1: Use the incoming request (example)
      const defaultLocale = request.headers.get('x-your-custom-locale') || 'en';

      // Step 2: Create and call the next-intl middleware (example)
      const handleI18nRouting = createMiddleware({
        locales: ['en', 'de'],
        defaultLocale
      });
      const response = handleI18nRouting(request);

      // Step 3: Alter the response (example)
      response.headers.set('x-your-custom-locale', defaultLocale);

      return response;
    }

    export const config = {
      // Match only internationalized pathnames
      matcher: '/((?!api|trpc|_next|_vercel|.*\\..*).*)'
    };
```

### 예시: 추가 리라이트[](https://next-intl.dev/docs/routing/middleware#example-additional-rewrites)

`next-intl`이 제공하는 것 외의 리라이트를 처리해야 한다면, `next-intl` 미들웨어가 실행된 뒤 조건부로 [`NextResponse.rewrite()`](https://nextjs.org/docs/app/api-reference/functions/next-response#rewrite)를 호출할 수 있습니다.

이 예시는 특수 쿠키가 설정되어 있으면 `/[locale]/profile` 요청을 `/[locale]/profile/new`로 리라이트합니다.

proxy.ts
```
    import createMiddleware from 'next-intl/middleware';
    import {NextRequest, NextResponse} from 'next/server';
    import {routing} from './i18n/routing';

    const handleI18nRouting = createMiddleware(routing);

    export default async function proxy(request: NextRequest) {
      let response = handleI18nRouting(request);

      // Additional rewrite when NEW_PROFILE cookie is set
      if (response.ok) {
        // (not for errors or redirects)
        const [, locale, ...rest] = new URL(
          response.headers.get('x-middleware-rewrite') || request.url
        ).pathname.split('/');
        const pathname = '/' + rest.join('/');

        if (
          pathname === '/profile' &&
          request.cookies.get('NEW_PROFILE')?.value === 'true'
        ) {
          response = NextResponse.rewrite(
            new URL(`/${locale}/profile/new`, request.url),
            {headers: response.headers}
          );
        }
      }

      return response;
    }

    export const config = {
      // Match only internationalized pathnames
      matcher: '/((?!api|trpc|_next|_vercel|.*\\..*).*)'
    };
```

라우팅 구성과 사용 사례에 맞게 이를 커스터마이즈할 수 있습니다.

### 스타터 템플릿 (auth, saas, tenants)[](https://next-intl.dev/docs/routing/middleware#starter-templates-auth-saas-tenants)

🌐 [learn.next-intl.dev](https://learn.next-intl.dev)는 미들웨어 조합이 포함된 추가 스타터 템플릿을 제공합니다.

**포함 항목:**

  * **`app-router-auth` with Better Auth**: 사용자 설정의 로케일을 사용하는 인증 보호 앱
  * **`app-router-saas` with Better Auth**: 공개 라우트에는 로케일 프리픽스를 적용하고, 보호된 앱으로 로그인하는 구조
  * **`app-router-tenants`** : 여러 로케일을 지원하면서 다중 테넌트와 랜딩 페이지 사이를 라우팅하는 고급 조합 패턴

[소스 코드](https://learn.next-intl.dev/#project-code)

## 프록시 / 미들웨어 없이 사용하기 (static export)[](https://next-intl.dev/docs/routing/middleware#usage-without-proxy--middleware-static-export)

Next.js의 [static export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports) 기능(`output: 'export'`)을 사용하면 프록시 / 미들웨어는 실행되지 않습니다. 그럼에도 [프리픽스 기반 라우팅](https://next-intl.dev/docs/routing/configuration#locale-prefix)을 사용해 앱을 국제화할 수 있지만, 몇 가지 트레이드오프가 있습니다.

**Static export 제한 사항:**

  1. 로케일 프리픽스 사용이 필수입니다 ([`localePrefix: 'always'`](https://next-intl.dev/docs/routing/configuration#locale-prefix-always)와 동일)
  2. 서버에서 로케일 협상을 할 수 없습니다 ([`localeDetection: false`](https://next-intl.dev/docs/routing/configuration#locale-detection)와 동일)
  3. 서버 측 리라이트가 필요하므로 [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames)를 사용할 수 없습니다
  4. [정적 렌더링](https://next-intl.dev/docs/routing/setup#static-rendering)이 필수입니다

또한 Next.js 문서에 명시된 다른 [제한 사항](https://nextjs.org/docs/app/building-your-application/deploying/static-exports#unsupported-features)도 동일하게 적용됩니다.

이 접근을 선택한다면 앱 루트에 리디렉션을 활성화하는 것이 좋을 수 있습니다:

app/page.tsx
```
    import {redirect} from 'next/navigation';

    // Redirect the user to the default locale when `/` is requested
    export default function RootPage() {
      redirect('/en');
    }
```

`app/page.tsx`에 이런 루트 페이지를 추가했다면, `children`을 그대로 전달만 하더라도 `app/layout.tsx`에 루트 레이아웃도 함께 추가해야 합니다:

app/layout.tsx
```
    export default function RootLayout({children}) {
      return children;
    }
```

## 문제 해결[](https://next-intl.dev/docs/routing/middleware#troubleshooting)

### ”특정 페이지에서 프록시 / 미들웨어가 실행되지 않습니다.”[](https://next-intl.dev/docs/routing/middleware#middleware-not-running)

이를 해결하려면 다음을 확인하세요:

  1. [프록시 / 미들웨어](https://next-intl.dev/docs/routing/setup#proxy)가 올바른 파일(예: `src/proxy.ts`)에 설정되어 있는지.
  2. [`matcher`](https://next-intl.dev/docs/routing/middleware#matcher-config)가 점 같은 예상 밖 문자가 포함될 수 있는 동적 세그먼트(예: `/users/jane.doe`)를 포함해 애플리케이션의 모든 라우트를 올바르게 매칭하는지.
  3. [다른 미들웨어와 조합](https://next-intl.dev/docs/routing/middleware#composing-other-middlewares)하는 경우, 미들웨어가 올바르게 호출되는지.
  4. 정적 렌더링이 필요한 경우 [`force-static`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) 같은 우회 방법에 의존하지 말고 [정적 렌더링 가이드](https://next-intl.dev/docs/routing/setup#static-rendering)를 따르고 있는지.

### ”pathname에 로케일 프리픽스가 포함되어 있는데도 페이지 콘텐츠가 현지화되지 않습니다.”[](https://next-intl.dev/docs/routing/middleware#content-not-localized)

이는 요청에서 [프록시 / 미들웨어가 실행되지 않은](https://next-intl.dev/docs/routing/middleware#middleware-not-running) 결과일 가능성이 매우 높습니다. 그 결과 [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#i18n-request)의 잠재적 폴백이 적용될 수 있습니다.

### ”이 요청에서 프록시 / 미들웨어가 실행되지 않았고 `getRequestConfig`에서 `locale`이 반환되지 않아 `next-intl` 로케일을 찾을 수 없습니다.”[](https://next-intl.dev/docs/routing/middleware#unable-to-find-locale)

이 요청에서 미들웨어가 실행되지 _않는 것이_ 의도된 경우(예: 로케일 기반 라우팅이 없는 설정을 사용하는 경우), 이 오류에서 복구하려면 [`getRequestConfig`](https://next-intl.dev/docs/usage/configuration#i18n-request)에서 `locale`을 명시적으로 반환해야 합니다.

미들웨어가 실행될 것으로 예상된다면, [미들웨어가 올바르게 설정되었는지](https://next-intl.dev/docs/routing/middleware#middleware-not-running) 확인하세요.

`next-intl`은 `getRequestConfig`가 실행된 후 사용 가능한 로캘이 없으면 렌더링을 중단하기 위해 `notFound()` 함수를 호출한다는 점에 유의하세요. 이 때문에 [`not-found` 페이지](https://next-intl.dev/docs/environments/error-files#not-foundjs)를 추가하는 것을 고려해야 합니다.

