---
title: "Worker"
description: "The Worker class represents a WebWorker.  event is emitted on the page object to signal a worker creation.  event is emitted on the worker object when..."
---

Source URL: https://playwright.dev/docs/api/class-worker

# Worker | Playwright

The Worker class represents a [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API). `worker` event is emitted on the page object to signal a worker creation. `close` event is emitted on the worker object when the worker is gone.

```
    page.on('worker', worker => {
      console.log('Worker created: ' + worker.url());
      worker.on('close', worker => console.log('Worker destroyed: ' + worker.url()));
    });

    console.log('Current workers:');
    for (const worker of page.workers())
      console.log('  ' + worker.url());

```

---

## Methods[​](https://playwright.dev/docs/api/class-worker#methods "Direct link to Methods")

### evaluate[​](https://playwright.dev/docs/api/class-worker#worker-evaluate "Direct link to evaluate")

Added before v1.9 worker.evaluate

Returns the return value of [pageFunction](https://playwright.dev/docs/api/class-worker#worker-evaluate-option-expression).

If the function passed to the [worker.evaluate()](https://playwright.dev/docs/api/class-worker#worker-evaluate) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [worker.evaluate()](https://playwright.dev/docs/api/class-worker#worker-evaluate) would wait for the promise to resolve and return its value.

If the function passed to the [worker.evaluate()](https://playwright.dev/docs/api/class-worker#worker-evaluate) returns a non-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") value, then [worker.evaluate()](https://playwright.dev/docs/api/class-worker#worker-evaluate) returns `undefined`. Playwright also supports transferring some additional values that are not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

```
    await worker.evaluate(pageFunction);
    await worker.evaluate(pageFunction, arg);

```

**Arguments**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-worker#worker-evaluate-option-expression)

Function to be evaluated in the worker context.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-worker#worker-evaluate-option-arg)

Optional argument to pass to [pageFunction](https://playwright.dev/docs/api/class-worker#worker-evaluate-option-expression).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-worker#worker-evaluate-return)

---

### evaluateHandle[​](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle "Direct link to evaluateHandle")

Added before v1.9 worker.evaluateHandle

Returns the return value of [pageFunction](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle-option-expression) as a [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle").

The only difference between [worker.evaluate()](https://playwright.dev/docs/api/class-worker#worker-evaluate) and [worker.evaluateHandle()](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle) is that [worker.evaluateHandle()](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle) returns [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle").

If the function passed to the [worker.evaluateHandle()](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [worker.evaluateHandle()](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle) would wait for the promise to resolve and return its value.

**Usage**

```
    await worker.evaluateHandle(pageFunction);
    await worker.evaluateHandle(pageFunction, arg);

```

**Arguments**

- `pageFunction` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle-option-expression)

Function to be evaluated in the worker context.

- `arg` [EvaluationArgument](https://playwright.dev/docs/evaluating#evaluation-argument "EvaluationArgument") _(optional)_[#](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle-option-arg)

Optional argument to pass to [pageFunction](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle-option-expression).

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")>[#](https://playwright.dev/docs/api/class-worker#worker-evaluate-handle-return)

---

### url[​](https://playwright.dev/docs/api/class-worker#worker-url "Direct link to url")

Added before v1.9 worker.url

**Usage**

```
    worker.url();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-worker#worker-url-return)

---

### waitForEvent[​](https://playwright.dev/docs/api/class-worker#worker-wait-for-event "Direct link to waitForEvent")

Added in: v1.57 worker.waitForEvent

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

**Usage**

```
    // Start waiting for download before clicking. Note no await.
    const consolePromise = worker.waitForEvent('console');
    await worker.evaluate('console.log(42)');
    const consoleMessage = await consolePromise;

```

**Arguments**

- `event` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-worker#worker-wait-for-event-option-event)

Event name, same one typically passed into `*.on(event)`.

- `optionsOrPredicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-worker#worker-wait-for-event-option-options-or-predicate)
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")

Receives the event data and resolves to truthy value when the waiting should resolve.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

Maximum time to wait for in milliseconds. Defaults to `0` \- no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

Either a predicate that receives an event or an options object. Optional.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") _(optional)_[#](https://playwright.dev/docs/api/class-worker#worker-wait-for-event-option-predicate)

Receives the event data and resolves to truthy value when the waiting should resolve.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-worker#worker-wait-for-event-return)

---

## Events[​](https://playwright.dev/docs/api/class-worker#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-worker#worker-event-close "Direct link to on('close')")

Added before v1.9 worker.on('close')

Emitted when this dedicated [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) is terminated.

**Usage**

```
    worker.on('close', data => {});

```

**Event data**

- [Worker](https://playwright.dev/docs/api/class-worker "Worker")

---

### on('console')[​](https://playwright.dev/docs/api/class-worker#worker-event-console "Direct link to on('console')")

Added in: v1.57 worker.on('console')

Emitted when JavaScript within the worker calls one of console API methods, e.g. `console.log` or `console.dir`.

**Usage**

```
    worker.on('console', data => {});

```

**Event data**

- [ConsoleMessage](https://playwright.dev/docs/api/class-consolemessage "ConsoleMessage")
