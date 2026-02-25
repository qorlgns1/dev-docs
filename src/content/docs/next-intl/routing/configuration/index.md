---
title: '라우팅 구성'
description: "import {defineRouting} from 'next-intl/routing';"
---

원문 URL: https://next-intl.dev/docs/routing/configuration

# 라우팅 구성

## `defineRouting`[](https://next-intl.dev/docs/routing/configuration#definerouting)

[middleware](https://next-intl.dev/docs/routing/middleware)와 [navigation APIs](https://next-intl.dev/docs/routing/navigation) 간에 공유되는 라우팅 구성은 `defineRouting` 함수를 사용해 정의할 수 있습니다.

src/i18n/routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // A list of all locales that are supported
      locales: ['en', 'de'],

      // Used when no locale matches
      defaultLocale: 'en'
    });
```

라우팅 요구사항에 따라 추가 설정이 필요할 수 있습니다. 아래를 참고하세요.

[](https://next-intl.dev/docs/routing/configuration#locales-unknown)빌드 시점에 `locales`를 알 수 없다면 어떻게 하나요?

런타임에 `locales`가 추가/제거될 수 있는 앱을 만드는 경우, middleware용 라우팅 구성을 [요청별로 동적으로](https://next-intl.dev/docs/routing/middleware#composing-other-middlewares) 제공할 수 있습니다.

이 경우 해당 navigation APIs를 만들 때 `createNavigation`에서 [`locales` 인수를 생략](https://next-intl.dev/docs/routing/navigation#locales-unknown)할 수 있습니다.

그래도 다른 라우팅 구성을 정의한다면, middleware와 navigation APIs 간 설정이 서로 동기화되도록 해야 합니다.

### `localePrefix`[](https://next-intl.dev/docs/routing/configuration#localeprefix)

기본적으로 앱의 경로명은 디렉터리 구조와 일치하는 프리픽스로 제공됩니다(예: `/en/about` → `app/[locale]/about/page.tsx`). 하지만 `localePrefix` 설정으로 프리픽스를 선택적으로 제거하거나 로케일별로 커스터마이즈할 수 있습니다.

**자세히 보기:**

[Prefix-based routing](https://learn.next-intl.dev/chapters/06-routing/07-prefix-based)

#### `localePrefix: 'always'` (기본값)[](https://next-intl.dev/docs/routing/configuration#locale-prefix-always)

기본적으로 경로명은 항상 로케일로 시작합니다(예: `/en/about`).

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // ...
      localePrefix: 'always'
    });
```

#### `localePrefix: 'as-needed'`[](https://next-intl.dev/docs/routing/configuration#locale-prefix-as-needed)

기본 로케일에는 프리픽스를 사용하지 않고(예: `/about`), 다른 로케일에는 유지하려면(예: `/de/about`) 다음처럼 라우팅을 구성할 수 있습니다.

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // ...
      localePrefix: 'as-needed'
    });
```

**참고:**

  1. 이 라우팅 전략을 사용한다면 [`matcher`](https://next-intl.dev/docs/routing/middleware#matcher-config)가 프리픽스 없는 경로명을 감지하도록 설정해야 합니다.
  2. middleware는 기본적으로 사용자의 로케일 선호를 기억하기 위해 [cookie](https://next-intl.dev/docs/routing/configuration#locale-cookie)를 설정합니다. 경로명에 명시적인 로케일 프리픽스가 없다면, [로케일 감지](https://next-intl.dev/docs/routing/middleware#locale-detection-prefix)에 의해 cookie 값을 기준으로 마지막으로 일치한 로케일로 리디렉션될 수 있습니다(예: `/` → `/de`).
  3. `/en/about` 같은 불필요한 로케일 프리픽스가 요청되면 middleware는 자동으로 프리픽스 없는 버전 `/about`으로 리디렉션합니다. 이는 다른 로케일에서 리디렉션할 때 cookie 값을 먼저 업데이트하려는 경우에 유용합니다(예: [`<Link />`](https://next-intl.dev/docs/routing/navigation#link)는 이 메커니즘에 의존합니다).

#### `localePrefix: 'never'`[](https://next-intl.dev/docs/routing/configuration#locale-prefix-never)

예를 들어 사용자 설정 기반으로 `next-intl`에 로케일을 제공하려는 경우, 애초에 로케일 기반 라우팅을 사용하지 않는 것도 고려할 수 있습니다.

하지만 middleware를 구성해 URL에 로케일 프리픽스가 절대 표시되지 않게 할 수도 있으며, 다음 경우에 유용합니다.

  1. [도메인 기반 라우팅](https://next-intl.dev/docs/routing/configuration#domains)을 사용하고 도메인당 로케일이 하나뿐인 경우
  2. 정적 렌더링을 활성화한 상태에서 cookie로 로케일을 결정하고 싶은 경우

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // ...
      localePrefix: 'never'
    });
```

