---
title: '함수: userAgent'
description: '최종 업데이트: 2026년 2월 20일'
---

# 함수: userAgent | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/functions/userAgent

[API Reference](https://nextjs.org/docs/app/api-reference)[Functions](https://nextjs.org/docs/app/api-reference/functions)userAgent

페이지 복사

# userAgent

최종 업데이트: 2026년 2월 20일

`userAgent` 헬퍼는 요청에서 사용자 에이전트 객체와 상호작용할 수 있도록 [Web Request API](https://developer.mozilla.org/docs/Web/API/Request)에 추가 속성과 메서드를 확장합니다.

proxy.ts

JavaScriptTypeScript
[code]
    import { NextRequest, NextResponse, userAgent } from 'next/server'
     
    export function proxy(request: NextRequest) {
      const url = request.nextUrl
      const { device } = userAgent(request)
     
      // device.type can be: 'mobile', 'tablet', 'console', 'smarttv',
      // 'wearable', 'embedded', or undefined (for desktop browsers)
      const viewport = device.type || 'desktop'
     
      url.searchParams.set('viewport', viewport)
      return NextResponse.rewrite(url)
    }
[/code]

## `isBot`[](https://nextjs.org/docs/app/api-reference/functions/userAgent#isbot)

요청이 알려진 봇에서 왔는지를 나타내는 불리언 값입니다.

## `browser`[](https://nextjs.org/docs/app/api-reference/functions/userAgent#browser)

요청에 사용된 브라우저 정보를 담고 있는 객체입니다.

  * `name`: 브라우저 이름을 나타내는 문자열이며, 식별할 수 없는 경우 `undefined`입니다.
  * `version`: 브라우저 버전을 나타내는 문자열이며, 식별할 수 없는 경우 `undefined`입니다.



## `device`[](https://nextjs.org/docs/app/api-reference/functions/userAgent#device)

요청에 사용된 디바이스 정보를 담고 있는 객체입니다.

  * `model`: 디바이스 모델을 나타내는 문자열이며, 없으면 `undefined`입니다.
  * `type`: `console`, `mobile`, `tablet`, `smarttv`, `wearable`, `embedded` 또는 `undefined`와 같이 디바이스 유형을 나타내는 문자열입니다.
  * `vendor`: 디바이스 제조사를 나타내는 문자열이며, 없으면 `undefined`입니다.



## `engine`[](https://nextjs.org/docs/app/api-reference/functions/userAgent#engine)

브라우저 엔진 정보를 담고 있는 객체입니다.

  * `name`: 엔진 이름을 나타내는 문자열입니다. 가능한 값은 `Amaya`, `Blink`, `EdgeHTML`, `Flow`, `Gecko`, `Goanna`, `iCab`, `KHTML`, `Links`, `Lynx`, `NetFront`, `NetSurf`, `Presto`, `Tasman`, `Trident`, `w3m`, `WebKit` 또는 `undefined`입니다.
  * `version`: 엔진 버전을 나타내는 문자열이며, 없으면 `undefined`입니다.



## `os`[](https://nextjs.org/docs/app/api-reference/functions/userAgent#os)

운영체제 정보를 담고 있는 객체입니다.

  * `name`: OS 이름을 나타내는 문자열이며, 없으면 `undefined`입니다.
  * `version`: OS 버전을 나타내는 문자열이며, 없으면 `undefined`입니다.



## `cpu`[](https://nextjs.org/docs/app/api-reference/functions/userAgent#cpu)

CPU 아키텍처 정보를 담고 있는 객체입니다.

  * `architecture`: CPU 아키텍처를 나타내는 문자열입니다. 가능한 값은 `68k`, `amd64`, `arm`, `arm64`, `armhf`, `avr`, `ia32`, `ia64`, `irix`, `irix64`, `mips`, `mips64`, `pa-risc`, `ppc`, `sparc`, `sparc64` 또는 `undefined`입니다.



도움이 되었나요?

지원됨.

보내기
