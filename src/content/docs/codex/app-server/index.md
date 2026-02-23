---
title: 'List models (model/list)'
description: 'Codex app-server는 Codex가 풍부한 클라이언트(ex. Codex VS Code 확장)에서 사용하는 인터페이스입니다. 인증, 대화 기록, 승인, 스트리밍 에이전트 이벤트처럼 자체 제품에 깊이 통합하려면 이것을 사용하세요. app-server 구현은 Cod...'
---

Codex App Server
===============

Codex app-server는 Codex가 풍부한 클라이언트(ex. Codex VS Code 확장)에서 사용하는 인터페이스입니다. 인증, 대화 기록, 승인, 스트리밍 에이전트 이벤트처럼 자체 제품에 깊이 통합하려면 이것을 사용하세요. app-server 구현은 Codex GitHub 리포지토리([openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server))에서 오픈 소스로 공개되어 있습니다. 전체 오픈소스 Codex 구성요소 목록은 [Open Source](https://developers.openai.com/codex/open-source) 페이지를 참조하세요.

작업 자동화나 CI에서 Codex를 실행 중이라면 <a href="/codex/sdk">Codex SDK</a>를 사용하세요.

Protocol
--------

[MCP](https://modelcontextprotocol.io/)처럼 `codex app-server`는 JSON-RPC 2.0 메시지(`"jsonrpc":"2.0"` 헤더는 wire에서 생략)로 양방향 통신을 지원합니다.

지원 트랜스포트:

- `stdio` (`--listen stdio://`, 기본): 줄 끝 구분 JSON(JSONL).
- `websocket` (`--listen ws://IP:PORT`, 실험적): WebSocket 텍스트 프레임당 하나의 JSON-RPC 메시지.

WebSocket 모드에서 app-server는 유한 큐를 사용합니다. 요청 인그레스가 가득 차면 서버는 JSON-RPC 오류 코드 `-32001`과 메시지 `"Server overloaded; retry later."`로 새 요청을 거부합니다. 클라이언트는 지터가 포함된 지수 증가 지연으로 재시도해야 합니다.

Message schema
--------------

요청에는 `method`, `params`, `id`가 포함됩니다:

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.1-codex" } }
```

응답은 `id`를 그대로 echo하며 `result` 또는 `error`를 포함합니다:

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }
```

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }
```

알림은 `id` 없이 `method`와 `params`만 사용합니다:

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }
```

CLI에서 TypeScript 스키마 또는 JSON 스키마 번들을 생성할 수 있습니다. 출력은 실행한 Codex 버전에 특화되므로 생성된 결과물이 해당 버전과 정확히 일치합니다:

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas
```

Getting started
---------------

1. `codex app-server`(기본 stdio 트랜스포트) 또는 `codex app-server --listen ws://127.0.0.1:4500`(실험적 WebSocket 트랜스포트)로 서버를 시작합니다.
2. 선택한 트랜스포트로 클라이언트를 연결한 다음 `initialize`를 보내고 `initialized` 알림을 전송합니다.
3. thread와 turn을 시작하고 활성 트랜스포트 스트림에서 알림을 계속 읽습니다.

예시(Node.js / TypeScript):

```ts

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
```

Core primitives
---------------

- **Thread**: 사용자와 Codex 에이전트 간 대화. Thread는 turns를 포함합니다.
- **Turn**: 단일 사용자 요청과 뒤따르는 에이전트 작업. Turn은 items와 점진적 업데이트 스트리밍을 포함합니다.
- **Item**: 입력 또는 출력 단위(사용자 메시지, 에이전트 메시지, 명령 실행, 파일 변경, 도구 호출 등).

thread API를 사용해 대화를 생성, 나열 또는 보관하세요. turn API로 대화를 진행하고 turn 알림을 통해 진행 상황을 스트리밍하세요.

Lifecycle overview
------------------

- **연결당 한 번 초기화**: 트랜스포트 연결 직후, 클라이언트 메타데이터와 함께 `initialize` 요청을 보내고 `initialized`를 전송합니다. 이 핸드셰이크 전에는 서버가 해당 연결에 대한 요청을 거절합니다.
- **Thread 시작(또는 재개)**: 새 대화는 `thread/start`, 기존 대화 이어받기는 `thread/resume`, 히스토리 분기할 때는 `thread/fork`.
- **Turn 시작**: 대상 `threadId`와 사용자 입력으로 `turn/start`를 호출합니다. 선택 필드로 모델, 페르소나, `cwd`, 샌드박스 정책 등을 재정의할 수 있습니다.
- **진행 중인 Turn 조정**: 새로운 Turn을 만들지 않고 현재 진행 중인 Turn에 사용자 입력을 추가하려면 `turn/steer`를 호출합니다.
- **이벤트 스트리밍**: `turn/start` 이후 stdout에서 알림을 계속 읽습니다: `item/started`, `item/completed`, `item/agentMessage/delta`, 도구 진행 상황 등.
- **Turn 종료**: 모델이 완료되거나 `turn/interrupt`로 취소되면 서버가 최종 상태와 함께 `turn/completed`를 발생시킵니다.

Initialization
--------------

클라이언트는 연결당 하나의 `initialize` 요청을 보내고 `initialized` 알림으로 응답해야 다른 메서드를 호출할 수 있습니다. 초기화 이전에 전송된 요청은 `Not initialized` 오류를 받고, 동일 연결에서 반복된 `initialize`는 `Already initialized`를 반환합니다.

서버는 상위 서비스에 사용할 사용자 에이전트 문자열을 반환합니다. `clientInfo`로 통합을 식별하세요.

`initialize.params.capabilities`에서는 `optOutNotificationMethods`를 통해 연결별 알림 제외도 지원합니다. 이 목록에는 해당 연결에서 생략할 정확한 메서드 이름을 나열하며 일치 여부는 엄격합니다(와일드카드/접두사 없음). 알 수 없는 메서드 이름은 수락되며 무시됩니다.

**중요**: OpenAI Compliance Logs Platform에 클라이언트 식별자로 `clientInfo.name`을 사용하세요. 엔터프라이즈용 새로운 Codex 통합을 개발 중이라면 OpenAI에 문의해 알려진 클라이언트 목록에 추가해달라고 요청하세요. 자세한 문맥은 [Codex logs reference](https://chatgpt.com/admin/api-reference#tag/Logs:-Codex)를 참조하세요.

Codex VS Code 확장에서의 예시:

```json
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
```

알림 제외 예시:

```json
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
```

Experimental API opt-in
-----------------------

일부 app-server 메서드와 필드는 `experimentalApi` 기능 뒤에 숨겨져 있습니다.

- `capabilities`를 생략하거나 `experimentalApi`를 `false`로 설정하면 안정적인 API 표면만 사용하며 서버는 실험적 메서드/필드를 거부합니다.
- `capabilities.experimentalApi`를 `true`로 설정하면 실험적 메서드 및 필드가 활성화됩니다.

```json
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
```

옵트인 없이 실험적 메서드나 필드를 보내면 app-server가 다음과 같이 거부합니다:

`<descriptor> requires experimentalApi capability`

API overview
------------

- `thread/start` - 새 thread 생성; `thread/started`를 내보내고 해당 thread의 turn/item 이벤트를 자동으로 구독합니다.
- `thread/resume` - 기존 thread를 아이디로 다시 열어 이후 `turn/start` 호출이 이어집니다.
- `thread/fork` - 저장된 히스토리를 복사해 새 thread id로 분기; 새 thread에 대해 `thread/started` 발생.
- `thread/read` - 저장된 thread를 읽되 재개하지 않음; 전체 turn 기록을 가져오려면 `includeTurns` 설정.
- `thread/list` - 저장된 thread 로그를 페이지로 탐색; 커서 기반 페이지네이션과 `modelProviders`, `sourceKinds`, `archived`, `cwd` 필터 지원.
- `thread/loaded/list` - 메모리에 로드된 thread id 나열.
- `thread/archive` - thread 로그 파일을 보관 디렉터리로 이동; 성공 시 `{}` 반환.
- `thread/unarchive` - 보관된 thread를 활성 세션 디렉터리로 복원; 복원된 `thread` 반환.
- `thread/compact/start` - thread의 대화 기록 압축 트리거; 즉시 `{}` 반환하며 진행 상황은 `turn/*`, `item/*` 알림을 통해 스트리밍.
- `thread/rollback` - 메모리 컨텍스트에서 마지막 N turn을 제거하고 롤백 마커를 영속화; 업데이트된 `thread` 반환.
- `turn/start` - thread에 사용자 입력 추가하고 Codex 생성을 시작; 초기 `turn` 응답 및 이벤트 스트리밍. `collaborationMode`에서는 `settings.developer_instructions: null`이 선택된 모드의 기본 지침 사용 의미.
- `turn/steer` - thread의 활성 진행 중인 turn에 사용자 입력 추가; 수락된 `turnId` 반환.
- `turn/interrupt` - 진행 중인 turn 취소 요청; 성공 시 `{}`이고 turn 상태는 `status: "interrupted"`.
- `review/start` - thread에서 Codex 리뷰어 시작; `enteredReviewMode` 및 `exitedReviewMode` item 발생.
- `command/exec` - thread/turn 없이 서버 샌드박스에서 단일 명령 실행.
- `model/list` - 사용 가능한 모델 나열(`includeHidden: true`로 `hidden: true` 항목 포함), effort 옵션, 선택적 `upgrade`, `inputModalities` 포함.
- `experimentalFeature/list` - 수명 주기 메타데이터와 커서 페이지네이션을 갖춘 기능 플래그 나열.
- `collaborationMode/list` - 협업 모드 프리셋 나열(실험적, 페이지네이션 없음).
- `skills/list` - 하나 이상의 `cwd`에 대해 스킬 나열(`forceReload`, 선택적 `perCwdExtraUserRoots` 지원).
- `app/list` - 접근성과 활성 상태 메타데이터와 함께 앱(커넥터) 나열, 페이지네이션 지원.
- `skills/config/write` - 경로별 스킬 활성화/비활성화.
- `mcpServer/oauth/login` - 구성된 MCP 서버 OAuth 로그인 시작; 인증 URL 반환 및 완료 시 `mcpServer/oauthLogin/completed` 발생.
- `tool/requestUserInput` - 도구 호출을 위한 1~3개의 짧은 질문 표시(실험적); 질문에는 자유 입력 옵션을 위한 `isOther` 설정 가능.
- `config/mcpServer/reload` - 디스크에서 MCP 서버 구성 재로드 및 로드된 thread에 새로고침 예약.
- `mcpServerStatus/list` - MCP 서버, 도구, 리소스, 인증 상태 나열(커서 + 제한 페이지네이션).
- `feedback/upload` - 피드백 보고서 제출(분류 + 선택적 이유/로그 + 대화 id).
- `config/read` - 구성 레이어링을 해결한 후 디스크의 유효 구성 가져오기.
- `config/value/write` - 사용자의 `config.toml`에 단일 구성 키/값 쓰기.
- `config/batchWrite` - 사용자의 `config.toml`에 구성 편집을 원자적으로 적용.
- `configRequirements/read` - `requirements.toml` 및/또는 MDM에서 요구 사항(허용 목록, 거주 요구 사항 포함) 가져오기(설정하지 않은 경우 `null`).

Models
------

### List models (`model/list`)

모델이나 페르소나 선택기를 렌더링하기 전에 `model/list`를 호출해 사용 가능한 모델과 기능을 알아보세요.

```json
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
```

각 모델 항목에는 다음을 포함할 수 있습니다:

- `reasoningEffort` - 모델이 지원하는 노력 수준 옵션입니다.
- `defaultReasoningEffort` - 클라이언트를 위한 기본 권장 노력입니다.
- `upgrade` - 클라이언트의 마이그레이션 프롬프트용 선택적 추천 업그레이드 모델 ID입니다.
- `hidden` - 모델이 기본 선택기 목록에서 숨겨져 있는지 여부입니다.
- `inputModalities` - 모델이 지원하는 입력 유형(`text`, `image` 등)입니다.
- `supportsPersonality` - `/personality`와 같은 성격별 지침을 모델이 지원하는지 여부입니다.
- `isDefault` - 모델이 추천 기본인지 여부입니다.

기본적으로 `model/list`는 선택기에 보이는 모델만 반환합니다. 전체 목록이 필요하고 클라이언트 쪽에서 `hidden` 기준으로 필터링하려면 `includeHidden: true`를 설정하세요.

`inputModalities`가 없을 경우(이전 모델 목록의 경우) 이전 호환성을 위해 `["text", "image"]`로 처리하세요.

### 실험적 기능 나열 (`experimentalFeature/list`)

이 엔드포인트를 사용하여 메타데이터와 수명 주기 단계를 포함한 기능 플래그를 확인하세요:

```json
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
```

`stage`는 `beta`, `underDevelopment`, `stable`, `deprecated`, `removed` 중 하나일 수 있습니다. 베타가 아닌 플래그의 경우 `displayName`, `description`, `announcement`이 `null`일 수 있습니다.

## Threads

- `thread/read`는 구독 없이 저장된 스레드를 읽습니다; 턴을 포함하려면 `includeTurns`를 설정하세요.
- `thread/list`는 커서 기반 페이지네이션과 `modelProviders`, `sourceKinds`, `archived`, `cwd` 필터링을 지원합니다.
- `thread/loaded/list`는 현재 메모리에 로드된 스레드 ID를 반환합니다.
- `thread/archive`는 스레드의 지속화된 JSONL 로그를 보관(archived) 디렉터리로 이동합니다.
- `thread/unarchive`는 보관된 스레드 롤아웃을 활성 세션 디렉터리로 복원합니다.
- `thread/compact/start`는 압축을 트리거하고 즉시 `{}`를 반환합니다.
- `thread/rollback`은 메모리 내 컨텍스트에서 마지막 N 턴을 삭제하고 롤백 마커를 로그에 기록합니다.

### 스레드 시작 또는 재개

새로운 Codex 대화를 시작해야 할 때는 새로운 스레드를 시작하세요.

```json
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
```

이전에 저장한 세션을 이어가려면 기록해 둔 `thread.id`로 `thread/resume`을 호출하세요. 응답 형식은 `thread/start`와 동일합니다. `personality` 등 `thread/start`에서 지원하는 동일한 설정 재정의를 전달할 수도 있습니다:

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123" } } }
```

스레드를 재개해도 `thread.updatedAt`(또는 롤아웃 파일의 수정 시간)은 자동으로 업데이트되지 않습니다. 턴을 시작할 때 타임스탬프가 갱신됩니다.

설정에서 활성화된 MCP 서버를 `required`로 표시했고 해당 서버가 초기화에 실패하면 `thread/start`와 `thread/resume`은 서버 없이 계속하기보다 실패합니다.

`thread/start`의 `dynamicTools`는 실험적 필드이며(`capabilities.experimentalApi = true` 필요) Codex는 이러한 동적 도구를 스레드 롤아웃 메타데이터에 저장하고 새 동적 도구를 제공하지 않으면 `thread/resume` 시 복원합니다.

롤아웃에 기록된 모델과 다른 모델로 재개하면 Codex 는 경고를 출력하고 다음 턴에서 한 번만 모델 전환 지침을 적용합니다.

저장된 세션에서 분기하려면 `thread/fork`에 `thread.id` 를 전달하세요. 새 스레드 ID가 생성되고 해당 스레드에 대해 `thread/started` 알림이 발생합니다:

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123" } }
{ "id": 12, "result": { "thread": { "id": "thr_456" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }
```

### 저장된 스레드 읽기 (재개하지 않음)

스레드를 재개하거나 이벤트를 구독하고 싶지 않을 때 `thread/read`를 사용하세요.

- `includeTurns` - `true`면 응답에 턴이 포함되고, `false`거나 생략하면 스레드 요약만 반환됩니다.

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "turns": [] } } }
```

`thread/resume`와 달리 `thread/read`는 스레드를 메모리에 로드하지 않으며 `thread/started`를 방출하지 않습니다.

### 페이지네이션 및 필터 포함 스레드 목록

`thread/list`는 기록 UI를 렌더링할 때 사용합니다. 결과는 기본적으로 `createdAt` 기준 최신 순입니다. 필터는 페이지네이션보다 먼저 적용됩니다. 다음 조합을 전달할 수 있습니다:

- `cursor` - 이전 응답에서 받은 불투명 문자열; 첫 페이지라면 생략하세요.
- `limit` - 서버는 설정하지 않으면 합리적인 페이지 크기를 기본값으로 둡니다.
- `sortKey` - `created_at` (기본값) 또는 `updated_at`.
- `modelProviders` - 특정 공급자로 결과를 제한합니다; 설정하지 않거나 `null` 또는 빈 배열이면 모든 공급자가 포함됩니다.
- `sourceKinds` - 특정 스레드 소스로 제한합니다. 생략하거나 `[]`이면 기본적으로 대화형 소스(`cli`, `vscode`)만 포함합니다.
- `archived` - `true`면 보관된 스레드만 나열합니다. `false`거나 생략하면 보관되지 않은 스레드(기본)가 나옵니다.
- `cwd` - 세션의 현재 작업 디렉터리가 정확히 이 경로와 일치하는 스레드로 제한합니다.

`sourceKinds`는 다음 값을 허용합니다:

- `cli`
- `vscode`
- `exec`
- `appServer`
- `subAgent`
- `subAgentReview`
- `subAgentCompact`
- `subAgentThreadSpawn`
- `subAgentOther`
- `unknown`

예시:

```json
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
```

`nextCursor`가 `null`이면 마지막 페이지에 도달한 것입니다.

### 로드된 스레드 목록

`thread/loaded/list`는 현재 메모리에 로드된 스레드 ID를 반환합니다.

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }
```

