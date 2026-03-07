---
title: "다른 테스트 러너와의 비교"
description: "Vite 설정에서도 Jest를 사용할 수 있습니다. @sodatea가 vite-jest를 만들었고, 이는 Jest에 대한 1급 Vite 통합을 제공하는 것을 목표로 합니다. 마지막 Jest의 블로커도 해결되었기 때문에, 단위 테스트를 위한 유효한 선택지입니다."
---

출처 URL: https://vitest.dev/guide/comparisons

# 다른 테스트 러너와의 비교

## Jest

[Jest](https://jestjs.io/)는 대부분의 JavaScript 프로젝트에 대한 즉시 사용 가능한 지원, 익숙한 API(`it` 및 `expect`), 그리고 대부분의 환경에서 필요한 전체 테스트 기능(스냅샷, 모킹, 커버리지)을 제공하며 테스트 프레임워크 영역을 주도해 왔습니다. 웹 생태계의 표준이 된 다양한 테스트 패턴을 발전시키고 훌륭한 테스트 API를 만들어 준 Jest 팀과 커뮤니티에 감사드립니다.

Vite 설정에서도 Jest를 사용할 수 있습니다. [@sodatea](https://bsky.app/profile/haoqun.dev)가 [vite-jest](https://github.com/sodatea/vite-jest#readme)를 만들었고, 이는 [Jest](https://jestjs.io/)에 대한 1급 Vite 통합을 제공하는 것을 목표로 합니다. 마지막 [Jest의 블로커](https://github.com/sodatea/vite-jest/blob/main/packages/vite-jest/README.md#vite-jest)도 해결되었기 때문에, 단위 테스트를 위한 유효한 선택지입니다.

하지만 [Vite](https://vitejs.dev)가 이미 가장 일반적인 웹 툴링(TypeScript, JSX, 인기 UI 프레임워크 대부분)을 지원하는 환경에서, Jest는 복잡성을 중복시키는 선택이 됩니다. 앱이 Vite 기반이라면 서로 다른 두 파이프라인을 설정하고 유지할 이유가 없습니다. Vitest를 사용하면 개발, 빌드, 테스트 환경 구성을 하나의 파이프라인으로 정의할 수 있고, 동일한 플러그인과 같은 `vite.config.js`를 공유할 수 있습니다.

라이브러리가 Vite를 사용하지 않더라도(예: esbuild 또는 Rollup으로 빌드하는 경우), Vitest는 흥미로운 선택지입니다. Vite의 즉시 Hot Module Reload(HMR)를 활용한 기본 watch 모드 덕분에 단위 테스트 실행 속도가 더 빠르고 DX도 향상됩니다. Vitest는 Jest API 및 생태계 라이브러리 대부분과 호환되므로, 대다수 프로젝트에서 Jest를 거의 그대로 대체할 수 있습니다.

## Cypress

[Cypress](https://www.cypress.io/)는 브라우저 기반 테스트 러너이며 Vitest를 보완하는 도구입니다. Cypress를 사용하고 싶다면, 애플리케이션의 헤드리스 로직은 Vitest로, 브라우저 기반 로직은 Cypress로 테스트하는 것을 권장합니다.

Cypress는 엔드투엔드 테스트 도구로 잘 알려져 있지만, [새 컴포넌트 테스트 러너](https://on.cypress.io/component)는 Vite 컴포넌트 테스트를 매우 잘 지원하며 브라우저에 렌더링되는 모든 것을 테스트하기에 이상적인 선택입니다.

Cypress, WebdriverIO, Web Test Runner 같은 브라우저 기반 러너는 실제 브라우저와 실제 브라우저 API를 사용하기 때문에 Vitest가 잡아내지 못하는 이슈를 찾아낼 수 있습니다.

Cypress의 테스트 드라이버는 요소가 보이는지, 접근 가능한지, 상호작용 가능한지를 판단하는 데 초점을 둡니다. Cypress는 UI 개발과 테스트를 위해 설계되었고, DX도 시각적 컴포넌트를 테스트 주도로 개발하는 데 맞춰져 있습니다. 테스트 리포터와 함께 렌더링된 컴포넌트를 바로 볼 수 있으며, 테스트 완료 후에도 컴포넌트는 상호작용 가능한 상태로 유지되어 브라우저 devtools로 실패 원인을 디버깅할 수 있습니다.

반면 Vitest는 번개처럼 빠른 _헤드리스_ 테스트를 위한 최고의 DX 제공에 집중합니다. Vitest 같은 Node 기반 러너는 `jsdom` 같은 부분 구현 브라우저 환경을 지원하며, 이를 통해 브라우저 API를 참조하는 코드를 빠르게 단위 테스트할 수 있습니다. 다만 이런 브라우저 환경은 구현 가능한 범위에 한계가 있습니다. 예를 들어 [jsdom은 `window.navigation`이나 레이아웃 엔진(`offsetTop` 등) 같은 기능이 다수 빠져 있습니다](https://github.com/jsdom/jsdom/issues?q=is%3Aissue+is%3Aopen+sort%3Acomments-desc).

마지막으로 Web Test Runner와 비교하면, Cypress 테스트 러너는 테스트 결과와 로그와 함께 브라우저에서 실제 렌더링된 컴포넌트를 볼 수 있기 때문에 테스트 러너라기보다 IDE에 가깝습니다.

Cypress는 또한 [자사 제품에 Vite를 통합](https://www.youtube.com/watch?v=7S5cbY8iYLk)해 왔습니다. 예를 들어 [Vitesse](https://github.com/antfu/vitesse)로 앱 UI를 재구축하고, 프로젝트 개발을 테스트 주도로 진행하는 데 Vite를 사용합니다.

Vitest는 헤드리스 코드의 단위 테스트에 Cypress가 좋은 선택은 아니라고 보지만, Cypress(E2E 및 컴포넌트 테스트)와 Vitest(단위 테스트)를 함께 사용하면 앱의 테스트 요구사항을 폭넓게 충족할 수 있습니다.

## WebdriverIO

[WebdriverIO](https://webdriver.io/)는 Cypress와 마찬가지로 브라우저 기반의 대체 테스트 러너이자 Vitest를 보완하는 도구입니다. 엔드투엔드 테스트 도구로도 사용할 수 있고 [web components](https://webdriver.io/docs/component-testing) 테스트에도 사용할 수 있습니다. 심지어 컴포넌트 테스트 내 [mocking and stubbing](https://webdriver.io/docs/mocksandspies/) 같은 기능을 위해 내부적으로 Vitest의 구성 요소를 사용하기도 합니다.

WebdriverIO는 Cypress와 동일한 장점, 즉 실제 브라우저에서 로직을 테스트할 수 있다는 장점을 제공합니다. 하지만 자동화에는 실제 [web standards](https://w3c.github.io/webdriver/)를 사용하므로, Cypress에서 테스트를 실행할 때의 일부 트레이드오프와 제약을 극복할 수 있습니다. 또한 모바일에서도 테스트를 실행할 수 있어 더 다양한 환경에서 애플리케이션을 검증할 수 있습니다.

## Web Test Runner

[@web/test-runner](https://modern-web.dev/docs/test-runner/overview/)는 헤드리스 브라우저 내부에서 테스트를 실행하므로, 브라우저 API나 DOM을 모킹하지 않고도 웹 애플리케이션과 동일한 실행 환경을 제공합니다. 이 덕분에 실제 브라우저에서 devtools로 디버깅하는 것도 가능하지만, Cypress 테스트처럼 테스트를 단계별로 진행하는 UI는 제공되지 않습니다.

Vite 프로젝트에서 @web/test-runner를 사용하려면 [@remcovaes/web-test-runner-vite-plugin](https://github.com/remcovaes/web-test-runner-vite-plugin)을 사용하세요. @web/test-runner에는 assertion 또는 mocking 라이브러리가 포함되어 있지 않으므로, 직접 추가해야 합니다.

## uvu

[uvu](https://github.com/lukeed/uvu)는 Node.js와 브라우저를 위한 테스트 러너입니다. 단일 스레드에서 테스트를 실행하므로 테스트가 격리되지 않으며 파일 간 상태 누수가 발생할 수 있습니다. 반면 Vitest는 worker thread를 사용해 테스트를 격리하고 병렬 실행합니다.

코드 변환 측면에서 uvu는 require 및 loader hooks에 의존합니다. Vitest는 [Vite](https://vitejs.dev)를 사용하므로 Vite의 플러그인 시스템 전체 기능으로 파일을 변환합니다. Vite가 이미 가장 일반적인 웹 툴링(TypeScript, JSX, 인기 UI 프레임워크 대부분)을 지원하는 환경에서 uvu는 복잡성을 중복시킵니다. 앱이 Vite 기반이라면 서로 다른 두 파이프라인을 설정하고 유지할 이유가 없습니다. Vitest를 사용하면 개발, 빌드, 테스트 환경 구성을 하나의 파이프라인으로 정의하고, 동일한 플러그인과 같은 구성을 공유할 수 있습니다.

uvu는 변경된 테스트만 다시 실행하는 지능형 watch 모드를 제공하지 않지만, Vitest는 Vite의 즉시 Hot Module Reload(HMR)를 사용하는 기본 watch 모드 덕분에 뛰어난 DX를 제공합니다.

uvu는 단순한 테스트를 빠르게 실행하는 데 좋은 선택이지만, 더 복잡한 테스트와 프로젝트에서는 Vitest가 더 빠르고 신뢰할 수 있습니다.

## Mocha

[Mocha](https://mochajs.org)는 Node.js와 브라우저에서 실행되는 테스트 프레임워크입니다. Mocha는 서버 사이드 테스트에서 널리 사용되는 선택지입니다. Mocha는 설정 유연성이 높지만 일부 기능이 기본 포함되어 있지는 않습니다. 예를 들어 assertion 라이브러리가 내장되어 있지 않은데, 이는 Node 내장 assertion 러너만으로도 대부분의 사용 사례에 충분하다는 관점에 기반합니다. Mocha에서 assertions를 위해 자주 쓰이는 또 다른 선택지는 [Chai](https://www.chaijs.com)입니다.

Vitest는 아래와 같은 몇 가지 기능도 즉시 사용 가능하게 제공합니다. 반면 Mocha에서는 추가 설정이나 다른 라이브러리 도입이 필요합니다. 예를 들면:

- Snapshot testing
- TypeScript
- JSX support
- Code Coverage
- Mocking
- Smart watch mode (영향받은 테스트만 재실행)

Mocha는 Native ESM을 지원하지만 제한과 설정 제약이 있습니다. 예를 들어 watch mode는 ES Module 파일에서 동작하지 않습니다.

성능 측면에서 Mocha는 기본적으로 테스트를 직렬 실행하지만 `--parallel` 플래그로 병렬 실행도 지원합니다(다만 일부 리포터와 기능은 병렬 모드에서 동작하지 않습니다).

빌드 파이프라인에서 이미 Vite를 사용 중이라면, Vitest는 테스트에도 동일한 설정과 플러그인을 재사용할 수 있는 반면 Mocha는 별도의 테스트 설정이 필요합니다. Vitest는 Jest 호환 API를 제공하는 동시에 Mocha의 익숙한 `describe`, `it`, hook 문법도 지원하므로 대부분의 테스트 스위트에서 마이그레이션이 간단합니다.

Mocha는 테스트 스택을 완전히 제어해야 하는 프로젝트에서 여전히 견고한, 최소 구성의 유연한 선택지입니다. 하지만 즉시 사용 가능한 모든 것이 포함된 현대적인 테스트 경험을 원한다면, 특히 Vite 기반 애플리케이션에서는 Vitest가 좋은 선택입니다.

## Playwright

[Playwright](https://playwright.dev)는 Microsoft의 테스트 프레임워크로, 여러 브라우저(Chromium, Firefox, WebKit)에서의 엔드투엔드 테스트에 강점을 가집니다. 실제 브라우저를 제어해 로그인, 앱 탐색, 폼 제출, 결과 검증까지 완전한 사용자 워크플로를 테스트합니다. 반면 Vitest는 헤드리스 환경에서 빠르고 격리된 단위 및 컴포넌트 테스트에 최적화되어 있습니다. 이러한 차이 덕분에 Playwright는 Vitest를 보완하는 이상적인 도구입니다.

일반적인 구성은 단위 및 컴포넌트 테스트(비즈니스 로직, 유틸리티, hooks, UI 컴포넌트 테스트)는 Vitest로, 핵심 사용자 경로와 브라우저 간 호환성을 검증하는 엔드투엔드 테스트는 Playwright로 수행하는 방식입니다. 이 조합은 개발 중에는 Vitest로 빠른 피드백을 제공하면서, 실제 브라우저에서는 Playwright로 애플리케이션 전체가 올바르게 동작함을 보장합니다.

Vitest는 최근 실제 브라우저에서 테스트를 실행하는 [browser mode](https://vitest.dev/guide/browser)를 도입했습니다. 다만 아키텍처 차이가 있습니다. Playwright 컴포넌트 테스트는 Node.js 프로세스에서 실행되며 브라우저를 원격 제어합니다. Vitest의 browser mode는 브라우저에서 테스트를 네이티브로 실행해 Vitest의 테스트 러너 및 개발자 경험과의 일관성을 유지하지만, 일부 [limitations](https://vitest.dev/guide/browser/#limitations)이 있습니다.
