---
title: 클라우드 환경
description: "출처 URL: https://developers.openai.com/codex/cloud/environments"
---

# 클라우드 환경

출처 URL: https://developers.openai.com/codex/cloud/environments

환경을 사용하면 클라우드 작업 동안 Codex가 설치하고 실행하는 항목을 제어할 수 있습니다. 예를 들어 종속성을 추가하고, 린터와 포매터 같은 도구를 설치하며, 환경 변수를 설정할 수 있습니다.

환경은 [Codex settings](https://chatgpt.com/codex/settings/environments)에서 구성합니다.

## Codex 클라우드 작업이 실행되는 방식

작업을 제출하면 다음과 같이 진행됩니다:

  1. Codex는 컨테이너를 생성하고 선택한 브랜치 또는 커밋 SHA에서 리포지토리를 체크아웃합니다.
  2. Codex는 설정 스크립트를 실행하고, 캐시된 컨테이너를 다시 사용할 때는 선택적으로 유지보수 스크립트를 실행합니다.
  3. Codex는 인터넷 액세스 설정을 적용합니다. 설정 스크립트는 인터넷 액세스를 사용해 실행되며, 에이전트의 인터넷 액세스는 기본적으로 꺼져 있지만 필요하면 제한적이거나 무제한 접근을 활성화할 수 있습니다. [agent internet access](https://developers.openai.com/codex/cloud/internet-access)를 참고하세요.
  4. 에이전트는 터미널 명령을 반복 실행하면서 코드를 수정하고 검사하며 결과를 검증하려고 시도합니다. 리포지토리에 `AGENTS.md`가 있으면 프로젝트별 린트와 테스트 명령을 찾기 위해 이를 사용합니다.
  5. 에이전트가 종료되면 답변과 변경된 파일의 diff를 보여줍니다. 이후 PR을 열거나 후속 질문을 할 수 있습니다.

## 기본 universal 이미지

Codex 에이전트는 `universal`이라는 기본 컨테이너 이미지에서 실행되며, 일반적인 언어와 패키지, 도구가 미리 설치되어 있습니다.

환경 설정에서 **Set package versions**를 선택하면 Python, Node.js 등 런타임 버전을 고정할 수 있습니다.

설치된 항목에 대한 자세한 정보는 [openai/codex-universal](https://github.com/openai/codex-universal)의 참조 Dockerfile과 로컬에서 가져와 테스트할 수 있는 이미지를 확인하세요.

`codex-universal`에는 속도와 편의를 위해 주요 언어가 미리 설치되어 있지만, 필요하면 [setup scripts](https://developers.openai.com/codex/cloud/environments#manual-setup)를 사용해 추가 패키지를 설치할 수도 있습니다.

## 환경 변수와 시크릿

**Environment variables**는 작업 전체(설정 스크립트와 에이전트 단계 포함) 동안 설정된 상태로 유지됩니다.

**Secrets**는 환경 변수와 유사하지만 다음과 같은 차이가 있습니다:

  * 추가적인 암호화 계층으로 저장되며 작업 실행 시에만 복호화됩니다.
  * 설정 스크립트에서만 사용할 수 있습니다. 보안을 위해 에이전트 단계가 시작되기 전에 제거됩니다.

## 자동 설정

일반적인 패키지 관리자(`npm`, `yarn`, `pnpm`, `pip`, `pipenv`, `poetry`)를 사용하는 프로젝트라면 Codex가 종속성과 도구를 자동으로 설치할 수 있습니다.

## 수동 설정

개발 환경이 더 복잡하다면 사용자 정의 설정 스크립트를 제공할 수 있습니다. 예:

[code] 
    # Install type checker
    pip install pyright
    
    # Install dependencies
    poetry install --with test
    pnpm install
[/code]

설정 스크립트는 에이전트와 별도의 Bash 세션에서 실행되므로 `export` 같은 명령은 에이전트 단계로 이어지지 않습니다. 환경 변수를 유지하려면 `~/.bashrc`에 추가하거나 환경 설정에서 구성하세요.

## 컨테이너 캐싱

Codex는 새 작업과 후속 작업을 빠르게 처리하기 위해 컨테이너 상태를 최대 12시간 동안 캐시합니다.

환경이 캐시될 때:

  * Codex는 리포지토리를 복제하고 기본 브랜치를 체크아웃합니다.
  * Codex는 설정 스크립트를 실행하고 그 결과 컨테이너 상태를 캐시합니다.

캐시된 컨테이너를 다시 사용할 때:

  * Codex는 작업에 지정된 브랜치를 체크아웃합니다.
  * Codex는 유지보수 스크립트(선택 사항)를 실행합니다. 이는 설정 스크립트가 이전 커밋에서 실행되어 종속성 업데이트가 필요한 경우에 유용합니다.

설정 스크립트, 유지보수 스크립트, 환경 변수 또는 시크릿을 변경하면 Codex가 자동으로 캐시를 무효화합니다. 리포지토리 변경으로 캐시 상태가 호환되지 않으면 환경 페이지에서 **Reset cache**를 선택하세요.

비즈니스 및 엔터프라이즈 사용자의 경우, 캐시는 해당 환경에 접근 권한이 있는 모든 사용자와 공유됩니다. 캐시를 무효화하면 워크스페이스 내 환경의 모든 사용자에게 영향을 줍니다.

## 인터넷 액세스 및 네트워크 프록시

설정 스크립트 단계에서는 종속성을 설치하기 위해 인터넷 액세스가 제공됩니다. 에이전트 단계에서는 기본적으로 인터넷 액세스가 꺼져 있지만, 제한적 또는 무제한 액세스를 구성할 수 있습니다. [agent internet access](https://developers.openai.com/codex/cloud/internet-access)를 참고하세요.

환경은 보안 및 오용 방지를 위해 HTTP/HTTPS 네트워크 프록시 뒤에서 실행됩니다. 모든 아웃바운드 인터넷 트래픽은 이 프록시를 통해 전달됩니다.
