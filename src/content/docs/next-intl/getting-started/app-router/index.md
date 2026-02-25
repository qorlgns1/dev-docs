---
title: 'Next.js App Router 국제화(i18n)'
description: '아직 하지 않았다면, App Router를 사용하는 Next.js 앱을 생성하고 다음을 실행하세요:'
---

Source URL: https://next-intl.dev/docs/getting-started/app-router

문서[시작하기](https://next-intl.dev/docs/getting-started "Getting started")App Router

# Next.js App Router 국제화(i18n)

동영상으로 보는 편이 좋으신가요?

[Set up next-intl](https://learn.next-intl.dev/chapters/03-translations/01-setup)

## 시작하기[](https://next-intl.dev/docs/getting-started/app-router#getting-started)

아직 하지 않았다면, App Router를 사용하는 [Next.js 앱을 생성](https://nextjs.org/docs/getting-started/installation)하고 다음을 실행하세요:
```
    npm install next-intl
```

이제 다음과 같은 파일 구조를 만들겠습니다:
```
    ├── messages
    │   ├── en.json
    │   └── ...
    ├── next.config.ts
    └── src
        ├── i18n
        │   └── request.ts
        └── app
            ├── layout.tsx
            └── page.tsx
```

**파일을 설정해봅시다:**

### `messages/en.json`[](https://next-intl.dev/docs/getting-started/app-router#messages)

메시지는 언어별로 사용 가능한 번역을 의미하며, 로컬에서 제공하거나 원격 데이터 소스에서 불러올 수 있습니다.

가장 간단한 방법은 로컬 프로젝트 폴더에 JSON 파일을 추가하는 것입니다:

messages/en.json
```
    {
      "HomePage": {
        "title": "Hello world!"
      }
    }
```

### `i18n/request.ts`[](https://next-intl.dev/docs/getting-started/app-router#i18n-request)

`next-intl`은 요청 범위(request-scoped)의 구성 객체를 생성하며, 이를 사용해 사용자의 로케일에 따라 메시지와 기타 옵션을 Server Components에 제공할 수 있습니다.

src/i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      // Static for now, we'll change this later
      const locale = 'en';

      return {
        locale,
        messages: (await import(`../../messages/${locale}.json`)).default
      };
    });
```

[](https://next-intl.dev/docs/getting-started/app-router#i18n-request-path)이 파일을 다른 위치로 옮겨도 되나요?

이 파일은 `src` 폴더와 프로젝트 루트 모두에서 `./i18n/request.ts`로 기본 지원되며, 확장자는 `.ts`, `.tsx`, `.js`, `.jsx`를 사용할 수 있습니다.

이 파일을 다른 위치로 옮기고 싶다면, 선택적으로 플러그인에 경로를 지정할 수 있습니다:

next.config.ts
```
    const withNextIntl = createNextIntlPlugin(
      // Specify a custom path here
      './somewhere/else/request.ts'
    );
```

### `next.config.ts`[](https://next-intl.dev/docs/getting-started/app-router#next-config)

이제 `i18n/request.ts` 파일을 `next-intl`에 연결하는 플러그인을 설정합니다.

next.config.tsnext.config.js

next.config.ts
```
    import {NextConfig} from 'next';
    import createNextIntlPlugin from 'next-intl/plugin';

    const nextConfig: NextConfig = {};

    const withNextIntl = createNextIntlPlugin();
    export default withNextIntl(nextConfig);
```

next.config.js
```
    const createNextIntlPlugin = require('next-intl/plugin');

    const withNextIntl = createNextIntlPlugin();

    /** @type {import('next').NextConfig} */
    const nextConfig = {};

    module.exports = withNextIntl(nextConfig);
```

### `app/layout.tsx`[](https://next-intl.dev/docs/getting-started/app-router#layout)

요청 구성을 Client Components에서 사용할 수 있도록, 루트 레이아웃에서 `children`을 `NextIntlClientProvider`로 감쌀 수 있습니다.

app/layout.tsx
```
    import {NextIntlClientProvider} from 'next-intl';

    type Props = {
      children: React.ReactNode;
    };

    export default async function RootLayout({children}: Props) {
      return (
        <html>
          <body>
          </body>
        </html>
      );
    }
```

### `app/page.tsx`[](https://next-intl.dev/docs/getting-started/app-router#page)

페이지 컴포넌트나 그 외 어디에서든 번역을 사용하세요!

app/page.tsx
```
    import {useTranslations} from 'next-intl';

    export default function HomePage() {
      const t = useTranslations('HomePage');
      return <h1>{t('title')}</h1>;
    }
```

비동기 컴포넌트의 경우, 대신 await 가능한 `getTranslations` 함수를 사용할 수 있습니다:

app/page.tsx
```
    import {getTranslations} from 'next-intl/server';

    export default async function HomePage() {
      const t = await getTranslations('HomePage');
      return <h1>{t('title')}</h1>;
    }
```

## 다음 단계[](https://next-intl.dev/docs/getting-started/app-router#next-steps)

### 로케일 기반 라우팅[](https://next-intl.dev/docs/getting-started/app-router#locale-based-routing)

앱이 지원하는 각 언어마다 고유한 경로명(예: `/en/about` 또는 `example.de/über-uns`)을 사용하고 싶다면, 앱에 최상위 `[locale]` 세그먼트를 설정하는 단계로 계속 진행할 수 있습니다.

[Set up locale-based routing→](https://next-intl.dev/docs/routing)

### 로케일 제공하기[](https://next-intl.dev/docs/getting-started/app-router#provide-a-locale)

앱에서 로케일별 고유 경로명이 필요하지 않다면, 사용자 선호도나 기타 애플리케이션 로직에 따라 `next-intl`에 로케일을 제공할 수 있습니다.

가장 간단한 방법은 쿠키를 사용하는 것입니다:

src/i18n/request.ts
```
    import {cookies} from 'next/headers';
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      const store = await cookies();
      const locale = store.get('locale')?.value || 'en';

      return {
        locale
        // ...
      };
    });
```

### 국제화는 단순히 단어를 번역하는 것만이 아닙니다[](https://next-intl.dev/docs/getting-started/app-router#internationalization-isnt-just-translating-words)

`next-intl`은 Next.js 앱 국제화를 위한 핵심 기반을 제공합니다. 번역, 날짜/숫자 포맷팅, 국제화 라우팅 같은 요소를 처리합니다.

하지만 글로벌 사용자를 위한 제품 구축은 더 폭넓은 주제를 포함합니다:

  * 앱에 맞는 **아키텍처와 라우팅 전략** 선택
  * **백엔드 서비스 또는 CMS**와의 통합
  * 콘텐츠 현지화를 위한 **생성형 AI** 활용
  * TypeScript와 IDE 도구로 **개발 워크플로우** 간소화
  * **번역 관리 시스템**을 활용한 팀 협업
  * **진정으로 현지화된 경험**에 기여하는 모든 요소 이해
  * 글로벌 사용자 도달을 위한 다국어 앱의 **SEO 최적화 마스터하기**

[![동영상 미리보기](https://next-intl.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fthumb.06bfa870.jpg&w=384&q=75)](https://learn.next-intl.dev)

### 자신 있게 국제화된 Next.js 앱 구축하기

기초부터 고급 패턴까지, 실제 프로젝트를 통해 Next.js로 매력적인 다국어 앱을 만드는 방법을 배워보세요.

[Get started→](https://learn.next-intl.dev)

