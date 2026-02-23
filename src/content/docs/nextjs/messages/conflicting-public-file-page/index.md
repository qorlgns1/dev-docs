---
title: '퍼블릭 파일과 페이지 파일 충돌'
description: '퍼블릭 파일 중 하나가 페이지 파일과 동일한 경로를 갖고 있어 지원되지 않습니다. 하나의 리소스만 해당 URL에 존재할 수 있으므로 퍼블릭 파일과 페이지 파일은 각각 고유해야 합니다.'
---

# 퍼블릭 파일과 페이지 파일 충돌 | Next.js

Source URL: https://nextjs.org/docs/messages/conflicting-public-file-page

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)퍼블릭 파일과 페이지 파일 충돌

# 퍼블릭 파일과 페이지 파일 충돌

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/conflicting-public-file-page#why-this-error-occurred)

퍼블릭 파일 중 하나가 페이지 파일과 동일한 경로를 갖고 있어 지원되지 않습니다. 하나의 리소스만 해당 URL에 존재할 수 있으므로 퍼블릭 파일과 페이지 파일은 각각 고유해야 합니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/conflicting-public-file-page#possible-ways-to-fix-it)

충돌을 일으키는 퍼블릭 파일 또는 페이지 파일 중 하나의 이름을 변경하세요.

퍼블릭 파일과 페이지 파일 사이의 충돌 예시

Folder structure
[code]
    public/
      hello
    pages/
      hello.js
[/code]

충돌이 없는 퍼블릭 파일과 페이지 파일

Folder structure
[code]
    public/
      hello.txt
    pages/
      hello.js
[/code]

## 유용한 링크[](https://nextjs.org/docs/messages/conflicting-public-file-page#useful-links)

  * [정적 파일 제공 문서](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder)

supported.

Send
