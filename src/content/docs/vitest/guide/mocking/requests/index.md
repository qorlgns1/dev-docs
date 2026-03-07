---
title: "요청 모킹"
description: "Vitest는 Node에서 실행되기 때문에 네트워크 요청을 모킹하는 일은 까다롭습니다. 웹 API를 사용할 수 없으므로, 네트워크 동작을 대신 흉내 내는 도구가 필요합니다. 이를 위해 Mock Service Worker 사용을 권장합니다. 이 도구는 , ,  네트워크 ..."
---

출처 URL: https://vitest.dev/guide/mocking/requests

# 요청 모킹

Vitest는 Node에서 실행되기 때문에 네트워크 요청을 모킹하는 일은 까다롭습니다. 웹 API를 사용할 수 없으므로, 네트워크 동작을 대신 흉내 내는 도구가 필요합니다. 이를 위해 [Mock Service Worker](https://mswjs.io/) 사용을 권장합니다. 이 도구는 `http`, `WebSocket`, `GraphQL` 네트워크 요청을 모킹할 수 있으며, 특정 프레임워크에 종속되지 않습니다.

Mock Service Worker(MSW)는 테스트가 보내는 요청을 가로채는 방식으로 동작하므로, 애플리케이션 코드를 변경하지 않고도 사용할 수 있습니다. 브라우저에서는 [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)를 사용합니다. Node.js 환경과 Vitest에서는 [`@mswjs/interceptors`](https://github.com/mswjs/interceptors) 라이브러리를 사용합니다. MSW에 대해 더 알아보려면 [소개 문서](https://mswjs.io/docs/)를 참고하세요.

## 구성

[setup file](https://vitest.dev/config/setupfiles)에서 아래와 같이 사용할 수 있습니다.

::: code-group

```js [HTTP Setup]
import { afterAll, afterEach, beforeAll } from "vitest";
import { setupServer } from "msw/node";
import { http, HttpResponse } from "msw";

const posts = [
  {
    userId: 1,
    id: 1,
    title: "first post title",
    body: "first post body",
  },
  // ...
];

export const restHandlers = [
  http.get("https://rest-endpoint.example/path/to/posts", () => {
    return HttpResponse.json(posts);
  }),
];

const server = setupServer(...restHandlers);

// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));

// Close server after all tests
afterAll(() => server.close());

// Reset handlers after each test for test isolation
afterEach(() => server.resetHandlers());
```

```js [GraphQL Setup]
import { afterAll, afterEach, beforeAll } from "vitest";
import { setupServer } from "msw/node";
import { graphql, HttpResponse } from "msw";

const posts = [
  {
    userId: 1,
    id: 1,
    title: "first post title",
    body: "first post body",
  },
  // ...
];

const graphqlHandlers = [
  graphql.query("ListPosts", () => {
    return HttpResponse.json({
      data: { posts },
    });
  }),
];

const server = setupServer(...graphqlHandlers);

// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));

// Close server after all tests
afterAll(() => server.close());

// Reset handlers after each test for test isolation
afterEach(() => server.resetHandlers());
```

```js [WebSocket Setup]
import { afterAll, afterEach, beforeAll } from "vitest";
import { setupServer } from "msw/node";
import { ws } from "msw";

const chat = ws.link("wss://chat.example.com");

const wsHandlers = [
  chat.addEventListener("connection", ({ client }) => {
    client.addEventListener("message", (event) => {
      console.log("Received message from client:", event.data);
      // Echo the received message back to the client
      client.send(`Server received: ${event.data}`);
    });
  }),
];

const server = setupServer(...wsHandlers);

// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));

// Close server after all tests
afterAll(() => server.close());

// Reset handlers after each test for test isolation
afterEach(() => server.resetHandlers());
```

:::

> `onUnhandledRequest: 'error'`로 서버를 구성하면, 대응되는 요청 핸들러가 없는 요청이 발생할 때마다 오류가 발생하도록 보장할 수 있습니다.

## 더 알아보기

MSW로 할 수 있는 일은 훨씬 더 많습니다. 쿠키와 쿼리 파라미터에 접근하고, 모킹된 에러 응답을 정의하는 등 다양한 작업이 가능합니다. MSW로 할 수 있는 모든 내용을 보려면 [공식 문서](https://mswjs.io/docs)를 읽어보세요.
