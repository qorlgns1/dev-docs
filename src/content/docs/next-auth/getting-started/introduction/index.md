---
title: 'NextAuth.js 소개[​](https://next-auth.js.org/getting-started/introduction#about-nextauthjs "Direct link to heading")'
description: "NextAuth.js는 Next.js 애플리케이션을 위한 완전한 오픈 소스 인증 솔루션입니다."
---

Source URL: https://next-auth.js.org/getting-started/introduction

# 소개 | NextAuth.js

버전: v4

## NextAuth.js 소개[​](https://next-auth.js.org/getting-started/introduction#about-nextauthjs "Direct link to heading")

NextAuth.js는 [Next.js](http://nextjs.org/) 애플리케이션을 위한 완전한 오픈 소스 인증 솔루션입니다.

처음부터 Next.js와 Serverless를 지원하도록 설계되었습니다.

인증에 NextAuth.js를 사용하는 것이 얼마나 쉬운지 [예제 코드](https://next-auth.js.org/getting-started/example)에서 확인해 보세요.

### 유연하고 사용하기 쉬움[​](https://next-auth.js.org/getting-started/introduction#flexible-and-easy-to-use "Direct link to heading")

- 어떤 [OAuth 서비스와도 동작하도록 설계되었으며, OAuth 1.0, 1.0A, 2.0 및 OpenID Connect를 지원합니다](https://next-auth.js.org/providers)
- [많은 인기 로그인 서비스](https://next-auth.js.org/configuration/providers/oauth)를 기본 지원합니다
- [email / passwordless 인증](https://next-auth.js.org/providers/email)을 지원합니다
- [어떤 백엔드와도](https://authjs.dev/getting-started/database) 상태 비저장 인증을 지원합니다 (Active Directory, LDAP 등)
- JSON Web Tokens와 데이터베이스 세션을 모두 지원합니다
- Serverless를 위해 설계되었지만 어디서나 실행됩니다 (AWS Lambda, Docker, Heroku 등…)

### 데이터를 직접 소유하세요[​](https://next-auth.js.org/getting-started/introduction#own-your-own-data "Direct link to heading")

NextAuth.js는 데이터베이스와 함께 또는 없이 사용할 수 있습니다.

- 데이터를 계속 제어할 수 있게 해주는 오픈 소스 솔루션
- Bring Your Own Database (BYOD)를 지원하며 어떤 데이터베이스와도 사용할 수 있습니다
- [MySQL, MariaDB, Postgres, SQL Server, MongoDB, SQLite](https://next-auth.js.org/configuration/databases)를 기본 지원합니다
- 인기 호스팅 제공업체의 데이터베이스와도 매우 잘 동작합니다
- _데이터베이스 없이도_ 사용할 수 있습니다 (예: OAuth + JWT)

_참고: Email 로그인을 사용하려면 일회용 검증 토큰을 저장할 수 있도록 데이터베이스 구성이 필요합니다._

### 기본적으로 안전함[​](https://next-auth.js.org/getting-started/introduction#secure-by-default "Direct link to heading")

- passwordless 로그인 메커니즘 사용을 권장합니다
- 기본적으로 안전하도록 설계되었으며 사용자 데이터 보호를 위한 모범 사례를 장려합니다
- POST 라우트(로그인, 로그아웃)에서 Cross-Site Request Forgery Tokens를 사용합니다
- 기본 쿠키 정책은 각 쿠키에 적합한 가장 엄격한 정책을 목표로 합니다
- JSON Web Tokens가 활성화되면 기본적으로 A256GCM 방식의 JWE로 암호화됩니다
- 개발 편의를 위해 대칭 서명 및 암호화 키를 자동 생성합니다
- 짧은 수명의 세션을 지원하기 위해 탭/창 동기화 및 keepalive 메시지 기능을 제공합니다
- [Open Web Application Security Project](https://owasp.org/)에서 발행한 최신 가이드를 구현하려고 합니다

고급 옵션을 사용하면 로그인 가능한 계정을 제어하는 처리 로직, JSON Web Tokens의 인코딩/디코딩, 사용자 지정 쿠키 보안 정책 및 세션 속성을 직접 정의할 수 있으므로, 누가 로그인할 수 있는지와 세션을 얼마나 자주 다시 검증해야 하는지를 제어할 수 있습니다.

## 크레딧[​](https://next-auth.js.org/getting-started/introduction#credits "Direct link to heading")

NextAuth.js는 현재 [Better Auth Inc.](https://better-auth.com)가 소유하고 유지 관리합니다. 이 프로젝트는 계속 오픈 소스로 유지되며, [기여자들](https://next-auth.js.org/contributors) 덕분에 가능했습니다.

## 시작하기[​](https://next-auth.js.org/getting-started/introduction#getting-started "Direct link to heading")

인증에 NextAuth.js를 사용하는 것이 얼마나 쉬운지 [예제 코드](https://next-auth.js.org/getting-started/example)에서 확인해 보세요.
