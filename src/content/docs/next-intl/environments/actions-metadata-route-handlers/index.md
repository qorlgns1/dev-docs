---
title: '서버 액션, 메타데이터 및 라우트 핸들러'
description: 'Next.js 앱에서는 React 컴포넌트 밖에서도 국제화를 적용할 수 있는 위치가 몇 가지 있습니다:'
---

Source URL: https://next-intl.dev/docs/environments/actions-metadata-route-handlers

[문서](https://next-intl.dev/docs/getting-started "Docs")[환경](https://next-intl.dev/docs/environments "Environments")서버 액션, 메타데이터 및 라우트 핸들러

# 서버 액션, 메타데이터 및 라우트 핸들러

Next.js 앱에서는 React 컴포넌트 밖에서도 국제화를 적용할 수 있는 위치가 몇 가지 있습니다:

  1. [메타데이터 API](https://nextjs.org/docs/app/building-your-application/optimizing/metadata)
  2. [서버 액션](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)
  3. [Open Graph 이미지](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  4. [매니페스트](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
  5. [사이트맵](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  6. [라우트 핸들러](https://nextjs.org/docs/app/building-your-application/routing/router-handlers)

`next-intl/server`는 이러한 경우에 사용할 수 있는 [await 가능한 함수](https://next-intl.dev/docs/environments/server-client-components#async-components) 세트를 제공합니다.

### 메타데이터 API[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#metadata-api)

페이지 제목 같은 메타데이터를 국제화하려면, 페이지와 레이아웃에서 export할 수 있는 [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function) 함수에서 `next-intl` 기능을 사용할 수 있습니다.

layout.tsx
```
    import {getTranslations} from 'next-intl/server';

    export async function generateMetadata({params}) {
      const {locale} = await params;
      const t = await getTranslations({locale, namespace: 'Metadata'});

      return {
        title: t('title')
      };
    }
```

💡

`next-intl`의 await 가능한 함수에 명시적으로 `locale`를 전달하면, [locale 기반 라우팅](https://next-intl.dev/docs/routing)을 사용하는 경우 메타데이터 핸들러가 [정적 렌더링](https://next-intl.dev/docs/routing/setup#static-rendering) 대상이 될 수 있습니다.

### 서버 액션[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#server-actions)

[서버 액션](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)은 클라이언트에서 호출되는 서버 측 코드를 실행하는 메커니즘을 제공합니다. 사용자에게 보여지는 메시지를 반환하는 경우, 사용자의 locale에 맞춰 `next-intl`로 이를 현지화할 수 있습니다.
```
    import {getTranslations} from 'next-intl/server';

    async function loginAction(data: FormData) {
      'use server';

      const t = await getTranslations('LoginForm');
      const areCredentialsValid = /* ... */;
      if (!areCredentialsValid) {
        return {error: t('invalidCredentials')};
      }
    }
```

Server Actions에서 생성된 메시지를 사용자에게 표시할 때는, 메시지가 표시되는 동안 사용자가 locale을 변경할 수 있는 경우를 고려해 UI가 일관되게 현지화되도록 해야 합니다. 라우팅 전략의 일부로 [a `[locale]` segment](https://next-intl.dev/docs/routing)를 사용 중이라면 이는 자동으로 처리됩니다. 그렇지 않다면 `key={locale}`를 통해 해당 컴포넌트의 [state를 재설정](https://react.dev/learn/preserving-and-resetting-state#resetting-a-form-with-a-key)하여 메시지를 수동으로 지우는 방법을 고려할 수 있습니다.

[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#server-actions-zod)검증에 Zod를 사용할 때 오류 메시지를 어떻게 현지화할 수 있나요?

[Zod](https://zod.dev/)는 parse 호출별로 오류 메시지를 커스터마이즈할 수 있는 [contextual error map](https://zod.dev/ERROR_HANDLING?id=contextual-error-map)을 제공합니다. locale은 특정 요청에 종속되므로, 이 메커니즘은 `zod`의 구조화된 오류를 현지화된 메시지로 변환하는 데 유용합니다:
```
    import {getTranslations} from 'next-intl/server';
    import {loginUser} from '@/services/session';
    import {z} from 'zod';

    const loginFormSchema = z.object({
      email: z.string().email(),
      password: z.string().min(1)
    });

    // ...

    async function loginAction(data: FormData) {
      'use server';

      const t = await getTranslations('LoginForm');
      const values = Object.fromEntries(data);

      const result = loginFormSchema.safeParse(values, {
        error(issue) {
          if (issue.path) {
            const path = issue.path.join('.');
            return {
              email: t('invalidEmail'),
              password: t('invalidPassword')
            }[path];
          }
        }
      });

      // ...
    }
```

### Open Graph 이미지[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#open-graph-images)

[Open Graph 이미지](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)를 프로그래밍 방식으로 생성하는 경우, export된 컴포넌트에서 `next-intl` 함수를 호출할 수 있습니다:

app/[locale]/opengraph-image.tsx
```
    import {ImageResponse} from 'next/og';
    import {getTranslations} from 'next-intl/server';

    export default async function OpenGraphImage({params}) {
      const {locale} = await params;
      const t = await getTranslations({locale, namespace: 'OpenGraphImage'});
      return new ImageResponse(<div style={{fontSize: 128}}>{t('title')}</div>);
    }
```

Next.js는 `opengraph-image.tsx`가 배치된 세그먼트를 기준으로 공개 라우트를 생성합니다. 예:
```
    http://localhost:3000/en/opengraph-image?f87b2d56cee109c7
```

하지만 [locale 기반 라우팅](https://next-intl.dev/docs/routing)을 사용하고 [`localePrefix`](https://next-intl.dev/docs/routing/configuration#locale-prefix) 설정을 커스터마이즈했다면, Next.js가 middleware의 잠재적 rewrite를 알지 못하므로 이 라우트에 접근하지 못할 수 있습니다.

이 경우에는 `opengraph-image.tsx` 파일 요청을 우회하도록 [matcher](https://next-intl.dev/docs/routing/middleware#matcher-config)를 조정할 수 있습니다:

proxy.ts
```
    // ...

    export const config = {
      matcher: [
        // Skip all paths that should not be internationalized
        '/((?!api|_next|_vercel|.*/opengraph-image|.*\\..*).*)'

        // ...
      ]
    };
```

### 매니페스트[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#manifest)

[manifest file](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)는 `app` 폴더 루트(`[`locale]` 동적 세그먼트 바깥)에 위치해야 하므로, `next-intl`이 pathname에서 locale을 추론할 수 없기 때문에 locale을 명시적으로 제공해야 합니다:

app/manifest.ts
```
    import {MetadataRoute} from 'next';
    import {getTranslations} from 'next-intl/server';

    export default async function manifest(): Promise<MetadataRoute.Manifest> {
      // Pick a locale that is representative of the app
      const locale = 'en';

      const t = await getTranslations({
        namespace: 'Manifest',
        locale
      });

      return {
        name: t('name'),
        start_url: '/',
        theme_color: '#101E33'
      };
    }
```

### 사이트맵[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#sitemap)

사이트의 모든 페이지를 검색 엔진에 알리기 위해 사이트맵을 사용한다면, 각 URL에 locale별 [alternate entries](https://developers.google.com/search/docs/specialty/international/localized-versions#sitemap)를 추가하여 특정 페이지가 여러 언어 또는 지역에서 제공됨을 나타낼 수 있습니다.

기본적으로 `next-intl`은 페이지가 여러 언어로 제공된다는 사실을 검색 엔진에 알리기 위해 [`link`](https://next-intl.dev/docs/routing/configuration#alternate-links) 응답 헤더를 반환한다는 점에 유의하세요. 이 방식만으로도 검색 엔진에 현지화된 페이지를 충분히 연결할 수 있지만, 더 구체적인 요구사항이 있다면(예: `articleSlug`가 locale에 따라 달라지는 `/news/[articleSlug]` 같은 CMS 기반 URL 사용 시) 이 정보를 사이트맵에서 제공하도록 선택할 수 있습니다.

Next.js는 [`alternates`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generate-a-localized-sitemap) 항목을 통해 언어별 대체 URL 제공을 지원하며, 이를 [`getPathname`](https://next-intl.dev/docs/routing/navigation#getpathname)과 결합해 각 locale의 URL을 구성할 수 있습니다:
```
    import {MetadataRoute} from 'next';
    import {getPathname} from '@/i18n/navigation';

    const host = 'https://acme.com';

    export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
      return [
        {
          url: host,
          lastModified: new Date(),
          alternates: {
            languages: {
              es: host + (await getPathname({locale: 'es', href: '/'})),
              de: host + (await getPathname({locale: 'de', href: '/'}))
            }
          }
        }
      ];
    }
```

**더 알아보기:**

[사이트맵](https://learn.next-intl.dev/chapters/08-seo/04-sitemap)

[CMS 기반 URL](https://learn.next-intl.dev/chapters/07-content/03-cms-driven-urls)

### 라우트 핸들러[](https://next-intl.dev/docs/environments/actions-metadata-route-handlers#route-handlers)

[Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/router-handlers)에서도 `next-intl`을 사용할 수 있습니다. `locale`은 search param, layout segment 또는 요청의 `accept-language` 헤더 파싱을 통해 받을 수 있습니다.

app/api/hello/route.tsx
```
    import {NextResponse} from 'next/server';
    import {hasLocale} from 'next-intl';
    import {getTranslations} from 'next-intl/server';
    import {routing} from '@/i18n/routing';

    export async function GET(request) {
      // Example: Receive the `locale` via a search param
      const {searchParams} = new URL(request.url);
      const locale = searchParams.get('locale');
      if (!hasLocale(routing.locales, locale)) {
        return NextResponse.json({error: 'Invalid locale'}, {status: 400});
      }

      const t = await getTranslations({locale, namespace: 'Hello'});
      return NextResponse.json({title: t('title')});
    }
```

