---
title: 'Codex SDK'
description: 'Codex CLI, IDE 확장 또는 Codex Web을 통해 Codex를 사용하는 경우에도 프로그램적으로 제어할 수 있습니다.'
---

Source URL: https://developers.openai.com/codex/sdk

# Codex SDK

Codex CLI, IDE 확장 또는 Codex Web을 통해 Codex를 사용하는 경우에도 프로그램적으로 제어할 수 있습니다.

다음과 같은 상황에서는 SDK를 사용하세요:

- CI/CD 파이프라인의 일부로 Codex를 제어할 때
- 복잡한 엔지니어링 작업을 수행하기 위해 Codex와 상호작용하는 자체 에이전트를 만들 때
- 내부 툴이나 워크플로에 Codex를 통합할 때
- 자체 애플리케이션에 Codex를 통합할 때

## TypeScript 라이브러리

TypeScript 라이브러리는 비대화형 모드보다 더 종합적이고 유연하게 애플리케이션 내에서 Codex를 제어하는 방법을 제공합니다.

이 라이브러리는 서버 측에서 사용하며 Node.js 18 이상이 필요합니다.

### 설치

시작하려면 `npm`을 사용해 Codex SDK를 설치하세요:

```bash
npm install @openai/codex-sdk
```

### 사용법

Codex와 스레드를 시작하고 프롬프트로 실행하세요.

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result);
```

같은 스레드를 계속하려면 `run()`을 다시 호출하거나 스레드 ID를 제공해 과거 스레드를 다시 시작하세요.

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2);
```

자세한 내용은 [TypeScript 저장소](https://github.com/openai/codex/tree/main/sdk/typescript)를 참조하세요.
