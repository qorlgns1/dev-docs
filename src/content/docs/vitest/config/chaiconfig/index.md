---
title: "chaiConfig"
description: "Assertion 오류 메시지에 스택 트레이스를 포함할지 여부에 영향을 줍니다. 기본값 는 오류 메시지에서 스택 트레이스를 숨깁니다."
---

출처 URL: https://vitest.dev/config/chaiconfig

# chaiConfig

- **유형:** `{ includeStack?, showDiff?, truncateThreshold? }`
- **기본값:** `{ includeStack: false, showDiff: true, truncateThreshold: 40 }`

[Chai config](https://github.com/chaijs/chai/blob/4.x.x/lib/chai/config.js)와 동일합니다.

## chaiConfig.includeStack

- **유형:** `boolean`
- **기본값:** `false`

Assertion 오류 메시지에 스택 트레이스를 포함할지 여부에 영향을 줍니다. 기본값 `false`는 오류 메시지에서 스택 트레이스를 숨깁니다.

## chaiConfig.showDiff

- **유형:** `boolean`
- **기본값:** `true`

던져진 AssertionErrors에 `showDiff` 플래그를 포함할지 여부에 영향을 줍니다. `false`는 항상 `false`이고, `true`는 단언에서 diff 표시를 요청한 경우 `true`가 됩니다.

## chaiConfig.truncateThreshold

- **유형:** `number`
- **기본값:** `40`

Assertion 오류에서 actual 및 expected 값의 길이 임계값을 설정합니다. 이 임계값을 초과하면(예: 큰 데이터 구조), 값은 `[ Array(3) ]` 또는 `{ Object (prop1, prop2) }` 같은 형태로 대체됩니다. 잘라내기를 완전히 비활성화하려면 `0`으로 설정하세요.

이 구성 옵션은 `test.each` 제목과 assertion 오류 메시지 내부 값의 잘라내기에 영향을 줍니다.
