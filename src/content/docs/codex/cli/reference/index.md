---
title: 명령줄 옵션
description: 이 페이지는 문서화된 모든 Codex CLI 명령과 플래그를 나열합니다. 인터랙티브 표를 사용해 키나 설명으로 검색할 수 있습니다. 각 섹션에서 옵션이 안정판인지 실험판인지, 그리고 위험한 조합이 무엇인지 알려 줍니다.
---

# 명령줄 옵션

Source URL: https://developers.openai.com/codex/cli/reference

## 이 레퍼런스를 읽는 방법

이 페이지는 문서화된 모든 Codex CLI 명령과 플래그를 나열합니다. 인터랙티브 표를 사용해 키나 설명으로 검색할 수 있습니다. 각 섹션에서 옵션이 안정판인지 실험판인지, 그리고 위험한 조합이 무엇인지 알려 줍니다.

CLI는 대부분의 기본값을 `~/.codex/config.toml`에서 상속합니다. 명령줄에서 전달하는 `-c key=value` 재정의가 해당 실행 동안 우선합니다. 자세한 내용은 [Config basics](https://developers.openai.com/codex/config-basic#configuration-precedence)를 확인하세요.

## 전역 플래그

Key| Type / Values| Details  
---|---|---  
`--add-dir`| `path`| 기본 워크스페이스와 함께 추가 디렉터리에 대한 쓰기 권한을 부여합니다. 여러 경로가 필요하면 반복 지정하세요.  
`--ask-for-approval, -a`| `untrusted | on-request | never`| Codex가 명령 실행 전에 사용자 승인을 요청하는 타이밍을 제어합니다. `on-failure`는 더 이상 사용하지 않으니 대화형 실행에는 `on-request`, 비대화형 실행에는 `never`를 권장합니다.  
`--cd, -C`| `path`| 에이전트가 요청을 처리하기 전에 사용할 작업 디렉터리를 설정합니다.  
`--config, -c`| `key=value`| 구성 값을 재정의합니다. 가능한 경우 값은 JSON으로 파싱되고, 그렇지 않으면 원문 문자열을 사용합니다.  
`--dangerously-bypass-approvals-and-sandbox, --yolo`| `boolean`| 모든 명령을 승인이나 샌드박싱 없이 실행합니다. 외부적으로 강화된 환경에서만 사용하세요.  
`--disable`| `feature`| 기능 플래그를 강제로 비활성화합니다(`-c features.<name>=false`와 동일). 반복 가능.  
`--enable`| `feature`| 기능 플래그를 강제로 활성화합니다(`-c features.<name>=true`와 동일). 반복 가능.  
`--full-auto`| `boolean`| 로컬 작업 마찰을 줄이는 단축키입니다. `--ask-for-approval on-request`와 `--sandbox workspace-write`를 설정합니다.  
`--image, -i`| `path[,path...]`| 초기 프롬프트에 하나 이상의 이미지 파일을 첨부합니다. 여러 경로는 쉼표로 구분하거나 플래그를 반복하세요.  
`--model, -m`| `string`| 구성에 설정된 모델을 재정의합니다(예: `gpt-5-codex`).  
`--no-alt-screen`| `boolean`| TUI의 대체 화면 모드를 비활성화합니다(이번 실행에서 `tui.alternate_screen`을 덮어씁니다).  
`--oss`| `boolean`| 로컬 오픈소스 모델 공급자를 사용합니다(`-c model_provider="oss"`와 동일). Ollama 실행 여부를 검증합니다.  
`--profile, -p`| `string`| `~/.codex/config.toml`에서 불러올 구성 프로필 이름입니다.  
`--sandbox, -s`| `read-only | workspace-write | danger-full-access`| 모델이 생성한 셸 명령에 적용할 샌드박스 정책을 선택합니다.  
`--search`| `boolean`| 실시간 웹 검색을 활성화합니다(기본 `"cached"` 대신 `web_search = "live"` 설정).  
`PROMPT`| `string`| 세션 시작 시 선택적으로 제공할 텍스트 지시입니다. 생략하면 미리 채워진 메시지 없이 TUI를 시작합니다.  
  
Key

`--add-dir`

Type / Values

`path`

Details

기본 워크스페이스와 함께 추가 디렉터리에 대한 쓰기 권한을 부여합니다. 여러 경로가 필요하면 반복 지정하세요.

Key

`--ask-for-approval, -a`

Type / Values

`untrusted | on-request | never`

Details

Codex가 명령 실행 전에 사용자 승인을 요청하는 타이밍을 제어합니다. `on-failure`는 더 이상 사용하지 않으니 대화형 실행에는 `on-request`, 비대화형 실행에는 `never`를 권장합니다.

Key

`--cd, -C`

Type / Values

`path`

Details

에이전트가 요청을 처리하기 전에 사용할 작업 디렉터리를 설정합니다.

Key

`--config, -c`

Type / Values

`key=value`

Details

구성 값을 재정의합니다. 가능한 경우 값은 JSON으로 파싱되고, 그렇지 않으면 원문 문자열을 사용합니다.

Key

`--dangerously-bypass-approvals-and-sandbox, --yolo`

Type / Values

`boolean`

Details

모든 명령을 승인이나 샌드박싱 없이 실행합니다. 외부적으로 강화된 환경에서만 사용하세요.

Key

`--disable`

Type / Values

`feature`

Details

기능 플래그를 강제로 비활성화합니다(`-c features.<name>=false`와 동일). 반복 가능.

Key

`--enable`

Type / Values

`feature`

Details

기능 플래그를 강제로 활성화합니다(`-c features.<name>=true`와 동일). 반복 가능.

Key

`--full-auto`

Type / Values

`boolean`

세부 정보

마찰 없는 로컬 작업을 위한 바로 가기: `--ask-for-approval on-request`와 `--sandbox workspace-write`를 설정합니다.

키

`--image, -i`

유형 / 값

`path[,path...]`

세부 정보

초기 프롬프트에 하나 이상의 이미지 파일을 첨부합니다. 여러 경로는 쉼표로 구분하거나 플래그를 반복해 지정합니다.

키

`--model, -m`

유형 / 값

`string`

세부 정보

구성에서 설정된 모델을 재정의합니다(예: `gpt-5-codex`).

키

`--no-alt-screen`

유형 / 값

`boolean`

세부 정보

TUI에 대한 대체 화면 모드를 비활성화합니다(이번 실행에서 `tui.alternate_screen`을 무시).

키

`--oss`

유형 / 값

`boolean`

세부 정보

로컬 오픈 소스 모델 제공자를 사용합니다(`-c model_provider="oss"`와 동일). Ollama가 실행 중인지 확인합니다.

키

`--profile, -p`

유형 / 값

`string`

세부 정보

`~/.codex/config.toml`에서 로드할 구성 프로필 이름입니다.

키

`--sandbox, -s`

유형 / 값

`read-only | workspace-write | danger-full-access`

세부 정보

모델이 생성한 셸 명령에 적용할 샌드박스 정책을 선택합니다.

키

`--search`

유형 / 값

`boolean`

세부 정보

실시간 웹 검색을 활성화합니다(기본값 `"cached"` 대신 `web_search = "live"`로 설정).

키

`PROMPT`

유형 / 값

`string`

세부 정보

세션을 시작할 선택적 텍스트 지시입니다. 생략하면 미리 채워진 메시지 없이 TUI가 시작됩니다.

모두 보려면 펼치기

이 옵션은 기본 `codex` 명령에 적용되며, 아래 섹션에서 별도로 지정하지 않는 한 각 하위 명령에도 전달됩니다. 하위 명령을 실행할 때는 글로벌 플래그를 그 뒤에 배치하세요(예: `codex exec --oss ...`). 그래야 Codex가 의도한 대로 적용합니다.

## Command overview

성숙도 열은 Experimental, Beta, Stable 등 기능 성숙도 라벨을 사용합니다. 해석 방법은 [Feature Maturity](https://developers.openai.com/codex/feature-maturity)를 참고하세요.

키|성숙도|세부 정보  
---|---|---  
[`codex`](https://developers.openai.com/codex/cli/reference#codex-interactive)|Stable|터미널 UI를 실행합니다. 위 글로벌 플래그와 선택적 프롬프트 또는 이미지 첨부를 받습니다.  
[`codex app`](https://developers.openai.com/codex/cli/reference#codex-app)|Stable|macOS에서 Codex 데스크톱 앱을 실행하고, 필요하면 특정 워크스페이스 경로를 엽니다.  
[`codex app-server`](https://developers.openai.com/codex/cli/reference#codex-app-server)|Experimental|로컬 개발 또는 디버깅을 위해 Codex 앱 서버를 실행합니다.  
[`codex apply`](https://developers.openai.com/codex/cli/reference#codex-apply)|Stable|Codex Cloud 작업이 생성한 최신 diff를 로컬 작업 트리에 적용합니다. 별칭: `codex a`.  
[`codex cloud`](https://developers.openai.com/codex/cli/reference#codex-cloud)|Experimental|터미널에서 TUI를 열지 않고 Codex Cloud 작업을 탐색하거나 실행합니다. 별칭: `codex cloud-tasks`.  
[`codex completion`](https://developers.openai.com/codex/cli/reference#codex-completion)|Stable|Bash, Zsh, Fish, PowerShell용 셸 자동 완성 스크립트를 생성합니다.  
[`codex debug app-server send-message-v2`](https://developers.openai.com/codex/cli/reference#codex-debug-app-server-send-message-v2)|Experimental|내장 테스트 클라이언트를 통해 V2 메시지 하나를 보내며 앱 서버를 디버그합니다.  
[`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec)|Stable|Codex를 비대화식으로 실행합니다. 별칭: `codex e`. stdout 또는 JSONL로 결과를 스트리밍하고 이전 세션을 재개할 수 있습니다.  
[`codex execpolicy`](https://developers.openai.com/codex/cli/reference#codex-execpolicy)|Experimental|execpolicy 규칙 파일을 평가하고 명령이 허용, 승인 요청, 차단 중 어느 상태인지 확인합니다.  
[`codex features`](https://developers.openai.com/codex/cli/reference#codex-features)|Stable|기능 플래그를 나열하고 `config.toml`에서 지속적으로 활성화 또는 비활성화합니다.  
[`codex fork`](https://developers.openai.com/codex/cli/reference#codex-fork)|Stable|이전 대화형 세션을 원본 대화를 유지한 채 새 스레드로 포크합니다.

[`codex login`](https://developers.openai.com/codex/cli/reference#codex-login)| 안정| ChatGPT OAuth, 디바이스 인증 또는 stdin으로 전달된 API 키를 사용해 Codex를 인증합니다.  
[`codex logout`](https://developers.openai.com/codex/cli/reference#codex-logout)| 안정| 저장된 인증 자격 증명을 제거합니다.  
[`codex mcp`](https://developers.openai.com/codex/cli/reference#codex-mcp)| 실험적| Model Context Protocol 서버를 관리합니다(목록, 추가, 제거, 인증).  
[`codex mcp-server`](https://developers.openai.com/codex/cli/reference#codex-mcp-server)| 실험적| Codex 자체를 stdio 위에서 MCP 서버로 실행합니다. 다른 에이전트가 Codex를 사용할 때 유용합니다.  
[`codex resume`](https://developers.openai.com/codex/cli/reference#codex-resume)| 안정| ID로 이전 대화형 세션을 이어가거나 가장 최근 대화를 재개합니다.  
[`codex sandbox`](https://developers.openai.com/codex/cli/reference#codex-sandbox)| 실험적| Codex가 제공하는 macOS seatbelt 또는 Linux 샌드박스(기본값 Landlock, 선택적 bubblewrap 파이프라인) 안에서 임의의 명령을 실행합니다.  
  
키

[`codex`](https://developers.openai.com/codex/cli/reference#codex-interactive)

성숙도

안정

세부 정보

터미널 UI를 실행합니다. 위의 전역 플래그와 선택적 프롬프트 또는 이미지 첨부를 받을 수 있습니다.

키

[`codex app`](https://developers.openai.com/codex/cli/reference#codex-app)

성숙도

안정

세부 정보

macOS에서 Codex 데스크톱 앱을 실행하며, 선택적으로 특정 워크스페이스 경로를 열 수 있습니다.

키

[`codex app-server`](https://developers.openai.com/codex/cli/reference#codex-app-server)

성숙도

실험적

세부 정보

로컬 개발 또는 디버깅을 위해 Codex 앱 서버를 실행합니다.

키

[`codex apply`](https://developers.openai.com/codex/cli/reference#codex-apply)

성숙도

안정

세부 정보

Codex Cloud 작업이 생성한 최신 diff를 로컬 작업 트리에 적용합니다. 별칭: `codex a`.

키

[`codex cloud`](https://developers.openai.com/codex/cli/reference#codex-cloud)

성숙도

실험적

세부 정보

TUI를 열지 않고 터미널에서 Codex Cloud 작업을 찾아보거나 실행합니다. 별칭: `codex cloud-tasks`.

키

[`codex completion`](https://developers.openai.com/codex/cli/reference#codex-completion)

성숙도

안정

세부 정보

Bash, Zsh, Fish, 또는 PowerShell용 셸 자동 완성 스크립트를 생성합니다.

키

[`codex debug app-server send-message-v2`](https://developers.openai.com/codex/cli/reference#codex-debug-app-server-send-message-v2)

성숙도

실험적

세부 정보

내장 테스트 클라이언트를 통해 단일 V2 메시지를 보내 app-server를 디버그합니다.

키

[`codex exec`](https://developers.openai.com/codex/cli/reference#codex-exec)

성숙도

안정

세부 정보

Codex를 비대화형으로 실행합니다. 별칭: `codex e`. 결과를 stdout 또는 JSONL로 스트리밍하고, 선택적으로 이전 세션을 재개합니다.

키

[`codex execpolicy`](https://developers.openai.com/codex/cli/reference#codex-execpolicy)

성숙도

실험적

세부 정보

execpolicy 규칙 파일을 평가하고 명령이 허용, 프롬프트, 차단 중 무엇인지 확인합니다.

키

[`codex features`](https://developers.openai.com/codex/cli/reference#codex-features)

성숙도

안정

세부 정보

피처 플래그를 나열하고 `config.toml`에서 지속적으로 활성화 또는 비활성화합니다.

키

[`codex fork`](https://developers.openai.com/codex/cli/reference#codex-fork)

성숙도

안정

세부 정보

이전 대화형 세션을 새로운 스레드로 포크하여 원본 대화 기록을 보존합니다.

키

[`codex login`](https://developers.openai.com/codex/cli/reference#codex-login)

성숙도

안정

세부 정보

ChatGPT OAuth, 디바이스 인증 또는 stdin으로 전달된 API 키를 사용해 Codex를 인증합니다.

키

[`codex logout`](https://developers.openai.com/codex/cli/reference#codex-logout)

성숙도

안정

세부 정보

저장된 인증 자격 증명을 제거합니다.

키

[`codex mcp`](https://developers.openai.com/codex/cli/reference#codex-mcp)

성숙도

실험적

세부 정보

Model Context Protocol 서버를 관리합니다(목록, 추가, 제거, 인증).

키

[`codex mcp-server`](https://developers.openai.com/codex/cli/reference#codex-mcp-server)

성숙도

실험적

세부정보

Codex를 stdio 상의 MCP 서버로 직접 실행합니다. 다른 에이전트가 Codex를 사용할 때 유용합니다.

키

[`codex resume`](https://developers.openai.com/codex/cli/reference#codex-resume)

성숙도

안정적

세부정보

이전 대화형 세션 ID를 지정하거나 가장 최근 대화를 다시 이어갑니다.

키

[`codex sandbox`](https://developers.openai.com/codex/cli/reference#codex-sandbox)

성숙도

실험적

세부정보

Codex가 제공하는 macOS seatbelt 또는 Linux 샌드박스(Landlock 기본, 선택적 bubblewrap 파이프라인) 안에서 임의 명령을 실행합니다.

모두 보려면 확장

## 명령 세부정보

### `codex` (대화형)

하위 명령 없이 `codex`를 실행하면 대화형 터미널 UI(TUI)가 시작됩니다. 에이전트는 위에 나온 전역 플래그와 이미지 첨부를 수락합니다. 웹 검색은 기본적으로 캐시 모드이며, `--search`로 실시간 브라우징으로 전환하고 `--full-auto`로 대부분의 명령을 프롬프트 없이 Codex가 실행하도록 할 수 있습니다.

### `codex app-server`

Codex 앱 서버를 로컬에서 실행합니다. 주로 개발 및 디버깅용이며 예고 없이 변경될 수 있습니다.

키| 유형 / 값| 세부정보  
---|---|---  
`--listen`| `stdio:// | ws://IP:PORT`| Transport listener URL입니다. `ws://`는 실험적이며 개발/테스트용입니다.  
  
키

`--listen`

유형 / 값

`stdio:// | ws://IP:PORT`

세부정보

Transport listener URL입니다. `ws://`는 실험적이며 개발/테스트용입니다.

`codex app-server --listen stdio://`는 기본 JSONL-over-stdio 동작을 유지합니다. `--listen ws://IP:PORT`는 WebSocket 전송(실험적)을 활성화합니다. 클라이언트 바인딩용 스키마를 생성할 때는 제한된 필드와 메서드를 포함하려면 `--experimental`을 추가하세요.

### `codex app`

터미널에서 macOS용 Codex Desktop을 실행하고, 선택적으로 특정 워크스페이스 경로를 엽니다.

키| 유형 / 값| 세부정보  
---|---|---  
`--download-url`| `url`| Codex 데스크톱 DMG 다운로드 URL을 설치 시 강제로 지정하는 고급 옵션입니다.  
`PATH`| `path`| Codex Desktop에서 열 워크스페이스 경로입니다(`codex app`은 macOS에서만 사용 가능).  
  
키

`--download-url`

유형 / 값

`url`

세부정보

Codex 데스크톱 DMG 다운로드 URL을 설치 시 강제로 지정하는 고급 옵션입니다.

키

`PATH`

유형 / 값

`path`

세부정보

Codex Desktop에서 열 워크스페이스 경로입니다(`codex app`은 macOS에서만 사용 가능).

`codex app`은 macOS에서 데스크톱 앱을 설치/실행한 뒤 제공된 워크스페이스 경로를 엽니다. 이 하위 명령은 macOS 전용입니다.

### `codex debug app-server send-message-v2`

내장된 app-server 테스트 클라이언트를 사용해 app-server의 V2 thread/turn 흐름으로 메시지 하나를 전송합니다.

키| 유형 / 값| 세부정보  
---|---|---  
`USER_MESSAGE`| `string`| 내장 V2 테스트 클라이언트 흐름을 통해 app-server로 전송할 메시지 텍스트입니다.  
  
키

`USER_MESSAGE`

유형 / 값

`string`

세부정보

내장 V2 테스트 클라이언트 흐름을 통해 app-server로 전송할 메시지 텍스트입니다.

이 디버그 흐름은 experimentalApi: true로 초기화되고 스레드를 시작한 뒤 턴을 전송하며 서버 알림을 스트리밍합니다. 로컬에서 app-server 프로토콜 동작을 재현하고 검사하는 데 사용하세요.

### `codex apply`

Codex 클라우드 작업에서 가장 최근의 diff를 로컬 저장소에 적용합니다. 인증되어 있고 작업에 접근할 수 있어야 합니다.

키| 유형 / 값| 세부정보  
---|---|---  
`TASK_ID`| `string`| diff를 적용할 Codex 클라우드 작업 식별자입니다.  
  
키

`TASK_ID`

유형 / 값

`string`

세부정보

diff를 적용할 Codex 클라우드 작업 식별자입니다.

Codex는 패치된 파일을 출력하고 `git apply`가 실패하면(예: 충돌) 0이 아닌 코드로 종료합니다.

### `codex cloud`

터미널에서 Codex 클라우드 작업과 상호작용합니다. 기본 명령은 대화형 선택기를 열고, `codex cloud exec`은 작업을 바로 제출하며, `codex cloud list`는 스크립팅이나 빠른 검토용 최근 작업을 반환합니다.

키| 유형 / 값| 세부정보  
---|---|---  
`--attempts`| `1-4`| Codex Cloud가 실행할 어시스턴트 시도 횟수(최대 N)입니다.

`--env`| `ENV_ID`| 대상 Codex Cloud 환경 식별자(필수). 옵션을 확인하려면 `codex cloud`를 사용하세요.  
`QUERY`| `string`| 작업 프롬프트. 생략하면 Codex가 대화형으로 세부 정보를 요청합니다.  
  
키

`--attempts`

유형 / 값

`1-4`

세부 정보

Codex Cloud가 실행해야 하는 어시스턴트 시도 횟수(best-of-N)입니다.

키

`--env`

유형 / 값

`ENV_ID`

세부 정보

대상 Codex Cloud 환경 식별자(필수). 옵션을 확인하려면 `codex cloud`를 사용하세요.

키

`QUERY`

유형 / 값

`string`

세부 정보

작업 프롬프트. 생략하면 Codex가 대화형으로 세부 정보를 요청합니다.

인증은 기본 CLI와 동일한 자격 증명을 사용합니다. 작업 제출에 실패하면 Codex는 0이 아닌 코드로 종료합니다.

#### `codex cloud list`

필터링과 페이지네이션 옵션을 사용하여 최신 클라우드 작업을 나열합니다.

Key| Type / Values| Details  
---|---|---  
`--cursor`| `string`| 이전 요청에서 반환된 페이지네이션 커서.  
`--env`| `ENV_ID`| 환경 식별자로 작업을 필터링합니다.  
`--json`| `boolean`| 일반 텍스트 대신 기계가 읽을 수 있는 JSON을 출력합니다.  
`--limit`| `1-20`| 반환할 작업의 최대 개수.  
  
키

`--cursor`

유형 / 값

`string`

세부 정보

이전 요청에서 반환된 페이지네이션 커서입니다.

키

`--env`

유형 / 값

`ENV_ID`

세부 정보

환경 식별자로 작업을 필터링합니다.

키

`--json`

유형 / 값

`boolean`

세부 정보

일반 텍스트 대신 기계가 읽을 수 있는 JSON을 출력합니다.

키

`--limit`

유형 / 값

`1-20`

세부 정보

반환할 작업의 최대 개수입니다.

일반 텍스트 출력은 작업 URL과 상태 세부 정보를 순서대로 표시합니다. 자동화에는 `--json`을 사용하세요. JSON 페이로드에는 `tasks` 배열과 선택적 `cursor` 값이 포함됩니다. 각 작업은 `id`, `url`, `title`, `status`, `updated_at`, `environment_id`, `environment_label`, `summary`, `is_review`, `attempt_total`을 담고 있습니다.

### `codex completion`

셸 완성 스크립트를 생성한 뒤 적절한 위치로 리디렉션합니다. 예: `codex completion zsh > "${fpath[1]}/_codex"`.

Key| Type / Values| Details  
---|---|---  
`SHELL`| `bash | zsh | fish | power-shell | elvish`| 완성 스크립트를 생성할 셸. 출력은 stdout에 기록됩니다.  
  
키

`SHELL`

유형 / 값

`bash | zsh | fish | power-shell | elvish`

세부 정보

완성 스크립트를 생성할 셸입니다. 출력은 stdout에 기록됩니다.

### `codex features`

`~/.codex/config.toml`에 저장된 기능 플래그를 관리합니다. `enable`과 `disable` 명령은 변경 사항을 영구적으로 저장하여 이후 세션에도 적용됩니다. `--profile`을 사용해 실행하면 Codex는 루트 구성 대신 해당 프로필에 기록합니다.

Key| Type / Values| Details  
---|---|---  
`Disable subcommand`| `codex features disable <feature>`| `config.toml`에서 기능 플래그를 영구적으로 비활성화합니다. 제공된 경우 활성 `--profile`을 따릅니다.  
`Enable subcommand`| `codex features enable <feature>`| `config.toml`에서 기능 플래그를 영구적으로 활성화합니다. 제공된 경우 활성 `--profile`을 따릅니다.  
`List subcommand`| `codex features list`| 알려진 기능 플래그, 성숙도 단계, 적용 상태를 표시합니다.  
  
키

`Disable subcommand`

유형 / 값

`codex features disable <feature>`

세부 정보

`config.toml`에서 기능 플래그를 영구적으로 비활성화합니다. 제공된 경우 활성 `--profile`을 따릅니다.

키

`Enable subcommand`

유형 / 값

`codex features enable <feature>`

세부 정보

`config.toml`에서 기능 플래그를 영구적으로 활성화합니다. 제공된 경우 활성 `--profile`을 따릅니다.

키

`List subcommand`

유형 / 값

`codex features list`

세부 정보

알려진 기능 플래그, 성숙도 단계, 적용 상태를 표시합니다.

### `codex exec`

사람의 개입 없이 완료되어야 하는 스크립트형 또는 CI 스타일 실행에는 `codex exec`(약칭 `codex e`)을 사용하세요.

Key| Type / Values| Details  
---|---|---  
`--cd, -C`| `path`| 작업을 실행하기 전에 워크스페이스 루트를 설정합니다.  
`--color`| `always | never | auto`| stdout ANSI 색상 출력을 제어합니다.

`--dangerously-bypass-approvals-and-sandbox, --yolo`| `boolean`| 승인 프롬프트와 샌드박스를 우회합니다. 위험하므로 격리된 러너에서만 사용하세요.  
`--ephemeral`| `boolean`| 세션 롤아웃 파일을 디스크에 남기지 않고 실행합니다.  
`--full-auto`| `boolean`| 저마찰 자동화 프리셋을 적용합니다 (`workspace-write` 샌드박스와 `on-request` 승인).  
`--image, -i`| `path[,path...]`| 첫 번째 메시지에 이미지를 첨부합니다. 반복 가능하며 쉼표로 구분된 목록을 지원합니다.  
`--json, --experimental-json`| `boolean`| 서식 있는 텍스트 대신 줄바꿈으로 구분된 JSON 이벤트를 출력합니다.  
`--model, -m`| `string`| 이 실행에 사용할 모델을 재정의합니다.  
`--oss`| `boolean`| 로컬 오픈 소스 제공자를 사용합니다(실행 중인 Ollama 인스턴스 필요).  
`--output-last-message, -o`| `path`| 어시스턴트의 마지막 메시지를 파일로 기록합니다. 다운스트림 스크립팅에 유용합니다.  
`--output-schema`| `path`| 예상되는 최종 응답 형태를 설명하는 JSON 스키마 파일입니다. Codex가 도구 출력을 이에 맞춰 검증합니다.  
`--profile, -p`| `string`| config.toml에 정의된 구성 프로파일을 선택합니다.  
`--sandbox, -s`| `read-only | workspace-write | danger-full-access`| 모델이 생성한 명령의 샌드박스 정책입니다. 기본값은 구성에 따릅니다.  
`--skip-git-repo-check`| `boolean`| Git 저장소 외부에서 실행을 허용합니다(단발성 디렉터리에 유용).  
`-c, --config`| `key=value`| 비대화형 실행에 대한 인라인 구성 재정의입니다(반복 가능).  
`PROMPT`| `string | - (read stdin)`| 작업의 초기 지시입니다. `-`를 사용하면 stdin에서 프롬프트를 파이프할 수 있습니다.  
`Resume subcommand`| `codex exec resume [SESSION_ID]`| ID로 exec 세션을 재개하거나 `--last`를 추가해 현재 작업 디렉터리의 가장 최근 세션을 이어갑니다. `--all`을 추가하면 모든 디렉터리의 세션을 고려합니다. 선택적 후속 프롬프트를 허용합니다.  
  
키

`--cd, -C`

유형 / 값

`path`

세부 정보

작업을 실행하기 전에 워크스페이스 루트를 설정합니다.

키

`--color`

유형 / 값

`always | never | auto`

세부 정보

stdout의 ANSI 색상을 제어합니다.

키

`--dangerously-bypass-approvals-and-sandbox, --yolo`

유형 / 값

`boolean`

세부 정보

승인 프롬프트와 샌드박스를 우회합니다. 위험하므로 격리된 러너에서만 사용하세요.

키

`--ephemeral`

유형 / 값

`boolean`

세부 정보

세션 롤아웃 파일을 디스크에 남기지 않고 실행합니다.

키

`--full-auto`

유형 / 값

`boolean`

세부 정보

저마찰 자동화 프리셋을 적용합니다 (`workspace-write` 샌드박스와 `on-request` 승인).

키

`--image, -i`

유형 / 값

`path[,path...]`

세부 정보

첫 번째 메시지에 이미지를 첨부합니다. 반복 가능하며 쉼표로 구분된 목록을 지원합니다.

키

`--json, --experimental-json`

유형 / 값

`boolean`

세부 정보

서식 있는 텍스트 대신 줄바꿈으로 구분된 JSON 이벤트를 출력합니다.

키

`--model, -m`

유형 / 값

`string`

세부 정보

이 실행에 사용할 모델을 재정의합니다.

키

`--oss`

유형 / 값

`boolean`

세부 정보

로컬 오픈 소스 제공자를 사용합니다(실행 중인 Ollama 인스턴스 필요).

키

`--output-last-message, -o`

유형 / 값

`path`

세부 정보

어시스턴트의 마지막 메시지를 파일로 기록합니다. 다운스트림 스크립팅에 유용합니다.

키

`--output-schema`

유형 / 값

`path`

세부 정보

예상되는 최종 응답 형태를 설명하는 JSON 스키마 파일입니다. Codex가 도구 출력을 이에 맞춰 검증합니다.

키

`--profile, -p`

유형 / 값

`string`

세부 정보

config.toml에 정의된 구성 프로파일을 선택합니다.

키

`--sandbox, -s`

유형 / 값

`read-only | workspace-write | danger-full-access`

세부 정보

모델이 생성한 명령의 샌드박스 정책입니다. 기본값은 구성에 따릅니다.

키

`--skip-git-repo-check`

유형 / 값

`boolean`

세부 정보

Git 저장소 외부에서 실행을 허용합니다(단발성 디렉터리에 유용).

키

`-c, --config`

유형 / 값

`key=value`

세부 정보

비대화형 실행에 대한 인라인 구성 재정의입니다(반복 가능).

키

`PROMPT`

유형 / 값

`string | - (read stdin)`

세부 정보

작업의 초기 지시입니다. `-`를 사용하면 stdin에서 프롬프트를 파이프할 수 있습니다.

키

`Resume subcommand`

유형 / 값

`codex exec resume [SESSION_ID]`

세부 정보

ID로 exec 세션을 재개하거나 `--last`를 추가해 현재 작업 디렉터리에서 가장 최근 세션을 이어서 진행합니다. `--all`을 추가하면 모든 디렉터리의 세션을 고려합니다. 선택적으로 후속 프롬프트를 전달할 수 있습니다.

모두 보기로 확장

Codex는 기본적으로 서식이 적용된 출력을 제공합니다. 상태 변경마다 한 줄의 JSON 이벤트를 받으려면 `--json`을 추가하세요. 선택적 `resume` 하위 명령어는 비대화식 작업을 계속할 수 있게 합니다. `--last`로 현재 작업 디렉터리의 가장 최근 세션을 선택하거나 `--all`을 추가해 모든 세션을 검색합니다:

Key| Type / Values| Details  
---|---|---  
`--all`| `boolean`| 가장 최근 세션을 선택할 때 현재 작업 디렉터리 밖의 세션도 포함합니다.  
`--image, -i`| `path[,path...]`| 후속 프롬프트에 하나 이상의 이미지를 첨부합니다. 여러 경로는 쉼표로 구분하거나 플래그를 반복하세요.  
`--last`| `boolean`| 현재 작업 디렉터리에서 가장 최근의 대화를 재개합니다.  
`PROMPT`| `string | - (read stdin)`| 재개 직후 즉시 전송되는 선택적 후속 지시문입니다.  
`SESSION_ID`| `uuid`| 지정한 세션을 재개합니다. 생략하고 `--last`를 사용하면 가장 최근 세션을 이어갑니다.  
  
Key

`--all`

Type / Values

`boolean`

Details

가장 최근 세션을 선택할 때 현재 작업 디렉터리 밖의 세션을 포함합니다.

Key

`--image, -i`

Type / Values

`path[,path...]`

Details

후속 프롬프트에 하나 이상의 이미지를 첨부합니다. 여러 경로는 쉼표로 구분하거나 플래그를 반복하세요.

Key

`--last`

Type / Values

`boolean`

Details

현재 작업 디렉터리에서 가장 최근의 대화를 재개합니다.

Key

`PROMPT`

Type / Values

`string | - (read stdin)`

Details

재개 직후 즉시 전송되는 선택적 후속 지시문입니다.

Key

`SESSION_ID`

Type / Values

`uuid`

Details

지정한 세션을 재개합니다. 생략하고 `--last`를 사용하면 가장 최근 세션을 이어갑니다.

### `codex execpolicy`

저장하기 전에 `execpolicy` 규칙 파일을 확인하세요. `codex execpolicy check`는 하나 이상의 `--rules` 플래그(예: `~/.codex/rules` 아래의 파일)를 받고, 가장 엄격한 결정과 일치한 규칙을 보여주는 JSON을 출력합니다. `--pretty`를 추가하면 출력 서식을 정리합니다. `execpolicy` 명령은 현재 프리뷰 상태입니다.

Key| Type / Values| Details  
---|---|---  
`--pretty`| `boolean`| JSON 결과를 보기 좋게 출력합니다.  
`--rules, -r`| `path (repeatable)`| 평가할 execpolicy 규칙 파일 경로입니다. 여러 플래그를 제공해 파일 간 규칙을 결합하세요.  
`COMMAND...`| `var-args`| 지정된 정책에 대해 확인할 명령입니다.  
  
Key

`--pretty`

Type / Values

`boolean`

Details

JSON 결과를 보기 좋게 출력합니다.

Key

`--rules, -r`

Type / Values

`path (repeatable)`

Details

평가할 execpolicy 규칙 파일 경로입니다. 여러 플래그를 제공해 파일 간 규칙을 결합하세요.

Key

`COMMAND...`

Type / Values

`var-args`

Details

지정된 정책에 대해 확인할 명령입니다.

### `codex login`

ChatGPT 계정 또는 API 키로 CLI를 인증합니다. 플래그 없이 실행하면 Codex가 ChatGPT OAuth 흐름을 위한 브라우저를 엽니다.

Key| Type / Values| Details  
---|---|---  
`--device-auth`| `boolean`| 브라우저 창을 여는 대신 OAuth 디바이스 코드 흐름을 사용합니다.  
`--with-api-key`| `boolean`| stdin에서 API 키를 읽습니다(예: `printenv OPENAI_API_KEY | codex login --with-api-key`).  
`status subcommand`| `codex login status`| 활성 인증 모드를 출력하고 로그인되어 있으면 0으로 종료합니다.  
  
Key

`--device-auth`

Type / Values

`boolean`

Details

브라우저 창을 열지 않고 OAuth 디바이스 코드 흐름을 사용합니다.

Key

`--with-api-key`

Type / Values

`boolean`

Details

stdin에서 API 키를 읽습니다(예: `printenv OPENAI_API_KEY | codex login --with-api-key`).

Key

`status subcommand`

Type / Values

`codex login status`

Details

활성 인증 모드를 출력하고 로그인되어 있으면 0으로 종료합니다.

`codex login status`는 자격 증명이 있을 때 `0`으로 종료하므로 자동화 스크립트에 유용합니다.

### `codex logout`

API 키와 ChatGPT 인증에 대한 저장된 자격 증명을 모두 제거합니다. 이 명령에는 플래그가 없습니다.

### `codex mcp`

`~/.codex/config.toml`에 저장된 Model Context Protocol 서버 엔트리를 관리합니다.

Key|Type / Values|Details  
---|---|---  
`add <name>`|`-- <command...> | --url <value>`|stdio 런처 명령 또는 스트리밍 가능한 HTTP URL을 사용해 서버를 등록합니다. stdio 전송에서는 `--env KEY=VALUE`를 지원합니다.  
`get <name>`|`--json`|지정한 서버 구성을 표시합니다. `--json`은 원시 구성 엔트리를 출력합니다.  
`list`|`--json`|구성된 MCP 서버를 나열합니다. 기계 판독 가능한 출력이 필요하면 `--json`을 추가합니다.  
`login <name>`|`--scopes scope1,scope2`|스트리밍 가능한 HTTP 서버(오직 OAuth를 지원하는 서버)의 OAuth 로그인을 시작합니다.  
`logout <name>`||스트리밍 가능한 HTTP 서버의 저장된 OAuth 자격 증명을 제거합니다.  
`remove <name>`||저장된 MCP 서버 정의를 삭제합니다.  
  
Key

`add <name>`

Type / Values

`-- <command...> | --url <value>`

Details

stdio 런처 명령 또는 스트리밍 가능한 HTTP URL을 사용해 서버를 등록합니다. stdio 전송에서는 `--env KEY=VALUE`를 지원합니다.

Key

`get <name>`

Type / Values

`--json`

Details

지정한 서버 구성을 표시합니다. `--json`은 원시 구성 엔트리를 출력합니다.

Key

`list`

Type / Values

`--json`

Details

구성된 MCP 서버를 나열합니다. 기계 판독 가능한 출력이 필요하면 `--json`을 추가합니다.

Key

`login <name>`

Type / Values

`--scopes scope1,scope2`

Details

스트리밍 가능한 HTTP 서버(오직 OAuth를 지원하는 서버)의 OAuth 로그인을 시작합니다.

Key

`logout <name>`

Details

스트리밍 가능한 HTTP 서버의 저장된 OAuth 자격 증명을 제거합니다.

Key

`remove <name>`

Details

저장된 MCP 서버 정의를 삭제합니다.

`add` 하위 명령은 stdio와 스트리밍 가능한 HTTP 전송 방식을 모두 지원합니다:

Key|Type / Values|Details  
---|---|---  
`--bearer-token-env-var`|`ENV_VAR`|스트리밍 가능한 HTTP 서버에 연결할 때 베어러 토큰으로 전송할 환경 변수 이름입니다.  
`--env KEY=VALUE`|`repeatable`|stdio 서버를 실행할 때 적용할 환경 변수 할당입니다.  
`--url`|`https://…`|stdio 대신 스트리밍 가능한 HTTP 서버를 등록합니다. `COMMAND...`와는 상호 배타적입니다.  
`COMMAND...`|`stdio transport`|MCP 서버를 실행할 실행 파일과 인수를 의미합니다. `--` 이후에 제공합니다.  
  
Key

`--bearer-token-env-var`

Type / Values

`ENV_VAR`

Details

스트리밍 가능한 HTTP 서버에 연결할 때 베어러 토큰으로 전송할 환경 변수 이름입니다.

Key

`--env KEY=VALUE`

Type / Values

`repeatable`

Details

stdio 서버를 실행할 때 적용할 환경 변수 할당입니다.

Key

`--url`

Type / Values

`https://…`

Details

stdio 대신 스트리밍 가능한 HTTP 서버를 등록합니다. `COMMAND...`와는 상호 배타적입니다.

Key

`COMMAND...`

Type / Values

`stdio transport`

Details

MCP 서버를 실행할 실행 파일과 인수를 의미합니다. `--` 이후에 제공합니다.

OAuth 작업(`login`, `logout`)은 스트리밍 가능한 HTTP 서버(그리고 해당 서버가 OAuth를 지원하는 경우)에만 작동합니다.

### `codex mcp-server`

다른 도구가 연결할 수 있도록 stdio를 통해 Codex를 MCP 서버로 실행합니다. 이 명령은 전역 구성 재정의를 상속하며, 하위 클라이언트가 연결을 닫으면 종료합니다.

### `codex resume`

ID로 인터랙티브 세션을 계속하거나 가장 최근 대화를 다시 시작합니다. `codex resume`은 `--all`을 전달하지 않는 한 `--last`의 범위를 현재 작업 디렉터리로 제한합니다. 모델 및 샌드박스 재정의를 포함해 `codex`와 동일한 전역 플래그를 받습니다.

Key|Type / Values|Details  
---|---|---  
`--all`|`boolean`|가장 최근 세션을 선택할 때 현재 작업 디렉터리 밖의 세션까지 포함합니다.  
`--last`|`boolean`|선택기를 건너뛰고 현재 작업 디렉터리에서 가장 최근 대화를 다시 시작합니다.  
`SESSION_ID`|`uuid`|지정한 세션을 다시 시작합니다. 생략하고 `--last`를 사용하면 가장 최근 세션을 이어갑니다.  
  
Key

`--all`

Type / Values

`boolean`

Details

가장 최근 세션을 선택할 때 현재 작업 디렉터리 밖의 세션까지 포함합니다.

Key

`--last`

유형 / 값

`boolean`

세부 사항

선택기를 건너뛰고 현재 작업 디렉터리에서 가장 최근 대화를 다시 시작합니다.

키

`SESSION_ID`

유형 / 값

`uuid`

세부 사항

지정된 세션을 다시 시작합니다. 생략하고 `--last`를 사용하면 가장 최근 세션을 이어갈 수 있습니다.

### `codex fork`

이전에 실행한 대화형 세션을 새 스레드로 포크합니다. 기본적으로 `codex fork`는 세션 선택기를 열며, 가장 최근 세션을 즉시 포크하려면 `--last`를 추가합니다.

키| 유형 / 값| 세부 사항  
---|---|---  
`--all`| `boolean`| 현재 작업 디렉터리 밖의 세션도 선택기에 표시합니다.  
`--last`| `boolean`| 선택기를 건너뛰고 가장 최근 대화를 자동으로 포크합니다.  
`SESSION_ID`| `uuid`| 지정된 세션을 포크합니다. 생략하고 `--last`를 사용하면 가장 최근 세션을 포크합니다.  
  
키

`--all`

유형 / 값

`boolean`

세부 사항

현재 작업 디렉터리 밖의 세션도 선택기에 표시합니다.

키

`--last`

유형 / 값

`boolean`

세부 사항

선택기를 건너뛰고 가장 최근 대화를 자동으로 포크합니다.

키

`SESSION_ID`

유형 / 값

`uuid`

세부 사항

지정된 세션을 포크합니다. 생략하고 `--last`를 사용하면 가장 최근 세션을 포크합니다.

### `codex sandbox`

Codex가 내부적으로 사용하는 것과 동일한 정책으로 명령을 실행하는 샌드박스 도우미를 사용합니다.

#### macOS Seatbelt

키| 유형 / 값| 세부 사항  
---|---|---  
`--config, -c`| `key=value`| 샌드박스 실행에 구성 재정의를 전달합니다(반복 가능).  
`--full-auto`| `boolean`| 현재 워크스페이스와 `/tmp`에 대한 쓰기 권한을 승인 없이 부여합니다.  
`COMMAND...`| `var-args`| macOS Seatbelt에서 실행할 셸 명령입니다. `--` 이후 모든 인수가 전달됩니다.  
  
키

`--config, -c`

유형 / 값

`key=value`

세부 사항

샌드박스 실행에 구성 재정의를 전달합니다(반복 가능).

키

`--full-auto`

유형 / 값

`boolean`

세부 사항

현재 워크스페이스와 `/tmp`에 대한 쓰기 권한을 승인 없이 부여합니다.

키

`COMMAND...`

유형 / 값

`var-args`

세부 사항

macOS Seatbelt에서 실행할 셸 명령입니다. `--` 이후 모든 인수가 전달됩니다.

#### Linux Landlock

키| 유형 / 값| 세부 사항  
---|---|---  
`--config, -c`| `key=value`| 샌드박스를 시작하기 전에 적용할 구성 재정의입니다(반복 가능).  
`--full-auto`| `boolean`| Landlock 샌드박스 내에서 현재 워크스페이스와 `/tmp`에 대한 쓰기 권한을 부여합니다.  
`COMMAND...`| `var-args`| Landlock + seccomp에서 실행할 명령입니다. `--` 뒤에 실행 파일을 제공합니다.  
  
키

`--config, -c`

유형 / 값

`key=value`

세부 사항

샌드박스를 시작하기 전에 적용할 구성 재정의입니다(반복 가능).

키

`--full-auto`

유형 / 값

`boolean`

세부 사항

Landlock 샌드박스 내에서 현재 워크스페이스와 `/tmp`에 대한 쓰기 권한을 부여합니다.

키

`COMMAND...`

유형 / 값

`var-args`

세부 사항

Landlock + seccomp에서 실행할 명령입니다. `--` 뒤에 실행 파일을 제공합니다.

## 플래그 조합 및 안전 팁

  * 로컬 무인 작업에는 `--full-auto`를 설정하되, 전용 샌드박스 VM이 아니라면 `--dangerously-bypass-approvals-and-sandbox`와 함께 사용하지 마세요.
  * Codex에 더 많은 디렉터리에 대한 쓰기 권한을 부여해야 한다면 `--sandbox danger-full-access`를 강제하기보다 `--add-dir`을 사용하는 것이 좋습니다.
  * CI에서 `--json`은 `--output-last-message`와 함께 사용하면 기계 판독 가능한 진행 상태와 마지막 자연어 요약을 모두 캡처할 수 있습니다.

## 관련 리소스

  * [Codex CLI 개요](https://developers.openai.com/codex/cli): 설치, 업그레이드, 빠른 팁.
  * [Config 기본](https://developers.openai.com/codex/config-basic): 모델과 공급자를 비롯한 기본값을 지속적으로 관리합니다.
  * [고급 Config](https://developers.openai.com/codex/config-advanced): 프로필, 공급자, 샌드박스 튜닝, 통합.
  * [AGENTS.md](https://developers.openai.com/codex/guides/agents-md): Codex 에이전트 기능과 모범 사례에 대한 개념적 개요.
