---
title: "시각적 회귀 테스트"
description: "Vitest는 별도 설정 없이 시각적 회귀 테스트를 실행할 수 있습니다. UI 컴포넌트와 페이지의 스크린샷을 캡처한 뒤, 기준 이미지와 비교해 의도하지 않은 시각적 변경을 감지합니다."
---

출처 URL: https://vitest.dev/guide/browser/visual-regression-testing

# 시각적 회귀 테스트

Vitest는 별도 설정 없이 시각적 회귀 테스트를 실행할 수 있습니다. UI 컴포넌트와 페이지의 스크린샷을 캡처한 뒤, 기준 이미지와 비교해 의도하지 않은 시각적 변경을 감지합니다.

동작을 검증하는 기능 테스트와 달리, 시각적 테스트는 충분한 수동 테스트 없이는 놓치기 쉬운 스타일 이슈, 레이아웃 흔들림, 렌더링 문제를 잡아냅니다.

## 왜 시각적 회귀 테스트인가요?

시각적 버그는 에러를 던지지 않고, 그냥 보기만 이상해집니다. 이럴 때 시각적 테스트가 필요합니다.

- 버튼은 여전히 폼을 제출합니다... 그런데 왜 갑자기 핫핑크일까요?
- 텍스트는 완벽하게 맞습니다... 누군가 모바일에서 보기 전까지는요
- 모든 게 잘 동작합니다... 단, 저 두 컨테이너는 뷰포트 밖에 있습니다
- 신중하게 진행한 CSS 리팩터링은 잘 됐습니다... 하지만 아무도 테스트하지 않는 페이지의 레이아웃이 깨졌습니다

시각적 회귀 테스트는 UI를 위한 안전망 역할을 하며, 이런 시각적 변경이 프로덕션에 도달하기 전에 자동으로 잡아냅니다.

## 시작하기

::: warning 브라우저 렌더링 차이
시각적 회귀 테스트는 **환경이 다르면 본질적으로 불안정합니다**. 스크린샷은 다음 이유로 머신마다 다르게 보입니다.

- 폰트 렌더링 (가장 큰 요인입니다. Windows, macOS, Linux는 모두 텍스트를 다르게 렌더링합니다)
- GPU 드라이버와 하드웨어 가속
- headless 실행 여부
- 브라우저 설정과 버전
- ...그리고 솔직히 말해, 가끔은 달의 위상 때문인 것처럼 느껴질 때도 있습니다

그래서 Vitest는 스크린샷 이름에 브라우저와 플랫폼을 포함합니다 (예: `button-chromium-darwin.png`).

