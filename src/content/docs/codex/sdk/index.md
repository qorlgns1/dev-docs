---
title: Codex SDK
description: "출처 URL: https://developers.openai.com/codex/sdk"
sidebar:
  order: 51
---

# Codex SDK

출처 URL: https://developers.openai.com/codex/sdk

Codex CLI, IDE 확장, Codex Web을 통해 Codex를 사용한다면, 프로그램적으로 제어할 수도 있습니다.

SDK를 사용하면 다음과 같은 필요를 충족할 수 있습니다:

  * CI/CD 파이프라인의 일부로 Codex를 제어
  * Codex와 상호작용하며 복잡한 엔지니어링 작업을 수행할 수 있는 자체 에이전트 생성
  * Codex를 내부 도구와 워크플로에 통합
  * Codex를 자체 애플리케이션에 연동



## TypeScript 라이브러리

TypeScript 라이브러리는 애플리케이션 내부에서 Codex를 제어할 수 있는 방법을 제공하며, 비대화형 모드보다 더 포괄적이고 유연합니다.

라이브러리는 서버 사이드에서 사용해야 하며, Node.js 18 이상이 필요합니다.

### 설치

시작하려면 `npm`으로 Codex SDK를 설치하세요:
```
    npm install @openai/codex-sdk
```

### 사용법

Codex와 스레드를 시작한 뒤, 프롬프트로 실행합니다.
```
    import { Codex } from "@openai/codex-sdk";
    
    const codex = new Codex();
    const thread = codex.startThread();
    const result = await thread.run(
      "Make a plan to diagnose and fix the CI failures"
    );
    
    console.log(result);
```

동일한 스레드를 계속하려면 `run()`을 다시 호출하고, 스레드 ID를 제공하여 과거 스레드를 재개할 수도 있습니다.
```
    // running the same thread
    const result = await thread.run("Implement the plan");
    
    console.log(result);
    
    // resuming past thread
    
    const threadId = "<thread-id>";
    const thread2 = codex.resumeThread(threadId);
    const result2 = await thread2.run("Pick up where you left off");
    
    console.log(result2);
```

자세한 내용은 [TypeScript 저장소](https://github.com/openai/codex/tree/main/sdk/typescript)를 확인하세요.