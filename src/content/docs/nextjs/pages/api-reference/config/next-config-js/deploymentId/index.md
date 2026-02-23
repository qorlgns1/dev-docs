---
title: 'next.config.js 옵션: deploymentId'
description: '옵션을 사용하면 배포에 대한 식별자를 설정할 수 있습니다. 이 식별자는 버전 스큐 보호와 롤링 배포 중 캐시 무효화에 사용됩니다.'
---

# next.config.js 옵션: deploymentId | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId

[Configuration](https://nextjs.org/docs/pages/api-reference/config)[next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)deploymentId

Copy page

# deploymentId

Last updated February 20, 2026

`deploymentId` 옵션을 사용하면 배포에 대한 식별자를 설정할 수 있습니다. 이 식별자는 [버전 스큐](https://nextjs.org/docs/app/guides/self-hosting#version-skew) 보호와 롤링 배포 중 캐시 무효화에 사용됩니다.

next.config.js
```js
module.exports = {
  deploymentId: 'my-deployment-id',
}
```

`NEXT_DEPLOYMENT_ID` 환경 변수를 사용해 배포 ID를 설정할 수도 있습니다:
```
NEXT_DEPLOYMENT_ID=my-deployment-id next build
```

> **알아두면 좋아요:** 둘 다 설정되어 있으면, `next.config.js`의 `deploymentId` 값이 `NEXT_DEPLOYMENT_ID` 환경 변수보다 우선합니다.

## 작동 방식[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#how-it-works)

`deploymentId`를 구성하면 Next.js는 다음을 수행합니다:

  1. 정적 자산 URL(JavaScript, CSS, 이미지)에 `?dpl=<deploymentId>`를 추가합니다.
  2. 클라이언트 측 내비게이션 요청에 `x-deployment-id` 헤더를 추가합니다.
  3. 내비게이션 응답에 `x-nextjs-deployment-id` 헤더를 추가합니다.
  4. `<html>` 요소에 `data-dpl-id` 속성을 주입합니다.

클라이언트가 자신의 배포 ID와 서버(응답 헤더를 통해)의 배포 ID가 일치하지 않는 것을 감지하면, 클라이언트 측 내비게이션 대신 하드 내비게이션(전체 페이지 새로고침)을 트리거합니다. 이를 통해 사용자는 항상 동일한 배포 버전의 자산을 받게 됩니다.

> **알아두면 좋아요:** Next.js는 들어오는 요청의 `?dpl=` 쿼리 매개변수를 읽지 않습니다. 이 쿼리 매개변수는 라우팅이 아니라 캐시 무효화(브라우저와 CDN이 최신 자산을 가져오도록 보장)를 위한 것입니다. 버전 인식 라우팅이 필요하면, 호스팅 제공자나 CDN 문서를 참고하여 배포 기반 라우팅을 구현하세요.

## 사용 사례[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#use-cases)

### 롤링 배포[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#rolling-deployments)

롤링 배포 동안 일부 서버 인스턴스는 새 버전을 실행하고, 다른 인스턴스는 이전 버전을 계속 실행할 수 있습니다. 배포 ID가 없으면 사용자가 이전 자산과 새 자산을 섞어 받아 오류가 발생할 수 있습니다.

배포당 일관된 `deploymentId`를 설정하면 다음을 보장합니다:

  * 클라이언트는 항상 해당 배포 버전의 자산을 요청합니다.
  * 불일치가 감지되면 올바른 자산을 가져오기 위해 전체 새로고침을 트리거합니다.

### 다중 서버 환경[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#multi-server-environments)

로드 밸런서 뒤에서 Next.js 애플리케이션의 여러 인스턴스를 실행할 때, 동일한 배포에 속한 모든 인스턴스는 동일한 `deploymentId`를 사용해야 합니다.

next.config.js
```js
module.exports = {
  deploymentId: process.env.DEPLOYMENT_VERSION || process.env.GIT_SHA,
}
```

## 버전 기록[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#version-history)

Version| Changes  
---|---  
`v14.1.4`| `deploymentId`가 최상위 구성 옵션으로 안정화되었습니다.  
`v13.4.10`| `experimental.deploymentId`가 도입되었습니다.  
  
## 관련 문서[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#related)

  * [Self-Hosting - Version Skew](https://nextjs.org/docs/app/guides/self-hosting#version-skew)
  * [generateBuildId](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)



Was this helpful?

supported.

Send
