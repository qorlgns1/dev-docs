---
title: 비대화형 모드
description: "비대화형 모드를 사용하면 인터랙티브 TUI를 열지 않고도 스크립트(예: CI 작업)에서 Codex를 실행할 수 있습니다. 으로 호출합니다."
sidebar:
  order: 50
---

# 비대화형 모드

Source URL: https://developers.openai.com/codex/noninteractive

비대화형 모드를 사용하면 인터랙티브 TUI를 열지 않고도 스크립트(예: CI 작업)에서 Codex를 실행할 수 있습니다. `codex exec`으로 호출합니다.

세부 플래그 설명은 [`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec)을 참고하세요.

## `codex exec`을 사용할 때

다음과 같은 경우 `codex exec`을 사용하세요.

  * 파이프라인(CI, 프리머지 검사, 예약 작업) 일부로 Codex를 실행해야 할 때.
  * 다른 도구로 파이프하여 활용할 수 있는 출력을 만들어야 할 때(예: 릴리스 노트나 요약 생성).
  * 미리 설정한 샌드박스 및 승인 구성을 명시적으로 적용해야 할 때.

## 기본 사용법

작업 프롬프트를 하나의 인수로 전달합니다:
[code] 
    codex exec "summarize the repository structure and list the top 5 risky areas"
[/code]

`codex exec`가 실행되는 동안 Codex는 진행 상황을 `stderr`로 스트리밍하고 최종 에이전트 메시지만 `stdout`에 출력합니다. 따라서 최종 결과를 리디렉션하거나 파이프 처리하기가 쉽습니다:
[code] 
    codex exec "generate release notes for the last 10 commits" | tee release-notes.md
[/code]

세션 rollout 파일을 디스크에 남기고 싶지 않다면 `--ephemeral`을 사용하세요:
[code] 
    codex exec --ephemeral "triage this repository and suggest next steps"
[/code]

## 권한 및 안전성

기본적으로 `codex exec`는 읽기 전용 샌드박스에서 실행됩니다. 자동화 환경에서는 워크플로에 필요한 최소 권한만 설정하세요.

  * 편집 허용: `codex exec --full-auto "<task>"`
  * 더 넓은 접근 허용: `codex exec --sandbox danger-full-access "<task>"`

`danger-full-access`는 격리된 CI 러너나 컨테이너처럼 통제된 환경에서만 사용하세요.

`required = true`로 설정된 MCP 서버가 활성화되었는데 초기화에 실패하면, `codex exec`는 해당 서버 없이 계속 진행하지 않고 오류로 종료합니다.

## 출력물을 기계가 읽을 수 있도록 만들기

스크립트에서 Codex 출력물을 처리하려면 JSON Lines 출력을 사용하세요:
[code] 
    codex exec --json "summarize the repo structure" | jq
[/code]

`--json`을 활성화하면 `stdout`이 JSON Lines(JSONL) 스트림이 되어 Codex가 실행 중에 내보내는 모든 이벤트를 캡처할 수 있습니다. 이벤트 유형에는 `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*`, `error`가 포함됩니다.

아이템 유형에는 에이전트 메시지, 추론, 명령 실행, 파일 변경, MCP 도구 호출, 웹 검색, 플랜 업데이트가 포함됩니다.

샘플 JSON 스트림(각 줄이 JSON 객체):
[code] 
    {"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
    {"type":"turn.started"}
    {"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
    {"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
    {"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122}}
[/code]

최종 메시지만 필요하다면 `-o <path>`/`--output-last-message <path>`로 파일에 기록하세요. 이 옵션은 최종 메시지를 파일에 쓰면서도 `stdout`에는 계속 출력합니다(자세한 내용은 [`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec) 참조).

## 스키마로 구조화된 출력 만들기

후속 단계에서 구조화된 데이터가 필요하다면 `--output-schema`를 사용하여 JSON Schema를 만족하는 최종 응답을 요청하세요. 이는 작업 요약, 위험 보고서, 릴리스 메타데이터처럼 안정적인 필드가 필요한 자동화 워크플로에 유용합니다.

