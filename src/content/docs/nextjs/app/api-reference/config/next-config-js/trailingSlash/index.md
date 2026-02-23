---
title: 'next.config.js: trailingSlash'
description: '기본적으로 Next.js는 슬래시가 붙은 URL을 슬래시가 없는 대응 경로로 리디렉션합니다. 예를 들어 은 으로 이동합니다. 이 동작을 반대로 설정해, 슬래시가 없는 URL을 슬래시가 붙은 경로로 리디렉션하도록 구성할 수 있습니다.'
---

# next.config.js: trailingSlash | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash

# trailingSlash

2026년 2월 20일 업데이트

기본적으로 Next.js는 슬래시가 붙은 URL을 슬래시가 없는 대응 경로로 리디렉션합니다. 예를 들어 `/about/`은 `/about`으로 이동합니다. 이 동작을 반대로 설정해, 슬래시가 없는 URL을 슬래시가 붙은 경로로 리디렉션하도록 구성할 수 있습니다.

`next.config.js`를 열고 `trailingSlash` 설정을 추가하세요:

next.config.js
```
    module.exports = {
      trailingSlash: true,
    }
```

이 옵션을 설정하면 `/about` 같은 URL은 `/about/`으로 리디렉션됩니다.

`trailingSlash: true`를 사용할 때는 특정 URL이 예외로 처리되어 슬래시가 추가되지 않습니다.

  * 확장자를 가진 정적 파일 URL
  * `.well-known/` 이하의 모든 경로

예를 들어 `/file.txt`, `images/photos/picture.png`, `.well-known/subfolder/config.json` 같은 URL은 변경되지 않습니다.

[`output: "export"`](https://nextjs.org/docs/app/guides/static-exports) 구성과 함께 사용하면 `/about` 페이지는 기본값인 `/about.html` 대신 `/about/index.html`을 출력합니다.

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash#version-history)

Version| Changes
---|---
`v9.5.0`| `trailingSlash` 추가.

유용했나요?

보내기