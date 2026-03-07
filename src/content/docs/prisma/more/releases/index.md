---
title: "ORM 릴리스 및 성숙도 수준"
description: "Prisma ORM 구성 요소의 릴리스 프로세스, 버전 관리, 성숙도와 릴리스 전반에서 발생할 수 있는 호환성 깨짐 변경에 대응하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/more/releases

# ORM 릴리스 및 성숙도 수준

Prisma ORM 구성 요소의 릴리스 프로세스, 버전 관리, 성숙도와 릴리스 전반에서 발생할 수 있는 호환성 깨짐 변경에 대응하는 방법을 알아보세요.

이 페이지에서는 Prisma ORM의 릴리스 프로세스, 버전 관리 방식, 그리고 릴리스 전반에서 발생할 수 있는 호환성 깨짐 변경에 대응하는 방법을 설명합니다.

## 릴리스

Prisma ORM 릴리스는 일반적으로 2주마다 이루어집니다. 다만 이는 _엄격한 규칙_ 은 아니며, 내부 사정으로 릴리스가 연기될 수 있습니다.

[GitHub에서 모든 릴리스 노트 확인하기](https://github.com/prisma/prisma/releases).

## 제품 성숙도 수준

하나의 릴리스에는 서로 다른 성숙도 수준의 제품 또는 기능이 포함될 수 있습니다. 성숙도 수준은 제품 또는 기능의 완성도와, 호환성 깨짐 변경 측면에서 사용자가 기대할 수 있는 바를 나타냅니다.

> **참고** : 버전 [2.13.0](https://github.com/prisma/prisma/releases/2.13.0)부터 'Experimental'은 더 이상 제품 성숙도 단계에 포함되지 않습니다.

- 얼리 액세스

기능 또는 제품이 **Early Access** 인 경우:

- 저희는 문제를 검증했고 그에 대한 해결책을 검토하고 있지만, 해당 해결책이 완전한지 또는 완벽하게 적합한지는 아직 확신하지 못합니다.
- 더 많은 피드백을 수집하고 필요에 따라 해결책을 조정하고자 하며, 사용자는 큰 폭의 호환성 깨짐 변경이 있을 수 있음을 감수합니다.

Early Access 기능이나 제품을 프로덕션에서 사용하는 것은 권장하지 않습니다.

- 프리뷰

기능 또는 제품이 **Preview** 인 경우:

- 해당 기능 또는 제품의 방향성과 표면(API 범위)을 검증했습니다.
- 릴리스 노트 및 문서에서 별도로 명시되지 않는 한, 사용자는 해당 기능/제품과 관련 API가 대부분 안정적이라고 기대할 수 있습니다.
- 치명적으로 알려진 문제는 없지만, 경미한 버그는 존재할 수 있습니다.
- 가능한 한 빠르게 안정화하기 위해 피드백을 환영합니다.

Preview는 일반적으로 기능 플래그 뒤에서 제공되거나 어떤 형태로든 옵트인이 필요합니다(예: CLI에 `--preview-feature` 플래그 제공, 또는 Prisma 스키마에서 Prisma Client용 [adding them to a `previewFeatures` property in the `generator` block](https://docs.prisma.io/docs/orm/reference/preview-features/cli-preview-features)).

Preview 기능이나 제품을 프로덕션에서 사용하는 것은 권장하지 않습니다.

참고: [현재 사용 가능한 모든 Preview 기능](https://docs.prisma.io/docs/orm/reference/preview-features/client-preview-features).

- 정식 출시(GA)

기능 또는 제품이 **Generally Available** 인 경우:

- 해당 솔루션은 일정 기간 테스트되었고, 안정적이며 프로덕션 사용 준비가 되었다고 판단할 만큼 충분한 피드백을 받았습니다.
- 99%의 경우 버그가 없어야 합니다(완전히 버그가 없는 소프트웨어는 보장할 수 없습니다).

## 버전 관리

Prisma ORM의 릴리스 체계는 버전 `3.x.x`부터 시맨틱 버전 관리([SemVer](https://semver.org/))를 따릅니다.

- Prisma ORM과 시맨틱 버전 관리(SemVer)

#

- SemVer 버전 관리는 어떻게 동작하나요?

시맨틱 버전 관리(SemVer)는 버전 업그레이드에 대해 다음 규칙을 사용합니다([SemVer](https://semver.org/) 명세에서 인용):

_버전 번호`MAJOR.MINOR.PATCH`가 주어졌을 때, 다음을 증가시킵니다:_

1. _호환되지 않는 API 변경을 할 때 `MAJOR` 버전,_
2. _하위 호환되는 방식으로 기능을 추가할 때 `MINOR` 버전,_
3. _하위 호환되는 버그 수정을 할 때 `PATCH` 버전._

#

- Prisma ORM 버전 관리는 SemVer를 어떻게 따르나요?

버전 `3.x.x`부터 Prisma ORM은 [SemVer](https://semver.org/) 버전 관리 체계를 엄격히 따릅니다.

다음은 Prisma ORM이 SemVer를 따르는 방식에 대한 간략한 개요입니다:

- 안정된 표면(즉, [General Availability](https://docs.prisma.io/docs/orm/more/releases#generally-available-ga))에서의 호환성 깨짐 변경은 새로운 `MAJOR` 릴리스에서만 도입됩니다.
- 호환성 깨짐 변경은 여전히 `MINOR`에서 출시될 수 있지만, 기본적으로 활성화되지 않은 옵트인 Preview 및 Early Access 기능에 한정됩니다(예: Preview 기능 플래그, 특정 옵트인 옵션, 또는 새로운 CLI 명령을 통해).
- `MINOR`에서 릴리스된 옵트인 호환성 깨짐 변경(즉, Preview 및 Early Access)은 새로운 `MAJOR` 릴리스에서만 General Availability(옵트인 불필요)로 승격됩니다.

버전 번호 `MAJOR.MINOR.PATCH`가 주어졌을 때, Prisma ORM의 버전 번호는 다음과 같이 증가합니다:

1. `MAJOR` 버전: **호환성 깨짐 변경이 포함된** 주요 제품 업데이트가 General Availability로 릴리스될 때 증가합니다.
2. `MINOR` 버전: 하위 호환되는 새 기능을 추가하는 제품 업데이트가 릴리스될 때 증가합니다. 호환성 깨짐 변경이 있는 기능은 **opt-in** 인 경우에만 도입될 수 있으며, 즉 Early Access와 Preview에 해당합니다.
3. `PATCH` 버전: 기능 버그가 수정될 때 증가하며, 항상 **하위 호환** 됩니다.

> **참고:** 버전 `2.28.0`까지 Prisma ORM은 SemVer 버전 관리를 엄격하게 따르지 않았습니다. 즉, `2.MINOR.PATCH` 범위의 릴리스에서 `MINOR` 버전에 호환성 깨짐 변경이 포함될 수 있었습니다. Prisma ORM의 SemVer 도입에 대해 더 알아보려면 [블로그 게시물](https://www.prisma.io/blog/prisma-adopts-semver-strictly)을 확인하세요.
