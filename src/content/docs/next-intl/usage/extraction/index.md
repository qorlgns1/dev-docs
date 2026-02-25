---
title: 'useExtracted (실험적)'
description: '네임스페이스와 키를 수동으로 관리하는 대신, 은 와 유사하게 동작하지만 소스 파일에서 메시지를 자동으로 추출하는 추가 API를 제공합니다.'
---

Source URL: https://next-intl.dev/docs/usage/extraction

# `useExtracted` (실험적)

네임스페이스와 키를 수동으로 관리하는 대신, `next-intl`은 [`useTranslations`](https://next-intl.dev/docs/usage/translations)와 유사하게 동작하지만 소스 파일에서 메시지를 자동으로 추출하는 추가 API를 제공합니다.
```
    import {useExtracted} from 'next-intl';

    function InlineMessages() {
      const t = useExtracted();
      return <h1>{t('Look ma, no keys!')}</h1>;
    }
```

추출은 Turbo 또는 Webpack 로더를 통해 `next dev`와 `next build`에 자동으로 통합되므로, 수동으로 실행할 필요가 없습니다.

위 파일이 컴파일되면 다음이 수행됩니다:

  1. 자동으로 할당된 키와 함께 인라인 메시지를 소스 로케일로 추출합니다:

messages/en.json
```
    {
      "VgH3tb": "Look ma, no keys!"
    }
```

  2. 빈 항목을 추가하거나 오래된 항목을 제거하여 대상 로케일을 동기화 상태로 유지합니다:

messages/de.json
```
    {
      "VgH3tb": ""
    }
```

  3. `useExtracted`를 `useTranslations`로 대체하도록 파일을 컴파일합니다

```
    import {useTranslations} from 'next-intl';

    function InlineMessages() {
      const t = useTranslations();
      return <h1>{t('VgH3tb')}</h1>;
    }
```

**링크:**

  * [소개 블로그 게시물](https://next-intl.dev/blog/use-extracted)
  * [예제 앱](https://next-intl.dev/examples#app-router-extracted)

## 시작하기[](https://next-intl.dev/docs/usage/extraction#getting-started)

이 API는 현재 실험적이며, `next.config.ts`에서 활성화해야 합니다:

next.config.ts
```
    import {NextConfig} from 'next';
    import createNextIntlPlugin from 'next-intl/plugin';

    const withNextIntl = createNextIntlPlugin({
      experimental: {
        // Relative path(s) to source files
        srcPath: './src',

        extract: {
          // Defines which locale to extract to
          sourceLocale: 'en'
        },

        messages: {
          // Relative path to the directory
          path: './messages',

          // Either 'json', 'po', or a custom format (see below)
          format: 'json',

          // Either 'infer' to automatically detect locales based on
          // matching files in `path` or an explicit array of locales
          locales: 'infer'
        }
      }
    });

    const config: NextConfig = {};
    export default withNextIntl(config);
```

이렇게 하면 `next dev` 또는 `next build`를 실행할 때마다, 발견된 메시지가 추출되고 메시지가 동기화 상태로 유지됩니다.

자세한 내용은 [`createNextIntlPlugin`](https://next-intl.dev/docs/usage/plugin#extract)을 참고하세요.

[](https://next-intl.dev/docs/usage/extraction#manual)메시지를 수동으로 추출할 수 있나요?

메시지 추출은 `next dev`와 `next build` 실행을 기반으로 개발 워크플로에 자연스럽게 통합되도록 설계되었지만, 메시지를 수동으로 추출할 수도 있습니다:
```
    import {unstable_extractMessages} from 'next-intl/extractor';

    await unstable_extractMessages({
      srcPath: './src',
      sourceLocale: 'en',
      messages: {
        path: './messages',
        format: 'json',
        locales: 'infer'
      }
    });

    console.log('✔ Messages extracted');
```

이는 Next.js 개발 서버를 실행하지 않는 컴포넌트 라이브러리 같은 패키지를 개발하면서, 패키지와 함께 메시지를 제공하려는 경우에 유용할 수 있습니다.

## 인라인 메시지[](https://next-intl.dev/docs/usage/extraction#inline-messages)

### ICU 메시지[](https://next-intl.dev/docs/usage/extraction#icu-messages)

`useTranslations`에서 익숙한 모든 [ICU 기능](https://next-intl.dev/docs/usage/translations#icu-messages)을 지원하며, 평소처럼 사용할 수 있습니다:
```
    // Interpolation of arguments
    t('Hello {name}!', {name: 'Jane'});
```
```
    // Cardinal pluralization
    t(
      'You have {count, plural, =0 {no followers yet} =1 {one follower} other {# followers}}.',
      {count: 3580}
    );
```
```
    // Ordinal pluralization
    t(
      "It's your {year, selectordinal, one {#st} two {#nd} few {#rd} other {#th}} birthday!",
      {year: 22}
    );
```
```
    // Select values
    t('{gender, select, female {She is} male {He is} other {They are}} online.', {
      gender: 'female'
    });
```
```
    // Rich text
    t.rich('Please refer to the <link>guidelines</link>.', {
      link: (chunks) => <Link href="/guidelines">{chunks}</Link>
    });
```

예외는 `t.raw` 하나이며, 이 기능은 메시지 추출과 함께 사용하도록 의도되지 않았습니다.

### 설명[](https://next-intl.dev/docs/usage/extraction#descriptions)

(AI) 번역가에게 메시지에 대한 더 많은 맥락을 제공하려면 설명을 추가할 수 있습니다:
```
    <button onClick={onSlideRight}>
      {t({
        message: 'Right',
        description: 'Advance to the next slide'
      })}
    </button>
```

### 명시적 ID[](https://next-intl.dev/docs/usage/extraction#explicit-ids)

자동 생성된 ID 대신 명시적 ID를 사용하려면 선택적으로 지정할 수 있습니다:
```
    <button onClick={onSlideRight}>
      {t({
        id: 'carousel.next',
        message: 'Right'
      })}
    </button>
```

이는 여러 곳에서 사용되는 레이블이 다른 언어에서는 서로 다른 번역을 가져야 할 때 유용할 수 있습니다. 이는 드물게만 필요해야 하는 탈출구입니다.

### 네임스페이스[](https://next-intl.dev/docs/usage/extraction#namespaces)

메시지를 특정 네임스페이스 아래로 구성하려면 이를 `useExtracted`에 전달할 수 있습니다:
```
    function Modal() {
      const t = useExtracted('design-system');
      return (
        <>
          <button>{t('Close')}</button>
          ...
        </>
      );
    }
```

이렇게 하면 `t` 호출과 연관된 메시지가 지정한 네임스페이스로 추출됩니다:
```
    {
      "design-system": {
        "5VpL9Z": "Close"
      }
    }
```

네임스페이스는 다음과 같은 상황에서 유용합니다:

  1. **라이브러리:** 모노레포에 여러 패키지가 있는 경우, 서로 다른 패키지의 메시지를 단일 카탈로그로 병합하고 패키지 간 키 충돌을 방지할 수 있습니다.
  2. **분할:** 특정 메시지만 클라이언트 측에 전달하려는 경우, 이에 맞게 그룹화하는 데 도움이 됩니다(예: `<NextIntlClientProvider messages={messages.client}>`).

네임스페이스를 과도하게 사용하지 않는 것이 좋습니다. 네임스페이스 리팩터링이 수반될 때 컴포넌트 간 메시지 이동이 더 어려워질 수 있기 때문입니다.

### `await getExtracted()`[](https://next-intl.dev/docs/usage/extraction#get-extracted)

Server Components, Metadata, Server Actions 같은 비동기 함수에서 사용하려면 `next-intl/server`의 비동기 변형을 사용합니다:

page.tsx
```
    import {getExtracted} from 'next-intl/server';

    export default async function ProfilePage() {
      const user = await fetchUser();
      const t = await getExtracted();

      return (
      );
    }
```

### 선택적 컴파일[](https://next-intl.dev/docs/usage/extraction#optional-compilation)

메시지 추출은 주로 실행 중인 Next.js 앱과 함께 사용하도록 설계되었지만, `useExtracted`는 `useTranslations`로 컴파일되지 않아도 완전히 정상적으로 동작합니다. 이 경우 인라인 메시지는 번역 키로 대체되지 않고 직접 사용됩니다.

예를 들어 테스트에 유용할 수 있습니다:
```
    import {expect, it} from 'vitest';
    import {NextIntlClientProvider} from 'next-intl';
    import {renderToString} from 'react-dom/server';

    function Component() {
      const t = useExtracted();
      return t('Hello {name}!', {name: 'Jane'});
    }

    it('renders', () => {
      const html = renderToString(
        // No need to pass any messages
      );

      // ✅ The inline message will be used
      expect(html).toContain('Hello Jane!');
    });
```

## 형식[](https://next-intl.dev/docs/usage/extraction#formats)

메시지는 [`.json`](https://next-intl.dev/docs/usage/plugin#formats-json), [`.po`](https://next-intl.dev/docs/usage/plugin#formats-po), 또는 [사용자 정의 파일 형식](https://next-intl.dev/docs/usage/plugin#formats-custom)으로 추출할 수 있습니다. 구성 세부사항은 [`messages.format`](https://next-intl.dev/docs/usage/plugin#format)을 참고하세요.

**권장 사항:** `useExtracted`에서는 키가 자동 생성되므로, 파일 참조와 설명처럼 메시지에 대한 더 많은 맥락을 제공할 수 있는 **PO 파일** 사용을 권장합니다. 이는 (AI) 번역가에게 도움이 될 수 있습니다.

💡

[Crowdin](https://next-intl.dev/docs/workflows/localization-management) 같은 번역 관리 시스템을 사용하면 AI 기반 번역을 자동화할 수 있습니다.

