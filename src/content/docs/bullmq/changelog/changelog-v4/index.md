---
title: '[4.18.3](https://github.com/taskforcesh/bullmq/compare/v4.18.2...v4.18.3) (2025-07-19)'
description: '원본 URL: https://docs.bullmq.io/changelog/changelog-v4'
---

원본 URL: https://docs.bullmq.io/changelog/changelog-v4

# v4

### [4.18.3](https://github.com/taskforcesh/bullmq/compare/v4.18.2...v4.18.3) (2025-07-19)

#### 성능 개선

* **delayed:** 지연된 작업을 승격할 때 마커를 한 번만 추가 ([#3312](https://github.com/taskforcesh/bullmq/issues/3312)) ([c4a4ada](https://github.com/taskforcesh/bullmq/commit/c4a4adaf5db970d042efe0853145974c62aabdfe))

### [4.18.2](https://github.com/taskforcesh/bullmq/compare/v4.18.1...v4.18.2) (2024-10-24)

#### 버그 수정

* 버전을 가져오는 올바른 방식 ([1a433d2](https://github.com/taskforcesh/bullmq/commit/1a433d2a17b58ba8d30f0ecf52d9091f8377978f))

### [4.18.1](https://github.com/taskforcesh/bullmq/compare/v4.18.0...v4.18.1) (2024-10-19)

#### 버그 수정

* lua 명령에 versions 사용 ([b0a216d](https://github.com/taskforcesh/bullmq/commit/b0a216deacb0295e77b039ea67c100e57b045037))

## [4.18.0](https://github.com/taskforcesh/bullmq/compare/v4.17.0...v4.18.0) (2024-10-14)

#### 기능

* **queue:** 버전 지원 추가 ([a600463](https://github.com/taskforcesh/bullmq/commit/a6004639612118ce5adc2a87f0402386ba8e1c2f))

## [4.17.0](https://github.com/taskforcesh/bullmq/compare/v4.16.0...v4.17.0) (2023-12-21)

#### 기능

* **sandbox:** processor 파일로 URL(로컬 파일) 지원 ([7eea670](https://github.com/taskforcesh/bullmq/commit/7eea6700b33bfd7f36b030b647b819a4c5fd9606))

## [4.16.0](https://github.com/taskforcesh/bullmq/compare/v4.15.4...v4.16.0) (2023-12-18)

#### 기능

* **queue:** 페이지네이션된 getDependencies 추가 ([#2327](https://github.com/taskforcesh/bullmq/issues/2327)) ([c5b8ba3](https://github.com/taskforcesh/bullmq/commit/c5b8ba318b12a84a3a6a928345377fa0eaa08ee3))

### [4.15.4](https://github.com/taskforcesh/bullmq/compare/v4.15.3...v4.15.4) (2023-12-14)

#### 버그 수정

* **flows:** 생성자와 메서드를 queue base에 맞게 업데이트 ([#2324](https://github.com/taskforcesh/bullmq/issues/2324)) ([d6c2064](https://github.com/taskforcesh/bullmq/commit/d6c2064b1fdd88bd4cc61e049ce055ff620b0062))

### [4.15.3](https://github.com/taskforcesh/bullmq/compare/v4.15.2...v4.15.3) (2023-12-13)

#### 버그 수정

* **sandboxed:** esbuild와의 호환성 개선 ([8eaf955](https://github.com/taskforcesh/bullmq/commit/8eaf9550fe8b322df624893c507c55d2cce34b11))

### [4.15.2](https://github.com/taskforcesh/bullmq/compare/v4.15.1...v4.15.2) (2023-12-07)

#### 버그 수정

* **child-processor:** commonjs에서 dynamic imports 유지 ([d97a5e0](https://github.com/taskforcesh/bullmq/commit/d97a5e06816cff04d86facdb8d32b512f29c6fb9))

### [4.15.1](https://github.com/taskforcesh/bullmq/compare/v4.15.0...v4.15.1) (2023-12-06)

#### 버그 수정

* **flows:** flows로 생성된 queues에 meta 키 추가 ([272ec69](https://github.com/taskforcesh/bullmq/commit/272ec69557f601a138e1aaba739f7e7878d5344b))

## [4.15.0](https://github.com/taskforcesh/bullmq/compare/v4.14.4...v4.15.0) (2023-12-05)

#### 기능

* **sandboxes:** require 대신 호환성이 더 좋은 dynamic import 사용 ([6d2fe6e](https://github.com/taskforcesh/bullmq/commit/6d2fe6e7c0473b75aeb9a6d3080b0676f9521065))

### [4.14.4](https://github.com/taskforcesh/bullmq/compare/v4.14.3...v4.14.4) (2023-11-28)

#### 버그 수정

* **repeat-strategy:** 누락된 Promise 반환 타입 추가 ([#2301](https://github.com/taskforcesh/bullmq/issues/2301)) ([6f8f534](https://github.com/taskforcesh/bullmq/commit/6f8f5342cc8aa03f596d9ed5b8831f96a1d4c736))

### [4.14.3](https://github.com/taskforcesh/bullmq/compare/v4.14.2...v4.14.3) (2023-11-27)

#### 버그 수정

* **update-progress:** 충돌 방지를 위해 기존 updateProgress 스크립트 제거 ([#2298](https://github.com/taskforcesh/bullmq/issues/2298)) (python) ([e65b819](https://github.com/taskforcesh/bullmq/commit/e65b819101f8e0e8fdef8c51cfdf9a52f5e73f13))
* **worker:** module.filename을 사용해 dirname 가져오기 ([#2296](https://github.com/taskforcesh/bullmq/issues/2296)) [#2288](https://github.com/taskforcesh/bullmq/issues/2288) 수정 ([6e4db5a](https://github.com/taskforcesh/bullmq/commit/6e4db5a3f3648c6a7e10991f2e18f3dab96fb1d7))

### [4.14.2](https://github.com/taskforcesh/bullmq/compare/v4.14.1...v4.14.2) (2023-11-24)

#### 버그 수정

* **worker:** update progress 이벤트 수를 제한해야 함 ([2cab9e9](https://github.com/taskforcesh/bullmq/commit/2cab9e94f65c7bdd053e3fb5944bcda6e3ebaa39))

### [4.14.1](https://github.com/taskforcesh/bullmq/compare/v4.14.0...v4.14.1) (2023-11-23)

#### 버그 수정

* **worker:** 느린 작업을 기다리지 않음 [#2290](https://github.com/taskforcesh/bullmq/issues/2290) 수정 ([568d758](https://github.com/taskforcesh/bullmq/commit/568d7585edb1f2ef15991d4ae4a2425e6834046a))

## [4.14.0](https://github.com/taskforcesh/bullmq/compare/v4.13.3...v4.14.0) (2023-11-18)

#### 기능

* **worker:** 작업 가져오기 시 동시성 처리 개선 ([#2242](https://github.com/taskforcesh/bullmq/issues/2242)) ([d2e2035](https://github.com/taskforcesh/bullmq/commit/d2e203588878ee64cb21e67141f73b32867dfb40))

### [4.13.3](https://github.com/taskforcesh/bullmq/compare/v4.13.2...v4.13.3) (2023-11-16)

#### 버그 수정

* **utils:** namespace 대신 EventEmitter를 타입으로 사용 ([#2283](https://github.com/taskforcesh/bullmq/issues/2283)) ([41c9d1d](https://github.com/taskforcesh/bullmq/commit/41c9d1d05eedc7351272708e667e8d65eb6773fc))

### [4.13.2](https://github.com/taskforcesh/bullmq/compare/v4.13.1...v4.13.2) (2023-11-09)

#### 버그 수정

* **job:** 재시도 시 현재 job 인스턴스에 delay 값 설정 ([#2266](https://github.com/taskforcesh/bullmq/issues/2266)) (python) ([76e075f](https://github.com/taskforcesh/bullmq/commit/76e075f54d5745b6cec3cb11305bf3110d963eae))

### [4.13.1](https://github.com/taskforcesh/bullmq/compare/v4.13.0...v4.13.1) (2023-11-08)

#### 버그 수정

* **connection:** 연결된 리스너 처리 개선 ([02474ad](https://github.com/taskforcesh/bullmq/commit/02474ad59a7b340d7bb2a7415ae7a88e14200398))
* **connection:** redis 인스턴스 체크를 queue base로 이동 ([13a339a](https://github.com/taskforcesh/bullmq/commit/13a339a730f46ff22acdd4a046e0d9c4b7d88679))

## [4.13.0](https://github.com/taskforcesh/bullmq/compare/v4.12.10...v4.13.0) (2023-11-05)

#### 기능

* **queue:** 반복적으로 동작하도록 clean 개선 ([#2260](https://github.com/taskforcesh/bullmq/issues/2260)) ([0cfa66f](https://github.com/taskforcesh/bullmq/commit/0cfa66fd0fa0dba9b3941f183cf6f06d8a4f281d))

### [4.12.10](https://github.com/taskforcesh/bullmq/compare/v4.12.9...v4.12.10) (2023-11-05)

#### 버그 수정

* delayed set으로 이동할 때 delay job 속성 업데이트 ([#2261](https://github.com/taskforcesh/bullmq/issues/2261)) ([69ece08](https://github.com/taskforcesh/bullmq/commit/69ece08babd7716c14c38c3dd50630b44c7c1897))

### [4.12.9](https://github.com/taskforcesh/bullmq/compare/v4.12.8...v4.12.9) (2023-11-05)

#### 버그 수정

* **add-job:** waiting-children 이벤트가 발행될 때 events 트림 ([#2262](https://github.com/taskforcesh/bullmq/issues/2262)) (python) ([198bf05](https://github.com/taskforcesh/bullmq/commit/198bf05fa5a4e1ce50081296033a2e0f26ece498))

### [4.12.8](https://github.com/taskforcesh/bullmq/compare/v4.12.7...v4.12.8) (2023-11-03)

#### 버그 수정

* **worker:** worker 종료 중에도 locks 확장 유지 ([#2259](https://github.com/taskforcesh/bullmq/issues/2259)) ([c4d12ea](https://github.com/taskforcesh/bullmq/commit/c4d12ea3a9837ffd7f58e2134796137c4181c3de))

### [4.12.7](https://github.com/taskforcesh/bullmq/compare/v4.12.6...v4.12.7) (2023-10-29)

#### 성능 개선

* **redis-connection:** redis 버전이 v6 이상인지 확인을 한 번만 수행 ([#2252](https://github.com/taskforcesh/bullmq/issues/2252)) ([a09b15a](https://github.com/taskforcesh/bullmq/commit/a09b15af0d5dedfa83bce7130ee9094f3fb69e10))

### [4.12.6](https://github.com/taskforcesh/bullmq/compare/v4.12.5...v4.12.6) (2023-10-26)

#### 버그 수정

* **sandbox:** 값이 undefined일 때 빈 객체 결과를 반환하지 않음 ([#2247](https://github.com/taskforcesh/bullmq/issues/2247)) ([308db7f](https://github.com/taskforcesh/bullmq/commit/308db7f58758a72b8abb272da8e92509813a2178))

### [4.12.5](https://github.com/taskforcesh/bullmq/compare/v4.12.4...v4.12.5) (2023-10-18)

#### 성능 개선

* **events:** 작업 제거 시 events 트림 ([#2235](https://github.com/taskforcesh/bullmq/issues/2235)) (python) ([889815c](https://github.com/taskforcesh/bullmq/commit/889815c412666e5fad8f32d2e3a2d41cf650f001))

### [4.12.4](https://github.com/taskforcesh/bullmq/compare/v4.12.3...v4.12.4) (2023-10-13)

#### 버그 수정

* **events:** 존재하지 않는 작업에 대해 removed 이벤트를 발행하지 않음 ([#2227](https://github.com/taskforcesh/bullmq/issues/2227)) ([c134606](https://github.com/taskforcesh/bullmq/commit/c1346064c6cd9f93c59b184f150eac11d51c91b4))

### [4.12.3](https://github.com/taskforcesh/bullmq/compare/v4.12.2...v4.12.3) (2023-10-10)

#### 버그 수정

* **events:** 작업 재시도 시 events 트림 ([#2224](https://github.com/taskforcesh/bullmq/issues/2224)) ([1986b05](https://github.com/taskforcesh/bullmq/commit/1986b05ac03fe4ee48861aa60caadcc9df8170a6))

### [4.12.2](https://github.com/taskforcesh/bullmq/compare/v4.12.1...v4.12.2) (2023-10-05)

#### 버그 수정

* **sandbox:** job 인스턴스의 progress 값 업데이트 ([#2214](https://github.com/taskforcesh/bullmq/issues/2214)) [#2213](https://github.com/taskforcesh/bullmq/issues/2213) 수정 ([3d0f36a](https://github.com/taskforcesh/bullmq/commit/3d0f36a134b7f5c6b6de26967c9d71bcfb346e72))

### [4.12.1](https://github.com/taskforcesh/bullmq/compare/v4.12.0...v4.12.1) (2023-10-04)

#### 버그 수정

* **delayed:** 작업을 delayed로 이동할 때 events 트림 (python) ([#2211](https://github.com/taskforcesh/bullmq/issues/2211)) ([eca8c2d](https://github.com/taskforcesh/bullmq/commit/eca8c2d4dfeafbd8ac36a49764dbd4897303628c))

## [4.12.0](https://github.com/taskforcesh/bullmq/compare/v4.11.4...v4.12.0) (2023-09-29)

#### 기능

* addJobLog와 updateJobProgress를 Queue 인스턴스에 노출 ([#2202](https://github.com/taskforcesh/bullmq/issues/2202)) ([2056939](https://github.com/taskforcesh/bullmq/commit/205693907a4d6c2da9bd0690fb552b1d1e369c08))

### [4.11.4](https://github.com/taskforcesh/bullmq/compare/v4.11.3...v4.11.4) (2023-09-22)

#### 버그 수정

* **queue:** batched unpack이 이제 range를 사용 ([#2188](https://github.com/taskforcesh/bullmq/issues/2188)) ([b5e97f4](https://github.com/taskforcesh/bullmq/commit/b5e97f420bc0c4bc82772f3e87883ee522be43d9))

### [4.11.3](https://github.com/taskforcesh/bullmq/compare/v4.11.2...v4.11.3) (2023-09-22)

#### 버그 수정

* **worker:** skipVersionCheck를 blockingConnection으로 전달 ([#2189](https://github.com/taskforcesh/bullmq/issues/2189)) ref [#2149](https://github.com/taskforcesh/bullmq/issues/2149) ([c8aa9a3](https://github.com/taskforcesh/bullmq/commit/c8aa9a36224cba8ecb19af1bf652f4f1c4c20d40))

### [4.11.2](https://github.com/taskforcesh/bullmq/compare/v4.11.1...v4.11.2) (2023-09-20)

#### 버그 수정

* **worker:** concurrency가 NaN일 때 예외 발생 ([#2184](https://github.com/taskforcesh/bullmq/issues/2184)) ([f36ac8b](https://github.com/taskforcesh/bullmq/commit/f36ac8b61dcd4bb3d9e283278310cd50cfc83fae))

### [4.11.1](https://github.com/taskforcesh/bullmq/compare/v4.11.0...v4.11.1) (2023-09-20)

#### 버그 수정

* **queue:** clean 메서드에서 상태별 score 목적을 구분 ([#2133](https://github.com/taskforcesh/bullmq/issues/2133)) [#2124](https://github.com/taskforcesh/bullmq/issues/2124) 수정 ([862f10b](https://github.com/taskforcesh/bullmq/commit/862f10b586276314d9bffff2a5e6caf939399f7e))

## [4.11.0](https://github.com/taskforcesh/bullmq/compare/v4.10.0...v4.11.0) (2023-09-16)

#### 기능

* **sandbox:** 확장을 위해 wrapJob 메서드를 protected로 전환 ([#2182](https://github.com/taskforcesh/bullmq/issues/2182)) ([1494b55](https://github.com/taskforcesh/bullmq/commit/1494b5566573356e0248b4a5cab48ae21d82f1da))

## [4.10.0](https://github.com/taskforcesh/bullmq/compare/v4.9.0...v4.10.0) (2023-09-12)

#### 버그 수정

* **move-to-finished:** 마지막 활성 작업을 처리할 때 우선순위 작업 추가를 고려 (python) ([#2176](https://github.com/taskforcesh/bullmq/issues/2176)) ([4b01f35](https://github.com/taskforcesh/bullmq/commit/4b01f359c290cfc62ea74ff3ab0b43ccc6956a02))
* **remove:** 작업이 잠긴 경우 오류 메시지 변경 (python) ([#2175](https://github.com/taskforcesh/bullmq/issues/2175)) ([2f5628f](https://github.com/taskforcesh/bullmq/commit/2f5628feffab66cdcc78abf4d7bb608bdcaa65bb))

## [4.9.0](https://github.com/taskforcesh/bullmq/compare/v4.8.0...v4.9.0) (2023-09-05)

#### 기능

* **connection:** 공유 연결에 대해 skipVersionCheck 옵션 제공 ([#2149](https://github.com/taskforcesh/bullmq/issues/2149)) 참조 [#2148](https://github.com/taskforcesh/bullmq/issues/2148) ([914820f](https://github.com/taskforcesh/bullmq/commit/914820f720cbc48b49f4bd1c46d148eb2bb5b79c))

## [4.8.0](https://github.com/taskforcesh/bullmq/compare/v4.7.4...v4.8.0) (2023-08-20)

#### 기능

* **sandbox:** moveToDelayed 메서드 에뮬레이션 ([#2122](https://github.com/taskforcesh/bullmq/issues/2122)) 참조 [#2118](https://github.com/taskforcesh/bullmq/issues/2118) ([4c4559b](https://github.com/taskforcesh/bullmq/commit/4c4559b3c678313b3727c9781a6d3f963bcfda4e))

### [4.7.4](https://github.com/taskforcesh/bullmq/compare/v4.7.3...v4.7.4) (2023-08-19)

#### 버그 수정

* **sandbox:** processor에서 추가 파라미터 무시 ([#2142](https://github.com/taskforcesh/bullmq/issues/2142)) ([3602c20](https://github.com/taskforcesh/bullmq/commit/3602c20ab80cbe0a0d3de66210a01ad119e1090b))

### [4.7.3](https://github.com/taskforcesh/bullmq/compare/v4.7.2...v4.7.3) (2023-08-17)

#### 버그 수정

* **worker:** worker 종료 시 rate-limit 지연 중단 ([264a81c](https://github.com/taskforcesh/bullmq/commit/264a81ca5f4e4f88c361d507312324b5f6c3225c))

### [4.7.2](https://github.com/taskforcesh/bullmq/compare/v4.7.1...v4.7.2) (2023-08-12)

#### 버그 수정

* **queue:** name이 제공되지 않으면 오류 발생 ([#2123](https://github.com/taskforcesh/bullmq/issues/2123)) ([78fb0e2](https://github.com/taskforcesh/bullmq/commit/78fb0e2a93cfa59a43a0fb337f857e78f1c6fcf4))

### [4.7.1](https://github.com/taskforcesh/bullmq/compare/v4.7.0...v4.7.1) (2023-08-10)

#### 성능 개선

* **rate-limit:** 필요할 때만 pttl 조회 ([#2129](https://github.com/taskforcesh/bullmq/issues/2129)) ([12ce2f3](https://github.com/taskforcesh/bullmq/commit/12ce2f3746626a81ea961961bb1a629077eed68a))

## [4.7.0](https://github.com/taskforcesh/bullmq/compare/v4.6.3...v4.7.0) (2023-08-03)

#### 기능

* **queue:** getRateLimitTtl 메서드 추가 ([#2105](https://github.com/taskforcesh/bullmq/issues/2105)) ([7426c64](https://github.com/taskforcesh/bullmq/commit/7426c64b109f1beacf742d57a987282597385469))

### [4.6.3](https://github.com/taskforcesh/bullmq/compare/v4.6.2...v4.6.3) (2023-07-28)

#### 성능 개선

* **job:** priority limit 상수를 한 번만 생성 ([#2102](https://github.com/taskforcesh/bullmq/issues/2102)) ([8880f9f](https://github.com/taskforcesh/bullmq/commit/8880f9f2983282d343d603a89abe5e1e6bff78e5))

### [4.6.2](https://github.com/taskforcesh/bullmq/compare/v4.6.0...v4.6.2) (2023-07-26)

#### 성능 개선

* **retry:** regex 표현식 대신 이전 상태를 비교 ([#2099](https://github.com/taskforcesh/bullmq/issues/2099)) ([c141283](https://github.com/taskforcesh/bullmq/commit/c1412831903d1fae0955af097e0be049024839fe))

## [4.6.0](https://github.com/taskforcesh/bullmq/compare/v4.5.0...v4.6.0) (2023-07-19)

#### 기능

* **queue:** 모든 지연 작업을 승격하는 promoteJobs 추가 ([6074592](https://github.com/taskforcesh/bullmq/commit/6074592574256ec4b1c340126288e803e56b1a64))

## [4.5.0](https://github.com/taskforcesh/bullmq/compare/v4.4.0...v4.5.0) (2023-07-18)

#### 기능

* **job:** remove 메서드에 하위 작업 제거 옵션 추가 (python) ([#2064](https://github.com/taskforcesh/bullmq/issues/2064)) ([841dc87](https://github.com/taskforcesh/bullmq/commit/841dc87a689897df81438ad1f43e45a4da77c388))

## [4.4.0](https://github.com/taskforcesh/bullmq/compare/v4.3.0...v4.4.0) (2023-07-17)

#### 기능

* **job:** removeDependencyOnFailure 옵션 추가 ([#1953](https://github.com/taskforcesh/bullmq/issues/1953)) ([ffd49e2](https://github.com/taskforcesh/bullmq/commit/ffd49e289c57252487200d47b92193228ae7451f))

## [4.3.0](https://github.com/taskforcesh/bullmq/compare/v4.2.1...v4.3.0) (2023-07-14)

#### 기능

* **worker:** 토큰의 일부로 id 추가 ([#2061](https://github.com/taskforcesh/bullmq/issues/2061)) ([e255356](https://github.com/taskforcesh/bullmq/commit/e2553562271e1e4143a8fef616349bb30de4899d))

### [4.2.1](https://github.com/taskforcesh/bullmq/compare/v4.2.0...v4.2.1) (2023-07-10)

#### 버그 수정

* **flow:** 부모가 delayed로 이동될 때 delayed 이벤트 발생 ([#2055](https://github.com/taskforcesh/bullmq/issues/2055)) ([f419ff1](https://github.com/taskforcesh/bullmq/commit/f419ff1ec5cb34986fe4b79402c727a6487e949c))

## [4.2.0](https://github.com/taskforcesh/bullmq/compare/v4.1.0...v4.2.0) (2023-07-03)

#### 기능

* **common:** 반복 작업 redis 키 해시 알고리즘을 변경하는 옵션 추가 ([#2023](https://github.com/taskforcesh/bullmq/issues/2023)) ([ca17364](https://github.com/taskforcesh/bullmq/commit/ca17364cc2a52f6577fb66f09ec3168bbf9f1e07))

## [4.1.0](https://github.com/taskforcesh/bullmq/compare/v4.0.0...v4.1.0) (2023-06-23)

#### 기능

* **queue:** getPrioritized 및 getPrioritizedCount 메서드 추가 ([#2005](https://github.com/taskforcesh/bullmq/issues/2005)) ([7363abe](https://github.com/taskforcesh/bullmq/commit/7363abebce6e3bcf067fc7c220d845807ebb1489))

## [4.0.0](https://github.com/taskforcesh/bullmq/compare/v3.15.8...v4.0.0) (2023-06-21)

#### 기능

* **queue:** removeDeprecatedPriorityKey 메서드 추가

#### 성능 개선

* **priority:** prioritized를 새로운 상태로 추가 ([#1984](https://github.com/taskforcesh/bullmq/issues/1984)) (python) ([42a890a](https://github.com/taskforcesh/bullmq/commit/42a890a2bfe45b29348030f886766400f5d41aa3))

#### 주요 변경 사항

* **priority:** priority가 자체 zset으로 분리되어 중복이 더 이상 필요하지 않음
* **job:** job 메서드 이름 update를 updateData로 변경

참조 [faster priority jobs](https://bullmq.io/news/062123/faster-priority-jobs/)

