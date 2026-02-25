---
title: 'Storybook integration for next-intl'
description: 'To set up Storybook for , you can configure a global decorator that renders  to wrap your stories accordingly:'
---

Source URL: https://next-intl.dev/docs/workflows/storybook

# Storybook integration for `next-intl`

[Storybook](https://storybook.js.org/) is a tool for developing UI components in isolation and can be used in combination with `next-intl` to handle components that rely on internationalization.

## Manual setup[](https://next-intl.dev/docs/workflows/storybook#manual-setup)

To set up Storybook for `next-intl`, you can configure a [global decorator](https://storybook.js.org/docs/writing-stories/decorators#global-decorators) that renders [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider) to wrap your stories accordingly:

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

With this setup in place, you’re able to render components that use hook-based APIs like `useTranslations`.

Note that support for async Server Components is currently [experimental](https://storybook.js.org/docs/get-started/frameworks/nextjs#react-server-components-rsc) in Storybook and might require additional configuration.

💡

**Tip:** If you declare components that render as Server Components in your app via [non-async components](https://next-intl.dev/docs/environments/server-client-components#shared-components), these components can render as Client Components in Storybook and will consume configuration from `NextIntlClientProvider`.

## `storybook-next-intl`[](https://next-intl.dev/docs/workflows/storybook#storybook-next-intl)

Alternatively to setting up the global decorator yourself, you can use [`storybook-next-intl`](https://github.com/stevensacks/storybook-next-intl), a community-maintained addon that configures Storybook accordingly for you.

**Features**

  * Sets up [`NextIntlClientProvider`](https://next-intl.dev/docs/usage/configuration#nextintlclientprovider) globally for you
  * Provides a locale switcher so you can test components with different locales

![Storybook integration for next-intl](https://next-intl.dev/_next/image?url=%2Fstorybook-integration.png&w=3840&q=75)

