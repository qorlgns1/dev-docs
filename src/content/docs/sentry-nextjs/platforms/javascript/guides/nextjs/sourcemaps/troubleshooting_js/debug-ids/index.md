---
title: 'Debug ID란 무엇인가 | Sentry for Next.js'
description: '이 문서는 Debug ID를 심층적으로 설명하며, Debug ID가 어떻게 동작하는지와 Sentry가 이를 권장하는 이유를 다룹니다. 소스맵 업로드 방법 가이드를 찾고 있다면 Uploading Source Maps를 참고하세요.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids

# Debug ID란 무엇인가 | Sentry for Next.js

이 문서는 Debug ID를 심층적으로 설명하며, Debug ID가 어떻게 동작하는지와 Sentry가 이를 권장하는 이유를 다룹니다. 소스맵 업로드 방법 가이드를 찾고 있다면 [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/react/sourcemaps/uploading.md)를 참고하세요.

## [소개](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#introduction)

현대 웹 애플리케이션은 JavaScript를 사용할 때 대개 어떤 형태로든 빌드 프로세스를 거칩니다. 이 빌드 프로세스는 입력 JavaScript를 받아 특정 방식으로 변환한 뒤, 웹사이트와 함께 제공되는 JavaScript를 출력합니다. 대표적인 변환 예로는 JavaScript 코드 난독화/압축(minify, 최종 번들을 더 작고 빠르게 로드하도록 함)이나 TypeScript 타입 제거(브라우저에서는 JavaScript만 실행 가능)가 있습니다.

그 결과, 프로덕션에서 실행되는 JavaScript 코드는 일반적으로 개발자가 소스 에디터에서 작성한 코드와 동일하지 않습니다. 대신 minification, transpilation, downcompilation, bundling, polyfilling 등 여러 변환을 거치며, 성능 향상과 브라우저 간 호환성 확보를 목표로 합니다. 이러한 변환을 수행하는 대표 도구로는 Babel, Vite, Webpack, Rollup, Terser, SWC가 있으며, Next.js, Nuxt, Create React App 같은 상위 도구에서 자주 사용됩니다.

스택 트레이스는 에러 디버깅에 필수지만, 생성된 JavaScript에서 나온 스택 트레이스는 종종 읽기 어렵거나 활용하기 힘듭니다! 작성한 코드와 전혀 다르게 보이고, 소스 코드 저장소와 연결하기도 어렵습니다.

Sentry(및 기타 도구)에서 읽기 쉽고 유용한 스택 트레이스를 제공하려면 [source maps](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/use_a_source_map/index.html)를 생성하고 사용해야 합니다. 소스맵은 변환된 JavaScript를 원본 코드로 매핑해 주는 추가 정보(대개 파일 형태)입니다. 이를 통해 Sentry가 에러를 원본 소스와 연결할 수 있고, 결과적으로 생성된 코드가 아니라 작성한 코드 기준의 스택 트레이스를 확인할 수 있습니다.

JavaScript 파일과 소스맵을 연결하기 위해 기존에는 파일명에 의존했지만, 이는 종종 신뢰하기 어려웠습니다. 예를 들어 JavaScript 파일이 제공되는 서브패스가 바뀌면 파일명이 더 이상 일치하지 않아, 해당 sourcemap을 Sentry가 찾지 못하게 됩니다.

`//# source mappingURL=http://example.com/path/to/your/source-map.js.map`

