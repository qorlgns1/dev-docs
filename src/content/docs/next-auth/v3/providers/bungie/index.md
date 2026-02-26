---
title: "Bungie"
description: "원본 URL: https://next-auth.js.org/v3/providers/bungie"
---

원본 URL: https://next-auth.js.org/v3/providers/bungie

# Bungie | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/bungie#documentation "Direct link to heading")

<https://github.com/Bungie-net/api/wiki/OAuth-Documentation>

## 구성[​](https://next-auth.js.org/v3/providers/bungie#configuration "Direct link to heading")

<https://www.bungie.net/en/Application>

## 옵션[​](https://next-auth.js.org/v3/providers/bungie#options "Direct link to heading")

**Bungie Provider**에는 기본 옵션 세트가 포함되어 있습니다:

- [Bungie Provider 옵션](https://github.com/nextauthjs/next-auth/blob/main/src/providers/bungie.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예시[​](https://next-auth.js.org/v3/providers/bungie#example "Direct link to heading")

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Bungie({
        clientId: process.env.BUNGIE_CLIENT_ID,
        clientSecret: process.env.BUNGIE_SECRET,
        headers: {
          'X-API-Key': provess.env.BUNGIE_API_KEY
        }
      }),
    ]
    ...

```

### 구성[​](https://next-auth.js.org/v3/providers/bungie#configuration-1 "Direct link to heading")

tip

Bungie는 모든 사이트가 HTTPS로 실행되도록 요구합니다(로컬 개발 인스턴스 포함).

tip

Bungie는 웹사이트 URL로 localhost 사용을 허용하지 않으므로, 대신 <https://127.0.0.1:3000>을 사용해야 합니다.

<https://www.bungie.net/en/Application>으로 이동하여 필수 항목을 입력하세요:

- 애플리케이션 이름
- 애플리케이션 상태
- 웹사이트
- OAuth 클라이언트 유형
  - Confidential
- 리디렉션 URL
  - https://localhost:3000/api/auth/callback/bungie
- Scope
  - `Access items like your Bungie.net notifications, memberships, and recent Bungie.Net forum activity.`
- Origin Header

다음 가이드가 도움이 될 수 있습니다:

- [Next.js 앱에서 HTTPS로 localhost 설정하는 방법](https://medium.com/@anMagpie/secure-your-local-development-server-with-https-next-js-81ac6b8b3d68)

### 예제 서버[​](https://next-auth.js.org/v3/providers/bungie#example-server "Direct link to heading")

호스트 파일을 수정하고 사이트가 `127.0.0.1`을 가리키도록 설정해야 합니다.

[호스트 파일은 어떻게 편집하나요?](https://phoenixnap.com/kb/how-to-edit-hosts-file-in-windows-mac-or-linux)

Windows에서 (Powershell을 관리자 권한으로 실행)

```
    Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "127.0.0.1`tdev.example.com" -Force

```

```
    127.0.0.1 dev.example.com

```

#### 인증서 생성[​](https://next-auth.js.org/v3/providers/bungie#create-certificate "Direct link to heading")

localhost용 인증서는 openssl로 쉽게 만들 수 있습니다. 아래 명령어를 터미널에 입력하세요. 출력 결과로 `localhost.key`와 `localhost.crt` 두 파일이 생성됩니다.

```
    openssl req -x509 -out localhost.crt -keyout localhost.key \
      -newkey rsa:2048 -nodes -sha256 \
      -subj '/CN=localhost' -extensions EXT -config <( \
       printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

```

tip

**Windows**

OpenSSL 실행 파일은 Windows용 [Git](https://git-scm.com/download/win%5D9)과 함께 배포됩니다. 설치 후 `C:/Program Files/Git/mingw64/bin`에서 openssl.exe 파일을 찾을 수 있으며, 아직 설정되지 않았다면 시스템 PATH 환경 변수에 추가할 수 있습니다.

환경 변수 `OPENSSL_CONF=C:/Program Files/Git/mingw64/ssl/openssl.cnf`를 추가하세요.

```
     req -x509 -out localhost.crt -keyout localhost.key \
      -newkey rsa:2048 -nodes -sha256 \
      -subj '/CN=localhost'

```

`certificates` 디렉터리를 만들고 `localhost.key`와 `localhost.crt`를 넣으세요.

프로젝트 루트에 `server.js`를 만들고 `node server.js`로 실행하면 로컬에서 Bungie 로그인 연동을 테스트할 수 있습니다:

```
    const { createServer } = require("https")
    const { parse } = require("url")
    const next = require("next")
    const fs = require("fs")

    const dev = process.env.NODE_ENV !== "production"
    const app = next({ dev })
    const handle = app.getRequestHandler()

    const httpsOptions = {
      key: fs.readFileSync("./certificates/localhost.key"),
      cert: fs.readFileSync("./certificates/localhost.crt"),
    }

    app.prepare().then(() => {
      createServer(httpsOptions, (req, res) => {
        const parsedUrl = parse(req.url, true)
        handle(req, res, parsedUrl)
      }).listen(3000, (err) => {
        if (err) throw err
        console.log("> Ready on https://localhost:3000")
      })
    })

```
