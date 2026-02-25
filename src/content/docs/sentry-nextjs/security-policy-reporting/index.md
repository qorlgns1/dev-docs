---
title: '보안 정책 보고 설정 | Next.js용 Sentry'
description: 'Sentry는 적절한 HTTP 헤더를 설정해 Content-Security-Policy (CSP) 위반 정보를 수집할 수 있도록 지원하며, 이 설정을 통해 위반 보고가 *report-uri*에 지정된 Sentry 엔드포인트로 전송됩니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/security-policy-reporting

# 보안 정책 보고 설정 | Next.js용 Sentry

Sentry는 적절한 HTTP 헤더를 설정해 [Content-Security-Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) 위반 정보를 수집할 수 있도록 지원하며, 이 설정을 통해 위반 보고가 *report-uri*에 지정된 Sentry 엔드포인트로 전송됩니다.

통합 과정은 **Project Settings > Security Headers**에서 찾을 수 있는 프로젝트 키의 Security Header 엔드포인트를 사용해 적절한 헤더를 구성하는 것으로 이루어집니다.

## [Content-Security-Policy](https://docs.sentry.io/platforms/javascript/guides/nextjs/security-policy-reporting.md#content-security-policy)

[Content-Security-Policy](https://en.wikipedia.org/wiki/Content_Security_Policy)(CSP)는 신뢰된 웹 페이지 컨텍스트에서 악성 콘텐츠가 실행되어 발생하는 크로스 사이트 스크립팅(XSS), 클릭재킹 및 기타 코드 주입 공격을 방지하는 데 도움이 되는 보안 표준입니다. 이는 브라우저 벤더에 의해 적용되며, Sentry는 표준 CSP 보고 훅을 사용해 CSP 위반을 수집할 수 있도록 지원합니다.

Sentry에서 CSP 보고를 구성하려면, 정책을 설명하고 인증된 Sentry 엔드포인트를 지정하는 헤더를 서버에서 전송해야 합니다:

```bash
Content-Security-Policy: ...;
    report-uri https://___ORG_INGEST_DOMAIN___/api/___PROJECT_ID___/security/?sentry_key=___PUBLIC_KEY___;
    report-to csp-endpoint

Report-To: {"group":"csp-endpoint","max_age":10886400,"endpoints":[{"url":"https://___ORG_INGEST_DOMAIN___/api/___PROJECT_ID___/security/?sentry_key=___PUBLIC_KEY___"}],"include_subdomains":true}
Reporting-Endpoints: csp-endpoint="https://___ORG_INGEST_DOMAIN___/api/___PROJECT_ID___/security/?sentry_key=___PUBLIC_KEY___"
```

##### 호환성 권장 사항

`report-to` 지시어는 더 이상 사용되지 않는 `report-uri` 지시어를 대체하도록 의도되었지만, 아직 대부분의 브라우저에서 `report-to`를 지원하지 않습니다. 따라서 현재 브라우저와의 호환성을 유지하면서 브라우저가 `report-to`를 지원할 때의 전방 호환성도 확보하려면, Content-Security-Policy (CSP)에 `report-uri`와 `report-to`를 모두 지정하고 [Report-To](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Report-To) 및 [Reporting-Endpoints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Reporting-Endpoints) 헤더도 추가할 수 있습니다.

또는 정책을 강제하는 대신 보고만 전송하도록 CSP 보고를 설정할 수도 있습니다:

```bash
Content-Security-Policy-Report-Only: ...;
    report-uri https://___ORG_INGEST_DOMAIN___/api/___PROJECT_ID___/security/?sentry_key=___PUBLIC_KEY___;
    report-to csp-endpoint

Report-To: {"group":"csp-endpoint","max_age":10886400,"endpoints":[{"url":"https://___ORG_INGEST_DOMAIN___/api/___PROJECT_ID___/security/?sentry_key=___PUBLIC_KEY___"}],"include_subdomains":true}
Reporting-Endpoints: csp-endpoint="https://___ORG_INGEST_DOMAIN___/api/___PROJECT_ID___/security/?sentry_key=___PUBLIC_KEY___"
```

정책을 정의할 때는 `sentry.io` 또는 자체 호스팅 Sentry 도메인이 `default-src` 또는 `connect-src` 정책에 포함되어 있는지 반드시 확인해야 합니다. 그렇지 않으면 브라우저가 정책 위반 제출 요청을 차단합니다.

자세한 내용은 [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) 문서를 참고하세요.

## [추가 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/security-policy-reporting.md#additional-configuration)

`sentry_key` 매개변수 외에도, 보고 URI의 쿼리 문자열에 다음 항목을 전달할 수 있습니다:

`sentry_environment`

환경 이름(예: production)입니다. 환경 이름은 대소문자를 구분하며 줄바꿈, 공백 또는 슬래시를 포함할 수 없습니다. 또한 "None" 문자열일 수 없고 64자를 초과할 수 없습니다.

`sentry_release`

애플리케이션의 버전입니다.

