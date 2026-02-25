---
title: 'Next.js 플러그인 (createNextIntlPlugin)'
description: "import {NextConfig} from 'next';"
---

Source URL: https://next-intl.dev/docs/usage/plugin

[문서](https://next-intl.dev/docs/getting-started "문서")[사용 가이드](https://next-intl.dev/docs/usage "사용 가이드")Next.js 플러그인

# Next.js 플러그인 (`createNextIntlPlugin`)

[App Router](https://next-intl.dev/docs/getting-started/app-router)용 `next-intl`을 설정할 때는 Next.js 설정에 `next-intl/plugin`을 추가합니다.

최소 구성은 다음과 같습니다:

next.config.ts
```
    import {NextConfig} from 'next';
    import createNextIntlPlugin from 'next-intl/plugin';

    const nextConfig: NextConfig = {};

    const withNextIntl = createNextIntlPlugin();
    export default withNextIntl(nextConfig);
```

커스터마이징하려면 플러그인에 옵션을 전달할 수 있습니다.

## `requestConfig`[](https://next-intl.dev/docs/usage/plugin#request-config)

기본적으로 `next-intl`은 요청별 설정을 반환하는 [`i18n/request.ts`](https://next-intl.dev/docs/usage/configuration#server-client-components) 파일을 찾습니다. 이 파일은 `src` 폴더와 프로젝트 루트 모두에서 `.ts`, `.tsx`, `.js`, `.jsx` 확장자로 검색됩니다.

이 파일을 다른 위치로 옮기고 싶다면 플러그인에 경로를 전달할 수 있습니다:

next.config.ts
```
    const withNextIntl = createNextIntlPlugin(
      // Specify a custom path here
      './somewhere/else/request.ts'
    );
```

또는 다른 옵션과 함께 조합하는 경우 `requestConfig` 옵션을 사용할 수 있습니다:

next.config.ts
```
    const withNextIntl = createNextIntlPlugin({
      requestConfig: './somewhere/else/request.ts'
    });
```

## `experimental`[](https://next-intl.dev/docs/usage/plugin#experimental)

새 기능을 먼저 사용해 보고 싶은 사용자를 위해, Next.js 플러그인은 정식 안정 버전으로 출시되기 전에 기능을 시험해 볼 수 있는 다양한 실험적 옵션을 제공합니다.

### `createMessagesDeclaration`[](https://next-intl.dev/docs/usage/plugin#create-messages-declaration)

[타입 안전한 메시지 인자](https://next-intl.dev/docs/workflows/typescript#messages-arguments)를 활성화하려면, `createMessagesDeclaration` 옵션을 샘플 메시지 파일로 지정해 해당 파일에 대한 엄격한 선언 파일을 생성할 수 있습니다.

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

자세한 내용은 [TypeScript augmentation](https://next-intl.dev/docs/workflows/typescript)을 참고하세요.

**참고:** [`useExtracted`](https://next-intl.dev/docs/usage/extraction)를 사용하는 경우에는 필요하지 않습니다.

### `extract`[](https://next-intl.dev/docs/usage/plugin#extract)

이 옵션을 사용하면 [`useExtracted`](https://next-intl.dev/docs/usage/extraction)를 통해 소스 파일에서 메시지를 자동으로 추출할 수 있습니다.
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

**참고:** `extract` 옵션은 [`messages`](https://next-intl.dev/docs/usage/plugin#messages) 및 [`srcPath`](https://next-intl.dev/docs/usage/plugin#src-path)와 함께 사용해야 합니다.

### `messages`[](https://next-intl.dev/docs/usage/plugin#messages)

로케일별 메시지를 어디에 저장하고 어떻게 로드할지 정의합니다.
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

`experimental.messages`를 설정하면 Turbo 또는 Webpack 로더가 구성되어 메시지를 일반 JavaScript 객체로 가져올 수 있습니다([`format`](https://next-intl.dev/docs/usage/plugin#format) 참고).

#### `path`[](https://next-intl.dev/docs/usage/plugin#path)

메시지를 포함한 디렉터리의 상대 경로:
```
    // ...
    path: './messages';
```

#### `locales`[](https://next-intl.dev/docs/usage/plugin#locales)

[`useExtracted`](https://next-intl.dev/docs/usage/extraction)를 사용할 때, 어떤 메시지를 [`extract.sourceLocale`](https://next-intl.dev/docs/usage/plugin#extract)와 동기화할지 정의합니다.

`messages.path` 내의 모든 로케일을 자동 감지할 수도 있고:
```
    // ...
    locales: 'infer';
```

… 또는 명시적으로 지정할 수도 있습니다(예: 일부만 사용):
```
    // ...
    locales: ['en', 'de', 'fr'];
```

#### `format`[](https://next-intl.dev/docs/usage/plugin#format)

카탈로그를 어떤 형식으로 저장할지 정의합니다(예: `'json'`, `'po'`, 또는 사용자 정의 형식).

##### JSON format[](https://next-intl.dev/docs/usage/plugin#formats-json)

이 옵션을 사용하면 메시지는 다음과 같은 형태가 될 수 있습니다:
```
    {
      "greeting": "Hello"
    }
```

… 또는 [`useExtracted`](https://next-intl.dev/docs/usage/extraction)의 경우 자동 생성된 키를 사용합니다:
```
    {
      "NhX4DJ": "Hello"
    }
```

로컬에서 JSON 메시지를 편집할 때는 i18n Ally 같은 [VSCode integration](https://next-intl.dev/docs/workflows/vscode-integration)을 사용할 수 있습니다.

JSON 파일은 키-값 쌍만 저장할 수 있다는 점에 유의하세요. 파일 참조나 설명처럼 메시지에 더 많은 컨텍스트를 제공하려면 [PO files](https://next-intl.dev/docs/usage/plugin#formats-po)를 사용하거나 추가 메타데이터를 저장할 수 있도록 [custom format](https://next-intl.dev/docs/usage/plugin#formats-custom)을 만들 수 있습니다.

##### PO format[](https://next-intl.dev/docs/usage/plugin#formats-po)

이 옵션을 사용하면 메시지는 다음과 같은 형태가 됩니다:
```
    #. Advance to the next slide
    #: src/components/Carousel.tsx:13
    msgid "carousel.next"
    msgstr "Right"
```

… 또는 [`useExtracted`](https://next-intl.dev/docs/usage/extraction)의 경우 자동 생성된 키를 사용합니다:
```
    #. Advance to the next slide
    #: src/components/Carousel.tsx:13
    msgid "5VpL9Z"
    msgstr "Right"
```

메시지 키와 라벨 자체 외에도, 이 형식은 선택적 설명과 해당 메시지를 사용하는 모든 모듈의 파일 참조를 지원합니다.

로컬에서 `.po` 파일을 편집할 때는 [Poedit](https://poedit.net/) 같은 도구를 사용할 수 있습니다.

##### Custom format[](https://next-intl.dev/docs/usage/plugin#formats-custom)

사용자 정의 형식을 구성하려면 확장자와 함께 codec을 지정해야 합니다.

codec은 `next-intl/extractor`의 `defineCodec`으로 만들 수 있습니다:

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

그런 다음 설정에서 `extension`과 함께 참조합니다:

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

영감을 얻기 위해 내장 [`codecs`](https://github.com/amannn/next-intl/tree/main/packages/next-intl/src/extractor/format/codecs)와 함께 제공되는 타입 및 JSDoc 레퍼런스도 참고하세요.

💡

위 예제처럼 필요한 TypeScript 네이티브 실행은 Node.js v22.18부터 지원됩니다. 더 낮은 버전을 사용 중이라면 codec을 JavaScript 파일로 정의해야 합니다.

#### `precompile`[](https://next-intl.dev/docs/usage/plugin#precompile)

성능 최적화를 위해, 빌드 중에 메시지를 사전 컴파일하면 번들 크기를 줄이고 런타임 메시지 포매팅 속도를 높일 수 있습니다:
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

제공한 옵션에 따라, 이제 앱에서 메시지를 가져올 때 사전 컴파일됩니다:
```
    // ✅ Will be pre-processed by a Turbo- or Webpack loader
    const messages = (await import(`../../messages/en.json`)).default;
```

추가 참고: [Ahead-of-time compilation with `next-intl`](https://next-intl.dev/blog/precompilation)

**참고:** 사전 컴파일된 메시지에서는 `t.raw`를 지원하지 않습니다([tradeoffs](https://github.com/amannn/next-intl/blob/main/rfcs/002-icu-message-precompilation.md#tradeoffs) 참고)

[](https://next-intl.dev/docs/usage/plugin#precompile-runtime-messages)메시지를 수동으로 사전 컴파일하려면 어떻게 하나요?

앱에 메시지를 `import`하지 않는 경우(예: 런타임에 가져오는 경우), `icu-minify/compile`을 사용해 수동으로 사전 컴파일할 수 있습니다:

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

이 경우 호환성을 위해, 사용 중인 `next-intl` 버전이 의존하는 `icu-minify`와 동일한 버전을 사용해야 합니다.

### `srcPath`[](https://next-intl.dev/docs/usage/plugin#src-path)

메시지를 추출할 소스 경로를 정의합니다.
```
    const withNextIntl = createNextIntlPlugin({
      experimental: {
        srcPath: './src'
        // ...
      }
    });
```

프로젝트가 여러 폴더로 나뉘어 있다면 경로 배열을 전달할 수 있습니다:
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

`node_modules`, `.next`, `.git` 디렉터리는 `srcPath` 배열에 명시적으로 포함된 경우를 제외하고 자동으로 추출 대상에서 제외됩니다.

패키지와 함께 메시지를 제공하려는 경우 [수동으로](https://next-intl.dev/docs/usage/extraction#manual) 추출할 수도 있습니다.

**참고:** `srcPath` 옵션은 [`extract`](https://next-intl.dev/docs/usage/plugin#extract) 및 [`messages`](https://next-intl.dev/docs/usage/plugin#messages)와 함께 사용해야 합니다.

