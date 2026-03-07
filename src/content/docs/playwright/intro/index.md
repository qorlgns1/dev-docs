---
title: "설치"
description: "Playwright Test는 최신 웹 앱을 위한 엔드 투 엔드 테스트 프레임워크입니다. 테스트 러너, 단언(assertion), 격리, 병렬화, 그리고 풍부한 도구를 함께 제공합니다. ..."
---

출처 URL: https://playwright.dev/docs/intro

# 설치 | Playwright

## 소개

Playwright Test는 최신 웹 앱을 위한 엔드 투 엔드 테스트 프레임워크입니다. 테스트 러너, 단언(assertion), 격리, 병렬화, 그리고 풍부한 도구를 함께 제공합니다. Playwright는 Windows, Linux, macOS에서 Chromium, WebKit, Firefox를 지원하며, 로컬 또는 CI 환경, 헤드리스(headless) 또는 헤디드(headed) 모드에서 실행할 수 있고, Chrome(Android) 및 Mobile Safari를 위한 네이티브 모바일 에뮬레이션도 지원합니다.

**학습 내용**

- [Playwright 설치 방법](https://playwright.dev/docs/intro#installing-playwright)
- [설치되는 항목](https://playwright.dev/docs/intro#whats-installed)
- [예제 테스트 실행 방법](https://playwright.dev/docs/intro#running-the-example-test)
- [HTML 테스트 리포트 여는 방법](https://playwright.dev/docs/intro#html-test-reports)

## Playwright 설치하기

다음 방법 중 하나로 Playwright를 설치해 시작하세요.

### npm, yarn 또는 pnpm 사용

아래 명령은 새 프로젝트를 초기화하거나 기존 프로젝트에 Playwright를 추가합니다.

- npm
- yarn
- pnpm

```
    npm init playwright@latest

```

```
    yarn create playwright

```

```
    pnpm create playwright

```

프롬프트가 표시되면 다음을 선택하거나 확인하세요.

- TypeScript 또는 JavaScript (기본값: TypeScript)
- 테스트 폴더 이름 (기본값: `tests`, `tests`가 이미 있으면 `e2e`)
- GitHub Actions 워크플로 추가 (CI에 권장)
- Playwright 브라우저 설치 (기본값: 예)

이 명령은 나중에 다시 실행할 수 있으며, 기존 테스트를 덮어쓰지 않습니다.

### VS Code 확장 사용

[VS Code 확장](https://playwright.dev/docs/getting-started-vscode)으로도 테스트를 생성하고 실행할 수 있습니다.

## 설치되는 항목

Playwright는 필요한 브라우저 바이너리를 다운로드하고 아래 스캐폴드를 생성합니다.

```
    playwright.config.ts         # 테스트 설정
    package.json
    package-lock.json            # 또는 yarn.lock / pnpm-lock.yaml
    tests/
      example.spec.ts            # 최소 예제 테스트

```

[playwright.config](https://playwright.dev/docs/test-configuration)는 대상 브라우저, 타임아웃, 재시도, 프로젝트, 리포터 등 설정을 중앙에서 관리합니다. 기존 프로젝트에서는 의존성이 현재 `package.json`에 추가됩니다.

`tests/`에는 최소한의 시작용 테스트가 포함됩니다.

## 예제 테스트 실행하기

기본적으로 테스트는 Chromium, Firefox, WebKit에서 병렬로 헤드리스(headless) 모드로 실행됩니다([playwright.config](https://playwright.dev/docs/test-configuration)에서 설정 가능). 출력과 집계된 결과는 터미널에 표시됩니다.

- npm
- yarn
- pnpm

```
    npx playwright test

```

```
    yarn playwright test

```

```
    pnpm exec playwright test

```

![명령줄에서 실행 중인 테스트](https://playwright.dev/assets/images/run-tests-cli-6e7e3119a14239c9021b406d7109dc44.png)

팁:

- 브라우저 창 보기: `--headed`를 추가하세요.
- 단일 프로젝트/브라우저 실행: `--project=chromium`.
- 파일 하나 실행: `npx playwright test tests/example.spec.ts`.
- 테스트 UI 열기: `--ui`.

필터링, 헤디드(headed) 모드, 샤딩, 재시도에 대한 자세한 내용은 [테스트 실행하기](https://playwright.dev/docs/running-tests)를 참고하세요.

## HTML 테스트 리포트

테스트 실행 후 [HTML 리포터](https://playwright.dev/docs/test-reporters#html-reporter)는 브라우저, 성공(passed), 실패(failed), 건너뜀(skipped), 불안정(flaky) 상태 등으로 필터링 가능한 대시보드를 제공합니다. 테스트를 클릭하면 오류, 첨부 파일, 단계를 확인할 수 있습니다. 실패가 발생한 경우에만 자동으로 열리며, 아래 명령으로 수동으로 열 수 있습니다.

- npm
- yarn
- pnpm

```
    npx playwright show-report

```

```
    yarn playwright show-report

```

```
    pnpm exec playwright show-report

```

![HTML 리포트](https://playwright.dev/assets/images/html-report-basic-8a88e44830660bfd1da1d17a7241f035.png)

## UI 모드에서 예제 테스트 실행하기

watch 모드, 실시간 단계 보기, 타임 트래블 디버깅 등을 위해 [UI 모드](https://playwright.dev/docs/test-ui-mode)로 테스트를 실행하세요.

- npm
- yarn
- pnpm

```
    npx playwright test --ui

```

```
    yarn playwright test --ui

```

```
    pnpm exec playwright test --ui

```

![UI 모드](https://playwright.dev/assets/images/ui-mode-1958baf0398aef5e9c9b5c68c5d56f2d.png)

watch 필터, 단계 상세, 트레이스(trace) 통합은 [UI 모드 상세 가이드](https://playwright.dev/docs/test-ui-mode)를 참고하세요.

## Playwright 업데이트

Playwright를 업데이트하고 새 브라우저 바이너리 및 해당 의존성을 다운로드하세요.

- npm
- yarn
- pnpm

```
    npm install -D @playwright/test@latest
    npx playwright install --with-deps

```

```
    yarn add --dev @playwright/test@latest
    yarn playwright install --with-deps

```

```
    pnpm install --save-dev @playwright/test@latest
    pnpm exec playwright install --with-deps

```

설치된 버전 확인:

- npm
- yarn
- pnpm

```
    npx playwright --version

```

```
    yarn playwright --version

```

```
    pnpm exec playwright --version

```

## 시스템 요구 사항

- Node.js: 최신 20.x, 22.x 또는 24.x.
- Windows 11+, Windows Server 2019+ 또는 Windows Subsystem for Linux (WSL).
- macOS 14 (Ventura) 이상.
- Debian 12 / 13, Ubuntu 22.04 / 24.04 (x86-64 또는 arm64).

## 다음 단계

- [웹 우선 단언(assertion), 픽스처(fixture), 로케이터(locator)를 사용해 테스트 작성하기](https://playwright.dev/docs/writing-tests)
- [단일 또는 여러 테스트 실행, 헤디드(headed) 모드](https://playwright.dev/docs/running-tests)
- [Codegen으로 테스트 생성하기](https://playwright.dev/docs/codegen-intro)
- [테스트 트레이스(trace) 보기](https://playwright.dev/docs/trace-viewer-intro)
