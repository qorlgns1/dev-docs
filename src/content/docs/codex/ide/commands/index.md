---
title: 'Codex IDE 확장 명령'
description: "title: 'Codex IDE 확장 명령'"
---

**번역**

---
title: 'Codex IDE 확장 명령'
description: '이 명령으로 VS Code 명령 팔레트에서 Codex를 제어할 수 있습니다. 키보드 단축키에 연결하는 것도 가능합니다.'
---

Source URL: https://developers.openai.com/codex/ide/commands

# Codex IDE 확장 명령

이 명령을 사용하여 VS Code 명령 팔레트에서 Codex를 제어할 수 있습니다. 키보드 단축키에 연결하는 것도 가능합니다.

## 키 바인딩 지정

Codex 명령의 키 바인딩을 지정하거나 변경하려면:

1. 명령 팔레트 열기( macOS: **Cmd+Shift+P**, Windows/Linux: **Ctrl+Shift+P** ).
2. **Preferences: Open Keyboard Shortcuts** 실행.
3. `Codex` 또는 명령 ID(예: `chatgpt.newChat`) 검색.
4. 연필 아이콘 선택 후 원하는 단축키 입력.

## 확장 명령

| Command                   | Default key binding                        | Description                                               |
| ------------------------- | ------------------------------------------ | --------------------------------------------------------- |
| `chatgpt.addToThread`     | -                                          | 선택한 텍스트 범위를 현재 스레드의 컨텍스트로 추가       |
| `chatgpt.addFileToThread` | -                                          | 전체 파일을 현재 스레드의 컨텍스트로 추가                 |
| `chatgpt.newChat`         | macOS: `Cmd+N`<br/>Windows/Linux: `Ctrl+N` | 새 스레드 생성                                            |
| `chatgpt.implementTodo`   | -                                          | 선택한 TODO 주석을 Codex에게 해결해 달라고 요청          |
| `chatgpt.newCodexPanel`   | -                                          | 새 Codex 패널 생성                                        |
| `chatgpt.openSidebar`     | -                                          | Codex 사이드바 패널 열기                                  |

