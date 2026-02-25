---
title: 'Vitest[](https://next-intl.dev/docs/environments/testing#vitest)'
description: '원본 URL: https://next-intl.dev/docs/environments/testing'
---

원본 URL: https://next-intl.dev/docs/environments/testing

# 테스트

`next-intl`을 사용하는 컴포넌트는 단위 테스트에서 사용할 수 있습니다:
```
    import {render} from '@testing-library/react';
    import {NextIntlClientProvider} from 'next-intl';
    import {expect, it} from 'vitest';
    import messages from '../../messages/en.json';
    import UserProfile from './UserProfile';

    it('renders', () => {
      render(
      );
    });
```

서버 컴포넌트를 목킹하지 않아도 되도록, 컴포넌트를 [non-async 함수](https://next-intl.dev/docs/environments/server-client-components#async-or-non-async)로 정의하면 유용할 수 있으며, 이를 통해 어떤 환경에서든 유연하게 렌더링할 수 있습니다.

## Vitest[](https://next-intl.dev/docs/environments/testing#vitest)

`next-intl`은 ESM-only로 번들되므로 내부적으로 [명시적 파일 확장자](https://nodejs.org/api/esm.html#mandatory-file-extensions)를 사용해야 합니다. 하지만 [Next.js의 디옵티마이제이션](https://github.com/vercel/next.js/issues/77200)을 피하기 위해, 현재 `next-intl`은 `next/navigation.js` 대신 `next/navigation`에서 import해야 합니다.

다만 Vitest는 파일 확장자를 올바르게 가정하므로, 현재로서는 [`createNavigation`](https://next-intl.dev/docs/routing/navigation)을 사용하는 경우 Vitest가 `next-intl` 내부의 import를 처리하도록 설정해야 합니다:

vitest.config.mts
```
    import {defineConfig} from 'vitest/config';

    export default defineConfig({
      test: {
        server: {
          deps: {
            // https://github.com/vercel/next.js/issues/77200
            inline: ['next-intl']
          }
        }
      }
    });
```

## Jest[](https://next-intl.dev/docs/environments/testing#jest)

Jest에는 내장 ESM 지원이 없기 때문에, `next-intl`에서 가져오는 import를 변환하도록 Jest에 지시해야 합니다:

jest.config.js
```
    const nextJest = require('next/jest');

    const createJestConfig = nextJest({dir: './'});

    module.exports = async () => ({
      ...(await createJestConfig({
        testEnvironment: 'jsdom',
        rootDir: 'src'
      })()),
      // https://github.com/vercel/next.js/issues/40183
      transformIgnorePatterns: ['node_modules/(?!next-intl)/']
    });
```

[에러 파일(예: not-found)](https://next-intl.dev/docs/environments/error-files "에러 파일 \(예: not-found\)")[코어 라이브러리](https://next-intl.dev/docs/environments/core-library "코어 라이브러리")

