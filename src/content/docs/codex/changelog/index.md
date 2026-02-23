---
title: 'Codex 변경 로그'
description: '$ npm install -g @openai/codex@0.104.0'
---

Source URL: https://developers.openai.com/codex/changelog

# Codex 변경 로그

```
    $ npm install -g @openai/codex@0.104.0
```

세부 정보 보기

## 신규 기능

  * 네트워크 프록시에서 웹소켓 프록시용으로 `WS_PROXY`/`WSS_PROXY` 환경(소문자 버전 포함) 지원을 추가했습니다. ([#11784](https://github.com/openai/codex/pull/11784))
  * App-server v2가 스레드 보관/보관 해제 시 알림을 발행해 폴링 없이 클라이언트가 반응할 수 있도록 했습니다. ([#12030](https://github.com/openai/codex/pull/12030))
  * Protocol/core가 이제 단일 셸 명령 실행 흐름에서 여러 승인을 지원할 수 있도록 명령 승인용 별도 승인 ID를 전달합니다. ([#12051](https://github.com/openai/codex/pull/12051))

## 버그 수정

  * `Ctrl+C`/`Ctrl+D`가 resume/fork 흐름에서 현재 작업 디렉터리 변경 프롬프트를 암시적 옵션 선택 없이 깔끔하게 종료하도록 개선했습니다. ([#12040](https://github.com/openai/codex/pull/12040))
  * 응답 본문 모델 슬러그 대신 응답 헤더 모델(및 웹소켓 최상위 이벤트)에 의존해 안전 검사 오탐 다운그레이드 행동을 줄였습니다. ([#12061](https://github.com/openai/codex/pull/12061))

## 문서

  * 웹소켓 프록시 구성, 새로운 스레드 보관/보관 해제 알림, 명령 승인 ID 연결을 다루도록 문서와 스키마를 업데이트했습니다. ([#11784](https://github.com/openai/codex/pull/11784), [#12030](https://github.com/openai/codex/pull/12030), [#12051](https://github.com/openai/codex/pull/12051))

## 잡무

  * Rust 릴리스 워크플로우가 이미 배포된 버전으로 `npm publish`를 시도할 때에도 실패하지 않도록 만들었습니다. ([#12044](https://github.com/openai/codex/pull/12044))
  * 기본 운영 형태 행동에 맞춰 원격 압축 테스트 모킹을 표준화하고 관련 스냅샷을 갱신했습니다. ([#12050](https://github.com/openai/codex/pull/12050))

## 변경 로그

전체 변경 로그: [`rust-v0.103.0...rust-v0.104.0`](https://github.com/openai/codex/compare/rust-v0.103.0...rust-v0.104.0)

  * [#11784](https://github.com/openai/codex/pull/11784) feat(network-proxy): 웹소켓 프록시 환경 지원 추가 [@viyatb-oai](https://github.com/viyatb-oai)
  * [#12044](https://github.com/openai/codex/pull/12044) 기존 버전에 대한 npm publish 시도에도 실패하지 않도록 처리 [@iceweasel-oai](https://github.com/iceweasel-oai)
  * [#12040](https://github.com/openai/codex/pull/12040) tui: cwd 변경 프롬프트에서 Ctrl+C로 세션 종료 [@charley-oai](https://github.com/charley-oai)
  * [#12030](https://github.com/openai/codex/pull/12030) app-server: 스레드 보관/보관 해제 알림 발행 [@euroelessar](https://github.com/euroelessar)
  * [#12061](https://github.com/openai/codex/pull/12061) 잡무: 응답 모델 검사를 제거하고 다운그레이드는 헤더 모델에 의존 [@shijie-oai](https://github.com/shijie-oai)
  * [#12051](https://github.com/openai/codex/pull/12051) feat(core): 명령 승인마다 별도 승인 ID 연결 [@owenlin0](https://github.com/owenlin0)
  * [#12050](https://github.com/openai/codex/pull/12050) 기본 엔드포인트 행동 중심으로 원격 압축 스냅샷 모킹 통합 [@charley-oai](https://github.com/charley-oai)

[ 전체 릴리스 (Github) ](https://github.com/openai/codex/releases/tag/rust-v0.104.0)
