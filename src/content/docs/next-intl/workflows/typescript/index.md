---
title: 'TypeScript 보강'
description: '은 별도의 추가 설정 없이 기본적으로 TypeScript와 매끄럽게 통합됩니다.'
---

원문 URL: https://next-intl.dev/docs/workflows/typescript

[문서](https://next-intl.dev/docs/getting-started "문서")[워크플로우 및 통합](https://next-intl.dev/docs/workflows "워크플로우 및 통합")TypeScript 보강

# TypeScript 보강

동영상으로 보고 싶으신가요?

[에디터 도구](https://learn.next-intl.dev/chapters/03-translations/05-tooling)

`next-intl`은 별도의 추가 설정 없이 기본적으로 TypeScript와 매끄럽게 통합됩니다.

하지만 선택적으로 보조 정의를 제공해 `next-intl`이 사용하는 타입을 보강할 수 있으며, 이를 통해 앱 전반에서 자동 완성과 타입 안정성을 향상시킬 수 있습니다.

global.ts
```
    import {routing} from '@/i18n/routing';
    import {formats} from '@/i18n/request';
    import messages from './messages/en.json';

    declare module 'next-intl' {
      interface AppConfig {
        Locale: (typeof routing.locales)[number];
        Messages: typeof messages;
        Formats: typeof formats;
      }
    }
```

타입 보강은 다음 항목에 사용할 수 있습니다:

  * [`Locale`](https://next-intl.dev/docs/workflows/typescript#locale)
  * [`Messages`](https://next-intl.dev/docs/workflows/typescript#messages)
  * [`Formats`](https://next-intl.dev/docs/workflows/typescript#formats)

## `Locale`[](https://next-intl.dev/docs/workflows/typescript#locale)

`Locale` 타입을 보강하면 locale을 반환하거나 받는 `next-intl`의 모든 API에 영향을 줍니다:
```
    import {useLocale} from 'next-intl';

    // ✅ 'en' | 'de'
    const locale = useLocale();
```
```
    import {Link} from '@/i18n/routing';

    // ✅ Passes the validation
```

