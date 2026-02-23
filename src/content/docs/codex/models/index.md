---
title: Codex 모델
description: "출처 URL: https://developers.openai.com/codex/models"
sidebar:
  order: 9
---

# Codex 모델

출처 URL: https://developers.openai.com/codex/models

## 추천 모델

gpt-5.3-codex

프런티어급 코딩 성능에 강화된 추론과 전문 지식을 결합한, 지금까지 가장 강력한 에이전틱 코딩 모델입니다.

codex -m gpt-5.3-codex

명령 복사

기능

속도

Codex CLI 및 SDK

Codex 앱 및 IDE 확장

Codex Cloud

ChatGPT 크레딧

API 액세스

gpt-5.3-codex-spark

거의 즉각적인 실시간 코딩 반복을 위해 최적화된 텍스트 전용 리서치 프리뷰 모델입니다. ChatGPT Pro 사용자에게 제공됩니다.

codex -m gpt-5.3-codex-spark

명령 복사

기능

속도

Codex CLI 및 SDK

Codex 앱 및 IDE 확장

Codex Cloud

ChatGPT 크레딧

API 액세스

gpt-5.2-codex

실제 엔지니어링을 위한 고급 코딩 모델입니다. GPT-5.3-Codex가 후속 모델입니다.

codex -m gpt-5.2-codex

명령 복사

기능

속도

Codex CLI 및 SDK

Codex 앱 및 IDE 확장

Codex Cloud

ChatGPT 크레딧

API 액세스

대부분의 Codex 코딩 작업은 gpt-5.3-codex로 시작하세요. Codex 앱, CLI, IDE 확장, Codex Cloud에서 ChatGPT 인증 Codex 세션으로 사용할 수 있습니다. GPT-5.3-Codex용 API 액세스는 곧 제공될 예정입니다. gpt-5.3-codex-spark 모델은 ChatGPT Pro 가입자를 위한 리서치 프리뷰로 제공됩니다.

## 대체 모델

gpt-5.2

산업과 도메인을 아우르는 작업을 위한 최고의 범용 에이전틱 모델입니다.

codex -m gpt-5.2

명령 복사

자세히 보기

gpt-5.1-codex-max

Codex에서 장기적 에이전틱 코딩 작업에 최적화되었습니다.

codex -m gpt-5.1-codex-max

명령 복사

자세히 보기

gpt-5.1

도메인 전반의 코딩과 에이전틱 작업에 적합합니다. GPT-5.2가 후속 모델입니다.

codex -m gpt-5.1

명령 복사

자세히 보기

gpt-5.1-codex

Codex에서 장시간 실행되는 에이전틱 코딩 작업에 최적화되었습니다. GPT-5.1-Codex-Max가 후속 모델입니다.

codex -m gpt-5.1-codex

명령 복사

자세히 보기

gpt-5-codex

장시간 실행되는 에이전틱 코딩 작업을 위해 조정된 GPT-5 버전입니다. GPT-5.1-Codex가 후속 모델입니다.

codex -m gpt-5-codex

명령 복사

자세히 보기

gpt-5-codex-mini

GPT-5-Codex의 더 작고 비용 효율적인 버전입니다. GPT-5.1-Codex-Mini가 후속 모델입니다.

codex -m gpt-5-codex

명령 복사

자세히 보기

gpt-5

도메인 전반의 코딩과 에이전틱 작업을 위한 추론 모델입니다. GPT-5.1이 후속 모델입니다.

codex -m gpt-5

명령 복사

자세히 보기

## 기타 모델

Codex는 위에 나열된 모델과 함께 사용할 때 가장 뛰어난 성능을 발휘합니다.

또한 특정 사용 사례에 맞게 [Chat Completions](https://platform.openai.com/docs/api-reference/chat) 또는 [Responses API](https://platform.openai.com/docs/api-reference/responses)를 지원하는 어떤 모델과 제공자든 Codex에 연결할 수 있습니다.

Chat Completions API 지원은 사용 중단 예정이며 앞으로의 Codex 릴리스에서 제거됩니다.

## 모델 구성

### 기본 로컬 모델 구성

Codex CLI와 IDE 확장은 동일한 `config.toml` [구성 파일](https://developers.openai.com/codex/config-basic)을 사용합니다. 모델을 지정하려면 구성 파일에 `model` 항목을 추가하세요. 모델을 지정하지 않으면 Codex 앱, CLI, IDE 확장은 권장 모델을 기본값으로 사용합니다.
```
    model = "gpt-5.2"
```

### 일시적으로 다른 로컬 모델 선택

Codex CLI에서는 활성 스레드 동안 `/model` 명령을 사용해 모델을 변경할 수 있습니다. IDE 확장에서는 입력 상자 아래 모델 선택기를 사용해 모델을 고를 수 있습니다.

특정 모델로 새 Codex CLI 스레드를 시작하거나 `codex exec`에 사용할 모델을 지정하려면 `--model`/`-m` 플래그를 사용하세요:
```
    codex -m gpt-5.3-codex
```

### 클라우드 작업용 모델 선택

현재는 Codex 클라우드 작업의 기본 모델을 변경할 수 없습니다.