이 경우 모든 로케일 요청은 내부적으로만 로케일 프리픽스가 붙도록 rewrite됩니다. 라우트가 `locale` 파라미터를 받을 수 있도록 모든 페이지를 여전히 `[locale]` 폴더 안에 배치해야 합니다.

**참고:**

  1. 이 라우팅 전략을 사용한다면 [`matcher`](https://next-intl.dev/docs/routing/middleware#matcher-config)가 프리픽스 없는 경로명을 감지하도록 설정해야 합니다.
  2. 이 모드에서는 로케일별 URL이 고유하지 않을 수 있으므로 [alternate links](https://next-intl.dev/docs/routing/configuration#alternate-links)가 비활성화됩니다. 따라서 직접 포함하거나, `alternates`로 현지화된 페이지를 연결하는 [sitemap](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#sitemap)을 구성하는 것을 고려하세요.
  3. 세션 간 사용자 선호를 더 오래 기억하려면 로케일 cookie의 [`maxAge`](https://next-intl.dev/docs/routing/configuration#locale-cookie) 속성을 더 길게 설정하는 것을 고려할 수 있습니다.

#### `prefixes`[](https://next-intl.dev/docs/routing/configuration#locale-prefix-prefixes)

사용자에게 보이는 프리픽스를 커스터마이즈하려면 로케일 기반 매핑을 제공할 수 있습니다.

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      locales: ['en-US', 'de-AT', 'zh'],
      defaultLocale: 'en-US',
      localePrefix: {
        mode: 'always',
        prefixes: {
          'en-US': '/us',
          'de-AT': '/eu/at'
          // (/zh will be used as-is)
        }
      }
    });
```

**참고:**

  1. 사용자 지정 프리픽스와 일치하도록 [`matcher`](https://next-intl.dev/docs/routing/middleware#matcher-config)를 조정해야 합니다.
  2. 사용자 지정 프리픽스는 사용자에게만 보이며 내부적으로 해당 로케일로 rewrite됩니다. 따라서 `[locale]` 세그먼트는 프리픽스가 아니라 로케일에 해당합니다.

[](https://next-intl.dev/docs/routing/configuration#locale-prefix-custom-read-prefix)앱에서 매칭된 프리픽스를 읽을 수 있나요?

사용자 지정 프리픽스는 내부적으로 로케일로 rewrite되므로 프리픽스 자체에는 직접 접근할 수 없습니다. 하지만 로케일에서 지역 같은 정보를 추출할 수는 있습니다.
```
    import {useLocale} from 'next-intl';

    function Component() {
      // Assuming the locale is 'en-US'
      const locale = useLocale();

      // Extracts the "US" region
      const {region} = new Intl.Locale(locale);
    }
```

지역은 유효한 [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) 또는 [UN M49 region code](https://en.wikipedia.org/wiki/UN_M49#Code_lists)여야 합니다. `Intl.Locale`에 전달되면 지역 코드는 대소문자를 구분하지 않고 대문자로 정규화됩니다. 언어가 원어로 사용되지 않는 지역과 언어를 조합할 수도 있습니다(예: `en-AT`는 오스트리아에서 사용되는 영어를 의미).

지역 외에도 로케일은 숫자 체계 같은 [추가 속성](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale#description)을 인코딩할 수 있습니다.

로케일에 커스텀 정보를 인코딩하려면 `-x-` 프리픽스로 표시되는 임의의 [private extensions](https://tc39.es/proposal-intl-locale/#sec-insert-unicode-extension-and-canonicalize)를 사용할 수 있습니다(예: `en-US-x-usd`). `Intl.Locale` 생성자는 private extensions를 무시하지만, 로케일 문자열에서 수동으로 추출할 수 있습니다.

### `pathnames`[](https://next-intl.dev/docs/routing/configuration#pathnames)

영상으로 보는 것이 더 편하신가요?

[Localized pathnames](https://learn.next-intl.dev/chapters/06-routing/08-localized-pathnames)

많은 앱이 특히 검색 엔진 최적화가 중요한 경우 경로명을 현지화합니다.

**예시:**

  * `/en/about`
  * `/de/über-uns`

일반적으로 내부에서는 이 라우트들을 한 번만 정의하고 싶기 때문에, `next-intl` middleware를 사용해 이런 들어오는 요청을 공용 경로명으로 [rewrite](https://nextjs.org/docs/api-reference/next.config.js/rewrites)할 수 있습니다.

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      locales: ['en-US', 'en-UK', 'de'],
      defaultLocale: 'en-US',

      // The `pathnames` object holds pairs of internal and
      // external paths. Based on the locale, the external
      // paths are rewritten to the shared, internal ones.
      pathnames: {
        // If all locales use the same pathname, a single
        // external path can be used for all locales
        '/': '/',
        '/blog': '/blog',

        // If locales use different paths, you can
        // specify the relevant external pathnames
        '/services': {
          de: '/leistungen'
        },

        // Encoding of non-ASCII characters is handled
        // automatically where relevant
        '/about': {
          de: '/über-uns'
        },

        // Dynamic params are supported via square brackets
        '/news/[articleSlug]': {
          de: '/neuigkeiten/[articleSlug]'
        },

        // Static pathnames that overlap with dynamic segments
        // will be prioritized over the dynamic segment
        '/news/just-in': {
          de: '/neuigkeiten/aktuell'
        },

        // Also (optional) catch-all segments are supported
        '/categories/[...slug]': {
          de: '/kategorien/[...slug]'
        }
      }
    });
```

현지화된 경로명은 Next.js의 파일 시스템 기반 라우팅으로 생성된 단일 내부 경로명에 매핑됩니다. 위 예시에서 `/de/über-uns`는 `/[locale]/about/page.tsx`의 페이지가 처리합니다.

[](https://next-intl.dev/docs/routing/configuration#localized-pathnames-dynamic-segments)CMS 기반 URL을 어떻게 현지화하나요?

`/news/[articleSlug]` 같은 라우트가 있다면, 경로명을 다음처럼 현지화하고 싶을 수 있습니다.
```
    /en/news/launch-of-new-product
    /de/neuigkeiten/produktneuheit
```

이 경우 `pathnames`를 사용해 경로명의 정적 부분을 현지화할 수 있습니다.
```
    '/news/[articleSlug]': {
      de: '/neuigkeiten/[articleSlug]'
    }
```

… 그리고 동적 부분에는 CMS의 현지화된 slug를 사용하세요.

이렇게 할 때는 로케일 전환기와 alternate links도 CMS 기반 URL을 인지하도록 하여, 올바른 현지화 경로명을 가리키게 해야 합니다.

**자세히 보기:**

[ CMS-driven URLs](https://learn.next-intl.dev/chapters/07-content/03-cms-driven-urls)

[](https://next-intl.dev/docs/routing/configuration#localized-pathnames-revalidation)현지화된 경로명은 어떻게 revalidate하나요?

라우트가 정적으로(빌드 시) 생성되는지 동적으로(런타임) 생성되는지에 따라 [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)를 현지화 경로명 또는 내부 경로명에 호출해야 합니다.

다음 예시를 보겠습니다.
```
    app
    └── [locale]
        └── news
            └── [slug]
```

… 그리고 다음 라우팅 구성이 있다고 할 때:

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      locales: ['en', 'de'],
      defaultLocale: 'en',
      pathnames: {
        '/news/[slug]': {
          en: '/news/[slug]',
          de: '/neuigkeiten/[slug]'
        }
      }
    });
```

`some-article`이 [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)에 포함되었는지 여부에 따라 다음처럼 라우트를 revalidate할 수 있습니다.
```
    // Statically generated at build time
    revalidatePath('/de/news/some-article');

    // Dynamically generated at runtime:
    revalidatePath('/de/neuigkeiten/some-article');
```

확신이 없다면 `revalidateTag`로 대신 revalidate할 수 있습니다.

참고: [`vercel/next.js#59825`](https://github.com/vercel/next.js/issues/59825)

### `domains`[](https://next-intl.dev/docs/routing/configuration#domains)

영상으로 보는 것이 더 편하신가요?

[Domain-based routing](https://learn.next-intl.dev/chapters/06-routing/06-domain-based)

서로 다른 도메인 기준으로 현지화 콘텐츠를 제공하려면, `domains` 설정으로 도메인과 로케일 간 매핑 목록을 제공할 수 있습니다.

**예시:**

  * `us.example.com`: `en-US`
  * `ca.example.com`: `en-CA`
  * `ca.example.com/fr`: `fr-CA`
  * `fr.example.com`: `fr-FR`

많은 경우 위와 같은 결과를 위해 `domains`는 [`localePrefix`](https://next-intl.dev/docs/routing/configuration#locale-prefix) 설정과 함께 사용됩니다. 또한 로케일별 사용자 노출 프리픽스를 커스터마이즈하기 위해 [custom prefixes](https://next-intl.dev/docs/routing/configuration#locale-prefix-prefixes)를 사용할 수 있습니다.

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      locales: ['en-US', 'en-CA', 'fr-CA', 'fr-FR'],
      defaultLocale: 'en-US',
      domains: [
        {
          domain: 'us.example.com',
          defaultLocale: 'en-US',
          locales: ['en-US']
        },
        {
          domain: 'ca.example.com',
          defaultLocale: 'en-CA',
          locales: ['en-CA', 'fr-CA']
        },
        {
          domain: 'fr.example.com',
          defaultLocale: 'fr-FR',
          locales: ['fr-FR']
        }
      ],
      localePrefix: {
        mode: 'as-needed',
        prefixes: {
          // Cleaner prefix for `ca.example.com/fr`
          'fr-CA': '/fr'
        }
      }
    });
```

로케일은 도메인 간 고유해야 하므로, 보통 충돌 방지를 위해 지역 변형을 사용합니다. 다만 사용 사례에 전체 언어만으로 충분하다면 각 로케일마다 반드시 [messages](https://next-intl.dev/docs/usage/configuration#messages)를 제공할 필요는 없습니다.

일치하는 도메인이 없으면 middleware는 [prefixes](https://next-intl.dev/docs/routing/middleware#location-detection-prefix) 기반 기본 로케일 매칭으로 폴백합니다(예: 로컬 개발 시 `localhost`).

참고: [Domain-based routing](https://next-intl.dev/docs/routing/middleware#location-detection-domain)

[](https://next-intl.dev/docs/routing/configuration#domains-localeprefix-individual)도메인별로 다른 `localePrefix` 설정을 사용할 수 있나요?

현재는 기본 제공되지 않지만, 환경 변수를 통해 서로 다른 라우팅 구성을 주입하면서 도메인별로 앱을 따로 빌드해 구현할 수 있습니다.

**예시:**

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    const isUsDomain =
      process.env.VERCEL_PROJECT_PRODUCTION_URL === 'us.example.com';

    export const routing = defineRouting({
      locales: isUsDomain ? ['en-US'] : ['en-CA', 'fr-CA'],
      defaultLocale: isUsDomain ? 'en-US' : 'en-CA',
      localePrefix: isUsDomain ? 'never' : 'always'
    });
```

### `localeDetection`[](https://next-intl.dev/docs/routing/configuration#locale-detection)

middleware는 라우팅 구성과 들어오는 요청을 기반으로 [일치하는 로케일을 감지](https://next-intl.dev/docs/routing/middleware#locale-detection)하고, 일치하면 요청을 통과시키고 아니면 일치하는 로케일로 리디렉션합니다.

로케일 결정에 URL만 전적으로 사용하고 싶다면 `localeDetection` 속성을 `false`로 설정할 수 있습니다. 이렇게 하면 `accept-language` 헤더 및 이전 방문에서 남았을 수 있는 cookie 값을 기반으로 한 로케일 감지가 비활성화됩니다.

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // ...
      localeDetection: false
    });
```

이 경우 로케일을 결정할 때 로케일 프리픽스와 잠재적인 [일치 도메인](https://next-intl.dev/docs/routing/configuration#domains)만 사용됩니다.

### `localeCookie`[](https://next-intl.dev/docs/routing/configuration#locale-cookie)

사용자가 로케일을 `accept-language` 헤더와 일치하지 않는 값으로 변경하면, `next-intl`은 가장 최근에 감지된 로케일을 담은 `NEXT_LOCALE`이라는 세션 쿠키를 설정합니다. 이는 이후 요청에서 사용자의 로케일 선호도를 [기억](https://next-intl.dev/docs/routing/middleware#locale-detection)하는 데 사용됩니다.

기본적으로 이 쿠키는 다음 속성으로 구성됩니다:

  2. [**`sameSite`**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#samesitesamesite-value): 외부 사이트에서 유입될 때도 쿠키를 설정할 수 있도록 이 값은 `lax`로 설정됩니다.
  3. [**`path`**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#pathpath-value): 이 값은 기본적으로 설정되지 않지만, 설정되어 있다면 [`basePath`](https://next-intl.dev/docs/routing/configuration#basepath) 값을 사용합니다.

더 구체적인 요구사항이 있다면, 다음과 같이 이 설정을 조정할 수 있습니다:

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // ...

      // Will be merged with the defaults
      localeCookie: {
        // Custom cookie name
        name: 'USER_LOCALE',
        // Expire in one year
        maxAge: 60 * 60 * 24 * 365
      }
    });
```

… 또는 쿠키를 완전히 비활성화할 수 있습니다:

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // ...

      localeCookie: false
    });
