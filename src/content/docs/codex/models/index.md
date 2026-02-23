---
title: 'Codex 모델'
description: "description: '최첨단 코딩 성능과 강화된 추론 및 전문 지식 역량을 결합한 지금까지 가장 능력 있는 대리 코딩 모델입니다.'"
---

title: 'Codex 모델'
description: '최첨단 코딩 성능과 강화된 추론 및 전문 지식 역량을 결합한 지금까지 가장 능력 있는 대리 코딩 모델입니다.'

Source URL: https://developers.openai.com/codex/models

# Codex 모델

## 추천 모델

### gpt-5.3-codex
지금까지 가장 능력 있는 대리 코딩 모델로, 최첨단 코딩 성능에 더 강력한 추론력과 전문 지식 역량을 결합했습니다.
- Model ID: `gpt-5.3-codex`

### gpt-5.3-codex-spark
실시간에 가까운 초고속 코딩 반복을 위해 최적화된 텍스트 전용 연구 미리보기 모델입니다. ChatGPT Pro 사용자에게 제공됩니다.
- Model ID: `gpt-5.3-codex-spark`

### gpt-5.2-codex
현실 세계 엔지니어링에 적합한 고급 코딩 모델입니다. GPT-5.3-Codex로 이어졌습니다.
- Model ID: `gpt-5.2-codex`

Codex에서 대부분의 코딩 작업은 gpt-5.3-codex부터 시작하세요. Codex 앱, CLI, IDE 확장 및 Codex Cloud의 ChatGPT 인증 Codex 세션에서 사용할 수 있습니다. GPT-5.3-Codex의 API 접근은 곧 제공될 예정입니다. gpt-5.3-codex-spark 모델은 ChatGPT Pro 구독자를 위한 연구 미리보기로 제공됩니다.

## 대체 모델

{" "}

### gpt-5.2
업종과 도메인 전반에 걸친 작업을 위한 최고의 일반 대리 모델입니다.
- Model ID: `gpt-5.2`

### gpt-5.1-codex-max
Codex에서 장기 대리 코딩 작업을 위해 최적화되었습니다.
- Model ID: `gpt-5.1-codex-max`

### gpt-5.1
코딩과 대리 작업에 모두 적합한 모델로, GPT-5.2로 이어졌습니다.
- Model ID: `gpt-5.1`

### gpt-5.1-codex
Codex에서 장시간 실행되는 대리 코딩 작업에 최적화되었으며 GPT-5.1-Codex-Max의 후속입니다.
- Model ID: `gpt-5.1-codex`

### gpt-5-codex
장시간 실행되는 대리 코딩 작업에 맞춰 조정된 GPT-5 버전입니다. GPT-5.1-Codex의 후속입니다.
- Model ID: `gpt-5-codex`

### gpt-5-codex-mini
GPT-5-Codex의 더 작고 비용 효율적인 버전입니다. GPT-5.1-Codex-Mini의 후속입니다.
- Model ID: `gpt-5-codex`

### gpt-5
도메인 전반에 걸친 코딩과 대리 작업을 위한 추론 모델입니다. GPT-5.1로 이어졌습니다.
- Model ID: `gpt-5`

## 기타 모델

Codex는 위에 나열된 모델에서 가장 잘 작동합니다.

특정 사용 사례에 맞게 Codex를 [Chat Completions](https://platform.openai.com/docs/api-reference/chat) 또는 [Responses API](https://platform.openai.com/docs/api-reference/responses)를 지원하는 모든 모델과 제공업체에 연결할 수도 있습니다.

Chat Completions API에 대한 지원은 더 이상 권장되지 않으며 향후 Codex 릴리스에서 제거될 예정입니다.

## 모델 구성

### 기본 로컬 모델 구성

Codex CLI와 IDE 확장은 동일한 `config.toml` [구성 파일](https://developers.openai.com/codex/config-basic)을 사용합니다. 모델을 지정하려면 구성 파일에 `model` 항목을 추가하세요. 모델을 지정하지 않으면 Codex 앱, CLI 또는 IDE 확장에서 추천 모델을 기본값으로 사용합니다.

```toml
model = "gpt-5.2"
```

### 임시로 다른 로컬 모델 선택

Codex CLI에서는 활성 스레드에서 `/model` 명령을 사용하여 모델을 변경할 수 있습니다. IDE 확장에서는 입력 상자 아래의 모델 선택기를 사용하여 모델을 선택할 수 있습니다.

특정 모델로 새로운 Codex CLI 스레드를 시작하거나 `codex exec`의 모델을 지정하려면 `--model`/`-m` 플래그를 사용할 수 있습니다.

```bash
codex -m gpt-5.3-codex
```

### 클라우드 작업을 위한 모델 선택

현재 Codex 클라우드 작업의 기본 모델은 변경할 수 없습니다.

