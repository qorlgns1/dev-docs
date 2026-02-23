---
title: 인증
description: "원본 URL: https://developers.openai.com/codex/auth"
sidebar:
  order: 40
---

# 인증

원본 URL: https://developers.openai.com/codex/auth

## OpenAI 인증

Codex는 OpenAI 모델을 사용할 때 두 가지 로그인 방식을 제공합니다:

  * 구독용 ChatGPT 로그인
  * 사용량 기반 액세스를 위한 API 키 로그인

Codex Cloud는 ChatGPT 로그인이 필요합니다. Codex CLI와 IDE 확장은 두 가지 로그인 방식을 모두 지원합니다.

### ChatGPT로 로그인

Codex 앱, CLI, 또는 IDE 확장에서 ChatGPT로 로그인하면 Codex가 브라우저 창을 열어 로그인 절차를 완료합니다. 로그인 후 브라우저가 액세스 토큰을 CLI나 IDE 확장에 반환합니다.

### API 키로 로그인

Codex 앱, CLI, 또는 IDE 확장에 API 키로 로그인할 수도 있습니다. [OpenAI 대시보드](https://platform.openai.com/api-keys)에서 API 키를 발급받으세요.

OpenAI는 API 키 사용량을 OpenAI Platform 계정의 표준 API 요율로 청구합니다. [API 가격 페이지](https://openai.com/api/pricing)를 참고하세요.

## Codex Cloud 계정 보안 강화

Codex Cloud는 코드베이스와 직접 상호작용하므로 다른 ChatGPT 기능보다 강력한 보안이 필요합니다. 다중 요소 인증(MFA)을 활성화하세요.

Google, Microsoft, Apple과 같은 소셜 로그인 제공자를 사용한다면 ChatGPT 계정에서 MFA를 필수로 설정할 필요는 없지만, 소셜 로그인 제공자 측에서 설정할 수 있습니다.

설정 안내:

  * [Google](https://support.google.com/accounts/answer/185839)
  * [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
  * [Apple](https://support.apple.com/en-us/102660)

ChatGPT에 단일 사인온(SSO)으로 접근한다면 조직의 SSO 관리자가 모든 사용자에 대해 MFA를 강제해야 합니다.

이메일과 비밀번호로 로그인하는 경우 Codex Cloud에 접근하기 전에 반드시 계정에 MFA를 설정해야 합니다.

계정이 여러 로그인 방식을 지원하고 그중 하나가 이메일/비밀번호라면, 다른 방식을 사용해 로그인하더라도 Codex에 접근하기 전에 MFA를 설정해야 합니다.

## 로그인 캐싱

ChatGPT 또는 API 키로 Codex 앱, CLI, IDE 확장에 로그인하면 Codex가 로그인 정보를 캐싱하고 다음에 CLI나 확장을 시작할 때 재사용합니다. CLI와 확장은 동일한 캐시된 로그인 정보를 공유합니다. 둘 중 하나에서 로그아웃하면 다음에 CLI나 확장을 시작할 때 다시 로그인해야 합니다.

Codex는 로그인 정보를 `~/.codex/auth.json` 또는 OS별 자격 증명 저장소에 평문 파일로 로컬 캐시합니다.

## 자격 증명 저장

Codex CLI가 캐시된 자격 증명을 저장할 위치를 제어하려면 `cli_auth_credentials_store`를 사용하세요:
```
    # file | keyring | auto
    cli_auth_credentials_store = "keyring"
```

  * `file`은 `CODEX_HOME`(기본값은 `~/.codex`) 아래의 `auth.json`에 자격 증명을 저장합니다.
  * `keyring`은 운영체제의 자격 증명 저장소에 자격 증명을 저장합니다.
  * `auto`는 사용 가능한 경우 OS 자격 증명 저장소를 사용하고, 그렇지 않으면 `auth.json`으로 폴백합니다.

파일 기반 저장을 사용하는 경우 `~/.codex/auth.json`을 비밀번호처럼 취급하세요. 액세스 토큰이 포함되어 있으므로 커밋하거나 티켓에 붙여 넣거나 채팅으로 공유하지 마세요.

## 로그인 방식 또는 워크스페이스 강제

관리 환경에서는 관리자가 사용자 인증 방식을 제한할 수 있습니다:
```
    # Only allow ChatGPT login or only allow API key login.
    forced_login_method = "chatgpt" # or "api"
    
    # When using ChatGPT login, restrict users to a specific workspace.
    forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"
```

활성 자격 증명이 구성된 제한과 일치하지 않으면 Codex는 사용자를 로그아웃시키고 종료합니다.

이 설정은 사용자별이 아니라 관리형 구성으로 적용되는 경우가 많습니다. [Managed configuration](https://developers.openai.com/codex/security#managed-configuration)을 참고하세요.

## 헤드리스 디바이스에서 로그인

Codex CLI로 ChatGPT에 로그인하는 경우 브라우저 기반 로그인 UI가 작동하지 않을 수 있는 상황이 있습니다:

* CLI를 원격 또는 헤드리스 환경에서 실행 중입니다.
  * 로컬 네트워크 구성이 로그인 후 OAuth 토큰을 CLI로 돌려주는 Codex의 localhost 콜백을 차단합니다.



이러한 상황에서는 장치 코드 인증(베타)을 권장합니다. 대화형 로그인 UI에서 **Sign in with Device Code** 를 선택하거나 `codex login --device-auth` 를 직접 실행하세요. 장치 코드 인증이 환경에서 작동하지 않으면 아래의 대체 방법을 사용하십시오.

### 권장: 장치 코드 인증(베타)

  1. ChatGPT 보안 설정(개인 계정) 또는 ChatGPT 워크스페이스 권한(워크스페이스 관리자)에서 장치 코드 로그인을 사용하도록 설정합니다.
  2. Codex를 실행 중인 터미널에서 다음 옵션 중 하나를 선택합니다. 
     * 대화형 로그인 UI에서 **Sign in with Device Code** 를 선택합니다.
     * `codex login --device-auth` 를 실행합니다.
  3. 브라우저에서 링크를 열어 로그인한 뒤 일회용 코드를 입력합니다.



서버에서 장치 코드 로그인을 허용하지 않으면 Codex는 표준 브라우저 기반 로그인 흐름으로 돌아갑니다.

### 대체: 로컬에서 인증 후 인증 캐시 복사

브라우저가 있는 머신에서 로그인 흐름을 완료할 수 있다면 캐시된 자격 증명을 헤드리스 머신으로 복사할 수 있습니다.

  1. 브라우저 기반 로그인 흐름을 사용할 수 있는 머신에서 `codex login` 을 실행합니다.
  2. 로그인 캐시가 `~/.codex/auth.json` 에 존재하는지 확인합니다.
  3. `~/.codex/auth.json` 을 헤드리스 머신의 `~/.codex/auth.json` 으로 복사합니다.



`~/.codex/auth.json` 은 비밀번호처럼 취급하세요. 액세스 토큰이 포함되어 있으므로 커밋하거나 티켓에 붙여넣거나 채팅으로 공유하지 마십시오.

운영체제가 `~/.codex/auth.json` 대신 자격 증명을 크리덴셜 스토어에 저장한다면 이 방법은 적용되지 않을 수 있습니다. 파일 기반 저장소 구성 방법은 [Credential storage](https://developers.openai.com/codex/auth#credential-storage) 를 참조하세요.

SSH로 원격 머신에 복사:
```
    ssh user@remote 'mkdir -p ~/.codex'
    scp ~/.codex/auth.json user@remote:~/.codex/auth.json
```

또는 `scp` 를 사용하지 않는 원라이너:
```
    ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json
```

Docker 컨테이너에 복사:
```
    # Replace MY_CONTAINER with the name or ID of your container.
    CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
    docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
    docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"
```

### 대체: SSH로 localhost 콜백 포워딩

로컬 머신과 원격 호스트 간에 포트를 포워딩할 수 있다면 Codex의 로컬 콜백 서버(기본 `localhost:1455`)를 터널링하여 표준 브라우저 기반 흐름을 사용할 수 있습니다.

  1. 로컬 머신에서 포트 포워딩을 시작합니다:


```
    ssh -L 1455:localhost:1455 user@remote
```

  2. 해당 SSH 세션에서 `codex login` 을 실행하고 로컬 머신에 표시된 주소를 따릅니다.



## 대안 모델 제공자

구성 파일에서 [사용자 지정 모델 제공자](https://developers.openai.com/codex/config-advanced#custom-model-providers) 를 정의할 때 다음 인증 방법 중 하나를 선택할 수 있습니다.

  * **OpenAI 인증** : `requires_openai_auth = true` 를 설정하여 OpenAI 인증을 사용합니다. 이후 ChatGPT 또는 API 키로 로그인할 수 있습니다. LLM 프록시 서버를 통해 OpenAI 모델에 접근할 때 유용합니다. `requires_openai_auth = true` 이면 Codex는 `env_key` 를 무시합니다.
  * **환경 변수 인증** : `env_key = "<ENV_VARIABLE_NAME>"` 을 설정하여 `<ENV_VARIABLE_NAME>` 로 명명된 로컬 환경 변수에서 제공자 전용 API 키를 사용합니다.
  * **인증 없음** : `requires_openai_auth` 를 설정하지 않거나(`false`) `env_key` 를 설정하지 않으면 Codex는 제공자가 인증을 요구하지 않는다고 간주합니다. 로컬 모델에 유용합니다.