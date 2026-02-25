---
title: 'SystemJS | Next.js용 Sentry'
description: '이 가이드에서는  도구를 사용해 SystemJS의 소스 맵을 성공적으로 업로드하는 방법을 알아봅니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs

# SystemJS | Next.js용 Sentry

이 가이드에서는 `sentry-cli` 도구를 사용해 SystemJS의 소스 맵을 성공적으로 업로드하는 방법을 알아봅니다.

이 가이드는 다음을 전제로 합니다.

* `sentry-cli` 버전 >= `2.17.0`
* Sentry JavaScript SDK 버전 >= `7.47.0`

- [1. 소스 맵 생성](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#1-generate-source-maps)

먼저, 소스 맵을 출력하도록 SystemJS를 구성하세요.

```bash
builder.bundle("src/app.js", "dist/app.min.js", {
  minify: true,
  sourceMaps: true,
  sourceMapContents: true,
});
```

소스 맵을 생성하면 **공개적으로 노출될 수 있어**, 소스 코드가 유출될 가능성이 있습니다. 이를 방지하려면 서버에서 `.js.map` 파일에 대한 접근을 차단하도록 구성하거나, 애플리케이션 배포 전에 sourcemap을 삭제하세요.

- [2. Sentry CLI 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#2-configure-sentry-cli)

Sentry CLI 설치 방법은 여기에서 확인할 수 있습니다: [https://docs.sentry.io/cli/installation/](https://docs.sentry.io/cli/installation.md)

`sentry-cli` 구성에 대한 자세한 정보는 [Sentry CLI 구성 문서](https://docs.sentry.io/cli/configuration.md)를 참고하세요.

프로젝트에 맞게 `sentry-cli`가 구성되어 있는지 확인하세요. 이를 위해 환경 변수를 사용할 수 있습니다:

`.env.local`

```bash
SENTRY_ORG=___ORG_SLUG___
SENTRY_PROJECT=___PROJECT_SLUG___
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

- [3. 아티팩트에 Debug ID 주입](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#3-inject-debug-ids-into-artifacts)

Debug ID는 이벤트의 스택 프레임을 해당하는 난독화된 소스 및 소스 맵 파일과 매칭하는 데 사용됩니다. Debug ID에 대해 더 알고 싶다면 [What are Debug IDs](https://docs.sentry.io/platforms/javascript/sourcemaps/troubleshooting_js/debug-ids.md)를 참고하세요.

Debug ID를 주입하려면 다음 명령을 사용하세요:

```bash
sentry-cli sourcemaps inject /path/to/directory
```

#
- [아티팩트에 Debug ID가 주입되었는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#verify-debug-ids-were-injected-in-artifacts)

난독화된 소스 파일 끝에는 다음과 같이 `debugId`라는 주석이 포함되어 있어야 합니다:

`example_minified_file.js`

```javascript
...
//# debugId=<debug_id>
//# sourceMappingURL=<sourcemap_url>
```

소스 맵에는 다음과 같이 `debug_id`라는 필드가 포함되어 있어야 합니다:

`example_source_map.js.map`

```json
{
    ...
    "debug_id":"<debug_id>",
    ...
}
```

- [4. 아티팩트 번들 업로드](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#4-upload-artifact-bundle)

아티팩트에 Debug ID를 주입한 후, 다음 명령으로 업로드하세요.

```bash
sentry-cli sourcemaps upload /path/to/directory
```

#
- [아티팩트 번들이 업로드되었는지 확인](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#verify-that-artifact-bundles-were-uploaded)

Sentry를 열고 **Project Settings > Source Maps**로 이동하세요. 탭 탐색에서 “Artifact Bundles”를 선택하면 Sentry에 성공적으로 업로드된 모든 아티팩트 번들을 확인할 수 있습니다.

- [5. 애플리케이션 배포](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#5-deploy-your-application)

이 가이드를 로컬 머신에서 따라왔다면, 다음 작업을 성공적으로 완료한 것입니다:

1. 애플리케이션 빌드 프로세스를 실행하여 난독화된 소스 및 소스 맵 파일(아티팩트) 생성
2. 방금 생성한 아티팩트에 Debug ID 주입
3. 업로드 명령으로 해당 아티팩트를 Sentry에 업로드

마지막 단계는 1단계에서 생성한 아티팩트를 사용해 애플리케이션의 새 버전을 배포하는 것입니다. **각 후속 배포에서 각 아티팩트에 debug ID를 자동으로 주입하고 이를 Sentry에 직접 업로드할 수 있도록, `sentry-cli`를 CI/CD 파이프라인에 통합할 것을 강력히 권장합니다.**

- [선택 단계](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#optional-steps)

##### 경고

이 선택 단계는 반드시 필요하다고 결론 내린 경우에만 진행하세요. `release` 및 `dist` 값을 사용하면 아티팩트 업로드를 더 구체적으로 만들 수 있지만, 전체 프로세스의 허용 범위가 줄어들어 Sentry가 코드를 난독화 해제하지 못할 수 있습니다.

#
- [아티팩트 번들에 `release` 연결](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#associating-release-with-artifact-bundle)

SDK 옵션에 `release` 속성을 제공하세요.

```javascript
Sentry.init({
  // This value must be identical to the release name specified during upload
  // with the `sentry-cli`.
  release: "<release_name>",
});
```

그다음 추가 `--release` 옵션과 함께 `sourcemaps upload` 명령을 실행하세요. `<release_name>`에 지정한 값이 SDK 옵션에 지정한 값과 동일한지 반드시 확인하세요.

```bash
sentry-cli sourcemaps upload --release=<release_name> /path/to/directory
```

`--release`와 함께 `upload`를 실행해도 **Sentry에서 릴리스가 자동 생성되지는 않습니다**. `Sentry.init`에서 새 릴리스를 설정한 첫 이벤트가 Sentry로 전송될 때까지 기다리거나, 별도 단계에서 [CLI](https://docs.sentry.io/cli/releases.md)로 동일한 이름의 릴리스를 생성하세요.

#
- [아티팩트 번들에 `dist` 연결](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/systemjs.md#associating-dist-with-artifact-bundle)

`release`에 더해 업로드된 아티팩트에 `dist`도 추가하여 업로드 파일의 배포 식별자를 설정할 수 있습니다. 이를 위해 추가 `--dist` 옵션과 함께 `sourcemaps upload` 명령을 실행하세요.

SDK 옵션에 `release` 및 `dist` 속성을 제공하세요.

```javascript
Sentry.init({
  // These values must be identical to the release and dist names specified during upload
  // with the `sentry-cli`.
  release: "<release_name>",
  dist: "<dist_name>",
});
```

배포 식별자는 단일 릴리스 내에서 동일한 이름을 가진 여러 파일을 구분하는 데 사용됩니다. `dist`는 빌드 또는 배포 변형을 구분하는 데 사용할 수 있습니다.

```bash
sentry-cli sourcemaps upload --release=<release_name> --dist=<dist_name> /path/to/directory
```

