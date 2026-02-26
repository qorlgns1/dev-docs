---
title: '리플레이 이슈 | Next.js용 Sentry'
description: 'Project Settings > Replay로 이동해 각 이슈 유형의 감지를 on/off로 전환하여 어떤 이슈 유형을 생성할지 구성할 수 있습니다. 기본값은 모든 이슈 유형이 활성화되어 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/issue-types

# 리플레이 이슈 | Next.js용 Sentry

*[리플레이 이슈](https://docs.sentry.io/product/issues/issue-details/replay-issues.md)*는 캡처된 Session Replay 데이터를 사용해 감지된 이슈입니다. 애플리케이션이 [Session Replay](https://docs.sentry.io/product/session-replay.md)로 구성되어 있다면, 리플레이 수집 과정에서 서버 측에서 문제가 감지되고 이슈로 그룹화됩니다. Sentry는 fingerprint를 기준으로 유사한 이벤트를 이슈로 묶습니다. 리플레이 이슈의 경우 fingerprint는 주로 문제 유형과 문제가 발생한 url 또는 transaction name을 기반으로 합니다.

Project Settings > Replay로 이동해 각 이슈 유형의 감지를 on/off로 전환하여 어떤 이슈 유형을 생성할지 구성할 수 있습니다. 기본값은 모든 이슈 유형이 활성화되어 있습니다.

## [Rage Click 이슈 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/issue-types.md#configuring-rage-click-issues)

"Dead clicks"(또는 "slow clicks")는 7초 이내에 DOM 업데이트나 페이지 스크롤로 이어지지 않는 `<button>`, `<input>`, `<a>` 요소에서만 감지됩니다. 사용자가 이 7초 시간대 안에 이러한 요소 중 하나를 3번 이상 클릭하면 좌절 신호로 간주되며, SDK는 ["rage click"](https://docs.sentry.io/product/issues/issue-details/replay-issues/rage-clicks.md)을 등록합니다.

때때로 "Print" 또는 "Download" 버튼처럼 DOM 변경이 예상되지 않는 요소에서도 rage click 또는 dead click이 감지될 수 있습니다. 이 경우 `slowClickIgnoreSelectors`를 구성하면 해당 버튼들이 새 이슈를 생성하지 않도록 할 수 있습니다.

**rage click 이슈**를 보려면 SDK 버전 7.60.1 이상이 필요합니다.

## [Hydration Error 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay/issue-types.md#configuring-hydration-errors)

React 앱에서 [hydration error](https://docs.sentry.io/product/issues/issue-details/replay-issues/hydration-error.md)가 발생하면 SDK는 hydration 문제에 대한 데이터를 담은 error object와 replay breadcrumb를 모두 전송합니다. 이 두 데이터는 모두 처리 목적으로 서버로 전송됩니다. 이슈 스트림에서는 Hydration Error 이슈를 보게 되며, 이는 두 데이터 소스 중 어느 쪽에서든 생성될 수 있습니다. 다만 디버깅을 더 쉽게 해주는 diff 도구는 리플레이가 해당 에러와 연결된 경우에만 표시됩니다.

이 때문에 [Inbound Filter](https://docs.sentry.io/concepts/data-management/filtering.md)와 "Create Hydration Error Issues" Replay 설정을 모두 활성화하는 것을 권장합니다. 이것이 기본값이기도 합니다.

기본 설정은 다음 네 가지 방식 중 하나로 구성될 수 있습니다:

| Inbound Filters | Replay Hydration Error toggle | 결과                                                                            |
| --------------- | ----------------------------- | ------------------------------------------------------------------------------- |
| enabled         | enabled                       | (권장) 리플레이 데이터를 기반으로 이슈가 생성됩니다.                            |
| enabled         | disabled                      | 이슈가 생성되지 않습니다.                                                       |
| disabled        | enabled                       | 리플레이 데이터와 에러 데이터에서 각각 이슈가 생성되어, 중복 이슈 2개가 생성됩니다. |
| disabled        | disabled                      | 캡처된 에러 데이터를 기반으로 이슈가 생성됩니다.                                |

리플레이 데이터에서 **hydration error 이슈**를 감지하려면 SDK 버전 7.87.0 이상이 필요합니다.

