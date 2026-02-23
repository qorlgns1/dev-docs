---
title: 'OpenAI 인증'
description: 'Codex는 OpenAI 모델 사용 시 두 가지 로그인 방법을 제공합니다:'
---

출처 URL: https://developers.openai.com/codex/auth

# 인증

## OpenAI 인증

Codex는 OpenAI 모델 사용 시 두 가지 로그인 방법을 제공합니다:

- 구독 액세스를 위해 ChatGPT로 로그인
- 사용량 기반 액세스를 위해 API 키로 로그인

Codex 클라우드는 ChatGPT 로그인을 요구합니다. Codex CLI와 IDE 확장은 두 가지 로그인 방법을 모두 지원합니다.

### ChatGPT로 로그인

Codex 앱, CLI 또는 IDE 확장에서 ChatGPT로 로그인하면 브라우저 창이 열려 로그인 흐름을 완료하게 됩니다. 로그인 후 브라우저는 CLI나 IDE 확장으로 액세스 토큰을 반환합니다.

### API 키로 로그인

Codex 앱, CLI 또는 IDE 확장에 API 키로 로그인할 수도 있습니다. API 키는 [OpenAI 대시보드](https://platform.openai.com/api-keys)에서 받으세요.

OpenAI는 API 키 사용량을 표준 API 요율로 OpenAI 플랫폼 계정에 청구합니다. 자세한 내용은 [API 요금 페이지](https://openai.com/api/pricing/)를 참고하세요.

## Codex 클라우드 계정 보안 강화

Codex 클라우드는 코드베이스와 직접 상호작용하므로 많은 다른 ChatGPT 기능보다 더 강력한 보안이 필요합니다. 다중 요소 인증(MFA)을 활성화하세요.

소셜 로그인 제공자(Google, Microsoft, Apple)를 사용하는 경우 ChatGPT 계정에서 MFA를 반드시 활성화할 필요는 없지만, 소셜 로그인 제공자 쪽에서 설정할 수 있습니다.

설정 방법은 다음 링크를 참고하세요:

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

조직의 싱글 사인온(SSO)을 통해 ChatGPT에 접근한다면, 조직의 SSO 관리자가 모든 사용자에게 MFA를 의무화해야 합니다.

이메일과 비밀번호로 로그인하는 경우 Codex 클라우드에 액세스하기 전에 반드시 계정에서 MFA를 설정해야 합니다.

계정이 둘 이상의 로그인 방법을 지원하고 그중 하나가 이메일과 비밀번호인 경우, 다른 방법으로 로그인하더라도 Codex에 접근하기 전에 MFA를 설정해야 합니다.

## 로그인 캐싱

ChatGPT 또는 API 키로 Codex 앱, CLI 또는 IDE 확장에 로그인하면, Codex는 로그인 정보를 캐시하여 다음에 CLI 또는 확장을 시작할 때 재사용합니다. CLI와 IDE 확장은 동일한 캐시된 로그인 정보를 공유합니다. 둘 중 하나에서 로그아웃하면 다음에 CLI나 확장을 시작할 때 다시 로그인해야 합니다.

Codex는 `~/.codex/auth.json` 또는 운영체제 전용 자격 증명 저장소에 로그인 정보를 로컬로 평문으로 캐시합니다.

## 자격 증명 저장

`cli_auth_credentials_store`를 사용하여 Codex CLI가 캐시된 자격 증명을 저장할 위치를 제어하세요:

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"
```

- `file`은 `CODEX_HOME`(기본 `~/.codex`) 아래의 `auth.json`에 자격 증명을 저장합니다.
- `keyring`은 운영체제의 자격 증명 저장소에 자격 증명을 저장합니다.
- `auto`는 OS 자격 증명 저장소를 사용 가능할 때 사용하고, 그렇지 않으면 `auth.json`으로 대체합니다.

파일 기반 저장소를 사용할 경우 `~/.codex/auth.json`은 액세스 토큰을 포함하므로 비밀번호처럼 취급하세요. 커밋하지 말고, 티켓에 붙여 넣거나 채팅에서 공유하지 마세요.

## 로그인 방식 또는 워크스페이스 강제 적용

관리되는 환경에서는 관리자가 사용자의 인증 방식을 제한할 수 있습니다:

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"
```

활성 자격 증명이 구성된 제한과 일치하지 않으면 Codex는 사용자를 로그아웃시키고 종료합니다.

이러한 설정은 일반적으로 사용자별 설정이 아니라 관리형 구성으로 적용됩니다. 자세한 내용은 [관리형 구성](https://developers.openai.com/codex/security#managed-configuration)을 참고하세요.

## 헤드리스 장치에서의 로그인

Codex CLI로 ChatGPT에 로그인하는 경우, 브라우저 기반 로그인 UI가 작동하지 않을 수 있는 상황이 있습니다:

- CLI를 원격 또는 헤드리스 환경에서 실행 중인 경우
- 로컬 네트워크 설정이 Codex가 OAuth 토큰을 반환하기 위해 사용하는 localhost 콜백을 차단하는 경우

이 경우 장치 코드 인증(beta)을 사용하는 것이 좋습니다. 대화형 로그인 UI에서 **Sign in with Device Code**를 선택하거나 `codex login --device-auth`를 직접 실행하세요. 장치 코드 인증이 환경에서 작동하지 않으면 다른 대체 방법을 사용하세요.

### 권장: 장치 코드 인증(beta)

1. ChatGPT 보안 설정(개인 계정) 또는 ChatGPT 워크스페이스 권한(워크스페이스 관리자)에서 장치 코드 로그인을 활성화하세요.
2. Codex를 실행 중인 터미널에서 다음 옵션 중 하나를 선택하세요:
   - 대화형 로그인 UI에서 **Sign in with Device Code** 선택
   - `codex login --device-auth` 실행
3. 브라우저에서 링크를 열고 로그인한 후 일회용 코드를 입력하세요.

서버에서 장치 코드 로그인이 활성화되지 않은 경우 Codex는 기본 브라우저 기반 로그인 흐름으로 되돌아갑니다.

### 대체: 로컬에서 인증하고 인증 캐시 복사

브라우저 기반 로그인 흐름을 사용할 수 있는 머신에서 로그인 흐름을 완료한 후 캐시된 자격 증명을 헤드리스 머신으로 복사할 수 있습니다.

1. 브라우저 기반 로그인 흐름을 사용할 수 있는 머신에서 `codex login` 실행
2. 로그인 캐시가 `~/.codex/auth.json`에 존재하는지 확인
3. `~/.codex/auth.json`을 헤드리스 머신의 `~/.codex/auth.json`으로 복사

`~/.codex/auth.json`은 액세스 토큰을 포함하므로 비밀번호처럼 취급하세요. 커밋하거나 티켓에 붙여 넣거나 채팅에서 공유하지 마세요.

운영체제가 `~/.codex/auth.json` 대신 자격 증명 저장소에 자격 증명을 저장하는 경우 이 방법은 적용되지 않을 수 있습니다. 파일 기반 저장소 구성 방법은 [자격 증명 저장](#credential-storage)을 참고하세요.

SSH로 원격 머신에 복사:

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json
```

또는 `scp`를 사용하지 않는 원라이너:

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json
```

Docker 컨테이너로 복사:

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"
```

### 대체: SSH로 localhost 콜백 전달

로컬 머신과 원격 호스트 간에 포트를 전달할 수 있다면 Codex의 로컬 콜백 서버(기본 `localhost:1455`)를 터널링하여 기본 브라우저 흐름을 사용할 수 있습니다.

1. 로컬 머신에서 포트 포워딩 시작:

```shell
ssh -L 1455:localhost:1455 user@remote
```

2. 해당 SSH 세션에서 `codex login`을 실행하고 로컬 머신에 출력된 주소를 따라가세요.

## 대체 모델 제공자

구성 파일에서 [사용자 지정 모델 제공자](https://developers.openai.com/codex/config-advanced#custom-model-providers)를 정의할 때 다음 인증 방법 중 하나를 선택할 수 있습니다:

- **OpenAI 인증**: `requires_openai_auth = true`로 설정하여 OpenAI 인증을 사용합니다. 이후 ChatGPT 또는 API 키로 로그인할 수 있습니다. LLM 프록시 서버를 통해 OpenAI 모델에 접근할 때 유용합니다. `requires_openai_auth = true`인 경우 Codex는 `env_key`를 무시합니다.
- **환경 변수 인증**: `env_key = "<ENV_VARIABLE_NAME>"`로 설정하여 로컬 환경 변수 `<ENV_VARIABLE_NAME>`에 저장된 공급자 전용 API 키를 사용합니다.
- **인증 없음**: `requires_openai_auth`를 설정하지 않거나 `false`로 설정하고 `env_key`도 설정하지 않는 경우, Codex는 공급자가 인증을 요구하지 않는다고 가정합니다. 로컬 모델에 유용합니다.
