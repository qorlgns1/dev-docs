---
title: '규칙 파일 생성'
description: '원본 URL: https://developers.openai.com/codex/rules'
---

원본 URL: https://developers.openai.com/codex/rules

# 규칙

규칙을 사용하여 Codex가 샌드박스 외부에서 실행할 수 있는 명령을 제어하세요.

규칙은 실험적이며 변경될 수 있습니다.

## 규칙 파일 생성

1. `./codex/rules/` 아래에 `.rules` 파일을 만듭니다(예: `~/.codex/rules/default.rules`).
2. 규칙을 추가합니다. 이 예시는 `gh pr view`를 샌드박스 외부에서 실행하기 전에 프롬프트를 띄우도록 합니다.

   ```python
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

3. Codex를 재시작합니다.

Codex는 시작 시 모든 [팀 구성](https://developers.openai.com/codex/enterprise/admin-setup#team-config) 위치 아래의 `rules/`를 스캔합니다. TUI에서 허용 목록에 명령을 추가하면 Codex는 향후 실행에서 프롬프트를 건너뛰도록 사용자 레이어의 `~/.codex/rules/default.rules`에 기록합니다.

스마트 승인이 활성화되어 있으면(기본값) Codex가 승격 요청 중에 `prefix_rule`을 제안할 수 있습니다. 수락하기 전에 제안된 접두사를 주의 깊게 검토하세요.

관리자는 [`requirements.toml`](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)에서 제한적인 `prefix_rule` 항목을 강제로 적용할 수도 있습니다.

## 규칙 필드 이해

`prefix_rule()`은 다음 필드를 지원합니다:

- `pattern` **(필수)**: 일치시킬 명령 접두사를 정의하는 비어 있지 않은 목록입니다. 각 요소는 다음 중 하나입니다:
  - 리터럴 문자열(예: `"pr"`).
  - 해당 인수 위치에서 대안을 매치하기 위한 리터럴의 합집합(예: `["view", "list"]`).
- `decision` **(기본값 `"allow"`)**: 규칙이 일치할 때 취할 동작입니다. Codex는 여러 규칙이 일치하면 가장 제한적인 결정을 적용합니다(`forbidden` > `prompt` > `allow`).
  - `allow`: 프롬프트 없이 샌드박스 외부에서 명령을 실행합니다.
  - `prompt`: 일치하는 호출마다 프롬프트를 표시합니다.
  - `forbidden`: 프롬프트 없이 요청을 차단합니다.
- `justification` **(선택 사항)**: 규칙의 이유를 설명하는 비어 있지 않은 사람이 읽을 수 있는 문구입니다. Codex는 승인 프롬프트나 거부 메시지에 이 내용을 표시할 수 있습니다. `forbidden`을 사용할 때는 적절하다면 권장 대안을 포함하세요(예: `"Use \`rg\` instead of \`grep\`."`).
- `match` 및 `not_match` **(기본값 `[]`)**: Codex가 규칙을 로드할 때 검증하는 예시입니다. 규칙이 적용되기 전에 실수를 잡는 데 사용하세요.

Codex는 명령을 실행할 때 명령의 인수 목록을 `pattern`과 비교합니다. 내부적으로 Codex는 명령을 인수 목록(예: `execvp(3)`에 전달되는 것처럼)으로 처리합니다.

## 셸 래퍼 및 복합 명령

일부 도구는 여러 셸 명령을 단일 호출로 감쌀 수 있습니다. 예를 들면:

```text
["bash", "-lc", "git add . && rm -rf /"]
```

이러한 명령은 하나의 문자열에 여러 동작을 숨길 수 있으므로 Codex는 `bash -lc`, `bash -c`, 그리고 해당하는 `zsh`/`sh` 동등물을 특별하게 다룹니다.

### Codex가 스크립트를 안전하게 분리할 수 있는 경우

스크립트가 다음 항목으로만 구성된 선형 체인이라면:

- 일반 단어(변수 확장 없음, `VAR=...`, `$FOO`, `*` 등 없음)
- 안전한 연산자(`&&`, `||`, `;`, `|`)로 연결됨

Codex는 이를 파싱(tree-sitter 사용)하고 규칙을 적용하기 전에 개별 명령으로 분리합니다.

위 스크립트는 다음 두 개의 개별 명령으로 처리됩니다:

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

Codex는 각 명령을 규칙에 따라 평가하며 가장 제한적인 결과가 적용됩니다.

`pattern=["git", "add"]`를 허용하더라도 Codex는 `git add . && rm -rf /` 전체를 자동으로 허용하지 않습니다. `rm -rf /` 부분이 별도로 평가되어 전체 호출에 자동 허용을 막기 때문입니다.

이렇게 하면 안전한 명령과 함께 위험한 명령이 몰래 섞이는 것을 방지할 수 있습니다.

### Codex가 스크립트를 분리하지 않는 경우

스크립트가 다음과 같은 더 고급 셸 기능을 사용한다면:

- 리디렉션(`>`, `>>`, `<`)
- 치환(`$(...)`, `...`)
- 환경 변수(`FOO=bar`)
- 와일드카드 패턴(`*`, `?`)
- 제어 흐름(`if`, `for`, 할당과 함께 쓰인 `&&` 등)

Codex는 이를 해석하거나 분리하려 하지 않습니다.

이런 경우 전체 호출은 다음처럼 취급됩니다:

```text
["bash", "-lc", "<full script>"]
```

그리고 규칙은 이 **단일** 호출에 적용됩니다.

이 처리를 통해 안전할 때는 명령별 평가의 보안을 유지하고, 그렇지 않을 때는 보수적인 동작을 보장합니다.

## 규칙 파일 테스트

`codex execpolicy check`를 사용하여 명령에 규칙이 어떻게 적용되는지 테스트하세요:

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments
```

이 명령은 가장 엄격한 결정과 일치하는 규칙(일치한 규칙의 `justification` 값 포함)을 JSON으로 출력합니다. 여러 `--rules` 플래그를 사용해 파일을 결합하고, 출력 형식을 정렬하려면 `--pretty`를 추가하세요.

## 규칙 언어 이해

`.rules` 파일 형식은 `Starlark`를 사용합니다([언어 명세](https://github.com/bazelbuild/starlark/blob/master/spec.md) 참조). 문법은 Python과 비슷하지만 안전하게 실행하도록 설계되어 있어 규칙 엔진이 부작용 없이(예: 파일 시스템에 접근하지 않고) 실행할 수 있습니다.
