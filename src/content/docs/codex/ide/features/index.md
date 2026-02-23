---
title: 'Codex IDE 확장 기능'
description: 'Codex IDE 확장을 통해 VS Code, Cursor, Windsurf 및 기타 VS Code 호환 편집기에서 Codex에 바로 접근할 수 있습니다. Codex CLI와 동일한 에이전트를 사용하며, 설정도 공유합니다.'
---

Source URL: https://developers.openai.com/codex/ide/features

# Codex IDE 확장 기능

Codex IDE 확장을 통해 VS Code, Cursor, Windsurf 및 기타 VS Code 호환 편집기에서 Codex에 바로 접근할 수 있습니다. Codex CLI와 동일한 에이전트를 사용하며, 설정도 공유합니다.

## Codex에 프롬프트 보내기

에디터에서 Codex와 대화하고, 편집하고, 변경 사항을 미리 보기까지 매끄럽게 진행할 수 있습니다. Codex가 열린 파일이나 선택한 코드의 맥락을 알게 되면 짧은 프롬프트로 더 빠르고 관련성 높은 결과를 얻을 수 있습니다.

아래처럼 프롬프트에서 태그하여 에디터 안의 어떤 파일이라도 참조할 수 있습니다.

```text
Use @example.tsx as a reference to add a new page named "Resources" to the app that contains a list of resources defined in @resources.ts
```

## 모델 간 전환

채팅 입력란 아래의 스위처로 모델을 전환할 수 있습니다.

  <img src="https://developers.openai.com/images/codex/ide/switch_model.png"
    alt="Codex model switcher"
    class="block h-auto w-full mx-0!"
  />

## 추론 노력 조정

Codex가 응답하기 전에 얼마나 오래 생각할지 추론 노력을 조정할 수 있습니다. 복잡한 작업에는 더 높은 노력이 도움이 되지만, 응답 시간이 길어지고 GPT-5-Codex처럼 토큰 소모가 커져 속도 제한을 더 빨리 소진할 수 있습니다.

위에서 본 모델 스위처를 활용해 각 모델에 대해 `low`, `medium`, `high` 중 하나를 선택하세요. 처음에는 `medium`으로 시작하고 더 깊은 내용을 원할 때만 `high`로 바꾸세요.

## 승인 모드 선택

기본적으로 Codex는 `Agent` 모드로 실행됩니다. 이 모드에서는 Codex가 작업 디렉터리에서 파일을 읽고 편집하며 명령을 자동으로 실행할 수 있습니다. 작업 디렉터리 밖에서 활동하거나 네트워크에 접근하려면 여전히 승인이 필요합니다.

그냥 대화하거나 변경을 계획한 다음 작업하고 싶을 경우, 채팅 입력란 아래의 스위처로 `Chat` 모드로 전환하세요.

  <img src="https://developers.openai.com/images/codex/ide/approval_mode.png"
    alt="Codex approval modes"
    class="block h-auto w-full mx-0!"
  />

승인 없이 파일을 읽고 편집하며 네트워크 명령을 실행해야 한다면 `Agent (Full Access)`를 사용하세요. 이 모드는 신중히 선택하세요.

## 클라우드 위임

큰 작업은 Codex에게 클라우드에서 맡기고, IDE를 떠나지 않고 진행 상황을 추적하며 결과를 검토할 수 있습니다.

1. [Codex용 클라우드 환경 설정](https://chatgpt.com/codex/settings/environments)을 완료합니다.
2. 환경을 선택하고 **Run in the cloud**를 클릭합니다.

`main`에서 Codex를 실행하면 새로운 아이디어를 시작할 때 유용하고, 로컬 변경 내용에서 실행하면 작업을 마무리할 때 유용합니다.

  <img src="https://developers.openai.com/images/codex/ide/start_cloud_task.png"
    alt="Start a cloud task from the IDE"
    class="block h-auto w-full mx-0!"
  />

로컬 대화에서 클라우드 작업을 시작하면 Codex가 대화 맥락을 기억해 이어서 작업할 수 있습니다.

## 클라우드 작업 후속

Codex 확장은 클라우드 변경 사항을 미리 보는 과정을 간단하게 만듭니다. 클라우드에서 후속 작업을 요청할 수 있지만, 보통은 로컬에 적용해 테스트하고 마무리하게 됩니다. 로컬에서 대화를 이어가면 Codex가 맥락을 유지해 시간을 절약합니다.

  <img src="https://developers.openai.com/images/codex/ide/load_cloud_task.png"
    alt="Load a cloud task into the IDE"
    class="block h-auto w-full mx-0!"
  />

[Codex 클라우드 인터페이스](https://chatgpt.com/codex)에서도 클라우드 작업을 확인할 수 있습니다.

## 웹 검색

Codex는 자체 웹 검색 도구를 제공합니다. Codex IDE 확장에서 로컬 작업을 수행할 때는 기본적으로 웹 검색이 활성화되며, 웹 검색 캐시에서 결과를 제공합니다. 이 캐시는 OpenAI가 유지하는 웹 결과 인덱스이며, 캐시 모드는 실시간 페이지를 새로 가져오는 대신 사전 인덱싱된 결과를 반환합니다. 따라서 임의의 실시간 콘텐츠로부터 오는 프롬프트 주입 위험이 줄어들지만, 웹 결과는 여전히 신뢰하지 않는 것으로 처리하는 것이 좋습니다. [전체 액세스](https://developers.openai.com/codex/security)를 위해 샌드박스를 구성하면 웹 검색은 실시간 결과로 기본 설정되고, 가장 최신 데이터를 가져옵니다. [Config basics](https://developers.openai.com/codex/config-basic)를 참고하여 웹 검색을 비활성화하거나 최신 데이터를 가져오는 실시간 결과로 전환하세요.

Codex가 무언가를 찾아볼 때마다 대화 기록이나 `codex exec --json` 출력에 `web_search` 항목이 표시됩니다.

## 프롬프트에 이미지 드래그 앤 드롭

프롬프트 작성기에 이미지를 드래그앤드롭하여 컨텍스트로 포함할 수 있습니다.

이미지를 드롭할 때 `Shift`를 누르고 있어야 합니다. 그렇지 않으면 VS Code가 확장 프로그램에 드롭을 허용하지 않습니다.

## 참고

- [Codex IDE 확장 설정](https://developers.openai.com/codex/ide/settings)
