---
title: "Apple"
description: "사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다."
---

Source URL: https://next-auth.js.org/providers/apple

# Apple | NextAuth.js

버전: v4

## 문서[​](https://next-auth.js.org/providers/apple#documentation "제목으로 바로 가는 링크")

<https://developer.apple.com/sign-in-with-apple/get-started/>

## 구성[​](https://next-auth.js.org/providers/apple#configuration "제목으로 바로 가는 링크")

<https://developer.apple.com/account/resources/identifiers/list/serviceId>

## 옵션[​](https://next-auth.js.org/providers/apple#options "제목으로 바로 가는 링크")

**Apple Provider**에는 기본 옵션 세트가 포함되어 있습니다.

- [Apple Provider options](https://github.com/nextauthjs/next-auth/blob/v4/packages/next-auth/src/providers/apple.ts)

사용 사례에 맞게 어떤 옵션이든 재정의할 수 있습니다.

### secret 생성[​](https://next-auth.js.org/providers/apple#generating-a-secret "제목으로 바로 가는 링크")

Apple은 client secret이 JWT 형식이길 요구합니다. 생성하려면 다음 스크립트를 사용할 수 있습니다: <https://bal.so/apple-gen-secret>.

자세한 내용은 [Apple docs](https://developer.apple.com/documentation/sign_in_with_apple/generate_and_validate_tokens#3262048)를 참고하세요.

그다음 결과를 `.env.local` 파일의 `APPLE_SECRET`에 붙여 넣으면 코드에서 참조할 수 있습니다:

```
    import AppleProvider from "next-auth/providers/apple";
    ...
    providers: [
      AppleProvider({
        clientId: process.env.APPLE_ID,
        clientSecret: process.env.APPLE_SECRET
      })
    ]
    ...

```

팁

TeamID는 로그인 후 오른쪽 상단에 있습니다.

팁

KeyID는 키를 생성한 뒤에 확인할 수 있습니다. k8 파일을 다운로드하기 전에 찾아두세요.

## 개발 서버에서 테스트하기[​](https://next-auth.js.org/providers/apple#testing-on-a-development-server "제목으로 바로 가는 링크")

팁

Apple은 모든 사이트가 HTTPS로 동작해야 한다고 요구합니다(로컬 개발 인스턴스 포함).

팁

Apple은 도메인 또는 서브도메인에서 localhost 사용을 허용하지 않습니다.

### 호스트 이름 해석[​](https://next-auth.js.org/providers/apple#host-name-resolution "제목으로 바로 가는 링크")

host 파일을 수정해 사이트가 `127.0.0.1`을 가리키도록 설정하세요.

_Linux/macOS_

```
     echo '127.0.0.1 dev.example.com' | sudo tee -a /etc/hosts

```

_Windows_ (PowerShell을 관리자 권한으로 실행)

```
    Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "127.0.0.1 dev.example.com" -Force

```

추가 정보: [How to edit my host file?](https://phoenixnap.com/kb/how-to-edit-hosts-file-in-windows-mac-or-linux)

### 인증서 생성[​](https://next-auth.js.org/providers/apple#create-certificate "제목으로 바로 가는 링크")

`certificates` 디렉터리를 만들고 OpenSSL로 생성한 인증서 파일 `localhost.key`, `localhost.crt`를 추가하세요.

_Linux/macOS_

```
     openssl req -x509 -out localhost.crt -keyout localhost.key \
      -newkey rsa:2048 -nodes -sha256 \
      -subj "/CN=localhost" -extensions EXT -config <( \
       printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

```

_Windows_

OpenSSL 실행 파일은 Windows용 [Git](https://git-scm.com/download/win)에 포함되어 배포됩니다. 설치 후 `C:\Program Files\Git\mingw64\bin`에서 openssl.exe 파일을 찾을 수 있으며, 아직 설정하지 않았다면 시스템 PATH 환경 변수에 추가할 수 있습니다.

환경 변수 `OPENSSL_CONF=C:\Program Files\Git\mingw64\ssl\openssl.cnf`를 추가하세요.

```
     req -x509 -out localhost.crt -keyout localhost.key \
      -newkey rsa:2048 -nodes -sha256 \
      -subj "/CN=localhost"

```

### 서버에 배포[​](https://next-auth.js.org/providers/apple#deploy-to-server "제목으로 바로 가는 링크")

프로젝트 루트에 `server.js`를 만들고 `node server.js`로 실행하면 로컬에서 Sign in with Apple 통합을 테스트할 수 있습니다:

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

### 유용한 가이드[​](https://next-auth.js.org/providers/apple#helpful-guides "제목으로 바로 가는 링크")

- [How to setup localhost with HTTPS with a Next.js app](https://medium.com/@anMagpie/secure-your-local-development-server-with-https-next-js-81ac6b8b3d68)

- [Guide to configuring Sign in with Apple](https://developer.okta.com/blog/2019/06/04/what-the-heck-is-sign-in-with-apple)