### 스레드 보관

`thread/archive`를 사용하여 디스크에 저장된 스레드 로그(JSONL 파일)를 보관된 세션 디렉터리로 이동하세요.

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
```

보관된 스레드는 `archived: true`를 전달하지 않는 한 이후 `thread/list` 호출에 나타나지 않습니다.

### 스레드 보관 해제

`thread/unarchive`를 사용하여 보관된 스레드 롤아웃을 다시 활성 세션 디렉터리로 옮기세요.

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b" } } }
```

### 스레드 압축 트리거

`thread/compact/start`로 특정 스레드의 기록 압축을 수동으로 트리거하세요. 요청은 즉시 `{}`를 반환합니다.

앱 서버는 동일한 `threadId`에서 표준 `turn/*` 및 `item/*` 알림으로 진행 상황을 전송하며, `contextCompaction` 아이템 생명주기(`item/started` → `item/completed`)도 포함됩니다.

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }
```

## Turns

`input` 필드는 다음 타입의 항목 목록을 허용합니다:

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

턴 단위로 구성 설정(모델, 노력 수준, 성격, `cwd`, 샌드박스 정책, 요약)을 재정의할 수 있습니다. 지정하면 해당 턴 이후 같은 스레드의 기본값으로 설정됩니다. `outputSchema`는 현재 턴에만 적용됩니다. `sandboxPolicy.type = "externalSandbox"`인 경우 `networkAccess`를 `restricted` 또는 `enabled`로 설정하세요; `workspaceWrite`에서는 `networkAccess`가 boolean으로 유지됩니다.

`turn/start.collaborationMode`에서 `settings.developer_instructions: null`은 모드 지침을 제거하는 대신 "선택한 모드의 기본 내장 지침을 사용"하라는 의미입니다.

### 샌드박스 읽기 액세스(`ReadOnlyAccess`)

`sandboxPolicy`는 명시적 읽기 액세스 제어를 지원합니다:

- `readOnly`: 선택적 `access`(`{ "type": "fullAccess" }`가 기본값, 또는 제한된 루트)
- `workspaceWrite`: 선택적 `readOnlyAccess`(`{ "type": "fullAccess" }`가 기본값, 또는 제한된 루트)

제한된 읽기 액세스 형식:

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}
```

