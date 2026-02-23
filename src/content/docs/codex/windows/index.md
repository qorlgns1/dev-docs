---
title: Windows
description: "출처 URL: https://developers.openai.com/codex/windows"
---

# Windows

출처 URL: https://developers.openai.com/codex/windows

Windows에서 Codex를 가장 쉽게 사용하는 방법은 [IDE 확장 프로그램을 설정](https://developers.openai.com/codex/ide)하거나 [CLI를 설치](https://developers.openai.com/codex/cli)한 뒤 PowerShell에서 실행하는 것입니다.

Windows에서 Codex를 네이티브로 실행하면, 에이전트 모드는 실험적인 Windows 샌드박스를 사용해 작업 폴더 밖의 파일 시스템 쓰기를 차단하고 명시적으로 승인하지 않은 네트워크 접근을 막습니다. [아래에서 자세히 알아보기](https://developers.openai.com/codex/windows#windows-experimental-sandbox).

대신 [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL2)를 사용할 수도 있습니다. WSL2는 Linux 셸, 유닉스 방식의 시맨틱, 그리고 모델이 학습 중에 접했던 많은 작업과 일치하는 도구 체인을 제공합니다.

## Windows Subsystem for Linux

### WSL 내부에서 VS Code 실행

단계별 안내는 [공식 VS Code WSL 튜토리얼](https://code.visualstudio.com/docs/remote/wsl-tutorial)을 참고하세요.

#### Prerequisites

  * WSL이 설치된 Windows. WSL을 설치하려면 PowerShell을 관리자 권한으로 열고 `wsl --install`을 실행하세요(보통 Ubuntu를 선택).
  * [WSL 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)이 설치된 VS Code.

#### Open VS Code from a WSL terminal
[code] 
    # From your WSL shell
    cd ~/code/your-project
    code .
[/code]

이 작업은 WSL 원격 창을 열고, 필요하다면 VS Code Server를 설치하며, 통합 터미널이 Linux에서 실행되도록 보장합니다.

#### Confirm you’re connected to WSL

  * `WSL: <distro>`를 표시하는 초록색 상태 표시줄을 확인하세요.

  * 통합 터미널이 `C:\` 대신 `/home/...` 같은 Linux 경로를 보여야 합니다.

  * 다음 명령으로 확인할 수 있습니다:
[code] echo $WSL_DISTRO_NAME
[/code]

이 명령은 배포판 이름을 출력합니다.

상태 표시줄에 “WSL: …”이 보이지 않으면 `Ctrl+Shift+P`를 눌러 `WSL: Reopen Folder in WSL`을 선택하고, 리포지토리는 `/home/...`( `C:\` 가 아님 ) 아래에 두어 최고의 성능을 얻으세요.

### Use Codex CLI with WSL

승격된 PowerShell 또는 Windows Terminal에서 다음 명령을 실행하세요:
[code] 
    # Install default Linux distribution (like Ubuntu)
    wsl --install
    
    # Start a shell inside Windows Subsystem for Linux
    wsl
[/code]

그다음 WSL 셸에서 아래 명령을 실행합니다:
[code] 
    # https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl
    # Install Node.js in WSL (via nvm)
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
    
    # In a new tab or after exiting and running `wsl` again to install Node.js
    nvm install 22
    
    # Install and run Codex in WSL
    npm i -g @openai/codex
    codex
[/code]

### Working on code inside WSL

  * `/mnt/c/…`처럼 Windows에 마운트된 경로에서 작업하면 Windows 네이티브 경로보다 느릴 수 있습니다. 리포지토리를 `~/code/my-app` 같은 Linux 홈 디렉터리 아래에 두면 I/O가 더 빠르고 심볼릭 링크 및 권한 문제도 줄어듭니다: 
[code]mkdir -p ~/code && cd ~/code
        git clone https://github.com/your/repo.git
        cd repo
[/code]

  * Windows에서 파일에 접근해야 한다면 Explorer에서 `\wsl$\Ubuntu\home&lt;user>` 아래에 위치합니다.

## Windows experimental sandbox

Windows 샌드박스 지원은 실험적입니다. 동작 방식은 다음과 같습니다:

  * AppContainer 프로필에서 파생된 제한 토큰 안에서 명령을 실행합니다.
  * 해당 프로필에 기능 보안 식별자를 부여하여 명시적으로 요청된 파일 시스템 권한만 허용합니다.
  * 프록시 관련 환경 변수를 오버라이드하고 일반적인 네트워크 도구에 스텁 실행 파일을 삽입해 아웃바운드 네트워크 접근을 차단합니다.

주요 제한 사항은 Everyone SID가 이미 쓰기 권한을 가진 디렉터리(예: 모든 사용자에게 쓰기 가능한 폴더)에서는 파일 쓰기, 삭제, 생성 등을 막을 수 없다는 점입니다. Windows 샌드박스를 사용할 때 Codex는 Everyone이 쓰기 권한을 가진 폴더를 찾아 해당 권한을 제거하도록 권장합니다.

### 샌드박스 읽기 권한 부여

Windows 샌드박스가 디렉터리를 읽지 못해 명령이 실패할 때는 다음을 실행하세요:
[code] 
    /sandbox-add-read-dir C:\absolute\directory\path
[/code]

경로는 반드시 존재하는 절대 디렉터리여야 합니다. 명령이 성공하면, 이후 샌드박스에서 실행되는 명령은 현재 세션 동안 해당 디렉터리를 읽을 수 있습니다.

### 문제 해결 및 FAQ

#### 확장을 설치했는데 반응하지 않음

일부 네이티브 종속성이 요구하는 C++ 개발 도구가 시스템에 없을 수 있습니다:

  * Visual Studio Build Tools (C++ 워크로드)
  * Microsoft Visual C++ Redistributable (x64)
  * `winget`으로 `winget install --id Microsoft.VisualStudio.2022.BuildTools -e` 실행

설치 후 VS Code를 완전히 재시작하세요.

#### 대형 리포지토리에서 느리게 느껴지는 경우

  * `/mnt/c` 아래에서 작업 중이 아닌지 확인하세요. 리포지토리를 WSL로 옮기세요(예: `~/code/...`).
  * 필요하다면 WSL의 메모리와 CPU를 늘리고, 최신 버전으로 업데이트하세요: 
[code]wsl --update
        wsl --shutdown
[/code]

#### WSL의 VS Code가 `codex`를 찾지 못함

WSL 내부에서 바이너리가 존재하고 PATH에 있는지 확인하세요:
[code] 
    which codex || echo "codex not found"
[/code]

바이너리를 찾지 못하면 위 링크의 [설치 안내](https://developers.openai.com/codex/windows#use-codex-cli-with-wsl)를 따라 설치하세요.
