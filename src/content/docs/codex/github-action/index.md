---
title: Codex GitHub 액션
description: "출처 URL: https://developers.openai.com/codex/github-action"
sidebar:
  order: 53
---

# Codex GitHub 액션
출처 URL: https://developers.openai.com/codex/github-action

Codex GitHub 액션(`openai/codex-action@v1`)을 사용해 CI/CD 작업에서 Codex를 실행하고, 패치를 적용하거나 GitHub Actions 워크플로에서 리뷰를 게시하세요. 이 액션은 Codex CLI를 설치하고, API 키를 제공하면 Responses API 프록시를 시작하며, 지정한 권한으로 `codex exec`을 실행합니다.

다음이 필요할 때 이 액션을 사용하세요:

  * CLI를 직접 관리하지 않고도 PR 또는 릴리스에 Codex 피드백을 자동화하고 싶을 때
  * CI 파이프라인의 일부로 Codex 기반 품질 검사를 통해 변경 사항을 게이트하고 싶을 때
  * 워크플로 파일에서 반복 가능한 Codex 작업(코드 리뷰, 릴리스 준비, 마이그레이션 등)을 실행하고 싶을 때



CI 예시는 [비대화형 모드](https://developers.openai.com/codex/noninteractive)를 참고하고, [openai/codex-action 저장소](https://github.com/openai/codex-action)의 소스를 살펴보세요.

## 사전 준비

  * OpenAI 키를 GitHub secret(예: `OPENAI_API_KEY`)으로 저장하고 워크플로에서 참조하세요.
  * Linux 또는 macOS 러너에서 작업을 실행하세요. Windows의 경우 `safety-strategy: unsafe`를 설정하세요.
  * Codex가 저장소 내용을 읽을 수 있도록 액션을 호출하기 전에 코드를 체크아웃하세요.
  * 실행할 프롬프트를 결정하세요. `prompt`로 인라인 텍스트를 제공하거나 저장소에 커밋된 파일을 `prompt-file`로 지정할 수 있습니다.



## 워크플로 예시

아래 샘플 워크플로는 새 풀 리퀘스트를 리뷰하고 Codex 응답을 캡처한 뒤 PR에 다시 게시합니다.
```
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

`.github/codex/prompts/review.md`를 사용자 정의 프롬프트 파일로 교체하거나 인라인 텍스트를 위해 `prompt` 입력을 사용하세요. 또한 이 예시는 최종 Codex 메시지를 `codex-output.md`에 기록해 이후 검토하거나 아티팩트로 업로드할 수 있게 합니다.

## `codex exec` 구성

`codex exec` 옵션에 매핑되는 액션 입력을 설정해 Codex 실행 방식을 세밀하게 조정하세요.

  * `prompt` 또는 `prompt-file`(둘 중 하나): 작업과 함께할 인라인 지시문이나 저장소 내 Markdown/텍스트 경로입니다. 프롬프트를 `.github/codex/prompts/`에 보관하는 방식을 고려하세요.
  * `codex-args`: 추가 CLI 플래그입니다. JSON 배열(예: `["--full-auto"]`) 또는 셸 문자열(`--full-auto --sandbox danger-full-access`)로 제공해 편집, 스트리밍, MCP 구성을 허용할 수 있습니다.

* `model` 및 `effort`: 원하는 Codex 에이전트 구성을 선택하고, 기본값을 사용하려면 비워 두세요.
  * `sandbox`: Codex 실행에 필요한 권한에 맞춰 `sandbox` 모드(`workspace-write`, `read-only`, `danger-full-access`)를 지정하세요.
  * `output-file`: 최종 Codex 메시지를 디스크에 저장해 후속 단계에서 업로드하거나 diff할 수 있게 합니다.
  * `codex-version`: 사용할 특정 CLI 릴리스를 고정합니다. 최신 공개 버전을 쓰려면 비워 두세요.
  * `codex-home`: 여러 단계에서 설정 파일이나 MCP 구성을 재사용하려면 공유 Codex 홈 디렉터리를 가리키도록 설정하세요.



## 권한 관리

GitHub 호스트 러너에서는 제한하지 않는 한 Codex가 넓은 권한을 가집니다. 다음 입력 값으로 노출 범위를 제어하세요:

  * `safety-strategy`(기본값 `drop-sudo`)는 Codex를 실행하기 전에 `sudo`를 제거합니다. 작업 전체에 되돌릴 수 없으며, 메모리에 있는 비밀을 보호합니다. Windows에서는 반드시 `safety-strategy: unsafe`를 설정해야 합니다.
  * `unprivileged-user`는 `safety-strategy: unprivileged-user`와 `codex-user`를 함께 지정해 Codex를 특정 계정으로 실행합니다. 해당 사용자가 저장소 체크아웃에 읽기/쓰기 권한을 갖도록 하세요(`.cache/codex-action/examples/unprivileged-user.yml`에서 소유권 수정 예시 확인).
  * `read-only`는 Codex가 파일을 변경하거나 네트워크를 사용하는 것을 막지만, 여전히 높은 권한으로 실행됩니다. 비밀을 보호하려면 `read-only`만으로는 충분하지 않습니다.
  * `sandbox`는 Codex 내부에서 파일 시스템과 네트워크 접근을 제한합니다. 작업을 완료할 수 있는 가장 좁은 옵션을 선택하세요.
  * `allow-users`와 `allow-bots`는 워크플로를 트리거할 수 있는 대상을 제한합니다. 기본적으로 쓰기 권한이 있는 사용자만 실행할 수 있으니, 추가 신뢰 계정이 필요하면 명시적으로 나열하거나 기본 동작을 원하면 비워 두세요.



## 출력 캡처

액션은 마지막 Codex 메시지를 `final-message` 출력으로 내보냅니다. 위 예시처럼 잡 출력에 매핑하거나 이후 단계에서 바로 처리하세요. 러너에서 전체 대화를 수집하려면 `output-file`을 업로드 아티팩트 기능과 함께 사용하세요. 구조화된 데이터가 필요할 때는 `codex-args`에 `--output-schema`를 전달해 JSON 형식을 강제하세요.

## 보안 체크리스트

  * 워크플로를 시작할 수 있는 대상을 제한하세요. 저장소에 대해 Codex를 실행할 수 있도록 모든 사람에게 허용하기보다 신뢰 이벤트나 명시적 승인을 우선하세요.
  * 풀 리퀘스트, 커밋 메시지, 이슈 본문에서 들어오는 프롬프트 입력을 정화해 프롬프트 인젝션을 방지하세요. Codex에 전달하기 전 HTML 주석이나 숨겨진 텍스트를 검토하세요.
  * `OPENAI_API_KEY`를 보호하려면 `safety-strategy`를 `drop-sudo`로 유지하거나 Codex를 비권한 사용자로 이동하세요. 다중 테넌트 러너에서 `unsafe` 모드를 그대로 두지 마세요.
  * Codex를 작업의 마지막 단계로 실행해 이후 단계가 의도치 않은 상태 변화를 물려받지 않도록 하세요.
  * 프록시 로그나 액션 출력에 비밀이 노출됐다고 의심되면 즉시 키를 교체하세요.



## 문제 해결

  * **You set both prompt and prompt-file** : 입력이 하나만 전달되도록 중복을 제거하세요.
  * **responses-api-proxy didn’t write server info** : API 키가 존재하고 유효한지 확인하세요. `openai-api-key`를 제공할 때만 프록시가 시작됩니다.
  * **Expected`sudo` removal, but `sudo` succeeded**: 이전 단계에서 `sudo`를 복구하지 않았는지, 러너 OS가 Linux 또는 macOS인지 확인하세요. 새 작업으로 다시 실행하세요.
  * **Permission errors after`drop-sudo`**: 액션이 실행되기 전에 쓰기 권한을 부여하세요(예: `chmod -R g+rwX "$GITHUB_WORKSPACE"` 실행 또는 unprivileged-user 패턴 사용).
  * **Unauthorized trigger blocked** : 기본 쓰기 협력자 외 서비스 계정을 허용하려면 `allow-users`나 `allow-bots` 입력을 조정하세요.