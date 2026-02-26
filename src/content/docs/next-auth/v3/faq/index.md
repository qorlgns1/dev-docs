---
title: "자주 묻는 질문"
description: "NextAuth.js는 개인 기여자들이 만든 오픈 소스 프로젝트입니다."
---

Source URL: https://next-auth.js.org/v3/faq

# 자주 묻는 질문 | NextAuth.js

버전: v3

## NextAuth.js에 대하여[​](https://next-auth.js.org/v3/faq#about-nextauthjs "Direct link to heading")

### NextAuth.js는 상용 소프트웨어인가요?[​](https://next-auth.js.org/v3/faq#is-nextauthjs-commercial-software "Direct link to heading")

NextAuth.js는 개인 기여자들이 만든 오픈 소스 프로젝트입니다.

상용 소프트웨어가 아니며, 상업 조직과도 관련이 없습니다.

---

## 호환성[​](https://next-auth.js.org/v3/faq#compatibility "Direct link to heading")

### NextAuth.js는 어떤 데이터베이스를 지원하나요?[​](https://next-auth.js.org/v3/faq#what-databases-does-nextauthjs-support "Direct link to heading")

NextAuth.js는 MySQL, MariaDB, Postgres, MongoDB, SQLite와 함께 사용할 수 있으며 데이터베이스 없이도 사용할 수 있습니다. (참고: [Databases](https://next-auth.js.org/configuration/databases))

커스텀 데이터베이스 어댑터를 사용하거나 커스텀 credentials 인증 provider를 사용하면 어떤 데이터베이스와도 NextAuth.js를 함께 사용할 수 있습니다. 예: 기존 데이터베이스에 저장된 사용자 이름/비밀번호로 로그인 지원.

### NextAuth.js는 어떤 인증 서비스를 지원하나요?[​](https://next-auth.js.org/v3/faq#what-authentication-services-does-nextauthjs-support "Direct link to heading")

NextAuth.js는 42 School, Amazon Cognito, Apple, Atlassian, Auth0, Authentik, Azure Active Directory, Azure Active Directory B2C, Battle.net, Box, BoxyHQ SAML, Bungie, Coinbase, Credentials, Discord, Dropbox, DuendeIdentityServer6, EVE Online, Email, FACEIT, Facebook, Foursquare, Freshbooks, FusionAuth, GitHub, GitLab, Google, HubSpot, IdentityServer4, Instagram, Kakao, Keycloak, LINE, LinkedIn, Mail.ru, Mailchimp, Medium, Naver, Netlify, Okta, OneLogin, Osso, Patreon, Pinterest, Pipedrive, Reddit, Salesforce, Slack, Spotify, Strava, Todoist, Trakt, Twitch, Twitter, United Effects, VK, Wikimedia, WordPress.com, WorkOS, Yandex, Zitadel, Zoho, Zoom, osu! 로그인에 대한 내장 지원을 포함합니다. (참고: [Providers](https://next-auth.js.org/configuration/providers/oauth))

NextAuth.js는 비밀번호 없는 로그인을 위한 email도 지원합니다. 이는 계정 복구 시나리오나 구성된 OAuth 서비스 계정을 사용할 수 없는 사용자(예: 서비스 장애, 계정 정지, 기타 이유로 인한 계정 잠김)에게 유용합니다.

또한 외부 데이터베이스에 저장된 사용자 이름/비밀번호 로그인 및/또는 2단계 인증을 지원하기 위해 custom based provider를 사용할 수도 있습니다.

### NextAuth.js는 사용자 이름/비밀번호 로그인을 지원하나요?[​](https://next-auth.js.org/v3/faq#does-nextauthjs-support-signing-in-with-a-username-and-password "Direct link to heading")

NextAuth.js는 사용자 계정 비밀번호를 저장할 필요를 피하도록 설계되었습니다.

기존 사용자 이름/비밀번호 데이터베이스가 있다면, 커스텀 credentials provider를 사용해 기존 데이터베이스에 저장된 사용자 이름/비밀번호 로그인을 허용할 수 있습니다.

_NextAuth.js에서 커스텀 credentials provider를 사용하면(데이터베이스가 설정되어 있어도) 사용자 계정은 데이터베이스에 영속 저장되지 않습니다. 커스텀 credentials provider를 사용하려면 세션 토큰에 JSON Web Tokens를 사용하는 옵션(세션 데이터베이스 없이 로그인 가능)을 활성화해야 합니다._

### Next.js를 사용하지 않는 웹사이트에서도 NextAuth.js를 사용할 수 있나요?[​](https://next-auth.js.org/v3/faq#can-i-use-nextauthjs-with-a-website-that-does-not-use-nextjs "Direct link to heading")

NextAuth.js는 Next.js 및 Serverless 환경에서 사용하도록 설계되었습니다.

웹사이트에 다른 프레임워크를 사용 중이라면, Next.js로 로그인을 처리하는 웹사이트를 만든 뒤 동일 도메인에 있는 Next.js 미사용 웹사이트에서 해당 세션에 접근할 수 있습니다.

웹사이트의 나머지 부분과 다른 하위 도메인에서 NextAuth.js를 사용할 경우(예: `auth.example.com` vs `www.example.com`), Session Token cookie에 대한 커스텀 cookie 도메인 정책을 설정해야 합니다. (참고: [Cookies](https://next-auth.js.org/configuration/options#cookies))

NextAuth.js는 현재 단일 세션을 이용해 서로 다른 최상위 도메인 사이트(예: `www.example.com` vs `www.example.org`)에 자동 로그인하는 것을 지원하지 않습니다.

### React Native에서 NextAuth.js를 사용할 수 있나요?[​](https://next-auth.js.org/v3/faq#can-i-use-nextauthjs-with-react-native "Direct link to heading")

NextAuth.js는 안전한 confidential client로 설계되었으며 서버 사이드 인증 플로우를 구현합니다.

일반적으로 public client를 구현하는 데스크톱/모바일 네이티브 애플리케이션(예: 애플리케이션에 client / secrets 내장)에서 사용하도록 의도되지 않았습니다.

### NextAuth.js는 TypeScript를 지원하나요?[​](https://next-auth.js.org/v3/faq#is-nextauthjs-supporting-typescript "Direct link to heading")

네! [TypeScript docs](https://next-auth.js.org/getting-started/typescript)를 확인하세요.

---

## 데이터베이스[​](https://next-auth.js.org/v3/faq#databases "Direct link to heading")

### NextAuth.js는 어떤 데이터베이스를 지원하나요?[​](https://next-auth.js.org/v3/faq#what-databases-are-supported-by-nextauthjs "Direct link to heading")

NextAuth.js는 MySQL, Postgres, MongoDB, SQLite 및 호환 데이터베이스(예: MariaDB, Amazon Aurora, Amazon DocumentDB…)와 함께 사용할 수 있으며, 데이터베이스 없이도 사용할 수 있습니다.

또한 어떤 데이터베이스와도 연결할 수 있도록 Adapter API를 제공합니다.

### NextAuth.js는 데이터베이스를 무엇에 사용하나요?[​](https://next-auth.js.org/v3/faq#what-does-nextauthjs-use-databases-for "Direct link to heading")

NextAuth.js에서 데이터베이스는 사용자, OAuth 계정, email 로그인 토큰, 세션을 영속 저장하는 데 사용됩니다.

사용자 데이터 영속 저장이나 email 로그인이 필요하지 않다면 데이터베이스 지정은 선택 사항입니다. 데이터베이스를 지정하지 않으면 세션 저장용으로 JSON Web Tokens가 활성화되어 세션 데이터를 저장합니다.

NextAuth.js와 함께 데이터베이스를 사용하더라도, 세션에 대해 JSON Web Tokens를 명시적으로 활성화할 수 있습니다(데이터베이스 세션 대신).

### 데이터베이스를 사용해야 하나요?[​](https://next-auth.js.org/v3/faq#should-i-use-a-database "Direct link to heading")

- 데이터베이스 없이 NextAuth.js를 사용하는 방식은 내부 도구에 잘 맞습니다. 누가 로그인할 수 있는지는 제어해야 하지만, 애플리케이션에서 사용자 계정을 만들 필요는 없는 경우입니다.

- 데이터베이스와 함께 NextAuth.js를 사용하는 방식은 일반적으로 소비자 대상 애플리케이션에 더 적합합니다. 계정을 영속 저장해야 하는 경우(예: 과금, 고객 연락 등)입니다.

### 어떤 데이터베이스를 사용해야 하나요?[​](https://next-auth.js.org/v3/faq#what-database-should-i-use "Direct link to heading")

MySQL, Postgres, MongoDB(및 호환 데이터베이스)용 관리형 데이터베이스 솔루션은 Amazon, Google, Microsoft, Atlas 같은 클라우드 제공업체에서 잘 지원됩니다.

특정 클라우드 플랫폼에 직접 배포하는 경우, 해당 플랫폼의 serverless 데이터베이스 제공도 고려할 수 있습니다(예: [Amazon Aurora Serverless on AWS](https://aws.amazon.com/rds/aurora/serverless/)).

---

## 보안[​](https://next-auth.js.org/v3/faq#security "Direct link to heading")

### 보안 문제가 있다고 생각되면 어떻게 해야 하나요?[​](https://next-auth.js.org/v3/faq#i-think-ive-found-a-security-problem-what-should-i-do "Direct link to heading")

덜 심각하거나 엣지 케이스 이슈(예: 선택적 RFC 사양과의 호환성 문의)는 GitHub 공개 이슈로 제기할 수 있습니다.

잠재적으로 심각한 보안 문제라고 판단되는 내용을 발견했다면, 비공개 채널(예: [me@iaincollins.com](mailto:me@iaincollins.com) 이메일)로 코어 팀 멤버에게 연락하거나, 선호하는 방법으로 자세한 내용을 주고받을 수 있게 연락 요청 공개 이슈를 올려 주세요.

### NextAuth.js의 공개 정책은 무엇인가요?[​](https://next-auth.js.org/v3/faq#what-is-the-disclosure-policy-for-nextauthjs "Direct link to heading")

저희는 책임 있는 공개(responsible disclosure)를 실천합니다.

잠재적으로 심각한 이슈에 대해 연락을 주시면 72시간 이내 답변, 30일 이내 수정 배포를 목표로 합니다. 이슈 해결 수정본이 배포되면(또는 90일 경과 시, 더 빠른 시점 기준) 책임 있게 이슈를 공개하며, 동의하시면 제보자 크레딧도 함께 표기합니다.

### OAuth 계정의 Refresh Tokens와 Access Tokens는 어떻게 얻나요?[​](https://next-auth.js.org/v3/faq#how-do-i-get-refresh-tokens-and-access-tokens-for-an-oauth-account "Direct link to heading")

NextAuth.js는 인증, 세션 관리, 사용자 계정 생성을 위한 솔루션을 제공합니다.

NextAuth.js는 로그인 시 Refresh Tokens와 Access Tokens를 기록하며(provider가 제공한 경우), User ID, Provider, Provider Account ID와 함께 다음 중 하나로 전달합니다:

1. 데이터베이스 - 데이터베이스 연결 문자열이 제공된 경우
2. JSON Web Token callback - JWT 세션이 활성화된 경우(예: 데이터베이스 미지정)

그런 다음 데이터베이스에서 조회하거나 JSON Web Token에 영속 저장할 수 있습니다.

참고: NextAuth.js는 현재 OAuth provider의 Access Token rotation을 자동으로 처리하지 않습니다. 이를 구현하려면 [this tutorial](https://authjs.dev/guides/basics/refresh-token-rotation)을 참고하세요.

### 같은 이메일 주소를 가진 다른 계정으로 로그인할 때 계정이 자동으로 연결되지 않는 이유는 무엇인가요?[​](https://next-auth.js.org/v3/faq#when-i-sign-in-with-another-account-with-the-same-email-address-why-are-accounts-not-linked-automatically "Direct link to heading")

로그인 시 임의 provider 간 자동 계정 연결은 안전하지 않습니다. 예외적으로 email 주소를 대체 로그인(fallback)으로 허용하는 경우는 가능합니다(플로우에서 이메일 주소 검증이 필요하기 때문).

이메일 주소가 OAuth 계정과 연관되어 있다고 해서 반드시 계정 소유자 소유임이 검증되었다는 뜻은 아닙니다. 이메일 주소 검증 방식은 OAuth 사양의 일부가 아니며 provider마다 다릅니다(예: 어떤 곳은 미검증, 어떤 곳은 선검증, 또 어떤 곳은 검증 상태 메타데이터 반환).

로그인 자동 계정 연결이 있으면 악의적 행위자가 다른 사용자의 이메일 주소로 OAuth 계정을 만들어 계정을 탈취하는 데 악용할 수 있습니다.

이 때문에 로그인 시 임의 provider 간 자동 계정 연결은 안전하지 않으며, 그래서 일반적으로 인증 서비스에서도 제공하지 않고 NextAuth.js에서도 제공하지 않습니다.

일부 사이트에서는 자동 계정 연결이 보이기도 하며, 때로는 안전하지 않은 방식입니다. 관련된 모든 provider가 계정의 이메일 주소를 안전하게 검증한다고 신뢰할 수 있다면 기술적으로 안전한 자동 계정 연결이 가능할 수는 있지만, 그 과정의 보안을 해당 provider에 신뢰(및 위험 이전)해야 합니다.

안전한 시나리오 예로는 직접 제어하는 OAuth provider(예: 조직 내부 사용자만 인증) 또는 사용자 이메일 주소를 검증했다고 명시적으로 신뢰하는 provider가 있습니다.

자동 계정 연결은 NextAuth.js의 계획된 기능은 아니지만, 안전한 방식으로 계정 연결 사용자 경험과 이 플로우 처리를 개선할 여지는 있습니다. 일반적으로 email 로그인 대체 옵션을 제공하는 방식이며, 이는 이미 가능하고(권장됨), 다만 현재 구현은 개선될 수 있습니다.

추가 provider의 안전한 계정 연결/연결 해제 지원은 사용자 로그인 상태에서만 가능하며, 원래 v1.x 기능이었지만 v2.0 이후 포함되지 않았고 향후 릴리스에서 복귀 예정입니다.

---

## 기능 요청[​](https://next-auth.js.org/v3/faq#feature-requests "Direct link to heading")

### 왜 NextAuth.js는 [특정 기능]을 지원하지 않나요?[​](https://next-auth.js.org/v3/faq#why-doesnt-nextauthjs-support-a-particular-feature "Direct link to heading")

NextAuth.js는 개인 기여자들이 여가 시간에 코드를 작성하고 지원을 제공하며 만드는 오픈 소스 프로젝트입니다.

NextAuth.js가 특정 기능을 지원하길 원한다면, 해당 기능을 설명하는 기능 요청을 올리고 다른 기여자들과 함께 개발 및 테스트에 참여하겠다고 제안하는 것이 그 기능을 실현하는 가장 좋은 방법입니다.

직접 기능을 개발할 수 없다면, 누군가가 그 작업을 할 수 있도록 후원할 수도 있습니다.

### 설계 결정에 동의하지 않는데, 어떻게 하면 생각을 바꿀 수 있나요?[​](https://next-auth.js.org/v3/faq#i-disagree-with-a-design-decision-how-can-i-change-your-mind "Direct link to heading")

NextAuth.js의 제품 설계 결정은 코어 팀 멤버들이 내립니다.

기능 요청 / 개선 요청 형태로 제안을 올릴 수 있습니다.

템플릿에서 요구하는 세부 정보를 제공하고 요청된 형식을 따르는 요청일수록 채택될 가능성이 더 높습니다. 템플릿이 요구하는 추가 정보에는 중요한 맥락이 담기는 경우가 많기 때문입니다.

최종적으로 요청이 수용되지 않거나 활발히 개발되지 않는 경우, ISC License 조건에 따라 언제든지 프로젝트를 포크할 수 있습니다.

---

## JSON Web Tokens[​](https://next-auth.js.org/v3/faq#json-web-tokens "Direct link to heading")

### NextAuth.js는 JSON Web Tokens를 사용하나요?[​](https://next-auth.js.org/v3/faq#does-nextauthjs-use-json-web-tokens "Direct link to heading")

NextAuth.js는 데이터베이스 세션 토큰과 JWT 세션 토큰을 모두 지원합니다.

- 데이터베이스를 지정하면 기본적으로 데이터베이스 세션 토큰이 사용됩니다.
- 데이터베이스를 지정하지 않으면 기본적으로 JWT 세션 토큰이 사용됩니다.

`session: { jwt: true }` 옵션을 명시적으로 설정하면, 데이터베이스를 사용하면서도 JSON Web Tokens를 세션 토큰으로 선택할 수 있습니다.

### JSON Web Tokens의 장점은 무엇인가요?[​](https://next-auth.js.org/v3/faq#what-are-the-advantages-of-json-web-tokens "Direct link to heading")

JSON Web Tokens는 세션 토큰으로 사용할 수 있을 뿐 아니라, 인증 흐름에서 서비스 간 서명된 객체를 전달하는 등 다양한 용도로도 사용됩니다.

- 세션 토큰으로 JWT를 사용할 때의 장점은 세션 저장을 위한 데이터베이스가 필요 없다는 점이며, 이로 인해 더 빠르고 저렴하게 운영할 수 있고 확장도 더 쉬워집니다.

- NextAuth.js의 JSON Web Tokens는 기본적으로 암호학적 서명(JWS)으로 보호되며, 서비스와 API 엔드포인트가 토큰 검증을 위해 데이터베이스에 문의하지 않고도 토큰을 쉽게 검증할 수 있습니다.

- 암호화(JWE)를 활성화하면 비밀로 유지하고 싶은 정보를 JWT 세션 토큰에 직접 포함해 저장할 수 있고, 동일한 도메인의 서비스/API 간에 정보를 전달하는 데 토큰을 사용할 수 있습니다.

- 암호화가 없어도 JWT를 사용해 클라이언트가 알아도 괜찮은 정보를 안전하게 저장할 수 있습니다. JWT가 server-readable-only-token에 저장되므로 JWT 안의 데이터는 사이트에서 실행되는 제3자 JavaScript에서 접근할 수 없습니다.

### JSON Web Tokens의 단점은 무엇인가요?[​](https://next-auth.js.org/v3/faq#what-are-the-disadvantages-of-json-web-tokens "Direct link to heading")

- JSON Web Token은 만료 처리(무효화)를 쉽게 할 수 없습니다. 이를 위해서는 서버 측에서 무효 토큰 블록리스트(최소한 해당 토큰이 만료될 때까지)를 유지하고, 토큰이 제시될 때마다 매번 목록과 대조해야 합니다.

JSON Web Tokens를 세션 토큰으로 사용할 때는 이 문제를 단순화하고 세션을 더 빨리 무효화할 수 있도록 더 짧은 세션 만료 시간이 사용됩니다.

NextAuth.js 클라이언트는 짧은 세션 만료 시간이 사용자 경험에 주는 단점을 완화하기 위한 고급 기능을 포함합니다. 여기에는 자동 세션 토큰 로테이션, 창이나 탭이 열려 있을 때 짧은 수명의 세션이 만료되지 않도록 하는 선택적 keep alive 메시지 전송, 백그라운드 재검증, 그리고 세션 상태가 바뀌거나 창/탭이 포커스를 얻거나 잃을 때마다 창 간 세션을 동기화하는 자동 탭/창 동기화가 포함됩니다.

- 데이터베이스 세션 토큰과 마찬가지로 JSON Web Tokens도 저장할 수 있는 데이터 양에 제한이 있습니다. 일반적으로 쿠키당 약 4096바이트 제한이 있지만, 정확한 한도는 브라우저, 프록시, 호스팅 서비스에 따라 다릅니다. 대부분의 브라우저를 지원하려면 쿠키당 4096바이트를 넘기지 마세요. 더 많은 데이터를 저장하려면 세션을 데이터베이스에 영속화해야 합니다(출처: [browsercookielimits.iain.guru](http://browsercookielimits.iain.guru/))

토큰에 저장하려는 데이터가 많아지고 다른 쿠키도 많이 설정할수록 이 제한에 가까워집니다. 약 4 KB를 넘는 데이터를 저장하려 한다면, 토큰에는 고유 ID만 저장하고 실제 데이터는 다른 곳(예: 서버 측 key/value 저장소)에 영속화해야 할 시점일 가능성이 큽니다.

- 암호화된 JSON Web Token(JWE)에 저장된 데이터는 어느 시점에 손상될 수 있습니다.

적절하게 구성했더라도, 암호화된 JWT에 저장한 정보는 언젠가 복호화되지 않을 것이라고 가정해서는 안 됩니다. 예를 들어 결함 발견이나 기술 발전으로 인해 복호화될 수 있습니다.

미래에 복호화될 경우 문제가 될 수 있는 데이터는 토큰에 저장하지 마세요.

- NextAuth.js에 secret을 명시적으로 지정하지 않으면, NextAuth.js가 자동 생성된 secret을 기본값으로 사용하기 때문에 NextAuth.js 구성이 바뀔 때마다 기존 세션이 무효화됩니다.

JSON Web Token을 사용하는 경우 최소한 secret은 지정하고, 이상적으로는 공개/개인 키를 구성해야 합니다.

### JSON Web Tokens는 안전한가요?[​](https://next-auth.js.org/v3/faq#are-json-web-tokens-secure "Direct link to heading")

기본적으로 토큰은 서명(JWS)되지만 암호화(JWE)되지는 않습니다. 암호화는 추가 오버헤드를 발생시키고 데이터 저장에 사용할 수 있는 공간을 줄이기 때문입니다(도메인별 전체 쿠키 크기는 4KB로 제한됨).

- NextAuth.js의 JSON Web Tokens는 JWS를 사용하며, 자동 생성된 키로 HS512 서명이 적용됩니다.

- `jwt: { encryption: true }` 옵션으로 암호화를 활성화하면 JWT는 _추가로_ JWE를 사용해 토큰을 암호화하며, 자동 생성된 키로 A256GCM을 사용합니다.

유효한 다른 알고리즘도 secret(대칭 암호화용) 또는 공개/개인 키 쌍(대칭 암호화용)과 함께 지정할 수 있습니다. [RFC 7518](https://tools.ietf.org/html/rfc7517)에서 규정한 내용입니다.

NextAuth.js가 키를 생성해줄 수는 있지만, 시작 시 경고가 발생합니다.

서명을 위해 명시적인 공개/개인 키를 사용하는 것을 강력히 권장합니다.

### NextAuth.js는 어떤 서명 및 암호화 표준을 지원하나요?[​](https://next-auth.js.org/v3/faq#what-signing-and-encryption-standards-does-nextauthjs-support "Direct link to heading")

NextAuth.js에는 JSON Object Signing and Encryption (JOSE)의 대부분을 포괄하는 구현이 포함되어 있습니다:

- [RFC 7515 - JSON Web Signature (JWS)](https://tools.ietf.org/html/rfc7515)
- [RFC 7516 - JSON Web Encryption (JWE)](https://tools.ietf.org/html/rfc7516)
- [RFC 7517 - JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517)
- [RFC 7518 - JSON Web Algorithms (JWA)](https://tools.ietf.org/html/rfc7518)
- [RFC 7519 - JSON Web Token (JWT)](https://tools.ietf.org/html/rfc7519)

여기에는 다음 지원이 포함됩니다:

- [RFC 7638 - JSON Web Key Thumbprint](https://tools.ietf.org/html/rfc7638)
- [RFC 7787 - JSON JWS Unencoded Payload Option](https://tools.ietf.org/html/rfc7797)
- [RFC 8037 - CFRG Elliptic Curve ECDH and Signatures](https://tools.ietf.org/html/rfc8037)
