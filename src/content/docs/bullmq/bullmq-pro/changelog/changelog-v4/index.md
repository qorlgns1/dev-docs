---
title: '[4.0.3](https://github.com/taskforcesh/bullmq-pro/compare/v4.0.2...v4.0.3) (2022-11-19)'
---

Source URL: https://docs.bullmq.io/bullmq-pro/changelog/changelog-v4

# v4

### [4.0.3](https://github.com/taskforcesh/bullmq-pro/compare/v4.0.2...v4.0.3) (2022-11-19)

#### 버그 수정

* **stalled:** type 결과를 테이블로 사용 ([#113](https://github.com/taskforcesh/bullmq-pro/issues/113)) ([0507801](https://github.com/taskforcesh/bullmq-pro/commit/05078015f0ed687d8151780bb102a43d7da642ca))

### [4.0.2](https://github.com/taskforcesh/bullmq-pro/compare/v4.0.1...v4.0.2) (2022-11-08)

#### 버그 수정

* **promote:** 그룹 고려 ([#109](https://github.com/taskforcesh/bullmq-pro/issues/109)) ([c46c67b](https://github.com/taskforcesh/bullmq-pro/commit/c46c67b785fe521e5742582460c960bc16fd5c60))

### [4.0.1](https://github.com/taskforcesh/bullmq-pro/compare/v4.0.0...v4.0.1) (2022-11-07)

#### 기능

* **flows:** addBulk 메서드에서 루트 작업에 parent 허용 ([#1488](https://github.com/taskforcesh/bullmq/issues/1488)) ref [#1480](https://github.com/taskforcesh/bullmq/issues/1480) ([92308e5](https://github.com/taskforcesh/bullmq/commit/92308e53acf14e0ce108d94ecd616633ac93e35d))

## [4.0.0](https://github.com/taskforcesh/bullmq-pro/compare/v3.0.0...v4.0.0) (2022-10-27)

#### 버그 수정

* **job:** failParentOnFailure일 때 failed 이벤트 전송 ([#1481](https://github.com/taskforcesh/bullmq/issues/1481)) fixes [#1469](https://github.com/taskforcesh/bullmq/issues/1469) ([b20eb6f](https://github.com/taskforcesh/bullmq/commit/b20eb6f65c7e2c4593d5f9f4d4b940f780bf26d2))
* **redis:** throw exception을 console.error로 대체 ([fafa2f8](https://github.com/taskforcesh/bullmq/commit/fafa2f89e796796f950e6c4abbdda4d3d71ad1b0))
* **connection:** Cluster에서 문자열 배열 검증 ([#1468](https://github.com/taskforcesh/bullmq/issues/1468)) fixes [#1467](https://github.com/taskforcesh/bullmq/issues/1467) ([8355182](https://github.com/taskforcesh/bullmq/commit/8355182a372b68ec62e9c3953bacbd69e0abfc74))
* **worker:** worker 종료 시 stalled jobs 타이머 정리 ([1567a0d](https://github.com/taskforcesh/bullmq/commit/1567a0df0ca3c8d43a18990fe488888f4ff68040))
* **getters:** getJobLogs의 반환 타입 수정 ([d452927](https://github.com/taskforcesh/bullmq/commit/d4529278c59b2c94eee604c7d4455acc490679e9))
* **sandbox:** get-port 대신 내장 모듈을 사용해 열린 포트 가져오기 ([#1446](https://github.com/taskforcesh/bullmq/issues/1446)) ([6db6288](https://github.com/taskforcesh/bullmq/commit/6db628868a9d64c5a3e47d1c9201017e6d05c1ae))
* **job:** wait로 이동할 때 delay 값 업데이트 ([#1436](https://github.com/taskforcesh/bullmq/issues/1436)) ([9560915](https://github.com/taskforcesh/bullmq/commit/95609158c1800cf661f22ad7995541fb9474826a))
* **connection:** noeviction policy가 없으면 에러 발생 ([3468390](https://github.com/taskforcesh/bullmq/commit/3468390dd6331291f4cf71a54c32028a06d1d99e))
* **compat:** Queue3 클래스 제거 ([#1421](https://github.com/taskforcesh/bullmq/issues/1421)) ([fc797f7](https://github.com/taskforcesh/bullmq/commit/fc797f7cd334c19a95cb1290ddb6611cd3417179))
* **delayed:** 하나씩 가져오는 대신 delayed jobs 승격 ([1b938af](https://github.com/taskforcesh/bullmq/commit/1b938af75069d69772ddf2b03f95db7f53eada68))
* **delayed:** delayed job 승격 시 marker 제거 ([1aea0dc](https://github.com/taskforcesh/bullmq/commit/1aea0dcc5fb29086cef3d0c432c387d6f8261963))
* **getters:** "mark" job id 보정 ([231b9aa](https://github.com/taskforcesh/bullmq/commit/231b9aa0f4781e4493d3ea272c33b27c0b7dc0ab))
* **sandbox:** progress 메서드 제거 ([b43267b](https://github.com/taskforcesh/bullmq/commit/b43267be50f9eade8233500d189d46940a01cc29))
* **stalled-jobs:** job id 0 처리 ([829e6e0](https://github.com/taskforcesh/bullmq/commit/829e6e0252e78bf2cbc55ab1d3bd153faa0cee4c))
* **worker:** stalledInterval이 0보다 작아지는 것 방지 ([831ffc5](https://github.com/taskforcesh/bullmq/commit/831ffc520ccd3c6ea63af6b04ddddc9f7829c667))
* **worker:** 종료 상태 판단에 connection closing 사용 ([fe1d173](https://github.com/taskforcesh/bullmq/commit/fe1d17321f1eb49bd872c52965392add22729941))

#### 기능

* **redis-connection:** 확장을 위해 스크립트 제공 허용 ([#1472](https://github.com/taskforcesh/bullmq/issues/1472)) ([f193cfb](https://github.com/taskforcesh/bullmq/commit/f193cfb1830e127f9fd47a969baad30011a0e3a4))
* **flow-producer:** 플로우 추가 시 루트 작업에서 parent opts 허용 ([#1110](https://github.com/taskforcesh/bullmq/issues/1110)) ref [#1097](https://github.com/taskforcesh/bullmq/issues/1097) ([3c3ac71](https://github.com/taskforcesh/bullmq/commit/3c3ac718ad84f6bd0cc1575013c948e767b46f38))
* **job-options:** failParentOnFailure 옵션 추가 ([#1339](https://github.com/taskforcesh/bullmq/issues/1339)) ([65e5c36](https://github.com/taskforcesh/bullmq/commit/65e5c3678771f26555c9128bdb908dd62e3584f9))
* delayed jobs 개선 및 QueueSchedulerPro 제거 ([1f66e5a](https://github.com/taskforcesh/bullmq/commit/1f66e5a6c891d52e0671e58a685dbca511e45e7e))
* stalled jobs 검사 및 처리를 QueueSchedulerPro에서 WorkerPro 클래스로 이동 ([13769cb](https://github.com/taskforcesh/bullmq/commit/13769cbe38ba22793cbc66e9706a6be28a7f1512))

#### 성능 개선

* **scripts:** 스크립트 사전 빌드 ([#1441](https://github.com/taskforcesh/bullmq/issues/1441)) ([7f72603](https://github.com/taskforcesh/bullmq/commit/7f72603d463f705d0617898cb221f832c49a4aa3))
* **events:** added 이벤트에서 data 및 opts 제거 ([e13d4b8](https://github.com/taskforcesh/bullmq/commit/e13d4b8e0c4f99203f4249ccc86e369d124ff483))

#### 호환성 깨지는 변경 사항

* QueueSchedulerPro 클래스를 제거했습니다. QueueSchedulerPro 기능은 WorkerPro 클래스가 처리해야 합니다.
* **compat:** Bullv3용 호환 클래스는 더 이상 제공되지 않습니다.
* Failed 및 stalled 이벤트는 이제 QueueSchedulerPro가 아니라 WorkerPro 클래스에서 생성됩니다.
* 권장되는 Redis 최소 버전은 6.2.0입니다.

