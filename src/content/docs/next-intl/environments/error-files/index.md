---
title: 'Next.js 오류 파일에서의 국제화'
description: 'Next.js App Router의 파일 컨벤션은 오류 처리를 위해 사용할 수 있는 두 가지 파일을 제공합니다.'
---

원문 URL: https://next-intl.dev/docs/environments/error-files

[문서](https://next-intl.dev/docs/getting-started "Docs")[환경](https://next-intl.dev/docs/environments "Environments")오류 파일 (예: not-found)

# Next.js 오류 파일에서의 국제화

Next.js App Router의 파일 컨벤션은 오류 처리를 위해 사용할 수 있는 두 가지 파일을 제공합니다.

  1. [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)
  2. [`error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error)

이 페이지에서는 이러한 경우에 대한 실용적인 가이드를 제공합니다.

**팁:** 오류 처리가 포함된 동작 앱을 확인하려면 [App Router example](https://next-intl.dev/examples#app-router)을 살펴보세요.

## `not-found.js`[](https://next-intl.dev/docs/environments/error-files#not-foundjs)

💡

이 섹션은 [locale-based routing](https://next-intl.dev/docs/routing)을 사용하는 경우에만 관련이 있습니다.

Next.js는 라우트 세그먼트가 [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) 함수를 호출할 때 가장 가까운 `not-found` 페이지를 렌더링합니다. 이 메커니즘을 사용하면 `[locale]` 폴더 안에 `not-found` 파일을 추가해 지역화된 404 페이지를 제공할 수 있습니다.

app/[locale]/not-found.tsx
```
    import {useTranslations} from 'next-intl';

    export default function NotFoundPage() {
      const t = useTranslations('NotFoundPage');
      return <h1>{t('title')}</h1>;
    }
```

다만 Next.js는 일반적인 모든 알 수 없는 라우트에 대해 이 페이지를 렌더링하는 것이 아니라, 라우트 내부에서 `notFound` 함수가 호출될 때만 이 페이지를 렌더링합니다.

### 알 수 없는 라우트 처리[](https://next-intl.dev/docs/environments/error-files#catching-unknown-routes)

알 수 없는 라우트까지 처리하려면 `notFound` 함수를 명시적으로 호출하는 catch-all 라우트를 정의할 수 있습니다.

app/[locale]/[...rest]/page.tsx
```
    import {notFound} from 'next/navigation';

    export default function CatchAllPage() {
      notFound();
    }
```

이 변경 후에는 `[locale]` 세그먼트 내에서 매칭되는 모든 요청에서 알 수 없는 라우트를 만나면 `not-found` 페이지가 렌더링됩니다(예: `/en/unknown`).

### 로케일이 없는 요청 처리[](https://next-intl.dev/docs/environments/error-files#catching-non-localized-requests)

사용자가 `next-intl` [middleware](https://next-intl.dev/docs/routing/middleware)와 매칭되지 않는 라우트를 요청하면, 해당 요청에는 연결된 로케일이 없습니다([`matcher` config](https://next-intl.dev/docs/routing/middleware#matcher-config)에 따라 다르며, 예를 들어 `/unknown.txt`는 매칭되지 않을 수 있음).

이 경우까지 처리하려면 루트 `not-found` 페이지를 추가할 수 있습니다.

app/not-found.tsx
```
    'use client';

    import Error from 'next/error';

    export default function NotFound() {
      return (
        <html lang="en">
          <body>
          </body>
        </html>
      );
    }
```

`app/not-found.tsx`가 존재하면 루트 레이아웃이 반드시 필요합니다. 단순히 `children`을 그대로 전달하는 형태여도 됩니다.

app/layout.tsx
```
    // Since we have a root `not-found.tsx` page, a layout file
    // is required, even if it's just passing children through.
    export default function RootLayout({children}) {
      return children;
    }
```

404 페이지가 렌더링되려면, 들어오는 `locale` param이 유효하지 않다고 감지했을 때 루트 레이아웃에서 `notFound` 함수를 호출해야 합니다.

app/[locale]/layout.tsx
```
    import {hasLocale} from 'next-intl';
    import {notFound} from 'next/navigation';
    import {routing} from '@/i18n/routing';

    export default function LocaleLayout({children, params}) {
      const {locale} = await params;
      if (!hasLocale(routing.locales, locale)) {
        notFound();
      }

      // ...
    }
```

## `error.js`[](https://next-intl.dev/docs/environments/error-files#errorjs)

`error` 파일이 정의되면 Next.js는 레이아웃 내부에 [error boundary](https://nextjs.org/docs/app/building-your-application/routing/error-handling#how-errorjs-works)를 생성하고, 런타임 오류를 잡기 위해 해당 경계로 페이지를 감쌉니다.
```
```

Next.js가 내부적으로 생성하는 개략적인 컴포넌트 계층 구조입니다.

`error` 파일은 반드시 Client Component로 정의되어야 하므로, 렌더링될 경우 메시지를 제공하기 위해 [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider)를 사용해야 합니다.

layout.tsx
```
    import pick from 'lodash/pick';
    import {NextIntlClientProvider} from 'next-intl';
    import {getMessages} from 'next-intl/server';

    export default async function RootLayout(/* ... */) {
      const messages = await getMessages();

      return (
        <html lang={locale}>
          <body>
              {children}
          </body>
        </html>
      );
    }
```

`NextIntlClientProvider`를 설정하고 나면 `error` 파일에서 `next-intl` 기능을 사용할 수 있습니다.

error.tsx
```
    'use client';

    import {useTranslations} from 'next-intl';

    export default function Error({error, reset}) {
      const t = useTranslations('Error');

      return (
          <h1>{t('title')}</h1>
          <button onClick={reset}>{t('retry')}</button>
      );
    }
```

`error.tsx`는 앱이 초기화된 직후 로드된다는 점에 유의하세요. 앱이 성능에 민감하고 이 번들에 `next-intl` 번역 기능이 포함되어 로드되는 것을 피하고 싶다면, `error` 파일에서 lazy reference를 export할 수 있습니다.

error.tsx
```
    'use client';

    import {lazy} from 'react';

    // Move error content to a separate chunk and load it only when needed
    export default lazy(() => import('./Error'));
```

