---
title: '가이드: JSON-LD'
description: '원본 URL: https://nextjs.org/docs/app/guides/json-ld'
---

# 가이드: JSON-LD | Next.js

원본 URL: https://nextjs.org/docs/app/guides/json-ld

# Next.js 애플리케이션에서 JSON-LD를 구현하는 방법

최종 업데이트 2026년 2월 20일

[JSON-LD](https://json-ld.org/)는 구조화된 데이터를 위한 포맷으로, 검색 엔진과 AI가 순수 콘텐츠를 넘어 페이지의 구조를 이해하도록 돕습니다. 예를 들어 사람, 이벤트, 조직, 영화, 책, 레시피 등 다양한 엔터티 유형을 설명할 때 사용할 수 있습니다.

현재 JSON-LD에 대한 권장 사항은 `layout.js` 또는 `page.js` 컴포넌트에서 `<script>` 태그로 구조화 데이터를 렌더링하는 것입니다.

아래 스니펫은 `JSON.stringify`를 사용하며, 이는 XSS 인젝션에 쓰이는 악성 문자열을 정리하지 않습니다. 이러한 유형의 취약점을 방지하려면, 예를 들어 `<` 문자를 유니코드 등가인 `\u003c`로 바꾸는 방식으로 `JSON-LD` 페이로드에서 `HTML` 태그를 제거할 수 있습니다.

조직에서 권장하는 잠재적으로 위험한 문자열 정리 방식을 검토하거나 [serialize-javascript](https://www.npmjs.com/package/serialize-javascript)와 같은 `JSON.stringify`의 커뮤니티 유지 대안을 사용하세요.

app/products/[id]/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page({ params }) {
      const { id } = await params
      const product = await getProduct(id)

      const jsonLd = {
        '@context': 'https://schema.org',
        '@type': 'Product',
        name: product.name,
        image: product.image,
        description: product.description,
      }

      return (
        <section>
          {/* Add JSON-LD to your page */}
          <script
            type="application/ld+json"
            dangerouslySetInnerHTML={{
              __html: JSON.stringify(jsonLd).replace(/</g, '\\u003c'),
            }}
          />
          {/* ... */}
        </section>
      )
    }
[/code]

구조화 데이터를 Google용 [Rich Results Test](https://search.google.com/test/rich-results) 또는 범용 [Schema Markup Validator](https://validator.schema.org/)로 검증하고 테스트할 수 있습니다.

[`schema-dts`](https://www.npmjs.com/package/schema-dts)와 같은 커뮤니티 패키지를 사용해 TypeScript로 JSON-LD 타입을 지정할 수도 있습니다:
[code]
    import { Product, WithContext } from 'schema-dts'

    const jsonLd: WithContext<Product> = {
      '@context': 'https://schema.org',
      '@type': 'Product',
      name: 'Next.js Sticker',
      image: 'https://nextjs.org/imgs/sticker.png',
      description: 'Dynamic at the speed of static.',
    }
[/code]

보내기
