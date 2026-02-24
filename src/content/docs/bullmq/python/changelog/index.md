---
title: '변경 로그'
description: '원본 URL: https://docs.bullmq.io/python/changelog'
---

원본 URL: https://docs.bullmq.io/python/changelog

# 변경 로그

### [2.19.5](https://github.com/taskforcesh/bullmq/compare/vpy2.19.4...vpy2.19.5) (2026-02-11)

#### 성능 개선

* **job:** 등록된 스크립트 재사용 \[python] ([#3757](https://github.com/taskforcesh/bullmq/issues/3757)) ([715d0a5](https://github.com/taskforcesh/bullmq/commit/715d0a5074864ed0c12a384e41740b219382ac80))

### [2.19.4](https://github.com/taskforcesh/bullmq/compare/vpy2.19.3...vpy2.19.4) (2026-01-28)

#### 버그 수정

* priority 대신 prioritized 키 이름 사용 \[python] ([#3717](https://github.com/taskforcesh/bullmq/issues/3717)) fixes [#3716](https://github.com/taskforcesh/bullmq/issues/3716) ([f824c01](https://github.com/taskforcesh/bullmq/commit/f824c01c53d57e75d7b57efce7a124adffed9dfa))

### [2.19.3](https://github.com/taskforcesh/bullmq/compare/vpy2.19.2...vpy2.19.3) (2026-01-24)

#### 버그 수정

* 클러스터에서 worker connection name 수정 [#3340](https://github.com/taskforcesh/bullmq/issues/3340) (elixir) (python) ([#3660](https://github.com/taskforcesh/bullmq/issues/3660)) ([fa22e84](https://github.com/taskforcesh/bullmq/commit/fa22e844d29961db95df58f2ae63b440d71c11f6))

### [2.19.2](https://github.com/taskforcesh/bullmq/compare/vpy2.19.1...vpy2.19.2) (2026-01-22)

#### 버그 수정

* **queue:** QueueBaseOptions TypedDict에 누락된 defaultJobOptions 필드 추가 \[python] ([#3702](https://github.com/taskforcesh/bullmq/issues/3702)) fixes [#3695](https://github.com/taskforcesh/bullmq/issues/3695) ([61504f1](https://github.com/taskforcesh/bullmq/commit/61504f12fe591295fea5b087a6b7c533465e8653))

### [2.19.1](https://github.com/taskforcesh/bullmq/compare/vpy2.19.0...vpy2.19.1) (2026-01-22)

#### 성능 개선

* **job:** max age 기준으로 jobs를 제거할 때 limit 적용 (python) (elixir) ([#3694](https://github.com/taskforcesh/bullmq/issues/3694)) fixes [#3672](https://github.com/taskforcesh/bullmq/issues/3672) ([a8fc316](https://github.com/taskforcesh/bullmq/commit/a8fc316c0989bd3edb54577ceb02bff0c600aa93))

## [2.19.0](https://github.com/taskforcesh/bullmq/compare/vpy2.18.3...vpy2.19.0) (2026-01-13)

#### 기능

* **queue:** drain method 지원 \[python] ([#3673](https://github.com/taskforcesh/bullmq/issues/3673)) ([21ab9cc](https://github.com/taskforcesh/bullmq/commit/21ab9cc5df2947e49aa132994dfe89e043b7082d))

### [2.18.3](https://github.com/taskforcesh/bullmq/compare/vpy2.18.2...vpy2.18.3) (2025-12-25)

#### 버그 수정

* **queue:** obliterate method에서 boolean force parameter를 string으로 변환 \[python] ([#3642](https://github.com/taskforcesh/bullmq/issues/3642)) fixes [#3640](https://github.com/taskforcesh/bullmq/issues/3640) ([706da0d](https://github.com/taskforcesh/bullmq/commit/706da0dc703d6be353d0140f1fd0de7683362e60))

### [2.18.2](https://github.com/taskforcesh/bullmq/compare/vpy2.18.1...vpy2.18.2) (2025-12-24)

#### 버그 수정

* **flow:** failParentOnFailure option에서 child job이 실패할 때 발생하는 KeyError 해결 \[python] ([#3639](https://github.com/taskforcesh/bullmq/issues/3639)) fixes [#3638](https://github.com/taskforcesh/bullmq/issues/3638) ([7f602e1](https://github.com/taskforcesh/bullmq/commit/7f602e1c6e31070f02c5ee5babbff33f55193551))

### [2.18.1](https://github.com/taskforcesh/bullmq/compare/vpy2.18.0...vpy2.18.1) (2025-12-20)

#### 버그 수정

* **flow:** 검증과 함께 failParentOnFailure 및 관련 dependency options 지원 \[python] ([#3621](https://github.com/taskforcesh/bullmq/issues/3621)) fixes [#3620](https://github.com/taskforcesh/bullmq/issues/3620) ([9c533c0](https://github.com/taskforcesh/bullmq/commit/9c533c0347865445b7f7df6b1c6e0923d25b4a8f))

## [2.18.0](https://github.com/taskforcesh/bullmq/compare/vpy2.17.0...vpy2.18.0) (2025-12-19)

#### 기능

* **add:** deduplication 지원 추가 \[python] ([#3614](https://github.com/taskforcesh/bullmq/issues/3614)) ref [#3613](https://github.com/taskforcesh/bullmq/issues/3613) ([0c3beb5](https://github.com/taskforcesh/bullmq/commit/0c3beb58f4a8c90ad7800f5616c2a3494a952963))

## [2.17.0](https://github.com/taskforcesh/bullmq/compare/vpy2.16.2...vpy2.17.0) (2025-12-14)

#### 기능

* **job:** retry method options 지원 \[elixir] \[python] ([#3601](https://github.com/taskforcesh/bullmq/issues/3601)) ([6e406a9](https://github.com/taskforcesh/bullmq/commit/6e406a94a5a2fe1f2c1c6e8a1073c6c9b1f11092))

### [2.16.2](https://github.com/taskforcesh/bullmq/compare/vpy2.16.1...vpy2.16.2) (2025-12-02)

#### 버그 수정

* **worker:** retryIfFailed method 추가 fixes [#3517](https://github.com/taskforcesh/bullmq/issues/3517) \[python] ([#3521](https://github.com/taskforcesh/bullmq/issues/3521)) ([c385b52](https://github.com/taskforcesh/bullmq/commit/c385b520b9fbe3dd58cdaead79c258835cab4361))

### [2.16.1](https://github.com/taskforcesh/bullmq/compare/vpy2.16.0...vpy2.16.1) (2025-09-08)

#### 버그 수정

* **deps:** semver를 v3로 업그레이드 \[python] ([#3414](https://github.com/taskforcesh/bullmq/issues/3414)) ([7dfd251](https://github.com/taskforcesh/bullmq/commit/7dfd2510a7bb03301365a2c24f045a0cd20580ef))

## [2.16.0](https://github.com/taskforcesh/bullmq/compare/vpy2.15.1...vpy2.16.0) (2025-09-07)

#### 기능

* **queue:** getWaitingCount method 지원 \[python] ([#3434](https://github.com/taskforcesh/bullmq/issues/3434)) ([1c75abb](https://github.com/taskforcesh/bullmq/commit/1c75abb4806971a2ac14c47b302c87f86095a2c3))

### [2.15.1](https://github.com/taskforcesh/bullmq/compare/vpy2.15.0...vpy2.15.1) (2025-09-06)

#### 버그 수정

* **job:** 재시도 시 parent 업데이트 고려 ([#3402](https://github.com/taskforcesh/bullmq/issues/3402)) (python) fixes [#3320](https://github.com/taskforcesh/bullmq/issues/3320) ([316d1ed](https://github.com/taskforcesh/bullmq/commit/316d1ed32680e690b1d2ab92c79a53e0d4c00c2d))
* **job:** 실패 시 scripts에 stacktrace 전달 \[python] ([#3294](https://github.com/taskforcesh/bullmq/issues/3294)) ([97b215d](https://github.com/taskforcesh/bullmq/commit/97b215d5a7aeaf4dceb4543bef1a00e463f12197))

## [2.15.0](https://github.com/taskforcesh/bullmq/compare/vpy2.14.0...vpy2.15.0) (2025-05-13)

#### 버그 수정

* **worker:** maxStalledCount가 0보다 작지 않도록 수정 ([#3249](https://github.com/taskforcesh/bullmq/issues/3249)) fixes [#3248](https://github.com/taskforcesh/bullmq/issues/3248) ([34dcb8c](https://github.com/taskforcesh/bullmq/commit/34dcb8c3d01a822b07852bc928d882bd6e4049d2))
* **remove:** 올바른 children meta references 전달 ([#3245](https://github.com/taskforcesh/bullmq/issues/3245)) ([01c62ad](https://github.com/taskforcesh/bullmq/commit/01c62ada0cea80c73ba28d79fd14ea5ba78fdc7d))

#### 기능

* **job:** moveToCompleted method 추가 \[python] ([#3251](https://github.com/taskforcesh/bullmq/issues/3251)) ([6a8e3e2](https://github.com/taskforcesh/bullmq/commit/6a8e3e206384b56063c6f5a46ca030d2b330c712))

## [2.14.0](https://github.com/taskforcesh/bullmq/compare/vpy2.13.1...vpy2.14.0) (2025-05-01)

#### 버그 수정

* **connection:** connection option에 str 타입 추가 \[python] ([#3212](https://github.com/taskforcesh/bullmq/issues/3212)) ([72fac42](https://github.com/taskforcesh/bullmq/commit/72fac4297f5a60e0c2ae0831507cb16ce8baed5f))
* **flow:** failParentOnFailure 또는 continueParentOnFailure일 때 dependencies에서 job 제거 ([#3201](https://github.com/taskforcesh/bullmq/issues/3201)) ([1fbcbec](https://github.com/taskforcesh/bullmq/commit/1fbcbec56969fc4aa628f77e4b05d2c6844894ae))
* **flow:** lock 제거 전에 pending dependencies 검증 ([#3182](https://github.com/taskforcesh/bullmq/issues/3182)) ([8d59e3b](https://github.com/taskforcesh/bullmq/commit/8d59e3b8084c60afad16372b4f7fc22f1b9d3f4e))
* **flow:** completed로 이동할 때만 pending dependencies 검증 ([#3164](https://github.com/taskforcesh/bullmq/issues/3164)) ([d3c397f](https://github.com/taskforcesh/bullmq/commit/d3c397fa3f122287026018aaae5ed2c5dfad19aa))
* **flow:** parent를 failed로 이동할 때 prioritized state 고려 ([#3160](https://github.com/taskforcesh/bullmq/issues/3160)) ([d91d9f4](https://github.com/taskforcesh/bullmq/commit/d91d9f4398584506f5af8b46e4d47b769beaa212))

#### 기능

* **flows:** continueParentOnFailure option 추가 ([#3181](https://github.com/taskforcesh/bullmq/issues/3181)) ([738d375](https://github.com/taskforcesh/bullmq/commit/738d3752934746a347fd04e59e9dcd4726777508))

#### 성능 개선

* **flow:** parent failure를 지연(lazy) 방식으로 변경 ([#3228](https://github.com/taskforcesh/bullmq/issues/3228)) ([6b37a37](https://github.com/taskforcesh/bullmq/commit/6b37a379cc65abe7b4c60ba427065957c9080a08))
* **flow:** failed로 이동시키기 전에 parentKey 존재 여부 검증 ([#3163](https://github.com/taskforcesh/bullmq/issues/3163)) ([5a88e47](https://github.com/taskforcesh/bullmq/commit/5a88e4745d9449e41c5e2c467b5d02ca21357703))

### [2.13.1](https://github.com/taskforcesh/bullmq/compare/vpy2.13.0...vpy2.13.1) (2025-03-15)

#### 버그 수정

* 변경 사항 없음

## [2.13.0](https://github.com/taskforcesh/bullmq/compare/vpy2.12.1...vpy2.13.0) (2025-03-15)

#### 버그 수정

* **flow:** failParentOnFailure가 제공될 때 waiting-children에 없는 parent도 failed 처리하도록 고려 ([#3098](https://github.com/taskforcesh/bullmq/issues/3098)) ([589adb4](https://github.com/taskforcesh/bullmq/commit/589adb4f89bcb7d7721200333c2d605eb6ba7864))

### [2.12.1](https://github.com/taskforcesh/bullmq/compare/vpy2.12.0...vpy2.12.1) (2025-02-28)

#### 버그 수정

* **worker:** delay\_until을 integer로 캐스팅 \[python] ([#3116](https://github.com/taskforcesh/bullmq/issues/3116)) ([db617e4](https://github.com/taskforcesh/bullmq/commit/db617e48ef1dd52446bfd73e15f24957df2ca315))
* **flow:** parent를 failed로 이동할 때 delayed state 고려 ([#3112](https://github.com/taskforcesh/bullmq/issues/3112)) ([6a28b86](https://github.com/taskforcesh/bullmq/commit/6a28b861346a3efa89574a78b396954d6c4ed113))

## [2.12.0](https://github.com/taskforcesh/bullmq/compare/vpy2.11.0...vpy2.12.0) (2025-02-21)

#### 버그 수정

* **flow:** parent에서 removeOnFail과 failParentOnFailure를 함께 사용할 수 있도록 허용 ([#2947](https://github.com/taskforcesh/bullmq/issues/2947)) fixes [#2229](https://github.com/taskforcesh/bullmq/issues/2229) ([85f6f6f](https://github.com/taskforcesh/bullmq/commit/85f6f6f181003fafbf75304a268170f0d271ccc3))

#### 성능 개선

* **delayed:** delayed jobs를 promote할 때 marker를 한 번만 추가 ([#3096](https://github.com/taskforcesh/bullmq/issues/3096)) (python) ([38912fb](https://github.com/taskforcesh/bullmq/commit/38912fba969d614eb44d05517ba2ec8bc418a16e))
* **add-job:** delay가 0으로 제공될 때 job을 wait 또는 prioritized state에 추가 ([#3052](https://github.com/taskforcesh/bullmq/issues/3052)) ([3e990eb](https://github.com/taskforcesh/bullmq/commit/3e990eb742b3a12065110f33135f282711fdd7b9))

## [2.11.0](https://github.com/taskforcesh/bullmq/compare/vpy2.10.1...vpy2.11.0) (2024-11-26)

#### 기능

* **queue:** getDelayedCount method 추가 \[python] ([#2934](https://github.com/taskforcesh/bullmq/issues/2934)) ([71ce75c](https://github.com/taskforcesh/bullmq/commit/71ce75c04b096b5593da0986c41a771add1a81ce))

#### 성능 개선

* **marker:** jobs를 consume하는 동안 worker가 바쁘게 동작하도록 base markers 추가 ([#2904](https://github.com/taskforcesh/bullmq/issues/2904)) fixes [#2842](https://github.com/taskforcesh/bullmq/issues/2842) ([1759c8b](https://github.com/taskforcesh/bullmq/commit/1759c8bc111cab9e43d5fccb4d8d2dccc9c39fb4))

### [2.10.1](https://github.com/taskforcesh/bullmq/compare/vpy2.10.0...vpy2.10.1) (2024-10-26)

#### 버그 수정

* **commands:** 릴리스 시 누락된 build statement 추가 \[python] ([#2869](https://github.com/taskforcesh/bullmq/issues/2869)) fixes [#2868](https://github.com/taskforcesh/bullmq/issues/2868) ([ff2a47b](https://github.com/taskforcesh/bullmq/commit/ff2a47b37c6b36ee1a725f91de2c6e4bcf8b011a))

## [2.10.0](https://github.com/taskforcesh/bullmq/compare/vpy2.9.4...vpy2.10.0) (2024-10-24)

#### 기능

* **job:** getChildrenValues 메서드 추가 \[python] ([#2853](https://github.com/taskforcesh/bullmq/issues/2853)) ([0f25213](https://github.com/taskforcesh/bullmq/commit/0f25213b28900a1c35922bd33611701629d83184))

### [2.9.4](https://github.com/taskforcesh/bullmq/compare/vpy2.9.3...vpy2.9.4) (2024-09-10)

#### 버그 수정

* **metrics:** 정확도를 높이기 위해 서로 다른 분의 포인트를 구분 ([#2766](https://github.com/taskforcesh/bullmq/issues/2766)) (python) ([7cb670e](https://github.com/taskforcesh/bullmq/commit/7cb670e1bf9560a24de3da52427b4f6b6152a59a))

#### 성능 개선

* **metrics:** 0을 최대 데이터 포인트 수만큼 저장 ([#2758](https://github.com/taskforcesh/bullmq/issues/2758)) ([3473054](https://github.com/taskforcesh/bullmq/commit/347305451a9f5d7f2c16733eb139b5de96ea4b9c))

### [2.9.3](https://github.com/taskforcesh/bullmq/compare/vpy2.9.2...vpy2.9.3) (2024-08-31)

#### 버그 수정

* **flow:** ignoreDependencyOnFailure 옵션을 재귀적으로 적용 ([#2712](https://github.com/taskforcesh/bullmq/issues/2712)) ([53bc9eb](https://github.com/taskforcesh/bullmq/commit/53bc9eb68b5bb0a470a8fe64ef78ece5cde44632))

### [2.9.2](https://github.com/taskforcesh/bullmq/compare/vpy2.9.1...vpy2.9.2) (2024-08-10)

#### 버그 수정

* **flow:** stalled 체크가 발생할 때 ignoreDependencyOnFailure 전에 parentData 검증 ([#2702](https://github.com/taskforcesh/bullmq/issues/2702)) (python) ([9416501](https://github.com/taskforcesh/bullmq/commit/9416501551b1ad464e59bdba1045a5a9955e2ea4))

### [2.9.1](https://github.com/taskforcesh/bullmq/compare/vpy2.9.0...vpy2.9.1) (2024-08-08)

#### 버그 수정

* 변경 사항 없음

## [2.9.0](https://github.com/taskforcesh/bullmq/compare/vpy2.8.1...vpy2.9.0) (2024-08-02)

#### 버그 수정

* **job:** json.dumps가 JSON 규격을 준수하는 JSON을 반환하도록 보장 \[python] ([#2683](https://github.com/taskforcesh/bullmq/issues/2683)) ([4441711](https://github.com/taskforcesh/bullmq/commit/4441711a986a9f6a326100308d639eb0a2ea8c8d))

### [2.8.1](https://github.com/taskforcesh/bullmq/compare/vpy2.8.0...vpy2.8.1) (2024-07-11)

#### 버그 수정

* **delayed:** 지연 작업 스케줄링 시 jobId 사용 회피 ([#2587](https://github.com/taskforcesh/bullmq/issues/2587)) (python) ([228db2c](https://github.com/taskforcesh/bullmq/commit/228db2c780a1ca8323900fc568156495a13355a3))

#### 성능

* **delayed:** 큐가 일시 중지된 경우에도 지연 작업을 waiting으로 계속 이동 ([#2640](https://github.com/taskforcesh/bullmq/issues/2640)) (python) ([b89e2e0](https://github.com/taskforcesh/bullmq/commit/b89e2e0913c0886561fc1c2470771232f17f5b3b))

## [2.8.0](https://github.com/taskforcesh/bullmq/compare/vpy2.7.8...vpy2.8.0) (2024-07-10)

#### 버그 수정

* **parent:** 동일한 jobIds를 사용해 completed 상태의 자식을 다시 추가하는 경우를 고려 ([#2627](https://github.com/taskforcesh/bullmq/issues/2627)) (python) fixes [#2554](https://github.com/taskforcesh/bullmq/issues/2554) ([00cd017](https://github.com/taskforcesh/bullmq/commit/00cd0174539fbe1cc4628b9b6e1a7eb87a5ef705))
* **priority:** getCountsPerPriority 호출 시 paused 상태 고려 (python) ([#2609](https://github.com/taskforcesh/bullmq/issues/2609)) ([6e99250](https://github.com/taskforcesh/bullmq/commit/6e992504b2a7a2fa76f1d04ad53d1512e98add7f))
* **priority:** 순서를 유지하기 위해 bit.band 대신 module 사용 (python) ([#2597](https://github.com/taskforcesh/bullmq/issues/2597)) ([9ece15b](https://github.com/taskforcesh/bullmq/commit/9ece15b17420fe0bee948a5307e870915e3bce87))

#### 기능

* **queue:** getCountsPerPriority 메서드 추가 \[python] ([#2607](https://github.com/taskforcesh/bullmq/issues/2607)) ([02b8338](https://github.com/taskforcesh/bullmq/commit/02b83380334879cc2434043141566f2a375db958))

### [2.7.8](https://github.com/taskforcesh/bullmq/compare/vpy2.7.7...vpy2.7.8) (2024-06-05)

#### 버그 수정

* print 호출 제거 \[python] ([#2579](https://github.com/taskforcesh/bullmq/issues/2579)) ([f957186](https://github.com/taskforcesh/bullmq/commit/f95718689864dbaca8a6b4113a6b37727919d6df))

### [2.7.7](https://github.com/taskforcesh/bullmq/compare/vpy2.7.6...vpy2.7.7) (2024-06-04)

#### 버그 수정

* **retry-job:** 작업이 active 상태가 아니면 오류 발생 ([#2576](https://github.com/taskforcesh/bullmq/issues/2576)) ([ca207f5](https://github.com/taskforcesh/bullmq/commit/ca207f593d0ed455ecc59d9e0ef389a9a50d9634))

### [2.7.6](https://github.com/taskforcesh/bullmq/compare/vpy2.7.5...vpy2.7.6) (2024-05-09)

#### 버그 수정

* **connection:** async Retry 사용 ([#2555](https://github.com/taskforcesh/bullmq/issues/2555)) \[python] ([d6dd21d](https://github.com/taskforcesh/bullmq/commit/d6dd21d3ac28660bbfa7825bba0b586328769709))

### [2.7.5](https://github.com/taskforcesh/bullmq/compare/vpy2.7.4...vpy2.7.5) (2024-04-28)

#### 버그 수정

* **worker:** close 시 작업이 완료될 때까지 대기 ([#2545](https://github.com/taskforcesh/bullmq/issues/2545)) \[python] ([d81f210](https://github.com/taskforcesh/bullmq/commit/d81f210a5f5968fc040e820946fb672deb24bd01))

### [2.7.4](https://github.com/taskforcesh/bullmq/compare/vpy2.7.3...vpy2.7.4) (2024-04-26)

#### 버그 수정

* **redis-connection:** redis 재시도 전략 백오프 증가 ([#2546](https://github.com/taskforcesh/bullmq/issues/2545)) \[python] ([6cf7712](https://github.com/taskforcesh/bullmq/commit/6cf77122da845e5b0afa1607348cf06602679329))

### [2.7.3](https://github.com/taskforcesh/bullmq/compare/vpy2.7.2...vpy2.7.3) (2024-04-24)

#### 버그 수정

* **stalled:** ignoreDependencyOnFailure 옵션 고려 (python) ([#2540](https://github.com/taskforcesh/bullmq/issues/2540)) fixes [#2531](https://github.com/taskforcesh/bullmq/issues/2531) ([0140959](https://github.com/taskforcesh/bullmq/commit/0140959cabd2613794631e41ebe4c2ddee6f91da))

### [2.7.2](https://github.com/taskforcesh/bullmq/compare/vpy2.7.1...vpy2.7.2) (2024-04-20)

#### 버그 수정

* **worker:** redis 버전에 따라 minimumBlockTimeout 반환 (python) ([#2532](https://github.com/taskforcesh/bullmq/issues/2532)) ([83dfb63](https://github.com/taskforcesh/bullmq/commit/83dfb63e72a1a36a4dfc40f122efb54fbb796339))

### [2.7.1](https://github.com/taskforcesh/bullmq/compare/vpy2.7.0...vpy2.7.1) (2024-04-18)

#### 버그 수정

* **stalled:** 자식을 failed로 이동할 때 failParentOnFailure 고려 ([#2526](https://github.com/taskforcesh/bullmq/issues/2526)) fixes [#2464](https://github.com/taskforcesh/bullmq/issues/2464) (python) ([5e31eb0](https://github.com/taskforcesh/bullmq/commit/5e31eb096169ea57350db591bcebfc2264a6b6dc))

## [2.7.0](https://github.com/taskforcesh/bullmq/compare/vpy2.6.0...vpy2.7.0) (2024-04-13)

#### 기능

* **queue:** getJobLogs 메서드 추가 \[python] ([#2523](https://github.com/taskforcesh/bullmq/issues/2523)) ref [#2472](https://github.com/taskforcesh/bullmq/issues/2472) ([a24a16e](https://github.com/taskforcesh/bullmq/commit/a24a16ea2707541ee06ec3c4d636cd30dcdaade5))

## [2.6.0](https://github.com/taskforcesh/bullmq/compare/vpy2.5.0...vpy2.6.0) (2024-04-13)

#### 기능

* **worker:** redis 버전이 7.0.8보다 낮을 때 최소 timeout으로 0.002 사용 \[python] ([#2521](https://github.com/taskforcesh/bullmq/issues/2521)) ([f3862dd](https://github.com/taskforcesh/bullmq/commit/f3862dd0c85cf2c2122fb0306c5f4b5eb8ad0bcd))

## [2.5.0](https://github.com/taskforcesh/bullmq/compare/vpy2.4.0...vpy2.5.0) (2024-04-08)

#### 기능

* **python:** 재사용 가능한 redis 연결 지원 ([29ad8c8](https://github.com/taskforcesh/bullmq/commit/29ad8c83596b14a312ad1cd375e0e34d4fdecc52))

## [2.4.0](https://github.com/taskforcesh/bullmq/compare/vpy2.3.3...vpy2.4.0) (2024-04-07)

#### 성능 개선

* **stalled:** active에서 이동된 후 lock 제거 시 stalled에서 jobId 제거 ([#2512](https://github.com/taskforcesh/bullmq/issues/2512)) (python) ([64feec9](https://github.com/taskforcesh/bullmq/commit/64feec91b0b034fe640a846166bd95b546ff6d71))

### [2.3.3](https://github.com/taskforcesh/bullmq/compare/vpy2.3.2...vpy2.3.3) (2024-03-24)

#### 버그 수정

* **connection:** redis 연결에 대한 모든 파라미터 허용 \[python] ([#2486](https://github.com/taskforcesh/bullmq/issues/2486)) ([ce30192](https://github.com/taskforcesh/bullmq/commit/ce30192ad30f66fb0f39c8c9ed669ddd133346c8))

### [2.3.2](https://github.com/taskforcesh/bullmq/compare/vpy2.3.1...vpy2.3.2) (2024-03-23)

#### 버그 수정

* 변경 사항 없음

### [2.3.1](https://github.com/taskforcesh/bullmq/compare/vpy2.3.0...vpy2.3.1) (2024-03-19)

#### 버그 수정

* **worker:** 지연 작업을 가져올 시간이 되면 blockTimeout을 0.001로 설정 \[python] ([#2478](https://github.com/taskforcesh/bullmq/issues/2478)) ([b385034](https://github.com/taskforcesh/bullmq/commit/b385034006ac183a26093f593269349eb78f8b54))

## [2.3.0](https://github.com/taskforcesh/bullmq/compare/vpy2.2.4...vpy2.3.0) (2024-03-16)

#### 기능

* **job:** log 메서드 추가 \[python] ([#2476](https://github.com/taskforcesh/bullmq/issues/2476)) ref [#2472](https://github.com/taskforcesh/bullmq/issues/2472) ([34946c4](https://github.com/taskforcesh/bullmq/commit/34946c4b29cc9e7d5ae81f8fd170a2e539ac6279))

### [2.2.4](https://github.com/taskforcesh/bullmq/compare/vpy2.2.3...vpy2.2.4) (2024-02-13)

#### 버그 수정

* **flow:** 부모 작업을 교체할 수 없음 (python) ([#2417](https://github.com/taskforcesh/bullmq/issues/2417)) ([2696ef8](https://github.com/taskforcesh/bullmq/commit/2696ef8200058b7f616938c2166a3b0454663b39))

### [2.2.3](https://github.com/taskforcesh/bullmq/compare/vpy2.2.2...vpy2.2.3) (2024-02-10)

#### 성능 개선

* **marker:** standard와 delayed marker 구분 (python) ([#2389](https://github.com/taskforcesh/bullmq/issues/2389)) ([18ebee8](https://github.com/taskforcesh/bullmq/commit/18ebee8c242f66f1b5b733d68e48c574b1f1fdef))

### [2.2.2](https://github.com/taskforcesh/bullmq/compare/vpy2.2.1...vpy2.2.2) (2024-02-03)

#### 버그 수정

* **reprocess-job:** 필요 시 marker 추가 ([#2406](https://github.com/taskforcesh/bullmq/issues/2406)) ([5923ed8](https://github.com/taskforcesh/bullmq/commit/5923ed885f5451eee2f14258767d7d5f8d80ae13))
* **stalled:** 작업을 wait로 다시 이동할 때 marker 추가를 고려 ([#2384](https://github.com/taskforcesh/bullmq/issues/2384)) ([4914df8](https://github.com/taskforcesh/bullmq/commit/4914df87e416711835291e81da93b279bd758254))

#### 성능 개선

* **flow:** 부모를 wait로 이동할 때 marker 추가 (python) ([#2408](https://github.com/taskforcesh/bullmq/issues/2408)) ([6fb6896](https://github.com/taskforcesh/bullmq/commit/6fb6896701ae7595e1cb5e2cdbef44625c48d673))
* **move-to-active:** rate limited를 한 번만 확인 ([#2391](https://github.com/taskforcesh/bullmq/issues/2391)) ([`ca6c17a`](https://github.com/taskforcesh/bullmq/commit/ca6c17a43e38d5339e62471ea9f59c62a169b797))

### [2.2.1](https://github.com/taskforcesh/bullmq/compare/vpy2.2.0...vpy2.2.1) (2024-01-16)

#### 버그 수정

* **retry-jobs:** 필요 시 marker 추가 ([#2374](https://github.com/taskforcesh/bullmq/issues/2374)) ([`1813d5f`](https://github.com/taskforcesh/bullmq/commit/1813d5fa12b7db69ee6c8c09273729cda8e3e3b5))

## [2.2.0](https://github.com/taskforcesh/bullmq/compare/vpy2.1.0...vpy2.2.0) (2024-01-14)

#### 기능

* **queue:** promoteJobs 메서드 추가 \[python] ([#2377](https://github.com/taskforcesh/bullmq/issues/2377)) ([3b9de96](https://github.com/taskforcesh/bullmq/commit/3b9de967efa34ea22cdab1fbc7ff65d49927d787))

## [2.1.0](https://github.com/taskforcesh/bullmq/compare/vpy2.0.0...vpy2.1.0) (2024-01-12)

#### 버그 수정

* **redis:** v5로 업그레이드 \[python] ([#2364](https://github.com/taskforcesh/bullmq/issues/2364)) ([d5113c8](https://github.com/taskforcesh/bullmq/commit/d5113c88ad108b281b292e2890e0eef3be41c8fb))

## [2.0.0](https://github.com/taskforcesh/bullmq/compare/vpy1.24.0...vpy2.0.0) (2023-12-23)

#### 버그 수정

* **connection:** Queue와 Worker의 redis 연결 인자를 통일 ([#2282](https://github.com/taskforcesh/bullmq/issues/2282)) ([8eee20f](https://github.com/taskforcesh/bullmq/commit/8eee20f1210a49024eeee6647817f0659b8c3893))

#### 기능

* **job:** isActive 메서드 추가 \[python] ([#2352](https://github.com/taskforcesh/bullmq/issues/2352)) ([afb5e31](https://github.com/taskforcesh/bullmq/commit/afb5e31484ed2e5a1c381c732321225c0a8b78ff))
* **job:** 작업을 수동으로 이동할 때 attemptsMade를 attemptsStarted와 분리 ([#2203](https://github.com/taskforcesh/bullmq/issues/2203)) ([0e88e4f](https://github.com/taskforcesh/bullmq/commit/0e88e4fe4ed940487dfc79d1345d0686de22d0c6))
* **scripts:** 새로운 queue markers 사용 ([4276eb7](https://github.com/taskforcesh/bullmq/commit/4276eb725ca294ddbfc00c4edc627bb2cb5d403a))
* **worker:** markers 처리 개선 ([73cf5fc](https://github.com/taskforcesh/bullmq/commit/73cf5fc1e6e13d8329e1e4e700a8db92173e0624)) ([0bac0fb](https://github.com/taskforcesh/bullmq/commit/0bac0fbb97afa968aa7644f1438b86d7bc18bbc5))

#### 호환성이 깨지는 변경 사항

* **connection:** connection은 옵션의 일부로 제공되어야 합니다 ([#2282](https://github.com/taskforcesh/bullmq/issues/2282)) ([8eee20f](https://github.com/taskforcesh/bullmq/commit/8eee20f1210a49024eeee6647817f0659b8c3893))
* **worker:** markers는 이제 특수 Job ID를 사용하는 대신 redis의 전용 key를 사용합니다. ([`73cf5fc`](https://github.com/taskforcesh/bullmq/commit/73cf5fc1e6e13d8329e1e4e700a8db92173e0624)) ([`0bac0fb`](https://github.com/taskforcesh/bullmq/commit/0bac0fbb97afa968aa7644f1438b86d7bc18bbc5))
* 참고:
  * [Better Queue Markers](https://bullmq.io/news/231204/better-queue-markers/)

