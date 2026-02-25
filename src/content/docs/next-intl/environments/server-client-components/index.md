---
title: '서버 및 클라이언트 컴포넌트의 국제화'
description: '이는 국제화 처리에도 동일하게 적용됩니다.'
---

출처 URL: https://next-intl.dev/docs/environments/server-client-components

[문서](https://next-intl.dev/docs/getting-started "Docs")[환경](https://next-intl.dev/docs/environments "Environments")서버 및 클라이언트 컴포넌트

# 서버 및 클라이언트 컴포넌트의 국제화

[React Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)를 사용하면 `useState`, `useEffect` 같은 React의 상호작용 기능이 필요하지 않은 컴포넌트를 서버 전용으로 구현할 수 있습니다.

이는 국제화 처리에도 동일하게 적용됩니다.

page.tsx
```
    import {useTranslations} from 'next-intl';

    // Since this component doesn't use any interactive features
    // from React, it can be run as a Server Component.

    export default function HomePage() {
      const t = useTranslations('HomePage');
      return <h1>{t('title')}</h1>;
    }
```

국제화를 서버 측으로 옮기면 새로운 수준의 성능을 확보할 수 있고, 클라이언트 측은 상호작용 기능에 집중할 수 있습니다.

**서버 측 국제화의 이점:**

  1. 메시지가 서버를 벗어나지 않으며 클라이언트 측으로 전달할 필요가 없습니다
  2. 국제화를 위한 라이브러리 코드를 클라이언트 측에서 로드할 필요가 없습니다
  3. 예를 들어 라우트나 컴포넌트 기준으로 메시지를 분할할 필요가 없습니다
  4. 클라이언트 측 런타임 비용이 없습니다

## 서버 컴포넌트에서 국제화 사용하기[](https://next-intl.dev/docs/environments/server-client-components#using-internationalization-in-server-components)

서버 컴포넌트는 두 가지 방식으로 선언할 수 있습니다:

  1. 비동기 컴포넌트
  2. 비동기가 아닌 일반 컴포넌트

일반적인 앱에서는 두 유형의 컴포넌트를 모두 보게 될 가능성이 높습니다. `next-intl`은 각 컴포넌트 유형에 맞게 동작하는 API를 제공합니다.

### 비동기 컴포넌트[](https://next-intl.dev/docs/environments/server-client-components#async-components)

이 컴포넌트들은 주로 데이터 페칭을 담당하며 [hooks를 사용할 수 없습니다](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md#capabilities--constraints-of-server-and-client-components). 그래서 `next-intl`은 보통 컴포넌트 내부에서 hooks로 호출하던 함수들의 await 가능한 버전을 제공합니다.

page.tsx
```
    import {getTranslations} from 'next-intl/server';

    export default async function ProfilePage() {
      const user = await fetchUser();
      const t = await getTranslations('ProfilePage');

      return (
      );
    }
```

다음 함수들을 사용할 수 있습니다:

  * `getTranslations`
  * `getFormatter`
  * `getNow`
  * `getTimeZone`
  * `getMessages`
  * `getLocale`

### 비동기가 아닌 컴포넌트[](https://next-intl.dev/docs/environments/server-client-components#shared-components)

`async` 키워드로 선언되지 않았고 `useState` 같은 상호작용 기능을 사용하지 않는 컴포넌트는 [shared components](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md#sharing-code-between-server-and-client)라고 부릅니다. 이들은 어디에서 import되었는지에 따라 서버 컴포넌트 또는 클라이언트 컴포넌트로 렌더링될 수 있습니다.

Next.js에서는 서버 컴포넌트가 기본값이므로, shared components는 일반적으로 서버 컴포넌트로 실행됩니다:

UserDetails.tsx
```
    import {useTranslations} from 'next-intl';

    export default function UserDetails({user}) {
      const t = useTranslations('UserProfile');

      // This component will execute as a Server Component by default.
      // However, if it is imported from a Client Component, it will
      // execute as a Client Component.
      return (
          <h2>{t('title')}</h2>
          <p>{t('followers', {count: user.numFollowers})}</p>
      );
    }
```

shared component에서 `useTranslations`, `useFormatter`, `useLocale`, `useNow`, `useTimeZone`을 import하면, `next-intl`이 해당 컴포넌트가 실행되는 환경(서버 또는 클라이언트)에 가장 적합한 구현을 자동으로 제공합니다.

[](https://next-intl.dev/docs/environments/server-client-components#rsc-background)서버 컴포넌트 통합은 어떻게 동작하나요?

`next-intl`은 서버/클라이언트 컴포넌트 사용에 최적화된 코드를 로드하기 위해 [`react-server` conditional exports](https://github.com/reactjs/rfcs/blob/main/text/0227-server-module-conventions.md#react-server-conditional-exports)를 사용합니다. 클라이언트 측에서는 `useTranslations` 같은 hooks의 설정을 `useContext`로 읽고, 서버 측에서는 [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#i18n-request)를 통해 로드합니다.

현재 hooks는 보통 state를 가지거나 서버 환경에 맞지 않는 경우가 많아 주로 클라이언트 컴포넌트에서 쓰이는 것으로 알려져 있습니다. 하지만 [`useId`](https://react.dev/reference/react/useId) 같은 hooks는 서버 컴포넌트에서도 사용할 수 있습니다. 마찬가지로 `next-intl`은 서버/클라이언트 컴포넌트 여부와 관계없이 동일한 형태의 hooks 기반 API를 제공합니다.

이 패턴의 현재 제약은 `async` 컴포넌트에서 hooks를 호출할 수 없다는 점입니다. 따라서 `next-intl`은 이 사용 사례를 위해 별도의 [await 가능한 API](https://next-intl.dev/docs/environments/server-client-components#async-components)를 제공합니다.

[](https://next-intl.dev/docs/environments/server-client-components#async-or-non-async)컴포넌트에는 `async` 함수와 비동기가 아닌 함수 중 무엇을 사용해야 하나요?

shared component에 해당하는 컴포넌트를 구현하는 경우, 비동기가 아닌 함수로 구현하면 이점이 있을 수 있습니다. 이렇게 하면 해당 컴포넌트를 서버 또는 클라이언트 환경 모두에서 사용할 수 있어 유연성이 커집니다. 특정 컴포넌트를 클라이언트에서 실행할 계획이 전혀 없더라도, 이런 호환성은 예를 들어 테스트 단순화에 도움이 될 수 있습니다.

다만 국제화 처리를 위해 비동기가 아닌 함수만을 고집할 필요는 없습니다. 앱에 가장 잘 맞는 방식을 사용하세요.

성능 측면에서는 비동기 함수와 hooks를 서로 대체해 사용할 수 있습니다. [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#i18n-request)의 설정은 최초 사용 시 한 번만 로드되며, 두 구현 모두 관련 구간에서 내부적으로 요청 기반 캐싱을 사용합니다. 차이가 있다면, 비동기 함수는 호출 직후 렌더링을 재개할 수 있다는 작은 장점이 있습니다. 반면 hook 호출이 `i18n/request.ts`의 초기화를 유발하면 설정이 해석될 때까지 컴포넌트가 suspend되고 이후 다시 렌더링되며, hook 호출 이전의 컴포넌트 로직이 다시 실행될 수 있습니다. 하지만 한 요청 내에서 설정이 한 번 해석되고 나면 hooks는 suspend 없이 동기적으로 실행되므로, 마이크로태스크 큐가 비워질 때까지 기다릴 필요가 있는 비동기 함수보다 오버헤드가 더 적을 수 있습니다(관련 React RFC의 [resuming a suspended component by replaying its execution](https://github.com/acdlite/rfcs/blob/first-class-promises/text/0000-first-class-support-for-promises.md#resuming-a-suspended-component-by-replaying-its-execution) 참고).

## 클라이언트 컴포넌트에서 국제화 사용하기[](https://next-intl.dev/docs/environments/server-client-components#using-internationalization-in-client-components)

상황에 따라 클라이언트 컴포넌트에서 국제화를 처리해야 할 수 있습니다. 시작하기 가장 쉬운 방법은 모든 메시지를 클라이언트 측에 제공하는 것이며, 그래서 `next-intl`은 [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider)를 렌더링할 때 이를 자동으로 수행합니다. 많은 앱에서 이는 합리적인 접근입니다.

하지만 앱 성능 최적화에 관심이 있다면, 클라이언트 측으로 전달할 메시지를 더 선택적으로 고를 수 있습니다:

layout.tsx
```
      ...
```

앱의 특정 부분에서 `messages`를 클라이언트에 전달하고 싶다면, 그 부분에 `NextIntlClientProvider` 인스턴스를 하나 더 추가할 수도 있습니다.

클라이언트 컴포넌트에서 `next-intl` 번역을 사용하는 방법에는 여러 가지가 있으며, 여기서는 성능에 가장 유리한 순서로 나열합니다:

### 옵션 1: 번역된 라벨을 클라이언트 컴포넌트에 전달하기[](https://next-intl.dev/docs/environments/server-client-components#option-1-passing-translated-labels-to-client-components)

권장되는 방식은 처리된 라벨을 서버 컴포넌트에서 props 또는 `children`으로 전달하는 것입니다.

FAQEntry.tsx
```
    import {useTranslations} from 'next-intl';
    import Expandable from './Expandable'; // A Client Component
    import FAQContent from './FAQContent';

    export default function FAQEntry() {
      // Call `useTranslations` in a Server Component ...
      const t = useTranslations('FAQEntry');

      // ... and pass translated content to a Client Component
      return (
      );
    }
```

Expandable.tsx
```
    'use client';

    import {useState} from 'react';

    function Expandable({title, children}) {
      const [expanded, setExpanded] = useState(false);

      function onToggle() {
        setExpanded(!expanded);
      }

      return (
          <button onClick={onToggle}>{title}</button>
          {expanded && <div>{children}</div>}
      );
    }
```

이렇게 하면 번역은 서버 측에서만 실행되더라도, 번역된 콘텐츠에 대해 `useState` 같은 React 상호작용 기능을 사용할 수 있습니다.

Next.js 문서에서 자세히 보기: [Passing Server Components to Client Components as Props](https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns#supported-pattern-passing-server-components-to-client-components-as-props)

[](https://next-intl.dev/docs/environments/server-client-components#example-locale-switcher)예시: 로케일 스위처는 어떻게 구현할 수 있나요?

로케일 스위처를 상호작용 가능한 select로 구현하는 경우, 라벨은 서버 컴포넌트에서 렌더링하고 `select` 요소만 클라이언트 컴포넌트로 표시하여 국제화를 서버 측에 유지할 수 있습니다.

LocaleSwitcher.tsx
```
    import {useLocale, useTranslations} from 'next-intl';
    import {locales} from '@/config';

    // A Client Component that registers an event listener for
    // the `change` event of the select, uses `useRouter`
    // to change the locale and uses `useTransition` to display
    // a loading state during the transition.
    import LocaleSwitcherSelect from './LocaleSwitcherSelect';

    export default function LocaleSwitcher() {
      const t = useTranslations('LocaleSwitcher');
      const locale = useLocale();

      return (
          {locales.map((cur) => (
            <option key={cur} value={cur}>
              {t('locale', {locale: cur})}
            </option>
          ))}
      );
    }
```

[예제 구현](https://github.com/amannn/next-intl/blob/main/examples/example-app-router/src/components/LocaleSwitcher.tsx) ([demo](https://next-intl-example-app-router.vercel.app/en))

참고: [`useRouter`](https://next-intl.dev/docs/routing/navigation#userouter)

[](https://next-intl.dev/docs/environments/server-client-components#example-form)예시: 폼은 어떻게 구현할 수 있나요?

폼은 로딩 인디케이터와 유효성 검사 오류를 표시하기 위해 클라이언트 측 상태가 필요합니다.

국제화를 서버 측에 유지하려면, 폼 전체에 `'use client';`를 지정하는 대신 상호작용이 필요한 부분만 리프 컴포넌트로 분리하는 구조가 도움이 됩니다.

**예시:**

app/register/page.tsx
```
    import {useTranslations} from 'next-intl';

    // A Client Component, so that `useActionState` can be used
    // to potentially display errors received after submission.
    import RegisterForm from './RegisterForm';

    // A Client Component, so that `useFormStatus` can be used
    // to disable the input field during submission.
    import FormField from './FormField';

    // A Client Component, so that `useFormStatus` can be used
    // to disable the submit button during submission.
    import FormSubmitButton from './FormSubmitButton';

    export default function RegisterPage() {
      const t = useTranslations('RegisterPage');

      function registerAction() {
        'use server';
        // ...
      }

      return (
      );
    }
```

### 옵션 2: 상태를 서버 측으로 이동하기[](https://next-intl.dev/docs/environments/server-client-components#option-2-moving-state-to-the-server-side)

페이지네이션처럼 번역된 메시지에 반영되어야 하는 동적 상태를 다뤄야 하는 경우가 있을 수 있습니다.

Pagination.tsx
```
    function Pagination({curPage, totalPages}) {
      const t = useTranslations('Pagination');
      return <p>{t('info', {curPage, totalPages})}</p>;
    }
```

다음 방법을 사용하면 번역을 여전히 서버 측에서 관리할 수 있습니다:

  1. 페이지 또는 검색 파라미터
  2. 쿠키
  3. 데이터베이스 상태

특히 페이지 및 검색 파라미터는 URL 공유 시 앱 상태를 보존할 수 있고 브라우저 히스토리와도 통합되므로, 자주 매우 좋은 선택지입니다.

💡

Smashing Magazine에는 [서버 컴포넌트에서 `next-intl` 사용하기](https://www.smashingmagazine.com/2023/03/internationalization-nextjs-13-react-server-components)에 관한 글이 있으며, 실제 사례를 통해 검색 파라미터 활용을 다룹니다(특히 [상호작용 추가하기](https://www.smashingmagazine.com/2023/03/internationalization-nextjs-13-react-server-components/#adding-interactivity-dynamic-ordering-of-photos) 섹션).

### 옵션 3: 개별 메시지 제공하기[](https://next-intl.dev/docs/environments/server-client-components#option-3-providing-individual-messages)

서버 측으로 옮길 수 없는 컴포넌트에 동적 상태를 반영해야 한다면, 해당 컴포넌트를 `NextIntlClientProvider`로 감싸고 관련 메시지를 제공할 수 있습니다.

Counter.tsx
```
    import pick from 'lodash/pick';
    import {NextIntlClientProvider, useMessages} from 'next-intl';
    import ClientCounter from './ClientCounter';

    export default function Counter() {
      // Receive messages provided in `i18n/request.ts` …
      const messages = useMessages();

      return (
      );
    }
```

[](https://next-intl.dev/docs/environments/server-client-components#messages-client-namespaces)클라이언트 측에 어떤 메시지를 제공해야 하는지 어떻게 알 수 있나요?

현재는 클라이언트 측으로 전달할 메시지를, 감싼 컴포넌트의 구현에 대한 지식을 바탕으로 선택해야 합니다.

컴파일러 기반의 자동 접근 방식은 [`next-intl#1`](https://github.com/amannn/next-intl/issues/1)에서 검토 중입니다.

### 옵션 4: 모든 메시지 제공하기[](https://next-intl.dev/docs/environments/server-client-components#option-4-providing-all-messages)

대부분의 컴포넌트가 React의 상호작용 기능을 사용하는 매우 동적인 앱을 만든다면, 모든 메시지를 클라이언트 컴포넌트에서 사용할 수 있게 하는 편을 선호할 수 있습니다. 이것이 `next-intl`의 기본 동작입니다.

layout.tsx
```
    import {NextIntlClientProvider} from 'next-intl';

    export default async function RootLayout(/* ... */) {
      return (
        <html lang={locale}>
          <body>
          </body>
        </html>
      );
    }
```

[](https://next-intl.dev/docs/environments/server-client-components#client-messages-performance)클라이언트 측에서 메시지를 로드하는 것은 성능과 어떤 관련이 있나요?

앱 요구사항에 따라, 앱이 성능 목표를 충족하는지 확인하기 위해 [Core Web Vitals](https://web.dev/articles/vitals)를 모니터링하는 것이 좋습니다.

메시지를 `NextIntlClientProvider`에 전달하면, Next.js는 스트리밍 렌더링 중 해당 메시지를 페이지 마크업에 출력하여 Client Components에서 사용할 수 있게 합니다. 이는 [total blocking time](https://web.dev/articles/tbt)에 영향을 줄 수 있고, 나아가 [interaction to next paint](https://web.dev/articles/inp) 지표와도 관련될 수 있습니다. 앱에서 이러한 지표를 개선하려면 클라이언트 측으로 전달하는 메시지를 더 선별적으로 선택할 수 있습니다.

하지만 최적화의 일반적인 원칙은 다음과 같습니다: 최적화하기 전에 항상 먼저 측정하세요. 앱이 이미 잘 동작하고 있다면 최적화는 필요하지 않습니다.

현재 클라이언트 측에서 메시지 사용 성능을 최대화하기 위한 두 가지 연구 영역이 있습니다:

  1. [메시지의 자동 트리 셰이킹](https://github.com/amannn/next-intl/issues/1)
  2. [메시지의 사전 컴파일](https://github.com/amannn/next-intl/issues/962)

이들의 목표는 `next-intl`에서 이미 사용 중인 패턴을 최적화하여, 코드 변경 없이도 앱에서 최고 수준의 성능을 낼 수 있도록 하는 것입니다.

## 문제 해결[](https://next-intl.dev/docs/environments/server-client-components#troubleshooting)

### ”`NextIntlClientProvider`의 context를 찾을 수 없어 `useTranslations`를 호출하지 못했습니다.”[](https://next-intl.dev/docs/environments/server-client-components#missing-context)

앱을 개발하는 동안 이 오류 또는 `useFormatter`를 참조하는 유사한 오류를 만날 수 있습니다.

이런 일이 발생하는 이유는 다음과 같습니다:

  1. 의도적으로 Client Component에서 훅을 호출했지만, 컴포넌트 트리의 상위에 `NextIntlClientProvider`가 없는 경우입니다. 이 경우 오류를 해결하려면 [컴포넌트를 `NextIntlClientProvider`로 감싸면 됩니다](https://next-intl.dev/docs/environments/server-client-components#option-3-providing-individual-messages).
  2. 훅을 호출하는 컴포넌트가 의도치 않게 클라이언트 측 모듈 그래프에 포함되었고, 원래는 Server Component로 렌더링되기를 기대한 경우입니다. 이 경우 대신 해당 컴포넌트를 Client Component에 [`children`으로 전달](https://next-intl.dev/docs/environments/server-client-components#option-1-passing-translations-to-client-components)해 보세요.

### ”직렬화할 수 없기 때문에 함수를 Client Components에 직접 전달할 수 없습니다.”[](https://next-intl.dev/docs/environments/server-client-components#non-serializable-props)

`NextIntlClientProvider`에 직렬화할 수 없는 prop을 전달하려고 할 때 이 오류를 만날 수 있습니다.

이 컴포넌트는 다음과 같은 직렬화 불가능한 props를 받습니다:

  1. [`onError`](https://next-intl.dev/docs/usage/configuration#error-handling)
  2. [`getMessageFallback`](https://next-intl.dev/docs/usage/configuration#error-handling)

이들을 설정하려면, `NextIntlClientProvider`를 `'use client'`로 표시된 다른 컴포넌트로 감싸고 해당 props를 그 컴포넌트에서 정의하면 됩니다.

참고: [`onError` 같은 직렬화 불가능한 props를 `NextIntlClientProvider`에 어떻게 제공할 수 있나요?](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider-non-serializable-props)

