---
title: 'Testing'
description: 'Components that use  can be used in unit tests:'
---

Source URL: https://next-intl.dev/docs/environments/testing

# Testing

Components that use `next-intl` can be used in unit tests:
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

To avoid having to mock server components, it can be beneficial to define components as [non-async functions](https://next-intl.dev/docs/environments/server-client-components#async-or-non-async), allowing you to flexibly render them in any environment.

## Vitest[](https://next-intl.dev/docs/environments/testing#vitest)

`next-intl` is bundled as ESM-only, which requires the usage of [explicit file extensions](https://nodejs.org/api/esm.html#mandatory-file-extensions) internally. However, in order to avoid a [deoptimization in Next.js](https://github.com/vercel/next.js/issues/77200), `next-intl` currently has to import from `next/navigation` instead of `next/navigation.js`.

Vitest correctly assumes a file extension though, therefore for the time being, if you’re using [`createNavigation`](https://next-intl.dev/docs/routing/navigation), you need to ask Vitest to process imports within `next-intl`:

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

Since Jest doesn’t have built-in ESM support, you need to instruct Jest to transform imports from `next-intl`:

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

[Error files (e.g. not-found)](https://next-intl.dev/docs/environments/error-files "Error files \(e.g. not-found\)")[Core library](https://next-intl.dev/docs/environments/core-library "Core library")

