---
title: "자주 묻는 질문"
description: "원본 URL: https://next-auth.js.org/faq"
---

원본 URL: https://next-auth.js.org/faq

# 자주 묻는 질문 | NextAuth.js

버전: v4

## NextAuth.js 소개[​](https://next-auth.js.org/faq#about-nextauthjs "제목으로 바로 가는 링크")

### NextAuth.js는 상용 소프트웨어인가요?[​](https://next-auth.js.org/faq#is-nextauthjs-commercial-software "제목으로 바로 가는 링크")

NextAuth.js는 개별 기여자들이 만든 오픈 소스 프로젝트입니다.

상용 소프트웨어가 아니며, 상업 조직과도 관련이 없습니다.

---

## 호환성[​](https://next-auth.js.org/faq#compatibility "제목으로 바로 가는 링크")

### NextAuth.js는 어떤 데이터베이스를 지원하나요?

NextAuth.js는 MySQL, MariaDB, Postgres, MongoDB, SQLite와 함께 사용할 수 있으며, 데이터베이스 없이도 사용할 수 있습니다. (참고: [Databases](https://next-auth.js.org/configuration/databases))

또한 커스텀 데이터베이스 adapter를 사용하거나 커스텀 credentials authentication provider를 사용해 어떤 데이터베이스와도 NextAuth.js를 사용할 수 있습니다. 예: 기존 데이터베이스에 저장된 사용자 이름/비밀번호로 로그인 지원.

### NextAuth.js는 어떤 인증 서비스를 지원하나요?

NextAuth.js는 42 School, Amazon Cognito, Apple, Atlassian, Auth0, Authentik, Azure Active Directory, Azure Active Directory B2C, Battle.net, Box, BoxyHQ SAML, Bungie, Coinbase, Credentials, Discord, Dropbox, DuendeIdentityServer6, EVE Online, Email, FACEIT, Facebook, Foursquare, Freshbooks, FusionAuth, GitHub, GitLab, Google, HubSpot, IdentityServer4, Instagram, Kakao, Keycloak, LINE, LinkedIn, Mail.ru, Mailchimp, Medium, Naver, Netlify, Okta, OneLogin, Osso, Patreon, Pinterest, Pipedrive, Reddit, Salesforce, Slack, Spotify, Strava, Todoist, Trakt, Twitch, Twitter, United Effects, VK, Wikimedia, WordPress.com, WorkOS, Yandex, Zitadel, Zoho, Zoom, osu! 로그인에 대한 기본 지원을 포함합니다. (참고: [Providers](https://next-auth.js.org/configuration/providers/oauth))

NextAuth.js는 비밀번호 없는 로그인을 위한 이메일도 지원하며, 이는 계정 복구나 구성된 OAuth 서비스를 사용하는 계정을 이용할 수 없는 사용자(예: 서비스 장애, 계정 정지, 기타 이유로 계정 잠김)에게 유용합니다.

또한 외부 데이터베이스에 저장된 사용자 이름/비밀번호 로그인 및/또는 2단계 인증을 지원하도록 커스텀 기반 provider를 사용할 수 있습니다.

### NextAuth.js는 사용자 이름/비밀번호 로그인을 지원하나요?

NextAuth.js는 사용자 계정 비밀번호를 저장할 필요를 피하도록 설계되었습니다.

기존의 사용자 이름/비밀번호 데이터베이스가 있다면, 커스텀 credentials provider를 사용해 기존 데이터베이스에 저장된 사용자 이름/비밀번호로 로그인할 수 있습니다.

_커스텀 credentials provider를 사용하면 NextAuth.js는 사용자 계정을 데이터베이스에 영속화하지 않습니다(설정되어 있어도 동일). 커스텀 credentials provider를 사용하려면, 세션 데이터베이스 없이 로그인할 수 있게 해주는 세션 토큰용 JSON Web Tokens 옵션이 활성화되어 있어야 합니다._

### Next.js가 아닌 다른 프레임워크와 함께 NextAuth.js를 사용할 수 있나요?

NextAuth.js는 원래 Next.js 및 Serverless와 함께 사용하도록 설계되었습니다. 하지만 오늘날에는 어떤 프레임워크와도 NextAuth.js core를 사용할 수 있습니다. [Gatsby](https://github.com/nextauthjs/next-auth/tree/main/apps/playground-gatsby)와 [SvelteKit](https://sveltekit.authjs.dev/) 예제를 확인해 보세요. 다른 프레임워크 통합을 추가하고 싶다면 자유롭게 작업해서 pull request를 보내주세요. 새 이슈를 열기 전에 진행 중인 작업이 있는지 꼭 확인하세요.

### NextAuth.js가 생성한 session을 다른 웹사이트에서 사용할 수 있나요?

**동일 도메인** : NextAuth.js로 로그인 처리를 하는 웹사이트를 만들고, 같은 도메인이라면 NextAuth.js를 사용하지 않는 다른 웹사이트에서도 해당 세션에 접근할 수 있습니다.

**동일 루트 도메인, 다른 서브도메인** : 웹사이트의 나머지 부분과 다른 서브도메인에서 NextAuth.js를 사용하는 경우(예: `auth.example.com` vs. `www.example.com`), Session Token cookie에 대해 커스텀 cookie domain 정책을 설정해야 합니다. (참고: [Cookies](https://next-auth.js.org/configuration/options#cookies)).

danger

기본 cookies domain 정책을 변경하면, 잘못 구성했을 때 보안 문제가 발생할 수 있습니다. 진행 전에 그 영향 범위를 반드시 이해하세요.

작동하는 예시는 [this example repo](https://github.com/vercel/examples/tree/main/solutions/subdomain-auth)에서 확인할 수 있습니다.

**다른 루트 도메인** : 현재 NextAuth.js는 단일 세션으로 서로 다른 최상위 도메인 사이트(예: `www.example.com` vs. `www.example.org`)에 자동 로그인하는 기능을 지원하지 않습니다.

### React Native와 함께 NextAuth.js를 사용할 수 있나요?

NextAuth.js는 안전한 confidential client로 설계되었으며 서버 사이드 인증 플로우를 구현합니다.

일반적으로 public client를 구현하는 데스크톱/모바일 네이티브 애플리케이션(예: 클라이언트/시크릿이 앱에 내장됨)에서 사용하도록 의도된 것은 아닙니다.

### NextAuth.js는 TypeScript를 지원하나요?

네! [TypeScript docs](https://next-auth.js.org/getting-started/typescript)를 확인하세요.

### NextAuth.js는 Next.js 12 Middleware와 호환되나요?

[Next.js Middleware](https://nextjs.org/docs/middleware)를 지원합니다. [this page](https://next-auth.js.org/configuration/nextjs#middleware)로 이동하세요.

---

## 데이터베이스[​](https://next-auth.js.org/faq#databases "제목으로 바로 가는 링크")

### NextAuth.js는 어떤 데이터베이스를 지원하나요?

NextAuth.js는 MySQL, Postgres, MongoDB, SQLite 및 호환 데이터베이스(예: MariaDB, Amazon Aurora, Amazon DocumentDB…)와 함께 사용할 수 있고, 데이터베이스 없이도 사용할 수 있습니다.

또한 어떤 데이터베이스와도 연결할 수 있도록 Adapter API를 제공합니다.

### NextAuth.js는 데이터베이스를 어디에 사용하나요?

NextAuth.js의 데이터베이스는 사용자, OAuth 계정, 이메일 로그인 토큰, 세션을 영속화하는 데 사용됩니다.

사용자 데이터를 영속화하거나 이메일 로그인을 지원할 필요가 없다면 데이터베이스 지정은 선택 사항입니다. 데이터베이스를 지정하지 않으면 세션 저장을 위해 JSON Web Tokens가 활성화되며, 세션 데이터 저장에 사용됩니다.

NextAuth.js와 함께 데이터베이스를 사용하는 경우에도, 데이터베이스 세션 대신 세션에 JSON Web Tokens를 명시적으로 활성화할 수 있습니다.

### 데이터베이스를 사용해야 하나요?

- 데이터베이스 없이 NextAuth.js를 사용하는 방식은 내부 도구에 잘 맞습니다. 누가 로그인할 수 있는지는 제어해야 하지만, 애플리케이션 내 사용자 계정을 만들 필요는 없는 경우입니다.

- 데이터베이스와 함께 NextAuth.js를 사용하는 방식은 보통 소비자 대상 애플리케이션에서 더 좋습니다. 계정을 영속화해야 하는 경우(예: 과금, 고객 연락 등)입니다.

### 어떤 데이터베이스를 사용해야 하나요?

MySQL, Postgres, MongoDB(및 호환 데이터베이스)를 위한 관리형 데이터베이스 솔루션은 Amazon, Google, Microsoft, Atlas 같은 클라우드 제공자에서 잘 지원됩니다.

특정 클라우드 플랫폼에 직접 배포한다면, 해당 플랫폼의 serverless 데이터베이스 서비스도 고려할 수 있습니다(예: [Amazon Aurora Serverless on AWS](https://aws.amazon.com/rds/aurora/serverless/)).

---

## 보안[​](https://next-auth.js.org/faq#security "제목으로 바로 가는 링크")

이 섹션의 일부 내용은 [별도 페이지](https://next-auth.js.org/security)로 이동되었습니다.

### OAuth 계정의 Refresh Tokens와 Access Tokens는 어떻게 얻나요?

NextAuth.js는 인증, 세션 관리, 사용자 계정 생성 솔루션을 제공합니다.

NextAuth.js는 로그인 시(제공자가 제공한 경우) Refresh Tokens와 Access Tokens를 기록하고, User ID, Provider, Provider Account ID와 함께 아래 중 한 곳으로 전달합니다.

1. 데이터베이스 - 데이터베이스 connection string이 제공된 경우
2. JSON Web Token callback - JWT 세션이 활성화된 경우(예: 데이터베이스 미지정)

그 후 데이터베이스에서 조회하거나 JSON Web Token에 영속화할 수 있습니다.

참고: NextAuth.js는 현재 OAuth 제공자의 Access Token rotation을 자동으로 처리하지 않습니다. 구현하려면 [this tutorial](https://authjs.dev/guides/refresh-token-rotation)을 참고하세요.

또한 NextAuth.js v4 기반의 [example repository](https://github.com/nextauthjs/next-auth-refresh-token-example) / 프로젝트도 제공하며, 여기서 refresh token으로 제공된 access token을 갱신하는 방법을 보여줍니다.

### 같은 이메일 주소의 다른 계정으로 로그인하면 왜 계정이 자동으로 연결되지 않나요?

로그인 시 자동 계정 연결은 임의의 provider 간에는 안전하지 않습니다. 예외적으로 이메일 주소를 대체 로그인 수단으로 허용하는 경우는 가능하며(이 플로우에서 이메일 검증이 필수이기 때문).

이메일 주소가 OAuth 계정과 연결되어 있다고 해서 반드시 계정 소유자가 검증한 주소라는 뜻은 아닙니다. 이메일 검증 방식은 OAuth 명세에 포함되지 않으며 provider마다 다릅니다(예: 먼저 검증하지 않는 곳, 먼저 검증하는 곳, 검증 상태 메타데이터를 반환하는 곳).

로그인 시 자동 계정 연결을 사용하면, 악의적인 사용자가 다른 사용자의 이메일 주소와 연결된 OAuth 계정을 만들어 계정을 탈취하는 데 악용할 수 있습니다.

이 때문에 로그인 시 임의의 provider 간 계정을 자동 연결하는 것은 안전하지 않으며, 그래서 일반적으로 인증 서비스에서 이 기능을 제공하지 않습니다.

일부 사이트에서는 자동 계정 연결을 제공하며, 때로는 안전하지 않은 방식으로 구현됩니다. 관련된 모든 provider가 계정 이메일 주소를 안전하게 검증한다고 신뢰할 수 있다면 자동 계정 연결을 안전하게 구현하는 것이 기술적으로 가능할 수는 있지만, 이 과정의 보안을 provider에 신뢰하고 위험을 이전해야 합니다.

안전한 시나리오의 예로는 직접 제어하는 OAuth provider(예: 조직 내부 사용자만 승인) 또는 사용자의 이메일 주소를 검증했다고 명시적으로 신뢰하는 provider가 있습니다.

자동 계정 연결은 provider별로 `allowDangerousEmailAccountLinking`을 통해 지원됩니다.

추가 provider의 안전한 계정 연결/연결 해제 지원 기능은 원래 v1.x에 있었지만 v2.0 이후 빠졌고, 사용자 로그인 상태에서만 수행 가능하며, 향후 릴리스에서 다시 제공될 예정입니다.

note

사용자가 먼저 Email로 로그인한 뒤 OAuth provider로 다시 로그인하려고 하면, NextAuth.js의 기본 동작은 OAuth 계정의 이메일 주소가 기존 사용자 이메일 주소와 일치하지 않아도 계정 연결을 허용합니다.

---

## 기능 요청[​](https://next-auth.js.org/faq#feature-requests "제목으로 바로 가는 링크")

### NextAuth.js는 왜 [특정 기능]을 지원하지 않나요?

NextAuth.js는 개별 기여자들이 오픈 소스로 개발하는 프로젝트이며, 이들은 자원봉사자로서 여가 시간에 코드 작성과 지원을 제공합니다.

NextAuth.js가 특정 기능을 지원하길 원한다면, 해당 기능을 설명하는 기능 요청을 올리고 다른 기여자와 함께 개발 및 테스트에 참여하겠다고 제안하는 것이 가장 좋은 방법입니다.

### 설계 결정에 동의하지 않습니다. 어떻게 하면 생각을 바꿀 수 있나요?

NextAuth.js의 제품 설계 결정은 코어 팀 멤버가 내립니다.

기능 요청 / 개선 요청 형태로 제안을 올릴 수 있습니다.

템플릿이 요구하는 상세 정보를 제공하고 요청된 형식을 따르면, 지원받을 가능성이 더 높을 수 있습니다. 템플릿의 추가 질문은 종종 중요한 맥락을 제공합니다.

최종적으로 요청이 수용되지 않거나 활발히 개발되지 않더라도, ISC License 조건에 따라 언제든 프로젝트를 포크할 수 있습니다.

---

## JSON Web Tokens[​](https://next-auth.js.org/faq#json-web-tokens "제목으로 바로 가는 링크")

### NextAuth.js는 JSON Web Tokens를 사용하나요?

NextAuth.js는 기본적으로 사용자의 세션을 저장하기 위해 JSON Web Tokens를 사용합니다. 하지만 [database adapter](https://authjs.dev/getting-started/database)를 사용하면 사용자의 세션을 영속화하는 데 데이터베이스가 사용됩니다. 데이터베이스를 사용할 때도 [configuration options](https://next-auth.js.org/configuration/options#session)을 통해 JWT 사용을 강제할 수 있습니다. v4부터는 모든 JWT 토큰이 기본적으로 A256GCM으로 암호화됩니다.

### JSON Web Tokens의 장점은 무엇인가요?

JSON Web Tokens는 세션 토큰으로 사용할 수 있을 뿐 아니라, 인증 플로우에서 서비스 간 서명된 객체를 전송하는 등 다양한 용도로도 사용됩니다.

- 세션 토큰으로 JWT를 사용할 때의 장점은 세션 저장을 위한 데이터베이스가 필요 없다는 점이며, 이로 인해 더 빠르고 저렴하게 운영할 수 있고 확장도 더 쉽습니다.

- NextAuth.js의 JSON Web Tokens는 포함된 정보를 JWT 세션 토큰에 직접 저장하기 위해 암호학적 암호화(JWE)를 사용해 보호됩니다. 따라서 포함된 정보를 검증하기 위해 데이터베이스에 접속하지 않고도 동일한 도메인 내 서비스와 API 간에 토큰으로 정보를 전달할 수 있습니다.

- 암호화가 없더라도, 클라이언트가 알아도 괜찮은 정보는 JWT에 안전하게 저장할 수 있습니다. JWT는 서버에서만 읽을 수 있는 쿠키에 저장되므로 사이트에서 실행되는 서드파티 JavaScript는 JWT의 데이터에 접근할 수 없습니다.

### JSON Web Tokens의 단점은 무엇인가요?

- JSON Web Token은 쉽게 만료시킬 수 없습니다. 이를 위해서는 무효 토큰의 서버 측 blocklist를 유지하고(적어도 만료될 때까지), 토큰이 제시될 때마다 매번 목록과 대조해야 합니다.

JSON Web Tokens를 세션 토큰으로 사용할 때는 세션을 더 빨리 무효화하고 이 문제를 단순화하기 위해 더 짧은 세션 만료 시간이 사용됩니다.

NextAuth.js 클라이언트에는 짧은 세션 만료 시간이 사용자 경험에 미치는 단점을 완화하기 위한 고급 기능이 포함되어 있습니다. 여기에는 자동 세션 토큰 로테이션, 창이나 탭이 열려 있을 때 짧은 수명의 세션이 만료되지 않도록 선택적으로 keep alive 메시지 전송, 백그라운드 재검증, 그리고 세션 상태가 변경되거나 창/탭이 포커스를 얻거나 잃을 때마다 창 간 세션을 동기화하는 자동 탭/창 동기화가 포함됩니다.

- 데이터베이스 세션 토큰과 마찬가지로 JSON Web Tokens에도 저장할 수 있는 데이터 양의 제한이 있습니다. 일반적으로 쿠키당 약 4096바이트 제한이 있지만, 정확한 제한은 브라우저, 프록시, 호스팅 서비스에 따라 다릅니다. 대부분의 브라우저를 지원하려면 쿠키당 4096바이트를 넘기지 마세요. 더 많은 데이터를 저장하려면 세션을 데이터베이스에 영속화해야 합니다 (출처: [browsercookielimits.iain.guru](http://browsercookielimits.iain.guru/))

토큰에 저장하려는 데이터가 많을수록, 그리고 설정하는 다른 쿠키가 많을수록 이 제한에 더 가까워집니다. v4부터는 4kb 제한을 초과하는 쿠키를 분할하고 파싱 시 재조립하는 cookie chunking을 구현했습니다. 다만 이 데이터는 모든 요청마다 전송되어야 하므로, 약 4 KB를 초과하는 데이터를 저장하려는 경우에는 토큰에는 고유 ID만 저장하고 실제 데이터는 다른 곳(예: 서버 측 key/value store)에 영속화하는 단계에 이르렀다고 볼 수 있습니다.

- 암호화된 JSON Web Token(JWE)에 저장된 데이터는 언젠가 손상될 수 있습니다.

적절히 구성했더라도, 암호화된 JWT에 저장된 정보는 절대 해독 불가능하다고 가정해서는 안 됩니다. 예를 들어 결함 발견이나 기술 발전으로 인해 해독될 수 있습니다.

미래에 해독되었을 때 문제가 될 수 있는 데이터는 토큰에 저장하지 마세요.

- NextAuth.js에 secret을 명시적으로 지정하지 않으면, NextAuth.js가 자동 생성된 secret을 기본값으로 사용하므로 NextAuth.js 설정이 변경될 때마다 기존 세션이 무효화됩니다. v4부터는 이는 개발 환경에만 영향을 주며, 운영 환경에서는 secret 생성이 필수입니다.

### JSON Web Tokens는 안전한가요?

기본적으로 토큰은 서명(JWS)되지 않지만 암호화(JWE)됩니다. v4부터는 4kb 제한을 초과하는 쿠키를 분할하고 파싱 시 재조립하는 cookie chunking을 구현했습니다.

유효한 다른 알고리즘도 지정할 수 있습니다 - [RFC 7518에 명시된 대로](https://tools.ietf.org/html/rfc7517) \- secret(대칭 암호화용) 또는 공개/개인 키 쌍(비대칭 암호화용)과 함께 사용할 수 있습니다.

NextAuth.js가 키를 생성해 줄 수 있지만, 시작 시 경고가 발생합니다.

서명을 위해 명시적인 공개/개인 키를 사용하는 것을 강력히 권장합니다.

### NextAuth.js는 어떤 서명 및 암호화 표준을 지원하나요?

NextAuth.js는 JSON Object Signing and Encryption(JOSE)을 거의 완전하게 구현하고 있습니다:

- [RFC 7515 - JSON Web Signature (JWS)](https://tools.ietf.org/html/rfc7515)
- [RFC 7516 - JSON Web Encryption (JWE)](https://tools.ietf.org/html/rfc7516)
- [RFC 7517 - JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517)
- [RFC 7518 - JSON Web Algorithms (JWA)](https://tools.ietf.org/html/rfc7518)
- [RFC 7519 - JSON Web Token (JWT)](https://tools.ietf.org/html/rfc7519)

여기에는 다음에 대한 지원도 포함됩니다:

- [RFC 7638 - JSON Web Key Thumbprint](https://tools.ietf.org/html/rfc7638)
- [RFC 7787 - JSON JWS Unencoded Payload Option](https://tools.ietf.org/html/rfc7797)
- [RFC 8037 - CFRG Elliptic Curve ECDH and Signatures](https://tools.ietf.org/html/rfc8037)
