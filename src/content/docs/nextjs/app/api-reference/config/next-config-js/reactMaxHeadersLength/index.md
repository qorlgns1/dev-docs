---
title: 'next.config.js: reactMaxHeadersLength'
description: '정적 렌더링 중에 React는 응답에 추가할 수 있는 헤더를 생성할 수 있습니다. 이를 통해 브라우저가 폰트, 스크립트, 스타일시트 같은 리소스를 미리 로드하도록 허용해 성능을 향상시킬 수 있습니다. 기본값은 이지만, 의  옵션을 구성하여 이 값을 재정의할 수 있습니다...'
---

# next.config.js: reactMaxHeadersLength | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength

# reactMaxHeadersLength

마지막 업데이트: 2026년 2월 20일

정적 렌더링 중에 React는 응답에 추가할 수 있는 헤더를 생성할 수 있습니다. 이를 통해 브라우저가 폰트, 스크립트, 스타일시트 같은 리소스를 미리 로드하도록 허용해 성능을 향상시킬 수 있습니다. 기본값은 `6000`이지만, `next.config.js`의 `reactMaxHeadersLength` 옵션을 구성하여 이 값을 재정의할 수 있습니다:

next.config.js
[code]
    module.exports = {
      reactMaxHeadersLength: 1000,
    }
[/code]

> **참고**: 이 옵션은 App Router에서만 사용할 수 있습니다.

브라우저와 서버 사이에 어떤 종류의 프록시가 있느냐에 따라 헤더가 잘릴 수 있습니다. 예를 들어 긴 헤더를 지원하지 않는 리버스 프록시를 사용하는 경우, 헤더가 잘리지 않도록 더 낮은 값을 설정해야 합니다.

보내기
