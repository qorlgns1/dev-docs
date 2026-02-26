---
title: "Apple"
description: "사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/v3/providers/apple

# Apple | NextAuth.js

버전: v3

## 문서[​](https://next-auth.js.org/v3/providers/apple#documentation "Direct link to heading")

<https://developer.apple.com/sign-in-with-apple/get-started/>

## 구성[​](https://next-auth.js.org/v3/providers/apple#configuration "Direct link to heading")

<https://developer.apple.com/account/resources/identifiers/list/serviceId>

## 옵션[​](https://next-auth.js.org/v3/providers/apple#options "Direct link to heading")

**Apple Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Apple Provider options](https://github.com/nextauthjs/next-auth/blob/ead715219a5d7a6e882a6ba27fa56b03954d062d/src/providers/apple.js)

사용 사례에 맞게 모든 옵션을 재정의할 수 있습니다.

## 예제[​](https://next-auth.js.org/v3/providers/apple#example "Direct link to heading")

Sign in with Apple provider를 사용하는 방법은 두 가지입니다.

### 동적으로 생성된 secret[​](https://next-auth.js.org/v3/providers/apple#dynamically-generated-secret "Direct link to heading")

동적으로 생성된 secret을 사용하면 서버를 수동으로 업데이트할 필요가 없습니다.

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Apple({
        clientId: process.env.APPLE_ID,
        clientSecret: {
          teamId: process.env.APPLE_TEAM_ID,
          privateKey: process.env.APPLE_PRIVATE_KEY,
          keyId: process.env.APPLE_KEY_ID,
        }
      })
    ]
    ...

```

팁

Apple 키를 한 줄로 변환해 환경 변수에서 사용할 수 있습니다.

**Mac**

```
     awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}'  AuthKey_ID.k8

```

**Windows**

```
     $k8file = "AuthKey_ID.k8"
    (Get-Content "C:\Users\$env:UserName\Downloads\${k8file}") -join "\n"

```

### 사전 생성된 secret[​](https://next-auth.js.org/v3/providers/apple#pre-generated-secret "Direct link to heading")

사전 생성된 secret을 사용하면 개인 키를 환경 변수로 추가하지 않아도 됩니다.

```
    import Providers from `next-auth/providers`
    ...
    providers: [
      Providers.Apple({
        clientId: process.env.APPLE_ID,
        clientSecret: process.env.APPLE_KEY_SECRET
      })
    ]
    ...

```

팁

TeamID는 로그인 후 오른쪽 상단에서 확인할 수 있습니다.

팁

KeyID는 키를 생성한 후 `k8` 파일을 다운로드하기 전에 확인할 수 있습니다.

## 안내[​](https://next-auth.js.org/v3/providers/apple#instructions "Direct link to heading")

### 테스트[​](https://next-auth.js.org/v3/providers/apple#testing "Direct link to heading")

팁

Apple은 모든 사이트가 HTTPS로 실행되어야 합니다(로컬 개발 인스턴스 포함).

팁

Apple은 도메인 또는 서브도메인에서 localhost 사용을 허용하지 않습니다.

다음 가이드가 도움이 될 수 있습니다:

- [How to setup localhost with HTTPS with a Next.js app](https://medium.com/@anMagpie/secure-your-local-development-server-with-https-next-js-81ac6b8b3d68)

- [Guide to configuring Sign in with Apple](https://developer.okta.com/blog/2019/06/04/what-the-heck-is-sign-in-with-apple)

### 예제 서버[​](https://next-auth.js.org/v3/providers/apple#example-server "Direct link to heading")

host 파일을 수정하고 사이트가 `127.0.0.1`을 가리키도록 설정해야 합니다.

[How to edit my host file?](https://phoenixnap.com/kb/how-to-edit-hosts-file-in-windows-mac-or-linux)

Windows에서(관리자 권한으로 Powershell 실행)

```
    Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "127.0.0.1`tdev.example.com" -Force

```

```
    127.0.0.1 dev.example.com

```

#### 인증서 생성[​](https://next-auth.js.org/v3/providers/apple#create-certificate "Direct link to heading")

localhost용 인증서는 openssl로 쉽게 만들 수 있습니다. 아래 명령어를 터미널에 입력하면 됩니다. 출력 결과로 `localhost.key`와 `localhost.crt` 두 파일이 생성됩니다.

```
    openssl req -x509 -out localhost.crt -keyout localhost.key \
      -newkey rsa:2048 -nodes -sha256 \
      -subj '/CN=localhost' -extensions EXT -config <( \
       printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

```

팁

**Windows**

OpenSSL 실행 파일은 Windows용 [Git](https://git-scm.com/download/win%5D9)에 포함되어 배포됩니다. 설치 후 `C:/Program Files/Git/mingw64/bin`에서 openssl.exe 파일을 찾을 수 있으며, 아직 설정하지 않았다면 시스템 PATH 환경 변수에 추가할 수 있습니다.

환경 변수 `OPENSSL_CONF=C:/Program Files/Git/mingw64/ssl/openssl.cnf`를 추가하세요.

```
     req -x509 -out localhost.crt -keyout localhost.key \
      -newkey rsa:2048 -nodes -sha256 \
      -subj '/CN=localhost'

```

`certificates` 디렉터리를 만들고 `localhost.key`와 `localhost.crt`를 배치하세요.

프로젝트 루트에 `server.js`를 생성하고 `node server.js`로 실행하면 로컬에서 Sign in with Apple 통합을 테스트할 수 있습니다:

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

### JWT 코드 예제[​](https://next-auth.js.org/v3/providers/apple#example-jwt-code "Direct link to heading")

secret을 사전 생성하려는 경우, 필요한 코드 예제는 다음과 같습니다:

```
    const jwt = require("jsonwebtoken")
    const fs = require("fs")

    const appleId = "myapp.example.com"
    const keyId = ""
    const teamId = ""
    const privateKey = fs.readFileSync("path/to/key")

    const secret = jwt.sign(
      {
        iss: teamId,
        iat: Math.floor(Date.now() / 1000),
        exp: Math.floor(Date.now() / 1000) + 86400 * 180, // 6 months
        aud: "https://appleid.apple.com",
        sub: appleId,
      },
      privateKey,
      {
        algorithm: "ES256",
        keyid: keyId,
      }
    )

    console.log(secret)

```
