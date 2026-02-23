---
title: Codex IDE 확장 기능
description: "출처 URL: https://developers.openai.com/codex/ide/features"
sidebar:
  order: 2
---

# Codex IDE 확장 기능

출처 URL: https://developers.openai.com/codex/ide/features

Codex IDE 확장을 사용하면 VS Code, Cursor, Windsurf 및 기타 VS Code 호환 편집기에서 Codex에 직접 접근할 수 있습니다. Codex CLI와 동일한 에이전트를 사용하며 동일한 구성을 공유합니다.

## Codex 프롬프트 사용

에디터에서 Codex를 사용하면 채팅, 편집, 변경 사항 미리보기를 매끄럽게 수행할 수 있습니다. Codex가 열린 파일과 선택한 코드의 컨텍스트를 갖고 있을 때, 더 짧은 프롬프트로 더 빠르고 관련성 높은 결과를 받을 수 있습니다.

프롬프트에서 다음과 같이 파일을 태그하여 에디터의 어떤 파일이든 참조할 수 있습니다.
```
    Use @example.tsx as a reference to add a new page named "Resources" to the app that contains a list of resources defined in @resources.ts
```

## 모델 전환

채팅 입력란 아래의 스위처로 모델을 전환할 수 있습니다.

## 추론 노력 조절

Codex가 응답하기 전에 얼마나 오래 생각할지를 추론 노력으로 조절할 수 있습니다. 노력 수준이 높을수록 복잡한 작업에 도움이 되지만 응답 시간이 길어집니다. 노력 수준을 높이면 토큰 사용량도 늘어나서 속도 제한을 더 빨리 소모할 수 있습니다(특히 GPT-5-Codex 사용 시).

위에 언급한 동일한 모델 스위처에서 각 모델에 대해 `low`, `medium`, `high` 중 하나를 선택하세요. 기본적으로는 `medium`으로 시작하고, 더 깊은 분석이 필요할 때만 `high`로 전환하세요.

## 승인 모드 선택

기본적으로 Codex는 `Agent` 모드로 실행됩니다. 이 모드에서는 Codex가 작업 디렉터리에서 파일을 읽고, 수정하고, 명령을 자동으로 실행할 수 있습니다. 작업 디렉터리 밖에서 작업하거나 네트워크에 접근하려면 여전히 승인이 필요합니다.

단순히 대화를 하거나 변경 전에 계획을 세우고 싶다면 채팅 입력란 아래의 스위처에서 `Chat`으로 전환하세요.

승인 없이 Codex가 파일을 읽고, 수정하고, 네트워크 접근 권한으로 명령을 실행하도록 해야 한다면 `Agent (Full Access)`를 사용하세요. 이때는 반드시 주의를 기울이세요.

## 클라우드 위임

더 큰 작업을 클라우드의 Codex에 위임하고, IDE를 떠나지 않고 진행 상황을 추적하고 결과를 검토할 수 있습니다.

  1. [Codex용 클라우드 환경](https://chatgpt.com/codex/settings/environments)을 설정합니다.
  2. 환경을 선택한 뒤 **Run in the cloud**를 선택합니다.

Codex를 `main`에서 실행할 수도 있고(새 아이디어를 시작할 때 유용), 로컬 변경 내용에서 실행할 수도 있습니다(작업을 마무리할 때 유용).

로컬 대화에서 클라우드 작업을 시작하면 Codex가 대화 컨텍스트를 기억하여 중단한 지점부터 이어갈 수 있습니다.

## 클라우드 작업 후속 처리

Codex 확장을 사용하면 클라우드 변경 사항 미리보기가 간단합니다. 클라우드에서 후속 작업을 실행하도록 요청할 수 있지만, 종종 변경 사항을 로컬에 적용해 테스트하고 마무리하고 싶을 때가 있습니다. 대화를 로컬로 이어가면 Codex는 시간을 절약할 수 있도록 컨텍스트를 계속 유지합니다.

[Codex 클라우드 인터페이스](https://chatgpt.com/codex)에서도 클라우드 작업을 확인할 수 있습니다.

## 웹 검색

Codex는 1차 웹 검색 도구를 기본으로 제공합니다. Codex IDE 확장에서 로컬 작업을 수행할 때 Codex는 기본적으로 웹 검색을 활성화하고 웹 검색 캐시에서 결과를 제공합니다. 이 캐시는 OpenAI가 관리하는 웹 결과 인덱스이므로, 캐시 모드에서는 실시간 페이지를 가져오는 대신 사전에 인덱싱된 결과를 반환합니다. 이는 무작위 라이브 콘텐츠의 프롬프트 인젝션 노출을 줄여 주지만, 웹 결과는 여전히 신뢰할 수 없는 것으로 취급해야 합니다. 샌드박스를 [full access](https://developers.openai.com/codex/security)로 구성하면, 웹 검색이 기본적으로 라이브 결과를 사용합니다. 웹 검색을 비활성화하거나 최신 데이터를 가져오는 라이브 결과로 전환하려면 [Config basics](https://developers.openai.com/codex/config-basic)를 참조하세요.

Codex가 무언가를 검색할 때마다 대화 기록 또는 `codex exec --json` 출력에 `web_search` 항목이 표시됩니다.

## 프롬프트에 이미지 드래그 앤 드롭

이미지를 프롬프트 작성기에 드래그 앤 드롭하여 컨텍스트로 포함할 수 있습니다.

이미지를 드롭하는 동안 `Shift` 키를 누르세요. 그렇지 않으면 VS Code가 확장에서 드롭을 받지 못하게 합니다.

## 함께 보기

  * [Codex IDE 확장 설정](https://developers.openai.com/codex/ide/settings)