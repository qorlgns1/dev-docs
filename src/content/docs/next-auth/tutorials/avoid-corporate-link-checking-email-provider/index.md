---
title: "기업용 링크 검사기 환경에서 이메일 가입 허용"
description: "원본 URL: https://next-auth.js.org/tutorials/avoid-corporate-link-checking-email-provider"
---

원본 URL: https://next-auth.js.org/tutorials/avoid-corporate-link-checking-email-provider

# 기업용 링크 검사기 환경에서 이메일 가입 허용 | NextAuth.js

버전: v4

Office 365나 Outlook, 또는 다른 이메일 시스템을 사용하는 경우 이메일 초대 링크가 동작하지 않는 것을 볼 수 있습니다.

이는 사용자가 받는 초대 이메일이 이메일 제공업체에 의해 스캔되기 때문입니다. Outlook의 "SafeLink" 기능의 경우, 이메일의 각 링크에 `HEAD` 요청을 보냅니다. 이 요청은 사용자 초대 토큰과 함께 NextAuth.js의 catch-all API Route를 트리거하여, 사실상 토큰을 소모해 버립니다.

따라서 사용자가 직접 사용하려고 초대 링크를 클릭하면 초대가 유효하지 않다는 오류 메시지를 보게 됩니다.

## 우회 방법[​](https://next-auth.js.org/tutorials/avoid-corporate-link-checking-email-provider#workarounds "Direct link to heading")

### "SafeLink" 비활성화[​](https://next-auth.js.org/tutorials/avoid-corporate-link-checking-email-provider#disable-safelink "Direct link to heading")

첫 번째 가능한 우회 방법은 조직에서 이 "SafeLink" 기능을 비활성화하는 것입니다. Microsoft의 자세한 설명은 [여기](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-links?view=o365-worldwide#do-not-rewrite-the-following-urls-lists-in-safe-links-policies)에서 확인할 수 있습니다. 물론 이는 보통 기업 IT 정책의 일부이므로 모든 사람에게 가능한 선택지는 아닙니다.

### 'HEAD' 요청을 위해 NextAuth.js 업데이트[​](https://next-auth.js.org/tutorials/avoid-corporate-link-checking-email-provider#update-nextauthjs-for-head-requests "Direct link to heading")

두 번째 옵션은 이메일 서비스에서 오는 초기 `HEAD` 요청을 초대 링크를 실수로 소모하지 않고 정상적으로 처리하도록 `[...nextauth].js` catch-all API route를 약간 수정하는 것입니다.

이 작업은 API route의 가장 상단에서, 다른 로직이 실행되기 전에 `HEAD` 요청에 대해 `200` 응답을 반환하도록 하면 됩니다.

예시

/pages/api/auth/[...nextauth].js

```
    import type { NextApiRequest, NextApiResponse } from "next"
    import NextAuth from "next-auth"

    export default async function auth(req: NextApiRequest, res: NextApiResponse) {

      if(req.method === "HEAD") {
         return res.status(200).end()
      }

      ...
    }

```

이렇게 하면 엄격한 기업 IT 설정 환경에서도 NextAuth.js의 Email provider를 성공적으로 사용할 수 있습니다.
