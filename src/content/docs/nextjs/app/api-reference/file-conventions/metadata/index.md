---
title: '파일 시스템 규칙: Metadata Files'
description: '이 문서 섹션에서는 메타데이터 파일 규칙을 다룹니다. 파일 기반 메타데이터는 라우트 세그먼트에 특수한 메타데이터 파일을 추가하여 정의할 수 있습니다.'
---

# 파일 시스템 규칙: Metadata Files | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/metadata

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)Metadata Files

Copy page

# Metadata Files API Reference

Last updated 2026년 2월 20일

이 문서 섹션에서는 **메타데이터 파일 규칙**을 다룹니다. 파일 기반 메타데이터는 라우트 세그먼트에 특수한 메타데이터 파일을 추가하여 정의할 수 있습니다.

각 파일 규칙은 정적 파일(예: `opengraph-image.jpg`) 또는 파일을 생성하는 코드를 사용하는 동적 변형(예: `opengraph-image.js`)으로 정의할 수 있습니다.

파일이 정의되면 Next.js는 해당 파일을 자동으로 제공하며(프로덕션에서는 캐싱을 위해 해시 적용) 애셋 URL, 파일 유형, 이미지 크기와 같은 올바른 메타데이터로 관련 head 요소를 업데이트합니다.

> **알아두면 좋은 점** :
>
>   * [`sitemap.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`icon.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons) 같은 특수 라우트 핸들러와 기타 [메타데이터 파일](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)은 기본적으로 캐시됩니다.
>   * [`proxy.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)와 함께 사용하는 경우, 메타데이터 파일을 제외하도록 [matcher를 구성](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher)해야 합니다.
>

- [favicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
  - 파일 규칙을 위한 API Reference.

- [manifest.json](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
  - 파일을 위한 API Reference.

- [opengraph-image and twitter-image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  - Open Graph Image과 Twitter Image 파일 규칙을 위한 API Reference.

- [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)
  - 파일을 위한 API Reference.

- [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  - 파일을 위한 API Reference.

Was this helpful?

supported.

Send
