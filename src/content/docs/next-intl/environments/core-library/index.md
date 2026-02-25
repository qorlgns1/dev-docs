---
title: '코어 라이브러리'
description: '은 주로 Next.js 앱에서 사용하도록 설계되었지만, 코어는 프레임워크 비종속적이며 독립적으로 사용할 수 있습니다. 즉, React 앱이나 다른 모든 JavaScript 환경에서도 사용할 수 있습니다.'
---

출처 URL: https://next-intl.dev/docs/environments/core-library

[문서](https://next-intl.dev/docs/getting-started "Docs")[환경](https://next-intl.dev/docs/environments "Environments")코어 라이브러리

# 코어 라이브러리

`next-intl`은 주로 Next.js 앱에서 사용하도록 설계되었지만, 코어는 프레임워크 비종속적이며 독립적으로 사용할 수 있습니다. 즉, React 앱이나 다른 모든 JavaScript 환경에서도 사용할 수 있습니다.

## React 앱[](https://next-intl.dev/docs/environments/core-library#react-apps)

`next-intl`은 내부적으로 [`use-intl`](https://www.npmjs.com/package/use-intl)이라는 라이브러리를 사용합니다. 이 코어 라이브러리에는 `next-intl`에서 익숙한 대부분의 기능이 포함되어 있지만, 아래의 Next.js 전용 기능은 없습니다:

  1. [라우팅 API](https://next-intl.dev/docs/routing)
  2. Server Actions, Metadata, Route Handlers를 위한 [await 가능한 API](https://next-intl.dev/docs/environments/actions-metadata-route-handlers)
  3. `i18n/request.ts`와 함께 제공되는 [Server Components 통합](https://next-intl.dev/docs/environments/server-client-components)

만약 Next.js 외부의 React 앱에서도 Server Components가 정착된다면, 향후 Server Components 지원이 코어 라이브러리로 이동할 수 있습니다.

반대로 `use-intl`에는 일반적인 React 앱에서 i18n을 처리하는 데 필요한 모든 API가 포함되어 있습니다:

  * 메시지 번역을 위한 [`useTranslations`](https://next-intl.dev/docs/usage/translations)
  * [숫자](https://next-intl.dev/docs/usage/numbers), [날짜 및 시간](https://next-intl.dev/docs/usage/dates-times), [리스트](https://next-intl.dev/docs/usage/lists) 포매팅을 위한 `useFormatter`
  * [설정 API](https://next-intl.dev/docs/usage/configuration) (`use-intl`에서는 `NextIntlProvider`가 `IntlProvider`라는 점에 유의)

이를 통해 다른 환경에서도 `next-intl`에서 익숙한 동일한 API를 사용할 수 있습니다:

  1. React 앱([예시](https://next-intl.dev/examples#use-intl))
  2. React Native
  3. Jest 같은 테스트 환경([예시](https://github.com/amannn/next-intl/blob/main/examples/example-app-router/src/components/Navigation.spec.tsx))
  4. [Storybook](https://next-intl.dev/docs/workflows/storybook)

**기본 사용법:**
```
    import {IntlProvider, useTranslations} from 'use-intl';

    // You can get the messages from anywhere you like. You can also
    // fetch them from within a component and then render the provider
    // along with your app once you have the messages.
    const messages = {
      App: {
        hello: 'Hello {username}!'
      }
    };

    function Root() {
      return (
      );
    }

    function App({user}) {
      const t = useTranslations('App');
      return <h1>{t('hello', {username: user.name})}</h1>;
    }
```

[](https://next-intl.dev/docs/environments/core-library#shared-components)Next.js와 일반 React 앱 모두에서 동작하는 공유 컴포넌트를 만들 수 있나요?

네, 어느 환경에서든 렌더링되는 공유 컴포넌트를 지원합니다.

이 경우, 해당 컴포넌트에서는 `next-intl`에서 import하는 것이 유리할 수 있습니다. Next.js에서 렌더링할 때 [Server Components 통합](https://next-intl.dev/docs/environments/server-client-components)의 이점을 얻을 수 있기 때문입니다. 다른 환경에서도 `next-intl`로의 import는 정상 동작하지만, `IntlProvider`가 존재해야 합니다.

## 비React 앱[](https://next-intl.dev/docs/environments/core-library#non-react-apps)

React 전용 API 외에도 `use-intl`은 모든 JavaScript 환경에서 사용할 수 있는 두 가지 저수준 함수를 내보냅니다:

  1. 메시지 번역을 위한 `createTranslator`
  2. 숫자, 날짜 및 시간, 리스트 포매팅을 위한 `createFormatter`

이 API들은 필요한 모든 설정을 직접 전달받으며 전역 설정에 의존하지 않습니다.

다음과 같이 이 API들을 사용할 수 있습니다:
```
    import {createTranslator, createFormatter} from 'use-intl/core';

    const messages = {
      basic: 'Hello {name}!',
      rich: 'Hello <b>{name}</b>!'
    };

    // This creates the same function that is returned by `useTranslations`.
    // Since there's no provider, you can pass all the properties you'd
    // usually pass to the provider directly here.
    const t = createTranslator({locale: 'en', messages});

    // Result: "Hello world!"
    t('basic', {name: 'world'});

    // To generate HTML markup, you can consider using the `markup`
    // function which in contrast to `t.rich` returns a markup string.
    t.markup('rich', {
      name: 'world',
      b: (chunks) => `<b>${chunks}</b>`
    });

    // Creates the same object that is returned by `useFormatter`.
    const format = createFormatter({locale: 'en'});

    // Result: "Oct 17, 2022"
    format.dateTime(new Date(2022, 9, 17), {dateStyle: 'medium'});
```

