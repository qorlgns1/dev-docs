---
title: "includeTaskLocation"
description: "Vitest API가 reporters에서 task를 받을 때  속성을 포함할지 여부를 설정합니다. 테스트가 매우 많은 경우, 성능이 소폭 저하될 수 있습니다."
---

출처 URL: https://vitest.dev/config/includetasklocation

# includeTaskLocation

- **Type:** `boolean`
- **Default:** `false`

Vitest API가 [reporters](#reporters)에서 task를 받을 때 `location` 속성을 포함할지 여부를 설정합니다. 테스트가 매우 많은 경우, 성능이 소폭 저하될 수 있습니다.

`location` 속성에는 원본 파일에서 `test` 또는 `describe` 위치에 해당하는 `column` 및 `line` 값이 포함됩니다.

이 옵션은 명시적으로 비활성화하지 않은 상태에서 다음과 같이 Vitest를 실행하면 자동으로 활성화됩니다:

- Vitest UI
- 또는 [headless](https://vitest.dev/guide/browser/#headless) 모드 없이 [Browser Mode](https://vitest.dev/guide/browser/)를 사용하는 경우
- 또는 [HTML Reporter](https://vitest.dev/guide/reporters#html-reporter)를 사용하는 경우

::: tip
이 옵션에 의존하는 커스텀 코드를 사용하지 않으면 아무런 효과가 없습니다.
:::
