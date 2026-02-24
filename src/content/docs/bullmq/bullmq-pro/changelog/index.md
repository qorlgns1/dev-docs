---
title: '변경 로그'
---

Source URL: https://docs.bullmq.io/bullmq-pro/changelog

# 변경 로그

### [7.42.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.42.0...v7.42.1) (2026-02-12)

#### 버그 수정

* **job-scheduler-pro:** template option에서 group 옵션을 고려 ([#405](https://github.com/taskforcesh/bullmq-pro/issues/405)) ([4c936ca](https://github.com/taskforcesh/bullmq-pro/commit/4c936ca9fb481e800e7dd56e48c10db058245b50))

## [7.42.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.41.1...v7.42.0) (2026-01-28)

#### 기능

* **deps:** bullmq를 v5.67.2로 업그레이드 ([#403](https://github.com/taskforcesh/bullmq-pro/issues/403)) ([b4e5b1d](https://github.com/taskforcesh/bullmq-pro/commit/b4e5b1d7d960ec61d39a9190d5d30b332eb2e086))

### [7.41.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.41.0...v7.41.1) (2026-01-19)

#### 버그 수정

* **types:** 모든 pro 타입 내보내기 ([#400](https://github.com/taskforcesh/bullmq-pro/issues/400)) ([8055d53](https://github.com/taskforcesh/bullmq-pro/commit/8055d539b51e3f3c3c68a0c74adbb0d6e867a34e))

## [7.41.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.40.3...v7.41.0) (2025-12-28)

#### 버그 수정

* **flow:** flow producer에서 deduplication 옵션 제거 ([#3637](https://github.com/taskforcesh/bullmq/issues/3637)) ([f60c172](https://github.com/taskforcesh/bullmq/commit/f60c172725ab29c0159b804ae0b9d691105689c4))
* **telemetry:** 완료 시 가장 최신 attemptsMade 값 전송 ([#3623](https://github.com/taskforcesh/bullmq/issues/3623)) ([1380a16](https://github.com/taskforcesh/bullmq/commit/1380a16fa45c70f0bc5b938efdf178b33a19cac1))
* **deps:** 종속성 버전 고정 ([#3609](https://github.com/taskforcesh/bullmq/issues/3609)) ([5fbf778](https://github.com/taskforcesh/bullmq/commit/5fbf778f0b8f58b90e82f9020c041f3248b0b269))

#### 기능

* **job:** retry 시 attemptsMade 및 attemptsStarted 속성 재설정 허용 ([#3596](https://github.com/taskforcesh/bullmq/issues/3596)) ref [#2152](https://github.com/taskforcesh/bullmq/issues/2152) ([241d847](https://github.com/taskforcesh/bullmq/commit/241d847fbc798d957bf25ccfaa5c9ec96928a4ae))

### [7.40.3](https://github.com/taskforcesh/bullmq-pro/compare/v7.40.2...v7.40.3) (2025-12-08)

#### 버그 수정

* **job:** job을 failed로 이동할 때 deferredFailure 제거
* **stalled:** job이 더 이상 active 상태가 아닐 때 lock 오류 방지 ([#3579](https://github.com/taskforcesh/bullmq/issues/3579)) ([a8b9d76](https://github.com/taskforcesh/bullmq/commit/a8b9d76496afa5e913f823cf8c68eb428f6dd757))
* **connection:** connection 오류 확인 시 error code 고려 ([#3537](https://github.com/taskforcesh/bullmq/issues/3537)) ([045f3e7](https://github.com/taskforcesh/bullmq/commit/045f3e7a5d8edb85e1adbe82eb9e20ef33ad491b))

#### 기능

* **job:** removeDeduplicationKey 메서드 지원 ([#3575](https://github.com/taskforcesh/bullmq/issues/3575)) ([b059cfc](https://github.com/taskforcesh/bullmq/commit/b059cfcba48524446a62fd29785142c3d1edc30d))
* **worker:** job 취소 추가 ([#3564](https://github.com/taskforcesh/bullmq/issues/3564)) ([f41f5d0](https://github.com/taskforcesh/bullmq/commit/f41f5d0c64afe7707ad8c23a86cb9228c4d45671))

#### 성능 개선

* **worker:** queue가 rate limited 상태일 때 delayed job 승격 ([#3561](https://github.com/taskforcesh/bullmq/issues/3561)) ([a474801](https://github.com/taskforcesh/bullmq/commit/a47480111a2f1238a57ea9bfbab44f7de958227f))

### [7.40.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.40.1...v7.40.2) (2025-11-25)

#### 버그 수정

* **batch:** global concurrency 고려 ([#388](https://github.com/taskforcesh/bullmq-pro/issues/388)) ([7befad4](https://github.com/taskforcesh/bullmq-pro/commit/7befad4a67cc122404694395d0fc28e69fd7f99e))

### [7.40.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.40.0...v7.40.1) (2025-11-15)

#### 버그 수정

* **job-scheduler:** upsert에서 every를 변경하면 iterations가 재설정됨 ([#3551](https://github.com/taskforcesh/bullmq/issues/3551)) ([b4c7c65](https://github.com/taskforcesh/bullmq/commit/b4c7c6579b430b53d135b7a21d20d01d14c1814e))

## [7.40.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.39.3...v7.40.0) (2025-11-04)

#### 버그 수정

* **queue:** updateJobProgress 호출 시 progress 이벤트 발생 ([#3528](https://github.com/taskforcesh/bullmq/issues/3528)) ([c82df83](https://github.com/taskforcesh/bullmq/commit/c82df834dc83b3cf889b6a1aba9d18ec8b5eaf70))
* upsertJobScheduler가 기존 scheduled job의 변경 사항을 적용하지 않음 ([#3524](https://github.com/taskforcesh/bullmq/issues/3524)) ([98f73b3](https://github.com/taskforcesh/bullmq/commit/98f73b3f33aa79cdd67d0c4090cc86a8e4cfeb4c)), closes [#3500](https://github.com/taskforcesh/bullmq/issues/3500)
* **worker:** moveToActive 실패 시에만 error 발생 ([0aa7cc5](https://github.com/taskforcesh/bullmq/commit/0aa7cc57db27a4e7b9fe3c5f52600abba749b053))
* **queue:** remove 메서드 호출 시 removed 이벤트 발생 ([#3492](https://github.com/taskforcesh/bullmq/issues/3492)) fixes [#2668](https://github.com/taskforcesh/bullmq/issues/2668) ([7a3f2fa1](https://github.com/taskforcesh/bullmq/commit/7a3f2fa131e20de80c45877a1018e1ccdf8a6506))
* **worker:** moveToFinished에서 실패 발생 시 error를 한 번만 발생 ([#3498](https://github.com/taskforcesh/bullmq/issues/3498)) ([4b4bd97e](https://github.com/taskforcesh/bullmq/commit/4b4bd97ee78af861121e2ccb90f210e4a74fbd26))
* **worker:** connection 오류 발생 시 processor를 재시도하지 않음 ([#3482](https://github.com/taskforcesh/bullmq/issues/3482)) ([f1573b3](https://github.com/taskforcesh/bullmq/commit/f1573b3023807aab9a68ea6b2ce16a58afe4402b))
* **job-scheduler:** 불안정한 upsert 수정 ([#3446](https://github.com/taskforcesh/bullmq/issues/3446)) ([2241101](https://github.com/taskforcesh/bullmq/commit/22411010beca628d172790cfbac45e3cd3d102ed))

#### 기능

* **queue:** getMeta 메서드 지원 ([#3513](https://github.com/taskforcesh/bullmq/issues/3513)) ([e212d1c](https://github.com/taskforcesh/bullmq/commit/e212d1c8f0945dbff2d95309afe1376366910482))
* **queue:** getGlobalRateLimit 메서드 지원 ([#3511](https://github.com/taskforcesh/bullmq/issues/3511)) ([6a31e0a](https://github.com/taskforcesh/bullmq/commit/6a31e0aeab1311d7d089811ede7e11a98b6dd408))
* **queue:** removeGlobalRateLimit 메서드 추가 ([#3481](https://github.com/taskforcesh/bullmq/issues/3481)) ([d3fff80](https://github.com/taskforcesh/bullmq/commit/d3fff80f7135251db65e22cba8852a5584030cb1))
* **queue:** global rate limit 지원 ([#3468](https://github.com/taskforcesh/bullmq/issues/3468)) ref [#3019](https://github.com/taskforcesh/bullmq/issues/3019) ([bef57a0](https://github.com/taskforcesh/bullmq/commit/bef57a0e252a5d8bd0bf319d0bca3b1ad0e6519f))
* **deduplication:** single mode에서 replace 옵션 지원 ([#3472](https://github.com/taskforcesh/bullmq/issues/3472)) ([eea35b7](https://github.com/taskforcesh/bullmq/commit/eea35b763c0965e129cf0ef4a104d05aa1f65f74))
* **sandbox:** mjs 파일 지원 ([#3476](https://github.com/taskforcesh/bullmq/issues/3476)) ref [#3474](https://github.com/taskforcesh/bullmq/issues/3474) ([2e2b214](https://github.com/taskforcesh/bullmq/commit/2e2b21454cc6125fcf3abfec939d6d6d8d02c40b))
* **worker:** maxStartedAttempts 옵션 지원 ([#3331](https://github.com/taskforcesh/bullmq/issues/3331)) ([9384a64](https://github.com/taskforcesh/bullmq/commit/9384a64d6d48718220e472c26d0c03e7b7e8e555))

#### 성능 개선

* **worker:** 특수 오류 이후 moveToActive 호출 ([#3497](https://github.com/taskforcesh/bullmq/issues/3497)) ([37e9db5](https://github.com/taskforcesh/bullmq/commit/37e9db52a67b4e120139c1d2620cc0f73a08c006))
* **worker:** connection 오류에서만 무한 재시도를 고려 ([#3473](https://github.com/taskforcesh/bullmq/issues/3473)) ([9d5a678](https://github.com/taskforcesh/bullmq/commit/9d5a678660f6bb927ad375d7de58814d392dbe9d))
* **metrics:** getMetrics 호출 시 lua script 사용 ([#3459](https://github.com/taskforcesh/bullmq/issues/3459)) ([61987c6](https://github.com/taskforcesh/bullmq/commit/61987c62ca71ec11a84b98e6dd51a6d5ebf1737d))

### [7.39.3](https://github.com/taskforcesh/bullmq-pro/compare/v7.39.2...v7.39.3) (2025-10-08)

#### 버그 수정

* **classes:** WaitingError 노출 ([#379](https://github.com/taskforcesh/bullmq-pro/issues/379)) ([1cd999e](https://github.com/taskforcesh/bullmq-pro/commit/1cd999e7b52a531d14f5a94f90ef3b3cee167517))

### [7.39.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.39.1...v7.39.2) (2025-10-04)

#### 버그 수정

* **job:** `:` 포함을 방지하기 위해 custom jobId 검증 추가 ([#3384](https://github.com/taskforcesh/bullmq/issues/3384)) fixes [#3382](https://github.com/taskforcesh/bullmq/issues/3382) ([845a6f5](https://github.com/taskforcesh/bullmq/commit/845a6f5fdede9ecf4050e8b5617feb56dbb3c9a1))
* **deps:** uuid를 v11로 업그레이드 ([#3452](https://github.com/taskforcesh/bullmq/issues/3452)) ([bd8fbc1](https://github.com/taskforcesh/bullmq/commit/bd8fbc164caaa01f665d0c7e94177d0584d04f8c))
* **events:** retryJob script 호출 시 prev 파라미터를 active로 설정 ([#3426](https://github.com/taskforcesh/bullmq/issues/3426)) ([e0ebd15](https://github.com/taskforcesh/bullmq/commit/e0ebd15e47b95f9300d6683475ec5d2176f07c95))
* **deduplication:** id 옵션 제공 여부 검증 ([#3443](https://github.com/taskforcesh/bullmq/issues/3443)) fixes [#3432](https://github.com/taskforcesh/bullmq/issues/3432) ([533b844](https://github.com/taskforcesh/bullmq/commit/533b84461a908a3d0182002f16e9c0c0a0260014))

### [7.39.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.39.0...v7.39.1) (2025-09-20)

#### 버그 수정

* **scripts:** 변환된 script 누락 감지 ([#371](https://github.com/taskforcesh/bullmq-pro/issues/371)) ([006b394](https://github.com/taskforcesh/bullmq-pro/commit/006b3948928eab365c17bd6adac57c2f17fd1f75))

## [7.39.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.38.5...v7.39.0) (2025-09-18)

#### 버그 수정

* **queue:** JobBase에 명시적 타입이 없을 때 Job 타입 추론 유지 ([#3423](https://github.com/taskforcesh/bullmq/issues/3423)) fixes [#3421](https://github.com/taskforcesh/bullmq/issues/3421) ([f642818](https://github.com/taskforcesh/bullmq/commit/f6428188f39f054e8b94579435b16e260aff27cd))
* **types:** Processor 타입 내보내기 ([#3418](https://github.com/taskforcesh/bullmq/issues/3418)) ([70e8a3f](https://github.com/taskforcesh/bullmq/commit/70e8a3f91595dcdc2d21122170ef4af1f53972ad))
* **job-scheduler:** getJobScheduler 반환 타입에서 undefined 타입 고려 ([#3412](https://github.com/taskforcesh/bullmq/issues/3412)) ([ffc6e26](https://github.com/taskforcesh/bullmq/commit/ffc6e26eb66533fc6eae4c406bb4b9a9f7590d9b))
* **job:** retry 시 parent 업데이트 고려 ([#3402](https://github.com/taskforcesh/bullmq/issues/3402)) (python) fixes [#3320](https://github.com/taskforcesh/bullmq/issues/3320) ([316d1ed](https://github.com/taskforcesh/bullmq/commit/316d1ed32680e690b1d2ab92c79a53e0d4c00c2d))
* **job:** getTraces에서 불필요한 tryCatch 호출 방지 ([#3400](https://github.com/taskforcesh/bullmq/issues/3400)) ([d71b872](https://github.com/taskforcesh/bullmq/commit/d71b87245c8196d19dfeaf82e6ef14c91fb9a7c5))

#### 기능

* **worker:** processJob 호출 시 span 속성에 jobName과 attemptsMade 추가 ([#3199](https://github.com/taskforcesh/bullmq/issues/3199)) ([db0a922](https://github.com/taskforcesh/bullmq/commit/db0a922741d8c7eae8d5119a0831cd734aba02a2))
* **sandbox:** moveToWaitingChildren 메서드 지원 ([#3389](https://github.com/taskforcesh/bullmq/issues/3389)) ([0fecc6c](https://github.com/taskforcesh/bullmq/commit/0fecc6cd0d0dea06f486ab0b0fe760d866f1fc34))

### [7.38.5](https://github.com/taskforcesh/bullmq-pro/compare/v7.38.4...v7.38.5) (2025-09-05)

#### 버그 수정

* **includes:** 누락된 base includes를 pro로 대체 ([#368](https://github.com/taskforcesh/bullmq-pro/issues/368)) ([e51bb10](https://github.com/taskforcesh/bullmq-pro/commit/e51bb100d02cf420480f97420b9d49fe3086d358))

### [7.38.4](https://github.com/taskforcesh/bullmq-pro/compare/v7.38.3...v7.38.4) (2025-08-14)

#### 버그 수정

* **scheduler:** pattern 사용 시 nextMillis를 생성할 때 startDate를 고려하도록 수정 ([#3385](https://github.com/taskforcesh/bullmq/issues/3385)) [#3378](https://github.com/taskforcesh/bullmq/issues/3378) 수정 ([53754fb](https://github.com/taskforcesh/bullmq/commit/53754fb239cf1b021ffc55391990d879d363dcf7))

### [7.38.3](https://github.com/taskforcesh/bullmq-pro/compare/v7.38.2...v7.38.3) (2025-08-06)

#### 버그 수정

* **worker:** moveToWaitingChildren에서 자식이 실패한 경우 failed 이벤트를 emit하도록 수정 ([#3346](https://github.com/taskforcesh/bullmq/issues/3346)) ([93df852](https://github.com/taskforcesh/bullmq/commit/93df852f97f04023d791546d30a6af24fbca6114))
* **queue:** clean 메서드에서 'waiting' 파라미터 지원 추가 ([#3338](https://github.com/taskforcesh/bullmq/issues/3338)) [#3125](https://github.com/taskforcesh/bullmq/issues/3125) 수정 ([edb7147](https://github.com/taskforcesh/bullmq/commit/edb714764066b06c068c8c8a5140b010f27c3b9a))
* **flow:** 성공하지 못한 자식이 있을 때 parent를 active에서 제거하도록 수정 ([#3348](https://github.com/taskforcesh/bullmq/issues/3348)) ([34ee339](https://github.com/taskforcesh/bullmq/commit/34ee33955a660b0696f4b6cff6d8d39fdcd160db))
* **worker:** pause 또는 close 시 active 작업을 유지하지 않도록 수정 ([#3350](https://github.com/taskforcesh/bullmq/issues/3350)) [#3349](https://github.com/taskforcesh/bullmq/issues/3349) 수정 ([424d155](https://github.com/taskforcesh/bullmq/commit/424d15508172a028479059920ed6bfcf1c54a389))
* **repeat:** 구형 포맷이 있을 때 legacy updateRepeatableJob 스크립트를 사용하도록 수정 ([#3364](https://github.com/taskforcesh/bullmq/issues/3364)) [#3275](https://github.com/taskforcesh/bullmq/issues/3275) 수정 ([1e221d5](https://github.com/taskforcesh/bullmq/commit/1e221d5404dcea750a08342c832a682e454135a3))
* **rate-limit:** 작업이 존재하지 않을 때 올바른 에러 메시지를 던지도록 수정 ([#3354](https://github.com/taskforcesh/bullmq/issues/3354)) ([83d9695](https://github.com/taskforcesh/bullmq/commit/83d969541f19fa9703eb73ff0006cd29a358c1e7))

### [7.38.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.38.1...v7.38.2) (2025-07-18)

#### 버그 수정

* **scheduler:** startMillis 계산에 offset을 반영하도록 수정 ([#2944](https://github.com/taskforcesh/bullmq/issues/2944)) [#247](https://github.com/taskforcesh/bullmq/issues/247) 수정 ([1e3f3c5](https://github.com/taskforcesh/bullmq/commit/1e3f3c507a7ceb8d8147941adc9de69367947a5e))
* **connection:** skipVersionCheck가 true로 제공된 경우 info 명령을 무시하도록 수정 ([#3342](https://github.com/taskforcesh/bullmq/issues/3342)) [#3341](https://github.com/taskforcesh/bullmq/issues/3341) 수정 ([b94d7ed](https://github.com/taskforcesh/bullmq/commit/b94d7ed5602e366b4401051b236f31ac2dd2a90d))

### [7.38.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.38.0...v7.38.1) (2025-07-15)

#### 버그 수정

* **groups:** delayed marker보다 낮을 때 rate limit delay를 blockTimeout으로 사용하도록 수정 ([#353](https://github.com/taskforcesh/bullmq-pro/issues/353)) ([9936325](https://github.com/taskforcesh/bullmq-pro/commit/993632504d1469398947ba3779ef76589276917b))

#### 성능 개선

* **worker:** 작업을 가져올 때 rate limit을 기다리지 않도록 개선 ([#3322](https://github.com/taskforcesh/bullmq/issues/3322)) ([c32e6a0](https://github.com/taskforcesh/bullmq/commit/c32e6a0ff6df8bc34c9c13238c192974a93f7ddb))
* **woker:** delayed marker를 소비할 때 더 낮은 blockTimeout을 유지하도록 개선 ([#3333](https://github.com/taskforcesh/bullmq/issues/3333)) ([e687d7c](https://github.com/taskforcesh/bullmq/commit/e687d7cf86108138bbd5e911b11ab3c5717fc23c))

## [7.38.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.37.0...v7.38.0) (2025-07-11)

#### 기능

* **deduplication:** replace 및 extend 옵션 지원 추가 ([#3260](https://github.com/taskforcesh/bullmq/issues/3260)) 참조 [#2767](https://github.com/taskforcesh/bullmq/issues/2767) [#3151](https://github.com/taskforcesh/bullmq/issues/3151) [#3250](https://github.com/taskforcesh/bullmq/issues/3250) ([4a53609](https://github.com/taskforcesh/bullmq/commit/4a5360936c1a543a1ff31ebbb6ab1289cc8ddf07))

## [7.37.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.36.0...v7.37.0) (2025-07-10)

#### 버그 수정

* scripts와 queue 간 순환 참조 방지 ([#3301](https://github.com/taskforcesh/bullmq/issues/3301)) ([fb65677](https://github.com/taskforcesh/bullmq/commit/fb65677f2d636e1aca3cc75cb3b740b8729b3358))
* **scheduler:** every 사용 시 slot 계산 수정 ([#3307](https://github.com/taskforcesh/bullmq/issues/3307)) ([588719e](https://github.com/taskforcesh/bullmq/commit/588719ee49c7615affeb69d3a431025757115c10))

#### 기능

* **worker:** 작업이 처리 중일 때 moveToWait 호출 허용 ([#3302](https://github.com/taskforcesh/bullmq/issues/3302)) 참조 [#3296](https://github.com/taskforcesh/bullmq/issues/3296) ([e742511](https://github.com/taskforcesh/bullmq/commit/e742511baf35225718c01e621623eab661f37284))

#### 성능 개선

* **scheduler:** every가 제공될 때 offset 값 저장 ([#3142](https://github.com/taskforcesh/bullmq/issues/3142)) ([98f35bc](https://github.com/taskforcesh/bullmq/commit/98f35bc1eabb3ab1010737869c310d2001a84fac))

## [7.36.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.35.2...v7.36.0) (2025-07-09)

#### 버그 수정

* **deps:** v1.1.12로 brace-expansion 취약점 대응 ([240b0b5](https://github.com/taskforcesh/bullmq-pro/commit/240b0b554b5cde889ea25930e9f4ff186c035ff2))
* **job-scheduler:** groups 지원 ([#345](https://github.com/taskforcesh/bullmq-pro/issues/345)) ([467544e](https://github.com/taskforcesh/bullmq-pro/commit/467544e4dc7f9cbd5bbd6512b151c1f7d8ea0fac))
* **flow:** parent에 실패한 자식이 있을 때 새로운 에러 코드 추가 ([#3268](https://github.com/taskforcesh/bullmq/issues/3268)) ([b8fba5e](https://github.com/taskforcesh/bullmq/commit/b8fba5e937a41d0c7ddc97443e9fa8d0f0de566b))
* **job:** getDependencies에서 무시된 실패를 파싱하지 않도록 수정 ([#3284](https://github.com/taskforcesh/bullmq/issues/3284)) [#3283](https://github.com/taskforcesh/bullmq/issues/3283) 수정 ([04ca6b5](https://github.com/taskforcesh/bullmq/commit/04ca6b55c15698aab3ceaf72bd2ed9c589d76197))
* **scheduler:** 현재 작업이 delayed 상태일 때 제거하도록 수정 ([#3269](https://github.com/taskforcesh/bullmq/issues/3269)) [#3262](https://github.com/taskforcesh/bullmq/issues/3262) [#3272](https://github.com/taskforcesh/bullmq/issues/3272) 수정 ([1ca4cbd](https://github.com/taskforcesh/bullmq/commit/1ca4cbd17a58c7eba83030bd6440d0f5e5d69633))
* **worker:** rate limit 상황에서 dangling jobs로 인해 큐가 멈추지 않도록 수정 ([#3297](https://github.com/taskforcesh/bullmq/issues/3297)) [#3289](https://github.com/taskforcesh/bullmq/issues/3289) 수정 ([263d33d](https://github.com/taskforcesh/bullmq/commit/263d33d536a92daf578c56cbb58765917046e052))

#### 기능

* **sandbox:** job의 wrapper에 getIgnoredChildrenFailures 메서드 추가 ([#3263](https://github.com/taskforcesh/bullmq/issues/3263)) ([5d2723d](https://github.com/taskforcesh/bullmq/commit/5d2723dd82e636846e2ff886abb4c0161c15a441))
* **backoff:** jitter 옵션 추가 ([#3291](https://github.com/taskforcesh/bullmq/issues/3291)) ([86c4c6d](https://github.com/taskforcesh/bullmq/commit/86c4c6dd25ef868f1f37c917ab11cb663e330e2f))

#### 성능 개선

* **stalled:** stalled 작업을 지연 평가 방식으로 실패 처리 ([#3266](https://github.com/taskforcesh/bullmq/issues/3266)) ([5cbf064](https://github.com/taskforcesh/bullmq/commit/5cbf0647e106d45d78318a5e5e9fb017261374c9))

### [7.35.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.35.1...v7.35.2) (2025-05-23)

#### 버그 수정

* **groups:** 올바른 local concurrency 속성 이름을 사용하도록 수정 ([#343](https://github.com/taskforcesh/bullmq-pro/issues/343)) ([712d263](https://github.com/taskforcesh/bullmq-pro/commit/712d263bb1538ac39052871029e97597ad20e26d))

### [7.35.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.35.0...v7.35.1) (2025-05-16)

#### 버그 수정

* **remove:** 올바른 children meta 참조를 전달하도록 수정 ([#3245](https://github.com/taskforcesh/bullmq/issues/3245)) ([01c62ad](https://github.com/taskforcesh/bullmq/commit/01c62ada0cea80c73ba28d79fd14ea5ba78fdc7d))
* **worker:** maxStalledCount가 0 미만이 되지 않도록 수정 ([#3249](https://github.com/taskforcesh/bullmq/issues/3249)) [#3248](https://github.com/taskforcesh/bullmq/issues/3248) 수정 ([34dcb8c](https://github.com/taskforcesh/bullmq/commit/34dcb8c3d01a822b07852bc928d882bd6e4049d2))

## [7.35.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.34.0...v7.35.0) (2025-05-02)

#### 버그 수정

* **deduplication:** 저장된 마지막 항목과 jobId가 일치할 때만 deduplication key를 제거하도록 수정 ([#3236](https://github.com/taskforcesh/bullmq/issues/3236)) ([192e82c](https://github.com/taskforcesh/bullmq/commit/192e82caa0f7f530ed495740ec2ade37fe89b43b))
* **job-scheduler:** scheduler가 존재하지 않아도 다음 delayed 작업이 있으면 제거하도록 수정 ([#3203](https://github.com/taskforcesh/bullmq/issues/3203)) 참조 [#3197](https://github.com/taskforcesh/bullmq/issues/3197) ([61395bf](https://github.com/taskforcesh/bullmq/commit/61395bf0b2fc656d1cdaf094fc62a03920ebe07d))
* **queue-events:** telemetry 옵션 생략 ([#3239](https://github.com/taskforcesh/bullmq/issues/3239)) ([e4dac2c](https://github.com/taskforcesh/bullmq/commit/e4dac2c39fac0c8cce34fbcb98a0c72c1619ed4e))

#### 기능

* **queue:** getIgnoredChildrenFailures 메서드 추가 ([#3194](https://github.com/taskforcesh/bullmq/issues/3194)) ([4affb11](https://github.com/taskforcesh/bullmq/commit/4affb11be26afad9f867db19a210c361ba64dd4b))
* **flow:** getFlow 및 getDependencies 메서드에서 무시된 자식 지원 ([#3238](https://github.com/taskforcesh/bullmq/issues/3238)) 참조 [#3213](https://github.com/taskforcesh/bullmq/issues/3213) ([2927803](https://github.com/taskforcesh/bullmq/commit/2927803b4b1eaddb77d3690634beb9c071b5adf7))
* **flow:** getFlow 및 getDependencies 메서드에서 실패한 자식 지원 ([#3243](https://github.com/taskforcesh/bullmq/issues/3243)) ([d3b1cff](https://github.com/taskforcesh/bullmq/commit/d3b1cff4cf02aad8ae0812b1d465316a067118d0))

## [7.34.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.33.0...v7.34.0) (2025-04-30)

#### 버그 수정

* **flow-producer:** addNode에 전달할 때 queueName otel 속성 수정 ([#3198](https://github.com/taskforcesh/bullmq/issues/3198)) ([758ea26](https://github.com/taskforcesh/bullmq/commit/758ea2647b3dad683796351919b0380172fa717f))
* **flow:** failParentOnFailure 또는 continueParentOnFailure일 때 dependencies에서 작업을 제거하도록 수정 ([#3201](https://github.com/taskforcesh/bullmq/issues/3201)) ([1fbcbec](https://github.com/taskforcesh/bullmq/commit/1fbcbec56969fc4aa628f77e4b05d2c6844894ae))
* **job-scheduler:** endDate 존재 여부 검증 수정 ([#3195](https://github.com/taskforcesh/bullmq/issues/3195)) ([339f13e](https://github.com/taskforcesh/bullmq/commit/339f13e277c7c087adc9023f5a433d9a21c661a2))
* line split이 더 호환되도록 개선 ([#3208](https://github.com/taskforcesh/bullmq/issues/3208)) ([3c2349a](https://github.com/taskforcesh/bullmq/commit/3c2349a2936d0c59cfa8d136585a0c0156de3212)), [#3204](https://github.com/taskforcesh/bullmq/issues/3204) 닫음
* **flow-producer:** getFlow 호출 시 기본적으로 FlowProducer prefix를 사용하도록 수정 ([#3224](https://github.com/taskforcesh/bullmq/issues/3224)) ([bd17aad](https://github.com/taskforcesh/bullmq/commit/bd17aad64ec73917548e1bb45ee611b799363cc0))

#### 기능

* **flows:** continueParentOnFailure 옵션 추가 ([#3181](https://github.com/taskforcesh/bullmq/issues/3181)) ([738d375](https://github.com/taskforcesh/bullmq/commit/738d3752934746a347fd04e59e9dcd4726777508))
* removeUnprocessedChildren 추가 ([#3190](https://github.com/taskforcesh/bullmq/issues/3190)) ([4b96266](https://github.com/taskforcesh/bullmq/commit/4b96266d4a7e2fe4b1b3eba12e9e7cc5a64fc044))

* **job:** `stalledCounter` 속성 노출 ([#3218](https://github.com/taskforcesh/bullmq/issues/3218)) ([9456472](https://github.com/taskforcesh/bullmq/commit/94564724593699d13bc0ac238e23c13737edbbf2))

#### 성능 개선

* **flow:** 부모 실패를 지연 평가 방식으로 변경 ([#3228](https://github.com/taskforcesh/bullmq/issues/3228)) ([6b37a37](https://github.com/taskforcesh/bullmq/commit/6b37a379cc65abe7b4c60ba427065957c9080a08))

## [7.33.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.32.2...v7.33.0) (2025-04-17)

#### 버그 수정

* **job:** `fromJSON`에서 `priority` 역직렬화 ([#3126](https://github.com/taskforcesh/bullmq/issues/3126)) ([c3269b1](https://github.com/taskforcesh/bullmq/commit/c3269b11e2def4e2acd4eafc02ce7958a8fcf63e))
* **scheduler:** job scheduler 업데이트 시 `multi` 제거 ([#3108](https://github.com/taskforcesh/bullmq/issues/3108)) ([4b619ca](https://github.com/taskforcesh/bullmq/commit/4b619cab9a6bf8d25efec83dcdf0adaaa362e12a))
* **flow:** `failParentOnFailure`가 제공되면 `waiting-children`에 없는 부모도 failed 처리하도록 고려 ([#3098](https://github.com/taskforcesh/bullmq/issues/3098)) ([589adb4](https://github.com/taskforcesh/bullmq/commit/589adb4f89bcb7d7721200333c2d605eb6ba7864))
* **job-scheduler:** `iterationCount` 속성 복원 ([#3134](https://github.com/taskforcesh/bullmq/issues/3134)) ([eec7114](https://github.com/taskforcesh/bullmq/commit/eec711468de39ec10da9206d7f8c5ad1eb0df882))
* **job-scheduler:** 필요 시 job scheduler upsert 시 marker 추가 ([#3145](https://github.com/taskforcesh/bullmq/issues/3145)) ([0e137b2](https://github.com/taskforcesh/bullmq/commit/0e137b2e78882b6206b3fa47d4a6babb4fcfc484))
* **flow:** 부모를 failed로 이동할 때 prioritized 상태 고려 ([#3160](https://github.com/taskforcesh/bullmq/issues/3160)) ([d91d9f4](https://github.com/taskforcesh/bullmq/commit/d91d9f4398584506f5af8b46e4d47b769beaa212))
* **flow:** completed로 이동할 때만 대기 중 의존성 검증 ([#3164](https://github.com/taskforcesh/bullmq/issues/3164)) ([d3c397f](https://github.com/taskforcesh/bullmq/commit/d3c397fa3f122287026018aaae5ed2c5dfad19aa))
* **scheduler:** 가능하면 다음 delayed job 제거 ([#3153](https://github.com/taskforcesh/bullmq/issues/3153)) ([219c0db](https://github.com/taskforcesh/bullmq/commit/219c0dba7180143b19b4a21dc96db45af941ca7d))
* **job-scheduler:** 다음 delayed job이 존재하면 duplicated 이벤트 발생 ([#3172](https://github.com/taskforcesh/bullmq/issues/3172)) ([d57698f](https://github.com/taskforcesh/bullmq/commit/d57698f9af64fd1bb85f571f22b7fd663c3e05ee))
* **flow:** lock 제거 전에 대기 중 의존성 검증 ([#3182](https://github.com/taskforcesh/bullmq/issues/3182)) ([8d59e3b](https://github.com/taskforcesh/bullmq/commit/8d59e3b8084c60afad16372b4f7fc22f1b9d3f4e))
* **queue-events:** `JobProgress` 타입에 올바른 path 전달 ([#3192](https://github.com/taskforcesh/bullmq/issues/3192)) [#3191](https://github.com/taskforcesh/bullmq/issues/3191) 수정 ([33c62e6](https://github.com/taskforcesh/bullmq/commit/33c62e67268daf24d92653abb5b857ac2241b3aa))
* 수동 재시도가 groups 최대 동시성을 준수하도록 수정 ([#332](https://github.com/taskforcesh/bullmq-pro/issues/332)) ([5fffdc6](https://github.com/taskforcesh/bullmq-pro/commit/5fffdc6d0f77f1726a892101c61df9c33f952b9a))

#### 기능

* **job:** `moveToCompleted` 메서드에 complete span 추가 ([#3132](https://github.com/taskforcesh/bullmq/issues/3132)) ([c37123c](https://github.com/taskforcesh/bullmq/commit/c37123cc84632328d8c4e251641688eb36ac1a8a))
* **job:** `getDependenciesCount`에서 ignored 및 failed 카운트 지원 ([#3137](https://github.com/taskforcesh/bullmq/issues/3137)) 참조 [#3136](https://github.com/taskforcesh/bullmq/issues/3136) ([83953db](https://github.com/taskforcesh/bullmq/commit/83953db54cad80e4ec0a7659f41cb5bc086ccacf))
* **prometheus export:** 전역 변수 노출 ([0325a39](https://github.com/taskforcesh/bullmq/commit/0325a39f4243f3bea682bcfc20dc43b62d3f9fd9))
* deduplicated 이벤트에 deduplicated job id 추가 ([0f21c10](https://github.com/taskforcesh/bullmq/commit/0f21c10bc9fd9a2290e8dde3c9b43bc366fcb15a))
* **updateProgress:** progress로 더 많은 타입을 사용할 수 있도록 허용 ([#3187](https://github.com/taskforcesh/bullmq/issues/3187)) ([f16b748](https://github.com/taskforcesh/bullmq/commit/f16b748d7e3af2535ccdc54e12500af74874a235))

#### 성능 개선

* **worker:** failed job을 청크 단위로 가져오도록 작업 조회 최적화 ([#3127](https://github.com/taskforcesh/bullmq/issues/3127)) ([e0f02ce](https://github.com/taskforcesh/bullmq/commit/e0f02ceb00ced5ca00a6c73d96801a040c40d958))
* **flow:** 부모를 failed로 이동하려고 시도하기 전에 `parentKey` 존재 여부 검증 ([#3163](https://github.com/taskforcesh/bullmq/issues/3163)) ([5a88e47](https://github.com/taskforcesh/bullmq/commit/5a88e4745d9449e41c5e2c467b5d02ca21357703))

### [7.32.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.32.1...v7.32.2) (2025-03-15)

#### 버그 수정

* **job:** batch 제네릭 타입 수정 ([#307](https://github.com/taskforcesh/bullmq-pro/issues/307)) ([857f4a8](https://github.com/taskforcesh/bullmq-pro/commit/857f4a85356e050776d26313de18d8b57b82368d))

### [7.32.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.32.0...v7.32.1) (2025-03-11)

#### 버그 수정

* **worker-pro:** `getNextJob` 메서드의 반환 타이핑 수정 ([#305](https://github.com/taskforcesh/bullmq-pro/issues/305)) ([ee43930](https://github.com/taskforcesh/bullmq-pro/commit/ee439302ed5fe085301ddfc24a76d679e23d3202))

## [7.32.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.31.1...v7.32.0) (2025-03-05)

#### 기능

* **group:** 커스텀 group rate limit 제거 지원 ([#299](https://github.com/taskforcesh/bullmq-pro/issues/299)) ([685eec1](https://github.com/taskforcesh/bullmq-pro/commit/685eec1b2e1b067795dd4201f0cb93895c913399))

### [7.31.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.31.0...v7.31.1) (2025-03-04)

#### 버그 수정

* **scheduler:** failed jobs 정리 시 `repeatKey`가 있으면 검증 ([#3115](https://github.com/taskforcesh/bullmq/issues/3115)) fixes [#3114](https://github.com/taskforcesh/bullmq/issues/3114) ([d4cad84](https://github.com/taskforcesh/bullmq/commit/d4cad8402628f1773299c9cf33e6cc6a0e694037))
* **flow:** 부모를 failed로 이동할 때 delayed 상태 고려 ([#3112](https://github.com/taskforcesh/bullmq/issues/3112)) ([6a28b86](https://github.com/taskforcesh/bullmq/commit/6a28b861346a3efa89574a78b396954d6c4ed113))
* **telemetry:** `moveToFailed` 로직의 span 이름 수정 ([#3113](https://github.com/taskforcesh/bullmq/issues/3113)) ([7a4b500](https://github.com/taskforcesh/bullmq/commit/7a4b500dc63320807e051d8efd2b8fee07bb0db5))

## [7.31.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.30.4...v7.31.0) (2025-03-02)

#### 버그 수정

* **batch:** debug 문 제거 ([6620f82](https://github.com/taskforcesh/bullmq-pro/commit/6620f82680cd03755483a42c8532aba4f4e5ad73))

#### 기능

* **batches:** `minSize` 초기 지원 추가 ([48d1e01](https://github.com/taskforcesh/bullmq-pro/commit/48d1e01cffe7b5763c8d5bd55f3633a8c81a2d79))
* **batches:** `minSize`용 `timeout` 옵션 추가 ([2c40aff](https://github.com/taskforcesh/bullmq-pro/commit/2c40affe2977ebcd423c8453c7b830ea19d6cbfc))

### [7.30.4](https://github.com/taskforcesh/bullmq-pro/compare/v7.30.3...v7.30.4) (2025-03-01)

#### 버그 수정

* **job-scheduler:** `wait`, `paused` 또는 `prioritized`에서 현재 job 제거를 고려 ([#3066](https://github.com/taskforcesh/bullmq/issues/3066)) ([97cd2b1](https://github.com/taskforcesh/bullmq/commit/97cd2b147d541e0984d1c2e107110e1a9d56d9b5))

#### 성능 개선

* **delayed:** delayed jobs 승격 시 marker를 한 번만 추가 ([#3096](https://github.com/taskforcesh/bullmq/issues/3096)) (python) ([38912fb](https://github.com/taskforcesh/bullmq/commit/38912fba969d614eb44d05517ba2ec8bc418a16e))

### [7.30.3](https://github.com/taskforcesh/bullmq-pro/compare/v7.30.2...v7.30.3) (2025-02-21)

#### 버그 수정

* **repeat:** delayed job 생성 시 `JobPro` 클래스 사용 ([#292](https://github.com/taskforcesh/bullmq-pro/issues/292)) ([ce9eff8](https://github.com/taskforcesh/bullmq-pro/commit/ce9eff8a7c000afb5bc23173267f44b2040a0c6a))
* **worker:** 재개 시 processor가 정의되어 있지 않으면 `run` 메서드를 실행하지 않음 ([#3089](https://github.com/taskforcesh/bullmq/issues/3089)) ([4a66933](https://github.com/taskforcesh/bullmq/commit/4a66933496db68a84ec7eb7c153fcedb7bd14c7b))
* **worker:** 종료 중에는 재개하지 않음 ([#3080](https://github.com/taskforcesh/bullmq/issues/3080)) ([024ee0f](https://github.com/taskforcesh/bullmq/commit/024ee0f3f0e808c256712d3ccb1bcadb025eb931))
* **job:** `moveToFinished`에서 job을 active로 이동할 때 `processedBy` 설정 ([#3077](https://github.com/taskforcesh/bullmq/issues/3077)) fixes [#3073](https://github.com/taskforcesh/bullmq/issues/3073) ([1aa970c](https://github.com/taskforcesh/bullmq/commit/1aa970ced3c55949aea6726c4ad29531089f5370))
* **drain:** redis cluster용 delayed key 전달 ([#3074](https://github.com/taskforcesh/bullmq/issues/3074)) ([05ea32b](https://github.com/taskforcesh/bullmq/commit/05ea32b7e4f0cd4099783fd81d2b3214d7a293d5))
* **job-scheduler:** `limit` 옵션이 저장되도록 복원 ([#3071](https://github.com/taskforcesh/bullmq/issues/3071)) ([3e649f7](https://github.com/taskforcesh/bullmq/commit/3e649f7399514b343447ed2073cc07e4661f7390))
* **job-scheduler:** `getJobScheduler`에서 존재하지 않으면 `undefined` 반환 ([#3065](https://github.com/taskforcesh/bullmq/issues/3065)) fixes [#3062](https://github.com/taskforcesh/bullmq/issues/3062) ([548cc1c](https://github.com/taskforcesh/bullmq/commit/548cc1ce8080042b4b44009ea99108bd24193895))
* `getNextJob`의 반환 타입 수정 ([b970281](https://github.com/taskforcesh/bullmq/commit/b9702812e6961f0f5a834f66d43cfb2feabaafd8))

#### 기능

* **job:** 수동 처리를 위한 `moveToWait` 메서드 추가 ([#2978](https://github.com/taskforcesh/bullmq/issues/2978)) ([5a97491](https://github.com/taskforcesh/bullmq/commit/5a97491a0319df320b7858657e03c357284e0108))
* **queue:** `removeGlobalConcurrency` 메서드 지원 ([#3076](https://github.com/taskforcesh/bullmq/issues/3076)) ([ece8532](https://github.com/taskforcesh/bullmq/commit/ece853203adb420466dfaf3ff8bccc73fb917147))

#### 성능 개선

* **add-job:** `delay`가 `0`으로 제공되면 job을 `wait` 또는 `prioritized` 상태에 추가 ([#3052](https://github.com/taskforcesh/bullmq/issues/3052)) ([3e990eb](https://github.com/taskforcesh/bullmq/commit/3e990eb742b3a12065110f33135f282711fdd7b9))

### [7.30.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.30.1...v7.30.2) (2025-02-20)

#### 버그 수정

* **worker:** 종료 시 가져온 job들이 처리될 때까지 대기 ([#3059](https://github.com/taskforcesh/bullmq/issues/3059)) ([d4de2f5](https://github.com/taskforcesh/bullmq/commit/d4de2f5e88d57ea00274e62ab23d09f4806196f8))

### [7.30.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.30.0...v7.30.1) (2025-02-20)

#### 버그 수정

* **job:** 처리 준비 시 `processedBy` 속성 저장 ([#300](https://github.com/taskforcesh/bullmq-pro/issues/300)) ([c947f6e](https://github.com/taskforcesh/bullmq-pro/commit/c947f6eab80ecd7124e77a589e23f50909e0dee8))

## [7.30.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.29.0...v7.30.0) (2025-02-19)

#### 기능

* **groups:** 로컬 limiter 옵션 지원 ([#262](https://github.com/taskforcesh/bullmq-pro/issues/262)) ([fed293c](https://github.com/taskforcesh/bullmq-pro/commit/fed293cceb575caa7be4987cb65c488faf700075))

## [7.29.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.28.0...v7.29.0) (2025-02-18)

#### 기능

* **job-scheduler:** 동일 스크립트에서 delayed job을 추가하고 업데이트하던 변경을 되돌림 ([9f0f1ba](https://github.com/taskforcesh/bullmq/commit/9f0f1ba9b17874a757ac38c1878792c0df3c5a9a))

## [7.28.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.27.0...v7.28.0) (2025-02-15)

#### 버그 수정

* **worker:** failed로 이동할 때 job을 가져와야 하는지 평가 ([#3043](https://github.com/taskforcesh/bullmq/issues/3043)) ([406e21c](https://github.com/taskforcesh/bullmq/commit/406e21c9aadd7670f353c1c6b102a401fc327653))
* **retry-job:** job의 failures 업데이트 고려 ([#3036](https://github.com/taskforcesh/bullmq/issues/3036)) ([21e8495](https://github.com/taskforcesh/bullmq/commit/21e8495b5f2bf5418d86f60b59fad25d306a0298))
* **flow-producer:** skipWaitingForReady 지원 추가 ([6d829fc](https://github.com/taskforcesh/bullmq/commit/6d829fceda9f204f193c533ffc780962692b8f16))

#### 기능

* **job-scheduler:** limit 옵션 저장 ([#3033](https://github.com/taskforcesh/bullmq/issues/3033)) ([a1571ea](https://github.com/taskforcesh/bullmq/commit/a1571ea03be6c6c41794fa272c38c29588351bbf))
* **queue:** 연결 준비 완료까지의 대기를 건너뛰는 옵션 추가 ([e728299](https://github.com/taskforcesh/bullmq/commit/e72829922d4234b92290346dce5d33f5b98ee373))

## [7.27.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.26.6...v7.27.0) (2025-02-12)

#### 버그 수정

* **worker:** worker 종료 시 발생 가능한 위험 회피 ([0f07467](https://github.com/taskforcesh/bullmq/commit/0f0746727176d7ff285ae2d1f35048109b4574c5))

#### 기능

* **queue-getters:** prometheus exporter 추가 ([078ae9d](https://github.com/taskforcesh/bullmq/commit/078ae9db80f6ca64ff0a8135b57a6dc71d71cb1e))
* **job-scheduler:** iteration 횟수 저장 ([#3018](https://github.com/taskforcesh/bullmq/issues/3018)) ([ad5c07c](https://github.com/taskforcesh/bullmq/commit/ad5c07cc7672a3f7a7185310b1250763a5fef76b))
* **sandbox:** getChildrenValues 지원 추가 ([dcc3b06](https://github.com/taskforcesh/bullmq/commit/dcc3b0628f992546d7b93f509795e5d4eb3e1b15))

### [7.26.6](https://github.com/taskforcesh/bullmq-pro/compare/v7.26.5...v7.26.6) (2025-02-03)

#### 버그 수정

* **worker:** lock 확장 시 누락된 otel trace 추가 ([#290](https://github.com/taskforcesh/bullmq-pro/issues/290)) ([efbf948](https://github.com/taskforcesh/bullmq-pro/commit/efbf948585fee4614311db7789d4d351ecc87767))

### [7.26.5](https://github.com/taskforcesh/bullmq-pro/compare/v7.26.4...v7.26.5) (2025-02-02)

#### 버그 수정

* **worker:** lock 확장에서 multi 사용 제거 ([3862075](https://github.com/taskforcesh/bullmq-pro/commit/3862075ab4e41cfa4c1f6b3f87ba50a5087f8c0d))

### [7.26.4](https://github.com/taskforcesh/bullmq-pro/compare/v7.26.3...v7.26.4) (2025-01-30)

#### 버그 수정

* **retry-job:** limiter 대신 stalled key 전달 ([#291](https://github.com/taskforcesh/bullmq-pro/issues/291)) ([e981c69](https://github.com/taskforcesh/bullmq-pro/commit/e981c69067afa68f86be7599b3f835e53406dd9b))

### [7.26.3](https://github.com/taskforcesh/bullmq-pro/compare/v7.26.2...v7.26.3) (2025-01-26)

#### 버그 수정

* **queue:** add 메서드에서 BullMQ와 동일한 telemetry 로직 사용 ([#287](https://github.com/taskforcesh/bullmq-pro/issues/287)) ([214c0d9](https://github.com/taskforcesh/bullmq-pro/commit/214c0d979bd38519df3faa98e0f622ef6f813f68))

### [7.26.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.26.1...v7.26.2) (2025-01-18)

#### 버그 수정

* **job-scheduler:** template data가 없을 때 delayed job data 사용 ([#3010](https://github.com/taskforcesh/bullmq/issues/3010)) [#3009](https://github.com/taskforcesh/bullmq/issues/3009) 수정 ([95edb40](https://github.com/taskforcesh/bullmq/commit/95edb4008fcd32f09ec0953d862692d4ac7608c0))
* **job-scheduler:** prevMillis가 producerId와 일치할 때만 다음 delayed job 추가 ([#3001](https://github.com/taskforcesh/bullmq/issues/3001)) ([4ea35dd](https://github.com/taskforcesh/bullmq/commit/4ea35dd9e16ff0197f204210696f41c0c5bd0e30))
* **job-scheduler:** 빠른 연속 upsert 시 중복 방지 ([#2991](https://github.com/taskforcesh/bullmq/issues/2991)) ([e8cdb99](https://github.com/taskforcesh/bullmq/commit/e8cdb99881bc7cebbc48cb7834da5eafa289712f))
* **dynamic-rate-limit:** job lock 케이스 검증 ([#2975](https://github.com/taskforcesh/bullmq/issues/2975)) ([8bb27ea](https://github.com/taskforcesh/bullmq/commit/8bb27ea4438cbd11e85fa4d0aa516bd1c0e7d51b))

#### 성능 개선

* **job-scheduler:** 동일한 스크립트에서 delayed job 추가 및 scheduler 업데이트 ([#2997](https://github.com/taskforcesh/bullmq/issues/2997)) ([9be28a0](https://github.com/taskforcesh/bullmq/commit/9be28a0c4a907798a447d02ca50662c12333dd82))
* **job-scheduler:** 동일한 스크립트에서 delayed job과 scheduler 추가 ([#2993](https://github.com/taskforcesh/bullmq/issues/2993)) ([95718e8](https://github.com/taskforcesh/bullmq/commit/95718e888ba64b4071f21bbe0823b55a51ab145c))

### [7.26.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.26.0...v7.26.1) (2024-12-22)

#### 버그 수정

* **sandbox:** job이 active 상태에 영구적으로 남을 수 있는 문제 수정 ([#2979](https://github.com/taskforcesh/bullmq/issues/2979)) ([c0a6bcd](https://github.com/taskforcesh/bullmq/commit/c0a6bcdf9594540ef6c8ec08df28550f4f5e1950))
* **sandboxed:** 기본 메시지 전송으로 특수 오류 감지 문제 수정 ([#2967](https://github.com/taskforcesh/bullmq/issues/2967)) [#2962](https://github.com/taskforcesh/bullmq/issues/2962) 수정 ([52b0e34](https://github.com/taskforcesh/bullmq/commit/52b0e34f0a38ac71ebd0667a5fa116ecd73ae4d2))

## [7.26.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.25.0...v7.26.0) (2024-12-17)

#### 버그 수정

* **scripts:** unpack 전에 jobs 필드가 비어 있지 않은지 확인 ([4360572](https://github.com/taskforcesh/bullmq/commit/4360572745a929c7c4f6266ec03d4eba77a9715c))
* 모든 repeatable job이 슬롯에 배치되도록 보장 ([9917df1](https://github.com/taskforcesh/bullmq/commit/9917df166aff2e2f143c45297f41ac8520bfc8ae))
* **job-scheduler:** repeatable job 재시도 시 delayed job 중복 방지 ([af75315](https://github.com/taskforcesh/bullmq/commit/af75315f0c7923f5e0a667a9ed4606b28b89b719))
* **job-scheduler:** template options에서 deduplication 및 debounce 옵션 제외 ([#2960](https://github.com/taskforcesh/bullmq/issues/2960)) ([b5fa6a3](https://github.com/taskforcesh/bullmq/commit/b5fa6a3208a8f2a39777dc30c2db2f498addb907))

#### 기능

* **telemetry:** jobs에서 context propagation을 생략하는 옵션 추가 ([#2946](https://github.com/taskforcesh/bullmq/issues/2946)) ([6514c33](https://github.com/taskforcesh/bullmq/commit/6514c335231cb6e727819cf5e0c56ed3f5132838))
* moveToFailed에서 multi를 lua scripts로 대체 ([#2958](https://github.com/taskforcesh/bullmq/issues/2958)) ([c19c914](https://github.com/taskforcesh/bullmq/commit/c19c914969169c660a3e108126044c5152faf0cd))

## [7.25.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.24.0...v7.25.0) (2024-12-17)

#### 기능

* **queue:** template 정보를 포함하도록 getJobSchedulers 메서드 개선 ([#2956](https://github.com/taskforcesh/bullmq/issues/2956)) ref [#2875](https://github.com/taskforcesh/bullmq/issues/2875) ([5b005cd](https://github.com/taskforcesh/bullmq/commit/5b005cd94ba0f98677bed4a44f8669c81f073f26))

## [7.24.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.23.1...v7.24.0) (2024-12-07)

#### 버그 수정

* **worker:** moveToActive 호출 시 connection error 처리 ([#2952](https://github.com/taskforcesh/bullmq/issues/2952)) ([544fc7c](https://github.com/taskforcesh/bullmq/commit/544fc7c9e4755e6b62b82216e25c0cb62734ed59))
* **scheduler-template:** template 정보 조회 시 console.log 제거 ([#2950](https://github.com/taskforcesh/bullmq/issues/2950)) ([3402bfe](https://github.com/taskforcesh/bullmq/commit/3402bfe0d01e5e5205db74d2106cd19d7df53fcb))
* **flow:** 부모에서 removeOnFail 및 failParentOnFailure 사용 허용 ([#2947](https://github.com/taskforcesh/bullmq/issues/2947)) [#2229](https://github.com/taskforcesh/bullmq/issues/2229) 수정 ([85f6f6f](https://github.com/taskforcesh/bullmq/commit/85f6f6f181003fafbf75304a268170f0d271ccc3))
* **job-scheduler:** 동일한 패턴 옵션이 제공되면 template upsert ([#2943](https://github.com/taskforcesh/bullmq/issues/2943)) ref [#2940](https://github.com/taskforcesh/bullmq/issues/2940) ([b56c3b4](https://github.com/taskforcesh/bullmq/commit/b56c3b45a87e52f5faf25406a2b992d1bfed4900))

#### 기능

* **queue:** template 정보를 포함하도록 getJobScheduler 메서드 개선 ([#2929](https://github.com/taskforcesh/bullmq/issues/2929)) ref [#2875](https://github.com/taskforcesh/bullmq/issues/2875) ([cb99080](https://github.com/taskforcesh/bullmq/commit/cb990808db19dd79b5048ee99308fa7d1eaa2e9f))
* **queue:** getJobSchedulersCount 메서드 추가 ([#2945](https://github.com/taskforcesh/bullmq/issues/2945)) ([38820dc](https://github.com/taskforcesh/bullmq/commit/38820dc8c267c616ada9931198e9e3e9d2f0d536))

### [7.23.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.23.0...v7.23.1) (2024-12-06)

#### 버그 수정

* **stalled:** 필요 시 부모를 group으로 이동 ([#276](https://github.com/taskforcesh/bullmq-pro/issues/276)) ([8449a41](https://github.com/taskforcesh/bullmq-pro/commit/8449a41847aa19bcede07bd9dc71032f58ede420))

## [7.23.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.22.0...v7.23.0) (2024-11-26)

#### 버그 수정

* **scheduler:** immediately 옵션의 deprecation warning 제거 ([#2923](https://github.com/taskforcesh/bullmq/issues/2923)) ([14ca7f4](https://github.com/taskforcesh/bullmq/commit/14ca7f44f31a393a8b6d0ce4ed244e0063198879))

#### 기능

* **telemetry:** telemetry 지원 추가 ([#273](https://github.com/taskforcesh/bullmq-pro/issues/273)) ([e5cc134](https://github.com/taskforcesh/bullmq-pro/commit/e5cc13453b4cee58b04c87568b5cad6a26c31eb7))
* **queue:** telemetry 확장을 허용하도록 protected addJob 메서드 리팩터링 ([09f2571](https://github.com/taskforcesh/bullmq/commit/09f257196f6d5a6690edbf55f12d585cec86ee8f))

## [7.22.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.21.1...v7.22.0) (2024-11-22)

#### 버그 수정

* **queue:** 확장을 위해 \_jobScheduler를 private에서 protected로 변경 ([#2920](https://github.com/taskforcesh/bullmq/issues/2920)) ([34c2348](https://github.com/taskforcesh/bullmq/commit/34c23485bcb32b3c69046b2fb37e5db8927561ce))
* **scheduler:** 확장을 위해 getter에서 Job class 사용 ([#2917](https://github.com/taskforcesh/bullmq/issues/2917)) ([5fbb075](https://github.com/taskforcesh/bullmq/commit/5fbb075dd4abd51cc84a59575261de84e56633d8))
* **telemetry:** undefined인 경우 parent context에 span을 설정하지 않음 ([c417a23](https://github.com/taskforcesh/bullmq/commit/c417a23bb28d9effa42115e954b18cc41c1fc043))

#### 기능

* **job-scheduler:** job scheduler에 telemetry 지원 추가 ([72ea950](https://github.com/taskforcesh/bullmq/commit/72ea950ea251aa12f879ba19c0b5dfeb6a093da2))
* **queue:** rateLimit 메서드 추가 ([#2896](https://github.com/taskforcesh/bullmq/issues/2896)) ([db84ad5](https://github.com/taskforcesh/bullmq/commit/db84ad51a945c754c3cd03e5e718cd8d0341a8b4))
* **queue:** removeRateLimitKey 메서드 추가 ([#2806](https://github.com/taskforcesh/bullmq/issues/2806)) ([ff70613](https://github.com/taskforcesh/bullmq/commit/ff706131bf642fb7544b9d15994d75b1edcb27dc))

#### 성능 개선

* **marker:** worker를 바쁘게 유지하기 위해 job 소비 중 base marker 추가 ([#2904](https://github.com/taskforcesh/bullmq/issues/2904)) [#2842](https://github.com/taskforcesh/bullmq/issues/2842) 수정 ([1759c8b](https://github.com/taskforcesh/bullmq/commit/1759c8bc111cab9e43d5fccb4d8d2dccc9c39fb4))

### [7.21.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.21.0...v7.21.1) (2024-11-15)

#### 버그 수정

* **deps:** bullmq v5.26.1 고정 버전 사용 ([#269](https://github.com/taskforcesh/bullmq-pro/issues/269)) ([33e73e4](https://github.com/taskforcesh/bullmq-pro/commit/33e73e4cb5864d91ca1fe84308f349771e41cdba))

## [7.21.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.20.2...v7.21.0) (2024-11-14)

#### 버그 수정

* **queue:** generics가 올바르게 확장될 수 있도록 수정 ([f2495e5](https://github.com/taskforcesh/bullmq/commit/f2495e5ee9ecdb26492da510dc38730718cb28c5))

#### 기능

* **queue-pro:** getter에서 jobs pro 노출 ([e1da097](https://github.com/taskforcesh/bullmq-pro/commit/e1da0973b9421d24940cbd828a6e33c952fc6cf0))
* generic job type을 사용하도록 queue getter 개선 ([#2905](https://github.com/taskforcesh/bullmq/issues/2905)) ([c9531ec](https://github.com/taskforcesh/bullmq/commit/c9531ec7a49126a017611eb2fd2eaea8fcb5ada5))

### [7.20.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.20.1...v7.20.2) (2024-11-13)

#### 버그 수정

* **job-scheculer:** job scheduler를 동시에 upsert할 때 발생하는 위험 회피 ([022f7b7](https://github.com/taskforcesh/bullmq/commit/022f7b7d0a0ce14387ed2b9fed791e1f56e34770))
* **connection:** blockingConnection option 설정 불가 ([#2851](https://github.com/taskforcesh/bullmq/issues/2851)) ([9391cc2](https://github.com/taskforcesh/bullmq/commit/9391cc22200914ecc8958972ebc580862a70f63c))

### [7.20.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.20.0...v7.20.1) (2024-11-10)

#### 버그 수정

* **repeatable:** 첫 번째 반복에서만 immediately 적용 ([f69cfbc](https://github.com/taskforcesh/bullmq/commit/f69cfbcbc5516a854adbbc29b259d08e65a19705))

## [7.20.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.19.0...v7.20.0) (2024-11-09)

#### 버그 수정

* **scripts:** 확장을 위해 기본적으로 package version 설정 ([#2887](https://github.com/taskforcesh/bullmq/issues/2887)) ([b955340](https://github.com/taskforcesh/bullmq/commit/b955340b940e4c1e330445526cd572e0ab25daa9))
* **worker:** concurrency 값 조회 허용 ([#2883](https://github.com/taskforcesh/bullmq/issues/2883)) 수정 [#2880](https://github.com/taskforcesh/bullmq/issues/2880) ([52f6317](https://github.com/taskforcesh/bullmq/commit/52f6317ecd2080a5c9684a4fe384e20d86f21de4))
* **connection:** 확장을 위해 packageVersion을 protected attribute로 설정 ([#2884](https://github.com/taskforcesh/bullmq/issues/2884)) ([411ccae](https://github.com/taskforcesh/bullmq/commit/411ccae9419e008d916be6cf71c4d57dd2a07b2b))

#### 기능

* **queue-events:** 커스텀 이벤트 발행을 위한 QueueEventsProducer 추가 ([#2844](https://github.com/taskforcesh/bullmq/issues/2844)) ([5eb03cd](https://github.com/taskforcesh/bullmq/commit/5eb03cd7f27027191eb4bc4ed7386755fd9be1fb))
* **flows:** telemetry 지원 추가 ([#2879](https://github.com/taskforcesh/bullmq/issues/2879)) ([5ed154b](https://github.com/taskforcesh/bullmq/commit/5ed154ba240dbe9eb5c22e27ad02e851c0f3cf69))

## [7.19.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.18.0...v7.19.0) (2024-11-08)

#### 버그 수정

* **deps:** ERR\_BUFFER\_OUT\_OF\_BOUNDS 오류 해결을 위해 msgpackr를 1.1.2로 상향 ([#2882](https://github.com/taskforcesh/bullmq/issues/2882)) 참조 [#2747](https://github.com/taskforcesh/bullmq/issues/2747) ([4d2136c](https://github.com/taskforcesh/bullmq/commit/4d2136cc6ba340e511a539c130c9a739fe1055d0))

#### 기능

* **scheduler:** getJobScheduler method 추가 ([#2877](https://github.com/taskforcesh/bullmq/issues/2877)) 참조 [#2875](https://github.com/taskforcesh/bullmq/issues/2875) ([956d98c](https://github.com/taskforcesh/bullmq/commit/956d98c6890484742bb080919c70692234f28c69))
* **queue:** telemetry interface 추가 ([#2721](https://github.com/taskforcesh/bullmq/issues/2721)) ([273b574](https://github.com/taskforcesh/bullmq/commit/273b574e6b5628680990eb02e1930809c9cba5bb))

## [7.18.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.17.2...v7.18.0) (2024-11-07)

#### 버그 수정

* 버전을 가져오는 올바른 방식 ([b4e25c1](https://github.com/taskforcesh/bullmq/commit/b4e25c13cafc001748ee6eb590133feb8ee24d7b))
* **scripts:** isJobInList에 누락된 wait 추가 ([9ef865c](https://github.com/taskforcesh/bullmq/commit/9ef865c7de6086cb3c906721fd046aeed1e0d27f))
* **redis:** 로드된 lua script 이름 지정에 version 사용 ([fe73f6d](https://github.com/taskforcesh/bullmq/commit/fe73f6d4d776dc9f99ad3a094e5c59c5fafc96f1))

#### 기능

* **queue:** metas update를 건너뛸 수 있는 option 추가 ([b7dd925](https://github.com/taskforcesh/bullmq/commit/b7dd925e7f2a4468c98a05f3a3ca1a476482b6c0))
* **queue:** queue version 지원 추가 ([#2822](https://github.com/taskforcesh/bullmq/issues/2822)) ([3a4781b](https://github.com/taskforcesh/bullmq/commit/3a4781bf7cadf04f6a324871654eed8f01cdadae))

### [7.17.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.17.1...v7.17.2) (2024-10-23)

#### 버그 수정

* **sandbox:** 순환 참조가 있을 때 에러 직렬화 수정 ([#2815](https://github.com/taskforcesh/bullmq/issues/2815)) 수정 [#2813](https://github.com/taskforcesh/bullmq/issues/2813) ([a384d92](https://github.com/taskforcesh/bullmq/commit/a384d926bee15bffa84178a8fad7b94a6a08b572))

### [7.17.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.17.0...v7.17.1) (2024-10-18)

#### 버그 수정

* **worker-pro:** WorkerProListener 이벤트의 일부로 JobPro 사용 ([#260](https://github.com/taskforcesh/bullmq-pro/issues/260)) ([966ac9c](https://github.com/taskforcesh/bullmq-pro/commit/966ac9cb41088c13a917450814ed9f6b48b79a9b))

## [7.17.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.16.0...v7.17.0) (2024-10-12)

#### 버그 수정

* **repeat:** "every" 사용 시 startDate도 함께 고려 ([25bbaa8](https://github.com/taskforcesh/bullmq/commit/25bbaa81af87f9944a64bc4fb7e0c76ef223ada4))
* **sandbox:** exit error 처리 ([#2800](https://github.com/taskforcesh/bullmq/issues/2800)) ([6babb9e](https://github.com/taskforcesh/bullmq/commit/6babb9e2f355feaf9bd1a8ed229c1001e6de7144))

#### 기능

* **repeat:** job scheduler에서 immediately 폐기 예정 처리 ([ed047f7](https://github.com/taskforcesh/bullmq/commit/ed047f7ab69ebdb445343b6cb325e90b95ee9dc5))
* **job:** priority 값 노출 ([#2804](https://github.com/taskforcesh/bullmq/issues/2804)) ([9abec3d](https://github.com/taskforcesh/bullmq/commit/9abec3dbc4c69f2496c5ff6b5d724f4d1a5ca62f))
* **job:** deduplication 로직 추가 ([#2796](https://github.com/taskforcesh/bullmq/issues/2796)) ([0a4982d](https://github.com/taskforcesh/bullmq/commit/0a4982d05d27c066248290ab9f59349b802d02d5))
* **queue:** upsertJobScheduler, getJobSchedulers, removeJobSchedulers method 추가 ([dd6b6b2](https://github.com/taskforcesh/bullmq/commit/dd6b6b2263badd8f29db65d1fa6bcdf5a1e9f6e2))
* **worker-fork:** fork option 전달 허용 ([#2795](https://github.com/taskforcesh/bullmq/issues/2795)) ([f7a4292](https://github.com/taskforcesh/bullmq/commit/f7a4292e064b41236f4489b3d7785a4c599a6435))
* **worker-thread:** Worker option 전달 허용 ([#2791](https://github.com/taskforcesh/bullmq/issues/2791)) 참조 [#1555](https://github.com/taskforcesh/bullmq/issues/1555) ([6a1f7a9](https://github.com/taskforcesh/bullmq/commit/6a1f7a9f0303561d6ec7b2005ba0227132b89e07))

## [7.16.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.15.4...v7.16.0) (2024-09-24)

#### 버그 수정

* **repeatable:** 다음 job이 이미 존재하는 경우 delayed job 삭제 방지 ([#2778](https://github.com/taskforcesh/bullmq/issues/2778)) ([6a851c1](https://github.com/taskforcesh/bullmq/commit/6a851c1140b336f0e458b6dfe1022470ac41fceb))
* **connection:** IORedis에 connection string 전달 허용 ([#2746](https://github.com/taskforcesh/bullmq/issues/2746)) ([73005e8](https://github.com/taskforcesh/bullmq/commit/73005e8583110f43914df879aef3481b42f3b3af))
* **metrics:** 정확도를 높이기 위해 서로 다른 분(minute)의 포인트를 구분 ([#2766](https://github.com/taskforcesh/bullmq/issues/2766)) (python) ([7cb670e](https://github.com/taskforcesh/bullmq/commit/7cb670e1bf9560a24de3da52427b4f6b6152a59a))
* **pattern:** immediately가 제공된 경우 offset 저장 안 함 ([#2756](https://github.com/taskforcesh/bullmq/issues/2756)) ([a8cb8a2](https://github.com/taskforcesh/bullmq/commit/a8cb8a21ea52437ac507097994ef0fde058c5433))

#### 기능

* **groups:** 그룹 내 priority 변경 지원 ([#255](https://github.com/taskforcesh/bullmq-pro/issues/255)) ([2b0bf7e](https://github.com/taskforcesh/bullmq-pro/commit/2b0bf7ef56778c4df26e52df3366363b75e59f81))
* **queue:** getDebounceJobId method 추가 ([#2717](https://github.com/taskforcesh/bullmq/issues/2717)) ([a68ead9](https://github.com/taskforcesh/bullmq/commit/a68ead95f32a7d9dabba602895d05c22794b2c02))

#### 성능 개선

* **metrics:** max data points만큼 0 저장 ([#2758](https://github.com/taskforcesh/bullmq/issues/2758)) ([3473054](https://github.com/taskforcesh/bullmq/commit/347305451a9f5d7f2c16733eb139b5de96ea4b9c))

### [7.15.4](https://github.com/taskforcesh/bullmq-pro/compare/v7.15.3...v7.15.4) (2024-09-21)

#### 버그 수정

* **repeat:** repeat key 업데이트 시 delayed job 교체 ([88029bb](https://github.com/taskforcesh/bullmq/commit/88029bbeab2a58768f9c438318f540010cd286a7))

### [7.15.3](https://github.com/taskforcesh/bullmq-pro/compare/v7.15.2...v7.15.3) (2024-09-07)

#### 버그 수정

* **flows:** queueName에 colon이 포함되면 error 발생 ([#2719](https://github.com/taskforcesh/bullmq/issues/2719)) 수정 [#2718](https://github.com/taskforcesh/bullmq/issues/2718) ([9ef97c3](https://github.com/taskforcesh/bullmq/commit/9ef97c37663e209f03c501a357b6b1a662b24d99))
* **sandboxed:** 래핑된 job의 data를 올바르게 업데이트 ([#2739](https://github.com/taskforcesh/bullmq/issues/2739)) 수정 [#2731](https://github.com/taskforcesh/bullmq/issues/2731) ([9c4b245](https://github.com/taskforcesh/bullmq/commit/9c4b2454025a14459de47b0586a09130d7a93cae))

### [7.15.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.15.1...v7.15.2) (2024-09-07)

#### 버그 수정

* **flow:** parent가 fail로 이동할 때 debounce key 제거 ([#2720](https://github.com/taskforcesh/bullmq/issues/2720)) ([d51aabe](https://github.com/taskforcesh/bullmq/commit/d51aabe999a489c285f871d21e36c3c84e2bef33))
* **flow:** ignoreDependencyOnFailure option 재귀 적용 ([#2712](https://github.com/taskforcesh/bullmq/issues/2712)) ([53bc9eb](https://github.com/taskforcesh/bullmq/commit/53bc9eb68b5bb0a470a8fe64ef78ece5cde44632))
* **job:** removeDependencyOnFailure와 ignoreDependencyOnFailure를 함께 사용하면 error 발생 ([#2711](https://github.com/taskforcesh/bullmq/issues/2711)) ([967632c](https://github.com/taskforcesh/bullmq/commit/967632c9ef8468aab59f0b36d1d828bcde1fbd70))
* **job:** jobData를 반영하도록 moveToFinished return type 변경 ([#2706](https://github.com/taskforcesh/bullmq/issues/2706)) 참조 [#2342](https://github.com/taskforcesh/bullmq/issues/2342) ([de094a3](https://github.com/taskforcesh/bullmq/commit/de094a361a25886acbee0112bb4341c6b285b1c9))
* **stalled:** job이 stalled 상태일 때 removeDependencyOnFailure option 지원 ([#2708](https://github.com/taskforcesh/bullmq/issues/2708)) ([e0d3790](https://github.com/taskforcesh/bullmq/commit/e0d3790e755c4dfe31006b52f177f08b40348e61))

#### 성능 개선

* **fifo-queue:** queue에 linked list 구조 사용 ([#2629](https://github.com/taskforcesh/bullmq/issues/2629)) ([df74578](https://github.com/taskforcesh/bullmq/commit/df7457844a769e5644eb11d31d1a05a9d5b4e084))

### [7.15.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.15.0...v7.15.1) (2024-09-06)

#### 버그 수정

* **worker:** open handler 관련 위험을 줄이도록 close sequence 수정 ([#2656](https://github.com/taskforcesh/bullmq/issues/2656)) ([8468e44](https://github.com/taskforcesh/bullmq/commit/8468e44e5e9e39c7b65691945c26688a9e5d2275))
* **flow:** stalled 검사 발생 시 ignoreDependencyOnFailure 전에 parentData 검증 ([#2702](https://github.com/taskforcesh/bullmq/issues/2702)) (python) ([9416501](https://github.com/taskforcesh/bullmq/commit/9416501551b1ad464e59bdba1045a5a9955e2ea4))

## [7.15.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.14.1...v7.15.0) (2024-09-05)

#### 버그 수정

* **job:** stackTraceLimit을 0으로 전달하는 경우도 고려 ([#2692](https://github.com/taskforcesh/bullmq/issues/2692)) 참조 [#2487](https://github.com/taskforcesh/bullmq/issues/2487) ([509a36b](https://github.com/taskforcesh/bullmq/commit/509a36baf8d8cf37176e406fd28e33f712229d27))

#### 기능

* **queue-pro:** getGroupRateLimitTtl 메서드 추가 ([#250](https://github.com/taskforcesh/bullmq-pro/issues/250)) ([5a907d9](https://github.com/taskforcesh/bullmq-pro/commit/5a907d9ca1f4719ad835673fcf0773b5f64c2398))

#### 성능 개선

* **worker:** 큐에 rate limit이 걸린 동안 지연된 작업을 promote ([#2697](https://github.com/taskforcesh/bullmq/issues/2697)) 참조 [#2582](https://github.com/taskforcesh/bullmq/issues/2582) ([f3290ac](https://github.com/taskforcesh/bullmq/commit/f3290ace2f117e26357f9fae611a255af26b950b))

### [7.14.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.14.0...v7.14.1) (2024-08-09)

#### 버그 수정

* **flow:** moveToWaitingChildren 스크립트에서 groupId 가져오기 ([#247](https://github.com/taskforcesh/bullmq-pro/issues/247)) ([1bee26e](https://github.com/taskforcesh/bullmq-pro/commit/1bee26ec6da1bcfa40ce1c7593a9b1183f6215a4))

## [7.14.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.13.0...v7.14.0) (2024-08-08)

#### 기능

* **queue-events:** debounced 이벤트의 파라미터로 debounceId 전달 ([#2678](https://github.com/taskforcesh/bullmq/issues/2678)) ([97fb97a](https://github.com/taskforcesh/bullmq/commit/97fb97a054d6cebbe1d7ff1cb5c46d7da1c018d8))
* **job:** 옵션으로 debounce 전달 허용 ([#2666](https://github.com/taskforcesh/bullmq/issues/2666)) ([163ccea](https://github.com/taskforcesh/bullmq/commit/163ccea19ef48191c4db6da27638ff6fb0080a74))

## [7.13.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.12.0...v7.13.0) (2024-07-31)

#### 버그 수정

* **repeatable:** repeatable 작업 제거 시 repeat hash 제거 ([#2676](https://github.com/taskforcesh/bullmq/issues/2676)) ([97a297d](https://github.com/taskforcesh/bullmq/commit/97a297d90ad8b27bcddb7db6a8a158acfb549389))
* **repeatable:** 새 구조로 생성하는 대신 기존 legacy repeatables가 있으면 유지 ([#2665](https://github.com/taskforcesh/bullmq/issues/2665)) ([93fad41](https://github.com/taskforcesh/bullmq/commit/93fad41a9520961d0e6814d82454bc916a039501))
* **repeatable:** legacy repeatable 작업 제거 고려 ([#2658](https://github.com/taskforcesh/bullmq/issues/2658)) 수정 [#2661](https://github.com/taskforcesh/bullmq/issues/2661) ([a6764ae](https://github.com/taskforcesh/bullmq/commit/a6764aecb557fb918d061f5e5c2e26e4afa3e8ee))
* **repeatable:** CROSSSLOT 이슈 방지를 위해 addRepeatableJob에 인자로 custom key 전달 ([#2662](https://github.com/taskforcesh/bullmq/issues/2662)) 수정 [#2660](https://github.com/taskforcesh/bullmq/issues/2660) ([9d8f874](https://github.com/taskforcesh/bullmq/commit/9d8f874b959e09662985f38c4614b95ab4d5e89c))

#### 기능

* **repeatable:** 새로운 repeatables 구조 ([#2617](https://github.com/taskforcesh/bullmq/issues/2617)) 참조 [#2612](https://github.com/taskforcesh/bullmq/issues/2612) 수정 [#2399](https://github.com/taskforcesh/bullmq/issues/2399) [#2596](https://github.com/taskforcesh/bullmq/issues/2596) ([8376a9a](https://github.com/taskforcesh/bullmq/commit/8376a9a9007f58ac7eab1a3a1c2f9e7ec373bbd6))

#### 성능 개선

* **worker:** 실패 시 다음 작업 가져오기 ([#2342](https://github.com/taskforcesh/bullmq/issues/2342)) ([f917b80](https://github.com/taskforcesh/bullmq/commit/f917b8090f306c0580aac12f6bd4394fd9ef003d))

## [7.12.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.11.0...v7.12.0) (2024-07-26)

#### 기능

* **queue:** 전역 동시성 지원 ([#243](https://github.com/taskforcesh/bullmq-pro/issues/243)) ([4baac78](https://github.com/taskforcesh/bullmq-pro/commit/4baac78a1e00e42b58e62778a5b13df62decd792))

## [7.11.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.10.1...v7.11.0) (2024-07-14)

#### 기능

* **groups:** getCountsPerPriorityForGroup 메서드 추가 ([#241](https://github.com/taskforcesh/bullmq-pro/issues/241)) 참조 [#238](https://github.com/taskforcesh/bullmq-pro/issues/238) ([2d3c81c](https://github.com/taskforcesh/bullmq-pro/commit/2d3c81c11c5c566913de15d50250ca5ade1eb59a))

### [7.10.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.10.0...v7.10.1) (2024-07-09)

#### 버그 수정

* **get-groups-count:** waiting 외 다른 group 상태도 고려 ([#240](https://github.com/taskforcesh/bullmq-pro/issues/240)) ([eccd4e6](https://github.com/taskforcesh/bullmq-pro/commit/eccd4e69ee3bda08136d227c3628be24746a5464))

## [7.10.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.9.2...v7.10.0) (2024-07-06)

#### 버그 수정

* **queue-getters:** getRateLimitTtl 호출 시 maxJobs 전달 고려 ([#2631](https://github.com/taskforcesh/bullmq/issues/2631)) 수정 [#2628](https://github.com/taskforcesh/bullmq/issues/2628) ([9f6609a](https://github.com/taskforcesh/bullmq/commit/9f6609ab1856c473b2d5cf0710068ce2751d708e))
* **job:** priority를 0으로 변경하는 경우 고려 ([#2599](https://github.com/taskforcesh/bullmq/issues/2599)) ([4dba122](https://github.com/taskforcesh/bullmq/commit/4dba122174ab5173315fca7fdbb7454761514a53))
* **priority:** getCountsPerPriority 호출 시 paused 상태 고려 (python) ([#2609](https://github.com/taskforcesh/bullmq/issues/2609)) ([6e99250](https://github.com/taskforcesh/bullmq/commit/6e992504b2a7a2fa76f1d04ad53d1512e98add7f))
* **priority:** 순서 유지를 위해 bit.band 대신 module 사용 (python) ([#2597](https://github.com/taskforcesh/bullmq/issues/2597)) ([9ece15b](https://github.com/taskforcesh/bullmq/commit/9ece15b17420fe0bee948a5307e870915e3bce87))

#### 기능

* **queue:** getCountsPerPriority 메서드 추가 ([#2595](https://github.com/taskforcesh/bullmq/issues/2595)) ([77971f4](https://github.com/taskforcesh/bullmq/commit/77971f42b9fc425ad66e0b581e800ea429fc254e))

#### 성능 개선

* **job:** hmset을 사용해 processedBy 설정 ([#2592](https://github.com/taskforcesh/bullmq/issues/2592)) (python) ([238680b](https://github.com/taskforcesh/bullmq/commit/238680b84593690a73d542dbe1120611c3508b47))

### [7.9.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.9.1...v7.9.2) (2024-06-28)

#### 버그 수정

* **groups:** active count 감소 후 maxed 그룹 promote ([#234](https://github.com/taskforcesh/bullmq-pro/issues/234)) ([545b6c2](https://github.com/taskforcesh/bullmq-pro/commit/545b6c28c9634d1603ff3d237f072736c2f2388b))

### [7.9.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.9.0...v7.9.1) (2024-06-18)

#### 버그 수정

* **maxed:** repairMaxedGroup에 max concurrency 전달 고려 ([#232](https://github.com/taskforcesh/bullmq-pro/issues/232)) ([a3885a5](https://github.com/taskforcesh/bullmq-pro/commit/a3885a5456a9ea12abfedb623def516b84c5c289))

## [7.9.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.8.3...v7.9.0) (2024-06-15)

#### 기능

* **groups:** getGroupsJobsCount 호출 시 limit 전달 허용 ([#230](https://github.com/taskforcesh/bullmq-pro/issues/230)) ([ac0469f](https://github.com/taskforcesh/bullmq-pro/commit/ac0469f2a43e7714a3b614780d3bc9f7f1f20382))

### [7.8.3](https://github.com/taskforcesh/bullmq-pro/compare/v7.8.2...v7.8.3) (2024-06-13)

#### 버그 수정

* **groups:** remove 메서드 사용 시 prioritized group에서 작업 제거 고려 ([#229](https://github.com/taskforcesh/bullmq-pro/issues/229)) ([b61b96f](https://github.com/taskforcesh/bullmq-pro/commit/b61b96f06c4e4c03be09babfb43ded7b3ef00616))

### [7.8.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.8.1...v7.8.2) (2024-05-31)

#### 버그 수정

* **worker:** 연결 끊김 중 blocking command를 올바르게 취소 ([2cf12b3](https://github.com/taskforcesh/bullmq/commit/2cf12b3622b0517f645971ece8acdcf673bede97))
* extendlock,createbulk에서 multi command 없이 pipeline 사용 ([a053d9b](https://github.com/taskforcesh/bullmq/commit/a053d9b87e9799b151e2563b499dbff309b9d2e5))
* **repeat:** endDate가 과거를 가리킬 때 오류 발생 ([#2574](https://github.com/taskforcesh/bullmq/issues/2574)) ([5bd7990](https://github.com/taskforcesh/bullmq/commit/5bd79900ea3ace8ec6aa00525aff81a345f8e18e))
* **retry-job:** 작업이 active 상태가 아닐 때 오류 발생 ([#2576](https://github.com/taskforcesh/bullmq/issues/2576)) ([ca207f5](https://github.com/taskforcesh/bullmq/commit/ca207f593d0ed455ecc59d9e0ef389a9a50d9634))
* **sandboxed:** Sandboxed processors에서 DelayedError 검사 보장 ([#2567](https://github.com/taskforcesh/bullmq/issues/2567)) 수정 [#2566](https://github.com/taskforcesh/bullmq/issues/2566) ([8158fa1](https://github.com/taskforcesh/bullmq/commit/8158fa114f57619b31f101bc8d0688a09c6218bb))
* **job:** 로그 추가 시 작업 존재 여부 검증 ([#2562](https://github.com/taskforcesh/bullmq/issues/2562)) ([f87e3fe](https://github.com/taskforcesh/bullmq/commit/f87e3fe029e48d8964722da762326e531c2256ee))

### [7.8.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.8.0...v7.8.1) (2024-05-18)

#### 버그 수정

* **groups:** 그룹 제거 시 concurrency 제거 ([#226](https://github.com/taskforcesh/bullmq-pro/issues/226)) ([332728e](https://github.com/taskforcesh/bullmq-pro/commit/332728e3a5c93a5f07263a77aedb27356259ddc2))

## [7.8.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.7.2...v7.8.0) (2024-05-10)

#### 기능

* **group:** getGroupConcurrency 메서드 추가 ([#224](https://github.com/taskforcesh/bullmq-pro/issues/224)) ([88e334e](https://github.com/taskforcesh/bullmq-pro/commit/88e334e567688570111f3109bdd0751e859f46dc))

### [7.7.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.7.1...v7.7.2) (2024-05-04)

#### 버그 수정

* **worker:** bzpopmin 이후 clearTimeout이 항상 호출되도록 보장 ([782382e](https://github.com/taskforcesh/bullmq/commit/782382e599218024bb9912ff0572c4aa9b1f22a3))
* **worker:** bzpopmin command에 timeout 강제 적용 ([#2543](https://github.com/taskforcesh/bullmq/issues/2543)) ([ae7cb6c](https://github.com/taskforcesh/bullmq/commit/ae7cb6caefdbfa5ca0d28589cef4b896ffcce2db))

#### 성능 개선

* **worker:** blockDelay가 0 이하일 때 bzpopmin을 호출하지 않음 ([#2544](https://github.com/taskforcesh/bullmq/issues/2544)) 참조 [#2466](https://github.com/taskforcesh/bullmq/issues/2466) ([9760b85](https://github.com/taskforcesh/bullmq/commit/9760b85dfbcc9b3c744f616961ef939e8951321d))

### [7.7.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.7.0...v7.7.1) (2024-04-30)

#### 버그 수정

* **worker-pro:** limiter용 options 인자의 오타 수정 ([0e999dd](https://github.com/taskforcesh/bullmq-pro/commit/0e999dd677f4852c1145213b9d1bc752e3e3b859))

## [7.7.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.6.2...v7.7.0) (2024-04-30)

#### 기능

* **groups:** setGroupConcurrency 메서드를 사용한 로컬 그룹 동시성 지원 ([#220](https://github.com/taskforcesh/bullmq-pro/issues/220)) ([159a341](https://github.com/taskforcesh/bullmq-pro/commit/159a341dd209c4cf8b9494205a2e2fcf8638c343))

### [7.6.2](https://github.com/taskforcesh/bullmq-pro/compare/v7.6.1...v7.6.2) (2024-04-25)

#### 버그 수정

* **stalled:** ignoreDependencyOnFailure 옵션 고려 (python) ([#2540](https://github.com/taskforcesh/bullmq/issues/2540)) 수정 [#2531](https://github.com/taskforcesh/bullmq/issues/2531) ([0140959](https://github.com/taskforcesh/bullmq/commit/0140959cabd2613794631e41ebe4c2ddee6f91da))

### [7.6.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.6.0...v7.6.1) (2024-04-23)

#### 버그 수정

* **worker:** redis 버전에 따라 minimumBlockTimeout 반환 (python) ([#2532](https://github.com/taskforcesh/bullmq/issues/2532)) ([83dfb63](https://github.com/taskforcesh/bullmq/commit/83dfb63e72a1a36a4dfc40f122efb54fbb796339))
* **stalled:** child를 failed로 이동할 때 failParentOnFailure 고려 ([#2526](https://github.com/taskforcesh/bullmq/issues/2526)) 수정 [#2464](https://github.com/taskforcesh/bullmq/issues/2464) (python) ([5e31eb0](https://github.com/taskforcesh/bullmq/commit/5e31eb096169ea57350db591bcebfc2264a6b6dc))

#### 성능 개선

* **worker:** `blockTimeout` 값을 생성한 후 지연을 재설정 ([#2529](https://github.com/taskforcesh/bullmq/issues/2529)) ([e92cea4](https://github.com/taskforcesh/bullmq/commit/e92cea4a9d7c99f649f6626d1c0a1e1e994179d6))

## [7.6.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.5.0...v7.6.0) (2024-04-17)

#### 기능

* **queue:** getGroupActiveCount 메서드 추가 ([#217](https://github.com/taskforcesh/bullmq-pro/issues/217)) ([d59d2e5](https://github.com/taskforcesh/bullmq-pro/commit/d59d2e5f82b7a83495dcdc948d4fbbf162dc72c5))

## [7.5.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.4.1...v7.5.0) (2024-04-10)

#### 버그 수정

* **worker:** 7.0.8 미만 redis 버전에서 최소 timeout으로 0.002 사용 ([#2515](https://github.com/taskforcesh/bullmq/issues/2515)) fixes [#2466](https://github.com/taskforcesh/bullmq/issues/2466) ([44f7d21](https://github.com/taskforcesh/bullmq/commit/44f7d21850747d9c636c78e08b9e577d684fb885))

#### 기능

* 임의로 큰 drainDelay 허용 ([9693321](https://github.com/taskforcesh/bullmq/commit/96933217bf79658e5bb23fd7afe47e0b1150a40d))

#### 성능 개선

* **stalled:** active에서 이동될 때 lock 제거 후 stalled에서 jobId 제거 ([#2512](https://github.com/taskforcesh/bullmq/issues/2512)) (python) ([64feec9](https://github.com/taskforcesh/bullmq/commit/64feec91b0b034fe640a846166bd95b546ff6d71))
* **add-to-group:** 그룹 재삽입 건너뛰기 ([#215](https://github.com/taskforcesh/bullmq-pro/issues/215)) ([6823251](https://github.com/taskforcesh/bullmq-pro/commit/682325108658e9b0d9ca9b45ed5bf0b29250066c))

### [7.4.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.4.0...v7.4.1) (2024-04-07)

#### 버그 수정

* **deps:** dist에서 script loader 제거 ([#213](https://github.com/taskforcesh/bullmq-pro/issues/213)) ([dd28ec8](https://github.com/taskforcesh/bullmq-pro/commit/dd28ec80549c41d89d62100d5d7d857825347f5e))

## [7.4.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.3.1...v7.4.0) (2024-04-04)

#### 버그 수정

* **connection:** 사용자 정의 종료 상태 설정 시 오류 무시 ([#2473](https://github.com/taskforcesh/bullmq/issues/2473)) ([3e17e45](https://github.com/taskforcesh/bullmq/commit/3e17e459a89a6ca9bccda64c5f06f91e70b372e4))
* **job:** stack trace 제한 ([#2487](https://github.com/taskforcesh/bullmq/issues/2487)) ([cce3bc3](https://github.com/taskforcesh/bullmq/commit/cce3bc3092eb7cf56c2a6c68e9fd8980f5f1f26a))
* **scripts:** finished로 이동할 때 오류 메시지에 command 이름 사용 ([#2483](https://github.com/taskforcesh/bullmq/issues/2483)) ([3c335d4](https://github.com/taskforcesh/bullmq/commit/3c335d49ba637145648c1ef0864d8e0d297dd890))
* **queue:** opts 속성에 QueueOptions 타입 사용 ([#2481](https://github.com/taskforcesh/bullmq/issues/2481)) ([51a589f](https://github.com/taskforcesh/bullmq/commit/51a589f7e07b5336eb35ed00a1b795501b24f254))
* **worker:** drainDelay가 0보다 커야 함을 검증 ([#2477](https://github.com/taskforcesh/bullmq/issues/2477)) ([ab43693](https://github.com/taskforcesh/bullmq/commit/ab436938d895125635aef0393ae2fb5c77c16c1f))

#### 기능

* **getters:** getWorkersCount 추가 ([743c7aa](https://github.com/taskforcesh/bullmq/commit/743c7aa8f979760bc04f7b8f55844020559038e1))

### [7.3.1](https://github.com/taskforcesh/bullmq-pro/compare/v7.3.0...v7.3.1) (2024-03-30)

#### 버그 수정

* **group-limit:** 그룹이 비어 있어도 rate limiting 설정 ([#212](https://github.com/taskforcesh/bullmq-pro/issues/212)) ([08824cf](https://github.com/taskforcesh/bullmq-pro/commit/08824cf5fea0887653acc8081abe9d25b6ea96a5))

## [7.3.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.2.0...v7.3.0) (2024-03-16)

#### 버그 수정

* **deps:** fast-glob 및 minimatch를 dev-dependencies로 이동 ([#2452](https://github.com/taskforcesh/bullmq/issues/2452)) ([cf13b31](https://github.com/taskforcesh/bullmq/commit/cf13b31ca552bcad53f40fe5668a907cf02e0a2e))
* **worker:** 지연된 작업을 가져올 시간에 도달하면 blockTimeout을 0.001로 설정 ([#2455](https://github.com/taskforcesh/bullmq/issues/2455)) fixes [#2450](https://github.com/taskforcesh/bullmq/issues/2450) ([2de15ca](https://github.com/taskforcesh/bullmq/commit/2de15ca1019517f7ce11f3734fff316a3e4ab894))

#### 기능

* **job:** removeChildDependency 메서드 추가 ([#2435](https://github.com/taskforcesh/bullmq/issues/2435)) ([1151022](https://github.com/taskforcesh/bullmq/commit/1151022e4825fbb20cf1ef6ce1ff3e7fe929de5c))

## [7.2.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.1.0...v7.2.0) (2024-03-15)

#### 버그 수정

* **deps:** 보안 권고로 인해 glob을 fast-glob으로 대체 ([91cf9a9](https://github.com/taskforcesh/bullmq/commit/91cf9a9253370ea76df48c27a7e0fcf8d7504c81))
* **sandbox:** SandboxedJob을 JobJsonSandbox에서 확장 ([#2446](https://github.com/taskforcesh/bullmq/issues/2446)) fixes [#2439](https://github.com/taskforcesh/bullmq/issues/2439) ([7606e36](https://github.com/taskforcesh/bullmq/commit/7606e3611f1cc18b1585c08b0f7fd9cb90749c9c))
* **add-job:** parent job을 대체할 수 없다는 오류 메시지 수정 ([#2441](https://github.com/taskforcesh/bullmq/issues/2441)) ([1e9a13f](https://github.com/taskforcesh/bullmq/commit/1e9a13fc0dc9de810ef75a042fbfeeae5b571ffe))

#### 기능

* **worker:** worker 이름 지정 지원 추가 ([7ba2729](https://github.com/taskforcesh/bullmq/commit/7ba27293615e443903cfdf7d0ff8be0052d061c4))

## [7.1.0](https://github.com/taskforcesh/bullmq-pro/compare/v7.0.0...v7.1.0) (2024-03-14)

#### 버그 수정

* **flow:** 자동 제거 시 실패한 자식 참조 제거 ([#2432](https://github.com/taskforcesh/bullmq/issues/2432)) ([8a85207](https://github.com/taskforcesh/bullmq/commit/8a85207cf3c552ebab37baca3c395821b9804b37))
* **redis-connection:** 초기화 중에도 redis 연결 종료 ([#2425](https://github.com/taskforcesh/bullmq/issues/2425)) fixes [#2385](https://github.com/taskforcesh/bullmq/issues/2385) ([1bc26a6](https://github.com/taskforcesh/bullmq/commit/1bc26a64871b85a2d1f6799a9b73b60f8bf9fa90))

#### 기능

* **flow:** ignoreDependencyOnFailure 옵션 추가 ([#2426](https://github.com/taskforcesh/bullmq/issues/2426)) ([c7559f4](https://github.com/taskforcesh/bullmq/commit/c7559f4f0a7fa51764ad43b4f46bb9d55ac42d0d))

## [7.0.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.11.0...v7.0.0) (2024-03-12)

#### 버그 수정

* **worker:** processor 타입 업데이트 ([#193](https://github.com/taskforcesh/bullmq-pro/issues/193)) ([8ebb72e](https://github.com/taskforcesh/bullmq-pro/commit/8ebb72e1d87ec819bb1efa12d0a931e8e9ead203))
* **flow:** parent job은 대체할 수 없음 (python) ([#2417](https://github.com/taskforcesh/bullmq/issues/2417)) ([2696ef8](https://github.com/taskforcesh/bullmq/commit/2696ef8200058b7f616938c2166a3b0454663b39))
* **reprocess-job:** 필요 시 marker 추가 ([#2406](https://github.com/taskforcesh/bullmq/issues/2406)) ([5923ed8](https://github.com/taskforcesh/bullmq/commit/5923ed885f5451eee2f14258767d7d5f8d80ae13))
* **rate-limit:** ttl이 0이어도 job을 wait으로 이동 ([#2403](https://github.com/taskforcesh/bullmq/issues/2403)) ([c1c2ccc](https://github.com/taskforcesh/bullmq/commit/c1c2cccc7c8c05591f0303e011d46f6efa0942a0))
* **stalled:** job을 다시 wait으로 이동할 때 marker 추가를 고려 ([#2384](https://github.com/taskforcesh/bullmq/issues/2384)) ([4914df8](https://github.com/taskforcesh/bullmq/commit/4914df87e416711835291e81da93b279bd758254))
* **retry-jobs:** 필요 시 marker 추가 ([#2374](https://github.com/taskforcesh/bullmq/issues/2374)) ([1813d5f](https://github.com/taskforcesh/bullmq/commit/1813d5fa12b7db69ee6c8c09273729cda8e3e3b5))
* **security:** msgpackr 업그레이드 <https://github.com/advisories/GHSA-7hpj-7hhx-2fgx> ([7ae0953](https://github.com/taskforcesh/bullmq/commit/7ae095357fddbdaacc286cbe5782946b95160d55))
* **worker:** Redis가 다운된 경우에도 worker를 종료할 수 있음 ([#2350](https://github.com/taskforcesh/bullmq/issues/2350)) ([888dcc2](https://github.com/taskforcesh/bullmq/commit/888dcc2dd40571e05fe1f4a5c81161ed062f4542))
* **worker:** 연결이 없으면 오류 발생 ([6491a18](https://github.com/taskforcesh/bullmq/commit/6491a185268ae546baa9b95a20b95d63c0e27915))

#### 기능

* **stalled:** stalled key를 복구하는 command 추가 ([#193](https://github.com/taskforcesh/bullmq-pro/issues/193)) ([8ebb72e](https://github.com/taskforcesh/bullmq-pro/commit/8ebb72e1d87ec819bb1efa12d0a931e8e9ead203))
* **repeatable:** 사용자 정의 key 저장 허용 ([#1824](https://github.com/taskforcesh/bullmq/issues/1824)) ([8ea0e1f](https://github.com/taskforcesh/bullmq/commit/8ea0e1f76baf36dab94a66657c0f432492cb9999))
* **job:** job을 수동으로 이동할 때 skipAttempt 옵션 제공 ([#2203](https://github.com/taskforcesh/bullmq/issues/2203)) ([0e88e4f](https://github.com/taskforcesh/bullmq/commit/0e88e4fe4ed940487dfc79d1345d0686de22d0c6))
* **worker:** marker 처리 개선 ([73cf5fc](https://github.com/taskforcesh/bullmq/commit/73cf5fc1e6e13d8329e1e4e700a8db92173e0624)) ([0bac0fb](https://github.com/taskforcesh/bullmq/commit/0bac0fbb97afa968aa7644f1438b86d7bc18bbc5))

#### 성능 개선

* **marker:** 표준 marker와 지연 marker를 구분 (python) ([#2389](https://github.com/taskforcesh/bullmq/issues/2389)) ([18ebee8](https://github.com/taskforcesh/bullmq/commit/18ebee8c242f66f1b5b733d68e48c574b1f1fdef))
* **change-delay:** 필요 시 delay marker 추가 ([#2411](https://github.com/taskforcesh/bullmq/issues/2411)) ([8b62d28](https://github.com/taskforcesh/bullmq/commit/8b62d28a06347e9dd04757807fce1b511ace79bc))
* **flow:** parent를 wait으로 이동할 때 marker 추가 (python) ([#2408](https://github.com/taskforcesh/bullmq/issues/2408)) ([6fb6896](https://github.com/taskforcesh/bullmq/commit/6fb6896701ae7595e1cb5e2cdbef44625c48d673))
* **move-to-active:** rate limited 확인을 한 번만 수행 ([#2391](https://github.com/taskforcesh/bullmq/issues/2391)) ([ca6c17a](https://github.com/taskforcesh/bullmq/commit/ca6c17a43e38d5339e62471ea9f59c62a169b797))

#### 주요 변경 사항

* **connection:** connection 전달 필수 ([#2335](https://github.com/taskforcesh/bullmq/issues/2335)) ([1867dd1](https://github.com/taskforcesh/bullmq/commit/1867dd107d7edbd417bf6918354ae4656480a544))
* **job:** 정수를 나타내는 사용자 정의 job id에 대한 console warn 되돌리기 ([#2312](https://github.com/taskforcesh/bullmq/issues/2312)) ([84015ff](https://github.com/taskforcesh/bullmq/commit/84015ffa04216c45d8f3181a7f859b8c0792c80d))
* **worker:** marker는 이제 특별한 Job ID를 사용하는 대신 redis의 전용 key를 사용합니다.
* **stalled:** stalled key의 type 검사 제거
* 참고:
  * [Better Queue Markers](https://bullmq.io/news/231204/better-queue-markers/)
  * [BullMQ v5 Migration Notes](https://bullmq.io/news/231221/bullmqv5-release/)
  * [BullMQ Pro v7 Release](https://bullmq.io/news/240312/bullmq-prov7-release/)

