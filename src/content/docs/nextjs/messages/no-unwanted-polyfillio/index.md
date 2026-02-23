---
title: '원치 않는 Polyfill.io 없음'
description: '> Polyfill.io에서 중복된 폴리필을 방지하세요.'
---

# 원치 않는 Polyfill.io 없음 | Next.js

Source URL: https://nextjs.org/docs/messages/no-unwanted-polyfillio

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)원치 않는 Polyfill.io 없음

# 원치 않는 Polyfill.io 없음

> Polyfill.io에서 중복된 폴리필을 방지하세요.

## 왜 이 오류가 발생했나요?[](https://nextjs.org/docs/messages/no-unwanted-polyfillio#why-this-error-occurred)

Polyfill.io의 폴리필을 사용하면서 Next.js에 이미 포함된 폴리필을 다시 추가하고 있습니다. 이는 페이지 용량을 불필요하게 증가시켜 로딩 성능에 영향을 줄 수 있습니다.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/no-unwanted-polyfillio#possible-ways-to-fix-it)

모든 중복 폴리필을 제거하세요. 폴리필을 추가해야 하지만 Next.js에 이미 포함되었는지 확신할 수 없다면 [지원되는 브라우저 및 기능](https://nextjs.org/docs/architecture/supported-browsers) 목록을 확인하세요.

## 유용한 링크[](https://nextjs.org/docs/messages/no-unwanted-polyfillio#useful-links)

  * [지원되는 브라우저 및 기능](https://nextjs.org/docs/architecture/supported-browsers)