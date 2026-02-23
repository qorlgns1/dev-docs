---
title: 'index'
---

**번역**
- `zod/v4` 패키지는 Zod 에코시스템의 “플래그십” 라이브러리입니다. 대부분의 애플리케이션에 이상적인 개발자 경험과 번들 크기 간의 균형을 맞춥니다.
- 번들 크기에 대해 매우 엄격한 제약이 있다면 [Zod Mini](https://zod.dev/packages/mini)를 고려하세요.
- Zod는 TypeScript 타입 시스템과 일대일로 매핑되는 스키마 API를 제공하는 것을 목표로 합니다.

- API는 복잡한 타입을 정의할 때 간결하고 체이닝 가능하며 자동완성에 친화적인 방법을 제공하기 위해 메서드에 의존합니다.

- 모든 스키마는 `z.ZodType` 베이스 클래스를 확장하며, 이는 [`zod/v4/core`](https://zod.dev/packages/core)의 `z.$ZodType`를 확장합니다. 모든 `ZodType` 인스턴스는 다음 메서드를 구현합니다:

