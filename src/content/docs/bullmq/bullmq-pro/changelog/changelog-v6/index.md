---
title: '[6.11.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.10.0...v6.11.0) (2024-02-26)'
description: 'ref faster priority jobs'
---

Source URL: https://docs.bullmq.io/bullmq-pro/changelog/changelog-v6

# v6

## [6.11.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.10.0...v6.11.0) (2024-02-26)

#### 기능

* sandboxed-job-pro 인터페이스 노출 ([6652e0a](https://github.com/taskforcesh/bullmq-pro/commit/6652e0afbdd45664c1e9436f9da0161adfea8c0d))

## [6.10.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.9.6...v6.10.0) (2024-02-21)

#### 기능

* **groups:** groups에 대한 sandbox 지원 추가 ([53be7a0](https://github.com/taskforcesh/bullmq-pro/commit/53be7a095fca70df7bf8e52dfec45dde8dac064a))

### [6.9.6](https://github.com/taskforcesh/bullmq-pro/compare/v6.9.5...v6.9.6) (2024-01-31)

#### 버그 수정

* **groups:** 마지막 job 제거 시 group 제거 ([#199](https://github.com/taskforcesh/bullmq-pro/issues/199)) ([3066686](https://github.com/taskforcesh/bullmq-pro/commit/3066686df4851334efadd7024cc8566407eabd7f))

### [6.9.5](https://github.com/taskforcesh/bullmq-pro/compare/v6.9.4...v6.9.5) (2024-01-27)

#### 버그 수정

* **batches:** movetoBatchFinished 응답 구분 ([#198](https://github.com/taskforcesh/bullmq-pro/issues/198)) ([bb74c50](https://github.com/taskforcesh/bullmq-pro/commit/bb74c501f19fabbb61c4cb637598591f508bd59d))

### [6.9.4](https://github.com/taskforcesh/bullmq-pro/compare/v6.9.3...v6.9.4) (2024-01-20)

#### 버그 수정

* **backoff:** delayed job 추가 후 marker 설정 ([#197](https://github.com/taskforcesh/bullmq-pro/issues/197)) ([50a012e](https://github.com/taskforcesh/bullmq-pro/commit/50a012e352b9608a2a7f36db0cd7643078e183ee))

### [6.9.3](https://github.com/taskforcesh/bullmq-pro/compare/v6.9.2...v6.9.3) (2024-01-18)

#### 성능 개선

* **prioritized:** addPrioritizedJob에서 대상 목록을 한 번만 조회 ([#195](https://github.com/taskforcesh/bullmq-pro/issues/195)) ([51cf4a3](https://github.com/taskforcesh/bullmq-pro/commit/51cf4a34d645013a49c01b740cf280666ebc4c97))

### [6.9.2](https://github.com/taskforcesh/bullmq-pro/compare/v6.9.1...v6.9.2) (2024-01-17)

#### 버그 수정

* **groups:** maxSize가 제공될 때 prioritized groups 고려 ([#194](https://github.com/taskforcesh/bullmq-pro/issues/194)) ([1c345c5](https://github.com/taskforcesh/bullmq-pro/commit/1c345c550685f5fdb2d2ff95056261af324d2ca5))

### [6.9.1](https://github.com/taskforcesh/bullmq-pro/compare/v6.9.0...v6.9.1) (2024-01-15)

#### 버그 수정

* **events:** job 완료 시에만 drained event 발생 ([#192](https://github.com/taskforcesh/bullmq-pro/issues/192)) ([22a503d](https://github.com/taskforcesh/bullmq-pro/commit/22a503d4f462cea68f03015af93e0701ed27e2d6))

## [6.9.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.8.0...v6.9.0) (2023-12-28)

#### 버그 수정

* **flows:** constructor와 methods를 queue base에 맞게 업데이트 ([#2324](https://github.com/taskforcesh/bullmq/issues/2324)) ([d6c2064](https://github.com/taskforcesh/bullmq/commit/d6c2064b1fdd88bd4cc61e049ce055ff620b0062))
* **sandboxed:** esbuild와의 호환성 개선 ([8eaf955](https://github.com/taskforcesh/bullmq/commit/8eaf9550fe8b322df624893c507c55d2cce34b11))
* **child-processor:** commonjs에서 dynamic imports 유지 ([d97a5e0](https://github.com/taskforcesh/bullmq/commit/d97a5e06816cff04d86facdb8d32b512f29c6fb9))
* **flows:** flows로 생성된 queues에 meta key 추가 ([272ec69](https://github.com/taskforcesh/bullmq/commit/272ec69557f601a138e1aaba739f7e7878d5344b))
* **repeat-strategy:** 누락된 Promise 반환 타입 추가 ([#2301](https://github.com/taskforcesh/bullmq/issues/2301)) ([6f8f534](https://github.com/taskforcesh/bullmq/commit/6f8f5342cc8aa03f596d9ed5b8831f96a1d4c736))
* **update-progress:** 충돌 방지를 위해 이전 updateProgress script 제거 ([#2298](https://github.com/taskforcesh/bullmq/issues/2298)) (python) ([e65b819](https://github.com/taskforcesh/bullmq/commit/e65b819101f8e0e8fdef8c51cfdf9a52f5e73f13))
* **worker:** module.filename을 사용해 dirname 가져오기 ([#2296](https://github.com/taskforcesh/bullmq/issues/2296)) fixes [#2288](https://github.com/taskforcesh/bullmq/issues/2288) ([6e4db5a](https://github.com/taskforcesh/bullmq/commit/6e4db5a3f3648c6a7e10991f2e18f3dab96fb1d7))
* **worker:** update progress events에 상한 적용 필요 ([2cab9e9](https://github.com/taskforcesh/bullmq/commit/2cab9e94f65c7bdd053e3fb5944bcda6e3ebaa39))

#### 기능

* **sandbox:** processor file로 URL(local files) 지원 ([7eea670](https://github.com/taskforcesh/bullmq/commit/7eea6700b33bfd7f36b030b647b819a4c5fd9606))
* **queue:** 페이지네이션된 getDependencies 추가 ([#2327](https://github.com/taskforcesh/bullmq/issues/2327)) ([c5b8ba3](https://github.com/taskforcesh/bullmq/commit/c5b8ba318b12a84a3a6a928345377fa0eaa08ee3))
* **sandboxes:** require 대신 호환성이 더 좋은 dynamic import 사용 ([6d2fe6e](https://github.com/taskforcesh/bullmq/commit/6d2fe6e7c0473b75aeb9a6d3080b0676f9521065))

## [6.8.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.7.0...v6.8.0) (2023-11-30)

#### 버그 수정

* **worker:** 느린 jobs를 기다리지 않도록 수정 fixes [#2290](https://github.com/taskforcesh/bullmq/issues/2290) ([568d758](https://github.com/taskforcesh/bullmq/commit/568d7585edb1f2ef15991d4ae4a2425e6834046a))
* **utils:** namespace 대신 타입으로 EventEmitter 사용 ([#2283](https://github.com/taskforcesh/bullmq/issues/2283)) ([41c9d1d](https://github.com/taskforcesh/bullmq/commit/41c9d1d05eedc7351272708e667e8d65eb6773fc))
* **job:** 재시도될 때 현재 job 인스턴스에 delay 값 설정 ([#2266](https://github.com/taskforcesh/bullmq/issues/2266)) (python) ([76e075f](https://github.com/taskforcesh/bullmq/commit/76e075f54d5745b6cec3cb11305bf3110d963eae))

#### 기능

* **worker:** jobs를 가져올 때 concurrency 처리 개선 ([#2242](https://github.com/taskforcesh/bullmq/issues/2242)) ([d2e2035](https://github.com/taskforcesh/bullmq/commit/d2e203588878ee64cb21e67141f73b32867dfb40))

#### 성능 개선

* **rate-limit:** paused 상태일 때도 groups 프로모션 계속 수행 ([#187](https://github.com/taskforcesh/bullmq-pro/issues/187)) ([17f9e81](https://github.com/taskforcesh/bullmq-pro/commit/17f9e81ad330eb273c3863f448fd3eee546d420f))

## [6.7.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.6.2...v6.7.0) (2023-11-22)

#### 기능

* **queue:** clean이 반복적으로 동작하도록 개선 ([#2260](https://github.com/taskforcesh/bullmq/issues/2260)) ([0cfa66f](https://github.com/taskforcesh/bullmq/commit/0cfa66fd0fa0dba9b3941f183cf6f06d8a4f281d)) ref ([#186](https://github.com/taskforcesh/bullmq-pro/issues/186))

#### 버그 수정

* **utils:** namespace 대신 타입으로 EventEmitter 사용 ([#2283](https://github.com/taskforcesh/bullmq/issues/2283)) ([41c9d1d](https://github.com/taskforcesh/bullmq/commit/41c9d1d05eedc7351272708e667e8d65eb6773fc))
* **job:** 재시도될 때 현재 job 인스턴스에 delay 값 설정 ([#2266](https://github.com/taskforcesh/bullmq/issues/2266)) (python) ([76e075f](https://github.com/taskforcesh/bullmq/commit/76e075f54d5745b6cec3cb11305bf3110d963eae))
* **connection:** 연결된 listeners 처리 개선 ([02474ad](https://github.com/taskforcesh/bullmq/commit/02474ad59a7b340d7bb2a7415ae7a88e14200398))
* **connection:** redis instance 검사 로직을 queue base로 이동 ([13a339a](https://github.com/taskforcesh/bullmq/commit/13a339a730f46ff22acdd4a046e0d9c4b7d88679))
* delayed set으로 이동할 때 delay job 속성 업데이트 ([#2261](https://github.com/taskforcesh/bullmq/issues/2261)) ([69ece08](https://github.com/taskforcesh/bullmq/commit/69ece08babd7716c14c38c3dd50630b44c7c1897))
* **add-job:** waiting-children event가 발행될 때 events trim ([#2262](https://github.com/taskforcesh/bullmq/issues/2262)) (python) ([198bf05](https://github.com/taskforcesh/bullmq/commit/198bf05fa5a4e1ce50081296033a2e0f26ece498))

### [6.6.2](https://github.com/taskforcesh/bullmq-pro/compare/v6.6.1...v6.6.2) (2023-11-03)

#### 버그 수정

* **worker:** workers 종료 중에도 locks 확장을 계속 유지 ([#2259](https://github.com/taskforcesh/bullmq/issues/2259)) ([c4d12ea](https://github.com/taskforcesh/bullmq/commit/c4d12ea3a9837ffd7f58e2134796137c4181c3de))
* **sandbox:** undefined일 때 빈 object 결과를 반환하지 않음 ([#2247](https://github.com/taskforcesh/bullmq/issues/2247)) ([308db7f](https://github.com/taskforcesh/bullmq/commit/308db7f58758a72b8abb272da8e92509813a2178))
* **events:** 존재하지 않는 jobs에 removed event를 발행하지 않음 ([#2227](https://github.com/taskforcesh/bullmq/issues/2227)) ([c134606](https://github.com/taskforcesh/bullmq/commit/c1346064c6cd9f93c59b184f150eac11d51c91b4))

#### 성능 개선

* **redis-connection:** redis 버전이 v6 이상인지 한 번만 확인 ([#2252](https://github.com/taskforcesh/bullmq/issues/2252)) ([a09b15a](https://github.com/taskforcesh/bullmq/commit/a09b15af0d5dedfa83bce7130ee9094f3fb69e10))
* **events:** jobs 제거 시 events trim ([#2235](https://github.com/taskforcesh/bullmq/issues/2235)) (python) ([889815c](https://github.com/taskforcesh/bullmq/commit/889815c412666e5fad8f32d2e3a2d41cf650f001))

### [6.6.1](https://github.com/taskforcesh/bullmq-pro/compare/v6.6.0...v6.6.1) (2023-10-11)

#### 버그 수정

* **events:** job 재시도 시 events trim ([#2224](https://github.com/taskforcesh/bullmq/issues/2224)) ([1986b05](https://github.com/taskforcesh/bullmq/commit/1986b05ac03fe4ee48861aa60caadcc9df8170a6))
* **sandbox:** job 인스턴스의 progress 값 업데이트 ([#2214](https://github.com/taskforcesh/bullmq/issues/2214)) fixes [#2213](https://github.com/taskforcesh/bullmq/issues/2213) ([3d0f36a](https://github.com/taskforcesh/bullmq/commit/3d0f36a134b7f5c6b6de26967c9d71bcfb346e72))

## [6.6.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.5.0...v6.6.0) (2023-10-06)

#### 버그 수정

* **delayed:** jobs를 delayed로 이동할 때 events trim (python) ([#2211](https://github.com/taskforcesh/bullmq/issues/2211)) ([eca8c2d](https://github.com/taskforcesh/bullmq/commit/eca8c2d4dfeafbd8ac36a49764dbd4897303628c))

#### 기능

* **queue:** addJobLog 및 updateJobProgress 노출 ([#2202](https://github.com/taskforcesh/bullmq/issues/2202)) ([2056939](https://github.com/taskforcesh/bullmq/commit/205693907a4d6c2da9bd0690fb552b1d1e369c08))

## [6.5.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.4.0...v6.5.0) (2023-09-28)

#### 기능

* **sandbox:** 확장을 위해 wrapJob method를 protected로 전환 ([#2182](https://github.com/taskforcesh/bullmq/issues/2182)) ([1494b55](https://github.com/taskforcesh/bullmq/commit/1494b5566573356e0248b4a5cab48ae21d82f1da))

#### 버그 수정

* **queue:** batched unpack이 이제 range를 사용 ([#2188](https://github.com/taskforcesh/bullmq/issues/2188)) ([b5e97f4](https://github.com/taskforcesh/bullmq/commit/b5e97f420bc0c4bc82772f3e87883ee522be43d9))
* **worker:** skipVersionCheck를 blockingConnection으로 전달 ([#2189](https://github.com/taskforcesh/bullmq/issues/2189)) ref [#2149](https://github.com/taskforcesh/bullmq/issues/2149) ([c8aa9a3](https://github.com/taskforcesh/bullmq/commit/c8aa9a36224cba8ecb19af1bf652f4f1c4c20d40))
* **worker:** concurrency가 NaN일 때 exception 발생 ([#2184](https://github.com/taskforcesh/bullmq/issues/2184)) ([f36ac8b](https://github.com/taskforcesh/bullmq/commit/f36ac8b61dcd4bb3d9e283278310cd50cfc83fae))
* **queue:** clean method에서 상태별 score 목적을 구분 ([#2133](https://github.com/taskforcesh/bullmq/issues/2133)) fixes [#2124](https://github.com/taskforcesh/bullmq/issues/2124) ([862f10b](https://github.com/taskforcesh/bullmq/commit/862f10b586276314d9bffff2a5e6caf939399f7e))

## [6.4.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.3.4...v6.4.0) (2023-09-16)

#### 기능

* **connection:** shared connections를 위한 skipVersionCheck 옵션 제공 ([#2149](https://github.com/taskforcesh/bullmq/issues/2149)) ref [#2148](https://github.com/taskforcesh/bullmq/issues/2148) ([914820f](https://github.com/taskforcesh/bullmq/commit/914820f720cbc48b49f4bd1c46d148eb2bb5b79c))

* **sandbox:** moveToDelayed 메서드 에뮬레이션 ([#180](https://github.com/taskforcesh/bullmq-pro/issues/180)) ([d61de09](https://github.com/taskforcesh/bullmq-pro/commit/d61de095115481b688101bfaf0b126a02545cc6f)) ref [#2118](https://github.com/taskforcesh/bullmq/issues/2118)

#### 버그 수정

* **remove:** job이 잠겨 있을 때 오류 메시지 변경 (python) ([#2175](https://github.com/taskforcesh/bullmq/issues/2175)) ([2f5628f](https://github.com/taskforcesh/bullmq/commit/2f5628feffab66cdcc78abf4d7bb608bdcaa65bb))
* **sandbox:** processor의 추가 params 무시 ([#2142](https://github.com/taskforcesh/bullmq/issues/2142)) ([3602c20](https://github.com/taskforcesh/bullmq/commit/3602c20ab80cbe0a0d3de66210a01ad119e1090b))

### [6.3.4](https://github.com/taskforcesh/bullmq-pro/compare/v6.3.3...v6.3.4) (2023-08-18)

#### 버그 수정

* **worker:** worker 종료 시 rate-limit 지연 중단 ([#179](https://github.com/taskforcesh/bullmq-pro/issues/179)) ([4ad650b](https://github.com/taskforcesh/bullmq-pro/commit/4ad650b7bc0c6a950536df252e510cb96e2e0054))

### [6.3.3](https://github.com/taskforcesh/bullmq-pro/compare/v6.3.2...v6.3.3) (2023-08-15)

#### 버그 수정

* **queue:** name이 제공되지 않으면 오류 발생 ([#178](https://github.com/taskforcesh/bullmq-pro/issues/178)) ([9715bf1](https://github.com/taskforcesh/bullmq-pro/commit/9715bf15edef1f54a9ebc618eb7d47c7b45a35ca))

### [6.3.2](https://github.com/taskforcesh/bullmq-pro/compare/v6.3.1...v6.3.2) (2023-08-11)

#### 버그 수정

* 일부 엣지 케이스에서 group rate limit 수정 ([#177](https://github.com/taskforcesh/bullmq-pro/issues/177)) ([c3c87a7](https://github.com/taskforcesh/bullmq-pro/commit/c3c87a7f0a6de5c35ac389efbac594d6d987cf49))

### [6.3.1](https://github.com/taskforcesh/bullmq-pro/compare/v6.3.0...v6.3.1) (2023-08-10)

#### 성능 개선

* **rate-limit:** 필요한 경우에만 pttl 조회 ([#175](https://github.com/taskforcesh/bullmq-pro/issues/175)) ([0439823](https://github.com/taskforcesh/bullmq-pro/commit/0439823c32a82e48abcae43c29e50ef912c31d15))

## [6.3.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.2.4...v6.3.0) (2023-08-03)

#### 기능

* **queue:** getRateLimitTtl 메서드 추가 ([#173](https://github.com/taskforcesh/bullmq-pro/issues/173)) ([3327350](https://github.com/taskforcesh/bullmq-pro/commit/3327350d06526651353974aa7822fdeeec881fb0))

### [6.2.4](https://github.com/taskforcesh/bullmq-pro/compare/v6.2.3...v6.2.4) (2023-07-29)

#### 버그 수정

* **group:** group option에 priority 옵션 추가 ([#171](https://github.com/taskforcesh/bullmq-pro/issues/171)) ([2e632f1](https://github.com/taskforcesh/bullmq-pro/commit/2e632f11013a0db520f7a642741df21bbdd38a78)), closes [taskforcesh/bullmq-pro-support#23](https://github.com/taskforcesh/bullmq-pro-support/issues/23) [taskforcesh/bullmq-pro-support#13](https://github.com/taskforcesh/bullmq-pro-support/issues/13)

### [6.2.3](https://github.com/taskforcesh/bullmq-pro/compare/v6.2.2...v6.2.3) (2023-07-27)

#### 성능 개선

* **groups:** rate-limited group 승격 시 job을 paused로 이동하지 않음 ([#169](https://github.com/taskforcesh/bullmq-pro/issues/169)) ([fa2bb3c](https://github.com/taskforcesh/bullmq-pro/commit/fa2bb3c98761615822035312dfdb782934d9a774))

### [6.2.2](https://github.com/taskforcesh/bullmq-pro/compare/v6.2.1...v6.2.2) (2023-07-26)

#### 기능

* **queue:** 모든 delayed job을 승격하는 promoteJobs 추가 ([6074592](https://github.com/taskforcesh/bullmq/commit/6074592574256ec4b1c340126288e803e56b1a64))
* **job:** remove 메서드에 children 제거 옵션 추가 (python) ([#2064](https://github.com/taskforcesh/bullmq/issues/2064)) ([841dc87](https://github.com/taskforcesh/bullmq/commit/841dc87a689897df81438ad1f43e45a4da77c388))
* **job:** removeDependencyOnFailure 옵션 추가 ([#1953](https://github.com/taskforcesh/bullmq/issues/1953)) ([ffd49e2](https://github.com/taskforcesh/bullmq/commit/ffd49e289c57252487200d47b92193228ae7451f))

### [6.2.1](https://github.com/taskforcesh/bullmq-pro/compare/v6.2.0...v6.2.1) (2023-07-25)

#### 버그 수정

* **flow:** parent가 delayed로 이동될 때 delayed 이벤트 발생 ([#166](https://github.com/taskforcesh/bullmq-pro/issues/166)) ([38afe1c](https://github.com/taskforcesh/bullmq-pro/commit/38afe1cf3187ddee33d33a39438587d921b8743a))

## [6.2.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.1.1...v6.2.0) (2023-07-25)

#### 기능

* **groups:** local priorities 지원 ([#156](https://github.com/taskforcesh/bullmq-pro/issues/156)) ([260bd24](https://github.com/taskforcesh/bullmq-pro/commit/260bd24a76d703ec87385c05cdd3b4589f142aa8)), closes [taskforcesh/bullmq-pro-support#23](https://github.com/taskforcesh/bullmq-pro-support/issues/23) [taskforcesh/bullmq-pro-support#13](https://github.com/taskforcesh/bullmq-pro-support/issues/13)

### [6.1.1](https://github.com/taskforcesh/bullmq-pro/compare/v6.1.0...v6.1.1) (2023-07-18)

#### 버그 수정

* 누락된 error export 추가 ([2b8c51f](https://github.com/taskforcesh/bullmq-pro/commit/2b8c51fd43c538fd3eed122ab96d55325da97b90))

## [6.1.0](https://github.com/taskforcesh/bullmq-pro/compare/v6.0.5...v6.1.0) (2023-07-18)

#### 버그 수정

* GroupMaxSizeExceededError prototype 수정 ([a1b6a96](https://github.com/taskforcesh/bullmq-pro/commit/a1b6a96f1a0b632940177a1057a4995d59957964))

#### 기능

* getGroupStatus 추가 ([3bac19d](https://github.com/taskforcesh/bullmq-pro/commit/3bac19d32e9a620a393736152844973951e45d47))
* 최대 크기 group 지원 추가 ([7bc654c](https://github.com/taskforcesh/bullmq-pro/commit/7bc654c2191c9a2e8c80f4e0843c4beda7d61565))

### [6.0.5](https://github.com/taskforcesh/bullmq-pro/compare/v6.0.4...v6.0.5) (2023-07-11)

#### 버그 수정

* **pause-group:** queue가 paused일 때 job을 wait로 이동하지 않음 ([#162](https://github.com/taskforcesh/bullmq-pro/issues/162)) ([458b381](https://github.com/taskforcesh/bullmq-pro/commit/458b3813eef982dc661a019349776d44d6ddb194))

### [6.0.4](https://github.com/taskforcesh/bullmq-pro/compare/v6.0.3...v6.0.4) (2023-07-07)

#### 버그 수정

* **group:** paused 상태 및 dynamic rate limit일 때 job을 group list로 이동 ([#161](https://github.com/taskforcesh/bullmq-pro/issues/161)) ([1625f36](https://github.com/taskforcesh/bullmq-pro/commit/1625f36b3014ac191828d8ce070f237c19494c67))

### [6.0.3](https://github.com/taskforcesh/bullmq-pro/compare/v6.0.2...v6.0.3) (2023-07-05)

#### 버그 수정

* **rate-limit:** rateLimitGroup에서 waiting 이벤트 발생 ([#160](https://github.com/taskforcesh/bullmq-pro/issues/160)) ([eaf3cd7](https://github.com/taskforcesh/bullmq-pro/commit/eaf3cd74e3bcd40e6ba46bb2f540cae9cb945962))

### [6.0.2](https://github.com/taskforcesh/bullmq-pro/compare/v6.0.1...v6.0.2) (2023-07-04)

#### 성능 개선

* **remove-job:** 마지막 group id를 제거하지 않음 ([#159](https://github.com/taskforcesh/bullmq-pro/issues/159)) ([f5a3cd5](https://github.com/taskforcesh/bullmq-pro/commit/f5a3cd50d78bcadfd09ca9c5de1054f9620c191b))

### [6.0.1](https://github.com/taskforcesh/bullmq-pro/compare/v6.0.0...v6.0.1) (2023-06-29)

#### 버그 수정

* **job:** job이 parent여도 groupId 저장 ([#157](https://github.com/taskforcesh/bullmq-pro/issues/157)) ([1debbf4](https://github.com/taskforcesh/bullmq-pro/commit/1debbf40ca4aa8f8b5ab45c36e8732f7ffe5442b))

## [6.0.0](https://github.com/taskforcesh/bullmq-pro/compare/v5.3.5...v6.0.0) (2023-06-26)

#### 성능 개선

* **priority:** prioritized를 새 상태로 추가 ([#155](https://github.com/taskforcesh/bullmq-pro/issues/155)) ([b2391ca](https://github.com/taskforcesh/bullmq-pro/commit/b2391cab4d63e97f807eaed3a6e814be01de0f32))

#### 호환성 깨지는 변경 사항

* **priority:** priority가 별도의 zset으로 분리되어 중복이 필요 없음
* job 메서드 이름 `update`를 `updateData`로 변경

ref [faster priority jobs](https://bullmq.io/news/062123/faster-priority-jobs/)

