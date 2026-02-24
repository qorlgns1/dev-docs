---
title: 'Debugging'
description: 'To see debug statements set or add  to the  environment variable:'
---

Source URL: https://docs.bullmq.io/bull/patterns/debugging

# Debugging

To see debug statements set or add `bull` to the `NODE_DEBUG` environment variable:

```
export NODE_DEBUG=bull
```

or:

```
NODE_DEBUG=bull node ./your-script.js
```

