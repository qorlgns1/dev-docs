---
title: '변경 로그'
---

Source URL: https://docs.bullmq.io/elixir/changelog

# 변경 로그

### [1.2.6](https://github.com/taskforcesh/bullmq/compare/vex1.2.5...vex1.2.6) (2026-02-11)

#### 버그 수정

* 중요한 성능 수정 및 개선 \[elixir] ([#3749](https://github.com/taskforcesh/bullmq/issues/3749)) ([5905423](https://github.com/taskforcesh/bullmq/commit/590542314f13590cf68330097f5bb09a96bb240c))

### [1.2.5](https://github.com/taskforcesh/bullmq/compare/vex1.2.4...vex1.2.5) (2026-01-27)

#### 버그 수정

* **scheduler:** 후속 반복 작업이 생성되지 않던 job scheduler 문제 수정 \[elixir] ([#3729](https://github.com/taskforcesh/bullmq/issues/3729)) ([3bd23d9](https://github.com/taskforcesh/bullmq/commit/3bd23d990c780ff0808d79499edd803084d2efe8))

### [1.2.4](https://github.com/taskforcesh/bullmq/compare/vex1.2.3...vex1.2.4) (2026-01-24)

#### 버그 수정

* cluster에서 worker connection name 수정 [#3340](https://github.com/taskforcesh/bullmq/issues/3340) (elixir) (python) ([#3660](https://github.com/taskforcesh/bullmq/issues/3660)) ([fa22e84](https://github.com/taskforcesh/bullmq/commit/fa22e844d29961db95df58f2ae63b440d71c11f6))

### [1.2.3](https://github.com/taskforcesh/bullmq/compare/vex1.2.2...vex1.2.3) (2026-01-22)

#### 성능 개선

* **job:** 최대 보관 기간 기준으로 작업을 제거할 때 limit 적용 (python) (elixir) ([#3694](https://github.com/taskforcesh/bullmq/issues/3694)) fixes [#3672](https://github.com/taskforcesh/bullmq/issues/3672) ([a8fc316](https://github.com/taskforcesh/bullmq/commit/a8fc316c0989bd3edb54577ceb02bff0c600aa93))

### [1.2.2](https://github.com/taskforcesh/bullmq/compare/vex1.2.1...vex1.2.2) (2026-01-14)

#### 버그 수정

* **scripts:** mix config에 누락된 lua scripts 추가 \[elixir] ([#3697](https://github.com/taskforcesh/bullmq/issues/3697)) fixes [#3681](https://github.com/taskforcesh/bullmq/issues/3681) ([c2c6743](https://github.com/taskforcesh/bullmq/commit/c2c6743428a306e39f74c86f63dc9122633040ea))

### [1.2.1](https://github.com/taskforcesh/bullmq/compare/vex1.2.0...vex1.2.1) (2026-01-14)

#### 버그 수정

* **scripts:** 릴리스 전에 lua scripts 복사 \[elixir] ([#3685](https://github.com/taskforcesh/bullmq/issues/3685)) fixes [#3681](https://github.com/taskforcesh/bullmq/issues/3681) ([5bcd4fb](https://github.com/taskforcesh/bullmq/commit/5bcd4fbe0eb725a95b878f97b95c74106e7dff0f))

## [1.2.0](https://github.com/taskforcesh/bullmq/compare/vex1.1.0...vex1.2.0) (2025-12-31)

#### 기능

* **queue:** `obliterate` 메서드 지원 \[elixir] ([#3657](https://github.com/taskforcesh/bullmq/issues/3657)) ([ede9fcf](https://github.com/taskforcesh/bullmq/commit/ede9fcf72a713f4de8941270251c7b51427484b4))

## [1.1.0](https://github.com/taskforcesh/bullmq/compare/vex1.0.1...vex1.1.0) (2025-12-14)

#### 기능

* **job:** `retry` 메서드 옵션 지원 \[elixir] \[python] ([#3601](https://github.com/taskforcesh/bullmq/issues/3601)) ([6e406a9](https://github.com/taskforcesh/bullmq/commit/6e406a94a5a2fe1f2c1c6e8a1073c6c9b1f11092))

### [1.0.1](https://github.com/taskforcesh/bullmq/compare/vex1.0.0...vex1.0.1) (2025-12-11)

#### 버그 수정

* **scheduler:** 현재 작업 처리 전에 생성된 지연 작업 추가 \[elixir] ([#3598](https://github.com/taskforcesh/bullmq/issues/3598)) ([84e8745](https://github.com/taskforcesh/bullmq/commit/84e8745e87dea9a7748852ccd281b728e6d0545e))

## 1.0.0 (2025-12-04)

#### 기능

* BullMQ for Elixir 초기 릴리스 ([976734f](https://github.com/taskforcesh/bullmq/commit/976734f2c983714b69f395441f5352999aededb0))
* 핵심 큐 기능 (`BullMQ.Queue`)
  * `add/3` 및 `add_bulk/3`로 작업 추가
  * 큐 일시 중지 및 재개
  * ID로 작업 조회
  * 큐 비우기 및 완전 삭제
* 워커 구현 (`BullMQ.Worker`)
  * 설정 가능한 동시성
  * 자동 lock 갱신
  * 정상 종료
  * rate limiting 지원
* 작업 기능 (`BullMQ.Job`)
  * 우선순위 큐
  * 지연 작업
  * backoff를 통한 자동 재시도
  * 진행률 추적
  * 사용자 지정 작업 ID
* Backoff 전략 (`BullMQ.Backoff`)
  * 고정 backoff
  * 지수 backoff
  * 사용자 지정 backoff 함수
  * jitter 지원
* Rate limiting (`BullMQ.RateLimiter`)
  * 큐 수준 rate limit
  * 그룹 기반 rate limit
  * 수동 rate limit 트리거
* 작업 스케줄링 (`BullMQ.JobScheduler`)
  * cron 기반 스케줄링
  * interval 기반 스케줄링
  * 스케줄러 관리 (upsert, remove, list)
* Flow producer (`BullMQ.FlowProducer`)
  * 부모-자식 작업 의존성
  * 중첩 flow
  * 대량 flow 생성
* Stalled 작업 감지 (`BullMQ.StalledChecker`)
  * 자동 복구
  * 설정 가능한 stalled 한도
* 이벤트 스트리밍 (`BullMQ.QueueEvents`)
  * 실시간 작업 수명주기 이벤트
  * 이벤트 필터링
* Telemetry 통합 (`BullMQ.Telemetry`)
  * 작업 수명주기 이벤트
  * 워커 이벤트
  * rate limit 이벤트
  * span 기반 추적
* 설정 검증 (`BullMQ.Config`)
  * NimbleOptions 기반 스키마
  * 큐, 워커, 연결 검증
* Redis key 관리 (`BullMQ.Keys`)
  * 일관된 key 네이밍
  * 설정 가능한 prefix
* Lua script 실행 (`BullMQ.Scripts`)
  * 원자적 연산
  * SHA 캐싱
  * EVAL로 폴백
* Redis 연결 풀링 (`BullMQ.RedisConnection`)
  * NimblePool 기반 풀링
  * 설정 가능한 pool 크기
* 포괄적인 문서
  * 시작 가이드
  * 작업 옵션 레퍼런스
  * 워커 설정
  * rate limiting 가이드
  * flow 패턴
  * telemetry 설정
* 테스트 스위트
  * 모든 모듈의 단위 테스트
  * 통합 테스트 (Redis 필요)

#### 호환성

* Node.js BullMQ v5.x와 호환
* Elixir 1.15+ 필요
* Erlang/OTP 26+ 필요
* Redis 6.0+ 필요