예시:

```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }
```

```json
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
```

### 턴 시작

```json
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
```

### 활성 턴 조정

`turn/steer`를 사용하여 진행 중인 턴에 사용자 입력을 추가할 수 있습니다.

- `expectedTurnId`를 포함해야 하며 현재 활성 턴 ID와 일치해야 합니다.
- 해당 스레드에 활성 턴이 없으면 요청이 실패합니다.
- `turn/steer`는 새로운 `turn/started` 알림을 발생시키지 않습니다.
- `turn/steer`는 턴 수준 재정의(`model`, `cwd`, `sandboxPolicy`, `outputSchema`)를 받지 않습니다.

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }
```

### 스킬을 호출하는 턴 시작

텍스트 입력에 `$<skill-name>`을 포함하고 해당 스킬 입력 항목을 추가하여 명시적으로 스킬을 호출하세요.

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }
```

### 턴 중단

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }
```

성공하면 턴은 `status: "interrupted"`로 종료됩니다.

## Review

`review/start`는 스레드에 대해 Codex 리뷰어를 실행하고 리뷰 항목을 스트리밍합니다. 대상은 다음과 같습니다:

- `uncommittedChanges`
- `baseBranch` (브랜치와의 diff)
- `commit` (특정 커밋 리뷰)
- `custom` (자유 형식 지침)

기존 스레드에서 검토를 실행하려면 기본값인 `delivery: "inline"`을 사용하고, 새 검토 스레드를 포크하려면 `delivery: "detached"`를 사용하세요.

예시 요청/응답:

```json
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
```

분리된 검토를 하려면 `"delivery": "detached"`를 사용하세요. 응답 구조는 같지만 `reviewThreadId`는 새 검토 스레드(원래 `threadId`와 다름)의 ID가 됩니다. 서버는 그 새 스레드에 대해 검토 턴을 스트리밍하기 전에 `thread/started` 알림도 전송합니다.

Codex는 일반적인 `turn/started` 알림을 스트리밍한 다음 `enteredReviewMode` 항목이 포함된 `item/started`를 스트리밍합니다:

```json
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
```

검토가 끝나면 서버는 최종 리뷰 텍스트가 담긴 `exitedReviewMode` 항목을 포함한 `item/started`와 `item/completed`를 전송합니다:

```json
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
```

이 알림을 사용해 클라이언트에서 검토자 출력을 렌더링하세요.

## 명령 실행

`command/exec`는 스레드를 만들지 않고 서버 샌드박스에서 단일 명령(`argv` 배열)을 실행합니다.

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }
```

