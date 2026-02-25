---
title: 'LocalVariables | Next.js용 Sentry'
description: '이 통합은 Node.js 런타임에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables

# LocalVariables | Next.js용 Sentry

이 통합은 Node.js 런타임에서만 동작합니다.

*가져오기 이름: `Sentry.localVariablesIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

이 통합은 예외 프레임에 로컬 변수를 캡처합니다. 통합을 통해 로컬 변수 캡처를 활성화하려면 SDK 설정에서 `includeLocalVariable`을 `true`로 설정하세요.

```JavaScript
Sentry.init({
  includeLocalVariables: true,
});
```

로컬 변수 통합은 애플리케이션 코드(`in_app = true`)의 로컬 변수만 캡처합니다. `node_modules`에서 시작된 스택트레이스 프레임에는 로컬 변수가 첨부되지 않습니다.

##### ESM 관련 이슈

[해결되지 않은 Node.js 이슈](https://github.com/nodejs/node/issues/38439)로 인해, 현재 JavaScript 모듈(ESM)을 사용할 때 처리되지 않은 오류에 대해서는 로컬 변수를 캡처할 수 없습니다.

이 문제를 우회하려면 관련 코드를 try-catch 블록으로 감싸고, 오류와 함께 `captureException`을 호출해 Sentry가 로컬 변수를 캡처할 수 있도록 하세요.

```javascript
try {
  // Your code here
} catch (error) {
  Sentry.captureException(error);
}
```

##### 난독화된 변수

예외 프레임에 첨부된 난독화된 로컬 변수 이름은 현재 Sentry에서 역난독화할 수 없습니다. 이 기능을 추가하기 위한 sourcemaps 사양의 [활성 제안](https://github.com/tc39/source-map/blob/main/proposals/scopes.md)이 있습니다.

##### 디버거와의 비호환성

`includeLocalVariables`를 `true`로 설정하면 프로세스에 연결된 다른 디버거 세션에 영향을 줄 수 있으며, 실제로 영향을 줍니다. 이 통합은 throw된 예외에서 실행을 잠시 멈춰 스코프의 변수를 수집한 뒤 즉시 재개하는 방식으로 동작합니다. 따라서 이 통합이 활성화되어 있을 때 브레이크포인트가 건너뛰어지는 현상을 확인할 수 있습니다.

다른 디버거 세션을 사용할 예정이라면 `includeLocalVariables`를 `false`로 설정하는 것을 권장합니다.

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md#options)

- [`captureAllExceptions`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md#captureallexceptions)

*유형: `boolean`*

기본값은 `true`입니다. 활성화하면 처리된 예외와 처리되지 않은 예외 모두에 대해 로컬 변수를 캡처합니다.

* false인 경우, 처리되지 않은 예외에만 로컬 변수가 포함됩니다.
* true인 경우, 처리된 예외와 처리되지 않은 예외 모두에 로컬 변수가 포함됩니다.

모든 예외에 대해 로컬 변수를 캡처하면, 로컬 변수 수집을 위해 모든 throw 시점마다 디버거가 일시 정지하므로 비용이 클 수 있습니다.

이 기능이 앱 성능이나 처리량에 영향을 줄 가능성을 줄이기 위해, 이 기능에는 레이트 리밋이 적용됩니다. 레이트 리밋에 도달하면 타임아웃에 도달할 때까지 로컬 변수는 처리되지 않은 예외에 대해서만 캡처됩니다.

- [`maxExceptionsPerSecond`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md#maxexceptionspersecond)

*유형: `number`*

레이트 리밋이 트리거되기 전에 초당 로컬 변수를 캡처할 수 있는 최대 예외 수입니다.

