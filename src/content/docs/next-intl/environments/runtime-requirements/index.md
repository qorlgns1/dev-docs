---
title: '런타임 요구사항'
description: '원본 URL: https://next-intl.dev/docs/environments/runtime-requirements'
---

원본 URL: https://next-intl.dev/docs/environments/runtime-requirements

[문서](https://next-intl.dev/docs/getting-started "Docs")[환경](https://next-intl.dev/docs/environments "Environments")런타임 요구사항

# 런타임 요구사항

## 브라우저[](https://next-intl.dev/docs/environments/runtime-requirements#browser)

`next-intl`의 소스 코드는 [Next.js가 지원하는](https://nextjs.org/docs/architecture/supported-browsers) 동일한 브라우저를 대상으로 컴파일됩니다.

사용 중인 기능에 따라, 대상 브라우저가 다음 API를 지원하는지 확인해야 합니다:

  * 기본 사용: `Intl.Locale` ([호환성](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#browser_compatibility))
  * 날짜 및 시간 포맷팅: `Intl.DateTimeFormat` ([호환성](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#browser_compatibility))
  * 숫자 포맷팅: `Intl.NumberFormat` ([호환성](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#browser_compatibility))
  * 복수형 처리: `Intl.PluralRules` ([호환성](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#browser_compatibility))
  * 상대 시간 포맷팅: `Intl.RelativeTimeFormat` ([호환성](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#browser_compatibility))
  * 목록 포맷팅: `Intl.ListFormat` ([호환성](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat#browser_compatibility))

필요한 API를 모두 지원하지 않는 브라우저를 대상으로 한다면, polyfill 사용을 고려하세요.

Cloudflare는 특정 로캘에 필요한 polyfill을 로드할 수 있는 [polyfill service](https://cdnjs.cloudflare.com/polyfill/)를 제공합니다.

**예시:**

IntlPolyfills.tsx
```
    import {useLocale} from 'next-intl';
    import Script from 'next/script';

    function IntlPolyfills() {
      const locale = useLocale();

      const polyfills = [
        'Intl',
        'Intl.Locale',
        'Intl.DateTimeFormat',
        `Intl.DateTimeFormat.~locale.${locale}`,
        `Intl.NumberFormat`,
        `Intl.NumberFormat.~locale.${locale}`,
        'Intl.PluralRules',
        `Intl.PluralRules.~locale.${locale}`,
        'Intl.RelativeTimeFormat',
        `Intl.RelativeTimeFormat.~locale.${locale}`,
        'Intl.ListFormat',
        `Intl.ListFormat.~locale.${locale}`
      ];

      return (
      );
    }
```

⚠️

polyfill service는 모든 로캘을 지원하지 않는다는 점에 유의하세요. 사용 가능한 polyfill 목록은 [`polyfill-service` repository](https://github.com/cdnjs/polyfill-service/tree/main/polyfill-libraries/3.101.0/polyfills/__dist)에서 확인할 수 있습니다(예: `Intl.DateTimeFormat.~locale.de-AT` 검색).

## Node.js[](https://next-intl.dev/docs/environments/runtime-requirements#nodejs)

관련된 모든 `Intl` API를 지원하기 위한 최소 버전은 **Node.js 13**입니다. 이 버전부터 필요한 API를 모두 사용할 수 있습니다.