서버 프로세스를 이미 샌드박스로 실행 중이라면 Codex가 자체 샌드박스 적용을 건너뛰도록 `sandboxPolicy.type = "externalSandbox"`를 사용하세요. 외부 샌드박스 모드에서는 `networkAccess`를 `restricted`(기본값) 또는 `enabled`로 설정하세요. `readOnly`와 `workspaceWrite`에서는 위에 나온 것과 같은 선택적 `access` / `readOnlyAccess` 구조를 사용하세요.

참고:

- 서버는 비어 있는 `command` 배열을 거절합니다.
- `sandboxPolicy`는 `turn/start`에서 사용하는 것과 같은 형태(예: `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`)를 허용합니다.
- `timeoutMs`를 생략하면 서버 기본값이 사용됩니다.

## 이벤트

이벤트 알림은 스레드 수명 주기, 턴 수명 주기, 그리고 그 안의 항목들에 대해 서버가 시작하는 스트림입니다. 스레드를 시작하거나 다시 시작한 후에는 활성 전송 스트림에서 `thread/started`, `turn/*`, `item/*` 알림을 계속 읽으세요.

### 알림 옵트아웃

클라이언트는 `initialize.params.capabilities.optOutNotificationMethods`에 정확한 메서드 이름을 보내 특정 알림을 연결별로 억제할 수 있습니다.

