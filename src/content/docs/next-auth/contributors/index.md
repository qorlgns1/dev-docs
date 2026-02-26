---
title: "코어 팀[](https://next-auth.js.org/contributors#core-team)"
description: "Auth.js를 오픈 소스 프로젝트로 유지하는 일은 매우 어려운 작업입니다. 코어 팀원 모두 각자의 본업이 있으며, 이 라이브러리는 우리의 여가 시간에 선의로 유지·개발되고 있습니다. 후원은 코어 팀이 궁극적으로 Auth.js에 전업으로 참여해 더 많은 기능과 더 나은..."
---

Source URL: https://next-auth.js.org/contributors

# 기여자

Auth.js를 오픈 소스 프로젝트로 유지하는 일은 매우 어려운 작업입니다. 코어 팀원 모두 각자의 본업이 있으며, 이 라이브러리는 우리의 여가 시간에 선의로 유지·개발되고 있습니다. 후원은 코어 팀이 궁극적으로 Auth.js에 전업으로 참여해 더 많은 기능과 더 나은 개발자 경험을 제공할 수 있도록 도와줍니다!

![](https://next-auth.js.org/img/etc/opencollective-logomark.svg)![](https://next-auth.js.org/img/etc/opencollective-wordmark.svg)

우리는 [Open Collective](https://opencollective.com/nextauth)에서 만나실 수 있습니다. 기존의 모든 기여자분들께 깊이 감사드리며, 여러분이나 여러분의 회사가 함께해 주신다면 매우 기쁠 것입니다.

## 코어 팀[](https://next-auth.js.org/contributors#core-team)

이분들이 없었다면, 이 프로젝트가 해당 분야에서 가장 널리 사용되는 인증 라이브러리 중 하나로 성장할 수 없었을 것입니다.

- [Balázs Orbán](https://github.com/balazsorban44) \- 리드 메인터이너
- [Thang Vu](https://github.com/ThangHuuVu) \- 메인터이너
- [Nico Domino](https://github.com/ndom91) \- 메인터이너
- [Lluis Agusti](https://github.com/lluia) \- 메인터이너

## 특별한 감사[](https://next-auth.js.org/contributors#special-thanks)

우리가 기반으로 삼고 있는 고품질 OAuth 라이브러리와 피드백을 제공해 준 Filip Skokan, 원래의 provider 설정 대부분을 만들어 준 Lori Karikari, 원래 Prisma Adapter를 만들어 준 Fredrik Pettersen, Sign in with Apple 지원을 추가해 준 Gerald Nolan, 초기 테스트 자동화를 작업해 준 Jefferson Bledsoe, 그리고 API Reference 문서 작업/가이드를 제공해 준 Tom Grey께 특별히 감사드립니다.

- [Filip Skokan](https://github.com/panva)
- [Lori Karikari](https://github.com/LoriKarikari)
- [Fredrik Pettersen](https://github.com/Fumler)
- [Gerald Nolan](https://github.com/geraldnolan)
- [Jefferson Bledsoe](https://github.com/JeffersonBledsoe)
- [Tom Grey](https://github.com/tgreyuk)

## 기타 기여자[](https://next-auth.js.org/contributors#other-contributors)

오늘날의 Auth.js는 수많은 개별 기여자들의 노력 덕분에 가능했습니다.

Auth.js를 함께 만들어 주신 [수십 명의 개별 기여자](https://github.com/nextauthjs/next-auth/graphs/contributors)분들께 감사드립니다.

## 역사[](https://next-auth.js.org/contributors#history)

### 2016 – 초기 릴리스[](https://next-auth.js.org/contributors#2016--initial-release)

NextAuth.js는 2016년에 [Iain Collins](https://github.com/iaincollins)가 [Next.js](https://nextjs.org/) 전용 인증 프레임워크로 처음 개발했습니다.

### 2020 – 리팩터링 및 정리[](https://next-auth.js.org/contributors#2020--refactor-and-clean-up)

NextAuth.js는 서버리스, MySQL, Postgres, MongoDB, JSON Web Tokens, 그리고 12개가 넘는 인증 provider에 대한 내장 지원을 위해 처음부터 다시 구축되었습니다.

[Balázs Orbán](https://github.com/balazsorban44)이 공동 메인터이너로 합류해 Iain의 업무 부담 일부를 덜어주었습니다.

### 2021 – 멀티 프레임워크 추진[](https://next-auth.js.org/contributors#2021--multi-framework-effort)

Iain과 Balázs는 프로젝트의 미래 목표를 정의했습니다. 두 사람의 비전은 완벽히 일치했고, NextAuth.js가 언젠가 다른 프레임워크에도 유용해질 수 있다는 점을 논의했습니다.

Iain은 Balázs가 두 사람이 공유한 비전을 이어갈 것이라는 확신 속에, 다른 일에 집중하기 위해 프로젝트를 떠났습니다.

Balázs는 프로젝트의 리드 메인터이너가 되었습니다.

NextAuth.js를 다른 프레임워크로 확장하고 가능한 한 많은 데이터베이스와 provider를 지원하려는 노력이 시작되었습니다.

하나의 패키지로는 이러한 모든 사용 사례를 지원할 수 없다는 점이 확인되었습니다.

Database Adapter는 `@next-auth/*-adapter`라는 이름으로 개별 패키지로 분리되었습니다.

### 2022 – Auth.js의 탄생[](https://next-auth.js.org/contributors#2022--birth-of-authjs)

NextAuth.js를 기반으로, Balázs는 [Auth.js (`@auth/core`)](https://twitter.com/balazsorban44/status/1603082914362986496)를 공개했습니다. 이는 런타임/프레임워크에 독립적인 코어 라이브러리로, 모든 Auth.js 라이브러리의 기반입니다. NextAuth.js와 공개 API 대부분을 공유하면서도 내부적으로는 매우 다른 완전한 재작성 버전이었습니다.

### 2023 – Auth.js의 조용한 릴리스[](https://next-auth.js.org/contributors#2023--authjs-silent-releases)

개인적인 사정으로 Balázs는 리드 메인터이너 자리에서 물러나야 했지만, 계속 기여는 이어갔습니다. 한동안 프로젝트는 [Thang Huu Vu](https://github.com/thanghuuvu)가 맡아 진행했습니다.

Balázs는 복귀하여 Auth.js 작업을 계속했습니다. 파일럿 프로젝트로 `next-auth@experimental`(이후 `next-auth@beta`) 릴리스가 배포되었고, 이를 통해 다른 프레임워크 지원을 위해 코어 라이브러리에 무엇이 필요한지, 기존 NextAuth.js 구현에서 어떤 부분이 프레임워크 종속적인지 정리했습니다.

새 기본 문서 페이지는 [authjs.dev](https://authjs.dev)(지금 읽고 있는 이 페이지)로 변경되었고, [next-auth.js.org](https://next-auth.js.org)의 기존 NextAuth.js 문서는 NextAuth.js v4 문서화를 위해 유지되며, 현재는 참고용 백레퍼런스로만 유지되고 있습니다.

Database Adapter는 `@next-auth/*-adapter` 네임스페이스에서 `@auth/*-adapter`로 이동했으며, 이는 더 이상 NextAuth.js 전용이 아님을 나타냅니다.

커뮤니티 통합 사례가 등장하기 시작했고, Auth.js의 초기 비전을 많은 이들이 공유하고 있음이 분명해졌습니다.

### 2024 – 성장하는 Auth.js 생태계[](https://next-auth.js.org/contributors#2024--growing-the-authjs-ecosystem)

[NextAuth.js v5](https://next-auth.js.org/getting-started/migrating-to-v5) 릴리스와 함께, 이제 모든 Auth.js 라이브러리는 동일한 코어 라이브러리를 기반으로 합니다. **“NextAuth.js”라는 이름은 Next.js 통합만을 가리키며** , Auth.js는 코어 라이브러리와 생태계 전체를 의미합니다. 다른 통합은 일반적으로 프레임워크 이름 + Auth 형태로 지칭되며, 예: “SvelteKit Auth”, “Express Auth”.

모든 공식 통합은 `@auth` 스코프 아래 배포되며, NextAuth.js만 마이그레이션 부담을 줄이기 위해 `next-auth`로 배포됩니다.

## 참고 사항[](https://next-auth.js.org/contributors#notes)

Auth.js/NextAuth.js 프로젝트는 Vercel Inc. 또는 그 자회사가 제공하거나 제휴한 것이 아닙니다. Vercel 소속 개인이 이 프로젝트에 기여한 내용은 모두 개인 자격으로 이루어진 것입니다.
