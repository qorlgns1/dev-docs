---
title: 'Next.js plugin (createNextIntlPlugin)'
description: 'When setting up  for the App Router, you’ll add  to your Next.js config.'
---

Source URL: https://next-intl.dev/docs/usage/plugin

[Docs](https://next-intl.dev/docs/getting-started "Docs")[Usage guide](https://next-intl.dev/docs/usage "Usage guide")Next.js plugin

# Next.js plugin (`createNextIntlPlugin`)

When setting up `next-intl` for the [App Router](https://next-intl.dev/docs/getting-started/app-router), you’ll add `next-intl/plugin` to your Next.js config.

At the minimum, it will look like this:

next.config.ts
```
    import {NextConfig} from 'next';
    import createNextIntlPlugin from 'next-intl/plugin';

    const nextConfig: NextConfig = {};

    const withNextIntl = createNextIntlPlugin();
    export default withNextIntl(nextConfig);
```

For customization, you can provide options to the plugin.

## `requestConfig`[](https://next-intl.dev/docs/usage/plugin#request-config)

By default, `next-intl` will look for a file called [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#server-client-components) which returns request-specific configuration. This file is searched for both in the `src` folder as well as in the project root with the extensions `.ts`, `.tsx`, `.js` and `.jsx`.

If you prefer to move this file somewhere else, you can provide a path to the plugin:

next.config.ts
```
    const withNextIntl = createNextIntlPlugin(
      // Specify a custom path here
      './somewhere/else/request.ts'
    );
```

Or if you’re combining this with other options, you can use the `requestConfig` option:

next.config.ts
```
    const withNextIntl = createNextIntlPlugin({
      requestConfig: './somewhere/else/request.ts'
    });
```

## `experimental`[](https://next-intl.dev/docs/usage/plugin#experimental)

For early adopters, the Next.js plugin provides various experimental options that let you try out new features before they’re released as stable.

### `createMessagesDeclaration`[](https://next-intl.dev/docs/usage/plugin#create-messages-declaration)

To enable [type-safe message arguments](https://next-intl.dev/docs/workflows/typescript#messages-arguments), you can point the `createMessagesDeclaration` option to a sample messages file in order to create a strict declaration file for it.

next.config.ts
```
    const withNextIntl = createNextIntlPlugin({
      experimental: {
        // Provide the path to the messages that you're using in `AppConfig`
        createMessagesDeclaration: './messages/en.json'
      }
      // ...
    });
```

See [TypeScript augmentation](https://next-intl.dev/docs/workflows/typescript) to learn more about this.

**Note:** This is not necessary when using [`useExtracted`](https://next-intl.dev/docs/usage/extraction).

### `extract`[](https://next-intl.dev/docs/usage/plugin#extract)

This enables the usage of [`useExtracted`](https://next-intl.dev/docs/usage/extraction) to automatically extract messages from source files.
```
    const withNextIntl = createNextIntlPlugin({
      experimental: {
        extract: {
          // Defines which locale to extract to
          sourceLocale: 'en'
        }
        // ...
      }
    });
```

**Note:** The `extract` option should be used together with [`messages`](https://next-intl.dev/docs/usage/plugin#messages) and [`srcPath`](https://next-intl.dev/docs/usage/plugin#src-path).

### `messages`[](https://next-intl.dev/docs/usage/plugin#messages)

This defines where messages for locales are stored and how they’re loaded.
```
    const withNextIntl = createNextIntlPlugin({
      experimental: {
        messages: {
          format: 'json',
          locales: 'infer',
          path: './messages',

          // Optional
          precompile: true
        }
      }
    });
```

Configuring `experimental.messages` sets up a Turbo- or Webpack loader that allows messages to be imported as plain JavaScript objects (see [`format`](https://next-intl.dev/docs/usage/plugin#format)).

#### `path`[](https://next-intl.dev/docs/usage/plugin#path)

Relative path to the directory containing messages:
```
    // ...
    path: './messages';
```

#### `locales`[](https://next-intl.dev/docs/usage/plugin#locales)

When using [`useExtracted`](https://next-intl.dev/docs/usage/extraction), this defines which messages are kept in sync with [`extract.sourceLocale`](https://next-intl.dev/docs/usage/plugin#extract).

You can either automatically detect all locales within `messages.path`:
```
    // ...
    locales: 'infer';
```

… or specify them explicitly (e.g. to use a subset):
```
    // ...
    locales: ['en', 'de', 'fr'];
```

#### `format`[](https://next-intl.dev/docs/usage/plugin#format)

Defines how your catalogs are stored (e.g. `'json'`, `'po'`, or a custom format).

##### JSON format[](https://next-intl.dev/docs/usage/plugin#formats-json)

When using this option, your messages might look like this:
```
    {
      "greeting": "Hello"
    }
```

… or in case of [`useExtracted`](https://next-intl.dev/docs/usage/extraction), with an auto-generated key:
```
    {
      "NhX4DJ": "Hello"
    }
```

For local editing of JSON messages, you can use e.g. a [VSCode integration](https://next-intl.dev/docs/workflows/vscode-integration) like i18n Ally.

Note that JSON files can only hold pairs of keys and values. To provide more context about a message like file references and descriptions, you can use [PO files](https://next-intl.dev/docs/usage/plugin#formats-po) or create a [custom format](https://next-intl.dev/docs/usage/plugin#formats-custom) to store additional metadata.

##### PO format[](https://next-intl.dev/docs/usage/plugin#formats-po)

When using this option, your messages will look like this:
```
    #. Advance to the next slide
    #: src/components/Carousel.tsx:13
    msgid "carousel.next"
    msgstr "Right"
```

… or in case of [`useExtracted`](https://next-intl.dev/docs/usage/extraction), with an auto-generated key:
```
    #. Advance to the next slide
    #: src/components/Carousel.tsx:13
    msgid "5VpL9Z"
    msgstr "Right"
```

Besides the message key and the label itself, this format also supports optional descriptions and file references to all modules that consume this message.

For local editing of .po files, you can use e.g. a tool like [Poedit](https://poedit.net/).

##### Custom format[](https://next-intl.dev/docs/usage/plugin#formats-custom)

To configure a custom format, you need to specify a codec along with an extension.

The codec can be created via `defineCodec` from `next-intl/extractor`:

./CustomCodec.ts
```
    import {defineCodec} from 'next-intl/extractor';

    export default defineCodec(() => ({
      decode(content, context) {
        // ...
      },

      encode(messages, context) {
        // ...
      },

      toJSONString(content, context) {
        // ...
      }
    }));
```

Then, reference it in your configuration along with an `extension`:

next.config.ts
```
    const withNextIntl = createNextIntlPlugin({
      experimental: {
        messages: {
          format: {
            codec: './CustomCodec.ts',
            extension: '.json'
          }
          // ...
        }
      }
    });
```

See also the built-in [`codecs`](https://github.com/amannn/next-intl/tree/main/packages/next-intl/src/extractor/format/codecs) for inspiration, as well as the supplied types and JSDoc reference.

💡

Node.js supports native TypeScript execution like it’s needed for the example above, starting with v22.18. If you’re on an older version, you should define your codec as a JavaScript file.

#### `precompile`[](https://next-intl.dev/docs/usage/plugin#precompile)

As a performance optimization, you can achieve smaller bundles and faster message formatting at runtime by precompiling messages ahead of time during the build:
```
    const withNextIntl = createNextIntlPlugin({
      experimental: {
        messages: {
          path: './messages',
          locales: 'infer',
          format: 'json',
          precompile: true
        }
        // ...
      }
    });
```

Based on the provided options, message will now be precompiled when imported into your app:
```
    // ✅ Will be pre-processed by a Turbo- or Webpack loader
    const messages = (await import(`../../messages/en.json`)).default;
```

See also: [Ahead-of-time compilation with `next-intl`](https://next-intl.dev/blog/precompilation)

**Note:** `t.raw` is not supported with precompiled messages (see [tradeoffs](https://github.com/amannn/next-intl/blob/main/rfcs/002-icu-message-precompilation.md#tradeoffs))

[](https://next-intl.dev/docs/usage/plugin#precompile-runtime-messages)How can I manually precompile messages?

For cases where you don’t `import` messages into your app (e.g. when fetching them at runtime), you can manually precompile them using `icu-minify/compile`:

i18n/request.ts
```
    import compile from 'icu-minify/compile';
    import {getRequestConfig} from 'next-intl/server';

    type Messages = Record<string, unknown>;

    function compileMessages(messages: Messages): Messages {
      return Object.fromEntries(
        Object.entries(messages).map(([key, value]) => {
          if (value && typeof value === 'object') {
            return [key, compileMessages(value as Messages)];
          }

          if (typeof value === 'string') {
            return [key, compile(value)];
          }

          throw new Error(`Unexpected message: ${typeof value}`);
        })
      );
    }

    export default getRequestConfig(async () => {
      const response = await fetch('https://cdn.example.com/messages/en.json');
      const messages = (await response.json()) as Messages;
      const compiled = compileMessages(messages);

      return {
        messages: compiled
        // ...
      };
    });
```

If you do this, be sure to use the same version of `icu-minify` as the one that your `next-intl` version depends on to ensure compatibility.

### `srcPath`[](https://next-intl.dev/docs/usage/plugin#src-path)

This defines the source path where messages should be extracted from.
```
    const withNextIntl = createNextIntlPlugin({
      experimental: {
        srcPath: './src'
        // ...
      }
    });
```

If your project is split into multiple folders, you can provide an array of paths:
```
    // Not using a `src` folder
    srcPath: './',
```
```
    // Monorepo with multiple packages
    srcPath: ['./src', '../ui'],
```
```
    // External dependency on a package
    srcPath: ['./src', './node_modules/@acme/components'],
```

Note that the directories `node_modules`, `.next` and `.git` are automatically excluded from extraction, except for if they appear explicitly in the `srcPath` array.

If you want to provide messages along with your package, you can also extract them [manually](https://next-intl.dev/docs/usage/extraction#manual).

**Note:** The `srcPath` option should be used together with [`extract`](https://next-intl.dev/docs/usage/plugin#extract) and [`messages`](https://next-intl.dev/docs/usage/plugin#messages).

