---
title: '디자인 원칙'
description: '이 페이지는 이 기반으로 삼고 있는 디자인 원칙을 깊이 있게 설명합니다.'
---

원문 URL: https://next-intl.dev/docs/design-principles

[문서](https://next-intl.dev/docs/getting-started "Docs")디자인 원칙

# 디자인 원칙

이 페이지는 `next-intl`이 기반으로 삼고 있는 디자인 원칙을 깊이 있게 설명합니다.

프로젝트에서 라이브러리를 효과적으로 사용하기 위해 이 페이지를 반드시 읽어야 하는 것은 아니지만, 라이브러리의 철학을 더 잘 이해하는 데 도움이 되며 `next-intl`이 프로젝트에 잘 맞는지 평가하는 데도 도움이 됩니다.

또한 이 페이지는 앞으로 `next-intl`에서 기대할 수 있는 개선 사항을 투명하게 참고할 수 있도록, 계획된 개선 항목으로 연결되는 링크를 제공합니다.

## 총체적 접근[](https://next-intl.dev/docs/design-principles#holistic)

국제화는 분명 코드베이스에 유연성을 요구합니다. 하지만 단일 언어를 제대로 구현하는 것만으로도 이미 쉽지 않은 과제일 수 있습니다.

**동적 텍스트 레이블**을 사용하는 것은 국제화에서 가장 눈에 띄는 요소이지만, 언어를 잘 지원하려면 그 외에도 많은 측면이 포함됩니다.

  1. **복수형 규칙**: 영어처럼 복수형이 두 가지(단수/복수)뿐인 언어가 있는 반면, 어떤 언어는 최대 여섯 가지 형태를 가집니다.
  2. **날짜 및 시간 형식**: 언어마다 날짜와 시간을 표기하는 관례가 다릅니다. 표시되는 연도조차 국가별로 다를 수 있습니다. 예를 들어 태국은 그레고리력보다 543년 앞선 불교력을 사용합니다.
  3. **숫자 형식**: 숫자 표기 규칙도 언어마다 다릅니다. 예를 들어 영어와 독일어를 비교하면 천 단위 구분자와 소수점 구분자가 서로 반대입니다.
  4. **목록 형식**: “HTML, CSS, and JavaScript” 같은 목록을 형식화하는 일은 단순히 문자열을 올바른 순서로 조합하는 문제가 아니라, 언어별 접속사와 문장 부호를 올바르게 사용하는 문제이기도 합니다.
  5. **텍스트 방향**: 대부분의 언어는 왼쪽에서 오른쪽으로 쓰지만, 아랍어 같은 일부 언어는 오른쪽에서 왼쪽으로 쓰며 레이아웃도 거울처럼 반전되어야 합니다.

여기에 더해 일반적인 앱 문제도 있습니다.

  1. **리치 텍스트 형식**: 많은 앱은 어떤 형태로든 리치 텍스트를 지원해야 합니다. 예를 들어 텍스트 레이블에 링크를 삽입하는 경우(“자세한 내용은 [리치 텍스트 문서](https://next-intl.dev/docs/usage/translations#rich-text)를 참고하세요.”)가 있습니다.
  2. **시간대**: 날짜를 표시하려면 서버와 클라이언트 전반에서 시간대를 일관되게 처리해야 하며, 경우에 따라 사용자 선호에 맞춰 커스터마이징해야 합니다.
  3. **상대 시간 형식**: “5분 전”, “2시간 후” 같은 상대 시간을 표시하려면 올바른 형식을 위해 특별한 주의가 필요하고, 현재 시간을 위한 일관된 기준값도 필요합니다. 경우에 따라 표시 시간을 주기적으로 갱신하는 메커니즘도 필요합니다.
  4. **로컬라이즈된 URL**: URL은 사용자의 언어 선호에 맞게 로컬라이즈되어야 합니다(예: 영어는 `/en/about-us`, 스페인어는 `/es/sobre-nosotros`). 구현 관점에서는 들어오는 요청을 올바른 페이지에 매핑하고, 개발자가 로케일에 구애받지 않는 방식으로 페이지 간 링크를 연결할 수 있도록 간결한 API를 제공해야 합니다.
  5. **언어 협상**: 사용자의 언어 선호는 브라우저 설정을 기반으로 감지되어야 하며, 로그인하지 않은 사용자라도 수동으로 설정할 수 있어야 합니다.
  6. **SEO**: 검색 엔진이 사용자에게 가장 적합한 콘텐츠를 보여주려면 [페이지의 로컬라이즈된 버전](https://developers.google.com/search/docs/specialty/international/localized-versions)에 대한 정보를 제공해야 합니다.
  7. **국가별 특성**: 여러 국가에서 서비스나 상품을 제공한다면, 통화나 측정 단위 같은 국가별 요소를 고려해야 할 수 있습니다.
  8. **환경 차이**: 컴포넌트는 서버, 클라이언트 또는 둘 다에서 실행될 수 있습니다. 서로 다른 환경에서 [일관된 렌더링](https://next-intl.dev/blog/date-formatting-nextjs)을 달성하려면, 사용자 로케일, 시간대, 현재 시간 기준값 같은 속성에 앱 전체가 통합된 방식으로 접근할 수 있어야 합니다.

이 목록을 보면 문제 영역이 얼마나 크고, 국제화의 여러 요소가 얼마나 긴밀하게 연결되어 있는지 분명해집니다.

`next-intl`은 국제화에 대해 총체적인 접근 방식을 취하며, 언어와 국가별 관례를 처리할 때 모범 사례를 따르도록 자연스럽게 유도합니다. 이를 통해 앱을 차별화하는 핵심에 더 많은 시간을 집중할 수 있습니다.

→ [계획된 개선 사항](https://github.com/amannn/next-intl/labels/area%3A%20routing)

## 사용성 중심[](https://next-intl.dev/docs/design-principles#ergonomic)

이 라이브러리의 과감한 주장은 국제화를 구현할수록 앱 코드가 복잡해지는 것이 아니라 더 단순해진다는 점입니다.

국제화가 포함하는 [총체적 그림](https://next-intl.dev/docs/design-principles#holistic)을 고려하면, 컴포넌트 대부분이 어떤 형태로든 국제화와 관련된다는 점은 분명합니다. 그래서 `next-intl`은 개발자가 생산성과 통제감을 느낄 수 있도록 편리한 API를 제공하는 것을 우선순위로 둡니다. 개발자는 실질적인 문제 해결에만 집중하면 되고, 국제화는 그 과정에 자연스럽게 통합되어야 합니다.

국제화 설정이 끝나면, 새 언어 추가는 가장 단순한 경우 번역이 담긴 새 JSON 파일 하나를 추가하는 일로 끝납니다. 나머지는 `next-intl`이 처리합니다.

→ [계획된 개선 사항](https://github.com/amannn/next-intl/labels/area%3A%20ergonomics)

## 표준 기반[](https://next-intl.dev/docs/design-principles#standards-based)

[ECMAScript Internationalization API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)가 도입되면서, 최근 몇 년간 JavaScript는 날짜, 시간, 숫자, 목록, 복수형 형식화 측면에서 매우 강력해졌습니다. `next-intl`은 이 API 위에서 동작하며, 앱별 설정과 요구사항을 고려해 이러한 기능을 다룰 수 있는 사용성 높은 인터페이스를 제공합니다.

텍스트 형식화에서 `next-intl`은 [International Components for Unicode (ICU)](https://unicode-org.github.io/icu/userguide/format_parse/)를 기반으로 합니다. ICU는 많은 프로그래밍 언어와 프레임워크에서 지원되는, 성숙하고 널리 사용되는 국제화 표준입니다. `next-intl`은 텍스트 레이블 정의에 ICU 메시지 문법을 사용하며, 이를 통해 변수 보간이나 복수형 같은 복잡한 형식 요구사항도 간결하고 읽기 쉬운 방식으로 표현할 수 있습니다. 번역가 같은 비개발자에게도 마찬가지입니다.

`next-intl`은 표준을 기반으로 하므로 국제화 코드의 미래 대응력을 높이고, 이미 국제화 경험이 있는 개발자에게 익숙한 사용감을 제공합니다. 또한 표준에 의존하기 때문에 [Crowdin](https://crowdin.com/) 같은 번역 관리 시스템과도 잘 통합됩니다.

`next-intl`은 메시지에 구조를 제공하기 위해 [중첩 스타일](https://next-intl.dev/docs/usage/translations#structuring-messages)을 사용하며, 중복 없이 메시지 계층을 표현할 수 있습니다. 하나의 스타일만 지원함으로써 [메시지 타입 안전성](https://next-intl.dev/docs/workflows/typescript#messages)처럼 이러한 가정에 의존하는 고급 기능을 제공할 수 있습니다. 다른 스타일을 사용 중이라면 중첩 스타일로 마이그레이션을 고려할 수 있습니다([메시지 구조화 문서](https://next-intl.dev/docs/usage/translations#structuring-messages)의 “Can I use a different style for structuring my messages?” 참고).

표준은 변할 수 있으므로, `next-intl`도 ECMAScript 표준의 최신 발전 사항(예: [`Temporal`](https://tc39.es/proposal-temporal/docs/) 및 [`Intl.MessageFormat`](https://github.com/tc39/proposal-intl-messageformat))을 따라갈 것으로 기대됩니다.

→ [계획된 개선 사항](https://github.com/amannn/next-intl/labels/area%3A%20standards)

## 호환성[](https://next-intl.dev/docs/design-principles#compatible)

`next-intl`은 국제화를 [총체적인 방식](https://next-intl.dev/docs/design-principles#holistic)으로 다루도록 설계되었지만, 국제화에는 다른 도구와 서비스와의 통합이 필요할 수 있다는 점을 고려하는 것이 중요합니다. 이렇게 해야 목적에 맞는 최적의 도구를 사용할 수 있고, 비개발자와의 협업도 가능해집니다.

일반적인 앱은 다음 통합 중 일부를 필요로 합니다.

**번역 관리 시스템 (TMS)**

보통 번역을 관리하고 [번역가와 협업](https://next-intl.dev/docs/workflows/localization-management)하기 위해 사용됩니다. [Crowdin](https://crowdin.com/) 같은 서비스는 번역가가 웹 기반 인터페이스에서 작업할 수 있도록 폭넓은 기능을 제공하며, 앱과 번역을 동기화하는 다양한 메커니즘도 제공합니다.

`next-intl`은 텍스트 레이블 정의에 ICU 메시지 문법을 사용하므로 이러한 서비스와 잘 통합됩니다. ICU는 널리 지원되는 표준입니다. 권장되는 메시지 저장 방식은 로케일별로 구조화된 JSON 파일이며, 이는 TMS로 가져오기 쉬운 대중적인 형식입니다. 기본 로케일 메시지는 최소한 로컬에 두는 것이 권장되지만(예: [타입 안전 메시지](https://next-intl.dev/docs/workflows/typescript#messages)), CDN 등 TMS가 제공하는 경로에서 메시지를 동적으로 로드할 수도 있습니다.

**콘텐츠 관리 시스템 (CMS)**

앱이 CMS 콘텐츠를 사용한다면 `next-intl`과 함께 사용할 수 있습니다. 예를 들어 블로그 게시물이나 마케팅 카피는 CMS에서 관리하고, UI 레이블은 `next-intl`에서 관리할 수 있습니다.

CMS는 보통 여러 언어의 콘텐츠를 정의하고 REST API를 통해 가져오는 방법을 제공합니다. `next-intl`이 [`getLocale`](https://next-intl.dev/docs/environments/server-client-components#async-components)로 반환하는 협상된 앱 로케일을 CMS API 요청에 전달하면, 사용자 선호 언어의 콘텐츠를 가져올 수 있습니다.

**백엔드 데이터**

CMS와 비슷하게, 백엔드 서비스나 데이터베이스에 있는 데이터도 사용자 언어와 국가를 기준으로 조회해야 할 수 있습니다. 예를 들어 국가별로 다른 가격과 통화를 보여주거나, 로컬라이즈된 상품명을 보여줘야 할 수 있습니다. 백엔드 요청에 `next-intl`의 협상된 앱 로케일을 사용하면, 로컬라이제이션이 앱의 모든 영역에 반영되도록 할 수 있습니다.

**기타 라이브러리**

Next.js에는 인증 처리 등 `next-intl`과 함께 사용할 수 있는 풍부한 라이브러리 생태계가 있습니다. `next-intl`은 [일반적인 통합](https://next-intl.dev/docs/routing/middleware#composing-other-middlewares)에 대한 문서와 예제를 제공함으로써, 다른 라이브러리와 통합할 때 마찰 없는 경험을 보장합니다.

→ [계획된 개선 사항](https://github.com/amannn/next-intl/labels/area%3A%20integrations)

## 성능 집착[](https://next-intl.dev/docs/design-principles#performance-obsessed)

`next-intl`은 빠르고 안정적인 사용자 경험을 제공해야 하는 고트래픽 사이트를 염두에 두고 설계되었으며, 복잡한 전자상거래 페이지에서도 뛰어난 Core Web Vitals를 달성하며 작동이 입증되었습니다.

이를 위해 현재 `next-intl`은 주로 다음 기법에 의존합니다.

  1. **RSC-first**: React Server Components와 깊게 통합하여 빌드 단계나 성능이 충분한 서버로 작업을 오프로드할 수 있으므로, 클라이언트 측 앱의 런타임 부담을 줄일 수 있습니다.
  2. **메시지 분할**: 메시지를 로케일별로, 선택적으로는 서버/클라이언트/컴포넌트별로 분할해 클라이언트로 전송되는 메시지 양을 줄일 수 있습니다. 이는 많은 언어를 지원하고 메시지 양이 큰 앱에서 특히 중요합니다.

3. **캐싱** : 메시지 파싱과 [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) 생성자 인스턴스화는 앱 전반에서 캐시되므로, 필요한 연산량이 줄어듭니다.
  4. **단축 경로** : 반복 작업의 결과를 캐시하는 것보다 더 좋은 것은 애초에 그 작업을 하지 않는 것입니다(예: 파싱이 필요 없는 일반 메시지를 감지).

→ [계획된 개선 사항](https://github.com/amannn/next-intl/labels/area%3A%20performance)

## Next.js 우선[](https://next-intl.dev/docs/design-principles#nextjs-first)

Next.js는 다양한 기능을 제공하지만, 동시에 신뢰할 수 있는 국제화 통합을 위해 신중하게 처리해야 할 요소도 여럿 있습니다. 이름에서 알 수 있듯이 `next-intl`은 Next.js와 잘 동작하도록 주로 설계되었습니다. 모든 경우를 포괄하는 만능 솔루션을 지향하기보다, 필요한 만큼 Next.js와 깊이 통합하고 Next.js 생태계의 최신 발전을 따라가는 것을 우선순위로 둡니다.

다만 `next-intl`에는 Next.js에 종속되지 않는 코어가 있으며, 이는 모든 React 앱이나 일반 JavaScript에서도 사용할 수 있습니다: [`use-intl`](https://next-intl.dev/docs/environments/core-library). 이 코어 라이브러리에는 `next-intl`의 대부분 기능이 포함되어 있지만, 라우팅 API 같은 Next.js 전용 통합은 빠져 있습니다. 이 라이브러리의 목표는 스택의 다른 영역(예: React Native)에서도 익숙한 API를 사용할 수 있게 하고, 언젠가 Next.js가 프로젝트에 더 이상 적합하지 않다고 느껴질 경우에도 간단한 [마이그레이션 경로](https://next-intl.dev/docs/design-principles#migration-friendly)를 제공하는 것입니다.

## 마이그레이션 친화적[](https://next-intl.dev/docs/design-principles#migration-friendly)

우리 모두 겪어봤듯 기술은 계속 바뀌고, 때로는 우리도 함께 옮겨가야 합니다. `next-intl`은 코드베이스에서 좋은 구성원으로 동작하도록, 그리고 필요해질 경우 스택의 특정 부분에서 벗어나 마이그레이션할 수 있도록 설계되었습니다.

언젠가 Next.js나 `next-intl`이 더 이상 프로젝트에 맞지 않는다고 느껴진다면, 여기에는 여러 선택지가 있습니다:

  1. **Next.js에서 벗어나기** : Next.js에서 마이그레이션하기로 결정하더라도, 모든 React 앱에서 코어 라이브러리 [`use-intl`](https://next-intl.dev/docs/environments/core-library)을 계속 사용할 수 있습니다. 예를 들어 React Router 앱에서도 기존 컴포넌트를 재사용할 수 있습니다.
  2. **`next-intl`에서 벗어나기**: `next-intl`이 더 이상 요구사항에 맞지 않는다면 라이브러리를 참조하는 앱 코드를 조정해야 하지만, [표준 기반](https://next-intl.dev/docs/design-principles#standards-based) ICU 메시지는 그대로 재사용할 수 있고, 포맷팅 API는 [ECMAScript Internationalization API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)를 직접 호출하는 방식 등으로 대체할 수 있습니다.

억지로 붙잡지는 않겠습니다. 원한다면 계속 좋은 관계로 지낼 수 있고요.

그렇더라도, 우리는 `next-intl`이 여러분의 프로젝트에 훌륭하게 맞도록 최선을 다하고 있습니다. 기대한 대로 동작하지 않는 부분이 있거나 개선 아이디어가 있다면 [issue tracker](https://github.com/amannn/next-intl/issues)에 알려 주세요. 최선을 다해 도와드리겠습니다.

* * *

와, 꽤 긴 글이었네요. 정말 끝까지 다 읽으셨나요? `next-intl`은 국제화에 대한 큰 호기심과 열정에서 시작되었습니다. 우리 통하는 것 같네요! `next-intl`이 여러분에게 어떻게 도움이 되고 있는지 항상 궁금합니다. 피드백이나 질문이 있다면 언제든 [문의해 주세요](https://github.com/amannn/next-intl/discussions)!

[메시지 검증](https://next-intl.dev/docs/workflows/messages "메시지 검증")

