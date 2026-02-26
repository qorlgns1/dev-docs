---
title: "Wikimedia"
description: "이 provider는 모든 Wikimedia 프로젝트도 지원합니다:"
---

Source URL: https://next-auth.js.org/providers/wikimedia

# Wikimedia | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/wikimedia#documentation "Direct link to heading")

<https://www.mediawiki.org/wiki/Extension:OAuth>

이 provider는 모든 Wikimedia 프로젝트도 지원합니다:

- Wikipedia
- Wikidata
- Wikibooks
- Wiktionary
- 등..

Wikimedia 계정에는 연결된 이메일 주소가 없을 수도 있다는 점에 유의하세요. 따라서 로그인 허용 전에 사용자가 이메일 주소를 가지고 있는지 확인하는 체크를 추가하는 것이 좋습니다.

## 구성[​](https://next-auth.js.org/providers/wikimedia#configuration "Direct link to heading")

1. 다음으로 이동해 Consumer Registration 문서를 수락하세요: <https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration>
2. 새 OAuth 2.0 consumer를 요청해 `clientId`와 `clientSecret`을 발급받으세요: <https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose/oauth2> 2a. 콘솔에 다음 redirect URL을 추가하세요 `http://<your-next-app-url>/api/auth/callback/wikimedia` 2b. `This consumer is only for [your username]` 옆의 체크박스는 선택하지 마세요 2c. 더 큰 scope가 명시적으로 필요한 경우가 아니라면, `User identity verification only - no ability to read pages or act on the users behalf.` 라벨의 라디오 버튼을 선택해도 됩니다.

등록 후에는 초기에 본인 Wikimedia 계정으로만 애플리케이션을 테스트할 수 있습니다. 모든 사용자가 사용할 수 있도록 애플리케이션이 승인되기까지 며칠이 걸릴 수 있습니다.

## 옵션[​](https://next-auth.js.org/providers/wikimedia#options "Direct link to heading")

**Wikimedia Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Wikimedia Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/wikimedia.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/wikimedia#example "Direct link to heading")

```
    import WikimediaProvider from "next-auth/providers/wikimedia";
    ...
    providers: [
      WikimediaProvider({
        clientId: process.env.WIKIMEDIA_CLIENT_ID,
        clientSecret: process.env.WIKIMEDIA_CLIENT_SECRET
      })
    ]
    ...

```