안정적인 테스트를 위해서는 어디서나 동일한 환경을 사용하세요. [Azure App Testing](https://azure.microsoft.com/en-us/products/app-testing/) 또는 [Docker containers](https://playwright.dev/docs/docker) 같은 클라우드 서비스를 **강력히 권장**합니다.
:::

Vitest에서 시각적 회귀 테스트는 [`toMatchScreenshot` assertion](https://vitest.dev/api/browser/assertions.html#tomatchscreenshot)으로 수행할 수 있습니다.

```ts
import { expect, test } from "vitest";
import { page } from "vitest/browser";

test("hero section looks correct", async () => {
  // ...the rest of the test

  // capture and compare screenshot
  await expect(page.getByTestId("hero")).toMatchScreenshot("hero-section");
});
```

### 기준 이미지 생성

시각적 테스트를 처음 실행하면, Vitest는 기준(베이스라인) 스크린샷을 만들고 다음 오류 메시지와 함께 테스트를 실패시킵니다.

```
expect(element).toMatchScreenshot()

No existing reference screenshot found; a new one was created. Review it before running tests again.

Reference screenshot:
  tests/__screenshots__/hero.test.ts/hero-section-chromium-darwin.png
```

이는 정상 동작입니다. 스크린샷이 올바른지 확인한 다음 테스트를 다시 실행하세요.
이제부터 Vitest는 이후 실행 결과를 이 베이스라인과 비교합니다.

::: tip
기준 스크린샷은 테스트 옆의 `__screenshots__` 폴더에 저장됩니다.
**커밋하는 것을 잊지 마세요!**
:::

### 스크린샷 구성

기본적으로 스크린샷은 다음과 같이 구성됩니다.

```
.
├── __screenshots__
│   └── test-file.test.ts
│       ├── test-name-chromium-darwin.png
│       ├── test-name-firefox-linux.png
│       └── test-name-webkit-win32.png
└── test-file.test.ts
```

이 네이밍 규칙에는 다음이 포함됩니다.

- **테스트 이름**: `toMatchScreenshot()` 호출의 첫 번째 인자이거나, 테스트 이름에서 자동 생성됨
- **브라우저 이름**: `chrome`, `chromium`, `firefox`, `webkit`
- **플랫폼**: `aix`, `darwin`, `freebsd`, `linux`, `openbsd`, `sunos`, `win32`

이렇게 하면 서로 다른 환경의 스크린샷이 서로 덮어써지는 일을 방지할 수 있습니다.

### 기준 이미지 업데이트

UI를 의도적으로 변경한 경우, 기준 스크린샷을 업데이트해야 합니다.

```bash
$ vitest --update
```

커밋 전에 업데이트된 스크린샷을 검토해 변경이 의도된 것인지 확인하세요.

## 시각적 테스트 동작 방식

시각적 회귀 테스트는 비교할 수 있는 안정적인 스크린샷이 필요합니다. 하지만 페이지는 이미지 로딩, 애니메이션 종료, 폰트 렌더링, 레이아웃 정착 때문에 즉시 안정 상태가 되지 않습니다.

Vitest는 "안정 스크린샷 감지(Stable Screenshot Detection)"를 통해 이를 자동 처리합니다.

1. Vitest가 첫 번째 스크린샷을 찍고(또는 기준 스크린샷이 있으면 그것을 베이스라인으로 사용)
1. 또 다른 스크린샷을 찍어 베이스라인과 비교합니다
   - 스크린샷이 일치하면 페이지는 안정 상태이며 테스트가 계속됩니다
   - 다르면 Vitest는 최신 스크린샷을 새 베이스라인으로 사용하고 반복합니다
1. 안정화되거나 타임아웃에 도달할 때까지 이를 계속합니다

이 방식은 로딩 스피너나 애니메이션 같은 일시적 시각 변화로 인한 오탐을 줄여줍니다. 다만 애니메이션이 끝나지 않으면 타임아웃에 걸릴 수 있으므로, [테스트 중 애니메이션 비활성화](#disable-animations)를 고려하세요.

재시도(1회 이상) 후 안정적인 스크린샷이 캡처되고 기준 스크린샷이 존재하면, Vitest는 `createDiff: true`로 기준 이미지와 최종 비교를 수행합니다. 일치하지 않으면 diff 이미지가 생성됩니다.

안정성 감지 중에는 일치 여부만 확인하면 되므로 Vitest는 `createDiff: false`로 comparator를 호출합니다. 이렇게 해서 감지 과정을 빠르게 유지합니다.

## 시각적 테스트 설정

### 전역 설정

[Vitest config](https://vitest.dev/config/browser/expect#tomatchscreenshot)에서 시각적 회귀 테스트 기본값을 설정하세요.

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    browser: {
      expect: {
        toMatchScreenshot: {
          comparatorName: "pixelmatch",
          comparatorOptions: {
            // 0-1, how different can colors be?
            threshold: 0.2,
            // 1% of pixels can differ
            allowedMismatchedPixelRatio: 0.01,
          },
        },
      },
    },
  },
});
```

### 테스트별 설정

특정 테스트에서 전역 설정을 재정의할 수 있습니다.

```ts
await expect(element).toMatchScreenshot("button-hover", {
  comparatorName: "pixelmatch",
  comparatorOptions: {
    // more lax comparison for text-heavy elements
    allowedMismatchedPixelRatio: 0.1,
  },
});
```

## 모범 사례

### 특정 요소 테스트

전체 페이지를 명시적으로 테스트하려는 경우가 아니라면, 오탐을 줄이기 위해 특정 컴포넌트만 캡처하는 것을 권장합니다.

```ts
// ❌ Captures entire page; prone to unrelated changes
await expect(page).toMatchScreenshot();

// ✅ Captures only the component under test
await expect(page.getByTestId("product-card")).toMatchScreenshot();
```

### 동적 콘텐츠 처리

타임스탬프, 사용자 데이터, 랜덤 값 같은 동적 콘텐츠는 테스트 실패를 유발합니다. 동적 콘텐츠의 소스를 목킹하거나, Playwright provider 사용 시 `screenshotOptions`의 [`mask` option](https://playwright.dev/docs/api/class-page#page-screenshot-option-mask)을 사용해 마스킹할 수 있습니다.

```ts
await expect(page.getByTestId("profile")).toMatchScreenshot({
  screenshotOptions: {
    mask: [page.getByTestId("last-seen")],
  },
});
```

### 애니메이션 비활성화

애니메이션은 flaky 테스트의 원인이 될 수 있습니다. 테스트 중에는 사용자 정의 CSS 스니펫을 주입해 비활성화하세요.

```css
*,
*::before,
*::after {
  animation-duration: 0s !important;
  animation-delay: 0s !important;
  transition-duration: 0s !important;
  transition-delay: 0s !important;
}
```

::: tip
Playwright provider를 사용할 때 assertion을 사용하면 애니메이션은 자동으로 비활성화됩니다. `screenshotOptions`의 `animations` 옵션 값이 기본적으로 `"disabled"`로 설정됩니다.
:::

### 적절한 임계값 설정

임계값 튜닝은 까다롭습니다. 콘텐츠, 테스트 환경, 앱에서 허용 가능한 수준에 따라 달라지며 테스트별로 달라질 수도 있습니다.

Vitest는 불일치 픽셀 수에 대한 기본값을 설정하지 않습니다. 이는 사용자 요구에 따라 결정해야 합니다. 권장 방식은 `allowedMismatchedPixelRatio`를 사용하는 것입니다. 이렇게 하면 고정 수치가 아니라 스크린샷 크기에 기반해 임계값이 계산됩니다.

`allowedMismatchedPixelRatio`와 `allowedMismatchedPixels`를 둘 다 설정하면, Vitest는 더 엄격한 한도를 사용합니다.

### 일관된 뷰포트 크기 설정

브라우저 인스턴스의 기본 크기가 다를 수 있으므로, 테스트 또는 인스턴스 설정에서 특정 뷰포트 크기를 지정하는 것이 좋습니다.

```ts
await page.viewport(1280, 720);
```

```ts [vitest.config.ts]
import { playwright } from "@vitest/browser-playwright";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [
        {
          browser: "chromium",
          viewport: { width: 1280, height: 720 },
        },
      ],
    },
  },
});
```

### Git LFS 사용

대규모 테스트 스위트를 운영할 계획이라면 기준 스크린샷을 [Git LFS](https://github.com/git-lfs/git-lfs?tab=readme-ov-file)에 저장하세요.

## 실패한 테스트 디버깅

시각적 테스트가 실패하면 Vitest는 디버깅을 돕기 위해 세 가지 이미지를 제공합니다.

1. **기준 스크린샷**: 기대되는 베이스라인 이미지
1. **실제 스크린샷**: 테스트 중 캡처된 이미지
1. **Diff 이미지**: 차이점을 강조하지만, 생성되지 않을 수도 있음

다음과 같은 형태를 보게 됩니다.

```
expect(element).toMatchScreenshot()

