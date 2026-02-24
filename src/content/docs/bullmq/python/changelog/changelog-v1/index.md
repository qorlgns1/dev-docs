---
title: '[1.24.0](https://github.com/taskforcesh/bullmq/compare/vpy1.23.0...vpy1.24.0) (2023-12-21)'
description: '원본 URL: https://docs.bullmq.io/python/changelog/changelog-v1'
---

원본 URL: https://docs.bullmq.io/python/changelog/changelog-v1

# v1

## [1.24.0](https://github.com/taskforcesh/bullmq/compare/vpy1.23.0...vpy1.24.0) (2023-12-21)

#### 기능

* **job:** isWaitingChildren 메서드 추가 \[python] ([#2345](https://github.com/taskforcesh/bullmq/issues/2345)) ([e9c1fa1](https://github.com/taskforcesh/bullmq/commit/e9c1fa10b258ebe171a0396c29b6ccb05aef2608))

## [1.23.0](https://github.com/taskforcesh/bullmq/compare/vpy1.22.0...vpy1.23.0) (2023-12-18)

#### 기능

* **queue:** getRateLimitTtl 메서드 추가 \[python] ([#2340](https://github.com/taskforcesh/bullmq/issues/2340)) ([f0a1f70](https://github.com/taskforcesh/bullmq/commit/f0a1f7084478f7899233021fbb4d4307c94dfead))

## [1.22.0](https://github.com/taskforcesh/bullmq/compare/vpy1.21.0...vpy1.22.0) (2023-12-14)

#### 기능

* **job:** isFailed 메서드 추가 \[python] ([#2333](https://github.com/taskforcesh/bullmq/issues/2333)) ([19bfccc](https://github.com/taskforcesh/bullmq/commit/19bfccc2d7734b150a5fbb6ea720fcd9887c9dd3))

## [1.21.0](https://github.com/taskforcesh/bullmq/compare/vpy1.20.0...vpy1.21.0) (2023-12-14)

#### 기능

* **job:** isCompleted 메서드 추가 \[python] ([#2331](https://github.com/taskforcesh/bullmq/issues/2331)) ([364f0c1](https://github.com/taskforcesh/bullmq/commit/364f0c1f2d4247d2b24041ab9ece0e429110d454))

## [1.20.0](https://github.com/taskforcesh/bullmq/compare/vpy1.19.0...vpy1.20.0) (2023-12-13)

#### 기능

* **job:** isWaiting 메서드 추가 \[python] ([#2328](https://github.com/taskforcesh/bullmq/issues/2328)) ([5db9f95](https://github.com/taskforcesh/bullmq/commit/5db9f957939cd873eea0224d34569189e5520e84))

## [1.19.0](https://github.com/taskforcesh/bullmq/compare/vpy1.18.0...vpy1.19.0) (2023-12-12)

#### 기능

* **job:** promote 메서드 추가 \[python] ([#2323](https://github.com/taskforcesh/bullmq/issues/2323)) ([61f4ba3](https://github.com/taskforcesh/bullmq/commit/61f4ba3e99486aa36e5cc3d9b448b8080c567eb1))

## [1.18.0](https://github.com/taskforcesh/bullmq/compare/vpy1.17.0...vpy1.18.0) (2023-12-10)

#### 버그 수정

* **retry:** retryJob 스크립트에 올바른 redis command 이름 전달 ([#2321](https://github.com/taskforcesh/bullmq/issues/2321)) \[python] ([6bb21a0](https://github.com/taskforcesh/bullmq/commit/6bb21a07c9754659fa5aa1734df1046a6da5d16a))
* **flows:** flows로 생성된 queue에 meta key 추가 ([272ec69](https://github.com/taskforcesh/bullmq/commit/272ec69557f601a138e1aaba739f7e7878d5344b))
* **update-progress:** 충돌 방지를 위해 기존 updateProgress 스크립트 제거 ([#2298](https://github.com/taskforcesh/bullmq/issues/2298)) (python) ([e65b819](https://github.com/taskforcesh/bullmq/commit/e65b819101f8e0e8fdef8c51cfdf9a52f5e73f13))
* **worker:** update progress 이벤트 수를 제한하도록 수정 ([2cab9e9](https://github.com/taskforcesh/bullmq/commit/2cab9e94f65c7bdd053e3fb5944bcda6e3ebaa39))

## [1.17.0](https://github.com/taskforcesh/bullmq/compare/vpy1.16.1...vpy1.17.0) (2023-11-24)

#### 기능

* **worker:** job을 가져올 때 동시성 처리 개선 ([#2242](https://github.com/taskforcesh/bullmq/issues/2242)) ([d2e2035](https://github.com/taskforcesh/bullmq/commit/d2e203588878ee64cb21e67141f73b32867dfb40))

### [1.16.1](https://github.com/taskforcesh/bullmq/compare/vpy1.16.0...vpy1.16.1) (2023-11-09)

#### 버그 수정

* **job:** 재시도 시 현재 job 인스턴스에 delay 값 설정 ([#2266](https://github.com/taskforcesh/bullmq/issues/2266)) (python) ([76e075f](https://github.com/taskforcesh/bullmq/commit/76e075f54d5745b6cec3cb11305bf3110d963eae))

## [1.16.0](https://github.com/taskforcesh/bullmq/compare/vpy1.15.4...vpy1.16.0) (2023-11-08)

#### 버그 수정

* **backoff:** builtin backoff type 수정 ([#2265](https://github.com/taskforcesh/bullmq/issues/2265)) \[python] ([76959eb](https://github.com/taskforcesh/bullmq/commit/76959eb9d9495eb1b6d2d31fab93c8951b5d3b93))

### [1.15.4](https://github.com/taskforcesh/bullmq/compare/vpy1.15.3...vpy1.15.4) (2023-11-05)

#### 버그 수정

* delayed set으로 이동할 때 delay job 속성 업데이트 ([#2261](https://github.com/taskforcesh/bullmq/issues/2261)) ([69ece08](https://github.com/taskforcesh/bullmq/commit/69ece08babd7716c14c38c3dd50630b44c7c1897))

### [1.15.3](https://github.com/taskforcesh/bullmq/compare/vpy1.15.2...vpy1.15.3) (2023-11-05)

#### 버그 수정

* **add-job:** waiting-children 이벤트가 발행될 때 이벤트 트리밍 ([#2262](https://github.com/taskforcesh/bullmq/issues/2262)) (python) ([198bf05](https://github.com/taskforcesh/bullmq/commit/198bf05fa5a4e1ce50081296033a2e0f26ece498))

### [1.15.2](https://github.com/taskforcesh/bullmq/compare/vpy1.15.1...vpy1.15.2) (2023-10-18)

#### 버그 수정

* **events:** 존재하지 않는 job에 대해 removed 이벤트를 발행하지 않음 ([#2227](https://github.com/taskforcesh/bullmq/issues/2227)) ([c134606](https://github.com/taskforcesh/bullmq/commit/c1346064c6cd9f93c59b184f150eac11d51c91b4))
* **events:** job 재시도 시 이벤트 트리밍 ([#2224](https://github.com/taskforcesh/bullmq/issues/2224)) ([1986b05](https://github.com/taskforcesh/bullmq/commit/1986b05ac03fe4ee48861aa60caadcc9df8170a6))

#### 성능 개선

* **events:** job 제거 시 이벤트 트리밍 ([#2235](https://github.com/taskforcesh/bullmq/issues/2235)) (python) ([889815c](https://github.com/taskforcesh/bullmq/commit/889815c412666e5fad8f32d2e3a2d41cf650f001))

### [1.15.1](https://github.com/taskforcesh/bullmq/compare/vpy1.15.0...vpy1.15.1) (2023-10-04)

#### 버그 수정

* **delayed:** job을 delayed로 이동할 때 이벤트 트리밍 (python) ([#2211](https://github.com/taskforcesh/bullmq/issues/2211)) ([eca8c2d](https://github.com/taskforcesh/bullmq/commit/eca8c2d4dfeafbd8ac36a49764dbd4897303628c))

## [1.15.0](https://github.com/taskforcesh/bullmq/compare/vpy1.14.0...vpy1.15.0) (2023-09-30)

#### 기능

* 변경 사항 없음

## [1.14.0](https://github.com/taskforcesh/bullmq/compare/vpy1.13.2...vpy1.14.0) (2023-09-26)

#### 기능

* **queue:** clean 메서드 추가 \[python] ([#2194](https://github.com/taskforcesh/bullmq/issues/2194)) ([3b67193](https://github.com/taskforcesh/bullmq/commit/3b6719379cbec5beb1b7dfb5f06d46cbbf74010f))

#### 버그 수정

* **move-to-finished:** 모든 반환 값을 문자열로 변환 \[python] ([#2198](https://github.com/taskforcesh/bullmq/issues/2198)) fixes [#2196](https://github.com/taskforcesh/bullmq/issues/2196) ([07f1335](https://github.com/taskforcesh/bullmq/commit/07f13356eb1c0136f03dfdf946d163f0ef3c4d62))
* **queue:** batched unpack이 이제 range를 사용 ([#2188](https://github.com/taskforcesh/bullmq/issues/2188)) ([b5e97f4](https://github.com/taskforcesh/bullmq/commit/b5e97f420bc0c4bc82772f3e87883ee522be43d9))
* **queue:** clean 메서드에서 상태별 score 용도 구분 ([#2133](https://github.com/taskforcesh/bullmq/issues/2133)) fixes [#2124](https://github.com/taskforcesh/bullmq/issues/2124) ([862f10b](https://github.com/taskforcesh/bullmq/commit/862f10b586276314d9bffff2a5e6caf939399f7e))

### [1.13.2](https://github.com/taskforcesh/bullmq/compare/vpy1.13.1...vpy1.13.2) (2023-09-12)

#### 버그 수정

* **remove:** job이 잠겨 있을 때 오류 메시지 변경 (python) ([#2175](https://github.com/taskforcesh/bullmq/issues/2175)) ([2f5628f](https://github.com/taskforcesh/bullmq/commit/2f5628feffab66cdcc78abf4d7bb608bdcaa65bb))

### [1.13.1](https://github.com/taskforcesh/bullmq/compare/vpy1.13.0...vpy1.13.1) (2023-09-11)

#### 버그 수정

* **move-to-finished:** 마지막 active job 처리 시 prioritized job 추가를 고려 ([@2176](https://github.com/taskforcesh/bullmq/issues/2176)) (python) ([4b01f35](https://github.com/taskforcesh/bullmq/commit/4b01f359c290cfc62ea74ff3ab0b43ccc6956a02))

## [1.13.0](https://github.com/taskforcesh/bullmq/compare/vpy1.12.0...vpy1.13.0) (2023-09-07)

#### 기능

* **flow-producer:** addBulk 메서드 추가 (python) ([#2174](https://github.com/taskforcesh/bullmq/issues/2174)) ([c67dfb4](https://github.com/taskforcesh/bullmq/commit/c67dfb49931ee4cb96573af660e9f2316942687c))

## [1.12.0](https://github.com/taskforcesh/bullmq/compare/vpy1.11.0...vpy1.12.0) (2023-08-31)

#### 기능

* **queue:** addBulk 메서드 추가 ([#2161](https://github.com/taskforcesh/bullmq/issues/2161)) ([555dd44](https://github.com/taskforcesh/bullmq/commit/555dd44a0190f4957e43f083e2f59d7f58b90ac9))

## [1.11.0](https://github.com/taskforcesh/bullmq/compare/vpy1.10.1...vpy1.11.0) (2023-08-26)

#### 기능

* flow producer 클래스 추가 ([#2115](https://github.com/taskforcesh/bullmq/issues/2115)) ([14a769b](https://github.com/taskforcesh/bullmq/commit/14a769b193d97576ff9b3f2a65de47463ba04ffd))

### [1.10.1](https://github.com/taskforcesh/bullmq/compare/vpy1.10.0...vpy1.10.1) (2023-08-19)

#### 버그 수정

* **job:** job getReturnValue가 returnvalue를 반환하지 않던 문제 수정 ([#2143](https://github.com/taskforcesh/bullmq/issues/2143)) ([dcb8e6a](https://github.com/taskforcesh/bullmq/commit/dcb8e6a8e62346fac8574bd9aac56c5a25589a2c))

#### 성능 개선

* **rate-limit:** 필요할 때만 pttl 조회 ([#2129](https://github.com/taskforcesh/bullmq/issues/2129)) ([12ce2f3](https://github.com/taskforcesh/bullmq/commit/12ce2f3746626a81ea961961bb1a629077eed68a))

## [1.10.0](https://github.com/taskforcesh/bullmq/compare/vpy1.9.0...vpy1.10.0) (2023-08-03)

#### 기능

* **redis-connection:** redisOpts에 username 옵션 추가 ([#2108](https://github.com/taskforcesh/bullmq/issues/2108)) ([d27f33e](https://github.com/taskforcesh/bullmq/commit/d27f33e997d30e6c0c7d4484bea338347c3fe67e))

#### 성능 개선

* **retry:** regex 표현식 대신 이전 상태(prev state) 비교 ([#2099](https://github.com/taskforcesh/bullmq/issues/2099)) ([c141283](https://github.com/taskforcesh/bullmq/commit/c1412831903d1fae0955af097e0be049024839fe))

## [1.9.0](https://github.com/taskforcesh/bullmq/compare/vpy1.8.0...vpy1.9.0) (2023-07-18)

#### 기능

* **job:** remove 메서드에 children 제거 옵션 추가 (python) ([#2064](https://github.com/taskforcesh/bullmq/issues/2064)) ([841dc87](https://github.com/taskforcesh/bullmq/commit/841dc87a689897df81438ad1f43e45a4da77c388))

## [1.8.0](https://github.com/taskforcesh/bullmq/compare/vpy1.7.0...vpy1.8.0) (2023-07-17)

#### 버그 수정

* **worker:** concurrency 준수 ([#2062](https://github.com/taskforcesh/bullmq/issues/2062)) fixes [#2063](https://github.com/taskforcesh/bullmq/issues/2063) ([1b95185](https://github.com/taskforcesh/bullmq/commit/1b95185e8f4a4349037b59e61455bdec79792644))

## [1.7.0](https://github.com/taskforcesh/bullmq/compare/vpy1.6.1...vpy1.7.0) (2023-07-14)

#### 기능

* **queue:** remove 메서드 추가 ([#2066](https://github.com/taskforcesh/bullmq/issues/2066)) ([808ee72](https://github.com/taskforcesh/bullmq/commit/808ee7231c75d4d826881f25e346f01b2fd2dc23))
* **worker:** token의 일부로 id 추가 ([#2061](https://github.com/taskforcesh/bullmq/issues/2061)) ([e255356](https://github.com/taskforcesh/bullmq/commit/e2553562271e1e4143a8fef616349bb30de4899d))

### [1.6.1](https://github.com/taskforcesh/bullmq/compare/vpy1.6.0...vpy1.6.1) (2023-07-10)

#### 버그 수정

* **pyproject:** requires-python 설정 추가 ([#2056](https://github.com/taskforcesh/bullmq/issues/2056)) fixes [#1979](https://github.com/taskforcesh/bullmq/issues/1979) ([a557970](https://github.com/taskforcesh/bullmq/commit/a557970c755d370ed23850e2f32af35774002bc9))

## [1.6.0](https://github.com/taskforcesh/bullmq/compare/vpy1.5.0...vpy1.6.0) (2023-07-06)

#### 기능

* **job:** moveToWaitingChildren 메서드 추가 ([#2049](https://github.com/taskforcesh/bullmq/issues/2049)) ([6d0e224](https://github.com/taskforcesh/bullmq/commit/6d0e224cd985069055786f447b0ba7c394a76b8a))

## [1.5.0](https://github.com/taskforcesh/bullmq/compare/vpy1.4.0...vpy1.5.0) (2023-07-04)

#### 버그 수정

* **queue:** custom prefix가 있을 때 isPaused 메서드 수정 ([#2047](https://github.com/taskforcesh/bullmq/issues/2047)) ([7ec1c5b](https://github.com/taskforcesh/bullmq/commit/7ec1c5b2ccbd575ecd50d339f5377e204ca7aa16))

## [1.4.0](https://github.com/taskforcesh/bullmq/compare/vpy1.3.1...vpy1.4.0) (2023-06-30)

#### 기능

* **queue:** getJobState 메서드 추가 ([#2040](https://github.com/taskforcesh/bullmq/issues/2040)) ([8ec9ed6](https://github.com/taskforcesh/bullmq/commit/8ec9ed67d2803224a3b866c51f67239a5c4b7042))

### [1.3.1](https://github.com/taskforcesh/bullmq/compare/vpy1.3.0...vpy1.3.1) (2023-06-29)

#### 버그 수정

* **pyproject:** 루트 위치에 egg-info 빌드 ([3c2d06e](https://github.com/taskforcesh/bullmq/commit/3c2d06e7e6e0944135fe6bd8045d08dd43fe7d9c))

## [1.3.0](https://github.com/taskforcesh/bullmq/compare/vpy1.2.0...vpy1.3.0) (2023-06-29)

#### 버그 수정

* **release:** 권장 pyproject.toml 구성 추가 ([#2029](https://github.com/taskforcesh/bullmq/issues/2029)) ([d03ffc9](https://github.com/taskforcesh/bullmq/commit/d03ffc9c98425a96d6e9dd47a6625382556a4cbf))

#### 기능

* **queue:** getFailedCount 메서드 추가 ([#2036](https://github.com/taskforcesh/bullmq/issues/2036)) ([92d7227](https://github.com/taskforcesh/bullmq/commit/92d7227bf5ec63a75b7af3fc7c312d9b4a81d69f))
* **queue:** getCompletedCount 메서드 추가 ([#2033](https://github.com/taskforcesh/bullmq/issues/2033)) ([3e9db5e](https://github.com/taskforcesh/bullmq/commit/3e9db5ef4d868f8b420e368a711c20c2568a5910))

## [1.2.0](https://github.com/taskforcesh/bullmq/compare/vpy1.1.0...vpy1.2.0) (2023-06-24)

#### 기능

* **queue:** 상태별 job 조회 메서드 추가 ([#2012](https://github.com/taskforcesh/bullmq/issues/2012)) ([57b2b72](https://github.com/taskforcesh/bullmq/commit/57b2b72f79afb683067d49170df5d2eed46e3712))

## [1.1.0](https://github.com/taskforcesh/bullmq/compare/vpy1.0.0...vpy1.1.0) (2023-06-23)

#### 기능

* **queue:** getJobs 메서드 추가 ([#2011](https://github.com/taskforcesh/bullmq/issues/2011)) ([8d5d6c1](https://github.com/taskforcesh/bullmq/commit/8d5d6c14442b7b967c42cb6ec3907a4d1a5bd575))

## [1.0.0](https://github.com/taskforcesh/bullmq/compare/vpy0.5.6...vpy1.1.0) (2023-06-21)

#### 성능 개선

* **priority:** 새로운 상태로 prioritized 추가 ([#1984](https://github.com/taskforcesh/bullmq/issues/1984)) (python) ([42a890a](https://github.com/taskforcesh/bullmq/commit/42a890a2bfe45b29348030f886766400f5d41aa3))

#### 호환성 깨지는 변경

* **priority:** priority가 자체 zset으로 분리되어 중복이 필요 없음 ([42a890a](https://github.com/taskforcesh/bullmq/commit/42a890a2bfe45b29348030f886766400f5d41aa3))

참조 [faster priority jobs](https://bullmq.io/news/062123/faster-priority-jobs/)

