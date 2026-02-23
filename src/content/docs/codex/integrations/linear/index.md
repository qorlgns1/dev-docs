---
title: 'Linear에서 Codex 사용하기'
description: '이슈에서 작업을 Codex에 위임하려면 Linear에서 Codex를 사용하세요. 이슈를 Codex에 할당하거나 댓글에서 를 언급하면 Codex가 클라우드 태스크를 만들고 진행 상황과 결과를 답글로 알려줍니다.'
---

Source URL: https://developers.openai.com/codex/integrations/linear

# Linear에서 Codex 사용하기

이슈에서 작업을 Codex에 위임하려면 Linear에서 Codex를 사용하세요. 이슈를 Codex에 할당하거나 댓글에서 `@Codex`를 언급하면 Codex가 클라우드 태스크를 만들고 진행 상황과 결과를 답글로 알려줍니다.

Linear에서 Codex는 유료 플랜에서 사용할 수 있습니다([Pricing](https://developers.openai.com/codex/pricing) 참고).

Enterprise 플랜을 사용 중이라면 ChatGPT 워크스페이스 관리자에게 [워크스페이스 설정](https://chatgpt.com/admin/settings)에서 Codex 클라우드 태스크를 활성화하고 [커넥터 설정](https://chatgpt.com/admin/ca)에서 **Codex for Linear**를 켜도록 요청하세요.

## Linear 통합 설정

1. [Codex 클라우드 태스크](https://developers.openai.com/codex/cloud)를 설정하려면 [Codex](https://chatgpt.com/codex)에서 GitHub을 연결하고 Codex가 작업할 리포지토리용 [환경](https://developers.openai.com/codex/cloud/environments)을 만드세요.
2. [Codex 설정](https://chatgpt.com/codex/settings/connectors)으로 이동해 워크스페이스에 **Codex for Linear**를 설치하세요.
3. Linear 이슈의 댓글 스레드에 `@Codex`를 언급해 Linear 계정을 연결하세요.

## Codex에 작업 위임하기

다음 두 가지 방식으로 작업을 위임할 수 있습니다:

### 이슈를 Codex에 할당하기

통합을 설치한 후에는 이슈를 팀원에게 할당하는 것처럼 Codex에 할당할 수 있습니다. Codex가 작업을 시작하고 이슈에 업데이트를 게시합니다.

  <img src="https://developers.openai.com/images/codex/integrations/linear-assign-codex-light.webp"
    alt="Linear 이슈에 Codex 할당하기(라이트 모드)"
    class="block h-auto w-full rounded-lg border border-default my-0 dark:hidden"
  />
  <img src="https://developers.openai.com/images/codex/integrations/linear-assign-codex-dark.webp"
    alt="Linear 이슈에 Codex 할당하기(다크 모드)"
    class="hidden h-auto w-full rounded-lg border border-default my-0 dark:block"
  />

### 댓글에서 `@Codex` 언급하기

댓글 스레드에서 `@Codex`를 언급해 작업을 위임하거나 질문하세요. Codex가 답변한 후에는 그 스레드에서 계속 같은 세션을 이어가며 후속 조치를 취할 수 있습니다.

  <img src="https://developers.openai.com/images/codex/integrations/linear-comment-light.webp"
    alt="Linear 이슈 댓글에서 Codex 언급하기(라이트 모드)"
    class="block h-auto w-full rounded-lg border border-default my-0 dark:hidden"
  />
  <img src="https://developers.openai.com/images/codex/integrations/linear-comment-dark.webp"
    alt="Linear 이슈 댓글에서 Codex 언급하기(다크 모드)"
    class="hidden h-auto w-full rounded-lg border border-default my-0 dark:block"
  />

Codex가 이슈 작업을 시작하면 작업할 환경과 리포지토리를 [환경과 리포지토리를 선택하는 방법](#how-codex-chooses-an-environment-and-repo)에서 결정합니다.
특정 리포지토리를 고정하려면 댓글에 리포지토리를 명시하세요. 예: `@Codex fix this in openai/codex`.

진행 상황을 추적하려면:

- 이슈에서 **Activity**를 열어 진행 업데이트를 확인하세요.
- 작업 링크를 열어 더 자세히 따라가세요.

작업이 완료되면 Codex가 요약과 완료된 작업 링크를 게시해 PR을 만들 수 있도록 도와줍니다.

### Codex가 환경과 리포지토리를 선택하는 방법

- Linear는 이슈 컨텍스트를 토대로 리포지토리를 제안합니다. Codex는 그 제안에 가장 잘 맞는 환경을 선택합니다. 요청이 모호하면 가장 최근에 사용한 환경으로 되돌아갑니다.
- 작업은 해당 환경의 리포지토리 맵에 나열된 첫 번째 리포지토리의 기본 브랜치에서 실행됩니다. 다른 기본 브랜치나 추가 리포지토리가 필요하면 Codex에서 리포지토리 맵을 업데이트하세요.
- 적절한 환경이나 리포지토리를 찾지 못하면 Codex가 Linear에서 문제를 수정하는 방법을 안내한 다음 다시 시도합니다.

## 이슈를 Codex에 자동 할당

다음과 같은 트리아지 규칙으로 이슈를 자동으로 Codex에 할당할 수 있습니다:

1. Linear에서 **Settings**로 이동합니다.
2. **Your teams** 아래에서 팀을 선택합니다.
3. 워크플로 설정에서 **Triage**를 열고 켭니다.
4. **Triage rules**에서 규칙을 만들고 **Delegate** > **Codex**(및 필요한 다른 속성)를 선택합니다.

Linear는 트리아지로 들어오는 새 이슈를 자동으로 Codex에 할당합니다.
트리아지 규칙을 사용하면 Codex는 이슈 작성자의 계정으로 태스크를 실행합니다.

  <img src="https://developers.openai.com/images/codex/integrations/linear-triage-rule-light.webp"
    alt='모든 항목을 Codex에 할당하고 "Triage" 상태로 라벨링한 트리아지 규칙 예시(라이트 모드)'
    class="block h-auto w-full rounded-lg border border-default my-0 dark:hidden"
  />
  <img src="https://developers.openai.com/images/codex/integrations/linear-triage-rule-dark.webp"
    alt='모든 항목을 Codex에 할당하고 "Triage" 상태로 라벨링한 트리아지 규칙 예시(다크 모드)'
    class="hidden h-auto w-full rounded-lg border border-default my-0 dark:block"
  />

## 데이터 사용, 개인정보 보호, 보안

`@Codex`를 언급하거나 이슈를 할당하면 Codex가 요청을 이해하고 태스크를 생성하기 위해 이슈 내용을 받습니다.
데이터 처리는 OpenAI의 [Privacy Policy](https://openai.com/privacy), [Terms of Use](https://openai.com/terms/), 기타 적용 가능한 [정책](https://openai.com/policies)을 따릅니다.
보안에 대해 더 알려면 [Codex 보안 문서](https://developers.openai.com/codex/security)를 확인하세요.

Codex는 실수를 할 수 있는 대형 언어 모델을 사용합니다. 항상 답변과 diff를 검토하세요.

## 팁과 문제 해결

- **연결 누락**: Codex가 Linear 연결을 확인하지 못하면 이슈에 연결 링크와 함께 답글을 남깁니다.
- **예상치 못한 환경 선택**: 원하는 환경을 스레드에 답글로 알려주세요(예: `@Codex please run this in openai/codex`).
- **코드의 잘못된 부분**: 이슈에 더 많은 컨텍스트를 추가하거나 `@Codex` 댓글에서 명시적인 지시를 주세요.
- **추가 도움**: [OpenAI Help Center](https://help.openai.com/)를 참고하세요.

## 로컬 태스크용으로 Linear 연결하기 (MCP)

Codex 앱, CLI 또는 IDE 확장 기능을 사용 중이며 Codex가 로컬에서 Linear 이슈에 접근하기를 원한다면 Linear Model Context Protocol(MCP) 서버를 사용하도록 Codex를 구성하세요.

자세한 내용은 [Linear MCP 문서](https://linear.app/integrations/codex-mcp)를 확인하세요.

IDE 확장 기능을 쓰든 CLI를 쓰든 설정은 동일하며 구성도 공유됩니다.

### CLI 사용(권장)

CLI가 설치되어 있다면 다음을 실행하세요:

```bash
codex mcp add linear --url https://mcp.linear.app/mcp
```

이 명령은 Linear 계정으로 로그인하고 Codex와 연결하도록 안내합니다.

### 수동 구성

1. `~/.codex/config.toml`을 에디터로 엽니다.
2. 다음을 추가합니다:

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"
```

3. `codex mcp login linear`을 실행해 로그인합니다.
