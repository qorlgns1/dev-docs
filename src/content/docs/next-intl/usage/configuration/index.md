---
title: '요청 구성'
description: '원본 URL: https://next-intl.dev/docs/usage/configuration'
---

원본 URL: https://next-intl.dev/docs/usage/configuration

[문서](https://next-intl.dev/docs/getting-started "Docs")[사용 가이드](https://next-intl.dev/docs/usage "Usage guide")요청 구성

# 요청 구성

Next.js 앱 전반에서 사용하는 구성 속성은 요청별로 설정할 수 있습니다.

## 서버 및 클라이언트 컴포넌트[](https://next-intl.dev/docs/usage/configuration#server-client-components)

국제화를 [Server Components 또는 Client Components](https://next-intl.dev/docs/environments/server-client-components) 중 어디에서 처리하는지에 따라, 각각 `i18n/request.ts` 또는 `NextIntlClientProvider`의 구성이 적용됩니다.

### `i18n/request.ts` & `getRequestConfig`[](https://next-intl.dev/docs/usage/configuration#i18n-request)

`i18n/request.ts`는 **서버 전용** 코드(예: Server Components, Server Actions 등)에 대한 구성을 제공하는 데 사용할 수 있습니다. 구성은 `getRequestConfig` 함수를 통해 제공되며, [locale 기반 라우팅](https://next-intl.dev/docs/routing)을 사용하는 경우 `requestLocale` 매개변수도 제공됩니다.

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';
    import {routing} from '@/i18n/routing';

    export default getRequestConfig(async ({requestLocale}) => {
      // ...

      return {
        locale,
        messages
        // ...
      };
    });
```

구성 객체는 내부적으로 React의 [`cache`](https://react.dev/reference/react/cache)를 사용해 요청마다 한 번 생성됩니다. 국제화를 처음 사용하는 컴포넌트가 `getRequestConfig`로 정의한 함수를 호출합니다.

이 함수는 Server Components 렌더 패스 중에 실행되므로, [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies), [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers) 같은 함수를 호출해 요청별 구성을 반환할 수 있습니다.

### `NextIntlClientProvider`[](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider)

`NextIntlClientProvider`는 **Client Components**에 대한 구성을 제공하는 데 사용할 수 있습니다.

layout.tsx
```
    import {NextIntlClientProvider} from 'next-intl';
    import {getMessages} from 'next-intl/server';

    export default async function RootLayout(/* ... */) {
      // ...

      return (
        <html lang={locale}>
          <body>
          </body>
        </html>
      );
    }
```

Server Component에서 `NextIntlClientProvider`를 렌더링하면 다음 props가 상속됩니다:

  1. `locale`
  2. `messages`
  3. `now`
  4. `timeZone`
  5. `formats`

이러한 props 중 일부를 상속하고 싶지 않다면(예: [Server & Client Components](https://next-intl.dev/docs/environments/server-client-components)에서 국제화 사용 방식을 선택적으로 구성하는 경우), opt-out할 수 있습니다:

layout.tsx
```
      ...
```

또한 중첩된 `NextIntlClientProvider` 인스턴스는 각자의 상위 인스턴스로부터 구성을 상속합니다. 다만 개별 props는 원자적으로 취급되므로, 필요하다면 예를 들어 `messages`는 수동으로 병합해야 합니다.

반대로 다음 props는 상속되지 않습니다:

  1. `onError`
  2. `getMessageFallback`

[](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider-non-serializable-props)`onError` 같은 직렬화 불가능한 props를 `NextIntlClientProvider`에 어떻게 제공하나요?

React는 Client Components로 전달할 수 있는 props 타입을 [직렬화 가능한](https://react.dev/reference/rsc/use-client#serializable-types) 타입으로 제한합니다. `onError`와 `getMessageFallback`은 함수를 받을 수 있으므로, 이 구성 옵션들은 클라이언트 측에 자동으로 상속될 수 없습니다.

클라이언트 측에서 이 값을 정의하려면, 해당 props를 정의하는 provider를 추가할 수 있습니다:

IntlErrorHandlingProvider.tsx
```
    'use client';

    import {NextIntlClientProvider} from 'next-intl';

    export default function IntlErrorHandlingProvider({children}) {
      return (
          {children}
      );
    }
```

클라이언트 측 provider 컴포넌트를 정의한 후에는 Server Component에서 사용할 수 있습니다:

layout.tsx
```
    import {NextIntlClientProvider} from 'next-intl';
    import {getLocale} from 'next-intl/server';
    import IntlErrorHandlingProvider from './IntlErrorHandlingProvider';

    export default async function RootLayout({children}) {
      const locale = await getLocale();

      return (
        <html lang={locale}>
          <body>
          </body>
        </html>
      );
    }
```

이렇게 하면 provider 컴포넌트가 이미 클라이언트 번들에 포함되므로, 함수를 props로 정의하고 전달할 수 있습니다.

내부의 `NextIntlClientProvider`는 외부 구성에서 상속을 받고, `onError`와 `getMessageFallback` 함수만 추가된다는 점에 유의하세요.

## Locale[](https://next-intl.dev/docs/usage/configuration#locale)

`locale`은 사용자의 언어 및 형식 선호도를 담는 식별자이며, 선택적으로 지역 정보(예: `en-US`)를 포함할 수 있습니다. locale은 [IETF BCP 47 language tags](https://en.wikipedia.org/wiki/IETF_language_tag)로 지정됩니다.

i18n/request.tsProvider

[locale 기반 라우팅](https://next-intl.dev/docs/routing)을 사용하는지에 따라, `requestLocale` 매개변수에서 locale을 읽거나 직접 값을 제공할 수 있습니다:

**locale 기반 라우팅 사용 시:**

i18n/request.ts
```
    export default getRequestConfig(async ({requestLocale}) => {
      // Typically corresponds to the `[locale]` segment
      const requested = await requestLocale;
      const locale = hasLocale(routing.locales, requested)
        ? requested
        : routing.defaultLocale;

      return {
        locale
        // ...
      };
    });
```

**locale 기반 라우팅 미사용 시:**

i18n/request.ts
```
    export default getRequestConfig(async () => {
      // Provide a static locale, fetch a user setting,
      // read from `cookies()`, `headers()`, etc.
      const locale = 'en';

      return {
        locale
        // ...
      };
    });
```

[](https://next-intl.dev/docs/usage/configuration#server-request-locale)`requestLocale` 매개변수에는 어떤 값이 들어갈 수 있나요?

`requestLocale` 매개변수는 일반적으로 middleware가 매칭한 `[locale]` 세그먼트에 대응하지만, 다음 3가지 특수 케이스를 고려해야 합니다:

  1. **Overrides** : `getTranslations({locale: 'en'})` 같은 [awaitable functions](https://next-intl.dev/docs/environments/actions-metadata-route-handlers)에 명시적인 `locale`을 전달하면, 세그먼트 대신 이 값이 사용됩니다.
  2. **`undefined`** : `[locale]` 세그먼트 밖의 페이지가 렌더링될 때(예: `app/page.tsx`의 언어 선택 페이지) 값이 `undefined`일 수 있습니다.
  3. **Invalid values** : `[locale]` 세그먼트는 사실상 알 수 없는 라우트를 위한 캐치올처럼 동작하므로(예: `/unknown.txt`), 잘못된 값은 유효한 locale로 대체해야 합니다. 추가로 이 경우 렌더링을 중단하기 위해 [root layout](https://next-intl.dev/docs/routing/setup#layout)에서 `notFound()`를 호출할 수 있습니다.

```
```

[](https://next-intl.dev/docs/usage/configuration#locale-change)locale은 어떻게 변경하나요?

[locale 기반 라우팅](https://next-intl.dev/docs/routing)을 사용하는지에 따라 locale은 다음과 같이 변경할 수 있습니다:

  1. **locale 기반 라우팅 사용 시** : locale은 라우터가 관리하며, [`Link`](https://next-intl.dev/docs/routing/navigation#link) 또는 [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter) 같은 `next-intl`의 내비게이션 API로 변경할 수 있습니다.
  2. **locale 기반 라우팅 미사용 시** : locale을 읽는 값(예: cookie, 사용자 설정 등)을 업데이트하여 변경할 수 있습니다.

더 알아보기:

[로케일 스위처](https://learn.next-intl.dev/chapters/04-adding-locales/02-locale-switcher)

### `useLocale` & `getLocale`[](https://next-intl.dev/docs/usage/configuration#use-locale)

앱의 현재 locale은 `useTranslations`, `useFormatter` 같은 훅에 자동으로 반영되어 렌더링 결과에 영향을 줍니다.

앱의 다른 위치에서 이 값이 필요하다면(예: 로케일 스위처 구현, API 호출에 전달), `useLocale` 또는 `getLocale`로 읽을 수 있습니다:
```
    // Regular components
    import {useLocale} from 'next-intl';
    const locale = useLocale();

    // Async Server Components
    import {getLocale} from 'next-intl/server';
    const locale = await getLocale();
```

[](https://next-intl.dev/docs/usage/configuration#locale-return-value)`useLocale`은 어떤 값을 반환하나요?

컴포넌트가 렌더링되는 방식에 따라 반환되는 locale은 다음에 대응합니다:

  1. **Server Components** : [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#i18n-request)에서 반환된 값입니다.
  2. **Client Components** : [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider)에서 전달받은 값입니다.

`NextIntlClientProvider`가 Server Component에서 렌더링될 경우 locale을 자동 상속하므로, 직접 locale을 전달해야 하는 경우는 드뭅니다.

[](https://next-intl.dev/docs/usage/configuration#locale-pages-router)Pages Router를 사용 중인데, locale에 어떻게 접근하나요?

[Pages Router의 국제화 라우팅](https://nextjs.org/docs/pages/building-your-application/routing/internationalization)을 사용한다면, 라우터에서 locale을 받아 `NextIntlClientProvider`에 전달할 수 있습니다:

_app.tsx
```
    import {useRouter} from 'next/router';

    // ...

    const router = useRouter();

    return (
        ...
      </NextIntlClientProvider>;
    );
```

### `Locale` type[](https://next-intl.dev/docs/usage/configuration#locale-type)

`locale`을 다른 함수에 전달할 때는, 받는 매개변수에 `Locale` 타입을 사용할 수 있습니다:
```
    import {Locale} from 'next-intl';

    async function getPosts(locale: Locale) {
      // ...
    }
```

이는 백엔드 서비스나 CMS와 연동할 때 유용할 수 있습니다:

[백엔드 콘텐츠](https://learn.next-intl.dev/chapters/07-content/01-overview)

💡

기본적으로 `Locale`은 `string`으로 타입 지정됩니다. 하지만 [augmenting the `Locale` type](https://next-intl.dev/docs/workflows/typescript#locale)을 통해, 지원하는 locale을 기반으로 한 엄격한 유니온 타입을 선택적으로 제공할 수 있습니다.

## Messages[](https://next-intl.dev/docs/usage/configuration#messages)

국제화에서 가장 중요한 부분은 사용자 언어에 맞는 라벨을 제공하는 것입니다. 권장 워크플로는 코드와 함께 저장소에 메시지를 보관하는 방식입니다.
```
    ├── messages
    │   ├── en.json
    │   ├── de-AT.json
    │   └── ...
    ...
```

메시지를 앱 코드와 함께 배치하면 개발자가 빠르게 변경할 수 있고, 로컬 메시지의 구조를 [type checking](https://next-intl.dev/docs/workflows/typescript#messages)에 활용할 수 있어 유리합니다.

팀이 자주 배포한다면 번역 프로세스 자동화를 고려할 수 있습니다:

[Crowdin을 사용한 AI 번역](https://learn.next-intl.dev/chapters/10-continuous-localization/01-local-workflow)

즉, `next-intl`은 메시지 저장 방식에 구애받지 않으며, 앱 렌더링 중에 메시지를 가져오는 비동기 함수를 자유롭게 정의할 수 있습니다:

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      return {
        messages: (await import(`../../messages/${locale}.json`)).default
        // ...
      };
    });
```

메시지 구성을 마친 후에는 [`useTranslations`](https://next-intl.dev/docs/usage/translations#rendering-messages-with-usetranslations)로 사용할 수 있습니다.

`getRequestConfig`는 임의 코드를 실행할 수 있으므로, 다음도 가능합니다:

  * 여러 locale 간 메시지 공유
  * 다른 locale의 메시지를 fallback으로 병합
  * 원격 소스에서 메시지 로드

**더 알아보기:**

[ 메시지 제공하기](https://learn.next-intl.dev/chapters/04-adding-locales/01-messages)

[](https://next-intl.dev/docs/usage/configuration#messages-split-files)메시지를 여러 파일로 분리하려면 어떻게 하나요?

메시지는 자유롭게 정의하고 로드할 수 있으므로, 원한다면 여러 파일로 분리한 뒤 런타임에 병합할 수 있습니다:
```
    const messages = {
      ...(await import(`../../messages/${locale}/login.json`)).default,
      ...(await import(`../../messages/${locale}/dashboard.json`)).default
    };
```

`next-intl`의 [VSCode integration](https://next-intl.dev/docs/workflows/vscode-integration)은 하나의 큰 파일 내에서 메시지를 관리하는 데 도움이 됩니다. 단지 정리를 위해 분리하는 것이라면 이 방법을 고려해 보세요.

### `useMessages` & `getMessages`

컴포넌트에서 메시지 접근이 필요하다면, 구성에서 `useMessages()` 또는 `getMessages()`로 읽을 수 있습니다:
```
    // Regular components
    import {useMessages} from 'next-intl';
    const messages = useMessages();

    // Async Server Components
    import {getMessages} from 'next-intl/server';
    const messages = await getMessages();
```
```
    import {NextIntlClientProvider} from 'next-intl';
    import {getMessages} from 'next-intl/server';
    import pick from 'lodash/pick';

    async function Component({children}) {
      // Read messages configured via `i18n/request.ts`
      const messages = await getMessages();

      return (
          ...
      );
    }
```

## Time zone[](https://next-intl.dev/docs/usage/configuration#time-zone)

시간대를 지정하면 날짜와 시간의 렌더링에 영향을 줍니다. 기본적으로 서버 런타임의 시간대가 사용되지만, 필요에 따라 사용자 지정할 수 있습니다.

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      return {
        // The time zone can either be statically defined, read from the
        // user profile if you store such a setting, or based on dynamic
        // request information like the locale or a cookie.
        timeZone: 'Europe/Vienna'

        // ...
      };
    });
```
```
    // The time zone can either be statically defined, read from the
    // user profile if you store such a setting, or based on dynamic
    // request information like the locale or a cookie.
    const timeZone = 'Europe/Vienna';

```

사용 가능한 시간대 이름은 [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)에서 확인할 수 있습니다.

Client Components의 시간대는 Server Component에서 렌더링되는 `NextIntlClientProvider`로 관련 컴포넌트를 감싸면 서버 측 값이 자동으로 상속됩니다. 그 외의 경우에는 래핑하는 `NextIntlClientProvider`에서 값을 명시적으로 지정할 수 있습니다.

**더 알아보기:**

[날짜 및 시간대](https://learn.next-intl.dev/chapters/05-formatting/02-dates-timezones)

### `useTimeZone` & `getTimeZone`[](https://next-intl.dev/docs/usage/configuration#use-time-zone)

구성된 시간대는 컴포넌트에서 `useTimeZone` 또는 `getTimeZone`으로 읽을 수 있습니다:
```
    // Regular components
    import {useTimeZone} from 'next-intl';
    const timeZone = useTimeZone();

    // Async Server Components
    import {getTimeZone} from 'next-intl/server';
    const timeZone = await getTimeZone();
```

## Now 값[](https://next-intl.dev/docs/usage/configuration#now)

[상대 날짜 및 시간](https://next-intl.dev/docs/usage/dates-times#relative-times)을 포맷할 때, `next-intl`은 “now”라고 불리는 기준 시점을 기준으로 시간을 포맷합니다. 캐싱 측면에서 필요할 때 [이 값을 제공](https://next-intl.dev/docs/usage/dates-times#relative-times-usenow)하는 것이 유리할 수 있지만, 예를 들어 테스트 실행 시 일관성을 보장하기 위해 `now`의 전역 값을 제공할 수도 있습니다.

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';

    export default getRequestConfig(async () => {
      return {
        now: new Date('2024-11-14T10:36:01.516Z')

        // ...
      };
    });
```
```
    const now = new Date('2024-11-14T10:36:01.516Z');

      ...
```

`formats`를 설정했다면, `useFormatter`를 통해 컴포넌트에서 이를 사용할 수 있습니다:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();

      format.dateTime(new Date('2020-11-20T10:36:01.516Z'), 'short');
      format.number(47.414329182, 'precise');
      format.list(['HTML', 'CSS', 'JavaScript'], 'enumeration');
    }
```

💡

기본적으로 포맷 이름은 `string`으로 느슨하게 타입이 지정됩니다. 하지만 [ `Formats` 타입을 보강](https://next-intl.dev/docs/workflows/typescript#formats)하면 선택적으로 엄격한 타입을 사용할 수 있습니다.

숫자, 날짜, 시간에 대한 전역 포맷은 메시지에서도 참조할 수 있습니다:

en.json
```
    {
      "ordered": "You've ordered this product on {orderDate, date, short}",
      "latitude": "Latitude: {latitude, number, precise}"
    }
```
```
    import {useTranslations} from 'next-intl';

    function Component() {
      const t = useTranslations();

      t('ordered', {orderDate: new Date('2020-11-20T10:36:01.516Z')});
      t('latitude', {latitude: 47.414329182});
    }
```

Server Component에서 렌더링되는 `NextIntlClientProvider`로 관련 컴포넌트를 감싸면, 포맷은 서버 측에서 자동으로 상속됩니다.

## 오류 처리 (`onError` & `getMessageFallback`)[](https://next-intl.dev/docs/usage/configuration#error-handling)

기본적으로 메시지를 확인하지 못했거나 포맷팅에 실패하면 콘솔에 오류가 출력됩니다. 이 경우 앱이 계속 동작하도록 `${namespace}.${key}`가 대신 렌더링됩니다.

이 동작은 `onError` 및 `getMessageFallback` 설정 옵션으로 커스터마이즈할 수 있습니다.

i18n/request.tsProvider

i18n/request.ts
```
    import {getRequestConfig} from 'next-intl/server';
    import {IntlErrorCode} from 'next-intl';

    export default getRequestConfig(async () => {
      return {
        onError(error) {
          if (error.code === IntlErrorCode.MISSING_MESSAGE) {
            // Missing translations are expected and should only log an error
            console.error(error);
          } else {
            // Other errors indicate a bug in the app and should be reported
            reportToErrorTracking(error);
          }
        },

        getMessageFallback({namespace, key, error}) {
          const path = [namespace, key].filter((part) => part != null).join('.');

          if (error.code === IntlErrorCode.MISSING_MESSAGE) {
            return path + ' is not yet translated';
          } else {
            return 'Dear developer, please fix this message: ' + path;
          }
        }

        // ...
      };
    });
```

`onError`와 `getMessageFallback`은 Client Component에 자동으로 상속되지 않는다는 점에 유의하세요. 다만 이 기능을 Client Component에서도 사용할 수 있게 하려면, 이러한 props를 정의하는 [클라이언트 사이드 provider](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider-non-serializable-props)를 만들 수 있습니다.

[](https://next-intl.dev/docs/usage/configuration#error-handling-fallback)다른 로케일의 메시지를 fallback으로 사용하려면 어떻게 해야 하나요?

`getMessageFallback` 설정은 누락된 메시지를 오류로 처리하려는 앱에서 오류 케이스를 커스터마이즈하기 위한 용도입니다.

특정 로케일에서 메시지 누락이 예상된다면, [messages](https://next-intl.dev/docs/usage/configuration#messages)를 제공할 때 기본 로케일의 메시지를 현재 로케일 메시지와 병합하는 방법을 고려할 수 있습니다.

**더 알아보기:**

[ 메시지 제공하기](https://learn.next-intl.dev/chapters/04-adding-locales/01-messages)
```
    import {NextIntlClientProvider, IntlErrorCode} from 'next-intl';

    function onError(error) {
      if (error.code === IntlErrorCode.MISSING_MESSAGE) {
        // Missing translations are expected and should only log an error
        console.error(error);
      } else {
        // Other errors indicate a bug in the app and should be reported
        reportToErrorTracking(error);
      }
    }

    function getMessageFallback({namespace, key, error}) {
      const path = [namespace, key].filter((part) => part != null).join('.');

      if (error.code === IntlErrorCode.MISSING_MESSAGE) {
        return path + ' is not yet translated';
      } else {
        return 'Dear developer, please fix this message: ' + path;
      }
    }

      ...
    </NextIntlClientProvider>;
```

