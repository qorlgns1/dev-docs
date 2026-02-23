---
title: 'Windows'
description: 'Windows에서 Codex를 가장 쉽게 사용하는 방법은 IDE 확장 설정이나 CLI 설치를 통해 PowerShell에서 실행하는 것입니다.'
---

Source URL: https://developers.openai.com/codex/windows

# Windows

Windows에서 Codex를 가장 쉽게 사용하는 방법은 [IDE 확장 설정](https://developers.openai.com/codex/ide)이나 [CLI 설치](https://developers.openai.com/codex/cli)를 통해 PowerShell에서 실행하는 것입니다.

Windows에서 Codex를 네이티브로 실행하면 에이전트 모드가 실험적인 Windows 샌드박스를 사용하여 작업 폴더 외부의 파일 시스템 쓰기와 네트워크 접근을 사용자의 명시적 승인 없이 차단합니다. [아래에서 자세히 알아보기](#windows-experimental-sandbox).

대신 [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install)(WSL2)를 사용할 수 있습니다. WSL2는 Linux 셸, 유닉스식 의미론, 툴링을 제공하여 훈련에서 모델이 많이 본 작업과 일치합니다.

## Windows Subsystem for Linux

### WSL 내부에서 VS Code 시작

단계별 안내는 [공식 VS Code WSL 튜토리얼](https://code.visualstudio.com/docs/remote/wsl-tutorial)을 참조하세요.

#### 전제 조건

- WSL이 설치된 Windows. WSL을 설치하려면 관리자로 PowerShell을 열고 `wsl --install`을 실행합니다(일반적으로 Ubuntu 선택).
- [WSL 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)이 설치된 VS Code.

#### WSL 터미널에서 VS Code 열기

```bash
# WSL 셸에서
cd ~/code/your-project
code .
```

이 명령은 WSL 원격 창을 열고 필요 시 VS Code Server를 설치하며 통합 터미널이 Linux에서 실행되도록 보장합니다.

#### WSL에 연결되었는지 확인

- `WSL: <distro>`를 표시하는 녹색 상태 표시줄을 확인합니다.
- 통합 터미널은 `C:\` 대신 Linux 경로(예: `/home/...`)를 보여야 합니다.
- 다음 명령으로 확인할 수 있습니다.

  ```bash
  echo $WSL_DISTRO_NAME
  ```

  이 명령은 배포판 이름을 출력합니다.

상태 표시줄에 "WSL: ..."이 표시되지 않으면 `Ctrl+Shift+P`를 누르고 `WSL: Reopen Folder in WSL`을 선택한 다음 저장소를 성능 향상을 위해 `/home/...`(즉, `C:\`가 아닌) 아래에 유지하세요.

### WSL에서 Codex CLI 사용

다음 명령을 관리자로 실행 중인 PowerShell 또는 Windows Terminal에서 실행하세요.

```powershell
# 기본 Linux 배포판(예: Ubuntu) 설치
wsl --install

# Windows Subsystem for Linux 내부 셸 시작
wsl
```

그런 다음 WSL 셸에서 다음 명령을 실행합니다.

```bash
# https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl
# WSL에서 Node.js 설치(nvm 사용)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash

# 새 탭에서 또는 `wsl`을 다시 실행하여 Node.js 설치
nvm install 22

# WSL에서 Codex 설치 및 실행
npm i -g @openai/codex
codex
```

### WSL 내부에서 코드 작업

- <code>/mnt/c/...</code>와 같은 Windows 마운트 경로에서 작업하면 Windows 기본 경로에서 작업하는 것보다 느릴 수 있습니다. 더 빠른 I/O와 적은 심볼릭 링크 및 권한 문제를 위해 저장소를 Linux 홈 디렉터리(예: <code>~/code/my-app</code>) 아래에 유지하세요.
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
  ```
- Windows에서 파일에 액세스해야 하면 파일이 탐색기에서 <code>\\wsl$\Ubuntu\home\&lt;user&gt;</code> 아래에 있습니다.

## Windows 실험용 샌드박스

Windows 샌드박스 지원은 실험적입니다. 작동 방식은 다음과 같습니다.

- AppContainer 프로파일에서 파생된 제한된 토큰 안에서 명령을 실행합니다.
- 해당 프로파일에 능력 보안 식별자를 연결하여 구체적으로 요청된 파일 시스템 권한만 부여합니다.
- 프록시 관련 환경 변수를 재정의하고 일반적인 네트워크 도구에 대한 스텁 실행 파일을 삽입하여 아웃바운드 네트워크 접근을 비활성화합니다.

주요 한계는 Everyone SID에 쓰기 권한이 이미 있는 디렉터리(예: 전 세계 쓰기 가능한 폴더)에서는 파일 쓰기, 삭제 또는 생성 작업을 차단할 수 없다는 점입니다. Windows 샌드박스를 사용하면 Codex가 Everyone이 쓰기 접근 권한을 가진 폴더를 검색하고 해당 접근 권한을 제거할 것을 권장합니다.

### 샌드박스에 읽기 권한 부여

Windows 샌드박스가 디렉터리를 읽을 수 없어 명령이 실패하면 다음을 사용하세요.

```text
/sandbox-add-read-dir C:\absolute\directory\path
```

경로는 기존 절대 디렉터리여야 합니다. 명령이 성공하면 해당 세션에서 샌드박스에서 실행되는 이후 명령이 해당 디렉터리를 읽을 수 있습니다.

### 문제 해결 및 FAQ

#### 확장 프로그램을 설치했지만 응답이 없음

일부 네이티브 종속 항목에 필요한 C++ 개발 도구가 시스템에 없을 수 있습니다.

- Visual Studio Build Tools(C++ 워크로드)
- Microsoft Visual C++ Redistributable(x64)
- `winget`을 사용하여 `winget install --id Microsoft.VisualStudio.2022.BuildTools -e` 실행

설치 후 VS Code를 완전히 재시작하세요.

#### 대규모 저장소에서 느리게 느껴진다면

- <code>/mnt/c</code> 아래에서 작업하지 않도록 하세요. 저장소를 WSL(예: <code>~/code/...</code>)로 이동하세요.
- 필요하다면 WSL의 메모리와 CPU를 늘리고 최신 버전으로 업데이트하세요.
  ```powershell
  wsl --update
  wsl --shutdown
  ```

#### WSL의 VS Code가 `codex`를 찾지 못함

WSL 내부에 바이너리가 존재하며 PATH에 포함되어 있는지 확인하세요.

```bash
which codex || echo "codex not found"
```

바이너리를 찾을 수 없으면 위의 [Codex CLI 사용](#use-codex-cli-with-wsl) 지침을 따라 설치하세요.
