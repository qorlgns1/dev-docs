---
title: '[1.91.1](https://github.com/taskforcesh/bullmq/compare/v1.91.0...v1.91.1) (2022-09-18)'
---

Source URL: https://docs.bullmq.io/changelog/changelog-v1

# v1

### [1.91.1](https://github.com/taskforcesh/bullmq/compare/v1.91.0...v1.91.1) (2022-09-18)

#### 버그 수정

* **drain:** 활성 목록이 비어 있는 경우를 고려 ([#1412](https://github.com/taskforcesh/bullmq/issues/1412)) ([f919a50](https://github.com/taskforcesh/bullmq/commit/f919a50b2f4972dcb9ecd5848b0f7fd9a0e137ea))

## [1.91.0](https://github.com/taskforcesh/bullmq/compare/v1.90.2...v1.91.0) (2022-09-16)

#### 기능

* **sandbox:** update 메서드 지원 ([#1416](https://github.com/taskforcesh/bullmq/issues/1416)) ([606b75d](https://github.com/taskforcesh/bullmq/commit/606b75d53e12dfc109f01eda38736c07e829e9b7))

### [1.90.2](https://github.com/taskforcesh/bullmq/compare/v1.90.1...v1.90.2) (2022-09-12)

#### 성능 개선

* **script-loader:** 캐시를 사용해 스크립트를 한 번만 읽도록 개선 ([#1410](https://github.com/taskforcesh/bullmq/issues/1410)) ([f956e93](https://github.com/taskforcesh/bullmq/commit/f956e937ae3488cdcd0e2eacbe3e096c8066ebd1))

### [1.90.1](https://github.com/taskforcesh/bullmq/compare/v1.90.0...v1.90.1) (2022-09-02)

#### 성능 개선

* **add-job:** js에서 parent split 처리 ([#1397](https://github.com/taskforcesh/bullmq/issues/1397)) ([566f074](https://github.com/taskforcesh/bullmq/commit/566f0747110679e5b07e7642fef793744565fffe))

## [1.90.0](https://github.com/taskforcesh/bullmq/compare/v1.89.2...v1.90.0) (2022-08-30)

#### 기능

* **repeat:** cron strategy 전달 허용 ([#1248](https://github.com/taskforcesh/bullmq/issues/1248)) 참조 [#1245](https://github.com/taskforcesh/bullmq/issues/1245) ([7f0534f](https://github.com/taskforcesh/bullmq/commit/7f0534f72449ae14a7415fa17a2eb2a70136a8b0))

### [1.89.2](https://github.com/taskforcesh/bullmq/compare/v1.89.1...v1.89.2) (2022-08-23)

#### 버그 수정

* **job:** changeDelay 시 delay 업데이트 ([#1389](https://github.com/taskforcesh/bullmq/issues/1389)) [#1160](https://github.com/taskforcesh/bullmq/issues/1160) 수정 ([d9b100d](https://github.com/taskforcesh/bullmq/commit/d9b100d04112c518ef2efbcf5586aa1226ccccab))

### [1.89.1](https://github.com/taskforcesh/bullmq/compare/v1.89.0...v1.89.1) (2022-08-19)

#### 버그 수정

* "chore: allow esm imports through exports field" 되돌림 ([#1388](https://github.com/taskforcesh/bullmq/issues/1388)) ([8e51272](https://github.com/taskforcesh/bullmq/commit/8e512724b1e8145bceb0152b70a934decf6d6864))

## [1.89.0](https://github.com/taskforcesh/bullmq/compare/v1.88.2...v1.89.0) (2022-08-18)

#### 기능

* **job:** 인스턴스에서 delay 노출 ([#1386](https://github.com/taskforcesh/bullmq/issues/1386)) ([d4d0d2e](https://github.com/taskforcesh/bullmq/commit/d4d0d2e737c7ceb5eb34a2c50d53bd1081e0ad4a))

### [1.88.2](https://github.com/taskforcesh/bullmq/compare/v1.88.1...v1.88.2) (2022-08-18)

#### 버그 수정

* "feat(sandbox): experimental support ESM" 되돌림 ([#1384](https://github.com/taskforcesh/bullmq/issues/1384)) ([7d180eb](https://github.com/taskforcesh/bullmq/commit/7d180eb18daa41062dcbca72213bc9d9f40153db))

### [1.88.1](https://github.com/taskforcesh/bullmq/compare/v1.88.0...v1.88.1) (2022-08-17)

#### 버그 수정

* husky 설치 수정 ([edee918](https://github.com/taskforcesh/bullmq/commit/edee918e84ba895ed4ef63cabcc26b97d9c52d8d))

## [1.88.0](https://github.com/taskforcesh/bullmq/compare/v1.87.2...v1.88.0) (2022-08-17)

#### 버그 수정

* **clean:** 대기 중인 작업 정리 시 priority 고려 ([#1357](https://github.com/taskforcesh/bullmq/issues/1357)) ([ced5be1](https://github.com/taskforcesh/bullmq/commit/ced5be1c9531953baa9cf87d6bda3faa5863270d))
* **parent-priority-check:** priority에 tonumber 사용 ([#1370](https://github.com/taskforcesh/bullmq/issues/1370)) ([e2043c6](https://github.com/taskforcesh/bullmq/commit/e2043c6f4b8ad5faea8c13edde76aea60612fec6))

#### 기능

* **sandbox:** ESM 실험적 지원 ([ed0faff](https://github.com/taskforcesh/bullmq/commit/ed0faff3c67c436116eb625ffacb03e435caee3f))

### [1.87.2](https://github.com/taskforcesh/bullmq/compare/v1.87.1...v1.87.2) (2022-08-13)

#### 버그 수정

* **move-parent-to-wait:** active 이벤트 대신 waiting 이벤트 emit ([#1356](https://github.com/taskforcesh/bullmq/issues/1356)) ([53578dd](https://github.com/taskforcesh/bullmq/commit/53578dd1cbe31b49361a833b1aca449486f3b925))

### [1.87.1](https://github.com/taskforcesh/bullmq/compare/v1.87.0...v1.87.1) (2022-08-09)

#### 버그 수정

* **job:** discarded를 protected로 선언 ([#1352](https://github.com/taskforcesh/bullmq/issues/1352)) ([870e01c](https://github.com/taskforcesh/bullmq/commit/870e01c4ab602c1e6e351cc369f3eac5f7afa083))

## [1.87.0](https://github.com/taskforcesh/bullmq/compare/v1.86.10...v1.87.0) (2022-08-05)

#### 기능

* **flow:** parent가 이동될 때 priority 고려 ([#1286](https://github.com/taskforcesh/bullmq/issues/1286)) ([d49760d](https://github.com/taskforcesh/bullmq/commit/d49760d09420c5fcc99ab06c8fe36168755fd397))

### [1.86.10](https://github.com/taskforcesh/bullmq/compare/v1.86.9...v1.86.10) (2022-07-29)

#### 성능 개선

* **clean-jobs-in-set:** limit > 0일 때 ZRANGEBYSCORE 사용 ([#1338](https://github.com/taskforcesh/bullmq/issues/1338)) ([f0d9985](https://github.com/taskforcesh/bullmq/commit/f0d998541f03778ca2a092080a19e6bf7b7d0af1))

### [1.86.9](https://github.com/taskforcesh/bullmq/compare/v1.86.8...v1.86.9) (2022-07-27)

#### 버그 수정

* **get-flow:** groupKey 고려 ([#1336](https://github.com/taskforcesh/bullmq/issues/1336)) [#1334](https://github.com/taskforcesh/bullmq/issues/1334) 수정 ([9f31272](https://github.com/taskforcesh/bullmq/commit/9f31272fa8b3f5b8ab26f15e21bd80537c5baef0))

### [1.86.8](https://github.com/taskforcesh/bullmq/compare/v1.86.7...v1.86.8) (2022-07-26)

#### 버그 수정

* **promote:** 일시 중지 시 빈 큐 고려 ([#1335](https://github.com/taskforcesh/bullmq/issues/1335)) ([9f742e8](https://github.com/taskforcesh/bullmq/commit/9f742e88d6338ce9ac7e0413bdac411ab6cf675c))

### [1.86.7](https://github.com/taskforcesh/bullmq/compare/v1.86.6...v1.86.7) (2022-07-15)

#### 버그 수정

* **sandboxed-process:** UnrecoverableError 고려 ([#1320](https://github.com/taskforcesh/bullmq/issues/1320)) [#1317](https://github.com/taskforcesh/bullmq/issues/1317) 수정 ([c1269cc](https://github.com/taskforcesh/bullmq/commit/c1269cc772c6cec84d82ff790b9a7c9cc4242dcb))

### [1.86.6](https://github.com/taskforcesh/bullmq/compare/v1.86.5...v1.86.6) (2022-07-14)

#### 버그 수정

* **retry-jobs:** 일시 중지된 큐 고려 ([#1321](https://github.com/taskforcesh/bullmq/issues/1321)) ([3e9703d](https://github.com/taskforcesh/bullmq/commit/3e9703d17fc9dc601d5d77e999f3e9a137f20843))

### [1.86.5](https://github.com/taskforcesh/bullmq/compare/v1.86.4...v1.86.5) (2022-07-09)

#### 버그 수정

* **retry-job:** 일시 중지된 큐 고려 ([#1314](https://github.com/taskforcesh/bullmq/issues/1314)) ([907ae1d](https://github.com/taskforcesh/bullmq/commit/907ae1d7e3504f31c625ec8a09e32785f08357ff))

### [1.86.4](https://github.com/taskforcesh/bullmq/compare/v1.86.3...v1.86.4) (2022-06-29)

#### 버그 수정

* **parent:** 대기 중인 자식이 없을 때 waiting 이벤트 emit ([#1296](https://github.com/taskforcesh/bullmq/issues/1296)) ([aa8fa3f](https://github.com/taskforcesh/bullmq/commit/aa8fa3f8cd5ab6d7d309d87ae45c558249b1c29c))

### [1.86.3](https://github.com/taskforcesh/bullmq/compare/v1.86.2...v1.86.3) (2022-06-26)

#### 버그 수정

* 큐가 종료되는 중이면 delay()를 호출하지 않도록 개선 ([#1295](https://github.com/taskforcesh/bullmq/issues/1295)) ([52a5045](https://github.com/taskforcesh/bullmq/commit/52a5045b903ed6e0e73dd747748787a6389f12f7))

### [1.86.2](https://github.com/taskforcesh/bullmq/compare/v1.86.1...v1.86.2) (2022-06-16)

#### 버그 수정

* **queue:** defaultJobOptions에서 repeat 옵션 제거 ([#1284](https://github.com/taskforcesh/bullmq/issues/1284)) ([cdd2a20](https://github.com/taskforcesh/bullmq/commit/cdd2a20c2c4ca47042ecd1da525ecb72941e4910))

### [1.86.1](https://github.com/taskforcesh/bullmq/compare/v1.86.0...v1.86.1) (2022-06-12)

#### 버그 수정

* 비어 있는 metrics를 배치로 언팩 처리 ([96829db](https://github.com/taskforcesh/bullmq/commit/96829db839fad4489415f7dbb047abdca5566e78))

## [1.86.0](https://github.com/taskforcesh/bullmq/compare/v1.85.4...v1.86.0) (2022-06-10)

#### 기능

* **repeat:** repeatJobKey 참조 저장 ([#1214](https://github.com/taskforcesh/bullmq/issues/1214)) ([4d5a8e3](https://github.com/taskforcesh/bullmq/commit/4d5a8e33b614cf099369c18298e5b2963b434b1b))

### [1.85.4](https://github.com/taskforcesh/bullmq/compare/v1.85.3...v1.85.4) (2022-06-08)

#### 버그 수정

* **error-prototype:** toJSON 메서드에 사용자 정의 name 지정 ([#1272](https://github.com/taskforcesh/bullmq/issues/1272)) ([66d80da](https://github.com/taskforcesh/bullmq/commit/66d80da4a6043755c7d296addb31857816ea4da3))

### [1.85.3](https://github.com/taskforcesh/bullmq/compare/v1.85.2...v1.85.3) (2022-06-03)

#### 버그 수정

* **queue:** addBulk 시그니처의 ResultType 수정 ([#1268](https://github.com/taskforcesh/bullmq/issues/1268)) ([f6770cc](https://github.com/taskforcesh/bullmq/commit/f6770cc383b68bf7b2fa655cd9eda713a06835aa))

### [1.85.2](https://github.com/taskforcesh/bullmq/compare/v1.85.1...v1.85.2) (2022-06-01)

#### 버그 수정

* **job:** 인스턴스에 finishedOn 속성 저장 ([#1267](https://github.com/taskforcesh/bullmq/issues/1267)) ([4cf6a63](https://github.com/taskforcesh/bullmq/commit/4cf6a63d197e6095841bb87cef297a9533ac79c3))

### [1.85.1](https://github.com/taskforcesh/bullmq/compare/v1.85.0...v1.85.1) (2022-05-31)

#### 성능 개선

* **remove-job:** jobKey 대신 prefix key 전송 ([#1252](https://github.com/taskforcesh/bullmq/issues/1252)) ([452856a](https://github.com/taskforcesh/bullmq/commit/452856a6c8c6e67ffda595c26c30988a15c1c1a4))

## [1.85.0](https://github.com/taskforcesh/bullmq/compare/v1.84.1...v1.85.0) (2022-05-30)

#### 기능

* **worker:** 동시 프로세스 수 변경 ([#1256](https://github.com/taskforcesh/bullmq/issues/1256)) 참조 [#22](https://github.com/taskforcesh/bullmq/issues/22) ([940dc8f](https://github.com/taskforcesh/bullmq/commit/940dc8f34d9a46dc9c8384661461bf0558e97600))

### [1.84.1](https://github.com/taskforcesh/bullmq/compare/v1.84.0...v1.84.1) (2022-05-27)

#### 버그 수정

* **waiting-children:** moveToWaitingChildren에 올바른 timestamp 값 전달 ([#1260](https://github.com/taskforcesh/bullmq/issues/1260)) ([0f993f7](https://github.com/taskforcesh/bullmq/commit/0f993f71ed481b02a3f859a2109177352336cb9a))

## [1.84.0](https://github.com/taskforcesh/bullmq/compare/v1.83.2...v1.84.0) (2022-05-26)

#### 기능

* **flow-producer:** event listener 타입 추가 ([#1257](https://github.com/taskforcesh/bullmq/issues/1257)) ([19ed099](https://github.com/taskforcesh/bullmq/commit/19ed099905cbb4f071370b2b6d67d9a378e3a8f8))

### [1.83.2](https://github.com/taskforcesh/bullmq/compare/v1.83.1...v1.83.2) (2022-05-24)

#### 버그 수정

* **close:** error 대신 ioredis:close 이벤트 emit ([#1251](https://github.com/taskforcesh/bullmq/issues/1251)) [#1231](https://github.com/taskforcesh/bullmq/issues/1231) 수정 ([74c1c38](https://github.com/taskforcesh/bullmq/commit/74c1c38f7ff468da1adc63aff160e31940d682a9))

### [1.83.1](https://github.com/taskforcesh/bullmq/compare/v1.83.0...v1.83.1) (2022-05-24)

#### 버그 수정

* **get-workers:** clientName 설정에 blockingConnection client 사용 ([#1255](https://github.com/taskforcesh/bullmq/issues/1255)) [#1254](https://github.com/taskforcesh/bullmq/issues/1254) 수정 ([df796bd](https://github.com/taskforcesh/bullmq/commit/df796bd0c085aff72cef001395809b3f1a8045e4))

## [1.83.0](https://github.com/taskforcesh/bullmq/compare/v1.82.3...v1.83.0) (2022-05-20)

#### 기능

* **flow-producer:** 확장 기능을 더 쉽게 구축할 수 있도록 개선 ([#1250](https://github.com/taskforcesh/bullmq/issues/1250)) ([aaf637e](https://github.com/taskforcesh/bullmq/commit/aaf637e74b9610651fd9e4efc5ff349971b7bb26))

### [1.82.3](https://github.com/taskforcesh/bullmq/compare/v1.82.2...v1.82.3) (2022-05-19)

#### 버그 수정

* **redis-connection:** cluster opts를 저장하고 redis 버전을 coerse 처리 ([#1247](https://github.com/taskforcesh/bullmq/issues/1247)) ref [#1246](https://github.com/taskforcesh/bullmq/issues/1246) fixes [#1243](https://github.com/taskforcesh/bullmq/issues/1243) ([acb69b5](https://github.com/taskforcesh/bullmq/commit/acb69b57d7a6417b8ca9fe1576a94d16e41f12d7))

### [1.82.2](https://github.com/taskforcesh/bullmq/compare/v1.82.1...v1.82.2) (2022-05-17)

#### 버그 수정

* **job:** 확장을 위한 job helper 속성 추가 ([#1242](https://github.com/taskforcesh/bullmq/issues/1242)) ([4d7ae9e](https://github.com/taskforcesh/bullmq/commit/4d7ae9e3fda23650e802ebac6b33ff3350f116f6))

### [1.82.1](https://github.com/taskforcesh/bullmq/compare/v1.82.0...v1.82.1) (2022-05-16)

#### 버그 수정

* **remove-job:** removed 이벤트에서 올바른 prev 파라미터 전달 ([#1237](https://github.com/taskforcesh/bullmq/issues/1237)) ([54df47e](https://github.com/taskforcesh/bullmq/commit/54df47edf715a0a2a42687bf827e0a62c03951a5))

## [1.82.0](https://github.com/taskforcesh/bullmq/compare/v1.81.4...v1.82.0) (2022-05-11)

#### 기능

* **remove-repeatable:** job 존재 여부에 따라 boolean 반환 ([#1239](https://github.com/taskforcesh/bullmq/issues/1239)) ref [#1235](https://github.com/taskforcesh/bullmq/issues/1235) ([59b0da7](https://github.com/taskforcesh/bullmq/commit/59b0da7d0e979e4f9e8a5b042acbdce433790611))

### [1.81.4](https://github.com/taskforcesh/bullmq/compare/v1.81.3...v1.81.4) (2022-05-05)

#### 버그 수정

* **repeatable:** 제거 시 removed 이벤트 발생 ([#1229](https://github.com/taskforcesh/bullmq/issues/1229)) ([7d2de8d](https://github.com/taskforcesh/bullmq/commit/7d2de8d075e5ee7774501429c5177b729c430c20))

### [1.81.3](https://github.com/taskforcesh/bullmq/compare/v1.81.2...v1.81.3) (2022-05-04)

#### 버그 수정

* **remove-parent:** waiting-children에서 removed 레코드 확인 ([#1227](https://github.com/taskforcesh/bullmq/issues/1227)) ([e7b25d0](https://github.com/taskforcesh/bullmq/commit/e7b25d00acb860ee3df36c6214a7162b2cf79635))

### [1.81.2](https://github.com/taskforcesh/bullmq/compare/v1.81.1...v1.81.2) (2022-05-03)

#### 버그 수정

* **stalled:** job 실패 시 removeOnFail 고려 ([#1225](https://github.com/taskforcesh/bullmq/issues/1225)) fixes [#1171](https://github.com/taskforcesh/bullmq/issues/1171) ([38486cb](https://github.com/taskforcesh/bullmq/commit/38486cb4d7cbfc78bd64d71f19d8bfbc908f3fc7))

### [1.81.1](https://github.com/taskforcesh/bullmq/compare/v1.81.0...v1.81.1) (2022-04-29)

#### 버그 수정

* **add-bulk:** for loop를 사용하고 오류가 있으면 throw ([#1223](https://github.com/taskforcesh/bullmq/issues/1223)) fixes [#1222](https://github.com/taskforcesh/bullmq/issues/1222) ([564de4f](https://github.com/taskforcesh/bullmq/commit/564de4f907648f5a5667a845c5366f73cff1d384))

## [1.81.0](https://github.com/taskforcesh/bullmq/compare/v1.80.6...v1.81.0) (2022-04-26)

#### 기능

* **move-to-delayed:** token 전달 허용 ([#1213](https://github.com/taskforcesh/bullmq/issues/1213)) ([14f0e4a](https://github.com/taskforcesh/bullmq/commit/14f0e4a33d9ddfbaa1f86dbe7598e20a516a9d09))

### [1.80.6](https://github.com/taskforcesh/bullmq/compare/v1.80.5...v1.80.6) (2022-04-22)

#### 버그 수정

* **job:** delayed로 이동할 때 token 삭제 ([#1208](https://github.com/taskforcesh/bullmq/issues/1208)) ([37acf41](https://github.com/taskforcesh/bullmq/commit/37acf4109d17090dfaef992267e48130d34f7187))

### [1.80.5](https://github.com/taskforcesh/bullmq/compare/v1.80.4...v1.80.5) (2022-04-21)

#### 버그 수정

* **queue-base:** 닫는 중이 아닐 때 close error 이벤트 발생 ([#1203](https://github.com/taskforcesh/bullmq/issues/1203)) fixes [#1205](https://github.com/taskforcesh/bullmq/issues/1205) ([4d76582](https://github.com/taskforcesh/bullmq/commit/4d7658272af94b57a09486e1141b0e15a7bac3ba))

### [1.80.4](https://github.com/taskforcesh/bullmq/compare/v1.80.3...v1.80.4) (2022-04-19)

#### 버그 수정

* **queue-scheduler:** isNotConnectionError 적용 ([#1189](https://github.com/taskforcesh/bullmq/issues/1189)) fixes [#1181](https://github.com/taskforcesh/bullmq/issues/1181) ([605d685](https://github.com/taskforcesh/bullmq/commit/605d68595d8fa1d9d47348a3fa9e0d7a4e28c706))

### [1.80.3](https://github.com/taskforcesh/bullmq/compare/v1.80.2...v1.80.3) (2022-04-15)

#### 버그 수정

* **cluster:** 올바른 Upstash 호스트 확인 ([#1195](https://github.com/taskforcesh/bullmq/issues/1195)) fixes [#1193](https://github.com/taskforcesh/bullmq/issues/1193) ([69f2863](https://github.com/taskforcesh/bullmq/commit/69f28632408c741219c1ba49304d36f49cf5cb83))

### [1.80.2](https://github.com/taskforcesh/bullmq/compare/v1.80.1...v1.80.2) (2022-04-15)

#### 버그 수정

* **job:** moveToWaitingChildren의 Promise 반환에서 Error 제거 ([#1197](https://github.com/taskforcesh/bullmq/issues/1197)) ([180a8bf](https://github.com/taskforcesh/bullmq/commit/180a8bf8fb2fe62b9929765a6dfd084574c77936))

### [1.80.1](https://github.com/taskforcesh/bullmq/compare/v1.80.0...v1.80.1) (2022-04-14)

#### 버그 수정

* **worker:** worker suffix를 빈 문자열로 복원 ([#1194](https://github.com/taskforcesh/bullmq/issues/1194)) fixes [#1185](https://github.com/taskforcesh/bullmq/issues/1185) ([2666ea5](https://github.com/taskforcesh/bullmq/commit/2666ea5b8532645da24482cf01c5692da5f2ceda))

## [1.80.0](https://github.com/taskforcesh/bullmq/compare/v1.79.1...v1.80.0) (2022-04-12)

#### 기능

* **worker-listener:** 이벤트에 generics 사용 ([#1190](https://github.com/taskforcesh/bullmq/issues/1190)) ref [#1188](https://github.com/taskforcesh/bullmq/issues/1188) ([2821193](https://github.com/taskforcesh/bullmq/commit/28211937d9ed405330eede5ad7d4b0b817accf39))

### [1.79.1](https://github.com/taskforcesh/bullmq/compare/v1.79.0...v1.79.1) (2022-04-12)

#### 버그 수정

* **connection:** Queue reconnect overrides 제거 ([#1119](https://github.com/taskforcesh/bullmq/issues/1119)) ([83f1c79](https://github.com/taskforcesh/bullmq/commit/83f1c797b8a5272028c8d78d5ce464236e90909e))

## [1.79.0](https://github.com/taskforcesh/bullmq/compare/v1.78.2...v1.79.0) (2022-04-08)

#### 기능

* **queue-getters:** getQueueEvents 추가 ([#1085](https://github.com/taskforcesh/bullmq/issues/1085)) ([f10a20a](https://github.com/taskforcesh/bullmq/commit/f10a20a90ab6dbf2d9f3f75ba99dacbdc797c329))

### [1.78.2](https://github.com/taskforcesh/bullmq/compare/v1.78.1...v1.78.2) (2022-03-31)

#### 버그 수정

* **clean:** processedOn 및 finishedOn 속성 고려 ([#1158](https://github.com/taskforcesh/bullmq/issues/1158)) ([8c3cb72](https://github.com/taskforcesh/bullmq/commit/8c3cb72235ec6123da389553f37433c2943e0f57))

### [1.78.1](https://github.com/taskforcesh/bullmq/compare/v1.78.0...v1.78.1) (2022-03-24)

#### 버그 수정

* **queue:** close 호출 시 repeat connection 종료 ([#1154](https://github.com/taskforcesh/bullmq/issues/1154)) ([7d79616](https://github.com/taskforcesh/bullmq/commit/7d796167229048ec79660ca5d3ac8a7c85d125e7))

## [1.78.0](https://github.com/taskforcesh/bullmq/compare/v1.77.3...v1.78.0) (2022-03-23)

#### 기능

* **cron-parser:** 버전을 4.2.1로 업그레이드 ([#1149](https://github.com/taskforcesh/bullmq/issues/1149)) fixes [#1147](https://github.com/taskforcesh/bullmq/issues/1147) ([88a6c9c](https://github.com/taskforcesh/bullmq/commit/88a6c9c437172035173628842909f5170eb481f7))

### [1.77.3](https://github.com/taskforcesh/bullmq/compare/v1.77.2...v1.77.3) (2022-03-22)

#### 버그 수정

* **async-send:** proc.send 타입 확인 ([#1150](https://github.com/taskforcesh/bullmq/issues/1150)) ([4f44173](https://github.com/taskforcesh/bullmq/commit/4f44173f0a3cc54705ca9a7e1730aeff26ea1c5a))

### [1.77.2](https://github.com/taskforcesh/bullmq/compare/v1.77.1...v1.77.2) (2022-03-20)

#### 버그 수정

* **trim-events:** maxLenEvents를 0으로 고려 ([#1137](https://github.com/taskforcesh/bullmq/issues/1137)) ([bc58a49](https://github.com/taskforcesh/bullmq/commit/bc58a49fba1b6f4e3595a0371ecf8410000a9021))

#### 성능 개선

* **clean:** deletion marker를 사용해 clean 작업 속도 향상 ([#1144](https://github.com/taskforcesh/bullmq/issues/1144)) ([5fb32ef](https://github.com/taskforcesh/bullmq/commit/5fb32ef2c60843d8d1f2cbc000aacf4df3388b7e))

### [1.77.1](https://github.com/taskforcesh/bullmq/compare/v1.77.0...v1.77.1) (2022-03-17)

#### 버그 수정

* **flow:** 처리된 자식 제거 ([#1060](https://github.com/taskforcesh/bullmq/issues/1060)) fixes [#1056](https://github.com/taskforcesh/bullmq/issues/1056) ([6b54e86](https://github.com/taskforcesh/bullmq/commit/6b54e86c12f287a13da036f3ec7801b8656f0434))

## [1.77.0](https://github.com/taskforcesh/bullmq/compare/v1.76.6...v1.77.0) (2022-03-16)

#### 기능

* QueueScheduler 확장 허용 ([289beb8](https://github.com/taskforcesh/bullmq/commit/289beb87d2ef3e3dd7583159f7be2b5450f7de3c))

### [1.76.6](https://github.com/taskforcesh/bullmq/compare/v1.76.5...v1.76.6) (2022-03-15)

#### 버그 수정

* **master:** master 파일을 export하지 않음 ([#1136](https://github.com/taskforcesh/bullmq/issues/1136)) fixes [#1125](https://github.com/taskforcesh/bullmq/issues/1125) ref [#1129](https://github.com/taskforcesh/bullmq/issues/1129) ([6aa2f96](https://github.com/taskforcesh/bullmq/commit/6aa2f9657b8787aa791ab5af7267a6d27d7d7869))

### [1.76.5](https://github.com/taskforcesh/bullmq/compare/v1.76.4...v1.76.5) (2022-03-15)

#### 버그 수정

* **queue:** getJobs 및 getJobsCount에서 job 타입 정리(sanitize) ([#1113](https://github.com/taskforcesh/bullmq/issues/1113)) fixes [#1112](https://github.com/taskforcesh/bullmq/issues/1112) ([d452b29](https://github.com/taskforcesh/bullmq/commit/d452b29773cead153a73b8322adda3164fb610d8))

### [1.76.4](https://github.com/taskforcesh/bullmq/compare/v1.76.3...v1.76.4) (2022-03-13)

#### 성능 개선

* **move-to-finished:** rate limit 사용 시 추가 roundtrip 방지 ([#1131](https://github.com/taskforcesh/bullmq/issues/1131)) ([1711547](https://github.com/taskforcesh/bullmq/commit/171154707bf5cbcb750ea9d2a9957128c1abc044))

### [1.76.3](https://github.com/taskforcesh/bullmq/compare/v1.76.2...v1.76.3) (2022-03-10)

#### 버그 수정

* **drained:** queue가 waiting list를 비웠을 때 이벤트를 한 번만 발생 ([#1123](https://github.com/taskforcesh/bullmq/issues/1123)) fixes [#1121](https://github.com/taskforcesh/bullmq/issues/1121) ref [#1070](https://github.com/taskforcesh/bullmq/issues/1070) ([b89b4e8](https://github.com/taskforcesh/bullmq/commit/b89b4e8a83fe4c9349ac5a9c439fc07374ff1e63))

### [1.76.2](https://github.com/taskforcesh/bullmq/compare/v1.76.1...v1.76.2) (2022-03-09)

#### 버그 수정

* **utils:** proc.send 타입 수정 ([#1122](https://github.com/taskforcesh/bullmq/issues/1122)) fixes [#1120](https://github.com/taskforcesh/bullmq/issues/1120) ([da23977](https://github.com/taskforcesh/bullmq/commit/da239774379825d9f0a51c118740bc0fefa568bd))

### [1.76.1](https://github.com/taskforcesh/bullmq/compare/v1.76.0...v1.76.1) (2022-03-04)

#### 버그 수정

* **get-waiting-children-count:** waiting-children 상태만 고려 ([#1117](https://github.com/taskforcesh/bullmq/issues/1117)) ([1820df7](https://github.com/taskforcesh/bullmq/commit/1820df73c17ce119d2fdb0f526fc95f99845a5ec))

## [1.76.0](https://github.com/taskforcesh/bullmq/compare/v1.75.1...v1.76.0) (2022-03-02)

#### 기능

* **metrics:** metrics 지원 추가 ([ab51326](https://github.com/taskforcesh/bullmq/commit/ab51326cf318b4b48e37a1a77f5609e405eecb45))

### [1.75.1](https://github.com/taskforcesh/bullmq/compare/v1.75.0...v1.75.1) (2022-02-26)

#### 버그 수정

* **rate-limiter:** groupKey가 누락되면 재시도 후 job을 wait로 이동 ([#1103](https://github.com/taskforcesh/bullmq/issues/1103)) fixes [#1084](https://github.com/taskforcesh/bullmq/issues/1084) ([8aeab37](https://github.com/taskforcesh/bullmq/commit/8aeab37ac5a5c1c760be21bff2ba8752a485577c))

## [1.75.0](https://github.com/taskforcesh/bullmq/compare/v1.74.3...v1.75.0) (2022-02-24)

#### 버그 수정

* **cluster:** Upstash 유효성 검사에서 host 존재 여부 확인 ([#1102](https://github.com/taskforcesh/bullmq/issues/1102)) [#1101](https://github.com/taskforcesh/bullmq/issues/1101) 수정 ([54d4eac](https://github.com/taskforcesh/bullmq/commit/54d4eac52cfe13d4be99410932c0226c8d06d5d5))

#### 기능

* **retry-jobs:** 완료된 작업도 재시도할 수 있도록 허용 ([#1082](https://github.com/taskforcesh/bullmq/issues/1082)) ([e17b3f2](https://github.com/taskforcesh/bullmq/commit/e17b3f21606757a16630988a69c9607e8c843bd2))

### [1.74.3](https://github.com/taskforcesh/bullmq/compare/v1.74.2...v1.74.3) (2022-02-24)

#### 버그 수정

* **connection:** Upstash host가 제공되면 오류를 발생시키도록 변경 ([#1098](https://github.com/taskforcesh/bullmq/issues/1098)) [#1087](https://github.com/taskforcesh/bullmq/issues/1087) 수정 ([5156d0a](https://github.com/taskforcesh/bullmq/commit/5156d0a4812d8c649a3b41bd98e3e0efb41d0491))

### [1.74.2](https://github.com/taskforcesh/bullmq/compare/v1.74.1...v1.74.2) (2022-02-23)

#### 버그 수정

* **move-to-finished:** 작업을 active로 이동할 때 attemptsMade 증가 ([#1095](https://github.com/taskforcesh/bullmq/issues/1095)) [#1094](https://github.com/taskforcesh/bullmq/issues/1094) 수정 ([321b0e1](https://github.com/taskforcesh/bullmq/commit/321b0e1d515d01c5b3f1ca9f404cd571e3f753b7))

### [1.74.1](https://github.com/taskforcesh/bullmq/compare/v1.74.0...v1.74.1) (2022-02-20)

#### 버그 수정

* **flow:** queue opts의 defaultJobOptions를 준수하도록 변경 ([#1080](https://github.com/taskforcesh/bullmq/issues/1080)) [#1034](https://github.com/taskforcesh/bullmq/issues/1034) 수정 ([0aca072](https://github.com/taskforcesh/bullmq/commit/0aca072f805302e660b6675fd4097ba893c91eb0))

## [1.74.0](https://github.com/taskforcesh/bullmq/compare/v1.73.0...v1.74.0) (2022-02-19)

#### 기능

* **retry-jobs:** 옵션으로 timestamp 전달 ([#1054](https://github.com/taskforcesh/bullmq/issues/1054)) ([1522359](https://github.com/taskforcesh/bullmq/commit/15223590b235f749af9cb229fc784760d4b3add2))

## [1.73.0](https://github.com/taskforcesh/bullmq/compare/v1.72.0...v1.73.0) (2022-02-16)

#### 기능

* **job:** prefix getter 추가 ([#1077](https://github.com/taskforcesh/bullmq/issues/1077)) ([db9ef10](https://github.com/taskforcesh/bullmq/commit/db9ef105a7a524d7502664d52bd9f9c7dfa9477f))
* **queue-getters:** getQueueSchedulers 추가 ([#1078](https://github.com/taskforcesh/bullmq/issues/1078)) [#1075](https://github.com/taskforcesh/bullmq/issues/1075) 참조 ([0b3b1c4](https://github.com/taskforcesh/bullmq/commit/0b3b1c4382de34bd68733d162c2fa2ba9417f79c))

## [1.72.0](https://github.com/taskforcesh/bullmq/compare/v1.71.0...v1.72.0) (2022-02-15)

#### 기능

* **backoff:** UnrecoverableError 존재 여부 검증 ([#1074](https://github.com/taskforcesh/bullmq/issues/1074)) ([1defeac](https://github.com/taskforcesh/bullmq/commit/1defeac3f251a13aad57f3027d8eb8f857e40acb))

## [1.71.0](https://github.com/taskforcesh/bullmq/compare/v1.70.0...v1.71.0) (2022-02-14)

#### 기능

* **get-job-counts:** 기본값 추가 ([#1068](https://github.com/taskforcesh/bullmq/issues/1068)) ([1c7f841](https://github.com/taskforcesh/bullmq/commit/1c7f841a52b3ea18fa7878f10986b362ccc6c4fe))

## [1.70.0](https://github.com/taskforcesh/bullmq/compare/v1.69.1...v1.70.0) (2022-02-11)

#### 기능

* **sandbox:** parent 속성 전달 ([#1065](https://github.com/taskforcesh/bullmq/issues/1065)) ([1fd33f6](https://github.com/taskforcesh/bullmq/commit/1fd33f6fd3a3af17753de8c4d48e14ef86c7409c))

### [1.69.1](https://github.com/taskforcesh/bullmq/compare/v1.69.0...v1.69.1) (2022-02-10)

#### 버그 수정

* **move-to-finished:** 먼저 lock을 검증하도록 변경 ([#1064](https://github.com/taskforcesh/bullmq/issues/1064)) ([9da1b29](https://github.com/taskforcesh/bullmq/commit/9da1b29486c6c6e2b097ec2f6107494a36525495))

## [1.69.0](https://github.com/taskforcesh/bullmq/compare/v1.68.4...v1.69.0) (2022-02-08)

#### 기능

* **job:** sandbox에 queueName 전달 ([#1053](https://github.com/taskforcesh/bullmq/issues/1053)) [#1050](https://github.com/taskforcesh/bullmq/issues/1050) 수정 [#1051](https://github.com/taskforcesh/bullmq/issues/1051) 참조 ([12bb19c](https://github.com/taskforcesh/bullmq/commit/12bb19c1586d8755b973a80be97f407630827d4f))

### [1.68.4](https://github.com/taskforcesh/bullmq/compare/v1.68.3...v1.68.4) (2022-02-05)

#### 버그 수정

* **clean:** 정리 시 부모 작업 확인을 고려하도록 변경 ([#1048](https://github.com/taskforcesh/bullmq/issues/1048)) ([0708a24](https://github.com/taskforcesh/bullmq/commit/0708a24c7f4cb6d1cda776ed983d3f20fc3261f1))

### [1.68.3](https://github.com/taskforcesh/bullmq/compare/v1.68.2...v1.68.3) (2022-02-04)

#### 버그 수정

* **drain:** priority queueKey 삭제 ([#1049](https://github.com/taskforcesh/bullmq/issues/1049)) ([2e6129a](https://github.com/taskforcesh/bullmq/commit/2e6129a4a08783eeafa2f0b69c10ac810f53d085))

### [1.68.2](https://github.com/taskforcesh/bullmq/compare/v1.68.1...v1.68.2) (2022-02-03)

#### 성능 개선

* **remove-parent-dependency:** 하드 삭제 시 wait 이벤트를 emit하지 않도록 변경 ([#1045](https://github.com/taskforcesh/bullmq/issues/1045)) ([4069821](https://github.com/taskforcesh/bullmq/commit/40698218d13a880615f832a9926f0f057b1c33f9))

### [1.68.1](https://github.com/taskforcesh/bullmq/compare/v1.68.0...v1.68.1) (2022-02-01)

#### 버그 수정

* **update:** job key가 없을 때 오류를 발생시키도록 변경 ([#1042](https://github.com/taskforcesh/bullmq/issues/1042)) ([a00ae5c](https://github.com/taskforcesh/bullmq/commit/a00ae5c9b3f6d51cb0229adca29d13d932fc5601))

## [1.68.0](https://github.com/taskforcesh/bullmq/compare/v1.67.3...v1.68.0) (2022-01-29)

#### 기능

* **queue:** 실패한 작업용 retryJobs 메서드 추가 ([#1024](https://github.com/taskforcesh/bullmq/issues/1024)) ([310a730](https://github.com/taskforcesh/bullmq/commit/310a730ed322501cc19cdd5cf5244bc8eee6fee2))

#### 성능 개선

* **lua:** 여러 key로 del 명령 호출 ([#1035](https://github.com/taskforcesh/bullmq/issues/1035)) ([9cfaab8](https://github.com/taskforcesh/bullmq/commit/9cfaab8965d0c9f92460d31d6c3083839c36447f))

### [1.67.3](https://github.com/taskforcesh/bullmq/compare/v1.67.2...v1.67.3) (2022-01-28)

#### 버그 수정

* **drain:** draining 시 부모 작업 확인을 고려하도록 변경 ([#992](https://github.com/taskforcesh/bullmq/issues/992)) ([81b7221](https://github.com/taskforcesh/bullmq/commit/81b72213a9ff31d6b297825391de77557598ebd1))

### [1.67.2](https://github.com/taskforcesh/bullmq/compare/v1.67.1...v1.67.2) (2022-01-28)

#### 버그 수정

* **repeat:** cron과 함께 immediately 옵션을 고려하도록 변경 ([#1030](https://github.com/taskforcesh/bullmq/issues/1030)) [#1020](https://github.com/taskforcesh/bullmq/issues/1020) 수정 ([b9e7488](https://github.com/taskforcesh/bullmq/commit/b9e748870385a88b2384df40f50df3144c11d7e0))

### [1.67.1](https://github.com/taskforcesh/bullmq/compare/v1.67.0...v1.67.1) (2022-01-27)

#### 버그 수정

* **retry:** 오류 메시지에 state 전달 ([#1027](https://github.com/taskforcesh/bullmq/issues/1027)) ([c646a45](https://github.com/taskforcesh/bullmq/commit/c646a45377fdfaff340185d1f7bedceb80c214c2))

#### 성능 개선

* **retry:** retryJob lua script에서 props 삭제 ([#1016](https://github.com/taskforcesh/bullmq/issues/1016)) ([547cedd](https://github.com/taskforcesh/bullmq/commit/547cedd5ecd30c9a73d37e4053b9e518cb3fbe53))

## [1.67.0](https://github.com/taskforcesh/bullmq/compare/v1.66.1...v1.67.0) (2022-01-26)

#### 기능

* 시간 기반 removeOn 지원 추가 ([6c4ac75](https://github.com/taskforcesh/bullmq/commit/6c4ac75bb3ac239cc83ef6144d69c04b2bba1311))

### [1.66.1](https://github.com/taskforcesh/bullmq/compare/v1.66.0...v1.66.1) (2022-01-25)

#### 버그 수정

* **job:** 작업을 active로 이동할 때 attemptsMade 증가 ([#1009](https://github.com/taskforcesh/bullmq/issues/1009)) [#1002](https://github.com/taskforcesh/bullmq/issues/1002) 수정 ([0974ae0](https://github.com/taskforcesh/bullmq/commit/0974ae0ff6db73c223be4b18fb2aab53b6a23c88))

## [1.66.0](https://github.com/taskforcesh/bullmq/compare/v1.65.1...v1.66.0) (2022-01-23)

#### 기능

* **queue-events:** retries-exhausted 이벤트 추가 ([#1010](https://github.com/taskforcesh/bullmq/issues/1010)) ([e476f35](https://github.com/taskforcesh/bullmq/commit/e476f35f5c3f9b1baf2bbc3d46712b8ba597f73c))

### [1.65.1](https://github.com/taskforcesh/bullmq/compare/v1.65.0...v1.65.1) (2022-01-21)

#### 버그 수정

* 빈 modules 경로를 순회하지 않도록 변경 ([#1013](https://github.com/taskforcesh/bullmq/issues/1013)) [#1012](https://github.com/taskforcesh/bullmq/issues/1012) 수정 ([86e84df](https://github.com/taskforcesh/bullmq/commit/86e84df933c2662380b00a11b5f4000f2618d218))

## [1.65.0](https://github.com/taskforcesh/bullmq/compare/v1.64.4...v1.65.0) (2022-01-21)

#### 기능

* **queue:** 더 나은 타이핑을 위해 JobType 및 JobState union 추가 ([#1011](https://github.com/taskforcesh/bullmq/issues/1011)) ([3b9b79d](https://github.com/taskforcesh/bullmq/commit/3b9b79dbdd754ab66c3948e7e16380f2d5513262))

### [1.64.4](https://github.com/taskforcesh/bullmq/compare/v1.64.3...v1.64.4) (2022-01-19)

#### 버그 수정

* **queue:** getJobCountByTypes reducer의 초기값으로 0 사용 ([#1005](https://github.com/taskforcesh/bullmq/issues/1005)) ([f0e23ef](https://github.com/taskforcesh/bullmq/commit/f0e23ef01b97d36c775db0bf8c9dd2f63f6cb194))

### [1.64.3](https://github.com/taskforcesh/bullmq/compare/v1.64.2...v1.64.3) (2022-01-17)

#### 버그 수정

* **worker:** 구버전 Redis에서 blockTime은 정수여야 함 ([6fedc0a](https://github.com/taskforcesh/bullmq/commit/6fedc0a03bdb217ef0dbae60d49fccb0f2a5dbdb))

### [1.64.2](https://github.com/taskforcesh/bullmq/compare/v1.64.1...v1.64.2) (2022-01-14)

#### 버그 수정

* **remove-job:** lua scripts에서 부모 의존성 key 제거를 고려하도록 변경 ([#990](https://github.com/taskforcesh/bullmq/issues/990)) ([661abf0](https://github.com/taskforcesh/bullmq/commit/661abf0921e663c9ea2fa7d59c12da35950637dc))

### [1.64.1](https://github.com/taskforcesh/bullmq/compare/v1.64.0...v1.64.1) (2022-01-14)

#### 버그 수정

* **sandbox:** 오류를 throw하는 대신 uncaughtException에서 종료 ([013d6a5](https://github.com/taskforcesh/bullmq/commit/013d6a5ee0c70266ae740abfa596ca9e506de71b))

## [1.64.0](https://github.com/taskforcesh/bullmq/compare/v1.63.3...v1.64.0) (2022-01-07)

#### 기능

* **sanboxed-process:** .cjs 파일 지원 ([#984](https://github.com/taskforcesh/bullmq/issues/984)) ([531e4de](https://github.com/taskforcesh/bullmq/commit/531e4de1525f2cf322e0b97f5537ed43276ff72b))

### [1.63.3](https://github.com/taskforcesh/bullmq/compare/v1.63.2...v1.63.3) (2022-01-06)

#### 버그 수정

* **job:** delay와 repeat가 함께 제공되면 오류를 발생시키도록 변경 ([#983](https://github.com/taskforcesh/bullmq/issues/983)) ([07b0082](https://github.com/taskforcesh/bullmq/commit/07b008273ead9360fc43564fa9ff1a7503616ceb))

### [1.63.2](https://github.com/taskforcesh/bullmq/compare/v1.63.1...v1.63.2) (2022-01-04)

#### 버그 수정

* **queue:** 누락된 error 이벤트 타이핑 추가 ([#979](https://github.com/taskforcesh/bullmq/issues/979)) ([afdaac6](https://github.com/taskforcesh/bullmq/commit/afdaac6b072c7af5973222cc7fb69f3f138f3b0b))

### [1.63.1](https://github.com/taskforcesh/bullmq/compare/v1.63.0...v1.63.1) (2022-01-04)

#### 버그 수정

* **update-progress:** job key가 없으면 오류를 발생시키도록 변경 ([#978](https://github.com/taskforcesh/bullmq/issues/978)) [#977](https://github.com/taskforcesh/bullmq/issues/977) 참조 ([b03aaf1](https://github.com/taskforcesh/bullmq/commit/b03aaf10ca694745d143def2129f952b9bac18a6))

## [1.63.0](https://github.com/taskforcesh/bullmq/compare/v1.62.0...v1.63.0) (2021-12-31)

#### 기능

* **job:** 정적 메서드에 generic types 사용 ([#975](https://github.com/taskforcesh/bullmq/issues/975)) ([f78f4d0](https://github.com/taskforcesh/bullmq/commit/f78f4d0f75adb5c73558b3e8cf511db22f972791))

## [1.62.0](https://github.com/taskforcesh/bullmq/compare/v1.61.0...v1.62.0) (2021-12-31)

#### 버그 수정

* progress 및 Queue3 클래스에 deprecated 태그 추가 ([#973](https://github.com/taskforcesh/bullmq/issues/973)) ([6abdf5b](https://github.com/taskforcesh/bullmq/commit/6abdf5b66717cc8bc8ddb048029f7d9b92509942))

#### 기능

* **queue:** 더 나은 이벤트 타이핑 추가 ([#971](https://github.com/taskforcesh/bullmq/issues/971)) ([596fd7b](https://github.com/taskforcesh/bullmq/commit/596fd7b260f2e95607f0eb4ff9553fb35137ec54))

## [1.61.0](https://github.com/taskforcesh/bullmq/compare/v1.60.0...v1.61.0) (2021-12-29)

#### 기능

* **queue:** 작업에 제네릭 타이핑 재사용 ([5c10818](https://github.com/taskforcesh/bullmq/commit/5c10818d90724cccdf510f0358c01233aeac77e4))
* **worker:** 작업에 제네릭 타이핑 재사용 ([9adcdb7](https://github.com/taskforcesh/bullmq/commit/9adcdb798b4ee55835123a9f3d04c1397b176dc1))

## [1.60.0](https://github.com/taskforcesh/bullmq/compare/v1.59.4...v1.60.0) (2021-12-29)

#### 기능

* **queue-scheduler:** 더 나은 이벤트 타이핑 추가 ([#963](https://github.com/taskforcesh/bullmq/issues/963)) ([b23c006](https://github.com/taskforcesh/bullmq/commit/b23c006e2bfce8a0709f0eb8e8739261b68c2f48))

### [1.59.4](https://github.com/taskforcesh/bullmq/compare/v1.59.3...v1.59.4) (2021-12-21)

#### 버그 수정

* typescript를 3.9.10으로 다운그레이드하여 [#917](https://github.com/taskforcesh/bullmq/issues/917) 수정 ([#960](https://github.com/taskforcesh/bullmq/issues/960)) ([4e51fe0](https://github.com/taskforcesh/bullmq/commit/4e51fe00751092ee8f521039a3f2b41d881b71ae))

### [1.59.3](https://github.com/taskforcesh/bullmq/compare/v1.59.2...v1.59.3) (2021-12-21)

#### 버그 수정

* **worker:** undefined moveToActive 수정 ([87e8cab](https://github.com/taskforcesh/bullmq/commit/87e8cab16dad6f8bd9e9ec369ef7e79f471180be))

### [1.59.2](https://github.com/taskforcesh/bullmq/compare/v1.59.1...v1.59.2) (2021-12-17)

#### 버그 수정

* **package:** jsnext:main prop 추가 ([#953](https://github.com/taskforcesh/bullmq/issues/953)) ([1a92bf7](https://github.com/taskforcesh/bullmq/commit/1a92bf7d41860f758841c5a833c1192d9a84a25f))

### [1.59.1](https://github.com/taskforcesh/bullmq/compare/v1.59.0...v1.59.1) (2021-12-17)

#### 버그 수정

* lua 파일을 올바른 위치로 복사 ([2be1120](https://github.com/taskforcesh/bullmq/commit/2be1120974692ee57ec00e30d6dbbef670d88a1e))

## [1.59.0](https://github.com/taskforcesh/bullmq/compare/v1.58.0...v1.59.0) (2021-12-17)

#### 버그 수정

* dist 경로 수정 ([067d4c2](https://github.com/taskforcesh/bullmq/commit/067d4c2009b877f8bf6e6145507a41a53e5f7af3))

#### 기능

* bullmq도 ESM으로 export ([e97e5b5](https://github.com/taskforcesh/bullmq/commit/e97e5b52b079adf2ed79f7cb61699e40a91e34e8))

## [1.58.0](https://github.com/taskforcesh/bullmq/compare/v1.57.4...v1.58.0) (2021-12-15)

#### 기능

* **worker:** 더 나은 이벤트 타이핑 추가 ([#940](https://github.com/taskforcesh/bullmq/issues/940)) ([a326d4f](https://github.com/taskforcesh/bullmq/commit/a326d4f27e96ffa462a908ac14356d29839ff073))

### [1.57.4](https://github.com/taskforcesh/bullmq/compare/v1.57.3...v1.57.4) (2021-12-14)

#### 버그 수정

* **move-to-active:** moveToActive 호출에 try catch 추가 ([#933](https://github.com/taskforcesh/bullmq/issues/933)) ([bab45b0](https://github.com/taskforcesh/bullmq/commit/bab45b05d08c625557e2df65921e12f48081d39c))
* **redis-connection:** 클러스터 redisOptions config 고려 ([#934](https://github.com/taskforcesh/bullmq/issues/934)) ([5130f63](https://github.com/taskforcesh/bullmq/commit/5130f63ad969efa9649ab8f9abf36a72e8f553f4))

### [1.57.3](https://github.com/taskforcesh/bullmq/compare/v1.57.2...v1.57.3) (2021-12-14)

#### 버그 수정

* debug console.error 제거 ([#932](https://github.com/taskforcesh/bullmq/issues/932)) ([271aac3](https://github.com/taskforcesh/bullmq/commit/271aac3417bc7f76ac02435b456552677b2847db))

### [1.57.2](https://github.com/taskforcesh/bullmq/compare/v1.57.1...v1.57.2) (2021-12-11)

#### 버그 수정

* **connection:** deprecation 메시지를 console log로 출력하기 위해 instance options 확인 ([#927](https://github.com/taskforcesh/bullmq/issues/927)) ([fc1e2b9](https://github.com/taskforcesh/bullmq/commit/fc1e2b9f3f20db53f9dc7ecdfa4644f02acc9f83))

#### 성능 개선

* **add-job:** 부모 데이터를 json으로 저장 ([#859](https://github.com/taskforcesh/bullmq/issues/859)) ([556d4ee](https://github.com/taskforcesh/bullmq/commit/556d4ee427090f60270945a7fd438e2595bb43e9))

### [1.57.1](https://github.com/taskforcesh/bullmq/compare/v1.57.0...v1.57.1) (2021-12-11)

#### 버그 수정

* **worker:** block timeout 처리 개선 ([be4c933](https://github.com/taskforcesh/bullmq/commit/be4c933ae0a7a790d24a081b2ed4e7e1c0216e47))

## [1.57.0](https://github.com/taskforcesh/bullmq/compare/v1.56.0...v1.57.0) (2021-12-08)

#### 기능

* **queue-events:** 더 나은 이벤트 타이핑 추가 ([#919](https://github.com/taskforcesh/bullmq/issues/919)) ([e980080](https://github.com/taskforcesh/bullmq/commit/e980080767bc56ae09a5c5cf33728a85a023bb42))

## [1.56.0](https://github.com/taskforcesh/bullmq/compare/v1.55.1...v1.56.0) (2021-12-06)

#### 버그 수정

* 완료 시 남은 작업이 없으면 drain 이벤트 emit ([9ad78a9](https://github.com/taskforcesh/bullmq/commit/9ad78a91c0a4a74cf84bd77d351d98195104f0b6))
* **worker:** worker 이름 설정에 client 사용 ([af65c2c](https://github.com/taskforcesh/bullmq/commit/af65c2cd0d3fb232c617b018d4991f3276db11ea))

#### 기능

* **worker:** moveToActive를 protected로 변경 ([d2897ee](https://github.com/taskforcesh/bullmq/commit/d2897ee7bbf4aee5251ac4fb28705f2bebbe7bfe))

### [1.55.1](https://github.com/taskforcesh/bullmq/compare/v1.55.0...v1.55.1) (2021-12-03)

#### 버그 수정

* **worker:** 작업 대기 후 항상 active로 이동 시도 ([#914](https://github.com/taskforcesh/bullmq/issues/914)) ([97b7084](https://github.com/taskforcesh/bullmq/commit/97b708451bf4ce14a461a50f8a24d14b0e40dd4b))

## [1.55.0](https://github.com/taskforcesh/bullmq/compare/v1.54.6...v1.55.0) (2021-12-02)

#### 기능

* **script-loader:** include 지원이 있는 lua script loader ([#897](https://github.com/taskforcesh/bullmq/issues/897)) ([64b6ccf](https://github.com/taskforcesh/bullmq/commit/64b6ccf2a373b40d7ea763b3d35cf34f36ba11da))

### [1.54.6](https://github.com/taskforcesh/bullmq/compare/v1.54.5...v1.54.6) (2021-11-30)

#### 버그 수정

* **stalled:** 작업이 허용 한도를 넘게 stalled 상태가 되면 finishedOn 저장 ([#900](https://github.com/taskforcesh/bullmq/issues/900)) ([eb89edf](https://github.com/taskforcesh/bullmq/commit/eb89edf2f4eb85dedb1485de32e79331940a654f))

### [1.54.5](https://github.com/taskforcesh/bullmq/compare/v1.54.4...v1.54.5) (2021-11-26)

#### 버그 수정

* **tsconfig:** node types만 포함 ([#895](https://github.com/taskforcesh/bullmq/issues/895)) ([5f4fdca](https://github.com/taskforcesh/bullmq/commit/5f4fdca5f416f2cd9d83eb0fba84e56c24320b63))

### [1.54.4](https://github.com/taskforcesh/bullmq/compare/v1.54.3...v1.54.4) (2021-11-24)

#### 버그 수정

* **child-processor:** progress 메서드에 대한 deprecation 경고 추가 ([#890](https://github.com/taskforcesh/bullmq/issues/890)) ([f80b19a](https://github.com/taskforcesh/bullmq/commit/f80b19a5aa85413b8906aa0fac1bfd09bec990cb))

### [1.54.3](https://github.com/taskforcesh/bullmq/compare/v1.54.2...v1.54.3) (2021-11-22)

#### 버그 수정

* **clean:** lua script에서 range 값 사용 ([#885](https://github.com/taskforcesh/bullmq/issues/885)) ([02ef63a](https://github.com/taskforcesh/bullmq/commit/02ef63a8163e627a270a1c1bd74989a67c3f15f7))

### [1.54.2](https://github.com/taskforcesh/bullmq/compare/v1.54.1...v1.54.2) (2021-11-20)

#### 버그 수정

* **job:** 새 연산자를 사용할 때 this 사용 ([#884](https://github.com/taskforcesh/bullmq/issues/884)) ([7b84283](https://github.com/taskforcesh/bullmq/commit/7b842839e1d30967ebf15b901033e3b31e929df8))

### [1.54.1](https://github.com/taskforcesh/bullmq/compare/v1.54.0...v1.54.1) (2021-11-19)

#### 버그 수정

* **job:** 확장을 위해 private attributes를 protected로 변경 ([#882](https://github.com/taskforcesh/bullmq/issues/882)) ([ffcc3f0](https://github.com/taskforcesh/bullmq/commit/ffcc3f083c23e6de3587c38fb7aacb2e19085351))

## [1.54.0](https://github.com/taskforcesh/bullmq/compare/v1.53.0...v1.54.0) (2021-11-17)

#### 기능

* **load-includes:** 확장에서 재사용할 수 있도록 includes export ([#877](https://github.com/taskforcesh/bullmq/issues/877)) ([b56c4a9](https://github.com/taskforcesh/bullmq/commit/b56c4a9cf2ecebb44481618026589162be61680a))

## [1.53.0](https://github.com/taskforcesh/bullmq/compare/v1.52.2...v1.53.0) (2021-11-16)

#### 기능

* **queue-events:** cleaned 이벤트 추가 ([#865](https://github.com/taskforcesh/bullmq/issues/865)) ([b3aebad](https://github.com/taskforcesh/bullmq/commit/b3aebad8a62311e135d53be2e7c5e47740547465))

### [1.52.2](https://github.com/taskforcesh/bullmq/compare/v1.52.1...v1.52.2) (2021-11-14)

#### 버그 수정

* **worker:** pro extension을 위해 private attributes를 protected로 변경 ([#874](https://github.com/taskforcesh/bullmq/issues/874)) ([1c73881](https://github.com/taskforcesh/bullmq/commit/1c738819b49f206688ed7b3b9d103077045e1b05))

### [1.52.1](https://github.com/taskforcesh/bullmq/compare/v1.52.0...v1.52.1) (2021-11-12)

#### 성능 개선

* **clean:** limit param과 함께 호출될 때 clean 메서드 속도 개선 ([#864](https://github.com/taskforcesh/bullmq/issues/864)) ([09b5cb4](https://github.com/taskforcesh/bullmq/commit/09b5cb45a79c4bc53a52d540918c22477a066e16))

## [1.52.0](https://github.com/taskforcesh/bullmq/compare/v1.51.3...v1.52.0) (2021-11-11)

#### 기능

* **queue:** waiting 이벤트 타입 선언 추가 ([#872](https://github.com/taskforcesh/bullmq/issues/872)) ([f29925d](https://github.com/taskforcesh/bullmq/commit/f29925da3b12f573582ea188ec386e86023cefc9))

### [1.51.3](https://github.com/taskforcesh/bullmq/compare/v1.51.2...v1.51.3) (2021-11-04)

#### 버그 수정

* **move-to-failed:** 스크립트 실행을 막는 closing 체크 삭제 ([#858](https://github.com/taskforcesh/bullmq/issues/858)) fixes [#834](https://github.com/taskforcesh/bullmq/issues/834) ([d50814f](https://github.com/taskforcesh/bullmq/commit/d50814f864448c10fec8e93651a2095fa4ef3f4e))

### [1.51.2](https://github.com/taskforcesh/bullmq/compare/v1.51.1...v1.51.2) (2021-11-03)

#### 버그 수정

* **flow:** FlowJob opts에서 repeat 옵션 제거 ([#853](https://github.com/taskforcesh/bullmq/issues/853)) fixes [#851](https://github.com/taskforcesh/bullmq/issues/851) ([c9ee2f1](https://github.com/taskforcesh/bullmq/commit/c9ee2f100a23aa24034598b7d452c69720d7aabd))

### [1.51.1](https://github.com/taskforcesh/bullmq/compare/v1.51.0...v1.51.1) (2021-10-29)

#### 버그 수정

* **commands:** includes lua scripts 복사 ([#843](https://github.com/taskforcesh/bullmq/issues/843)) fixes [#837](https://github.com/taskforcesh/bullmq/issues/837) ([cab33e0](https://github.com/taskforcesh/bullmq/commit/cab33e08bc78bd3c45b86158a818100beeb06d81))

## [1.51.0](https://github.com/taskforcesh/bullmq/compare/v1.50.7...v1.51.0) (2021-10-28)

#### 기능

* **flow:** 작업을 지속적으로 추가하는 경우 고려 ([#828](https://github.com/taskforcesh/bullmq/issues/828)) fixes [#826](https://github.com/taskforcesh/bullmq/issues/826) ([b0fde69](https://github.com/taskforcesh/bullmq/commit/b0fde69f4370160a891e4654485c09745066b80b))

### [1.50.7](https://github.com/taskforcesh/bullmq/compare/v1.50.6...v1.50.7) (2021-10-28)

#### 버그 수정

* enableReadyCheck, maxRetriesPerRequest를 override하여 재연결 문제 수정 ([09ba358](https://github.com/taskforcesh/bullmq/commit/09ba358b6f761bdc52b0f5b2aa315cc6c2a9db6e))
* **queue-base:** connection 누락 시 deprecation 경고 ([2f79802](https://github.com/taskforcesh/bullmq/commit/2f79802378d7e015b5d0702945a71c1c2073251e))

### [1.50.6](https://github.com/taskforcesh/bullmq/compare/v1.50.5...v1.50.6) (2021-10-28)

#### 버그 수정

* **queue-base:** 연결 지원 중단 경고 표시 ([#832](https://github.com/taskforcesh/bullmq/issues/832)) [#829](https://github.com/taskforcesh/bullmq/issues/829) 수정 ([5d023fe](https://github.com/taskforcesh/bullmq/commit/5d023fe7b671a2547398fd68995ccd85216cc7a5))

### [1.50.5](https://github.com/taskforcesh/bullmq/compare/v1.50.4...v1.50.5) (2021-10-21)

#### 버그 수정

* **child-pool:** 프로세스 `stdout` 및 `stderr`를 파이프로 연결([#822](https://github.com/taskforcesh/bullmq/issues/822)) [#821](https://github.com/taskforcesh/bullmq/issues/821) 수정 ([13f5c62](https://github.com/taskforcesh/bullmq/commit/13f5c62174925e4638acda6a9de379668048189d))

### [1.50.4](https://github.com/taskforcesh/bullmq/compare/v1.50.3...v1.50.4) (2021-10-20)

#### 버그 수정

* sharedConnection 옵션을 worker 베이스 클래스에 올바르게 전달 ([56557f1](https://github.com/taskforcesh/bullmq/commit/56557f1c0c3fb04bc3dd8824819c2d4367324c3b))

### [1.50.3](https://github.com/taskforcesh/bullmq/compare/v1.50.2...v1.50.3) (2021-10-18)

#### 버그 수정

* **msgpackr:** esm 번들러 지원을 위해 버전을 1.4.6으로 업그레이드 ([#818](https://github.com/taskforcesh/bullmq/issues/818)) [#813](https://github.com/taskforcesh/bullmq/issues/813) 수정 ([913d7a9](https://github.com/taskforcesh/bullmq/commit/913d7a9a892d2c7e2fa5822367355c2dee888583))

### [1.50.2](https://github.com/taskforcesh/bullmq/compare/v1.50.1...v1.50.2) (2021-10-12)

#### 버그 수정

* **msgpack:** msgpack을 msgpackr로 교체 ([dc13a75](https://github.com/taskforcesh/bullmq/commit/dc13a75374bbd29fefbf3e56f822e763df3712d9))

### [1.50.1](https://github.com/taskforcesh/bullmq/compare/v1.50.0...v1.50.1) (2021-10-12)

#### 버그 수정

* **queue-getters:** 처음 2개 작업만 가져오던 문제 ([653873a](https://github.com/taskforcesh/bullmq/commit/653873a6a86dd6c3e1afc3142efbe11014d80557))

## [1.50.0](https://github.com/taskforcesh/bullmq/compare/v1.49.0...v1.50.0) (2021-10-12)

#### 기능

* BullMQ 위에 확장을 더 쉽게 구축할 수 있도록 개선 ([b1a9e64](https://github.com/taskforcesh/bullmq/commit/b1a9e64a9184addc0b8245a04013e1c896e9c2bc))

## [1.49.0](https://github.com/taskforcesh/bullmq/compare/v1.48.3...v1.49.0) (2021-10-08)

#### 기능

* **sandboxed-process:** init-failed 오류 처리 ([#797](https://github.com/taskforcesh/bullmq/issues/797)) ([5d2f553](https://github.com/taskforcesh/bullmq/commit/5d2f55342b19ee99d34f8d8003f09359cfe17d4f))

### [1.48.3](https://github.com/taskforcesh/bullmq/compare/v1.48.2...v1.48.3) (2021-10-05)

#### 버그 수정

* **change-delay:** 지연값에 현재 시간 추가 ([#789](https://github.com/taskforcesh/bullmq/issues/789)) [#787](https://github.com/taskforcesh/bullmq/issues/787) 수정 ([4a70def](https://github.com/taskforcesh/bullmq/commit/4a70def6e85cf9ea384ec5f38c3c4f83e4eb523c))

### [1.48.2](https://github.com/taskforcesh/bullmq/compare/v1.48.1...v1.48.2) (2021-09-24)

#### 성능 개선

* **obliterate:** 사용되지 않는 변수 전달하지 않음 ([#766](https://github.com/taskforcesh/bullmq/issues/766)) ([e9abfa6](https://github.com/taskforcesh/bullmq/commit/e9abfa6f821064901770a9b72adfb00cac96154c))

### [1.48.1](https://github.com/taskforcesh/bullmq/compare/v1.48.0...v1.48.1) (2021-09-23)

#### 버그 수정

* **obliterate:** dependencies 및 processed 키 고려 ([#765](https://github.com/taskforcesh/bullmq/issues/765)) ([fd6bad8](https://github.com/taskforcesh/bullmq/commit/fd6bad8c7444c21e6f1d67611a28f8e4aace293d))

## [1.48.0](https://github.com/taskforcesh/bullmq/compare/v1.47.2...v1.48.0) (2021-09-23)

#### 기능

* **queue:** drain lua 스크립트 추가 ([#764](https://github.com/taskforcesh/bullmq/issues/764)) ([2daa698](https://github.com/taskforcesh/bullmq/commit/2daa698a7cc5dc8a6cd087b2d29356bc02fb4944))

### [1.47.2](https://github.com/taskforcesh/bullmq/compare/v1.47.1...v1.47.2) (2021-09-22)

#### 버그 수정

* **flow-producer:** add 메서드에서 기본 prefix 사용 ([#763](https://github.com/taskforcesh/bullmq/issues/763)) [#762](https://github.com/taskforcesh/bullmq/issues/762) 수정 ([fffdb55](https://github.com/taskforcesh/bullmq/commit/fffdb55f37917776494a4471673ef4564e0faab5))

### [1.47.1](https://github.com/taskforcesh/bullmq/compare/v1.47.0...v1.47.1) (2021-09-17)

#### 버그 수정

* **running:** 첫 번째 async 호출 전에 running 속성 이동 ([#756](https://github.com/taskforcesh/bullmq/issues/756)) ([f7f0660](https://github.com/taskforcesh/bullmq/commit/f7f066076bbe6cbcbf716ae622d55c6c1ae9b270))

## [1.47.0](https://github.com/taskforcesh/bullmq/compare/v1.46.7...v1.47.0) (2021-09-16)

#### 기능

* **queue-events:** 프로세스를 시작하지 않고 시작 ([#750](https://github.com/taskforcesh/bullmq/issues/750)) ([23a2360](https://github.com/taskforcesh/bullmq/commit/23a23606e727ca13b24924a1e867c6b557d6a09d))

### [1.46.7](https://github.com/taskforcesh/bullmq/compare/v1.46.6...v1.46.7) (2021-09-16)

#### 버그 수정

* **wait-for-job:** catch 블록 추가 및 error emit ([#749](https://github.com/taskforcesh/bullmq/issues/749)) ([b407f9a](https://github.com/taskforcesh/bullmq/commit/b407f9ac429c825984856eebca58bbfd16feb9d3))

### [1.46.6](https://github.com/taskforcesh/bullmq/compare/v1.46.5...v1.46.6) (2021-09-15)

#### 버그 수정

* **connection:** redis 연결이 복구되지 않는 경우에만 실패 처리 ([#751](https://github.com/taskforcesh/bullmq/issues/751)) ([8d59ced](https://github.com/taskforcesh/bullmq/commit/8d59ced27831a636f40ed4233eba3d4ac0654534))

### [1.46.5](https://github.com/taskforcesh/bullmq/compare/v1.46.4...v1.46.5) (2021-09-12)

#### 버그 수정

* **is-finished:** job 키가 없을 때 reject ([#746](https://github.com/taskforcesh/bullmq/issues/746)) [#85](https://github.com/taskforcesh/bullmq/issues/85) 수정 ([bd49bd2](https://github.com/taskforcesh/bullmq/commit/bd49bd20492676559072e5e16adb6d4e47afb22b))

### [1.46.4](https://github.com/taskforcesh/bullmq/compare/v1.46.3...v1.46.4) (2021-09-10)

#### 버그 수정

* **wait-until-finished:** isFinished가 failedReason 또는 returnValue 반환 ([#743](https://github.com/taskforcesh/bullmq/issues/743)) [#555](https://github.com/taskforcesh/bullmq/issues/555) 수정 ([63acae9](https://github.com/taskforcesh/bullmq/commit/63acae98cb083ec978ea17833819d1a21086be33))

### [1.46.3](https://github.com/taskforcesh/bullmq/compare/v1.46.2...v1.46.3) (2021-09-08)

#### 버그 수정

* **add-job:** parent 키가 없을 때 오류 발생 ([#739](https://github.com/taskforcesh/bullmq/issues/739)) ([d751070](https://github.com/taskforcesh/bullmq/commit/d751070f4ab6553c782341270574ccd253d309b8))

### [1.46.2](https://github.com/taskforcesh/bullmq/compare/v1.46.1...v1.46.2) (2021-09-07)

#### 버그 수정

* **queue-events:** 연결 중복 ([#733](https://github.com/taskforcesh/bullmq/issues/733)) [#726](https://github.com/taskforcesh/bullmq/issues/726) 수정 ([e2531ed](https://github.com/taskforcesh/bullmq/commit/e2531ed0c1dc195f210f8cf996e9ffe04c9e4b7d))

### [1.46.1](https://github.com/taskforcesh/bullmq/compare/v1.46.0...v1.46.1) (2021-09-06)

#### 버그 수정

* **redis-connection:** 종료 처리 개선, [#721](https://github.com/taskforcesh/bullmq/issues/721) 수정 ([9d8eb03](https://github.com/taskforcesh/bullmq/commit/9d8eb0306ef5e63c9d34ffd5c96fc15491da639d))

## [1.46.0](https://github.com/taskforcesh/bullmq/compare/v1.45.0...v1.46.0) (2021-09-02)

#### 기능

* **worker:** 프로세스를 시작하지 않고 시작 ([#724](https://github.com/taskforcesh/bullmq/issues/724)) ([af689e4](https://github.com/taskforcesh/bullmq/commit/af689e4e3945b9bc68bfc08c8f0ad57644206c5b)), closes [#436](https://github.com/taskforcesh/bullmq/issues/436)

## [1.45.0](https://github.com/taskforcesh/bullmq/compare/v1.44.3...v1.45.0) (2021-09-02)

#### 기능

* **queue-scheduler:** 프로세스를 시작하지 않고 시작 ([#729](https://github.com/taskforcesh/bullmq/issues/729)) ([f1932a7](https://github.com/taskforcesh/bullmq/commit/f1932a789af13da9b705a72d6f633f984a218862)), closes [#436](https://github.com/taskforcesh/bullmq/issues/436)

### [1.44.3](https://github.com/taskforcesh/bullmq/compare/v1.44.2...v1.44.3) (2021-09-02)

#### 버그 수정

* **queuescheduler:** shared connection 처리, [#721](https://github.com/taskforcesh/bullmq/issues/721) 수정 ([32a2b2e](https://github.com/taskforcesh/bullmq/commit/32a2b2eccfa3ba1516eacd71e334cae6c787ce4c))

### [1.44.2](https://github.com/taskforcesh/bullmq/compare/v1.44.1...v1.44.2) (2021-08-29)

#### 버그 수정

* **worker:** processing map 키에서 spread operator 사용 ([#720](https://github.com/taskforcesh/bullmq/issues/720)) ([32f1e57](https://github.com/taskforcesh/bullmq/commit/32f1e570a9a3369174a228f729f1d1330dcb6965))

### [1.44.1](https://github.com/taskforcesh/bullmq/compare/v1.44.0...v1.44.1) (2021-08-29)

#### 버그 수정

* **retry:** 실패하지 않은 job을 retry할 때 오류 발생 ([#717](https://github.com/taskforcesh/bullmq/issues/717)) ([bb9b192](https://github.com/taskforcesh/bullmq/commit/bb9b192e9a1a4f3c25374fcb8c0fb2159eb3f779))

## [1.44.0](https://github.com/taskforcesh/bullmq/compare/v1.43.0...v1.44.0) (2021-08-27)

#### 기능

* **queue-events:** waiting-children 이벤트 추가 ([#704](https://github.com/taskforcesh/bullmq/issues/704)) ([18b0b79](https://github.com/taskforcesh/bullmq/commit/18b0b7954313274a61fcc058380bfb9d682c059d))

## [1.43.0](https://github.com/taskforcesh/bullmq/compare/v1.42.1...v1.43.0) (2021-08-25)

#### 기능

* **events:** job 생성 시 added 이벤트 추가 ([#699](https://github.com/taskforcesh/bullmq/issues/699)) ([f533cc5](https://github.com/taskforcesh/bullmq/commit/f533cc55a43cf6ea78a60e85102f15b1c1ff69a0))

### [1.42.1](https://github.com/taskforcesh/bullmq/compare/v1.42.0...v1.42.1) (2021-08-23)

#### 버그 수정

* emit 호출을 throw/catch로 보호 ([79f879b](https://github.com/taskforcesh/bullmq/commit/79f879bf1bca1acea19485def361cc36f1d13b7e))

## [1.42.0](https://github.com/taskforcesh/bullmq/compare/v1.41.0...v1.42.0) (2021-08-20)

#### 기능

* **flows:** rate limit용 queuesOptions 추가 ([#692](https://github.com/taskforcesh/bullmq/issues/692)) ([6689ec3](https://github.com/taskforcesh/bullmq/commit/6689ec3fadd21904d9935f932c047f540ed8caf0)), closes [#621](https://github.com/taskforcesh/bullmq/issues/621)

## [1.41.0](https://github.com/taskforcesh/bullmq/compare/v1.40.4...v1.41.0) (2021-08-20)

#### 기능

* **flow:** bulk 추가 ([dc59fe6](https://github.com/taskforcesh/bullmq/commit/dc59fe62e57b6e761fe4d2ab6179a69dc4792399))

### [1.40.4](https://github.com/taskforcesh/bullmq/compare/v1.40.3...v1.40.4) (2021-08-06)

#### 버그 수정

* **rate-limiter:** groupKey가 undefined가 아닌지 확인 ([999b918](https://github.com/taskforcesh/bullmq/commit/999b91868814caf4c5c1ddee40798178b71e0ea8))

### [1.40.3](https://github.com/taskforcesh/bullmq/compare/v1.40.2...v1.40.3) (2021-08-06)

#### 버그 수정

* **redis-connection:** waitUntilReady에 error 이벤트 추가 ([ac4101e](https://github.com/taskforcesh/bullmq/commit/ac4101e3e798110c022d6c9f10f3b98f5e86b151))

### [1.40.2](https://github.com/taskforcesh/bullmq/compare/v1.40.1...v1.40.2) (2021-08-06)

#### 버그 수정

* clientCommandMessageReg를 utils로 이동 ([dd5d555](https://github.com/taskforcesh/bullmq/commit/dd5d5553fe768eb18b17b53c7f75e7066024e382))

### [1.40.1](https://github.com/taskforcesh/bullmq/compare/v1.40.0...v1.40.1) (2021-07-24)

#### 버그 수정

* 연결 실패 시 connection이 멈추는 문제, [#656](https://github.com/taskforcesh/bullmq/issues/656) 수정 ([c465611](https://github.com/taskforcesh/bullmq/commit/c465611ed76afd2adfd0e05a8babd6e369f5c310))

## [1.40.0](https://github.com/taskforcesh/bullmq/compare/v1.39.5...v1.40.0) (2021-07-22)

#### 기능

* **worker:** run loop에서 delay 오류 재시도 ([409fe7f](https://github.com/taskforcesh/bullmq/commit/409fe7fc09b87b7916a3362a463bb9e0f17ecea8))

### [1.39.5](https://github.com/taskforcesh/bullmq/compare/v1.39.4...v1.39.5) (2021-07-21)

#### 버그 수정

* **move-to-finished:** 완료 시 stalled job 제거 ([3867126](https://github.com/taskforcesh/bullmq/commit/38671261ccc00ca7fefa677663e45a40a92df555))

### [1.39.4](https://github.com/taskforcesh/bullmq/compare/v1.39.3...v1.39.4) (2021-07-21)

#### 버그 수정

* **repeatable:** 다음 repeatable job을 추가할 때 endDate 검증 ([1324cbb](https://github.com/taskforcesh/bullmq/commit/1324cbb4effd55e98c29d95a21afca7cd045b46c))

### [1.39.3](https://github.com/taskforcesh/bullmq/compare/v1.39.2...v1.39.3) (2021-07-16)

#### 버그 수정

* redis client 상태가 "wait"이면 연결 ([f711717](https://github.com/taskforcesh/bullmq/commit/f711717f56822aef43c9fd0440e30fad0876ba62))

### [1.39.2](https://github.com/taskforcesh/bullmq/compare/v1.39.1...v1.39.2) (2021-07-15)

#### 버그 수정

* **queue:** client가 닫혀 있으면 Queue 생성자가 queue options를 설정하려고 시도하지 않도록 보장 ([b40c6eb](https://github.com/taskforcesh/bullmq/commit/b40c6eb931a71d0ae9f6454eb70d84259a6981b7))

### [1.39.1](https://github.com/taskforcesh/bullmq/compare/v1.39.0...v1.39.1) (2021-07-15)

#### 버그 수정

* **sandbox:** updateProgress 메서드 이름 사용 ([27d62c3](https://github.com/taskforcesh/bullmq/commit/27d62c32b2fac091b2700d6077de593c9fda4c22))

## [1.39.0](https://github.com/taskforcesh/bullmq/compare/v1.38.1...v1.39.0) (2021-07-13)

#### 기능

* **worker+scheduler:** 헬스체크를 위한 "running" 속성 추가 ([aae358e](https://github.com/taskforcesh/bullmq/commit/aae358e067a0b6f20124751cffcdeaebac6eb7fd))

### [1.38.1](https://github.com/taskforcesh/bullmq/compare/v1.38.0...v1.38.1) (2021-07-12)

#### 버그 수정

* **reprocess:** added list에 job.id를 저장하지 않음 ([9c0605e](https://github.com/taskforcesh/bullmq/commit/9c0605e10f0bbdce94153d3f318d56c23bfd3269))

## [1.38.0](https://github.com/taskforcesh/bullmq/compare/v1.37.1...v1.38.0) (2021-07-12)

#### 기능

* **queue:** 누락된 events typings 추가 ([b42e78c](https://github.com/taskforcesh/bullmq/commit/b42e78c36cb6a6579a4c7cce1d7e969b230ff5b6))

### [1.37.1](https://github.com/taskforcesh/bullmq/compare/v1.37.0...v1.37.1) (2021-07-02)

#### 버그 수정

* **stalled-jobs:** stalled jobs를 배치 단위로 wait로 이동 ([a23fcb8](https://github.com/taskforcesh/bullmq/commit/a23fcb82d4ca20cbc4b8cd8b544b2d2eaddd86c3)), closes [#422](https://github.com/taskforcesh/bullmq/issues/422)

## [1.37.0](https://github.com/taskforcesh/bullmq/compare/v1.36.1...v1.37.0) (2021-06-30)

#### 기능

* **job:** 지연 작업을 위한 changeDelay 메서드 추가 ([f0a9f9c](https://github.com/taskforcesh/bullmq/commit/f0a9f9c6479062413abc0ac9a6f744329571a618))

### [1.36.1](https://github.com/taskforcesh/bullmq/compare/v1.36.0...v1.36.1) (2021-06-22)

#### 버그 수정

* **worker:** active event typing 변경 ([220b4f6](https://github.com/taskforcesh/bullmq/commit/220b4f619b30a8f04979e9abd0139e46d89b424d))

## [1.36.0](https://github.com/taskforcesh/bullmq/compare/v1.35.0...v1.36.0) (2021-06-20)

#### 버그 수정

* **queue-events:** drained typing 수정 ([9cf711d](https://github.com/taskforcesh/bullmq/commit/9cf711d4d4e7d8214dfd93a243c35d0bf135cdaf))

#### 기능

* **worker:** active event typing 추가 ([5508cdf](https://github.com/taskforcesh/bullmq/commit/5508cdf7cf372ae2f4af0ef576016eb901580671))
* **worker:** progress event typing 추가 ([119cb7c](https://github.com/taskforcesh/bullmq/commit/119cb7cd7a91c0f1866f5957faf2850afadbe709))

## [1.35.0](https://github.com/taskforcesh/bullmq/compare/v1.34.2...v1.35.0) (2021-06-19)

#### 기능

* **worker:** drained event typing 추가 ([ed5f315](https://github.com/taskforcesh/bullmq/commit/ed5f3155415693d2a6dbfb779397d53d74b704e2))

### [1.34.2](https://github.com/taskforcesh/bullmq/compare/v1.34.1...v1.34.2) (2021-06-18)

#### 버그 수정

* **worker:** processing functions를 await 처리 ([0566804](https://github.com/taskforcesh/bullmq/commit/056680470283f134b447a8ba39afa29e1e113585))

### [1.34.1](https://github.com/taskforcesh/bullmq/compare/v1.34.0...v1.34.1) (2021-06-18)

#### 버그 수정

* **redis-connection:** client에서 error event listener 제거 ([2d70fe7](https://github.com/taskforcesh/bullmq/commit/2d70fe7cc7d43673674ec2ba0204c10661b34e95))

## [1.34.0](https://github.com/taskforcesh/bullmq/compare/v1.33.1...v1.34.0) (2021-06-11)

#### 기능

* **job:** queueName 노출 ([8683bd4](https://github.com/taskforcesh/bullmq/commit/8683bd470cc7304f087d646fd40c5bc3acc1263c))

### [1.33.1](https://github.com/taskforcesh/bullmq/compare/v1.33.0...v1.33.1) (2021-06-10)

#### 버그 수정

* **job:** pagination을 위해 default opts 구조 분해 할당 ([73363a5](https://github.com/taskforcesh/bullmq/commit/73363a551f56608f8936ad1f730d0a9c778aafd2))

## [1.33.0](https://github.com/taskforcesh/bullmq/compare/v1.32.0...v1.33.0) (2021-06-10)

#### 기능

* **job:** getDependenciesCount 메서드 추가 ([ae39a4c](https://github.com/taskforcesh/bullmq/commit/ae39a4c77a958242cb445dbb32ae27b15a953653))

## [1.32.0](https://github.com/taskforcesh/bullmq/compare/v1.31.1...v1.32.0) (2021-06-07)

#### 기능

* **flow-producer:** getFlow 메서드 추가 ([ce93d04](https://github.com/taskforcesh/bullmq/commit/ce93d04c962686aff34f670f2decadadbf1cf4ca))

### [1.31.1](https://github.com/taskforcesh/bullmq/compare/v1.31.0...v1.31.1) (2021-06-07)

#### 버그 수정

* **worker:** removeOnComplete 시 processed key 제거 ([4ec1b73](https://github.com/taskforcesh/bullmq/commit/4ec1b739d6aeeb2fc21887b58f5978027ddcdb50))

## [1.31.0](https://github.com/taskforcesh/bullmq/compare/v1.30.2...v1.31.0) (2021-06-04)

#### 기능

* **job:** pagination을 지원하도록 getDependencies 확장 ([9b61bbb](https://github.com/taskforcesh/bullmq/commit/9b61bbb9160358f629cd458fa8dc4c9b6ebcd9f5))

### [1.30.2](https://github.com/taskforcesh/bullmq/compare/v1.30.1...v1.30.2) (2021-06-03)

#### 버그 수정

* **job:** processed jobs에 대해 getDependencies에서 결과 파싱 ([6fdc701](https://github.com/taskforcesh/bullmq/commit/6fdc7011ba910e5ca9c6d87926cc523ef38ef3ca))

### [1.30.1](https://github.com/taskforcesh/bullmq/compare/v1.30.0...v1.30.1) (2021-06-02)

#### 버그 수정

* **move-to-waiting-children:** opts를 optional로 설정 ([33bd76a](https://github.com/taskforcesh/bullmq/commit/33bd76a2cac9be450b5d76c6cfe16751c7569ceb))

## [1.30.0](https://github.com/taskforcesh/bullmq/compare/v1.29.1...v1.30.0) (2021-06-02)

#### 기능

* 일부 event typing 추가 ([934c004](https://github.com/taskforcesh/bullmq/commit/934c0040b0802bb67f44a979584405d795a8ab5e))

### [1.29.1](https://github.com/taskforcesh/bullmq/compare/v1.29.0...v1.29.1) (2021-05-31)

#### 버그 수정

* **move-stalled-jobs-to-wait:** queueEvents에 failedReason 전달 ([7c510b5](https://github.com/taskforcesh/bullmq/commit/7c510b542558bd4b1330371b73331f37b97a818d))

## [1.29.0](https://github.com/taskforcesh/bullmq/compare/v1.28.2...v1.29.0) (2021-05-31)

#### 기능

* 수동 처리를 위한 move to waiting children 추가 ([#477](https://github.com/taskforcesh/bullmq/issues/477)) ([f312f29](https://github.com/taskforcesh/bullmq/commit/f312f293b8cac79af9c14848ffd1b11b65a806c3))

### [1.28.2](https://github.com/taskforcesh/bullmq/compare/v1.28.1...v1.28.2) (2021-05-31)

#### 버그 수정

* **obliterate:** job logs 제거 ([ea91895](https://github.com/taskforcesh/bullmq/commit/ea918950d7696241047a23773cc13cd675209c4b))

### [1.28.1](https://github.com/taskforcesh/bullmq/compare/v1.28.0...v1.28.1) (2021-05-31)

#### 버그 수정

* **get-workers:** name에 strict equality 사용 fixes [#564](https://github.com/taskforcesh/bullmq/issues/564) ([4becfa6](https://github.com/taskforcesh/bullmq/commit/4becfa66e09dacf9830804898c45cb3317dcf438))

## [1.28.0](https://github.com/taskforcesh/bullmq/compare/v1.27.0...v1.28.0) (2021-05-24)

#### 기능

* **flow-producer:** client connection 노출 ([17d4263](https://github.com/taskforcesh/bullmq/commit/17d4263abfa57797535cd8773c4cc316ff5149d2))

## [1.27.0](https://github.com/taskforcesh/bullmq/compare/v1.26.5...v1.27.0) (2021-05-24)

#### 기능

* **repeat:** repeat에 immediately opt 추가 ([d095573](https://github.com/taskforcesh/bullmq/commit/d095573f8e7ce5911f777df48368382eceb99d6a))

### [1.26.5](https://github.com/taskforcesh/bullmq/compare/v1.26.4...v1.26.5) (2021-05-21)

#### 버그 수정

* **movetofinished:** events에 parent queue 사용 ([1b17b62](https://github.com/taskforcesh/bullmq/commit/1b17b62a794728a318f1079e73d07e33fe65c9c7))

### [1.26.4](https://github.com/taskforcesh/bullmq/compare/v1.26.3...v1.26.4) (2021-05-20)

#### 버그 수정

* **removejob:** processed hash 삭제 ([a2a5058](https://github.com/taskforcesh/bullmq/commit/a2a5058f18ab77ed4d0114d48f47e6144d632cbf))

### [1.26.3](https://github.com/taskforcesh/bullmq/compare/v1.26.2...v1.26.3) (2021-05-19)

#### 버그 수정

* pausing 시 connection이 재연결되도록 보장 fixes [#160](https://github.com/taskforcesh/bullmq/issues/160) ([f38fee8](https://github.com/taskforcesh/bullmq/commit/f38fee84def75dd8a38cbb8bfb5aa662485ddf91))

### [1.26.2](https://github.com/taskforcesh/bullmq/compare/v1.26.1...v1.26.2) (2021-05-18)

#### 버그 수정

* **getjoblogs:** reversed pagination 없음 ([fb0c3a5](https://github.com/taskforcesh/bullmq/commit/fb0c3a50f0d37851a8f35cb4c478259a63d93461))

### [1.26.1](https://github.com/taskforcesh/bullmq/compare/v1.26.0...v1.26.1) (2021-05-17)

#### 버그 수정

* **flow-producer:** children의 parentId로 custom jobId 사용 fixes [#552](https://github.com/taskforcesh/bullmq/issues/552) ([645b576](https://github.com/taskforcesh/bullmq/commit/645b576c1aabd8426ab77a68c199a594867cd729))

## [1.26.0](https://github.com/taskforcesh/bullmq/compare/v1.25.1...v1.26.0) (2021-05-16)

#### 기능

* **custombackoff:** 세 번째 파라미터로 job 제공 ([ddaf8dc](https://github.com/taskforcesh/bullmq/commit/ddaf8dc2f95ca336cb117a540edd4640d5d579e4))

### [1.25.2](https://github.com/taskforcesh/bullmq/compare/v1.25.1...v1.25.2) (2021-05-16)

#### 버그 수정

* **flow-producer:** children을 빈 배열로 하여 parent 처리 fixes [#547](https://github.com/taskforcesh/bullmq/issues/547) ([48168f0](https://github.com/taskforcesh/bullmq/commit/48168f07cbaed7ed522c68d127a0c7d5e4cb380e))

### [1.25.1](https://github.com/taskforcesh/bullmq/compare/v1.25.0...v1.25.1) (2021-05-13)

#### 버그 수정

* **addbulk:** repeat option을 고려하지 않아야 함 ([c85357e](https://github.com/taskforcesh/bullmq/commit/c85357e415b9ea66f845f751a4943b5c48c2bb18))

## [1.25.0](https://github.com/taskforcesh/bullmq/compare/v1.24.5...v1.25.0) (2021-05-11)

#### 기능

* **job:** job 생성 시 sizeLimit 옵션 추가 ([f10aeeb](https://github.com/taskforcesh/bullmq/commit/f10aeeb62520d20b31d35440524d147ac4adcc9c))

### [1.24.5](https://github.com/taskforcesh/bullmq/compare/v1.24.4...v1.24.5) (2021-05-08)

#### 버그 수정

* **deps:** lodash를 4.17.21로 업그레이드 ([6e90c3f](https://github.com/taskforcesh/bullmq/commit/6e90c3f0a3d2735875ebf44457b342629aa14572))

### [1.24.4](https://github.com/taskforcesh/bullmq/compare/v1.24.3...v1.24.4) (2021-05-07)

#### 버그 수정

* **cluster:** redis cluster 지원 추가 ([5a7dd14](https://github.com/taskforcesh/bullmq/commit/5a7dd145bd3ae11850cac6d1b4fb9b01af0e6766))
* **redisclient:** import에서 types를 참조하지 않음 ([022fc04](https://github.com/taskforcesh/bullmq/commit/022fc042a17c1754af7d74acabb7dd5c397576ab))

### [1.24.3](https://github.com/taskforcesh/bullmq/compare/v1.24.2...v1.24.3) (2021-05-05)

#### 버그 수정

* **sandbox:** stdout을 올바르게 리디렉션 ([#525](https://github.com/taskforcesh/bullmq/issues/525)) ([c8642a0](https://github.com/taskforcesh/bullmq/commit/c8642a0724dc3d2f77abc4b5d6d24efa67c1e592))

### [1.24.2](https://github.com/taskforcesh/bullmq/compare/v1.24.1...v1.24.2) (2021-05-05)

#### 버그 수정

* **sandbox:** 손상된 processor 파일 처리 ([2326983](https://github.com/taskforcesh/bullmq/commit/23269839af0be2f7cf2a4f6062563d30904bc259))

### [1.24.1](https://github.com/taskforcesh/bullmq/compare/v1.24.0...v1.24.1) (2021-05-05)

#### 버그 수정

* **queueevents:** active type 추가 fixes [#519](https://github.com/taskforcesh/bullmq/issues/519) ([10af883](https://github.com/taskforcesh/bullmq/commit/10af883db849cf9392b26724903f88752d9be92c))

## [1.24.0](https://github.com/taskforcesh/bullmq/compare/v1.23.1...v1.24.0) (2021-05-03)

#### 기능

* non-blocking `getNextJob` 옵션 추가 ([13ce2cf](https://github.com/taskforcesh/bullmq/commit/13ce2cfd4ccd64f45567df31de11af95b0fe67d9))

### [1.23.1](https://github.com/taskforcesh/bullmq/compare/v1.23.0...v1.23.1) (2021-05-03)

#### 버그 수정

* `job.waitUntilFinished()`의 반환 타입 추가 ([59ede97](https://github.com/taskforcesh/bullmq/commit/59ede976061a738503f70d9eb0c92a4b1d6ae4a3))

## [1.23.0](https://github.com/taskforcesh/bullmq/compare/v1.22.2...v1.23.0) (2021-04-30)

#### 기능

* **job:** `addBulk`에 parent opts 전달 ([7f21615](https://github.com/taskforcesh/bullmq/commit/7f216153293e45c4f33f2592561c925ca4464d44))

### [1.22.2](https://github.com/taskforcesh/bullmq/compare/v1.22.1...v1.22.2) (2021-04-29)

#### 버그 수정

* 누락된 Redis Cluster 타입 추가, [#406](https://github.com/taskforcesh/bullmq/issues/406) 수정 ([07743ff](https://github.com/taskforcesh/bullmq/commit/07743ff310ad716802afdd5bdc6844eb5296318e))

### [1.22.1](https://github.com/taskforcesh/bullmq/compare/v1.22.0...v1.22.1) (2021-04-28)

#### 버그 수정

* **addjob:** redis cluster CROSSSLOT 수정 ([a5fd1d7](https://github.com/taskforcesh/bullmq/commit/a5fd1d7a0713585d11bd862bfe2d426d5242bd3c))

## [1.22.0](https://github.com/taskforcesh/bullmq/compare/v1.21.0...v1.22.0) (2021-04-28)

#### 기능

* **jobcreate:** `job.create`에서 parent 전달 허용 ([ede3626](https://github.com/taskforcesh/bullmq/commit/ede3626b65fb5d3f4cebc55c813e9fa4b482b887))

## [1.21.0](https://github.com/taskforcesh/bullmq/compare/v1.20.6...v1.21.0) (2021-04-26)

#### 기능

* `addNextRepeatableJob` 타이핑 추가 ([a3be937](https://github.com/taskforcesh/bullmq/commit/a3be9379e29ae3e01264e2269e8b03aa614fd42c))

### [1.20.6](https://github.com/taskforcesh/bullmq/compare/v1.20.5...v1.20.6) (2021-04-25)

#### 버그 수정

* **movetocompleted:** 자식 작업보다 먼저 완료되지 않도록 수정 ([812ff66](https://github.com/taskforcesh/bullmq/commit/812ff664b3e162dd87831ca04ebfdb783cc7ae5b))

### [1.20.5](https://github.com/taskforcesh/bullmq/compare/v1.20.4...v1.20.5) (2021-04-23)

#### 버그 수정

* **obliterate:** 다수의 작업을 올바르게 제거 ([b5ae4ce](https://github.com/taskforcesh/bullmq/commit/b5ae4ce92aeaf000408ffbbcd22d829cee20f2f8))

### [1.20.4](https://github.com/taskforcesh/bullmq/compare/v1.20.3...v1.20.4) (2021-04-23)

#### 버그 수정

* barrel에 대한 내부 의존성 제거, [#469](https://github.com/taskforcesh/bullmq/issues/469) 수정 ([#495](https://github.com/taskforcesh/bullmq/issues/495)) ([60dbeed](https://github.com/taskforcesh/bullmq/commit/60dbeed7ff1d9b6cb0e35590713fee8a7be09477))

### [1.20.3](https://github.com/taskforcesh/bullmq/compare/v1.20.2...v1.20.3) (2021-04-23)

#### 버그 수정

* **flows:** 타입 정의 수정, [#492](https://github.com/taskforcesh/bullmq/issues/492) 해결 ([a77f80b](https://github.com/taskforcesh/bullmq/commit/a77f80bc07e7627f512323f0dcc9141fe408809e))

### [1.20.2](https://github.com/taskforcesh/bullmq/compare/v1.20.1...v1.20.2) (2021-04-22)

#### 버그 수정

* **movetodelayed:** 작업이 active 상태인지 확인 ([4e63f70](https://github.com/taskforcesh/bullmq/commit/4e63f70aac367d4dd695bbe07c72a08a82a65d97))

### [1.20.1](https://github.com/taskforcesh/bullmq/compare/v1.20.0...v1.20.1) (2021-04-22)

#### 버그 수정

* **worker:** processor function에서 token을 선택 사항으로 변경, [#490](https://github.com/taskforcesh/bullmq/issues/490) 해결 ([3940bd7](https://github.com/taskforcesh/bullmq/commit/3940bd71c6faf3bd5fce572b9c1f11cb5b5d2123))

## [1.20.0](https://github.com/taskforcesh/bullmq/compare/v1.19.3...v1.20.0) (2021-04-21)

#### 기능

* **worker:** processor function에서 token 전달 ([2249724](https://github.com/taskforcesh/bullmq/commit/2249724b1bc6fbf40b0291400011f201fd02dab3))

### [1.19.3](https://github.com/taskforcesh/bullmq/compare/v1.19.2...v1.19.3) (2021-04-20)

#### 버그 수정

* **movetocompleted:** 작업이 active 상태가 아니면 오류를 던지도록 수정 ([c2fe5d2](https://github.com/taskforcesh/bullmq/commit/c2fe5d292fcf8ac2e53906c30282df69d43321b1))

### [1.19.2](https://github.com/taskforcesh/bullmq/compare/v1.19.1...v1.19.2) (2021-04-19)

#### 버그 수정

* **worker:** base class connection 종료 [#451](https://github.com/taskforcesh/bullmq/issues/451) ([0875306](https://github.com/taskforcesh/bullmq/commit/0875306ae801a7cbfe04758dc2481cb86ca2ef69))

### [1.19.1](https://github.com/taskforcesh/bullmq/compare/v1.19.0...v1.19.1) (2021-04-19)

#### 버그 수정

* `obliterate` 시 repeatable 제거 ([1c5e581](https://github.com/taskforcesh/bullmq/commit/1c5e581a619ba707863c2a6e9f3e5f6eadfbe64f))

## [1.19.0](https://github.com/taskforcesh/bullmq/compare/v1.18.2...v1.19.0) (2021-04-19)

#### 기능

* limiter에 `workerDelay` 옵션 추가 ([9b6ab8a](https://github.com/taskforcesh/bullmq/commit/9b6ab8ad4bc0a94068f3bc707ad9c0ed01596068))

### [1.18.2](https://github.com/taskforcesh/bullmq/compare/v1.18.1...v1.18.2) (2021-04-16)

#### 버그 수정

* Job에 `parentKey` 속성 추가 ([febc60d](https://github.com/taskforcesh/bullmq/commit/febc60dba94c29b85be3e1bc2547fa83ed932806))

### [1.18.1](https://github.com/taskforcesh/bullmq/compare/v1.18.0...v1.18.1) (2021-04-16)

#### 버그 수정

* Flow 클래스를 FlowProducer 클래스로 이름 변경 ([c64321d](https://github.com/taskforcesh/bullmq/commit/c64321d03e2af7cee88eaf6df6cd2e5b7840ae64))

## [1.18.0](https://github.com/taskforcesh/bullmq/compare/v1.17.0...v1.18.0) (2021-04-16)

#### 기능

* flows에 remove 지원 추가 ([4e8a7ef](https://github.com/taskforcesh/bullmq/commit/4e8a7efd53f918937478ae13f5da7dee9ea9d8b3))

## [1.17.0](https://github.com/taskforcesh/bullmq/compare/v1.16.2...v1.17.0) (2021-04-16)

#### 기능

* **job:** waiting-children 상태 고려 ([2916dd5](https://github.com/taskforcesh/bullmq/commit/2916dd5d7ba9438d2eae66436899d32ec8ac0e91))

### [1.16.2](https://github.com/taskforcesh/bullmq/compare/v1.16.1...v1.16.2) (2021-04-14)

#### 버그 수정

* lua 스크립트를 순차적으로 읽도록 수정 ([69e73b8](https://github.com/taskforcesh/bullmq/commit/69e73b87bc6855623240a7b1a45368a7914b23b7))

### [1.16.1](https://github.com/taskforcesh/bullmq/compare/v1.16.0...v1.16.1) (2021-04-12)

#### 버그 수정

* **flow:** 상대 의존성 경로 수정, [#466](https://github.com/taskforcesh/bullmq/issues/466) 해결 ([d104bf8](https://github.com/taskforcesh/bullmq/commit/d104bf802d6d1000ac1ccd781fa7a07bce2fe140))

## [1.16.0](https://github.com/taskforcesh/bullmq/compare/v1.15.1...v1.16.0) (2021-04-12)

#### 기능

* flows(부모-자식 의존성) 지원 추가 ([#454](https://github.com/taskforcesh/bullmq/issues/454)) ([362212c](https://github.com/taskforcesh/bullmq/commit/362212c58c4be36b5435df862503699deb8bb79c))

### [1.15.1](https://github.com/taskforcesh/bullmq/compare/v1.15.0...v1.15.1) (2021-03-19)

#### 버그 수정

* **obliterate:** 더 안전한 구현 ([82f571f](https://github.com/taskforcesh/bullmq/commit/82f571f2548c61c776b897fd1c5050bb09c8afca))

## [1.15.0](https://github.com/taskforcesh/bullmq/compare/v1.14.8...v1.15.0) (2021-03-18)

#### 기능

* 큐를 "obliterate"하는 메서드 추가, [#430](https://github.com/taskforcesh/bullmq/issues/430) 수정 ([624be0e](https://github.com/taskforcesh/bullmq/commit/624be0ed48159c2aa405025938925a723330e0c2))

### [1.14.8](https://github.com/taskforcesh/bullmq/compare/v1.14.7...v1.14.8) (2021-03-06)

#### 버그 수정

* TS 4.1 및 4.2 호환을 위해 promise 타입 명시. ([#418](https://github.com/taskforcesh/bullmq/issues/418)) ([702f609](https://github.com/taskforcesh/bullmq/commit/702f609b410d8b0652c2d0504a8a67526966fdc3))

### [1.14.7](https://github.com/taskforcesh/bullmq/compare/v1.14.6...v1.14.7) (2021-02-16)

#### 버그 수정

* QueueBaseOptions의 "client" 속성 제거 ([#324](https://github.com/taskforcesh/bullmq/issues/324)) ([e0b9e71](https://github.com/taskforcesh/bullmq/commit/e0b9e71c4da4a93af54c4386af461c61ab5f146c))

### [1.14.6](https://github.com/taskforcesh/bullmq/compare/v1.14.5...v1.14.6) (2021-02-16)

#### 버그 수정

* `removeRepeatableByKey`에서 다음 작업 제거, [#165](https://github.com/taskforcesh/bullmq/issues/165) 수정 ([fb3a7c2](https://github.com/taskforcesh/bullmq/commit/fb3a7c2f429d535dd9f038687d7230d61201defc))

### [1.14.5](https://github.com/taskforcesh/bullmq/compare/v1.14.4...v1.14.5) (2021-02-16)

#### 버그 수정

* repeatable 작업에 `jobId` 지원 추가, [#396](https://github.com/taskforcesh/bullmq/issues/396) 수정 ([c2dc669](https://github.com/taskforcesh/bullmq/commit/c2dc6693a4546e547245bc7ec1e71b4841829619))

### [1.14.4](https://github.com/taskforcesh/bullmq/compare/v1.14.3...v1.14.4) (2021-02-08)

#### 버그 수정

* 시작 시 재연결, [#337](https://github.com/taskforcesh/bullmq/issues/337) 수정 ([fb33772](https://github.com/taskforcesh/bullmq/commit/fb3377280b3bda04a15a62d2901bdd78b869e08c))

### [1.14.3](https://github.com/taskforcesh/bullmq/compare/v1.14.2...v1.14.3) (2021-02-07)

#### 버그 수정

* **worker:** 발생 가능한 무한 루프 방지, [#389](https://github.com/taskforcesh/bullmq/issues/389) 수정 ([d05566e](https://github.com/taskforcesh/bullmq/commit/d05566ec0153f31a1257f7338399fdb55c959487))

### [1.14.2](https://github.com/taskforcesh/bullmq/compare/v1.14.1...v1.14.2) (2021-02-02)

#### 버그 수정

* 오류 메시지에 작업 이름과 id를 포함해 작업 타임아웃 알림 개선 ([#387](https://github.com/taskforcesh/bullmq/issues/387)) ([ca886b1](https://github.com/taskforcesh/bullmq/commit/ca886b1f854051aed0888f5b872a64b052b2383e))

### [1.14.1](https://github.com/taskforcesh/bullmq/compare/v1.14.0...v1.14.1) (2021-02-01)

#### 버그 수정

* 작업 완료 큐 이벤트 레이스 컨디션 수정 ([355bca5](https://github.com/taskforcesh/bullmq/commit/355bca5ee128bf4ff37608746f9c6f7cca580eb0))

## [1.14.0](https://github.com/taskforcesh/bullmq/compare/v1.13.0...v1.14.0) (2021-01-06)

#### 기능

* **job:** `extendLock`을 public 메서드로 노출 ([17e8431](https://github.com/taskforcesh/bullmq/commit/17e8431af8bba58612bf9913c63ab5d38afecbb9))

## [1.13.0](https://github.com/taskforcesh/bullmq/compare/v1.12.3...v1.13.0) (2020-12-30)

#### 기능

* 작업 수동 처리 지원 추가, [#327](https://github.com/taskforcesh/bullmq/issues/327) 수정 ([e42bfd2](https://github.com/taskforcesh/bullmq/commit/e42bfd2814fc5136b175470c3085355090cc2e01))

### [1.12.3](https://github.com/taskforcesh/bullmq/compare/v1.12.2...v1.12.3) (2020-12-28)

#### 버그 수정

* "falsy" 데이터 값을 올바르게 처리, [#264](https://github.com/taskforcesh/bullmq/issues/264) 수정 ([becad91](https://github.com/taskforcesh/bullmq/commit/becad91350fd4ac01037e5b0d4a8a93724dd8dbd))
* **worker:** worker blocking connection에 `setname` 설정 ([645b633](https://github.com/taskforcesh/bullmq/commit/645b6338f5883b0c21ae78007777d86b45422615))

### [1.12.2](https://github.com/taskforcesh/bullmq/compare/v1.12.1...v1.12.2) (2020-12-23)

#### 버그 수정

* Repeat에서 발생한 오류를 catch ([#348](https://github.com/taskforcesh/bullmq/issues/348)) ([09a1a98](https://github.com/taskforcesh/bullmq/commit/09a1a98fc42dc1a9ae98bfb29c0cca3fac02013f))

### [1.12.1](https://github.com/taskforcesh/bullmq/compare/v1.12.0...v1.12.1) (2020-12-21)

#### 버그 수정

* "falsy" 데이터 값을 올바르게 처리, [#264](https://github.com/taskforcesh/bullmq/issues/264) 수정 ([cf1dbaf](https://github.com/taskforcesh/bullmq/commit/cf1dbaf7e60d74fc8443a5f8a537455f28a8dba3))

## [1.12.0](https://github.com/taskforcesh/bullmq/compare/v1.11.2...v1.12.0) (2020-12-16)

#### 기능

* 큐가 일시 중지되었는지 여부를 가져오는 기능 추가 ([e98b7d8](https://github.com/taskforcesh/bullmq/commit/e98b7d8973df830cc29e0afc5d86e82c9a7ce76f))

### [1.11.2](https://github.com/taskforcesh/bullmq/compare/v1.11.1...v1.11.2) (2020-12-15)

#### 버그 수정

* 일시 중지 시 작업을 올바른 "list"로 이동 ([d3df615](https://github.com/taskforcesh/bullmq/commit/d3df615d37b1114c02eacb45f23643ee2f05374d))

### [1.11.1](https://github.com/taskforcesh/bullmq/compare/v1.11.0...v1.11.1) (2020-12-15)

#### 버그 수정

* GCP memorystore v5를 지원하도록 clientCommandMessageReg 추가 ([8408dda](https://github.com/taskforcesh/bullmq/commit/8408dda9fa64fc0b968e88fb2726e0a30f717ed7))

## [1.11.0](https://github.com/taskforcesh/bullmq/compare/v1.10.0...v1.11.0) (2020-11-24)

#### 버그 수정

* processor에 generic type 추가 ([d4f6501](https://github.com/taskforcesh/bullmq/commit/d4f650120804bd6161f0eeda5162ad5a96811a05))

#### 기능

* queue, worker, processor에 name 및 return type 추가 ([4879715](https://github.com/taskforcesh/bullmq/commit/4879715ec7c917f11e3a0ac3c5f5126029340ed3))

## [1.10.0](https://github.com/taskforcesh/bullmq/compare/v1.9.0...v1.10.0) (2020-10-20)

#### 버그 수정

* **job:** promise를 resolve하기 전에 리스너 제거 ([563ce92](https://github.com/taskforcesh/bullmq/commit/563ce9218f5dd81f2bc836f9e8ccdedc549f09dd))
* **worker:** handleFailed가 실패해도 처리를 계속함. [#286](https://github.com/taskforcesh/bullmq/issues/286) 수정 ([4ef1cbc](https://github.com/taskforcesh/bullmq/commit/4ef1cbc13d53897b57ae3d271afbaa1b213824aa))
* **worker:** Promise.race에서 발생하는 메모리 누수 수정 ([#282](https://github.com/taskforcesh/bullmq/issues/282)) ([a78ab2b](https://github.com/taskforcesh/bullmq/commit/a78ab2b362e54f897eec6c8b16f16ecccf7875c2))
* **worker:** worker blocking connection에 setname 설정 ([#291](https://github.com/taskforcesh/bullmq/issues/291)) ([50a87fc](https://github.com/taskforcesh/bullmq/commit/50a87fcb1dab976a6a0273d2b0cc4b31b63c015f))
* child pool에서 async for loop 제거, [#229](https://github.com/taskforcesh/bullmq/issues/229) 수정 ([d77505e](https://github.com/taskforcesh/bullmq/commit/d77505e989cd1395465c5222613555f79e4d9720))

#### 기능

* **sandbox:** child worker를 정상적으로 종료 ([#243](https://github.com/taskforcesh/bullmq/issues/243)) ([4262837](https://github.com/taskforcesh/bullmq/commit/4262837bc67e007fe44606670dce48ee7fec65cd))

## [1.9.0](https://github.com/taskforcesh/bullmq/compare/v1.8.14...v1.9.0) (2020-07-19)

#### 기능

* grouped rate limiting 추가 ([3a958dd](https://github.com/taskforcesh/bullmq/commit/3a958dd30d09a049b0d761679d3b8d92709e815e))

### [1.8.14](https://github.com/taskforcesh/bullmq/compare/v1.8.13...v1.8.14) (2020-07-03)

#### 버그 수정

* **typescript:** typings 수정, ioredis 의존성 업그레이드 ([#220](https://github.com/taskforcesh/bullmq/issues/220)) ([7059f20](https://github.com/taskforcesh/bullmq/commit/7059f2089553a206ab3937f7fd0d0b9de96aa7b7))
* **worker:** close 호출 시 this.closing 반환 ([b68c845](https://github.com/taskforcesh/bullmq/commit/b68c845c77de6b2973ec31d2f22958ab60ad87aa))

### [1.8.13](https://github.com/taskforcesh/bullmq/compare/v1.8.12...v1.8.13) (2020-06-05)

#### 버그 수정

* **redis-connection:** 재사용된 redis client에 대해 load command 실행 ([fab9bba](https://github.com/taskforcesh/bullmq/commit/fab9bba4caee8fd44523febb3bde588b151e8514))

### [1.8.12](https://github.com/taskforcesh/bullmq/compare/v1.8.11...v1.8.12) (2020-06-04)

#### 버그 수정

* 사용되지 않는 options 제거 ([23aadc3](https://github.com/taskforcesh/bullmq/commit/23aadc300b947693f4afb22296d236a924bd11ca))

### [1.8.11](https://github.com/taskforcesh/bullmq/compare/v1.8.10...v1.8.11) (2020-05-29)

#### 버그 수정

* **scheduler:** 4096으로의 불필요한 나눗셈 제거 ([4d25e95](https://github.com/taskforcesh/bullmq/commit/4d25e95f9522388bd85e932e04b6668e3da57686))

### [1.8.10](https://github.com/taskforcesh/bullmq/compare/v1.8.9...v1.8.10) (2020-05-28)

#### 버그 수정

* **scheduler:** update set에서 timestamp를 4096으로 나누도록 수정, [#168](https://github.com/taskforcesh/bullmq/issues/168) 수정 ([0c5db83](https://github.com/taskforcesh/bullmq/commit/0c5db8391bb8994bee19f25a33efb9dfee792d7b))

### [1.8.9](https://github.com/taskforcesh/bullmq/compare/v1.8.8...v1.8.9) (2020-05-25)

#### 버그 수정

* **scheduler:** next timestamp를 4096으로 나눔 ([#204](https://github.com/taskforcesh/bullmq/issues/204)) ([9562d74](https://github.com/taskforcesh/bullmq/commit/9562d74625e20b7b6de8750339c85345ba027357))

### [1.8.8](https://github.com/taskforcesh/bullmq/compare/v1.8.7...v1.8.8) (2020-05-25)

#### 버그 수정

* **queue-base:** error event가 전달됨 ([ad14e77](https://github.com/taskforcesh/bullmq/commit/ad14e777171c0c44b7e50752d9847dec23f46158))
* **redis-connection:** error event가 전달됨 ([a15b1a1](https://github.com/taskforcesh/bullmq/commit/a15b1a1824c6863ecf3e5132e22924fc3ff161f6))
* **worker:** error event가 전달됨 ([d7f0374](https://github.com/taskforcesh/bullmq/commit/d7f03749ce300e917399a435a3f426e66145dd8c))

### [1.8.7](https://github.com/taskforcesh/bullmq/compare/v1.8.6...v1.8.7) (2020-04-10)

#### 버그 수정

* **worker:** global child pool을 사용하지 않음, [#172](https://github.com/taskforcesh/bullmq/issues/172) 수정 ([bc65f26](https://github.com/taskforcesh/bullmq/commit/bc65f26dd47c59d0a7277ac947140405557be9a5))

### [1.8.6](https://github.com/taskforcesh/bullmq/compare/v1.8.5...v1.8.6) (2020-04-10)

#### 버그 수정

* **workers:** super.close()를 호출하지 않음 ([ebd2ae1](https://github.com/taskforcesh/bullmq/commit/ebd2ae1a5613d71643c5a7ba3f685d77585de68e))
* 모든 close 호출에서 closing이 반환되도록 보장 ([88c5948](https://github.com/taskforcesh/bullmq/commit/88c5948d33a9a7b7a4f4f64f3183727b87d80207))
* **scheduler:** 중복 연결 문제 수정 [#174](https://github.com/taskforcesh/bullmq/issues/174) ([011b8ac](https://github.com/taskforcesh/bullmq/commit/011b8acfdec54737d94a9fead2423e060e3364db))
* **worker:** close 호출 시 this.closing 반환 ([06d3d4f](https://github.com/taskforcesh/bullmq/commit/06d3d4f476444a2d2af8538d60cb2561a1915868))

### [1.8.5](https://github.com/taskforcesh/bullmq/compare/v1.8.4...v1.8.5) (2020-04-05)

#### 버그 수정

* deprecated되었고 사용되지 않는 node-uuid 제거 ([c810579](https://github.com/taskforcesh/bullmq/commit/c810579029d33ef47d5a7563e63126a69c62fd87))

### [1.8.4](https://github.com/taskforcesh/bullmq/compare/v1.8.3...v1.8.4) (2020-03-17)

#### 버그 수정

* **job:** nullable/optional 속성 추가 ([cef134f](https://github.com/taskforcesh/bullmq/commit/cef134f7c4d87e1b80ba42a5e06c3877956ff4cc))

### [1.8.3](https://github.com/taskforcesh/bullmq/compare/v1.8.2...v1.8.3) (2020-03-13)

#### 버그 수정

* **sandbox:** child process가 종료되면 pool에서 제거. ([8fb0fb5](https://github.com/taskforcesh/bullmq/commit/8fb0fb569a0236b37d3bae06bf58a2a1da3221c6))

### [1.8.2](https://github.com/taskforcesh/bullmq/compare/v1.8.1...v1.8.2) (2020-03-03)

#### 버그 수정

* JSON 데이터 역직렬화 시 Job timestamp 복원 ([#138](https://github.com/taskforcesh/bullmq/issues/138)) ([#152](https://github.com/taskforcesh/bullmq/issues/152)) ([c171bd4](https://github.com/taskforcesh/bullmq/commit/c171bd47f7b75378e75307a1decdc0f630ac1cd6))

### [1.8.1](https://github.com/taskforcesh/bullmq/compare/v1.8.0...v1.8.1) (2020-03-02)

#### 버그 수정

* esModuleInterop이 비활성화되어도 동작하도록 imports 수정 ([#132](https://github.com/taskforcesh/bullmq/issues/132)) ([01681f2](https://github.com/taskforcesh/bullmq/commit/01681f282bafac2df2c602edb51d6bde3483896c))

## [1.8.0](https://github.com/taskforcesh/bullmq/compare/v1.7.0...v1.8.0) (2020-03-02)

#### 버그 수정

* queue add 및 addBulk 시그니처 정리 ([#127](https://github.com/taskforcesh/bullmq/issues/127)) ([48e221b](https://github.com/taskforcesh/bullmq/commit/48e221b53909079a4def9c48c1b69cebabd0ed74))
* child process와 inspect 사용 시 exit code 12 문제 수정 ([#137](https://github.com/taskforcesh/bullmq/issues/137)) ([43ebc67](https://github.com/taskforcesh/bullmq/commit/43ebc67cec3e8f283f9a555b4466cf918226687b))

#### 기능

* **types:** sandboxed job processor 타입 추가 ([#114](https://github.com/taskforcesh/bullmq/issues/114)) ([a50a88c](https://github.com/taskforcesh/bullmq/commit/a50a88cd1658fa9d568235283a4c23a74eb8ed2a))

## [1.7.0](https://github.com/taskforcesh/bullmq/compare/v1.6.8...v1.7.0) (2020-03-02)

#### 기능

* [#140](https://github.com/taskforcesh/bullmq/issues/140)을 위해 queue name을 공개적으로 읽을 수 있도록 변경 ([f2bba2e](https://github.com/taskforcesh/bullmq/commit/f2bba2efd9d85986b01bb35c847a232b5c42ae57))

### [1.6.8](https://github.com/taskforcesh/bullmq/compare/v1.6.7...v1.6.8) (2020-02-22)

#### 버그 수정

* QueueGetters.getJob 및 Job.fromId가 null도 반환하도록 수정 ([65183fc](https://github.com/taskforcesh/bullmq/commit/65183fcf542d0227ec1d4d6637b46b5381331787))
* QueueGetters.getJob 및 Job.fromId가 undefined를 반환하도록 수정 ([ede352b](https://github.com/taskforcesh/bullmq/commit/ede352be75ffe05bf633516db9eda88467c562bf))

### [1.6.7](https://github.com/taskforcesh/bullmq/compare/v1.6.6...v1.6.7) (2020-01-16)

#### 버그 수정

* worker가 이미 lock을 잃은 경우 job을 실패 처리하지 않음 ([23c0bf7](https://github.com/taskforcesh/bullmq/commit/23c0bf70eab6d166b0483336f103323d1bf2ca64))

### [1.6.6](https://github.com/taskforcesh/bullmq/compare/v1.6.5...v1.6.6) (2020-01-05)

#### 버그 수정

* 중복된 active entry 제거 ([1d2cca3](https://github.com/taskforcesh/bullmq/commit/1d2cca38ee61289adcee4899a91f7dcbc93a7c05))

### [1.6.5](https://github.com/taskforcesh/bullmq/compare/v1.6.4...v1.6.5) (2020-01-05)

#### 버그 수정

* 테스트에서 flushdb/flushall 제거 ([550c67b](https://github.com/taskforcesh/bullmq/commit/550c67b25de5f6d800e5e317398044cd16b85924))

### [1.6.4](https://github.com/taskforcesh/bullmq/compare/v1.6.3...v1.6.4) (2020-01-05)

#### 버그 수정

* set에서 job 정리 시 로그 삭제 ([b11c6c7](https://github.com/taskforcesh/bullmq/commit/b11c6c7c9f4f1c49eac93b98fdc93ac8f861c8b2))

### [1.6.3](https://github.com/taskforcesh/bullmq/compare/v1.6.2...v1.6.3) (2020-01-01)

#### 버그 수정

* tslib 의존성 추가, [#65](https://github.com/taskforcesh/bullmq/issues/65) 수정 ([7ad7995](https://github.com/taskforcesh/bullmq/commit/7ad799544a9c30b30aa96df8864119159c9a1185))

### [1.6.2](https://github.com/taskforcesh/bullmq/compare/v1.6.1...v1.6.2) (2019-12-16)

#### 버그 수정

* QueueEvents 기본 lastEventId를 $로 변경 ([3c5b01d](https://github.com/taskforcesh/bullmq/commit/3c5b01d16ee1442f5802a0fe4e7675c14f7a7f1f))
* 테스트 이벤트를 추가하기 전에 QE가 준비되었는지 보장 ([fd190f4](https://github.com/taskforcesh/bullmq/commit/fd190f4be792b03273481c8aaf73be5ca42663d1))
* .on 및 .once 동작을 명시적으로 테스트 ([ea11087](https://github.com/taskforcesh/bullmq/commit/ea11087b292d9325105707b53f92ac61c334a147))

### [1.6.1](https://github.com/taskforcesh/bullmq/compare/v1.6.0...v1.6.1) (2019-12-16)

#### 버그 수정

* 기존 redis instance 확인 ([dd466b3](https://github.com/taskforcesh/bullmq/commit/dd466b332b03b430108126531d59ff9e66ce9521))

## [1.6.0](https://github.com/taskforcesh/bullmq/compare/v1.5.0...v1.6.0) (2019-12-12)

#### 기능

* job data와 return value에 generic type 추가 ([87c0531](https://github.com/taskforcesh/bullmq/commit/87c0531efc2716db37f8a0886848cdb786709554))

## [1.5.0](https://github.com/taskforcesh/bullmq/compare/v1.4.3...v1.5.0) (2019-11-22)

#### 기능

* delay 의존성 제거 ([97e1a30](https://github.com/taskforcesh/bullmq/commit/97e1a3015d853e615ddd623af07f12a194ccab2c))
* Bluebird.delay 의존성 제거 [#67](https://github.com/taskforcesh/bullmq/issues/67) ([bedbaf2](https://github.com/taskforcesh/bullmq/commit/bedbaf25af6479e387cd7548e246dca7c72fc140))

### [1.4.3](https://github.com/taskforcesh/bullmq/compare/v1.4.2...v1.4.3) (2019-11-21)

#### 버그 수정

* moveToFinished에서 opts.maxLenEvents에 기본값을 사용하도록 확인 ([d1118aa](https://github.com/taskforcesh/bullmq/commit/d1118aab77f755b4a65e3dd8ea2e195baf3d2602))

### [1.4.2](https://github.com/taskforcesh/bullmq/compare/v1.4.1...v1.4.2) (2019-11-21)

#### 버그 수정

* Job<->Queue 순환 json 오류 방지 ([5752727](https://github.com/taskforcesh/bullmq/commit/5752727a6294e1b8d35f6a49e4953375510e10e6))

* `.toJSON` serializer 인터페이스 사용 회피 [#70](https://github.com/taskforcesh/bullmq/issues/70) ([5941b82](https://github.com/taskforcesh/bullmq/commit/5941b82b646e46d53970197a404e5ea54f09d008))

### [1.4.1](https://github.com/taskforcesh/bullmq/compare/v1.4.0...v1.4.1) (2019-11-08)

#### 버그 수정

* 기본 job 설정 [#58](https://github.com/taskforcesh/bullmq/issues/58) ([667fc6e](https://github.com/taskforcesh/bullmq/commit/667fc6e00ae4d6da639d285a104fb67e01c95bbd))

## [1.4.0](https://github.com/taskforcesh/bullmq/compare/v1.3.0...v1.4.0) (2019-11-06)

#### 기능

* `job.progress()`가 sandboxed processor에 대해 마지막 진행 상태를 반환 ([5c4b146](https://github.com/taskforcesh/bullmq/commit/5c4b146ca8e42c8a29f9db87326a17deac30e10e))

## [1.3.0](https://github.com/taskforcesh/bullmq/compare/v1.2.0...v1.3.0) (2019-11-05)

#### 기능

* job이 활성 상태인 동안 테스트 worker가 job lock을 연장 ([577efdf](https://github.com/taskforcesh/bullmq/commit/577efdfb1d2d3140be78dee3bd658b5ce969b16d))

## [1.2.0](https://github.com/taskforcesh/bullmq/compare/v1.1.0...v1.2.0) (2019-11-03)

#### 버그 수정

* 성공 후에만 coveralls 실행 ([bd51893](https://github.com/taskforcesh/bullmq/commit/bd51893c35793657b65246a2f5a06469488c8a06))

#### 기능

* code coverage와 coveralls 추가 ([298cfc4](https://github.com/taskforcesh/bullmq/commit/298cfc48e35e648e6a22ac0d1633ac16c7b6e3de))
* coverage에 필요한 누락 deps 추가 ([6f3ab8d](https://github.com/taskforcesh/bullmq/commit/6f3ab8d78ba8503a76447f0db5abf0c1c4f8e185))
* coverage에서 commitlint 파일 무시 ([f874441](https://github.com/taskforcesh/bullmq/commit/f8744411a1b20b95e568502be15ec50cf8520926))
* 모든 테스트 통과 후 coverage를 한 번만 업로드 ([a7f73ec](https://github.com/taskforcesh/bullmq/commit/a7f73ecc2f51544f1d810de046ba073cb7aa5663))

## [1.1.0](https://github.com/taskforcesh/bullmq/compare/v1.0.1...v1.1.0) (2019-11-01)

#### 버그 수정

* 빌드 실패 ([bb21d53](https://github.com/taskforcesh/bullmq/commit/bb21d53b199885dcc97e7fe20f60caf65e55e782))
* 실패하는 테스트 수정 ([824eb6b](https://github.com/taskforcesh/bullmq/commit/824eb6bfb2b750b823d057c894797ccb336245d8))

#### 기능

* job locking 메커니즘의 초기 버전 ([1d4fa38](https://github.com/taskforcesh/bullmq/commit/1d4fa383e39f4f5dcb69a71a1359dd5dea75544c))

### [1.0.1](https://github.com/taskforcesh/bullmq/compare/v1.0.0...v1.0.1) (2019-10-27)

#### 버그 수정

* 실패 시 job stacktrace 저장 ([85dfe52](https://github.com/taskforcesh/bullmq/commit/85dfe525079a5f89c1901dbf35c7ddc6663afc24))
* `stackTraceLimit` 로직 단순화 ([296bd89](https://github.com/taskforcesh/bullmq/commit/296bd89514d430a499afee934dcae2aec41cffa2))

## 1.0.0 (2019-10-20)

#### 버그 수정

* 테스트 실행 전에 컴파일 단계 추가 ([64abc13](https://github.com/taskforcesh/bullmq/commit/64abc13681f8735fb3ee5add5b271bb4da618047))
* worker 수정에 추가 client 반영 [#34](https://github.com/taskforcesh/bullmq/issues/34) ([90bd891](https://github.com/taskforcesh/bullmq/commit/90bd891c7514f5e9e397d7aad15069ee55bebacd))
* 누락된 의존성 추가 ([b92e330](https://github.com/taskforcesh/bullmq/commit/b92e330aad35ae54f43376f92ad1b41209012b76))
* pause에서 재개한 뒤 closing 여부 확인 ([7b2cef3](https://github.com/taskforcesh/bullmq/commit/7b2cef3677e2b3af0370e0023aec4b971ad313fe))
* 기본 opts ([333c73b](https://github.com/taskforcesh/bullmq/commit/333c73b5819a263ae92bdb54f0406c19db5cb64f))
* `blockTime`이 0이면 block하지 않음 ([13b2df2](https://github.com/taskforcesh/bullmq/commit/13b2df20cf045c069b8b581751e117722681dcd4))
* closing 중이면 exec하지 않음 ([b1d1c08](https://github.com/taskforcesh/bullmq/commit/b1d1c08a2948088eeb3dd65de78085329bac671b))
* `maxEvents`가 undefined이면 trim하지 않음 ([7edd8f4](https://github.com/taskforcesh/bullmq/commit/7edd8f47b392c8b3a7369196befdafa4b29421d1))
* job 추가 시 wait event emit ([39cba31](https://github.com/taskforcesh/bullmq/commit/39cba31a30b7ef762a8d55d4bc34efec636207bf))
* 일부 job 테스트 수정 ([e66b97b](https://github.com/taskforcesh/bullmq/commit/e66b97be4577d5ab373fff0f3f45d73de7842a37))
* 컴파일 오류 수정 ([3cf2617](https://github.com/taskforcesh/bullmq/commit/3cf261703292d263d1e2017ae30eb490121dab4e))
* 추가 테스트 수정 ([6a07b35](https://github.com/taskforcesh/bullmq/commit/6a07b3518f856e8f7158be032110c925ed5c924f))
* progress 스크립트 수정 ([4228e27](https://github.com/taskforcesh/bullmq/commit/4228e2768c0cf404e09642ebb4053147d0badb56))
* retry 기능 수정 ([ec41ea4](https://github.com/taskforcesh/bullmq/commit/ec41ea4e0bd88b10b1ba434ef5ceb0952bb59f7b))
* 여러 floating promise 수정 ([590a4a9](https://github.com/taskforcesh/bullmq/commit/590a4a925167a7c7d6c0d9764bbb5ab69235beb7))
* reprocess lua 스크립트 수정 ([b78296f](https://github.com/taskforcesh/bullmq/commit/b78296f33517b8c5d79b300fef920edd03149d2f))
* 동시성 메커니즘 개선 ([a3f6148](https://github.com/taskforcesh/bullmq/commit/a3f61489e3c9891f42749ff85bd41064943c62dc))
* queue events의 연결 해제 개선 ([56b53a1](https://github.com/taskforcesh/bullmq/commit/56b53a1aca1e527b50f04d906653060fe8ca644e))
* 생성자에서 events consumption 초기화 ([dbb66cd](https://github.com/taskforcesh/bullmq/commit/dbb66cda9722d44eca806fa6ad1cabdaabac846a))
* ioredis typings을 일반 의존성으로 변경 ([fb80b90](https://github.com/taskforcesh/bullmq/commit/fb80b90b12931a12a1a93c5e204dbf90eed4f48f))
* 사소한 수정 ([7791cda](https://github.com/taskforcesh/bullmq/commit/7791cdac2bfb6a7fbbab9c95c5d89b1eae226a4c))
* events에서 progres와 반환값 파싱 ([9e43d0e](https://github.com/taskforcesh/bullmq/commit/9e43d0e30ab90a290942418718cde1f5bfbdcf56))
* progress용 event를 올바르게 emit ([3f70175](https://github.com/taskforcesh/bullmq/commit/3f701750b1c957027825ee90b58141cd2556694f))
* drain 지연을 5초로 줄임 ([c6cfe7c](https://github.com/taskforcesh/bullmq/commit/c6cfe7c0b50cabe5e5eb31f4b631a8b1d3706611))
* redis-connection의 버그 있는 `close()` 제거 (실패 테스트 5개 수정) ([64c2ede](https://github.com/taskforcesh/bullmq/commit/64c2edec5e738f43676d0f4ca61bdea8609203fc))
* 사용하지 않는 의존성 제거 ([34293c8](https://github.com/taskforcesh/bullmq/commit/34293c84bb0ed54f18d70c86821c3ac627d376a5))
* init을 `waitUntilReady`로 대체 ([4336161](https://github.com/taskforcesh/bullmq/commit/43361610de5b1a993a1c65f3f21ac745b8face21))
* redis client 초기화 방식 재작업 ([c17d4be](https://github.com/taskforcesh/bullmq/commit/c17d4be5a2ecdda3efcdc6b9d7aecdfaccd06d83))
* 라이브러리가 다른 ts 프로젝트에서도 동작하도록 여러 수정 적용 ([3cac1b0](https://github.com/taskforcesh/bullmq/commit/3cac1b0715613d9df51cb1ed6fe0859bcfbb8e9b))
* 코드 대신 에러 메시지를 throw ([9267541](https://github.com/taskforcesh/bullmq/commit/92675413f1c3b9564574dc264ffcab0d6089e70e))
* 병합 후 테스트 업데이트 ([51f75a4](https://github.com/taskforcesh/bullmq/commit/51f75a4929e7ae2704e42fa9035e335fe60d8dc0))
* job 조회 시도 전에 ready 상태까지 대기 ([f3b768f](https://github.com/taskforcesh/bullmq/commit/f3b768f251ddafa207466af552376065b35bec8f))
* **connections:** 연결 재사용 ([1e808d2](https://github.com/taskforcesh/bullmq/commit/1e808d24018a29f6611f4fccd2f5754de0fa3e39))
* `waitUntilFinished` 개선 ([18d4afe](https://github.com/taskforcesh/bullmq/commit/18d4afef08f04d19cb8d931e02fff8f962d07ee7))

#### 기능

* cleaned event 추가 ([c544775](https://github.com/taskforcesh/bullmq/commit/c544775803626b5f03cf6f7c3cf18ed1d92debab))
* empty 메서드 추가 ([4376112](https://github.com/taskforcesh/bullmq/commit/4376112369d869c0a5c7ab4a543cfc50200e1414))
* retry errors 추가 ([f6a7990](https://github.com/taskforcesh/bullmq/commit/f6a7990fb74585985729c5d95e2238acde6cf74a))
* typedocs 생성 스크립트 추가 ([d0a8cb3](https://github.com/taskforcesh/bullmq/commit/d0a8cb32ef9090652017f8fbf2ca42f0960687f7))
* compat class용 새 테스트 추가 및 기타 사소한 수정 ([bc0f653](https://github.com/taskforcesh/bullmq/commit/bc0f653ecf7aedd5a46eee6f912ecd6849395dca))
* job 대량 추가 지원 ([b62bddc](https://github.com/taskforcesh/bullmq/commit/b62bddc054b266a809b4b1646558a095a276d6d1))
* queue client에 `trimEvents` 메서드 추가 ([b7da7c4](https://github.com/taskforcesh/bullmq/commit/b7da7c4de2de81282aa41f8b7624b9030edf7d15))
* events 자동 trim ([279bbba](https://github.com/taskforcesh/bullmq/commit/279bbbab7e96ad8676ed3bd68663cb199067ea67))
* global stalled event emit 수정 [#10](https://github.com/taskforcesh/bullmq/issues/10) ([241f229](https://github.com/taskforcesh/bullmq/commit/241f229761691b9ac17124da005f91594a78273d))
* Job3를 제거하고 bullmq Job 클래스로 대체 ([7590cea](https://github.com/taskforcesh/bullmq/commit/7590ceae7abe32a8824e4a265f95fef2f9a6665f))
* redis connection의 close 구현 수정 [#8](https://github.com/taskforcesh/bullmq/issues/8) ([6de8b48](https://github.com/taskforcesh/bullmq/commit/6de8b48c9612ea39bb28db5f4130cb2a2bb5ee90))
* backoffs의 delay를 선택 사항으로 변경 ([30d59e5](https://github.com/taskforcesh/bullmq/commit/30d59e519794780a8198222d0bbd88779c623275))
* 비동기 초기화를 생성자로 이동 ([3fbacd0](https://github.com/taskforcesh/bullmq/commit/3fbacd088bc3bfbd61ed8ff173e4401193ce48ec))
* bull 3.x의 많은 기능 포팅 ([ec9f3d2](https://github.com/taskforcesh/bullmq/commit/ec9f3d266c1aca0c27cb600f056d813c81259b4c))
* bull 3.x에서 더 많은 기능 포팅 ([75bd261](https://github.com/taskforcesh/bullmq/commit/75bd26158678ee45a14e04fd7c3a1f96219979a2))
* bull 3의 테스트 및 기능 포팅 ([1b6b192](https://github.com/taskforcesh/bullmq/commit/1b6b1927c7e8e6b6f1bf0bbd6c74eb59cc17deb6))
* **workers:** 비동기 backoffs 지원 ([c555837](https://github.com/taskforcesh/bullmq/commit/c55583701e5bdd4e6436a61c833e506bc05749de))
* compat class에서 bull3 config 형식 지원 제거 ([d909486](https://github.com/taskforcesh/bullmq/commit/d9094868e34c2af21f810aaef4542951a509ccf8))
* global:progress event 지원 ([60f4d85](https://github.com/taskforcesh/bullmq/commit/60f4d85d332b3be4a80db7aa179f3a9ceeb1d6f8))
* event stream에 trim 옵션 추가 [#21](https://github.com/taskforcesh/bullmq/issues/21) 및 [#17](https://github.com/taskforcesh/bullmq/issues/17) 수정 ([7eae653](https://github.com/taskforcesh/bullmq/commit/7eae65340820043101fadf1f87802f506020d553))

### 4.0.0-beta.2

#### 수정됨

* 인간을 제거했습니다. 동물들과는 잘 지내지 못했거든요.

#### 변경됨

* 이제 모든 동물이 매우 귀여워졌습니다.

### 4.0.0-beta.1

#### 추가됨

* 세상에 동물을 도입했습니다. 꽤 멋진 추가가 될 거라고 믿습니다.

### 4.0.0-beta.0

