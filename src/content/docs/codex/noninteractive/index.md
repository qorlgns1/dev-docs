---
title: '비대화형 모드'
description: '비대화형 모드를 사용하면 대화형 TUI를 열지 않고도 스크립트(예: 지속적 통합(CI) 작업)에서 Codex를 실행할 수 있습니다.'
---

Source URL: https://developers.openai.com/codex/noninteractive

# 비대화형 모드

비대화형 모드를 사용하면 대화형 TUI를 열지 않고도 스크립트(예: 지속적 통합(CI) 작업)에서 Codex를 실행할 수 있습니다.
`codex exec`로 호출합니다.

플래그 수준의 세부 정보는 [`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec)를 참조하세요.

## `codex exec`을 사용해야 할 때

Codex가 다음을 수행하도록 하려면 `codex exec`을 사용하세요:

- 파이프라인(CI, 병합 전 검사, 예약 작업)의 일부로 실행할 때.
- 다른 도구로 파이프라인하거나 파이프 입력이 가능한 출력(예: 릴리스 노트 또는 요약 생성)을 만들 때.
- 명시적인 미리 설정된 샌드박스 및 승인 설정으로 실행할 때.

## 기본 사용법

작업 프롬프트를 단일 인수로 전달하세요:

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"
```

`codex exec`이 실행되는 동안 Codex는 진행 상황을 `stderr`에 스트리밍하고 최종 에이전트 메시지만 `stdout`에 출력합니다. 이렇게 하면 최종 결과를 리디렉션하거나 파이프로 전달하기가 쉽습니다:

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md
```

세션 롤아웃 파일을 디스크에 유지하고 싶지 않을 때는 `--ephemeral`을 사용하세요:

```bash
codex exec --ephemeral "triage this repository and suggest next steps"
```

## 권한 및 안전

기본적으로 `codex exec`은 읽기 전용 샌드박스에서 실행됩니다. 자동화에서는 워크플로에 필요한 최소 권한만 설정하세요:

- 편집 허용: `codex exec --full-auto "<task>"`
- 더 넓은 액세스 허용: `codex exec --sandbox danger-full-access "<task>"`

`danger-full-access`는 제어된 환경(예: 격리된 CI 러너나 컨테이너)에서만 사용하세요.

`required = true`로 설정된 활성화된 MCP 서버를 구성하였는데 초기화에 실패하면 `codex exec`은 계속 실행하지 않고 오류로 종료됩니다.

## 출력 기계 판독 가능하게 만들기

Codex 출력을 스크립트에서 사용하려면 JSON Lines 출력을 사용하세요:

```bash
codex exec --json "summarize the repo structure" | jq
```

`--json`을 활성화하면 `stdout`이 JSON Lines(JSONL) 스트림이 되어 실행 중 Codex가 방출하는 모든 이벤트를 캡처할 수 있습니다. 이벤트 유형에는 `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*`, `error`가 포함됩니다.

항목 유형에는 에이전트 메시지, 추론, 명령 실행, 파일 변경, MCP 도구 호출, 웹 검색, 플랜 업데이트가 포함됩니다.

샘플 JSON 스트림(각 줄은 JSON 객체):

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122}}
```

최종 메시지만 필요하다면 `-o <path>`/`--output-last-message <path>`로 파일에 작성하세요. 이렇게 하면 최종 메시지가 파일에 쓰이고 여전히 `stdout`에도 출력됩니다([`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec) 참조).

## 스키마로 구조화된 출력 생성

하류 단계에서 구조화된 데이터가 필요하다면 `--output-schema`를 사용하여 JSON Schema를 준수하는 최종 응답을 요청하세요.
이는 안정적인 필드가 필요한 자동화된 워크플로(예: 작업 요약, 위험 보고서, 릴리스 메타데이터)에 유용합니다.

`schema.json`

```json
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
```

스키마와 함께 Codex를 실행하고 최종 JSON 응답을 디스크에 작성하세요:

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json
```

예시 최종 출력(`stdout`):

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}
```

## CI에서 인증

`codex exec`은 기본적으로 저장된 CLI 인증을 재사용합니다. CI에서는 일반적으로 자격 증명을 명시적으로 제공합니다:

- 작업의 비밀 환경 변수로 `CODEX_API_KEY`를 설정하세요.
- 프롬프트와 도구 출력에는 민감한 코드나 데이터가 포함될 수 있다는 점을 기억하세요.

단일 실행에 다른 API 키를 사용하려면 인라인으로 `CODEX_API_KEY`를 설정하세요:

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"
```

`CODEX_API_KEY`는 `codex exec`에서만 지원됩니다.

## 비대화형 세션 재개

이전 실행(예: 2단계 파이프라인)을 계속해야 할 때는 `resume` 하위 명령을 사용하세요:

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"
```

특정 세션 ID를 지정하려면 `codex exec resume <SESSION_ID>`를 사용하세요.

## Git 저장소 필요

Codex는 파괴적 변경을 방지하기 위해 Git 저장소 내에서 명령을 실행해야 합니다. 환경이 안전하다고 확신한다면 `codex exec --skip-git-repo-check`로 이 확인을 무시할 수 있습니다.

## 일반 자동화 패턴

### 예시: GitHub Actions에서 CI 실패 자동 수정

CI 워크플로가 실패할 때 Codex를 사용하여 자동으로 수정을 제안할 수 있습니다. 일반적인 패턴은 다음과 같습니다:

1. 기본 CI 워크플로가 오류로 완료되면 후속 워크플로를 트리거합니다.
2. 실패한 커밋 SHA를 체크아웃합니다.
3. 의존성을 설치하고 좁은 프롬프트와 최소 권한으로 Codex를 실행합니다.
4. 테스트 명령을 다시 실행합니다.
5. 결과 패치를 포함한 풀 리퀘스트를 엽니다.

#### Codex CLI를 사용하는 최소 워크플로

아래 예시는 핵심 단계만 보여줍니다. 설치 및 테스트 명령은 스택에 맞게 조정하세요.

```yaml
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
```

#### 대안: Codex GitHub Action 사용

CLI 설치를 피하려면 [Codex GitHub Action](https://developers.openai.com/codex/github-action)을 통해 `codex exec`를 실행하고 프롬프트를 입력으로 전달할 수 있습니다.