Screenshot does not match the stored reference.
245 pixels (ratio 0.03) differ.

Reference screenshot:
  tests/__screenshots__/button.test.ts/button-chromium-darwin.png

Actual screenshot:
  tests/.vitest-attachments/button.test.ts/button-chromium-darwin-actual.png

Diff image:
  tests/.vitest-attachments/button.test.ts/button-chromium-darwin-diff.png
```

### diff 이미지 이해하기

- **빨간 픽셀**: 기준 이미지와 실제 이미지가 다른 영역
- **노란 픽셀**: 안티앨리어싱 차이(안티앨리어싱 무시가 비활성화된 경우)
- **투명/원본**: 변경되지 않은 영역

:::tip
diff가 대부분 빨간색이면 문제가 꽤 큽니다. 텍스트 주변에 빨간 픽셀이 드문드문 보이는 정도라면 임계값을 조금 올리면 해결되는 경우가 많습니다.
:::

## 자주 발생하는 문제와 해결 방법

### 폰트 렌더링으로 인한 오탐

폰트 가용성과 렌더링은 시스템마다 크게 다릅니다. 가능한 해결 방법은 다음과 같습니다.

- 웹 폰트를 사용하고 로딩 완료를 기다리기:

  ```ts
  // wait for fonts to load
  await document.fonts.ready;

  // continue with your tests
  ```

- 텍스트 비중이 큰 영역에 대해 비교 임계값 올리기:

  ```ts
  await expect(page.getByTestId("article-summary")).toMatchScreenshot({
    comparatorName: "pixelmatch",
    comparatorOptions: {
      // 10% of the pixels are allowed to change
      allowedMismatchedPixelRatio: 0.1,
    },
  });
  ```

- 폰트 렌더링 일관성을 위해 클라우드 서비스 또는 컨테이너 환경 사용

### flaky 테스트 또는 스크린샷 크기 불일치

테스트가 랜덤하게 통과/실패하거나 실행마다 스크린샷 크기가 다르다면:

- 로딩 인디케이터를 포함해 모든 리소드가 로드될 때까지 대기
- 명시적인 뷰포트 크기 설정: `await page.viewport(1920, 1080)`
- 뷰포트 경계에서 반응형 동작 확인
- 의도치 않은 애니메이션이나 트랜지션 확인
- 대형 스크린샷의 경우 테스트 타임아웃 증가
- 클라우드 서비스 또는 컨테이너 환경 사용

## 팀을 위한 시각적 회귀 테스트

앞서 시각적 테스트에는 안정적인 환경이 필요하다고 했습니다. 핵심은 이겁니다. 로컬 머신은 그 환경이 아닙니다.

팀 단위에서는 기본적으로 세 가지 선택지가 있습니다.

1. **Self-hosted runners**: 설정이 복잡하고 유지보수가 어렵습니다
1. **GitHub Actions**: (오픈소스 기준) 무료이며 어떤 provider와도 함께 동작합니다
1. **Cloud services**: [Azure App Testing](https://azure.microsoft.com/en-us/products/app-testing/)처럼 이 문제 해결을 위해 만들어진 서비스입니다

여기서는 가장 빠르게 도입할 수 있는 2번과 3번에 집중합니다.

미리 말하면 주요 트레이드오프는 다음과 같습니다.

- **GitHub Actions**: 시각적 테스트는 CI에서만 실행됨(개발자는 로컬 실행 불가)
- **Microsoft's service**: 어디서나 동작하지만 비용이 들고 Playwright에서만 동작

:::: tabs key:vrt-for-teams
=== GitHub Actions

핵심은 시각적 테스트를 일반 테스트와 분리하는 것입니다.
그렇지 않으면 스크린샷 불일치로 실패한 로그를 확인하느라 시간을 낭비하게 됩니다.

#### 테스트 구성하기

먼저 시각적 테스트를 분리하세요. `visual` 폴더(또는 프로젝트에 맞는 이름)에 두면 됩니다.

```json [package.json]
{
  "scripts": {
    "test:unit": "vitest --exclude tests/visual/*.test.ts",
    "test:visual": "vitest tests/visual/*.test.ts"
  }
}
```

이제 개발자는 로컬에서 `npm run test:unit`을 실행할 때 시각적 테스트에 방해받지 않습니다. 시각적 테스트는 환경이 일관된 CI에만 남게 됩니다.

::: tip Alternative
glob 패턴이 마음에 들지 않나요? 별도의 [Test Projects](https://vitest.dev/guide/projects)를 사용하고 다음처럼 실행할 수도 있습니다.

- `vitest --project unit`
- `vitest --project visual`
  :::

#### CI 설정

CI에는 브라우저 설치가 필요합니다. 방식은 provider에 따라 다릅니다.

::: tabs key:provider
== Playwright

[Playwright](https://npmjs.com/package/playwright)를 사용하면 간단합니다. 버전을 고정하고 테스트 실행 전에 다음을 추가하세요.

```yaml [.github/workflows/ci.yml]
# ...the rest of the workflow
- name: Install Playwright Browsers
  run: npx --no playwright install --with-deps --only-shell
