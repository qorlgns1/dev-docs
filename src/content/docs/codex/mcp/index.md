---
title: 모델 컨텍스트 프로토콜
description: 모델 컨텍스트 프로토콜(MCP)은 모델을 도구와 컨텍스트에 연결합니다. 이를 사용하면 Codex가 서드파티 문서를 읽거나 브라우저, Figma 같은 개발자 도구와 상호작용하도록 할 수 있습니다.
sidebar:
  order: 36
---

# 모델 컨텍스트 프로토콜

Source URL: https://developers.openai.com/codex/mcp

모델 컨텍스트 프로토콜(MCP)은 모델을 도구와 컨텍스트에 연결합니다. 이를 사용하면 Codex가 서드파티 문서를 읽거나 브라우저, Figma 같은 개발자 도구와 상호작용하도록 할 수 있습니다.

Codex는 CLI와 IDE 확장 모두에서 MCP 서버를 지원합니다.

## 지원되는 MCP 기능

  * **STDIO 서버**: 명령으로 시작되는 로컬 프로세스로 실행되는 서버.
    * Environment variables
  * **스트리밍 가능한 HTTP 서버**: 주소를 통해 접근하는 서버.
    * Bearer token authentication
    * OAuth authentication (run `codex mcp login <server-name>` for servers that support OAuth)



## Codex를 MCP 서버에 연결하기

Codex는 `config.toml`에 MCP 구성을 저장하며, 다른 Codex 설정과 함께 보관됩니다. 기본 위치는 `~/.codex/config.toml`이지만, 신뢰된 프로젝트에 한해 `.codex/config.toml`로 프로젝트 단위에서 MCP 서버를 구성할 수도 있습니다.

CLI와 IDE 확장은 이 구성을 공유합니다. MCP 서버를 한 번 설정하면 두 Codex 클라이언트 간에 설정을 다시 할 필요 없이 전환할 수 있습니다.

MCP 서버를 구성하려면 다음 옵션 중 하나를 선택하세요.

  1. **CLI 사용**: `codex mcp`를 실행해 서버를 추가하고 관리합니다.
  2. **`config.toml` 수정**: `~/.codex/config.toml`(또는 신뢰된 프로젝트의 `.codex/config.toml`)을 직접 업데이트합니다.



### CLI로 구성하기

#### MCP 서버 추가
[code] 
    codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>
[/code]

예를 들어 개발자 문서를 위한 무료 MCP 서버 Context7을 추가하려면 다음 명령을 실행하면 됩니다:
[code] 
    codex mcp add context7 -- npx -y @upstash/context7-mcp
[/code]

#### 기타 CLI 명령

사용 가능한 MCP 명령 전체를 보려면 `codex mcp --help`를 실행하세요.

#### 터미널 UI(TUI)

`codex` TUI에서는 `/mcp`를 입력해 활성 MCP 서버를 확인할 수 있습니다.

### config.toml로 구성하기

MCP 서버 옵션을 더욱 세밀하게 제어하려면 `~/.codex/config.toml`(또는 프로젝트 범위의 `.codex/config.toml`)을 편집하세요. IDE 확장에서는 기어 메뉴에서 **MCP settings** > **Open config.toml**을 선택합니다.

구성 파일에서 각 MCP 서버는 `[mcp_servers.<server-name>]` 테이블로 정의합니다.

#### STDIO 서버

  * `command` (필수): 서버를 시작하는 명령.
  * `args` (선택): 서버에 전달할 인수.
  * `env` (선택): 서버에 설정할 환경 변수.
  * `env_vars` (선택): 허용·전달할 환경 변수.
  * `cwd` (선택): 서버 시작 시 사용할 작업 디렉터리.



#### 스트리밍 가능한 HTTP 서버

  * `url` (필수): 서버 주소.
  * `bearer_token_env_var` (선택): `Authorization`에 보낼 베어러 토큰용 환경 변수 이름.
  * `http_headers` (선택): 헤더 이름과 정적 값의 매핑.
  * `env_http_headers` (선택): 헤더 이름과 환경 변수 이름의 매핑(값은 환경에서 가져옴).



#### 기타 구성 옵션

  * `startup_timeout_sec` (선택): 서버 시작 제한 시간(초). 기본값: `10`.
  * `tool_timeout_sec` (선택): 서버가 도구를 실행하는 제한 시간(초). 기본값: `60`.
  * `enabled` (선택): 서버를 삭제하지 않고 비활성화하려면 `false`.
  * `required` (선택): 활성 서버가 초기화되지 않으면 시작을 실패하게 하려면 `true`.
  * `enabled_tools` (선택): 허용할 도구 목록.
  * `disabled_tools` (선택): 거부할 도구 목록(`enabled_tools` 적용 후 평가).



OAuth 공급자가 고정 콜백 URI를 요구하면 `config.toml`의 최상위 `mcp_oauth_callback_port`를 설정하세요. 설정하지 않으면 Codex는 임시 포트에 바인딩합니다.

#### config.toml 예시
[code] 
    [mcp_servers.context7]
    command = "npx"
    args = ["-y", "@upstash/context7-mcp"]
    
    [mcp_servers.context7.env]
    MY_ENV_VAR = "MY_ENV_VALUE"
[/code]
[code] 
    [mcp_servers.figma]
    url = "https://mcp.figma.com/mcp"
    bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
[/code]

http_headers = { "X-Figma-Region" = "us-east-1" }
[/code]
[code] 
    [mcp_servers.chrome_devtools]
    url = "http://localhost:3000/mcp"
    enabled_tools = ["open", "screenshot"]
    disabled_tools = ["screenshot"] # applied after enabled_tools
    startup_timeout_sec = 20
    tool_timeout_sec = 45
    enabled = true
[/code]

## 유용한 MCP 서버 예시

MCP 서버 목록은 계속 늘어나고 있습니다. 아래는 자주 쓰이는 몇 가지 예시입니다:

  * [OpenAI Docs MCP](https://developers.openai.com/resources/docs-mcp): OpenAI 개발자 문서를 검색하고 읽습니다.
  * [Context7](https://github.com/upstash/context7): 최신 개발자 문서에 연결합니다.
  * Figma [Local](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) 및 [Remote](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Figma 디자인에 접근합니다.
  * [Playwright](https://www.npmjs.com/package/@playwright/mcp): Playwright를 사용해 브라우저를 제어하고 검사합니다.
  * [Chrome Developer Tools](https://github.com/ChromeDevTools/chrome-devtools-mcp/): Chrome을 제어하고 검사합니다.
  * [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex): Sentry 로그에 접근합니다.
  * [GitHub](https://github.com/github/github-mcp-server): `git`이 지원하지 않는 작업(예: 풀 리퀘스트와 이슈)을 포함해 GitHub을 관리합니다.
