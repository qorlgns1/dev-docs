# Codex IDE 확장 명령

출처 URL: https://developers.openai.com/codex/ide/commands

이 명령들을 사용해 VS Code 명령 팔레트에서 Codex를 제어할 수 있습니다. 또한 키보드 단축키에 연결할 수도 있습니다.

## 키 바인딩 지정

Codex 명령에 대한 키 바인딩을 지정하거나 변경하려면:

  1. 명령 팔레트를 엽니다 (macOS에서는 **Cmd+Shift+P**, Windows/Linux에서는 **Ctrl+Shift+P**).
  2. **Preferences: Open Keyboard Shortcuts**를 실행합니다.
  3. `Codex` 또는 명령 ID(예: `chatgpt.newChat`)를 검색합니다.
  4. 연필 아이콘을 선택한 뒤 원하는 단축키를 입력합니다.



## 확장 명령

Command| Default key binding| Description  
---|---|---  
`chatgpt.addToThread`| -| 현재 스레드의 컨텍스트로 선택한 텍스트 범위를 추가합니다  
`chatgpt.addFileToThread`| -| 현재 스레드의 컨텍스트로 전체 파일을 추가합니다  
`chatgpt.newChat`| macOS: `Cmd+N`  
Windows/Linux: `Ctrl+N`| 새 스레드를 생성합니다  
`chatgpt.implementTodo`| -| 선택한 TODO 주석을 Codex가 처리하도록 요청합니다  
`chatgpt.newCodexPanel`| -| 새 Codex 패널을 생성합니다  
`chatgpt.openSidebar`| -| Codex 사이드바 패널을 엽니다
