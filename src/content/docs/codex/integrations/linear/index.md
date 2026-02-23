---
title: Linear에서 Codex 사용
description: "원본 URL: https://developers.openai.com/codex/integrations/linear"
---

# Linear에서 Codex 사용

원본 URL: https://developers.openai.com/codex/integrations/linear

Linear에서 Codex를 사용하면 이슈에서 작업을 위임할 수 있습니다. 이슈를 Codex에 할당하거나 댓글에서 `@Codex`를 언급하면 Codex가 클라우드 태스크를 생성하고 진행 상황과 결과를 답변합니다.

Codex in Linear는 유료 요금제에서 사용할 수 있습니다([가격](https://developers.openai.com/codex/pricing) 참고).

Enterprise 요금제를 사용 중이라면 ChatGPT 워크스페이스 관리자에게 [워크스페이스 설정](https://chatgpt.com/admin/settings)에서 Codex 클라우드 태스크를 켜고 [커넥터 설정](https://chatgpt.com/admin/ca)에서 **Codex for Linear**를 활성화해 달라고 요청하세요.

## Linear 통합 설정

  1. [Codex](https://chatgpt.com/codex)에서 GitHub를 연결하고 Codex가 작업할 리포지토리용 [환경](https://developers.openai.com/codex/cloud/environments)을 생성하여 [Codex 클라우드 태스크](https://developers.openai.com/codex/cloud)를 설정합니다.
  2. [Codex 설정](https://chatgpt.com/codex/settings/connectors)으로 이동하여 워크스페이스에 **Codex for Linear**를 설치합니다.
  3. Linear 이슈의 댓글 스레드에서 `@Codex`를 언급해 Linear 계정을 연결합니다.

## Codex에 작업 위임

다음 두 가지 방식으로 위임할 수 있습니다.

### Codex에 이슈 할당

통합을 설치한 후에는 팀원에게 할당하듯 Codex에게 이슈를 할당할 수 있습니다. Codex가 작업을 시작하고 업데이트를 이슈에 게시합니다.

### 댓글에서 `@Codex` 언급

댓글 스레드에서 `@Codex`를 언급해 작업을 위임하거나 질문할 수도 있습니다. Codex가 답변한 뒤에는 같은 스레드에서 계속 후속 질문을 하세요.

Codex가 이슈 작업을 시작하면 작업할 [환경과 리포지토리를 선택](https://developers.openai.com/codex/integrations/linear#how-codex-chooses-an-environment-and-repo)합니다. 특정 리포지토리를 고정하려면 댓글에 포함하세요. 예: `@Codex fix this in openai/codex`.

진행 상황을 추적하려면:

  * 이슈에서 **Activity**를 열어 진행 업데이트를 확인하세요.
  * 태스크 링크를 열어 더 자세히 따라가세요.

태스크가 완료되면 Codex가 요약과 완료된 태스크 링크를 게시하므로 이를 사용해 풀 리퀘스트를 생성할 수 있습니다.

### Codex가 환경과 리포지토리를 선택하는 방식

  * Linear는 이슈 컨텍스트를 기반으로 리포지토리를 제안합니다. Codex는 해당 제안과 가장 잘 맞는 환경을 선택합니다. 요청이 모호하면 가장 최근에 사용한 환경으로 돌아갑니다.
  * 태스크는 해당 환경의 리포지도에서 첫 번째로 나열된 리포지토리의 기본 브랜치에서 실행됩니다. 다른 기본값이나 추가 리포지토리가 필요하면 Codex에서 리포지도 맵을 업데이트하세요.
  * 적절한 환경이나 리포지토리가 없으면 Codex는 Linear에서 문제를 해결한 뒤 다시 시도하는 방법을 안내합니다.

## Codex에 자동으로 이슈 할당

트리아지 규칙을 사용해 이슈를 Codex에 자동으로 할당할 수 있습니다.

  1. Linear에서 **Settings**로 이동합니다.
  2. **Your teams**에서 팀을 선택합니다.
  3. 워크플로 설정에서 **Triage**를 열어 활성화합니다.
  4. **Triage rules**에서 규칙을 만들고 **Delegate** > **Codex**(및 설정하려는 다른 속성)를 선택합니다.

Linear는 트리아지에 들어오는 새 이슈를 자동으로 Codex에 할당합니다. 트리아지 규칙을 사용하면 Codex는 이슈 작성자의 계정으로 태스크를 실행합니다.

## 데이터 사용, 프라이버시, 보안

`@Codex`를 언급하거나 이슈를 할당하면 Codex는 요청을 이해하고 태스크를 만들기 위해 이슈 내용을 수신합니다. 데이터 처리는 OpenAI의 [프라이버시 정책](https://openai.com/privacy), [이용 약관](https://openai.com/terms/), 기타 적용 가능한 [정책](https://openai.com/policies)을 따릅니다. 보안 관련 추가 정보는 [Codex 보안 문서](https://developers.openai.com/codex/security)를 참고하세요.

Codex는 실수를 할 수 있는 대규모 언어 모델을 사용합니다. 항상 답변과 diff를 검토하세요.

## 팁 및 문제 해결

  * **Missing connections**: Codex가 Linear 연결을 확인할 수 없으면 계정 연결 링크와 함께 이슈에 답변합니다.

* **예상치 못한 환경 선택** : 원하는 환경을 스레드에 답글로 남겨 주세요 (예: `@Codex please run this in openai/codex`).
  * **잘못된 코드 부분** : 이슈에 더 많은 컨텍스트를 추가하거나 `@Codex` 댓글에서 명확한 지시를 제공하세요.
  * **추가 도움** : [OpenAI 도움말 센터](https://help.openai.com/)를 참고하세요.



## 로컬 작업을 위한 Linear 연결 (MCP)

Codex 앱, CLI, 또는 IDE 확장을 사용하면서 Codex가 로컬 Linear 이슈에 접근하도록 하려면 Linear Model Context Protocol(MCP) 서버를 사용하도록 Codex를 구성하세요.

자세한 내용은 [Linear MCP 문서](https://linear.app/integrations/codex-mcp)를 확인하세요.

IDE 확장을 사용하든 CLI를 사용하든, 두 환경이 동일한 구성을 공유하므로 MCP 서버 설정 단계는 같습니다.

### CLI 사용(권장)

CLI가 설치되어 있다면 다음을 실행하세요:
[code] 
    codex mcp add linear --url https://mcp.linear.app/mcp
[/code]

그러면 Linear 계정으로 로그인하고 Codex와 연결하라는 메시지가 표시됩니다.

### 수동 구성

  1. 편집기에서 `~/.codex/config.toml`을 엽니다.
  2. 다음을 추가합니다:


[code] 
    [mcp_servers.linear]
    url = "https://mcp.linear.app/mcp"
[/code]

  3. `codex mcp login linear`를 실행해 로그인합니다.
