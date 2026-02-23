---
title: '가이드: AI 코딩 에이전트'
description: '원본 URL: https://nextjs.org/docs/app/guides/ai-agents'
---

# 가이드: AI 코딩 에이전트 | Next.js

원본 URL: https://nextjs.org/docs/app/guides/ai-agents

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)AI 코딩 에이전트

# AI 코딩 에이전트를 위한 Next.js 프로젝트 설정 방법

마지막 업데이트: 2026년 2월 20일

Next.js는 `next` 패키지 안에 버전이 일치하는 문서를 포함해 배포하므로, AI 코딩 에이전트가 최신 API와 패턴을 정확하게 참조할 수 있습니다. 프로젝트 루트에 있는 `AGENTS.md` 파일은 에이전트가 학습 데이터 대신 이 번들 문서를 읽도록 안내합니다.

## 작동 방식[](https://nextjs.org/docs/app/guides/ai-agents#how-it-works)

`next`를 설치하면 Next.js 문서가 `node_modules/next/dist/docs/`에 번들로 포함됩니다. 이 문서는 [Next.js 문서 사이트](https://nextjs.org/docs) 구조와 동일합니다:
```
    node_modules/next/dist/docs/
    ├── 01-app/
    │   ├── 01-getting-started/
    │   ├── 02-guides/
    │   └── 03-api-reference/
    ├── 02-pages/
    ├── 03-architecture/
    └── index.mdx
```

즉, 에이전트는 항상 설치된 버전에 맞는 문서에 접근할 수 있으며 추가 네트워크 요청이나 외부 조회가 필요 없습니다.

프로젝트 루트의 `AGENTS.md` 파일은 에이전트에게 코드를 작성하기 전에 이 번들 문서를 읽으라고 지시합니다. Claude Code, Cursor, GitHub Copilot 등 대부분의 AI 코딩 에이전트는 세션을 시작할 때 자동으로 `AGENTS.md`를 확인합니다.

## 시작하기[](https://nextjs.org/docs/app/guides/ai-agents#getting-started)

### 새 프로젝트[](https://nextjs.org/docs/app/guides/ai-agents#new-projects)

[`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app)은 `AGENTS.md`와 `CLAUDE.md`를 자동으로 생성하므로 추가 설정이 필요 없습니다.

pnpmnpmyarnbun

터미널
```
    pnpm create next-app@canary
```

에이전트 파일이 필요 없다면 `--no-agents-md`를 전달하세요:
```
    npx create-next-app@canary --no-agents-md
```

### 기존 프로젝트[](https://nextjs.org/docs/app/guides/ai-agents#existing-projects)

Next.js `v16.2.0-canary.37` 이상인지 확인한 뒤, 다음 파일을 프로젝트 루트에 추가하세요.

`AGENTS.md`에는 에이전트가 읽게 될 지침이 들어 있습니다.

AGENTS.md
```
    <!-- BEGIN:nextjs-agent-rules -->

    # Next.js: ALWAYS read docs before coding

    Before any Next.js work, find and read the relevant doc in `node_modules/next/dist/docs/`. Your training data is outdated — the docs are the source of truth.

    <!-- END:nextjs-agent-rules -->
```

`CLAUDE.md`는 `AGENTS.md`를 `@` 임포트 구문으로 포함하므로, [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 사용자도 내용을 중복 없이 동일하게 전달받습니다.

CLAUDE.md
```
    @AGENTS.md
```

## AGENTS.md 이해하기[](https://nextjs.org/docs/app/guides/ai-agents#understanding-agentsmd)

기본 `AGENTS.md`는 **코드 작성 전에 번들 문서를 읽으라**는 단일하고 명확한 지침만 담고 있습니다. 의도적으로 최소화하여, 에이전트가 오래된 학습 데이터가 아니라 `node_modules/next/dist/docs/`에 있는 정확한 버전의 문서로 향하도록 만드는 것이 목적입니다.

`<!-- BEGIN:nextjs-agent-rules -->`와 `<!-- END:nextjs-agent-rules -->` 주석 마커는 Next.js에서 관리하는 구간을 구분합니다. 향후 업데이트로 덮어쓰일 걱정 없이, 이 마커 바깥에 프로젝트별 지침을 자유롭게 추가할 수 있습니다.

번들 문서에는 앱 라우터와 페이지 라우터를 위한 가이드, API 레퍼런스, 파일 규칙이 모두 포함됩니다. 에이전트가 라우팅, 데이터 패칭 등 어떤 Next.js 기능을 다루더라도, 오래된 학습 데이터 대신 번들 문서에서 정확한 API를 찾아볼 수 있습니다.

> **알아두면 좋아요:** 번들 문서와 `AGENTS.md`가 실제 Next.js 작업에서 에이전트 성능을 어떻게 개선하는지 확인하려면 [벤치마크 결과](https://nextjs.org/evals)를 참고하세요.

## 다음 단계

- [Next.js MCP 서버코딩 에이전트가 애플리케이션 상태에 접근하도록 Next.js MCP 지원을 사용하는 방법 알아보기](https://nextjs.org/docs/app/guides/mcp)

보내기