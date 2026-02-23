---
title: '파일 시스템 규칙: public'
description: '마지막 업데이트: 2026년 2월 20일'
---

# 파일 시스템 규칙: public | Next.js

출처 URL: https://nextjs.org/docs/app/api-reference/file-conventions/public-folder

[API 레퍼런스](https://nextjs.org/docs/app/api-reference)[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)public

페이지 복사

# public 폴더

마지막 업데이트: 2026년 2월 20일

Next.js는 루트 디렉터리의 `public` 폴더 아래에서 이미지 같은 정적 파일을 제공할 수 있습니다. `public` 내부의 파일은 기본 URL(`/`)부터 시작하여 코드에서 참조할 수 있습니다.

예를 들어, `public/avatars/me.png` 파일은 `/avatars/me.png` 경로로 방문해 볼 수 있습니다. 해당 이미지를 표시하는 코드는 다음과 같을 수 있습니다:

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

## 캐싱[](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder#caching)

`public` 폴더의 에셋은 변경될 수 있으므로 Next.js는 안전하게 캐시할 수 없습니다. 기본으로 적용되는 캐싱 헤더는 다음과 같습니다:
[code] 
    Cache-Control: public, max-age=0
[/code]

## 로봇, 파비콘 등[](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder#robots-favicons-and-others)

`robots.txt`, `favicon.ico` 같은 정적 메타데이터 파일의 경우 `app` 폴더 내부에 있는 [특수 메타데이터 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)을 사용해야 합니다.

도움이 되었나요?

지원됨.

보내기