- 정확히 일치하는 경우만: `item/agentMessage/delta`는 그 메서드만 억제합니다.
- 알 수 없는 메서드 이름은 무시됩니다.
- 구식(`codex/event/*`)과 v2(`thread/*`, `turn/*`, `item/*` 등) 알림 모두에 적용됩니다.
- 요청, 응답, 오류에는 적용되지 않습니다.

### 퍼지 파일 검색 이벤트(실험적)

퍼지 파일 검색 세션 API는 쿼리별 알림을 내보냅니다:

- `fuzzyFileSearch/sessionUpdated` - 활성 쿼리에 대한 현재 매치를 담은 `{ sessionId, query, files }`.
- `fuzzyFileSearch/sessionCompleted` - 해당 쿼리의 인덱싱과 매칭이 완료되면 `{ sessionId }`.

### 턴 이벤트

- `turn/started` - 턴 ID, 빈 `items`, `status: "inProgress"`을 포함한 `{ turn }`.
- `turn/completed` - `turn.status`가 `completed`, `interrupted`, 또는 `failed`인 `{ turn }`. 실패한 경우 `{ error: { message, codexErrorInfo?, additionalDetails? } }`를 포함합니다.
- `turn/diff/updated` - 턴 내 모든 파일 변경에 대한 최신 통합 diff를 담은 `{ threadId, turnId, diff }`.
- `turn/plan/updated` - 에이전트가 계획을 공유하거나 변경할 때마다 `{ turnId, explanation?, plan }`. 각 `plan` 항목은 `status`가 `pending`, `inProgress`, 또는 `completed`인 `{ step, status }`입니다.
- `thread/tokenUsage/updated` - 활성 스레드의 사용량 업데이트.

