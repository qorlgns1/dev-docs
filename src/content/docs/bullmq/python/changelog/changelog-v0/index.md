---
title: '[0.5.6](https://github.com/taskforcesh/bullmq/compare/vpy0.5.5...vpy0.5.6) (2023-06-21)'
description: '원본 URL: https://docs.bullmq.io/python/changelog/changelog-v0'
---

원본 URL: https://docs.bullmq.io/python/changelog/changelog-v0

# v0

### [0.5.6](https://github.com/taskforcesh/bullmq/compare/vpy0.5.5...vpy0.5.6) (2023-06-21)

#### 버그 수정

* **queue:** trimEvents method에 올바른 params 전달 ([#2004](https://github.com/taskforcesh/bullmq/issues/2004)) ([a55fd77](https://github.com/taskforcesh/bullmq/commit/a55fd777655f7d4bb7af9e4fa2f7b4f48f559189))

### [0.5.5](https://github.com/taskforcesh/bullmq/compare/vpy0.5.4...vpy0.5.5) (2023-06-16)

#### 버그 수정

* **rate-limit:** priority fifo 순서 유지 ([#1991](https://github.com/taskforcesh/bullmq/issues/1991)) [#1929](https://github.com/taskforcesh/bullmq/issues/1929) 수정 (python) ([56bd7ad](https://github.com/taskforcesh/bullmq/commit/56bd7ad8c4daffcfb1f9f199abfc5d6495eb291e))
* **worker:** initialization 시 redis version을 항상 설정 ([#1989](https://github.com/taskforcesh/bullmq/issues/1989)) [#1988](https://github.com/taskforcesh/bullmq/issues/1988) 수정 ([a1544a8](https://github.com/taskforcesh/bullmq/commit/a1544a8c0f29522cd33772b14f559969db852d1d))

### [0.5.4](https://github.com/taskforcesh/bullmq/compare/vpy0.5.3...vpy0.5.4) (2023-06-14)

#### 버그 수정

* **connection:** connection에 retry strategy 추가 ([#1975](https://github.com/taskforcesh/bullmq/issues/1975)) ([7c5ee20](https://github.com/taskforcesh/bullmq/commit/7c5ee20471b989d297c8c5e87a6ea497a2077ae6))

### [0.5.3](https://github.com/taskforcesh/bullmq/compare/vpy0.5.2...vpy0.5.3) (2023-06-13)

#### 버그 수정

* **worker:** redis v6.0.0 미만에서는 timeout을 integer로 사용 (python) ([#1981](https://github.com/taskforcesh/bullmq/issues/1981)) ([0df6afa](https://github.com/taskforcesh/bullmq/commit/0df6afad5e71a693b721ba52ffa6be733ee45ccb))

### [0.5.2](https://github.com/taskforcesh/bullmq/compare/vpy0.5.1...vpy0.5.2) (2023-06-11)

#### 버그 수정

* **retry-job:** job을 wait로 이동할 때 priority 고려 (python) ([#1969](https://github.com/taskforcesh/bullmq/issues/1969)) ([e753855](https://github.com/taskforcesh/bullmq/commit/e753855eef248da73a5e9f6b18f4b79319dc2f86))

### [0.5.1](https://github.com/taskforcesh/bullmq/compare/vpy0.5.0...vpy0.5.1) (2023-06-09)

#### 버그 수정

* **python:** release 시 lua scripts 포함 ([bb4f3b2](https://github.com/taskforcesh/bullmq/commit/bb4f3b2be8e3d5a54a87f0f5d6ba8dfa09900e53))

## [0.5.0](https://github.com/taskforcesh/bullmq/compare/vpy0.4.4...vpy0.5.0) (2023-06-09)

#### 기능

* **python:** remove job method 추가 ([#1965](https://github.com/taskforcesh/bullmq/issues/1965)) ([6a172e9](https://github.com/taskforcesh/bullmq/commit/6a172e97e65684f65ee570c2ae9bcc108720d5df))

### [0.4.4](https://github.com/taskforcesh/bullmq/compare/vpy0.4.3...vpy0.4.4) (2023-06-08)

#### 버그 수정

* **deps:** version 이슈를 피하기 위해 python-semantic-release 다운그레이드

### [0.4.3](https://github.com/taskforcesh/bullmq/compare/vpy0.4.2...vpy0.4.3) (2023-06-07)

#### 버그 수정

* **rate-limit:** paused queue 고려 ([#1931](https://github.com/taskforcesh/bullmq/issues/1931)) ([d97864a](https://github.com/taskforcesh/bullmq/commit/d97864a550992aeb8673557c7d8f186ab4ccb5bf))

#### 기능

* **job:** changePriority method 추가 ([#1943](https://github.com/taskforcesh/bullmq/issues/1943)) ([945bcd3](https://github.com/taskforcesh/bullmq/commit/945bcd39db0f76ef6e9a513304714c120317c7f3))

### [0.4.2](https://github.com/taskforcesh/bullmq/compare/vpy0.4.1...vpy0.4.2) (2023-06-01)

#### 버그 수정

* **deps:** semver를 포함하도록 'install\_requires' 수정 ([#1927](https://github.com/taskforcesh/bullmq/issues/1927)) ([ce86ece](https://github.com/taskforcesh/bullmq/commit/ce86eceed40283b5d3276968b65ceae31ce425bb))

### [0.4.1](https://github.com/taskforcesh/bullmq/compare/vpy0.4.0...vpy0.4.1) (2023-05-29)

#### 기능

* **job:** getState method 추가 ([#1906](https://github.com/taskforcesh/bullmq/issues/1906)) ([f0867a6](https://github.com/taskforcesh/bullmq/commit/f0867a679c75555fa764078481252110c1e7377f))

## [0.4.0](https://github.com/taskforcesh/bullmq/compare/vpy0.3.0...vpy0.4.0) (2023-05-18)

#### 버그 수정

* **retry:** queue가 paused 상태일 때를 고려 ([#1880](https://github.com/taskforcesh/bullmq/issues/1880)) ([01b621f](https://github.com/taskforcesh/bullmq/commit/01b621fea0cbdae602482ff61361c05646823223))
* **worker:** force stop 시 processes 중지 ([#1837](https://github.com/taskforcesh/bullmq/issues/1837)) ([514699c](https://github.com/taskforcesh/bullmq/commit/514699cd8be96db2320bf0f85d4b6593809a09f1))

#### 기능

* **connection:** redis options를 string으로 허용 ([01f549e](https://github.com/taskforcesh/bullmq/commit/01f549e62a33619a7816758910a2d2b5ac75b589))
* **job:** moveToDelayed job method 추가 ([#1849](https://github.com/taskforcesh/bullmq/issues/1849)) ([5bebf8d](https://github.com/taskforcesh/bullmq/commit/5bebf8d6560de78448b0413baaabd26f7227575c))
* **job:** job에 retry method 추가 ([#1877](https://github.com/taskforcesh/bullmq/issues/1877)) ([870da45](https://github.com/taskforcesh/bullmq/commit/870da459f419076f03885a12a4ce5a2930c500f3))
* **job:** updateData method 추가 ([#1871](https://github.com/taskforcesh/bullmq/issues/1871)) ([800b8c4](https://github.com/taskforcesh/bullmq/commit/800b8c46e709a8cbc4674d84bd59d5c62251d271))
* **job:** job class에 updateProgress method 추가([#1830](https://github.com/taskforcesh/bullmq/issues/1830)) ([e1e1aa2](https://github.com/taskforcesh/bullmq/commit/e1e1aa2e7a41e5418a5a50af4cea347a38bbc7d1))
* **job:** job 실패 시 stacktrace 저장 ([#1859](https://github.com/taskforcesh/bullmq/issues/1859)) ([0b538ce](https://github.com/taskforcesh/bullmq/commit/0b538cedf63c3f006838ee3d016e463ee3492f81))
* retryJob logic 지원 ([#1869](https://github.com/taskforcesh/bullmq/issues/1869)) ([b044a03](https://github.com/taskforcesh/bullmq/commit/b044a03159bc3a8d8823c71019f64825f318a6c2))

## [0.3.0](https://github.com/taskforcesh/bullmq/compare/vpy0.2.0...vpy0.3.0) (2023-04-18)

#### 버그 수정

* worker가 job 처리를 무기한 계속하도록 조건 수정 ([#1800](https://github.com/taskforcesh/bullmq/issues/1800)) ([ef0c5d6](https://github.com/taskforcesh/bullmq/commit/ef0c5d6cae1dcbae607fa02da32d5236069f2339))
* array2obj function의 scripts typing 수정 ([#1786](https://github.com/taskforcesh/bullmq/issues/1786)) ([134f6ab](https://github.com/taskforcesh/bullmq/commit/134f6ab5f3219ddd7a421e61ace6bac72bb51e6d))
* maxMetricsSize가 제공되지 않은 경우 빈 문자열로 전달하도록 수정 fixes ([#1754](https://github.com/taskforcesh/bullmq/issues/1754)) ([6bda2b2](https://github.com/taskforcesh/bullmq/commit/6bda2b24be38a78e5fcfc71ed2913f0150a41dfc))

#### 기능

* **queue:** getJobCounts method 추가 ([#1807](https://github.com/taskforcesh/bullmq/issues/1807)) ([46d6f94](https://github.com/taskforcesh/bullmq/commit/46d6f94575454fe2a32be0c5247f16d18739fe27))
* worker concurrency 개선 ([#1809](https://github.com/taskforcesh/bullmq/issues/1809)) ([ec7c49e](https://github.com/taskforcesh/bullmq/commit/ec7c49e284fd1ecdd52b96197281247f5222ea34))

## [0.2.0](https://github.com/taskforcesh/bullmq/compare/vpy0.1.0...vpy0.2.0) (2023-03-29)

#### 기능

* trimEvents method 추가 ([#1695](https://github.com/taskforcesh/bullmq/issues/1695)) ([ca48163](https://github.com/taskforcesh/bullmq/commit/ca48163263b12a85533563485176c684e548df0b))
* **queue:** retryJobs method 추가 ([#1688](https://github.com/taskforcesh/bullmq/issues/1688)) ([2745327](https://github.com/taskforcesh/bullmq/commit/2745327c7a7080f72e8c265bae77429e597cb6d3))

## 0.1.0 (2023-02-15)

#### 기능

* 초기 python package ([a97b22f](https://github.com/taskforcesh/bullmq/commit/a97b22f518a9f6c5d9c30a77bfd03cafdcbc57ff))