`schema.json`
[code] 
    {
      "type": "object",
      "properties": {
        "project_name": { "type": "string" },
        "programming_languages": {
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["project_name", "programming_languages"],
      "additionalProperties": false
    }
[/code]

스키마와 함께 Codex를 실행하고 최종 JSON 응답을 디스크에 기록하세요:
[code] 
    codex exec "Extract project metadata" \
[/code]

--output-schema ./schema.json \
      -o ./project-metadata.json
[/code]

예시 최종 출력(stdout):
[code] 
    {
      "project_name": "Codex CLI",
      "programming_languages": ["Rust", "TypeScript", "Shell"]
    }
[/code]

## CI에서 인증하기

`codex exec`은 기본적으로 저장된 CLI 인증을 재사용합니다. CI에서는 자격 증명을 명시적으로 제공하는 경우가 많습니다.

  * 작업용 비밀 환경 변수로 `CODEX_API_KEY`를 설정하세요.
  * 프롬프트와 도구 출력을 유념하세요. 민감한 코드나 데이터가 포함될 수 있습니다.

단일 실행에서 다른 API 키를 사용하려면 `CODEX_API_KEY`를 인라인으로 설정하세요:
[code] 
    CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"
[/code]

`CODEX_API_KEY`는 `codex exec`에서만 지원됩니다.

## 비대화형 세션 다시 이어가기

이전 실행(예: 2단계 파이프라인)을 계속해야 한다면 `resume` 하위 명령을 사용하세요:
[code] 
    codex exec "review the change for race conditions"
    codex exec resume --last "fix the race conditions you found"
[/code]

`codex exec resume <SESSION_ID>`로 특정 세션 ID를 지정할 수도 있습니다.

## Git 저장소 필요

Codex는 파괴적인 변경을 방지하기 위해 Git 저장소 안에서 명령을 실행해야 합니다. 환경이 안전하다고 확신한다면 `codex exec --skip-git-repo-check`로 이 검사를 건너뛰세요.

## 일반적인 자동화 패턴

### 예시: GitHub Actions에서 CI 실패 자동 수정

CI 워크플로우가 실패했을 때 `codex exec`으로 자동 수정 제안을 만들 수 있습니다. 일반적인 패턴은 다음과 같습니다.

  1. 기본 CI 워크플로우가 오류로 완료되면 후속 워크플로우를 트리거합니다.
  2. 실패한 커밋 SHA를 체크아웃합니다.
  3. 종속성을 설치하고 제한된 프롬프트와 최소 권한으로 Codex를 실행합니다.
  4. 테스트 명령을 다시 실행합니다.
  5. 생성된 패치로 풀 리퀘스트를 엽니다.

#### Codex CLI를 사용하는 최소 워크플로우

아래 예시는 핵심 단계를 보여줍니다. 스택에 맞게 설치 및 테스트 명령을 조정하세요.
[code] 
    name: Codex auto-fix on CI failure
    
    on:
      workflow_run:
        workflows: ["CI"]
        types: [completed]
    
    permissions:
      contents: write
      pull-requests: write
    
    jobs:
      auto-fix:
        if: ${{ github.event.workflow_run.conclusion == 'failure' }}
        runs-on: ubuntu-latest
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
        steps:
          - uses: actions/checkout@v4
            with:
              ref: ${{ env.FAILED_HEAD_SHA }}
              fetch-depth: 0
    
          - uses: actions/setup-node@v4
            with:
              node-version: "20"
    
          - name: Install dependencies
            run: |
              if [ -f package-lock.json ]; then npm ci; else npm i; fi
    
          - name: Install Codex
            run: npm i -g @openai/codex
    
          - name: Authenticate Codex
            run: codex login --api-key "$OPENAI_API_KEY"
    
          - name: Run Codex
            run: |
              codex exec --full-auto --sandbox workspace-write \
                "Read the repository, run the test suite, identify the minimal change needed to make all tests pass, implement only that change, and stop. Do not refactor unrelated files."
    
          - name: Verify tests
            run: npm test --silent
    
          - name: Create pull request
            if: success()
            uses: peter-evans/create-pull-request@v6
            with:
              branch: codex/auto-fix-${{ github.event.workflow_run.run_id }}
              base: ${{ env.FAILED_HEAD_BRANCH }}
              title: "Auto-fix failing CI via Codex"
[/code]

#### 대안: Codex GitHub Action 사용

CLI를 직접 설치하지 않으려면 [Codex GitHub Action](https://developers.openai.com/codex/github-action)에서 `codex exec`을 실행하고 프롬프트를 입력 값으로 전달할 수 있습니다.
