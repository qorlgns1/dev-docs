---
title: '모델 컨텍스트 프로토콜'
description: '모델 컨텍스트 프로토콜(MCP)은 모델을 도구와 컨텍스트에 연결합니다. Codex가 서드파티 문서에 접근하도록 하거나 브라우저나 Figma 같은 개발자 도구와 상호작용하게 하는 데 사용하세요.'
---

Source URL: https://developers.openai.com/codex/mcp

# 모델 컨텍스트 프로토콜

모델 컨텍스트 프로토콜(MCP)은 모델을 도구와 컨텍스트에 연결합니다. Codex가 서드파티 문서에 접근하도록 하거나 브라우저나 Figma 같은 개발자 도구와 상호작용하게 하는 데 사용하세요.

Codex는 CLI와 IDE 확장 양쪽에서 MCP 서버를 지원합니다.

## 지원되는 MCP 기능

- **STDIO 서버**: 로컬 프로세스(명령으로 시작되는)로 실행되는 서버입니다.
  - 환경 변수
- **스트리밍 HTTP 서버**: 주소로 접근하는 서버입니다.
  - Bearer 토큰 인증
  - OAuth 인증 (`codex mcp login <server-name>` 명령을 지원하는 서버의 경우)

## Codex를 MCP 서버에 연결하기

Codex는 다른 Codex 설정과 함께 `config.toml`에 MCP 구성을 저장합니다. 기본적으로는 `~/.codex/config.toml`이지만, 트러스트된 프로젝트의 `.codex/config.toml`에 프로젝트 범위로 MCP 서버를 설정할 수도 있습니다.

CLI와 IDE 확장은 이 구성을 공유합니다. MCP 서버를 구성한 후에는 설정을 다시 하지 않고도 두 Codex 클라이언트 사이를 전환할 수 있습니다.

MCP 서버를 구성하려면 아래 옵션 중 하나를 선택하세요:

1. **CLI 사용**: `codex mcp`를 실행하여 서버를 추가하거나 관리합니다.
2. **`config.toml` 편집**: `~/.codex/config.toml`(또는 트러스트된 프로젝트에서는 프로젝트 범위의 `.codex/config.toml`)을 직접 수정합니다.

### CLI로 구성하기

#### MCP 서버 추가

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>
```

예를 들어 Context7(개발자 문서를 위한 무료 MCP 서버)을 추가하려면 다음 명령을 실행할 수 있습니다:

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

#### 기타 CLI 명령

사용 가능한 MCP 명령 전체를 보려면 `codex mcp --help`를 실행하세요.

#### 터미널 UI(TUI)

`codex` TUI에서는 `/mcp`를 입력하여 활성 MCP 서버를 확인하세요.

### config.toml로 구성하기

MCP 서버 옵션을 더 세밀하게 제어하려면 `~/.codex/config.toml`(또는 프로젝트 범위 `.codex/config.toml`)을 편집하세요. IDE 확장에서는 톱니바퀴 메뉴에서 **MCP 설정** > **config.toml 열기**를 선택합니다.

설정 파일에서 각 MCP 서버를 `[mcp_servers.<server-name>]` 테이블로 구성합니다.

#### STDIO 서버

- `command`(필수): 서버를 시작하는 명령입니다.
- `args`(선택): 서버에 전달할 인수입니다.
- `env`(선택): 서버를 위한 환경 변수입니다.
- `env_vars`(선택): 허용하고 전달할 환경 변수입니다.
- `cwd`(선택): 서버를 시작할 작업 디렉터리입니다.

#### 스트리밍 HTTP 서버

- `url`(필수): 서버 주소입니다.
- `bearer_token_env_var`(선택): `Authorization`에 보낼 Bearer 토큰을 위한 환경 변수 이름입니다.
- `http_headers`(선택): 헤더 이름과 고정 값을 매핑합니다.
- `env_http_headers`(선택): 헤더 이름과 환경 변수 이름을 매핑합니다(값은 환경에서 가져옴).

#### 기타 구성 옵션

- `startup_timeout_sec`(선택): 서버 시작 타임아웃(초). 기본값: `10`.
- `tool_timeout_sec`(선택): 서버가 도구를 실행하는 타임아웃(초). 기본값: `60`.
- `enabled`(선택): 서버를 삭제하지 않고 비활성화하려면 `false`로 설정합니다.
- `required`(선택): 이 서버가 활성화되어 있고 초기화되지 않으면 시작을 실패하게 하려면 `true`로 설정합니다.
- `enabled_tools`(선택): 도구 허용 목록입니다.
- `disabled_tools`(선택): 도구 거부 목록입니다(`enabled_tools` 적용 후).

OAuth 공급자가 고정 콜백 URI를 요구하면 `config.toml` 최상위에 `mcp_oauth_callback_port`를 설정하세요. 설정하지 않으면 Codex가 임시 포트에 바인딩합니다.

#### config.toml 예시

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"
```

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }
```

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # enabled_tools 적용 후
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true
```

## 유용한 MCP 서버 사례

MCP 서버 목록은 계속 늘어나고 있습니다. 여기 몇 가지 대표적인 예시입니다:

- [OpenAI Docs MCP](https://developers.openai.com/resources/docs-mcp): OpenAI 개발자 문서를 검색하고 읽기.
- [Context7](https://github.com/upstash/context7): 최신 개발자 문서에 연결하기.
- Figma [로컬](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) 및 [원격](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Figma 디자인에 접근하기.
- [Playwright](https://www.npmjs.com/package/@playwright/mcp): Playwright를 사용해 브라우저를 제어하고 검사하기.
- [Chrome Developer Tools](https://github.com/ChromeDevTools/chrome-devtools-mcp/): Chrome을 제어하고 검사하기.
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex): Sentry 로그에 접근하기.
- [GitHub](https://github.com/github/github-mcp-server): `git`이 지원하지 않는 기능(예: PR 및 이슈)을 관리하기.
