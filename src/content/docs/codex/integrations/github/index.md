---
title: 'GitHub에서 Codex 사용하기'
description: 'GitHub을 떠나지 않고 Codex로 풀 리퀘스트를 검토하세요.  코멘트를 추가하면 Codex가 표준 GitHub 코드 리뷰로 응답합니다.'
---

출처 URL: https://developers.openai.com/codex/integrations/github

# GitHub에서 Codex 사용하기

GitHub을 떠나지 않고 Codex로 풀 리퀘스트를 검토하세요. `@codex review` 코멘트를 추가하면 Codex가 표준 GitHub 코드 리뷰로 응답합니다.

- [Codex 코드 리뷰 안내](https://www.youtube.com/watch?v=HwbSWVg5Ln4)

## 코드 리뷰 설정

1. [Codex 클라우드](https://developers.openai.com/codex/cloud)를 설정하세요.
2. [Codex 설정](https://chatgpt.com/codex/settings/code-review)으로 이동하여 리포지토리에 대해 **Code review**를 켜세요.

  <img src="https://developers.openai.com/images/codex/code-review/code-review-settings.png"
    alt="코드 리뷰 토글이 보이는 Codex 설정"
    class="block h-auto w-full mx-0!"
  />

## 리뷰 요청하기

1. 풀 리퀘스트 코멘트에서 `@codex review`를 언급하세요.
2. Codex가 반응(👀)하고 리뷰를 게시할 때까지 기다리세요.

  <img src="https://developers.openai.com/images/codex/code-review/review-trigger.png"
    alt="@codex review가 포함된 풀 리퀘스트 코멘트"
    class="block h-auto w-full mx-0!"
  />

Codex는 동료처럼 풀 리퀘스트에 리뷰를 게시합니다.

  <img src="https://developers.openai.com/images/codex/code-review/review-example.png"
    alt="풀 리퀘스트에 대한 Codex 코드 리뷰 예시"
    class="block h-auto w-full mx-0!"
  />

## 자동 리뷰 활성화

Codex가 모든 풀 리퀘스트를 자동으로 리뷰하게 하려면 [Codex 설정](https://chatgpt.com/codex/settings/code-review)에서 **Automatic reviews**를 켜세요. Codex는 새로운 PR이 리뷰용으로 열릴 때마다 `@codex review` 코멘트 없이도 리뷰를 게시합니다.

## Codex 리뷰 대상 맞춤화

Codex는 리포지토리에서 `AGENTS.md` 파일을 찾아 포함된 **리뷰 가이드라인**을 따릅니다.

리포지토리의 가이드라인을 설정하려면 최상위 `AGENTS.md`에 다음과 같은 섹션을 추가하거나 업데이트하세요:

```md
## Review guidelines

- Don't log PII.
- Verify that authentication middleware wraps every route.
```

Codex는 변경된 각 파일에 가장 가까운 `AGENTS.md`의 지침을 적용합니다. 특정 패키지에 대해 더 세부적인 지침이 필요하면 트리 아래에 더 구체적인 지침을 둘 수 있습니다.

일회성으로 특정 부분에 집중하고 싶다면 풀 리퀘스트 코멘트에 다음과 같이 추가하세요:

`@codex review for security regressions`

GitHub에서는 Codex가 P0 및 P1 문제만 표시합니다. 문서에서 오타도 표시하길 원하면 `AGENTS.md`에 지침을 추가하세요(예: “문서 오타를 P1으로 처리”).

## Codex에 다른 작업 지시하기

`@codex`를 `review` 외의 내용과 함께 코멘트에 언급하면 Codex가 해당 풀 리퀘스트를 컨텍스트로 사용해 [클라우드 작업](https://developers.openai.com/codex/cloud)을 시작합니다.

```md
@codex fix the CI failures
```
