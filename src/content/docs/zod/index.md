---
title: '추천 스폰서: Jazz'
description: 'TypeScript 우선 스키마 유효성 검사 및 정적 타입 추론'
---

**Zod**

TypeScript 우선 스키마 유효성 검사 및 정적 타입 추론  
작성자 [@colinhacks](https://x.com/colinhacks)

[](https://github.com/colinhacks/zod/actions?query=branch%3Amain)[](https://twitter.com/colinhacks)[](https://opensource.org/licenses/MIT)[](https://www.npmjs.com/package/zod)[](https://github.com/colinhacks/zod)

[웹사이트](https://zod.dev) • [Discord](https://discord.gg/RcG33DQJdf) • [𝕏](https://twitter.com/colinhacks) • [Bluesky](https://bsky.app/profile/zod.dev)

Zod 4가 이제 안정화되었습니다! [릴리스 노트 읽기](https://zod.dev/v4).

## 추천 스폰서: Jazz

[](https://jazz.tools/?utm_source=zod)

소개를 원하시나요? [문의하기](https://zod.dev/cdn-cgi/l/email-protection#85f6f5eaebf6eaf7f6edecf5c5e6eae9ecebede4e6eef6abe6eae8)

## [소개](https://zod.dev/?id=introduction)

Zod는 TypeScript 우선 유효성 검사 라이브러리입니다. Zod를 사용하면 간단한 `string`부터 복잡한 중첩 객체까지 데이터를 검증하는 _스키마_를 정의할 수 있습니다.
```
    import * as z from "zod";

    const User = z.object({
      name: z.string(),
    });

    // 일부 신뢰되지 않은 데이터...
    const input = { /* stuff */ };

    // 구문 분석된 결과는 검증되며 타입 안전합니다!
    const data = User.parse(input);

    // 그러므로 안심하고 사용할 수 있습니다 :)
    console.log(data.name);
```

## [특징](https://zod.dev/?id=features)

  * 외부 의존성 없음
  * Node.js 및 모든 최신 브라우저에서 작동
  * 작음: 코어 번들 2kb (gzip)
  * 불변 API: 메서드는 새 인스턴스 반환
  * 간결한 인터페이스
  * TypeScript 및 일반 JS와 호환
  * 내장 JSON Schema 변환
  * 광범위한 생태계

## [설치](https://zod.dev/?id=installation)
```
    npm install zod
```

Zod는 [jsr.io](https://jsr.io/@zod/zod)에서 `@zod/zod`로도 제공됩니다.

Zod는 에이전트가 Zod 문서를 검색할 수 있는 MCP 서버를 제공합니다. 에디터에 추가하려면 [이 지침](https://share.inkeep.com/zod/mcp)을 따르세요. Zod는 또한 [llms.txt](https://zod.dev/llms.txt) 파일을 제공합니다.

## [요구 사항](https://zod.dev/?id=requirements)

Zod는 _TypeScript v5.5_ 이상에서 테스트되었습니다. 이전 버전도 작동할 수 있지만 공식적으로 지원되지 않습니다.

- [`"strict"`](https://zod.dev/?id=strict)

`tsconfig.json`에서 `strict` 모드를 반드시 활성화해야 합니다. 이는 모든 TypeScript 프로젝트에 대한 권장 사항입니다.
```
    // tsconfig.json
    {
      // ...
      "compilerOptions": {
        // ...
        "strict": true
      }
    }
```

## [생태계](https://zod.dev/?id=ecosystem)

Zod는 활발한 라이브러리, 도구, 통합 생태계를 갖추고 있습니다. Zod를 지원하거나 그 위에 구축된 라이브러리의 전체 목록은 [생태계 페이지](https://zod.dev/ecosystem)를 참고하세요.

  * [리소스](https://zod.dev/ecosystem?id=resources)
  * [API 라이브러리](https://zod.dev/ecosystem?id=api-libraries)
  * [폼 통합](https://zod.dev/ecosystem?id=form-integrations)
  * [Zod에서 X로](https://zod.dev/ecosystem?id=zod-to-x)
  * [X에서 Zod로](https://zod.dev/ecosystem?id=x-to-zod)
  * [모킹 라이브러리](https://zod.dev/ecosystem?id=mocking-libraries)
  * [Zod 기반](https://zod.dev/ecosystem?id=powered-by-zod)

다음 프로젝트에도 기여하고 있으며 강조하고 싶습니다:

  * [tRPC](https://trpc.io) \- Zod 스키마를 지원하는 종단간 타입 안전 API
  * [React Hook Form](https://react-hook-form.com) \- [Zod resolver](https://react-hook-form.com/docs/useform#resolver)를 사용하는 훅 기반 폼 검증
  * [zshy](https://github.com/colinhacks/zshy) \- 원래 Zod 내부 빌드 도구로 만들어졌습니다. 번들러 없이 TypeScript 라이브러리를 위한 만능 빌드 도구. `tsc` 기반.

## [스폰서](https://zod.dev/?id=sponsors)

모든 수준의 후원을 감사히 여기며 권장합니다. Zod로 유료 제품을 구축했다면 [기업 티어](https://github.com/sponsors/colinhacks)를 고려해보세요.

- [플래티넘](https://zod.dev/?id=platinum)

[](https://www.coderabbit.ai/)

코드 리뷰 시간 및 버그 절반으로 단축

[coderabbit.ai](https://www.coderabbit.ai/)

- [골드](https://zod.dev/?id=gold)

[](https://brand.dev/?utm_source=zod)

로고, 색상, 회사 정보를 위한 API

[brand.dev](https://brand.dev/?utm_source=zod)

[](https://www.courier.com/?utm_source=zod&utm_campaign=osssponsors)

알림 전송을 위한 API 플랫폼

[courier.com](https://www.courier.com/?utm_source=zod&utm_campaign=osssponsors)

[](https://liblab.com/?utm_source=zod)

API용 더 나은 SDK 생성

[liblab.com](https://liblab.com/?utm_source=zod)

[](https://neon.tech)

서버리스 Postgres — 더 빠르게 출시

[neon.tech](https://neon.tech)

[](https://retool.com/?utm_source=github&utm_medium=referral&utm_campaign=zod)

Retool AI로 AI 앱 및 워크플로 구축

[retool.com](https://retool.com/?utm_source=github&utm_medium=referral&utm_campaign=zod)

[](https://stainlessapi.com)

최고 수준의 SDK 생성

[stainlessapi.com](https://stainlessapi.com)

[](https://speakeasy.com/?utm_source=zod+docs)

API용 SDK 및 Terraform 공급자

[speakeasy.com](https://speakeasy.com/?utm_source=zod+docs)

- [실버](https://zod.dev/?id=silver)

[sanity.io](https://www.sanity.io/)

[subtotal.com](https://www.subtotal.com/?utm_source=zod)

[nitric.io](https://nitric.io/)

[propelauth.com](https://www.propelauth.com/)

[cerbos.dev](https://cerbos.dev/)

[scalar.com](https://scalar.com/)

[trigger.dev](https://trigger.dev)

[transloadit.com](https://transloadit.com/?utm_source=zod&utm_medium=referral&utm_campaign=sponsorship&utm_content=github)

[infisical.com](https://infisical.com)

[whop.com](https://whop.com/)

[cryptojobslist.com](https://cryptojobslist.com/)

[plain.com](https://plain.com/)

[inngest.com](https://inngest.com/)

[storyblok.com](https://storyblok.com/)

[mux.link/zod](https://mux.link/zod)

- [브론즈](https://zod.dev/?id=bronze)

[](https://mintlify.com)[mintlify.com](https://mintlify.com)

[](https://www.val.town/)[val.town](https://www.val.town/)

[](https://www.route4me.com/)[route4me.com](https://www.route4me.com/)

[](https://encore.dev)[encore.dev](https://encore.dev)

[](https://www.replay.io/)[replay.io](https://www.replay.io/)

[](https://www.numeric.io)[numeric.io](https://www.numeric.io)

[](https://marcatopartners.com)[marcatopartners.com](https://marcatopartners.com)

[](https://interval.com)[interval.com](https://interval.com)

[](https://seasoned.cc)[seasoned.cc](https://seasoned.cc)

[](https://www.bamboocreative.nz/)[bamboocreative.nz](https://www.bamboocreative.nz/)

[](https://github.com/jasonLaster)[github.com/jasonLaster](https://github.com/jasonLaster)

[](https://www.clipboardhealth.com/engineering)[clipboardhealth.com/engineering](https://www.clipboardhealth.com/engineering)

