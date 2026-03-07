---
title: "왜 Vitest인가"
description: "이 가이드는 여러분이 Vite에 익숙하다고 가정합니다. 더 알아보는 좋은 방법은 Why Vite Guide와 Next generation frontend tooling with ViteJS를 보는 것입니다. 이 스트림에서 Evan You가 핵심 개념을 설명하는 데모를 ..."
---

출처 URL: https://vitest.dev/guide/why

# 왜 Vitest인가

:::tip 참고
이 가이드는 여러분이 Vite에 익숙하다고 가정합니다. 더 알아보는 좋은 방법은 [Why Vite Guide](https://vitejs.dev/guide/why.html)와 [Next generation frontend tooling with ViteJS](https://www.youtube.com/watch?v=UJypSr8IhKY)를 보는 것입니다. 이 스트림에서 [Evan You](https://bsky.app/profile/evanyou.me)가 핵심 개념을 설명하는 데모를 진행했습니다.
:::

## Vite 네이티브 테스트 러너의 필요성

Vite는 일반적인 웹 패턴에 대한 기본 지원, glob import 및 SSR primitive 같은 기능, 그리고 다양한 플러그인 및 통합을 바탕으로 활발한 생태계를 만들어 가고 있습니다. 개발 및 빌드 경험은 Vite 성공의 핵심입니다. 문서화 영역에서도 Vite 기반의 여러 SSG 대안이 존재합니다. 하지만 Vite의 Unit Testing 경험은 그동안 명확하지 않았습니다. [Jest](https://jestjs.io/) 같은 기존 옵션은 다른 맥락에서 만들어졌습니다. Jest와 Vite 사이에는 중복되는 부분이 많아, 사용자가 서로 다른 두 파이프라인을 설정해야 했습니다.

테스트 중 파일 변환에 Vite dev server를 사용하면, 소스 파일 변환의 복잡성을 처리할 필요 없이 테스트 중 최고의 DX 제공에만 집중하는 단순한 러너를 만들 수 있습니다. 앱의 동일한 설정(`vite.config.js`)을 사용하는 테스트 러너로, 개발·빌드·테스트 전반에서 공통 변환 파이프라인을 공유할 수 있습니다. 또한 동일한 plugin API로 확장 가능하여, 여러분과 도구 유지보수자가 Vite와의 일급 통합을 제공할 수 있습니다. 처음부터 Vite를 염두에 두고 만들어져 즉각적인 Hot Module Reload (HMR) 같은 DX 개선을 적극 활용하는 도구. 이것이 바로 Vite로 구동되는 차세대 테스트 프레임워크 Vitest입니다.

Jest가 대규모로 채택되어 있다는 점을 고려해, Vitest는 대부분의 프로젝트에서 바로 교체해 사용할 수 있도록 호환 API를 제공합니다. 또한 unit test 설정 시 일반적으로 필요한 기능(mocking, snapshots, coverage)도 포함합니다. Vitest는 성능을 매우 중요하게 생각하며 Worker thread를 사용해 가능한 한 많은 작업을 병렬로 실행합니다. 일부 포팅 사례에서는 테스트 실행 속도가 한 자릿수 배수 이상 빨라지기도 했습니다. Watch mode는 기본으로 활성화되어 있으며, 이는 Vite가 지향하는 dev-first 경험과도 일치합니다. 이러한 DX 개선에도 불구하고 Vitest는 의존성을 신중히 선택하거나(또는 필요한 부분을 직접 인라인하여) 경량성을 유지합니다.

**Vitest는 Vite 프로젝트에서 가장 먼저 선택되는 Test Runner가 되는 것을 목표로 하며, Vite를 사용하지 않는 프로젝트에도 견고한 대안이 되고자 합니다.**

계속해서 [Getting Started Guide](https://vitest.dev/guide/index)를 읽어보세요.

## Vitest는 X와 어떻게 다른가?

Vitest가 다른 유사 도구와 어떻게 다른지에 대한 자세한 내용은 [Comparisons](https://vitest.dev/guide/comparisons) 섹션에서 확인할 수 있습니다.