```

[](https://next-intl.dev/docs/routing/configuration#locale-cookie-gdpr)GDPR 준수를 위해 어떤 `maxAge` 값을 고려해야 하나요?

기본적으로 규정을 준수할 수 있도록 `next-intl`은 쿠키의 `max-age` 값을 설정하지 않습니다. 따라서 브라우저를 닫으면 만료되는 세션 쿠키가 됩니다.

법적 요구사항은 지역에 따라 달라질 수 있으므로, 이를 별도로 확인하는 것을 권장합니다. 이 정보를 최대한 최신으로 유지하려고 노력하지만, 정확성을 보장할 수는 없습니다.

**더 알아보기:**

[ Cookie regulations](https://learn.next-intl.dev/chapters/06-routing/09-cookie-regulations)

### `alternateLinks` (`hreflang`)[](https://next-intl.dev/docs/routing/configuration#alternate-links)

미들웨어는 검색 엔진에 콘텐츠가 여러 언어로 제공된다는 것을 알리기 위해 [`link`](https://developers.google.com/search/docs/specialty/international/localized-versions#http) 헤더를 자동으로 설정합니다. 이 기능은 라우팅 전략과 자동으로 통합되며, 설정에 맞춰 올바른 링크를 생성합니다.

하지만 다음과 같이 이 링크를 직접 제공하고 싶을 수 있는 경우도 있습니다:

  1. 특정 로케일에서만 제공되는 페이지가 있는 경우
  2. 페이지 경로명을 관리하기 위해 CMS 같은 외부 시스템을 사용하는 경우

이 경우 `alternateLinks`를 `false`로 설정하여 이 동작을 비활성화할 수 있습니다:

routing.ts
```
    import {defineRouting} from 'next-intl/routing';

    export const routing = defineRouting({
      // ...

      alternateLinks: false
    });