```

== WebdriverIO

[WebdriverIO](https://www.npmjs.com/package/webdriverio)는 브라우저를 직접 준비해야 합니다.
[@browser-actions](https://github.com/browser-actions)가 도움을 줍니다.

```yaml [.github/workflows/ci.yml]
# ...the rest of the workflow
- uses: browser-actions/setup-chrome@v1
  with:
    chrome-version: 120
```

:::

그다음 시각적 테스트를 실행합니다.

```yaml [.github/workflows/ci.yml]
# ...the rest of the workflow
# ...browser setup
- name: Visual Regression Testing
  run: npm run test:visual
```

#### 업데이트 워크플로

이제 중요한 부분입니다. 모든 PR에서 스크린샷을 자동 업데이트하면 안 됩니다 _(혼란의 시작!)_.
대신 UI를 의도적으로 변경했을 때 개발자가 직접 실행할 수 있는 수동 트리거 워크플로를 만드세요.

아래 워크플로는 다음을 수행합니다.

- feature 브랜치에서만 실행됨(main에서는 절대 실행되지 않음)
- 트리거한 사람을 공동 작성자로 기록
- 같은 브랜치에서 동시 실행 방지
- 보기 좋은 요약 제공:
  - **스크린샷이 변경된 경우**, 무엇이 바뀌었는지 목록 표시

  - **변경이 없는 경우**, 그 사실도 알려줌

::: tip
이건 하나의 접근 방식일 뿐입니다. 어떤 팀은 PR 코멘트(`/update-screenshots`)를 선호하고, 다른 팀은 라벨을 사용합니다. 팀 워크플로에 맞게 조정하세요!

중요한 건 베이스라인을 통제된 방식으로 업데이트하는 체계를 갖추는 것입니다.
:::

```yaml [.github/workflows/update-screenshots.yml]
name: Update Visual Regression Screenshots

