---
title: 'Ionic Capacitor 빌드 | Sentry for Next.js'
description: '이 가이드에서는  도구를 사용해 TypeScript용 소스 맵을 성공적으로 업로드하는 방법을 알아봅니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor

# Ionic Capacitor 빌드 | Sentry for Next.js

이 가이드에서는 `sentry-cli` 도구를 사용해 TypeScript용 소스 맵을 성공적으로 업로드하는 방법을 알아봅니다.

이 가이드는 다음을 가정합니다:

* `sentry-cli` 버전 >= `2.17.0`
* Sentry JavaScript SDK 버전 >= `7.47.0`

이 가이드는 프로젝트를 컴파일할 때 `ionic capacitor build` 명령을 사용하는 경우에만 적용됩니다. 다른 명령을 사용한다면, 해당 가이드를 따르는 것이 더 적절할 가능성이 높습니다.

## [자동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#automatic-setup)

Sentry Wizard를 사용해 초기 설정을 할 수 있지만, 이 빌드 설정에서 소스 맵을 구성하려면 여전히 수동 변경이 필요합니다.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

Wizard는 다음 단계를 안내합니다:

* Sentry에 로그인하고 프로젝트 선택
* 필요한 Sentry 패키지 설치
* 소스 맵 생성 및 업로드를 위해 빌드 도구 구성
* 소스 맵 업로드를 위해 CI 구성

## [수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#manual-setup)

