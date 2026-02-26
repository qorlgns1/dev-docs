---
title: "Firebase"
description: "이 문서는 를 위한 Firebase Adapter입니다. 이 패키지는 기본  패키지와 함께 사용할 때만 동작합니다. 독립적으로 사용할 수 있는 패키지가 아닙니다."
---

Source URL: https://next-auth.js.org/v3/adapters/firebase

버전: v3

# Firebase

이 문서는 [`next-auth`](https://next-auth.js.org)를 위한 Firebase Adapter입니다. 이 패키지는 기본 `next-auth` 패키지와 함께 사용할 때만 동작합니다. 독립적으로 사용할 수 있는 패키지가 아닙니다.

## 시작하기[​](https://next-auth.js.org/v3/adapters/firebase#getting-started "제목으로 직접 링크")

1. `next-auth`와 `@next-auth/firebase-adapter@canary`를 설치합니다.

```
    npm install next-auth @next-auth/firebase-adapter@canary

```

2. 이 어댑터를 `pages/api/auth/[...nextauth].js`의 next-auth 구성 객체에 추가합니다.

pages/api/auth/[...nextauth].js

```
    import NextAuth from "next-auth"
    import Providers from "next-auth/providers"
    import { FirebaseAdapter } from "@next-auth/firebase-adapter"

    import firebase from "firebase/app"
    import "firebase/firestore"

    const firestore = (
      firebase.apps[0] ?? firebase.initializeApp(/* your config */)
    ).firestore()

    // For more information on each option (and a full list of options) go to
    // https://next-auth.js.org/configuration/options
    export default NextAuth({
      // https://providers.authjs.dev
      providers: [
        Providers.Google({
          clientId: process.env.GOOGLE_ID,
          clientSecret: process.env.GOOGLE_SECRET,
        }),
      ],
      adapter: FirebaseAdapter(firestore),
      ...
    })

```

## 옵션[​](https://next-auth.js.org/v3/adapters/firebase#options "제목으로 직접 링크")

firestore adapter를 초기화할 때는 프로젝트 세부 정보가 포함된 firebase config 객체를 반드시 전달해야 합니다. 해당 config 객체를 얻는 방법에 대한 자세한 내용은 [여기](https://support.google.com/firebase/answer/7015592)에서 확인할 수 있습니다.

firebase config 예시는 다음과 같습니다.

```
    const firebaseConfig = {
      apiKey: "AIzaSyDOCAbC123dEf456GhI789jKl01-MnO",
      authDomain: "myapp-project-123.firebaseapp.com",
      databaseURL: "https://myapp-project-123.firebaseio.com",
      projectId: "myapp-project-123",
      storageBucket: "myapp-project-123.appspot.com",
      messagingSenderId: "65211879809",
      appId: "1:65211879909:web:3ae38ef1cdcb2e01fe5f0c",
      measurementId: "G-8GSGZQ44ST",
    }

```

자세한 내용은 [firebase.google.com/docs/web/setup](https://firebase.google.com/docs/web/setup)을 참고하세요.

**Firebase 안내**

**주의** : 앱의 Firebase config 파일 또는 객체를 수동으로 수정하는 것은 권장하지 않습니다. 이러한 필수 "Firebase options" 중 하나라도 유효하지 않거나 누락된 값으로 앱을 초기화하면 최종 사용자에게 심각한 문제가 발생할 수 있습니다.

오픈 소스 프로젝트의 경우, 일반적으로 앱의 Firebase config 파일 또는 객체를 소스 제어에 포함하는 것을 권장하지 않습니다. 대부분의 경우 사용자는 각자 Firebase 프로젝트를 생성하고, 자신의 Firebase 리소스(자신의 Firebase config 파일 또는 객체를 통해)를 사용하도록 앱을 설정해야 하기 때문입니다.
