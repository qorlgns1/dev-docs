---
title: "snapshotFormat"
description: "스냅샷 테스트를 위한 포맷 옵션입니다. 이 옵션들은 의 포크 버전으로 전달됩니다.  옵션 외에도 을 지원합니다."
---

출처 URL: https://vitest.dev/config/snapshotformat

# snapshotFormat

- **유형:** `PrettyFormatOptions`

스냅샷 테스트를 위한 포맷 옵션입니다. 이 옵션들은 [`pretty-format`](https://www.npmjs.com/package/pretty-format)의 포크 버전으로 전달됩니다. `pretty-format` 옵션 외에도 `printShadowRoot: boolean`을 지원합니다.

::: tip
이 객체의 `plugins` 필드는 무시된다는 점에 유의하세요.

pretty-format 플러그인을 통해 스냅샷 serializer를 확장해야 한다면 [`expect.addSnapshotSerializer`](https://vitest.dev/api/expect#expect-addsnapshotserializer) API 또는 [snapshotSerializers](#snapshotserializers) 옵션을 사용하세요.
:::
