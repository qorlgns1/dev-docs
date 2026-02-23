---
title: 'Agents SDK로 Codex 사용하기'
description: "title: 'Agents SDK로 Codex 사용하기'"
---

title: 'Agents SDK로 Codex 사용하기'
description: 'Codex를 MCP 서버로 실행하고 다른 MCP 클라이언트(예: OpenAI Agents SDK로 만든 에이전트)에서 연결할 수 있습니다.'

Source URL: https://developers.openai.com/codex/guides/agents-sdk

# Agents SDK로 Codex 사용하기

# Codex를 MCP 서버로 실행하기

Codex를 MCP 서버로 실행한 다음 다른 MCP 클라이언트(예: [OpenAI Agents SDK](https://openai.github.io/openai-agents-js/guides/mcp/)로 만든 에이전트)에서 연결할 수 있습니다.

Codex를 MCP 서버로 시작하려면 다음 명령을 사용하세요:

```bash
codex mcp-server
```

[Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector)와 함께 Codex MCP 서버를 시작하려면 다음을 사용하세요:

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

`tools/list` 요청을 보내면 두 개의 도구가 표시됩니다:

**`codex`**: Codex 세션을 실행합니다. Codex의 `Config` 구조체와 맞는 구성 매개변수를 받습니다. `codex` 도구는 다음 속성을 사용합니다:

| Property                | Type      | Description                                                                                              |
| ----------------------- | --------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** (required) | `string`  | Codex 대화를 시작하는 초기 사용자 프롬프트입니다.                                                          |
| `approval-policy`       | `string`  | 모델이 생성한 셸 명령에 대한 승인 정책입니다: `untrusted`, `on-request`, `never`.                          |
| `base-instructions`     | `string`  | 기본 지침 대신 사용할 지침 세트입니다.                                                                    |
| `config`                | `object`  | `$CODEX_HOME/config.toml`에 있는 설정을 재정의하는 개별 구성 설정입니다.                                  |
| `cwd`                   | `string`  | 세션의 작업 디렉터리입니다. 상대 경로인 경우 서버 프로세스의 현재 디렉터리를 기준으로 해석됩니다.           |
| `include-plan-tool`     | `boolean` | 대화에 plan 도구를 포함할지 여부입니다.                                                                   |
| `model`                 | `string`  | 모델 이름을 선택적으로 덮어쓸 때 사용합니다(예: `o3`, `o4-mini`).                                            |
| `profile`               | `string`  | 기본 옵션을 지정할 `config.toml`의 구성 프로필입니다.                                                      |
| `sandbox`               | `string`  | 샌드박스 모드입니다: `read-only`, `workspace-write`, `danger-full-access`.                                 |

**`codex-reply`**: 스레드 ID와 프롬프트를 제공해 Codex 세션을 이어갑니다. `codex-reply` 도구는 다음 속성을 사용합니다:

| Property                      | Type   | Description                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** (required)       | string | Codex 대화를 이어갈 다음 사용자 프롬프트입니다.             |
| **`threadId`** (required)     | string | 계속할 스레드의 ID입니다.                                   |
| `conversationId` (deprecated) | string | `threadId`의 호환성 유지를 위한 더 이상 사용되지 않는 별칭입니다. |

`tools/call` 응답의 `structuredContent.threadId`에서 `threadId`를 사용하세요. 승인 프롬프트(exec/patch)도 `params` 페이로드에 `threadId`를 포함합니다.

응답 페이로드 예:

```json
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

모던 MCP 클라이언트는 도구 호출 결과로 `"structuredContent"`만 보고하는 경우가 많지만, Codex MCP 서버는 구식 MCP 클라이언트를 위해 `"content"`도 함께 반환합니다.

# 다중 에이전트 워크플로우 만들기

Codex CLI는 단발성 작업 이상을 수행할 수 있습니다. CLI를 [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) 서버로 노출하고 OpenAI Agents SDK로 오케스트레이션하면 단일 에이전트에서 완전한 소프트웨어 전달 파이프라인까지 확장 가능한 결정론적이고 리뷰 가능한 워크플로우를 만들 수 있습니다.

이 가이드는 [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb)에 소개된 것과 동일한 워크플로우를 단계별로 안내합니다. 다음을 수행합니다:

- Codex CLI를 장기 실행 MCP 서버로 실행,
- 소규모 브라우저 게임을 만드는 집중된 단일 에이전트 워크플로우 구축,
- 핸드오프, 보호 장치, 이후 검토 가능한 전체 추적을 갖춘 다중 에이전트 팀 오케스트레이션.

시작하기 전에 다음을 준비하세요:

- `npx codex` 실행이 가능한 [Codex CLI](https://developers.openai.com/codex/cli)가 로컬에 설치되어 있어야 합니다.
- `pip`이 설치된 Python 3.10+.
- `npx`에 필요한 Node.js 18+.
- 로컬에 저장된 OpenAI API 키. [OpenAI 대시보드](https://platform.openai.com/account/api-keys)에서 키를 생성하거나 관리할 수 있습니다.

가이드를 위한 작업 디렉터리를 만들고 `.env` 파일에 API 키를 추가하세요:

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## 종속성 설치

Agents SDK는 Codex, 핸드오프, 추적 간 오케스트레이션을 처리합니다. 최신 SDK 패키지를 설치하세요:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

가상 환경을 활성화하면 SDK 종속성이 시스템의 나머지 부분과 격리됩니다.

## Codex CLI를 MCP 서버로 초기화

Codex CLI를 Agents SDK가 호출할 수 있는 MCP 서버로 전환하는 것으로 시작하세요. 이 서버는 두 가지 도구(`codex()`로 대화 시작, `codex-reply()`로 이어감)를 노출하며 여러 에이전트 턴에 걸쳐 Codex를 유지합니다.

`codex_mcp.py` 파일을 만들고 다음 코드를 추가하세요:

```python
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

스크립트를 한 번 실행하여 Codex가 정상적으로 시작되는지 확인하세요:

```bash
python codex_mcp.py
```

스크립트는 `Codex MCP server started.`를 출력한 뒤 종료됩니다. 다음 섹션에서는 더 풍부한 워크플로우에서 동일한 MCP 서버를 재사용하게 됩니다.

## 단일 에이전트 워크플로우 구축

Codex MCP를 사용하여 작은 브라우저 게임을 만드는 범위 예제로 시작해 보겠습니다. 이 워크플로우는 두 명의 에이전트에 의존합니다:

1. **Game Designer**: 게임을 위한 브리핑 작성.
2. **Game Developer**: Codex MCP를 호출하여 게임 구현.

`codex_mcp.py`를 다음 코드로 업데이트합니다. 이전의 MCP 서버 설정은 그대로 유지하면서 두 에이전트를 추가합니다.

```python
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

```bash
python codex_mcp.py
```

Codex는 디자이너의 브리핑을 읽고 `index.html` 파일을 생성하며 전체 게임을 디스크에 씁니다. 생성된 파일을 브라우저에서 열어 결과를 플레이하세요. 매 실행마다 고유한 플레이 스타일이나 연출이 있는 다른 디자인이 생성됩니다.

## 다중 에이전트 워크플로우로 확장

이제 단일 에이전트 구성을 손꼽히게 추적 가능한 오케스트레이션 워크플로우로 확장합니다. 시스템은 다음을 추가합니다:

- **Project Manager**: 요구사항을 공유하고 핸드오프를 조율하며 보호 장치를 적용.
- **Designer**, **Frontend Developer**, **Server Developer**, **Tester**: 각각 정해진 지침과 출력 폴더를 갖춤.

`multi_agent_workflow.py`라는 새 파일을 만듭니다:

```python
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
            name="Backend Developer",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                "You are the Backend Developer.\n"
                "Read AGENT_TASKS.md and REQUIREMENTS.md. Implement the backend endpoints described there.\n\n"
                "Deliverables (write to /backend):\n"
                "- package.json – include a start script if requested\n"
                "- server.js – implement the API endpoints and logic exactly as specified\n\n"
                "Keep the code as simple and readable as possible. No external database.\n\n"
                "When complete, handoff to the Project Manager with transfer_to_project_manager_agent."
                "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."
            ),
            model="gpt-5",
            mcp_servers=[codex_mcp_server],
        )

        tester_agent = Agent(
            name="Tester",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                "You are the Tester.\n"
                "Read AGENT_TASKS.md and TEST.md. Verify that the outputs of the other roles meet the acceptance criteria.\n\n"
                "Deliverables (write to /tests):\n"
                "- TEST_PLAN.md – bullet list of manual checks or automated steps as requested\n"
                "- test.sh or a simple automated script if specified\n\n"
                "Keep it minimal and easy to run.\n\n"
                "When complete, handoff to the Project Manager with transfer_to_project_manager."
                "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."
            ),
            model="gpt-5",
            mcp_servers=[codex_mcp_server],
        )

        project_manager_agent = Agent(
            name="Project Manager",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                """
                You are the Project Manager.

                Objective:
                Convert the input task list into three project-root files the team will execute against.

                Deliverables (write in project root):
                - REQUIREMENTS.md: concise summary of product goals, target users, key features, and constraints.
                - TEST.md: tasks with [Owner] tags (Designer, Frontend, Backend, Tester) and clear acceptance criteria.
                - AGENT_TASKS.md: one section per role containing:
                  - Project name
                  - Required deliverables (exact file names and purpose)
                  - Key technical notes and constraints

                Process:
                - Resolve ambiguities with minimal, reasonable assumptions. Be specific so each role can act without guessing.
                - Create files using Codex MCP with {"approval-policy":"never","sandbox":"workspace-write"}.
                - Do not create folders. Only create REQUIREMENTS.md, TEST.md, AGENT_TASKS.md.

                Handoffs (gated by required files):
                1) After the three files above are created, hand off to the Designer with transfer_to_designer_agent and include REQUIREMENTS.md and AGENT_TASKS.md.
                2) Wait for the Designer to produce /design/design_spec.md. Verify that file exists before proceeding.
                3) When design_spec.md exists, hand off in parallel to both:
                   - Frontend Developer with transfer_to_frontend_developer_agent (provide design_spec.md, REQUIREMENTS.md, AGENT_TASKS.md).
                   - Backend Developer with transfer_to_backend_developer_agent (provide REQUIREMENTS.md, AGENT_TASKS.md).
                4) Wait for Frontend to produce /frontend/index.html and Backend to produce /backend/server.js. Verify both files exist.
                5) When both exist, hand off to the Tester with transfer_to_tester_agent and provide all prior artifacts and outputs.
                6) Do not advance to the next handoff until the required files for that step are present. If something is missing, request the owning agent to supply it and re-check.

                PM Responsibilities:
                - Coordinate all roles, track file completion, and enforce the above gating checks.
                - Do NOT respond with status updates. Just handoff to the next agent until the project is complete.
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
Goal: Build a tiny browser game to showcase a multi-agent workflow.

High-level requirements:
- Single-screen game called "Bug Busters".
- Player clicks a moving bug to earn points.
- Game ends after 20 seconds and shows final score.
- Optional: submit score to a simple backend and display a top-10 leaderboard.

Roles:
- Designer: create a one-page UI/UX spec and basic wireframe.
- Frontend Developer: implement the page and game logic.
- Backend Developer: implement a minimal API (GET /health, GET/POST /scores).
- Tester: write a quick test plan and a simple script to verify core routes.

Constraints:
- No external database—memory storage is fine.
- Keep everything readable for beginners; no frameworks required.
- All outputs should be small files saved in clearly named folders.
"""

        result = await Runner.run(project_manager_agent, task_list, max_turns=30)
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

스크립트를 실행하고 생성된 파일을 확인하세요:

```bash
python multi_agent_workflow.py
ls -R
```

프로젝트 매니저 에이전트는 `REQUIREMENTS.md`, `TEST.md`, `AGENT_TASKS.md`를 작성하고 디자이너, 프론트엔드, 서버, 테스터 에이전트 간의 핸드오프를 조율합니다. 각 에이전트는 자신의 폴더에 범위가 정해진 아티팩트를 작성한 후 프로젝트 매니저에게 제어를 반환합니다.

## 워크플로 추적

Codex는 모든 프롬프트, 도구 호출, 핸드오프를 캡처한 트레이스를 자동으로 기록합니다. 다중 에이전트 실행이 완료되면 [Traces 대시보드](https://platform.openai.com/trace)를 열어 실행 타임라인을 확인하세요.

상위 수준 트레이스는 프로젝트 매니저가 다음 단계로 넘어가기 전에 핸드오프를 검증하는 방법을 강조합니다. 개별 단계를 클릭하면 프롬프트, Codex MCP 호출, 작성된 파일, 실행 시간 등을 확인할 수 있습니다. 이러한 세부정보 덕분에 각 핸드오프를 쉽게 감사할 수 있고 워크플로가 턴 단위로 어떻게 진화했는지 이해할 수 있습니다.
이러한 트레이스는 추가 계측 없이도 워크플로 문제를 디버깅하고 에이전트 행동을 감사하며 시간에 따른 성능을 측정하는 데 매우 유용합니다.

