---
title: "maxConcurrency"
description: "로 표시된 테스트 중 동시에 실행이 허용되는 개수입니다."
---

출처 URL: https://vitest.dev/config/maxconcurrency

# maxConcurrency

- **타입**: `number`
- **기본값**: `5`
- **CLI**: `--max-concurrency=10`, `--maxConcurrency=10`

`test.concurrent`로 표시된 테스트 중 동시에 실행이 허용되는 개수입니다.

이 제한을 초과하는 테스트는 실행 가능한 슬롯이 생기면 대기열에서 순차적으로 실행됩니다.
