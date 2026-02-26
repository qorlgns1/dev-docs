---
title: 'MCP 서버 계측 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module

# MCP 서버 계측 | Next.js용 Sentry

Sentry의 [MCP monitoring](https://docs.sentry.io/ai/monitoring/mcp.md)을 사용하면 전체 스택 컨텍스트와 함께 MCP 서버를 추적하고 디버깅할 수 있습니다. 도구 실행, 프롬프트 조회, 리소스 접근, 오류율을 모니터링할 수 있습니다. MCP 모니터링 데이터는 로그, 오류, 트레이스 같은 다른 Sentry 데이터와 완전히 연결됩니다.

JavaScript로 MCP 모니터링을 설정하기 위한 사전 요구사항으로, 먼저 [set up tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)을 완료해야 합니다. 이 작업이 끝나면 JavaScript SDK가 지원되는 라이브러리로 생성된 MCP 서버를 자동으로 계측합니다. 이 방식이 사용 사례에 맞지 않으면 아래에 설명된 사용자 지정 계측을 사용할 수 있습니다.

## [자동 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#automatic-instrumentation)

JavaScript SDK는 MCP 서버에 대한 자동 계측을 지원합니다. MCP 작업에 대한 span을 자동으로 수집하려면 Sentry 설정에 MCP 통합을 추가하는 것을 권장합니다.

* [MCP (Model Context Protocol)](https://docs.sentry.io/ai/monitoring/mcp/getting-started.md)

## [수동 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#manual-instrumentation)

MCP 데이터가 Sentry에 표시되려면, 잘 정의된 이름과 데이터 속성으로 span이 생성되어야 합니다. 계측할 수 있는 MCP 작업 유형은 아래를 참고하세요.

이러한 span을 생성하려면 [Sentry.startSpan()](https://docs.sentry.io/platforms/javascript/tracing/instrumentation/custom-instrumentation.md#starting-a-span) 메서드를 사용할 수 있습니다.

## [Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#spans)

- [도구 실행 Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#tool-execution-span)

MCP 도구 실행을 설명합니다.

이 span을 만들 때 [@sentry\_sdk.trace()](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md#span-templates) 데코레이터도 사용할 수 있습니다.

* span의 `op`는 MUST `"mcp.server"`여야 합니다.
* span `name`은 SHOULD `"tools/call {mcp.tool.name}"`여야 합니다.
* `mcp.tool.name` 속성은 MUST 도구 이름으로 설정되어야 합니다. (예: `"get_weather"`)
* `mcp.method.name` 속성은 SHOULD `"tools/call"`로 설정되어야 합니다.
* [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes)는 모두 SHOULD 설정되어야 합니다.

span의 추가 속성:

| 데이터 속성                      | 타입    | 요구 수준          | 설명                                                     | 예시                                              |
| ------------------------------- | ------- | ----------------- | -------------------------------------------------------- | ------------------------------------------------- |
| `mcp.tool.name`                 | string  | 필수              | 호출되는 MCP 도구의 이름입니다.                          | `"get_weather"`                                   |
| `mcp.method.name`               | string  | 권장              | "tools/call"로 설정하는 것이 좋습니다.                   | `"tools/call"`                                    |
| `mcp.request.id`                | string  | 선택              | MCP 요청의 고유 식별자입니다.                            | `"req_123abc"`                                    |
| `mcp.request.argument.*`        | any     | 선택              | 도구 입력 인수입니다 (`send_default_pii=True` 필요).    | `mcp.request.argument.city`에 대한 `"San Francisco"` |
| `mcp.tool.result.content`       | string  | 선택              | 도구 실행의 결과/출력 콘텐츠입니다.                      | `"The weather is sunny"`                          |
| `mcp.tool.result.content_count` | int     | 선택              | 도구 결과의 항목/키 개수입니다.                          | `5`                                               |
| `mcp.tool.result.is_error`      | boolean | 선택              | 도구 실행 결과가 오류였는지 여부입니다.                  | `True`                                            |

#
- [도구 실행 Span 예시:](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#example-tool-execution-span)

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  // ... your Sentry configuration
});

// Example tool execution
const toolName = "get_weather";
const toolArguments = { city: "San Francisco" };

await Sentry.startSpan(
  {
    op: "mcp.server",
    name: `tools/call ${toolName}`,
  },
  async (span) => {
    // Set MCP-specific attributes
    span.setAttribute("mcp.tool.name", toolName);
    span.setAttribute("mcp.method.name", "tools/call");

    // Set request metadata
    span.setAttribute("mcp.request.id", "req_123abc");
    span.setAttribute("mcp.session.id", "session_xyz789");
    span.setAttribute("mcp.transport", "stdio"); // or "http", "sse" for HTTP/WebSocket/SSE
    span.setAttribute("network.transport", "pipe"); // or "tcp" for HTTP/SSE

    // Set tool arguments (optional, requires recordInputs: true)
    for (const [key, value] of Object.entries(toolArguments)) {
      span.setAttribute(`mcp.request.argument.${key}`, value);
    }

    // Execute the tool
    try {
      const result = executeTool(toolName, toolArguments);

      // Set result data
      span.setAttribute("mcp.tool.result.content", JSON.stringify(result));
      span.setAttribute("mcp.tool.result.is_error", false);

      // Set result content count if applicable
      if (
        Array.isArray(result) ||
        (typeof result === "object" && result !== null)
      ) {
        span.setAttribute(
          "mcp.tool.result.content_count",
          Array.isArray(result)
            ? result.length
            : Object.keys(result).length,
        );
      }
    } catch (error) {
      span.setAttribute("mcp.tool.result.is_error", true);
      throw error;
    }
  },
);
```

- [프롬프트 조회 Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#prompt-retrieval-span)

MCP 프롬프트 조회를 설명합니다.

이 span을 만들 때 [@sentry\_sdk.trace()](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md#span-templates) 데코레이터도 사용할 수 있습니다.

* span의 `op`는 MUST `"mcp.server"`여야 합니다.
* span `name`은 SHOULD `"prompts/get {mcp.prompt.name}"`여야 합니다.
* `mcp.prompt.name` 속성은 MUST 프롬프트 이름으로 설정되어야 합니다. (예: `"code_review"`)
* `mcp.method.name` 속성은 SHOULD `"prompts/get"`로 설정되어야 합니다.
* [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes)는 모두 SHOULD 설정되어야 합니다.

span의 추가 속성:

| 데이터 속성                          | 타입   | 요구 수준          | 설명                                                                              | 예시                                           |
| ----------------------------------- | ------ | ----------------- | --------------------------------------------------------------------------------- | ---------------------------------------------- |
| `mcp.prompt.name`                   | string | 필수              | 조회되는 MCP 프롬프트의 이름입니다.                                               | `"code_review"`                                |
| `mcp.method.name`                   | string | 권장              | "prompts/get"으로 설정하는 것이 좋습니다.                                         | `"prompts/get"`                                |
| `mcp.request.id`                    | string | 선택              | MCP 요청의 고유 식별자입니다.                                                     | `"req_456def"`                                 |
| `mcp.request.argument.*`            | any    | 선택              | 프롬프트 입력 인수입니다 (`send_default_pii=True` 필요).                          | `mcp.request.argument.language`에 대한 `"python"` |
| `mcp.prompt.result.message_content` | string | 선택              | 프롬프트 조회의 메시지 콘텐츠입니다 (`send_default_pii=True` 필요).               | `"Review the following code..."`               |
| `mcp.prompt.result.message_role`    | string | 선택              | 메시지 역할입니다 (단일 메시지 프롬프트에만 해당).                                | `"user"`, `"assistant"`, `"system"`            |
| `mcp.prompt.result.message_count`   | int    | 선택              | 프롬프트 결과에 포함된 메시지 수입니다.                                           | `1`, `3`                                       |

#
- [프롬프트 조회 Span 예시:](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#example-prompt-retrieval-span)

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  // ... your Sentry configuration
});

// Example prompt retrieval
const promptName = "code_review";
const promptArguments = { language: "python" };

await Sentry.startSpan(
  {
    op: "mcp.server",
    name: `prompts/get ${promptName}`,
  },
  async (span) => {
    // Set MCP-specific attributes
    span.setAttribute("mcp.prompt.name", promptName);
    span.setAttribute("mcp.method.name", "prompts/get");

    // Set request metadata
    span.setAttribute("mcp.request.id", "req_456def");
    span.setAttribute("mcp.session.id", "session_xyz789");
    span.setAttribute("mcp.transport", "http");
    span.setAttribute("network.transport", "tcp");

    // Set prompt arguments (optional, requires recordInputs: true)
    for (const [key, value] of Object.entries(promptArguments)) {
      span.setAttribute(`mcp.request.argument.${key}`, value);
    }

    // Retrieve the prompt
    const promptResult = getPrompt(promptName, promptArguments);

    // Set result data
    const messages = promptResult.messages || [];
    span.setAttribute("mcp.prompt.result.message_count", messages.length);

    // For single-message prompts, set role and content
    if (messages.length === 1) {
      span.setAttribute(
        "mcp.prompt.result.message_role",
        messages[0].role,
      );
      // Content may contain sensitive data, only set if recordOutputs: true
      span.setAttribute(
        "mcp.prompt.result.message_content",
        JSON.stringify(messages[0].content),
      );
    }
  },
);
```

- [리소스 읽기 Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#resource-read-span)

MCP 리소스 접근을 설명합니다.

이 span을 만들 때 [@sentry\_sdk.trace()](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md#span-templates) 데코레이터도 사용할 수 있습니다.

* span의 `op`는 MUST `"mcp.server"`여야 합니다.
* span `name`은 SHOULD `"resources/read {mcp.resource.uri}"`여야 합니다.
* `mcp.resource.uri` 속성은 MUST 리소스의 URI로 설정되어야 합니다. (예: `"file:///path/to/resource"`)
* `mcp.method.name` 속성은 SHOULD `"resources/read"`로 설정되어야 합니다.
* [Common Span Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes)는 모두 SHOULD 설정되어야 합니다.

span의 추가 속성:

| 데이터 속성              | 타입   | 요구 수준          | 설명                                       | 예시                          |
| ----------------------- | ------ | ----------------- | ------------------------------------------ | ----------------------------- |
| `mcp.resource.uri`      | string | 필수              | 접근되는 MCP 리소스의 URI입니다.           | `"file:///path/to/resource"`  |
| `mcp.method.name`       | string | 권장              | "resources/read"로 설정하는 것이 좋습니다. | `"resources/read"`            |
| `mcp.request.id`        | string | 선택              | MCP 요청의 고유 식별자입니다.              | `"req_789ghi"`                |
| `mcp.resource.protocol` | string | 선택              | MCP 리소스 URI의 프로토콜/스킴입니다.      | `"file"`, `"http"`, `"https"` |

#
- [리소스 읽기 Span 예시:](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#example-resource-read-span)

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  // ... your Sentry configuration
});

// Example resource access
const resourceUri = "file:///path/to/resource.txt";

await Sentry.startSpan(
  {
    op: "mcp.server",
    name: `resources/read ${resourceUri}`,
  },
  async (span) => {
    // Set MCP-specific attributes
    span.setAttribute("mcp.resource.uri", resourceUri);
    span.setAttribute("mcp.method.name", "resources/read");

    // Set request metadata
    span.setAttribute("mcp.request.id", "req_789ghi");
    span.setAttribute("mcp.session.id", "session_xyz789");
    span.setAttribute("mcp.transport", "http");
    span.setAttribute("network.transport", "tcp");

    // Access the resource
    const resourceData = readResource(resourceUri);
  },
);
```

## [공통 Span 속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/mcp-module.md#common-span-attributes)

다음 속성은 모든 MCP span 유형에서 공통으로 사용되며, 사용할 수 있을 때 SHOULD 설정되어야 합니다:

| 데이터 속성          | 타입   | 요구 수준          | 설명                                           | 예시                       |
| ------------------- | ------ | ----------------- | ---------------------------------------------- | -------------------------- |
| `mcp.transport`     | string | 권장              | MCP 통신에 사용된 전송 방식입니다.             | `"stdio"`, `"sse", "http"` |
| `network.transport` | string | 권장              | 사용된 네트워크 전송 방식입니다.               | `"pipe"`, `"tcp"`          |
| `mcp.session.id`    | string | 권장              | MCP 연결의 세션 식별자입니다.                  | `"a1b2c3d4e5f6"`           |
| `mcp.request.id`    | string | 선택              | MCP 요청의 고유 식별자입니다.                  | `"req_123abc"`             |

