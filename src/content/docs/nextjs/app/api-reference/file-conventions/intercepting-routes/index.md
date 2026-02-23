---
title: '파일 시스템 규칙: 인터셉트(Intercepting) 라우트'
description: '인터셉트 라우트를 사용하면 현재 레이아웃 안에서 앱의 다른 위치에 있는 라우트를 로드할 수 있습니다. 이 라우팅 패러다임은 사용자가 다른 컨텍스트로 전환하지 않고도 특정 라우트의 콘텐츠를 표시하고 싶을 때 유용합니다.'
---

# 파일 시스템 규칙: 인터셉트(Intercepting) 라우트 | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes

[API Reference](https://nextjs.org/docs/app/api-reference)[File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)인터셉트(Intercepting) 라우트

페이지 복사

# 인터셉트 라우트

마지막 업데이트: 2026년 2월 20일

인터셉트 라우트를 사용하면 현재 레이아웃 안에서 앱의 다른 위치에 있는 라우트를 로드할 수 있습니다. 이 라우팅 패러다임은 사용자가 다른 컨텍스트로 전환하지 않고도 특정 라우트의 콘텐츠를 표시하고 싶을 때 유용합니다.

예를 들어 피드에서 사진을 클릭할 때 사진을 피드 위에 오버레이된 모달로 표시할 수 있습니다. 이 경우 Next.js는 `/photo/123` 라우트를 인터셉트하여 URL을 마스킹하고 `/feed` 위에 오버레이합니다.

하지만 공유 가능한 URL을 클릭하거나 페이지를 새로 고쳐서 사진으로 이동할 때는 모달 대신 전체 사진 페이지가 렌더링되어야 합니다. 이때는 라우트 인터셉트가 일어나지 않아야 합니다.

## 규칙[](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention)

인터셉트 라우트는 `(..)` 규칙으로 정의할 수 있으며, 이는 상대 경로 규칙 `../` 와 유사하지만 라우트 세그먼트용입니다.

다음과 같이 사용할 수 있습니다.

  * `(.)`: **동일한 레벨**의 세그먼트 매칭
  * `(..)`: **한 레벨 위** 세그먼트 매칭
  * `(..)(..)`: **두 레벨 위** 세그먼트 매칭
  * `(...)`: **루트** `app` 디렉터리에서 세그먼트 매칭



예를 들어 `feed` 세그먼트 안에서 `photo` 세그먼트를 인터셉트하려면 `(..)photo` 디렉터리를 만들 수 있습니다.

> **참고:** `(..)` 규칙은 파일 시스템이 아니라 _라우트 세그먼트_ 를 기준으로 합니다. 예를 들어 [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)의 `@slot` 폴더는 고려하지 않습니다.

## 예시[](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#examples)

### 모달[](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#modals)

인터셉트 라우트는 [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)와 함께 사용하여 모달을 만들 수 있습니다. 이를 통해 다음과 같은 모달 구축 시 자주 발생하는 과제를 해결할 수 있습니다.

  * 모달 콘텐츠를 **URL로 공유 가능**하게 만들기
  * 모달을 닫는 대신 페이지 새로 고침 시 **컨텍스트 유지**
  * 이전 라우트로 이동하는 대신 **뒤로 가기에서 모달 닫기**
  * 앞으로 가기 시 **모달 다시 열기**



다음 UI 패턴을 생각해 보세요. 사용자가 클라이언트 측 내비게이션으로 갤러리에서 사진 모달을 열 수도 있고, 공유 가능한 URL을 통해 직접 사진 페이지로 이동할 수도 있습니다.

위 예시에서 `photo` 세그먼트의 경로는 `@modal`이 세그먼트가 아닌 슬롯이기 때문에 `(..)` 매처를 사용할 수 있습니다. 즉, 파일 시스템 레벨로는 두 단계 위에 있어도 라우트 세그먼트로는 한 단계만 위라는 뜻입니다.

단계별 예시는 [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#modals) 문서를 참고하거나 [이미지 갤러리 예제](https://github.com/vercel-labs/nextgram)를 확인하세요.

> **참고:**
> 
>   * 다른 예시로는 상단 내비게이션 바에서 `/login` 페이지와 별도로 로그인 모달을 열거나, 사이드 모달에서 장바구니를 여는 경우 등이 있습니다.
> 


## 다음 단계

인터셉트 라우트와 Parallel Routes로 모달 만드는 방법을 알아보세요.

### [Parallel Routes동일 뷰에서 하나 이상의 페이지를 독립적으로 내비게이션하며 동시에 렌더링합니다. 고도로 동적인 애플리케이션에 적합한 패턴입니다.](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)

도움이 되었나요?

지원됨.

보내기
