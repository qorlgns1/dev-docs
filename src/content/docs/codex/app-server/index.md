---
title: Codex 앱 서버
description: "Codex app-server는 Codex가 풍부한 클라이언트를 구동할 때 사용하는 인터페이스입니다(예: Codex VS Code 확장). 인증, 대화 기록, 승인, 스트리밍 에이전트 이벤트까지 포함한 깊은 제품 내 통합이 필요할 때 사용하세요. app-server 구..."
---

# Codex 앱 서버

Source URL: https://developers.openai.com/codex/app-server

Codex app-server는 Codex가 풍부한 클라이언트를 구동할 때 사용하는 인터페이스입니다(예: Codex VS Code 확장). 인증, 대화 기록, 승인, 스트리밍 에이전트 이벤트까지 포함한 깊은 제품 내 통합이 필요할 때 사용하세요. app-server 구현은 Codex GitHub 리포지토리의 오픈 소스입니다([openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)). 전체 오픈 소스 Codex 구성 요소 목록은 [Open Source](https://developers.openai.com/codex/open-source) 페이지를 참고하세요.

작업 자동화나 CI 환경에서 Codex를 실행한다면 대신 [Codex SDK](https://developers.openai.com/codex/sdk)를 사용하세요.

## Protocol

[MCP](https://modelcontextprotocol.io/)와 마찬가지로, `codex app-server`는 JSON-RPC 2.0 메시지를 사용해 양방향 통신을 지원합니다(전송 시 `"jsonrpc":"2.0"` 헤더 생략).

지원되는 전송 방식:

  * `stdio` (`--listen stdio://`, 기본값): 줄바꿈으로 구분된 JSON(JSONL).
  * `websocket` (`--listen ws://IP:PORT`, 실험적): WebSocket 텍스트 프레임당 한 개의 JSON-RPC 메시지.

WebSocket 모드에서는 app-server가 제한된 큐를 사용합니다. 요청 유입이 가득 차면 서버는 JSON-RPC 오류 코드 `-32001`, 메시지 `"Server overloaded; retry later."`로 새 요청을 거부합니다. 클라이언트는 지수적으로 증가하는 지연과 지터를 사용해 재시도해야 합니다.

## Message schema

요청에는 `method`, `params`, `id`가 포함됩니다:
[code] 
    { "method": "thread/start", "id": 10, "params": { "model": "gpt-5.1-codex" } }
[/code]

응답은 `id`를 그대로 되돌려 보내며 `result` 또는 `error`를 포함합니다:
[code] 
    { "id": 10, "result": { "thread": { "id": "thr_123" } } }
[/code]
[code] 
    { "id": 10, "error": { "code": 123, "message": "Something went wrong" } }
[/code]

알림은 `id`를 생략하고 `method`와 `params`만 사용합니다:
[code] 
    { "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }
[/code]

CLI에서 TypeScript 스키마 또는 JSON Schema 번들을 생성할 수 있습니다. 각 출력물은 실행한 Codex 버전에 맞춰져 있으므로 생성된 산출물은 해당 버전에 정확히 일치합니다:
[code] 
    codex app-server generate-ts --out ./schemas
    codex app-server generate-json-schema --out ./schemas
[/code]

## Getting started

  1. `codex app-server`(기본 stdio 전송) 또는 `codex app-server --listen ws://127.0.0.1:4500`(실험적 WebSocket 전송)로 서버를 시작합니다.
  2. 선택한 전송 방식으로 클라이언트를 연결한 뒤 `initialize`를 보내고 `initialized` 알림을 이어서 전송합니다.
  3. 스레드와 턴을 시작하고, 활성화된 전송 스트림에서 계속 알림을 읽습니다.

예시(Node.js / TypeScript):
[code] 
    import { spawn } from "node:child_process";
    import readline from "node:readline";
    
    const proc = spawn("codex", ["app-server"], {
      stdio: ["pipe", "pipe", "inherit"],
    });
    const rl = readline.createInterface({ input: proc.stdout });
    
    const send = (message: unknown) => {
      proc.stdin.write(`${JSON.stringify(message)}\n`);
    };
    
    let threadId: string | null = null;
    
    rl.on("line", (line) => {
      const msg = JSON.parse(line) as any;
      console.log("server:", msg);
    
      if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
        threadId = msg.result.thread.id;
        send({
          method: "turn/start",
          id: 2,
          params: {
            threadId,
            input: [{ type: "text", text: "Summarize this repo." }],
          },
        });
      }
    });
    
    send({
      method: "initialize",
      id: 0,
      params: {
        clientInfo: {
          name: "my_product",
          title: "My Product",
          version: "0.1.0",
        },
      },
    });
    send({ method: "initialized", params: {} });
    send({ method: "thread/start", id: 1, params: { model: "gpt-5.1-codex" } });
[/code]

## Core primitives

* **스레드** : 사용자와 Codex 에이전트 간의 대화입니다. 스레드는 턴을 포함합니다.
  * **턴** : 단일 사용자 요청과 그에 따른 에이전트 작업입니다. 턴에는 항목과 스트리밍 방식의 점진적 업데이트가 포함됩니다.
  * **항목** : 입력 또는 출력 단위(사용자 메시지, 에이전트 메시지, 명령 실행, 파일 변경, 도구 호출 등)입니다.



스레드 API를 사용해 대화를 생성·목록화·보관할 수 있습니다. 턴 API로 대화를 진행하고, 턴 알림을 통해 진행 상황을 스트리밍하세요.

## 라이프사이클 개요

  * **연결당 한 번 초기화** : 전송 연결을 연 직후 `initialize` 요청을 보내 클라이언트 메타데이터를 전달하고, 이어서 `initialized`를 내보냅니다. 이 핸드셰이크 전에 들어오는 요청은 서버가 거부합니다.
  * **스레드 시작(또는 재개)** : 새 대화는 `thread/start`, 기존 대화는 `thread/resume`, 과거를 분기해 새 스레드 ID를 만들려면 `thread/fork`를 호출합니다.
  * **턴 시작** : 대상 `threadId`와 사용자 입력을 포함해 `turn/start`를 호출합니다. 선택적 필드로 모델, 개성, `cwd`, 샌드박스 정책 등을 덮어쓸 수 있습니다.
  * **진행 중인 턴 조정** : 새 턴을 만들지 않고 현재 진행 중인 턴에 사용자 입력을 추가하려면 `turn/steer`를 호출합니다.
  * **이벤트 스트림** : `turn/start` 이후 stdout에서 `item/started`, `item/completed`, `item/agentMessage/delta`, 도구 진행 상황 등 알림을 계속 읽습니다.
  * **턴 종료** : 모델이 끝나거나 `turn/interrupt` 취소 후 서버가 최종 상태와 함께 `turn/completed`를 내보냅니다.



## 초기화

클라이언트는 각 전송 연결마다 다른 메서드를 호출하기 전에 단 한 번 `initialize` 요청을 보내고, 이어 `initialized` 알림으로 확인해야 합니다. 초기화 전에 보낸 요청은 `Not initialized` 오류가 발생하며, 동일 연결에서 반복된 `initialize` 호출은 `Already initialized`를 반환합니다.

서버는 상위 서비스에 제시할 사용자 에이전트 문자열을 반환합니다. `clientInfo`를 설정해 통합을 식별하세요.

`initialize.params.capabilities`는 연결 단위 알림 옵트아웃도 지원합니다. `optOutNotificationMethods`는 해당 연결에서 억제할 정확한 메서드 이름 목록이며, 정확히 일치해야 합니다(와일드카드/접두사 없음). 알 수 없는 메서드 이름은 허용하지만 무시됩니다.

**중요** : OpenAI Compliance Logs Platform에서 클라이언트를 식별하려면 `clientInfo.name`을 사용하세요. 엔터프라이즈용 새 Codex 통합을 개발 중이라면 OpenAI에 연락해 알려진 클라이언트 목록에 추가되도록 하세요. 자세한 내용은 [Codex 로그 레퍼런스](https://chatgpt.com/admin/api-reference#tag/Logs:-Codex)를 참조하세요.

예시(Codex VS Code 확장):
[code] 
    {
      "method": "initialize",
      "id": 0,
      "params": {
        "clientInfo": {
          "name": "codex_vscode",
          "title": "Codex VS Code Extension",
          "version": "0.1.0"
        }
      }
    }
[/code]

알림 옵트아웃 예시:
[code] 
    {
      "method": "initialize",
      "id": 1,
      "params": {
        "clientInfo": {
          "name": "my_client",
          "title": "My Client",
          "version": "0.1.0"
        },
        "capabilities": {
          "experimentalApi": true,
          "optOutNotificationMethods": [
            "codex/event/session_configured",
            "item/agentMessage/delta"
          ]
        }
      }
    }
[/code]

## 실험적 API 옵트인

일부 앱 서버 메서드와 필드는 의도적으로 `experimentalApi` 기능 뒤에 게이트되어 있습니다.

  * `capabilities`를 생략하거나 `experimentalApi`를 `false`로 설정하면 안정적인 API 범위를 유지하며, 서버는 실험적 메서드/필드를 거부합니다.
  * `capabilities.experimentalApi`를 `true`로 설정하면 실험적 메서드와 필드를 사용할 수 있습니다.


[code] 
    {
      "method": "initialize",
      "id": 1,
      "params": {
        "clientInfo": {
          "name": "my_client",
          "title": "My Client",
          "version": "0.1.0"
        },

"capabilities": {
          "experimentalApi": true
        }
      }
    }
[/code]

클라이언트가 opt-in 없이 실험적 메서드나 필드를 보내면, app-server는 다음 메시지로 요청을 거부합니다:

`<descriptor> requires experimentalApi capability`

## API 개요

  * `thread/start` - 새 스레드를 생성합니다; `thread/started`를 내보내고 해당 스레드의 turn/item 이벤트를 자동 구독합니다.
  * `thread/resume` - 기존 스레드 ID를 다시 열어 이후 `turn/start` 호출이 이어서 추가되도록 합니다.
  * `thread/fork` - 저장된 기록을 복사해 새 스레드 ID로 분기합니다; 새 스레드에 대해 `thread/started`를 내보냅니다.
  * `thread/read` - 스레드 ID로 저장된 스레드를 다시 열지 않고 읽습니다; 전체 turn 기록을 반환하려면 `includeTurns`를 설정합니다.
  * `thread/list` - 저장된 스레드 로그를 페이지 체계로 탐색합니다; 커서 기반 페이지네이션과 `modelProviders`, `sourceKinds`, `archived`, `cwd` 필터를 지원합니다.
  * `thread/loaded/list` - 현재 메모리에 로드된 스레드 ID를 목록으로 제공합니다.
  * `thread/archive` - 스레드 로그 파일을 아카이브 디렉터리로 이동합니다; 성공 시 `{}`를 반환합니다.
  * `thread/unarchive` - 아카이브된 스레드 롤아웃을 활성 세션 디렉터리로 복원하고, 복원된 `thread`를 반환합니다.
  * `thread/compact/start` - 스레드의 대화 기록 압축을 트리거합니다; 즉시 `{}`를 반환하고 진행 상황은 `turn/*`, `item/*` 알림으로 스트리밍됩니다.
  * `thread/rollback` - 인메모리 컨텍스트에서 마지막 N개의 turn을 제거하고 롤백 마커를 유지합니다; 업데이트된 `thread`를 반환합니다.
  * `turn/start` - 스레드에 사용자 입력을 추가하고 Codex 생성을 시작합니다; 초기 `turn`으로 응답하고 이벤트를 스트리밍합니다. `collaborationMode`에서 `settings.developer_instructions: null`은 “선택된 모드의 기본 내장 지침 사용”을 의미합니다.
  * `turn/steer` - 스레드의 현재 진행 중인 turn에 사용자 입력을 이어 붙입니다; 승인된 `turnId`를 반환합니다.
  * `turn/interrupt` - 진행 중인 turn의 취소를 요청합니다; 성공 시 `{}`이며 해당 turn은 `status: "interrupted"`로 종료됩니다.
  * `review/start` - 스레드에 대해 Codex 검토자를 시작합니다; `enteredReviewMode`와 `exitedReviewMode` 항목을 내보냅니다.
  * `command/exec` - 스레드/turn을 시작하지 않고 서버 샌드박스에서 단일 명령을 실행합니다.
  * `model/list` - 사용 가능한 모델을 나열합니다 (`includeHidden: true`를 설정하면 `hidden: true` 항목 포함); 노력 옵션, 선택적 `upgrade`, `inputModalities`를 제공합니다.
  * `experimentalFeature/list` - 수명 주기 단계 메타데이터와 커서 페이지네이션을 포함하는 기능 플래그를 나열합니다.
  * `collaborationMode/list` - 협업 모드 프리셋을 나열합니다(실험적, 페이지네이션 없음).
  * `skills/list` - 하나 이상의 `cwd` 값에 대한 스킬을 나열합니다 (`forceReload`와 선택적 `perCwdExtraUserRoots` 지원).
  * `app/list` - 페이지네이션과 접근성/활성화 메타데이터를 포함해 사용 가능한 앱(커넥터)을 나열합니다.
  * `skills/config/write` - 경로별로 스킬을 활성화하거나 비활성화합니다.
  * `mcpServer/oauth/login` - 구성된 MCP 서버에 대한 OAuth 로그인을 시작합니다; 인증 URL을 반환하고 완료 시 `mcpServer/oauthLogin/completed`를 내보냅니다.
  * `tool/requestUserInput` - 도구 호출을 위해 1-3개의 짧은 질문으로 사용자를 프롬프트합니다(실험적); 질문은 자유 입력 옵션을 위한 `isOther`를 설정할 수 있습니다.
  * `config/mcpServer/reload` - 디스크에서 MCP 서버 구성을 다시 로드하고 로드된 스레드에 새로고침을 큐에 추가합니다.
  * `mcpServerStatus/list` - MCP 서버, 도구, 리소스, 인증 상태를 나열합니다(커서 + 제한 페이지네이션).
  * `feedback/upload` - 피드백 보고서를 제출합니다(분류 + 선택적 이유/로그 + 대화 ID).
  * `config/read` - 설정 계층을 해석한 뒤 디스크에 적용된 최종 구성을 가져옵니다.
  * `config/value/write` - 사용자의 `config.toml`에 단일 구성 키/값을 씁니다.
  * `config/batchWrite` - 사용자의 `config.toml`에 구성 편집을 원자적으로 적용합니다.

* `configRequirements/read` \- `requirements.toml` 및/또는 MDM에서 allow-list와 데이터 레지던시 요구 사항을 포함한 요구 사항을 가져오며(아무 것도 설정되지 않았다면 `null`).



## 모델

### 모델 나열 (`model/list`)

`model/list`를 호출해 모델이나 퍼스널리티 선택기를 렌더링하기 전에 사용 가능한 모델과 해당 역량을 확인합니다.
[code] 
    { "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
    { "id": 6, "result": {
      "data": [{
        "id": "gpt-5.2-codex",
        "model": "gpt-5.2-codex",
        "upgrade": "gpt-5.3-codex",
        "displayName": "GPT-5.2 Codex",
        "hidden": false,
        "defaultReasoningEffort": "medium",
        "reasoningEffort": [{
          "effort": "low",
          "description": "Lower latency"
        }],
        "inputModalities": ["text", "image"],
        "supportsPersonality": true,
        "isDefault": true
      }],
      "nextCursor": null
    } }
[/code]

각 모델 항목에는 다음이 포함될 수 있습니다:

  * `reasoningEffort` \- 모델이 지원하는 추론 노력 옵션.
  * `defaultReasoningEffort` \- 클라이언트에 권장되는 기본 노력.
  * `upgrade` \- 클라이언트에서 마이그레이션 프롬프트에 사용할 선택적 권장 업그레이드 모델 ID.
  * `hidden` \- 모델이 기본 선택기 목록에서 숨김 처리되는지 여부.
  * `inputModalities` \- 모델이 지원하는 입력 유형(예: `text`, `image`).
  * `supportsPersonality` \- `/personality`와 같은 퍼스널리티별 지침을 모델이 지원하는지 여부.
  * `isDefault` \- 모델이 권장 기본값인지 여부.



기본적으로 `model/list`는 선택기에서 보이는 모델만 반환합니다. 전체 목록이 필요하고 클라이언트 측에서 `hidden`을 활용해 필터링하려면 `includeHidden: true`로 설정합니다.

`inputModalities`가 없는 오래된 모델 카탈로그의 경우, 하위 호환성을 위해 `["text", "image"]`로 간주합니다.

### 실험적 기능 나열 (`experimentalFeature/list`)

이 엔드포인트를 사용해 메타데이터와 라이프사이클 단계가 포함된 기능 플래그를 확인합니다:
[code] 
    { "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
    { "id": 7, "result": {
      "data": [{
        "name": "unified_exec",
        "stage": "beta",
        "displayName": "Unified exec",
        "description": "Use the unified PTY-backed execution tool.",
        "announcement": "Beta rollout for improved command execution reliability.",
        "enabled": false,
        "defaultEnabled": false
      }],
      "nextCursor": null
    } }
[/code]

`stage`는 `beta`, `underDevelopment`, `stable`, `deprecated`, `removed`일 수 있습니다. 베타가 아닌 플래그의 경우 `displayName`, `description`, `announcement`가 `null`일 수 있습니다.

## 스레드

  * `thread/read`는 구독 없이 저장된 스레드를 읽으며, 턴을 포함하려면 `includeTurns`를 설정합니다.
  * `thread/list`는 커서 기반 페이지네이션과 함께 `modelProviders`, `sourceKinds`, `archived`, `cwd` 필터링을 지원합니다.
  * `thread/loaded/list`는 현재 메모리에 있는 스레드 ID를 반환합니다.
  * `thread/archive`는 스레드의 영구 JSONL 로그를 아카이브 디렉터리로 이동합니다.
  * `thread/unarchive`는 아카이브된 스레드 롤아웃을 활성 세션 디렉터리로 복원합니다.
  * `thread/compact/start`는 압축을 트리거하고 즉시 `{}`를 반환합니다.
  * `thread/rollback`은 인메모리 컨텍스트에서 마지막 N개의 턴을 제거하고 스레드의 영구 JSONL 로그에 롤백 마커를 기록합니다.



### 스레드 시작 또는 재개

새 Codex 대화가 필요할 때 새 스레드를 시작하세요.
[code] 
    { "method": "thread/start", "id": 10, "params": {
      "model": "gpt-5.1-codex",
      "cwd": "/Users/me/project",
      "approvalPolicy": "never",
      "sandbox": "workspaceWrite",
      "personality": "friendly"
    } }
    { "id": 10, "result": {
      "thread": {
        "id": "thr_123",
        "preview": "",
        "modelProvider": "openai",
        "createdAt": 1730910000
      }
    } }
    { "method": "thread/started", "params": { "thread": { "id": "thr_123" } } }
[/code]

저장된 세션을 계속하려면 미리 기록해 둔 `thread.id`로 `thread/resume`를 호출하세요. 응답 형식은 `thread/start`와 동일합니다. 또한 `thread/start`에서 지원하는 것과 동일한 구성 override(`personality` 등)를 전달할 수 있습니다:
[code] 
    { "method": "thread/resume", "id": 11, "params": {
      "threadId": "thr_123",
      "personality": "friendly"
    } }
    { "id": 11, "result": { "thread": { "id": "thr_123" } } }
[/code]

스레드를 재개해도 `thread.updatedAt`(또는 rollout 파일의 수정 시각)은 자동으로 갱신되지 않습니다. 타임스탬프는 턴을 시작할 때 업데이트됩니다.

구성에서 활성 MCP 서버를 `required`로 표시했는데 해당 서버가 초기화에 실패하면, `thread/start`와 `thread/resume`는 그 서버 없이 계속 진행하는 대신 실패합니다.

`thread/start`의 `dynamicTools`는 실험적 필드이며(`capabilities.experimentalApi = true` 필요) Codex는 이 동적 도구를 스레드 rollout 메타데이터에 저장했다가 새 동적 도구를 제공하지 않으면 `thread/resume` 시 복원합니다.

롤아웃에 기록된 것과 다른 모델로 재개하면 Codex가 경고를 내고 다음 턴에 일회성 모델 전환 지시를 적용합니다.

저장된 세션에서 분기하려면 `thread.id`로 `thread/fork`를 호출하세요. 이렇게 하면 새 스레드 ID가 생성되고 `thread/started` 알림이 발생합니다:
[code] 
    { "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123" } }
    { "id": 12, "result": { "thread": { "id": "thr_456" } } }
    { "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }
[/code]

### 저장된 스레드 읽기(재개 없이)

스레드 데이터를 확인하되 스레드를 재개하거나 이벤트를 구독하고 싶지 않을 때는 `thread/read`를 사용하세요.

  * `includeTurns` \- `true`일 때 응답에 스레드의 턴이 포함되고, `false`이거나 생략하면 스레드 요약만 받습니다.


[code] 
    { "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
    { "id": 19, "result": { "thread": { "id": "thr_123", "turns": [] } } }
[/code]

`thread/resume`와 달리 `thread/read`는 스레드를 메모리에 로드하거나 `thread/started`를 발생시키지 않습니다.

### 스레드 나열(페이지네이션 및 필터 포함)

`thread/list`를 사용하면 기록 UI를 렌더링할 수 있습니다. 결과는 기본적으로 `createdAt` 기준 최신순이며, 필터는 페이지네이션 전에 적용됩니다. 다음 옵션을 조합해 전달할 수 있습니다:

  * `cursor` \- 이전 응답에서 받은 불투명 문자열; 첫 페이지에는 생략합니다.
  * `limit` \- 설정하지 않으면 서버가 적절한 페이지 크기를 기본값으로 사용합니다.
  * `sortKey` \- `created_at`(기본값) 또는 `updated_at`.
  * `modelProviders` \- 특정 제공자로 결과를 제한합니다; 설정하지 않거나 `null` 또는 빈 배열이면 모든 제공자가 포함됩니다.
  * `sourceKinds` \- 특정 스레드 소스로 제한합니다. 생략하거나 `[]`이면 서버는 기본적으로 `cli`와 `vscode` 같은 상호작용 소스만 포함합니다.
  * `archived` \- `true`이면 보관된 스레드만 나열합니다. `false`이거나 생략하면 비보관 스레드만 나열합니다(기본값).
  * `cwd` \- 세션의 현재 작업 디렉터리가 이 경로와 정확히 일치하는 스레드만 포함합니다.



`sourceKinds`는 다음 값을 허용합니다:

  * `cli`
  * `vscode`
  * `exec`
  * `appServer`
  * `subAgent`
  * `subAgentReview`
  * `subAgentCompact`
  * `subAgentThreadSpawn`
  * `subAgentOther`
  * `unknown`



예:
[code] 
    { "method": "thread/list", "id": 20, "params": {
      "cursor": null,
      "limit": 25,
      "sortKey": "created_at"
    } }
    { "id": 20, "result": {
      "data": [
        { "id": "thr_a", "preview": "Create a TUI", "modelProvider": "openai", "createdAt": 1730831111, "updatedAt": 1730831111 },
        { "id": "thr_b", "preview": "Fix tests", "modelProvider": "openai", "createdAt": 1730750000, "updatedAt": 1730750000 }
      ],
      "nextCursor": "opaque-token-or-null"
    } }
[/code]

`nextCursor`가 `null`이면 마지막 페이지에 도달한 것입니다.

### 로드된 스레드 나열

`thread/loaded/list`는 현재 메모리에 로드된 스레드 ID를 반환합니다.
[code]

{ "method": "thread/loaded/list", "id": 21 }
    { "id": 21, "result": { "data": ["thr_123", "thr_456"] } }
[/code]

### 스레드 보관

JSONL 파일로 디스크에 저장된 지속 스레드 로그를 보관 세션 디렉터리로 이동하려면 `thread/archive`를 사용하세요.
[code] 
    { "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
    { "id": 22, "result": {} }
[/code]

보관된 스레드는 `archived: true`를 전달하지 않는 한 이후 `thread/list` 호출 결과에 나타나지 않습니다.

### 스레드 보관 해제

보관된 스레드 롤아웃을 활성 세션 디렉터리로 다시 이동하려면 `thread/unarchive`를 사용하세요.
[code] 
    { "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
    { "id": 24, "result": { "thread": { "id": "thr_b" } } }
[/code]

### 스레드 압축 트리거

스레드의 수동 기록 압축을 트리거하려면 `thread/compact/start`를 사용하세요. 요청은 `{}`와 함께 즉시 반환됩니다.

앱 서버는 동일한 `threadId`에서 표준 `turn/*` 및 `item/*` 알림으로 진행 상황을 내보내며, `contextCompaction` 항목 라이프사이클(`item/started` 후 `item/completed`)을 포함합니다.
[code] 
    { "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
    { "id": 25, "result": {} }
[/code]

## 턴

`input` 필드는 다음과 같은 항목 목록을 받습니다:

  * `{ "type": "text", "text": "Explain this diff" }`
  * `{ "type": "image", "url": "https://.../design.png" }`
  * `{ "type": "localImage", "path": "/tmp/screenshot.png" }`



턴마다 구성 설정(모델, 노력도, 개성, `cwd`, 샌드박스 정책, 요약)을 재정의할 수 있습니다. 지정된 설정은 같은 스레드의 이후 턴에서 기본값이 됩니다. `outputSchema`는 현재 턴에만 적용됩니다. `sandboxPolicy.type = "externalSandbox"`인 경우 `networkAccess`를 `restricted` 또는 `enabled`로 설정하고, `workspaceWrite`인 경우 `networkAccess`는 불리언으로 유지합니다.

`turn/start.collaborationMode`에서 `settings.developer_instructions: null`은 모드 지시를 제거하는 대신 “선택한 모드의 기본 지시를 사용”함을 의미합니다.

### 샌드박스 읽기 권한(`ReadOnlyAccess`)

`sandboxPolicy`는 명시적 읽기 권한 제어를 지원합니다:

  * `readOnly`: 선택적 `access`(기본값은 `{ "type": "fullAccess" }`, 또는 제한된 루트).
  * `workspaceWrite`: 선택적 `readOnlyAccess`(기본값은 `{ "type": "fullAccess" }`, 또는 제한된 루트).



제한된 읽기 권한 구조:
[code] 
    {
      "type": "restricted",
      "includePlatformDefaults": true,
      "readableRoots": ["/Users/me/shared-read-only"]
    }
[/code]

예시:
[code] 
    { "type": "readOnly", "access": { "type": "fullAccess" } }
[/code]
[code] 
    {
      "type": "workspaceWrite",
      "writableRoots": ["/Users/me/project"],
      "readOnlyAccess": {
        "type": "restricted",
        "includePlatformDefaults": true,
        "readableRoots": ["/Users/me/shared-read-only"]
      },
      "networkAccess": false
    }
[/code]

### 턴 시작
[code] 
    { "method": "turn/start", "id": 30, "params": {
      "threadId": "thr_123",
      "input": [ { "type": "text", "text": "Run tests" } ],
      "cwd": "/Users/me/project",
      "approvalPolicy": "unlessTrusted",
      "sandboxPolicy": {
        "type": "workspaceWrite",
        "writableRoots": ["/Users/me/project"],
        "networkAccess": true
      },
      "model": "gpt-5.1-codex",
      "effort": "medium",
      "summary": "concise",
      "personality": "friendly",
      "outputSchema": {
        "type": "object",
        "properties": { "answer": { "type": "string" } },
        "required": ["answer"],
        "additionalProperties": false
      }
    } }
    { "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }
[/code]

### 활성 턴 조정

진행 중인 턴에 사용자 입력을 더 추가하려면 `turn/steer`를 사용하세요.

  * `expectedTurnId`를 포함해야 하며 활성 턴 ID와 일치해야 합니다.
  * 해당 스레드에 활성 턴이 없으면 요청이 실패합니다.

* `turn/steer`는 새로운 `turn/started` 알림을 내보내지 않습니다.
  * `turn/steer`는 턴 수준 오버라이드(`model`, `cwd`, `sandboxPolicy`, `outputSchema`)를 허용하지 않습니다.

[code] 
    { "method": "turn/steer", "id": 32, "params": {
      "threadId": "thr_123",
      "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
      "expectedTurnId": "turn_456"
    } }
    { "id": 32, "result": { "turnId": "turn_456" } }
[/code]

### 턴 시작하기(스킬 호출)

텍스트 입력에 `$<skill-name>`을 포함하고 그와 함께 `skill` 입력 항목을 추가하여 스킬을 명시적으로 호출합니다.
[code] 
    { "method": "turn/start", "id": 33, "params": {
      "threadId": "thr_123",
      "input": [
        { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
        { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
      ]
    } }
    { "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }
[/code]

### 턴 중단하기
[code] 
    { "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
    { "id": 31, "result": {} }
[/code]

성공하면 해당 턴은 `status: "interrupted"` 상태로 종료됩니다.

## 리뷰

`review/start`는 특정 스레드에 대해 Codex 리뷰어를 실행하고 리뷰 항목을 스트리밍합니다. 가능한 대상은 다음과 같습니다:

  * `uncommittedChanges`
  * `baseBranch` (브랜치와의 diff)
  * `commit` (지정 커밋 리뷰)
  * `custom` (자유 형식 지시사항)

`delivery: "inline"`(기본값)을 사용하면 기존 스레드에서 리뷰를 실행하고, `delivery: "detached"`를 사용하면 새로운 리뷰 스레드를 분기합니다.

요청/응답 예시:
[code] 
    { "method": "review/start", "id": 40, "params": {
      "threadId": "thr_123",
      "delivery": "inline",
      "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
    } }
    { "id": 40, "result": {
      "turn": {
        "id": "turn_900",
        "status": "inProgress",
        "items": [
          { "type": "userMessage", "id": "turn_900", "content": [ { "type": "text", "text": "Review commit 1234567: Polish tui colors" } ] }
        ],
        "error": null
      },
      "reviewThreadId": "thr_123"
    } }
[/code]

분리된 리뷰의 경우 `"delivery": "detached"`를 사용합니다. 응답 형식은 동일하지만 `reviewThreadId`가 원래 `threadId`와 다른 새 리뷰 스레드 ID가 됩니다. 서버는 리뷰 턴을 스트리밍하기 전에 해당 새 스레드에 대해 `thread/started` 알림도 보냅니다.

Codex는 일반적인 `turn/started` 알림을 전송한 후 `enteredReviewMode` 항목이 포함된 `item/started`를 이어서 스트리밍합니다:
[code] 
    {
      "method": "item/started",
      "params": {
        "item": {
          "type": "enteredReviewMode",
          "id": "turn_900",
          "review": "current changes"
        }
      }
    }
[/code]

리뷰가 끝나면 서버는 최종 리뷰 텍스트가 담긴 `exitedReviewMode` 항목과 함께 `item/started`, `item/completed`를 전송합니다:
[code] 
    {
      "method": "item/completed",
      "params": {
        "item": {
          "type": "exitedReviewMode",
          "id": "turn_900",
          "review": "Looks solid overall..."
        }
      }
    }
[/code]

이 알림을 사용하여 클라이언트에서 리뷰어 출력 내용을 렌더링합니다.

## 명령 실행

`command/exec`는 새 스레드를 만들지 않고 서버 샌드박스에서 단일 명령(`argv` 배열)을 실행합니다.
[code] 
    { "method": "command/exec", "id": 50, "params": {
      "command": ["ls", "-la"],
      "cwd": "/Users/me/project",
      "sandboxPolicy": { "type": "workspaceWrite" },
      "timeoutMs": 10000
    } }
    { "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }
[/code]

Use `sandboxPolicy.type = "externalSandbox"`를 사용하면 서버 프로세스를 이미 샌드박싱했을 때 Codex가 자체 샌드박스 적용을 건너뛰도록 할 수 있습니다. 외부 샌드박스 모드에서는 `networkAccess`를 기본값인 `restricted` 또는 `enabled`로 설정하세요. `readOnly`와 `workspaceWrite`에는 위에서 보여 준 선택적 `access` / `readOnlyAccess` 구조를 동일하게 사용합니다.

Notes:

  * 서버는 비어 있는 `command` 배열을 거부합니다.
  * `sandboxPolicy`는 `turn/start`에서 사용한 것과 동일한 형태(예: `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`)를 허용합니다.
  * 생략되면 `timeoutMs`는 서버 기본값으로 되돌아갑니다.



## 이벤트

이벤트 알림은 스레드 수명 주기, 턴 수명 주기, 그리고 그 안의 항목을 위한 서버 주도 스트림입니다. 스레드를 시작하거나 재개한 뒤에는 활성 전송 스트림을 계속 읽어 `thread/started`, `turn/*`, `item/*` 알림을 수신하세요.

### 알림 옵트아웃

클라이언트는 `initialize.params.capabilities.optOutNotificationMethods`에서 정확한 메서드 이름을 보내 연결 단위로 특정 알림을 억제할 수 있습니다.

  * 정확히 일치하는 경우만 해당합니다. 예를 들어 `item/agentMessage/delta`는 해당 메서드만 억제합니다.
  * 알 수 없는 메서드 이름은 무시됩니다.
  * 레거시(`codex/event/*`)와 v2(`thread/*`, `turn/*`, `item/*` 등) 알림 모두에 적용됩니다.
  * 요청, 응답, 오류에는 적용되지 않습니다.



### 퍼지 파일 검색 이벤트(실험적)

퍼지 파일 검색 세션 API는 쿼리마다 다음과 같은 알림을 발생시킵니다.

  * `fuzzyFileSearch/sessionUpdated` \- `{ sessionId, query, files }`로 현재 쿼리의 일치 결과를 제공합니다.
  * `fuzzyFileSearch/sessionCompleted` \- `{ sessionId }`를 통해 해당 쿼리에 대한 인덱싱과 매칭이 완료되었음을 알립니다.



### 턴 이벤트

  * `turn/started` \- `{ turn }`에 턴 ID, 비어 있는 `items`, `status: "inProgress"`를 포함합니다.
  * `turn/completed` \- `{ turn }`에서 `turn.status`가 `completed`, `interrupted`, `failed` 중 하나이며, 실패 시 `{ error: { message, codexErrorInfo?, additionalDetails? } }`를 전달합니다.
  * `turn/diff/updated` \- `{ threadId, turnId, diff }`로 턴에서 발생한 모든 파일 변경에 대한 최신 누적 통합 diff를 제공합니다.
  * `turn/plan/updated` \- `{ turnId, explanation?, plan }`으로 에이전트가 계획을 공유하거나 수정할 때마다 발생하며, 각 `plan` 항목은 `{ step, status }`이고 `status`는 `pending`, `inProgress`, `completed` 중 하나입니다.
  * `thread/tokenUsage/updated` \- 활성 스레드의 사용량을 업데이트합니다.



`turn/diff/updated`와 `turn/plan/updated`는 항목 이벤트가 스트림으로 흘러도 현재는 비어 있는 `items` 배열을 포함합니다. 턴 항목의 정확한 근거로는 `item/*` 알림을 사용하세요.

### 항목

`ThreadItem`은 턴 응답과 `item/*` 알림에서 전달되는 태그형 유니언입니다. 일반적인 항목 타입은 다음과 같습니다.

  * `userMessage` \- `{id, content}`이며 `content`는 사용자 입력(`text`, `image`, `localImage`) 목록입니다.
  * `agentMessage` \- `{id, text}`로 누적된 에이전트 응답을 담습니다.
  * `plan` \- `{id, text}`로 계획 모드에서 제안된 계획 텍스트이며, `item/completed`가 보낸 마지막 `plan` 항목을 기준으로 삼습니다.
  * `reasoning` \- `{id, summary, content}`로 `summary`에는 스트리밍된 추론 요약이, `content`에는 원본 추론 블록이 들어 있습니다.
  * `commandExecution` \- `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`입니다.
  * `fileChange` \- `{id, changes, status}`로 제안된 편집을 설명하며, `changes`는 `{path, kind, diff}` 목록입니다.
  * `mcpToolCall` \- `{id, server, tool, status, arguments, result?, error?}`입니다.
  * `collabToolCall` \- `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`입니다.
  * `webSearch` \- `{id, query, action?}`으로 에이전트가 실행한 웹 검색 요청을 나타냅니다.
  * `imageView` \- `{id, path}`는 에이전트가 이미지 뷰어 도구를 호출했을 때 발생합니다.
  * `enteredReviewMode` \- `{id, review}`는 검토자가 시작할 때 전송됩니다.
  * `exitedReviewMode` \- `{id, review}`는 검토가 완료되었을 때 발생합니다.
  * `contextCompaction` \- `{id}`는 Codex가 대화 기록을 압축할 때 전송됩니다.

`webSearch.action`의 action `type`은 `search` (`query?`, `queries?`), `openPage` (`url?`), 또는 `findInPage` (`url?`, `pattern?`)일 수 있습니다.

앱 서버는 기존 `thread/compacted` 알림을 사용 중단했으므로 대신 `contextCompaction` 항목을 사용하세요.

모든 항목은 두 가지 공통 라이프사이클 이벤트를 방출합니다:

  * `item/started` \- 새로운 작업 단위가 시작될 때 전체 `item`을 방출하며, `item.id`는 델타에서 사용하는 `itemId`와 일치합니다.
  * `item/completed` \- 작업이 끝나면 최종 `item`을 전송하므로 이를 권위 있는 상태로 간주하세요.



### 항목 델타

  * `item/agentMessage/delta` \- 에이전트 메시지에 대한 스트리밍 텍스트를 이어 붙입니다.
  * `item/plan/delta` \- 제안된 계획 텍스트를 스트리밍합니다. 최종 `plan` 항목은 연결된 델타와 정확히 일치하지 않을 수 있습니다.
  * `item/reasoning/summaryTextDelta` \- 읽기 쉬운 추론 요약을 스트리밍하며, 새로운 요약 구역이 열릴 때 `summaryIndex`가 증가합니다.
  * `item/reasoning/summaryPartAdded` \- 추론 요약 구역 사이의 경계를 표시합니다.
  * `item/reasoning/textDelta` \- (모델이 지원하는 경우) 원시 추론 텍스트를 스트리밍합니다.
  * `item/commandExecution/outputDelta` \- 명령의 stdout/stderr를 스트리밍하며, 델타를 순서대로 이어 붙입니다.
  * `item/fileChange/outputDelta` \- 내부 `apply_patch` 도구 호출의 도구 호출 응답을 포함합니다.



## 오류

turn이 실패하면 서버는 `{ error: { message, codexErrorInfo?, additionalDetails? } }`를 포함한 `error` 이벤트를 방출하고 `status: "failed"`로 turn을 종료합니다. 업스트림 HTTP 상태가 제공되면 `codexErrorInfo.httpStatusCode`에 표시됩니다.

일반적인 `codexErrorInfo` 값은 다음과 같습니다:

  * `ContextWindowExceeded`
  * `UsageLimitExceeded`
  * `HttpConnectionFailed` (4xx/5xx upstream errors)
  * `ResponseStreamConnectionFailed`
  * `ResponseStreamDisconnected`
  * `ResponseTooManyFailedAttempts`
  * `BadRequest`, `Unauthorized`, `SandboxError`, `InternalServerError`, `Other`



업스트림 HTTP 상태가 제공되면 서버는 해당 `codexErrorInfo` 변형의 `httpStatusCode`에 이를 전달합니다.

## 승인

사용자의 Codex 설정에 따라 명령 실행과 파일 변경에는 승인이 필요할 수 있습니다. 앱 서버는 서버 주도의 JSON-RPC 요청을 클라이언트에 보내고, 클라이언트는 결정 페이로드로 응답합니다.

  * 명령 실행 결정: `accept`, `acceptForSession`, `decline`, `cancel`, 또는 `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`.
  * 파일 변경 결정: `accept`, `acceptForSession`, `decline`, `cancel`.
  * 요청에는 `threadId`와 `turnId`가 포함되며, 이를 사용해 UI 상태를 활성 대화 범위로 제한하세요.
  * 서버는 작업을 재개하거나 거부하고 `item/completed`로 항목을 종료합니다.




### 명령 실행 승인

메시지 순서:

  1. `item/started`는 `command`, `cwd` 등 필드를 포함한 보류 중인 `commandExecution` 항목을 보여줍니다.
  2. `item/commandExecution/requestApproval`에는 `itemId`, `threadId`, `turnId`, 선택적 `reason`, 선택적 `command`, 선택적 `cwd`, 선택적 `commandActions`, 선택적 `proposedExecpolicyAmendment`가 포함됩니다.
  3. 클라이언트는 위 명령 실행 승인 결정 중 하나로 응답합니다.
  4. `item/completed`는 `status: completed | failed | declined`가 포함된 최종 `commandExecution` 항목을 반환합니다.



### 파일 변경 승인

메시지 순서:

  1. `item/started`는 제안된 `changes`와 `status: "inProgress"`가 있는 `fileChange` 항목을 방출합니다.
  2. `item/fileChange/requestApproval`에는 `itemId`, `threadId`, `turnId`, 선택적 `reason`, 선택적 `grantRoot`가 포함됩니다.
  3. 클라이언트는 위 파일 변경 승인 결정 중 하나로 응답합니다.
  4. `item/completed`는 `status: completed | failed | declined`가 있는 최종 `fileChange` 항목을 반환합니다.



### MCP 도구 호출 승인 (apps)

앱(커넥터) 도구 호출에도 승인이 필요할 수 있습니다. 앱 도구 호출에 부작용이 있을 경우 서버는 `tool/requestUserInput`과 **Accept**, **Decline**, **Cancel** 같은 옵션으로 승인을 요청할 수 있습니다. 사용자가 거부하거나 취소하면 해당 `mcpToolCall` 항목은 도구를 실행하지 않고 오류로 완료됩니다.

## 스킬

사용자 텍스트 입력에 `$<skill-name>`을 포함하면 스킬을 호출할 수 있습니다. 모델이 이름을 직접 해석하도록 두는 대신 서버가 전체 스킬 지침을 주입하도록 `skill` 입력 항목을 추가하는 것이 좋습니다.
[code] 
    {
      "method": "turn/start",
      "id": 101,
      "params": {
        "threadId": "thread-1",
        "input": [
          {
            "type": "text",
            "text": "$skill-creator Add a new skill for triaging flaky CI."
          },
          {
            "type": "skill",
            "name": "skill-creator",
            "path": "/Users/me/.codex/skills/skill-creator/SKILL.md"
          }
        ]
      }
    }
[/code]

`skill` 항목을 생략해도 모델은 `$<skill-name>` 표식을 파싱해 스킬을 찾지만, 이로 인해 지연 시간이 늘어날 수 있습니다.

예:
[code] 
    $skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.
[/code]

`skills/list`를 사용하여 사용 가능한 스킬을 가져오세요(`cwds`로 범위를 지정하고 `forceReload`를 함께 사용할 수 있음). 특정 `cwd` 값에 대해 추가 절대 경로를 `user` 범위로 스캔하려면 `perCwdExtraUserRoots`를 포함할 수도 있습니다. App-server는 `cwds`에 없는 `cwd` 항목은 무시합니다. `skills/list`는 `cwd`별로 캐시된 결과를 재사용할 수 있으므로 디스크에서 새로 고치려면 `forceReload: true`를 설정하세요. 존재하는 경우 서버는 `SKILL.json`에서 `interface`와 `dependencies`를 읽습니다.
[code] 
    { "method": "skills/list", "id": 25, "params": {
      "cwds": ["/Users/me/project", "/Users/me/other-project"],
      "forceReload": true,
      "perCwdExtraUserRoots": [
        {
          "cwd": "/Users/me/project",
          "extraUserRoots": ["/Users/me/shared-skills"]
        }
      ]
    } }
    { "id": 25, "result": {
      "data": [{
        "cwd": "/Users/me/project",
        "skills": [
          {
            "name": "skill-creator",
            "description": "Create or update a Codex skill",
            "enabled": true,
            "interface": {
              "displayName": "Skill Creator",
              "shortDescription": "Create or update a Codex skill"
            },
            "dependencies": {
              "tools": [
                {
                  "type": "env_var",
                  "value": "GITHUB_TOKEN",
                  "description": "GitHub API token"
                },
                {
                  "type": "mcp",
                  "value": "github",
                  "transport": "streamable_http",
                  "url": "https://example.com/mcp"
                }
              ]
            }
          }
        ],
        "errors": []
      }]
    } }
[/code]

경로를 기준으로 스킬을 활성화하거나 비활성화하려면 다음을 사용하세요:
[code] 
    {
      "method": "skills/config/write",
      "id": 26,
      "params": {
        "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
        "enabled": false
      }
    }
[/code]

## 앱(커넥터)

`app/list`를 사용해 사용 가능한 앱을 가져옵니다. CLI/TUI에서는 `/apps`가 사용자용 선택기이며, 커스텀 클라이언트에서는 `app/list`를 직접 호출하세요. 각 항목에는 `isAccessible`(사용자가 이용 가능한지)과 `isEnabled`(`config.toml`에서 활성화되었는지)가 함께 포함되어 클라이언트가 설치·접근 여부와 로컬 활성 상태를 구분할 수 있습니다.
[code] 
    { "method": "app/list", "id": 50, "params": {
      "cursor": null,
      "limit": 50,
      "threadId": "thread-1",
      "forceRefetch": false
    } }
    { "id": 50, "result": {
      "data": [
        {
          "id": "demo-app",
          "name": "Demo App",
          "description": "Example connector for documentation.",
          "logoUrl": "https://example.com/demo-app.png",
          "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",

"isAccessible": true,
          "isEnabled": true
        }
      ],
      "nextCursor": null
    } }
[/code]

`threadId`를 제공하면 앱 기능 게이팅(`features.apps`)이 해당 스레드의 구성 스냅샷을 사용합니다. 생략하면 app-server는 최신 전역 구성을 사용합니다.

`app/list`는 접근 가능한 앱과 디렉터리 앱이 모두 로드된 후 응답합니다. `forceRefetch: true`를 설정하면 앱 캐시를 우회하고 새 데이터를 가져옵니다. 새로 고침이 성공해야만 캐시 항목이 교체됩니다.

서버는 접근 가능한 앱 또는 디렉터리 앱 중 어느 한 쪽이 로드를 마칠 때마다 `app/list/updated` 알림을 발생시킵니다. 각 알림에는 최신 병합 앱 목록이 포함됩니다.
[code] 
    {
      "method": "app/list/updated",
      "params": {
        "data": [
          {
            "id": "demo-app",
            "name": "Demo App",
            "description": "Example connector for documentation.",
            "logoUrl": "https://example.com/demo-app.png",
            "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
            "isAccessible": true,
            "isEnabled": true
          }
        ]
      }
    }
[/code]

텍스트 입력란에 `$<app-slug>`을 삽입하고 `app://<id>` 경로를 가진 `mention` 입력 항목을 추가하면 앱을 호출할 수 있습니다(권장).
[code] 
    {
      "method": "turn/start",
      "id": 51,
      "params": {
        "threadId": "thread-1",
        "input": [
          {
            "type": "text",
            "text": "$demo-app Pull the latest updates from the team."
          },
          {
            "type": "mention",
            "name": "Demo App",
            "path": "app://demo-app"
          }
        ]
      }
    }
[/code]

## 인증 엔드포인트

JSON-RPC auth/account 인터페이스는 요청/응답 메서드와 서버가 시작하는 알림(`id` 없음)을 모두 노출합니다. 이를 사용해 인증 상태를 확인하고, 로그인 시작 또는 취소, 로그아웃, ChatGPT 레이트 리밋 점검을 수행합니다.

### 인증 모드

Codex는 세 가지 인증 모드를 지원합니다. 활성 모드는 `account/updated.authMode`에 표시되며, `account/read`도 해당 모드를 보고합니다.

  * **API 키 (`apikey`)** - 호출자가 OpenAI API 키를 제공하면 Codex가 이를 API 요청용으로 저장합니다.
  * **ChatGPT 관리형 (`chatgpt`)** - Codex가 ChatGPT OAuth 플로우를 소유하고 토큰을 유지하며 자동으로 갱신합니다.
  * **ChatGPT 외부 토큰 (`chatgptAuthTokens`)** - 호스트 앱이 `idToken`과 `accessToken`을 직접 제공합니다. Codex는 이 토큰들을 메모리에 저장하며, 호스트 앱은 요청을 받으면 토큰을 갱신해야 합니다.

### API 개요

  * `account/read` - 현재 계정 정보를 가져오고, 필요하면 토큰을 갱신합니다.
  * `account/login/start` - 로그인(`apiKey`, `chatgpt`, 또는 `chatgptAuthTokens`)을 시작합니다.
  * `account/login/completed` (notify) - 로그인 시도가 완료되면(성공 또는 오류) 발생합니다.
  * `account/login/cancel` - `loginId`로 지정된 보류 중인 ChatGPT 로그인을 취소합니다.
  * `account/logout` - 로그아웃하며 `account/updated`를 트리거합니다.
  * `account/updated` (notify) - 인증 모드가 변경될 때마다(`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, 또는 `null`) 발생합니다.
  * `account/chatgptAuthTokens/refresh` (server request) - 인증 오류 이후 외부 관리 ChatGPT 토큰을 새로 요청합니다.
  * `account/rateLimits/read` - ChatGPT 레이트 리밋을 조회합니다.
  * `account/rateLimits/updated` (notify) - 사용자의 ChatGPT 레이트 리밋이 변경될 때마다 발생합니다.
  * `mcpServer/oauthLogin/completed` (notify) - `mcpServer/oauth/login` 플로우가 끝나면 발생하며 `{ name, success, error? }` 페이로드를 포함합니다.

### 1) 인증 상태 확인

요청:
[code] 
    { "method": "account/read", "id": 1, "params": { "refreshToken": false } }
[/code]

응답 예시:
[code] 
    { "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }
[/code]
[code] 
    { "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }
[/code]
[code] 
    {
      "id": 1,
      "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
    }
[/code]
[code] 
    {
      "id": 1,
      "result": {
[/code]

"account": {
          "type": "chatgpt",
          "email": "user@example.com",
          "planType": "pro"
        },
        "requiresOpenaiAuth": true
      }
    }
[/code]

필드 노트:

  * `refreshToken` (boolean): 관리형 ChatGPT 모드에서 토큰을 강제로 새로 고치려면 `true`로 설정합니다. 외부 토큰 모드(`chatgptAuthTokens`)에서는 app-server가 이 플래그를 무시합니다.
  * `requiresOpenaiAuth`는 활성 공급자를 나타내며, `false`인 경우 Codex는 OpenAI 자격 증명 없이 실행될 수 있습니다.

### 2) API 키로 로그인

  1. 전송:
[code] {
           "method": "account/login/start",
           "id": 2,
           "params": { "type": "apiKey", "apiKey": "sk-..." }
         }
[/code]

  2. 응답 예상:
[code] { "id": 2, "result": { "type": "apiKey" } }
[/code]

  3. 알림:
[code] {
           "method": "account/login/completed",
           "params": { "loginId": null, "success": true, "error": null }
         }
[/code]
[code] { "method": "account/updated", "params": { "authMode": "apikey" } }
[/code]

### 3) ChatGPT(브라우저 플로우)로 로그인

  1. 시작:
[code] { "method": "account/login/start", "id": 3, "params": { "type": "chatgpt" } }
[/code]
[code] {
           "id": 3,
           "result": {
             "type": "chatgpt",
             "loginId": "<uuid>",
             "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
           }
         }
[/code]

  2. 브라우저에서 `authUrl`을 열면 app-server가 로컬 콜백을 호스팅합니다.

  3. 다음 알림을 기다립니다:
[code] {
           "method": "account/login/completed",
           "params": { "loginId": "<uuid>", "success": true, "error": null }
         }
[/code]
[code] { "method": "account/updated", "params": { "authMode": "chatgpt" } }
[/code]

### 3b) 외부에서 관리되는 ChatGPT 토큰(`chatgptAuthTokens`)으로 로그인

호스트 애플리케이션이 사용자의 ChatGPT 인증 수명 주기를 소유하고 토큰을 직접 제공할 때 이 모드를 사용합니다.

  1. 전송:
[code] {
           "method": "account/login/start",
           "id": 7,
           "params": {
             "type": "chatgptAuthTokens",
             "idToken": "<jwt>",
             "accessToken": "<jwt>"
           }
         }
[/code]

  2. 응답 예상:
[code] { "id": 7, "result": { "type": "chatgptAuthTokens" } }
[/code]

  3. 알림:
[code] {
           "method": "account/login/completed",
           "params": { "loginId": null, "success": true, "error": null }
         }
[/code]
[code] {
           "method": "account/updated",
           "params": { "authMode": "chatgptAuthTokens" }
         }
[/code]

서버가 `401 Unauthorized`를 받으면 호스트 앱에 토큰 새로 고침을 요청할 수 있습니다:
[code] 
    {
      "method": "account/chatgptAuthTokens/refresh",
      "id": 8,
      "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
    }
    { "id": 8, "result": { "idToken": "<jwt>", "accessToken": "<jwt>" } }
[/code]

서버는 새로 고침 응답이 성공하면 원래 요청을 재시도하며, 요청은 약 10초 후에 타임아웃됩니다.

### 4) ChatGPT 로그인 취소
[code] 
    { "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
    { "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }
[/code]

### 5) 로그아웃
[code] 
    { "method": "account/logout", "id": 5 }
    { "id": 5, "result": {} }
    { "method": "account/updated", "params": { "authMode": null } }
[/code]

### 6) 속도 제한(ChatGPT)
[code] 
    { "method": "account/rateLimits/read", "id": 6 }
    { "id": 6, "result": {
      "rateLimits": {
        "limitId": "codex",
        "limitName": null,
        "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
        "secondary": null
      },
      "rateLimitsByLimitId": {
        "codex": {
          "limitId": "codex",
          "limitName": null,
          "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },

"secondary": null
        },
        "codex_other": {
          "limitId": "codex_other",
          "limitName": "codex_other",
          "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
          "secondary": null
        }
      }
    } }
    { "method": "account/rateLimits/updated", "params": {
      "rateLimits": {
        "limitId": "codex",
        "primary": { "usedPercent": 31, "windowDurationMins": 15, "resetsAt": 1730948100 }
      }
    } }
[/code]

필드 노트:

  * `rateLimits`는 이전 버전과 호환되는 단일 버킷 뷰입니다.
  * `rateLimitsByLimitId`(존재하는 경우)는 계량된 `limit_id`(예: `codex`)를 키로 사용하는 다중 버킷 뷰입니다.
  * `limitId`는 계량된 버킷 식별자입니다.
  * `limitName`은 버킷에 대한 선택적 사용자 표시 레이블입니다.
  * `usedPercent`는 쿼터 윈도 내 현재 사용량입니다.
  * `windowDurationMins`는 쿼터 윈도 길이입니다.
  * `resetsAt`는 다음 리셋 시점을 나타내는 유닉스 타임스탬프(초)입니다.
