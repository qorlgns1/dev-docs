---
title: "WebSocket"
description: "The WebSocket class represents WebSocket connections within a page. It provides the ability to inspect and manipulate the data being transmitted and r..."
---

Source URL: https://playwright.dev/docs/api/class-websocket

# WebSocket | Playwright

The [WebSocket](https://playwright.dev/docs/api/class-websocket "WebSocket") class represents WebSocket connections within a page. It provides the ability to inspect and manipulate the data being transmitted and received.

If you want to intercept or modify WebSocket frames, consider using [WebSocketRoute](https://playwright.dev/docs/api/class-websocketroute "WebSocketRoute").

---

## Methods[​](https://playwright.dev/docs/api/class-websocket#methods "Direct link to Methods")

### isClosed[​](https://playwright.dev/docs/api/class-websocket#web-socket-is-closed "Direct link to isClosed")

Added before v1.9 webSocket.isClosed

Indicates that the web socket has been closed.

**Usage**

```
    webSocket.isClosed();

```

**Returns**

- [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[#](https://playwright.dev/docs/api/class-websocket#web-socket-is-closed-return)

---

### url[​](https://playwright.dev/docs/api/class-websocket#web-socket-url "Direct link to url")

Added before v1.9 webSocket.url

Contains the URL of the WebSocket.

**Usage**

```
    webSocket.url();

```

**Returns**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-websocket#web-socket-url-return)

---

### waitForEvent[​](https://playwright.dev/docs/api/class-websocket#web-socket-wait-for-event "Direct link to waitForEvent")

Added before v1.9 webSocket.waitForEvent

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy value. Will throw an error if the webSocket is closed before the event is fired. Returns the event data value.

**Usage**

```
    await webSocket.waitForEvent(event);
    await webSocket.waitForEvent(event, optionsOrPredicate, options);

```

**Arguments**

- `event` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-websocket#web-socket-wait-for-event-option-event)

Event name, same one would pass into `webSocket.on(event)`.

- `optionsOrPredicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") | [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-websocket#web-socket-wait-for-event-option-options-or-predicate)
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")

Receives the event data and resolves to truthy value when the waiting should resolve.

    * `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_

Maximum time to wait for in milliseconds. Defaults to `0` \- no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

Either a predicate that receives an event or an options object. Optional.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `predicate` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function") _(optional)_[#](https://playwright.dev/docs/api/class-websocket#web-socket-wait-for-event-option-predicate)

Receives the event data and resolves to truthy value when the waiting should resolve.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-websocket#web-socket-wait-for-event-return)

---

## Events[​](https://playwright.dev/docs/api/class-websocket#events "Direct link to Events")

### on('close')[​](https://playwright.dev/docs/api/class-websocket#web-socket-event-close "Direct link to on('close')")

Added before v1.9 webSocket.on('close')

Fired when the websocket closes.

**Usage**

```
    webSocket.on('close', data => {});

```

**Event data**

- [WebSocket](https://playwright.dev/docs/api/class-websocket "WebSocket")

---

### on('framereceived')[​](https://playwright.dev/docs/api/class-websocket#web-socket-event-frame-received "Direct link to on('framereceived')")

Added in: v1.9 webSocket.on('framereceived')

Fired when the websocket receives a frame.

**Usage**

```
    webSocket.on('framereceived', data => {});

```

**Event data**

- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")
  - `payload` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

frame payload

---

### on('framesent')[​](https://playwright.dev/docs/api/class-websocket#web-socket-event-frame-sent "Direct link to on('framesent')")

Added in: v1.9 webSocket.on('framesent')

Fired when the websocket sends a frame.

**Usage**

```
    webSocket.on('framesent', data => {});

```

**Event data**

- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")
  - `payload` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

frame payload

---

### on('socketerror')[​](https://playwright.dev/docs/api/class-websocket#web-socket-event-socket-error "Direct link to on('socketerror')")

Added in: v1.9 webSocket.on('socketerror')

Fired when the websocket has an error.

**Usage**

```
    webSocket.on('socketerror', data => {});

```

**Event data**

- [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")
