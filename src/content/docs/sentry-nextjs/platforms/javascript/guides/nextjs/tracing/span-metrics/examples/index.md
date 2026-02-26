---
title: '계측 예제 | Sentry for Next.js'
description: '이 페이지의 샘플 코드는 데모 목적 전용입니다. 프로덕션 환경에 바로 사용할 수 없으며, 사용하는 언어 또는 프레임워크에 직접 적용되지 않을 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples

# 계측 예제 | Sentry for Next.js

이 페이지의 샘플 코드는 데모 목적 전용입니다. 프로덕션 환경에 바로 사용할 수 없으며, 사용하는 언어 또는 프레임워크에 직접 적용되지 않을 수 있습니다.

이 가이드는 애플리케이션 전체 스택에서 자주 발생하는 모니터링 및 디버깅 과제를 해결하기 위해 span 속성과 메트릭을 사용하는 실용적인 예시를 제공합니다. 각 예시는 프런트엔드와 백엔드 컴포넌트를 모두 계측하는 방법을 보여주며, 분산 트레이스 안에서 이들이 함께 동작해 end-to-end 가시성을 제공하는 과정을 설명합니다. 또한 예제 저장소 코드, 워크스루, 탐색할 속성도 확인할 수 있습니다.

## [이커머스 체크아웃 흐름 (React + Backend)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md#e-commerce-checkout-flow-react--backend)

