---
title: 'Next.js Pages Router 국제화(i18n)'
description: "import {NextIntlClientProvider} from 'next-intl';"
---

Source URL: https://next-intl.dev/docs/getting-started/pages-router

문서[시작하기](https://next-intl.dev/docs/getting-started "Getting started")Pages Router

# Next.js Pages Router 국제화(i18n)

[`next-intl`을 App Router와 함께 사용하는 것](https://next-intl.dev/docs/getting-started/app-router)이 권장되지만, Pages Router도 여전히 완전히 지원됩니다.

여러 언어단일 언어

  1. `npm install next-intl`
  2. [국제화 라우팅](https://nextjs.org/docs/advanced-features/i18n-routing) 설정
  3. `_app.tsx`에 provider 추가

_app.tsx
```
    import {NextIntlClientProvider} from 'next-intl';
    import {useRouter} from 'next/router';

    export default function App({Component, pageProps}) {
      const router = useRouter();

      return (
      );
    }
```

  4. 페이지 단위로 messages 제공

pages/index.tsx
```
    export async function getStaticProps(context) {
      return {
        props: {
          // You can get the messages from anywhere you like. The recommended
          // pattern is to put them in JSON files separated by locale and read
          // the desired one based on the `locale` received from Next.js.
          messages: (await import(`../../messages/${context.locale}.json`)).default
        }
      };
    }
```

  5. 컴포넌트에서 번역 사용!

단일 언어만 지원하더라도, `next-intl`은 레이블과 포맷팅 관련 관심사를 애플리케이션 로직과 분리하는 데 여전히 유용합니다.

  1. `npm install next-intl`

  2. `_app.tsx`에 provider 추가

_app.tsx
```
    import {NextIntlClientProvider} from 'next-intl';

    export default function App({Component, pageProps}) {
      return (
      );
    }
```

  3. 페이지 단위로 messages 제공

pages/index.tsx
```
    export async function getStaticProps() {
      const locale = 'en';

      return {
        props: {
          // You can get the messages from anywhere you like. The recommended pattern
          // is to put them in JSON files separated by locale (e.g. `en.json`).
          messages: (await import(`../../messages/${locale}.json`)).default
        }
      };
    }
```

  4. 컴포넌트에서 번역 사용!

💡

**다음 단계:**

  * `next-intl`을 살펴보고 있나요? [사용 가이드](https://next-intl.dev/docs/usage)를 확인해 보세요.
  * 문제가 발생했나요? 동작하는 앱을 확인하려면 [Pages Router 예제](https://next-intl.dev/examples#pages-router)를 살펴보세요.

  * Pages Router에서 App Router로 전환 중인가요? [마이그레이션 예제](https://next-intl.dev/examples#app-router-migration)를 확인해 보세요.

