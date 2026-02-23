---
title: '파일 시스템 규칙: public'
description: 'Next.js는 루트 디렉터리의  폴더 아래에서 이미지와 같은 정적 파일을 제공할 수 있습니다.  안의 파일은 기본 URL()을 기준으로 코드에서 참조할 수 있습니다.'
---

# 파일 시스템 규칙: public | Next.js
출처 URL: https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder

[API Reference](https://nextjs.org/docs/pages/api-reference)[File-system conventions](https://nextjs.org/docs/pages/api-reference/file-conventions)public

페이지 복사

# public 폴더

최종 업데이트 2026년 2월 20일

Next.js는 루트 디렉터리의 `public` 폴더 아래에서 이미지와 같은 정적 파일을 제공할 수 있습니다. `public` 안의 파일은 기본 URL(`/`)을 기준으로 코드에서 참조할 수 있습니다.

예를 들어 `public/avatars/me.png` 파일은 `/avatars/me.png` 경로로 방문하여 볼 수 있습니다. 해당 이미지를 표시하는 코드는 다음과 같습니다:

avatar.js
[code]
    import Image from 'next/image'
     
    export function Avatar({ id, alt }) {
      return <Image src={`/avatars/${id}.png`} alt={alt} width="64" height="64" />
    }
     
    export function AvatarOfMe() {
      return <Avatar id="me" alt="A portrait of me" />
    }
[/code]

## 캐싱[](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder#caching)

`public` 폴더의 자산은 변경될 수 있으므로 Next.js는 안전하게 캐시할 수 없습니다. 기본으로 적용되는 캐싱 헤더는 다음과 같습니다:
[code] 
    Cache-Control: public, max-age=0
[/code]

## Robots, Favicons, 그리고 기타[](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder#robots-favicons-and-others)

이 폴더는 `robots.txt`, `favicon.ico`, Google 사이트 인증, 그리고 다른 정적 파일(`.html` 포함)에도 유용합니다. 하지만 동일한 이름의 정적 파일이 `pages/` 디렉터리에도 존재하면 오류가 발생하므로 주의하세요. [자세히 알아보기](https://nextjs.org/docs/messages/conflicting-public-file-page).

도움이 되었나요?

지원됨.

보내기
