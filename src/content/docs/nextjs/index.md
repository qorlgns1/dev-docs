---
title: "Next.js 문서"
description: "Next.js 문서에 오신 것을 환영합니다!"
---

출처 URL: https://nextjs.org/docs

# Next.js 문서

Next.js 문서에 오신 것을 환영합니다!

## Next.js란 무엇인가?

Next.js는 풀스택 웹 애플리케이션을 구축하기 위한 React 프레임워크입니다. React 컴포넌트로 사용자 인터페이스를 만들고, 추가 기능과 최적화는 Next.js가 제공합니다.

또한 번들러와 컴파일러 같은 하위 수준 도구를 자동으로 구성해 주므로, 제품을 만들고 빠르게 배포하는 데 집중할 수 있습니다.

개인 개발자든 더 큰 팀의 일원이든, Next.js는 상호작용적이고 동적이며 빠른 React 애플리케이션을 구축하는 데 도움을 줍니다.

## 문서 활용 방법

문서는 세 가지 섹션으로 구성되어 있습니다:

- [시작하기](https://nextjs.org/docs/app/getting-started): 새 애플리케이션을 만들고 핵심 Next.js 기능을 배우는 단계별 튜토리얼
- [가이드](https://nextjs.org/docs/app/guides): 특정 사용 사례를 다루며, 자신에게 필요한 내용을 골라 볼 수 있는 튜토리얼
- [API 레퍼런스](https://nextjs.org/docs/app/api-reference): 모든 기능에 대한 자세한 기술 레퍼런스

사이드바를 사용해 섹션을 탐색하거나, 검색(`Ctrl+K` 또는 `Cmd+K`)으로 원하는 페이지를 빠르게 찾으세요.

## App Router와 Pages Router

Next.js에는 두 가지 라우터가 있습니다:

- **App Router**: Server Components 같은 새로운 React 기능을 지원하는 최신 라우터
- **Pages Router**: 여전히 지원되며 계속 개선되고 있는 기존 라우터

사이드바 상단에는 [App Router](https://nextjs.org/docs/app) 문서와 [Pages Router](https://nextjs.org/docs/pages) 문서를 전환할 수 있는 드롭다운 메뉴가 있습니다.

### React 버전 처리

App Router와 Pages Router는 React 버전을 다르게 처리합니다:

- **App Router**: 새 React 릴리스 이전에 프레임워크에서 검증되는 최신 기능과 안정적인 React 19 변경 사항을 포함한 [React canary 릴리스](https://react.dev/blog/2023/05/03/react-canaries)를 기본으로 사용합니다.
- **Pages Router**: 프로젝트의 `package.json`에 설치된 React 버전을 사용합니다.

이 접근 방식은 App Router에서 새로운 React 기능이 안정적으로 동작하도록 하면서도, 기존 Pages Router 애플리케이션과의 하위 호환성을 유지합니다.

## 사전 지식

이 문서는 웹 개발에 대한 어느 정도의 익숙함을 가정합니다. 시작하기 전에 다음에 익숙하면 도움이 됩니다:

- HTML
- CSS
- JavaScript
- React

React가 처음이거나 복습이 필요하다면 [React Foundations 과정](https://nextjs.org/learn/react-foundations)과, 애플리케이션을 만들며 배우는 [Next.js Foundations 과정](https://nextjs.org/learn/dashboard-app)을 권장합니다.

## 접근성

스크린 리더를 사용할 때 최상의 경험을 위해 Firefox와 NVDA, 또는 Safari와 VoiceOver 조합을 권장합니다.

## 커뮤니티에 참여하세요

Next.js와 관련된 질문이 있다면 [GitHub Discussions](https://github.com/vercel/next.js/discussions), [Discord](https://discord.com/invite/bUG2bvbtHy), [X (Twitter)](https://x.com/nextjs), [Reddit](https://www.reddit.com/r/nextjs) 커뮤니티에서 언제든지 물어볼 수 있습니다.

## 다음 단계

첫 애플리케이션을 만들고 Next.js의 핵심 기능을 배워 보세요.

- [시작하기](https://nextjs.org/docs/app/getting-started) Next.js App Router로 풀스택 웹 애플리케이션을 만드는 방법을 알아보세요.
