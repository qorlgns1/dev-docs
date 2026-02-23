---
title: '캐시가 감지되지 않음'
description: '연속 통합(CI) 환경에서 Next.js 빌드가 트리거됐지만, 캐시가 감지되지 않았습니다.'
---

# 캐시가 감지되지 않음 | Next.js

Source URL: https://nextjs.org/docs/messages/no-cache

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)캐시가 감지되지 않음

# 캐시가 감지되지 않음

## 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-cache#why-this-error-occurred)

연속 통합(CI) 환경에서 Next.js 빌드가 트리거됐지만, 캐시가 감지되지 않았습니다.

이로 인해 빌드 속도가 느려지고, 빌드 간에 Next.js의 클라이언트 번들 파일 시스템 캐시에 악영향을 줄 수 있습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-cache#possible-ways-to-fix-it)

> **Note** : 새로운 프로젝트이거나 CI에서 처음 빌드하는 경우라면 이 오류를 무시해도 됩니다. 다만, 동일한 문제가 계속 발생하지 않도록 확인하고 재발 시 해결해야 합니다!

Next.js 캐시가 빌드 사이에 유지되도록 [CI Build Caching](https://nextjs.org/docs/pages/guides/ci-build-caching)의 지침을 따르세요.

Was this helpful?

supported.

Send