---
title: '클라이언트[\u200b](https://next-auth.js.org/warnings#client "Direct link to heading")'
description: "원본 URL: https://next-auth.js.org/warnings"
---

원본 URL: https://next-auth.js.org/warnings

# 경고 | NextAuth.js

버전: v4

다음은 NextAuth.js에서 출력하는 경고 목록입니다.

모든 경고는 확인이 필요한 사항을 알려주지만, 정상 동작을 막지는 않습니다.

---

## 클라이언트[​](https://next-auth.js.org/warnings#client "Direct link to heading")

#### NEXTAUTH_URL[​](https://next-auth.js.org/warnings#nextauth_url "Direct link to heading")

환경 변수 `NEXTAUTH_URL`이 없습니다. `.env` 파일에서 설정해 주세요.

참고

[Vercel](https://vercel.com) 배포에서는 `VERCEL_URL` 환경 변수를 읽기 때문에 `NEXTAUTH_URL`을 별도로 정의할 필요가 없습니다.

---

## 서버[​](https://next-auth.js.org/warnings#server "Direct link to heading")

이 경고들은 터미널에 표시됩니다.

#### NO_SECRET[​](https://next-auth.js.org/warnings#no_secret "Direct link to heading")

개발 환경에서는 편의를 위해 설정을 기반으로 `secret`을 생성합니다. 이는 고정되지 않으므로 프로덕션에서는 오류가 발생합니다. [자세히 보기](https://next-auth.js.org/configuration/options#secret)

#### TWITTER_OAUTH_2_BETA[​](https://next-auth.js.org/warnings#twitter_oauth_2_beta "Direct link to heading")

Twitter OAuth 2.0은 일부 변경이 여전히 필요할 수 있어 현재 베타 상태입니다. 이는 semver 적용 대상이 아닙니다. 문서 참조: <https://next-auth.js.org/providers/twitter#oauth-2>

#### EXPERIMENTAL_API[​](https://next-auth.js.org/warnings#experimental_api "Direct link to heading")

일부 API는 아직 실험적 상태이며, 향후 변경되거나 제거될 수 있습니다. 사용에 따른 책임은 사용자에게 있습니다.

#### DEBUG_ENABLED[​](https://next-auth.js.org/warnings#debug_enabled "Direct link to heading")

`debug` 옵션이 활성화되어 있습니다. 이 옵션은 인증 흐름의 문제를 찾는 데 도움이 되도록 개발 전용으로 제공되며, 프로덕션 배포 시에는 제거를 고려해야 합니다. 프로덕션이 아닐 때만 디버깅을 허용하는 한 가지 방법은 `debug: process.env.NODE_ENV !== "production"`으로 설정하는 것입니다. 이렇게 하면 값을 바꿀 필요 없이 커밋할 수 있습니다.

프로덕션 중에도 디버그 메시지를 기록하려면, 잠재적으로 민감한 사용자 정보를 적절히 마스킹하여 [`logger` 옵션](https://next-auth.js.org/configuration/options#logger)을 설정하는 것을 권장합니다.

## 어댑터[​](https://next-auth.js.org/warnings#adapter "Direct link to heading")

### ADAPTER_TYPEORM_UPDATING_ENTITIES[​](https://next-auth.js.org/warnings#adapter_typeorm_updating_entities "Direct link to heading")

이 경고는 typeorm이 제공된 엔티티가 데이터베이스 엔티티와 다르다고 판단할 때 발생합니다. 기본적으로 `production`이 아닐 때 typeorm 어댑터는 엔티티 코드 파일의 변경 사항을 항상 동기화합니다.

typeorm 설정에서 `synchronize: false`를 설정하면 이 경고를 비활성화할 수 있습니다.

예시:

/pages/api/auth/[...nextauth].js

```
    adapter: TypeORMLegacyAdapter({
      type: 'mysql',
      username: process.env.DATABASE_USERNAME,
      password: process.env.DATABASE_PASSWORD,
      host: process.env.DATABASE_HOST,
      database: process.env.DATABASE_DB,
      synchronize: false
    }),

```
