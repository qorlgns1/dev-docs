---
title: 자동화
description: "원본 URL: https://developers.openai.com/codex/app/automations"
---

# 자동화

원본 URL: https://developers.openai.com/codex/app/automations

백그라운드에서 반복 작업을 자동화하세요. Codex는 발견 사항을 받은편지함에 추가하거나, 보고할 내용이 없으면 작업을 자동으로 보관합니다. 더 복잡한 작업을 위해 자동화를 [스킬](https://developers.openai.com/codex/skills)과 결합할 수 있습니다.

자동화는 Codex 앱에서 로컬로 실행됩니다. 앱이 실행 중이어야 하며, 선택한 프로젝트가 디스크에서 사용 가능해야 합니다.

Git 저장소에서는 각 자동화 실행이 메인 체크아웃에 간섭하지 않도록 새로운 [worktree](https://developers.openai.com/codex/app/worktrees)에서 시작됩니다. 버전 관리되지 않는 프로젝트에서는 자동화가 프로젝트 디렉터리에서 직접 실행됩니다.

## 작업 관리

모든 자동화와 해당 실행 기록은 Codex 앱 사이드바의 automations 패널에서 확인할 수 있습니다.

“Triage” 섹션은 받은편지함 역할을 합니다. 발견 사항이 있는 자동화 실행이 여기에 표시되며, 받은편지함 필터를 사용해 모든 자동화 실행 또는 읽지 않은 항목만 볼 수 있습니다.

자동화가 Git 저장소에서 실행될 때 Codex는 전용 백그라운드 [worktree](https://developers.openai.com/codex/app/features#worktree-support)를 사용합니다. 버전 관리되지 않는 프로젝트에서는 자동화가 프로젝트 디렉터리에서 직접 실행됩니다. 백그라운드 worktree에서 실행할 수 있도록 Git 사용을 고려하세요. 동일한 자동화를 여러 프로젝트에서 실행할 수 있습니다.

자동화는 기본 샌드박스 설정을 사용합니다. read-only 모드에서는 파일 수정, 네트워크 접근, 또는 컴퓨터의 앱과 상호작용이 필요한 도구 호출이 실패합니다. full access를 활성화하면 백그라운드 자동화의 위험이 커집니다. [Settings](https://developers.openai.com/codex/app/settings)에서 샌드박스 설정을 조정하고 [rules](https://developers.openai.com/codex/rules)로 명령을 선택적으로 allowlist할 수 있습니다.

자동화를 유지보수 가능하고 팀 간 공유 가능하게 유지하려면 [skills](https://developers.openai.com/codex/skills)를 사용해 동작을 정의하고 Codex에 도구와 컨텍스트를 제공할 수 있습니다. 자동화 내에서 `$skill-name`을 사용해 특정 스킬을 자동화의 일부로 명시적으로 트리거할 수 있습니다.

## 자동화를 안전하게 테스트하기

자동화를 예약하기 전에 먼저 일반 스레드에서 프롬프트를 수동으로 테스트하세요. 이렇게 하면 다음을 확인할 수 있습니다:

  * 프롬프트가 명확하고 범위가 올바르게 설정되어 있다.
  * 선택한 모델과 도구가 예상대로 동작한다.
  * 생성된 diff를 검토할 수 있다.



실행 예약을 시작하면 처음 몇 개의 출력 결과를 면밀히 검토하고 필요에 따라 프롬프트나 실행 주기를 조정하세요.

## 자동화를 위한 Worktree 정리

Git 저장소의 경우 자동화는 worktree에서 실행됩니다. 빈번한 스케줄은 시간이 지나면서 많은 worktree를 만들 수 있습니다. 더 이상 필요 없는 자동화 실행은 보관 처리하고, 해당 worktree를 유지할 의도가 없다면 실행을 고정(pin)하지 마세요.

## 권한 및 보안 모델

자동화는 무인으로 실행되도록 설계되어 있으며 기본 샌드박스 설정을 사용합니다.

  * 샌드박스 모드가 **read-only** 이면 파일 수정, 네트워크 접근, 또는 컴퓨터의 앱과 상호작용이 필요한 도구 호출은 실패합니다. 샌드박스 설정을 workspace write로 업데이트하는 것을 고려하세요.
  * 샌드박스 모드가 **workspace-write** 이면 워크스페이스 외부 파일 수정, 네트워크 접근, 또는 컴퓨터의 앱과 상호작용이 필요한 도구 호출은 실패합니다. [rules](https://developers.openai.com/codex/rules)를 사용해 샌드박스 외부에서 실행할 명령을 선택적으로 allowlist할 수 있습니다.
  * 샌드박스 모드가 **full access** 이면 Codex가 확인 없이 파일을 수정하고, 명령을 실행하며, 네트워크에 접근할 수 있으므로 백그라운드 자동화의 위험이 커집니다. 샌드박스 설정을 workspace write로 업데이트하고, [rules](https://developers.openai.com/codex/rules)를 사용해 에이전트가 full access로 실행할 수 있는 명령을 선택적으로 정의하는 것을 고려하세요.



관리형 환경에 있는 경우 관리자는 관리자 강제 요구사항을 사용해 이러한 동작을 제한할 수 있습니다. 예를 들어 `approval_policy = "never"`를 금지하거나 허용되는 샌드박스 모드를 제한할 수 있습니다. [관리자 강제 요구사항 (`requirements.toml`)](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)을 참조하세요.

조직 정책에서 허용하는 경우 자동화는 `approval_policy = "never"`를 사용합니다. 관리자 요구사항으로 `approval_policy = "never"`가 금지된 경우 자동화는 선택한 모드의 승인 동작으로 대체됩니다.

## 예시

### 새 스킬 자동 생성
[code] 
    Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.
    
    If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.
    
    Definitely don't feel like you need to update any- only if there's a good reason!
    
    Let me know if you make any.
[/code]

### 프로젝트 최신 상태 유지
[code] 
    Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch <DIRECTORY>
    
    Formatting + structure:
    
    - Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
    - Preamble can read something like “Here’s the last 24h brief for <directory>:”
    - Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
    - Group by workstream rather than listing each commit. Workstream titles should be H1.
    - Write a short narrative per workstream that explains the changes in plain language.
    - Use bullet points and bolding when it makes things more readable
    - Feel free to make bullets per person, but bold their name
    
    Content requirements:
    
    - Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
    - Do NOT include commit hashes or a “Key commits” section.
    - It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.
    
    Scope rules:
    
    - Only include changes within the current cwd (or main checkout equivalent)
    - Only include the last 24h of commits.
    - Use `gh` to fetch PR titles and descriptions if it helps.
      Also feel free to pull PR reviews and comments
[/code]

### 자동화와 스킬을 결합해 자신의 버그 수정하기

본인의 커밋으로 도입된 버그를 수정하도록 시도하는 새 스킬을 만들기 위해 새로운 `$recent-code-bugfix`를 생성하고 [개인 스킬에 저장하세요](https://developers.openai.com/codex/skills#where-to-save-skills).
[code] 
    ---
    name: recent-code-bugfix
    description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
    ---
    
    # Recent Code Bugfix
    
    ## Overview
    
    Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.
    
    ## Workflow
    
    ### 1) Establish the recent-change scope
    
    Use Git to identify the author and changed files from the last week.
    
    - Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
    - Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
    - If the user’s prompt is empty, proceed directly with this default scope.
    
    ### 2) Find a concrete failure tied to recent changes
    
    Prioritize defects that are directly attributable to the author’s edits.
    
    - Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
    - If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
    - Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.
    
    ### 3) Implement the fix
    
    Make a minimal fix that aligns with project conventions.
    
    - Update only the files needed to resolve the issue.
    - Avoid adding extra defensive checks or unrelated refactors.
    - Keep changes consistent with local style and tests.
    
    ### 4) Verify
    
    Attempt verification when possible.
    
    - Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
    - If verification cannot be run, state what would be run and why it wasn’t executed.
    
    ### 5) Report
    
    Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.
[/code]

그런 다음 새 자동화를 만드세요:
[code] 
    Check my commits from the last 24h and submit a $recent-code-bugfix.
[/code]
