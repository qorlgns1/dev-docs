---
title: 규칙
description: "원본 URL: https://developers.openai.com/codex/rules"
sidebar:
  order: 34
---

# 규칙

원본 URL: https://developers.openai.com/codex/rules

규칙을 사용하면 Codex가 샌드박스 밖에서 실행할 수 있는 명령을 제어할 수 있습니다.

규칙은 실험적이며 변경될 수 있습니다.

## 규칙 파일 만들기

  1. `./codex/rules/` 아래에 `.rules` 파일을 만드세요(예: `~/.codex/rules/default.rules`).

  2. 규칙을 추가하세요. 다음 예시는 `gh pr view`를 샌드박스 밖에서 실행하기 전에 프롬프트를 띄웁니다.
```
# Prompt before running commands with the prefix `gh pr view` outside the sandbox.
         prefix_rule(
             # The prefix to match.
             pattern = ["gh", "pr", "view"],
         
             # The action to take when Codex requests to run a matching command.
             decision = "prompt",
         
             # Optional rationale for why this rule exists.
             justification = "Viewing PRs is allowed with approval",
         
             # `match` and `not_match` are optional "inline unit tests" where you can
             # provide examples of commands that should (or should not) match this rule.
             match = [
                 "gh pr view 7888",
                 "gh pr view --repo openai/codex",
                 "gh pr view 7888 --json title,body,comments",
             ],
             not_match = [
                 # Does not match because the `pattern` must be an exact prefix.
                 "gh pr --repo openai/codex view 7888",
             ],
         )
```

  3. Codex를 다시 시작하세요.

Codex는 시작할 때마다 모든 [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config) 위치 아래의 `rules/`를 스캔합니다. TUI에서 허용 목록에 명령을 추가하면, Codex는 사용자 계층의 `~/.codex/rules/default.rules`에 기록하여 이후 실행에서 프롬프트를 건너뛸 수 있게 합니다.

Smart approvals(기본값)가 활성화되어 있으면, Codex가 승격 요청 중에 `prefix_rule`을 제안할 수 있습니다. 제안된 접두어를 승인하기 전에 주의 깊게 검토하세요.

관리자는 [`requirements.toml`](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)에서 제한적인 `prefix_rule` 항목을 강제할 수도 있습니다.

## 규칙 필드 이해하기

`prefix_rule()`은 다음 필드를 지원합니다:

  * `pattern` **(필수)**: 일치시킬 명령 접두어를 정의하는 비어 있지 않은 리스트입니다. 각 요소는 다음 중 하나입니다. 
    * 문자열 리터럴(예: `"pr"`).
    * 같은 인자 위치에서 대안을 매칭하기 위한 리터럴들의 합집합(예: `["view", "list"]`).
  * `decision` **(`"allow"`가 기본값)**: 규칙이 일치할 때 취할 동작입니다. 여러 규칙이 일치하면 Codex는 가장 제한적인 결정을 적용합니다(`forbidden` > `prompt` > `allow`). 
    * `allow`: 프롬프트 없이 샌드박스 밖에서 명령을 실행합니다.
    * `prompt`: 일치하는 호출마다 프롬프트를 띄웁니다.
    * `forbidden`: 프롬프트 없이 요청을 차단합니다.
  * `justification` **(선택 사항)**: 규칙에 대한 비어 있지 않은 사람이 읽을 수 있는 이유입니다. Codex는 승인 프롬프트나 거부 메시지에서 이를 보여줄 수 있습니다. `forbidden`을 사용할 때는 적절하다면 권장 대안을 justification에 포함하세요(예: `"Use \`rg\` instead of \`grep\`."`).
  * `match` 및 `not_match` **(기본값은 `[]`)**: Codex가 규칙을 로드할 때 검증하는 예시입니다. 규칙이 적용되기 전에 실수를 잡아내는 데 사용하세요.

Codex가 명령 실행을 검토할 때는 명령의 인자 리스트를 `pattern`과 비교합니다. 내부적으로 Codex는 명령을 `execvp(3)`이 받는 것처럼 인자 리스트로 취급합니다.

## 셸 래퍼와 복합 명령

일부 도구는 다음과 같이 여러 셸 명령을 단일 호출로 감쌀 수 있습니다:
```
    ["bash", "-lc", "git add . && rm -rf /"]
```

이러한 명령은 하나의 문자열 안에 여러 동작을 숨길 수 있으므로, Codex는 `bash -lc`, `bash -c` 및 그에 해당하는 `zsh`/`sh` 변형을 특별히 처리합니다.

### Codex가 스크립트를 안전하게 분할할 수 있는 경우

스크립트가 다음으로만 이루어진 직렬 명령 체인인 경우:

  * 순수 단어(변수 확장 없음, `VAR=...`, `$FOO`, `*` 등 없음)

* 안전한 연산자(`&&`, `||`, `;`, 또는 `|`)로 연결된 경우



그때 Codex는 이를 tree-sitter로 파싱해 개별 명령으로 분리한 뒤, 규칙을 적용합니다.

위 스크립트는 두 개의 별도 명령으로 처리됩니다:

  * `["git", "add", "."]`
  * `["rm", "-rf", "/"]`



Codex는 각 명령을 규칙과 대조해 평가하며, 가장 제한적인 결과가 최종 결론이 됩니다.

`pattern=["git", "add"]`를 허용하더라도 Codex가 `git add . && rm -rf /`를 자동 허용하지 않는 이유는, `rm -rf /` 부분이 별도로 평가되어 전체 호출을 막기 때문입니다.

이 방식은 안전한 명령과 함께 위험한 명령이 끼어드는 것을 방지합니다.

### Codex가 스크립트를 분리하지 않는 경우

다음과 같이 더 고급 셸 기능을 쓰는 스크립트라면:

  * 리다이렉션(`>`, `>>`, `<`)
  * 치환(`$(...)`, `...`)
  * 환경 변수(`FOO=bar`)
  * 와일드카드 패턴(`*`, `?`)
  * 제어 흐름(`if`, `for`, 할당이 포함된 `&&` 등)



Codex는 해석하거나 분리하려 하지 않습니다.

이런 경우 전체 호출은 다음과 같이 처리됩니다:
```
    ["bash", "-lc", "<full script>"]
```

그리고 규칙은 해당 **단일** 호출에 적용됩니다.

이 접근을 통해 안전할 때는 명령별 평가로 보안을 확보하고, 그렇지 않을 때는 보수적으로 동작할 수 있습니다.

## 규칙 파일 테스트

명령에 규칙이 어떻게 적용되는지 확인하려면 `codex execpolicy check`를 사용하세요:
```
    codex execpolicy check --pretty \
      --rules ~/.codex/rules/default.rules \
      -- gh pr view 7888 --json title,body,comments
```

이 명령은 가장 엄격한 결정과 일치한 규칙(해당 규칙의 `justification` 값 포함)을 보여 주는 JSON을 출력합니다. 여러 개의 규칙 파일을 결합하려면 `--rules` 플래그를 여러 번 사용하고, 출력 서식을 맞추려면 `--pretty`를 추가하세요.

## 규칙 언어 이해하기

`.rules` 파일 형식은 `Starlark`( [language spec](https://github.com/bazelbuild/starlark/blob/master/spec.md) 참고)를 사용합니다. 구문은 Python과 비슷하지만, 규칙 엔진이 부작용 없이 실행할 수 있도록 설계되었습니다(예: 파일 시스템에 접근하지 않음).