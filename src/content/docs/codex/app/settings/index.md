---
title: Codex 앱 설정
description: "소스 URL: https://developers.openai.com/codex/app/settings"
sidebar:
  order: 3
---

# Codex 앱 설정

소스 URL: https://developers.openai.com/codex/app/settings

설정 패널을 사용해 Codex 앱의 동작 방식, 파일을 여는 방식, 도구에 연결하는 방식을 조정할 수 있습니다. 앱 메뉴에서 [**설정**](codex://settings)을 열거나 `Cmd`+`,`를 누르세요.

## 일반

파일을 어디에서 열지, 스레드에 명령 출력이 얼마나 표시될지 선택하세요. 여러 줄 프롬프트에 `Cmd`+`Enter`를 필수로 설정하거나, 스레드 실행 중 절전 모드로 전환되지 않도록 할 수도 있습니다.

## 모양

테마를 선택하고, 창을 불투명하게 표시할지 결정하며, UI 또는 코드 글꼴을 조정하세요. 글꼴 선택은 diff 리뷰 패널과 터미널을 포함한 앱 전체에 적용됩니다.

## 알림

턴 완료 알림을 언제 표시할지, 그리고 앱이 알림 권한을 요청할지 선택하세요.

## 에이전트 구성

앱의 Codex 에이전트는 IDE 및 CLI 확장과 동일한 구성을 상속합니다. 일반적인 설정은 앱 내 컨트롤을 사용하고, 고급 옵션은 `config.toml`을 편집하세요. 자세한 내용은 [Codex 보안](https://developers.openai.com/codex/security) 및 [config basics](https://developers.openai.com/codex/config-basic)를 참고하세요.

## Git

Git 설정을 사용해 브랜치 이름 규칙을 표준화하고 Codex가 force push를 사용할지 선택하세요. Codex가 커밋 메시지와 pull request 설명을 생성할 때 사용할 프롬프트도 설정할 수 있습니다.

## 통합 및 MCP

MCP(Model Context Protocol)를 통해 외부 도구를 연결하세요. 권장 서버를 활성화하거나 직접 추가할 수 있습니다. 서버에 OAuth가 필요하면 앱이 인증 흐름을 시작합니다. MCP 구성은 `config.toml`에 저장되므로 이러한 설정은 Codex CLI 및 IDE 확장에도 적용됩니다. 자세한 내용은 [Model Context Protocol 문서](https://developers.openai.com/codex/mcp)를 참고하세요.

## 개인화

기본 성격으로 **Friendly**, **Pragmatic**, **None** 중에서 선택하세요. 성격 지시를 비활성화하려면 **None**을 사용하세요. 이 설정은 언제든지 변경할 수 있습니다.

직접 사용자 지정 지시를 추가할 수도 있습니다. 사용자 지정 지시를 편집하면 [ `AGENTS.md`의 개인 지시](https://developers.openai.com/codex/guides/agents-md)도 함께 업데이트됩니다.

## 보관된 스레드

**Archived threads** 섹션에는 날짜와 프로젝트 컨텍스트가 포함된 보관된 채팅 목록이 표시됩니다. 스레드를 복원하려면 **Unarchive**를 사용하세요.
