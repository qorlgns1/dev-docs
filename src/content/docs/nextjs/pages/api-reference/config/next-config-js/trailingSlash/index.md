---
title: 'next.config.js Options: trailingSlash'
description: '기본적으로 Next.js는 슬래시로 끝나는 URL을 슬래시가 없는 대응 URL로 리다이렉트합니다. 예를 들어 는 으로 리다이렉트됩니다. 이 동작을 반대로 설정해, 슬래시 없이 끝나는 URL을 슬래시가 붙은 대응 URL로 리다이렉트하도록 구성할 수 있습니다.'
---

# next.config.js Options: trailingSlash | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash

Copy page

# trailingSlash

마지막 업데이트 2026년 2월 20일

기본적으로 Next.js는 슬래시로 끝나는 URL을 슬래시가 없는 대응 URL로 리다이렉트합니다. 예를 들어 `/about/`는 `/about`으로 리다이렉트됩니다. 이 동작을 반대로 설정해, 슬래시 없이 끝나는 URL을 슬래시가 붙은 대응 URL로 리다이렉트하도록 구성할 수 있습니다.

`next.config.js`를 열고 `trailingSlash` 설정을 추가하세요:

next.config.js
```
    module.exports = {
      trailingSlash: true,
    }
```

이 옵션을 설정하면 `/about`과 같은 URL이 `/about/`으로 리다이렉트됩니다.

`trailingSlash: true`를 사용할 때에는 특정 URL이 예외로 처리되어 슬래시가 추가되지 않습니다:

  * 확장자를 가진 파일 등 정적 파일 URL.
  * `.well-known/` 이하의 모든 경로.

예를 들어 `/file.txt`, `images/photos/picture.png`, `.well-known/subfolder/config.json`과 같은 URL은 변경되지 않습니다.

[`output: "export"`](https://nextjs.org/docs/app/guides/static-exports) 설정과 함께 사용하면 `/about` 페이지는 기본 `/about.html` 대신 `/about/index.html`을 출력합니다.

## Version History[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash#version-history)

Version| Changes
---|---
`v9.5.0`| `trailingSlash`가 추가되었습니다.

Was this helpful?

supported.

Send