`turn/diff/updated`와 `turn/plan/updated`는 항목 이벤트가 스트리밍될 때도 현재 빈 `items` 배열을 포함합니다. 턴 항목의 진실 소스로 `item/*` 알림을 사용하세요.

### 항목

`ThreadItem`은 턴 응답과 `item/*` 알림에서 전달되는 태그형 공용체입니다. 흔한 항목 유형은 다음과 같습니다:

- `userMessage` - `content`가 사용자 입력(`text`, `image`, 또는 `localImage`) 목록인 `{id, content}`.
- `agentMessage` - 누적된 에이전트 응답이 담긴 `{id, text}`.
- `plan` - 계획 모드에서 제안된 계획 텍스트가 들어 있는 `{id, text}`. `item/completed`의 최종 `plan` 항목을 권위 있는 것으로 취급하세요.
- `reasoning` - `summary`에 스트리밍된 추론 요약, `content`에 원시 추론 블록을 담은 `{id, summary, content}`.
- `commandExecution` - `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`.
- `fileChange` - 제안된 편집을 설명하는 `{id, changes, status}`; `changes`는 `{path, kind, diff}` 목록입니다.
- `mcpToolCall` - `{id, server, tool, status, arguments, result?, error?}`.
- `collabToolCall` - `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`.
- `webSearch` - 에이전트가 발행한 웹 검색 요청을 위한 `{id, query, action?}`.
- `imageView` - 에이전트가 이미지 뷰어 도구를 호출할 때 전송되는 `{id, path}`.
- `enteredReviewMode` - 리뷰어가 시작할 때 전송되는 `{id, review}`.
- `exitedReviewMode` - 리뷰어가 종료할 때 전송되는 `{id, review}`.
- `contextCompaction` - Codex가 대화 히스토리를 압축할 때 전송되는 `{id}`.

`webSearch.action`에서 액션 `type`은 `search`(`query?`, `queries?`), `openPage`(`url?`), 또는 `findInPage`(`url?`, `pattern?`)일 수 있습니다.

앱 서버는 구식 `thread/compacted` 알림을 더 이상 권장하지 않습니다; 대신 `contextCompaction` 항목을 사용하세요.

모든 항목은 두 가지 공통 수명 주기 이벤트를 발생시킵니다:

- `item/started` - 새로운 작업 단위가 시작될 때 전체 `item`을 전송합니다; `item.id`는 델타에서 사용하는 `itemId`와 일치합니다.
- `item/completed` - 작업이 끝나면 최종 `item`을 전송합니다; 이를 권위 있는 상태로 취급하세요.

### 항목 델타

- `item/agentMessage/delta` - 에이전트 메시지를 위한 스트리밍 텍스트를 덧붙입니다.
- `item/plan/delta` - 제안된 계획 텍스트를 스트리밍합니다. 최종 `plan` 항목은 연결된 델타와 정확히 같지 않을 수 있습니다.
- `item/reasoning/summaryTextDelta` - 읽을 수 있는 추론 요약을 스트리밍합니다; 새 요약 섹션이 열리면 `summaryIndex`가 증가합니다.
- `item/reasoning/summaryPartAdded` - 추론 요약 섹션 사이의 경계를 표시합니다.
- `item/reasoning/textDelta` - 원시 추론 텍스트를 스트리밍합니다(모델에서 지원하는 경우).
- `item/commandExecution/outputDelta` - 명령의 stdout/stderr를 스트리밍합니다; 델타를 순서대로 이어붙이세요.
- `item/fileChange/outputDelta` - 기본 `apply_patch` 도구 호출의 툴 응답을 포함합니다.

## 오류

턴이 실패하면 서버는 `{ error: { message, codexErrorInfo?, additionalDetails? } }`를 포함한 `error` 이벤트를 전송한 뒤 `status: "failed"`로 턴을 종료합니다. 업스트림 HTTP 상태 코드가 있을 경우 `codexErrorInfo.httpStatusCode`에 나타납니다.

일반적인 `codexErrorInfo` 값은 다음과 같습니다:

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed`
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`
- `Unauthorized`
- `SandboxError`
- `InternalServerError`
- `Other`

업스트림 HTTP 상태가 있을 경우 서버는 해당 `codexErrorInfo` 변형의 `httpStatusCode`에 전달합니다.

## 승인

사용자의 Codex 설정에 따라 명령 실행과 파일 변경은 승인을 필요로 할 수 있습니다. 앱 서버는 클라이언트에 서버가 시작한 JSON-RPC 요청을 보내고, 클라이언트는 결정 페이로드로 응답합니다.

- 명령 실행 결정: `accept`, `acceptForSession`, `decline`, `cancel`, 또는 `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`.
- 파일 변경 결정: `accept`, `acceptForSession`, `decline`, `cancel`.

- 요청에는 `threadId`와 `turnId`가 포함되므로 현재 대화에 UI 상태를 적용하세요.
- 서버는 작업을 계속하거나 거절하고 항목을 `item/completed`로 종료합니다.

