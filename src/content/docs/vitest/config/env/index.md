---
title: "index"
description: "테스트 중  및 에서 사용할 수 있는 환경 변수입니다. 이러한 변수는 메인 프로세스(예: )에서는 사용할 수 없습니다."
---

출처 URL: https://vitest.dev/config/env

# env

- **Type:** `Partial<NodeJS.ProcessEnv>`

테스트 중 `process.env` 및 `import.meta.env`에서 사용할 수 있는 환경 변수입니다. 이러한 변수는 메인 프로세스(예: `globalSetup`)에서는 사용할 수 없습니다.
