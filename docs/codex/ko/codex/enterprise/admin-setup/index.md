# 관리자 설정

Source URL: https://developers.openai.com/codex/enterprise/admin-setup

이 가이드는 워크스페이스에서 Codex를 설정하려는 ChatGPT Enterprise 관리자용입니다.

## 엔터프라이즈급 보안 및 프라이버시

Codex는 다음을 포함한 ChatGPT Enterprise 보안 기능을 지원합니다.

  * 엔터프라이즈 데이터로 학습하지 않음
  * CLI 및 IDE에 대한 데이터 미보존
  * 데이터 상주 및 보존은 ChatGPT Enterprise 정책 준수
  * 세분화된 사용자 액세스 제어
  * 저장 중(AES 256) 및 전송 중(TLS 1.2+) 데이터 암호화



자세한 내용은 [Security](https://developers.openai.com/codex/security)를 참조하세요.

## 로컬 vs. 클라우드 설정

Codex는 로컬과 클라우드 두 가지 환경에서 동작합니다.

  1. 로컬 사용에는 Codex 앱, CLI, IDE 확장이 포함됩니다. 에이전트는 개발자의 컴퓨터 샌드박스에서 실행됩니다.
  2. 클라우드 사용에는 Codex cloud, iOS, Code Review, [Slack integration](https://developers.openai.com/codex/integrations/slack)으로 생성된 작업이 포함됩니다. 에이전트는 코드베이스가 포함된 호스팅 컨테이너에서 원격으로 실행됩니다.



로컬 및 클라우드 기능에 대한 액세스를 제어하려면 별도의 권한과 RBAC(Role-Based Access Control)를 사용하세요. 모든 사용자 또는 특정 그룹에 대해 로컬, 클라우드, 혹은 둘 다를 활성화할 수 있습니다.

## Codex 로컬 설정

### 워크스페이스 설정에서 Codex 앱, CLI, IDE 확장 활성화

워크스페이스 구성원에게 로컬 Codex를 활성화하려면 [Workspace Settings > Settings and Permissions](https://chatgpt.com/admin/settings)로 이동한 뒤 **Allow members to use Codex Local**을 켭니다. 이 설정은 GitHub 커넥터가 필요하지 않습니다.

이를 켠 후 사용자는 ChatGPT 계정으로 Codex 앱, CLI, IDE 확정을 사용하기 위해 로그인할 수 있습니다. 이 설정을 끄면 Codex 앱, CLI, IDE를 사용하려는 사용자는 “403 - Unauthorized. Contact your ChatGPT administrator for access.” 오류를 보게 됩니다.

## Team Config

조직 전체에서 Codex를 표준화하려는 팀은 Team Config를 사용해 기본값, 규칙, 스킬을 공유함으로써 각 로컬 구성을 중복 설정하지 않아도 됩니다.

Type| Path| Use it to  
---|---|---  
[Config basics](https://developers.openai.com/codex/config-basic)| `config.toml`| 샌드박스 모드, 승인, 모델, reasoning effort 등 기본값을 설정합니다.  
[Rules](https://developers.openai.com/codex/rules)| `rules/`| Codex가 샌드박스 밖에서 실행할 수 있는 명령을 제어합니다.  
[Skills](https://developers.openai.com/codex/skills)| `skills/`| 팀에서 공유할 스킬을 제공합니다.  
  
위치와 우선순위는 [Config basics](https://developers.openai.com/codex/config-basic#configuration-precedence)를 참조하세요.

## Codex 클라우드 설정

### 사전 요구 사항

Codex cloud에는 **GitHub(클라우드 호스팅) 리포지토리**가 필요합니다. 코드베이스가 온프레미스이거나 GitHub에 없다면 Codex SDK를 사용해 자체 인프라에 유사한 워크플로를 구축할 수 있습니다.

관리자로 Codex를 설정하려면 조직 전반에서 일반적으로 사용하는 리포지토리에 대한 GitHub 액세스 권한이 있어야 합니다. 필요한 액세스 권한이 없다면 권한이 있는 엔지니어링 팀 구성원과 협업하세요.

### 워크스페이스 설정에서 Codex 클라우드 활성화

[Workspace Settings > Settings and Permissions](https://chatgpt.com/admin/settings)의 Codex 섹션에서 ChatGPT GitHub Connector를 켜는 것부터 시작하세요.

워크스페이스에서 Codex cloud를 사용하려면 **Allow members to use Codex cloud**를 켭니다.

활성화되면 사용자는 ChatGPT 왼쪽 탐색 패널에서 Codex에 바로 접근할 수 있습니다.

Enterprise 워크스페이스 설정에서 Codex를 켠 뒤 ChatGPT에 Codex가 나타나기까지 최대 10분이 걸릴 수 있습니다.

### GitHub Connector IP 허용 목록 구성

ChatGPT GitHub 커넥터에 연결할 수 있는 IP 주소를 제어하려면 다음 IP 범위를 구성하세요.

  * [ChatGPT egress IP ranges](https://openai.com/chatgpt-actions.json)
  * [Codex container egress IP ranges](https://openai.com/chatgpt-agents.json)



이 IP 범위는 변경될 수 있습니다. 최신 값에 따라 허용 목록을 자동으로 확인하고 업데이트하는 방안을 고려하세요.

### 구성원이 Codex를 관리하도록 허용

이 토글을 켜면 사용자가 Codex 워크스페이스 분석 정보를 보고 환경을 관리(편집 및 삭제)할 수 있습니다.

Codex는 역할 기반 액세스(자세한 내용은 [Role-based access (RBAC)](https://developers.openai.com/codex/enterprise/admin-setup#role-based-access-rbac) 참조)를 지원하므로 특정 사용자 하위 집합에 대해 이 토글을 켤 수 있습니다.

### 작업 완료 시 Codex Slack 앱이 답변을 게시하도록 허용

Codex는 Slack과 통합되어 있습니다. 사용자가 Slack에서 `@Codex`를 멘션하면 Codex가 클라우드 작업을 시작하고 Slack 스레드에서 컨텍스트를 가져온 다음 해당 스레드에 검토할 PR 링크와 함께 응답합니다.

작업 완료 시 Slack 앱이 답변을 게시하도록 허용하려면 **Allow Codex Slack app to post answers on task completion**을 켭니다. 활성화되면 Codex는 작업이 완료될 때 전체 답변을 Slack에 다시 게시하며, 비활성화된 경우 작업 링크만 게시합니다.

자세한 내용은 [Codex in Slack](https://developers.openai.com/codex/integrations/slack)을 참조하세요.

### Codex 에이전트의 인터넷 액세스 활성화

기본적으로 Codex 클라우드 에이전트는 런타임 중 보안 및 안전 위험(예: 프롬프트 인젝션)으로부터 보호하기 위해 인터넷에 접근할 수 없습니다.

관리자는 사용자가 자신의 환경에서 에이전트 인터넷 액세스를 활성화하도록 허용할 수 있습니다. 이를 위해 **Allow Codex agent to access the internet**을 켜세요.

이 설정이 켜져 있으면 사용자는 일반적인 소프트웨어 종속성 도메인에 대한 허용 목록을 사용하고, 도메인과 신뢰할 수 있는 사이트를 추가하며, 허용되는 HTTP 메서드를 지정할 수 있습니다.

### Codex 클라우드를 통한 코드 리뷰 활성화

Codex가 코드 리뷰를 수행하도록 허용하려면 [Settings → Code review](https://chatgpt.com/codex/settings/code-review)로 이동하세요.

사용자는 Codex가 자신의 풀 리퀘스트를 검토할지 여부를 지정할 수 있으며, 코드 리뷰를 리포지토리의 모든 기여자에게 실행할지 여부도 구성할 수 있습니다.

Codex는 두 가지 유형의 코드 리뷰를 지원합니다:

  1. 사용자가 리뷰용 PR을 열 때 자동으로 트리거되는 코드 리뷰.
  2. 사용자가 문제를 살펴보도록 @Codex를 멘션할 때 수행되는 반응형 코드 리뷰. 예: “@Codex fix this CI error” 또는 “@Codex address that feedback.”

## Role-based access (RBAC)

Codex는 역할 기반 액세스를 지원합니다. RBAC는 사용자 역할 할당에 따라 시스템이나 리소스에 대한 액세스를 제어하는 데 사용하는 보안 및 권한 모델입니다.

Codex에서 RBAC를 활성화하려면 [ChatGPT 관리 페이지](https://chatgpt.com/admin/settings)의 Settings & Permissions → Custom Roles로 이동해 그룹 탭에서 만든 그룹에 역할을 할당하세요.

이를 통해 Codex 권한 관리를 단순화하고 ChatGPT 워크스페이스의 보안을 강화할 수 있습니다. 자세한 내용은 [도움말 센터 문서](https://help.openai.com/en/articles/11750701-rbac)를 참조하세요.

## 첫 번째 Codex 클라우드 환경 설정

  1. Codex 클라우드로 이동하여 **Get started**를 선택합니다.
  2. GitHub를 아직 ChatGPT에 연결하지 않았다면 ChatGPT GitHub Connector를 설치하기 위해 **Connect to GitHub**을 선택합니다. 
     * 계정에 대해 ChatGPT Connector를 허용합니다.
     * ChatGPT Connector의 설치 대상을 선택합니다(일반적으로 기본 조직).
     * Codex에 연결하려는 리포지토리를 허용합니다(GitHub 관리자 승인이 필요할 수 있음).
  3. 개발자와 가장 관련성이 높은 리포지토리를 선택해 첫 번째 환경을 만들고 **Create environment**를 선택합니다. 
     * 편집 권한을 부여하려면 환경 협력자의 이메일 주소를 추가합니다.
  4. 테스트 작성, 버그 수정, 코드 탐색과 같은 시작 작업을 몇 가지 실행합니다.

이제 첫 번째 환경을 만들었습니다. GitHub에 연결된 사용자는 이 환경을 사용해 작업을 생성할 수 있으며, 리포지토리에 액세스할 수 있는 사용자는 작업에서 생성된 풀 리퀘스트를 푸시할 수도 있습니다.

### 환경 관리

ChatGPT 워크스페이스 관리자는 워크스페이스에서 Codex 환경을 편집하거나 삭제할 수 있습니다.

### Codex 클라우드에 더 많은 GitHub 리포지토리 연결

  1. **Environments**를 선택하거나 환경 선택기를 열고 **Manage Environments**를 선택합니다.
  2. **Create Environment**를 선택합니다.

3. 연결하려는 저장소를 선택합니다.
  4. 이름과 설명을 입력합니다.
  5. 환경 공개 범위를 선택합니다.
  6. **Create Environment**를 선택합니다.



Codex는 코드베이스를 검토하여 환경 설정을 자동으로 최적화합니다. 특정 성능 문제가 나타날 때까지 고급 환경 구성을 피하세요. 자세한 내용은 [Codex cloud](https://developers.openai.com/codex/cloud)를 확인하세요.

### 사용자와 설정 지침 공유

다음 단계를 최종 사용자에게 공유할 수 있습니다.

  1. ChatGPT 왼쪽 패널에서 [Codex](https://chatgpt.com/codex)로 이동합니다.
  2. 아직 연결되어 있지 않다면 프롬프트 작성기에서 **Connect to GitHub**을 선택합니다. 
     * GitHub에 로그인합니다.
  3. 이제 워크스페이스에서 공유 환경을 사용하거나 자신의 환경을 만들 수 있습니다.
  4. Ask 모드와 Code 모드에서 각각 작업을 시도해 보세요. 예: 
     * Ask: 이 코드베이스에서 버그를 찾아줘.
     * Write code: 기존 테스트 패턴을 따르면서 테스트 커버리지를 개선해줘.



## Codex 사용량 추적

  * 레이트 리밋이 있는 워크스페이스는 [Settings → Usage](https://chatgpt.com/codex/settings/usage)에서 Codex 워크스페이스 지표를 확인하세요.
  * 엔터프라이즈 거버넌스에 대한 자세한 내용은 [Governance](https://developers.openai.com/codex/enterprise/governance) 페이지를 참조하세요.
  * 유연한 가격의 엔터프라이즈 워크스페이스는 ChatGPT 워크스페이스 결제 콘솔에서 크레딧 사용량을 확인할 수 있습니다.



## 제로 데이터 보존(ZDR)

Codex는 [Zero Data Retention (ZDR)](https://platform.openai.com/docs/guides/your-data#zero-data-retention)이 활성화된 OpenAI 조직을 지원합니다.
