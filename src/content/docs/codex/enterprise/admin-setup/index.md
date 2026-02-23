---
title: '관리자 설정'
description: '이 가이드는 워크스페이스에서 Codex를 설정하려는 ChatGPT Enterprise 관리자용입니다.'
---

Source URL: https://developers.openai.com/codex/enterprise/admin-setup

# 관리자 설정

이 가이드는 워크스페이스에서 Codex를 설정하려는 ChatGPT Enterprise 관리자용입니다.

## 엔터프라이즈급 보안 및 개인정보 보호

Codex는 다음을 포함한 ChatGPT Enterprise 보안 기능을 지원합니다.

- 엔터프라이즈 데이터에 대한 학습 없음
- CLI 및 IDE에서의 데이터 보관 없음
- 거주지 및 보관은 ChatGPT Enterprise 정책 준수
- 세분화된 사용자 접근 제어
- 저장 시(AES 256) 및 전송 시(TLS 1.2+) 데이터 암호화

자세한 내용은 [Security](https://developers.openai.com/codex/security)를 참조하세요.

## 로컬 vs. 클라우드 설정

Codex는 로컬 환경과 클라우드 환경의 두 가지 방식에서 작동합니다.

1. 로컬 사용에는 Codex 앱, CLI, IDE 확장이 포함됩니다. 에이전트는 개발자의 컴퓨터 샌드박스에서 실행됩니다.
2. 클라우드 사용에는 Codex cloud, iOS, Code Review, [Slack 통합](https://developers.openai.com/codex/integrations/slack)을 통해 생성된 작업이 포함됩니다. 에이전트는 코드베이스가 호스팅된 컨테이너에서 원격으로 실행됩니다.

로컬 기능과 클라우드 기능에 대한 접근을 제어하려면 별도의 권한과 RBAC(역할 기반 접근 제어)를 사용하세요. 모든 사용자 또는 특정 그룹에 대해 로컬, 클라우드 또는 둘 다를 활성화할 수 있습니다.

## Codex 로컬 설정

### 워크스페이스 설정에서 Codex 앱, CLI, IDE 확장 활성화

워크스페이스 구성원이 로컬에서 Codex를 사용하려면 [Workspace Settings > Settings and Permissions](https://chatgpt.com/admin/settings)로 이동해 **Allow members to use Codex Local**을 켭니다. 이 설정은 GitHub 커넥터를 필요로 하지 않습니다.

이 설정을 켜면 사용자는 ChatGPT 계정으로 Codex 앱, CLI, IDE 확장에 로그인할 수 있습니다. 이 설정을 끄면 Codex 앱, CLI 또는 IDE를 사용하려는 사용자는 다음 오류를 보게 됩니다: "403 - Unauthorized. Contact your ChatGPT administrator for access."

## 팀 구성

조직 내에서 Codex를 표준화하려는 팀은 Team Config를 사용하여 각 로컬 구성에 중복 없이 기본값, 규칙, 스킬을 공유할 수 있습니다.

| Type                                 | Path          | Use it to                                                                    |
| ------------------------------------ | ------------- | ---------------------------------------------------------------------------- |
| [Config basics](https://developers.openai.com/codex/config-basic) | `config.toml` | 샌드박스 모드, 승인, 모델, 추론 노력 등 기본값 설정.                            |
| [Rules](https://developers.openai.com/codex/rules)                | `rules/`      | 샌드박스를 벗어난 Codex 실행 명령 제어.                                       |
| [Skills](https://developers.openai.com/codex/skills)              | `skills/`     | 팀에서 공유 스킬을 사용할 수 있게 함.                                         |

위치 및 우선순위는 [Config basics](https://developers.openai.com/codex/config-basic#configuration-precedence)를 참고하세요.

## Codex 클라우드 설정

### 사전 조건

Codex cloud는 **GitHub(클라우드 호스팅) 리포지토리**를 필요로 합니다. 코드베이스가 온프레미스이거나 GitHub에 없으면 Codex SDK를 사용해 자체 인프라에서 유사한 워크플로를 구축할 수 있습니다.

관리자로 Codex를 설정하려면 조직 전체에서 일반적으로 사용하는 리포지토리에 대한 GitHub 접근 권한이 있어야 합니다. 필요한 권한이 없다면 해당 권한을 가진 엔지니어링 팀의 누군가와 협업하세요.

### 워크스페이스 설정에서 Codex 클라우드 활성화

처음에는 [Workspace Settings > Settings and Permissions](https://chatgpt.com/admin/settings)의 Codex 섹션에서 ChatGPT GitHub Connector를 켜세요.

워크스페이스에서 Codex cloud를 사용하려면 **Allow members to use Codex cloud**를 켭니다.

활성화되면 사용자는 ChatGPT 왼쪽 탐색 패널에서 Codex에 직접 접근할 수 있습니다.

  <img src="https://developers.openai.com/images/codex/enterprise/cloud-toggle-config.png"
    alt="Codex cloud toggle"
    class="block w-full mx-auto rounded-lg"
  />

Enterprise 워크스페이스 설정에서 Codex를 켠 후 최대 10분까지 Codex가 ChatGPT에 표시되지 않을 수 있습니다.

### GitHub 커넥터 IP 허용 목록 구성

ChatGPT GitHub 커넥터에 연결할 수 있는 IP 주소를 관리하려면 다음 IP 대역을 구성하세요.

- [ChatGPT egress IP ranges](https://openai.com/chatgpt-actions.json)
- [Codex container egress IP ranges](https://openai.com/chatgpt-agents.json)

이 IP 범위는 변경될 수 있습니다. 자동으로 확인하고 최신 값에 따라 허용 목록을 업데이트하는 방안을 고려하세요.

### Codex 관리 권한 부여

이 토글을 켜면 사용자는 Codex 워크스페이스 분석을 보고 환경을 관리(편집 및 삭제)할 수 있습니다.

Codex는 역할 기반 접근(RBAC)을 지원하므로 ([Role-based access (RBAC)](#role-based-access-rbac) 참조) 특정 사용자 하위 집합에 대해 이 토글을 켤 수 있습니다.

### Codex Slack 앱이 작업 완료 시 응답 게시 허용

Codex는 Slack과 통합됩니다. 사용자가 Slack에서 `@Codex`를 언급하면 Codex가 클라우드 작업을 시작하고 Slack 스레드의 컨텍스트를 가져온 다음 검토할 PR 링크와 함께 응답합니다.

작업 완료 시 Slack에 응답을 게시하려면 **Allow Codex Slack app to post answers on task completion**을 켭니다. 이 설정이 켜져 있으면 작업 완료 시 Codex가 전체 응답을 Slack으로 다시 게시합니다. 그렇지 않으면 작업 링크만 게시됩니다.

자세한 내용은 [Codex in Slack](https://developers.openai.com/codex/integrations/slack)을 참고하세요.

### Codex 에이전트의 인터넷 접근 허용

기본적으로 Codex 클라우드 에이전트는 프롬프트 주입 같은 보안 및 안전 위험을 방지하기 위해 런타임 시 인터넷 접근이 없습니다.

관리자로서 사용자 환경에서 에이전트 인터넷 접근을 허용하도록 설정할 수 있습니다. 이 기능을 허용하려면 **Allow Codex agent to access the internet**을 켭니다.

이 설정을 켜면 사용자는 일반적인 소프트웨어 종속성 도메인에 대한 허용 목록을 사용하고, 더 많은 도메인 및 신뢰할 수 있는 사이트를 추가하며, 허용된 HTTP 메서드를 지정할 수 있습니다.

### Codex 클라우드에서 코드 리뷰 활성화

Codex가 코드 리뷰를 수행하도록 허용하려면 [Settings → Code review](https://chatgpt.com/codex/settings/code-review)로 이동하세요.

사용자는 Codex가 풀 리퀘스트를 검토할지 여부를 지정할 수 있습니다. 사용자는 또한 코드 리뷰가 특정 리포지토리의 모든 기여자에게 실행될지 구성할 수 있습니다.

Codex는 두 가지 유형의 코드 리뷰를 지원합니다.

1. 사용자가 PR을 열면 자동으로 실행되는 코드 리뷰
2. 사용자가 @Codex를 언급하여 이슈를 검토하도록 요청할 때의 반응형 코드 리뷰(예: "@Codex fix this CI error" 또는 "@Codex address that feedback")

## 역할 기반 접근(RBAC)

Codex는 역할 기반 접근을 지원합니다. RBAC는 사용자의 역할 할당에 기반하여 시스템 또는 리소스에 대한 접근을 제어하는 보안 및 권한 모델입니다.

Codex에 RBAC를 활성화하려면 [ChatGPT 관리자 페이지](https://chatgpt.com/admin/settings)의 Settings & Permissions → Custom Roles로 이동하고 Groups 탭에서 만든 그룹에 역할을 할당하세요.

이로써 Codex 권한 관리를 단순화하고 ChatGPT 워크스페이스에서 보안을 강화할 수 있습니다. 자세한 내용은 [Help Center article](https://help.openai.com/en/articles/11750701-rbac)를 참조하세요.

## 첫 Codex 클라우드 환경 설정

1. Codex cloud로 이동하여 **Get started**를 선택합니다.
2. **Connect to GitHub**를 선택하여 아직 ChatGPT에 GitHub을 연결하지 않았다면 ChatGPT GitHub Connector를 설치합니다.
   - ChatGPT Connector를 계정에 허용합니다.
   - 일반적으로 기본 조직과 같은 설치 대상을 선택합니다.
   - Codex에 연결하려는 리포지토리를 허용합니다(이 작업은 GitHub 관리자 승인이 필요할 수 있습니다).
3. 개발자와 가장 관련 있는 리포지토리를 선택하여 첫 번째 환경을 만든 다음 **Create environment**를 선택합니다.
   - 편집 권한을 줄 환경 협업자의 이메일 주소를 추가합니다.
4. 몇 가지 시작 작업(예: 테스트 작성, 버그 수정, 코드 탐색)을 시작합니다.

이제 첫 환경을 만들었습니다. GitHub에 연결한 사용자는 이 환경을 사용해 작업을 만들 수 있으며, 리포지토리에 접근 권한이 있는 사용자는 작업에서 생성된 PR도 푸시할 수 있습니다.

### 환경 관리

ChatGPT 워크스페이스 관리자는 워크스페이스에서 Codex 환경을 편집하고 삭제할 수 있습니다.

### Codex 클라우드와 더 많은 GitHub 리포지토리 연결

1. **Environments**를 선택하거나 환경 선택기를 열고 **Manage Environments**를 선택합니다.
2. **Create Environment**를 선택합니다.
3. 연결하려는 리포지토리를 선택합니다.
4. 이름과 설명을 입력합니다.
5. 환경 공개 범위를 선택합니다.
6. **Create Environment**를 선택합니다.

Codex는 코드베이스를 검토하여 환경 구성을 자동으로 최적화합니다. 특정 성능 문제가 나타날 때까지 고급 환경 구성은 피하세요. 자세한 내용은 [Codex cloud](https://developers.openai.com/codex/cloud)를 참고하세요.

### 사용자와 설정 안내 공유

다음 단계를 최종 사용자와 공유할 수 있습니다.

1. ChatGPT 왼쪽 패널의 [Codex](https://chatgpt.com/codex)로 이동합니다.
2. 프롬프트 작성기에서 **Connect to GitHub**를 선택합니다(이미 연결되지 않은 경우).
   - GitHub에 로그인합니다.
3. 워크스페이스와 공유된 환경을 사용하거나 자체 환경을 만들 수 있습니다.
4. Ask와 Code 모드에서 작업을 시도해 보세요. 예:
   - Ask: 이 코드베이스에서 버그를 찾아주세요.
   - Write code: 기존 테스트 패턴을 따라 테스트 커버리지를 개선하세요.

## Codex 사용량 추적

- 사용량 제한이 있는 워크스페이스의 경우 [Settings → Usage](https://chatgpt.com/codex/settings/usage)에서 Codex 워크스페이스 메트릭을 확인하세요.
- 엔터프라이즈 거버넌스에 대해 더 알고 싶다면 [Governance](https://developers.openai.com/codex/enterprise/governance) 페이지를 참조하세요.
- 유연한 가격 책정이 적용된 엔터프라이즈 워크스페이스는 ChatGPT 워크스페이스 청구 콘솔에서 크레딧 사용량을 확인할 수 있습니다.

## Zero Data Retention (ZDR)

Codex는 [Zero Data Retention (ZDR)](https://platform.openai.com/docs/guides/your-data#zero-data-retention)이 활성화된 OpenAI 조직을 지원합니다.
