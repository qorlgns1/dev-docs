---
title: "corporate-proxy"
description: "원본 URL: https://next-auth.js.org/tutorials/corporate-proxy"
---

원본 URL: https://next-auth.js.org/tutorials/corporate-proxy

# corporate-proxy | NextAuth.js

버전: v4

\-- id: corporate-proxy

## title: HTTP Proxy 지원 추가[​](https://next-auth.js.org/tutorials/corporate-proxy#title-add-support-for-http-proxy "Direct link to heading")

사내 프록시 뒤에서 NextAuth.js를 사용하는 것은 기본적으로 지원되지 않습니다. 이는 우리가 사용하는 기반 라이브러리인 [`openid-client`](https://npm.im/openid-client)가 기본 제공 Node.js `http` / `https` 라이브러리를 사용하기 때문이며, 이 라이브러리들은 기본적으로 프록시를 지원하지 않습니다. (참고: [`http` docs](https://nodejs.org/dist/latest-v18.x/docs/api/http.html), [`https` docs](https://nodejs.org/dist/latest-v18.x/docs/api/https.html)).

따라서 `https-proxy-agent` 같은 추가 프록시 에이전트를 `http` 클라이언트에 설정해야 합니다. `openid-client`는 요청에 사용할 `agent`를 사용자가 설정할 수 있게 해줍니다 ([Source](https://github.com/panva/node-openid-client/blob/main/docs/README.md#customizing-individual-http-requests).

아래 diff를 제공해 준 [raphaelpc](https://github.com/raphaelpc)에게 감사드립니다. 이 diff를 `v4.2.1`에 적용하면 `client.js` 파일에 해당 에이전트 지원이 추가됩니다.

```
    diff --git a/node_modules/next-auth/core/lib/oauth/client.js b/node_modules/next-auth/core/lib/oauth/client.js
    index 77161bd..1082fba 100644
    --- a/node_modules/next-auth/core/lib/oauth/client.js
    +++ b/node_modules/next-auth/core/lib/oauth/client.js
    @@ -7,11 +7,19 @@ exports.openidClient = openidClient;

     var _openidClient = require("openid-client");

    +var HttpsProxyAgent = require("https-proxy-agent");
    +
     async function openidClient(options) {
       const provider = options.provider;
    -  if (provider.httpOptions) _openidClient.custom.setHttpOptionsDefaults(provider.httpOptions);
    -  let issuer;
    +  let httpOptions = {};
    +  if (provider.httpOptions) httpOptions = { ...provider.httpOptions };
    +  if (process.env.http_proxy) {
    +    let agent = new HttpsProxyAgent(process.env.http_proxy);
    +    httpOptions.agent = agent;
    +  }
    +  _openidClient.custom.setHttpOptionsDefaults(httpOptions);

    +  let issuer;
       if (provider.wellKnown) {
         issuer = await _openidClient.Issuer.discover(provider.wellKnown);
       } else {

```

> 자세한 내용은 [this issue](https://github.com/nextauthjs/next-auth/issues/2509#issuecomment-1035410802)를 참고하세요.

이 패치를 적용한 뒤에는 `http_proxy` 환경 변수를 통해 프록시 연결 문자열을 추가할 수 있습니다.

### 프로바이더[​](https://next-auth.js.org/tutorials/corporate-proxy#provider "Direct link to heading")

`https-proxy-agent`를 사용할 때 프로바이더에서 문제가 발생한다면, 예를 들어 사용자 프로필 사진을 가져오기 위한 추가 요청이 필요한 프로바이더를 사용 중일 수 있습니다. 이런 경우에는 프로바이더 설정에도 프록시 우회 방법을 추가해야 합니다. 아래는 `AzureAD` 프로바이더에서 이를 적용하는 예시입니다.

```
    diff --git a/node_modules/next-auth/providers/azure-ad.js b/node_modules/next-auth/providers/azure-ad.js
    index 73d96d3..536cd81 100644
    --- a/node_modules/next-auth/providers/azure-ad.js
    +++ b/node_modules/next-auth/providers/azure-ad.js
    @@ -5,6 +5,8 @@ Object.defineProperty(exports, "__esModule", {
     });
     exports.default = AzureAD;

    +const HttpsProxyAgent = require('https-proxy-agent');
    +
     function AzureAD(options) {
       var _options$tenantId, _options$profilePhoto;

    @@ -22,11 +24,15 @@ function AzureAD(options) {
         },

         async profile(profile, tokens) {
    -      const profilePicture = await fetch(`https://graph.microsoft.com/v1.0/me/photos/${profilePhotoSize}x${profilePhotoSize}/$value`, {
    +      let fetchOptions = {
             headers: {
    -          Authorization: `Bearer ${tokens.access_token}`
    -        }
    -      });
    +          Authorization: `Bearer ${tokens.access_token}`,
    +        },
    +      };
    +      if (process.env.http_proxy) {
    +        fetchOptions.agent = new HttpsProxyAgent(process.env.http_proxy);
    +      }
    +      const profilePicture = await fetch(`https://graph.microsoft.com/v1.0/me/photos/${profilePhotoSize}x${profilePhotoSize}/$value`, fetchOptions);

           if (profilePicture.ok) {
             const pictureBuffer = await profilePicture.arrayBuffer();

```