```

**더 알아보기:**

[hreflang & canonicals](https://learn.next-intl.dev/chapters/08-seo/03-alternate-links)

[Sitemaps](https://learn.next-intl.dev/chapters/08-seo/04-sitemap)

[](https://next-intl.dev/docs/routing/configuration#alternate-links-details)어떤 대체 링크가 포함되나요?

기본 미들웨어 설정을 사용하면, `/`에 대한 응답의 `link` 헤더는 다음과 같이 표시됩니다:
```
    link: <https://example.com/en>; rel="alternate"; hreflang="en",
          <https://example.com/de>; rel="alternate"; hreflang="de",
          <https://example.com/>; rel="alternate"; hreflang="x-default"
```

[`x-default`](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault) 항목은 사용자의 브라우저 설정과 일치하는 다른 언어가 없을 때 사용할 수 있는 변형을 가리키기 위해 포함됩니다. 이 특수 항목은 언어 선택 및 감지를 위해 예약되어 있으며, 이 경우 가장 잘 맞는 로케일로 307 리디렉션을 수행합니다.

완전한 URL을 제공하기 위해 도메인은 `x-forwarded-host` 헤더에서 읽고, 없으면 `host`로 대체합니다(호스팅 플랫폼은 일반적으로 이러한 헤더를 기본 제공함).

`domains`, `pathnames`, `basePath` 같은 옵션을 포함한 미들웨어 설정은 자동으로 반영됩니다.

[](https://next-intl.dev/docs/routing/configuration#alternate-links-customization)대체 링크를 커스터마이즈할 수 있나요?

대체 링크를 커스터마이즈해야 한다면, 이를 비활성화하고 자체 구현을 제공할 수 있습니다. 또는 사소한 조정만 필요하다면 [미들웨어를 조합](https://next-intl.dev/docs/routing/configuration#composing-other-middlewares)해 미들웨어 실행 후 사용자 정의 로직을 추가할 수 있습니다:

middleware.ts
```
    import createMiddleware from 'next-intl/middleware';
    import LinkHeader from 'http-link-header';
    import {NextRequest} from 'next/server';
    import {routing} from './i18n/routing';

    const handleI18nRouting = createMiddleware(routing);

    export default async function middleware(request: NextRequest) {
      const response = handleI18nRouting(request);

      // Example: Remove the `x-default` entry
      const link = LinkHeader.parse(response.headers.get('link'));
      link.refs = link.refs.filter((entry) => entry.hreflang !== 'x-default');
      response.headers.set('link', link.toString());

      return response;
    }
