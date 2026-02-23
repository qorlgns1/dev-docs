---
title: Codex changelog
description: $ npm install -g @openai/codex@0.104.0
sidebar:
  order: 80
---

# Codex changelog

Source URL: https://developers.openai.com/codex/changelog

[code]
    $ npm install -g @openai/codex@0.104.0
[/code]

View details

## New Features

  * Added `WS_PROXY`/`WSS_PROXY` environment support (including lowercase variants) for websocket proxying in the network proxy. ([#11784](https://github.com/openai/codex/pull/11784))
  * App-server v2 now emits notifications when threads are archived or unarchived, enabling clients to react without polling. ([#12030](https://github.com/openai/codex/pull/12030))
  * Protocol/core now carry distinct approval IDs for command approvals to support multiple approvals within a single shell command execution flow. ([#12051](https://github.com/openai/codex/pull/12051))



## Bug Fixes

  * `Ctrl+C`/`Ctrl+D` now cleanly exits the cwd-change prompt during resume/fork flows instead of implicitly selecting an option. ([#12040](https://github.com/openai/codex/pull/12040))
  * Reduced false-positive safety-check downgrade behavior by relying on the response header model (and websocket top-level events) rather than the response body model slug. ([#12061](https://github.com/openai/codex/pull/12061))



## Documentation

  * Updated docs and schemas to cover websocket proxy configuration, new thread archive/unarchive notifications, and the command approval ID plumbing. ([#11784](https://github.com/openai/codex/pull/11784), [#12030](https://github.com/openai/codex/pull/12030), [#12051](https://github.com/openai/codex/pull/12051))



## Chores

  * Made the Rust release workflow resilient to `npm publish` attempts for an already-published version. ([#12044](https://github.com/openai/codex/pull/12044))
  * Standardized remote compaction test mocking and refreshed related snapshots to align with the default production-shaped behavior. ([#12050](https://github.com/openai/codex/pull/12050))



## Changelog

Full Changelog: [`rust-v0.103.0...rust-v0.104.0`](https://github.com/openai/codex/compare/rust-v0.103.0...rust-v0.104.0)

  * [#11784](https://github.com/openai/codex/pull/11784) feat(network-proxy): add websocket proxy env support [@viyatb-oai](https://github.com/viyatb-oai)
  * [#12044](https://github.com/openai/codex/pull/12044) don't fail if an npm publish attempt is for an existing version. [@iceweasel-oai](https://github.com/iceweasel-oai)
  * [#12040](https://github.com/openai/codex/pull/12040) tui: exit session on Ctrl+C in cwd change prompt [@charley-oai](https://github.com/charley-oai)
  * [#12030](https://github.com/openai/codex/pull/12030) app-server: Emit thread archive/unarchive notifications [@euroelessar](https://github.com/euroelessar)
  * [#12061](https://github.com/openai/codex/pull/12061) Chore: remove response model check and rely on header model for downgrade [@shijie-oai](https://github.com/shijie-oai)
  * [#12051](https://github.com/openai/codex/pull/12051) feat(core): plumb distinct approval ids for command approvals [@owenlin0](https://github.com/owenlin0)
  * [#12050](https://github.com/openai/codex/pull/12050) Unify remote compaction snapshot mocks around default endpoint behavior [@charley-oai](https://github.com/charley-oai)



[ Full release on Github ](https://github.com/openai/codex/releases/tag/rust-v0.104.0)