- [1. 소스 맵 생성](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#1-generate-source-maps)

먼저, TypeScript 컴파일러가 소스 맵을 출력하도록 설정합니다:

`tsconfig.json`

```json
{
  "compilerOptions": {
    "sourceMap": true,
    "inlineSources": true,

    // Set `sourceRoot` to  "/" to strip the build path prefix from
    // generated source code references. This will improve issue grouping in Sentry.
    "sourceRoot": "/"
  }
}
```

소스 맵을 생성하면 공개되어 소스 코드가 유출될 수 있습니다. 이를 방지하려면 서버에서 `.js.map` 파일 접근을 차단하거나, 애플리케이션 배포 전에 소스 맵을 삭제할 수 있습니다.

- [2. Sentry CLI 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#2-configure-sentry-cli)

[Sentry CLI 설치 안내](https://docs.sentry.io/cli/installation.md)를 참고하세요.

`sentry-cli` 구성에 대한 자세한 내용은 [Sentry CLI 구성 문서](https://docs.sentry.io/cli/configuration.md)를 확인하세요.

프로젝트에 맞게 `sentry-cli`가 구성되어 있는지 확인하세요. 이를 위해 환경 변수를 사용할 수 있습니다:

`.env.local`

```bash
SENTRY_ORG=___ORG_SLUG___
SENTRY_PROJECT=___PROJECT_SLUG___
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

- [3. 아티팩트에 Debug ID 주입](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#3-inject-debug-ids-into-artifacts)

Debug ID는 이벤트의 스택 프레임을 해당 축소된 소스 및 소스 맵 파일과 매칭하는 데 사용됩니다. 자세한 내용은 [What are Debug IDs](https://docs.sentry.io/platforms/javascript/sourcemaps/troubleshooting_js/debug-ids.md)를 참고하세요.

Debug ID를 주입하려면, 프로젝트를 빌드한 후 다음 명령을 사용하세요:

```bash
// Paths can vary so check where your assets/public and App/public folder are.
sentry-cli sourcemaps inject /path/to/directory/android/app/src/main/assets/public
sentry-cli sourcemaps inject /path/to/directory/ios/App/public
```

#
- [아티팩트에 Debug ID가 주입되었는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#verify-debug-ids-were-injected-in-artifacts)

축소된 소스 파일의 끝에는 다음과 같이 `debugId`라는 주석이 포함되어야 합니다:

`example_minified_file.js`

```javascript
...
//# debugId=<debug_id>
//# sourceMappingURL=<sourcemap_url>
```

소스 맵에도 `debug_id`라는 필드가 포함되어야 합니다:

`example_source_map.js.map`

```json
{
    ...
    "debug_id":"<debug_id>",
    ...
}
```

- [4. 아티팩트 번들 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#4-upload-artifact-bundle)

아티팩트에 Debug ID를 주입한 후, 다음 명령으로 업로드하세요:

```bash
// Paths can vary so check where your assets/public and App/public folder are.
sentry-cli sourcemaps upload /path/to/directory/android/app/src/main/assets/public
sentry-cli sourcemaps upload /path/to/directory/ios/App/public
```

#
- [아티팩트 번들이 업로드되었는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#verify-that-artifact-bundles-were-uploaded)

Sentry를 열고 **Project Settings > Source Maps**로 이동하세요. 탭형 탐색에서 “Artifact Bundles”를 선택하면 Sentry에 성공적으로 업로드된 모든 아티팩트 번들을 확인할 수 있습니다.

- [5. 애플리케이션 배포](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#5-deploy-your-application)

로컬 머신에서 이 가이드를 따라왔다면, 다음을 성공적으로 완료한 것입니다:

1. 애플리케이션의 빌드 프로세스를 실행해 축소된 소스 및 소스 맵 파일(아티팩트) 생성
2. 방금 생성한 아티팩트에 Debug ID 주입
3. 업로드 명령으로 해당 아티팩트를 Sentry에 업로드

마지막 단계는 1단계에서 만든 생성 아티팩트를 사용해 애플리케이션의 새 버전을 배포하는 것입니다. 이후의 각 배포에서 각 아티팩트에 debug ID를 자동으로 주입하고 Sentry에 직접 업로드할 수 있도록, **`sentry-cli`를 CI/CD Pipeline에 통합할 것을 강력히 권장합니다**.

- [선택 단계](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#optional-steps)

##### 경고

이 선택 단계를 정말로 필요하다고 결론 내렸을 때만 진행하세요. `release`와 `dist` 값을 사용하면 아티팩트 업로드를 더 구체적으로 만들 수 있지만, 전체 프로세스의 허용 범위가 줄어들어 Sentry가 코드 난독화 해제를 하지 못하게 될 수 있습니다.

#
- [아티팩트 번들에 `release` 연결](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#associating-release-with-artifact-bundle)

SDK 옵션에 `release` 속성을 제공하세요.

```javascript
Sentry.init({
  // This value must be identical to the release name specified during upload
  // with the `sentry-cli`.
  release: "<release_name>",
});
```

그다음 추가 `--release` 옵션과 함께 `sourcemaps upload` 명령을 실행하세요. `<release_name>`에 지정한 값이 SDK 옵션에 지정한 값과 동일한지 확인하세요.

```bash
// Paths can vary so check where your assets/public and App/public folder are.
sentry-cli sourcemaps upload --release=<release_name> /path/to/directory/android/app/src/main/assets/public
sentry-cli sourcemaps upload --release=<release_name> /path/to/directory/ios/App/public
```

`--release`와 함께 `upload`를 실행해도 **Sentry에 release가 자동으로 생성되지는 않습니다**. `Sentry.init`에 새 release를 설정한 첫 이벤트가 Sentry로 전송될 때까지 기다리거나, 별도 단계에서 [CLI를 사용해](https://docs.sentry.io/cli/releases.md) 같은 이름의 release를 생성하세요.

#
- [아티팩트 번들에 `dist` 연결](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#associating-dist-with-your-artifact-bundle)

`release`에 더해 업로드된 아티팩트에 `dist`도 추가해 업로드 파일의 배포 식별자를 설정할 수 있습니다. 이를 위해 추가 `--dist` 옵션과 함께 `sourcemaps upload` 명령을 실행하세요.

SDK 옵션에 `release` 및 `dist` 속성을 제공하세요.

```javascript
Sentry.init({
  // These values must be identical to the release and dist names specified during upload
  // with the `sentry-cli`.
  release: "<release_name>",
  dist: "<dist_name>",
});
```

배포 식별자는 단일 release 내에서 같은 이름을 가진 여러 파일을 구분하는 데 사용됩니다. `dist`는 빌드 또는 배포 변형을 구분하는 데 사용할 수 있습니다.

```bash

// Paths can vary so check where your assets/public and App/public folder are.
sentry-cli sourcemaps upload --release=<release_name> --dist=<dist_name> /path/to/directory/android/app/src/main/assets/public
sentry-cli sourcemaps upload --release=<release_name> --dist=<dist_name> /path/to/directory/ios/App/public
```

## [TSLib 다루기](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic-capacitor.md#dealing-with-tslib)

컴파일 중 TypeScript는 필요할 경우 생성하는 출력 파일에 런타임 의존성을 일부 주입합니다. 여기에는 함수 제너레이터용 폴리필이나 모든 환경에서 사용 가능하지 않을 수 있는 API 같은 것들이 포함될 수 있습니다. 하지만 원본 소스가 없기 때문에, 컴파일된 코드의 프레임을 원본 소스로 매핑하는 것은 불가능합니다.

우회 방법으로 TypeScript 컴파일러가 런타임 의존성을 직접 주입하는 대신 `tslib`(컴파일러 내부 구성 요소를 담은 자체 서드파티 패키지)를 사용하도록 설정해야 합니다. 소스 코드는 바꿀 필요 없이 TypeScript 설정 파일 내부만 변경하면 됩니다. 방법은 다음과 같습니다:

1. `package.json` 파일의 의존성에 `tslib`가 포함되어 있는지 확인합니다.
2. 완료되면 `tsconfig.json`의 `compilerOptions` 섹션에 두 항목을 추가합니다:

* `"noEmitHelpers": true` and -`"importHelpers": true`.

이제 끝입니다! 이제 내부 TypeScript 컴파일러 코드 스니펫을 포함해 모든 스택 트레이스 프레임의 소스 맵을 올바르게 매핑할 수 있습니다.

