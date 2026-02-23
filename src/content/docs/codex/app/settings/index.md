---
title: 'Codex 앱 설정'
description: '설정 패널을 사용하여 Codex 앱의 동작 방식, 파일을 여는 방식, 도구와 연결하는 방식을 조정합니다. 앱 메뉴에서 설정을 열거나 <kbd>Cmd</kbd>+<kbd>,</kbd>를 누르세요.'
---

Source URL: https://developers.openai.com/codex/app/settings

# Codex 앱 설정

설정 패널을 사용하여 Codex 앱의 동작 방식, 파일을 여는 방식, 도구와 연결하는 방식을 조정합니다. 앱 메뉴에서 [**설정**](codex://settings)을 열거나 <kbd>Cmd</kbd>+<kbd>,</kbd>를 누르세요.

## 일반

파일이 어디에서 열릴지, 명령 출력이 스레드에 얼마나 표시될지를 선택하세요. 또한 <kbd>Cmd</kbd>+<kbd>Enter</kbd>를 다중 줄 프롬프트에 필수로 설정하거나 스레드 실행 중 휴면 상태로 전환되는 것을 방지할 수도 있습니다.

## 외형

테마를 선택하고, 창을 선명하게 할지 결정하며, UI 또는 코드 글꼴을 조정하세요. 글꼴 선택은 diff 검토 패널과 터미널을 포함한 앱 전체에 적용됩니다.

## 알림

턴 완료 알림이 언제 표시될지, 앱이 알림 권한을 요청할지 여부를 선택하세요.

## 에이전트 구성

앱 내 Codex 에이전트는 IDE 및 CLI 확장과 동일한 구성을 상속합니다. 일반적인 설정은 앱 내 제어를 사용하고, 고급 옵션은 `config.toml`을 편집하세요. 자세한 내용은 [Codex 보안](https://developers.openai.com/codex/security) 및 [구성 기본](https://developers.openai.com/codex/config-basic)을 참조하세요.

## Git

Git 설정을 사용하여 브랜치 명명 규칙을 표준화하고 Codex가 강제 푸시를 사용할지 선택하세요. Codex가 커밋 메시지와 풀 리퀘스트 설명을 생성하는 데 사용하는 프롬프트도 설정할 수 있습니다.

## 통합 및 MCP

MCP(Model Context Protocol)를 통해 외부 도구를 연결하세요. 권장 서버를 활성화하거나 직접 추가할 수 있습니다. 서버에 OAuth가 필요한 경우 앱에서 인증 흐름을 시작합니다. 이 설정은 MCP 구성이 `config.toml`에 저장되므로 Codex CLI 및 IDE 확장에도 적용됩니다. 자세한 내용은 [Model Context Protocol 문서](https://developers.openai.com/codex/mcp)를 참조하세요.

## 개인화

기본 성격으로 **친근함**, **실용성**, **없음**을 선택하세요. **없음**을 선택하면 성격 지시가 비활성화됩니다. 언제든지 변경할 수 있습니다.

사용자 정의 지침도 추가할 수 있습니다. 사용자 정의 지침을 편집하면 [ `AGENTS.md`의 개인 지침](https://developers.openai.com/codex/guides/agents-md)이 업데이트됩니다.

## 보관된 스레드

**보관된 스레드** 섹션에는 날짜와 프로젝트 컨텍스트가 포함된 보관된 대화가 나열됩니다. **보관 해제**를 사용하여 스레드를 복원하세요.
