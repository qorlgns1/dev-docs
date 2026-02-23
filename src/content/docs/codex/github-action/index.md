---
title: 'Codex GitHub Action'
description: 'Codex GitHub Action()을 사용하여 CI/CD 작업에서 Codex를 실행하거나, 패치를 적용하거나, GitHub Actions 워크플로우에서 리뷰를 게시하세요. 이 액션은 Codex CLI를 설치하고 API 키를 제공하면 Responses API 프록시를...'
---

Source URL: https://developers.openai.com/codex/github-action

# Codex GitHub Action

Codex GitHub Action(`openai/codex-action@v1`)을 사용하여 CI/CD 작업에서 Codex를 실행하거나, 패치를 적용하거나, GitHub Actions 워크플로우에서 리뷰를 게시하세요. 이 액션은 Codex CLI를 설치하고 API 키를 제공하면 Responses API 프록시를 시작하며, 지정한 권한으로 `codex exec`을 실행합니다.

다음과 같은 경우 이 액션을 사용하세요:

- CLI를 직접 관리하지 않고도 풀 리퀘스트나 릴리스에 대해 Codex 피드백을 자동화하려는 경우.
- Codex 기반의 품질 검사를 CI 파이프라인 중 변경 검증 조건으로 두려는 경우.
- 워크플로우 파일에서 반복 가능한 Codex 작업(코드 리뷰, 릴리스 준비, 마이그레이션)을 실행하려는 경우.

