---
title: 'Slack에서 Codex 사용하기'
description: 'Slack에서 Codex를 사용해 채널과 스레드에서 코딩 작업을 시작하세요. 프롬프트와 함께 를 언급하면 Codex가 클라우드 작업을 생성하고 결과를 응답합니다.'
---

Source URL: https://developers.openai.com/codex/integrations/slack

# Slack에서 Codex 사용하기

Slack에서 Codex를 사용해 채널과 스레드에서 코딩 작업을 시작하세요. 프롬프트와 함께 `@Codex`를 언급하면 Codex가 클라우드 작업을 생성하고 결과를 응답합니다.

  <img src="https://developers.openai.com/images/codex/integrations/slack-example.png"
    alt="Codex Slack integration in action"
    class="block h-auto w-full mx-0!"
  />

## Slack 앱 설정

1. [Codex 클라우드 작업](https://developers.openai.com/codex/cloud)을 설정하세요. Plus, Pro, Business, Enterprise 또는 Edu 플랜이 필요하고 ([ChatGPT 가격](https://chatgpt.com/pricing) 참조) 연결된 GitHub 계정과 최소 하나의 [환경](https://developers.openai.com/codex/cloud/environments)이 있어야 합니다.
2. [Codex 설정](https://chatgpt.com/codex/settings/connectors)으로 이동하여 작업공간에 Slack 앱을 설치하세요. Slack 작업공간 정책에 따라 관리자 승인이 필요할 수 있습니다.
3. 채널에 `@Codex`를 추가하세요. 아직 추가하지 않았다면 언급할 때 Slack이 안내해 줍니다.

## 작업 시작

1. 채널이나 스레드에서 `@Codex`를 언급하고 프롬프트를 포함하세요. Codex는 스레드의 이전 메시지를 참고할 수 있으므로, 대개 맥락을 다시 설명할 필요가 없습니다.
2. (선택 사항) 프롬프트에 환경 또는 리포지토리를 지정하세요. 예: `@Codex fix the above in openai/codex`.
3. Codex가 반응(👀)하고 작업 링크로 응답할 때까지 기다리세요. 작업이 완료되면 Codex가 결과를 게시하고, 설정에 따라 스레드에 답변을 덧붙입니다.

### Codex가 환경과 리포지토리를 선택하는 방법

- Codex는 사용 가능한 환경을 검토하고 요청에 가장 잘 맞는 환경을 선택합니다. 요청이 애매모호하면 최근에 사용한 환경으로 돌아갑니다.
- 작업은 해당 환경의 리포 맵에서 첫 번째로 나열된 리포지토리의 기본 브랜치에서 실행됩니다. 다른 기본값이나 더 많은 리포지토리가 필요하면 Codex에서 리포 맵을 업데이트하세요.
- 적절한 환경이나 리포지토리가 없으면 Codex가 Slack에서 문제 해결 방법을 안내한 뒤 다시 시도합니다.

### Enterprise 데이터 제어

기본적으로 Codex는 완료된 작업에 대한 답변을 스레드에 게시합니다. 이 답변에는 실행된 환경에서 가져온 정보가 포함될 수 있습니다. 이를 방지하려면 Enterprise 관리자가 [ChatGPT 작업공간 설정](https://chatgpt.com/admin/settings)에서 **작업 완료 시 Codex Slack 앱이 답변을 게시하도록 허용**을 해제할 수 있습니다. 관리자가 답변을 끄면 Codex는 작업 링크만 응답합니다.

### 데이터 사용, 개인정보 및 보안

`@Codex`를 언급하면 Codex가 요청을 이해하고 작업을 생성하기 위해 메시지와 스레드 기록을 받습니다. 데이터 처리는 OpenAI의 [개인정보 처리방침](https://openai.com/privacy), [이용약관](https://openai.com/terms/), 기타 해당 [정책들](https://openai.com/policies)을 따릅니다. 보안에 대한 자세한 내용은 Codex [보안 문서](https://developers.openai.com/codex/security)를 참조하세요.

Codex는 실수를 할 수 있는 대형 언어 모델을 사용합니다. 답변과 diff는 항상 검토하세요.

### 팁 및 문제 해결

- **연결 누락**: Codex가 Slack 또는 GitHub 연결을 확인할 수 없으면 다시 연결할 수 있는 링크와 함께 응답합니다.
- **예상치 못한 환경 선택**: 원하는 환경을 스레드에 회신하세요(예: `Please run this in openai/openai (applied)`)한 뒤 `@Codex`를 다시 언급하세요.
- **긴 스레드나 복잡한 스레드**: Codex가 앞쪽에 묻혀 있는 맥락을 놓치지 않도록 최신 메시지에 핵심 내용을 요약하세요.
- **워크스페이스 게시 제한**: 일부 Enterprise 워크스페이스는 최종 답변 게시를 제한합니다. 이런 경우 작업 링크를 열어 진행 상황과 결과를 확인하세요.
- **추가 도움말**: [OpenAI 도움말 센터](https://help.openai.com/)를 참조하세요.