URL 기반 파일명 접근 방식은 신뢰성이 낮았기 때문에, 우리는 [Debug IDs](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#what-are-debug-ids)를 도입했습니다.

## [Debug ID란 무엇인가](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#what-are-debug-ids)

네이티브 언어 생태계의 접근 방식에서 영감을 받아, Debug ID는 변환된 JavaScript 파일과 연결된 소스맵을 식별하는 전역 고유 ID입니다.

sentry-cli 또는 Webpack, Vite, Rollup용 Sentry 플러그인을 사용할 경우, Debug ID는 소스 파일 내용 기반으로 결정론적으로 생성됩니다. 단, 현재 esbuild에 대해서는 결정론적 Debug ID가 지원되지 않습니다.

이 방식은 축소(minified)된 JavaScript 파일을 원본 소스 코드와 연결하는 데 있어 Sentry가 권장하는 가장 신뢰도 높은 방법이며, 에러를 소스까지 추적하기 쉽게 해 줍니다. 파일 내용이 바뀌면 릴리스 간 Debug ID도 일반적으로 바뀌므로, 이제는 **release 생성이 더 이상 필수가 아닙니다**. 과거에는 배포 간 동일한 이름의 sourcemap을 구분하기 위해 release 이름을 사용했습니다.

Debug ID 도입 배경을 더 알고 싶다면 [engineering blog](https://sentry.engineering/blog/the-case-for-debug-ids)를 참고하세요.

## [Sentry가 Debug ID를 사용하는 방법](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#how-sentry-uses-debug-ids)

Next.js에서 Debug ID를 사용하려면 **Sentry SDK 버전 8.0.0 이상**이 필요합니다. 지원 버전으로 업그레이드했다면 아래 단계를 따르세요.

1. **전역 고유 Debug ID 생성**: 빌드 과정에서 Sentry Bundler Plugin 또는 Sentry CLI를 사용하면 전역 고유하며 이상적으로는 결정론적인 Debug ID가 생성됩니다.

2. **축소 파일에 Debug ID 임베드**: 각 축소 JavaScript 파일에는 `//# debugId=DEBUG_ID` 같은 특수 주석이 포함되며, 여기서 `DEBUG_ID`는 이전 단계에서 생성된 고유 식별자입니다.

3) **소스맵에도 동일한 Debug ID 추가**: 소스맵에도 동일한 Debug ID가 새 속성으로 포함되어, 축소 JavaScript 파일과 해당 소스맵이 연결됩니다.

4) **Sentry의 스택 트레이스가 Debug ID를 연결**: 에러가 발생하면 Sentry 이벤트에 Debug ID가 포함되고, 이를 통해 Sentry가 해당 에러를 올바른 소스맵과 자동으로 연결합니다. 이로써 스택 트레이스가 원본 소스 코드 기준으로 해석되어, JavaScript가 축소되거나 변환된 경우에도 더 명확하고 정확한 디버깅 정보를 제공합니다.

- [코드를 unminify할 때 왜 Debug ID를 사용해야 하나요?](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#why-use-debug-ids-to-uniminify-your-code)

효율적인 디버깅을 위해 코드 unminify는 필수입니다. Sentry에서는 이를 위한 다른 [기존 방식](https://docs.sentry.io/platforms/javascript/sourcemaps/troubleshooting_js/legacy-uploading-methods.md)도 있지만, **Debug ID 사용을 Sentry가 권장**합니다. 가장 신뢰할 수 있는 방법이기 때문입니다. 코드를 unminify하면 에러 발생 시 훨씬 명확한 스택 트레이스를 얻을 수 있습니다. 난독화된 코드 대신 원래 작성한 정확한 코드를 보게 되어, 문제를 이해하고 해결하기가 훨씬 쉬워집니다. 아래 예시는 그 차이를 보여줍니다.

#
- [나쁜 스택 트레이스](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#bad-stack-trace)

#
- [좋은 스택 트레이스](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#good-stack-trace)

## [보존 정책](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#retention-policy)

Debug ID를 포함한 아티팩트의 보존 기간은 *90일*이며, *time to idle* 만료 메커니즘을 사용합니다. 즉, 업로드된 Debug ID는 이벤트 처리에 실제로 사용되는 동안 유지됩니다. 특정 ID가 들어오는 이벤트 처리에 최소 90일 동안 사용되지 않으면, 자동으로 만료되어 삭제 대상이 됩니다.

## [Debug ID와 Release 연결하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/troubleshooting_js/debug-ids.md#associating-a-release-with-debug-ids)

특정 Debug ID가 어떤 release에 연결되어 있는지 여전히 알고 싶을 수 있기 때문에, 우리는 번들에 `release`를 계속 연결할 수 있는 새로운 방식을 설계했습니다.

새 Debug ID 형식은 `release` 및 선택적으로 `dist`와의 새로운 연결 방식(weak release association)을 지원합니다. 이 연결 방식은 소스맵 업로드 전에 `release`를 생성할 필요가 **없으며**, 따라서 파이프라인의 별도 단계에서 `release`를 생성할 수 있게 해줍니다.

`release`와 선택적으로 `dist`를 연결해 두면, 어떤 Debug ID가 에러에 사용됐는지 일일이 신경 쓰지 않아도 Sentry에서 `release`에서 해당 Debug ID로 빠르게 이동할 수 있습니다.