on:
  workflow_dispatch: # manual trigger only

env:
  AUTHOR_NAME: "github-actions[bot]"
  AUTHOR_EMAIL: "41898282+github-actions[bot]@users.noreply.github.com"
  COMMIT_MESSAGE: |
    test: update visual regression screenshots

    Co-authored-by: ${{ github.actor }} <${{ github.actor_id }}+${{ github.actor }}@users.noreply.github.com>

jobs:
  update-screenshots:
    runs-on: ubuntu-24.04

    # safety first: don't run on main
    if: github.ref_name != github.event.repository.default_branch

    # one at a time per branch
    concurrency:
      group: visual-regression-screenshots@${{ github.ref_name }}
      cancel-in-progress: true

    permissions:
      contents: write # needs to push changes

    steps:
      - name: Checkout selected branch
        uses: actions/checkout@v4
        with:
          ref: ${{ github.ref_name }}
          # use PAT if triggering other workflows
          # token: ${{ secrets.GITHUB_TOKEN }}

      - name: Configure Git
        run: |
          git config --global user.name "${{ env.AUTHOR_NAME }}"
          git config --global user.email "${{ env.AUTHOR_EMAIL }}"

      # your setup steps here (node, pnpm, whatever)
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 24

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright Browsers
        run: npx --no playwright install --with-deps --only-shell

      # the magic happens below 🪄
      - name: Update Visual Regression Screenshots
        run: npm run test:visual --update

      # check what changed
      - name: Check for changes
        id: check_changes
        run: |
          CHANGED_FILES=$(git status --porcelain | awk '{print $2}')
          if [ "${CHANGED_FILES:+x}" ]; then
            echo "changes=true" >> $GITHUB_OUTPUT
            echo "Changes detected"

            # save the list for the summary
            echo "changed_files<<EOF" >> $GITHUB_OUTPUT
            echo "$CHANGED_FILES" >> $GITHUB_OUTPUT
            echo "EOF" >> $GITHUB_OUTPUT
            echo "changed_count=$(echo "$CHANGED_FILES" | wc -l)" >> $GITHUB_OUTPUT
          else
            echo "changes=false" >> $GITHUB_OUTPUT
            echo "No changes detected"
          fi

      # commit if there are changes
      - name: Commit changes
        if: steps.check_changes.outputs.changes == 'true'
        run: |
          git add -A
          git commit -m "${{ env.COMMIT_MESSAGE }}"

      - name: Push changes
        if: steps.check_changes.outputs.changes == 'true'
        run: git push origin ${{ github.ref_name }}

      # pretty summary for humans
      - name: Summary
        run: |
          if [[ "${{ steps.check_changes.outputs.changes }}" == "true" ]]; then
            echo "### 📸 Visual Regression Screenshots Updated" >> $GITHUB_STEP_SUMMARY
            echo "" >> $GITHUB_STEP_SUMMARY
            echo "Successfully updated **${{ steps.check_changes.outputs.changed_count }}** screenshot(s) on \`${{ github.ref_name }}\`" >> $GITHUB_STEP_SUMMARY
            echo "" >> $GITHUB_STEP_SUMMARY
            echo "#### Changed Files:" >> $GITHUB_STEP_SUMMARY
            echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
            echo "${{ steps.check_changes.outputs.changed_files }}" >> $GITHUB_STEP_SUMMARY
            echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
            echo "" >> $GITHUB_STEP_SUMMARY
            echo "✅ The updated screenshots have been committed and pushed. Your visual regression baseline is now up to date!" >> $GITHUB_STEP_SUMMARY
          else
            echo "### ℹ️ No Screenshot Updates Required" >> $GITHUB_STEP_SUMMARY
            echo "" >> $GITHUB_STEP_SUMMARY
            echo "The visual regression test command ran successfully but no screenshots needed updating." >> $GITHUB_STEP_SUMMARY
            echo "" >> $GITHUB_STEP_SUMMARY
            echo "All screenshots are already up to date! 🎉" >> $GITHUB_STEP_SUMMARY
          fi
