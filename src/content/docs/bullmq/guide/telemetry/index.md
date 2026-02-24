---
title: '텔레메트리'
description: '원본 URL: https://docs.bullmq.io/guide/telemetry'
---

원본 URL: https://docs.bullmq.io/guide/telemetry

# 텔레메트리

BullMQ는 외부 텔레메트리 백엔드와 통합할 수 있는 Telemetry 인터페이스를 제공합니다. 현재는 텔레메트리 목적의 새로운 사실상 표준인 [OpenTelemetry](https://opentelemetry.io) 사양을 지원하며, 이 인터페이스는 향후 다른 백엔드도 지원할 수 있을 만큼 유연합니다.

텔레메트리는 시스템에 대한 상세하고 전체적인 개요가 필요한 대규모 애플리케이션에서 매우 유용합니다. BullMQ에서는 작업의 전체 생명주기 동안 작업이 가질 수 있는 다양한 상태를 파악하는 데 도움이 됩니다. 대규모 애플리케이션에서는 작업의 출처와, 작업 또는 메시지가 시스템의 다른 부분과 수행할 수 있는 모든 상호작용을 추적하는 데 도움이 됩니다.

