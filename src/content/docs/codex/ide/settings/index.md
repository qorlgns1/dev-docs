---
title: Codex IDE 확장 설정
description: Codex IDE 확장을 맞춤 설정하려면 다음 설정을 사용하세요.
sidebar:
  order: 3
---

# Codex IDE 확장 설정

Source URL: https://developers.openai.com/codex/ide/settings

Codex IDE 확장을 맞춤 설정하려면 다음 설정을 사용하세요.

## 설정 변경

설정을 변경하려면 다음 단계를 따르세요:

  1. 편집기 설정을 엽니다.
  2. `Codex` 또는 설정 이름을 검색합니다.
  3. 값을 업데이트합니다.



Codex IDE 확장은 Codex CLI를 사용합니다. 기본 모델, 승인, 샌드박스 설정 등 일부 동작은 편집기 설정이 아니라 공유된 `~/.codex/config.toml` 파일에서 구성하세요. [Config basics](https://developers.openai.com/codex/config-basic)를 참조하세요.

## 설정 참고

Setting| Description  
---|---  
`chatgpt.cliExecutable`| 개발 전용: Codex CLI 실행 파일 경로입니다. Codex CLI를 적극적으로 개발 중인 경우가 아니라면 설정할 필요가 없습니다. 값을 수동으로 지정하면 확장의 일부 기능이 예상대로 작동하지 않을 수 있습니다.  
`chatgpt.commentCodeLensEnabled`| Codex로 완료할 수 있도록 to-do 주석 위에 CodeLens를 표시합니다.  
`chatgpt.localeOverride`| Codex UI의 기본 언어입니다. 비워두면 자동으로 감지합니다.  
`chatgpt.openOnStartup`| 확장이 시작을 마치면 Codex 사이드바에 포커스를 둡니다.  
`chatgpt.runCodexInWindowsSubsystemForLinux`| Windows 전용: Windows Subsystem for Linux (WSL)을 사용할 수 있을 때 Codex를 WSL에서 실행합니다. 샌드박스 보안을 강화하고 성능을 개선하므로 권장됩니다. 현재 Windows의 Codex 에이전트 모드는 WSL이 필요합니다. 이 설정을 변경하면 변경 사항을 적용하기 위해 VS Code가 다시 로드됩니다.
