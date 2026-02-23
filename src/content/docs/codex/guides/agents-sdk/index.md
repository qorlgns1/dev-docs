---
title: Agents SDK와 함께 Codex 사용
description: "출처 URL: https://developers.openai.com/codex/guides/agents-sdk"
sidebar:
  order: 2
---

# Agents SDK와 함께 Codex 사용

출처 URL: https://developers.openai.com/codex/guides/agents-sdk

# Codex를 MCP 서버로 실행하기

Codex를 MCP 서버로 실행하고 다른 MCP 클라이언트(예: [OpenAI Agents SDK](https://openai.github.io/openai-agents-js/guides/mcp/)로 구축한 에이전트)에서 연결할 수 있습니다.

Codex를 MCP 서버로 시작하려면 다음 명령을 사용할 수 있습니다:
```
    codex mcp-server
```

[Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector)로 Codex MCP 서버를 실행할 수도 있습니다:
```
    npx @modelcontextprotocol/inspector codex mcp-server
```

두 가지 도구를 확인하려면 `tools/list` 요청을 보내세요:

**`codex`** : Codex 세션을 실행합니다. Codex `Config` 구조체와 동일한 구성 매개변수를 받습니다. `codex` 도구는 다음 속성을 사용합니다:

속성| 유형| 설명  
---|---|---  
**`prompt`** (required)| `string`| Codex 대화를 시작할 초기 사용자 프롬프트입니다.  
`approval-policy`| `string`| 모델이 생성한 셸 명령에 대한 승인 정책입니다: `untrusted`, `on-request`, `never`.  
`base-instructions`| `string`| 기본 지침 대신 사용할 지침 집합입니다.  
`config`| `object`| `$CODEX_HOME/config.toml`에 있는 내용을 재정의하는 개별 설정입니다.  
`cwd`| `string`| 세션의 작업 디렉터리입니다. 상대 경로면 서버 프로세스의 현재 디렉터리를 기준으로 해석됩니다.  
`include-plan-tool`| `boolean`| 대화에 plan 도구를 포함할지 여부입니다.  
`model`| `string`| 모델 이름(예: `o3`, `o4-mini`)을 선택적으로 재정의합니다.  
`profile`| `string`| 기본 옵션을 지정하는 `config.toml`의 구성 프로필입니다.  
`sandbox`| `string`| 샌드박스 모드입니다: `read-only`, `workspace-write`, `danger-full-access`.  
  
**`codex-reply`** : 스레드 ID와 프롬프트를 제공해 Codex 세션을 계속합니다. `codex-reply` 도구는 다음 속성을 사용합니다:

속성| 유형| 설명  
---|---|---  
**`prompt`** (required)| string| Codex 대화를 이어갈 다음 사용자 프롬프트입니다.  
**`threadId`** (required)| string| 계속 진행할 스레드의 ID입니다.  
`conversationId` (deprecated)| string| 호환성을 위해 유지되는 `threadId`의 더 이상 사용되지 않는 별칭입니다.  
  
`tools/call` 응답의 `structuredContent.threadId`에서 `threadId`를 사용하세요. 승인 프롬프트(exec/patch)에도 `params` 페이로드에 `threadId`가 포함됩니다.

예시 응답 페이로드:
```
    {
      "structuredContent": {
        "threadId": "019bbb20-bff6-7130-83aa-bf45ab33250e",
        "content": "`ls -lah` (or `ls -alh`) — long listing, includes dotfiles, human-readable sizes."
      },
      "content": [
        {
          "type": "text",
          "text": "`ls -lah` (or `ls -alh`) — long listing, includes dotfiles, human-readable sizes."
        }
      ]
    }
```

최신 MCP 클라이언트는 일반적으로 도구 호출 결과로 `"structuredContent"`만 보고하지만, Codex MCP 서버는 구형 MCP 클라이언트를 위해 `"content"`도 함께 반환합니다.

# 다중 에이전트 워크플로 만들기

Codex CLI는 임시 작업을 실행하는 것 이상의 기능을 제공합니다. CLI를 [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) 서버로 노출하고 OpenAI Agents SDK로 오케스트레이션하면 단일 에이전트부터 완전한 소프트웨어 전달 파이프라인까지 확장 가능한 결정적이며 검토 가능한 워크플로를 만들 수 있습니다.

이 가이드는 [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb)에 소개된 것과 동일한 워크플로를 순서대로 설명합니다. 다음을 수행하게 됩니다:

  * Codex CLI를 장기 실행 MCP 서버로 실행하고,
  * 실제로 실행 가능한 브라우저 게임을 만드는 데 집중하는 단일 에이전트 워크플로를 구축하며,
  * 핸드오프, 가드레일, 사후 검토 가능한 전체 추적을 갖춘 다중 에이전트 팀을 오케스트레이션합니다.



시작하기 전에 다음을 준비하세요:

* 로컬에 [Codex CLI](https://developers.openai.com/codex/cli)를 설치해 `npx codex`를 실행할 수 있어야 합니다.
  * `pip`이 포함된 Python 3.10 이상.
  * Node.js 18 이상 (`npx`에 필요).
  * 로컬에 저장된 OpenAI API 키. [OpenAI 대시보드](https://platform.openai.com/account/api-keys)에서 키를 생성하거나 관리할 수 있습니다.

가이드를 위한 작업 디렉터리를 만들고 `.env` 파일에 API 키를 추가합니다:
```
    mkdir codex-workflows
    cd codex-workflows
    printf "OPENAI_API_KEY=sk-..." > .env
```

## 의존성 설치

Agents SDK는 Codex, 핸드오프, 트레이스를 오케스트레이션합니다. 최신 SDK 패키지를 설치합니다:
```
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade openai openai-agents python-dotenv
```

가상 환경을 활성화하면 SDK 의존성을 시스템의 다른 부분과 분리할 수 있습니다.

## MCP 서버로 Codex CLI 초기화

먼저 Codex CLI를 Agents SDK가 호출할 수 있는 MCP 서버로 전환합니다. 이 서버는 두 가지 도구(`codex()`로 대화를 시작하고 `codex-reply()`로 계속)를 노출하고 여러 에이전트 턴 동안 Codex를 유지합니다.

`codex_mcp.py`라는 파일을 만들고 다음 내용을 추가합니다:
```
    import asyncio
    
    from agents import Agent, Runner
    from agents.mcp import MCPServerStdio
    
    
    async def main() -> None:
        async with MCPServerStdio(
            name="Codex CLI",
            params={
                "command": "npx",
                "args": ["-y", "codex", "mcp-server"],
            },
            client_session_timeout_seconds=360000,
        ) as codex_mcp_server:
            print("Codex MCP server started.")
            # More logic coming in the next sections.
            return
    
    
    if __name__ == "__main__":
        asyncio.run(main())
```

Codex가 정상적으로 실행되는지 확인하려면 스크립트를 한 번 실행합니다:
```
    python codex_mcp.py
```

`Codex MCP server started.`를 출력한 뒤 스크립트가 종료됩니다. 다음 섹션에서는 동일한 MCP 서버를 더 풍부한 워크플로에서 재사용합니다.

## 단일 에이전트 워크플로 구축

Codex MCP를 사용해 작은 브라우저 게임을 배포하는 제한된 예시로 시작하겠습니다. 이 워크플로에는 두 명의 에이전트가 필요합니다.

  1. **Game Designer** : 게임 브리프를 작성합니다.
  2. **Game Developer** : Codex MCP를 호출해 게임을 구현합니다.

`codex_mcp.py`를 다음 코드로 업데이트합니다. 앞서 작성한 MCP 서버 설정을 유지하면서 두 에이전트를 추가합니다.
```
    import asyncio
    import os
    
    from dotenv import load_dotenv
    
    from agents import Agent, Runner, set_default_openai_api
    from agents.mcp import MCPServerStdio
    
    load_dotenv(override=True)
    set_default_openai_api(os.getenv("OPENAI_API_KEY"))
    
    
    async def main() -> None:
        async with MCPServerStdio(
            name="Codex CLI",
            params={
                "command": "npx",
                "args": ["-y", "codex", "mcp-server"],
            },
            client_session_timeout_seconds=360000,
        ) as codex_mcp_server:
            developer_agent = Agent(
                name="Game Developer",
                instructions=(
                    "You are an expert in building simple games using basic html + css + javascript with no dependencies. "
                    "Save your work in a file called index.html in the current directory. "
                    "Always call codex with \"approval-policy\": \"never\" and \"sandbox\": \"workspace-write\"."
                ),
                mcp_servers=[codex_mcp_server],
            )
    
            designer_agent = Agent(
                name="Game Designer",
                instructions=(
                    "You are an indie game connoisseur. Come up with an idea for a single page html + css + javascript game that a developer could build in about 50 lines of code. "
                    "Format your request as a 3 sentence design brief for a game developer and call the Game Developer coder with your idea."

),
                model="gpt-5",
                handoffs=[developer_agent],
            )
    
            await Runner.run(designer_agent, "Implement a fun new game!")
    
    
    if __name__ == "__main__":
        asyncio.run(main())
```

스크립트를 실행하세요:
```
    python codex_mcp.py
```

Codex는 디자이너의 브리프를 읽고 `index.html` 파일을 생성해 전체 게임을 디스크에 기록합니다. 생성된 파일을 브라우저에서 열어 결과물을 플레이하세요. 실행할 때마다 플레이 스타일과 마감이 독특하게 바뀐 새로운 디자인이 나옵니다.

## 다중 에이전트 워크플로로 확장

이제 단일 에이전트 구성을 조율 가능하고 추적 가능한 워크플로로 전환합니다. 시스템에는 다음이 추가됩니다:

  * **Project Manager** : 공용 요구사항을 작성하고 핸드오프를 조율하며 가드레일을 집행합니다.
  * **Designer**, **Frontend Developer**, **Server Developer**, **Tester** : 각 에이전트는 범위가 정의된 지침과 출력 폴더를 가집니다.



`multi_agent_workflow.py`라는 새 파일을 만드세요:
````
    import asyncio
    import os
    
    from dotenv import load_dotenv
    
    from agents import (
        Agent,
        ModelSettings,
        Runner,
        WebSearchTool,
        set_default_openai_api,
    )
    from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
    from agents.mcp import MCPServerStdio
    from openai.types.shared import Reasoning
    
    load_dotenv(override=True)
    set_default_openai_api(os.getenv("OPENAI_API_KEY"))
    
    
    async def main() -> None:
        async with MCPServerStdio(
            name="Codex CLI",
            params={"command": "npx", "args": ["-y", "codex", "mcp"]},
            client_session_timeout_seconds=360000,
        ) as codex_mcp_server:
            designer_agent = Agent(
                name="Designer",
                instructions=(
                    f"""{RECOMMENDED_PROMPT_PREFIX}"""
                    "You are the Designer.\n"
                    "Your only source of truth is AGENT_TASKS.md and REQUIREMENTS.md from the Project Manager.\n"
                    "Do not assume anything that is not written there.\n\n"
                    "You may use the internet for additional guidance or research."
                    "Deliverables (write to /design):\n"
                    "- design_spec.md – a single page describing the UI/UX layout, main screens, and key visual notes as requested in AGENT_TASKS.md.\n"
                    "- wireframe.md – a simple text or ASCII wireframe if specified.\n\n"
                    "Keep the output short and implementation-friendly.\n"
                    "When complete, handoff to the Project Manager with transfer_to_project_manager."
                    "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."
                ),
                model="gpt-5",
                tools=[WebSearchTool()],
                mcp_servers=[codex_mcp_server],
            )
    
            frontend_developer_agent = Agent(
                name="Frontend Developer",
                instructions=(
                    f"""{RECOMMENDED_PROMPT_PREFIX}"""
                    "You are the Frontend Developer.\n"
                    "Read AGENT_TASKS.md and design_spec.md. Implement exactly what is described there.\n\n"
                    "Deliverables (write to /frontend):\n"
                    "- index.html – main page structure\n"
                    "- styles.css or inline styles if specified\n"
                    "- main.js or game.js if specified\n\n"
                    "Follow the Designer’s DOM structure and any integration points given by the Project Manager.\n"
                    "Do not add features or branding beyond the provided documents.\n\n"
                    "When complete, handoff to the Project Manager with transfer_to_project_manager_agent."
                    "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."

),
                model="gpt-5",
                mcp_servers=[codex_mcp_server],
            )

            backend_developer_agent = Agent(
                name="백엔드 개발자",
                instructions=(
                    f"""{RECOMMENDED_PROMPT_PREFIX}"""
                    "당신은 백엔드 개발자입니다.\n"
                    "AGENT_TASKS.md와 REQUIREMENTS.md를 읽고, 그 안에 설명된 백엔드 엔드포인트를 구현하세요.\n\n"
                    "산출물(/backend에 작성):\n"
                    "- package.json – 요청 시 start 스크립트를 포함하세요.\n"
                    "- server.js – 지정된 대로 API 엔드포인트와 로직을 정확히 구현하세요.\n\n"
                    "코드는 가능한 한 단순하고 읽기 쉽도록 유지하세요. 외부 데이터베이스는 사용하지 마세요.\n\n"
                    "완료되면 transfer_to_project_manager_agent로 프로젝트 매니저에게 인계하세요."
                    "파일을 생성할 때는 {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}로 Codex MCP를 호출하세요."
                ),
                model="gpt-5",
                mcp_servers=[codex_mcp_server],
            )

            tester_agent = Agent(
                name="테스터",
                instructions=(
                    f"""{RECOMMENDED_PROMPT_PREFIX}"""
                    "당신은 테스터입니다.\n"
                    "AGENT_TASKS.md와 TEST.md를 읽고, 다른 역할의 산출물이 승인 기준을 충족하는지 검증하세요.\n\n"
                    "산출물(/tests에 작성):\n"
                    "- TEST_PLAN.md – 요청된 대로 수동 확인 또는 자동화 단계의 불릿 목록을 작성하세요.\n"
                    "- 지정된 경우 test.sh 또는 간단한 자동화 스크립트를 작성하세요.\n\n"
                    "최소한으로 유지하고 실행하기 쉽게 만드세요.\n\n"
                    "완료되면 transfer_to_project_manager로 프로젝트 매니저에게 인계하세요."
                    "파일을 생성할 때는 {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}로 Codex MCP를 호출하세요."
                ),
                model="gpt-5",
                mcp_servers=[codex_mcp_server],
            )

            project_manager_agent = Agent(
                name="프로젝트 매니저",
                instructions=(
                    f"""{RECOMMENDED_PROMPT_PREFIX}"""
                    """
                    당신은 프로젝트 매니저입니다.

                    목표:
                    입력된 작업 목록을 팀이 실행할 세 개의 프로젝트 루트 파일로 전환하세요.

                    산출물(프로젝트 루트에 작성):
                    - REQUIREMENTS.md: 제품 목표, 대상 사용자, 핵심 기능, 제약을 간결하게 요약하세요.
                    - TEST.md: [Owner] 태그(Designer, Frontend, Backend, Tester)가 포함된 작업과 명확한 승인 기준을 작성하세요.
                    - AGENT_TASKS.md: 역할별 섹션에 다음을 포함하세요:
                      - 프로젝트 이름
                      - 필수 산출물(정확한 파일 이름과 목적)
                      - 핵심 기술 메모와 제약 사항

                    프로세스:
                    - 모호함은 최소한의 합리적인 가정으로 해소하세요. 각 역할이 추측 없이 행동할 수 있도록 구체적으로 작성하세요.
                    - {"approval-policy":"never","sandbox":"workspace-write"}로 Codex MCP를 사용해 파일을 생성하세요.
                    - 폴더를 만들지 마세요. REQUIREMENTS.md, TEST.md, AGENT_TASKS.md만 생성하세요.

                    인계(필수 파일 기준):
                    1) 위 세 파일을 만든 후 transfer_to_designer_agent로 디자이너에게 인계하고, REQUIREMENTS.md와 AGENT_TASKS.md를 포함하세요.
                    2) 디자이너가 /design/design_spec.md를 생성할 때까지 기다리세요. 진행 전에 해당 파일이 존재하는지 확인하세요.
                    3) design_spec.md가 존재하면 다음 둘 모두에게 병렬로 인계하세요:
```

- transfer_to_frontend_developer_agent와 함께하는 프런트엔드 개발자(design_spec.md, REQUIREMENTS.md, AGENT_TASKS.md 제공).
                       - transfer_to_backend_developer_agent와 함께하는 백엔드 개발자(REQUIREMENTS.md, AGENT_TASKS.md 제공).
                    4) 프런트엔드가 /frontend/index.html을, 백엔드가 /backend/server.js를 생성할 때까지 기다리고 두 파일이 모두 존재하는지 확인한다.
                    5) 두 파일이 모두 준비되면 transfer_to_tester_agent로 테스터에게 인계하고 이전 산출물과 출력을 모두 제공한다.
                    6) 해당 단계에 필요한 파일이 준비되기 전까지 다음 인계 단계로 이동하지 않는다. 누락된 것이 있으면 담당 에이전트에게 요청해 보완한 뒤 다시 확인한다.

                    PM 책임:
                    - 모든 역할을 조율하고 파일 완료 상태를 추적하며 위 게이팅 검사를 강제한다.
                    - 상태 업데이트로 응답하지 말 것. 프로젝트가 완료될 때까지 다음 에이전트에게 계속 인계한다.
                    """
                ),
                model="gpt-5",
                model_settings=ModelSettings(
                    reasoning=Reasoning(effort="medium"),
                ),
                handoffs=[designer_agent, frontend_developer_agent, backend_developer_agent, tester_agent],
                mcp_servers=[codex_mcp_server],
            )

            designer_agent.handoffs = [project_manager_agent]
            frontend_developer_agent.handoffs = [project_manager_agent]
            backend_developer_agent.handoffs = [project_manager_agent]
            tester_agent.handoffs = [project_manager_agent]

            task_list = """
    목표: 멀티 에이전트 워크플로를 보여 주는 작은 브라우저 게임을 만든다.

    상위 요구사항:
    - "Bug Busters"라는 단일 화면 게임.
    - 플레이어가 움직이는 벌레를 클릭해 점수를 획득한다.
    - 게임은 20초 후 종료되고 최종 점수를 표시한다.
    - 선택 사항: 점수를 단순 백엔드에 제출하고 상위 10개의 리더보드를 표시한다.

    역할:
    - 디자이너: 원페이지 UI/UX 사양과 기본 와이어프레임을 만든다.
    - 프런트엔드 개발자: 페이지와 게임 로직을 구현한다.
    - 백엔드 개발자: 최소한의 API(GET /health, GET/POST /scores)를 구현한다.
    - 테스터: 빠른 테스트 계획과 핵심 라우트를 검증하는 간단한 스크립트를 작성한다.

    제약:
    - 외부 데이터베이스 금지 — 메모리 저장소면 충분하다.
    - 초보자도 읽기 쉽도록 유지하고 프레임워크는 필요 없다.
    - 모든 출력은 명확한 폴더에 저장된 작은 파일이어야 한다.
    """

            result = await Runner.run(project_manager_agent, task_list, max_turns=30)
            print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
````

Run the script and watch the generated files:
```
    python multi_agent_workflow.py
    ls -R
```

프로젝트 매니저 에이전트는 `REQUIREMENTS.md`, `TEST.md`, `AGENT_TASKS.md`를 작성한 뒤 디자이너, 프런트엔드, 서버, 테스터 에이전트 간 인계를 조율한다. 각 에이전트는 자신의 폴더에서 범위가 지정된 산출물을 작성한 후 프로젝트 매니저에게 제어를 반환한다.

## 워크플로 추적

Codex는 모든 프롬프트, 도구 호출, 인계를 포착하는 트레이스를 자동으로 기록한다. 멀티 에이전트 실행이 완료되면 [Traces dashboard](https://platform.openai.com/trace)를 열어 실행 타임라인을 확인한다.

상위 트레이스는 프로젝트 매니저가 인계를 검증한 뒤 다음 단계로 이동하는 방식을 보여 준다. 각 단계를 클릭하면 프롬프트, Codex MCP 호출, 작성된 파일, 실행 시간을 확인할 수 있다. 이러한 세부정보 덕분에 모든 인계를 감사하고 워크플로가 턴마다 어떻게 발전했는지 쉽게 이해할 수 있다. 이 트레이스들은 추가 계측 없이도 워크플로 문제를 디버깅하고 에이전트 동작을 감사하며 성능을 장기적으로 측정하기 쉽게 만들어 준다.