### 명령 실행 승인

메시지 순서:

1. `item/started`는 `commandExecution` 항목(진행 중)의 `command`, `cwd` 등을 보여줍니다.
2. `item/commandExecution/requestApproval`은 `itemId`, `threadId`, `turnId`, 선택적 `reason`, 선택적 `command`, 선택적 `cwd`, 선택적 `commandActions`, 선택적 `proposedExecpolicyAmendment`을 포함합니다.
3. 클라이언트는 위의 명령 실행 승인 결정 중 하나로 응답합니다.
4. `item/completed`는 `status: completed | failed | declined`인 최종 `commandExecution` 항목을 반환합니다.

### 파일 변경 승인

메시지 순서:

1. `item/started`는 제안된 `changes`와 `status: "inProgress"`를 포함한 `fileChange` 항목을 보냅니다.
2. `item/fileChange/requestApproval`은 `itemId`, `threadId`, `turnId`, 선택적 `reason`, 선택적 `grantRoot`를 포함합니다.
3. 클라이언트는 위의 파일 변경 승인 결정 중 하나로 응답합니다.
4. `item/completed`는 `status: completed | failed | declined`인 최종 `fileChange` 항목을 반환합니다.

### MCP 도구 호출 승인(앱)

앱(커넥터) 도구 호출도 승인을 요구할 수 있습니다. 앱 도구 호출에 부작용이 있는 경우 서버는 `tool/requestUserInput`과 **Accept**, **Decline**, **Cancel** 같은 옵션을 포함한 요청을 보낼 수 있습니다. 사용자가 거절하거나 취소하면 관련 `mcpToolCall` 항목은 에러와 함께 완료되어 도구가 실행되지 않습니다.

## 스킬

사용자 텍스트 입력에 `$<skill-name>`을 포함하면 스킬을 호출합니다. `skill` 입력 항목을 추가하면 서버가 전체 스킬 지침을 삽입하므로 모델이 이름을 찾는 것보다 지연이 적습니다.

```json
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
```

`skill` 항목을 생략해도 모델은 `$<skill-name>` 마커를 분석하여 스킬을 찾으려 하지만 지연이 생길 수 있습니다.

예시:

```
$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.
```

사용 가능한 스킬을 가져오려면 `skills/list`를 사용하세요(선택적으로 `cwds`로 범위 지정, `forceReload`). `perCwdExtraUserRoots`를 포함하면 특정 `cwd` 값에 대해 추가 절대 경로를 `user` 범위로 스캔할 수 있습니다. 앱 서버는 `cwds`에 없는 `cwd` 항목을 무시합니다. `skills/list`는 `cwd`별로 캐시된 결과를 재사용할 수 있으므로 디스크에서 새로 고치려면 `forceReload: true`를 설정하세요. 존재하는 경우 서버는 `SKILL.json`에서 `interface`와 `dependencies`를 읽습니다.

```json
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
```

경로별 스킬 활성화/비활성화:

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}
```

## 앱(커넥터)

사용 가능한 앱을 가져오려면 `app/list`를 사용하세요. CLI/TUI에서는 `/apps`가 사용자용 선택기이며, 커스텀 클라이언트라면 `app/list`를 직접 호출합니다. 각 항목은 `isAccessible`(사용자 접근 가능 여부)과 `isEnabled`(`config.toml`에 활성화된 상태) 모두를 포함하여 클라이언트가 설치/접근과 로컬 활성화 상태를 구별할 수 있도록 합니다.

```json
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
```

`threadId`를 제공하면 앱 기능 게이팅(`features.apps`)이 해당 스레드의 설정 스냅샷을 사용합니다. 생략하면 앱 서버가 최신 글로벌 설정을 사용합니다.

`app/list`는 접근 가능한 앱과 디렉터리 앱이 모두 로드된 후에 응답합니다. `forceRefetch: true`를 설정하면 앱 캐시를 우회하여 새 데이터를 가져옵니다. 캐시 항목은 새로 고침이 성공했을 때만 교체됩니다.

서버는 접근 가능한 앱 또는 디렉터리 앱 중 어느 쪽이든 로드가 끝날 때마다 `app/list/updated` 알림을 내보냅니다. 각 알림에는 최신 병합된 앱 목록이 포함됩니다.

```json
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
```

텍스트 입력에 `$<app-slug>`를 넣고 `app://<id>` 경로를 가진 `mention` 입력 항목을 추가하면 앱을 호출할 수 있습니다(권장).

```json
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
```

## 인증 엔드포인트

JSON-RPC auth/account 표면은 요청/응답 메서드와 서버가 시작하는 알림( `id` 없음)을 공개합니다. 이를 사용해 인증 상태를 확인하고 로그인 시작 또는 취소, 로그아웃, ChatGPT 속도 제한 검사 등을 수행합니다.

### 인증 모드

Codex는 세 가지 인증 모드를 지원합니다. `account/updated.authMode`에서 활성 모드를 표시하고, `account/read`에서도 이를 보고합니다.

