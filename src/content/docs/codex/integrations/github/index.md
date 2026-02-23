---
title: GitHub에서 Codex 사용
description: GitHub를 벗어나지 않고도 Codex로 풀 리퀘스트를 리뷰할 수 있습니다. 풀 리퀘스트 댓글에 를 추가하면 Codex가 표준 GitHub 코드 리뷰로 응답합니다.
sidebar:
  order: 1
---

# GitHub에서 Codex 사용

Source URL: https://developers.openai.com/codex/integrations/github

GitHub를 벗어나지 않고도 Codex로 풀 리퀘스트를 리뷰할 수 있습니다. 풀 리퀘스트 댓글에 `@codex review`를 추가하면 Codex가 표준 GitHub 코드 리뷰로 응답합니다.

## 코드 리뷰 설정

  1. [Codex cloud](https://developers.openai.com/codex/cloud)를 설정합니다.
  2. [Codex 설정](https://chatgpt.com/codex/settings/code-review)으로 이동해 저장소에 대해 **Code review**를 켭니다.

## 리뷰 요청

  1. 풀 리퀘스트 댓글에서 `@codex review`를 멘션합니다.
  2. Codex가 반응(👀)하고 리뷰를 게시할 때까지 기다립니다.

Codex는 팀 동료처럼 풀 리퀘스트에 리뷰를 남깁니다.

## 자동 리뷰 활성화

모든 풀 리퀘스트를 Codex가 자동으로 리뷰하게 하려면 [Codex 설정](https://chatgpt.com/codex/settings/code-review)에서 **Automatic reviews**를 켭니다. 그러면 `@codex review` 댓글 없이도 새 PR이 리뷰 대기 상태가 될 때마다 Codex가 리뷰를 게시합니다.

## Codex 리뷰 범위 사용자 지정

Codex는 저장소에서 `AGENTS.md` 파일을 찾고 그 안의 **Review guidelines**를 따릅니다.

저장소 지침을 설정하려면 최상위 `AGENTS.md`에 다음과 같은 섹션을 추가하거나 업데이트하세요:
```
    ## Review guidelines
    
    - Don't log PII.
    - Verify that authentication middleware wraps every route.
```

Codex는 각 변경 파일에 가장 가까운 `AGENTS.md`의 지침을 적용합니다. 특정 패키지에 대해 더 면밀한 검토가 필요하면 트리 깊은 곳에 더욱 구체적인 지침을 둘 수 있습니다.

일회성으로 집중할 항목이 있다면 풀 리퀘스트 댓글에 예를 들어 다음처럼 추가하세요:

`@codex review for security regressions`

GitHub에서 Codex는 P0 및 P1 이슈만 표시합니다. 문서 오타도 Codex가 표시하길 원한다면 `AGENTS.md`에 “Treat typos in docs as P1.”처럼 지침을 추가하세요.

## Codex에 다른 작업 지시하기

댓글에서 `review` 이외의 내용으로 `@codex`를 멘션하면 Codex는 풀 리퀘스트를 컨텍스트로 사용해 [cloud task](https://developers.openai.com/codex/cloud)를 시작합니다.
```
    @codex fix the CI failures
```