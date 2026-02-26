---
title: "자동 대기"
description: "Playwright는 액션을 수행하기 전에 요소에 대해 다양한 실행 가능성 검사를 수행하여 액션이 예상대로 동작하도록 보장합니다. 관련된 모든 검사가 통과될 때까지 자동으로 대기한 뒤에만 요청된 액션을 수행합니다. 주어진  내에 필요한 검사가 통과하지 않으면 액션은 와..."
---

Source URL: https://playwright.dev/docs/actionability

# 자동 대기 | Playwright

## 소개[​](https://playwright.dev/docs/actionability#introduction "소개로 바로 가기")

Playwright는 액션을 수행하기 전에 요소에 대해 다양한 실행 가능성 검사를 수행하여 액션이 예상대로 동작하도록 보장합니다. 관련된 모든 검사가 통과될 때까지 자동으로 대기한 뒤에만 요청된 액션을 수행합니다. 주어진 `timeout` 내에 필요한 검사가 통과하지 않으면 액션은 `TimeoutError`와 함께 실패합니다.

예를 들어 [locator.click()](https://playwright.dev/docs/api/class-locator#locator-click)의 경우, Playwright는 다음을 보장합니다.

- locator가 정확히 하나의 요소로 해석됨
- 요소가 [Visible](https://playwright.dev/docs/actionability#visible "Visible") 상태임
- 요소가 [Stable](https://playwright.dev/docs/actionability#stable "Stable") 상태임 (즉, 애니메이션 중이 아니거나 애니메이션이 완료됨)
- 요소가 [Receives Events](https://playwright.dev/docs/actionability#receives-events "Receives Events") 상태임 (즉, 다른 요소에 가려지지 않음)
- 요소가 [Enabled](https://playwright.dev/docs/actionability#enabled "Enabled") 상태임

다음은 각 액션에서 수행되는 실행 가능성 검사 전체 목록입니다.

| Action                                                                                                               | [Visible](https://playwright.dev/docs/actionability#visible "Visible") | [Stable](https://playwright.dev/docs/actionability#stable "Stable") | [Receives Events](https://playwright.dev/docs/actionability#receives-events "Receives Events") | [Enabled](https://playwright.dev/docs/actionability#enabled "Enabled") | [Editable](https://playwright.dev/docs/actionability#editable "Editable") |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [locator.check()](https://playwright.dev/docs/api/class-locator#locator-check)                                       | Yes                                                                    | Yes                                                                 | Yes                                                                                            | Yes                                                                    | -                                                                         |
| [locator.click()](https://playwright.dev/docs/api/class-locator#locator-click)                                       | Yes                                                                    | Yes                                                                 | Yes                                                                                            | Yes                                                                    | -                                                                         |
| [locator.dblclick()](https://playwright.dev/docs/api/class-locator#locator-dblclick)                                 | Yes                                                                    | Yes                                                                 | Yes                                                                                            | Yes                                                                    | -                                                                         |
| [locator.setChecked()](https://playwright.dev/docs/api/class-locator#locator-set-checked)                            | Yes                                                                    | Yes                                                                 | Yes                                                                                            | Yes                                                                    | -                                                                         |
| [locator.tap()](https://playwright.dev/docs/api/class-locator#locator-tap)                                           | Yes                                                                    | Yes                                                                 | Yes                                                                                            | Yes                                                                    | -                                                                         |
| [locator.uncheck()](https://playwright.dev/docs/api/class-locator#locator-uncheck)                                   | Yes                                                                    | Yes                                                                 | Yes                                                                                            | Yes                                                                    | -                                                                         |
| [locator.hover()](https://playwright.dev/docs/api/class-locator#locator-hover)                                       | Yes                                                                    | Yes                                                                 | Yes                                                                                            | -                                                                      | -                                                                         |
| [locator.dragTo()](https://playwright.dev/docs/api/class-locator#locator-drag-to)                                    | Yes                                                                    | Yes                                                                 | Yes                                                                                            | -                                                                      | -                                                                         |
| [locator.screenshot()](https://playwright.dev/docs/api/class-locator#locator-screenshot)                             | Yes                                                                    | Yes                                                                 | -                                                                                              | -                                                                      | -                                                                         |
| [locator.fill()](https://playwright.dev/docs/api/class-locator#locator-fill)                                         | Yes                                                                    | -                                                                   | -                                                                                              | Yes                                                                    | Yes                                                                       |
| [locator.clear()](https://playwright.dev/docs/api/class-locator#locator-clear)                                       | Yes                                                                    | -                                                                   | -                                                                                              | Yes                                                                    | Yes                                                                       |
| [locator.selectOption()](https://playwright.dev/docs/api/class-locator#locator-select-option)                        | Yes                                                                    | -                                                                   | -                                                                                              | Yes                                                                    | -                                                                         |
| [locator.selectText()](https://playwright.dev/docs/api/class-locator#locator-select-text)                            | Yes                                                                    | -                                                                   | -                                                                                              | -                                                                      | -                                                                         |
| [locator.scrollIntoViewIfNeeded()](https://playwright.dev/docs/api/class-locator#locator-scroll-into-view-if-needed) | -                                                                      | Yes                                                                 | -                                                                                              | -                                                                      | -                                                                         |
| [locator.blur()](https://playwright.dev/docs/api/class-locator#locator-blur)                                         | -                                                                      | -                                                                   | -                                                                                              | -                                                                      | -                                                                         |
| [locator.dispatchEvent()](https://playwright.dev/docs/api/class-locator#locator-dispatch-event)                      | -                                                                      | -                                                                   | -                                                                                              | -                                                                      | -                                                                         |
| [locator.focus()](https://playwright.dev/docs/api/class-locator#locator-focus)                                       | -                                                                      | -                                                                   | -                                                                                              | -                                                                      | -                                                                         |
| [locator.press()](https://playwright.dev/docs/api/class-locator#locator-press)                                       | -                                                                      | -                                                                   | -                                                                                              | -                                                                      | -                                                                         |
| [locator.pressSequentially()](https://playwright.dev/docs/api/class-locator#locator-press-sequentially)              | -                                                                      | -                                                                   | -                                                                                              | -                                                                      | -                                                                         |
| [locator.setInputFiles()](https://playwright.dev/docs/api/class-locator#locator-set-input-files)                     | -                                                                      | -                                                                   | -                                                                                              | -                                                                      | -                                                                         |

## 액션 강제 실행[​](https://playwright.dev/docs/actionability#forcing-actions "액션 강제 실행으로 바로 가기")

[locator.click()](https://playwright.dev/docs/api/class-locator#locator-click) 같은 일부 액션은 필수적이지 않은 실행 가능성 검사를 비활성화하는 `force` 옵션을 지원합니다. 예를 들어 [locator.click()](https://playwright.dev/docs/api/class-locator#locator-click) 메서드에 truthy `force`를 전달하면 대상 요소가 실제로 클릭 이벤트를 받는지 확인하지 않습니다.

## 단언문[​](https://playwright.dev/docs/actionability#assertions "단언문으로 바로 가기")

Playwright에는 액션 전 자동 대기와 유사하게, 조건이 충족될 때까지 기다려 flaky함을 줄여 주는 자동 재시도 단언문이 포함되어 있습니다.

| Assertion                                                                                                                            | Description                     |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| [expect(locator).toBeAttached()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-attached)          | 요소가 DOM에 연결되어 있음      |
| [expect(locator).toBeChecked()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-checked)            | 체크박스가 선택되어 있음        |
| [expect(locator).toBeDisabled()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-disabled)          | 요소가 비활성화되어 있음        |
| [expect(locator).toBeEditable()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-editable)          | 요소를 편집할 수 있음           |
| [expect(locator).toBeEmpty()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-empty)                | 컨테이너가 비어 있음            |
| [expect(locator).toBeEnabled()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-enabled)            | 요소가 활성화되어 있음          |
| [expect(locator).toBeFocused()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-focused)            | 요소가 포커스 상태임            |
| [expect(locator).toBeHidden()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-hidden)              | 요소가 보이지 않음              |
| [expect(locator).toBeInViewport()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-in-viewport)     | 요소가 뷰포트와 교차함          |
| [expect(locator).toBeVisible()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-visible)            | 요소가 보임                     |
| [expect(locator).toContainText()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-contain-text)        | 요소가 텍스트를 포함함          |
| [expect(locator).toHaveAttribute()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-attribute)    | 요소가 DOM 속성을 가짐          |
| [expect(locator).toHaveClass()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-class)            | 요소가 class 속성을 가짐        |
| [expect(locator).toHaveCount()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-count)            | 목록의 자식 수가 정확함         |
| [expect(locator).toHaveCSS()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-css)                | 요소가 CSS 속성을 가짐          |
| [expect(locator).toHaveId()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-id)                  | 요소가 ID를 가짐                |
| [expect(locator).toHaveJSProperty()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-js-property) | 요소가 JavaScript 속성을 가짐   |
| [expect(locator).toHaveText()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-text)              | 요소의 텍스트가 일치함          |
| [expect(locator).toHaveValue()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-value)            | input에 값이 있음               |
| [expect(locator).toHaveValues()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-values)          | select에서 옵션이 선택되어 있음 |
| [expect(page).toHaveTitle()](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-title)                     | 페이지에 제목이 있음            |
| [expect(page).toHaveURL()](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-url)                         | 페이지에 URL이 있음             |
| [expect(response).toBeOK()](https://playwright.dev/docs/api/class-apiresponseassertions#api-response-assertions-to-be-ok)            | 응답이 OK 상태임                |

[assertions guide](https://playwright.dev/docs/test-assertions)에서 더 알아보세요.

## Visible[​](https://playwright.dev/docs/actionability#visible "Visible로 바로 가기")

요소는 바운딩 박스가 비어 있지 않고 계산된 스타일에 `visibility:hidden`이 없을 때 visible로 간주됩니다.

이 정의에 따르면:

- 크기가 0인 요소는 visible로 간주되지 않습니다.
- `display:none`인 요소는 visible로 간주되지 않습니다.
- `opacity:0`인 요소는 visible로 간주됩니다.

## Stable[​](https://playwright.dev/docs/actionability#stable "Stable로 바로 가기")

요소는 최소 두 개의 연속된 애니메이션 프레임 동안 동일한 바운딩 박스를 유지하면 stable로 간주됩니다.

## Enabled[​](https://playwright.dev/docs/actionability#enabled "Enabled로 바로 가기")

요소는 **disabled 상태가 아닐 때** enabled로 간주됩니다.

요소가 **disabled**인 경우:

- `[disabled]` 속성이 있는 `<button>`, `<select>`, `<input>`, `<textarea>`, `<option>`, `<optgroup>`인 경우
- `[disabled]` 속성이 있는 `<fieldset>`의 일부인 `<button>`, `<select>`, `<input>`, `<textarea>`, `<option>`, `<optgroup>`인 경우
- `[aria-disabled=true]` 속성이 있는 요소의 하위 요소인 경우

## Editable[​](https://playwright.dev/docs/actionability#editable "Editable로 바로 가기")

요소는 [enabled](https://playwright.dev/docs/actionability#enabled "Enabled") 상태이고 **readonly가 아닐 때** editable로 간주됩니다.

요소가 **readonly**인 경우:

- `[readonly]` 속성이 있는 `<select>`, `<input>`, `<textarea>`인 경우
- `[aria-readonly=true]` 속성이 있고 이를 [지원하는](https://w3c.github.io/aria/#aria-readonly) aria role을 가진 경우

## Receives Events[​](https://playwright.dev/docs/actionability#receives-events "Receives Events로 바로 가기")

요소는 액션 지점에서 포인터 이벤트의 히트 타깃일 때 포인터 이벤트를 받는 것으로 간주됩니다. 예를 들어 `(10;10)` 지점을 클릭할 때, Playwright는 다른 요소(보통 오버레이)가 대신 `(10;10)`에서 클릭을 가로채는지 확인합니다.

예를 들어 [locator.click()](https://playwright.dev/docs/api/class-locator#locator-click) 호출 시점과 상관없이 Playwright가 `Sign Up` 버튼을 클릭하게 되는 시나리오는 다음과 같습니다.

- 페이지가 사용자 이름의 고유성을 검사하는 동안 `Sign Up` 버튼이 비활성화되어 있음
- 서버 확인 후, 비활성화된 `Sign Up` 버튼이 이제 활성화된 다른 버튼으로 교체됨