- **API 키(`apikey`)** - 호출자가 OpenAI API 키를 제공하고 Codex가 이를 API 요청용으로 저장합니다.
- **ChatGPT 관리(`chatgpt`)** - Codex가 ChatGPT OAuth 흐름을 소유하고 토큰을 유지하며 자동으로 갱신합니다.
- **ChatGPT 외부 토큰(`chatgptAuthTokens`)** - 호스트 앱이 `idToken`과 `accessToken`을 직접 제공하는 경우입니다. Codex는 이 토큰을 메모리에 저장하며, 갱신 요청 시 호스트 앱이 직접 갱신해야 합니다.

### API 개요

- `account/read` - 현재 계정 정보를 가져옵니다; 선택적으로 토큰을 갱신합니다.
- `account/login/start` - 로그인 시작 (`apiKey`, `chatgpt`, 또는 `chatgptAuthTokens`).
- `account/login/completed` (알림) - 로그인 시도가 완료되면 (성공 또는 오류) 전송됩니다.
- `account/login/cancel` - `loginId`로 대기 중인 ChatGPT 로그인을 취소합니다.
- `account/logout` - 로그아웃; `account/updated`를 트리거합니다.
- `account/updated` (알림) - 인증 모드가 변경될 때마다 전송(`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, 또는 `null`).
- `account/chatgptAuthTokens/refresh` (서버 요청) - 권한 오류 발생 후 외부 관리 ChatGPT 토큰 갱신 요청.
- `account/rateLimits/read` - ChatGPT 속도 제한 가져오기.
- `account/rateLimits/updated` (알림) - 사용자의 ChatGPT 속도 제한 변경 시 전송.
- `mcpServer/oauthLogin/completed` (알림) - `mcpServer/oauth/login` 흐름이 끝난 후 전송; 페이로드는 `{ name, success, error? }`.

### 1) 인증 상태 확인

요청:

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }
```

응답 예시:

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }
```

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }
```

```json
{
  "id": 1,
  "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
}
```

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "chatgpt",
      "email": "user@example.com",
      "planType": "pro"
    },
    "requiresOpenaiAuth": true
  }
}
```

필드 설명:

- `refreshToken` (불리언): 관리형 ChatGPT 모드에서 토큰을 강제로 갱신하려면 `true`로 설정합니다. 외부 토큰 모드(`chatgptAuthTokens`)에서는 앱 서버가 이 플래그를 무시합니다.
- `requiresOpenaiAuth`: 활성 공급자를 반영합니다. `false`면 Codex가 OpenAI 자격 증명 없이 실행할 수 있습니다.

### 2) API 키로 로그인

1. 전송:

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }
   ```

2. 기대 응답:

   ```json
   { "id": 2, "result": { "type": "apiKey" } }
   ```

3. 알림:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }
   ```

   ```json
   { "method": "account/updated", "params": { "authMode": "apikey" } }
   ```

### 3) ChatGPT로 로그인 (브라우저 흐름)

1. 시작:

   ```json
   { "method": "account/login/start", "id": 3, "params": { "type": "chatgpt" } }
   ```

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }
   ```

2. 브라우저에서 `authUrl`을 열면 앱 서버가 로컬 콜백을 호스팅합니다.
3. 다음 알림을 기다립니다:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }
   ```

   ```json
   { "method": "account/updated", "params": { "authMode": "chatgpt" } }
   ```

### 3b) 외부에서 관리하는 ChatGPT 토큰으로 로그인 (`chatgptAuthTokens`)

이 모드는 호스트 애플리케이션이 사용자의 ChatGPT 인증 수명 주기를 소유하고 토큰을 직접 제공할 때 씁니다.

1. 전송:

   ```json
   {
     "method": "account/login/start",
     "id": 7,
     "params": {
       "type": "chatgptAuthTokens",
       "idToken": "<jwt>",
       "accessToken": "<jwt>"
     }
   }
   ```

2. 기대 응답:

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }
   ```

3. 알림:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }
   ```

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgptAuthTokens" }
   }
   ```

서버가 `401 Unauthorized`를 받으면 다음과 같이 호스트 앱에 토큰 갱신을 요청할 수 있습니다:

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "idToken": "<jwt>", "accessToken": "<jwt>" } }
```

서버는 갱신 응답 후 원래 요청을 다시 시도합니다. 요청은 약 10초 후 타임아웃됩니다.

### 4) ChatGPT 로그인 취소

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }
```

### 5) 로그아웃

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null } }
```

### 6) 속도 제한 (ChatGPT)

```json
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
```

필드 설명:

- `rateLimits`는 이전과 호환되는 단일 버킷 뷰입니다.
- `rateLimitsByLimitId`(존재하는 경우)는 측정된 `limit_id`(예: `codex`)로 키가 지정된 다중 버킷 뷰입니다.
- `limitId`는 측정된 버킷 식별자입니다.
- `limitName`은 버킷에 대한 선택적 사용자용 라벨입니다.
- `usedPercent`는 쿼터 창 내 현재 사용량입니다.
- `windowDurationMins`은 쿼터 창 길이입니다.
- `resetsAt`은 다음 초기화 시점을 나타내는 Unix 타임스탬프(초)입니다.

