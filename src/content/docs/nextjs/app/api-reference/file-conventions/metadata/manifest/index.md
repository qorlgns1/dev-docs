---
title: '메타데이터 파일: manifest.json'
description: '소스 URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest'
---

# 메타데이터 파일: manifest.json | Next.js

소스 URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest

[파일 시스템 규칙](https://nextjs.org/docs/app/api-reference/file-conventions)[메타데이터 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)manifest.json

페이지 복사

# manifest.json

마지막 업데이트 2026년 2월 20일

브라우저에 웹 애플리케이션 정보를 제공하려면 `app` 디렉터리의 **루트**에 [Web Manifest Specification](https://developer.mozilla.org/docs/Web/Manifest)을 준수하는 `manifest.(json|webmanifest)` 파일을 추가하거나 생성하세요.

## 정적 Manifest 파일[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#static-manifest-file)

app/manifest.json | app/manifest.webmanifest
[code]
    {
      "name": "My Next.js Application",
      "short_name": "Next.js App",
      "description": "An application built with Next.js",
      "start_url": "/"
      // ...
    }
[/code]

## Manifest 파일 생성[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#generate-a-manifest-file)

[`Manifest` 객체](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#manifest-object)를 반환하는 `manifest.js` 또는 `manifest.ts` 파일을 추가하세요.

> 알아두면 좋은 점: `manifest.js`는 특별한 Route Handler이며 [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis)나 [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) 옵션을 사용하지 않는 한 기본적으로 캐시됩니다.

app/manifest.ts

JavaScriptTypeScript
[code]
    import type { MetadataRoute } from 'next'
     
    export default function manifest(): MetadataRoute.Manifest {
      return {
        name: 'Next.js App',
        short_name: 'Next.js App',
        description: 'Next.js App',
        start_url: '/',
        display: 'standalone',
        background_color: '#fff',
        theme_color: '#fff',
        icons: [
          {
            src: '/favicon.ico',
            sizes: 'any',
            type: 'image/x-icon',
          },
        ],
      }
    }
[/code]

### Manifest 객체[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#manifest-object)

manifest 객체에는 새로운 웹 표준으로 인해 변경될 수 있는 다양한 옵션이 포함되어 있습니다. 모든 최신 옵션 정보는 [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin)를 사용하는 경우 코드 편집기에서 `MetadataRoute.Manifest` 타입을 참고하거나 [MDN](https://developer.mozilla.org/docs/Web/Manifest) 문서를 확인하세요.

도움이 되었나요?

지원됨.

보내기