예제 저장소: [Crash Commerce](https://github.com/getsentry/crash-commerce-tracing-sample)

**과제:** end-to-end 체크아웃 흐름을 수집하고, 평균 장바구니 크기와 금액을 파악하며, 프런트엔드와 서버 API 전반에서 결제 제공자의 성능을 진단합니다.

**해결 방법:** 체크아웃 액션에서 클라이언트 span을 시작하고, 체크아웃 흐름의 각 단계마다 백엔드에서 관련 span을 시작합니다. 거래에 사용된 장바구니 크기, 장바구니 금액, 결제 제공자처럼 애플리케이션의 핵심 메트릭을 나타내는 속성을 첨부합니다.

**프런트엔드 (React) - Checkout 클릭 핸들러 계측:**

```javascript
// In your Checkout button click handler
Sentry.startSpan(
  {
    name: 'Checkout',
    op: 'ui.action',
    attributes: {
      'cart.item_count': cartCount,
      'cart.value_minor': cartValueMinor,
      'cart.currency': 'USD',
      'payment.provider.ui_selected': paymentProvider,
    },
  },
  async (span) => {
    try {
      const response = await fetch(`${API_URL}/api/checkout`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ items: cart, paymentProvider }),
      })
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ error: 'Payment failed' }))
        throw new Error(errorData.error || `HTTP ${response.status}`)
      }
      const data: { orderId: string; paymentProvider: string } = await response.json()
      span.setAttribute('order.id', data.orderId)
      span.setAttribute('payment.provider', data.paymentProvider)
      Sentry.logger.info(Sentry.logger.fmt`Order ${data.orderId} confirmed via ${data.paymentProvider}`)

      // Show order confirmation
      setOrderConfirmation({
        orderId: data.orderId,
        provider: data.paymentProvider,
        total: cartValueMinor
      })
      setCart([])
      setIsCartOpen(false)
    } catch (err) {
      span.setStatus({ code: 2, message: 'internal_error' })
      const errorMessage = err instanceof Error ? err.message : 'Checkout failed'
      setCheckoutError(errorMessage)
      Sentry.logger.error(Sentry.logger.fmt`${errorMessage}`)
    } finally {
      setIsCheckingOut(false)
    }
  }
)
```

앱에서 이 코드를 넣을 위치:

* 체크아웃 버튼의 `onClick` 또는 체크아웃 폼/컨테이너 컴포넌트의 submit 핸들러 내부.
* 자동 계측이 클라이언트 `fetch` span을 추가합니다. 애플리케이션의 구체적인 컨텍스트를 위해 명시적 UI span은 유지하세요.

**백엔드 - 주문 처리 span과 결제 span이 포함된 Checkout API:**

```javascript
// Example: Node/Express
app.post('/api/checkout', async (req: Request, res: Response) => {
  await Sentry.startSpan(
    {
      name: 'Order Processing',
      op: 'commerce.order.server',
    },
    async (span) => {
      try {
        const items = (req.body?.items as { productId: string; quantity: number }[]) || []
        const requestedProviderRaw = (req.body?.paymentProvider as string | undefined) ?? undefined
        const requestedProvider = PAYMENT_PROVIDERS.find((p) => p === requestedProviderRaw) ?? pickPaymentProvider()

        // Validate cart
        if (!Array.isArray(items) || items.length === 0) {
          span.setAttribute('payment.status', 'failed')
          span.setAttribute('inventory.reserved', false)
          res.status(400).json({ error: 'Cart is empty' })
          return
        }

        let totalMinor = 0
        for (const line of items) {
          const product = PRODUCTS.find((p) => p.id === line.productId)
          if (!product || line.quantity <= 0) {
            span.setAttribute('payment.status', 'failed')
            span.setAttribute('inventory.reserved', false)
            res.status(400).json({ error: 'Invalid cart item' })
            return
          }
          totalMinor += product.priceMinor * line.quantity
        }

        // Simulate reserving inventory (80% chance true)
        const reserved = Math.random() < 0.8

        // Simulate payment
        const charge = await Sentry.startSpan(
          {
            name: 'Charge Payment Provider',
            op: 'commerce.payment',
            attributes: {
              'payment.provider': requestedProvider,
            },
          },
          async (paymentSpan) => {
            const result = await fakeCharge(totalMinor, requestedProvider)
            paymentSpan.setAttribute('payment.status', result.status)
            return result
          }
        )

        if (charge.status === 'failed' || !reserved) {
          span.setAttribute('payment.provider', charge.provider)
          span.setAttribute('payment.status', 'failed')
          span.setAttribute('inventory.reserved', reserved)
          res.status(402).json({ error: 'Payment failed' })
          return
        }

        const orderId = randomId()
        ORDERS.push({ id: orderId, totalMinor, items })

        // Set attributes before returning
        span.setAttribute('order.id', orderId)
        span.setAttribute('payment.provider', charge.provider)
        span.setAttribute('payment.status', 'success')
        span.setAttribute('inventory.reserved', reserved)

        res.json({ orderId, paymentProvider: charge.provider })
      } catch (err) {
        Sentry.captureException(err)
        res.status(500).json({ error: 'Internal error' })
      }
    }
  )
})
```

**트레이스가 함께 동작하는 방식:**

* 체크아웃이 선택되면 UI span이 시작됨 -> 서버의 `/checkout` API가 호출될 때 서버 백엔드가 추적을 이어가기 위한 span을 시작합니다. 결제가 진행되면 payment span이 시작됩니다.
* 속성과 Span 메트릭을 사용하면 요청 지연 시간뿐 아니라 더 많은 것을 추적할 수 있습니다. `cart.item_count` 및 기타 `cart` 속성으로 스토어의 비즈니스 성과를 추적하고, `payment.provider` 속성의 에러 성능을 확인해 스토어 신뢰성도 점검할 수 있습니다.

**Span 메트릭으로 모니터링할 항목:**

* `cart.item_count` 버킷별 `op:ui.action` checkout의 p95 span.duration.
* `payment.provider`별 `op:payment` 에러율.

## [백그라운드 처리 포함 미디어 업로드 (React + Express)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md#media-upload-with-background-processing-react--express)

예제 저장소: [SnapTrace](https://github.com/getsentry/snaptrace-tracing-example)

**과제:** 트레이스 연속성을 비동기 경계 전반에서 유지하면서, 사용자가 체감하는 업로드 시간, 서버 측 검증, 비동기 미디어 처리(최적화, 썸네일 생성)를 추적합니다.

**해결 방법:** 전체 업로드 경험에 대해 클라이언트 span을 시작하고, 업로드 검증용 백엔드 span과 비동기 미디어 처리용 span을 추가로 만듭니다. 과도한 span 대신 풍부한 속성으로 처리 세부사항을 캡처합니다.

**프런트엔드 (React) - 업로드 액션 계측**

```typescript
// In your UploadForm component's upload handler
const handleUpload = async () => {
  if (!selectedFile) return;

  // Start Sentry span for entire upload operation
  await Sentry.startSpan(
    {
      name: "Upload media",
      op: "file.upload",
      attributes: {
        "file.size_bytes": selectedFile.size,
        "file.mime_type": selectedFile.type,
      },
    },
    async (span) => {
      const uploadStartTime = Date.now();

      try {
        // Single API call to upload and start processing
        const uploadResponse = await fetch(`${API_BASE_URL}/api/upload`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            fileName: selectedFile.name,
            fileType: selectedFile.type,
            fileSize: selectedFile.size,
          }),
        });

        if (!uploadResponse.ok) {
          throw new Error(`Upload failed: ${uploadResponse.statusText}`);
        }

        const uploadData = await uploadResponse.json();

        // Set success attributes
        span.setAttribute("upload.success", true);
        span.setAttribute(
          "upload.duration_ms",
          Date.now() - uploadStartTime,
        );
        span.setAttribute("job.id", uploadData.jobId);

        // Update UI to show processing status
        updateUploadStatus(uploadData.jobId, "processing");
      } catch (error) {
        span.setStatus({ code: 2, message: "error" });
        span.setAttribute("upload.success", false);
        span.setAttribute(
          "upload.error",
          error instanceof Error ? error.message : "Unknown error",
        );
        setUploadStatus("error");
        Sentry.captureException(error);
      }
    },
  );
};
```

앱에서 이 코드를 넣을 위치:

* 업로드 버튼 클릭 핸들러 또는 폼 submit 핸들러
* 드래그 앤 드롭의 onDrop 콜백
* 자동 계측이 fetch span을 수집하며, 명시적 span은 비즈니스 컨텍스트를 추가합니다.

**백엔드 - 업로드 검증 및 큐 작업 등록**

이 예시는 올바른 큐 계측 패턴을 보여줍니다. 큐 계측에 대한 자세한 내용은 [Queues Module documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/queues-module.md)을 참고하세요.

```typescript
// Import Sentry instrumentation first (required for v10)
import "./instrument";
import express from "express";
import * as Sentry from "@sentry/node";

// POST /api/upload - Receive and validate upload, then enqueue for processing
app.post(
  "/api/upload",
  async (req: Request<{}, {}, UploadRequest>, res: Response) => {
    const { fileName, fileType, fileSize } = req.body;

    // Validate the upload
    if (!fileName || !fileType || !fileSize) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    if (fileSize > 50 * 1024 * 1024) {
      // 50MB limit
      return res.status(400).json({ error: "File too large (max 50MB)" });
    }

    // Create a job for processing
    const job = createJob(fileName, fileType, fileSize);

    // Producer span: Enqueue media processing job
    await Sentry.startSpan(
      {
        op: "queue.publish",
        name: "queue_producer",
        attributes: {
          "messaging.message.id": job.id,
          "messaging.destination.name": "media-processing",
          "messaging.message.body.size": fileSize,
        },
      },
      async () => {
        // Get trace headers to pass to consumer
        const { "sentry-trace": sentryTrace, baggage: sentryBaggage } =
          Sentry.getTraceData();

        // Store job with trace headers for async processing
        const enrichedJob = {
          ...job,
          sentryTrace,
          sentryBaggage,
          enqueuedAt: Date.now(),
        };
        await enqueueJob(enrichedJob);

        // Start async processing
        setImmediate(async () => {
          await processMedia(enrichedJob);
        });

        // Respond immediately with job ID
        res.json({
          jobId: job.id,
          status: "accepted",
          message: "Upload received and processing started",
        });
      },
    );
  },
);
```

**백엔드 - 비동기 미디어 처리 (Consumer)**

```typescript
// Async media processing (runs in background via setImmediate)
export async function processMedia(job: ProcessingJob): Promise<void> {
  // Continue trace from producer using stored trace headers
  await Sentry.continueTrace(
    { sentryTrace: job.sentryTrace, baggage: job.sentryBaggage },
    async () => {
      // Parent span for the consumer transaction
      await Sentry.startSpan(
        {
          name: "media_processing_consumer",
        },
        async (parentSpan) => {
          // Consumer span: Process the queued job
          await Sentry.startSpan(
            {
              op: "queue.process",
              name: "queue_consumer",
              attributes: {
                "messaging.message.id": job.id,
                "messaging.destination.name": "media-processing",
                "messaging.message.body.size": job.fileSize,
                "messaging.message.receive.latency":
                  Date.now() - job.enqueuedAt,
                "messaging.message.retry.count": 0,
              },
            },
            async (span) => {
              try {
                const startTime = Date.now();
                const operations: string[] = [];

                // Add job-specific attributes
                span.setAttribute("media.size_bytes", job.fileSize);
                span.setAttribute("media.mime_type", job.fileType);
                span.setAttribute(
                  "media.size_bucket",
                  getSizeBucket(job.fileSize),
                );

                // Simulate image optimization and thumbnail generation
                if (job.fileType.startsWith("image/")) {
                  // Note: No separate spans for these operations - use attributes instead
                  await optimizeImage(); // Simulated delay
                  operations.push("optimize");

                  await generateThumbnail(); // Simulated delay
                  operations.push("thumbnail");
                }

                // Calculate results
                const sizeSaved = Math.floor(job.fileSize * 0.3); // 30% reduction
                const thumbnailCreated = Math.random() > 0.05; // 95% success rate

                // Rich attributes instead of multiple spans
                span.setAttribute(
                  "processing.operations",
                  JSON.stringify(operations),
                );
                span.setAttribute("processing.optimization_level", "high");
                span.setAttribute(
                  "processing.thumbnail_created",
                  thumbnailCreated,
                );
                span.setAttribute(
                  "processing.duration_ms",
                  Date.now() - startTime,
                );
                span.setAttribute("result.size_saved_bytes", sizeSaved);
                span.setAttribute("result.size_reduction_percent", 30);
                span.setAttribute("result.status", "success");

                // Update job status
                job.status = "completed";

                // Mark parent span as successful
                parentSpan.setStatus({ code: 1, message: "ok" });
              } catch (error) {
                span.setAttribute("result.status", "failed");
                span.setAttribute(
                  "error.message",
                  error instanceof Error ? error.message : "Unknown error",
                );
                parentSpan.setStatus({ code: 2, message: "error" });
                Sentry.captureException(error);
              }
            },
          );
        },
      );
    },
  );
}
```

**트레이스가 함께 동작하는 방식:**

* 프런트엔드 span (`file.upload`)은 파일 선택부터 서버 응답까지 전체 사용자 경험을 캡처합니다.
* 백엔드 producer span (`queue.publish`)은 적절한 큐 속성과 함께 작업 enqueue를 추적합니다.
* consumer span (`queue.process`)은 작업에 저장된 trace header로 `continueTrace()`를 사용해 트레이스를 이어갑니다.
* 비동기 처리는 큐 계측으로 연결된 자체 트레이스에서 독립적으로 실행됩니다.
* consumer span의 풍부한 속성이 과도한 자식 span 생성 없이 모든 처리 세부사항을 캡처합니다.
* 이 패턴은 큐 성능 모니터링을 위해 Sentry의 Queues 인사이트 페이지를 채웁니다.

**Span 메트릭으로 모니터링할 항목:**

* `file.size_bucket`별 p95 업로드 시간.
* `media.mime_type`별 처리 성공률.
* `result.status = success` 조건에서 `result.size_saved_bytes`를 통한 평균 저장 용량 절감.
* 처리 지연 추적을 위한 `messaging.message.receive.latency` 기반 큐 지연 시간.
* `op:queue.publish` 및 `op:queue.process` span 수 기반 작업 처리량.

## [검색 자동완성 (디바운스, 취소 가능, 성능 모니터링)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md#search-autocomplete-debounced-cancellable-performance-monitoring)

예제 저장소: [NullFlix](https://github.com/getsentry/nullflix-tracing-example)

**과제:** 사용자가 검색창에 빠르게 입력할 때, 요청 디바운스, 진행 중 호출 취소, 우아한 오류 처리, 서로 다른 쿼리 유형 전반의 성능 모니터링을 수행하면서 예측 가능한 지연 시간을 유지해야 합니다.

**해결 방법:** 디바운스된 각 요청마다 클라이언트 span을 시작하고, 중단된 요청을 표시하며, 검색 패턴을 추적하고, 서버에서는 의미 있는 속성으로 검색 성능을 계측합니다.

**프런트엔드 (React + TypeScript) - 디바운스 검색 계측:**

```typescript
const searchResults = await Sentry.startSpan(
  {
    op: "function",
    name: "Search autocomplete request",
    attributes: {
      "query.length": searchQuery.length,
      "ui.debounce_ms": DEBOUNCE_MS,
    },
  },
  async (span) => {
    try {
      // SDK automatically instruments the fetch with op: 'http.client'
      const response = await fetch(
        `${API_URL}/api/search?${new URLSearchParams({ q: searchQuery })}`,
        {
          signal: controller.signal,
          headers: { "Content-Type": "application/json" },
        },
      );

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        const errorMessage =
          errorData.error || `Search failed: ${response.status}`;
        throw new Error(errorMessage);
      }

      const data: SearchResponse = await response.json();

      span.setAttribute("results.count", data.results.length);
      span.setAttribute("results.has_results", data.results.length > 0);
      span.setAttribute("http.response_size", JSON.stringify(data).length);
      span.setStatus({ code: 1, message: "ok" });

      return data;
    } catch (error) {
      if (error instanceof Error && error.name === "AbortError") {
        span.setAttribute("ui.aborted", true);
        span.setStatus({ code: 2, message: "cancelled" });
        // Don't re-throw AbortError to avoid sending it to Sentry
        return { results: [] };
      }

      span.setStatus({
        code: 2,
        message: error instanceof Error ? error.message : "unknown error",
      });
      throw error;
    }
  },
);
```

앱에서 이 코드를 넣을 위치:

* 검색 입력 컴포넌트에서 디바운스 타임아웃 이후 트리거되도록

**백엔드 (Node.js + Express) - 의미 있는 속성으로 검색 계측:**

```typescript
app.get("/api/search", async (req: Request, res: Response) => {
  await Sentry.startSpan(
    {
      name: "Search",
      op: "search",
    },
    async (span) => {
      try {
        const query = String(req.query.q || "");
        const queryLength = query.length;

        // Check if request was aborted
        req.on("close", () => {
          if (!res.headersSent) {
            span.setStatus({ code: 2, message: "cancelled" });
            span.setAttribute("request.aborted", true);
          }
        });

        if (!query) {
          span.setAttribute("results.count", 0);
          span.setAttribute("search.engine", "elasticsearch");
          return res.json({ results: [] });
        }

        // Perform search
        const startSearch = Date.now();
        const results = await searchMovies(query);
        const searchDuration = Date.now() - startSearch;

        // Set span attributes
        span.setAttribute("search.engine", "elasticsearch");
        span.setAttribute(
          "search.mode",
          queryLength < 3 ? "prefix" : "fuzzy",
        );
        span.setAttribute("results.count", results.length);
        span.setAttribute("query.length", queryLength);

        // Track slow searches
        if (searchDuration > 500) {
          span.setAttribute("performance.slow", true);
          span.setAttribute("search.duration_ms", searchDuration);
        }

        return res.json({ results });
      } catch (error: any) {
        span.setStatus({ code: 2, message: error?.message || "error" });
        span.setAttribute(
          "error.type",
          (error as any)?.constructor?.name || "Error",
        );

        Sentry.captureException(error);
        if (!res.headersSent) {
          return res.status(500).json({ error: "Search failed" });
        }
      }
    },
  );
});
```

**트레이스가 함께 동작하는 방식:**

* 클라이언트 span은 디바운스 검색이 트리거될 때 시작되어, 사용자가 체감하는 전체 지연 시간을 추적합니다.
* 중단된 요청은 `ui.aborted=true` 및 짧은 duration으로 표시되어, 낭비된 작업을 보여줍니다.
* 서버 span은 검색 성능 특성(모드(prefix vs fuzzy), 결과 수, 느린 쿼리)을 보여줍니다.

**Span 메트릭으로 모니터링할 항목:**

* `query.length`로 그룹화한 `op:search`의 p95 duration.
* `op:search performance.slow:true`를 통한 느린 검색 특성.
* `search.mode`로 그룹화한 `op:search`를 통해 prefix와 fuzzy 비교.
* `op:http.client ui.aborted:true`를 통한 취소율.
* `op:http.client results.has_results:false`를 통한 빈 결과 비율.
* 페이로드 최적화를 위한 `http.response_size` 분포.
* `status:error`로 필터링한 `op:search` 에러율.
* `op:search request.aborted:true`를 통한 백엔드 중단 비율.

## [수동 LLM 계측 (커스텀 AI 에이전트 + Tool Calls)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md#manual-llm-instrumentation-custom-ai-agent--tool-calls)

예제 저장소: [Customer Service Bot](https://github.com/getsentry/llm-manual-agent-monitoring-example)

**과제:** 독점 LLM API(OpenAI/Anthropic 아님)를 사용하고, tool call을 포함한 다단계 추론을 수행하는 커스텀 AI 에이전트를 구축하면서, 전체 대화 흐름 전반에서 토큰 사용량, 도구 성능, 에이전트 효과를 추적하기 위한 포괄적 모니터링이 필요합니다.

**해결 방법:** Sentry의 AI 에이전트 span 규약을 사용해 AI 파이프라인의 각 컴포넌트를 수동 계측합니다. 에이전트 호출, LLM 호출, 도구 실행, 에이전트 간 handoff에 대한 span을 만들고, 비용/성능/비즈니스 메트릭 모니터링을 위한 풍부한 속성을 추가합니다.

이 예시는 Sentry의 AI Agents Module 규약을 따릅니다. `gen_ai.*` span 속성과 요구사항의 상세 명세는 [AI Agents Module documentation](https://develop.sentry.dev/sdk/telemetry/traces/modules/ai-agents/)를 참고하세요.

**프런트엔드 (React) - AI 채팅 인터페이스 계측:**

```typescript
import { useState, useEffect } from 'react';
import { SEMANTIC_ATTRIBUTE_SENTRY_ORIGIN } from '@sentry/core';

// In your AI chat component
export default function CustomerSupportChat() {
  const [conversationHistory, setConversationHistory] = useState([]);
  const [sessionId, setSessionId] = useState('');

  // Generate sessionId on client-side only to avoid hydration mismatch
  useEffect(() => {
    setSessionId(`session_${Date.now()}`);
  }, []);

const handleSendMessage = async (userMessage: string) => {
  await Sentry.startSpan(
    {
      name: 'invoke_agent Customer Support Agent',
      op: 'gen_ai.invoke_agent',
      attributes: {
        'gen_ai.operation.name': 'invoke_agent',
        'gen_ai.agent.name': 'Customer Support Agent',
        'gen_ai.system': 'custom-llm',
        'gen_ai.request.model': 'custom-model-v2',
        'gen_ai.response.model': 'custom-model-v2',
        'gen_ai.request.messages': JSON.stringify([
          { role: 'system', content: 'You are a helpful customer support agent.' },
          ...conversationHistory,
          { role: 'user', content: userMessage }
        ]),
        [SEMANTIC_ATTRIBUTE_SENTRY_ORIGIN]: 'manual.ai.custom-llm',
        'conversation.turn': conversationHistory.length + 1,
        'conversation.session_id': sessionId,
      },
    },
    async (agentSpan) => {
      try {
        setIsLoading(true);

        // Call your backend AI agent endpoint
        const response = await fetch('/api/ai/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            message: userMessage,
            sessionId: sessionId,
            conversationHistory: conversationHistory
          })
        });

        if (!response.ok) {
          throw new Error(`AI request failed: ${response.status}`);
        }

        const aiResponse = await response.json();

        // Set response attributes
        agentSpan.setAttribute('gen_ai.response.text', aiResponse.message);
        agentSpan.setAttribute('gen_ai.response.id', aiResponse.responseId);
        agentSpan.setAttribute('gen_ai.response.model', 'custom-model-v2');
        agentSpan.setAttribute('gen_ai.usage.total_tokens', aiResponse.totalTokens);
        agentSpan.setAttribute('conversation.tools_used', aiResponse.toolsUsed?.length || 0);
        agentSpan.setAttribute('conversation.resolution_status', aiResponse.resolutionStatus);

        // Update UI with response
        setConversationHistory(prev => [
          ...prev,
          { role: 'user', content: userMessage },
          { role: 'assistant', content: aiResponse.message }
        ]);

        Sentry.logger.info(Sentry.logger.fmt`AI agent completed conversation turn ${conversationHistory.length + 1}`);

      } catch (error) {
        agentSpan.setStatus({ code: 2, message: 'internal_error' });
        agentSpan.setAttribute('error.type', error instanceof Error ? error.constructor.name : 'UnknownError');
        setError('Failed to get AI response. Please try again.');
        Sentry.logger.error(Sentry.logger.fmt`AI agent failed: ${error instanceof Error ? error.message : 'Unknown error'}`);
      } finally {
        setIsLoading(false);
      }
    }
  );
};
```

앱에서 이 코드를 넣을 위치:

* 애플리케이션에서 채팅 핸들러 응답을 제어하는 API 내부

**중요:** Server-Side Rendering (SSR) 사용 시 hydration 오류를 피하려면 `useEffect`에서 `sessionId`를 생성하세요. 컴포넌트 초기화 중 `Date.now()` 또는 랜덤 값을 사용하면 서버 렌더와 클라이언트 렌더 간 불일치가 발생합니다.

**백엔드 - Tool Calls를 포함한 커스텀 LLM 통합:**

```typescript
import { SEMANTIC_ATTRIBUTE_SENTRY_ORIGIN } from "@sentry/core";

// Express API route for custom AI agent
app.post("/api/ai/chat", async (req: Request, res: Response) => {
  const { message, sessionId, conversationHistory } = req.body;

  // Main agent invocation span (matches frontend)
  await Sentry.startSpan(
    {
      name: "invoke_agent Customer Support Agent",
      op: "gen_ai.invoke_agent",
      attributes: {
        "gen_ai.operation.name": "invoke_agent",
        "gen_ai.agent.name": "Customer Support Agent",
        "gen_ai.system": "custom-llm",
        "gen_ai.request.model": "custom-model-v2",
        [SEMANTIC_ATTRIBUTE_SENTRY_ORIGIN]: "manual.ai.custom-llm",
        "conversation.session_id": sessionId,
      },
    },
    async (agentSpan) => {
      try {
        const tools = [
          {
            name: "search_knowledge_base",
            description: "Search company knowledge base for answers",
          },
        ];

        agentSpan.setAttribute(
          "gen_ai.request.available_tools",
          JSON.stringify(tools),
        );

        let totalTokens = 0;
        let toolsUsed: string[] = [];
        let finalResponse = "";

        // Step 1: Call custom LLM for initial reasoning
        const llmResponse = await Sentry.startSpan(
          {
            name: "chat custom-model-v2",
            op: "gen_ai.request",
            attributes: {
              "gen_ai.operation.name": "summarize",
              "gen_ai.system": "custom-llm",
              "gen_ai.request.model": "custom-model-v2",
              "gen_ai.request.messages": JSON.stringify([
                {
                  role: "system",
                  content:
                    "You are a customer support agent. Use tools when needed.",
                },
                ...conversationHistory,
                { role: "user", content: message },
              ]),
              "gen_ai.request.temperature": 0.7,
              "gen_ai.request.max_tokens": 500,
              [SEMANTIC_ATTRIBUTE_SENTRY_ORIGIN]: "manual.ai.custom-llm",
            },
          },
          async (llmSpan) => {
            const llmData = await callCustomLLM(
              message,
              conversationHistory,
            );

            // Set LLM response attributes
            llmSpan.setAttribute(
              "gen_ai.response.text",
              llmData.choices[0].message.content || "",
            );
            llmSpan.setAttribute("gen_ai.response.id", llmData.id);
            llmSpan.setAttribute("gen_ai.response.model", llmData.model);
            llmSpan.setAttribute(
              "gen_ai.usage.input_tokens",
              llmData.usage.prompt_tokens,
            );
            llmSpan.setAttribute(
              "gen_ai.usage.output_tokens",
              llmData.usage.completion_tokens,
            );
            llmSpan.setAttribute(
              "gen_ai.usage.total_tokens",
              llmData.usage.total_tokens,
            );

            if (llmData.choices[0].message.tool_calls) {
              llmSpan.setAttribute(
                "gen_ai.response.tool_calls",
                JSON.stringify(llmData.choices[0].message.tool_calls),
              );
            }

            totalTokens += llmData.usage.total_tokens;
            return llmData;
          },
        );

        // Step 2: Execute tool calls if present
        if (llmResponse.choices[0].message.tool_calls) {
          for (const toolCall of llmResponse.choices[0].message
            .tool_calls) {
            await Sentry.startSpan(
              {
                name: `execute_tool ${toolCall.function.name}`,
                op: "gen_ai.execute_tool",
                attributes: {
                  "gen_ai.operation.name": "execute_tool",
                  "gen_ai.tool.name": toolCall.function.name,
                  "gen_ai.tool.type": "function",
                  "gen_ai.tool.input": toolCall.function.arguments,
                  [SEMANTIC_ATTRIBUTE_SENTRY_ORIGIN]:
                    "manual.ai.custom-llm",
                },
              },
              async (toolSpan) => {
                const toolOutput = await searchKnowledgeBase(
                  JSON.parse(toolCall.function.arguments).query,
                );

                toolSpan.setAttribute("gen_ai.tool.output", toolOutput);
                toolSpan.setAttribute(
                  "search.query",
                  JSON.parse(toolCall.function.arguments).query,
                );
                toolsUsed.push(toolCall.function.name);
              },
            );
          }

          // Step 3: Synthesize final response from tool results
          const synthesis = await synthesizeResponse(
            llmResponse,
            toolsUsed,
          );
          finalResponse = synthesis.message;
          totalTokens += synthesis.usage.total_tokens;
        } else {
          // No tools used - use original message content
          finalResponse = llmResponse.choices[0].message.content;
        }

        // Set final agent attributes
        const resolutionStatus =
          toolsUsed.length > 0 ? "resolved" : "answered";

        agentSpan.setAttribute("gen_ai.response.text", finalResponse);
        agentSpan.setAttribute("gen_ai.response.id", llmResponse.id);
        agentSpan.setAttribute("gen_ai.usage.total_tokens", totalTokens);
        agentSpan.setAttribute(
          "conversation.tools_used",
          JSON.stringify(toolsUsed),
        );
        agentSpan.setAttribute(
          "conversation.resolution_status",
          resolutionStatus,
        );

        res.json({
          message: finalResponse,
          responseId: llmResponse.id,
          totalTokens,
          toolsUsed,
          resolutionStatus,
        });
      } catch (error) {
        agentSpan.setStatus({
          code: 2,
          message: "agent_invocation_failed",
        });
        agentSpan.setAttribute(
          "error.type",
          error instanceof Error ? error.constructor.name : "UnknownError",
        );
        Sentry.captureException(error);
        res.status(500).json({ error: "AI agent processing failed" });
      }
    },
  );
});

// Helper functions for tool execution
async function searchKnowledgeBase(query: string): Promise<string> {
  // Search company knowledge base - returns relevant policy info
  const results = [
    "Our return policy allows returns within 30 days of purchase.",
    "Refunds are processed within 5-7 business days after we receive the item.",
    "Items must be in original condition with tags attached.",
    "Free return shipping is provided for defective items.",
  ];
  return results.join("\n");
}

async function synthesizeResponse(
  llmResponse: any,
  toolsUsed: string[],
): Promise<any> {
  // Make final LLM call to synthesize tool results into response
  return {
    message: "Based on the information I found, here's your answer...",
    usage: { total_tokens: 150 },
  };
}
```

**트레이스가 함께 동작하는 방식:**

* 프런트엔드 span (`gen_ai.invoke_agent`)은 메시지부터 응답까지 전체 사용자 상호작용을 캡처합니다.
* 백엔드 에이전트 span은 상관관계를 위해 동일한 operation과 agent name으로 트레이스를 이어갑니다.
* LLM span (`gen_ai.request`)은 토큰 사용량과 성능을 포함해 개별 모델 호출을 추적합니다.
* 도구 실행 span (`gen_ai.execute_tool`)은 각 tool call의 입력/출력과 타이밍을 모니터링합니다.
* 풍부한 속성으로 대화 품질, 비용, 비즈니스 성과를 모니터링할 수 있습니다.

**Span 메트릭으로 모니터링할 항목:**

* `conversation.resolution_status`로 그룹화한 `op:gen_ai.invoke_agent`의 p95 duration.
* `gen_ai.request.model`별 `gen_ai.usage.total_tokens` 기반 토큰 사용 추세.
* `gen_ai.tool.name`로 그룹화한 `op:gen_ai.execute_tool` 기반 도구 사용 패턴.
* 기간별 집계한 `conversation.cost_estimate_usd` 기반 비용 분석.
* `conversation.resolution_status` 분포 기반 에이전트 효과.
* 각 컴포넌트의 에러율: `op:gen_ai.request`, `op:gen_ai.execute_tool`, `op:gen_ai.invoke_agent`.

