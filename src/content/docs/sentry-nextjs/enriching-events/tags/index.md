---
title: '태그 | Next.js용 Sentry'
description: '이벤트의 모든 태그는 물론, 태그의 빈도와 Sentry가 해당 태그를 마지막으로 확인한 시점까지 자동으로 인덱싱됩니다. 또한 고유 태그 수를 추적하며, 다양한 이슈의 핫스팟을 파악하는 데 도움을 줍니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/tags

# 태그 | Next.js용 Sentry

**태그(Tags)**는 인덱싱되고 검색 가능한 키/값 문자열 쌍입니다. 태그는 sentry.io의 필터, 태그 분포 맵 같은 기능을 구동합니다. 또한 태그를 사용하면 관련 이벤트에 빠르게 접근하고, 이벤트 집합의 태그 분포를 확인할 수 있습니다. 태그의 일반적인 사용 예로는 hostname, platform version, user language가 있습니다.

이벤트의 모든 태그는 물론, 태그의 빈도와 Sentry가 해당 태그를 마지막으로 확인한 시점까지 자동으로 인덱싱됩니다. 또한 고유 태그 수를 추적하며, 다양한 이슈의 핫스팟을 파악하는 데 도움을 줍니다.

*태그 키(Tag keys)*는 최대 32자까지 가능하며, 문자(`a-zA-Z`), 숫자(`0-9`), 밑줄(`_`), 마침표(`.`), 콜론(`:`), 대시(`-`)만 포함할 수 있습니다.

태그 키에는 공백을 사용할 수 없습니다.

*태그 값(Tag values)*은 최대 200자까지 가능하며, 줄바꿈(`\n`) 문자를 포함할 수 없습니다.

태그 정의는 간단하며, [격리 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md)에 바인딩되어 스코프 내의 이후 모든 이벤트에 동일한 태그가 포함되도록 보장합니다.

먼저 평소와 같이 SDK를 import해야 합니다.

```javascript
import * as Sentry from "@sentry/nextjs";
```

태그를 정의합니다.

```javascript
Sentry.setTag("page_locale", "de-at");
```

일부 태그는 Sentry가 자동으로 설정합니다. 이러한 [태그](https://docs.sentry.io/concepts/search/searchable-properties.md#search-properties)를 덮어쓰지 않기를 강력히 권장합니다. 대신 조직의 명명 규칙에 맞춰 태그 이름을 지정하세요. 자동으로 설정된 태그를 덮어썼다면, 검색 시 [명시적 태그 문법](https://docs.sentry.io/concepts/search.md#explicit-tag-syntax)을 사용해야 합니다.

태그가 포함된 데이터를 보내기 시작하면, sentry.io에 로그인했을 때 해당 내용을 확인할 수 있습니다. 여기에서 Project 페이지 사이드바의 필터, 이벤트 내 요약 정보, 그리고 집계된 이벤트의 Tags 페이지를 볼 수 있습니다.

