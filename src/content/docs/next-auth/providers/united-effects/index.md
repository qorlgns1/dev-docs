---
title: "United Effects"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

소스 URL: https://next-auth.js.org/providers/united-effects

# United Effects | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/united-effects#documentation "Direct link to heading")

<https://docs.unitedeffects.com/integrations/nextauthjs>

## 구성[​](https://next-auth.js.org/providers/united-effects#configuration "Direct link to heading")

<https://core.unitedeffects.com>

## 옵션[​](https://next-auth.js.org/providers/united-effects#options "Direct link to heading")

**United Effects Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [United Effects Provider 옵션](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/united-effects.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/providers/united-effects#example "Direct link to heading")

```
    import UnitedEffectsProvider from "next-auth/providers/united-effects";
    ...
    providers: [
      UnitedEffectsProvider({
        clientId: process.env.UNITED_EFFECTS_CLIENT_ID,
        clientSecret: process.env.UNITED_EFFECTS_CLIENT_SECRET,
        issuer: process.env.UNITED_EFFECTS_ISSUER
      })
    ]
    ...

```

참고

`issuer`는 Auth Group ID를 포함한 정규화된 전체 URL이어야 합니다. 예: `https://auth.unitedeffects.com/YQpbQV5dbW-224dCovz-3`

주의

United Effects API는 설계상 사용자 이름이나 이미지를 반환하지 않으므로, 이 provider는 두 값 모두에 대해 null을 반환합니다. United Effects는 사용자 개인정보 보안을 최우선으로 하며, provider API와 분리된 보안 프로필 접근 요청 시스템을 구축했습니다.