```

=== Azure App Testing

테스트는 로컬에 두고, 브라우저만 클라우드에서 실행합니다. Playwright의 원격 브라우저 기능을 쓰되, 인프라는 Microsoft가 관리합니다.

#### 테스트 구성하기

비용 통제를 위해 시각적 테스트를 분리하세요. 실제로 스크린샷을 찍는 테스트만 서비스를 사용해야 합니다.

가장 깔끔한 방법은 [Test Projects](https://vitest.dev/guide/projects)를 사용하는 것입니다.

```ts [vitest.config.ts]
import { env } from "node:process";
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  // ...global Vite config
  tests: {
    // ...global Vitest config
    projects: [
      {
        extends: true,
        test: {
          name: "unit",
          include: ["tests/**/*.test.ts"],
          // regular config, can use local browsers
        },
      },
      {
        extends: true,
        test: {
          name: "visual",
          // or you could use a different suffix, e.g.,: `tests/**/*.visual.ts?(x)`
          include: ["visual-regression-tests/**/*.test.ts?(x)"],
          browser: {
            enabled: true,
            provider: playwright({
              connectOptions: {
                wsEndpoint: `${env.PLAYWRIGHT_SERVICE_URL}?${new URLSearchParams(
                  {
                    "api-version": "2025-09-01",
                    os: "linux", // always use Linux for consistency
                    // helps identifying runs in the service's dashboard
                    runName: `Vitest ${env.CI ? "CI" : "local"} run @${new Date().toISOString()}`,
                  },
                )}`,
                exposeNetwork: "<loopback>",
                headers: {
                  Authorization: `Bearer ${env.PLAYWRIGHT_SERVICE_ACCESS_TOKEN}`,
                },
                timeout: 30_000,
              },
            }),
            headless: true,
            instances: [
              {
                browser: "chromium",
                viewport: { width: 2560, height: 1440 },
              },
            ],
          },
        },
      },
    ],
  },
});
```

[공식 가이드(Playwright Workspace 생성)](https://learn.microsoft.com/en-us/azure/app-testing/playwright-workspaces/quickstart-run-end-to-end-tests?tabs=playwrightcli&pivots=playwright-test-runner#create-a-workspace)를 따라 워크스페이스를 만드세요.

워크스페이스를 만든 뒤, Vitest가 이를 사용하도록 설정합니다:

1. **엔드포인트 URL 설정**: [공식 가이드](https://learn.microsoft.com/en-us/azure/app-testing/playwright-workspaces/quickstart-run-end-to-end-tests?tabs=playwrightcli&pivots=playwright-test-runner#configure-the-browser-endpoint)를 따라 URL을 가져와 `PLAYWRIGHT_SERVICE_URL` 환경 변수로 설정합니다.
1. **토큰 인증 활성화**: 워크스페이스에서 [액세스 토큰을 활성화](https://learn.microsoft.com/en-us/azure/app-testing/playwright-workspaces/how-to-manage-authentication?pivots=playwright-test-runner#enable-authentication-using-access-tokens)한 다음, [토큰을 생성](https://learn.microsoft.com/en-us/azure/app-testing/playwright-workspaces/how-to-manage-access-tokens#generate-a-workspace-access-token)하여 `PLAYWRIGHT_SERVICE_ACCESS_TOKEN` 환경 변수로 설정합니다.

::: danger 해당 토큰을 반드시 비밀로 유지하세요!
`PLAYWRIGHT_SERVICE_ACCESS_TOKEN`을 절대 리포지토리에 커밋하지 마세요.
이 토큰을 가진 누구나 비용을 발생시킬 수 있습니다. 로컬에서는 환경 변수를 사용하고,
CI에서는 시크릿을 사용하세요.
:::

그다음 `test` 스크립트를 다음과 같이 분리합니다:

```json [package.json]
{
  "scripts": {
    "test:visual": "vitest --project visual",
    "test:unit": "vitest --project unit"
  }
}
```

#### 테스트 실행

```bash
# Local development
npm run test:unit    # free, runs locally
npm run test:visual  # uses cloud browsers