```

## `next.config.ts`[](https://next-intl.dev/docs/routing/configuration#next-config)

라우팅 설정 외에도 `next-intl`은 [`next.config.ts`](https://nextjs.org/docs/pages/api-reference/config/next-config-js)의 설정도 반영합니다.

### `basePath`[](https://next-intl.dev/docs/routing/configuration#basepath)

미들웨어와 내비게이션 API는 Next.js 설정에서 구성했을 수 있는 [`basePath`](https://nextjs.org/docs/app/api-reference/next-config-js/basePath)를 자동으로 고려합니다.

유일한 예외는 [`getPathname`](https://next-intl.dev/docs/routing/navigation#getpathname) 함수로, 이 함수는 base path가 없는 순수 pathname을 반환합니다. 따라서 필요하다면 반환된 pathname 앞에 수동으로 접두사를 붙일 수 있습니다.

base path를 사용하는 경우, [`matcher`](https://next-intl.dev/docs/routing/configuration#matcher-config)가 명시적 루트를 처리하도록 해야 합니다:

proxy.ts
```
    export const config = {
      // The `matcher` is relative to the `basePath`
      matcher: [
        // This entry handles the root of the base
        // path and should always be included
        '/'

        // ... other matcher config
      ]
    };
```

### `trailingSlash`[](https://next-intl.dev/docs/routing/configuration#trailingslash)

Next.js 설정에서 [`trailingSlash`](https://nextjs.org/docs/app/api-reference/next-config-js/trailingSlash)를 `true`로 설정한 경우, 이 설정은 미들웨어와 내비게이션 API에서 반영됩니다.

[`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames)를 사용하는 경우, 내부 및 외부 pathname은 후행 슬래시 포함 여부와 관계없이 정의할 수 있으며 내부적으로 정규화됩니다.

