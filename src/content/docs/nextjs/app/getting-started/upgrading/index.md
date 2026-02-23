---
title: '시작하기: 업그레이드'
description: '최신 버전의 Next.js로 업데이트하려면  명령을 사용할 수 있습니다.'
---

# 시작하기: 업그레이드 | Next.js

출처 URL: https://nextjs.org/docs/app/getting-started/upgrading

# 업그레이드

마지막 업데이트 2026년 2월 20일

## 최신 버전[](https://nextjs.org/docs/app/getting-started/upgrading#latest-version)

최신 버전의 Next.js로 업데이트하려면 `upgrade` 명령을 사용할 수 있습니다.

pnpmnpmyarnbun

터미널
[code]
    pnpm next upgrade
[/code]

Next.js 15 이하 버전은 `upgrade` 명령을 지원하지 않으므로 별도의 패키지를 사용해야 합니다.

터미널
[code]
    npx @next/codemod@canary upgrade latest
[/code]

수동 업그레이드를 선호한다면 최신 Next.js와 React 버전을 설치하세요.

pnpmnpmyarnbun

터미널
[code]
    pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
[/code]

## 카나리 버전[](https://nextjs.org/docs/app/getting-started/upgrading#canary-version)

최신 카나리 버전으로 업데이트하려면 먼저 최신 안정 버전의 Next.js를 사용하면서 모든 것이 정상 작동하는지 확인하세요. 그런 다음 다음 명령을 실행합니다.

pnpmnpmyarnbun

터미널
[code]
    pnpm add next@canary
[/code]

### 카나리에서 제공되는 기능[](https://nextjs.org/docs/app/getting-started/upgrading#features-available-in-canary)

현재 카나리에서 제공되는 기능은 다음과 같습니다.

**Authentication** :

  * [`forbidden`](https://nextjs.org/docs/app/api-reference/functions/forbidden)
  * [`unauthorized`](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
  * [`forbidden.js`](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
  * [`unauthorized.js`](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
  * [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)

## 버전 가이드

심층 업그레이드 지침은 버전 가이드를 참조하세요.

- [버전 16](https://nextjs.org/docs/app/guides/upgrading/version-16)
  - Next.js 애플리케이션을 버전 15에서 16으로 업그레이드하세요.

- [버전 15](https://nextjs.org/docs/app/guides/upgrading/version-15)
  - Next.js 애플리케이션을 버전 14에서 15로 업그레이드하세요.

- [버전 14](https://nextjs.org/docs/app/guides/upgrading/version-14)
  - Next.js 애플리케이션을 버전 13에서 14로 업그레이드하세요.

보내기
