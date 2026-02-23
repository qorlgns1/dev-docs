---
title: '가이드: Next.js MCP Server'
description: '소스 URL: https://nextjs.org/docs/app/guides/mcp'
---

# 가이드: Next.js MCP Server | Next.js
소스 URL: https://nextjs.org/docs/app/guides/mcp

[앱 라우터](https://nextjs.org/docs/app)[가이드](https://nextjs.org/docs/app/guides)Next.js MCP Server

페이지 복사

# 코딩 에이전트를 위한 Next.js MCP Server 활성화

최종 업데이트 2026년 2월 20일

[Model Context Protocol (MCP)](https://modelcontextprotocol.io)은 표준화된 인터페이스를 통해 AI 에이전트와 코딩 어시스턴트가 애플리케이션과 상호 작용할 수 있게 해 주는 오픈 표준입니다.

Next.js 16 이상에는 MCP 지원이 포함되어 있어 코딩 에이전트가 애플리케이션 내부를 실시간으로 조회할 수 있습니다. 이 기능을 사용하려면 [`next-devtools-mcp`](https://www.npmjs.com/package/next-devtools-mcp) 패키지를 설치하세요.

## 시작하기[](https://nextjs.org/docs/app/guides/mcp#getting-started)

**요구 사항:** Next.js 16 이상

프로젝트 루트의 `.mcp.json` 파일에 `next-devtools-mcp`를 추가하세요:

.mcp.json
[code]
    {
      "mcpServers": {
        "next-devtools": {
          "command": "npx",
          "args": ["-y", "next-devtools-mcp@latest"]
        }
      }
    }
[/code]

이게 전부입니다! 개발 서버를 시작하면 `next-devtools-mcp`가 실행 중인 Next.js 인스턴스를 자동으로 감지하고 연결합니다.

더 많은 구성 옵션은 [next-devtools-mcp 리포지터리](https://github.com/vercel/next-devtools-mcp)를 참조하세요.

## 기능[](https://nextjs.org/docs/app/guides/mcp#capabilities)

`next-devtools-mcp`는 코딩 에이전트에게 점점 더 많은 기능을 제공합니다:

### 애플리케이션 런타임 접근[](https://nextjs.org/docs/app/guides/mcp#application-runtime-access)

  * **오류 감지** : 개발 서버에서 현재 빌드 오류, 런타임 오류, 타입 오류를 가져옵니다
  * **실시간 상태 쿼리** : 실시간 애플리케이션 상태와 런타임 정보를 확인합니다
  * **페이지 메타데이터** : 페이지 라우트, 컴포넌트, 렌더링 세부 정보를 조회합니다
  * **서버 액션** : Server Actions와 컴포넌트 계층을 검사합니다
  * **개발 로그** : 개발 서버 로그와 콘솔 출력을 확인합니다

### 개발 도구[](https://nextjs.org/docs/app/guides/mcp#development-tools)

  * **Next.js 지식 베이스** : Next.js 문서와 모범 사례를 폭넓게 질의합니다
  * **마이그레이션 및 업그레이드 도구** : codemod를 활용해 Next.js 16으로 업그레이드를 도와줍니다
  * **Cache Components 가이드** : Cache Components 설정과 구성을 지원합니다
  * **브라우저 테스트** : [Playwright MCP](https://github.com/microsoft/playwright-mcp) 연동으로 브라우저에서 페이지를 검증합니다

> **참고:** Next.js 팀은 이러한 기능을 적극적으로 확장하고 있습니다. 에이전트 개발 경험을 개선하기 위해 새로운 도구와 기능이 정기적으로 추가됩니다.

## 개발 워크플로[](https://nextjs.org/docs/app/guides/mcp#development-workflow)

  1. Next.js 개발 서버를 시작하세요:

pnpmnpmyarnbun

터미널
[code]
    pnpm dev
[/code]

  2. 코딩 에이전트가 `next-devtools-mcp`를 통해 실행 중인 Next.js 인스턴스에 자동으로 연결됩니다
  3. 브라우저에서 애플리케이션을 열어 페이지를 확인하세요
  4. 아래 예시처럼 에이전트에게 인사이트와 진단을 요청하세요

### 사용 가능한 도구[](https://nextjs.org/docs/app/guides/mcp#available-tools)

`next-devtools-mcp`를 통해 에이전트는 다음 도구를 사용할 수 있습니다:

  * **`get_errors`** : 개발 서버에서 현재 빌드 오류, 런타임 오류, 타입 오류를 가져옵니다
  * **`get_logs`** : 브라우저 콘솔 로그와 서버 출력이 담긴 개발 로그 파일 경로를 가져옵니다
  * **`get_page_metadata`** : 특정 페이지의 라우트, 컴포넌트, 렌더링 정보를 조회합니다
  * **`get_project_metadata`** : 프로젝트 구조, 구성, 개발 서버 URL을 가져옵니다
  * **`get_server_action_by_id`** : ID로 Server Actions를 찾아 소스 파일과 함수 이름을 확인합니다

## 에이전트와 함께 사용하기[](https://nextjs.org/docs/app/guides/mcp#using-with-agents)

MCP 호환 코딩 에이전트는 Next.js 개발 서버를 자동으로 발견하고 연결하여 프로젝트에 대한 풍부한 컨텍스트를 제공합니다.

### 에이전트 지원 개발의 이점[](https://nextjs.org/docs/app/guides/mcp#benefits-for-agent-assisted-development)

에이전트는 다음을 수행할 수 있습니다:

  * **컨텍스트 인지 제안** : 기존 구조를 기반으로 새 기능을 추가할 최적의 위치를 추천합니다
  * **라이브 애플리케이션 상태 질의** : 개발 중 현재 구성, 라우트, 미들웨어를 확인합니다
  * **앱 라우터 페이지 레이아웃 이해** : 어떤 페이지와 레이아웃이 렌더링되는지 정확히 파악합니다
  * **정확한 구현 제공** : 프로젝트의 패턴과 규칙을 따르는 코드를 생성합니다

## 예시[](https://nextjs.org/docs/app/guides/mcp#examples)

### 오류 감지 및 진단[](https://nextjs.org/docs/app/guides/mcp#error-detection-and-diagnosis)

실시간으로 에이전트에게 오류를 물어보세요:
[code] 
    User: "What errors are currently in my application?"
[/code]

에이전트는 다음을 수행합니다:

  * `next-devtools-mcp`를 통해 실행 중인 Next.js 애플리케이션을 질의합니다
  * 현재 빌드 오류, 런타임 오류, 타입 오류를 가져옵니다
  * 오류를 분석하고 실행 가능한 해결책을 제공합니다

에이전트 응답(클릭하여 펼치기)
[code]
    > fix errors on the page
     
    ⏺ I'll help you fix the errors on the page. Let me first check what errors exist by looking at the
      current state of the project.
     
    ⏺ next-devtools - nextjs_runtime (MCP)(action: "discover_servers")
    ⏺ next-devtools - nextjs_runtime (MCP)(action: "call_tool", toolName: "get_errors")
     
    ⏺ I found a hydration error on the /about page. The error shows that the server is rendering
      "server" but the client is rendering "client", causing a mismatch. Let me create a todo list and fix
       this issue.
     
    ⏺ Perfect! Now let me check for errors on the page.           01:14 PM  claude-sonnet-4-5-20250929
     
    ⏺ next-devtools - nextjs_runtime (MCP)(action: "call_tool", toolName: "get_errors")
      ⎿ {
          "success": true,
          "port": 3000,
          "toolName": "get_errors",
          "result": {
            "content": [
              {
                "type": "text",
                "text": "# Found errors in 1 browser session(s)\n\n## Session: /about\n\n**1 error(s)
         found**\n\n### Runtime Errors\n\n#### Error 1 (Type: recoverable)\n\n**Error**: Hydration failed
[/code]

### 업그레이드 및 모범 사례[](https://nextjs.org/docs/app/guides/mcp#upgrading-and-best-practices)

Next.js 개념과 마이그레이션에 대한 도움을 받아보세요:
[code] 
    User: "Help me upgrade my Next.js app to version 16"
[/code]

에이전트는 현재 버전을 분석하고, codemod가 포함된 자동 마이그레이션을 안내하며, 주요 변경 사항을 처리하기 위한 단계별 지침을 제공합니다.

개념적 질문을 해보세요:
[code] 
    User: "When should I use 'use client' in App Router?"
[/code]

에이전트는 Next.js 지식 베이스를 질의하고 코드베이스 예시와 함께 문서 기반 설명을 제공합니다.

## 작동 방식[](https://nextjs.org/docs/app/guides/mcp#how-it-works)

Next.js 16 이상에는 개발 서버 내에서 실행되는 `/_next/mcp`에 기본 MCP 엔드포인트가 포함되어 있습니다. `next-devtools-mcp` 패키지는 이 엔드포인트를 자동으로 발견하고 통신하여 다음을 수행합니다:

  * 서로 다른 포트에서 실행 중인 여러 Next.js 인스턴스에 연결합니다
  * 도구 호출을 적절한 Next.js 개발 서버로 전달합니다
  * 코딩 에이전트를 위한 통합 인터페이스를 제공합니다

이 아키텍처는 에이전트 인터페이스를 내부 구현과 분리하여 `next-devtools-mcp`가 다양한 Next.js 프로젝트에서 원활하게 작동하도록 합니다.

## 문제 해결[](https://nextjs.org/docs/app/guides/mcp#troubleshooting)

### MCP 서버가 연결되지 않음[](https://nextjs.org/docs/app/guides/mcp#mcp-server-not-connecting)

  * Next.js v16 이상을 사용 중인지 확인하세요
  * `.mcp.json`에 `next-devtools-mcp`가 구성되어 있는지 검증하세요
  * 개발 서버를 시작하세요: `npm run dev`
  * 이미 실행 중이었다면 개발 서버를 재시작하세요
  * 코딩 에이전트가 MCP 서버 구성을 로드했는지 확인하세요

도움이 되었나요?

지원됨.

전송
