---
title: Codex 변경 로그
description: $ npm install -g @openai/codex@0.104.0
---

# Codex 변경 로그

Source URL: https://developers.openai.com/codex/changelog

[code]
    $ npm install -g @openai/codex@0.104.0
[/code]

자세히 보기

## 새로운 기능

  * 네트워크 프록시에서 웹소켓 프록시를 위해 `WS_PROXY`/`WSS_PROXY` 환경 변수 지원(소문자 변형 포함)을 추가했습니다. ([#11784](https://github.com/openai/codex/pull/11784))
  * App-server v2는 스레드가 보관되거나 보관 해제될 때 알림을 전송하여 클라이언트가 폴링 없이 반응할 수 있게 합니다. ([#12030](https://github.com/openai/codex/pull/12030))
  * Protocol/core는 단일 셸 명령 실행 흐름 내에서 여러 승인 단계를 지원할 수 있도록 명령 승인에 고유한 승인 ID를 전달합니다. ([#12051](https://github.com/openai/codex/pull/12051))



## 버그 수정

  * 재개/포크 흐름 동안 cwd 변경 프롬프트에서 `Ctrl+C`/`Ctrl+D` 입력 시 옵션을 암묵적으로 선택하지 않고 깔끔하게 종료합니다. ([#12040](https://github.com/openai/codex/pull/12040))
  * 응답 본문 모델 슬러그 대신 응답 헤더 모델(및 웹소켓 최상위 이벤트)에 의존하도록 하여 안전성 검사 다운그레이드의 오탐을 줄였습니다. ([#12061](https://github.com/openai/codex/pull/12061))



## 문서

  * 웹소켓 프록시 구성, 새 스레드 보관/보관 해제 알림, 명령 승인 ID 파이프라인을 다루도록 문서와 스키마를 업데이트했습니다. ([#11784](https://github.com/openai/codex/pull/11784), [#12030](https://github.com/openai/codex/pull/12030), [#12051](https://github.com/openai/codex/pull/12051))



## 잡무

  * 이미 게시된 버전에 대해 `npm publish`를 시도할 때도 실패하지 않도록 Rust 릴리스 워크플로를 견고하게 만들었습니다. ([#12044](https://github.com/openai/codex/pull/12044))
  * 원격 컴팩션 테스트 모킹을 표준화하고 기본 프로덕션 형태의 동작에 맞추기 위해 관련 스냅샷을 새로 고쳤습니다. ([#12050](https://github.com/openai/codex/pull/12050))



## 변경 로그

전체 변경 로그: [`rust-v0.103.0...rust-v0.104.0`](https://github.com/openai/codex/compare/rust-v0.103.0...rust-v0.104.0)

  * [#11784](https://github.com/openai/codex/pull/11784) feat(network-proxy): 웹소켓 프록시 환경 변수 지원 추가 [@viyatb-oai](https://github.com/viyatb-oai)
  * [#12044](https://github.com/openai/codex/pull/12044) 기존 버전에 대한 `npm publish` 시도라도 실패하지 않도록 처리 [@iceweasel-oai](https://github.com/iceweasel-oai)
  * [#12040](https://github.com/openai/codex/pull/12040) tui: cwd 변경 프롬프트에서 Ctrl+C로 세션 종료 [@charley-oai](https://github.com/charley-oai)
  * [#12030](https://github.com/openai/codex/pull/12030) app-server: 스레드 보관/보관 해제 알림 발송 [@euroelessar](https://github.com/euroelessar)
  * [#12061](https://github.com/openai/codex/pull/12061) Chore: 응답 모델 확인 제거 및 다운그레이드 시 헤더 모델 의존 [@shijie-oai](https://github.com/shijie-oai)
  * [#12051](https://github.com/openai/codex/pull/12051) feat(core): 명령 승인을 위해 별도의 승인 ID 연결 [@owenlin0](https://github.com/owenlin0)
  * [#12050](https://github.com/openai/codex/pull/12050) 기본 엔드포인트 동작에 맞춰 원격 컴팩션 스냅샷 모킹 통일 [@charley-oai](https://github.com/charley-oai)



[ GitHub에서 전체 릴리스 보기 ](https://github.com/openai/codex/releases/tag/rust-v0.104.0)
