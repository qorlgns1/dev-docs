---
title: '[2.7.1](https://github.com/taskforcesh/bullmq-pro/compare/v2.7.0...v2.7.1) (2022-10-13)'
---

소스 URL: https://docs.bullmq.io/bullmq-pro/changelog/changelog-v2

# v2

### [2.7.1](https://github.com/taskforcesh/bullmq-pro/compare/v2.7.0...v2.7.1) (2022-10-13)

#### 버그 수정

* **delete-groups:** rate-limit, 최대 동시성, 일시 중지 상태를 고려 ([#104](https://github.com/taskforcesh/bullmq-pro/issues/104)) ([29873f8](https://github.com/taskforcesh/bullmq-pro/commit/29873f8c900025f70cd88f8328fa8c6b3841bc7b))

## [2.7.0](https://github.com/taskforcesh/bullmq-pro/compare/v2.6.0...v2.7.0) (2022-10-11)

#### 기능

* getGroupStatus 추가 ([a7cd882](https://github.com/taskforcesh/bullmq-pro/commit/a7cd882f80b182612a19924823000cec15d2cf90))

## [2.6.0](https://github.com/taskforcesh/bullmq-pro/compare/v2.5.0...v2.6.0) (2022-10-11)

#### 기능

* 버전 지원 추가 ([b7e1831](https://github.com/taskforcesh/bullmq-pro/commit/b7e183116137d8774a12d09a4d97d29d1cdb2999))

## [2.5.0](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.14...v2.5.0) (2022-10-11)

#### 기능

* getters에 getGroupsByStatus 메서드 추가 ([949e93b](https://github.com/taskforcesh/bullmq-pro/commit/949e93bc3478607f95ee59eab41a1ac7e271e74d))

### [2.4.14](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.13...v2.4.14) (2022-10-07)

#### 버그 수정

* **delete-group:** max-concurrency 상태를 고려 ([#98](https://github.com/taskforcesh/bullmq-pro/issues/98)) ([d897dd9](https://github.com/taskforcesh/bullmq-pro/commit/d897dd9bef0f6844d9752bfb3c22f0be6368889b))

### [2.4.13](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.12...v2.4.13) (2022-10-05)

#### 버그 수정

* **delete-group:** rate-limit 상태를 고려 ([#97](https://github.com/taskforcesh/bullmq-pro/issues/97)) ([85f7f32](https://github.com/taskforcesh/bullmq-pro/commit/85f7f32a0c2e893f7921c8eee9bc0655fdff7a39))

### [2.4.12](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.11...v2.4.12) (2022-09-30)

#### 버그 수정

* **global-rate-limit:** 그룹을 고려 ([#95](https://github.com/taskforcesh/bullmq-pro/issues/95)) ([de95fde](https://github.com/taskforcesh/bullmq-pro/commit/de95fde1f07096f6d2dfff278b1d969a5b2a0c0f))

### [2.4.11](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.10...v2.4.11) (2022-09-29)

#### 버그 수정

* **drain:** 비어 있는 active 목록을 고려 ([#1412](https://github.com/taskforcesh/bullmq/issues/1412)) ([f919a50](https://github.com/taskforcesh/bullmq/commit/f919a50b2f4972dcb9ecd5848b0f7fd9a0e137ea))

#### 기능

* **sandbox:** update 메서드 지원 ([#1416](https://github.com/taskforcesh/bullmq/issues/1416)) ([606b75d](https://github.com/taskforcesh/bullmq/commit/606b75d53e12dfc109f01eda38736c07e829e9b7))

### [2.4.10](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.9...v2.4.10) (2022-09-14)

#### 버그 수정

* **timeout:** 사용되지 않는 옵션 삭제 ([#94](https://github.com/taskforcesh/bullmq-pro/issues/94)) ([4f8dc50](https://github.com/taskforcesh/bullmq-pro/commit/4f8dc5021c311fe10d20568c4dae4055d01ef98f))

### [2.4.9](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.8...v2.4.9) (2022-09-13)

#### 성능 개선

* **script-loader:** 캐시를 사용해 스크립트를 한 번만 읽도록 변경 ([#93](https://github.com/taskforcesh/bullmq-pro/issues/93)) ([04bbeec](https://github.com/taskforcesh/bullmq-pro/commit/04bbeece1dfc8e06d8590eb486879593d4dae437))

### [2.4.8](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.7...v2.4.8) (2022-09-09)

#### 버그 수정

* **concurrency:** 기본 rate limit을 고려 ([#90](https://github.com/taskforcesh/bullmq-pro/issues/90)) ([74a4a0b](https://github.com/taskforcesh/bullmq-pro/commit/74a4a0ba01f3a447f9dc24f5bbb898bc6afaeaa6))

### [2.4.7](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.6...v2.4.7) (2022-09-06)

#### 버그 수정

* **flow-producer-pro:** interim 클래스 사용 ([#92](https://github.com/taskforcesh/bullmq-pro/issues/92)) ([2406cc3](https://github.com/taskforcesh/bullmq-pro/commit/2406cc3f1b4c78feed8a4fbd91422e3ca1970b19))

### [2.4.6](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.5...v2.4.6) (2022-09-06)

#### 성능 개선

* **add-job:** js에서 parent split 처리 ([#1397](https://github.com/taskforcesh/bullmq/issues/1397)) ([566f074](https://github.com/taskforcesh/bullmq/commit/566f0747110679e5b07e7642fef793744565fffe))

### [2.4.5](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.4...v2.4.5) (2022-08-30)

#### 버그 수정

* **delete-group:** children을 고려 ([#88](https://github.com/taskforcesh/bullmq-pro/issues/88)) ([83de2a9](https://github.com/taskforcesh/bullmq-pro/commit/83de2a9c9b42775996a8c8893caf66d1af6bea15))

### [2.4.4](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.3...v2.4.4) (2022-08-30)

#### 버그 수정

* **deps:** bullmq를 1.90.0으로 업그레이드 ([#84](https://github.com/taskforcesh/bullmq-pro/issues/84)) ([69a01c5](https://github.com/taskforcesh/bullmq-pro/commit/69a01c5d91c3e6ad2b1fb7a32ced8a04021d91ec))

### [2.4.3](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.2...v2.4.3) (2022-08-26)

#### 버그 수정

* **waiting-children:** 그룹 동시성 감소를 고려 ([#86](https://github.com/taskforcesh/bullmq-pro/issues/86)) ([be430a7](https://github.com/taskforcesh/bullmq-pro/commit/be430a72f7bda55e22a0ae5e5623e8a2b835e98e))

### [2.4.2](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.1...v2.4.2) (2022-08-25)

#### 버그 수정

* **deps:** bullmq를 1.89.1로 업그레이드 ([#87](https://github.com/taskforcesh/bullmq-pro/issues/87)) ([228aca3](https://github.com/taskforcesh/bullmq-pro/commit/228aca3e72ef9401fe3c67e5ca72be6b1068b6c6))

### [2.4.1](https://github.com/taskforcesh/bullmq-pro/compare/v2.4.0...v2.4.1) (2022-08-18)

#### 버그 수정

* **job:** 그룹에서 제거 ([#57](https://github.com/taskforcesh/bullmq-pro/issues/57)) ([7c38aa1](https://github.com/taskforcesh/bullmq-pro/commit/7c38aa19ea9aba53689e14208892ab7f6547b699))

## [2.4.0](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.13...v2.4.0) (2022-08-16)

#### 기능

* **groups:** flows 지원 ([#81](https://github.com/taskforcesh/bullmq-pro/issues/81)) ([3db9478](https://github.com/taskforcesh/bullmq-pro/commit/3db947863093c7c7db83773876dd7593b5a33210))

### [2.3.13](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.12...v2.3.13) (2022-08-13)

#### 버그 수정

* **deps:** bullmq를 1.87.2로 업그레이드 ([#83](https://github.com/taskforcesh/bullmq-pro/issues/83)) ([5b3c866](https://github.com/taskforcesh/bullmq-pro/commit/5b3c866016837bdafa93bc315d31d9eee2465ed5))

### [2.3.12](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.11...v2.3.12) (2022-08-11)

#### 버그 수정

* **observables:** 저장 결과 순서를 보장 ([f963557](https://github.com/taskforcesh/bullmq-pro/commit/f9635571ae359cdf6de9cd18463ef879c166a4f4))
* **observables:** 마지막 값을 returnvalue로 저장 ([7306ae2](https://github.com/taskforcesh/bullmq-pro/commit/7306ae233b5a2ecb96d402a30d7db61bb8c74567))

### [2.3.11](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.10...v2.3.11) (2022-08-09)

#### 버그 수정

* **deps:** bullmq를 1.87.1로 업그레이드 ([#79](https://github.com/taskforcesh/bullmq-pro/issues/79)) ([3affc37](https://github.com/taskforcesh/bullmq-pro/commit/3affc37ab682f1d58c0dfa29d3db714c8e7f8c91))

### [2.3.10](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.9...v2.3.10) (2022-08-03)

#### 성능 개선

* **move-to-finished:** keepJobs를 opts 인자로 전달 ([#78](https://github.com/taskforcesh/bullmq-pro/issues/78)) ([08eb23f](https://github.com/taskforcesh/bullmq-pro/commit/08eb23fa54bfe1e46c1e79bfee9d72fb0dbba52b))

### [2.3.9](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.8...v2.3.9) (2022-08-01)

#### 버그 수정

* **deps:** bullmq를 1.86.10으로 업그레이드 ([#76](https://github.com/taskforcesh/bullmq-pro/issues/76)) ([d3df585](https://github.com/taskforcesh/bullmq-pro/commit/d3df5850fd92b6d98e77c6d7e7355f205f7df4c4))

### [2.3.8](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.7...v2.3.8) (2022-08-01)

#### 버그 수정

* **move-to-active:** 전역 참조 대신 로컬 jobId 사용 ([#77](https://github.com/taskforcesh/bullmq-pro/issues/77)) ([1f0b8dd](https://github.com/taskforcesh/bullmq-pro/commit/1f0b8dd747ce9ad9fdacdb7774cb1f34e989ceb5))

### [2.3.7](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.6...v2.3.7) (2022-07-28)

#### 버그 수정

* **deps:** bullmq를 1.86.9로 업그레이드 ([#73](https://github.com/taskforcesh/bullmq-pro/issues/73)) ([bbc0784](https://github.com/taskforcesh/bullmq-pro/commit/bbc07845f6cce0cc003681255b892330c729b30e))

### [2.3.6](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.5...v2.3.6) (2022-07-26)

#### 성능 개선

* **retry-jobs:** groupId가 있을 때 배치로 작업 추가 ([#72](https://github.com/taskforcesh/bullmq-pro/issues/72)) ([3961da0](https://github.com/taskforcesh/bullmq-pro/commit/3961da022843048597033e8f13034f245198bca3))

### [2.3.5](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.4...v2.3.5) (2022-07-20)

#### 버그 수정

* **retry-jobs:** 그룹을 고려 ([#70](https://github.com/taskforcesh/bullmq-pro/issues/70)) ([7b03017](https://github.com/taskforcesh/bullmq-pro/commit/7b030179d1a2de23aba2f9c5e71b5d13d6de67d3))

### [2.3.4](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.3...v2.3.4) (2022-07-16)

#### 버그 수정

* **scripts:** timestamp 인자에 tonumber 사용 ([#71](https://github.com/taskforcesh/bullmq-pro/issues/71)) ([5c6a62d](https://github.com/taskforcesh/bullmq-pro/commit/5c6a62de4d7df43343cca58f53ef39201c2aa6d1))

### [2.3.3](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.2...v2.3.3) (2022-07-12)

#### 버그 수정

* **deps:** bullmq를 1.86.5로 업그레이드 ([#69](https://github.com/taskforcesh/bullmq-pro/issues/69)) ([2ed4bf3](https://github.com/taskforcesh/bullmq-pro/commit/2ed4bf36a1a0245e0303a8bc5fe120dbf84d8e1d))

### [2.3.2](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.1...v2.3.2) (2022-07-09)

#### 버그 수정

* **concurrency:** retry backoff 전략을 고려 ([#68](https://github.com/taskforcesh/bullmq-pro/issues/68)) ([99f17bd](https://github.com/taskforcesh/bullmq-pro/commit/99f17bdd085ef1376bb1f35e2c679ab04e3a2d03))

### [2.3.1](https://github.com/taskforcesh/bullmq-pro/compare/v2.3.0...v2.3.1) (2022-07-01)

#### 버그 수정

* **job-pro:** gid 파싱 수정 ([#67](https://github.com/taskforcesh/bullmq-pro/issues/67)) ([5532eaf](https://github.com/taskforcesh/bullmq-pro/commit/5532eaf5d61790a9bf63604838c2c3cd5546697e))

## [2.3.0](https://github.com/taskforcesh/bullmq-pro/compare/v2.2.3...v2.3.0) (2022-07-01)

#### 기능

* **job-pro:** gid 값 노출 ([#65](https://github.com/taskforcesh/bullmq-pro/issues/65)) ([ea7ab29](https://github.com/taskforcesh/bullmq-pro/commit/ea7ab29d7d15c42fba6823de53c243c0eb20d2fa))

### [2.2.3](https://github.com/taskforcesh/bullmq-pro/compare/v2.2.2...v2.2.3) (2022-06-30)

#### 버그 수정

* **queue-pro:** addBulk opts 타이핑 수정 ([#66](https://github.com/taskforcesh/bullmq-pro/issues/66)) ([8b73ed9](https://github.com/taskforcesh/bullmq-pro/commit/8b73ed9b807375f1a18a62feef26c48c9b324fe8))

### [2.2.2](https://github.com/taskforcesh/bullmq-pro/compare/v2.2.1...v2.2.2) (2022-06-28)

#### 버그 수정

* **pause-group:** 실행 성공 여부를 boolean으로 반환 ([#64](https://github.com/taskforcesh/bullmq-pro/issues/64)) ([b665b82](https://github.com/taskforcesh/bullmq-pro/commit/b665b828ba950411567f3424f0e8a1f80467021b))

### [2.2.1](https://github.com/taskforcesh/bullmq-pro/compare/v2.2.0...v2.2.1) (2022-06-25)

#### 버그 수정

* **groups:** QueueEventsPro에서 paused 및 resumed 이벤트 이름 변경 ([#63](https://github.com/taskforcesh/bullmq-pro/issues/63)) ([e2d6abf](https://github.com/taskforcesh/bullmq-pro/commit/e2d6abff3d59a8417896f7405ffcab35f2a780f3))

## [2.2.0](https://github.com/taskforcesh/bullmq-pro/compare/v2.1.6...v2.2.0) (2022-06-24)

#### 기능

* **pause-group:** 특정 group을 일시 중지할 수 있도록 허용 ([#61](https://github.com/taskforcesh/bullmq-pro/issues/61)) ref [#25](https://github.com/taskforcesh/bullmq-pro/issues/25) ([a5ec201](https://github.com/taskforcesh/bullmq-pro/commit/a5ec2018935241b01be1c38323e6d1e31fffe89f))

### [2.1.6](https://github.com/taskforcesh/bullmq-pro/compare/v2.1.5...v2.1.6) (2022-06-10)

#### 버그 수정

* **deps:** bullmq를 1.86.0으로 업그레이드 ([#60](https://github.com/taskforcesh/bullmq-pro/issues/60)) ([ea07b00](https://github.com/taskforcesh/bullmq-pro/commit/ea07b0090e21efabfe25f65d277856eaab0d8fc5))

### [2.1.5](https://github.com/taskforcesh/bullmq-pro/compare/v2.1.4...v2.1.5) (2022-06-09)

#### 버그 수정

* **deps:** bullmq를 1.85.4로 업그레이드 ([#59](https://github.com/taskforcesh/bullmq-pro/issues/59)) ([b45b363](https://github.com/taskforcesh/bullmq-pro/commit/b45b36369909a7db9fa01968065af0ff9ad2cafd))

### [2.1.4](https://github.com/taskforcesh/bullmq-pro/compare/v2.1.3...v2.1.4) (2022-06-08)

#### 버그 수정

* **worker:** isObservable 사용 ([#58](https://github.com/taskforcesh/bullmq-pro/issues/58)) ([8bed7ce](https://github.com/taskforcesh/bullmq-pro/commit/8bed7ce5a933c0126abd441488180fb5036eb3f1))

### [2.1.3](https://github.com/taskforcesh/bullmq-pro/compare/v2.1.2...v2.1.3) (2022-05-25)

#### 버그 수정

* **deps:** bullmq를 1.83.2로 업그레이드 ([#56](https://github.com/taskforcesh/bullmq-pro/issues/56)) ([a98c917](https://github.com/taskforcesh/bullmq-pro/commit/a98c9177bbb526692a22b9407d0f0374db7ee8d2))

### [2.1.2](https://github.com/taskforcesh/bullmq-pro/compare/v2.1.1...v2.1.2) (2022-05-20)

#### 버그 수정

* **deps:** bullmq를 1.83.0으로 업그레이드 ([#55](https://github.com/taskforcesh/bullmq-pro/issues/55)) ([dc3b02d](https://github.com/taskforcesh/bullmq-pro/commit/dc3b02d28b583862ea2fab2e6557d5d35ff811e6))

### [2.1.1](https://github.com/taskforcesh/bullmq-pro/compare/v2.1.0...v2.1.1) (2022-05-18)

#### 버그 수정

* **flow-producer:** JobPro 인스턴스 사용 ([#54](https://github.com/taskforcesh/bullmq-pro/issues/54)) ([578d3db](https://github.com/taskforcesh/bullmq-pro/commit/578d3db5941752b72d1925a1026e013a590d55d5))

## [2.1.0](https://github.com/taskforcesh/bullmq-pro/compare/v2.0.3...v2.1.0) (2022-05-17)

#### 기능

* **get-state:** groups 검사 고려 ([#53](https://github.com/taskforcesh/bullmq-pro/issues/53)) ([1dad072](https://github.com/taskforcesh/bullmq-pro/commit/1dad072cad84b3b18219bd8c0caf883c2b5179fc))

### [2.0.3](https://github.com/taskforcesh/bullmq-pro/compare/v2.0.2...v2.0.3) (2022-05-07)

#### 버그 수정

* **deps:** bullmq를 1.81.4로 업그레이드 ([#52](https://github.com/taskforcesh/bullmq-pro/issues/52)) ([8d92b21](https://github.com/taskforcesh/bullmq-pro/commit/8d92b21571a1263a3be097bf7e1c7d7f60c06816))

### [2.0.2](https://github.com/taskforcesh/bullmq-pro/compare/v2.0.1...v2.0.2) (2022-04-27)

#### 버그 수정

* **stalled:** stalled 변경 사항에 대한 쉬운 전환 허용 ([#50](https://github.com/taskforcesh/bullmq-pro/issues/50)) ([ce40ead](https://github.com/taskforcesh/bullmq-pro/commit/ce40ead2c26bffbc80d3953ed80a63bceedbb73b))

### [2.0.1](https://github.com/taskforcesh/bullmq-pro/compare/v2.0.0...v2.0.1) (2022-04-22)

#### 버그 수정

* **deps:** bullmq를 1.80.6으로 업그레이드 ([#48](https://github.com/taskforcesh/bullmq-pro/issues/48)) ([4aed9b0](https://github.com/taskforcesh/bullmq-pro/commit/4aed9b0c11d77b96f0859ff6b1b32e4b7c95249d))

## [2.0.0](https://github.com/taskforcesh/bullmq-pro/compare/v1.4.1...v2.0.0) (2022-04-20)

#### 기능

* **groups:** addGroups가 모든 group 상태를 반환하도록 개선 ([3f01d66](https://github.com/taskforcesh/bullmq-pro/commit/3f01d66fee33965a68de634e6771ab9da158a0e1))

#### 호환성 깨지는 변경 사항

* **groups:** 모든 상태에서 group getter를 일관되게 만들기 위해 groups:active의 SET 타입을 ZSET으로 변경합니다. 또한 동시성 한도에 도달한 group을 나타내므로 ZSET 이름을 groups:max으로 변경합니다.