# Update screenshots
npm run test:visual -- --update
```

이 접근 방식의 가장 큰 장점은 별다른 작업 없이 그대로 잘 동작한다는 점입니다:

- **일관된 스크린샷**, 모두가 동일한 클라우드 브라우저를 사용
- **로컬에서 동작**, 개발자가 자신의 머신에서 시각적 테스트를 실행하고 업데이트 가능
- **사용한 만큼만 과금**, 시각적 테스트만 서비스 사용 시간을 소비
- **Docker나 워크플로 설정 불필요**, 관리하거나 유지할 항목이 없음

#### CI 설정

CI에 다음 시크릿을 추가합니다:

```yaml
env:
  PLAYWRIGHT_SERVICE_URL: ${{ vars.PLAYWRIGHT_SERVICE_URL }}
  PLAYWRIGHT_SERVICE_ACCESS_TOKEN: ${{ secrets.PLAYWRIGHT_SERVICE_ACCESS_TOKEN }}
```

그다음 평소처럼 테스트를 실행하면 됩니다. 나머지는 서비스가 처리합니다.

::::

### 그래서 어떤 걸 선택해야 할까?

두 접근 방식 모두 동작합니다. 진짜 질문은 팀에 어떤 불편이 더 중요한지입니다.

이미 GitHub 생태계를 깊게 사용 중이라면 GitHub Actions는 대체하기 어렵습니다.
오픈 소스에는 무료이고, 어떤 브라우저 제공자와도 함께 쓸 수 있으며, 모든 것을 직접 제어할 수 있습니다.

단점은 무엇일까요? 누군가 로컬에서 스크린샷을 생성했는데 CI 기대값과 더는 맞지 않을 때 나오는
“내 컴퓨터에서는 되는데요”라는 대화입니다.

개발자가 로컬에서 시각적 테스트를 실행해야 한다면 클라우드 서비스가 더 합리적입니다.

일부 팀은 디자이너가 결과를 직접 확인하거나, 개발자가 푸시 전에 이슈를 잡는 것을 선호합니다.
이 방식은 push-wait-check-fix-push 사이클을 줄일 수 있습니다.

아직 결정이 어렵다면 GitHub Actions부터 시작하세요.
로컬 테스트가 문제 지점이 되면 나중에 클라우드 서비스를 언제든 추가할 수 있습니다.
