---
title: 'NextAuth.js 소개[\u200b](https://next-auth.js.org/v3/getting-started/introduction#about-nextauthjs "헤딩으로 직접 연결")'
description: "NextAuth.js는 Next.js 애플리케이션을 위한 완전한 오픈 소스 인증 솔루션입니다."
---

출처 URL: https://next-auth.js.org/v3/getting-started/introduction

# 소개 | NextAuth.js

버전: v3

## NextAuth.js 소개[​](https://next-auth.js.org/v3/getting-started/introduction#about-nextauthjs "헤딩으로 직접 연결")

NextAuth.js는 [Next.js](http://nextjs.org/) 애플리케이션을 위한 완전한 오픈 소스 인증 솔루션입니다.

처음부터 Next.js와 Serverless를 지원하도록 설계되었습니다.

인증에 NextAuth.js를 얼마나 쉽게 사용할 수 있는지 [예제 코드](https://next-auth.js.org/getting-started/example)에서 확인해 보세요.

### 유연하고 사용하기 쉬움[​](https://next-auth.js.org/v3/getting-started/introduction#flexible-and-easy-to-use "헤딩으로 직접 연결")

- 모든 OAuth 서비스와 함께 동작하도록 설계되었으며, OAuth 1.0, 1.0A, 2.0을 지원합니다
- [다양한 인기 로그인 서비스](https://next-auth.js.org/configuration/providers/oauth)를 기본 지원합니다
- 이메일 / 비밀번호 없는 인증을 지원합니다
- 어떤 백엔드(Active Directory, LDAP 등)와도 상태 비저장 인증을 지원합니다
- JSON Web Token과 데이터베이스 세션을 모두 지원합니다
- Serverless를 위해 설계되었지만 어디서나 실행됩니다 (AWS Lambda, Docker, Heroku 등…)

### 데이터를 직접 소유하세요[​](https://next-auth.js.org/v3/getting-started/introduction#own-your-own-data "헤딩으로 직접 연결")

NextAuth.js는 데이터베이스를 사용하거나 사용하지 않고도 활용할 수 있습니다.

- 데이터를 계속 직접 통제할 수 있게 해주는 오픈 소스 솔루션입니다
- BYOD(Bring Your Own Database)를 지원하며 어떤 데이터베이스와도 사용할 수 있습니다
- [MySQL, MariaDB, Postgres, SQL Server, MongoDB, SQLite](https://next-auth.js.org/configuration/databases)를 기본 지원합니다
- 주요 호스팅 제공업체의 데이터베이스와도 잘 동작합니다
- _데이터베이스 없이도_ 사용할 수 있습니다 (예: OAuth + JWT)

_참고: 이메일 로그인은 일회용 검증 토큰 저장을 위해 데이터베이스 구성이 필요합니다._

### 기본적으로 안전함[​](https://next-auth.js.org/v3/getting-started/introduction#secure-by-default "헤딩으로 직접 연결")

- 비밀번호 없는 로그인 메커니즘 사용을 권장합니다
- 기본적으로 안전하도록 설계되었고 사용자 데이터 보호를 위한 모범 사례를 장려합니다
- POST 라우트(로그인, 로그아웃)에서 CSRF(Cross Site Request Forgery) 토큰을 사용합니다
- 기본 쿠키 정책은 각 쿠키에 적합한 가장 엄격한 정책을 목표로 합니다
- JSON Web Token이 활성화되면 기본적으로 HS512 방식의 서명(JWS)이 적용됩니다
- `encryption: true` 옵션을 설정하면 JWT 암호화(JWE)를 사용할 수 있습니다 (기본값은 A256GCM)
- 개발 편의를 위해 대칭 서명 키와 암호화 키를 자동 생성합니다
- 짧은 수명의 세션을 지원하기 위해 탭/창 동기화 및 keepalive 메시지 기능을 제공합니다
- [Open Web Application Security Project](https://owasp.org/)에서 공개한 최신 가이드를 반영하려고 노력합니다

고급 옵션을 사용하면 로그인 가능한 계정 제어, JSON Web Token 인코딩/디코딩, 커스텀 쿠키 보안 정책 및 세션 속성 설정을 위한 자체 루틴을 정의할 수 있으므로, 누가 로그인할 수 있는지와 세션 재검증 주기를 직접 제어할 수 있습니다.

## 크레딧[​](https://next-auth.js.org/v3/getting-started/introduction#credits "헤딩으로 직접 연결")

NextAuth.js는 [기여자들](https://next-auth.js.org/contributors) 덕분에 가능해진 오픈 소스 프로젝트입니다.

## 시작하기[​](https://next-auth.js.org/v3/getting-started/introduction#getting-started "헤딩으로 직접 연결")

인증에 NextAuth.js를 얼마나 쉽게 사용할 수 있는지 [예제 코드](https://next-auth.js.org/getting-started/example)에서 확인해 보세요.
