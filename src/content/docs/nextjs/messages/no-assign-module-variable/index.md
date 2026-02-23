---
title: '모듈 변수 할당 금지'
description: '변수에 어떤 값을 할당하고 있습니다.  변수는 이미 사용 중이므로 여기에 값을 다시 할당하면 오류가 발생할 가능성이 매우 높습니다.'
---

# 모듈 변수 할당 금지 | Next.js

Source URL: https://nextjs.org/docs/messages/no-assign-module-variable

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)모듈 변수 할당 금지

# 모듈 변수 할당 금지

> `module` 변수에 값을 할당하지 마세요.

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/no-assign-module-variable#why-this-error-occurred)

`module` 변수에 어떤 값을 할당하고 있습니다. `module` 변수는 이미 사용 중이므로 여기에 값을 다시 할당하면 오류가 발생할 가능성이 매우 높습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-assign-module-variable#possible-ways-to-fix-it)

다른 변수 이름을 사용하세요:

example.js
[code]
    let myModule = {...}
[/code]

이 정보가 도움이 되었나요?

Send
