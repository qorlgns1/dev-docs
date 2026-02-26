---
title: "WorkerInfo"
description: "contains information about the worker that is running tests and is available to worker-scoped fixtures.  is a subset of TestInfo that is available in ..."
---

Source URL: https://playwright.dev/docs/api/class-workerinfo

# WorkerInfo | Playwright

`WorkerInfo` contains information about the worker that is running tests and is available to worker-scoped fixtures. `WorkerInfo` is a subset of [TestInfo](https://playwright.dev/docs/api/class-testinfo "TestInfo") that is available in many other places.

---

## Properties[​](https://playwright.dev/docs/api/class-workerinfo#properties "Direct link to Properties")

### config[​](https://playwright.dev/docs/api/class-workerinfo#worker-info-config "Direct link to config")

Added in: v1.10 workerInfo.config

Processed configuration from the [configuration file](https://playwright.dev/docs/test-configuration).

**Usage**

```
    workerInfo.config

```

**Type**

- [FullConfig](https://playwright.dev/docs/api/class-fullconfig "FullConfig")

---

### parallelIndex[​](https://playwright.dev/docs/api/class-workerinfo#worker-info-parallel-index "Direct link to parallelIndex")

Added in: v1.10 workerInfo.parallelIndex

The index of the worker between `0` and `workers - 1`. It is guaranteed that workers running at the same time have a different `parallelIndex`. When a worker is restarted, for example after a failure, the new worker process has the same `parallelIndex`.

Also available as `process.env.TEST_PARALLEL_INDEX`. Learn more about [parallelism and sharding](https://playwright.dev/docs/test-parallel) with Playwright Test.

**Usage**

```
    workerInfo.parallelIndex

```

**Type**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")

---

### project[​](https://playwright.dev/docs/api/class-workerinfo#worker-info-project "Direct link to project")

Added in: v1.10 workerInfo.project

Processed project configuration from the [configuration file](https://playwright.dev/docs/test-configuration).

**Usage**

```
    workerInfo.project

```

**Type**

- [FullProject](https://playwright.dev/docs/api/class-fullproject "FullProject")

---

### workerIndex[​](https://playwright.dev/docs/api/class-workerinfo#worker-info-worker-index "Direct link to workerIndex")

Added in: v1.10 workerInfo.workerIndex

The unique index of the worker process that is running the test. When a worker is restarted, for example after a failure, the new worker process gets a new unique `workerIndex`.

Also available as `process.env.TEST_WORKER_INDEX`. Learn more about [parallelism and sharding](https://playwright.dev/docs/test-parallel) with Playwright Test.

**Usage**

```
    workerInfo.workerIndex

```

**Type**

- [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")
