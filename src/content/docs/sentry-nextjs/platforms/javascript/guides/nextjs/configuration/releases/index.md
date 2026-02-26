---
title: 'Releases & Health | Sentry for Next.js'
description: '릴리스는 environment에 배포되는 코드의 버전입니다. Sentry에 릴리스 정보를 제공하면 다음을 할 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases

# Releases & Health | Sentry for Next.js

릴리스는 [environment](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/environments.md)에 배포되는 코드의 버전입니다. Sentry에 릴리스 정보를 제공하면 다음을 할 수 있습니다.

* 새 릴리스에서 도입된 이슈와 회귀를 파악
* 어떤 커밋이 이슈를 유발했는지, 누가 책임 가능성이 높은지 예측
* 커밋 메시지에 이슈 번호를 포함해 이슈 해결
* 코드가 배포될 때 이메일 알림 수신

또한 릴리스는 난독화된 JavaScript에 [source maps](https://docs.sentry.io/platforms/javascript/sourcemaps.md)를 적용해 원본의 변환되지 않은 소스 코드를 확인하는 데 사용됩니다.

## [Bind the Version](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#bind-the-version)

SDK를 초기화할 때 release ID(흔히 "version"이라고 부름)를 포함하세요.

알아두어야 할 릴리스 이름 제한과 규칙이 있습니다. 자세한 내용은 [Learn more about naming releases](https://docs.sentry.io/product/releases/naming-releases.md)를 참고하세요.

릴리스는 다양한 시스템에서 자동 생성될 수도 있습니다. 예를 들어 source map 업로드 시, 또는 release 태그가 지정된 이벤트를 일부 클라이언트가 수집할 때 생성됩니다. 따라서 애플리케이션을 빌드하고 배포할 때 릴리스 이름을 설정하는 것이 중요합니다. 자세한 내용은 [Releases](https://docs.sentry.io/platform-redirect.md?next=/configuration/releases/) 문서를 참고하세요.

## [Setting a Release](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#setting-a-release)

sourcemap이 올바른 릴리스에 연결되도록 Sentry의 Next.js SDK에서 SENTRY\_RELEASE 환경 변수를 설정하세요.

릴리스 이름(또는 버전)을 코드에서 사용할 수 있게 만드는 방법은 자유롭게 선택할 수 있습니다. 예를 들어 빌드 과정이나 초기 시작 시점에 설정되는 환경 변수를 사용할 수 있습니다.

릴리스 이름을 설정하면 각 이벤트에 해당 릴리스 이름이 태그됩니다. 더 많은 기능을 활용하려면 해당 릴리스 이름의 이벤트를 전송하기 전에 새 릴리스 정보를 Sentry에 먼저 알려주는 것을 권장합니다. 자세한 내용은 [Releases](https://docs.sentry.io/product/releases.md) 문서를 참고하세요.

새 릴리스를 Sentry에 알리지 않으면, Sentry는 해당 release ID가 붙은 이벤트를 처음 볼 때 시스템에 릴리스 엔터티를 자동으로 생성합니다.

SDK를 구성한 후에는 저장소 통합을 설치하거나 커밋 메타데이터를 수동으로 Sentry에 제공할 수 있습니다. 통합, 커밋 연결, 릴리스 배포 시점 알림에 대한 자세한 내용은 [setting up releases](https://docs.sentry.io/product/releases/setup.md) 문서를 참고하세요.

## [Release Health](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#release-health)

사용자 채택, 애플리케이션 사용량, [crashes](https://docs.sentry.io/product/releases/health.md#crashes) 비율, [session data](https://docs.sentry.io/product/releases/health.md#sessions)를 관찰하여 [health of releases](https://docs.sentry.io/product/releases/health.md)를 모니터링하세요. Release health는 사용자 경험과 관련된 크래시 및 버그의 영향을 파악하게 해주며, [Release Details](https://docs.sentry.io/product/releases/release-details.md)의 그래프와 필터를 통해 새 이슈마다 나타나는 추세를 보여줍니다.

릴리스 헬스를 모니터링하기 위해 SDK는 세션 데이터를 전송합니다.

- [Sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#sessions)

세션은 사용자와 애플리케이션 간 상호작용을 나타냅니다. 세션에는 타임스탬프, 상태(세션이 정상인지 또는 크래시가 발생했는지)가 포함되며, 항상 특정 릴리스에 연결됩니다. 대부분의 Sentry SDK는 세션을 자동으로 관리할 수 있습니다.

기본적으로 JavaScript Browser SDK는 세션을 전송합니다. 페이지 로드마다 세션이 생성됩니다. 단일 페이지 애플리케이션의 경우 탐색 변경(History API)마다 새 세션을 생성합니다.

기본 세션 처리를 비활성화하려면 `BrowserSession` integration을 비활성화하세요.

```javascript
Sentry.init({
  integrations: (defaultIntegrations) => {
    return defaultIntegrations.filter(
      (integration) => integration.name !== "BrowserSession",
    );
  },
});
```

기본적으로 Node.js 기반 SDK는 세션을 전송합니다. 세션은 들어오는 각 요청마다 생성됩니다. 기본 세션 처리를 비활성화하려면 `httpIntegration`에서 `trackIncomingRequestsAsSessions: false`를 설정하세요.

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  integrations: [
    httpIntegration({ trackIncomingRequestsAsSessions: false }),
  ],
});
```

세션은 다음과 같이 표시됩니다.

* 전역 핸들러까지 전파된 *unhandled error* 또는 *unhandled promise rejection*이 있으면 `crashed`
* SDK가 예외를 포함한 이벤트를 캡처하면 `errored`(수동으로 캡처한 오류 포함)

사용자 crash free rate 비율이나 특정 릴리스를 채택한 사용자 수 같은 사용자 채택 데이터를 받으려면, SDK 초기화 시 [`initialScope`](https://docs.sentry.io/platforms/javascript/configuration/options.md#initial-scope)에 사용자를 설정하세요.

세션을 수동으로 캡처하는 방법에 대한 자세한 내용은 [Session APIs](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#sessions)를 참고하세요.

