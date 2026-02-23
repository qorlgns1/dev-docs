---
title: Slack에서 Codex 사용하기
description: Slack 채널과 스레드에서 코딩 작업을 시작하려면 Codex를 사용하세요. 를 멘션하고 프롬프트를 입력하면 Codex가 클라우드 작업을 생성하고 결과로 응답합니다.
---

# Slack에서 Codex 사용하기

Source URL: https://developers.openai.com/codex/integrations/slack

Slack 채널과 스레드에서 코딩 작업을 시작하려면 Codex를 사용하세요. `@Codex`를 멘션하고 프롬프트를 입력하면 Codex가 클라우드 작업을 생성하고 결과로 응답합니다.

## Slack 앱 설정

1. [Codex 클라우드 작업](https://developers.openai.com/codex/cloud)을 설정하세요. Plus, Pro, Business, Enterprise, 또는 Edu 플랜(참조: [ChatGPT 가격](https://chatgpt.com/pricing)), 연결된 GitHub 계정, 최소 한 개의 [environment](https://developers.openai.com/codex/cloud/environments)가 필요합니다.
2. [Codex 설정](https://chatgpt.com/codex/settings/connectors)으로 이동해 워크스페이스용 Slack 앱을 설치하세요. 워크스페이스 정책에 따라 설치 승인이 필요할 수 있습니다.
3. `@Codex`를 채널에 추가하세요. 아직 추가하지 않았다면 멘션 시 Slack이 안내합니다.

## 작업 시작하기

1. 채널이나 스레드에서 `@Codex`를 멘션하고 프롬프트를 포함하세요. Codex는 스레드의 이전 메시지를 참조할 수 있으므로 문맥을 반복할 필요가 없습니다.
2. (선택 사항) 프롬프트에 environment나 저장소를 지정할 수 있습니다. 예: `@Codex fix the above in openai/codex`.
3. Codex가 반응(👀)하고 작업 링크로 답할 때까지 기다리세요. 작업이 끝나면 Codex가 결과와 설정에 따라 스레드에 답변을 게시합니다.

### Codex가 environment와 repo를 선택하는 방법

* Codex는 접근 가능한 environment를 검토하고 요청과 가장 잘 맞는 항목을 선택합니다. 요청이 모호하면 최근에 사용한 environment로 되돌아갑니다.
* 작업은 해당 environment의 repo 맵에 첫 번째로 나열된 저장소의 기본 브랜치에서 실행됩니다. 다른 기본값이나 추가 저장소가 필요하면 Codex에서 repo 맵을 업데이트하세요.
* 사용 가능한 적절한 environment나 저장소가 없으면 Codex는 Slack에서 문제를 해결하는 방법을 안내한 뒤 다시 시도하도록 요청합니다.

### Enterprise 데이터 제어

기본적으로 Codex는 실행한 environment의 정보를 포함할 수 있는 답변을 스레드에 게시합니다. 이를 방지하려면 Enterprise 관리자가 [ChatGPT 워크스페이스 설정](https://chatgpt.com/admin/settings)에서 **Allow Codex Slack app to post answers on task completion**을 해제하세요. 답변을 끄면 Codex는 작업 링크만 공유합니다.

### 데이터 사용, 프라이버시, 보안

`@Codex`를 멘션하면 Codex는 요청을 파악하고 작업을 만들기 위해 메시지와 스레드 기록을 받습니다. 데이터 처리는 OpenAI의 [개인정보 처리방침](https://openai.com/privacy), [이용약관](https://openai.com/terms/), 기타 적용 가능한 [정책](https://openai.com/policies)을 따릅니다. 보안에 대한 자세한 내용은 Codex [보안 문서](https://developers.openai.com/codex/security)를 참조하세요.

Codex는 실수를 저지를 수 있는 대규모 언어 모델을 사용합니다. 항상 답변과 diff를 검토하세요.

### 팁 및 문제 해결

* **연결 누락**: Codex가 Slack 또는 GitHub 연결을 확인할 수 없으면 재연결 링크를 제공합니다.
* **예상치 못한 environment 선택**: 원하는 environment를 스레드에서 답장으로 명시한 뒤(`Please run this in openai/openai (applied)` 등) 다시 `@Codex`를 멘션하세요.
* **길거나 복잡한 스레드**: Codex가 이전 메시지에 묻힌 문맥을 놓치지 않도록 최신 메시지에 핵심 내용을 요약하세요.
* **워크스페이스 게시 제한**: 일부 Enterprise 워크스페이스는 최종 답변 게시를 제한합니다. 이 경우 작업 링크를 열어 진행 상황과 결과를 확인하세요.
* **추가 도움말**: [OpenAI 도움말 센터](https://help.openai.com/)를 참고하세요.
