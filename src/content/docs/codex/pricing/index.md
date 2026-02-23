---
title: 'Codex 요금제'
description: '한시적으로 ChatGPT Free와 Go에서 Codex를 무료로 체험하거나 Plus, Pro, Business, Enterprise 구독으로'
---

Source URL: https://developers.openai.com/codex/pricing

# Codex 요금제

한시적으로 **ChatGPT Free와 Go에서 Codex를 무료로 체험**하거나 Plus, Pro, Business, Enterprise 구독으로  
**2배 빨라진 Codex 속도 제한**을 누려보세요.

### Plus
매주 몇 차례 집중적인 코딩 세션에 적합합니다.  
가격: $20/월  
[Plus 가입](https://chatgpt.com/explore/plus?utm_internal_source=openai_developers_codex)

    - 웹, CLI, IDE 확장, iOS에서 사용할 수 있는 Codex
    - 자동 코드 리뷰 및 Slack 통합 같은 클라우드 기반 통합 기능
    - GPT-5.3-Codex를 포함한 최신 모델
    - 로컬 메시지에 대해 최대 4배 더 높은 사용량 한도를 제공하는 GPT-5.1-Codex-Mini
    - [ChatGPT 크레딧](#credits-overview)으로 유연하게 사용량 확장
    - Plus 요금제의 다른 [ChatGPT 기능](https://chatgpt.com/pricing)

### Pro
매일 정규 근무 시간 내내 Codex에 의존하는 경우.  
가격: $200/월  
[Pro 가입](https://chatgpt.com/explore/pro?utm_internal_source=openai_developers_codex)

    - 우선 요청 처리
    - 일상 코딩 작업을 위한 빠른 Codex 모델인 GPT-5.3-Codex-Spark(리서치 프리뷰) 접근
    - 로컬 및 클라우드 작업에 대해 6배 더 높은 사용량 한도
    - 클라우드 기반 코드 리뷰 10배 증가
    - Pro 요금제의 다른 [ChatGPT 기능](https://chatgpt.com/pricing)

### Business
스타트업이나 성장 중인 비즈니스에 Codex 도입.  
가격: $30/사용자/월  
[무료 체험](https://chatgpt.com/team-sign-up?utm_internal_source=openai_developers_codex)

    - 클라우드 작업을 더 빠르게 처리하는 더 큰 가상 머신
    - [ChatGPT 크레딧](#credits-overview)으로 유연하게 사용량 확장
    - 필수 관리자 제어, SAML SSO, MFA를 갖춘 보안 전용 워크스페이스
    - 기본적으로 비즈니스 데이터를 학습하지 않음. [자세히 알아보기](https://openai.com/business-data/)
    - Business 요금제의 다른 [ChatGPT 기능](https://chatgpt.com/pricing)

### Enterprise & Edu
전체 조직을 위한 엔터프라이즈급 기능을 갖춘 Codex 해제.  
[영업팀에 문의](https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex)

    - 우선 요청 처리
    - SCIM, EKM, 사용자 분석, 도메인 검증, 역할 기반 접근 제어([RBAC](https://help.openai.com/en/articles/11750701-rbac))를 포함한 엔터프라이즈급 보안 및 제어
    - [Compliance API](https://chatgpt.com/admin/api-reference#tag/Codex-Tasks)를 통한 감사 로그 및 사용량 모니터링
    - 데이터 보존 및 거주지 제어
    - Enterprise 요금제의 다른 [ChatGPT 기능](https://chatgpt.com/pricing)

### API Key
CI처럼 공유 환경에서 자동화를 구현할 때 적합합니다.  
[자세히 알아보기](https://developers.openai.com/codex/auth)

    - CLI, SDK, IDE 확장에 포함된 Codex
    - GitHub 코드 리뷰, Slack 등 클라우드 기반 기능 없음
    - GPT-5.3-Codex 및 GPT-5.3-Codex-Spark 같은 신규 모델은 지연된 접근
    - [API 요금](https://platform.openai.com/docs/pricing)에 따라 Codex가 사용하는 토큰에 대해서만 결제

## 자주 묻는 질문

### 내 요금제의 사용 한도는 어떻게 되나요?

보내는 Codex 메시지 수는 코딩 작업의 규모와 복잡도, 로컬 또는 클라우드 실행 여부에 따라 달라집니다.  
작은 스크립트나 일상 함수는 할당량의 일부만 소모하고, 더 큰 코드베이스나 장시간 실행, Codex가 더 많은 컨텍스트를 유지해야 하는 연장된 세션은 메시지당 훨씬 더 많이 소모합니다.

<table>
  <thead>
    <tr>
      <th scope="col"></th>
      <th scope="col" style="text-align:center">
        로컬 메시지[\*](#shared-limits) / 5h
      </th>
      <th scope="col" style="text-align:center">
        클라우드 작업[\*](#shared-limits) / 5h
      </th>
      <th scope="col" style="text-align:center">
        코드 리뷰 / 주
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ChatGPT Plus</td>
      <td style="text-align:center">45-225</td>
      <td style="text-align:center">10-60</td>
      <td style="text-align:center">10-25</td>
    </tr>
    <tr>
      <td>ChatGPT Pro</td>
      <td style="text-align:center">300-1500</td>
      <td style="text-align:center">50-400</td>
      <td style="text-align:center">100-250</td>
    </tr>
    <tr>
      <td>ChatGPT Business</td>
      <td style="text-align:center">45-225</td>
      <td style="text-align:center">10-60</td>
      <td style="text-align:center">10-25</td>
    </tr>
    <tr>
      <td>ChatGPT Enterprise &amp; Edu</td>
      <td colspan="3" style="text-align:center">
        고정 한도 없음 — 사용량은 [크레딧](#credits-overview)에 따라 확장
      </td>
    </tr>
    <tr>
      <td>API Key</td>
      <td style="text-align:center">
        [사용량 기반](https://platform.openai.com/docs/pricing)
      </td>
      <td style="text-align:center">지원 안 됨</td>
      <td style="text-align:center">지원 안 됨</td>
    </tr>
  </tbody>
</table>

<a id="shared-limits" class="footnote">
  *로컬 메시지와 클라우드 작업의 사용 한도는 **5시간 창**을 공유합니다. 추가 주간 한도가 적용될 수 있습니다.
</a>

유연한 가격 정책이 없는 Enterprise 및 Edu 요금제는 대부분 기능에 대해 Plus와 동일한 좌석별 한도를 가집니다.

GPT-5.1-Codex-Mini는 로컬 작업에 사용 가능하며 최대 4배 더 많은 사용량을 제공합니다.

GPT-5.3-Codex-Spark는 ChatGPT Pro 사용자만을 위한 리서치 프리뷰이며 출시 시점 API에서는 제공되지 않습니다.  
전용 저지연 하드웨어에서 실행되므로 수요에 따라 조정될 수 있는 별도의 사용 한도로 운영됩니다.

### 사용 한도에 도달하면 어떻게 되나요?

ChatGPT Plus 및 Pro 사용자는 한도에 도달하면 기존 요금제를 업그레이드하지 않고도 계속 작업할 수 있도록 추가 크레딧을 구매할 수 있습니다.

[유연한 가격 정책](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)이 적용되는 Business, Edu 및 Enterprise 요금제는 추가 워크스페이스 크레딧으로 Codex를 계속 사용할 수 있습니다.

사용 한도에 가까워지면 GPT-5.1-Codex-Mini 모델로 전환하여 한도를 더욱 오래 유지할 수도 있습니다.

모든 사용자는 API 키를 사용해 추가 로컬 작업을 실행할 수 있으며, 사용량은 [표준 API 요금](https://platform.openai.com/docs/pricing)으로 청구됩니다.

### 현재 사용 한도는 어디에서 확인할 수 있나요?

[Codex 사용 대시보드](https://chatgpt.com/codex/settings/usage)에서 현재 한도를 확인할 수 있습니다.  
활성 Codex CLI 세션 도중 남은 한도를 확인하려면 `/status`를 사용할 수 있습니다.

### 크레딧은 어떻게 작동하나요?

크레딧은 포함된 사용 한도를 넘겼을 때 Codex를 계속 사용할 수 있게 해줍니다.  
사용량은 사용한 모델과 기능에 따라 가용 크레딧에서 차감되어, 작업을 중단 없이 이어갈 수 있습니다.

메시지당 크레딧 비용은 작업 규모, 복잡도, 요구되는 추론량에 따라 달라집니다.  
표는 평균 크레딧 비용을 보여주며, 이러한 평균은 GPT-5.2, GPT-5.2-Codex, GPT-5.1, GPT-5.1-Codex-Max, GPT-5, GPT-5-Codex, GPT-5-Codex-Mini에도 적용됩니다.  
새로운 기능이 도입되면 평균 요율은 시간이 지나면서 변경될 수 있습니다.

|             |      단위      | GPT-5.3-Codex, GPT-5.2-Codex | GPT-5.1-Codex-Mini |
| :---------- | :------------: | :--------------------------: | :----------------: |
| 로컬 작업    |   1 메시지     |         \~5 크레딧           |     \~1 크레딧     |
| 클라우드 작업 |   1 메시지     |         \~25 크레딧          |   제공 안 됨       |
| 코드 리뷰    | 1 풀 리퀘스트  |         \~25 크레딧          |   제공 안 됨       |

[ChatGPT Free, Go, Plus, Pro의 유연한 사용을 위한 크레딧 더 알아보기.](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora)  
[ChatGPT Business, Enterprise, Edu의 크레딧 더 알아보기.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)

### 코드 리뷰 사용량은 무엇을 의미하나요?

코드 리뷰 사용량은 Codex가 GitHub을 통해 리뷰를 실행할 때만 적용됩니다. 예를 들어 풀 리퀘스트에서 `@Codex`를 태그하거나 저장소에 자동 리뷰를 활성화한 경우입니다.  
GitHub 외부에서 실행되거나 로컬에서 수행된 리뷰는 일반 사용 한도에 포함됩니다.

### 사용 한도를 오래 유지하려면 어떻게 해야 하나요?

위의 사용 한도와 크레딧은 평균 요율입니다. 한도를 최대한 활용하기 위해 다음 팁을 시도해보세요:

- **프롬프트 크기를 조절하세요.** Codex에 지시할 때 정확하게 전달하되 불필요한 컨텍스트는 제거하세요.
- **AGENTS.md 크기를 줄이세요.** 큰 프로젝트에서 작업한다면 [저장소 내에 AGENTS.md를 계층적으로 배치](https://developers.openai.com/codex/guides/agents-md#layer-project-instructions)하여 주입하는 컨텍스트를 제어할 수 있습니다.
- **사용하는 MCP 서버 수를 제한하세요.** Codex에 등록하는 [MCP](https://developers.openai.com/codex/mcp)마다 메시지에 더 많은 컨텍스트가 추가되어 한도를 더 많이 사용합니다. 필요 없을 때는 MCP 서버를 비활성화하세요.
- **일상 작업에는 GPT-5.1-Codex-Mini로 전환하세요.** 미니 모델을 사용하면 사용 한도를 약 4배 더 오래 유지할 수 있습니다.