CI 예시는 [Non-interactive mode](https://developers.openai.com/codex/noninteractive)를 참고하고, [openai/codex-action 저장소](https://github.com/openai/codex-action)에서 소스를 확인하세요.

## 요구 사항

- OpenAI 키를 GitHub 시크릿(예: `OPENAI_API_KEY`)으로 저장하고 워크플로우에서 참조하세요.
- 작업을 Linux 또는 macOS 러너에서 실행하세요. Windows의 경우 `safety-strategy: unsafe`를 설정하세요.
- Codex가 리포지토리 내용을 읽을 수 있도록 액션 호출 전에 코드를 체크아웃하세요.
- 실행할 프롬프트를 결정하세요. `prompt`로 인라인 텍스트를 제공하거나, 커밋된 파일을 `prompt-file`로 지정할 수 있습니다.

## 예시 워크플로우

다음 샘플 워크플로우는 새 풀 리퀘스트를 리뷰하고 Codex의 응답을 캡처하여 PR에 다시 게시합니다.

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge

      - name: Pre-fetch base and head refs
        run: |
          git fetch --no-tags origin \
            ${{ github.event.pull_request.base.ref }} \
            +refs/pull/${{ github.event.pull_request.number }}/head

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md
          safety-strategy: drop-sudo
          sandbox: workspace-write

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}
```

`.github/codex/prompts/review.md`를 자체 프롬프트 파일로 교체하거나 인라인 텍스트에 `prompt` 입력을 사용하세요. 예시는 최종 Codex 메시지를 `codex-output.md`에 기록하여 이후에 검토하거나 아티팩트로 업로드할 수 있게 합니다.

## `codex exec` 구성

다음 `codex exec` 옵션에 대응하는 액션 입력을 설정하여 Codex 실행을 조정하세요:

- `prompt` 또는 `prompt-file`(하나 선택): 작업을 설명하는 인라인 지시문 또는 리포지토리 내 Markdown/텍스트 경로입니다. `.github/codex/prompts/`에 프롬프트를 저장하는 것을 고려하세요.
- `codex-args`: 추가 CLI 플래그. JSON 배열(예: `["--full-auto"]`) 또는 쉘 문자열(`--full-auto --sandbox danger-full-access`)을 제공하여 편집, 스트리밍, MCP 설정을 허용하세요.
- `model` 및 `effort`: 원하는 Codex 에이전트 구성을 선택하세요. 기본값을 사용하려면 비워두세요.
- `sandbox`: 실행 중 Codex가 필요로 하는 권한에 맞춰 샌드박스 모드(`workspace-write`, `read-only`, `danger-full-access`)를 설정하세요.
- `output-file`: 최종 Codex 메시지를 디스크에 저장하여 이후 단계에서 업로드하거나 diff할 수 있습니다.
- `codex-version`: 특정 CLI 릴리스를 고정할 수 있습니다. 최신 릴리스를 사용하려면 비워두세요.
- `codex-home`: 여러 단계에서 구성 파일이나 MCP 설정을 재사용하려면 공유 Codex 홈 디렉터리를 지정하세요.

## 권한 관리

Codex는 제한하지 않으면 GitHub 호스팅 러너에서 넓은 접근권을 갖습니다. 다음 입력으로 노출을 제어하세요:

- `safety-strategy`(기본 `drop-sudo`): Codex 실행 전에 `sudo`를 제거합니다. 이 설정은 작업 내에서 되돌릴 수 없으며 메모리 내 시크릿을 보호합니다. Windows에서는 반드시 `safety-strategy: unsafe`를 설정해야 합니다.
- `unprivileged-user`: `safety-strategy: unprivileged-user`와 `codex-user`를 함께 사용하여 특정 계정으로 Codex를 실행합니다. 사용자가 리포지토리 체크아웃에 읽기/쓰기 가능한지 확인하세요(`.cache/codex-action/examples/unprivileged-user.yml`에서 소유권 수정 예시 확인).
- `read-only`: Codex가 파일을 변경하거나 네트워크를 사용할 수 없도록 하지만 여전히 높은 권한으로 실행됩니다. 시크릿 보호를 위해 이를 단독으로 신뢰하지 마세요.
- `sandbox`: Codex 자체의 파일시스템 및 네트워크 접근을 제한합니다. 작업을 완료할 수 있으면서도 가장 좁은 옵션을 선택하세요.
- `allow-users` 및 `allow-bots`: 워크플로우를 트리거할 수 있는 주체를 제한합니다. 기본적으로 쓰기 권한이 있는 사용자만 액션을 실행할 수 있으며, 추가 신뢰 계정을 명시하거나 기본 동작을 유지하려면 필드를 비워두세요.

## 출력 캡처

액션은 `final-message` 출력으로 마지막 Codex 메시지를 제공합니다. 이를 작업 출력에 매핑하거나 이후 단계에서 직접 처리하세요. 전체 대본을 수집하려면 `output-file`과 업로드된 아티팩트 기능을 함께 사용하세요. 구조화된 데이터가 필요할 경우 `codex-args`에 `--output-schema`를 전달하여 JSON 형태를 강제하세요.

## 보안 체크리스트

- 누가 워크플로우를 시작할 수 있는지 제한하세요. 모든 사람이 리포지토리에 대해 Codex를 실행하도록 허용하기보다는 신뢰할 수 있는 이벤트나 명시적 승인을 우선하세요.
- 풀 리퀘스트, 커밋 메시지, 이슈 본문에서 프롬프트 입력을 정제하여 프롬프트 인젝션을 방지하세요. Codex에 전달하기 전에 HTML 주석이나 숨겨진 텍스트를 검토하세요.
- `OPENAI_API_KEY`를 보호하려면 `safety-strategy`를 `drop-sudo`로 유지하거나 Codex를 비권한 사용자로 이동하세요. 멀티 테넌트 러너에서 `unsafe` 모드로 액션을 실행하지 마세요.
- Codex를 작업의 마지막 단계로 실행하여 이후 단계가 예기치 않은 상태 변경을 이어받지 않도록 하세요.
- 프록시 로그나 액션 출력에서 비밀이 노출되었다고 의심되면 즉시 키를 교체하세요.

## 문제 해결

- **prompt와 prompt-file을 모두 설정한 경우**: 중복 입력을 제거하여 정확히 하나의 소스를 제공하세요.
- **responses-api-proxy가 서버 정보를 쓰지 않은 경우**: API 키가 존재하고 유효한지 확인하세요. API 키를 제공해야 프록시가 시작됩니다.
- **`sudo` 제거를 기대했지만 `sudo`가 성공한 경우**: 이전 단계에서 `sudo`를 복원하지 않았는지, 러너 OS가 Linux 또는 macOS인지 확인하세요. 새 작업으로 다시 실행하세요.
- **`drop-sudo` 이후 권한 오류 발생**: 액션 실행 전에 쓰기 권한을 부여하세요(예: `chmod -R g+rwX "$GITHUB_WORKSPACE"` 또는 비권한 사용자 패턴 사용).
- **권한 없는 트리거 차단됨**: 기본 쓰기 협력자 외의 서비스 계정을 허용하려면 `allow-users` 또는 `allow-bots` 입력을 조정하세요.
