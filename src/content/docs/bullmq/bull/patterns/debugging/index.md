---
title: 'index'
description: '원본 URL: https://docs.bullmq.io/bull/patterns/debugging'
---

원본 URL: https://docs.bullmq.io/bull/patterns/debugging

# 디버깅

디버그 문을 보려면 `NODE_DEBUG` 환경 변수에 `bull`을 설정하거나 추가하세요:

```
export NODE_DEBUG=bull
```

또는:

```
NODE_DEBUG=bull node ./your-script.js
```

