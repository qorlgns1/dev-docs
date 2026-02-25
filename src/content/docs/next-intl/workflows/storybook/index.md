---
title: 'next-intl을 위한 Storybook 통합'
description: '용 Storybook을 설정하려면, 스토리를 적절히 감싸도록 를 렌더링하는 전역 데코레이터를 구성할 수 있습니다:'
---

Source URL: https://next-intl.dev/docs/workflows/storybook

# `next-intl`을 위한 Storybook 통합

[Storybook](https://storybook.js.org/)은 UI 컴포넌트를 격리된 환경에서 개발하기 위한 도구이며, 국제화에 의존하는 컴포넌트를 처리하기 위해 `next-intl`과 함께 사용할 수 있습니다.

## 수동 설정[](https://next-intl.dev/docs/workflows/storybook#manual-setup)

`next-intl`용 Storybook을 설정하려면, 스토리를 적절히 감싸도록 [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider)를 렌더링하는 [전역 데코레이터](https://storybook.js.org/docs/writing-stories/decorators#global-decorators)를 구성할 수 있습니다:

.storybook/preview.tsx
```
    import {Preview} from '@storybook/react';
    import defaultMessages from '../messages/en.json';

    const preview: Preview = {
      decorators: [
        (Story) => (
        )
      ]
    };

    export default preview;
```

이 설정을 적용하면 `useTranslations` 같은 훅 기반 API를 사용하는 컴포넌트를 렌더링할 수 있습니다.

비동기 Server Components 지원은 현재 Storybook에서 [실험적](https://storybook.js.org/docs/get-started/frameworks/nextjs#react-server-components-rsc)이며, 추가 구성이 필요할 수 있습니다.

💡

**팁:** 앱에서 [non-async components](https://next-intl.dev/docs/environments/server-client-components#shared-components)를 통해 Server Components로 렌더링되는 컴포넌트를 선언하면, 이러한 컴포넌트는 Storybook에서 Client Components로 렌더링될 수 있으며 `NextIntlClientProvider`의 구성을 사용하게 됩니다.

## `storybook-next-intl`[](https://next-intl.dev/docs/workflows/storybook#storybook-next-intl)

전역 데코레이터를 직접 설정하는 대신, 커뮤니티에서 유지 관리하는 애드온인 [`storybook-next-intl`](https://github.com/stevensacks/storybook-next-intl)을 사용하여 Storybook을 이에 맞게 구성할 수 있습니다.

**기능**

  * [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider)를 전역으로 설정해 줍니다
  * 로케일 전환기를 제공하여 서로 다른 로케일로 컴포넌트를 테스트할 수 있습니다

![next-intl을 위한 Storybook 통합](https://next-intl.dev/_next/image?url=%2Fstorybook-integration.png&w=3840&q=75)

